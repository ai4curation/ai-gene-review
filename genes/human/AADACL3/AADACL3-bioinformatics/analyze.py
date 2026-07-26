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
from urllib.parse import quote

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent
UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTERPRO = "https://www.ebi.ac.uk/interpro/api"
PROSITE_SER_PATTERN = "https://prosite.expasy.org/PS01174.txt"
ALLIANCE = "https://www.alliancegenome.org/api"

# Which UniProt cross-reference database must carry a WITH/FROM token back to
# the entry it was resolved to. A resolution that the resolved entry does not
# itself corroborate is rejected; see verify_resolution.
TOKEN_XREF_DB: dict[str, str] = {
    "MGI": "MGI",
    "RGD": "RGD",
    "SGD": "SGD",
    "AGI_LocusCode": "Araport",
}
GOA_TSV = HERE.parent / "AADACL3-goa.tsv"

QUERY = "Q5VUY0"

# One page must hold every signature match for a protein; see add_interpro.
MATCH_PAGE_SIZE = 200

# Panel: the human AADAC-family cluster plus the characterised relatives that
# PAINT and InterPro actually used as evidence for AADACL3's annotations.
PANEL: dict[str, str] = {
    "Q5VUY0": "AADACL3 (human, query; uncharacterised)",
    "Q5VUY2": "AADACL4 (human; uncharacterised paralog, same 1p36 cluster)",
    "Q6P093": "AADACL2 (human; secreted family member)",
    "P22760": "AADAC (human; characterised deacetylase/TG lipase, ER membrane)",
    "Q6PIU2": "NCEH1/AADACL1 (human; characterised ester hydrolase)",
    "Q8BLF1": "Nceh1 (mouse; source of AADACL3's ECO:0000250 active sites)",
    "A2A7Z8": "Aadacl3 (mouse; ortholog of the query, curated multi-pass membrane)",
    "Q5NUF3": "HIDH (soybean; source of AADACL3's ECO:0000250 oxyanion motif)",
}

# Residue identities expected at a GDXG-family Ser-Asp-His triad and at the
# HGG oxyanion loop. Used to check, not to assert.
EXPECTED_TRIAD = ("S", "D", "H")

# Signatures whose span and score decide whether an activity inference for
# AADACL3 is subfamily-level (constrains the reaction) or only fold-level
# (constrains the architecture). Reported per panel member for comparison.
TRACKED_SIGNATURES: dict[str, str] = {
    "IPR017157": "Arylacetamide deacetylase (InterPro, subfamily)",
    "PIRSF037251": "Arylacetamide deacetylase (PIRSF member signature)",
    "IPR013094": "Alpha/beta hydrolase fold-3 (InterPro, fold)",
    "IPR050300": "GDXG lipolytic enzyme (InterPro, family)",
}


def format_score(score: float | None) -> str:
    """Render a member-database e-value without making underflow look like an integer."""
    if score is None:
        return ""
    if score == 0:
        return "0.0"
    return f"{score:g}"


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
    signatures: dict[str, list[dict]] = field(default_factory=dict)


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
    matches = get_json(
        f"{INTERPRO}/entry/all/protein/uniprot/{entry.accession}/?page_size={MATCH_PAGE_SIZE}"
    )
    if matches.get("count", 0) == 0:
        raise RuntimeError(f"InterPro returned no signature matches for {entry.accession}")
    # The tracked-signature table reports *absences* as well as matches, so a
    # truncated page would turn a real match into a false negative. Refuse to
    # continue rather than paginate silently.
    if matches["count"] > MATCH_PAGE_SIZE:
        raise RuntimeError(
            f"InterPro reports {matches['count']} signature matches for {entry.accession}, "
            f"more than the single page of {MATCH_PAGE_SIZE} requested; the results would be "
            "truncated and absences could not be trusted. Raise MATCH_PAGE_SIZE or follow the "
            "API's `next` link."
        )
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

        # Keep span + score + representative flag for the signatures that decide
        # whether an activity inference is subfamily-level or merely fold-level.
        if meta["accession"] in TRACKED_SIGNATURES:
            entry.signatures[meta["accession"]] = [
                {
                    "start": fr["start"],
                    "end": fr["end"],
                    "score": loc.get("score"),
                    "representative": loc.get("representative"),
                    "model": loc.get("model"),
                }
                for prot in result["proteins"]
                for loc in prot["entry_protein_locations"]
                for fr in loc["fragments"]
            ]

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


def expected_xref(token: str) -> tuple[str, str]:
    """The (database, id) cross-reference a correct resolution of `token` must carry."""
    prefix, rest = token.split(":", 1)
    if prefix not in TOKEN_XREF_DB:
        raise RuntimeError(
            f"No cross-reference database known for WITH/FROM prefix {prefix!r} "
            f"(token {token!r}); add it to TOKEN_XREF_DB rather than resolving unchecked"
        )
    return TOKEN_XREF_DB[prefix], rest


def verify_resolution(token: str, accession: str) -> None:
    """Reject a resolution the resolved entry does not itself corroborate.

    Mapping a model-organism identifier through a third-party service, or an
    Arabidopsis locus through a gene-name search, can land on the wrong protein.
    The resolved UniProt entry must cross-reference the original token.
    """
    db, ident = expected_xref(token)
    d = get_json(f"{UNIPROT}/{accession}.json?fields=xref_{db.lower()}")
    have = {
        (x["database"], x["id"])
        for x in d.get("uniProtKBCrossReferences", [])
    }
    if (db, ident) not in have:
        raise RuntimeError(
            f"Resolution rejected: {token} was mapped to {accession}, but that entry "
            f"carries no {db} cross-reference {ident} (it has {sorted(have) or 'none'}). "
            "The mapping is wrong, or the cross-reference database has been renamed."
        )


def self_test_resolution_guard() -> None:
    """Prove the resolution guard rejects a deliberately wrong mapping.

    Without this the guard could silently stop working - for instance if UniProt
    renamed a cross-reference database and every lookup began returning nothing,
    which would make the check vacuous rather than loud.
    """
    good, bad = ("MGI:MGI:1915008", "P22760")  # mouse Aadac's id against the HUMAN protein
    try:
        verify_resolution(good, bad)
    except RuntimeError:
        pass
    else:
        raise RuntimeError(
            f"Resolution guard is not working: it accepted {good} -> {bad}, which is wrong "
            "(that is the mouse gene id against the human protein)"
        )
    # and it must accept a correct one, or it would reject everything
    verify_resolution("MGI:MGI:2443191", "Q8BLF1")


def read_iba_sources(term: str, evidence: str) -> list[str]:
    """Read the WITH/FROM tokens for one row of the gene's own GOA table.

    Reading them from the GOA file rather than restating them means the source
    list cannot drift from the record under review.
    """
    if not GOA_TSV.exists():
        raise RuntimeError(
            f"{GOA_TSV} not found; run `just fetch-gene human AADACL3` before this script"
        )
    rows = [ln.split("\t") for ln in GOA_TSV.read_text().splitlines() if ln.strip()]
    header, body = rows[0], rows[1:]
    i_term, i_ev, i_with = (
        header.index("GO TERM"),
        header.index("GO EVIDENCE CODE"),
        header.index("WITH/FROM"),
    )
    hits = [r[i_with] for r in body if r[i_term] == term and r[i_ev] == evidence]
    if len(hits) != 1:
        raise RuntimeError(
            f"Expected exactly one {evidence} row for {term} in {GOA_TSV.name}, found {len(hits)}"
        )
    return [t for t in hits[0].split("|") if t]


def reviewed_only(accessions: list[str]) -> list[str]:
    """Keep the Swiss-Prot entries among a set of accessions, sorted for determinism."""
    keep = []
    for acc in sorted(set(accessions)):
        d = get_json(f"{UNIPROT}/{acc}.json?fields=accession")
        if d.get("entryType", "").startswith("UniProtKB reviewed"):
            keep.append(acc)
    return keep


def resolve_source(token: str) -> dict:
    """Map one GOA WITH/FROM token to a UniProt accession, live and without guessing."""
    out: dict = {"token": token, "accession": None, "note": None}
    if token.startswith("UniProtKB:"):
        out["accession"] = token.split(":", 1)[1]
        out["note"] = "UniProt accession given directly"
        return out
    if token.startswith("PANTHER:"):
        out["note"] = "PANTHER ancestral node, not a protein; no nucleophile to read"
        return out
    if token.startswith("AGI_LocusCode:"):
        locus = token.split(":", 1)[1]
        q = f"(gene:{locus}) AND (taxonomy_id:3702) AND (reviewed:true)"
        d = get_json(f"{UNIPROT}/search?query={quote(q)}&fields=accession&size=10")
        accs = sorted({r["primaryAccession"] for r in d.get("results", [])})
        if len(accs) == 1:
            verify_resolution(token, accs[0])
            out["accession"] = accs[0]
            out["note"] = (
                "resolved via UniProt gene-name search restricted to A. thaliana, reviewed; "
                "confirmed by the entry's own Araport cross-reference"
            )
        else:
            out["note"] = f"UniProt gene-name search returned {len(accs)} reviewed entries: {accs}"
        return out
    # MGI / RGD / SGD: use the Alliance gene record's UniProt cross-references.
    curie = token[4:] if token.startswith("MGI:MGI:") else token
    d = get_json(f"{ALLIANCE}/gene/{curie}")
    gene = d.get("gene", {})
    xrefs = [
        x["referencedCurie"].split(":", 1)[1]
        for x in (gene.get("crossReferences") or [])
        if x.get("referencedCurie", "").startswith("UniProtKB:")
    ]
    symbol = (gene.get("geneSymbol") or {}).get("displayText")
    out["symbol"] = symbol
    if not xrefs:
        out["note"] = "Alliance record carries no UniProtKB cross-reference"
        return out
    reviewed = reviewed_only(xrefs)
    if len(reviewed) == 1:
        verify_resolution(token, reviewed[0])
        out["accession"] = reviewed[0]
        out["note"] = (
            f"resolved via Alliance ({symbol}); one reviewed entry of {len(set(xrefs))}, "
            f"confirmed by the entry's own {expected_xref(token)[0]} cross-reference"
        )
    else:
        out["note"] = (
            f"Alliance ({symbol}) gives {len(set(xrefs))} cross-references, "
            f"{len(reviewed)} of them reviewed: {reviewed}"
        )
    return out


def nucleophile_audit() -> dict:
    """Read the nucleophile residue of every source cited for the hydrolase IBA.

    GO:0017171 serine hydrolase activity is defined by mechanism - a serine
    nucleophile in a triad with an acidic and a basic residue - so it can only be
    placed at a node whose members all have a serine nucleophile. This checks that
    directly instead of assuming it from the family name.
    """
    tokens = read_iba_sources("GO:0016787", "IBA")
    rows = []
    for token in tokens:
        row = resolve_source(token)
        acc = row["accession"]
        if acc:
            d = get_json(f"{UNIPROT}/{acc}.json")
            seq = d["sequence"]["value"]
            sites = sorted(
                f["location"]["start"]["value"]
                for f in d.get("features", [])
                if f["type"] == "Active site"
            )
            row["uniprot_id"] = d["uniProtkbId"]
            row["organism"] = d["organism"]["scientificName"]
            row["n_active_sites"] = len(sites)
            row["nucleophile_position"] = sites[0] if sites else None
            row["nucleophile_residue"] = seq[sites[0] - 1] if sites else None
            row["serine_nucleophile"] = (seq[sites[0] - 1] == "S") if sites else None
        rows.append(row)
    with_sites = [r for r in rows if r.get("nucleophile_residue")]
    return {
        "term_audited": "GO:0016787 (IBA, GO_REF:0000033)",
        "tokens_in_goa": len(tokens),
        "resolved_to_protein": sum(1 for r in rows if r["accession"]),
        "nucleophile_readable": len(with_sites),
        "serine_nucleophile": sum(1 for r in with_sites if r["serine_nucleophile"]),
        "non_serine_nucleophile": [
            f"{r['uniprot_id']} {r['nucleophile_residue']}{r['nucleophile_position']}"
            for r in with_sites
            if not r["serine_nucleophile"]
        ],
        "sources": rows,
    }


def main() -> None:
    self_test_resolution_guard()

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
                    "residue_identical": (e.sequence[tp - 1] == query.sequence[p - 1]) if tp else False,
                    "conserved": (
                        tp in e.act_sites and e.sequence[tp - 1] == query.sequence[p - 1]
                    )
                    if tp
                    else False,
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
        "tracked_signatures": {
            "descriptions": TRACKED_SIGNATURES,
            "per_protein": {acc: e.signatures for acc, e in entries.items()},
        },
        "nucleophile_audit_of_iba_sources": nucleophile_audit(),
    }
    if QUERY not in results["tracked_signatures"]["per_protein"]:
        raise RuntimeError("query missing from tracked-signature table")
    if not entries[QUERY].signatures:
        raise RuntimeError(
            f"No tracked signatures ({', '.join(TRACKED_SIGNATURES)}) matched {QUERY}; "
            "the subfamily-versus-fold comparison cannot be made"
        )

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
        "Global pairwise alignment (BLOSUM62, gap -11/-1). Two different counts are "
        "reported because only the stricter one supports a conservation claim. "
        "\"on annotated site\" counts how many of AADACL3's three active-site residues align "
        "to a position UniProt annotates as an active site in the partner; \"conserved\" "
        "additionally requires the residue to be identical. HIDH shows why the distinction "
        "matters: AADACL3's Ser193 lands on HIDH's annotated site 164, but that residue is a "
        "threonine, so it counts for the first column and not the second."
    )
    L.append("")
    L.append(
        "| partner | % identity to AADACL3 | aligned triad residues | on annotated site | "
        "conserved (same residue too) | aligned oxyanion residues |"
    )
    L.append("|---|---|---|---|---|---|")
    for acc, a in r["pairwise_alignment_to_query"].items():
        res = "/".join(
            f"{t['query_residue']}{t['query_position']}→{t['target_residue'] or '-'}{t['target_position'] or ''}"
            for t in a["triad"]
        )
        n_ann = sum(1 for t in a["triad"] if t["target_annotated_active_site"])
        n_cons = sum(1 for t in a["triad"] if t["conserved"])
        L.append(
            f"| {entries[acc].uniprot_id} ({acc}) | {a['percent_identity']} | {res} | "
            f"{n_ann}/3 | {n_cons}/3 | `{a['oxyanion_target_residues']}` |"
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

    L.append("## 6. Subfamily-level versus fold-level signature assignment")
    L.append("")
    L.append(
        "Which signature carries an activity inference matters more than whether one "
        "matches at all: a fold signature constrains architecture, a subfamily "
        "signature constrains the reaction. Spans are residue ranges on each protein; "
        "score is the member-database e-value where the API reports one (InterPro "
        "entries themselves carry no score). An e-value of `0.0` is the API reporting "
        "underflow below double precision, not a literal zero."
    )
    L.append("")
    for sig, desc in TRACKED_SIGNATURES.items():
        L.append(f"- `{sig}` - {desc}")
    L.append("")
    L.append("| protein | " + " | ".join(TRACKED_SIGNATURES) + " |")
    L.append("|---" * (len(TRACKED_SIGNATURES) + 1) + "|")
    for acc, sigs in r["tracked_signatures"]["per_protein"].items():
        cells = []
        for sig in TRACKED_SIGNATURES:
            hits = sigs.get(sig) or []
            if not hits:
                cells.append("-")
                continue
            cells.append(
                "; ".join(
                    f"{h['start']}-{h['end']}"
                    + (f" ({format_score(h['score'])})" if h.get("score") is not None else "")
                    + (" [representative]" if h.get("representative") else "")
                    for h in hits
                )
            )
        L.append(f"| {entries[acc].uniprot_id} ({acc}) | " + " | ".join(cells) + " |")
    L.append("")

    L.append("## 7. Is the nucleophile a serine in every source cited for the hydrolase IBA?")
    L.append("")
    na = r["nucleophile_audit_of_iba_sources"]
    L.append(
        "GO:0017171 serine hydrolase activity is defined by *mechanism* - a serine "
        "nucleophile activated by a proton relay through an acidic and a basic residue - "
        "so asserting it at a phylogenetic node propagates a serine nucleophile to every "
        "descendant, and a single non-serine member makes a plain transfer unsafe. (It does "
        "not make the term unreachable: PAINT can annotate the ancestral node and mark the "
        "divergent descendant with a NOT.) This reads the residue at each source's first "
        "annotated active site. "
        "WITH/FROM tokens are taken from the gene's own `AADACL3-goa.tsv` so they cannot "
        "drift from the record under review; model-organism identifiers are resolved through "
        "the Alliance API and Arabidopsis loci through UniProt, and anything that cannot be "
        "resolved to a single reviewed entry is reported as unresolved rather than dropped."
    )
    L.append("")
    L.append(
        f"Audited: {na['term_audited']}. {na['tokens_in_goa']} WITH/FROM tokens, "
        f"{na['resolved_to_protein']} resolved to a protein, "
        f"{na['nucleophile_readable']} with a readable nucleophile, of which "
        f"**{na['serine_nucleophile']} are serine**. "
        + (
            "Non-serine: " + ", ".join(na["non_serine_nucleophile"]) + "."
            if na["non_serine_nucleophile"]
            else "No non-serine nucleophile found."
        )
    )
    L.append("")
    L.append("| WITH/FROM token | resolved | nucleophile | serine? | resolution note |")
    L.append("|---|---|---|---|---|")
    for s in na["sources"]:
        nuc = (
            f"{s['nucleophile_residue']}{s['nucleophile_position']}"
            if s.get("nucleophile_residue")
            else "-"
        )
        ser = {True: "yes", False: "**no**", None: "-"}[s.get("serine_nucleophile")]
        L.append(
            f"| `{s['token']}` | {s.get('uniprot_id') or '-'} | {nuc} | {ser} | "
            f"{s.get('note') or '-'} |"
        )
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
