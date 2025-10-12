# Create an image plot
fig, ax = plt.subplots(figsize=(12, 5))
img = b4_data_classified.plot.imshow(ax=ax, add_colorbar=False, interpolation="antialiased")
fig.colorbar(img, values=[0, 1, 2], ticks=[0, 1, 2])