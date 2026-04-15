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
    # Set center to Puerto Rico center (approximately)
    # This ensures the map focuses on Puerto Rico even if recording data is sparse
    puerto_rico_center = [18.22, -66.59]
    
    # Calculate bounds to fit all markers
    min_lat = recordings_df["lat"].min()
    max_lat = recordings_df["lat"].max()
    min_lng = recordings_df["lng"].min()
    max_lng = recordings_df["lng"].max()
    
    # Initialize map centered on Puerto Rico
    m = folium.Map(
        location=puerto_rico_center,
        zoom_start=9,
    )
    
    # Fit map to show all markers
    m.fit_bounds([[min_lat, min_lng], [max_lat, max_lng]], padding=(0.1, 0.1))

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
    if "selected_idx" in st.session_state and idx == st.session_state["selected_idx"]:
        return "red"  # highlight selected
    return "blue"     # default color
