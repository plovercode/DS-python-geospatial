gdf['land_use'] = raster.sel(
    band=1,
    x=xarray.DataArray(gdf_raster.geometry.x, dims="point"),
    y=xarray.DataArray(gdf_raster.geometry.y, dims="point"),
    method="nearest",
)