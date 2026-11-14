# E. coli sbcB / Exonuclease I (P04995) notes

## 2026-11-13 review session

Context: 3'->5' excision exonuclease candidate for the MMR module.

### Function summary (with provenance)

- Processive Mg2+-dependent 3'-5' ssDNA exonuclease [PMID:23609540 "Escherichia coli Exonuclease I (ExoI) digests single-stranded DNA (ssDNA) in the 3'-5' direction in a highly processive manner."]; monomer, C/O-shaped structure [PMID:11101894].
- SSB C-terminus recruits ExoI to its substrate [PMID:18591666 "SSB stimulates ExoI by recruiting the enzyme to its substrate"; PMID:20018747].
- MMR excision: component of the reconstituted reaction [PMID:2665076]; one of four redundant exonucleases [PMID:11418610 "extracts deficient in RecJ, ExoI, ExoVII, and ExoX exonucleases were devoid of normal repair activity"]; in vivo requirement [PMID:11381137 "These observations confirm involvement of the four exonucleases in methyl-directed mismatch repair in vivo"]; frameshift avoidance with ExoVII [PMID:9584082].
- Replication completion at converging forks with SbcCD [PMID:29208713].
- dRpase activity co-purifies with ExoI [PMID:1329027 "a major dRpase activity in E. coli is associated with the exonuclease I protein"].

### Decisions

- GO:0000175 3'-5'-RNA exonuclease (IEA, oligoribonuclease signature) -> REMOVE; ExoI is DNA-specific.
- GO:0051575 5'-dRP lyase (IDA) -> MARK_AS_OVER_ANNOTATED: real in vitro dRpase activity, but GO:0051575 is a beta-elimination lyase and ExoI is a hydrolytic DnaQ-like exonuclease; physiological role unshown.
- Generic exonuclease/DNA exonuclease/nucleic acid binding/DNA repair IEAs -> MODIFY to the specific supported descendants (GO:0008310, GO:0003697, GO:0006298).
- DNA catabolic process (4 rows), Mg binding (5 rows), ssDNA binding, replication termination -> KEEP_AS_NON_CORE.
- SSB protein binding rows -> REMOVE (policy).
- PMID:14235546 has no abstract in the cache; rows deferred to curator.
