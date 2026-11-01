# murP (yfeV, b2429, P77272) notes

## 2026-10-31 — initial review

No deep-research file. Sources: UniProt P77272, PMID:15060041 and PMID:15919996
(abstracts only in cache), PMID:18723630 (full text), PMID:16452451 (abstract).

### Identity
- PTS glucose-family EIIBC fusion: EIIB type-1 domain (1-89, active-site Cys29,
  phosphocysteine) and EIIC type-1 domain (115-474, 10 TM helices); no EIIA domain
  (UniProt; PROSITE PS51098, PS01035, PS51103).
- Requires the crr-encoded EIIA-Glc as phosphoryl donor, plus EI and HPr
  [PMID:15060041 "MurP lacks an EIIA domain and was found to require the activity of the crr-encoded enzyme IIA-glucose (EIIA(Glc)), a component of the major glucose transport system for growth on MurNAc."].

### Function
- Transports and phosphorylates MurNAc to cytoplasmic MurNAc 6-phosphate (EC 2.7.1.192)
  [PMID:18723630 "The PTS translocates the amino sugar across the cell membrane while phosphorylating it, receiving the phosphate ultimately from phosphoenolpyruvate and yielding intracellular MurNAc-6-phosphate (MurNAc-6-P)."].
- ΔmurP cannot grow on MurNAc; complemented in trans [PMID:15060041].
- Also takes up anhMurNAc but cannot phosphorylate it (1,6-anhydro ring blocks C6);
  AnmK then phosphorylates it [PMID:18723630 "AnhydroMurNAc can also be taken up by MurP, but in contrast to MurNAc this sugar is not phosphorylated by the PTS"].
  GO has no anhMurNAc transport term; not annotated.
- Inner membrane: His6-MurP isolated from membranes [PMID:15060041]; C-terminal
  PhoA/GFP topology mapping of the inner membrane proteome [PMID:15919996].
- murQP(-pbp4B) operon repressed by MurR, induced by MurNAc-6P, activated by cAMP-CAP
  [PMID:18723630].

### GO term notes
- GO:0090588 (protein-phosphocysteine-N-acetylmuramate PTS transporter activity) is
  the specific MF; it is_a GO:0090563 protein-phosphocysteine-sugar phosphotransferase
  activity, not a descendant of GO:0008982 (the phosphohistidine-donor form). Both
  describe the same EIIBC; GO:0008982 rows MODIFY to GO:0090588.
- GO:0009401 PTS is_a GO:0034219 carbohydrate transmembrane transport.
- Did not add GO:0097173 N-acetylmuramic acid catabolic process as NEW for MurP: the
  PTS phosphorylation is arguably the first catabolic step (UniPathway UPA00342), but
  the convention for PTS EII components is to annotate the transport/PTS process; left
  as a question.
