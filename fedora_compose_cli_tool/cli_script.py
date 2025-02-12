import argparse
from .fedora_compose_manager import FedoraComposeManager
from .nevra_parser import parse

class CLI:

    @staticmethod
<<<<<<< HEAD
    def list_composes(days):
        """List Fedora Rawhide composes from the past X days."""
=======
    def list_composes(days=None):
        """List Fedora Rawhide composes from the past X days."""
        if days is None:
            days = 7  # default to 7 days if no input is provided
>>>>>>> 56b1257 (Adding logic for "CHANGED" category)
        composes = FedoraComposeManager.list_composes(days)
        for compose in composes:
            print(compose)

    @staticmethod
    def compare_composes(old_date, new_date):
<<<<<<< HEAD
        """Compare two Fedora Rawhide composes and output package changes."""
        added, removed, changed = FedoraComposeManager.compare_composes(old_date, new_date)

        for pkg in sorted(removed):
            name, version = parse(pkg)
            print(f"{name} REMOVED ({version})")

        for pkg in sorted(added):
            name, version = parse(pkg)
            print(f"{name} ADDED ({version})")

        for pkg, (old_ver, new_ver) in sorted(changed.items()):
            print(f"{pkg} CHANGED ({old_ver} -> {new_ver})")
=======
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
>>>>>>> 56b1257 (Adding logic for "CHANGED" category)

    @staticmethod
    def run():
        """Run the CLI tool."""
        parser = argparse.ArgumentParser(description="Fedora Rawhide Compose Diff Tool")
        subparsers = parser.add_subparsers(dest="command", required=True)

        # List Composes
        list_parser = subparsers.add_parser("list", help="List recent Rawhide composes")
<<<<<<< HEAD
        list_parser.add_argument("days", type=int, help="Number of days to look back")
=======
        list_parser.add_argument(
            "days", 
            type=int, 
            nargs="?",  # Make the days argument optional
            help="Number of days to look back (default: 7)"
        )
>>>>>>> 56b1257 (Adding logic for "CHANGED" category)

        # Compare Composes
        diff_parser = subparsers.add_parser("diff", help="Compare two Rawhide composes")
        diff_parser.add_argument("old", type=str, help="Old compose date (YYYYMMDD)")
        diff_parser.add_argument("new", type=str, help="New compose date (YYYYMMDD)")

        args = parser.parse_args()

        if args.command == "list":
<<<<<<< HEAD
            CLI.list_composes(args.days)
        elif args.command == "diff":
            CLI.compare_composes(args.old, args.new)
=======
            CLI.list_composes(args.days)  # Pass the 'days' argument dynamically
        elif args.command == "diff":
            CLI.compare_composes(args.old, args.new)

>>>>>>> 56b1257 (Adding logic for "CHANGED" category)
