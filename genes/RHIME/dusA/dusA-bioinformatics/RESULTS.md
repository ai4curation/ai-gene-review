# dusA (Q92P85, SMc04235) bioinformatics results

Reproduce with:

```bash
bash fetch_gene_models.sh
uv run --project ../../../.. python map_ecoli_residues.py > alignment_output.txt
uv run --project ../../../.. python translate_upstream.py > translate_upstream_output.txt
```

## Query identity and gene models

The KBase Dark Protein Atlas item NZ_RPHN01000062.1_55
(`kbase_NZ_RPHN01000062.1_55.fasta`, saved from the dashboard's sequence panel on
2026-10-30) is a 398-residue protein from contig 62 of *Ensifer meliloti* strain
USDA1810 (NZ_RPHN01000062.1). `map_ecoli_residues.py` (`alignment_output.txt`)
shows:

- Q92P85 = KBase residues 40-398 exactly (KBase has a 39-residue N-terminal extension: MVQQAEKDRQNVTQANGHKELNFYAKARKSGLPIFAVAP)
- RefSeq WP_015241224.1 length 385; Q92P85 is its residues 27-385

So the dashboard protein, UniProt Q92P85 (S. meliloti 1021 SMc04235, 359 aa) and
the current RefSeq protein for the 1021 locus (WP_015241224.1, SM_RS09780, 385 aa)
share the same 359-residue body and differ only in where translation starts. The
RefSeq record for the USDA1810 contig itself (`usda1810_contig62_features.txt`)
also calls dusA with the 359-residue start (CN234_RS21650, 39436..40515,
WP_010969552.1), so the 398-residue model comes from the KBase gene caller.

## The 359-residue start lies inside the FMN-binding N-terminus

`translate_upstream.py` (`translate_upstream_output.txt`) translates 300 nt upstream
of the annotated ATG in frame:

- S. meliloti 1021: open frame upstream of annotated start: RDMMESVQTDGKRGENRYFKAPVFAVAP (28 codons)
- E. meliloti USDA1810: open frame upstream of annotated start: KMVQQAEKDRQNVTQANGHKELNFYAKARKSGLPIFAVAP (40 codons)

In both strains the reading frame stays open upstream of MIDWTD, and the residues
just before it (FAVAP) align to the E. coli DusA FMN-binding segment
(E. coli residues 32-34, SVAPMLDWTD). With the 359-residue start, E. coli P32 has no
counterpart (`alignment_output.txt`: "E. coli P32: gap in Q92P85"); with either
longer start it does:

- E. coli P32 -> P26 (RefSeq WP_015241224.1, ATG at -78 nt in 1021)
- E. coli P32 -> P39 (KBase model, ATG at -117 nt in USDA1810)

This accounts for the UniProt Q92P85 caution "Lacks conserved residue(s) required
for the propagation of feature annotation": the HAMAP MF_02041 FMN-binding feature
at E. coli 32-34 cannot be placed on the truncated sequence (Q92P85 carries every
other MF_02041 FMN-binding feature). The 359-residue model is most likely an
N-terminally truncated gene call; the longer RefSeq model (WP_015241224.1) restores
the motif. Which upstream codon is used in vivo is not known.

## The two strains have different 5' ends, and USDA1810 has a dusA-associated integrase

The upstream extensions differ between the strains (1021: MMESVQTDGKRGENRYFKAPV...;
USDA1810: MVQQAEKDRQNVTQANGHKELNFYAKARKSGLPI...), converging only at FAVAP.
In USDA1810 the gene immediately upstream of dusA is a tyrosine-type
recombinase/integrase on the opposite strand (CN234_RS21645, 38166..39263, minus
strand; dusA 39436..40515, plus strand; `usda1810_dusA_neighborhood.txt`), so the
two genes meet at their 5' ends. This is the arrangement of the dusA-associated
integrase (DAI) genomic islands, which integrate into the 5' end of dusA and supply
a new 5' end for the gene (PMID:25883135). The most parsimonious explanation for
the strain difference is that USDA1810 carries such an island and its first ~35
dusA codons come from the island. This was not checked further (for example by
looking for the attachment-site repeat).

## Catalytic and tRNA-binding residues are conserved

`map_ecoli_residues.py` aligns Q92P85 with E. coli DusA (P32695; global, BLOSUM62):

- aligned columns: 311; identity: 53.1%
- E. coli C114 -> Q92P85 C83 (KBase 122)  conserved   E.coli NLNVGCPSDRV  Q92P85 NMNVGCPSDRV
- FMN-binding E. coli Q84, K153, H186, N226-G228, G248-R249 are all conserved (Q92P85 Q53, K122, H154, N194-G196, G236-R237)
- tRNA-interacting E. coli N111 and R201 are conserved (N80, R169)
- DusA subfamily tRNA-binding signature: E. coli R314 and R317 conserved (R321, R324); E. coli K198 -> Q92P85 R166, a conservative substitution

C114 is the catalytic cysteine of E. coli DusA; the equivalent Thermus thermophilus
Dus Cys93 is covalently cross-linked to C5 of U20 in the tRNA complex
(PMID:22123979). The alignment shows two ~20-residue insertions in the S. meliloti
protein in the C-terminal helical region (after E. coli Q239 and R279); these lie
outside the catalytic barrel and the signature residues.

Together with the HAMAP MF_02041 and InterPro IPR004653 (DusA) assignments in UniProt,
the protein is an intact DusA-subfamily enzyme rather than a degenerate paralog.
