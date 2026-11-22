fig, ax = plt.subplots(figsize=(15, 15))
ax = gdf_gent.to_crs(3857).plot(column="no2", ax=ax, legend=True, vmax=50)
contextily.add_basemap(ax)
ax.set_axis_off()