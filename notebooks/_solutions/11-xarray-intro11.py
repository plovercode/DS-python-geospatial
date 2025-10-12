# Convert to float and make 65535 equal to Nan
b4_data_f = b4_data.astype(float)
b4_data_f = b4_data_f.where(b4_data != 65535)