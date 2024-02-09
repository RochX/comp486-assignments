#!/bin/sh
tar -xf ../assignment3/rps-data.tgz

rm rps-training-data.csv
rm rps-test-data.csv

python3 images_to_csv.py training
python3 images_to_csv.py test