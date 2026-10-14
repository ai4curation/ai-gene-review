# id3-a (Xenopus laevis, Q91399) — review notes

## 2026-10-01 — initial review (NEURAL_CREST_ORIGINS project, Tier 1)

### Identity
- Q91399, ID3A_XENLA, 118 aa, Id3 L-homeolog (Xenbase id3.L). Homeolog id3-b = Q7SZ28.
  Old names XIdI/XIdIa/XIdIb/XIdx/XId3 (UniProt).
- Single HLH domain (32-84) with no basic region; V59N mutation disrupts HLH and reduces
  ability to inhibit bHLH complex formation [PMID:7734394, via UniProt FT].
- PANTHER PTHR11723:SF16 (DNA-binding protein inhibitor ID-3).
- The older literature says "Xenopus Id3" without discriminating L/S homeologs; morpholinos
  and probes very likely hit both. All experimental GO rows sit on id3-a only; id3-b
  (Q7SZ28) carries ISS copies of them (QuickGO, 17 rows, all IBA/ISS/IEA). Homeolog split
  noted, not "fixed".

### Molecular activity (dominant-negative HLH)
- Ids lack the basic region and inhibit bHLH factors [PMID:7619724 "The activity of bHLH
  transcription factors that are involved in cell determination and differentiation is
  inhibited by Ids, HLH proteins lacking the basic amino acid sequence element."]
- XIdx (= Id3) "disrupts binding of myogenic factor/E-protein complexes to DNA in vitro and
  inhibits transactivation of the E-box regulated cardiac actin gene by MyoD in embryonic
  tissue" [PMID:7734394]. This is the direct biochemical evidence: an inhibitor of
  DNA-binding of bHLH dimers, i.e. a transcription regulator inhibitor, not a DNA binder.
- Partner selectivity in animal caps: "Id3 blocks only neuroD activity in our assays"
  [PMID:14651922] (Id4 broad, Id2 MyoD+NeuroD).
- Non-canonical partners in the neural plate border (NPB): Hairy2/Hes4 ("Id3 protein, which
  physically interacts with Hairy2, negatively regulates Hairy2 activity" [PMID:18721802])
  and Stat3/FGFR4 ("Hairy2 and Id3 proteins that, respectively, facilitate and disrupt
  Stat3-FGFR4 complex formation" [PMID:19851287]). So Id3 acts as an inhibitor of several
  transcription regulators by sequestration, the same molecular logic as with E proteins.
- Human/mouse ID proteins carry `GO:0140416 transcription regulator inhibitor activity`
  (IDA for ID1 PMID:17681138, ID2 mouse PMID:10652346, ID4 PMID:7665172; QuickGO check).
  The IBA `GO:0003714 transcription corepressor activity` is a poor fit: the corepressor
  definition requires binding a DNA-bound TF at a genomic locus, whereas Id proteins prevent
  bHLH partners reaching DNA.

### Expression
- Maternal low, zygotic after MBT, widespread at gastrula, then neural plate border,
  premigratory and migratory NC, anterior neural plate, eye, otic, myotome, etc. [UniProt;
  PMID:7619724 "in a large number of tissues, including the notochord, neural tube, eye,
  ear, neural crest cells, presomitic mesoderm, myotomes, tailbud and dorsal fin"].
- "Id3 is localized at the neural plate border during gastrulation and neurulation,
  overlapping the domain of neural crest induction" [PMID:15769946].
- Blastula: co-expressed with Oct/Sox/Vent pluripotency factors; "expression of Vent2 and
  Id3 was unchanged as explants aged from blastula to gastrula stages" [PMID:25931449];
  Snail1 block in animal cap "led to loss of expression of factors linked to the neural
  crest state, such as TF-AP2 and Id3" [PMID:25931449].

### Upstream regulation (inputs, not Id3 functions)
- BMP4 induces Id3 [PMID:14651922 "expression of Id3 and Id4 can be induced by
  overexpression of BMP4"]; Notch activates Id3 [PMID:14651922]; Myc target
  [PMID:15772131 "Id3 is a Myc target"]; Hairy2 represses Id3 via BMP attenuation
  [PMID:18721802]; Stat3 levels control Id3 transcription [PMID:19851287].

### Loss/gain of function in the NC
- MO knockdown: "depletion of Id3 results in the absence of neural crest precursors and a
  resultant loss of neural crest derivatives" mediated "by cell cycle inhibition followed by
  cell death of the neural crest progenitor pool, rather than a cell fate switch"
  [PMID:15769946]. Overexpression "increases cell proliferation and results in expansion of
  the neural crest domain" [PMID:15769946]. Authors: "independent of cell fate
  determination".
- Light et al.: "A morpholino-mediated 'knockdown' of Id3 protein results in embryos that
  lack neural crest" and "forced expression of Id3 maintains the expression of markers of
  the neural crest progenitor state beyond the time when they would normally be
  downregulated and blocks the differentiation of neural crest derivatives" [PMID:15772131].
- Deep research (falcon): Id2 MO did not phenocopy; chick Id3 rescued; p27Xic1 up on Id3
  depletion. [file:XENLA/id3-a/id3-a-deep-research-falcon.md]

### Network layer placement
- NOT a neural plate border specifier: Id3 is downstream of the border signals (BMP, Notch,
  Wnt/BMP balance, Myc, Hairy2, Stat3) and does not specify the border.
- NOT a classical NC fate specifier like Snai2/FoxD3/Sox10: its depletion kills/arrests
  progenitors rather than switching fate, and it does not bind DNA.
- Best placement: **NC progenitor maintenance/competence factor** — it keeps NPB/NC
  progenitors cycling and undifferentiated (Myc–Id3 axis), and is part of the blastula
  potency programme that the crest retains [PMID:25931449 "This model is supported by a
  shared requirement for Myc protein, and its transcriptional target Id3, in both neural
  crest cell genesis and ES cell pluripotency"].
- GO consequence: keep `GO:0014029 neural crest formation` (broad and appropriate);
  do NOT push to `GO:0014036`/`GO:0014034` fate specification/commitment. Add direction to
  cell-cycle (`GO:0045787 positive regulation of cell cycle`) and differentiation
  (`GO:0045596 negative regulation of cell differentiation`). "Stem cell population
  maintenance" (`GO:0019827`) is plausible but not proposed as NEW — raised as question
  (only co-expression evidence in blastula; NC-specific evidence is marker maintenance).

### Evolution
- Meulemans et al. 2003 [PMID:14651928]: "while expression of Id genes in the mesoderm and
  endoderm is conserved between amphioxus and vertebrates, expression in the lateral neural
  plate border and dorsal neural tube is a vertebrate novelty"; "recruitment of Id genes to
  these cells occurred very early in the vertebrate lineage" (lamprey). So the protein
  activity is ancestral (HLH inhibitor), the NC deployment is a co-option — a *cis*-
  regulatory/deployment change, not a new molecular function. This is a clean example of
  the co-option model for the project synthesis.

### Annotation decisions (summary)
- circadian regulation (TreeGrafter IEA): REMOVE — derives from Id2-specific mammalian data
  (mouse Id2 IMP PMID:19740747; human ID2 ISS); human ID3 itself has no circadian
  annotation; no Xenopus evidence.
- protein binding (Stat3 IPI): REMOVE (uninformative); functional content captured by
  transcription regulator inhibitor activity.
- transcription corepressor activity (IBA): MODIFY -> GO:0140416.
- negative regulation of Pol II transcription IPI with Hairy2: UNDECIDED — Id3 inhibits a
  repressor (Hairy2), so the direction is not obviously negative; abstract only.
