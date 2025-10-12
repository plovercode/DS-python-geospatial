# Calculate the min and max for each channel
h_min = herstappe_data.min(dim=["x", "y"])
h_max = herstappe_data.max(dim=["x", "y"])