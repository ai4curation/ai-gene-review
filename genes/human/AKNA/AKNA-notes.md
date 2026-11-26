# AKNA (Q7Z591) review notes

## 2026-10-03 — PAINT/affinage review

There are two separate literatures on AKNA, and nobody has reconciled them.

- **AT-hook transcription regulator in lymphocytes.** [PMID:11268217 "Here we describe AKNA, a human AT-hook protein that directly binds the A/T-rich regulatory elements of the promoters of CD40 and CD40 ligand (CD40L) and coordinately regulates their expression."]
  - The cached record is abstract-only.
  - The discovery group later calls it [PMID:21606955 "a hypothetical AT-hook-like transcription factor"].
  - A 2023 re-analysis of ENCODE ChIP-seq finds [PMID:36835622 "We detected 381 AKNA peaks at promoter regions"].
- **Centrosomal microtubule organizer, shown in mouse.** [PMID:30787442 "AKNA localizes at the subdistal appendages of the mother centriole in specific subtypes of neural stem cells, and in almost all basal progenitors."] It drives delamination and EMT.

Decisions:
- **No NEW rows. AKNA has no informative MF in any species.**
  - Mouse Akna (Q80VW7) experimental GO comes only from PMID:30787442 and PMID:21606955, and contains no DNA-binding or nucleation term. PAINT propagates only the centrosomal functions.
  - DNA-binding/TF activity and microtubule-nucleation activity are both recorded as MF_DARK knowledge gaps.
  - GO:0090063 positive regulation of microtubule nucleation is withheld on evidential grounds, not by convention. Round 1 of PR #3945 showed that my original comparator argument (NIN, CEP170 and ODF2 lack it) was wrong. AKNA's interactor DCTN1 carries both GO:0120103 and GO:0090063 by IDA, the latter from direct in vitro nucleation [PMID:23874158 "dimeric p150 Nt-GCN4 catalyzes microtubule nucleation in contrast to monomeric p150 Nt."]. AKNA's evidence is cellular necessity and sufficiency plus recruitment of nucleation factors, from an abstract-only cached record, so the term is raised as a suggested question rather than added.
- **Centriole rows are ACCEPTed.** The refinement to GO:0120103 centriolar subdistal appendage is raised as a question, because the mouse curator chose centriole.
- **Neuroblast division in SVZ is KEEP_AS_NON_CORE.** The abstract describes delamination and exit, not division, but the full text is not cached.
- **Protein binding:** CD2BP2 (GYF-motif screen) and LMO1 (HuRI) rows are REMOVEd per policy.
- **Membrane HDA** (NK membrane proteome) is MARK_AS_OVER_ANNOTATED.
