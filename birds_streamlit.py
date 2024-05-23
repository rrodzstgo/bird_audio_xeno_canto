import pandas as pd
import numpy as np
import folium
import streamlit as st   


puerto_rico_bird_recordings = pd.read_json('puerto_rico_recordings.json')
recordings_df = pd.DataFrame(puerto_rico_bird_recordings['recordings'].tolist())
recordings_df = recordings_df.query('file != "" and lng.notnull() and lat.notnull()')

recordings_df['lat'] = recordings_df['lat'].astype(float)
recordings_df['lng'] = recordings_df['lng'].astype(float)

st.map(recordings_df,
    latitude='lat',
    longitude='lng')

st.bar_chart(recordings_df, x = 'gen', y = 'alt')

st.dataframe(recordings_df)
