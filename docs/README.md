---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e19-4yp-Classification-of-Motor-Imagery-EEG-based-Tasks-for-Brain-Computer-Interfacing-Applications
title: Classification of Motor Imagery(MI) EEG-based Tasks for Brain-Computer-Interfacing(BCI) Applications
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Project Title

#### Team

- e19142, Hashini Illangarathne, [email](mailto:e19142@eng.pdn.ac.lk)
- e19249, Sayumi Muthukumarana, [email](mailto:e19249@eng.pdn.ac.lk)
- e19452, Ashan Wimalasiri, [email](mailto:e19452@eng.pdn.ac.lk)

#### Supervisors

- Dr. Ruwan Ranaweera, [email](mailto:ruwan@eng.pdn.ac.lk)
- Prof. Roshan G. Ragel, [email](mailto:roshanr@eng.pdn.ac.lk)
- A/Prof. Sam John, [email](mailto:sam.john@unimelb.edu.au)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)

---

<!--
DELETE THIS SAMPLE before publishing to GitHub Pages !!!
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)
![Sample Image](./images/sample.png)
-->

## Abstract

Brain Computer Interfaces(BCIs) have made a huge impact in neurotechnology by enabling direct communication between the human brain and electronic external systems. Motor Imagery (MI) based BCIs, which utilize electroencephalography(EEG) signals to interpret motor imagery tasks have demonstrated significant potential in assistive technologies and neurorehabilitation. Traditional MI classification approaches typically distinguish between broad movements. However, novel research suggests that targeting single-joint MI EEG classification (Eg:Wrist, Elbow, Knee) can enhance precision, providing more intuitive and natural control for BCI applications. This study focuses on a single-joint, specifically the wrist, based MI task classification. The introduction of a novel model capable of distinguishing distinct wrist movements and investigating model performance across distinct joint movements, is the main aim of this study. Thus, contributing to improved precision in BCI applications.

## Related works

Traditional MI classification research so far focuses on distinguishing between broad movement categories, such as left-hand and right-hand imagery.
- [[Lotte et al.](https://www.researchgate.net/publication/323465869_A_review_of_classification_algorithms_for_EEG-based_brain-computer_interfaces_a_10_year_update)] employed CSP-based feature extraction for limb-level MI tasks but did not address finer, joint-specific movements. 
- [[Fang et al.](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.655599/full)] utilized deep CNNs for hand-movement classification but did not distinguish between different joints like the wrist or elbow.

## Methodology

The primary objective is to classify MI tasks for single joint movements, focusing on the wrist, with high accuracy to enhance the usability of Brain-Computer Interface(BCI) applications in neurorehabilitation and assistive technology.

### EEG Data
EEG signals of 25 healthy subjects performing wrist movements, pronation and supination, are obtained through the publicly available dataset on GigaDB(https://gigadb.org/dataset/100788). 

### Data Preprocessing
Data Preprocessing is required to be carried out in order to develop models based on traditional machine learning. Techniques proposed to be utilized would include,
- 60 Hz notch filter will be applied to raw EEG data to reduce the effect of external electrical noises such as DC noise of power supply and the scan rate of the monitor. 
- Band-pass filter will be applied to remove both low-frequency and high-frequency components that are irrelevant to the Motor Imagery (MI) task.
- Independent Component Analysis(ICA) technique will be applied to remove artifacts such as eye-blinking effects, muscle movement, and other non-neural interferences.

![Preprocessing Techniques](docs/images/Preprocessing.png)

### Feature Extraction
- Common Spatial Patterns(CSP) to maximize variance between different MI tasks.
- Wavelet Transform for multi-resolution analysis. 

![Feature Extraction](docs/images/FeatureExtraction.png)

### Classification Approaches
Traditional Machine Learning Models include,
- Support Vector Machines (SVM)
- Linear Discriminant Analysis (LDA)
- Random Forest (RF)

Deep Learning Models include,
- Recurrent Neural Networks (RNN)
- Transformers

![Classification](docs/images/ClassificationMethods.png)

### Model Evaluation
The model’s performance will be assessed using standard classification metrics,
including accuracy, precision, recall, F1-score, and Matthews Correlation Coefficient
(MCC). Additionally, Area Under the ROC Curve (AUC-ROC) will provide insights
into the model’s discriminative capabilities. Statistical significance tests, such as
paired t-tests, will be conducted to validate performance improvements.

## Experiment Setup and Implementation

The higher overview of steps involved in classifying MI tasks is shown below. 

![Proposed Approach](docs/images/Propossed_Approach.jpg)

## Results and Analysis

Results have not yet been finalized.

## Conclusion

This proposed research approach focuses on classifying wrist Motor Imagery(MI) tasks using EEG signals, specifically pronation and supination movements. The approach consists of preprocessing, feature extraction, model training, and evaluation to enhance classification accuracy. This study
aims to improve MI-based BCI systems by addressing challenges in classifying single-joint movements, contributing to advancements in assistive technologies and neurorehabilitation.

## Publications

This project has not yet been published.

[//]: # "Note: Uncomment each once you uploaded the files to the repository"

<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->

## Links

[//]: # " NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS "

- [Project Repository](https://github.com/cepdnaclk/e19-4yp-Classification-of-Motor-Imagery-EEG-based-Tasks-for-Brain-Computer-Interfacing-Applications)
- [Project Page](https://cepdnaclk.github.io/e19-4yp-Classification-of-Motor-Imagery-EEG-based-Tasks-for-Brain-Computer-Interfacing-Applications/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
