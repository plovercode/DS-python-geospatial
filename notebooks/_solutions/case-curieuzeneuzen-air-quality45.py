# defining custom order of the classes (following the order in the CORINE hierarchy as defined in the legend csv)
classes = legend["group"].unique()
# but removing the infrequent ones
counts = gdf['land_use_class'].value_counts()
frequent_categories = counts[counts > 50].index
classes = [value for value in classes if value in frequent_categories]

fig, ax = plt.subplots(figsize=(8, 6))
seaborn.boxplot(y="land_use_class", x="no2", data=subset, ax=ax, color="C0", order=classes)
ax.set(xlabel="NO$_2$ concentration (µg/m³)", ylabel="CORINE Land Cover classes");