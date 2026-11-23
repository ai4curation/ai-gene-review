# Sequence identity of the assayed septacidin enzymes

The original cluster MF372757.1 is from Streptomyces fimbriatus strain CGMCC 4.1598 and cites PMID:29483275. All three extracted genomic CDS translations exactly match their deposited protein translations and the complete current UniProt sequences.

| Original gene | Original protein | Current UniProt | Length | CDS coordinates, 1-based inclusive | Exact sequence match |
|---|---|---|---|---|---|
| sepB | AVM80385.1 | A0A2P1G6C0 | 707 aa | 3611–5734 | yes |
| sepC | AVM80386.1 | A0A2P1G6C1 | 321 aa | 5814–6779 | yes |
| sepL | AVM80395.1 | A0A2P1G6D3 | 287 aa | 16085–16948 | yes |

SepB A0A2P1G6C0 is identical over all 707 residues to AVM80385.1, the sepB translation in the original MF372757.1 septacidin cluster.

SepC A0A2P1G6C1 is identical over all 321 residues to AVM80386.1, the sepC translation in the original MF372757.1 septacidin cluster.

SepL A0A2P1G6D3 is identical over all 287 residues to AVM80395.1, the sepL translation in the original MF372757.1 septacidin cluster.

Current UniProt gene labels differ: SepB is now rfaE2/ACFPN6_36080 and SepC is ACFPN6_36075, with newer genome cross-references. The exact sequence comparisons establish the original experimentally named identities without assigning functions to a vaguely similar same-species homolog. SepL retains its original name and sequence cross-reference.

The negative control compares the sepB CDS to the supplied SepC UniProt protein and reports false, with unequal lengths and unequal digests. The same generic script therefore discriminates unrelated inputs rather than always reporting agreement.

These comparisons establish sequence identity to the deposited assayed genes, not independent verification of the physical experimental plasmids. They do not prove enzyme activity, domain boundaries, subcellular localization, or genome-wide uniqueness. Activity evidence comes from the biochemical study. The original strain is supported by the deposited cluster source metadata; current UniProt species-level taxonomy alone does not establish strain identity.

## Reproducibility checklist

- [x] Original sequence source retained with version and retrieval URL.
- [x] Entire CDS translated independently using the deposited genetic code.
- [x] Reusable parameterized script; no hardcoded gene identity conclusions.
- [x] Exact dependency version recorded.
- [x] Three distinct positive input pairs checked.
- [x] Mismatched-protein negative control checked.
- [x] Raw lengths, equality flags and sequence digests retained.
- [x] Scope and limitations stated.
