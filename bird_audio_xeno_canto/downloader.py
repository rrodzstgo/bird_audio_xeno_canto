"""Audio file download utilities."""

import os
import requests
from typing import List


def download_file(url: str, save_path: str) -> bool:
    """
    Download a file from URL and save to disk.
    
    Args:
        url: URL of file to download
        save_path: Local path where file will be saved
        
    Returns:
        True if successful, False otherwise
    """
    try:
        response = requests.get(url, timeout=30, verify=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {save_path}")
            return True
        else:
            print(f"Failed to download {url}: Status {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print(f"Timeout downloading {url} (exceeded 30s)")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error downloading {url}: {e}")
        return False


def download_files_from_list(
    url_list: List[str], id_list: List[str], download_dir: str
) -> None:
    """
    Download multiple files from a list of URLs.
    
    Args:
        url_list: List of file URLs to download
        id_list: List of IDs to use as filenames
        download_dir: Directory where files will be saved
    """
    os.makedirs(download_dir, exist_ok=True)
    for url, file_id in zip(url_list, id_list):
        filename = f"{file_id}.mp3"
        save_path = os.path.join(download_dir, filename)
        download_file(url, save_path)
