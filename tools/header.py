#!/usr/bin/env python3
"""Render the profile header as light and dark SVGs.

Run from the repo root: python3 tools/header.py
Writes assets/header-light.svg and assets/header-dark.svg.
"""
from pathlib import Path
from xml.sax.saxutils import escape

NAME = "RAVI RANJAN"
HANDLE = "@raviranjan6020"
TAGLINE = "Cloud / Platform Engineer building Kubernetes platforms, cloud infrastructure and GPU systems."
ROLES = "CKA  ·  KUBERNETES CONTRIBUTOR  ·  OPEN CLUSTER MANAGEMENT (CNCF)  ·  BENGALURU"
FACTS = [
    ("FOCUS", ["Kubernetes platforms", "Multi-cluster and GitOps", "GPUs on Kubernetes"]),
    ("CURRENTLY", ["Software Engineer at Nava", "KubeVirt, GPU passthrough", "OpenBao secrets and KMS"]),
    ("OPEN SOURCE", ["kubernetes", "kubernetes-sigs", "open-cluster-management-io"]),
]

THEMES = {
    "light": dict(bg="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e", accent="#0969da"),
    "dark": dict(bg="#161b22", border="#30363d", text="#e6edf3", muted="#9198a1", accent="#4493f8"),
}

MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

W, H, PAD = 1200, 420, 56


def render(t):
    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'role="img" aria-label="{escape(NAME.title())}. {escape(TAGLINE)}">')
    a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>')
    # top label row
    a(f'<text x="{PAD}" y="50" font-family="{MONO}" font-size="16" letter-spacing="2" fill="{t["accent"]}">FIG_000 / PROFILE</text>')
    a(f'<text x="{W-PAD}" y="50" text-anchor="end" font-family="{MONO}" font-size="16" fill="{t["muted"]}">{escape(HANDLE)}</text>')
    a(f'<line x1="{PAD}" y1="68" x2="{W-PAD}" y2="68" stroke="{t["border"]}"/>')
    # name, tagline, roles
    a(f'<text x="{PAD}" y="142" font-family="{MONO}" font-size="66" font-weight="700" letter-spacing="4" fill="{t["accent"]}">{escape(NAME)}</text>')
    a(f'<text x="{PAD}" y="188" font-family="{SANS}" font-size="25" fill="{t["text"]}">{escape(TAGLINE)}</text>')
    a(f'<text x="{PAD}" y="226" font-family="{MONO}" font-size="16" letter-spacing="1.5" fill="{t["muted"]}">{escape(ROLES)}</text>')
    a(f'<line x1="{PAD}" y1="254" x2="{W-PAD}" y2="254" stroke="{t["border"]}"/>')
    # three fact columns
    col = (W - 2 * PAD) / len(FACTS)
    for i, (label, lines) in enumerate(FACTS):
        x = PAD + i * col
        if i:
            a(f'<line x1="{x-18:.0f}" y1="274" x2="{x-18:.0f}" y2="{H-34}" stroke="{t["border"]}" stroke-dasharray="3 4"/>')
        a(f'<text x="{x:.0f}" y="292" font-family="{MONO}" font-size="15" letter-spacing="2" fill="{t["accent"]}">{label}</text>')
        for j, line in enumerate(lines):
            a(f'<text x="{x:.0f}" y="{326 + j*30}" font-family="{MONO}" font-size="19" fill="{t["text"]}">{escape(line)}</text>')
    a(f'<rect x="{PAD}" y="{H-10}" width="{W-2*PAD}" height="4" rx="2" fill="{t["accent"]}"/>')
    a('</svg>')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    assets = Path("assets")
    assets.mkdir(exist_ok=True)
    for name, theme in THEMES.items():
        (assets / f"header-{name}.svg").write_text(render(theme))
        print(f"wrote assets/header-{name}.svg")
