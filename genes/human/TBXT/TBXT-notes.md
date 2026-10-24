# TBXT (Brachyury, O15178) review notes

Automated deep research was unavailable for this review (no deep-research provider
keys); these notes are compiled manually from the UniProt record, the GOA file, and the
cached publications in `publications/`. Full-text availability is noted per paper.

## Sources read

| PMID | Full text? | Use |
|------|-----------|-----|
| 8963900 | abstract only | cloning of human T; expression confined to notochord-derived cells |
| 21632880 | abstract only | Brachyury directly binds/activates MesP1 promoter (EMSA, ChIP, reporter); mouse ESCs |
| 22164283 | yes | Brachyury (incl. human T) binds Mixl1 homeodomain and represses Mixl1 transactivation |
| 22611028 | yes | nuclear Brachyury in human lung tumours (fractionation, IHC) |
| 24253444 | abstract only | human SAVA syndrome: T-box H171R reduces DNA binding; notochord canal persists |
| 28473536 | yes (main text only) | HT-SELEX of 542 human TFs (source of the GO:1990837 IDA); TBXT result is in supplementary data, not in cached text |
| 18593560 | abstract only | Mesp1 master regulator paper; abstract does not mention Brachyury |
| 24043797 | yes | premetazoan T-box evolution; Capsaspora Brachyury (CoBra) |

## Molecular function

- UniProt (by similarity to mouse P20293): binds the palindromic T site
  5'-TTCACACCTAGGTGTGAA-3' and activates transcription from it; T-box DNA-binding
  domain residues 51-219.
- Human/mouse direct target: [PMID:21632880 "We finally defined a 3.4 kb proximal
  MesP1-promoter fragment which is directly bound and activated by Brachyury(T) via a T
  responsive element as shown via bandshift, chromatin immuneprecipitation, and reporter
  assays."] -> GO:0000978, GO:0000981, GO:0045944, chromatin.
- Activator: [PMID:22164283 "Brachyury (T), the founding member of the T-box (Tbx)
  family, is a transcriptional activator and is expressed throughout the nascent mesoderm,
  tailbud and notochord [20]–[23]."] Supports GO:0001228 (activator) as a more precise
  MF than GO:0000981; proposed as NEW.
- Human disease variant in the T-box impairs DNA binding: [PMID:24253444 "The homozygous
  mutation results in diminished DNA binding, increased cell growth, and interferes with
  the normal expression of genes involved in ossification, notochord maintenance and
  axial mesoderm development."]
- Partner-TF interaction (secondary): [PMID:22164283 "Here we report that Mixl1 interacts
  physically and functionally with the T-box protein Brachyury and related members of
  the T-box family of transcription factors."]; the repression of Mixl1 does not use T
  sites [PMID:22164283 "Inspection of the Gsc promoter did not reveal consensus DNA
  binding sites for Brachyury [22], [23], suggesting that Brachyury was not directly
  binding to the Gsc promoter to regulate Mixl1 activity."]. This is the basis of the
  mouse IDA/IPI annotations (BHF-UCL) that were transferred to human by ISS
  (GO:0003714, GO:0000122, GO:0061629, GO:0000978). Kept as non-core; the corepressor
  claim is from overexpression reporter assays.

## Location

- Nucleus: [PMID:22611028 "a single band at the expected molecular weight was observed in
  nuclear fractions derived from the primary tumor of two lung cancer patients
  evaluated"]; also cytoplasmic staining in invading tumour cells.

## Biological process

- Mesoderm formation and axial development [PMID:8963900 "T protein is vital for the
  formation of posterior mesoderm and axial development in all vertebrates."];
  [PMID:8963900 "Brachyury mutant mice, which lack T protein, die in utero with abnormal
  notochord, posterior somites, and allantois."]
- Notochord: human SAVA syndrome with persistent notochordal canal (PMID:24253444);
  mouse T carries GO:0030903 notochord development by IMP (MGI, PMID:15384171,
  PMID:8155581, PMID:8293872; checked in QuickGO 2026-10-01). Human lacks this term in
  GOA, so it is proposed as NEW (comparator check: the mouse ortholog carries it by
  IMP; this is a gap in transfer, not a convention against TFs carrying the term).
- Cardiac: Brachyury acts upstream of MesP1 in cardiovascular progenitor specification
  [PMID:21632880 "shRNA-based loss of Brachyury(T) causes a dramatic decrease in MesP1
  expression accompanied by reduced cardiac markers in differentiating embryonic stem
  cells"]. Heart morphogenesis and cardiac myoblast differentiation are therefore
  indirect, early-mesoderm consequences; kept as non-core.
- Primitive streak formation (NAS PMID:18593560): the cached Mesp1 abstract does not
  mention Brachyury. Brachyury is expressed in the streak [PMID:22164283 "Mixl1 and
  Brachyury are both expressed in the primitive streak"]. Kept as non-core rather than
  removed (full text not available; plausible biology).
- Signal transduction (NAS PMID:8963900): nothing in the abstract supports it; TBXT is a
  nuclear TF, not a signal transducer. Removed.

## GO-CAM

`gocams/index.tsv` has no rows for TBXT / O15178 (checked 2026-10-01).

## Premetazoan evolution (PMID:24043797, full text)

- T-box genes are of opisthokont origin; Brachyury is the oldest class: [PMID:24043797
  "Our data confirm that Brachyury is the most ancient member of the T-box family and
  establish that the T-box family diversified at the onset of Metazoa."]
- Present in filastereans (Capsaspora, Ministeria), ichthyosporeans and early-branching
  fungi; lost in Dikarya and choanoflagellates: [PMID:24043797 "We did not identify T-box
  genes in either of the two sequenced choanoflagellates (the colonial Salpingoeca
  rosetta and the unicellular Monosiga brevicollis ), confirming that T-box genes were
  also lost in this group ( 16 )."] So no choanoflagellate Brachyury is known; the
  absence is interpreted as secondary loss.
- CoBra partially rescues dominant-negative XBra: [PMID:24043797 "Our data show that C.
  owczarzaki Brachyury ( CoBra ) can partially rescue Xenopus laevis embryos injected with
  a dominant negative XBra construct."] The authors caution that the XBra_En construct
  may hit other T-box genes, and the Tbx7-class CoTbx3 rescues equally well.
- CoBra lacks target specificity: it strongly activates all mesendodermal genes,
  including chordin, which metazoan Brachyury (sponge, cnidarian, frog) does not
  activate ("pan-Tbox" behaviour).
- DNA-binding motif conserved: [PMID:24043797 "Our results indicate that CoBra has a
  highly similar motif to that determined in the mouse Bra-homolog, called T ( Fig. 4 )
  ( 28 , 34 – 36 )."]
- Specificity mapped to the N- and C-terminal regions outside the T-box (chimera
  CoBra-XBra-CoBra behaves like CoBra), and attributed to cofactor interactions (e.g.
  Smad1, absent from Capsaspora).

**Ancestral vs animal-specific for human TBXT:**
- Ancestral (pre-metazoan, at least Holozoa/opisthokont): sequence-specific binding of
  the T-box motif and the capacity to activate transcription from it (GO:0000978,
  GO:0000981/GO:0001228, nucleus/chromatin).
- Animal-specific: target-gene specificity (restricted, cofactor-dependent target
  set), and all developmental process roles (mesoderm formation, notochord
  development, somitogenesis, primitive streak, cardiac progenitor specification).
  Notochord roles are chordate-specific. Capsaspora is unicellular, so these process
  terms cannot apply to CoBra; its endogenous function is unknown.
