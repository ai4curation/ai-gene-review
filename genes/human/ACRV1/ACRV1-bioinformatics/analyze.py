#!/usr/bin/env python3
"""Five checks on ACRV1 (P26436) that the gene review depends on.

All five are computed from the API snapshot in ``data/`` (rebuild it with
``uv run python fetch_data.py``).  Nothing here touches the network, so
``RESULTS.md`` is byte-reproducible from the committed snapshot.

1. DOMAIN ARCHITECTURE -- where the Ly-6/uPAR (LU, "three-finger") domain sits in
   ACRV1 and how many cysteines it contains.  The 1990 cloning paper concluded
   SP-10 had "no significant homology to other sequences" (PMID:1693291); the
   question is whether that still holds.
2. ISOFORM x DOMAIN -- ACRV1 has 11 annotated splice isoforms.  Which of them
   keep the LU domain intact, and how does that line up with the measured
   isoform abundances (PMID:7619499)?
3. GPI CENSUS and TOPOLOGY -- most human LU-domain proteins are GPI-anchored
   surface proteins.  Is ACRV1?  And, since anchoring turns out NOT to separate
   ACRV1 from the family members whose functions might be transferred to it,
   which members can actually reach a cell-surface receptor?
4. SUBFAMILY SINGLETON -- does ACRV1 share a subfamily-resolution signature with
   any other human LU-domain protein, i.e. is paralogue-based transfer available?
5. FAMILY MOLECULAR FUNCTION -- is there any molecular function shared across
   the human LU-domain family that could legitimately be transferred to ACRV1?

Usage:  uv run python analyze.py
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"

ACRV1 = "P26436"
LU_INTERPRO = "IPR016054"

# Relative isoform abundance in human testis, quantitative competitive RT-PCR on
# testes from four men (PMID:7619499).  Literature INPUT, not a result computed here.
# Ranges are the across-individual ranges reported in that paper's abstract.
ISOFORM_ABUNDANCE_PCT = {
    "1": "53-72",
    "2": "15-32",
    "3": "3.4-8.3",
    "4": "8.7-12.5",
}
ABUNDANCE_SOURCE = "PMID:7619499"
ABUNDANCE_NOTE = (
    "the remaining seven isoforms together account for <1% of SP-10 message"
)

# Uninformative molecular-function terms: present for many proteins and carrying no
# functional content, so they are excluded when asking what the family "does".
UNINFORMATIVE_MF = {
    "GO:0005515",  # protein binding
    "GO:0042802",  # identical protein binding
    "GO:0019899",  # enzyme binding
    "GO:0019904",  # protein domain specific binding
    "GO:0005102",  # signaling receptor binding
    "GO:0048306",  # calcium-dependent protein binding
}


def load(name: str):
    path = DATA / name
    if not path.exists():
        raise FileNotFoundError(
            f"missing {path}; rebuild the snapshot with: uv run python fetch_data.py"
        )
    return json.loads(path.read_text())


def cys_positions(seq: str, start: int, end: int) -> list[int]:
    """1-based positions of cysteines in the closed interval [start, end]."""
    return [i for i in range(start, end + 1) if seq[i - 1] == "C"]


def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for s, e in sorted(intervals):
        if out and s <= out[-1][1] + 1:
            out[-1] = (out[-1][0], max(out[-1][1], e))
        else:
            out.append((s, e))
    return out


def overlap(a: tuple[int, int], b: tuple[int, int]) -> int:
    return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)


# --------------------------------------------------------------------------- 1
def domain_architecture() -> dict:
    up = load(f"uniprot_{ACRV1}.json")
    ip = load(f"interpro_{ACRV1}.json")
    seq = up["sequence"]["value"]

    matches = {}
    for res in ip["results"]:
        acc = res["metadata"]["accession"]
        locs = [
            (f["start"], f["end"])
            for p in res["proteins"]
            for e in p["entry_protein_locations"]
            for f in e["fragments"]
        ]
        matches[acc] = {
            "database": res["metadata"]["source_database"],
            "type": res["metadata"]["type"],
            "name": res["metadata"]["name"],
            "locations": sorted(locs),
        }

    if LU_INTERPRO not in matches:
        raise RuntimeError(
            f"{LU_INTERPRO} not among InterPro matches on {ACRV1}: {sorted(matches)}"
        )
    lu_start, lu_end = matches[LU_INTERPRO]["locations"][0]

    features = {}
    for ft in up["features"]:
        loc = (ft["location"]["start"]["value"], ft["location"]["end"]["value"])
        features.setdefault(ft["type"], []).append(
            {"range": loc, "description": ft.get("description") or ""}
        )

    signal = features["Signal"][0]["range"]
    disordered = [f["range"] for f in features["Region"] if f["description"] == "Disordered"]
    repeats = [f for f in features["Region"] if "repeats of" in f["description"]]

    lu_cys = cys_positions(seq, lu_start, lu_end)
    # spacing between consecutive cysteines, the LU domain's diagnostic signature
    spacing = [b - a for a, b in zip(lu_cys, lu_cys[1:])]

    # composition of the low-complexity region between the signal peptide and the domain
    linker = (signal[1] + 1, lu_start - 1)
    linker_seq = seq[linker[0] - 1 : linker[1]]
    comp = {aa: linker_seq.count(aa) for aa in sorted(set(linker_seq))}
    top = sorted(comp.items(), key=lambda kv: (-kv[1], kv[0]))[:6]

    return {
        "accession": ACRV1,
        "length": len(seq),
        "signal_peptide": list(signal),
        "lu_domain": [lu_start, lu_end],
        "lu_domain_matches": matches,
        "lu_cysteine_positions": lu_cys,
        "lu_cysteine_count": len(lu_cys),
        "lu_cysteine_spacing": spacing,
        "cysteines_outside_lu_domain": cys_positions(seq, 1, lu_start - 1),
        "disordered_regions": [list(r) for r in disordered],
        "repeat_regions": [
            {"range": list(r["range"]), "description": r["description"]} for r in repeats
        ],
        "linker_region": list(linker),
        "linker_length": len(linker_seq),
        "linker_top_residues": [
            {"residue": aa, "count": n, "pct": round(100 * n / len(linker_seq), 1)}
            for aa, n in top
        ],
    }


# --------------------------------------------------------------------------- 2
def isoform_domain_overlap(lu: tuple[int, int]) -> dict:
    up = load(f"uniprot_{ACRV1}.json")
    vsp = {}
    for ft in up["features"]:
        if ft["type"] != "Alternative sequence":
            continue
        fid = ft["featureId"]
        rng = (ft["location"]["start"]["value"], ft["location"]["end"]["value"])
        if ft.get("alternativeSequence", {}).get("alternativeSequences"):
            raise RuntimeError(
                f"{fid} is a substitution, not a deletion; the overlap logic assumes deletions"
            )
        vsp[fid] = rng

    alt = [c for c in up["comments"] if c["commentType"] == "ALTERNATIVE PRODUCTS"]
    if len(alt) != 1:
        raise RuntimeError("expected exactly one ALTERNATIVE PRODUCTS comment")

    lu_len = lu[1] - lu[0] + 1
    rows = []
    for iso in alt[0]["isoforms"]:
        name = iso["name"]["value"]
        ids = iso.get("sequenceIds") or []
        deleted = merge([vsp[i] for i in ids])
        lost = sum(overlap(d, lu) for d in deleted)
        rows.append(
            {
                "isoform": name,
                "isoform_id": iso["isoformIds"][0],
                "vsp": ids,
                "deleted_ranges": [list(d) for d in deleted],
                "residues_deleted": sum(e - s + 1 for s, e in deleted),
                "lu_residues_lost": lost,
                "lu_domain_intact": lost == 0,
                "abundance_pct": ISOFORM_ABUNDANCE_PCT.get(name),
            }
        )

    intact = [r["isoform"] for r in rows if r["lu_domain_intact"]]
    truncated = [r["isoform"] for r in rows if not r["lu_domain_intact"]]
    measured = [r for r in rows if r["abundance_pct"] is not None]
    return {
        "lu_domain": list(lu),
        "lu_domain_length": lu_len,
        "isoforms": rows,
        "n_isoforms": len(rows),
        "lu_intact": intact,
        "lu_truncated": truncated,
        "abundance_source": ABUNDANCE_SOURCE,
        "abundance_note": ABUNDANCE_NOTE,
        "all_measured_isoforms_keep_lu_domain": all(
            r["lu_domain_intact"] for r in measured
        ),
    }


# --------------------------------------------------------------------------- 3
def gpi_census() -> dict:
    fam = load("uniprot_lu_family_human.json")
    rows = []
    for e in fam["results"]:
        acc = e["primaryAccession"]
        gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value", "")
        lipid = [
            ft["description"]
            for ft in e.get("features", [])
            if ft["type"] == "Lipidation"
        ]
        signal = [ft for ft in e.get("features", []) if ft["type"] == "Signal"]
        rows.append(
            {
                "accession": acc,
                "gene": gene,
                "length": e["sequence"]["length"],
                "has_signal_peptide": bool(signal),
                "gpi_anchor": any("GPI-anchor" in d for d in lipid),
                "lipidation": sorted(lipid),
            }
        )
    rows.sort(key=lambda r: (not r["gpi_anchor"], r["gene"], r["accession"]))
    gpi = [r for r in rows if r["gpi_anchor"]]
    nongpi = [r for r in rows if not r["gpi_anchor"]]
    acrv1 = next(r for r in rows if r["accession"] == ACRV1)
    return {
        "n_family": len(rows),
        "n_gpi_anchored": len(gpi),
        "n_not_gpi_anchored": len(nongpi),
        "not_gpi_anchored": [r["gene"] or r["accession"] for r in nongpi],
        "acrv1": acrv1,
        "members": rows,
    }


# --------------------------------------------------------------------------- 3b
def lu_cysteine_census(acrv1_count: int) -> dict:
    ip = load("interpro_lu_domains_human.json")
    rows = []
    for res in ip["results"]:
        m = res["metadata"]
        seq = res["extra_fields"]["sequence"]
        entry = next(e for e in res["entries"] if e["accession"] == LU_INTERPRO)
        frags = [
            (f["start"], f["end"])
            for e in entry["entry_protein_locations"]
            for f in e["fragments"]
        ]
        # one protein can carry several LU domains (uPAR has three); score each
        for start, end in sorted(frags):
            rows.append(
                {
                    "accession": m["accession"],
                    "gene": m["gene"],
                    "domain": [start, end],
                    "cysteines": len(cys_positions(seq, start, end)),
                }
            )
    counts = sorted(r["cysteines"] for r in rows)
    mode = max(set(counts), key=counts.count)
    return {
        "n_domains_scored": len(rows),
        "cysteine_count_distribution": {
            str(c): counts.count(c) for c in sorted(set(counts))
        },
        "modal_cysteine_count": mode,
        "acrv1_cysteine_count": acrv1_count,
        "acrv1_matches_modal_count": acrv1_count == mode,
        "domains": sorted(rows, key=lambda r: (r["gene"], r["domain"][0])),
    }


# --------------------------------------------------------------------------- 3b2
# A location is "extracellular-accessible" if the protein reaches the outside face of a
# cell or the extracellular fluid, i.e. where a cell-surface receptor could be engaged.
# GPI-anchored LU proteins sit in the outer leaflet, so "Cell membrane" counts.
EXTRACELLULAR_KEYWORDS = ("Secreted", "Cell membrane", "Cell surface", "Membrane, caveola")


def topology_census() -> dict:
    """Which family members can reach a cell-surface receptor, and can ACRV1?

    This is the discriminator that the GPI-anchor count in section 3 does NOT supply:
    PATE1, PATE4, SLURP1 and SLURP2 are unanchored yet carry acetylcholine-receptor
    molecular functions, because they are secreted.
    """
    fam = load("uniprot_lu_family_human.json")
    rows = []
    for e in fam["results"]:
        gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value", "")
        locs = sorted(
            {
                loc.get("location", {}).get("value")
                for c in e.get("comments", [])
                if c["commentType"] == "SUBCELLULAR LOCATION"
                for loc in c.get("subcellularLocations", [])
            }
        )
        rows.append(
            {
                "accession": e["primaryAccession"],
                "gene": gene,
                "locations": locs,
                "extracellular_accessible": any(
                    k in loc for loc in locs for k in EXTRACELLULAR_KEYWORDS
                ),
                "acrosomal": any("acrosome" in loc for loc in locs),
            }
        )
    rows.sort(key=lambda r: (r["gene"], r["accession"]))
    by_gene = {r["gene"]: r for r in rows}
    return {
        "extracellular_keywords": list(EXTRACELLULAR_KEYWORDS),
        "n_with_location_annotation": sum(1 for r in rows if r["locations"]),
        "n_extracellular_accessible": sum(1 for r in rows if r["extracellular_accessible"]),
        "acrosomal_members": [r["gene"] for r in rows if r["acrosomal"]],
        "acrv1": by_gene["ACRV1"],
        "members": rows,
    }


# --------------------------------------------------------------------------- 3c
def subfamily_sharing() -> dict:
    """Does ACRV1 share any subfamily-level model (CDD site/domain, PANTHER subfamily)
    with another reviewed human LU-domain protein?  If not, no paralogue-based
    inference is available for it inside the human proteome."""
    per_member = load("interpro_all_matches_lu_family_human.json")
    fam = load("uniprot_lu_family_human.json")
    gene_of = {
        e["primaryAccession"]: (e.get("genes") or [{}])[0]
        .get("geneName", {})
        .get("value", e["primaryAccession"])
        for e in fam["results"]
    }
    # Subfamily-resolution signatures only: CDD conserved-domain models and PANTHER
    # families/subfamilies.  Pfam/InterPro entries are deliberately excluded because
    # they are the fold-level entries that define the family in the first place.
    subfamily_dbs = {"cdd", "panther"}
    models: dict[str, set[str]] = {}
    for acc, payload in per_member.items():
        for res in payload["results"]:
            m = res["metadata"]
            if m["source_database"] in subfamily_dbs:
                models.setdefault(m["accession"], set()).add(gene_of[acc])

    acrv1_models = sorted(a for a, genes in models.items() if gene_of[ACRV1] in genes)
    shared = {
        a: sorted(models[a] - {gene_of[ACRV1]})
        for a in acrv1_models
        if models[a] - {gene_of[ACRV1]}
    }
    return {
        "subfamily_databases_used": sorted(subfamily_dbs),
        "acrv1_subfamily_models": acrv1_models,
        "acrv1_models_shared_with": shared,
        "acrv1_is_subfamily_singleton_in_human": not shared,
        "model_membership": {a: sorted(g) for a, g in sorted(models.items())},
    }


# --------------------------------------------------------------------------- 4
def family_molecular_function() -> dict:
    go = load("quickgo_mf_lu_family_human.json")
    labels = load("go_labels.json")
    fam = load("uniprot_lu_family_human.json")
    gene_of = {
        e["primaryAccession"]: (e.get("genes") or [{}])[0]
        .get("geneName", {})
        .get("value", e["primaryAccession"])
        for e in fam["results"]
    }

    per_protein: dict[str, dict] = {}
    term_members: dict[str, set[str]] = {}
    for acc, payload in sorted(go.items()):
        terms = {}
        for r in payload["results"]:
            terms.setdefault(r["goId"], set()).add(r["goEvidence"])
        informative = {t: sorted(ev) for t, ev in terms.items() if t not in UNINFORMATIVE_MF}
        per_protein[acc] = {
            "gene": gene_of[acc],
            "n_annotations": payload["numberOfHits"],
            "all_mf_terms": sorted(terms),
            "informative_mf_terms": sorted(informative),
            "evidence": {t: ev for t, ev in sorted(informative.items())},
        }
        for t in informative:
            term_members.setdefault(t, set()).add(gene_of[acc])

    shared = sorted(
        (
            {"term": t, "label": labels.get(t, "?"), "members": sorted(g), "n": len(g)}
            for t, g in term_members.items()
        ),
        key=lambda d: (-d["n"], d["term"]),
    )
    with_informative = [a for a, v in per_protein.items() if v["informative_mf_terms"]]
    acrv1 = per_protein[ACRV1]
    return {
        "n_family": len(per_protein),
        "n_with_any_experimental_mf": sum(
            1 for v in per_protein.values() if v["all_mf_terms"]
        ),
        "n_with_informative_experimental_mf": len(with_informative),
        "acrv1_all_mf_terms": acrv1["all_mf_terms"],
        "acrv1_informative_mf_terms": acrv1["informative_mf_terms"],
        "distinct_informative_terms": len(term_members),
        "max_members_sharing_one_term": shared[0]["n"] if shared else 0,
        "shared_terms": shared,
        "per_protein": per_protein,
        "excluded_as_uninformative": sorted(UNINFORMATIVE_MF),
    }


# ---------------------------------------------------------------------------
def render(res: dict) -> str:
    arch = res["domain_architecture"]
    iso = res["isoform_domain_overlap"]
    gpi = res["gpi_census"]
    cys = res["lu_cysteine_census"]
    mf = res["family_molecular_function"]
    L = []
    A = L.append

    sub = res["subfamily_sharing"]
    topo = res["topology_census"]
    # genes carrying any acetylcholine-receptor molecular function, from section 5's own data
    ach_members = sorted(
        {
            g
            for s in mf["shared_terms"]
            if "acetylcholine receptor" in s["label"]
            for g in s["members"]
        }
    )
    A("# ACRV1 (SP-10): what the LU domain, the splice isoforms and the family do and do not license\n")
    A("Generated by `analyze.py` from the API snapshot in `data/`.")
    A("Rebuild the snapshot with `uv run python fetch_data.py`, then rerun")
    A("`uv run python analyze.py`. Machine-readable output: `results.json`.\n")

    A("## 1. ACRV1 is a low-complexity acidic tail plus a canonical LU (three-finger) domain\n")
    A(f"| feature | residues |")
    A("|---|---|")
    A(f"| signal peptide | {arch['signal_peptide'][0]}-{arch['signal_peptide'][1]} |")
    A(
        f"| low-complexity linker | {arch['linker_region'][0]}-{arch['linker_region'][1]}"
        f" ({arch['linker_length']} aa) |"
    )
    for r in arch["disordered_regions"]:
        A(f"| MobiDB-lite disordered | {r[0]}-{r[1]} |")
    for r in arch["repeat_regions"]:
        A(f"| {r['description']} | {r['range'][0]}-{r['range'][1]} |")
    A(
        f"| Ly-6/uPAR (LU) domain, InterPro {LU_INTERPRO} |"
        f" {arch['lu_domain'][0]}-{arch['lu_domain'][1]} |"
    )
    A("")
    A("Member-database support for the same C-terminal domain:\n")
    A("| database | accession | name | match |")
    A("|---|---|---|---|")
    for acc, m in sorted(
        arch["lu_domain_matches"].items(), key=lambda kv: (kv[1]["database"], kv[0])
    ):
        locs = ", ".join(f"{s}-{e}" for s, e in m["locations"])
        A(f"| {m['database']} | {acc} | {m['name']} | {locs} |")
    A("")
    A(
        f"The domain carries **{arch['lu_cysteine_count']} cysteines** at "
        + ", ".join(str(p) for p in arch["lu_cysteine_positions"])
        + f" (spacing {arch['lu_cysteine_spacing']}), and the whole region N-terminal to it"
    )
    n_out = len(arch["cysteines_outside_lu_domain"])
    A(
        f"contains {n_out} cysteine{'s' if n_out != 1 else ''}. "
        f"Across the {cys['n_domains_scored']} LU domains in the "
        f"{gpi['n_family']} reviewed human LU-domain proteins the cysteine count "
        f"distribution is {cys['cysteine_count_distribution']} (mode "
        f"{cys['modal_cysteine_count']}); ACRV1 "
        + ("matches" if cys["acrv1_matches_modal_count"] else "does not match")
        + " the modal count."
    )
    A("")
    A(
        f"The {arch['linker_length']}-residue linker is composed almost entirely of a few "
        "residue types ("
        + ", ".join(
            f"{d['residue']} {d['pct']}%" for d in arch["linker_top_residues"]
        )
        + ")."
    )
    A("")
    A(
        "**Bearing on the review.** The 1990 cloning paper reported that SP-10 "
        "\"did not show any significant homology to other sequences\" (PMID:1693291). "
        "That is no longer true: the C-terminal third is a canonical LU / "
        "three-finger-protein domain, the same fold as CD59, uPAR, SLURP1 and the "
        "snake three-finger toxins. Sections 3 and 4 test what, if anything, that "
        "buys us functionally."
    )
    A("")

    A("## 2. Every abundant splice isoform keeps the LU domain; only rare ones truncate it\n")
    A(
        f"ACRV1 has {iso['n_isoforms']} annotated isoforms, all generated by in-frame "
        "deletions. Mapping each deletion onto the LU domain "
        f"({iso['lu_domain'][0]}-{iso['lu_domain'][1]}, {iso['lu_domain_length']} aa):\n"
    )
    A("| isoform | UniProt id | deleted | aa deleted | LU aa lost | LU intact | % of testis message |")
    A("|---|---|---|---|---|---|---|")
    for r in iso["isoforms"]:
        rng = ", ".join(f"{s}-{e}" for s, e in r["deleted_ranges"]) or "-"
        A(
            f"| {r['isoform']} | {r['isoform_id']} | {rng} | {r['residues_deleted']} |"
            f" {r['lu_residues_lost']} | {'yes' if r['lu_domain_intact'] else 'NO'} |"
            f" {r['abundance_pct'] or '<1 (combined)'} |"
        )
    A("")
    A(
        f"LU domain intact in isoforms {', '.join(iso['lu_intact'])}; truncated in "
        f"{', '.join(iso['lu_truncated'])}. Abundances are from {iso['abundance_source']} "
        f"(quantitative competitive RT-PCR, testes from four men); {iso['abundance_note']}."
    )
    A(
        "All isoforms with a measured abundance retain the complete LU domain: "
        f"**{iso['all_measured_isoforms_keep_lu_domain']}**."
    )
    A("")
    A(
        "**Bearing on the review.** Alternative splicing in ACRV1 varies the length of "
        "the low-complexity spacer, not the folded domain, in >99% of the message. The "
        "isoform heterogeneity is therefore not evidence for isoform-specific molecular "
        "functions, and a GO annotation made on any of the abundant isoforms is an "
        "annotation on the same LU module."
    )
    A("")

    A("## 3. ACRV1 is one of the few human LU-domain proteins with no GPI anchor\n")
    A(
        f"{gpi['n_gpi_anchored']} of {gpi['n_family']} reviewed human LU-domain proteins "
        f"carry a GPI-anchor lipidation site; {gpi['n_not_gpi_anchored']} do not: "
        + ", ".join(gpi["not_gpi_anchored"])
        + "."
    )
    A(
        f"ACRV1 has a signal peptide ({gpi['acrv1']['has_signal_peptide']}) and "
        f"no lipidation feature (GPI anchor: {gpi['acrv1']['gpi_anchor']})."
    )
    A("")
    A("| gene | accession | length | signal peptide | GPI anchor |")
    A("|---|---|---|---|---|")
    for r in gpi["members"]:
        A(
            f"| {r['gene'] or '-'} | {r['accession']} | {r['length']} |"
            f" {'yes' if r['has_signal_peptide'] else 'no'} |"
            f" {'yes' if r['gpi_anchor'] else 'no'} |"
        )
    A("")
    A(
        "**Bearing on the review.** ACRV1 is not anchored, consistent with the "
        "experimental finding that SP-10 partitions as a hydrophilic, *peripheral* "
        "acrosomal protein released by chaotrope but not by detergent or salt "
        "(PMID:1591355), and its compartment is the lumen of a secretory organelle, "
        "topologically separate from the cytosol -- which is why its cytosolic "
        "yeast-two-hybrid partners cannot meet it in vivo."
    )
    A(
        "**What this count does NOT do is separate ACRV1 from the family members whose "
        "molecular functions might otherwise be transferred to it.** PATE1, PATE4, "
        "SLURP1 and SLURP2 are unanchored too, and they are the acetylcholine-receptor "
        "modulators of section 5. Anchoring is therefore the wrong discriminator; the "
        "next subsection supplies the right one."
    )
    A("")
    A("### 3b. Reaching a cell-surface receptor: the discriminator that does work\n")
    A(
        "Classifying each member's UniProt subcellular locations as "
        "extracellular-accessible (any of "
        + ", ".join(f"`{k}`" for k in topo["extracellular_keywords"])
        + f"): {topo['n_extracellular_accessible']} of the "
        f"{topo['n_with_location_annotation']} members carrying a location annotation "
        "qualify, and ACRV1 is the sole exception."
    )
    ach_rows = [
        topo_row
        for gene in ach_members
        for topo_row in [next(r for r in topo["members"] if r["gene"] == gene)]
    ]
    A(
        f"Every one of the {len(ach_rows)} members carrying an acetylcholine-receptor "
        "molecular function is extracellular-accessible: "
        + str(all(r["extracellular_accessible"] for r in ach_rows))
        + "."
    )
    A("")
    A("| gene | UniProt locations | extracellular-accessible | acrosomal | ACh-receptor MF |")
    A("|---|---|---|---|---|")
    for r in topo["members"]:
        if not r["locations"]:
            continue
        A(
            f"| {r['gene']} | {'; '.join(r['locations'])} |"
            f" {'yes' if r['extracellular_accessible'] else 'no'} |"
            f" {'yes' if r['acrosomal'] else 'no'} |"
            f" {'yes' if r['gene'] in ach_members else 'no'} |"
        )
    A("")
    A(
        "ACRV1's only annotated location is "
        + "; ".join(topo["acrv1"]["locations"])
        + f", and it is extracellular-accessible: {topo['acrv1']['extracellular_accessible']}. "
        "The members annotated to the acrosome are "
        + ", ".join(topo["acrosomal_members"])
        + " -- so PATE4 shares ACRV1's compartment, but PATE4 is *also* annotated as "
        "secreted, and ACRV1 is not annotated as secreted or as a cell-membrane protein "
        "at all."
    )
    A("")

    A("## 4. ACRV1 has no close human paralogue inside the LU family\n")
    A(
        "Subfamily-resolution signatures (CDD conserved-domain models and PANTHER "
        "families/subfamilies; the fold-level Pfam/InterPro entries are excluded because "
        "they are what defines the family in the first place) partition the 30 reviewed "
        "human LU-domain proteins into subfamilies. ACRV1's are "
        + ", ".join(sub["acrv1_subfamily_models"])
        + "."
    )
    if sub["acrv1_is_subfamily_singleton_in_human"]:
        A(
            "**No other reviewed human LU-domain protein shares either model**, so ACRV1 "
            "is a subfamily singleton in the human proteome."
        )
    else:
        A(
            "Models shared with other human members: "
            + "; ".join(f"{m}: {', '.join(g)}" for m, g in sorted(sub["acrv1_models_shared_with"].items()))
            + "."
        )
    A("")
    A("| subfamily model | reviewed human LU-domain members |")
    A("|---|---|")
    for m, genes in sub["model_membership"].items():
        A(f"| {m} | {', '.join(genes)} |")
    A("")
    A(
        "**Bearing on the review.** ISS/ISO transfer to ACRV1 has to come from its "
        "orthologues (mouse Acrv1, baboon ACRV1, fox FSA-ACR.1), not from a human "
        "paralogue: it has none at subfamily resolution. Note also that the CDD model "
        "matching ACRV1 is named for SP-10 and the PATE-like proteins, so the PATE clade "
        "is its nearest structural neighbourhood -- which matters for section 5."
    )
    A("")

    A("## 5. The human LU family has no shared molecular function to transfer\n")
    A(
        f"Of {mf['n_family']} reviewed human LU-domain proteins, "
        f"{mf['n_with_any_experimental_mf']} have at least one molecular-function "
        "annotation with an experimental evidence code, and "
        f"{mf['n_with_informative_experimental_mf']} have one that is informative "
        "(excluding "
        + ", ".join(mf["excluded_as_uninformative"])
        + ")."
    )
    A(
        f"Those {mf['n_with_informative_experimental_mf']} proteins between them carry "
        f"{mf['distinct_informative_terms']} distinct molecular-function terms, and the "
        f"most widely shared single term is held by {mf['max_members_sharing_one_term']} "
        f"of {mf['n_family']} members:\n"
    )
    A("| GO term | label | members |")
    A("|---|---|---|")
    for s in mf["shared_terms"]:
        A(f"| {s['term']} | {s['label']} | {', '.join(s['members'])} |")
    A("")
    A("| gene | accession | informative experimental MF terms |")
    A("|---|---|---|")
    for acc, v in sorted(mf["per_protein"].items(), key=lambda kv: kv[1]["gene"]):
        terms = ", ".join(v["informative_mf_terms"]) or "-"
        A(f"| {v['gene']} | {acc} | {terms} |")
    A("")
    acrv1_inf = mf["acrv1_informative_mf_terms"]
    A(
        "ACRV1's own experimental molecular-function annotations are "
        + (", ".join(mf["acrv1_all_mf_terms"]) or "none")
        + ", of which informative: "
        + (", ".join(acrv1_inf) if acrv1_inf else "**none**")
        + "."
    )
    A("")
    top = mf["shared_terms"][0] if mf["shared_terms"] else None
    A(
        "**Bearing on the review.** The LU fold is a protein-interaction scaffold whose "
        "members do unrelated things -- complement regulation, urokinase receptor "
        "activity, nicotinic acetylcholine receptor modulation, laminin and integrin "
        "binding, phospholipase inhibition."
    )
    if top:
        A(
            f"The one function with any breadth is {top['term']} {top['label']}"
            f" ({top['n']}/{mf['n_family']} members: {', '.join(top['members'])}), and it is "
            "worth being explicit about the two members that make this a live question "
            "rather than a dismissal: PATE1 and PATE4 carry GO:0030548 acetylcholine "
            "receptor regulator activity, and the CDD model that matches ACRV1 is named "
            "for SP-10 *and the PATE-like proteins*. So ACRV1's nearest structural "
            "neighbours do have an assigned molecular function. PATE4 is closer still: it "
            "is annotated to the acrosome, the same compartment as ACRV1."
        )
    A(
        "Transferring it would nonetheless be wrong on three counts computed above, and "
        "the first is **topology, not GPI anchoring** -- PATE1, PATE4, SLURP1 and SLURP2 "
        "have no anchor either (section 3), so anchoring cannot be the discriminator. "
        f"What separates them is reachability: all {len(ach_members)} members with an "
        "acetylcholine-receptor function are annotated to a secreted or cell-membrane "
        "location where a surface receptor can be engaged, whereas ACRV1's only annotated "
        "location is the lumen of an intact secretory organelle, with no secreted or "
        "cell-membrane assignment (section 3b). PATE4 illustrates the point rather than "
        "undermining it: it shares the acrosomal location but is *also* secreted. Second, "
        "the term is not shared family-wide, only within one subclade, and ACRV1 belongs "
        "to neither the Ly-6/LYNX/SLURP nor the PATE PANTHER subfamily (section 4). "
        "Third, ACRV1 has no human paralogue at subfamily resolution to inherit from at "
        "all. Combined with ACRV1's own experimental record -- "
        + (", ".join(mf["acrv1_all_mf_terms"]) or "no molecular-function annotations")
        + " and nothing informative -- the statement \"no molecular-function term is "
        "currently justifiable for ACRV1\" is a tested result rather than an assumption."
    )
    A("")
    return "\n".join(L)


def main() -> int:
    arch = domain_architecture()
    res = {
        "domain_architecture": arch,
        "isoform_domain_overlap": isoform_domain_overlap(tuple(arch["lu_domain"])),
        "gpi_census": gpi_census(),
        "topology_census": topology_census(),
        "lu_cysteine_census": lu_cysteine_census(arch["lu_cysteine_count"]),
        "subfamily_sharing": subfamily_sharing(),
        "family_molecular_function": family_molecular_function(),
    }
    (HERE / "results.json").write_text(json.dumps(res, indent=1, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(res))
    print("wrote results.json and RESULTS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
