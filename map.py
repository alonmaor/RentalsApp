import folium
import pandas as pd


def produce_map(locations):
    print(locations)
    longitutes = [l[0] for l in locations]
    latitues = [l[1] for l in locations]
    names = [l[2] for l in locations]
    data = {
        'Name': names,
        'Latitude': longitutes,
        'Longitude': latitues
    }
    df = pd.DataFrame(data)

    m = folium.Map(location=[32.06, 34.78], zoom_start=13)

    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        for index, row in df.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name']
            ).add_to(m)

    m.save('map.html')

