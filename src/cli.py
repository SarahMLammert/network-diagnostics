"""
Command-line interface for the network diagnostics tool.

Responsible for parsing user input, loading hosts, and invoking
the diagnostics pipeline. Does not perform network operations itself.
"""
from pathlib import Path
import argparse
import sys

def read_hosts_file(path: Path) -> list[str]:
    """
    Reads a hosts file and returns a list of valid host strings.
    """
    if not path.is_file():
        raise FileNotFoundError(f"Hosts file not found: {path}")

    hosts: list[str] = []

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        hosts.append(line)
    if not hosts:
        raise ValueError("Hosts file contains no valid hosts")
    return hosts

def main():
    """
    Entry point for the CLI.

    Parses command-line arguments, loads the hosts file,
    and prints the validated host list. Handles user-facing
    error reporting and exit codes.
    """
    parser = argparse.ArgumentParser(
        description="Network diagnostics CLI tool."
    )
    parser.add_argument(
        "hosts_file",
        help="Path to newline-separated hosts file."
    )

    args = parser.parse_args()

    hosts_path = Path(args.hosts_file)

    try:
        hosts = read_hosts_file(hosts_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Loaded {len(hosts)} hosts:")

    for host in hosts:
        print(f"- {host}")

if __name__ == "__main__":
    main()
