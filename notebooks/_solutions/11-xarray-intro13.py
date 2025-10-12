# Create the histogram plots
fig, (ax0, ax1) = plt.subplots(1, 2, sharey=True, figsize=(12, 4))
b4_data.plot.hist(bins=30, log=True, ax=ax0)
b4_data_f.plot.hist(bins=30, log=True, ax=ax1);