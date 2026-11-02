# rab-11.1 review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene worm rab-11.1`; UniProt O01803 (RB11A_CAEEL) confirmed; 35 GOA rows.
- Cached 11 GOA PMIDs plus PMID:23840591 (GBF-1 paper, full text). Full text available:
  PMID:18385514, PMID:24843160, PMID:10588660, PMID:23840591. Abstract only: PMID:18765566,
  PMID:26506309, PMID:19158384, PMID:22634595, PMID:18472420, PMID:17704769, PMID:11378383,
  PMID:10508579.
- No deep research run (no API keys). Manual synthesis in `rab-11.1-deep-research-manual.md`.

### PMID:23840591 (GBF-1)
Not a GOA source for rab-11.1. Uses RAB-11.1::GFP as a recycling-endosome marker in oocytes;
states RAB-11.1 is "the Rab GTPase essential for recycling from endosomes to the plasma membrane"
[PMID:23840591] and shows labelled recycling endosomes reach the oocyte plasma membrane.
Supports recycling-endosome localization and the endocytic recycling role (background statement,
not a new experiment on rab-11.1 function).

### Key decisions
- GTPase activity / GTP binding: accepted (Rab11 subfamily, P-loop residues, REI-1 GEF prefers GDP form).
- endosome (EXP, IEA): MODIFY to recycling endosome (the cited paper says RAB-11-labelled recycling endosomes).
- centrosome, spindle (IEA from UniProt SubCell): MARK_AS_OVER_ANNOTATED. The evidence
  [PMID:18385514 "cytoplasmic puncta, around centrosomes, and at the periphery of the mitotic spindle"]
  shows recycling endosomes clustered near these structures, not the protein in them.
- apical plasma membrane (EXP PMID:24843160, IEA): full text says "apically enriched, is primarily
  cytosolic"; RAB-11 coats spore compartments that fuse with the apical PM. No direct PM residency
  shown. MODIFY to apical part of cell (GO:0045177).
- transport vesicle (IEA, from SubCell "secretory vesicle"): the secretory vesicles are cortical
  granules; MODIFY to cortical granule (GO:0060473). transport vesicle is not an ancestor of
  cortical granule in GO, so this is a lateral correction.
- receptor-mediated endocytosis (IMP PMID:10588660): authors interpret as receptor recycling
  defect; MODIFY to endocytic recycling (GO:0032456).
- obsolete GO:0061796 membrane addition at site of mitotic cytokinesis: QuickGO says obsolete,
  consider GO:0006887. Replaced with mitotic cytokinesis (GO:0000281), which the gene already
  carries by IMP. Abstract of PMID:11378383 is about BFA only; curator presumably used rab-11
  RNAi data in full text (not cached).
- embryo development (IMP lethality), eggshell formation: KEEP_AS_NON_CORE (downstream outcomes).
- No NEW rows. Endocytic recycling enters only via MODIFY of the RME row.

### Open points
- Spindle alignment role (PMID:18385514) is a phenotype with unclear mechanism; not annotated.
- Plasma membrane repair after Cry5B (PMID:21320697) not cached; not annotated.

## Description follow-up (2026-10-30)
- PMID:21320697 (Los et al. 2011) is now cached, with full text. Diluted rab-11.1 RNAi makes animals hypersensitive to the pore-forming toxin Cry5B [PMID:21320697 "Vector-RNAi control animals are only mildly affected by a low dose of PFT, but animals grown on rab-5 or rab-11.1 RNAi are significantly more intoxicated"]. It also reduces the PGP-1::GFP-positive membrane structures expelled into the intestinal lumen during repair. Added to the description. No NEW GO:0001778 (plasma membrane repair) row was added. The evidence is a single feeding-RNAi study with a protection phenotype, and RAB-11.1 acts through its general exocytic recycling activity, which the review already captures.
- WormBase says RAB-11.1 is required for peripheral localization of nuclei in the syncytial germline. No cached paper reports this. Grant & Hirsh 1999 (PMID:10588660) reports Ce-rab11 RNAi oocyte and embryo phenotypes but not germline nuclear position, and a PubMed search found no source. Unverified, so not added.
