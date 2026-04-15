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
    col_map, col_player = st.columns([2, 1])
    
    with col_map:
        m = create_recording_map(recordings_df)
        map_data = st_folium(m, width=100, height=500)

    # Display recording details
    st.subheader("Recording Information")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Recordings", len(recordings_df))
        st.metric("Unique Species", recordings_df["en"].nunique())

    with col2:
        st.metric("Unique Locations", recordings_df["loc"].nunique())
        st.metric("Recording Types", recordings_df["type"].nunique())

    # Display recording table with selection
    if len(recordings_df) > 0:
        st.write("### Select a Recording")
        
        # Create a selectbox for recording selection
        recording_options = [
            f"{row['en']} - {row['loc']}" 
            for _, row in recordings_df.iterrows()
        ]
        selected_idx = st.selectbox(
            "Choose a recording:",
            range(len(recording_options)),
            format_func=lambda i: recording_options[i],
            key="recording_selector"
        )
        
        # Get selected recording
        selected_recording = recordings_df.iloc[selected_idx]
        
        # Display selected recording details
        st.write("### Selected Recording Details")
        detail_col1, detail_col2 = st.columns(2)
        
        with detail_col1:
            st.write(f"**Species**: {selected_recording['en']}")
            st.write(f"**Scientific**: {selected_recording['gen']} {selected_recording['sp']}")
            st.write(f"**Location**: {selected_recording['loc']}")
            st.write(f"**Recording Type**: {selected_recording['type']}")
        
        with detail_col2:
            if "lat" in selected_recording and "lng" in selected_recording:
                st.write(f"**Latitude**: {selected_recording['lat']:.4f}")
                st.write(f"**Longitude**: {selected_recording['lng']:.4f}")
        
        # Audio player
        st.write("### 🎵 Audio Player")
        if "file" in selected_recording and selected_recording['file']:
            try:
                st.audio(selected_recording['file'], format="audio/mp3")
                st.caption(f"Recording ID: {selected_recording.get('id', 'N/A')}")
            except Exception as e:
                st.error(f"Could not load audio: {e}")
        else:
            st.warning("No audio file available for this recording")
        
        # Display all recordings as a table
        st.write("### All Recordings")
        display_cols = ["en", "gen", "sp", "loc", "type"]
        st.dataframe(
            recordings_df[display_cols],
            use_container_width=True,
            hide_index=False,
        )


if __name__ == "__main__":
    main()
