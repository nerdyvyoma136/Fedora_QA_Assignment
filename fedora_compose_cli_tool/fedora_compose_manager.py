import json
import os
from .utils import fetch_html, extract_compose_dates, extract_timestamp
from .config import BASE_URL, ARCHITECTURE
from .nevra_parser import parse

class FedoraComposeManager:

    @staticmethod
    def list_composes(days=7):
        """List unique Fedora Rawhide compose dates from the past X days."""
        html = fetch_html(BASE_URL)
        if not html:
            return []

        unique_dates = sorted(set(extract_compose_dates(html)), reverse=True)
        return unique_dates[:days]  # Get only the required number of unique dates

    @staticmethod
    def fetch_rpms(compose_date):
        """Fetch RPMs from the given Fedora Rawhide compose date."""
        url = f"{BASE_URL}Fedora-Rawhide-{compose_date}.n.0/compose/metadata/rpms.json"
        json_data = fetch_html(url)
        if not json_data:
            return set()

        try:
            data = json.loads(json_data)
            return set(data["payload"]["rpms"]["Everything"].get(ARCHITECTURE, {}).keys())
        except (KeyError, json.JSONDecodeError):
            print(f"Error parsing JSON data from {url}")
            return set()

    @staticmethod
    def compare_composes(old_date, new_date):
        """Compare two Fedora Rawhide composes and return added, removed, changed packages within date range."""

        # Ensure old_date and new_date are integers
        old_date = int(old_date)
        new_date = int(new_date)

        old_rpms = FedoraComposeManager.fetch_rpms(old_date)
        new_rpms = FedoraComposeManager.fetch_rpms(new_date)

        # Extract timestamps and filter within the date range
        added = {pkg: extract_timestamp(pkg) for pkg in new_rpms - old_rpms if old_date <= extract_timestamp(pkg) <= new_date}
        removed = {pkg: extract_timestamp(pkg) for pkg in old_rpms - new_rpms if old_date <= extract_timestamp(pkg) <= new_date}

        changed = {}
        for pkg in old_rpms & new_rpms:
            old_name, old_version = parse(pkg)
            new_name, new_version = parse(pkg)

            if old_version != new_version:  # Fix indentation
                timestamp = extract_timestamp(pkg)
                if old_date <= timestamp <= new_date:  # Ensure timestamp is within range
                    changed[old_name] = (old_version, new_version, timestamp)

        return added, removed, changed

