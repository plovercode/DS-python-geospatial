# A Diverging colormap `RdYlGn` with a normalization on the color limits in two directions of the central point - 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html
fig, ax = plt.subplots(figsize=(14, 5))

div_norm = mcolors.TwoSlopeNorm(vmin=-0.1, vcenter=0.4, vmax=0.8)

ll = ax.imshow(ndvi.values, cmap="RdYlGn", norm=div_norm)
fig.colorbar(ll);
ax.set_axis_off();