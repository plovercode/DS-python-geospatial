# Plot the stations with a background map
stations_webmercator.plot(markersize=5, tiles=True)

# or explicitly:
# import contextily
# ax = stations_webmercator.plot(markersize=5, tiles=True)
# contextily.add_basemap(ax)