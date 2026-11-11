# ATG4C (human, Q96DT6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human ATG4C is the experimentally characterised reference for donkey
ATG4C (EQUAS, A0A9L0IIU3). No ProtNLM2 output was opened or used.

### Deep research
- `just deep-research-falcon human ATG4C --fallback perplexity-lite` failed.
  Falcon returned "Edison API request failed: Failed to authenticate" (403) and
  the perplexity-lite fallback also failed, so no deep-research file exists. The
  review is built from the cached primary literature and the UniProt record.

### Evolutionary grounding
- PANTHER: human, mouse (Q811C2) and donkey ATG4C are all in PTHR22624:SF38
  (CYSTEINE PROTEASE ATG4C). ATG4A (SF35), ATG4B (SF39) and ATG4D (SF36) are in
  separate subfamilies (UniProt DR lines; `ATG4C-bioinformatics/RESULTS.md`).
- Catalytic triad Cys111/Asp345/His347 aligns to ATG4B Cys74/Asp278/His280
  (`ATG4C-bioinformatics/catalytic_residues.py`). Donkey ATG4C is 95% identical
  end to end with the triad conserved; mouse Atg4c is 90%.
- PAINT node: the human ATG4C IBA rows in GOA cite **PANTHER:PTN002503342**, the
  ancestral ATG4 node that includes yeast Atg4, worm atg-4.1/atg-4.2 and all four
  human paralogs. The campaign brief named PTN009050878 as the shared node, but
  that id appears only in the donkey TreeGrafter rows, not in the human GOA
  file. The two may be nested nodes, but I did not verify that, so this review
  cites only PTN002503342. All IBA terms are family-level, not ATG4C-subfamily
  specific.

### Experimental evidence in human ATG4C
- Priming (cysteine-type endopeptidase activity): weak but measurable in vitro
  [PMID:21177865 "whereas Atg4C and Atg4D had minimal activities as did the catalytic mutant of Atg4B (C74S)"].
  UniProt records Km 47.5 uM (LC3B) and 12.4 uM (GABARAPL2) and NEM inhibition from
  this paper. In cells ATG4C contributes partially to GABARAPL1/L2 priming
  [PMID:30661429 "suggests a partial involvement of ATG4C in GABARAPL1/L2 priming"].
- Delipidation (protein-PE deconjugating activity): direct biochemical evidence
  [PMID:29458288 "all 4 ATG4 proteases can be activated to similar enzymatic activities on lipid-attached substrates"];
  independently confirmed with full-length mammalian-expressed protein
  [PMID:33909989 "full-length ATG4C/D are active under these conditions, unlike the bacterially purified proteins"].
  ATG4D, not ATG4C, is the preferred ATG8-PS delipidase.
- Mitophagy: weakly or not involved in phagophore growth during PINK1/Parkin
  mitophagy, per UniProt's summary of PMID:33773106 (abstract-only in cache).
  This is negative or weak evidence and does **not** experimentally establish an
  ATG4C mitophagy function.
- Location: cytoplasm, by similarity only. The ISS source is mouse ATG4B
  (Q8BGE6), a paralog.

### Retractions
- PMID:12446702 (Human autophagins) was retracted (withdrawal PMID:30808002).
- PMID:17442669 (Atg4c-/- mice: diaphragm autophagy defect, fibrosarcoma
  susceptibility) was retracted in 2019. No mouse knockout phenotype is used.

### Decisions (summary)
- ACCEPT: autophagosome assembly (IBA, IDA), cysteine-type endopeptidase (IBA,
  IDA), cytoplasm (x3), protein processing (IBA), protein-PE deconjugating
  activity (IBA, IEA), protein delipidation (IDA).
- MODIFY: proteolysis -> protein processing; autophagy -> autophagosome
  assembly; cysteine-type peptidase activity (x3) -> cysteine-type endopeptidase
  activity.
- KEEP_AS_NON_CORE: mitophagy (IBA; target-specific evidence weak or negative),
  aggrephagy (IBA, worm donor).
- MARK_AS_OVER_ANNOTATED: piecemeal microautophagy of the nucleus (yeast-only
  donor, root-node propagation).
- REMOVE: protein binding (HTT, Y2H), per the GO:0005515 policy.

### For transfer to donkey ATG4C
Established experimentally in human ATG4C: protein-PE deconjugating activity /
protein delipidation (strong); cysteine-type endopeptidase priming (weak);
partial role in GABARAP priming and lipidation in autophagosome assembly.
Inferred only (IBA/ISS): cytoplasm, mitophagy, aggrephagy, piecemeal
microautophagy of the nucleus.
