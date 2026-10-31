"""Profile the PANTHER subfamilies of PTHR32329 from UniProtKB.

For each subfamily, fetch every UniProtKB entry whose PANTHER cross-reference
names it, then count members, length distribution, kingdom, and Pfam
architecture (sorted set of Pfam accessions; every architecture with at
least 10 members, with its median length). Also record the PANTHER
subfamily of named proteins, keeping experimentally studied proteins
separate from those whose function is inferred by orthology.

Run (from the repository root):
    uv run python interpro/panther/PTHR32329/PTHR32329-bioinformatics/subfamily_profile.py
Writes subfamily_profile.json next to this script. Nothing is hard-coded
except the query inputs below.
"""

import collections
import json
import statistics
import time
from pathlib import Path

import requests

HERE = Path(__file__).parent
FAMILY = "PTHR32329"
SUBFAMILIES = ["SF2", "SF4", "SF5", "SF7", "SF8"]

# Experimentally studied proteins whose subfamily placement is reported
STUDIED = {
    "P11568": "HgdC, (R)-2-hydroxyglutaryl-CoA dehydratase activator (A. fermentans)",
    "Q5U925": "HadI, 2-hydroxyisocaproyl-CoA dehydratase activator (C. difficile)",
    "Q93AM0": "FldI, phenyllactate dehydratase activator (C. sporogenes)",
    "G3KIM5": "LcdC, lactoyl-CoA dehydratase activator (A. propionicum)",
    "O87876": "BcrA, benzoyl-CoA reductase subunit A (T. aromatica)",
    "O87877": "BcrD, benzoyl-CoA reductase subunit D (T. aromatica)",
    "Q8DVN8": "SMU_438c, plasmalogen synthase (S. mutans)",
    "Q835P9": "EF1327, plasmalogen synthase (E. faecalis)",
    "G0VRE7": "MeHAD, plasmalogen synthase (M. elsdenii)",
    "A0A0H2YUD5": "CPF_1406, PlsA subunit (C. perfringens ATCC 13124)",
    "A0A0H2YN56": "CPF_1405, PlsR subunit (C. perfringens ATCC 13124)",
}

# Proteins whose function is inferred by orthology, not tested directly
INFERRED = {
    "Q9CDI2": "yxcA (L. lactis IL1403); ortholog of the tested L. cremoris PlsA "
              "LACR_2543, which has no UniProtKB entry",
}


def get(url, params):
    for attempt in range(5):
        r = requests.get(url, params=params, timeout=300)
        if r.ok:
            return r
        time.sleep(2 ** attempt)
    r.raise_for_status()


def kingdom(lineage):
    for k in ("Eukaryota", "Archaea", "Bacteria"):
        if k in lineage:
            return k
    return "other"


def profile(sf):
    r = get("https://rest.uniprot.org/uniprotkb/stream", {
        "query": f'xref:"panther-{FAMILY}:{sf}"',
        "fields": "accession,length,xref_pfam,lineage",
        "format": "tsv",
    })
    rows = [line.split("\t") for line in r.text.strip().split("\n")[1:]]
    lengths = [int(x[1]) for x in rows]
    arch_lengths = collections.defaultdict(list)
    for x in rows:
        key = "+".join(sorted({p for p in x[2].split(";") if p})) or "(no Pfam)"
        arch_lengths[key].append(int(x[1]))
    return {
        "n_members": len(rows),
        "median_length": statistics.median(lengths),
        "n_length_ge_1000": sum(1 for v in lengths if v >= 1000),
        "kingdoms": dict(collections.Counter(kingdom(x[3]) for x in rows)),
        "pfam_architectures": [
            {"architecture": k, "n": len(v), "median_length": statistics.median(v)}
            for k, v in sorted(arch_lengths.items(), key=lambda kv: -len(kv[1]))
            if len(v) >= 10
        ],
    }


def placements(proteins):
    r = get("https://rest.uniprot.org/uniprotkb/accessions", {
        "accessions": ",".join(proteins),
        "fields": "accession,length,xref_panther",
        "format": "tsv",
    })
    out = {}
    for line in r.text.strip().split("\n")[1:]:
        acc, length, panther = line.split("\t")
        out[acc] = {
            "note": proteins[acc],
            "length": int(length),
            "panther": sorted(p for p in panther.split(";") if p),
        }
    return out


def main():
    res = {
        "source": "UniProtKB REST, PANTHER cross-references",
        "retrieved": time.strftime("%Y-%m-%d"),
        "subfamilies": {sf: profile(sf) for sf in SUBFAMILIES},
        "studied_proteins": placements(STUDIED),
        "inferred_proteins": placements(INFERRED),
    }
    (HERE / "subfamily_profile.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
