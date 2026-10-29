# cac review notes

## Session 1 (initial review)

- `just fetch-gene DROME cac` resolved P91645 (CAC1A_DROME); 68 GOA rows seeded.
- No deep-research API keys; literature synthesis is in `cac-deep-research-manual.md`
  (manual, verbatim quotes from cached publications).
- PMID:22952921 (Astorga et al. 2012) read in full: cac^TS2 at restrictive temperature
  reduces FM4-64 bouton labelling in lamina photoreceptor terminals by ~85%, and PLTX-II
  reduces depolarization-evoked G-CaMP signals. Supports synaptic vesicle exocytosis in
  photoreceptor terminals [PMID:22952921 "vesicle exocytosis depends on cacophony, TRP and TRPL"].
  Caveat: immunostaining used an N-type alpha1 antibody, as "no specific antibody for
  cacophony is available".

### Decisions worth flagging

- NOT|involved_in neurotransmitter secretion (IMP, PMID:25811491, FlyBase): the paper
  states that cac is required for neurotransmitter release and that cac clones lack ERG
  on-transients; the negative statement in the paper is that the *autophagy* defect is
  not caused by loss of release [PMID:25811491 "It indicates that loss of neurotransmitter release in cac and stj mutants is not causing autophagy defects per se."].
  The NOT row appears to encode that conclusion as a negation of the process itself.
  REMOVE + source defect (FlyBase).
- Epithelial fluid transport (PMID:11208535, IDA/IEP + ARBA IEA): evidence is L-type
  pharmacology (verapamil, nifedipine) and RT-PCR of both Dmca1D and Dmca1A; UniProt says
  cac probably encodes a dihydropyridine-insensitive current. Abstract only, so UNDECIDED
  rather than REMOVE.
- detection of external/abiotic stimulus and detection of stimulus involved in sensory
  perception (ARBA IEA): no basis for a VGCC acting as a stimulus detector; REMOVE.
- calcium ion binding (EF-hand InterPro2GO): the Cav C-terminal EF-hand-like motif is
  not established as a functional Ca2+-binding site for Cac; MARK_AS_OVER_ANNOTATED.
- positive regulation of calcium ion transport into cytosol (IMP, PMID:25445363): the
  channel performs the transport; MODIFY to calcium ion import across plasma membrane.
- exocytosis (IMP, PMID:14715138): MODIFY to GO:0099703 induction of synaptic vesicle
  exocytosis by positive regulation of presynaptic cytosolic calcium ion concentration,
  the SynGO term for the presynaptic VGCC step.
- detection of light stimulus involved in visual perception (IMP, PMID:9649530,
  abstract only): cac^H18 can abolish light responses "in certain genetic combinations";
  cannot tell from the abstract whether this is a photoreceptor (receptor potential)
  defect or a synaptic one. UNDECIDED. Phototransduction (NAS, general review):
  MARK_AS_OVER_ANNOTATED; the phototransduction cascade is rhabdomeric TRP/TRPL.

### No NEW terms proposed
All supported functions are already represented in GOA; applying the strict NEW bar, no
mutant-phenotype-only process was added.

## 2026-10-28 correction: one NEW row

The "No NEW terms proposed" section above predates the review fixes. One NEW row now exists:
GO:0036477 somatodendritic compartment (IC, PMID:22183725). It is inferred from in situ patch-clamp
recordings of somatodendritic Ca2+ currents, combined with conditional mutants and RNAi showing those
currents come from Cac, and it backs the location of the core channel function.
