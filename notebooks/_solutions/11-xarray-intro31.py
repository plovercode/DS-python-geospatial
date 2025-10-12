# Classify the array into 3 bins
b4_data_classified = xr.apply_ufunc(np.digitize, b4_data, [0.05, 0.1])