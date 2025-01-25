import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend

def calc_mean_erp(trial_points_path, ecog_data_path):
    """
    Computes the average Event Related Potential (ERP) for finger movements.
    
    Parameters:
    trial_points_path (str): Path to the CSV file containing movement start points, peak points, and finger number.
    ecog_data_path (str): Path to the CSV file containing ECOG brain signal time series.
    
    Returns:
    np.ndarray: A matrix of size 5x1201 where each row corresponds to the averaged ERP of a specific finger (1-5).
    """
    # Load trial data (ensuring integers for proper indexing)
    trial_data = pd.read_csv(trial_points_path, dtype=int)
    
    # Load ECOG data (only one column, so squeeze it into a Series for easy access)
    ecog_signal = pd.read_csv(ecog_data_path, header=None).squeeze("columns")
    
    # Initialize matrix to store ERP means for each finger (5 fingers, 1201 time points)
    erp_matrix = np.zeros((5, 1201))
    
    # Iterate over each finger (1 to 5)
    for finger in range(1, 6):
        # Extract only the trials corresponding to the current finger
        start_points = trial_data[trial_data.iloc[:, 2] == finger].iloc[:, 0]
        
        # List to collect ERP segments for averaging
        erp_segments = []
        
        # Loop through all start points of this finger's movements
        for start_index in start_points:
            # Ensure that the extracted segment is within valid data range
            if start_index - 200 >= 0 and start_index + 1000 < len(ecog_signal):
                # Extract the excact time points surrounding the movement (-200ms to +1000ms)
                segment = ecog_signal[start_index - 200 : start_index + 1001].values
                erp_segments.append(segment)
        
        # If at least one segment was found, compute the mean ERP for this finger
        if erp_segments:
            erp_matrix[finger - 1, :] = np.mean(erp_segments, axis=0)
    
    # Define time axis to properly align with the extracted time window (-200ms to +1000ms)
    time_axis = np.arange(-200, 1001)
    
    # Plot the averaged ERP for each finger and save as a picture
    plt.figure(figsize=(10, 6))
    for i in range(5):
        plt.plot(time_axis, erp_matrix[i], label=f'Finger {i+1}')
    plt.xlabel("Time (ms)")
    plt.ylabel("ECOG Signal Amplitude (μV)")
    plt.title("Average Event Related Potential (ERP) for each finger")
    plt.legend()
    plt.savefig("ERG graph")
    
    return erp_matrix

# File paths for input data
trial_points_path = rf"data\events_file_ordered.csv"
ecog_data_path = rf"data\brain_data_channel_one.csv"

# Run the function and store the result
fingers_erp_mean = calc_mean_erp(trial_points_path, ecog_data_path)