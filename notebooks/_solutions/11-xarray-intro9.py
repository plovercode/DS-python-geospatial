b4_data = xr.open_dataarray("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff",
                            engine="rasterio", mask_and_scale=False)