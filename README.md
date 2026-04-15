# Bird Audio Xeno-canto 🐦

A Python package for exploring Puerto Rico bird audio recordings from Xeno-canto.

## Features

- **Interactive Map**: Visualize bird recording locations across Puerto Rico
- **Data Processing**: Clean and process recording metadata
- **Audio Download**: Batch download audio files from recordings
- **Streamlit App**: Web interface for exploring recordings

## Installation

### Quick Start with uv (Recommended)

```bash
# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or navigate to the project
cd bird_audio_xeno_canto

# Install in editable mode with dependencies
uv pip install -e . --python ve/bin/python
```

### Traditional pip Installation

```bash
# Clone or navigate to the project
cd bird_audio_xeno_canto

# Create and activate virtual environment
python -m venv ve
source ve/bin/activate

# Install in editable mode
pip install -e .
```

### Running the Streamlit App

```bash
# Activate virtual environment (if using traditional pip)
source ve/bin/activate

# Run the app
streamlit run apps/streamlit_app.py
```

## Project Structure

```
bird_audio_xeno_canto/
├── bird_audio_xeno_canto/           # Main package
│   ├── __init__.py                  # Package init and exports
│   ├── data_processor.py            # Data loading and processing
│   ├── downloader.py                # Audio file download utilities
│   └── visualize.py                 # Map visualization
├── apps/
│   ├── __init__.py
│   └── streamlit_app.py             # Streamlit web app
├── data/
│   └── puerto_rico_recordings.json  # Recording metadata
├── pyproject.toml                   # Python package configuration
├── uv.lock                          # Locked dependency versions (reproducible)
├── .gitignore                       # Git ignore rules
├── README.md                        # This file
└── ve/                              # Virtual environment
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
 >= 1.3.0
- streamlit >= 1.0
- folium >= 0.12
- streamlit-folium >= 0.6
- requests >= 2.25

All dependencies automatically installed during `uv pip install -e .` or `pip install -e .`

## Dependency Management

### Using uv (Recommended)

**Install dependencies:**
```bash
export PATH="$HOME/.local/bin:$PATH"  # Add to PATH permanently
uv pip install -e . --python ve/bin/python
```

**Update lock file:**
```bash
uv pip compile --python ve/bin/python pyproject.toml -o uv.lock
```

**Add new dependency:**
```bash
uv pip install package-name --python ve/bin/python
uv pip compile --python ve/bin/python pyproject.toml -o uv.lock
```

### Using traditional pip

```bash
pip install -e .           # Install from pyproject.toml
pip install -r uv.lock     # Install from lock file
```

## Development

### Install Development Dependencies

```bash
uv pip install -e ".[dev]" --python ve/bin/python
# or with traditional pip:
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

## Contributing

Contributions are welcome! Please:
1. Create a feature branch from `main`
2. Make your changes with clear, descriptive commits
3. Follow conventional commit format (feat:, fix:, chore:, etc.)
4. Update `uv.lock` if you add dependencies: `uv pip compile --python ve/bin/python pyproject.toml -o uv.lock`
5. Submit a pull request with a clear description Format Code

```bash
black .
```

## Data Source

Bird recording data from Xeno-canto (https://www.xeno-canto.org/)
