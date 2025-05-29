#!/bin/bash

URL="https://s3.ap-northeast-1.wasabisys.com/gigadb-datasets/live/pub/10.5524/100001_101000/100788/RawData.tar.gz"
# Define the rawdata directory (TMP_DIR) where the files will be extracted
TMP_DIR="./rawdata"

# Create the rawdata directory if it doesn't exist
mkdir -p "$TMP_DIR"

# Function to clean up files that don't contain the word "twist"
clean_files() {
    find "$TMP_DIR" -type f ! -name "*twist*" -exec rm -f {} \;
}

# Use wget to download and pipe directly into tar for extraction into rawdata
wget -c "$URL" -O - | tar -xzv -C "$TMP_DIR" --no-same-owner --wildcards --transform 's/^RawData\///' &

# Monitor extraction and clean up files while extracting
inotifywait -m -r -e close_write "$TMP_DIR" | while read path action file; do
    clean_files
done

# Wait for extraction to complete
wait


