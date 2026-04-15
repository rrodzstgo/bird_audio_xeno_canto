"""Data loading and processing utilities for bird recordings."""

import os
import pandas as pd


def load_recordings(json_path: str) -> pd.DataFrame:
    """
    Load bird recordings from JSON file.
    
    Args:
        json_path: Path to the puerto_rico_recordings.json file
        
    Returns:
        DataFrame with raw recording data
    """
    puerto_rico_bird_recordings = pd.read_json(json_path)
    recordings_df = pd.DataFrame(
        puerto_rico_bird_recordings["recordings"].tolist()
    )
    return recordings_df


def process_recordings(recordings_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and process recordings dataframe.
    
    Args:
        recordings_df: Raw recordings dataframe
        
    Returns:
        Processed dataframe with valid coordinates and files
    """
    # Filter records with valid files and coordinates
    recordings_df = recordings_df.query(
        'file != "" and lng.notnull() and lat.notnull()'
    ).copy()
    
    # Convert coordinates to float
    recordings_df["lat"] = recordings_df["lat"].astype(float)
    recordings_df["lng"] = recordings_df["lng"].astype(float)
    
    return recordings_df
