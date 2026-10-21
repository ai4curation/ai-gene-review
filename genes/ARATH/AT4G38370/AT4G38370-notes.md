# AT4G38370 (Q0WW53) notes

## 2026-10-20 full re-review (independent of ProtNLM predictions)

The previous version of this review was built around a ProtNLM prediction and its structure-matched
TIGAR donor. That framing has been dropped: TIGAR (human/zebrafish) sits in a different PANTHER family
from AT4G38370, so its fructose-2,6-bisphosphatase biochemistry cannot be transferred. The TIGAR
references and the prediction-derived files are no longer cited.

### Identity
- Q0WW53 (RIKEN cDNA BAE98645.1, 225 aa) is sequence-identical to F4JTN4, the TAIR/Araport
  AT4G38370 gene-model product (NP_568040.1). Q8LCU4 differs at one residue (K90E). So the benchmark
  accession is the full-length canonical product, not an isoform or fragment.
- UniProt PE level 1 comes from a large-scale N-terminal acetylation proteomics study
  (PMID:22223895); the gene is not named in the cached main text (supplementary data).

### Family / evolutionary placement
- Domains: Pfam PF00300 His_Phos_1, InterPro IPR013078 His_Pase_superF_clade-1, CDD cd07067
  HP_PGM_like [file:ARATH/AT4G38370/AT4G38370-uniprot.txt "DR   InterPro; IPR013078; His_Pase_superF_clade-1."].
- PANTHER PTHR47821 (single subfamily SF2), "PHOSPHOGLYCERATE MUTASE FAMILY PROTEIN".
  InterPro counts: 951 proteins, 697 proteomes. A UniProt query of the first 500 members shows
  land plants (Gossypium, Oryza, Solanum, Prunus, Populus, Arabidopsis...), algae/diatoms (Triparma,
  Durusdinium) and ~70 bacterial members (Halomonas, Vreelandella, Billgrantia, Enterovibrio,
  Brachybacterium). None is Swiss-Prot reviewed and none has experimental characterization.
- No GOA annotations exist for Q0WW53 (no IBA), so there is no PAINT node for this family.
- Motifs: RHG at 16-18 (His17, putative nucleophile); SHGD at 172-175 (His173, second conserved
  histidine typical of clade 1). Presence of the motifs suggests, but does not show, catalytic activity.
- The falcon deep research conflates clade 1 (PF00300) with clade-2 histidine acid phosphatases and
  phytases (RHGXRXP, PF00328). Its phytase/acid phosphatase discussion is not applicable.

### Closest characterized relative
- No experimentally characterized member of PTHR47821 exists. Characterized clade-1 proteins (dPGM,
  TIGAR, PFKFB bisphosphatase domain, UBASH3/Sts-1, bacterial SixA/PhoE) all belong to other PANTHER
  families, so any transfer would be superfamily-level only. Relative recorded as none_found.

### PANTHER family review
- interpro/panther/PTHR47821/PTHR47821-review.yaml: coherence UNKNOWN; agrees with SF2 placement.
  It leans on TIGAR/ProtNLM donor material, which this re-review no longer uses; no disagreement on
  subfamily placement.

### Modules
- No module includes AT4G38370. The glycolysis/gluconeogenesis modules containing PGAM are not
  applicable because phosphoglycerate mutase activity is not established for this family.

### Annotation decisions
- No existing GO annotations to review. No NEW annotations proposed: a generic catalytic or
  phosphatase activity term would rest only on superfamily membership, and the superfamily includes
  both mutases and phosphatases with diverse substrates.
