# Cc2d2a (mouse, Q8CFW7) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted for this review.

### Data and provenance

- `just fetch-gene mouse Cc2d2a` created the UniProt, GOA (34 GOA rows, seeded as 33
  review rows; the 9 per-partner IPI `protein binding` rows are kept separate) and stub files.
- `just deep-research-falcon mouse Cc2d2a --fallback perplexity-lite` FAILED: both falcon
  and the perplexity-lite fallback exited with error (recipe line 355, exit code 1). No
  deep-research file exists; the review is built from the cached primary literature below.
- All six GOA-cited PMIDs are cached; PMID:22179047 (Chih et al. 2012) is abstract-only.

### Evolutionary grounding

- PANTHER PTHR20837:SF7 (CC2D2A subfamily), same subfamily as human CC2D2A (Q9P2K1).
  Fly A1ZAV1 sits in SF0 (also named CC2D2A); CC2D2B is the separate SF2 subfamily
  (`interpro/panther/PTHR20837/PTHR20837-entries.csv`).
- PAINT node PTN000464650 (taxon Eukaryota) carries three IBDs: ciliary transition zone
  (GO:0035869), protein localization to ciliary transition zone (GO:1904491) and non-motile
  cilium assembly (GO:1905515); mouse MGI:1924487 is a seed for all three
  (`interpro/panther/PTHR20837/PTHR20837-paint.tsv`). PAINT did NOT propagate MKS complex,
  smoothened signaling or any organ-development term from the mouse experimental set; I
  treat this as a deliberate curator decision (transfer of these to other species should
  not be inferred from this review).

### Experimental findings in mouse (species-specific)

- Garcia-Gonzalo et al. 2011 [PMID:21725307]: Tctn1-LAP purification and co-IP place
  Cc2d2a in the Tectonic complex ["Tctn1 interacted with Tctn2, Tctn3, Mks1, Cc2d2a and
  B9d1"]; Cc2d2a localizes to TZ independently of Tctn1; gene-trap null embryos have
  randomized L/R axes, holoprosencephaly, microphthalmia; tissue-specific loss of cilia;
  null MEFs lack ciliary AC3 and Pkd2 and have reduced ciliary Smo ["an effect that was
  even stronger in Cc2d2a−/− MEFs"].
- Chih et al. 2012 [PMID:22179047] (abstract only): nine-protein TZ complex; TMEM231, B9D1
  and CC2D2A TZ localizations "dependent on one another and on Sept2"; complex acts as a
  diffusion barrier.
- Veleri et al. 2014 [PMID:24947469]: targeted null; null MEFs have mother centriole but
  no axoneme; "The mouse Cc2d2a transgene could rescue the axoneme assembly defect";
  absent/abnormal subdistal appendages, reduced Odf2/ninein/trichoplein; immunogold on SDA
  in mouse IMCD3 cells and monkey retina; node flattened with few cilia; neural-tube Shh
  patterning lost; docked ciliary vesicle without TZ in a fraction of MEFs.
- Li et al. 2016 [PMID:26982032]: Tmem80 TZ localisation in MEFs depends on Cc2d2a/Mks6.
- Forward-genetic CHD/kidney screens [PMID:25807483, PMID:27002738]: Cc2d2a mutant lines
  with CHD/laterality and prenatal cystic kidney; these are organismal phenotypes.

### Decisions

- Core: MKS complex, ciliary TZ, protein localization to ciliary TZ, cilium assembly /
  non-motile cilium assembly.
- Organ-development IMP rows (kidney, heart, eye, embryonic brain) marked over-annotated:
  downstream of cilia loss. L/R determination and neural tube closure kept as non-core
  (direct node-cilia / Shh-patterning link but still downstream of ciliogenesis).
- Smoothened signaling kept as non-core (TZ gating affects Smo ciliary entry; PAINT did
  not propagate it).
- Cytoplasm IEA -> MODIFY to ciliary basal body (UniProt curated location, mother-centriole
  immunolabelling).
- 9 generic protein binding IPI rows REMOVED per policy; complex membership captured by
  MKS complex.
- NEW ciliary transition zone assembly (GO:1905349) considered and NOT proposed: QuickGO
  (2026-10-20) shows core MKS-module partners (Tctn1, Mks1, B9d1) do not carry it in
  mouse/human; only Cep290, Ccdc66, Dzip1l do. Raised as a question instead.
- Centriolar subdistal appendage (GO:0120103) not proposed as NEW; immunogold data are
  single-study and conflict with later super-resolution mapping (as noted in the human
  CC2D2A review); raised as a question.
