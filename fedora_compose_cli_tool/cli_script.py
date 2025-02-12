import argparse
from .fedora_compose_manager import FedoraComposeManager
from .nevra_parser import parse

class CLI:

    @staticmethod
    def list_composes(days):
        """List Fedora Rawhide composes from the past X days."""
        composes = FedoraComposeManager.list_composes(days)
        for compose in composes:
            print(compose)

    @staticmethod
    def compare_composes(old_date, new_date):
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

    @staticmethod
    def run():
        """Run the CLI tool."""
        parser = argparse.ArgumentParser(description="Fedora Rawhide Compose Diff Tool")
        subparsers = parser.add_subparsers(dest="command", required=True)

        # List Composes
        list_parser = subparsers.add_parser("list", help="List recent Rawhide composes")
        list_parser.add_argument("days", type=int, help="Number of days to look back")

        # Compare Composes
        diff_parser = subparsers.add_parser("diff", help="Compare two Rawhide composes")
        diff_parser.add_argument("old", type=str, help="Old compose date (YYYYMMDD)")
        diff_parser.add_argument("new", type=str, help="New compose date (YYYYMMDD)")

        args = parser.parse_args()

        if args.command == "list":
            CLI.list_composes(args.days)
        elif args.command == "diff":
            CLI.compare_composes(args.old, args.new)