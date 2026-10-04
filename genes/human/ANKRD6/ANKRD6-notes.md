# ANKRD6 (Diversin) notes

- Vertebrate ortholog of fly Diego. It is a Wnt switch: it inhibits canonical beta-catenin signaling and promotes PCP/JNK [PMID:19591803, abstract]. Mouse Ankrd6 localizes asymmetrically in the inner ear, its knockout causes PCP defects and raises canonical Wnt, and it rescues fly diego [PMID:25218921, full text]. In Xenopus it forms tension-sensitive PCP complexes [PMID:40719643]. Hypomorphic human variants occur in neural tube defects [PMID:25200652].
- GOA has 4 rows:
  - Nucleus and cytoplasm (IEA from mouse IDA): ACCEPT.
  - Cell polarity (IBA; seed fly diego): ACCEPT.
  - Regulation of Wnt signaling (IBA; seeds mouse and zebrafish): MODIFY to GO:0090090 plus GO:2000096, the two specific directions the mouse ortholog carries by IDA. Done by MODIFY rather than NEW, because NEW descendants of a carried term are disallowed.
- Affinage: the script's BLOCKING "symbol collision" gate fired because of a Drosophila mention. That is a false positive (Diego ortholog), verified against the narrative, so it was written with --force and recorded in reference_review.
- PTHR24126 PAINT files committed.
