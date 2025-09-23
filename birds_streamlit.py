import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium

# ---- LOAD DATA ----
puerto_rico_bird_recordings = pd.read_json("puerto_rico_recordings.json")
recordings_df = pd.DataFrame(puerto_rico_bird_recordings["recordings"].tolist())
recordings_df = recordings_df.query("file != '' and lng.notnull() and lat.notnull()")

recordings_df["lat"] = recordings_df["lat"].astype(float)
recordings_df["lng"] = recordings_df["lng"].astype(float)

st.title("Puerto Rico Bird Recordings")

# ---- SESSION STATE ----
if "selected_row" not in st.session_state:
    st.session_state["selected_row"] = recordings_df.index[0]

# ---- COLOR FUNCTION ----
def get_marker_color(idx):
    if idx == st.session_state["selected_row"]:
        return "red"  # highlight selected
    return "blue"     # default color

# ---- CREATE MAP ----
m = folium.Map(
    location=[recordings_df["lat"].mean(), recordings_df["lng"].mean()],
    zoom_start=7,
)

# Add markers for each recording
for idx, row in recordings_df.iterrows():
    popup_html = f"""
    <b>{row['gen']} {row['sp']}</b><br>
    Common: {row['en']}<br>
    Location: {row['loc']}<br>
    Type: {row['type']}<br>
    <i>Click marker to select</i>
    """
    folium.Marker(
        location=[row["lat"], row["lng"]],
        tooltip=row["en"],
        popup=popup_html,
        icon=folium.Icon(color=get_marker_color(idx)),
    ).add_to(m)

# Render map with click tracking
map_data = st_folium(m, width=700, height=500)

# ---- UPDATE SELECTION FROM MAP ----
if map_data and map_data.get("last_object_clicked_tooltip"):
    clicked_name = map_data["last_object_clicked_tooltip"]
    match = recordings_df[recordings_df["en"] == clicked_name]
    if not match.empty:
        st.session_state["selected_row"] = match.index[0]

# ---- SELECTION BOX ----
selected_row = st.selectbox(
    "Select a recording to play:",
    recordings_df.index,
    index=recordings_df.index.get_loc(st.session_state["selected_row"]),
    format_func=lambda idx: f"{recordings_df.loc[idx,'gen']} - {recordings_df.loc[idx,'sp']} - {recordings_df.loc[idx,'en']} - {recordings_df.loc[idx,'loc']} - {recordings_df.loc[idx,'type']}",
    key="selected_row",
)

# ---- AUDIO PLAYER ----
audio_file_url = recordings_df.loc[st.session_state["selected_row"], "file"]
st.audio(audio_file_url)

# ---- FILTERED TABLE BASED ON MAP SELECTION ----
filtered_df = recordings_df.loc[[st.session_state["selected_row"]]]
st.dataframe(filtered_df)