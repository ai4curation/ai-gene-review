"""Is the membrane-associated AK1beta isoform represented in UniProt, and where?

The reviewed entry P00568 lists no alternative products. This script fetches the
unreviewed human entries with gene name AK1, finds any that carry the canonical
sequence behind an alternative N-terminus (the alternative first coding exon may
replace the first few canonical residues), and tests that N-terminus for the
N-myristoylation consensus (Met-Gly-x-x-x-Ser/Thr, PROSITE PS00008-like:
G-{EDRKHPFYW}-x(2)-[STAGCN]-{P} after the initiator Met).
"""
from __future__ import annotations

import json
import re

from ak1_common import dump, fetch, uniprot_sequence


def main() -> None:
    canon = uniprot_sequence()
    raw = json.loads(fetch(
        "https://rest.uniprot.org/uniprotkb/search?query=gene_exact:AK1+AND+organism_id:9606"
        "&format=json&fields=accession,reviewed,sequence,xref_refseq,xref_ensembl,protein_existence&size=100",
        "human_ak1_entries.json").read_text())
    rows = []
    for e in raw["results"]:
        seq = e["sequence"]["value"]
        acc = e["primaryAccession"]
        if acc == "P00568":
            continue
        # longest canonical suffix present in this entry, allowing the first few canonical
        # residues to be replaced by the alternative first exon
        hit = None
        for start in range(0, 6):
            idx = seq.find(canon[start:])
            if idx > 0:
                hit = (start, idx)
                break
        if hit is None or hit[1] <= hit[0]:
            continue
        start, idx = hit
        myr = bool(re.match(r"MG[^EDRKHPFYW]..[STAGCN][^P]", seq))
        rows.append({
            "accession": acc,
            "reviewed": "unreviewed" not in e["entryType"].lower(),
            "length": len(seq),
            "alternative_n_terminus": seq[:idx],
            "alternative_n_terminus_length": idx,
            "replaces_canonical_residues": f"1-{start}",
            "shared_canonical_residues": f"{start + 1}-{len(canon)}",
            "offset_isoform_minus_canonical_numbering": idx - start,
            "n_myristoylation_consensus_at_n_terminus": myr,
            "cysteines_in_alternative_n_terminus": [i + 1 for i, c in enumerate(seq[:idx]) if c == "C"],
            "protein_existence": e.get("proteinExistence"),
            "refseq": sorted({x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "RefSeq"}),
            "ensembl_transcripts": sorted({x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "Ensembl"}),
        })
    out = {"canonical": "P00568", "canonical_length": len(canon),
           "entries_with_alternative_n_terminus": rows,
           "n_human_AK1_entries_examined": len(raw["results"])}
    dump(out, "ak1beta_isoform.json")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
