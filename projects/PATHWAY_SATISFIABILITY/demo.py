import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Pathway satisfiability

        **Is a pathway wired up *here* — in this tissue, this genome?** A pathway is read as a
        logic formula over its steps, and a context — which genes are expressed, or encoded —
        decides which steps are on. Move the slider below: human gluconeogenesis switches on in
        exactly the tissues known to make glucose, and every other tissue fails at the same
        control point. The same logic then reconstructs methionine biosynthesis across microbial
        genomes.
        """
    )
    return


@app.cell
def _():
    from pathlib import Path

    from ai_gene_review.module_logic import (
        compile_module_file,
        core_atoms,
        enumerate_routes,
        is_satisfied,
        iter_atoms,
        step_id,
        unsatisfied_steps,
    )

    def find_repo_root() -> Path:
        """Walk up from the CWD until the committed caches are found."""
        marker = "modules/experimental/gluconeogenesis-context/cache/gtex_medians.tsv"
        for base in [Path.cwd(), *Path.cwd().parents]:
            if (base / marker).exists():
                return base
        raise FileNotFoundError(f"run from inside the repo; could not locate {marker}")

    ROOT = find_repo_root()
    MODULES = ROOT / "modules"
    CACHE = MODULES / "experimental" / "gluconeogenesis-context" / "cache"

    def load_matrix(path: Path) -> tuple[list[str], dict[str, dict[str, float]]]:
        """Parse a TSV whose first column is a key and the rest are float columns."""
        lines = path.read_text().strip().splitlines()
        cols = lines[0].split("\t")[1:]
        matrix: dict[str, dict[str, float]] = {}
        for row in lines[1:]:
            cells = row.split("\t")
            key, values = cells[0], cells[1:]
            matrix[key] = {c: float(v) for c, v in zip(cols, values)}
        return cols, matrix

    def resolve_gtex(circuit, routes, gate_atoms, tissues, matrix, thr):
        """Per-tissue: satisfiable? which variants? which gate atom fails?"""
        rows = []
        for tissue in tissues:
            def holds(atom, _t=tissue):
                if not atom.gene_symbol:
                    return True
                return matrix.get(atom.gene_symbol, {}).get(_t, 0.0) >= thr

            sat = is_satisfied(circuit, holds)
            variants = sorted(
                {
                    g
                    for r in routes
                    if all(holds(a) for a in r)
                    for g in (a.gene_symbol for a in r)
                    if g in {"PCK1", "PCK2", "FBP1", "FBP2"}
                }
            )
            missing = [a.gene_symbol for a in gate_atoms if not holds(a)]
            rows.append(
                {
                    "tissue": tissue,
                    "satisfiable": sat,
                    "variants": ", ".join(variants),
                    "gate failure": ", ".join(missing),
                }
            )
        return rows

    def reconstruct_genome(circuit, routes, organisms, matrix):
        """GapMind-style: per genome, which encoded route (or which step is a gap)?"""
        rows = []
        for org in organisms:
            def holds(atom, _o=org):
                if not atom.gene_symbol:
                    return True
                return matrix.get(_o, {}).get(atom.gene_symbol, 0.0) >= 1.0

            sat = is_satisfied(circuit, holds)
            n_routes = sum(1 for r in routes if all(holds(a) for a in r))
            gaps = [step_id(s) for s in unsatisfied_steps(circuit, holds)]
            rows.append(
                {
                    "genome": org,
                    "status": "FOUND" if sat else "GAP",
                    "encoded routes": n_routes,
                    "gap steps": ", ".join(gaps),
                }
            )
        return rows

    return (
        CACHE,
        MODULES,
        compile_module_file,
        core_atoms,
        enumerate_routes,
        iter_atoms,
        load_matrix,
        reconstruct_genome,
        resolve_gtex,
    )


@app.cell
def _(MODULES, compile_module_file, core_atoms, enumerate_routes):
    gluco_circuit = compile_module_file(MODULES / "gluconeogenesis_human.yaml")
    gluco_routes = enumerate_routes(gluco_circuit)
    gluco_gate_atoms = core_atoms(gluco_circuit)
    gluco_gate = [a.gene_symbol for a in gluco_gate_atoms]
    return gluco_circuit, gluco_gate, gluco_gate_atoms, gluco_routes


@app.cell
def _(gluco_gate, gluco_routes, mo):
    mo.md(
        f"""
        ## The pathway, and its bottleneck

        Human gluconeogenesis can run by **{len(gluco_routes)}** different isozyme combinations —
        but they all funnel through the same required steps:

        > **{", ".join(gluco_gate)}**

        `G6PC1` + `SLC37A4` are the terminal system that releases free glucose. A tissue missing
        this gate can't make glucose, no matter what else it expresses — which is exactly why
        only some tissues are gluconeogenic.
        """
    )
    return


@app.cell
def _(CACHE, load_matrix):
    gtex_tissues, gtex_matrix = load_matrix(CACHE / "gtex_medians.tsv")
    return gtex_matrix, gtex_tissues


@app.cell
def _(mo):
    threshold = mo.ui.slider(
        start=0.5, stop=20.0, step=0.5, value=1.0, label="expression gate — median TPM ≥"
    )
    threshold
    return (threshold,)


@app.cell
def _(
    gluco_circuit,
    gluco_gate_atoms,
    gluco_routes,
    gtex_matrix,
    gtex_tissues,
    mo,
    resolve_gtex,
    threshold,
):
    _rows = resolve_gtex(
        gluco_circuit, gluco_routes, gluco_gate_atoms, gtex_tissues, gtex_matrix, threshold.value
    )
    _sat = sorted(r["tissue"] for r in _rows if r["satisfiable"])
    _expected = {"Liver", "Kidney_Cortex", "Small_Intestine_Terminal_Ileum"}
    _recovered = sorted(_expected & set(_sat))
    _extra = sorted(set(_sat) - _expected)
    _missed = sorted(_expected - set(_sat))

    mo.vstack(
        [
            mo.md(
                f"""
                ## Which tissues can make glucose? (expression ≥ {threshold.value} TPM)

                **Yes, in {len(_sat)} of 54 tissues:** {", ".join(_sat) or "—"}

                - matches the textbook set: **{", ".join(_recovered) or "—"}**
                - false positives: {", ".join(_extra) or "none"} · missed: {", ".join(_missed) or "none"}

                *Raise the slider:* tissues drop out in the order **liver → kidney → intestine**
                — the same order as their real contribution to blood glucose. Every other tissue
                fails at the **same** step, `G6PC1`, and the near-ubiquitous look-alike `G6PC3`
                is correctly not accepted for it.
                """
            ),
            mo.ui.table(
                sorted(_rows, key=lambda r: (not r["satisfiable"], r["tissue"])),
                selection=None,
                pagination=True,
                page_size=8,
            ),
        ]
    )
    return


@app.cell
def _(
    MODULES,
    compile_module_file,
    enumerate_routes,
    load_matrix,
    mo,
    reconstruct_genome,
):
    _met = compile_module_file(MODULES / "methionine_biosynthesis.yaml")
    _routes = enumerate_routes(_met)
    _orgs, _kegg = load_matrix(
        MODULES / "experimental" / "gluconeogenesis-context" / "cache" / "kegg_presence.tsv"
    )
    # kegg_presence.tsv is organism-per-row; transpose the loader's view.
    _lines = (
        MODULES / "experimental" / "gluconeogenesis-context" / "cache" / "kegg_presence.tsv"
    ).read_text().strip().splitlines()
    _kos = _lines[0].split("\t")[1:]
    _by_org = {
        row.split("\t")[0]: {k: float(v) for k, v in zip(_kos, row.split("\t")[1:])}
        for row in _lines[1:]
    }
    _rows = reconstruct_genome(_met, _routes, list(_by_org), _by_org)

    mo.vstack(
        [
            mo.md(
                """
                ## The same idea across microbial genomes

                Now the context is *which genes a genome encodes* instead of expression. The same
                logic reconstructs **methionine biosynthesis** per organism — picking the route
                each one actually uses, or flagging the missing step. `C. glutamicum` (cgl) still
                completes through an alternative branch despite lacking `metC`; `Buchnera` (buc)
                and `Rickettsia` (rpr, a known methionine auxotroph) come up short.
                """
            ),
            mo.ui.table(_rows, selection=None),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        **One idea, many contexts.** The same step-logic finds which tissues run gluconeogenesis
        and the molecular gate that restricts them, then reconstructs microbial methionine
        biosynthesis — all read off data, not looked up. And when a pathway is known to run but a
        step has no candidate, that gap becomes a specific, gene-localised hypothesis to chase.

        See [Methods & reproduction](methods.md) for the API and the module-YAML shape, and
        [Background](background.md) for how this relates to GapMind, Pathway Tools, and IMG.
        """
    )
    return


if __name__ == "__main__":
    app.run()
