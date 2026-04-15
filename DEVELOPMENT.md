# Development Guide

This document provides technical details about the package architecture and development setup.

## Architecture

### Package Structure

The `bird_audio_xeno_canto` package is organized into three main modules:

#### data_processor.py
Handles data loading and processing:
- `load_recordings(json_path)`: Load recordings from JSON file
- `process_recordings(recordings_df)`: Clean and validate recording data
  - Filters records with valid files and coordinates
  - Converts coordinates to float type
  - Removes invalid entries

#### downloader.py
Manages audio file downloads:
- `download_file(url, save_path)`: Download single file from URL with error handling
- `download_files_from_list(url_list, id_list, download_dir)`: Batch download from list
  - Creates directory if needed
  - Handles errors gracefully
  - Prints progress for each download

#### visualize.py
Creates interactive visualizations:
- `create_recording_map(recordings_df)`: Generate Folium map with markers
- `get_marker_color(idx)`: Determine marker color based on selection state
  - Reads from Streamlit session state
  - Returns 'red' for selected, 'blue' for default

### Application Layer

#### apps/streamlit_app.py
Main web application:
- `main()`: Entry point for Streamlit app
- Imports all core functions from package
- Handles data path resolution
- Displays metrics and data tables
- Renders interactive map

## Data Flow

```
puerto_rico_recordings.json
        ↓
load_recordings()
        ↓
process_recordings()
        ↓
create_recording_map()
        ↓
st_folium() [Streamlit]
```

## Environment Setup

### Python Version
- Minimum: 3.9
- Tested: 3.12

### Virtual Environment
```bash
# Using uv
uv pip install -e . --python ve/bin/python

# Using venv
python -m venv ve
source ve/bin/activate
pip install -e .
```

## Dependency Management

### pyproject.toml
- `requires`: Build system requirements
- `project.dependencies`: Runtime dependencies
- `project.optional-dependencies.dev`: Development tools

### uv.lock
Auto-generated lock file from `pyproject.toml`:
- Pins exact versions of all dependencies
- Enables reproducible installs
- Update with: `uv pip compile pyproject.toml -o uv.lock`

## Common Development Tasks

### Adding a New Function

1. Create function in appropriate module:
   ```python
   # bird_audio_xeno_canto/data_processor.py
   def new_function(param):
       """Clear docstring describing purpose and parameters."""
       pass
   ```

2. Export in `__init__.py`:
   ```python
   from .data_processor import new_function
   __all__ = [..., "new_function"]
   ```

3. Update documentation: README.md or module docstrings

4. Commit with `feat:` prefix:
   ```bash
   git add -A
   git commit -m "feat: Add new_function for X functionality"
   ```

### Adding a Dependency

1. Install locally:
   ```bash
   uv pip install package-name --python ve/bin/python
   ```

2. Add to `pyproject.toml`:
   ```toml
   dependencies = [
       ...,
       "package-name>=version",
   ]
   ```

3. Update lock file:
   ```bash
   uv pip compile --python ve/bin/python pyproject.toml -o uv.lock
   ```

4. Commit both:
   ```bash
   git add pyproject.toml uv.lock
   git commit -m "chore: Add package-name dependency"
   ```

### Running Tests

```bash
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest tests/test_module.py    # Specific test file
pytest -k test_name            # Specific test
```

### Code Formatting

```bash
# Format with black
black bird_audio_xeno_canto/ apps/

# Check style with flake8
flake8 bird_audio_xeno_canto/ apps/

# All together
black . && flake8 .
```

## Debugging

### Enable Verbose Logging

In your script:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Streamlit Debug Mode

```bash
streamlit run apps/streamlit_app.py --logger.level=debug
```

### Interactive Python

```bash
python
>>> from bird_audio_xeno_canto import load_recordings
>>> df = load_recordings("data/puerto_rico_recordings.json")
>>> print(df.head())
```

## Performance Considerations

### Data Loading
- JSON parsing is done with pandas (generally fast)
- For large datasets, consider chunking or conversion to Parquet

### Visualization
- Map rendering can be slow with 1000+ markers
- Consider clustering or filtering for performance

### Downloads
- Serial downloads can be slow
- Consider adding concurrent.futures for parallel downloads

## Documentation Standards

### Docstrings
Use Google-style docstrings:
```python
def function(param1: str, param2: int) -> bool:
    """Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something is wrong
    """
```

### Type Hints
Always include type hints:
```python
from typing import List
def process_items(items: List[str]) -> dict:
    pass
```

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [uv Documentation](https://docs.astral.sh/uv/)
