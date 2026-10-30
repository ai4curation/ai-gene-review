# MT-ND5 notes

## Literature work

Deep research was not run for this gene; the literature was assembled from the cached
GOA references, the UniProt record and mammalian Complex I structure papers,
retrieved through the PubMed MCP and cached with `just fetch-pmid`.

## Function

- MT-ND5 encodes a core subunit of Complex I [file:human/MT-ND5/MT-ND5-uniprot.txt "Core subunit of the mitochondrial membrane respiratory chain"].
- The membrane arm includes "three homologous antiporter-like subunits (ALS), ND2/NuoN, ND4/NuoM and ND5/NuoL, containing 14 conserved transmembrane helices (TM) each" [PMID:36920092]. The proposed mechanism ends in "proton expulsion from the distal antiporter-like subunit" [PMID:36920092].
- Each of the four pumping units has "a proton-uptake and a proton-exit half-channel" [PMID:32747785].
- Human cell lines lacking ND5 lose membrane association of the 24 kDa subunit [PMID:15250827 "However, in cells lacking ND4 or ND5, very low amounts of 24 kDa subunit were found associated with the membranes"], and the ND subunits "are essential for NADH:ubiquinone oxidoreductase activity" [PMID:15250827].

## Curation decisions

- The core MF is proton transmembrane transporter activity (GO:0015078), added as NEW (ISS), with contributes_to GO:0008137. The core BP is GO:0006120, plus GO:0015990 (accepted IBA).
- The `enables` GO:0008137 rows are MODIFY, to contributes_to.
- GO:0042773 (IEA, InterPro) is MODIFY to GO:0006120.
- Response to hypoxia and response to hydrogen peroxide are Ensembl projections from rat, marked over-annotated.

## Disease context

m.13513G>A in MT-ND5 is the commonest MT-ND variant in MELAS/Leigh overlap (dismech
MELAS_Syndrome, PMID:34025555). The dismech node "Complex I structural subunit defect"
binds GO:0008137 DECREASED, which matches the contributes_to core function.
