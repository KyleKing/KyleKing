# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow"]
# ///
"""Validate that every *.gif URL linked from README.md is a real, playable animation.

lychee confirms the URL responds; this confirms the bytes behind it decode as
GIF frames, so a demo recording silently swapped for an error page or a
single-frame placeholder still fails the hook.
"""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageSequence, UnidentifiedImageError

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
GIF_URL_RE = re.compile(r"https://\S+\.gif")


def check_gif(url: str) -> str | None:
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
    except (urllib.error.URLError, TimeoutError) as err:
        return f"download failed: {err}"

    try:
        with Image.open(BytesIO(data)) as img:
            if img.format != "GIF":
                return f"not a GIF (detected {img.format})"
            frame_count = sum(1 for _ in ImageSequence.Iterator(img))
    except (UnidentifiedImageError, OSError) as err:
        return f"failed to decode: {err}"

    if frame_count < 2:
        return f"only {frame_count} frame(s), expected an animation"

    return None


def main() -> int:
    readme = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    text = HTML_COMMENT_RE.sub("", readme.read_text())
    urls = sorted(set(GIF_URL_RE.findall(text)))

    failures = []
    for url in urls:
        error = check_gif(url)
        if error:
            failures.append(f"{url}: {error}")
        else:
            print(f"ok: {url}")

    if failures:
        print("\nInvalid GIFs:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
