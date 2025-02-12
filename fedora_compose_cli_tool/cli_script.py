import argparse
from .fedora_compose_manager import FedoraComposeManager
from .nevra_parser import parse

class CLI:

    @staticmethod
    def list_composes(days=None):
        """List Fedora Rawhide composes from the past X days."""
        if days is None:
            days = 7  # default to 7 days if no input is provided
        composes = FedoraComposeManager.list_composes(days)
        for compose in composes:
            print(compose)

    @staticmethod
    def compare_composes(old_date, new_date):
        """Compare two Fedora Rawhide composes and output package changes separately in descending order."""
        added, removed, changed = FedoraComposeManager.compare_composes(old_date, new_date)

        print("\n=== REMOVED PACKAGES ===")
        for pkg, timestamp in sorted(removed.items(), key=lambda x: x[1], reverse=True):
            name, version = parse(pkg)
            print(f"[{timestamp}] {name} REMOVED ({version})")

        print("\n=== ADDED PACKAGES ===")
        for pkg, timestamp in sorted(added.items(), key=lambda x: x[1], reverse=True):
            name, version = parse(pkg)
            print(f"[{timestamp}] {name} ADDED ({version})")

        print("\n=== CHANGED PACKAGES ===")
        for pkg, (old_ver, new_ver, timestamp) in sorted(changed.items(), key=lambda x: x[1][2], reverse=True):
            print(f"[{timestamp}] {pkg} CHANGED ({old_ver} -> {new_ver})")

    @staticmethod
    def run():
        """Run the CLI tool."""
        parser = argparse.ArgumentParser(description="Fedora Rawhide Compose Diff Tool")
        subparsers = parser.add_subparsers(dest="command", required=True)

        # List Composes
        list_parser = subparsers.add_parser("list", help="List recent Rawhide composes")
        list_parser.add_argument(
            "days", 
            type=int, 
            nargs="?",  # Make the days argument optional
            help="Number of days to look back (default: 7)"
        )

        # Compare Composes
        diff_parser = subparsers.add_parser("diff", help="Compare two Rawhide composes")
        diff_parser.add_argument("old", type=str, help="Old compose date (YYYYMMDD)")
        diff_parser.add_argument("new", type=str, help="New compose date (YYYYMMDD)")

        args = parser.parse_args()

        if args.command == "list":
            CLI.list_composes(args.days)  # Pass the 'days' argument dynamically
        elif args.command == "diff":
            CLI.compare_composes(args.old, args.new)

