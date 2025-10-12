import rasterio.features

green_arr = rasterio.features.rasterize(
    green.to_crs("EPSG:31370").geometry, 
    out_shape=dem_gent.shape, 
    transform=dem_gent.rio.transform())