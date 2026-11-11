# awd review notes

All four seeded annotations and the original function paragraph are supported by the intact same-gene enzyme core. The selected 168 aa PC/PD sequence has 15 extra N-terminal residues, while the reviewed record questions that initiation. This discrepancy is documented without alleging a prediction-input error. [PMID:1320004](https://pubmed.ncbi.nlm.nih.gov/1320004/) purified the fly enzyme and [PMID:7559441](https://pubmed.ncbi.nlm.nih.gov/7559441/) connects conserved-site mutations to catalytic impairment. Native enzyme assays plus exact core conservation support the transfer.

## Provider research assessment

The completed Falcon synthesis was inspected. It supports canonical NDP kinase chemistry and identifies endocytic trafficking as a well-established cellular role. The primary PMID:24528630 was cached with full text and read: live trafficking, compartment markers, mutant clones and epistasis place Awd in early-endosome maturation needed for Notch progression. This supports a NEW early-to-late-endosomal transport annotation, with ISS specifying transfer to the exact longer PC/PD product. Awd is not the receptor protease, and local GTP channeling to Rab5/dynamin is not directly established. The provider’s His119 refers to the 153-residue form; it maps to His134 in the exact accession. The extracellular-release thesis observations and disputed protein-kinase activities do not change the core NDP-kinase assessment. PMID:11768313 is a review, not a purified-protein primary experiment.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

### Identity of the benchmark accession
- A0A0B4LHX6 is the FlyBase awd-PC/awd-PD product (168 aa; transcripts awd-RC, awd-RD). The reviewed, canonical product is P08879 = awd-PE (153 aa; awd-RE). It is an alternative gene model (initiation at an upstream ATG) of the same gene, not a fragment. The full P08879 sequence starts at target residue 16. The extension MLGTILAFFSVISAT (15 aa) is 67% hydrophobic, and UniProt's automatic SignalP feature calls 1-17 a signal peptide. UniProt P08879 flags AAF57188.3 (the 168-aa translation) as "Erroneous initiation".
- Biochemical evidence favours the 153-aa start for the native enzyme: [PMID:12099695 "the mature enzyme was found to comprise 152 amino acids, being modified by proteolytic removal of the initiator Met and N-acetylation of Ala2"]. My new mass comparison (awd-bioinformatics/mass_rereview.py, RESULTS-rereview.md) fits only Met-removed, acetylated P08879 2-153 (17080.5 vs 17082.3 Da observed). The full 168-aa form is +1640 Da off and a signal-peptide-cleaved 18-168 form is -115 Da off. Also [PMID:7559441 "Two revertants have substitutions of the initiator methionine and do not accumulate KPN protein."], i.e. the downstream Met is needed for protein accumulation.
- The catalytic core is fully intact in A0A0B4LHX6 (His119 -> His134; all binding residues; RESULTS.md). Function annotations are therefore correct for this product if it is made, but the description now states that it is probably not the bulk native form.

### Evolutionary placement
- PANTHER 19.0 classification: awd (P08879) is in PTHR11349:SF91 "NUCLEOSIDE DIPHOSPHATE KINASE", together with yeast YNK1 (P36010) and C. elegans ndk-1 (Q93576). Human NME1 (SF69) and NME2 (SF57) are in sister subfamilies. Fly-specific evidence on the gene itself (purified enzyme) supports the NDPK activity, so no cross-species transfer is needed for the MF. The gene's PAINT IBA (FlyBase GO table) is nucleoside triphosphate biosynthetic process, from PTN000887110.
- Family review interpro/panther/PTHR11349/PTHR11349-review.yaml does not assign subfamilies and asserts no PTN node, so there is no subfamily disagreement to report. Its GO:0004550 scope is UNRESOLVED only because of the NDK-like branches (SF97 etc.). awd is not in those branches.

### Annotation decisions
- GO:0004550 NDPK activity (IEA): ACCEPT (core).
- GO:0006183 GTP / GO:0006228 UTP / GO:0006241 CTP biosynthetic process (IEA InterPro): ACCEPT. Awd catalyses the terminal NDP->NTP step, so this is participation.
- Withdrawn: the earlier review's NEW GO:0045022 early endosome to late endosome transport (ISS, PMID:24528630). I re-read the full text. The evidence is necessity only: mutant clones, marker co-localisation, and Rab5CA failing to rescue ("awd function is downstream of or is required for Rab5 function"). The authors do not identify a step Awd performs; GTP supply to Rab5/dynamin remains a hypothesis (also stated in the falcon report). FlyBase curated awd's tracheal, adherens-junction and polarity phenotypes but has not given it an endosomal-transport term. Under the CLAUDE.md NEW bar (name the entity that performs the step), the step is done by Rab5/ESCRT/dynamin machinery. The question is moved to suggested_questions and suggested_experiments (a catalytic-dead rescue). In any case a gene-level process claim belongs on the canonical P08879 product rather than on this alternative model.
- core_functions: NDPK activity; GTP/UTP biosynthesis; cytoplasm (curated UniProt, PMID:2175255).

### Relative and modules
- Relative: the canonical same-gene product P08879 (awd-PE). It has no review (genes/DROME/awd is keyed to A0A0B4LHX6), so it needs a review at genes/DROME/awd__P08879. Gene-level experimental GO annotations (microtubule binding, tracheal migration, adherens junction organization, etc.) sit on P08879 and should be reviewed there.
- Modules using PTHR11349 NDK steps (awd is not listed as a representative member): modules/purine_nucleotide_interconversion.yaml, modules/de_novo_pyrimidine_synthesis.yaml, modules/dntp_de_novo_synthesis.yaml; also related: modules/thymidylate_synthesis.yaml (NDPK final step, not modelled).
