# Bird Audio Xeno-canto 🐦

A Python package for exploring Puerto Rico bird audio recordings from Xeno-canto.

## Features

- **Interactive Map**: Visualize bird recording locations across Puerto Rico
- **Data Processing**: Clean and process recording metadata
- **Audio Download**: Batch download audio files from recordings
- **Streamlit App**: Web interface for exploring recordings

## Installation

### Development Setup

```bash
# Clone or navigate to the project
cd bird_audio_xeno_canto

# Install in editable mode with dependencies
pip install -e .
```

### Running the Streamlit App

```bash
streamlit run apps/streamlit_app.py
```

Or using the installed command:

```bash
bird-app
```

## Project Structure

```
bird_audio_xeno_canto/
├── bird_audio_xeno_canto/      # Main package
│   ├── __init__.py             # Package init and exports
│   ├── data_processor.py       # Data loading and processing
│   ├── downloader.py           # Audio file download utilities
│   └── visualize.py            # Map visualization
├── apps/
│   └── streamlit_app.py        # Streamlit web app
├── data/
│   └── puerto_rico_recordings.json  # Recording metadata
├── pyproject.toml              # Python package configuration
└── README.md                   # This file
```

## Usage

### As a Package

```python
from bird_audio_xeno_canto import load_recordings, process_recordings

# Load and process data
recordings = load_recordings("data/puerto_rico_recordings.json")
clean_recordings = process_recordings(recordings)

# Download audio files
from bird_audio_xeno_canto import download_files_from_list
download_files_from_list(recordings["file"], recordings["id"], "audio_files")
```

### Using the Streamlit App

```bash
streamlit run apps/streamlit_app.py
```

Browse the interactive map to explore bird recording locations in Puerto Rico.

## Requirements

- Python 3.9+
- pandas
- streamlit
- folium
- streamlit-folium
- requests

## Development

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Format Code

```bash
black .
```

## Data Source

Bird recording data from Xeno-canto (https://www.xeno-canto.org/)
