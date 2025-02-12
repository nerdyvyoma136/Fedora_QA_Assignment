import requests
import re

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