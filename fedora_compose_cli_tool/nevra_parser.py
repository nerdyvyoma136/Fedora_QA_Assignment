def parse(nevra):
    """Parse NEVRA (Name, Environment, Version, Release, Architecture)."""
    name = nevra.rsplit("-", 2)[0]  # Extract package name
    version = '-'.join(nevra.rsplit('-', 2)[1:]).rsplit('.', 2)[0]  # Extract version
    return name, version