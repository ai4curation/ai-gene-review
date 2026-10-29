# HID1 (Q8IV36) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: HID1 is the closest experimentally characterised relative of Drosophila CG8841
(Q0E9B5); this review is of human HID1 in its own right. No ProtNLM2 output was used.

### Process
- `just fetch-gene human HID1` (33 GOA rows) and `just fetch-gene-pmids human HID1`.
- `just deep-research-falcon human HID1 --fallback perplexity-lite` failed: falcon timed
  out at 600 s and the perplexity-lite fallback also timed out. No deep-research file exists.
  The review was written from primary literature found by a PubMed search for
  HID1/HID-1/C17orf28, cached with `just fetch-pmid`.
- Ortholog grounding: `HID1-bioinformatics/hid1_orthologs.py` -> `RESULTS-orthologs.tsv`,
  summarised in `RESULTS.md`.

### Evolutionary grounding
- Human, mouse (Q8R1F6), rat (D4A0C3), fly CG8841 (Q0E9B5) and worm hid-1 (G5EG65) are all
  PANTHER PTHR21575:SF12. Rodent orthologs are about 95-96% identical, fly about 69%, worm 61%.
- Fission yeast SPAC17A5.16 (O13776) is in SF13 (about 32% identical); it is the sole seed of
  the Golgi organization IBD at the eukaryote node PTN000491103 [PMID:40899782 "the
  SPAC17A5.16 mutant lacks a stacked Golgi apparatus (GA) form"].
- PAINT puts localization terms (trans/medial Golgi, cytosol, membrane) and Golgi
  organization at PTN000491103, with IRD negations on Schizosaccharomyces paralog nodes;
  secretory granule maturation is placed at the lower node PTN001090684 (seed mouse Hid1).
  The placement of the granule term below the eukaryote node fits dense core vesicle
  function being a metazoan specialization.

### What is experimentally established, and in which species
- Human protein: localization to medial/trans-Golgi and cytosol, peripheral membrane
  association needing N-myristoylation [PMID:21337012 "dynamically shuttled between the
  Golgi apparatus and the cytosol"] (abstract only; it says "mammalian HID-1", cell lines not
  visible); HPA immunofluorescence (Golgi, cytosol); TGN colocalization in patient
  fibroblasts [PMID:33999436 "Colocalization of HID1 protein with the TGN was not altered in
  fibroblasts of patients compared to controls"]. Disease: biallelic variants cause DEE105
  with hypopituitarism (PMID:33999436).
- Rat (PC12, INS-1): HID1 KO reduces LDCV number, impairs cargo sorting and dense core
  formation, TGN acidification and V-ATPase a2 localization [PMID:29074564]. The N-terminus
  binds membrane without TGN specificity and the conserved C-terminus is the functional domain;
  the patient frameshift modelled in rat HID1 is loss of function [PMID:37751424]. The human
  IMP row for dense core granule biogenesis rests on this rat-cell work.
- Mouse: beta-cell conditional KO blocks homotypic fusion of immature secretory granules and
  proinsulin processing [PMID:27751232].
- C. elegans: hid-1 acts in dense core vesicle neurosecretion and neuropeptide sorting
  [PMID:21115972, PMID:21250940] (abstracts only).
- No molecular activity is known for any family member.

### Decisions
- 12 bare protein-binding IPI rows from interactome screens: REMOVE (policy).
- Cytoplasm (IDA, IEA): MODIFY to cytosol. Golgi apparatus (IDA HPA, IEA): MODIFY to
  trans/medial cisterna and TGN membrane. Membrane IBA: MODIFY to cytoplasmic side of Golgi
  membrane and TGN membrane.
- Cytoplasmic microtubule (IDA, ORFeome overexpression screen hit, PMID:23264731):
  MARK_AS_OVER_ANNOTATED.
- Golgi organization IBA: KEEP_AS_NON_CORE. The seed is from another subfamily (SF13) and
  there is no direct SF12 evidence; the node placement is the curator's decision and no
  loss in SF12 is documented.
- Exosome HDA: KEEP_AS_NON_CORE.
- Localization (trans/medial Golgi, cytosol, cytoplasmic side of Golgi membrane, TGN
  membrane), dense core granule biogenesis (IEA, IMP, ISS) and secretory granule
  maturation (IBA): ACCEPT.
- No NEW terms. TGN acidification/V-ATPase a2 mislocalization is knockout (necessity)
  evidence with no mechanism, so it does not meet the participation bar for a process term.

### Implication for transfer to CG8841
- Safe to transfer at SF12 level: Golgi/TGN peripheral localization and cytosol (already IBA
  from PTN000491103). Dense core granule biogenesis and granule maturation are established in
  rodents and supported in worm (SF12); CG8841 has no direct data here.
