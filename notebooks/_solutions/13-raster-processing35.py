roads_buffer_arr = rasterio.features.rasterize(
    roads_buffer.geometry, 
    out_shape=dem_gent.shape, 
    transform=dem_gent.rio.transform())