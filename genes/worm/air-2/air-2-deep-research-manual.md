# air-2 (O01427, AIR2_CAEEL): manual literature synthesis

No deep-research provider was run for this gene (no API keys in the session). This
synthesis was written by hand from the cached publications in `publications/`, the
UniProt record (`air-2-uniprot.txt`) and GO term lookups (QuickGO/OLS). Each claim
carries its source.

## Identity and family

- AIR-2 (Aurora/Ipl1-related kinase 2; also stu-7) is the single C. elegans Aurora B
  kinase, 305 aa, a member of the Ser/Thr protein kinase family, Aurora subfamily
  (UniProt SIMILARITY, PROSITE-ProRule PRU00159). Its paralog AIR-1 is the Aurora A
  kinase that sits on centrosomes [PMID:9852156 "AIR-1, like its relatives Eg2, IAK-1,
  and AIK-1, was also found to be associated with mitotic centrosomes"].
- stu-7 mutants, later shown to be air-2 alleles, are defective in post-embryonic and
  embryonic chromosome segregation but not in centrosome separation or bipolar spindle
  assembly [PMID:10354474 "is required for chromosome segregation though not for
  centrosome separation or for setting up a bipolar spindle"].

## Chromosomal passenger complex

- AIR-2 is the catalytic subunit of the C. elegans CPC with ICP-1 (INCENP), BIR-1
  (survivin) and CSC-1 (borealin-like) [PMID:12707312 "AIR-2/ICP-1/CSC-1/BIR-1 form a
  robust complex"]. ICP-1 is the activator; CSC-1/BIR-1 are targeting subunits
  [PMID:12707312 "ICP-1 dramatically stimulates AIR-2 kinase activity. This activity is
  not stimulated by CSC-1/BIR-1, suggesting that these two subunits function as
  targeting subunits for AIR-2 kinase."].
- Positive feedback: AIR-2 phosphorylates two adjacent serines in the ICP-1 C-terminus,
  and this phosphorylation is needed for ICP-1 to stimulate AIR-2 [PMID:12048181].
- BIR-1 is required for AIR-2 chromosome localization [PMID:10983970 "AIR-2 was not
  present on chromosomes in the absence of BIR-1"].
- Other regulators: TLK-1 is both substrate and activator (ICP-1-dependent)
  [PMID:15916946]; CDC-48.3 binds AIR-2 directly and inhibits its activity from metaphase
  to telophase [PMID:18854144]; LAB-1, via GSP-2/PP1, restricts AIR-2 to the
  interface between homologs in meiosis [PMID:18923084]; PP1 (GLC-7alpha/beta)
  antagonizes AIR-2 [PMID:11940606, PMID:10975519]; AIR-2 is SUMO-modified in vitro
  in a GEI-17-dependent manner [PMID:25475837].

## Kinase activity and substrates (direct, in vitro)

- REC-8 (meiotic cohesin) [PMID:11940606 "We show that AIR-2 phosphorylates REC-8 at a
  major amino acid in vitro."]
- ICP-1 (INCENP) C-terminal serines [PMID:12048181].
- BMK-1 (BimC kinesin) C-terminal tail [PMID:15548597].
- ZEN-4/MKLP1 C-terminal serines, in vitro and in vivo [PMID:15854913].
- TLK-1 Ser634 [PMID:15916946; UniProt FUNCTION].
- KLP-7 (kinesin-13) N-terminal region, with ICP-1 as co-activator [PMID:26168236].
- Histone H3 Ser10: AIR-2 is required for mitotic H3 phosphorylation; in vivo
  requirement rather than a cached in vitro assay [PMID:10975519 "both enzymes are
  required for H3 phosphorylation and chromosome segregation"; PMID:10983970].

## Localization

- Meiotic and mitotic chromosomes; in meiosis restricted to the mid-bivalent region
  (last points of contact between homologs, then sisters) [PMID:9852156; PMID:11940606;
  PMID:18923084].
- In mitosis on metaphase chromosomes, then central spindle/midzone in anaphase, then
  midbody, where it persists [PMID:9852156 "AIR-2 is found on metaphase chromosomes,
  moves to midbody microtubules at anaphase, and then persists at the cytokinesis
  remnant"; PMID:23684975; PMID:25475837].
- In meiosis the CPC lies in the gap between the kinetochore cups, i.e. not on the
  kinetochore itself [PMID:20729837].
- Not centrosomal (contrast with AIR-1) [PMID:9852156].

## Biological roles

- Mitotic chromosome segregation and metaphase congression [PMID:10983970;
  PMID:11050384; PMID:12707312].
- Meiotic chromosome separation: required for REC-8 release and homolog/sister
  separation at both meiotic anaphases [PMID:11940606].
- Recruitment of the ring-domain network (BUB-1 and downstream) in meiosis, and
  microtubule assembly between separating meiotic chromosomes [PMID:20729837].
- Cytokinesis: furrows initiate and regress; AIR-2 acts at metaphase/early anaphase to
  localize ZEN-4, in a pathway parallel to CYK-1 [PMID:9852156; PMID:11050384];
  phosphorylation of ZEN-4 by AIR-2 is needed for completion of cytokinesis
  [PMID:15854913]. AIR-2 is also required for localization of BMK-1 to spindles
  [PMID:15548597] and of CDC-14 to the central spindle [PMID:12213836].
- Chromatin bridges hyperactivate AIR-2 at the midzone/midbody, which recruits
  condensin I and prevents furrow regression [PMID:23684975].
- Condensin SMC-4 loading on mitotic chromosomes requires AIR-2 [PMID:11914278,
  abstract only; via UniProt FUNCTION].

## Not supported in C. elegans

- Spindle assembly checkpoint function and positive regulation of mitotic sister
  chromatid separation: asserted by ComplexPortal (NAS, PMID:12707312) by analogy; no
  worm data examined in cached literature.
- Centrosome/spindle pole localization: Aurora A (AIR-1) property, not AIR-2.
