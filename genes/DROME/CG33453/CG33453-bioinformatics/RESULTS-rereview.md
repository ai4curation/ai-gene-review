# CG33453 isoform indel mapping (2026-10-20 re-review)

Script: `indels_rereview.py` (new; the original `compare.py`, `RESULTS.md` and `results/` are unchanged).
Output: `results-rereview/indels.json`.

Command, run in this directory:

    uv run --no-project --with biopython==1.85 python indels_rereview.py ../CG33453-uniprot-source.json ../CG33453-reference-A1ZBI2-uniprot.json results-rereview/indels.json

## Result

A0A0B4LFV5 (CG33453-PB, 174 aa) and A1ZBI2 (CG33453-PA, 175 aa) differ only by two short indels and have no substitutions in aligned columns.
PB lacks a two-residue SV block at PA positions 20-21, inside the predicted signal peptide (SignalP 1..22 in PB, 1..23 in PA).
PB carries one extra valine at PB position 126, inside the mature DUF1091 chain (PA reads CPYGLQ where PB reads CPYVGLQ).
The exact placement of each gap within its local repeat (SVS, PY(V)G) is alignment-dependent, but the gap lengths are not.

## Interpretation

These are small in-frame differences of the kind produced by alternative splice-site choice at an exon boundary; the script does not test splice sites, so that is a hypothesis, not a result.
Neither isoform lacks the signal peptide or any part of the DUF1091 region, and neither is a fragment.
A one-residue insertion in the mature chain could alter local structure, but nothing here predicts a functional difference between PA and PB.

## PANTHER PTHR20898 census (UniProt REST, release 2026_03)

Counts are X-Total-Results headers from `https://rest.uniprot.org/uniprotkb/search?query=...` and were not saved as files.

| Query | Entries |
|---|---|
| `xref:panther-PTHR20898` | 3090 |
| `xref:panther-PTHR20898 AND taxonomy_id:7147` (Diptera) | 2997 |
| `xref:panther-PTHR20898 AND taxonomy_id:7214` (Drosophilidae) | 1812 |
| `xref:panther-PTHR20898 AND organism_id:7227` (D. melanogaster) | 102 |
| `xref:panther-PTHR20898 AND reviewed:true` | 0 |

`xref:panther-PTHR20898 AND taxonomy_id:50557` (Insecta) returns 3086 entries, so the non-dipteran members are almost all other insects (beetles, moths, thrips, wasps, a cockroach). The remaining four are Aspergillus entries (A0A1L9NGN9, A0A318YG94, A0A5N7A4Z4, A0ABQ6WYD4), whose origin (contamination or transfer) was not examined. There are no vertebrate, nematode or plant members.
CG33453 (both A0A0B4LFV5 and A1ZBI2) and daedalus/CG33690 (Q4ABJ0) are both assigned to subfamily PTHR20898:SF0, the large Drosophila-expanded subfamily.
decima/CG34351 (A8DYR1) is in a different family, PTHR21029.
No member of the family has a Swiss-Prot entry, so no member has a curated, experimentally determined molecular function.
