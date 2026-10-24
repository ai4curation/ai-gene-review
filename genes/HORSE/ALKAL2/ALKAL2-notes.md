# ALKAL2 (horse, F6XWZ3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Benchmark target for the DONKEY40_HORSE_PARTNER cohort. New review (no prior folder);
stub created with `just fetch-gene HORSE F6XWZ3 --alias ALKAL2` (stub id = F6XWZ3, confirmed).
ProtNLM2 output was not consulted.

Deep research: `just deep-research-falcon HORSE ALKAL2 --fallback perplexity-lite` failed
(falcon: "Edison API request failed: Failed to authenticate"; the perplexity-lite fallback also
failed). No deep-research file exists; the review uses the four cached full-text papers on human
ALKAL2 (PMID:26418745, PMID:30061385, PMID:34646012, PMID:34819673), the human Swiss-Prot record
and a gene-model comparison in `ALKAL2-bioinformatics/`.

### Identity: alternative (over-extended) gene model
- F6XWZ3 is 271 aa versus 152 aa for human ALKAL2 (Q6UX46). Residues 120-271 of F6XWZ3 are
  identical to horse A0A3Q2I4Q6 (152 aa, RefSeq XP_001503231.2), and that segment aligns to human
  ALKAL2 1-149 at 86.6% identity [file:HORSE/ALKAL2/ALKAL2-bioinformatics/RESULTS.md "A0A3Q2I4Q6 found in F6XWZ3 at residue 120 (F6XWZ3 N-terminal extension = 119 residues)."].
- All four horse UniProt entries come from one Ensembl gene (ENSECAG00000029965); Ensembl calls the
  F6XWZ3 transcript (ENSECAT00000009339) canonical, but the 119-aa N-terminal extension is
  Arg/Gly/Ala/Pro-rich (65%), predicted disordered (MobiDB-lite region 1..122), has no counterpart
  in human, and pushes the signal peptide (MRGPGRPLLLGLLLVLGAAG...) to an internal position (Met120).
  This is most likely an upstream-start annotation artefact; the bona fide product is expected to be
  the 152-aa protein (= A0A3Q2I4Q6).
- The augmentor domain is intact: the four cysteines that form the two intramolecular disulfides in
  human ALKAL2 (C111-C147, C125-C134) are conserved (F6XWZ3 C232, C246, C255, C268). Human C66, the
  primate-specific interchain cysteine [PMID:30061385 "a fifth, primate-specific cysteine located in the N-terminal variable region mediates dimerization"], is Tyr in horse.
- ALKAL2 not ALKAL1: 86.6% identity to human ALKAL2 vs 62.4% to human ALKAL1; PANTHER PTHR28676:SF2
  (ALK AND LTK LIGAND 2), the same subfamily as human ALKAL2 (interpro/panther/PTHR28676 entries list).

### Evolutionary grounding
- IBA rows derive from PAINT node PANTHER:PTN002010604 with human ALKAL2 (Q6UX46), human ALKAL1
  (Q6UXT8) and zebrafish members as descendants. F6XWZ3 sits in PTHR28676:SF2 with human ALKAL2,
  so transfer of the ligand activity is phylogenetically sound.
- PAINT propagated activator activity, RTK binding and positive regulation of ERK1/2 and ERK5
  cascades, but not the human IDA terms cytokine activity (GO:0005125), cell surface RTK signaling
  pathway (GO:0007169) or positive regulation of neuron projection development (GO:0010976).
  Treated as deliberate; no NEW annotations proposed.

### Function (human ortholog)
- Secreted cytokine ligand of ALK and LTK [PMID:26418745 "that FAM150A and FAM150B are potent ligands for human ALK that bind to the extracellular domain of ALK"].
- Three-helix-bundle cytokine driving receptor dimerization [PMID:34646012 "The cognate cytokines ALKAL1 and ALKAL2 are monomeric three-helix bundles, yet their binding to ALK and LTK elicits similar dimeric assemblies with two-fold symmetry"]; complex stabilized by ligand-membrane contact [PMID:34819673 "This orientation is further stabilized by an interaction between the ligand and the membrane."].
- Downstream ERK1/2 and ERK5 [PMID:26418745 "This response was observed at the level of ALK receptor phosphorylation (pALK-Y1604), and with downstream pERK5"].

### Annotation decisions
- extracellular region: ACCEPT. plasma membrane: KEEP_AS_NON_CORE.
- GO:0030298 receptor signaling protein tyrosine kinase activator activity (IBA, IEA): MODIFY to
  GO:0030297 transmembrane receptor protein tyrosine kinase activator activity. The two are siblings
  under GO:0030296; ALK/LTK are transmembrane RTKs and ALKAL2 is their extracellular ligand.
  Note: UniProt curators annotate human ALKAL2 with GO:0030298 by IDA, so this is raised as a
  suggested question rather than a source defect.
- GO:0030971 receptor tyrosine kinase binding (IBA, IEA): ACCEPT.
- positive regulation of ERK1/2 and ERK5 cascades (IBA): KEEP_AS_NON_CORE.

### Relative
- No reviewed horse ALKAL2 entry exists, and F6XWZ3 is itself the Ensembl-canonical transcript;
  A0A3Q2I4Q6 is an alternative model whose sequence is F6XWZ3 120-271, so a separate review would
  duplicate this one. Next relative: human ALKAL2 (Q6UX46), the experimentally characterised member
  of the same PANTHER subfamily (SF2) and a donor to PTN002010604; no review exists in genes/human.
