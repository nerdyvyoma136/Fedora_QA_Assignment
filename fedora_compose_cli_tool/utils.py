import requests
import re
from datetime import datetime

def fetch_html(url):
    """Fetch HTML content from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_compose_dates(html):
    """Extract Fedora Rawhide compose dates from HTML."""
    return sorted(re.findall(r'Fedora-Rawhide-(\d{8})\.n\.\d+/', html), reverse=True)

# Utility function to extract timestamps
def extract_timestamp(pkg_name):
    """Extracts a timestamp from package metadata (assuming it's encoded in name or available in metadata)."""
    
    match = re.search(r"(\d{4})(\d{2})(\d{2})", pkg_name)
    if match:
        return int(f"{match.group(1)}{match.group(2)}{match.group(3)}")  # Return YYYYMMDD as an integer

    return int(datetime.now().strftime("%Y%m%d"))  # Default to current date as integer
