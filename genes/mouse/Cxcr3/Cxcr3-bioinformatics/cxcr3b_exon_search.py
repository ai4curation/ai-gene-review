# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython>=1.85", "requests>=2.32"]
# ///
"""Search the mouse Cxcr3 locus for a counterpart of the human CXCR3-B N-terminal extension.

Human CXCR3-B (P49682-2) replaces the first four residues of CXCR3-A (MVLE) with a
51-residue extension (UniProt VAR_SEQ 1..4, VSP_015684). Many human CXCR3 GO
annotations (angiostatic, anti-proliferative, pro-apoptotic, cAMP signalling) were
made on that isoform, and they reach mouse Cxcr3 by orthology (ISO/ISS). This script
asks whether the mouse genome even encodes an equivalent peptide.

Method:
1. Read the isoform-2 replacement peptide from the human UniProt flat file.
2. Fetch genomic sequence of human CXCR3 and mouse Cxcr3 (gene span plus flanks)
   from the Ensembl REST API, in gene orientation.
3. Six-frame translate each region and run a local alignment (BLOSUM62) of the
   extension peptide against every frame.
4. Calibrate scores with shuffled versions of the peptide against the same region.
5. List annotated Ensembl transcripts for both genes.
6. Report global identity of the canonical mouse and human proteins.

Usage: uv run --script cxcr3b_exon_search.py  (dependencies are declared inline, PEP 723)
Writes results-cxcr3b.json next to this script.
"""

import json
import random
import re
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Seq import Seq

HERE = Path(__file__).parent
GENES = HERE.parent.parent.parent
HUMAN_UNIPROT = GENES / "human" / "CXCR3" / "CXCR3-uniprot.txt"
MOUSE_UNIPROT = HERE.parent / "Cxcr3-uniprot.txt"
ENSEMBL = "https://rest.ensembl.org"
FLANK = 5000
N_SHUFFLES = 200


def uniprot_sequence(path: Path) -> str:
    text = path.read_text()
    block = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"\s", "", block)


def isoform2_extension(path: Path) -> str:
    text = path.read_text()
    m = re.search(r'FT   VAR_SEQ         1\.\.4\n((?:FT {19}.*\n)+)', text)
    assert m, "VAR_SEQ 1..4 not found"
    note = "".join(line[21:].strip() for line in m.group(1).splitlines())
    note = note.split('/note="')[1].split('"')[0]
    replacement = note.split("->")[1].split("(")[0]
    return re.sub(r"\s", "", replacement)


def ensembl_gene(species: str, symbol: str) -> dict:
    r = requests.get(
        f"{ENSEMBL}/lookup/symbol/{species}/{symbol}",
        params={"expand": 1},
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def ensembl_region(species: str, gene: dict) -> str:
    start = gene["start"] - FLANK
    end = gene["end"] + FLANK
    region = f"{gene['seq_region_name']}:{start}..{end}:{gene['strand']}"
    r = requests.get(
        f"{ENSEMBL}/sequence/region/{species}/{region}",
        headers={"Content-Type": "text/plain"},
        timeout=60,
    )
    r.raise_for_status()
    return r.text.strip()


def six_frames(dna: str) -> list[tuple[str, str]]:
    frames = []
    seq = Seq(dna)
    for strand, s in (("+", seq), ("-", seq.reverse_complement())):
        for offset in range(3):
            sub = s[offset:]
            sub = sub[: len(sub) - len(sub) % 3]
            frames.append((f"{strand}{offset}", str(sub.translate())))
    return frames


def make_aligner(mode: str) -> Align.PairwiseAligner:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = mode
    return aligner


def best_hit(aligner, peptide: str, frames) -> dict:
    best = {"score": float("-inf")}
    for name, prot in frames:
        aln = aligner.align(peptide, prot.replace("*", "X"))[0]
        if aln.score > best["score"]:
            q = aln.aligned[0]
            t = aln.aligned[1]
            qseg = "".join(peptide[a:b] for a, b in q)
            tseg = "".join(prot[a:b] for a, b in t)
            ident = sum(1 for x, y in zip(qseg, tseg) if x == y)
            best = {
                "score": aln.score,
                "frame": name,
                "query_span": [int(q[0][0]), int(q[-1][1])],
                "aligned_query": qseg,
                "aligned_target": tseg,
                "identical_positions": ident,
                "aligned_length": len(qseg),
                "target_contains_stop": "*" in prot[t[0][0] : t[-1][1]],
                "target_context_60aa": prot[t[0][0] : t[0][0] + 60],
                "frame_offset_aa": int(t[0][0]),
            }
    return best


def main() -> None:
    ext = isoform2_extension(HUMAN_UNIPROT)
    human_prot = uniprot_sequence(HUMAN_UNIPROT)
    mouse_prot = uniprot_sequence(MOUSE_UNIPROT)
    aligner = make_aligner("local")
    rng = random.Random(42)

    results: dict = {"cxcr3b_replacement_peptide": ext, "flank_bp": FLANK}
    for species, symbol in (("homo_sapiens", "CXCR3"), ("mus_musculus", "Cxcr3")):
        gene = ensembl_gene(species, symbol)
        dna = ensembl_region(species, gene)
        frames = six_frames(dna)
        hit = best_hit(aligner, ext, frames)
        shuffled = []
        for _ in range(N_SHUFFLES):
            s = list(ext)
            rng.shuffle(s)
            shuffled.append(best_hit(aligner, "".join(s), frames)["score"])
        mean = sum(shuffled) / len(shuffled)
        sd = (sum((x - mean) ** 2 for x in shuffled) / len(shuffled)) ** 0.5
        results[species] = {
            "gene_id": gene["id"],
            "region": f"{gene['seq_region_name']}:{gene['start'] - FLANK}-{gene['end'] + FLANK}",
            "strand": gene["strand"],
            "region_length_bp": len(dna),
            "transcripts": [
                {
                    "id": t["id"],
                    "name": t.get("display_name"),
                    "biotype": t["biotype"],
                    "n_exons": len(t.get("Exon", [])),
                    "translation_length": t.get("Translation", {}).get("length"),
                }
                for t in gene["Transcript"]
            ],
            "best_hit": hit,
            "shuffled_score_mean": round(mean, 2),
            "shuffled_score_sd": round(sd, 2),
            "shuffled_score_max": max(shuffled),
            "z_score": round((hit["score"] - mean) / sd, 2) if sd else None,
        }

    glob = make_aligner("global")
    g = glob.align(human_prot, mouse_prot)[0]
    ident = sum(
        1
        for (a0, a1), (b0, b1) in zip(*g.aligned)
        for x, y in zip(human_prot[a0:a1], mouse_prot[b0:b1])
        if x == y
    )
    results["canonical_identity"] = {
        "human_P49682_length": len(human_prot),
        "mouse_O88410_length": len(mouse_prot),
        "identical_positions": ident,
        "percent_identity_over_human_length": round(100 * ident / len(human_prot), 1),
        "human_Nterm_10": human_prot[:10],
        "mouse_Nterm_10": mouse_prot[:10],
    }

    (HERE / "results-cxcr3b.json").write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
