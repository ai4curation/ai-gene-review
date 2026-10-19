# MT-ND6 notes

## Literature work

Deep research was not run for this gene; the literature was assembled from the cached
GOA references, the UniProt record and mammalian Complex I structure papers,
retrieved through the PubMed MCP and cached with `just fetch-pmid`.

## Function

- MT-ND6 encodes a core subunit of Complex I [file:human/MT-ND6/MT-ND6-uniprot.txt "Core subunit of the mitochondrial membrane respiratory chain"].
- ND3, ND6 and ND4L "form, together with part of ND1, the E-channel containing key glutamates" [PMID:36920092].
- Each pumping unit has "a proton-uptake and a proton-exit half-channel" [PMID:32747785].
- ND6 also controls the active/deactive transition: "In the induced deactive state, the open conformation is arrested by the ND6 subunit." [PMID:32972993]
- Patient cells and cybrids: "Cybrid clones showed a specific complex I defect that correlates with the mutant heteroplasmy levels." [PMID:14595656]. In an LHON/dystonia family, "Biochemical analysis of a muscle biopsy revealed a severe complex I deficiency" [PMID:8644732].

## Curation decisions

- The core MF is proton transmembrane transporter activity (GO:0015078), added as NEW (ISS). This activity is performed jointly with ND1, ND3 and ND4L as the E-channel unit. The core function also has contributes_to GO:0008137.
- The `enables` GO:0008137 rows are MODIFY, to contributes_to.

## Disease context

m.14453G>A in MT-ND6 is reported in MELAS (UniProt; dismech MELAS_Syndrome,
PMID:32552696). The dismech node binds GO:0008137 DECREASED, which is consistent with
the core function here.
