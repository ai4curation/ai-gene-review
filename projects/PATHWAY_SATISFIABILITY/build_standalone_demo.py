#!/usr/bin/env python
"""Generate a self-contained (WASM-ready) marimo notebook from repo sources.

The interactive demo (`demo.py`) imports `ai_gene_review` and reads cache files
from the repo — neither is available in a browser (Pyodide) sandbox. This script
inlines everything the notebook needs so the generated `demo_standalone.py` runs
with **only the standard library** (no `ai_gene_review`, no `yaml`, no file reads):

* the `module_logic` engine, copied verbatim from source (docstring / `__future__`
  / local imports stripped, a tiny `as_list` re-injected);
* the two module documents, pre-parsed from YAML at build time and embedded as
  base64'd JSON (so the notebook needs no YAML parser);
* the GTEx and KEGG cache TSVs, embedded as base64 text.

The result exports to an interactive WebAssembly page
(`marimo export html-wasm`) that runs entirely in the browser and drops into the
GitHub Pages site.

Regenerate:
    uv run python projects/PATHWAY_SATISFIABILITY/build_standalone_demo.py
"""

from __future__ import annotations

import base64
import json
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "modules" / "experimental" / "gluconeogenesis-context" / "cache"
OUT = Path(__file__).parent / "demo_standalone.py"


def clean_engine(src: str) -> str:
    """Strip module docstring, `__future__`, and repo-local imports from the engine."""
    # Remove the leading shebang + module docstring (the first triple-quoted block).
    _head, _docstring, body = src.split('"""', 2)
    keep = []
    skipping_fn = False  # drop compile_module_file (its body needs yaml, which we don't ship)
    for line in body.splitlines():
        stripped = line.strip()
        if line.startswith("def compile_module_file"):
            skipping_fn = True
            continue
        if skipping_fn:
            # stay inside the function until a new top-level (col-0) statement begins
            if line and not line[0].isspace():
                skipping_fn = False
            else:
                continue
        if stripped.startswith("from __future__"):
            continue
        if stripped == "import yaml":  # only used by compile_module_file, now removed
            continue
        if "from ai_gene_review.render_modules import as_list" in line:
            continue
        keep.append(line)
    as_list = (
        "def as_list(value):\n"
        '    """Return a value as a list; None/missing -> []."""\n'
        "    if value is None:\n"
        "        return []\n"
        "    if isinstance(value, list):\n"
        "        return value\n"
        "    return [value]\n"
    )
    return as_list + "\n" + "\n".join(keep).strip() + "\n"


def b64_json(path: Path) -> str:
    """YAML file -> parsed doc -> JSON -> base64 (so the notebook needs no YAML lib)."""
    doc = yaml.safe_load(path.read_text())
    return base64.b64encode(json.dumps(doc).encode()).decode()


def b64_text(path: Path) -> str:
    return base64.b64encode(path.read_text().encode()).decode()


ENGINE = clean_engine((ROOT / "src" / "ai_gene_review" / "module_logic.py").read_text())
GLUCO_B64 = b64_json(ROOT / "modules" / "gluconeogenesis_human.yaml")
MET_B64 = b64_json(ROOT / "modules" / "methionine_biosynthesis.yaml")
GTEX_B64 = b64_text(CACHE / "gtex_medians.tsv")
KEGG_B64 = b64_text(CACHE / "kegg_presence.tsv")

# The one "library" cell: inlined engine + embedded data + resolve helpers.
LIB_BODY = (
    ENGINE
    + "\n\n"
    + f'_GLUCO_B64 = "{GLUCO_B64}"\n'
    + f'_MET_B64 = "{MET_B64}"\n'
    + f'_GTEX_B64 = "{GTEX_B64}"\n'
    + f'_KEGG_B64 = "{KEGG_B64}"\n'
    + textwrap.dedent(
        '''
        import base64 as _b64
        import json as _json

        def _parse_matrix(tsv_text):
            """First column is a key; remaining columns are floats -> {key: {col: float}}."""
            rows = tsv_text.strip().splitlines()
            cols = rows[0].split("\\t")[1:]
            matrix = {}
            for row in rows[1:]:
                cells = row.split("\\t")
                matrix[cells[0]] = {c: float(v) for c, v in zip(cols, cells[1:])}
            return cols, matrix

        gluco_doc = _json.loads(_b64.b64decode(_GLUCO_B64))
        met_doc = _json.loads(_b64.b64decode(_MET_B64))

        gluco_circuit = compile_module(gluco_doc)
        gluco_routes = enumerate_routes(gluco_circuit)
        gluco_gate_atoms = core_atoms(gluco_circuit)
        gluco_gate = [a.gene_symbol for a in gluco_gate_atoms]

        met_circuit = compile_module(met_doc)
        met_routes = enumerate_routes(met_circuit)

        gtex_tissues, gtex_matrix = _parse_matrix(_b64.b64decode(_GTEX_B64).decode())
        kegg_organisms, kegg_matrix = _parse_matrix(_b64.b64decode(_KEGG_B64).decode())

        def resolve_gtex(circuit, routes, gate_atoms, tissues, matrix, thr):
            """Per-tissue: satisfiable? which variants? which gate atom fails?"""
            out = []
            for tissue in tissues:
                def holds(atom, _t=tissue):
                    if not atom.gene_symbol:
                        return True
                    return matrix.get(atom.gene_symbol, {}).get(_t, 0.0) >= thr
                sat = is_satisfied(circuit, holds)
                variants = sorted({
                    g for r in routes if all(holds(a) for a in r)
                    for g in (a.gene_symbol for a in r)
                    if g in {"PCK1", "PCK2", "FBP1", "FBP2"}
                })
                missing = [a.gene_symbol for a in gate_atoms if not holds(a)]
                out.append({
                    "tissue": tissue, "satisfiable": sat,
                    "variants": ", ".join(variants), "gate failure": ", ".join(missing),
                })
            return out

        def reconstruct_genome(circuit, routes, organisms, matrix):
            """GapMind-style: per genome, which encoded route (or which step is a gap)?"""
            out = []
            for org in organisms:
                def holds(atom, _o=org):
                    if not atom.gene_symbol:
                        return True
                    return matrix.get(_o, {}).get(atom.gene_symbol, 0.0) >= 1.0
                sat = is_satisfied(circuit, holds)
                n_routes = sum(1 for r in routes if all(holds(a) for a in r))
                gaps = [step_id(s) for s in unsatisfied_steps(circuit, holds)]
                out.append({
                    "genome": org, "status": "FOUND" if sat else "GAP",
                    "encoded routes": n_routes, "gap steps": ", ".join(gaps),
                })
            return out
        '''
    )
)

RETURN = (
    "    return (\n"
    "        gluco_circuit, gluco_gate, gluco_gate_atoms, gluco_routes,\n"
    "        gtex_tissues, gtex_matrix, resolve_gtex,\n"
    "        met_circuit, met_routes, kegg_organisms, kegg_matrix, reconstruct_genome,\n"
    "    )\n"
)

INTRO_MD = '''\
        # Pathway satisfiability — live, in your browser

        This entire notebook is running **in your browser** via WebAssembly (Pyodide) — no
        server, no install. The satisfiability engine, the module definitions, and the GTEx /
        KEGG data are all embedded. A curation **module** is read as a boolean formula over
        steps; a **context oracle** supplies the truth values. Same engine, different oracle →
        the pathway resolves *into* a context. Move the slider and watch textbook biology fall
        out of the logic.
'''

ROUTES_MD = '''\
        ## 1. Compile the module → boolean circuit

        `gluconeogenesis_human` compiles to **{n_routes} routes** (each a choice of isozymes).
        The **gate** — atoms required by *every* route — is:

        > **{gate}**

        `SLC37A4` + `G6PC1` are the terminal ER glucose-release system. Any tissue that fails to
        express the gate cannot release free glucose, no matter what else it expresses.
'''

NOTICE_MD = '''\
        ---
        **What this demonstrates, live in your browser:** one ~330-line pure-logic engine,
        evaluated against interchangeable oracles, recovers tissue-restricted gluconeogenesis,
        its molecular gate, and microbial pathway completeness — from data, not lookup.

        Source & context: [Methods](methods.md) · [Background](background.md) ·
        [main project page](../PATHWAY_SATISFIABILITY.md).
'''


def cell(body: str, params: str = "") -> str:
    return f"@app.cell\ndef _({params}):\n{body}\n"


NOTEBOOK = (
    "import marimo\n\n"
    '__generated_with = "0.23.13"\n'
    'app = marimo.App(width="medium")\n\n\n'
    # --- generated banner ---
    "# NOTE: generated by build_standalone_demo.py — do not edit by hand.\n"
    "# Regenerate: uv run python projects/PATHWAY_SATISFIABILITY/build_standalone_demo.py\n\n\n"
    # mo import
    + cell("    import marimo as mo\n    return (mo,)")
    + "\n\n"
    # intro md
    + cell(f'    mo.md(\n        r"""\n{INTRO_MD}        """\n    )\n    return', "mo")
    + "\n\n"
    # library cell (engine + data + helpers)
    + "@app.cell\ndef _():\n"
    + textwrap.indent(LIB_BODY.strip("\n"), "    ")
    + "\n"
    + RETURN
    + "\n\n"
    # routes/gate md
    + cell(
        "    mo.md(\n"
        f'        r"""\n{ROUTES_MD}        """.format(\n'
        "            n_routes=len(gluco_routes), gate=\", \".join(gluco_gate)\n"
        "        )\n"
        "    )\n    return",
        "gluco_gate, gluco_routes, mo",
    )
    + "\n\n"
    # slider
    + cell(
        "    threshold = mo.ui.slider(\n"
        '        start=0.5, stop=20.0, step=0.5, value=1.0, label="expression gate — median TPM ≥"\n'
        "    )\n    threshold\n    return (threshold,)",
        "mo",
    )
    + "\n\n"
    # reactive gtex table
    + cell(
        "    _rows = resolve_gtex(\n"
        "        gluco_circuit, gluco_routes, gluco_gate_atoms, gtex_tissues, gtex_matrix, threshold.value\n"
        "    )\n"
        '    _sat = sorted(r["tissue"] for r in _rows if r["satisfiable"])\n'
        '    _expected = {"Liver", "Kidney_Cortex", "Small_Intestine_Terminal_Ileum"}\n'
        "    _recovered = sorted(_expected & set(_sat))\n"
        "    _extra = sorted(set(_sat) - _expected)\n"
        "    _missed = sorted(_expected - set(_sat))\n"
        "    mo.vstack([\n"
        "        mo.md(\n"
        '            f"""\n'
        "            ## 2. Resolve across 54 GTEx tissues (TPM ≥ {threshold.value})\n\n"
        '            **Satisfiable in {len(_sat)} tissue(s):** {", ".join(_sat) or "—"}\n\n'
        '            - textbook set recovered: **{", ".join(_recovered) or "—"}**\n'
        '            - false positives: {", ".join(_extra) or "none"} · missed: {", ".join(_missed) or "none"}\n\n'
        "            *Raise the slider:* tissues drop out **liver → kidney → intestine**, the order of their\n"
        "            known quantitative contribution. Every non-gluconeogenic tissue fails at the **same**\n"
        "            gate atom, `G6PC1`, resisting the ubiquitous paralog `G6PC3`.\n"
        '            """\n'
        "        ),\n"
        "        mo.ui.table(\n"
        '            sorted(_rows, key=lambda r: (not r["satisfiable"], r["tissue"])),\n'
        "            selection=None, pagination=True, page_size=8,\n"
        "        ),\n"
        "    ])\n    return",
        "gluco_circuit, gluco_gate_atoms, gluco_routes, gtex_matrix, gtex_tissues, mo, resolve_gtex, threshold",
    )
    + "\n\n"
    # methionine table
    + cell(
        "    _rows = reconstruct_genome(met_circuit, met_routes, kegg_organisms, kegg_matrix)\n"
        "    mo.vstack([\n"
        "        mo.md(\n"
        '            """\n'
        "            ## 3. Same engine, other kingdom: GapMind-style genome reconstruction\n\n"
        "            Swap the oracle from *expression* to *genome ortholog presence* (KEGG) and the identical\n"
        "            engine reconstructs **L-methionine biosynthesis** per genome — picking the encoded route,\n"
        "            or flagging the missing step as a gap. `cgl` completes via direct sulfhydrylation despite\n"
        "            lacking `metC`; `buc` and the auxotroph `rpr` are flagged as gaps.\n"
        '            """\n'
        "        ),\n"
        "        mo.ui.table(_rows, selection=None),\n"
        "    ])\n    return",
        "kegg_matrix, kegg_organisms, met_circuit, met_routes, mo, reconstruct_genome",
    )
    + "\n\n"
    # epilogue md
    + cell(f'    mo.md(\n        r"""\n{NOTICE_MD}        """\n    )\n    return', "mo")
    + "\n\n"
    'if __name__ == "__main__":\n    app.run()\n'
)


if __name__ == "__main__":
    OUT.write_text(NOTEBOOK)
    kb = len(NOTEBOOK) / 1024
    print(f"wrote {OUT.relative_to(ROOT)} ({kb:.0f} KB); engine {len(ENGINE)} chars, "
          f"no third-party imports in the notebook")
