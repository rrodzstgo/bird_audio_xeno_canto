import pandas as pd
import numpy as np
import folium
import streamlit as ststr   


puerto_rico_bird_recordings = pd.read_json('puerto_rico_recordings.json')
recordings_df = pd.DataFrame(puerto_rico_bird_recordings['recordings'].tolist())

recordings_df =recordings_df[recordings_df['lat'].notna()]

recordings_df['lat'] = recordings_df['lat'].replace('', np.nan)
recordings_df['lat'] = recordings_df['lat'].astype(float)

recordings_df['lng'] = recordings_df['lng'].replace('', np.nan)
recordings_df['lng'] = recordings_df['lng'].astype(float)

map_osm = folium.Map(location=[18.22, -66.59], zoom_start=10)

recordings_df.apply(lambda row:folium.Marker(location=[row["lat"], row["lng"]], 
                                              radius=10, interactive = True, 
                                              tooltip=(row['loc']),
                                              popup=f"Lattitude:{row['lat']}<br>"
                                                f"Longitude:{row['lng']}<br>"
                                                 f"Name:{row['loc']}<br>"
                                                 f"Organism:{row['en']}"
                                              ).add_to(map_osm), axis=1)
map_osm