# npp-20 (Y77E11A.13; SEC13 homolog) — curation notes

UniProt Q9N4A7 (Swiss-Prot), WBGene00003806. 313 aa, six WD40 repeats, Sec13/Seh1 family
(InterPro IPR037363; PANTHER PTHR11024:SF2 "PROTEIN SEC13 HOMOLOG"). Isoform b is truncated
(lacks residues 212-313).

Deep research: `just deep-research-falcon` fails (auth) in this environment, so the literature
research below was done manually via PubMed searches and cached publications. No
`-deep-research-*.md` file was created.

## Literature

PubMed search `(npp-20 OR "SEC-13" OR Sec13) AND "Caenorhabditis elegans"` returned only four
records (2026-10-19): PMID:28122936, PMID:25452588, PMID:27203176 (ULK/SEC16A, mammalian focus),
PMID:42686406 (human SEC13 NMD follow-up). The GOA references add PMID:12937276 and PMID:21478858.

### Galy et al. 2003, MBoC (PMID:12937276) — nucleoporin RNAi survey

- Cached file is abstract-only (`full_text_available: false`; PMC refuses XML download for MBoC
  2003). I read the full text from the PMC HTML page (PMC284812) on 2026-10-19.
- Table 1 lists npp-20 = Y77E11A.13a, "Sec13R", 100 ± 0 % embryonic lethality (n = 588), nuclear
  morphology defect "++".
- Results text (full text, PMC284812): "In embryos depleted of CeSec13R, nuclear morphology was
  very irregular ( Figure 1N and Table 1 ). However, in contrast to the other genes analyzed here,
  RNAi against CeSec13R caused additional severe defects in embryonic appearance and blocked
  cytokinesis. Presumably these effects are due to pleiotropic functions of Sec13, which is
  localized both to the NPC and to the COPII coat involved in endoplasmic reticulum transport"
- Discussion (full text): "RNAi depletion of CeNup35, -98/96, -153, -155, -160, -358, or CeSec13
  seemed to completely block nuclear formation after the first mitosis."
- Localization (full text): "elegans nucleoporins have been confirmed to localize to the nuclear
  periphery as expected (see Supplementary Figure 1 )" — basis of the IDA nuclear pore row.
- UniProt has synced this as curated text: [file:worm/npp-20/npp-20-uniprot.txt "Cytokinesis is
  blocked and nucleus formation is impaired after the first embryonic mitosis (PubMed:12937276)"].

**Verdict on GO:0010973 positive regulation of division septum assembly (Wei et al. 2020,
PMID:32470107 flag):** the only phenotype in the paper that maps to cell division is "blocked
cytokinesis" in RNAi one-cell embryos. The UniProt curator evidently mapped "cytokinesis blocked"
onto a septum-assembly regulation term. Division septum assembly (GO:0000917 and regulation
children) is defined for fungal/bacterial septation and is not appropriate for a nematode
embryo. The phenotype itself is real (direct observation, DIC), so the row should be MODIFIED to
an animal cytokinesis term (GO:0000281 mitotic cytokinesis; the first embryonic division is
mitotic), not removed. The authors themselves attribute the cytokinesis block to pleiotropy
(COPII/secretion function), so this is a non-core, likely indirect, role. Wei et al.'s flag on the
term is correct in substance (wrong taxon-specific term), but the underlying experimental
observation is sound.

### Witte et al. 2011, Nat Cell Biol (PMID:21478858) — TFG-1 and COPII

- SEC-13 (= NPP-20) used as COPII marker in C. elegans germline: [PMID:21478858 "In control
  animals, the COPII subunit SEC-13 is found in close apposition to SEC-16 labeled exit sites and
  on the nuclear envelopes of proliferating germ nuclei"].
- Immuno-EM: [PMID:21478858 "Dual immuno-gold labeling with TFG-1 and SEC-13 antibodies indicated
  that both proteins localize to an identical area next to ER exit sites, although the SEC-13
  labeling was more discrete"].
- Native SEC-13 in a 54 Å complex [PMID:21478858 "which likely corresponds to a SEC-13-SEC-31
  heterotetramer that was described previously"]; TFG-1 depletion shifts SEC-13 to monomer.
- Nuclear envelope pool independent of TFG-1: [PMID:21478858 "while localization of SEC-13 to the
  nuclear envelope was largely unaffected"].

### Ferreira et al. 2017, J Cell Sci (PMID:28122936) — HCP-4 import

- Abstract only cached. [PMID:28122936 "Following the knockdown of NPP-10, NPP-13 and NPP-20,
  HCP-4 remains in the cytosol throughout prophase due to stalled import."]
- Centromere/sister-centromere resolution defects are explained by failed HCP-4 (CENP-C) nuclear
  import [PMID:28122936 "These results indicate that correct timing of the availability of HCP-4
  by nuclear import is essential."]. So the GO:1990893 centromere condensation row is a downstream
  consequence of the import defect, not a function of NPP-20 in chromatin compaction.

### Casadio et al. 2015, EMBO Rep (PMID:25452588) — NMD screen

- npp-20 identified in a C. elegans RNAi screen for NMD factors; human SEC13 required for NMD
  [PMID:25452588 "Importantly, we show that two human homologs, GNL2 (ngp-1) and SEC13 (npp-20),
  are also required for NMD in human cells."]
- Worm RNAi phenotype: [PMID:25452588 "Depletion of npp-20 resulted in worms arrested at L2–L3
  larval stages."]
- Not proposed as a NEW annotation: mechanism unknown, may be indirect (NPC export/ER), and the
  2026 follow-up (PMID:42686406, human cells) is outside this worm review.

### GATOR2 / TORC1

- Human SEC13 is a GATOR2 subunit [PMID:23723238 "inhibition of GATOR2 subunits (Mios, WDR24,
  WDR59, Seh1L, and Sec13) suppresses mTORC1 signaling"]. No worm-specific data on NPP-20 in
  GATOR2/TORC1; the IBA and ISS rows (lysosomal membrane, positive regulation of TOR signaling)
  rest on orthology.

## Action summary

See npp-20-ai-review.yaml. Core: structural constituent of NPC outer ring (Y-complex) and COPII
outer coat (with SEC-31); protein import into nucleus; COPII vesicle budding.
