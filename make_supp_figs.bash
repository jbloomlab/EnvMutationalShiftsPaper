#!/bin/bash
jupyter nbconvert analysis_code/analysis_notebook.ipynb && mv analysis_code/analysis_notebook.html paper/figures/

zip -r --exclude=analysis_code/run.sbatch --exclude=analysis_code/results/FASTQ_files/* --exclude=analysis_code/.* analysis_code.zip analysis_code && mv analysis_code.zip paper/figures/
