"""Main module for the project."""

from .console import display_welcome


def main() -> int:
    """Main function."""
    display_welcome()
    return 0


if __name__ == "__main__":
    exit(main())
