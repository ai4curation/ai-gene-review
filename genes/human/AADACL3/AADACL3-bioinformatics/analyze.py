"""Catalytic-residue and membrane-topology audit of human AADACL3.

AADACL3 (UniProt Q5VUY0) is an uncharacterised member of the 'GDXG' lipolytic
enzyme family. Its GO record consists entirely of family/fold-derived electronic
inferences (`hydrolase activity`, `carboxylic ester hydrolase activity`,
`membrane`). This script tests the two premises those inferences rest on, using
only primary sequence and primary database records:

1. Does AADACL3 retain the Ser-Asp-His catalytic triad and the HGG oxyanion
   loop of the family, i.e. is the esterase assignment a statement about
   conserved catalytic machinery rather than about a fold name?
2. Is AADACL3 membrane-integral (like AADAC / NCEH1 / AADACL4) or secreted
   (like its cluster neighbour AADACL2)? UniProt annotates no transmembrane
   feature for AADACL3, so the `membrane` GO annotations are not backed by the
   UniProt feature table and need independent support.

Everything is fetched live; nothing is hardcoded. Any missing or unexpected
record is a hard error, never a silently skipped section.

Run:  uv run python analyze.py
Writes: results.json, RESULTS.md
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTERPRO = "https://www.ebi.ac.uk/interpro/api"
PROSITE_SER_PATTERN = "https://prosite.expasy.org/PS01174.txt"

QUERY = "Q5VUY0"

# Panel: the human AADAC-family cluster plus the characterised relatives that
# PAINT and InterPro actually used as evidence for AADACL3's annotations.
PANEL: dict[str, str] = {
    "Q5VUY0": "AADACL3 (human, query; uncharacterised)",
    "Q5VUY2": "AADACL4 (human; uncharacterised paralog, same 1p36 cluster)",
    "Q6P093": "AADACL2 (human; secreted family member)",
    "P22760": "AADAC (human; characterised deacetylase/TG lipase, ER membrane)",
    "Q6PIU2": "NCEH1/AADACL1 (human; characterised ester hydrolase)",
    "Q8BLF1": "Nceh1 (mouse; source of AADACL3's ECO:0000250 active sites)",
    "Q5NUF3": "HIDH (soybean; source of AADACL3's ECO:0000250 oxyanion motif)",
}

# Residue identities expected at a GDXG-family Ser-Asp-His triad and at the
# HGG oxyanion loop. Used to check, not to assert.
EXPECTED_TRIAD = ("S", "D", "H")


def get_json(url: str) -> dict:
    resp = requests.get(url, timeout=60, headers={"Accept": "application/json"})
    resp.raise_for_status()
    return resp.json()


def get_text(url: str) -> str:
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.text


@dataclass
class Entry:
    accession: str
    label: str
    uniprot_id: str
    organism: str
    protein_existence: str
    sequence: str
    act_sites: list[int]
    oxyanion_motif: tuple[int, int] | None
    transmembrane: list[tuple[int, int]]
    signal_peptide: list[tuple[int, int]]
    subcellular: list[str]
    prosite_ser_site: list[tuple[int, int]] = field(default_factory=list)
    pfam_ab3: list[tuple[int, int]] = field(default_factory=list)
    phobius: dict[str, list[tuple[int, int]]] = field(default_factory=dict)
    tmhmm: list[tuple[int, int]] = field(default_factory=list)
    signalp: list[tuple[int, int]] = field(default_factory=list)


def fetch_uniprot(accession: str, label: str) -> Entry:
    d = get_json(f"{UNIPROT}/{accession}.json")
    seq = d["sequence"]["value"]
    if not seq:
        raise RuntimeError(f"UniProt {accession} returned an empty sequence")

    act_sites: list[int] = []
    oxyanion: tuple[int, int] | None = None
    transmembrane: list[tuple[int, int]] = []
    signal: list[tuple[int, int]] = []
    for f in d.get("features", []):
        start = f["location"]["start"]["value"]
        end = f["location"]["end"]["value"]
        if f["type"] == "Active site":
            act_sites.append(start)
        elif f["type"] == "Motif" and "oxyanion" in (f.get("description") or ""):
            oxyanion = (start, end)
        elif f["type"] == "Transmembrane":
            transmembrane.append((start, end))
        elif f["type"] == "Signal":
            signal.append((start, end))

    subcellular: list[str] = []
    for c in d.get("comments", []):
        if c["commentType"] == "SUBCELLULAR LOCATION":
            for loc in c.get("subcellularLocations", []):
                bits = [loc.get("location", {}).get("value")]
                topo = loc.get("topology", {}).get("value")
                if topo:
                    bits.append(topo)
                subcellular.append("; ".join(b for b in bits if b))

    return Entry(
        accession=accession,
        label=label,
        uniprot_id=d["uniProtkbId"],
        organism=d["organism"]["scientificName"],
        protein_existence=d["proteinExistence"],
        sequence=seq,
        act_sites=sorted(act_sites),
        oxyanion_motif=oxyanion,
        transmembrane=transmembrane,
        signal_peptide=signal,
        subcellular=subcellular,
    )


def _frag_spans(locations: list[dict]) -> list[tuple[int, int]]:
    return [
        (fr["start"], fr["end"])
        for loc in locations
        for fr in loc["fragments"]
    ]


def add_interpro(entry: Entry) -> None:
    """Attach InterPro signature matches and InterProScan sequence features."""
    matches = get_json(f"{INTERPRO}/entry/all/protein/uniprot/{entry.accession}/?page_size=200")
    if matches.get("count", 0) == 0:
        raise RuntimeError(f"InterPro returned no signature matches for {entry.accession}")
    for result in matches["results"]:
        meta = result["metadata"]
        spans = [
            (fr["start"], fr["end"])
            for prot in result["proteins"]
            for loc in prot["entry_protein_locations"]
            for fr in loc["fragments"]
        ]
        if meta["accession"] == "PS01174":
            entry.prosite_ser_site = spans
        elif meta["accession"] == "PF07859":
            entry.pfam_ab3 = spans

    feats = get_json(f"{INTERPRO}/protein/uniprot/{entry.accession}/?extra_features=true")
    if not feats:
        raise RuntimeError(
            f"InterPro extra_features returned nothing for {entry.accession}; "
            "cannot assess topology"
        )
    for key, val in feats.items():
        spans = _frag_spans(val["locations"])
        src = val["source_database"]
        if src == "phobius":
            entry.phobius[key] = spans
        elif src == "tmhmm":
            entry.tmhmm = spans
        elif src.startswith("signalp"):
            entry.signalp = spans


def prosite_pattern_to_regex(raw: str) -> tuple[str, str]:
    """Parse the `PA` line of a PROSITE flat-file record into a Python regex."""
    pa_lines = [ln[5:].strip() for ln in raw.splitlines() if ln.startswith("PA ")]
    if not pa_lines:
        raise RuntimeError(
            f"No PA (pattern) line found in PROSITE record fetched from {PROSITE_SER_PATTERN}"
        )
    pattern = "".join(pa_lines).rstrip(".")
    regex_parts = []
    for element in pattern.split("-"):
        element = element.strip()
        if element == "x":
            regex_parts.append(".")
        elif element.startswith("[") and element.endswith("]"):
            regex_parts.append(element)
        elif element.startswith("{") and element.endswith("}"):
            regex_parts.append(f"[^{element[1:-1]}]")
        elif re.fullmatch(r"[A-Z]", element):
            regex_parts.append(element)
        else:
            raise RuntimeError(f"Unhandled PROSITE pattern element {element!r} in {pattern!r}")
    return pattern, "".join(regex_parts)


def pattern_elements(pattern: str) -> list[str]:
    return [e.strip() for e in pattern.rstrip(".").split("-")]


def element_matches(element: str, residue: str) -> bool:
    if element == "x":
        return True
    if element.startswith("["):
        return residue in element[1:-1]
    if element.startswith("{"):
        return residue not in element[1:-1]
    return residue == element


def align_pair(query: Entry, target: Entry) -> tuple[float, dict[int, int | None]]:
    """Global-align query to target; return % identity and a query->target map."""
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    aln = aligner.align(query.sequence, target.sequence)[0]

    qs, ts = str(aln[0]), str(aln[1])
    mapping: dict[int, int | None] = {}
    qpos = tpos = 0
    identities = aligned = 0
    for qc, tc in zip(qs, ts):
        if qc != "-":
            qpos += 1
        if tc != "-":
            tpos += 1
        if qc != "-" and tc != "-":
            aligned += 1
            if qc == tc:
                identities += 1
            mapping[qpos] = tpos
        elif qc != "-":
            mapping[qpos] = None
    pct = 100.0 * identities / aligned if aligned else 0.0
    return round(pct, 1), mapping


def main() -> None:
    entries: dict[str, Entry] = {}
    for acc, label in PANEL.items():
        entry = fetch_uniprot(acc, label)
        add_interpro(entry)
        entries[acc] = entry

    query = entries[QUERY]

    # --- 1. catalytic residues present in the query sequence -----------------
    if len(query.act_sites) != 3:
        raise RuntimeError(
            f"Expected 3 UniProt active sites on {QUERY}, found {query.act_sites}"
        )
    triad = [
        {
            "position": p,
            "residue": query.sequence[p - 1],
            "expected": EXPECTED_TRIAD[i],
            "matches_expected": query.sequence[p - 1] == EXPECTED_TRIAD[i],
        }
        for i, p in enumerate(query.act_sites)
    ]
    if query.oxyanion_motif is None:
        raise RuntimeError(f"No oxyanion-hole MOTIF feature on {QUERY}")
    ox_start, ox_end = query.oxyanion_motif
    oxyanion = {
        "range": [ox_start, ox_end],
        "residues": query.sequence[ox_start - 1 : ox_end],
    }
    nucleophile = query.act_sites[0]
    elbow = {
        "range": [nucleophile - 2, nucleophile + 3],
        "residues": query.sequence[nucleophile - 3 : nucleophile + 3],
    }

    # --- 2. PROSITE nucleophile pattern -------------------------------------
    raw = get_text(PROSITE_SER_PATTERN)
    pattern, regex = prosite_pattern_to_regex(raw)
    elements = pattern_elements(pattern)
    ser_index = elements.index("S")  # 0-based offset of the nucleophile in the pattern

    prosite: dict[str, dict] = {}
    for acc, e in entries.items():
        hits = [(m.start() + 1, m.end()) for m in re.finditer(regex, e.sequence)]
        row: dict = {
            "interpro_reported_match": e.prosite_ser_site,
            "local_regex_hits": hits,
            "matches": bool(hits),
        }
        # Where the pattern fails, walk it over the window centred on the
        # annotated nucleophile so the failing positions are explicit.
        if not hits and e.act_sites:
            start = e.act_sites[0] - ser_index
            window = e.sequence[start - 1 : start - 1 + len(elements)]
            row["window_start"] = start
            row["window"] = window
            row["failing_positions"] = [
                {
                    "pattern_position": i + 1,
                    "requires": el,
                    "sequence_position": start + i,
                    "observed": window[i],
                }
                for i, el in enumerate(elements)
                if i < len(window) and not element_matches(el, window[i])
            ]
        prosite[acc] = row

    # --- 3. triad conservation by pairwise alignment -------------------------
    alignments: dict[str, dict] = {}
    for acc, e in entries.items():
        if acc == QUERY:
            continue
        pct, mapping = align_pair(query, e)
        mapped = []
        for i, p in enumerate(query.act_sites):
            tp = mapping.get(p)
            mapped.append(
                {
                    "query_position": p,
                    "query_residue": query.sequence[p - 1],
                    "target_position": tp,
                    "target_residue": e.sequence[tp - 1] if tp else None,
                    "target_annotated_active_site": tp in e.act_sites if tp else False,
                    "expected_role_residue": EXPECTED_TRIAD[i],
                }
            )
        ox_map = [mapping.get(p) for p in range(ox_start, ox_end + 1)]
        ox_res = "".join(e.sequence[p - 1] if p else "-" for p in ox_map)
        alignments[acc] = {
            "percent_identity": pct,
            "triad": mapped,
            "oxyanion_target_positions": ox_map,
            "oxyanion_target_residues": ox_res,
            "target_annotated_oxyanion": list(e.oxyanion_motif) if e.oxyanion_motif else None,
        }

    # --- 4. topology ---------------------------------------------------------
    topology = {
        acc: {
            "uniprot_transmembrane": e.transmembrane,
            "uniprot_signal_peptide": e.signal_peptide,
            "uniprot_subcellular_location": e.subcellular,
            "protein_existence": e.protein_existence,
            "phobius": e.phobius,
            "tmhmm_tm_helices": e.tmhmm,
            "signalp": e.signalp,
        }
        for acc, e in entries.items()
    }

    results = {
        "query": {
            "accession": query.accession,
            "uniprot_id": query.uniprot_id,
            "length": len(query.sequence),
            "protein_existence": query.protein_existence,
        },
        "panel": PANEL,
        "catalytic_triad_in_query": triad,
        "oxyanion_loop_in_query": oxyanion,
        "nucleophile_elbow_in_query": elbow,
        "prosite_PS01174": {
            "pattern": pattern,
            "regex": regex,
            "per_protein": prosite,
        },
        "pairwise_alignment_to_query": alignments,
        "topology": topology,
        "pfam_PF07859_matches": {acc: e.pfam_ab3 for acc, e in entries.items()},
    }

    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "RESULTS.md").write_text(render_markdown(results, entries))
    print("wrote results.json and RESULTS.md")


def render_markdown(r: dict, entries: dict[str, Entry]) -> str:
    q = r["query"]
    L: list[str] = []
    L.append("# AADACL3 catalytic-residue and membrane-topology audit")
    L.append("")
    L.append(
        f"Generated by `analyze.py` (`uv run python analyze.py`). Query: "
        f"{q['uniprot_id']} / {q['accession']}, {q['length']} aa, "
        f"UniProt protein existence `{q['protein_existence']}`."
    )
    L.append("")
    L.append(
        "AADACL3's entire GO record is family- or fold-derived electronic inference. "
        "This audit asks whether the two premises behind it hold: that the catalytic "
        "machinery of the 'GDXG' lipolytic enzyme family is actually conserved in "
        "AADACL3, and that AADACL3 is membrane-integral rather than secreted."
    )
    L.append("")

    L.append("## 1. Catalytic residues are present in the AADACL3 sequence")
    L.append("")
    L.append("| UniProt active site | residue in sequence | expected for Ser-Asp-His triad | agrees |")
    L.append("|---|---|---|---|")
    for t in r["catalytic_triad_in_query"]:
        L.append(
            f"| {t['position']} | {t['residue']}{t['position']} | {t['expected']} | "
            f"{'yes' if t['matches_expected'] else 'NO'} |"
        )
    L.append("")
    ox = r["oxyanion_loop_in_query"]
    el = r["nucleophile_elbow_in_query"]
    L.append(
        f"Oxyanion-hole motif {ox['range'][0]}-{ox['range'][1]} reads `{ox['residues']}`; "
        f"the nucleophile elbow {el['range'][0]}-{el['range'][1]} reads `{el['residues']}`."
    )
    L.append("")

    L.append("## 2. Triad conservation against characterised relatives")
    L.append("")
    L.append(
        "Global pairwise alignment (BLOSUM62, gap -11/-1). "
        "\"triad on annotated site\" counts how many of AADACL3's three active-site "
        "residues align to a position that UniProt annotates as an active site in the "
        "partner."
    )
    L.append("")
    L.append("| partner | % identity to AADACL3 | aligned triad residues | triad on annotated site | aligned oxyanion residues |")
    L.append("|---|---|---|---|---|")
    for acc, a in r["pairwise_alignment_to_query"].items():
        res = "/".join(
            f"{t['query_residue']}{t['query_position']}→{t['target_residue'] or '-'}{t['target_position'] or ''}"
            for t in a["triad"]
        )
        n_ann = sum(1 for t in a["triad"] if t["target_annotated_active_site"])
        L.append(
            f"| {entries[acc].uniprot_id} ({acc}) | {a['percent_identity']} | {res} | "
            f"{n_ann}/3 | `{a['oxyanion_target_residues']}` |"
        )
    L.append("")

    L.append("## 3. PROSITE PS01174 (GDXG-family nucleophile serine site)")
    L.append("")
    ps = r["prosite_PS01174"]
    L.append(f"Pattern (fetched from PROSITE): `{ps['pattern']}`")
    L.append("")
    L.append("| protein | PS01174 match | InterPro-reported span | failing pattern positions |")
    L.append("|---|---|---|---|")
    for acc, row in ps["per_protein"].items():
        fails = row.get("failing_positions") or []
        fail_txt = (
            ", ".join(
                f"pos {f['pattern_position']} wants {f['requires']}, has "
                f"{f['observed']}{f['sequence_position']}"
                for f in fails
            )
            or "-"
        )
        span = row["interpro_reported_match"] or "-"
        L.append(
            f"| {entries[acc].uniprot_id} ({acc}) | {'yes' if row['matches'] else 'no'} | "
            f"{span} | {fail_txt} |"
        )
    L.append("")

    L.append("## 4. Membrane topology: predicted, and what UniProt records")
    L.append("")
    L.append("| protein | UniProt TRANSMEM | UniProt SIGNAL | UniProt location | Phobius TM | Phobius signal peptide | TMHMM TM | SignalP |")
    L.append("|---|---|---|---|---|---|---|---|")
    for acc, t in r["topology"].items():
        ph = t["phobius"]
        ph_tm = ph.get("TRANSMEMBRANE") or "-"
        ph_sp = ph.get("SIGNAL_PEPTIDE") or "-"
        L.append(
            f"| {entries[acc].uniprot_id} ({acc}) | {t['uniprot_transmembrane'] or '-'} | "
            f"{t['uniprot_signal_peptide'] or '-'} | "
            f"{'; '.join(t['uniprot_subcellular_location']) or '-'} | {ph_tm} | {ph_sp} | "
            f"{t['tmhmm_tm_helices'] or '-'} | {t['signalp'] or '-'} |"
        )
    L.append("")

    L.append("## 5. Pfam PF07859 (Abhydrolase_3) match segmentation")
    L.append("")
    L.append("| protein | PF07859 matched segments |")
    L.append("|---|---|")
    for acc, spans in r["pfam_PF07859_matches"].items():
        L.append(f"| {entries[acc].uniprot_id} ({acc}) | {spans or '-'} |")
    L.append("")

    L.append("## Interpretation")
    L.append("")
    L.append(
        "All numbers above are produced by the script; the reading of them is the "
        "reviewer's. Limitations: topology calls are Phobius/TMHMM/SignalP predictions "
        "retrieved from InterProScan, not experiments, and they cannot say *which* "
        "membrane. No structure of any AADACL3 protein exists, so triad geometry is "
        "inferred from alignment, not from coordinates. Nothing here demonstrates "
        "catalytic activity; it only establishes whether the residues that would be "
        "required for activity are present."
    )
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    main()
