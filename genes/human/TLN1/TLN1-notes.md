# TLN1 (talin-1, human, Q9Y490) review notes

Automated deep research was unavailable for this review (no provider keys), so no
`-deep-research-*.md` file exists. These notes are based on the UniProt record, the GOA
rows and the cached publications in `publications/` (most TLN1 primary papers are
abstract-only; full text was available for PMID:26923917, 21423176, 23382103, 25468996,
19608030, 35044719, 39009827, 20479219 and 29880641).

## Core biology

- Talin links integrins to actin: "Talin is a major link between integrin and the actin
  cytoskeleton and was shown to play an important role in focal adhesion assembly."
  [PMID:11279249]
- PI(4,5)P2 activates talin: "the interaction between integrin and talin was greatly
  enhanced by PI4,5P(2)-induced talin activation" [PMID:11279249]
- FERM head binds integrin tails: "Talin mediates integrin signaling by binding to integrin
  cytoplasmic tails through its FERM domain" [PMID:16546176]; "Talin‐1 (TLN1) is a
  cytoplasmic adapter protein necessary for integrin‐mediated cell adhesion" [PMID:35044719]
- Required for matrix junction assembly: "talin is essential for the assembly of such
  junctions" (integrin-mediated junctions with the extracellular matrix) [PMID:15494027]
- Vinculin activation: "all of talin VBSs activate vinculin by provoking helical bundle
  conversion of the Vh domain, which displaces the vinculin tail (Vt) domain" [PMID:15070891]
- Platelets: "lack of Talin-1 or Kindlin-3 in platelets has been shown to abrogate integrin
  α IIb β 3 activation with loss of platelet spreading and aggregation in vivo" [PMID:23382103]

## Adhesion rows (judged on human evidence)

- `cell-cell junction assembly` (ARBA IEA, and TAS PMID:15494027): the cited review is about
  junctions with the extracellular matrix, so MODIFY to `GO:0048041 focal adhesion assembly`.
- `adherens junction` (IMP, PMID:26923917): full text read. Talin is used as an FA marker and
  the peripheral colocalization is interpreted as "an increased vinculin presence at AJ"
  [PMID:26923917]. Marked over-annotated for talin.
- `cell-cell adhesion` (IBA, PTN000463398): unlike the sponge case (where the review changed
  a TreeGrafter cell-cell adhesion to cell-matrix adhesion), human talin does take part in
  integrin-mediated cell-cell adhesion: platelet aggregation (GO places GO:0070527 under
  GO:0098609) depends on talin-activated alphaIIb beta3. Kept as non-core.
- Added NEW `GO:0007160 cell-matrix adhesion`. Comparator check (QuickGO, human, exact):
  intracellular integrin partners ITGB1BP1, LIMS1, PPFIA2 carry it; talin does the work
  (binds and activates integrins, links them to actin).

## Protein binding rows

Integrin (ITGB1, ITGB3) and vinculin partners were MODIFIED to `integrin binding` /
`vinculin binding`. Others (EGFR, ERBB2, synemin, ANKRD1, THSD1, ARHGAP31 x2, PIP5K1C, RET x2)
REMOVED as uninformative; removal does not mean the interactions are false.

## Premetazoan context

- Talin is older than animals: "all scaffolding proteins involved in the integrin adhesion
  apparatus (that is, α-actinin, vinculin, paxillin, and talin) are common among unikonts"
  [PMID:20479219]; "Many of the scaffolding proteins (talin, vinculin, paxillin) most likely
  evolved in the common ancestor of amoebozoans and opisthokonts, where they had ancestrally
  different functions" [PMID:20479219].
- Dictyostelium talin already binds an NPxY motif: "it has been shown that the talin homolog
  of the amoebozoan D. discoideum interacts with an NPXY motif (the same motif found in
  integrin β) of the cytoplasmic tail of an adhesion molecule called SibA" [PMID:20479219].
- Capsaspora integrin beta subunits keep the talin-binding motif: "Both motifs are well
  conserved in C. owczarzaki integrin β1–β3" [PMID:20479219].
- Capsaspora adheres via integrins: "We show that integrin β2 and its associated protein
  vinculin localize as distinct patches in the filopodia." [PMID:32857975, abstract only;
  talin not mentioned in the abstract].
- Sponge (Oscarella pearsei): "Full-length Op vinculin and Op vinculin D1 bound Op talin
  peptide"; "In the presence of Op talin peptide, full-length Op vinculin bound to F-actin
  filaments" [PMID:29880641]. See genes/OSCPE/TLN and genes/OSCPE/VIN1.

Summary: ancestral (pre-animal, likely amorphean) = actin-binding cytoskeletal adaptor with an
NPxY-binding FERM head; integrin coupling was likely available in unicellular holozoans
(Capsaspora integrins with NPxY, integrin-mediated substrate adhesion) though talin itself
has not been tested there; talin-vinculin activation is present at the base of animals
(sponge). Animal-specific applications: focal adhesions in tissues, platelet aggregation,
leukocyte adhesion, muscle costameres/myotendinous junctions (N-RAP, synemin partners).

## GO-CAM

`gocams/index.tsv` has no entry for TLN1 / Q9Y490.

## Label note

GO:0008093 is "cytoskeletal adaptor activity" in current QuickGO; the local term cache still
has the older label "cytoskeletal anchor activity", which gives one validation warning.
