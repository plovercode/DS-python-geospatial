fig, ax = plt.subplots(figsize=(15, 15))

gent.to_crs("EPSG:31370").plot(ax=ax, alpha=0.2, color="grey")
contextily.add_basemap(ax, crs="EPSG:31370")

suitable_locations.where(suitable_locations > 0).plot.imshow(ax=ax, alpha=0.5, add_colorbar=False)
ax.set_aspect("equal")