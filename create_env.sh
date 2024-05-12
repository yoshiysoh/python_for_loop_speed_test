#!/bin/sh

source ~/miniconda3/etc/profile.d/conda.sh

for env_file in environments/python*.yml; do
	conda env create -f "$env_file"
done
