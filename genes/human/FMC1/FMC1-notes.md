# FMC1 (human, Q96HJ9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human FMC1 is the experimental donor at PAINT node PTN001271866 (PTHR31716:SF1),
which propagates IBAs to fly CG34117 and other animal members. This review was written
without consulting any ProtNLM2 output.

### Process notes

- `just fetch-gene human FMC1` created the folder (7 GOA rows, 4 references).
- `just deep-research-falcon human FMC1 --fallback perplexity-lite` FAILED (falcon and the
  perplexity-lite fallback both exited with an error; no deep-research file was written).
  Review is based on literature read directly from `publications/`.
- PubMed search `FMC1[tiab] OR C7orf55[tiab]` (2026-10-21) returned 22 hits; most are
  unrelated uses of "FMC1" (bacterial strain, myelin cerebrosides, etc.). Relevant hits
  cached: PMID:28719601, PMID:11096112, PMID:25686363, PMID:35881696, PMID:42295981.

### Experimental evidence in human (the only species with direct FMC1 data in this family)

All primary experimental evidence comes from one paper, PMID:28719601 (Li et al. 2017,
CLIC; full text cached):

- Localization: endogenous C7orf55 immunostaining co-localizes with mito-dsRed in HeLa
  [PMID:28719601 "First, we confirmed mitochondrial localization (Fig 6A) by immunostaining with antibodies to endogenous C7orf55"].
- Knockout/rescue in K562: CRISPR KO reduces ATP5A/ATP5B levels, fully assembled complex V
  (BN-PAGE) and in-gel ATPase activity; all rescued by CRISPR-resistant cDNA
  [PMID:28719601 "All the defects in complex V were entirely rescued by the reintroduction of a CRISPR-resistant version of C7orf55"].
  Complex specificity: the other OXPHOS complexes were assayed and the defect was
  described as a specific destabilization of complex V.
- Interaction: FLAG-IP/MS of mitochondria-rich fraction, confirmed by reciprocal co-IP
  with ATPAF2-V5 (ATPAF2 is the human ortholog of yeast Atp12, an F1 alpha-subunit
  assembly chaperone).
- Authors' interpretation is necessity plus association: "required for mitochondrial ATP
  synthase function and specifically that C7orf55 binds a known assembly factor". No
  molecular activity was measured. Whether FMC1 acts on assembly vs. stability of the
  assembled enzyme is not resolved by steady-state BN-PAGE.

Supporting/independent (non-primary) human evidence:
- MitoCoP high-confidence mitochondrial proteome (PMID:34800366, HTP) — FMC1 not named in
  cached text; the HTP row is consistent with the IDA.
- Coevolution/AlphaFold modelling predicts an FMC1–ATPAF2 interface (PMID:35881696,
  abstract only) — computational support for a direct interaction.
- Gastric cancer study (PMID:42295981, abstract only): FMC1 downstream of RPL27,
  knockdown affects ATP5A expression and OXPHOS-dependent phenotypes. Cancer-cell
  context, abstract only; corroborative at best, not used for any annotation.

### Evolutionary grounding

- PANTHER: human FMC1 is in PTHR31716:SF1 (PROTEIN FMC1 HOMOLOG), with mouse, rat, cow,
  Xenopus, C. elegans C29E4.12, Nematostella and fly CG34117 (`interpro/panther/PTHR31716/PTHR31716-entries.csv`).
- Yeast Fmc1 (P40491) is NOT in PTHR31716: UniProt REST (queried 2026-10-21) places it in
  PTHR28015:SF1. The two are linked only by the Pfam LYR_2 domain (PF13233, also present
  in Q96HJ9) and the Li et al. note that human and yeast proteins show no BLASTP-detectable
  homology [PMID:28719601 "however these short human and yeast proteins have no sequence homology detectable via BLASTP"].
  Therefore yeast-specific findings (matrix localization, heat-stress-conditional
  requirement, suppression by Atp12 overexpression; PMID:11096112) are NOT transferred
  to human FMC1. The functional parallel (Fmc1–Atp12 in yeast; FMC1–ATPAF2 in human) is
  striking and suggests convergent/deep conservation of the role, but PANTHER does not
  establish orthology.
- PAINT PTN001271866: the only WITH/FROM donor is human Q96HJ9 itself; PAINT propagated
  GO:0033615 (BP) and GO:0005739 (CC). The protein-binding IPI was not (and cannot be)
  propagated. No MF was propagated, consistent with the absence of a measured activity.

### Isoforms

UniProt isoform 2 (Q96HJ9-2, VSP_047244) is encoded by ENSG00000269955 (the FMC1-LUC7L2
readthrough locus; separate Ensembl gene in UniProt xrefs) and replaces the C-terminus
with a long LUC7L2-like RS-rich sequence. No GOA annotations are isoform-specific; all
experimental work used the 113-aa canonical cDNA (sequence given in PMID:28719601 methods).

### Decisions

- GO:0033615 (IMP, IBA): ACCEPT — core process; knockout/rescue plus binding to an
  established F1 assembly chaperone gives participation-relevant evidence (not just
  necessity): FMC1 physically associates with the assembly machinery.
- GO:0005739 (IDA, HTP, IBA, IEA): ACCEPT — consistent; no sub-mitochondrial
  compartment established in human.
- GO:0005515 (IPI, ATPAF2): REMOVE per protein-binding policy (interaction is real; the
  term is uninformative). Consistent with genes/human/ATPAF2 review of the reciprocal row.
- No NEW terms. Mitochondrial matrix is plausible (yeast Fmc1, ATPAF2 is matrix) but not
  shown for human FMC1 and yeast is outside the PANTHER family.
