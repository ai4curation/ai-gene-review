# STUB1 (CHIP / E3 ubiquitin-protein ligase CHIP) — research notes

UniProt: Q9UNE7 (CHIP_HUMAN), 303 aa. C-terminus of HSC70-interacting protein.

## Core identity
Dual-function protein bridging the chaperone and ubiquitin-proteasome systems:
- N-terminal TPR domain binds HSP70/HSC70 (EEVD) and HSP90 (MEEVD) -> co-chaperone.
- C-terminal U-box domain -> RING-type E3 ubiquitin-protein ligase.
Functions as a homodimer. Ubiquitinates chaperone-bound misfolded/damaged clients
(with E2s e.g. UBE2D, UBE2N/UBE2V1) and targets them for proteasomal degradation
("triage" factor). Also modulates the HSP70/HSP90 chaperone cycle.

- [file:human/STUB1/STUB1-uniprot.txt "FUNCTION: E3 ubiquitin-protein ligase which targets misfolded chaperone substrates towards proteasomal degradation"]
- [file:human/STUB1/STUB1-uniprot.txt "Modulates the activity of several chaperone complexes, including Hsp70, Hsc70 and Hsp90"]
- [file:human/STUB1/STUB1-uniprot.txt "The TPR domain is essential for ubiquitination mediated by"]
- [file:human/STUB1/STUB1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm. Nucleus. Mitochondrion."]

## Disease
- SCAR16 [MIM:615768] autosomal-recessive spinocerebellar ataxia (ataxia + hypogonadism),
  caused by loss of CHIP ubiquitin-ligase activity.
- SCA48 [MIM:618093] autosomal-dominant spinocerebellar ataxia.

## Core MFs (per batch-5 guidance)
1. ubiquitin-protein ligase activity (GO:0061630) + ubiquitin-protein transferase
   activity (GO:0004842) — U-box E3.
2. Hsp70/Hsp90 co-chaperone binding (GO:0030544 / GO:0051879 / GO:0031072 /
   GO:0051087) via TPR.
3. Protein quality control for misfolded proteins (GO:0006515).

## Review approach (197 annotations, programmatically filled and validated)
- Core ligase MF/BP (GO:0061630, GO:0004842, GO:0034450, GO:0043161, GO:0006511,
  GO:0000209, GO:0016567, GO:0070534, GO:0006513, GO:0051865, GO:0006515) -> ACCEPT.
- Chaperone-binding MFs (GO:0030544, GO:0051879, GO:0031072, GO:0051087) -> ACCEPT.
- Homodimerization (GO:0042803), misfolded protein binding (GO:0051787),
  ubiquitin ligase complex (GO:0000151) -> ACCEPT.
- Cytoplasm/cytosol (GO:0005737/GO:0005829) -> ACCEPT; nucleus/mitochondrion/ER/Z-disc/
  inclusion body -> KEEP_AS_NON_CORE (documented secondary/specialized localizations).
- Downstream/regulatory & substrate-specific BP (proteolysis regulation, stress responses,
  cardiac/vascular/immune processes, CMA/mitophagy, TGFbeta/PPAR/ERBB2 signaling) ->
  KEEP_AS_NON_CORE (pleiotropic, substrate-specific consequences of the catalytic MF).
- 46x protein binding (GO:0005515 IPI): KEEP_AS_NON_CORE (real interactions, uninformative
  term); those with HSP70/HSC70/HSP90 partners MODIFY to Hsp70/Hsp90/heat-shock protein
  binding. HSP-partner PMIDs identified from goa WITH column (P11142=HSPA8, P07900=HSP90AA1,
  P08238=HSP90AB1, P0DMV8/9=HSPA1A/B).
