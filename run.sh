#!/bin/sh
# remove the file if it exists
rm -f for_loop_result.txt
touch for_loop_result.txt

source ~/miniconda3/etc/profile.d/conda.sh

python_versions=("python3.5" "python3.6" "python3.7" "python3.8" "python3.9" "python3.10" "python3.11" "python3.12")

for version in "${python_versions[@]}"
do
    conda activate "$version"
    python for_loop.py
    conda deactivate
done