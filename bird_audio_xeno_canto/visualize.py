"""Map visualization utilities for bird recordings."""

import pandas as pd
import folium
import streamlit as st


def create_recording_map(recordings_df: pd.DataFrame) -> folium.Map:
    """
    Create an interactive Folium map with recording markers.
    
    Args:
        recordings_df: DataFrame with recording data including lat/lng
        
    Returns:
        Folium map object
    """
    # Initialize map centered on Puerto Rico
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

    return m


def get_marker_color(idx: int) -> str:
    """
    Get marker color based on selection state.
    
    Args:
        idx: Row index
        
    Returns:
        Color string for marker
    """
    if "selected_row" in st.session_state and idx == st.session_state["selected_row"]:
        return "red"  # highlight selected
    return "blue"     # default color
