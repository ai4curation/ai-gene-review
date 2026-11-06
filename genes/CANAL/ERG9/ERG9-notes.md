# ERG9 notes

ERG9 is the C. albicans member of the canonical fungal squalene synthase lineage. The local
UniProt record places P78589 in `PANTHER:PTHR11626:SF2` (`SQUALENE SYNTHASE`), and the
PTHR11626 family review treats SF2 as the active squalene synthase subfamily while calling
out Arabidopsis SQS2 and Botryococcus SSL members as exceptions outside this canonical
Candida case [file:genes/CANAL/ERG9/ERG9-uniprot.txt, "DR   PANTHER; PTHR11626:SF2; SQUALENE SYNTHASE; 1."],
[file:interpro/panther/PTHR11626/PTHR11626-review.yaml, "Squalene synthase activity is conserved in
the single-copy orthologs of fungi, animals and plants, which make up most of SF2."].

Biologically, ERG9 sits at the branch where two molecules of farnesyl diphosphate are
committed to sterol synthesis as squalene. The 2024 fungal sterol-pathway paper is not direct
C. albicans ERG9 enzymology, but it gives a useful modern pathway statement: "farnesyl
pyrophosphate, the last product of the mevalonate pathway, is converted to squalene by
squalene synthase" [PMID:39060235].

The GOA-cited Song et al. paper is C. albicans specific but expression-only for this review.
It supports ERG9 belonging to the late sterol response rather than directly proving catalysis
or localization: ERG9 and ERG11 transcripts increased under lovastatin/fluconazole during
mid-logarithmic growth [PMID:14653518].

The 2026 GOA refresh pruned the older CGD ISS and plasma-membrane IDA rows, leaving nine
current rows. I kept the refreshed GO_REF:0000120 rows that combine UniProt's InterPro/Rhea/EC
inferences with `PANTHER:PTN002614878`, but treated that PTN as unaudited in this local
snapshot because PTHR11626 currently caches `PTN001700951`, `PTN000179294`, and
`PTN000907895` instead.

The current ISS activity row now cites `UniProtKB:P25340`, which is S. cerevisiae Erg4
instead of Erg9. The assertion remains correct for C. albicans ERG9 because SF2 contains
active fungal squalene synthases, but the donor provenance is recorded as a source-side
miscitation.

Newer-literature search:

- `just deep-research-falcon CANAL ERG9` failed because `agentapi` is not installed; no
  `ERG9-deep-research-falcon.md` was created.
- Web/PubMed searches on 2026-11-06 did not find newer papers directly assaying C. albicans
  ERG9. PMID:40852982 identified S. cerevisiae ERG9 repression as a ferulic-acid-resistance
  determinant and tested ferulic-acid/fluconazole synergy in C. albicans, but it does not
  provide direct C. albicans ERG9 enzymology or localization evidence.
