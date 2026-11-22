temp_mean = era5_renamed["temperature_k"].mean(dim=["latitude", "longitude"]).sel(time=slice("1981", "2025"))
temp_mean.resample(time="YE").mean().plot.line(figsize=(12, 5))