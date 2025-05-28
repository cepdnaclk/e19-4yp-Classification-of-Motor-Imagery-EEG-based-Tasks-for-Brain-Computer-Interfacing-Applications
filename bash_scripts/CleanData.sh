#!/bin/bash
TMP_DIR="./rawdata"

# Continuously monitor and delete files that don't contain the word "twist"
while true; do
    find "$TMP_DIR" -type f ! -name "*twist*" -exec rm -f {} \;
    sleep 5  # Sleep for 5 seconds before checking again (adjust as needed)
done

