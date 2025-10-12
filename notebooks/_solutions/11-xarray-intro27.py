# A sequential colormap `YlGn` using a Matplotlib norm to adjust colormap influence on image 
# https://matplotlib.org/stable/tutorials/colors/colormapnorms.html
import matplotlib.colors as mcolors

fig, ax = plt.subplots(figsize=(14, 5))

div_norm = mcolors.Normalize(0.1, 0.8)
ll = ndvi.plot.imshow(ax=ax, cmap="YlGn", norm=div_norm)
ax.set_aspect("equal")