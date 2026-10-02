"""Jump List Clear — Clear Explorer and app jump lists after a preview of the files they point at."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='jump_list_clear',
        description='Clear Explorer and app jump lists after a preview of the files they point at.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Jump List Clear')
    print('Taskbar jump lists without old paths.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
