"""Console script for yearver."""
import argparse
import sys
from yearver import Version, bump

def main():
    """Console script for yearver."""
    parser = argparse.ArgumentParser()
    parser.add_argument('last_release', type='str')
    parser.add_argument('current_version', type='str')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    release = Version(args.last_release)
    current = Version(args.current_version)

    print(str(bump(release, current)))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
