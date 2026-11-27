"""Compare all horse DUOX1 gene-model products with human Q9NRD9 (re-review).

Fetches (live) every horse UniProt entry with gene name DUOX1 or PANTHER
PTHR11972:SF75 membership (filtered from PTHR11972), the Ensembl transcript structure of horse gene
ENSECAG00000023918, and human Q9NRD9, then:

* aligns each horse product globally to human Q9NRD9-1;
* reports internal gaps relative to human;
* reports, for each human feature (EF-hands, TM helices, ferric oxidoreductase
  and FAD-binding domains) the fraction of human residues present in the horse
  product, and the identity of each human UniProt ligand-binding residue
  (Ca2+, heme, FAD, NADPH) at the aligned horse position;
* lists coding-exon lengths (nt) per Ensembl transcript.

Human features are parsed from the cached genes/human/DUOX1/DUOX1-uniprot.txt.
Writes RESULTS-rereview.md and results-rereview.json next to this script.
Run from the repository root:
    uv run python genes/HORSE/DUOX1/DUOX1-bioinformatics/compare_horse_models_rereview.py
"""

import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

from Bio import Align

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HUMAN = "Q9NRD9"
TARGET = "A0A9L0SQG9"
HORSE_GENE = "ENSECAG00000023918"
HUMAN_FLATFILE = ROOT / "genes" / "human" / "DUOX1" / "DUOX1-uniprot.txt"


def get(url: str, accept: str = "text/plain") -> str:
    with urlopen(Request(url, headers={"Accept": accept})) as r:
        return r.read().decode()


def fasta_seq(acc: str) -> str:
    text = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(text.splitlines()[1:])


def human_features() -> tuple[list[dict], list[dict]]:
    """Return (ranged features, binding sites) from the cached human flat file."""
    ranged: list[dict] = []
    binding: list[dict] = []
    current = None
    for line in HUMAN_FLATFILE.read_text().splitlines():
        m = re.match(r"FT   (\S+)\s+(\d+)(?:\.\.(\d+))?", line)
        if m:
            kind, start, end = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
            current = {"kind": kind, "start": start, "end": end, "note": ""}
            if kind in ("DOMAIN", "TRANSMEM", "REGION"):
                ranged.append(current)
            elif kind == "BINDING":
                binding.append(current)
            else:
                current = None
            continue
        if current is not None:
            n = re.search(r'/(?:note|ligand)="([^"]+)"', line)
            if n and not current["note"]:
                current["note"] = n.group(1)
    for i, f in enumerate(f for f in ranged if f["kind"] == "TRANSMEM"):
        f["note"] = f"TM helix {i + 1}"
    return ranged, binding


def horse_entries() -> list[dict]:
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query=xref:panther-PTHR11972"
        "+AND+organism_id:9796&fields=accession,length,xref_ensembl,xref_panther,fragment,gene_names&format=tsv&size=500"
    )
    rows = get(url).strip().splitlines()[1:]
    out = []
    for row in rows:
        acc, length, ens, panther, frag, gene = (row.split("\t") + ["", "", "", "", ""])[:6]
        if "PTHR11972:SF75;" not in panther and gene.split(" ")[0] != "DUOX1":
            continue
        out.append(
            {
                "accession": acc,
                "length": int(length),
                "ensembl_transcript": ens.strip(";").split(".")[0],
                "panther": panther,
                "fragment": frag,
            }
        )
    return out


def ensembl_transcripts() -> dict:
    d = json.loads(get(f"https://rest.ensembl.org/lookup/id/{HORSE_GENE}?expand=1", "application/json"))
    out = {}
    for t in d["Transcript"]:
        tl = t.get("Translation")
        if not tl:
            continue
        lo, hi = tl["start"], tl["end"]
        exons = sorted(t["Exon"], key=lambda e: e["start"], reverse=t["strand"] == -1)
        cds = [min(e["end"], hi) - max(e["start"], lo) + 1 for e in exons if e["end"] >= lo and e["start"] <= hi]
        out[t["id"]] = {
            "is_canonical": bool(t.get("is_canonical")),
            "biotype": t.get("biotype"),
            "n_exons": len(exons),
            "coding_exon_nt": cds,
            "protein_length": tl["length"],
        }
    return out


def align(human: str, horse: str, ranged: list[dict], binding: list[dict]) -> dict:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.match_score, a.mismatch_score = 2, -1
    a.open_gap_score, a.extend_gap_score = -10, -0.5
    a.end_gap_score = 0
    aln = a.align(human, horse)[0]
    x, y = str(aln[0]), str(aln[1])
    hmap: dict[int, str] = {}
    hp = 0
    gaps: list[list[int]] = []
    for u, v in zip(x, y):
        if u != "-":
            hp += 1
            if v != "-":
                hmap[hp] = v
            elif gaps and gaps[-1][1] == hp - 1:
                gaps[-1][1] = hp
            else:
                gaps.append([hp, hp])
    pairs = [(u, v) for u, v in zip(x, y) if u != "-" and v != "-"]
    ident = sum(u == v for u, v in pairs)
    first, last = min(hmap), max(hmap)
    internal = [g for g in gaps if g[0] > first and g[1] < last]
    feats = []
    for f in ranged:
        n = f["end"] - f["start"] + 1
        present = sum(1 for i in range(f["start"], f["end"] + 1) if i in hmap)
        feats.append({"feature": f"{f['note']} ({f['start']}-{f['end']})", "fraction_present": round(present / n, 3)})
    sites = []
    for b in binding:
        sites.append(
            {
                "ligand": b["note"],
                "human_pos": b["start"],
                "human_res": human[b["start"] - 1],
                "horse_res": hmap.get(b["start"], "-"),
            }
        )
    return {
        "identity_paired": round(ident / len(pairs), 4),
        "human_span_covered": [first, last],
        "internal_human_gaps": internal,
        "horse_insertions": sum(1 for u, v in zip(x, y) if u == "-" and v != "-"),
        "features": feats,
        "binding_sites": sites,
    }


def summarise_sites(sites: list[dict]) -> dict[str, str]:
    out: dict[str, list[int]] = {}
    tot: dict[str, int] = {}
    for s in sites:
        tot[s["ligand"]] = tot.get(s["ligand"], 0) + 1
        out.setdefault(s["ligand"], [])
        if s["horse_res"] == s["human_res"]:
            out[s["ligand"]].append(s["human_pos"])
    return {k: f"{len(out[k])}/{tot[k]}" for k in tot}


def main() -> None:
    human = fasta_seq(HUMAN)
    ranged, binding = human_features()
    entries = horse_entries()
    transcripts = ensembl_transcripts()
    for e in entries:
        e.update(align(human, fasta_seq(e["accession"]), ranged, binding))
        e["ensembl"] = transcripts.get(e["ensembl_transcript"])
        e["binding_site_summary"] = summarise_sites(e["binding_sites"])
    result = {
        "human": HUMAN,
        "human_length": len(human),
        "target": TARGET,
        "horse_gene": HORSE_GENE,
        "entries": entries,
        "transcripts": transcripts,
    }
    (HERE / "results-rereview.json").write_text(json.dumps(result, indent=2) + "\n")
    lines = [
        "# DUOX1 horse gene models vs human Q9NRD9 (re-review)",
        "",
        f"Generated by `compare_horse_models_rereview.py` from live UniProt (gene DUOX1 or PANTHER PTHR11972:SF75, taxon 9796) "
        f"and Ensembl ({HORSE_GENE}) queries. Human reference Q9NRD9-1, {len(human)} aa; human features from the cached UniProt flat file.",
        "",
        "| Accession | Length | PANTHER | Ensembl transcript | Ensembl canonical | Identity (paired) | Human span | Internal human gaps | Conserved binding residues |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for e in entries:
        ens = e["ensembl"] or {}
        sites = "; ".join(f"{k} {v}" for k, v in e["binding_site_summary"].items())
        lines.append(
            f"| {e['accession']} | {e['length']} | {e['panther'].strip(';')} | {e['ensembl_transcript'] or '-'} | {ens.get('is_canonical', '-')} | "
            f"{e['identity_paired']:.1%} | {e['human_span_covered'][0]}-{e['human_span_covered'][1]} | "
            f"{'; '.join(f'{a}-{b}' for a, b in e['internal_human_gaps']) or 'none'} | {sites} |"
        )
    lines += ["", "## Fraction of each human feature present per horse product", ""]
    header = "| Human feature | " + " | ".join(e["accession"] for e in entries) + " |"
    lines += [header, "|---|" + "---|" * len(entries)]
    for i, f in enumerate(entries[0]["features"]):
        lines.append(f"| {f['feature']} | " + " | ".join(f"{e['features'][i]['fraction_present']:.2f}" for e in entries) + " |")
    lines += ["", "## Coding-exon lengths (nt) per Ensembl transcript", ""]
    for tid, t in transcripts.items():
        lines.append(f"- {tid} (canonical={t['is_canonical']}, biotype={t['biotype']}, {t['protein_length']} aa): {t['coding_exon_nt']}")
    (HERE / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
