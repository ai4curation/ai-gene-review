# KRIT1 (horse, A0A3Q2GZV2) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This review did not open or use any ProtNLM2 output. The folder is `KRIT1__A0A3Q2GZV2` because the
plain `genes/HORSE/KRIT1` folder holds a different horse KRIT1 entry (A0A9L0SR44) from the same
Ensembl gene (ENSECAG00000016850). A0A3Q2GZV2 is the 736-aa full-length product, VGNC:19518.

**Deep research.** `just deep-research-falcon HORSE KRIT1__A0A3Q2GZV2 --fallback perplexity-lite`
failed. Falcon raised "Exception: Failed to authenticate" and perplexity-lite returned HTTP 401
(insufficient quota). No deep-research file was created. A web search found no horse-specific KRIT1
functional study. The review therefore relies on cached mammalian literature, the human KRIT1 review
(genes/human/KRIT1), the PTHR13283 PAINT table and a new sequence comparison.

**Evolutionary grounding.**
- The UniProt PANTHER cross-reference places A0A3Q2GZV2 in PTHR13283:SF11 (KREV INTERACTION TRAPPED PROTEIN 1),
  the same subfamily as human O00522, mouse Q6S5J6 and zebrafish F1REV3. FRMD8 is in other subfamilies.
- The protein carries IBAs from three PAINT nodes (interpro/panther/PTHR13283/PTHR13283-paint.tsv):
  - PTN002665063 (taxon 33213, Bilateria): microtubule binding (seed O00522), A/P axis specification
    (seed zebrafish krit1), cell redox homeostasis and regulation of establishment of cell polarity
    (seeds MGI:1930618 and O00522).
  - PTN002665064 (taxon 117571, vertebrates): negative regulation of angiogenesis.
  - PTN004412369 (taxon 2759, family-wide): plasma membrane.
- In the sequence comparison (KRIT1__A0A3Q2GZV2-bioinformatics/RESULTS.md, compare_to_human.py), horse
  and human KRIT1 are 98.6% identical over 736 residues with no gaps. The NPAY/NPLF/NPYF motifs, the ICAP1
  region (172-195) and the RAP1B region (430-452) are identical.

**Experimental status in horse.** Horse KRIT1 has no experimental GO annotation and no published
functional study. Every function in this review is inferred from human and mouse orthologs in the same
subfamily. The review text says so in each case.

**Decisions** (consistent with the human O00522 review):
- Plasma membrane (IBA, IEA): ACCEPT.
- Microtubule binding (IBA, human IDA seed): ACCEPT, core.
- Cytoskeleton: MODIFY to microtubule cytoskeleton. Anchoring junction: MODIFY to adherens junction.
- GTPase regulator activity (ARBA): MODIFY to small GTPase binding. KRIT1 is a Rap1 effector, not a
  GEF or GAP [PMID:21633110 "native KRIT1 protein binds the effector loop of Rap1A but not H-Ras in a GTP-dependent manner"].
- Negative regulation of angiogenesis, cell redox homeostasis and regulation of establishment of cell
  polarity (IBA plus ARBA IEA): KEEP_AS_NON_CORE. These are downstream or indirect outputs.
- Anterior/posterior axis specification (IBA): REMOVE. Its only seed is a zebrafish morphant body-axis
  phenotype [PMID:26540726 "also leads to substantial body axis abnormalities"], which is an organismal
  phenotype and not participation in the process.

**Not added (NEW).** Human KRIT1 has experimental support for HEG1/CCM2 adaptor activity, ICAP1 binding
and positive regulation of integrin activation. PAINT did not propagate any of these to the KRIT1 nodes,
so their absence is treated as a curator decision and they were not proposed for horse. The point is
raised as a suggested question. Small GTPase binding enters only as a refinement of the existing ARBA
GTPase-regulator row.
