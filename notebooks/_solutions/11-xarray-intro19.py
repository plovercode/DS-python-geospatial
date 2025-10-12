# Convert to float and convert values equal to 65535 into NaN
gent_f = gent.astype(float)
gent_f = gent_f.where(gent_f != 65535)