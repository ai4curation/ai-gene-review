# dct-1 (Q09969) review notes

## 2026-10-10: PTHR15186 family pass, GOA refresh

### Context
GOA was refreshed with `just fetch-gene worm dct-1 --force`. New rows: IBA
mitophagy (GO:0000423), positive regulation of apoptotic process (GO:0043065),
mitochondrial fragmentation involved in apoptotic process (GO:0043653), all
from PAINT node PTN001032684, plus two WormBase IPI protein binding rows from
PMID:9824163 (with WB:WBGene00000417 = ced-3, WB:WBGene00000423 = ced-9;
mapping checked against `genes/worm/ced-3/ced-3-uniprot.txt` and
`genes/worm/ced-9/ced-9-uniprot.txt`). The following rows are gone from GOA
and were removed from the review: IBA GO:0043067 and GO:0097345, and
keyword IEAs GO:0006914 and GO:0006915 (GO_REF:0000043).

### Literature summary (with provenance)
- Mitophagy receptor: [PMID:25896323 "We find that DCT-1 is a key mediator of
  mitophagy and longevity assurance under conditions of stress in C. elegans"].
  The cached copy is abstract-only. Full-text details come from UniProt Q09969:
  OMM localization [file:worm/dct-1/dct-1-uniprot.txt "SUBCELLULAR LOCATION:
  Mitochondrion outer membrane"] and K26 ubiquitination [file:worm/dct-1/dct-1-uniprot.txt
  "Under oxidative stress conditions, ubiquitinated at Lys-26 in a pink-1
  dependent manner"]. The deep-research summary says DCT-1 "colocalizes with
  LGG-1/Atg8" and carries a WXXL motif [file:worm/dct-1/dct-1-deep-research-falcon.md].
  A web search (2026-10-10) confirmed WXXL and LGG-1 colocalization on the OMM
  in the Nature paper (Extended Data). I found **no direct binding assay and no
  LIR-mutant experiment**. The previous description claimed "direct binding to
  LGG-1", which I corrected. GO:0140580 is kept as a NEW proposal, now coded
  ISS rather than IDA.
- Apoptosis literature: [PMID:9824163 "In transiently transfected mammalian
  cells, ceBNIP3 complexes with CED-9"] and ["CeBNIP3 also efficiently
  heterodimerizes with the cell death protease proCED-3 by direct binding via
  the prodomain"]. Cizeau et al. found [PMID:11114722 "although ceBNIP3
  interacts with CED-9 and CED-3 it kills by a BH3- and caspase-independent
  mechanism"]. Every experiment in these papers is overexpression in mammalian
  cells. I found no in vivo worm study showing dct-1 affects developmental or
  germline apoptosis (web search 2026-10-10 returned none).

### Decisions on new and changed rows
- IBA mitophagy: ACCEPT. DCT-1 (WB:WBGene00015776) is itself a seed and has its own IMP.
- IBA positive regulation of apoptotic process: KEEP_AS_NON_CORE. Vertebrate
  seeds only, but ceBNIP3 keeps its pro-death capacity in heterologous cells,
  and WormBase curators annotated apoptotic process IMP from PMID:11114722.
  Removing it is not justified (do not overrule curators), and the data are
  too weak to call it core.
- IBA mitochondrial fragmentation involved in apoptotic process: REMOVE. Its
  only seed is human BNIP3 (PMID:20436456, mammalian), yet it was placed at
  the eumetazoan node. No invertebrate data exist. Loss of dct-1
  *produces* fragmentation through failed clearance (UniProt: "altered network
  morphology"), which is the opposite relationship.
- IBA nucleus: changed from UNDECIDED to MARK_AS_OVER_ANNOTATED with
  propagation_review, matching the BNIP3L review. There is no worm nuclear
  data, and the vertebrate nuclear pools are context-specific.
- Protein binding (four rows: CED-9 x2 UniProt/WB, CED-3 WB, CED-9 WB): REMOVE.
  CED-3 binding is already captured as protease binding. CED-9 binding goes
  through the TM domain, not the BH3-like domain, so BH3 domain binding would be wrong.
- Protease binding (CED-3) and the ternary complex: downgraded from ACCEPT to
  KEEP_AS_NON_CORE, because these are heterologous overexpression data with
  no in vivo role.

### PAINT (PTHR15186) as it applies to worm
Source: `interpro/panther/PTHR15186/PTHR15186-paint.tsv`.
- PTN001032684 (taxon:6072, Eumetazoa; not Bilateria): OMM, nucleus,
  mitophagy, positive regulation of apoptotic process, and mitochondrial
  fragmentation involved in apoptotic process. For worm, OMM and mitophagy are
  sound (worm and fly seeds). Positive regulation of apoptotic process is
  plausible but vertebrate-seeded. Nucleus and mitochondrial fragmentation
  involved in apoptotic process are over-placed.
- PTN000795991 (nuclear envelope, ER; taxon blank): dct-1 receives neither
  term in GOA, so these statements do not reach the worm gene. There is also
  no worm evidence for either location.
- PTN002689498 (taxon:117571, Euteleostomi; seed: human BNIP3 only) carries
  GO:0140580 adaptor activity, GO:0005789 ER membrane and GO:0061709
  reticulophagy. Worm does not inherit the adaptor activity. That reflects
  missing invertebrate binding data, not counter-evidence.
