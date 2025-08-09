import pandas as pd
import numpy as np
import folium
import streamlit as st   
import pydeck as pdk

puerto_rico_bird_recordings = pd.read_json('puerto_rico_recordings.json')
recordings_df = pd.DataFrame(puerto_rico_bird_recordings['recordings'].tolist())
recordings_df = recordings_df.query('file != "" and lng.notnull() and lat.notnull()')

recordings_df['lat'] = recordings_df['lat'].astype(float)
recordings_df['lng'] = recordings_df['lng'].astype(float)

st.title('Puerto Rico Bird Recordings')

# Add a map click handler to synchronize the selected dot with the recording
selected_point = st.session_state.get("selected_point", None)

# Modify the map click handler to properly update the selected point
def on_map_click(event):
    if event and "object" in event:
        st.session_state["selected_point"] = event["object"]

# Ensure selected_point is retrieved from session state
selected_point = st.session_state.get("selected_point")

# Update the Pydeck layer to include the click handler
layer = pdk.Layer(
    "ScatterplotLayer",
    data=recordings_df,
    get_position=["lng", "lat"],
    get_radius=400,
    get_fill_color=[200, 30, 0, 160],
    pickable=True,
)

# Define the Pydeck view
view_state = pdk.ViewState(
    latitude=recordings_df["lat"].mean(),
    longitude=recordings_df["lng"].mean(),
    zoom=7,
    pitch=0,
)

# Add the map with tooltips and click handling
st.pydeck_chart(
    pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            "html": "<b>Genus:</b> {gen}<br><b>Altitude:</b> {alt}<br><b>File:</b> {file}",
            "style": {"backgroundColor": "steelblue", "color": "white"},
        },
    )
)

# Update the audio player to play the recording of the selected dot
if selected_point:
    selected_row = recordings_df[
        (recordings_df["lat"] == selected_point["lat"]) & 
        (recordings_df["lng"] == selected_point["lng"])
    ].index[0]
    audio_file_url = recordings_df.loc[selected_row, 'file']
    st.audio(audio_file_url)

# Add a selection box to select a row from the dataframe
if "selected_row" not in st.session_state:
    st.session_state["selected_row"] = recordings_df.index[0]

selected_row = st.selectbox(
    "Select a recording to play:",
    recordings_df.index,
    index=recordings_df.index.get_loc(st.session_state["selected_row"]),
    format_func=lambda idx: f"{recordings_df.loc[idx, 'gen']} - {recordings_df.loc[idx, 'sp']} - {recordings_df.loc[idx, 'en']}",
    key="selected_row"
)

# Update the audio player to play the recording of the selected row
çaudio_file_url = recordings_df.loc[st.session_state["selected_row"], 'file']
st.audio(audio_file_url)

# Display the full table without filtering
st.dataframe(recordings_df)