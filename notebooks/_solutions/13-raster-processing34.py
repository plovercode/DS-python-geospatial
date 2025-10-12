roads_buffer = roads_subset.to_crs("EPSG:31370").buffer(buffers)
roads_buffer.plot()