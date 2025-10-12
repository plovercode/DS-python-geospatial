# Rescale the data to 0-1
b4_data = (b4_data - b4_data.min())/(b4_data.max() - b4_data.min())
b8_data = (b8_data - b8_data.min())/(b8_data.max() - b8_data.min())