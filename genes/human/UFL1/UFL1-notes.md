# UFL1 (E3 UFM1-protein ligase 1) — research notes

UniProt: O94874 (UFL1_HUMAN), 794 aa. HGNC:23039. Chromosome 6. Synonyms: Maxer, NLBP, RCAD, KIAA0776.

## Step in the cascade
UFL1 is the **E3 ligase of the UFM1 (ufmylation) cascade** (E1=UBA5, E2=UFC1, E3=UFL1).
EC=2.3.2.- (transferase). It is the catalytic component of the **UREL complex** (UFL1 + DDRGK1 + CDK5RAP3).
- UniProt FUNCTION: "E3 protein ligase that mediates ufmylation, the covalent attachment of the ubiquitin-like modifier UFM1 to lysine residues on target proteins."
- Non-canonical scaffold-type E3 that activates the E2 UFC1 for aminolysis [PMID:36121123].
- DDRGK1 tethers UREL to the ER membrane; CDK5RAP3 is the third subunit.

## Core biology
- **Principal substrate RPL26/uL24** on 60S ribosomes [PMID:30626644 "Ribosomal protein RPL26 is the principal target of UFMylation."].
- **Ribosome recycling / ER-RQC**: mono-ufmylation of RPL26 weakens the 60S–SEC61 junction, promoting release/recycling of post-termination or stalled 60S subunits [PMID:38383785; PMID:38383789; PMID:37036982 "UFMylation of translocon-bound 60S subunits modulates the RTJ"]. Core BP = GO:0072344 rescue of stalled ribosome (recycling).
- **Reticulophagy / ER stress**: ufmylates CYB5R3 [PMID:36543799], RPN1; drives ER-phagy.
- **DNA-damage response**: recruited to DSBs via NBN; ufmylates histone H4 and MRE11 to promote ATM activation [PMID:30886146; PMID:30783677]. Phosphorylated at Ser-462 by ATM (positive feedback).
- **Other substrates**: TP53/p53 (stabilization) [PMID:32807901]; PD-L1/CD274 [PMID:36893266]; PD-1/PDCD1 (immune regulation) [PMID:38377992]; P4HB [PMID:35753586]; SYVN1/HRD1 [PMID:37795761]; TRIP4/ASC1 [PMID:25219498].

## Localization
Principal site: **ER membrane** (extensive EXP/IDA evidence). Also cytoplasm/cytosol, nucleus and chromosome (DNA-damage). Mitochondrial outer membrane (PMID:20164180, single IDA) is at odds with the dominant ER picture — marked over-annotation.

## Core function conclusion
Core MF: **GO:0061666 UFM1 ligase activity** (E3). Core BP: protein ufmylation (RPL26) supporting 60S recycling / ER-RQC. Many other roles (DNA damage, immune, reticulophagy, transcription) are downstream/non-core.

## 2026-11-15 ORGANELLES tethering route (rule 7)

- Added a NEW GO:0098554 cytoplasmic side of endoplasmic reticulum membrane IC row. The four conditions: (a) ER membrane location with seven curated ECO:0000269 citations; (b) the integral partner DDRGK1 [PMID:38383785 "DDRGK1 contains an N-terminal transmembrane domain and a flexible linker region"], which binds UFL1 directly [PMID:36543799 "We confirmed the direct interaction between UFL1 and UFBP1 by an in vitro pull-down assay"]; (c) dependence [PMID:36543799 "GFP-tagged UFL1 (GFP-UFL1) was present throughout the cytoplasm in the UFBP1 knockout HeLa cells"; PMID:32160526 "Deleting DDRGK1’s N-terminal ER-targeting transmembrane domain (TM) still supported a DDRGK1-UFL1 interaction but led to cytoplasmic localization of both DDRGK1 and UFL1 without ER-phagy"]; (d) no TM, signal or transit feature in UniProt, and cytoplasmic in the literature whenever DDRGK1 is absent or unanchored. Both dependence tests image tagged UFL1, so the row is IC and located_in. The existing GO:0005783 and GO:0005789 rows are unchanged.
- Fixed a pre-existing quote on the GO:1903895 IDA row (PMID:32160526): the text "Ufmylation-dependent reticulophagy inhibits the unfolded protein response" is not in the UniProt file, so the row now quotes PMID:32160526 directly.
