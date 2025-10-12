# Convert all values above 15000
tc_g.where(tc_g < 15000, 65535)