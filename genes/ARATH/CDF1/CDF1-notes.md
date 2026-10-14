# CDF1 (CYCLING DOF FACTOR 1; DOF5.5; At5g62430; UniProtKB:Q8W1E3) notes

## Identity check (2026-10-05)

- A symbol search for `CDF1` in A. thaliana returns two reviewed entries: Q9FN50 (CPP1, "CELL GROWTH
  DEFECT FACTOR 1", At5g23040, chloroplastic) and Q8W1E3 (Cyclic dof factor 1, At5g62430). The
  photoperiod-pathway CDF1 is Q8W1E3; the folder was fetched by accession
  (`just fetch-gene ARATH Q8W1E3 --alias CDF1`). The uniprot.txt reads `CDF1_ARATH`, `Name=CDF1;
  Synonyms=DOF5.5; OrderedLocusNames=At5g62430`.
- Falcon deep research failed (HTTP 402), so there is no deep-research file; the notes below come from
  the cached publications.

## Function summary with provenance

- Repressor of CO, degraded by FKF1: [PMID:16002617 "FKF1 physically interacts with CDF1, and CDF1
  protein is more stable in fkf1 mutants."] [PMID:16002617 "CDF1 and CO are expressed in the same
  tissues, and CDF1 binds to the CO promoter."]
- GI dependence: [PMID:17872410 "FKF1 function is dependent on GI, which interacts with a CO repressor,
  CYCLING DOF FACTOR 1 (CDF1), and controls CDF1 stability."] [PMID:17872410 "GI, FKF1, and CDF1
  proteins associate with CO chromatin."]
- Direct FT repression: [PMID:22628657 "indicating that CDF1 binds to the FT promoter regions in the
  morning."] [PMID:22628657 "These results indicate that CDF1 protein represses FT transcription
  independently of CO transcription."]
- Mechanism via TOPLESS: [PMID:28752516 "This TPL interaction confers a repressive function on CDF1, as
  mutations of the N-terminal TPL binding domain largely impair the ability of CDF1 protein to repress
  its targets."]
- Redundancy with other CDFs: [PMID:19619493 "Combining mutations in four of these, including CYCLING DOF
  FACTOR 2 (CDF2), caused photoperiod-insensitive early flowering by increasing CO mRNA levels."]
- Structure: [PMID:40263610 "Here we present the crystal structure of the Dof domain of CYCLING DOF
  FACTOR 1 (CDF1)"]
- Non-flowering outputs of the GI-CDF module: [PMID:25600594 "the CDFs function downstream of GI,
  influencing responses to freezing temperatures and growth, but are not necessary for proper clock
  function."]; hypocotyl elongation in short days [PMID:32379360 "Similar results were observed for
  CDF1."]

## Curation decisions

- MF core: GO:0001227 (DNA-binding transcription repressor activity, RNA pol II-specific) + GO:0001222
  (transcription corepressor binding; TPL).
- FKF1/LKP2 protein-binding rows -> MODIFY to GO:0031625 ubiquitin protein ligase binding (CDF1 is the
  SCF(FKF1) substrate).
- GI protein-binding row -> REMOVE (term only; interaction real, no informative MF term).
- Chloroplast organization IMP (PMID:22383539) -> UNDECIDED: abstract does not name CDF1, full text not
  retrievable (Europe PMC returned 500).
- NEW: GO:0048579 negative regulation of long-day photoperiodism, flowering. Entity check: CDF1 itself
  binds the CO and FT promoters and represses them (it performs the regulatory step), so the regulation
  term belongs on CDF1; comparator CO carries the positive counterpart GO:0048578.

## 2026-10-06 follow-up

- Chloroplast organization IMP (PMID:22383539): the publication was re-fetched with full text from PMC
  (`just fetch-pmid 22383539 --force`). The full text names CDF1 as an END (enhanced deetiolation) gene
  [PMID:22383539 "Three of these END genes encode transcription factors: SMZ , CDF1 , and RAP2.6 ."].
  Changed UNDECIDED -> KEEP_AS_NON_CORE.
