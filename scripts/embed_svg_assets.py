#!/usr/bin/env python3
"""Embed local asset references into SVG files as data URIs."""
from __future__ import annotations

import base64
import mimetypes
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "assets"

SVGS = [
    ASSETS_DIR / "engineering-universe.svg",
    ASSETS_DIR / "enterprise-ai-platform.svg",
    ASSETS_DIR / "engineering-orbit.svg",
]


def data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    if not mime:
      mime = "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def main() -> None:
    for svg in SVGS:
        text = svg.read_text(encoding="utf-8")
        for rel in sorted((ASSETS_DIR / "orbit-assets").glob("*")):
            marker = f'href="orbit-assets/{rel.name}"'
            if marker in text:
                text = text.replace(marker, f'href="{data_uri(rel)}"')
        svg.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
