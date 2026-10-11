# NDI1 (YML120C, P32340) review notes

## Provenance / process

- Data fetched with `just fetch-gene yeast NDI1`; publications cached with `just fetch-gene-pmids yeast NDI1`.
- Additional papers cached with `ai-gene-review fetch-pmid`: PMID:9689052 (Seo et al. 1998, full text),
  PMID:11479321 (Bai et al. 2001, abstract), PMID:9733747 (Luttik et al. 1998, abstract),
  PMID:11152939 (Bakker et al. 2001 review, abstract).
- Deep research: `just deep-research-falcon yeast NDI1 --fallback perplexity-lite` was launched
  (see end of file for outcome). The review below is based on my own reading of the cached
  publications and PubMed searches, not on a deep-research file.
- Context: chosen from projects/MITOTOL.md, based on Chen et al. 2026 (PMID:42822426), a
  comparative mitochondrial proteome study. That paper is not annotation evidence for NDI1 function.

## Identity and biochemistry

- Single-subunit, ~53 kDa, FAD-containing, rotenone-insensitive NADH:ubiquinone oxidoreductase
  (type II NADH dehydrogenase, NDH-2), EC 1.6.5.9 [PMID:3138118 "The purified NADH dehydrogenase consists of a
  single subunit with molecular mass of 53 kDa"; "The enzyme contains FAD, non-covalently linked, as the sole"].
- Specific for NADH, inhibited by flavone but not rotenone or piericidin
  [PMID:3138118 "by flavone (I50 = 95 microM), but not by rotenone or piericidin"]; uses several quinones,
  with natural UQ6 turnover ~500 s-1.
- Note: de Vries & Grivell (1988) initially suggested the purified enzyme was the *external* enzyme;
  the gene cloning and disruption paper (Marres et al. 1991) established that the same enzyme is the
  *internal* one, oxidising NADH generated inside the mitochondrion
  [PMID:1900238 "this NADH dehydrogenase catalyzes the oxidation of NADH generated inside"].
  So the SGD IDA for GO:0120555 from PMID:3138118 is correctly attached to NDI1.
- No proton pumping: transfers electrons from NADH via FAD to quinone without proton translocation
  [PMID:22949654 "transfer of an electron from NADH via FAD to quinone, without proton pumping."];
  consistent with reduced P:O in NDI1-expressing human cells [PMID:11479321 "as expected from the lack of proton pumping activity"].
- Hence the correct MF is GO:0120555 NADH dehydrogenase (ubiquinone) (non-electrogenic) activity
  (child of GO:0050136, which is a child of GO:0003954). GO:0008137 (NADH dehydrogenase (ubiquinone)
  activity) is defined with proton translocation (4 H+ out) and is the complex I term; it is NOT
  annotated to NDI1 (checked GOA file), which is correct. No complex I CC term (GO:0045271) is
  annotated to NDI1 either - also correct.

## Location / topology

- Nuclear-encoded, 26-residue mitochondrial presequence (UniProt TRANSIT 1..26).
- Monotopic/peripheral inner-membrane protein, catalytic site on the matrix side
  [PMID:22949654 "The Ndi1 protein from Saccharomyces cerevisiae is a monotopic membrane protein,"];
  [PMID:9733747 "dehydrogenase, the catalytic side of which projects to the matrix side of the"].
- Same matrix-facing topology when expressed in hamster/human cells
  [PMID:9689052 "enzyme was located on the matrix side of the inner mitochondrial membranes."].
- Found in a native-gel supramolecular dehydrogenase assembly with external dehydrogenases and TCA enzymes
  [PMID:11502169]; this is a co-migration observation, not an obligate complex.
- Cytosol (RCA from YeastPathways PWY3O-188 GO-CAM conversion) is wrong: the GO-CAM import
  (gocams/index.tsv row gomodel:RXN3O-165) places the activity in cytosol, which contradicts the
  established matrix-side topology.

## Structure

- Crystal structures (Iwata et al. 2012; Feng et al. 2012): dimer, amphipathic membrane anchor formed by dimer
  packing, overlapping NAD+ and quinone binding sites [PMID:22949654]; homodimerization through the C-terminal
  domain is critical for activity and membrane targeting; two UQ sites [PMID:23086143 "We find that Ndi1 homodimerization"].
- The IPI "identical protein binding" rows are best expressed as protein homodimerization activity (GO:0042803).

## Physiology

- Main entry point of matrix NADH into the respiratory chain in yeast, which lacks complex I
  [PMID:9689052 "It is the main entry point into the respiratory chain in this organism, just as complex I is in mammalian mitochondria"].
- ndi1 null: growth on glucose and ethanol unaffected, lactate/pyruvate/acetate impaired [PMID:1900238].
- Part of a set of parallel NADH reoxidation routes (internal Ndi1 for matrix NADH; external Nde1/Nde2 and
  Gut2 shuttle for cytosolic NADH) [PMID:11152939; PMID:9733747].
- Complements complex I deficiency in mammalian cells and animals [PMID:9689052; PMID:11479321; PMID:16543240 (not cached)].

## Apoptosis / ROS (Li et al. 2006, PMID:16436509)

- Overexpression of NDI1 (not NDE1) causes apoptosis-like death, associated with mitochondrial ROS, suppressed by
  respiration on glucose-limited media and by interrupting ETC components; deletion lowers ROS and extends
  chronological lifespan. These are gain-of-function / pleiotropic effects consistent with Ndi1 being a
  flavin-containing NADH oxidising enzyme that can leak electrons; there is no evidence that Ndi1 acts in a
  regulated apoptotic signalling step. The GO:0043065 IMP annotation is therefore treated as over-annotation
  (not removed: experimental, full text not cached).

## Evolutionary context (Chen et al. 2026, PMID:42822426)

- Comparative analysis reconstructs NDH2 in LOCA/LECA mitochondria; retained in yeast, lost in humans
  [PMID:42822426 "mitochondria inherited NDH2, amino acid and cofactor biosynthetic pathways"].
- NDH2 recovered as a candidate pathogen drug target absent from human mitochondria. Background only.
- Human AIFM1/AIFM2 are distantly related flavoproteins (NDH-2/AIF superfamily); human has no orthologous NDH-2.

## Decisions summary

- ACCEPT: MF terms GO:0120555 (x3), GO:0050136, GO:0003954, GO:0016491 (x2, general); BP GO:0006120,
  GO:0019646, GO:0015980; CC mitochondrion (x5), inner membrane, matrix (x2).
- MODIFY: GO:0042802 identical protein binding (x2) -> GO:0042803 protein homodimerization activity.
- MARK_AS_OVER_ANNOTATED: GO:0043065 positive regulation of apoptotic process.
- REMOVE: cytosol (RCA, YeastPathways GO-CAM conversion artifact).
- NEW: GO:0071949 FAD binding; GO:0099617 matrix side of mitochondrial inner membrane.

## Deep research outcome (2026-10-09)

`timeout 1500 just deep-research-falcon yeast NDI1 --fallback perplexity-lite` FAILED:
falcon timed out at the wrapper's 600 s limit, and the perplexity-lite fallback failed with
"Provider 'perplexity' not available. Available: falcon, asta, openscientist". No deep-research
file was produced (the orphaned falcon client process was killed). The review relies on the cached
publications listed above plus the reviewer's own PubMed searches (PubMed MCP).
