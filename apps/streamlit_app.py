"""Streamlit app for exploring Puerto Rico bird recordings."""

import os
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

# Import from the package
from bird_audio_xeno_canto import (
    load_recordings,
    process_recordings,
    create_recording_map,
)


def get_data_path():
    """Get the path to the data directory."""
    # The data directory is one level up from this file
    app_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(app_dir)
    return os.path.join(project_dir, "data", "puerto_rico_recordings.json")


def main():
    """Main Streamlit app."""
    st.set_page_config(
        page_title="Puerto Rico Bird Recordings",
        page_icon="🐦",
        layout="wide",
    )

    st.title("🐦 Puerto Rico Bird Recordings")

    # Load and process data
    data_path = get_data_path()
    
    if not os.path.exists(data_path):
        st.error(f"Data file not found at {data_path}")
        st.info("Please ensure puerto_rico_recordings.json is in the data/ directory")
        return

    recordings_df = load_recordings(data_path)
    recordings_df = process_recordings(recordings_df)

    # Initialize session state
    if "selected_row" not in st.session_state:
        st.session_state["selected_row"] = recordings_df.index[0]

    # Create and display map
    st.subheader("Recording Locations")
    m = create_recording_map(recordings_df)
    map_data = st_folium(m, width=700, height=500)

    # Display recording details
    st.subheader("Recording Information")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Recordings", len(recordings_df))
        st.metric("Unique Species", recordings_df["en"].nunique())

    with col2:
        st.metric("Unique Locations", recordings_df["loc"].nunique())
        st.metric("Recording Types", recordings_df["type"].nunique())

    # Display selected recording details in a table
    if len(recordings_df) > 0:
        st.write("### Sample Recordings")
        st.dataframe(
            recordings_df[["en", "gen", "sp", "loc", "type"]].head(10),
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
