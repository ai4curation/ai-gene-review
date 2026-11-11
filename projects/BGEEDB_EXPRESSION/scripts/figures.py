"""Draw the project figures from the committed results (never from hand-typed numbers).

    fig-calibration.svg  share of anatomy-bearing annotations whose GO anatomy is
                         among the gene's top-10% Bgee tissues, by reviewer action,
                         with the shuffled-pair rate as a reference tick
    fig-cerebellum.svg   cerebellum module genes x mouse developmental stage:
                         expressed in the step's declared context, only in the
                         wider cerebellar territory, only elsewhere, or no call

Both are plain SVG with light/dark CSS tokens and a <title> tooltip per mark.

Usage (from repo root, after calibrate.py and cerebellum_timing.py):
    uv run python projects/BGEEDB_EXPRESSION/scripts/figures.py
"""

from __future__ import annotations

import sys
from html import escape
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import bgee_common as bc  # noqa: E402

STYLE = """<style>
  .viz { --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --grid:#e4e3df; --s1:#2a78d6;
         --ord1:#1c5cab; --ord2:#86b6ef; --dot:#8a8984; }
  @media (prefers-color-scheme: dark) {
    .viz { --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --grid:#383835; --s1:#3987e5;
           --ord1:#9ec5f4; --ord2:#5598e7; --dot:#8a8984; }
  }
  text { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif; fill: var(--ink); }
  .muted { fill: var(--ink2); }
</style>"""


def bar_path(x: float, y: float, w: float, h: float, r: float = 4) -> str:
    """Bar with a 4px rounded data end (top), square at the baseline."""
    r = min(r, h, w / 2)
    return (f"M{x:.1f},{y + h:.1f} V{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} "
            f"H{x + w - r:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} V{y + h:.1f} Z")


def calibration_figure() -> str:
    d = yaml.safe_load((bc.RESULTS / "corpus_calibration.yaml").read_text())
    actions = ["ACCEPT", "KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "REMOVE"]
    labels = {"ACCEPT": "ACCEPT", "KEEP_AS_NON_CORE": "KEEP_AS_NON_CORE",
              "MARK_AS_OVER_ANNOTATED": "OVER_ANNOTATED", "REMOVE": "REMOVE"}
    W, H = 640, 330
    left, right, top, bottom = 56, 20, 64, 70
    pw, ph = W - left - right, H - top - bottom
    ymax = 0.6
    y = lambda v: top + ph * (1 - v / ymax)  # noqa: E731
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" class="viz" '
           f'role="img" aria-label="Share of annotations whose anatomy is among the gene\'s top Bgee tissues, by reviewer action">',
           STYLE, f'<rect width="{W}" height="{H}" fill="var(--surface)"/>',
           f'<text x="{left}" y="24" font-size="15" font-weight="600">Expression agrees with annotations, but not with reviewers\' verdicts</text>',
           f'<text x="{left}" y="44" font-size="12" class="muted">GO anatomy among the gene\'s top-10% Bgee tissues, '
           f'{d["anatomy_bearing_annotations"]:,} reviewed human annotations</text>']
    for t in (0, 0.2, 0.4, 0.6):
        out.append(f'<line x1="{left}" x2="{W - right}" y1="{y(t):.1f}" y2="{y(t):.1f}" stroke="var(--grid)" stroke-width="1"/>')
        out.append(f'<text x="{left - 8}" y="{y(t) + 4:.1f}" font-size="11" text-anchor="end" class="muted">{int(t * 100)}%</text>')
    slot = pw / len(actions)
    bw = 54
    for i, a in enumerate(actions):
        real = d["by_action"][a]["enriched_given_data"]
        shuf = d["shuffled_by_action"][a]["enriched_given_data"]
        n = d["by_action"][a]["n"]
        cx = left + slot * (i + 0.5)
        x0 = cx - bw / 2
        tip = escape(f"{a}: {real:.0%} enriched (n={n}); shuffled pairs {shuf:.0%}")
        out.append(f'<g><title>{tip}</title><path d="{bar_path(x0, y(real), bw, y(0) - y(real))}" fill="var(--s1)"/>'
                   f'<rect x="{x0 - 10}" y="{y(real) - 20}" width="{bw + 20}" height="{y(0) - y(real) + 20}" fill="transparent"/></g>')
        out.append(f'<line x1="{x0 - 8:.1f}" x2="{x0 + bw + 8:.1f}" y1="{y(shuf):.1f}" y2="{y(shuf):.1f}" '
                   f'stroke="var(--ink)" stroke-width="2" stroke-dasharray="4 3"><title>{escape(f"shuffled: {shuf:.0%}")}</title></line>')
        out.append(f'<text x="{cx:.1f}" y="{y(real) - 8:.1f}" font-size="12" text-anchor="middle" font-weight="600">{real:.0%}</text>')
        out.append(f'<text x="{cx:.1f}" y="{y(0) + 18:.1f}" font-size="11" text-anchor="middle">{labels[a]}</text>')
        out.append(f'<text x="{cx:.1f}" y="{y(0) + 33:.1f}" font-size="10" text-anchor="middle" class="muted">n={n:,}</text>')
    ly = H - 14
    out.append(f'<rect x="{left}" y="{ly - 9}" width="12" height="10" rx="2" fill="var(--s1)"/>')
    out.append(f'<text x="{left + 18}" y="{ly}" font-size="11">real gene–term pairs</text>')
    out.append(f'<line x1="{left + 170}" x2="{left + 194}" y1="{ly - 4}" y2="{ly - 4}" stroke="var(--ink)" stroke-width="2" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{left + 200}" y="{ly}" font-size="11">same terms, random gene (chance)</text>')
    out.append("</svg>")
    return "\n".join(out)


def cerebellum_figure() -> str:
    d = yaml.safe_load((bc.RESULTS / "cerebellum_timing.yaml").read_text())
    declared = d["variants"]["declared"]["genes"]
    territory = d["variants"]["territory"]["genes"]
    bins = [b["bin"] for b in d["bins_dpc"]]
    genes = sorted(declared, key=lambda g: (declared[g]["step_order"] or 0, g))
    short = {1: "1 anlage allocation", 2: "2 germinal zones", 3: "3 Purkinje cells", 4: "4 GCP proliferation",
             5: "5 migration, Bergmann glia", 6: "6 foliation"}
    cw, rh = 74, 24
    left, top = 250, 92
    W = left + cw * len(bins) + 24
    H = top + rh * len(genes) + 80
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" class="viz" '
           f'role="img" aria-label="Cerebellum development module genes by mouse developmental stage">',
           STYLE, f'<rect width="{W}" height="{H}" fill="var(--surface)"/>',
           '<text x="16" y="24" font-size="15" font-weight="600">Cerebellum module: when each gene is expressed where its step acts (mouse, Bgee)</text>',
           '<text x="16" y="44" font-size="12" class="muted">Rows grouped by module step (1 = anlage … 6 = foliation); '
           'stage-resolved present calls for the mouse ortholog</text>']
    for j, b in enumerate(bins):
        out.append(f'<text x="{left + cw * j + cw / 2:.1f}" y="{top - 12}" font-size="11" text-anchor="middle">{b}</text>')
    prev = None
    for i, g in enumerate(genes):
        yy = top + rh * i
        step = short.get(declared[g]["step_order"], str(declared[g]["step_order"]))
        if step != prev:
            if prev is not None:
                out.append(f'<line x1="16" x2="{W - 16}" y1="{yy}" y2="{yy}" stroke="var(--grid)" stroke-width="1"/>')
            out.append(f'<text x="16" y="{yy + 16}" font-size="11" class="muted">{escape(step)}</text>')
            prev = step
        out.append(f'<text x="{left - 12}" y="{yy + 16}" font-size="12" text-anchor="end" font-weight="600">{g}</text>')
        for j, b in enumerate(bins):
            x = left + cw * j
            dv, tv = declared[g]["by_stage"][b], territory[g]["by_stage"][b]
            if dv.startswith("IN_CONTEXT"):
                fill, label = "var(--ord1)", "in the step's declared context: " + dv.split(": ", 1)[1]
            elif tv.startswith("IN_CONTEXT"):
                fill, label = "var(--ord2)", "only in the wider cerebellar territory: " + tv.split(": ", 1)[1]
            else:
                fill, label = None, ("expressed only elsewhere at this stage" if dv == "ELSEWHERE" else "no Bgee call at this stage")
            tip = escape(f"{g}, {b}: {label}")
            if fill:
                out.append(f'<rect x="{x + 2}" y="{yy + 2}" width="{cw - 4}" height="{rh - 4}" rx="4" fill="{fill}"><title>{tip}</title></rect>')
            elif dv == "ELSEWHERE":
                out.append(f'<g><title>{tip}</title><rect x="{x + 2}" y="{yy + 2}" width="{cw - 4}" height="{rh - 4}" fill="transparent"/>'
                           f'<circle cx="{x + cw / 2}" cy="{yy + rh / 2}" r="3" fill="var(--dot)"/></g>')
            else:
                out.append(f'<rect x="{x + 2}" y="{yy + 2}" width="{cw - 4}" height="{rh - 4}" fill="transparent"><title>{tip}</title></rect>')
    ly = top + rh * len(genes) + 30
    rows = [[("var(--ord1)", "rect", "in the step's declared context"),
             ("var(--ord2)", "rect", "only in the wider cerebellar territory")],
            [("var(--dot)", "dot", "expressed only elsewhere"), (None, None, "blank: no Bgee call at that stage")]]
    for r, items in enumerate(rows):
        x, yl = 16, ly + 20 * r
        for fill, kind, text in items:
            if kind == "rect":
                out.append(f'<rect x="{x}" y="{yl - 10}" width="14" height="12" rx="3" fill="{fill}"/>')
                x += 20
            elif kind == "dot":
                out.append(f'<circle cx="{x + 5}" cy="{yl - 4}" r="3" fill="{fill}"/>')
                x += 14
            out.append(f'<text x="{x}" y="{yl}" font-size="11">{text}</text>')
            x += int(6.3 * len(text)) + 28
    out.append("</svg>")
    return "\n".join(out)


def main() -> None:
    (bc.PROJECT / "fig-calibration.svg").write_text(calibration_figure())
    (bc.PROJECT / "fig-cerebellum.svg").write_text(cerebellum_figure())
    print("wrote fig-calibration.svg, fig-cerebellum.svg")


if __name__ == "__main__":
    main()
