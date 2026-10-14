"""CLI entry kept stable: `python -m agents.sync_agent.run ideas push|pull|pull-remote`."""

from __future__ import annotations

import sys

from agents.sync_agent.ideas_run import main as ideas_main


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "ideas":
        argv = argv[1:]
    return ideas_main(argv)


if __name__ == "__main__":
    sys.exit(main())
