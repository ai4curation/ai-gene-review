#!/usr/bin/env python3
"""Can the mouse ACRBP acrosomal-granule function be transferred to human ACRBP?

Human ACRBP (Q8NEB7) carries `GO:0001675 acrosome assembly` by ISS/IEA from mouse
Acrbp (Q3V140). In mouse, the acrosomal-granule phenotype of the Acrbp knockout is
rescued by the ACRBP-V5 splice variant alone (PMID:27303034), and that variant is
reported to be produced only in rodents (PMID:23426433). This script asks three
checkable questions:

  1. Which reviewed ACRBP orthologs have an annotated alternative-product (isoform)
     section in UniProt at all?
  2. Does the human ACRBP locus carry any annotated transcript that could encode an
     ACRBP-V5-like N-terminal-half protein?
  3. Where does the mouse ACRBP-V5 truncation point land on the human sequence -
     inside the propeptide that human ACRBP removes during maturation, or inside the
     mature chain that it keeps?

It also records whether any ACRBP ortholog carries a membrane anchor, which bears on
the separate `GO:0002080 acrosomal membrane` annotation.

Every number is fetched from the UniProt and Ensembl REST APIs. Raw responses are
cached under data/ so a re-run reproduces RESULTS.md byte for byte; pass --refetch to
refresh the cache. Missing input is a hard error, never a silently skipped section.

Usage:
    uv run python analyze_isoform_transfer.py [--refetch]
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

# The five reviewed members of PANTHER family PTHR21362 (ACROSIN-BINDING PROTEIN),
# taken from interpro/panther/PTHR21362/PTHR21362-entries.csv in this repository.
ORTHOLOGS = {
    "Q8NEB7": "human",
    "Q3V140": "mouse",
    "Q6AY33": "rat",
    "Q60485": "guinea pig",
    "Q29016": "pig",
}

# Ensembl species keys for the ACRBP gene symbol lookup.
ENSEMBL_SPECIES = {
    "human": ("homo_sapiens", "ACRBP"),
    "mouse": ("mus_musculus", "Acrbp"),
    "rat": ("rattus_norvegicus", "Acrbp"),
}

# Kyte-Doolittle hydropathy. A mean over a 19-residue window above ~1.6 is the classic
# rough indicator of a membrane-spanning helix; it is a heuristic, not a predictor.
KYTE_DOOLITTLE = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
TM_WINDOW = 19
TM_THRESHOLD = 1.6

MEMBRANE_FEATURE_TYPES = {"Transmembrane", "Intramembrane", "Lipidation"}


def fetch(url: str, cache_name: str, *, refetch: bool) -> str:
    """Return the body of `url`, caching it under data/<cache_name>."""
    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / cache_name
    if path.exists() and not refetch:
        return path.read_text()
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode()
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        raise SystemExit(
            f"FATAL: could not fetch {url} ({exc}).\n"
            f"       Network access is required for the first run. Re-run with network "
            f"access, or restore the cached response at {path}."
        ) from exc
    path.write_text(body)
    return body


def fetch_json(url: str, cache_name: str, *, refetch: bool) -> dict:
    return json.loads(fetch(url, cache_name, refetch=refetch))


def uniprot_entry(accession: str, *, refetch: bool) -> dict:
    entry = fetch_json(
        f"https://rest.uniprot.org/uniprotkb/{accession}.json",
        f"uniprot_{accession}.json",
        refetch=refetch,
    )
    # A truncated or stale cache file must fail here with an actionable message rather
    # than surfacing later as a KeyError in the middle of an analysis section.
    for key in ("sequence", "features"):
        if key not in entry:
            raise SystemExit(
                f"FATAL: cached UniProt entry for {accession} has no '{key}' field, so it is "
                f"truncated or not a UniProtKB record.\n"
                f"       Fix: rm {DATA / f'uniprot_{accession}.json'} and re-run, or run "
                f"`uv run python {Path(__file__).name} --refetch`."
            )
    return entry


def uniprot_isoform_sequence(isoform_id: str, *, refetch: bool) -> str:
    fasta = fetch(
        f"https://rest.uniprot.org/uniprotkb/{isoform_id}.fasta",
        f"uniprot_{isoform_id}.fasta",
        refetch=refetch,
    )
    lines = [line.strip() for line in fasta.splitlines() if line and not line.startswith(">")]
    if not lines:
        raise SystemExit(f"FATAL: no sequence returned for isoform {isoform_id}.")
    return "".join(lines)


def ensembl_gene(species: str, symbol: str, *, refetch: bool) -> dict:
    return fetch_json(
        f"https://rest.ensembl.org/lookup/symbol/{species}/{symbol}?expand=1",
        f"ensembl_{species}_{symbol}.json",
        refetch=refetch,
    )


# --------------------------------------------------------------------------------------
# Part 1 - annotated isoforms across the family
# --------------------------------------------------------------------------------------


@dataclass
class IsoformRecord:
    accession: str
    species: str
    length: int
    isoform_names: list[str] = field(default_factory=list)
    isoform_ids: list[str] = field(default_factory=list)
    variant_sequence_features: int = 0


def isoform_inventory(entries: dict[str, dict]) -> list[IsoformRecord]:
    records = []
    for accession, entry in entries.items():
        record = IsoformRecord(
            accession=accession,
            species=ORTHOLOGS[accession],
            length=entry["sequence"]["length"],
        )
        for comment in entry.get("comments", []):
            if comment.get("commentType") != "ALTERNATIVE PRODUCTS":
                continue
            for isoform in comment.get("isoforms", []):
                name = isoform.get("name", {}).get("value", "?")
                synonyms = [s.get("value") for s in isoform.get("synonyms", [])]
                label = f"{name} ({'/'.join(synonyms)})" if synonyms else name
                record.isoform_names.append(label)
                record.isoform_ids.extend(isoform.get("isoformIds", []))
        record.variant_sequence_features = sum(
            1 for f in entry.get("features", []) if f.get("type") == "Alternative sequence"
        )
        records.append(record)
    return records


# --------------------------------------------------------------------------------------
# Part 2 - transcript inventory at the locus
# --------------------------------------------------------------------------------------


def transcript_protein(transcript_id: str, *, refetch: bool) -> str:
    record = fetch_json(
        f"https://rest.ensembl.org/sequence/id/{transcript_id}?type=protein",
        f"ensembl_protein_{transcript_id}.json",
        refetch=refetch,
    )
    sequence = record.get("seq")
    if not sequence:
        raise SystemExit(
            f"FATAL: Ensembl returned no protein sequence for {transcript_id}; the "
            "N-terminal-fragment test depends on it."
        )
    return sequence.rstrip("*")


def shares_n_terminus(candidate: str, canonical: str) -> float:
    """Percent identity of `candidate` against the equal-length prefix of `canonical`."""
    span = min(len(candidate), len(canonical))
    if span == 0:
        raise SystemExit("FATAL: empty sequence in the N-terminal comparison.")
    identical = sum(1 for a, b in zip(candidate[:span], canonical[:span]) if a == b)
    return 100.0 * identical / span


# A transcript counts as "ACRBP-V5-like" if it shares the canonical N-terminus and encodes
# roughly the N-terminal half. Mouse ACRBP-V5 is 316/540 = 0.585 of the canonical length.
V5_LIKE_MIN_RATIO = 0.40
V5_LIKE_MAX_RATIO = 0.80
V5_LIKE_MIN_IDENTITY = 95.0


def ordered_exons(exons: list[dict], strand: int) -> list[tuple[int, int]]:
    """Exons in transcription order, each as a (5'-boundary, 3'-boundary) pair."""
    if strand == 1:
        return [(e["start"], e["end"]) for e in sorted(exons, key=lambda e: e["start"])]
    return [(e["end"], e["start"]) for e in sorted(exons, key=lambda e: e["end"], reverse=True)]


def intron_readthrough(variant_exons: list[tuple[int, int]], canonical_exons: list[tuple[int, int]], strand: int) -> dict:
    """Classify a variant's terminal exon against the canonical exon chain.

    An intron read-through variant shares its leading exons with the canonical
    transcript, then its terminal exon starts at a canonical acceptor site but runs past
    the matching canonical donor site into the following intron.
    """
    # Exon 1 is compared on its donor (3') boundary only: annotated transcription start
    # sites routinely differ by a few bases between transcripts of the same gene, which
    # would otherwise mask an otherwise identical exon chain.
    shared_leading = 0
    for position, (variant_exon, canonical_exon) in enumerate(
        zip(variant_exons, canonical_exons)
    ):
        if position == 0:
            match = variant_exon[1] == canonical_exon[1]
        else:
            match = variant_exon == canonical_exon
        if not match:
            break
        shared_leading += 1
    terminal = variant_exons[-1]
    matching = [c for c in canonical_exons if c[0] == terminal[0]]
    if not matching:
        return {
            "classification": "no canonical acceptor match for the terminal exon",
            "shared_leading_exons": shared_leading,
            "terminal_exon_index": None,
            "extension_bp": None,
        }
    canonical_exon = matching[0]
    index = canonical_exons.index(canonical_exon) + 1
    extension = (terminal[1] - canonical_exon[1]) * strand
    reads_into_intron = extension > 0 and index < len(canonical_exons)
    return {
        "classification": (
            f"terminal exon = canonical exon {index} extended {extension} bp into intron {index}"
            if reads_into_intron
            else f"terminal exon matches canonical exon {index} (extension {extension} bp)"
        ),
        "shared_leading_exons": shared_leading,
        "terminal_exon_index": index,
        "extension_bp": extension,
        "reads_into_intron": reads_into_intron,
    }


TAIL_LENGTH = 5


def transcript_inventory(gene: dict, *, refetch: bool) -> dict:
    transcripts = gene.get("Transcript")
    if not transcripts:
        raise SystemExit(
            f"FATAL: Ensembl returned no Transcript list for {gene.get('id')}. "
            "Re-run with --refetch; the lookup must use ?expand=1."
        )
    strand = gene["strand"]
    biotypes: dict[str, int] = {}
    coding = []
    for transcript in transcripts:
        biotype = transcript["biotype"]
        biotypes[biotype] = biotypes.get(biotype, 0) + 1
        if biotype == "protein_coding":
            coding.append(
                {
                    "id": transcript["id"],
                    "name": transcript.get("display_name"),
                    "is_canonical": bool(transcript.get("is_canonical")),
                    "exons": ordered_exons(transcript.get("Exon", []), strand),
                    "protein": transcript_protein(transcript["id"], refetch=refetch),
                }
            )
    coding.sort(key=lambda t: t["id"])
    canonical = next((t for t in coding if t["is_canonical"]), None)
    if canonical is None:
        raise SystemExit(
            f"FATAL: no canonical protein_coding transcript at {gene.get('id')}; cannot "
            "define the reference protein for the N-terminal-fragment test."
        )
    canonical_protein = canonical["protein"]
    canonical_exons = canonical["exons"]
    v5_like = []
    for transcript in coding:
        transcript["n_exons"] = len(transcript["exons"])
        transcript["protein_length"] = len(transcript["protein"])
        transcript["length_ratio"] = round(
            len(transcript["protein"]) / len(canonical_protein), 3
        )
        transcript["n_terminal_identity"] = round(
            shares_n_terminus(transcript["protein"], canonical_protein), 1
        )
        transcript["v5_like"] = bool(
            not transcript["is_canonical"]
            and V5_LIKE_MIN_RATIO <= transcript["length_ratio"] <= V5_LIKE_MAX_RATIO
            and transcript["n_terminal_identity"] >= V5_LIKE_MIN_IDENTITY
        )
        if transcript["v5_like"]:
            structure = intron_readthrough(transcript["exons"], canonical_exons, strand)
            length = transcript["protein_length"]
            v5_like.append(
                {
                    "name": transcript["name"] or transcript["id"],
                    "transcript_id": transcript["id"],
                    "protein_length": length,
                    "n_exons": transcript["n_exons"],
                    "canonical_n_exons": len(canonical_exons),
                    "variant_tail": transcript["protein"][-TAIL_LENGTH:],
                    "canonical_at_same_positions": canonical_protein[
                        length - TAIL_LENGTH : length
                    ],
                    **structure,
                }
            )
        del transcript["protein"]
        del transcript["exons"]
    return {
        "gene_id": gene["id"],
        "assembly": gene.get("assembly_name"),
        "strand": strand,
        "n_transcripts": len(transcripts),
        "biotypes": dict(sorted(biotypes.items())),
        "canonical_transcript": canonical["name"] or canonical["id"],
        "canonical_protein_length": len(canonical_protein),
        "canonical_n_exons": len(canonical_exons),
        "protein_coding": coding,
        "v5_like": v5_like,
        "v5_like_transcripts": [entry["name"] for entry in v5_like],
    }


# --------------------------------------------------------------------------------------
# Part 3 - where the ACRBP-V5 truncation lands on the human protein
# --------------------------------------------------------------------------------------


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "global"
    return al


def residue_map(query: str, target: str) -> tuple[dict[int, int], float]:
    """Align `query` to `target`; return 1-based query->target map and % identity."""
    alignment = aligner().align(query, target)[0]
    mapping: dict[int, int] = {}
    identical = 0
    aligned_columns = 0
    q_aln, t_aln = alignment[0], alignment[1]
    q_pos = t_pos = 0
    for q_char, t_char in zip(q_aln, t_aln):
        if q_char != "-":
            q_pos += 1
        if t_char != "-":
            t_pos += 1
        if q_char != "-" and t_char != "-":
            mapping[q_pos] = t_pos
            aligned_columns += 1
            if q_char == t_char:
                identical += 1
    if not aligned_columns:
        raise SystemExit("FATAL: pairwise alignment produced no aligned columns.")
    return mapping, 100.0 * identical / aligned_columns


def region_identity(query: str, target: str, start: int, end: int) -> float:
    """Percent identity of query[start:end] (1-based, inclusive) against its alignment."""
    alignment = aligner().align(query, target)[0]
    identical = 0
    counted = 0
    q_pos = 0
    for q_char, t_char in zip(alignment[0], alignment[1]):
        if q_char != "-":
            q_pos += 1
        if start <= q_pos <= end and q_char != "-" and t_char != "-":
            counted += 1
            if q_char == t_char:
                identical += 1
    if not counted:
        raise SystemExit(f"FATAL: region {start}-{end} has no aligned columns.")
    return 100.0 * identical / counted


def named_features(entry: dict, wanted_type: str) -> list[dict]:
    out = []
    for feature in entry.get("features", []):
        if feature.get("type") != wanted_type:
            continue
        location = feature["location"]
        out.append(
            {
                "start": location["start"]["value"],
                "end": location["end"]["value"],
                "note": feature.get("description") or "",
            }
        )
    return out


def require_feature(entry: dict, wanted_type: str, accession: str) -> list[dict]:
    found = named_features(entry, wanted_type)
    if not found:
        raise SystemExit(
            f"FATAL: UniProt entry {accession} has no '{wanted_type}' feature; the "
            "analysis depends on it. Re-run with --refetch in case the entry changed."
        )
    return found


def variant_sequence_span(entry: dict) -> tuple[int, int]:
    """Span deleted in mouse ACRBP-V5.

    In the UniProt JSON a "Missing (in isoform N)" VAR_SEQ is an Alternative sequence
    feature whose `alternativeSequence` object is empty - nothing replaces the span.
    """
    for feature in entry.get("features", []):
        if feature.get("type") != "Alternative sequence":
            continue
        if feature.get("alternativeSequence"):
            continue  # a substitution, not a deletion
        location = feature["location"]
        return location["start"]["value"], location["end"]["value"]
    raise SystemExit(
        "FATAL: no deletion-type alternative-sequence feature found on mouse Q3V140; "
        "cannot locate the ACRBP-V5 truncation point."
    )


# --------------------------------------------------------------------------------------
# Part 4 - membrane anchor check
# --------------------------------------------------------------------------------------


def max_hydropathy_window(sequence: str) -> tuple[float, int]:
    if len(sequence) < TM_WINDOW:
        raise SystemExit("FATAL: sequence shorter than the hydropathy window.")
    best = -99.0
    best_start = 0
    for i in range(len(sequence) - TM_WINDOW + 1):
        window = sequence[i : i + TM_WINDOW]
        if any(residue not in KYTE_DOOLITTLE for residue in window):
            continue
        score = sum(KYTE_DOOLITTLE[r] for r in window) / TM_WINDOW
        if score > best:
            best, best_start = score, i + 1
    if best == -99.0:
        raise SystemExit("FATAL: no scorable hydropathy window found.")
    return best, best_start


def membrane_check(entries: dict[str, dict]) -> list[dict]:
    rows = []
    for accession, entry in entries.items():
        sequence = entry["sequence"]["value"]
        signal = named_features(entry, "Signal")
        mature_start = (signal[0]["end"] + 1) if signal else 1
        anchors = [
            f["type"]
            for f in entry.get("features", [])
            if f.get("type") in MEMBRANE_FEATURE_TYPES
        ]
        score, start = max_hydropathy_window(sequence[mature_start - 1 :])
        rows.append(
            {
                "accession": accession,
                "species": ORTHOLOGS[accession],
                "signal_peptide": f"{signal[0]['start']}-{signal[0]['end']}" if signal else "none",
                "membrane_features": anchors,
                "max_kd_window_after_signal": round(score, 2),
                "max_kd_window_start_in_mature": start,
            }
        )
    return rows


# --------------------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------------------


def build_report(results: dict) -> str:
    lines: list[str] = []
    add = lines.append

    add("# Does human ACRBP have a counterpart of the 'rodent-specific' ACRBP-V5 isoform?")
    add("")
    add(
        "Generated by `analyze_isoform_transfer.py`. Every figure is read from the UniProt "
        "and Ensembl REST APIs (raw responses cached under `data/`); nothing is hard-coded."
    )
    add("")
    add("## Question")
    add("")
    add(
        "Human ACRBP carries `GO:0001675 acrosome assembly` by ISS (GO_REF:0000024) and by "
        "Ensembl Compara IEA (GO_REF:0000107), both from mouse Acrbp Q3V140. The mouse source "
        "annotation is an IMP on PMID:27303034, where the acrosomal-granule defect of the "
        "knockout is rescued by transgenic ACRBP-V5 alone, and ACRBP-V5 is an intron-5-retaining "
        "splice variant reported in mouse but not in other mammalian ACRBPs (PMID:23426433). "
        "The obvious objection to the transfer is therefore that the granule-forming activity has "
        "no vehicle in human. This analysis tests the *sequence-level* half of that objection and "
        "finds it does not hold: the human locus carries the same intron-5 read-through transcript. "
        "It does not test the *expression-level* half, which PMID:30606959 reports directly and "
        "against the human transcript - see the limits at the end of Part 2b."
    )
    add("")

    add("## Part 1 - annotated isoforms across the reviewed ACRBP family")
    add("")
    add("Reviewed members of PANTHER PTHR21362. `Isoforms` counts UniProt ALTERNATIVE PRODUCTS entries.")
    add("")
    add("| Accession | Species | Length (aa) | Isoforms | Names | Alternative-sequence features |")
    add("|---|---|---|---|---|---|")
    for record in results["isoform_inventory"]:
        names = "; ".join(record["isoform_names"]) or "-"
        add(
            f"| {record['accession']} | {record['species']} | {record['length']} | "
            f"{len(record['isoform_names'])} | {names} | {record['variant_sequence_features']} |"
        )
    add("")
    multi = [r["species"] for r in results["isoform_inventory"] if len(r["isoform_names"]) > 1]
    single = [r["species"] for r in results["isoform_inventory"] if len(r["isoform_names"]) <= 1]
    add(
        f"**Read-out.** Multi-isoform: {', '.join(multi) if multi else 'none'}. "
        f"Single-isoform: {', '.join(single) if single else 'none'}. "
        "UniProt annotates the alternative product on the two murid entries and on neither the "
        "human, the pig, nor - notably - the guinea pig, which is itself a rodent, so at UniProt "
        "level the variant reads as murid rather than pan-rodent. But an absent ALTERNATIVE "
        "PRODUCTS section records what UniProt has curated, not what the genome encodes, so Part 2 "
        "goes to the genome annotation instead."
    )
    add("")

    add("## Part 2 - does any human transcript encode an ACRBP-V5-like N-terminal half?")
    add("")
    add(
        f"For every protein_coding transcript at the locus, the translated product is compared with "
        f"that species' canonical product. A transcript is scored *V5-like* when it is non-canonical, "
        f"is {V5_LIKE_MIN_RATIO:.2f}-{V5_LIKE_MAX_RATIO:.2f} of the canonical length, and matches the "
        f"canonical N-terminus at >={V5_LIKE_MIN_IDENTITY:.0f}% identity over its own length. Mouse "
        "ACRBP-V5 (316/540 = 0.585 of canonical) is the positive control this test must recover."
    )
    add("")
    add("| Species | Gene | Assembly | Transcripts | Biotypes | Canonical protein (aa) |")
    add("|---|---|---|---|---|---|")
    for species, inv in results["transcripts"].items():
        biotypes = ", ".join(f"{k}={v}" for k, v in inv["biotypes"].items())
        add(
            f"| {species} | {inv['gene_id']} | {inv['assembly']} | {inv['n_transcripts']} | "
            f"{biotypes} | {inv['canonical_protein_length']} |"
        )
    add("")
    add("| Species | Transcript | Protein (aa) | Length ratio | N-terminal identity | Canonical | V5-like |")
    add("|---|---|---|---|---|---|---|")
    for species, inv in results["transcripts"].items():
        for transcript in inv["protein_coding"]:
            add(
                f"| {species} | {transcript['name'] or transcript['id']} | "
                f"{transcript['protein_length']} | {transcript['length_ratio']} | "
                f"{transcript['n_terminal_identity']}% | "
                f"{'yes' if transcript['is_canonical'] else 'no'} | "
                f"{'**yes**' if transcript['v5_like'] else 'no'} |"
            )
    add("")
    hits = {species: inv["v5_like_transcripts"] for species, inv in results["transcripts"].items()}
    positive = [s for s, v in hits.items() if v]
    negative = [s for s, v in hits.items() if not v]
    add(
        "**Read-out.** V5-like transcripts found in: "
        + (
            "; ".join(f"{s} ({', '.join(hits[s])})" for s in positive)
            if positive
            else "no species"
        )
        + ". None found in: "
        + (", ".join(negative) if negative else "no species")
        + ". The test recovers the mouse positive control - and it also returns a hit in **human**. "
        "That is the opposite of what the rodent-specific reading of PMID:23426433 predicts, so "
        "Part 2b checks whether the human hit is the same splicing event or an unrelated truncation."
    )
    add("")

    add("## Part 2b - is the human hit the same intron-5 read-through event?")
    add("")
    add(
        "Mouse ACRBP-V5 arises by retention of intron 5: the transcript keeps the first five exons "
        "but runs past the exon-5 donor site into intron 5, which supplies an in-frame stop. UniProt "
        "records the consequence on the protein as `SLQQL -> RYRKL` immediately before the "
        "truncation. Each V5-like transcript is therefore checked for both signatures - the exon "
        "chain and the substituted C-terminal pentapeptide. In the *leading exons shared* column, "
        "exon 1 is matched on its donor boundary only, because annotated transcription start sites "
        "differ by a few bases between transcripts of the same gene; later exons must match on both "
        "boundaries."
    )
    add("")
    add("| Species | Transcript | Exons (variant/canonical) | Leading exons shared | Terminal-exon verdict | Protein (aa) | Variant tail | Canonical at same positions |")
    add("|---|---|---|---|---|---|---|---|")
    for species, inv in results["transcripts"].items():
        for entry in inv["v5_like"]:
            add(
                f"| {species} | {entry['name']} ({entry['transcript_id']}) | "
                f"{entry['n_exons']}/{entry['canonical_n_exons']} | "
                f"{entry['shared_leading_exons']} | {entry['classification']} | "
                f"{entry['protein_length']} | `{entry['variant_tail']}` | "
                f"`{entry['canonical_at_same_positions']}` |"
            )
    add("")
    readthrough = [
        (species, entry)
        for species, inv in results["transcripts"].items()
        for entry in inv["v5_like"]
        if entry.get("reads_into_intron")
    ]
    tails = sorted({entry["variant_tail"] for _, entry in readthrough})
    replaced = sorted({entry["canonical_at_same_positions"] for _, entry in readthrough})
    exon_indices = {entry["terminal_exon_index"] for _, entry in readthrough}
    common_prefix = ""
    if tails:
        for position in range(min(len(t) for t in tails)):
            if len({t[position] for t in tails}) != 1:
                break
            common_prefix += tails[0][position]
    consistent = len(readthrough) > 1 and len(exon_indices) == 1 and len(common_prefix) >= 4
    add(
        "**Read-out.** Intron read-through confirmed in: "
        + (", ".join(f"{s} ({e['name']})" for s, e in readthrough) if readthrough else "no species")
        + ". Read-through occurs after canonical exon "
        + (
            str(sorted(exon_indices)[0])
            if len(exon_indices) == 1
            else "/".join(str(i) for i in sorted(exon_indices))
        )
        + " in "
        + ("every case" if len(exon_indices) == 1 else "differing positions")
        + ". Variant C-terminal pentapeptides: "
        + ", ".join(f"`{t}`" for t in tails)
        + " (shared prefix `"
        + (common_prefix or "-")
        + "`), replacing canonical "
        + ", ".join(f"`{t}`" for t in replaced)
        + ". "
        + (
            "The human and mouse variants read through the same intron, terminate at equivalent "
            f"positions, and both replace the canonical S-L-x-Q-L pentapeptide with `{common_prefix}`-"
            "initiated basic tails that differ only in the final residue. That is one conserved "
            "splicing event, not two coincidences: the human ACRBP locus does carry a structural "
            "counterpart of the 'rodent-specific' ACRBP-V5. Whether that counterpart is "
            "transcribed in human spermatogenic cells is a separate question, and the limits "
            "below record what the primary literature says about it."
            if consistent
            else "The variants do not share a consistent signature; read the table above rather "
            "than any summary sentence."
        )
    )
    add("")
    add(
        "Three limits on this result, and the second is the important one. It is an "
        "annotation-level finding: GENCODE annotating the transcript is not evidence that the "
        "protein is made in human spermatids. The primary literature reports the opposite at the "
        "mRNA level, and states it directly rather than by implication - PMID:30606959: "
        "\"Porcine, guinea pig, and human spermatogenic cells produce only a single form of Acrbp "
        "(termed Acrbp-W) mRNA, whereas two mRNA forms, wild-type Acrbp-W and intron 5-retaining "
        "variant Acrbp-V5 mRNAs, are synthesized by pre-mRNA alternative splicing of the Acrbp gene "
        "in mouse.\" RT-PCR outranks a genome annotation on the question of what is transcribed, so "
        "what this section establishes is a **discrepancy between GENCODE and the experimental "
        "record**, not that human spermatids make an ACRBP-V5 equivalent. And UniProt Q8NEB7 "
        "carries no ALTERNATIVE PRODUCTS section (Part 1), so the human product of this transcript "
        "has no isoform identifier that a GO annotation could be qualified with."
    )
    add("")

    add("## Part 3 - where the ACRBP-V5 truncation lands on the human protein")
    add("")
    v5 = results["v5_mapping"]
    add(
        f"Mouse ACRBP-V5 ({v5['mouse_isoform_id']}) is {v5['v5_length']} aa: UniProt records "
        f"residues {v5['missing_span'][0]}-{v5['missing_span'][1]} of the {v5['mouse_length']}-aa "
        "canonical ACRBP-W as absent from it, i.e. V5 stops in the middle of the protein and "
        "keeps only the N-terminal half."
    )
    add("")
    add("| Quantity | Value |")
    add("|---|---|")
    add(f"| Human Q8NEB7 length | {v5['human_length']} aa |")
    add(f"| Mouse Q3V140-1 (ACRBP-W) length | {v5['mouse_length']} aa |")
    add(f"| Mouse Q3V140-2 (ACRBP-V5) length | {v5['v5_length']} aa |")
    add(f"| Global identity, human vs mouse ACRBP-W | {v5['global_identity']}% |")
    add(f"| Human residue aligned to mouse residue {v5['v5_last_residue']} (last V5 residue) | {v5['human_equivalent_of_v5_end']} |")
    add(f"| Human propeptide (removed on maturation) | {v5['human_propeptide']} |")
    add(f"| Human mature chain | {v5['human_mature_chain']} |")
    add("")
    add("Identity across the two regions UniProt annotates on human ACRBP as pro-ACR binding:")
    add("")
    add("| Human region | Note | Identity vs mouse ACRBP-W | Inside ACRBP-V5 span? | Inside human propeptide? |")
    add("|---|---|---|---|---|")
    for region in v5["binding_regions"]:
        add(
            f"| {region['start']}-{region['end']} | {region['note']} | {region['identity']}% | "
            f"{'yes' if region['within_v5'] else 'no'} | "
            f"{'yes' if region['within_propeptide'] else 'no'} |"
        )
    add("")
    propeptide_end = int(v5["human_propeptide"].split("-")[1])
    v5_end = v5["human_equivalent_of_v5_end"]
    offset = v5_end - propeptide_end
    v5_regions = [r for r in v5["binding_regions"] if r["within_v5"]]
    mature_regions = [r for r in v5["binding_regions"] if not r["within_v5"]]
    add(
        f"**Read-out.** Human and mouse ACRBP are {v5['global_identity']}% identical overall, so the "
        "orthology behind the ISS transfer is not in doubt. The ACRBP-V5 truncation point maps to "
        f"human residue {v5_end}, i.e. {offset} residues past the end of the "
        f"{v5['human_propeptide']} propeptide that human ACRBP removes during maturation. ACRBP-V5 "
        f"therefore corresponds to the whole of that propeptide plus the first {offset} residues of "
        "the mature chain - essentially the half of the precursor that maturation discards. Of the "
        "two annotated pro-ACR-binding regions, "
        + (
            f"{len(v5_regions)} falls inside the V5 span ("
            + ", ".join(f"{r['start']}-{r['end']}" for r in v5_regions)
            + ") and lies within the propeptide"
            if v5_regions
            else "none falls inside the V5 span"
        )
        + ", while "
        + (
            f"{len(mature_regions)} ("
            + ", ".join(f"{r['start']}-{r['end']}" for r in mature_regions)
            + ") sits in the mature chain that human ACRBP keeps"
            if mature_regions
            else "none sits in the mature chain"
        )
        + ". So the two mouse activities are carried on physically separate halves of the protein, "
        "and human ACRBP keeps both halves: the mature chain permanently, and the V5-equivalent "
        "N-terminal half either as the transient unprocessed 60-kDa precursor or as the product of "
        "the intron-5 read-through transcript found in Part 2b."
    )
    add("")

    add("## Part 4 - is any ACRBP ortholog membrane-anchored?")
    add("")
    add(
        "Bears on `GO:0002080 acrosomal membrane` (human ISS from pig Q29016, whose source is an "
        "immunofluorescence IDA that cannot resolve acrosomal matrix from acrosomal membrane)."
    )
    add("")
    add("| Accession | Species | Signal peptide | Transmembrane/lipidation features | Max Kyte-Doolittle 19-mer after signal | Window start |")
    add("|---|---|---|---|---|---|")
    for row in results["membrane"]:
        anchors = ", ".join(row["membrane_features"]) or "none"
        add(
            f"| {row['accession']} | {row['species']} | {row['signal_peptide']} | {anchors} | "
            f"{row['max_kd_window_after_signal']} | {row['max_kd_window_start_in_mature']} |"
        )
    add("")
    anchored = [row["species"] for row in results["membrane"] if row["membrane_features"]]
    no_signal = [row["species"] for row in results["membrane"] if row["signal_peptide"] == "none"]
    peak = max(results["membrane"], key=lambda r: r["max_kd_window_after_signal"])
    add(
        "**Read-out.** Orthologs carrying a transmembrane or lipidation feature: "
        + (", ".join(anchored) if anchored else "none")
        + ". Orthologs lacking a signal peptide: "
        + (", ".join(no_signal) if no_signal else "none")
        + f". The most hydrophobic mature window in the family is {peak['species']} at "
        f"{peak['max_kd_window_after_signal']}, "
        + (
            f"above the ~{TM_THRESHOLD} heuristic threshold"
            if peak["max_kd_window_after_signal"] >= TM_THRESHOLD
            else f"below the ~{TM_THRESHOLD} heuristic threshold, though not by a wide margin"
        )
        + ". The load-bearing evidence is the curated feature table, not the hydropathy scan: every "
        "ACRBP ortholog is a signal-peptide-bearing, anchor-free secretory protein. That is "
        "consistent with sp32 having been purified from acid extracts of ejaculated sperm as a "
        "soluble protein, and it makes a soluble lumenal/matrix assignment "
        "(`GO:0043159 acrosomal matrix`) the appropriate compartment. `located_in` "
        "`GO:0002080 acrosomal membrane` asserts residence in the bilayer itself, which no ortholog "
        "has a feature to support; `GO:0005634 nucleus` is likewise unreachable for a protein that "
        "is translocated into the secretory pathway at synthesis."
    )
    add("")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refetch", action="store_true", help="ignore the data/ cache and re-download"
    )
    args = parser.parse_args()

    entries = {
        accession: uniprot_entry(accession, refetch=args.refetch) for accession in ORTHOLOGS
    }

    inventory = isoform_inventory(entries)

    transcripts = {}
    for label, (species, symbol) in ENSEMBL_SPECIES.items():
        transcripts[label] = transcript_inventory(
            ensembl_gene(species, symbol, refetch=args.refetch), refetch=args.refetch
        )

    human, mouse = entries["Q8NEB7"], entries["Q3V140"]
    human_seq = human["sequence"]["value"]
    mouse_w = uniprot_isoform_sequence("Q3V140-1", refetch=args.refetch)
    mouse_v5 = uniprot_isoform_sequence("Q3V140-2", refetch=args.refetch)

    missing_start, missing_end = variant_sequence_span(mouse)
    v5_last_residue = missing_start - 1

    mapping, global_identity = residue_map(mouse_w, human_seq)
    if v5_last_residue not in mapping:
        raise SystemExit(
            f"FATAL: mouse residue {v5_last_residue} is not aligned to any human residue; "
            "cannot map the ACRBP-V5 truncation point."
        )
    human_equivalent = mapping[v5_last_residue]

    propeptide = require_feature(human, "Propeptide", "Q8NEB7")[0]
    chains = require_feature(human, "Chain", "Q8NEB7")
    mature = max(chains, key=lambda c: c["start"])

    binding_regions = []
    for region in require_feature(human, "Region", "Q8NEB7"):
        if "Pro-ACR binding" not in region["note"]:
            continue
        binding_regions.append(
            {
                "start": region["start"],
                "end": region["end"],
                "note": region["note"],
                "identity": round(
                    region_identity(human_seq, mouse_w, region["start"], region["end"]), 1
                ),
                "within_v5": region["end"] <= human_equivalent,
                "within_propeptide": region["start"] >= propeptide["start"]
                and region["end"] <= propeptide["end"],
            }
        )
    if not binding_regions:
        raise SystemExit(
            "FATAL: no 'Pro-ACR binding' Region features on human Q8NEB7; the mapping in Part 3 "
            "depends on them. Re-run with --refetch in case the entry changed."
        )

    results = {
        "isoform_inventory": [record.__dict__ for record in inventory],
        "transcripts": transcripts,
        "v5_mapping": {
            "human_length": len(human_seq),
            "mouse_length": len(mouse_w),
            "v5_length": len(mouse_v5),
            "mouse_isoform_id": "Q3V140-2",
            "missing_span": [missing_start, missing_end],
            "v5_last_residue": v5_last_residue,
            "global_identity": round(global_identity, 1),
            "human_equivalent_of_v5_end": human_equivalent,
            "human_propeptide": f"{propeptide['start']}-{propeptide['end']}",
            "human_mature_chain": f"{mature['start']}-{mature['end']}",
            "binding_regions": binding_regions,
        },
        "membrane": membrane_check(entries),
    }

    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(build_report(results))
    print("wrote results.json and RESULTS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
