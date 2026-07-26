# /// script
# requires-python = ">=3.11"
# ///
"""Run lychee and surface any redirected URLs, not just broken ones.

lychee's compact/default output only hints that redirects happened and
tells you to rerun with `-v`/`-vv` to see them; this runs that verbose,
JSON-formatted pass once and prints the redirect chain directly, so `hk`
output already has what you need without a manual rerun.
"""

from __future__ import annotations

import json
import subprocess
import sys


def main() -> int:
    files = sys.argv[1:] or ["README.md"]
    proc = subprocess.run(
        ["lychee", "--verbose", "--no-progress", "--format", "json", *files],
        capture_output=True,
        text=True,
        check=False,
    )

    try:
        report = json.loads(proc.stdout)
    except json.JSONDecodeError:
        sys.stdout.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        return proc.returncode or 1

    for file, entries in report.get("redirect_map", {}).items():
        for entry in entries:
            for redirect in entry["redirects"]:
                print(f"redirect ({file}): {entry['origin']} --[{redirect['code']}]--> {redirect['url']}")

    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        print(json.dumps(report.get("error_map", {}), indent=2), file=sys.stderr)
        return proc.returncode

    print(f"{report['successful']}/{report['total']} links OK, {report['redirects']} redirect(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
