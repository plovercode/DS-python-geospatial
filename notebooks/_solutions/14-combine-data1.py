base_url = 'https://psl.noaa.gov/thredds/fileServer/Datasets/ncep.reanalysis/surface/air.sig995'

files = [f'{base_url}.{year}.nc' for year in range(1990, 2001)]
files