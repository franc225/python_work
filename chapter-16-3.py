from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')

contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads (contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

# Create a scatter plot for earthquake locations.
lats = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
title = 'Global Earthquakes'

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth')
fig.show()