import json
import os
<<<<<<< HEAD
from .utils import fetch_html, extract_compose_dates
=======
from .utils import fetch_html, extract_compose_dates, extract_timestamp
>>>>>>> 56b1257 (Adding logic for "CHANGED" category)
from .config import BASE_URL, ARCHITECTURE
from .nevra_parser import parse

class FedoraComposeManager:

    @staticmethod
    def list_composes(days=7):
        """List Fedora Rawhide composes from the past X days."""
        html = fetch_html(BASE_URL)
        if not html:
            return []
        return extract_compose_dates(html)[:days]

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
<<<<<<< HEAD
        """Compare two Fedora Rawhide composes and return added, removed, changed packages."""
        old_rpms = FedoraComposeManager.fetch_rpms(old_date)
        new_rpms = FedoraComposeManager.fetch_rpms(new_date)

        added = new_rpms - old_rpms
        removed = old_rpms - new_rpms
=======
        """Compare two Fedora Rawhide composes and return added, removed, changed packages with timestamps."""
    
        old_rpms = FedoraComposeManager.fetch_rpms(old_date)
        new_rpms = FedoraComposeManager.fetch_rpms(new_date)

        added = {pkg: extract_timestamp(pkg) for pkg in new_rpms - old_rpms}
        removed = {pkg: extract_timestamp(pkg) for pkg in old_rpms - new_rpms}
>>>>>>> 56b1257 (Adding logic for "CHANGED" category)
        changed = {}

        for pkg in old_rpms & new_rpms:
            old_name, old_version = parse(pkg)
            new_name, new_version = parse(pkg)

            if old_version != new_version:
<<<<<<< HEAD
                changed[old_name] = (old_version, new_version)

        return added, removed, changed
=======
                changed[old_name] = (old_version, new_version, extract_timestamp(pkg))

        return added, removed, changed
>>>>>>> 56b1257 (Adding logic for "CHANGED" category)
