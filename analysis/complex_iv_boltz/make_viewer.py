#!/usr/bin/env python3
"""Build project-scoped static browser viewers for the retained BioLM CIF."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
CIF = (
    ROOT
    / "biolm_boltz2_model_c_domains_cu_api_out"
    / "boltz2_biolm_results_0.cif"
)
VIEWER_BASENAME = "complex_iv_cox2_copper_maturation_boltz_viewer.html"
OUT_PATHS = [
    REPO / "projects" / "PROTEIN_COMPLEX_FUNCTIONS" / VIEWER_BASENAME,
    REPO / "pages" / "projects" / "PROTEIN_COMPLEX_FUNCTIONS" / VIEWER_BASENAME,
]


def js_template_string(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")


def main() -> None:
    cif = js_template_string(CIF.read_text(encoding="utf-8"))
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>BioLM Boltz2 COX2/SCO1/SCO2 Viewer</title>
  <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
  <style>
    html, body {{
      height: 100%;
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #1f2933;
      background: #f6f8fa;
    }}
    main {{
      display: grid;
      grid-template-columns: minmax(280px, 370px) 1fr;
      height: 100%;
    }}
    aside {{
      padding: 18px;
      background: #ffffff;
      border-right: 1px solid #d8dee4;
      overflow: auto;
    }}
    h1 {{
      font-size: 18px;
      line-height: 1.25;
      margin: 0 0 12px;
    }}
    h2 {{
      font-size: 13px;
      margin: 20px 0 8px;
      text-transform: uppercase;
      letter-spacing: 0;
      color: #57606a;
    }}
    p, li {{
      font-size: 14px;
      line-height: 1.45;
    }}
    ul {{
      padding-left: 18px;
      margin: 8px 0;
    }}
    button {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 34px;
      margin: 4px 4px 4px 0;
      padding: 0 10px;
      border: 1px solid #afb8c1;
      border-radius: 6px;
      background: #f6f8fa;
      color: #24292f;
      cursor: pointer;
      font-size: 13px;
    }}
    button:hover {{
      background: #eef2f5;
    }}
    .metric {{
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 8px;
      font-size: 14px;
      padding: 4px 0;
      border-bottom: 1px solid #eef2f5;
    }}
    .swatch {{
      display: inline-block;
      width: 11px;
      height: 11px;
      border-radius: 50%;
      margin-right: 7px;
      vertical-align: -1px;
    }}
    #viewer {{
      position: relative;
      min-height: 100%;
    }}
    .warn {{
      border-left: 4px solid #bf8700;
      background: #fff8c5;
      padding: 10px 12px;
      margin: 12px 0;
    }}
    @media (max-width: 820px) {{
      main {{
        grid-template-columns: 1fr;
        grid-template-rows: auto 70vh;
      }}
      aside {{
        border-right: 0;
        border-bottom: 1px solid #d8dee4;
      }}
    }}
  </style>
</head>
<body>
<main>
  <aside>
    <h1>BioLM Boltz2 MT-CO2/SCO1/SCO2 Domain Model</h1>
    <p><a href="../PROTEIN_COMPLEX_FUNCTIONS.html">Back to Protein Complex Functions</a></p>
    <div class="warn">
      <p><strong>Hypothesis-generating only.</strong> This is the best retained Complex IV hosted
      run, but it is not structural evidence for GO curation.</p>
    </div>

    <h2>Confidence</h2>
    <div class="metric"><span>confidence_score</span><strong>0.642</strong></div>
    <div class="metric"><span>ipTM</span><strong>0.389</strong></div>
    <div class="metric"><span>complex pLDDT</span><strong>0.705</strong></div>
    <div class="metric"><span>SCO1:SCO2 pair ipTM</span><strong>0.540</strong></div>
    <div class="metric"><span>MT-CO2:SCO1 pair ipTM</span><strong>0.165</strong></div>
    <div class="metric"><span>MT-CO2:SCO2 pair ipTM</span><strong>0.196</strong></div>

    <h2>Chains</h2>
    <ul>
      <li><span class="swatch" style="background:#2563eb"></span>A: MT-CO2 88-227</li>
      <li><span class="swatch" style="background:#dc2626"></span>B: SCO1 112-301</li>
      <li><span class="swatch" style="background:#16a34a"></span>C: SCO2 79-266</li>
    </ul>

    <h2>Controls</h2>
    <button onclick="setCartoon()">Cartoon</button>
    <button onclick="setSurface()">Surface</button>
    <button onclick="setSticks()">Sticks</button>
    <button onclick="toggleSpin()">Spin</button>
    <button onclick="viewer.zoomTo(); viewer.render();">Fit</button>
  </aside>
  <div id="viewer"></div>
</main>
<script>
const cifData = `{cif}`;
const chainColors = {{
  A: "0x2563eb",
  B: "0xdc2626",
  C: "0x16a34a"
}};
let spinning = false;
const viewer = $3Dmol.createViewer("viewer", {{ backgroundColor: "white" }});
viewer.addModel(cifData, "cif");

function applyStyle(style) {{
  viewer.setStyle({{}}, {{}});
  for (const [chain, color] of Object.entries(chainColors)) {{
    if (style === "cartoon") {{
      viewer.setStyle({{ chain }}, {{ cartoon: {{ color }} }});
    }} else if (style === "surface") {{
      viewer.setStyle({{ chain }}, {{ cartoon: {{ color, opacity: 0.55 }} }});
      viewer.addSurface($3Dmol.SurfaceType.VDW, {{ opacity: 0.35, color }}, {{ chain }});
    }} else {{
      viewer.setStyle({{ chain }}, {{ stick: {{ color, radius: 0.18 }} }});
    }}
  }}
  viewer.zoomTo();
  viewer.render();
}}

function setCartoon() {{
  viewer.removeAllSurfaces();
  applyStyle("cartoon");
}}

function setSurface() {{
  viewer.removeAllSurfaces();
  applyStyle("surface");
}}

function setSticks() {{
  viewer.removeAllSurfaces();
  applyStyle("sticks");
}}

function toggleSpin() {{
  spinning = !spinning;
  viewer.spin(spinning);
}}

setCartoon();
</script>
</body>
</html>
"""
    for out_path in OUT_PATHS:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        print(out_path)


if __name__ == "__main__":
    main()
