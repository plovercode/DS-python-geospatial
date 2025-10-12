# As a quick reference, plot using the `"Greens"` colormap as such:
fig, ax = plt.subplots(figsize=(14, 5))
ll = ndvi.plot.imshow(ax=ax, cmap="Greens")
ax.set_aspect("equal")