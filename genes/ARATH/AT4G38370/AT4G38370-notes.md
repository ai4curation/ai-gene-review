# AT4G38370 (Q0WW53): evidence and exact-input prediction review

The fold-level name is reasonable. The only emitted GO term is generic catalytic activity; the TIGAR structural donor does not establish a particular phosphatase substrate or glycolytic role for AT4G38370.

## Input identity and functional boundary

Q0WW53 maps to AT4G38370 and PTHR47821:SF2. Its 225-residue sequence contains an N-terminal RHG motif. The emitted donor Q7ZVE3 is zebrafish TIGAR B. Exploratory global alignment preserves the donor catalytic histidine and proton-donor/acceptor residues, but is highly gapped and has low overall identity; the apparent mismatch at a transition-state contact is not reliable evidence of catalytic loss. No TIGAR-specific substrate assignment follows from this alignment.

## Biological evidence

- [PMID:19015259 — Structural and biochemical studies of TIGAR (TP53-induced glycolysis and apoptosis regulator).](https://pubmed.ncbi.nlm.nih.gov/19015259/): Direct TIGAR biochemistry establishes donor activity and substrate discrimination, not the substrate of the Arabidopsis protein.

> The
> recombinant human and zebra fish enzymes hydrolyze fructose-2,6-bisphosphate as
> well as fructose-1,6-bisphosphate but not fructose 6-phosphate in vitro.

## Exact non-GO claims

The complete emitted record is preserved in [AT4G38370-protnlm-source.json](AT4G38370-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Phosphoglycerate mutase-like protein

CNN (CS 2). “Phosphoglycerate mutase-like protein” is a qualified fold-level description consistent with the histidine-phosphatase domain assignment. The “-like” wording does not assert phosphoglycerate turnover or a glycolytic pathway role.

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [AT4G38370-protnlm-predictions-review.yaml](AT4G38370-protnlm-predictions-review.yaml).

## Family integration

PTHR47821:SF2 places the target among phosphoglycerate-mutase-family proteins. The histidine-phosphatase fold encompasses different phosphosugar reactions, so a common RHG catalytic motif cannot identify a substrate. It also does not establish the specialized secreted phytase architecture of another histidine-phosphatase branch.

## Evidence limits

No target-specific biochemical study was located under AT4G38370 or Q0WW53. The TIGAR primary report is abstract-only and explicitly establishes donor enzymology. The genuine Falcon synthesis supplies family hypotheses but does not establish a target reaction. The sequence comparison is exploratory: sparse global alignments are not used to call residue loss or to identify an evolved pseudoenzyme.

Exact sequence mapping: [AT4G38370-bioinformatics/RESULTS.md](AT4G38370-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20 full re-review (independent of ProtNLM predictions)

The previous version of this review was built around a ProtNLM prediction and its structure-matched
TIGAR donor. That framing has been dropped: TIGAR (human/zebrafish) sits in a different PANTHER family
from AT4G38370, so its fructose-2,6-bisphosphatase biochemistry cannot be transferred. The TIGAR
references and the prediction-derived files are no longer cited.

#### Identity
- Q0WW53 (RIKEN cDNA BAE98645.1, 225 aa) is sequence-identical to F4JTN4, the TAIR/Araport
  AT4G38370 gene-model product (NP_568040.1). Q8LCU4 differs at one residue (K90E). So the benchmark
  accession is the full-length canonical product, not an isoform or fragment.
- UniProt PE level 1 comes from a large-scale N-terminal acetylation proteomics study
  (PMID:22223895); the gene is not named in the cached main text (supplementary data).

#### Family / evolutionary placement
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

#### Closest characterized relative
- No experimentally characterized member of PTHR47821 exists. Characterized clade-1 proteins (dPGM,
  TIGAR, PFKFB bisphosphatase domain, UBASH3/Sts-1, bacterial SixA/PhoE) all belong to other PANTHER
  families, so any transfer would be superfamily-level only. Relative recorded as none_found.

#### PANTHER family review
- interpro/panther/PTHR47821/PTHR47821-review.yaml: coherence UNKNOWN; agrees with SF2 placement.
  It leans on TIGAR/ProtNLM donor material, which this re-review no longer uses; no disagreement on
  subfamily placement.

#### Modules
- No module includes AT4G38370. The glycolysis/gluconeogenesis modules containing PGAM are not
  applicable because phosphoglycerate mutase activity is not established for this family.

#### Annotation decisions
- No existing GO annotations to review. No NEW annotations proposed: a generic catalytic or
  phosphatase activity term would rest only on superfamily membership, and the superfamily includes
  both mutases and phosphatases with diverse substrates.
