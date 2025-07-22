import os
import mne
import numpy as np
from glob import glob
from sklearn.preprocessing import StandardScaler
import gc

#Input and Output Paths
data_dir = "/storage/projects1/e19-4yp-mi-eeg-for-bci/rawdata"
output_dir = "preprocessed_epochs"
os.makedirs(output_dir, exist_ok=True)

#Collect all session .vhdr files
all_vhdr_files = sorted(glob(os.path.join(data_dir, "session*_sub*_twist_MI.vhdr")))

#Filter problematic or missing files
vhdr_paths = [
    f for f in all_vhdr_files
    if 'Move' not in os.path.basename(f)
    and 'session3_sub13' not in os.path.basename(f)
    and 'session1_sub23' not in os.path.basename(f)
    and 'session2_sub7' not in os.path.basename(f)
    and 'session2_sub12' not in os.path.basename(f)
    and 'session2_sub6' not in os.path.basename(f)
]

#Define event codes
wrist_events = {'pronation': 91, 'supination': 101}

for i, vhdr_path in enumerate(vhdr_paths):
    try:
        print(f"\n🔄 Processing: {vhdr_path}")

        raw = mne.io.read_raw_brainvision(vhdr_path, preload=True, verbose='ERROR')

        #Drop non-EEG artifact channels
        raw.drop_channels([ch for ch in raw.ch_names if 'EOG' in ch or 'EMG' in ch])

        #Downsample to 256 Hz
        raw.resample(256)

        #Apply filters
        raw.notch_filter(freqs=60)
        raw.filter(8., 30., fir_design='firwin')

        #ICA on short segment - artifact removal
        ica = mne.preprocessing.ICA(n_components=15, random_state=97, max_iter='auto')
        ica.fit(raw.copy().crop(tmax=60))  # 1 min
        raw = ica.apply(raw)

        #Extract events
        events, event_id = mne.events_from_annotations(raw)

        epochs = mne.Epochs(
            raw, events, event_id=wrist_events,
            tmin=-0.2, tmax=2.0,
            baseline=(None, 0),
            preload=True,
            reject=dict(eeg=150e-6),  # peak-to-peak rejection
            verbose='ERROR'
        )

        if len(epochs) == 0:
            print(f"⚠️ All epochs rejected for {vhdr_path}")
            continue

        #Get data
        X = epochs.get_data()  # shape (n_epochs, n_channels, n_times)
        y = epochs.events[:, -1]
        y = np.array([0 if label == 91 else 1 for label in y])

        #Channel-wise standardization per epoch
        X_scaled = np.zeros_like(X, dtype=np.float32)
        for j in range(X.shape[0]):
            scaler = StandardScaler()
            X_scaled[j] = scaler.fit_transform(X[j].T).T

        #Save as .npz
        filename = os.path.splitext(os.path.basename(vhdr_path))[0]
        save_path = os.path.join(output_dir, f"{filename}.npz")
        np.savez_compressed(save_path, X=X_scaled, y=y)
        print(f"✅ Saved: {save_path} → {X_scaled.shape}")

        #Clear memory
        del raw, events, event_id, epochs, X, y, X_scaled, ica
        gc.collect()

    except Exception as e:
        print(f"❌ Failed processing {vhdr_path}: {e}")
