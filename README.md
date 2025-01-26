# mini_project_2 - ERP Analysis for Finger Movements
second mini-project for "Advanced Programming in Python" course

## Project Overview
This project analyzes brain activity during finger movements using ERP (Event-Related Potentials). The goal is to extract and visualize neural responses recorded via ECOG electrodes.

## Data
- **Trial Points File**: Contains movement start points, peaks, and finger numbers.
- **ECOG Data File**: Time-series brain signals recorded during movements.

## Functionality
The function `calc_mean_erp`:
- Extracts 1201 time points around each movement (-200ms to +1000ms).
- Computes the average ERP for each finger.
- Plots the ERP curves.

## Repository Contents
- `main.py` – Main script, contains the calc_mean_erp function
- `README.md` – Project description.
- `data` – All the provided data files.
- `ERG graph.png` - The graph obtained from running the function
