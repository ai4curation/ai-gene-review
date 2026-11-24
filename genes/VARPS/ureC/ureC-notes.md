# Curation Notes: `ureC` (`C5CY00` / `Vapar_4243`) in *Variovorax paradoxus* S110

## 1. Gene & Protein Identity
- **UniProt Accession:** `C5CY00` (`URE1_VARPS`, reviewed Swiss-Prot, 572 aa, EC 3.5.1.5)
- **Gene Symbol / Locus Tag:** `ureC` / `Vapar_4243`
- **Organism:** *Variovorax paradoxus* strain S110 (`NCBITaxon:543728`) [PMID:21183664, "Complete genome sequence of the metabolically versatile plant growth-promoting endophyte, Variovorax paradoxus S110."].
- **Sequence & Active-Site Architecture:**
  - Matches HAMAP family rule `MF_01953` (`Urease_alpha`), `Pfam:PF00449` (`Urease_alpha`), `Pfam:PF01979` (`Amidohydro_1`), `TIGR01792` (`urease_alph`).
  - Dinuclear $\text{Ni}^{2+}$ metallocenter ligands (`ChEBI:CHEBI:49786`):
    - $\text{Ni}_1$: His139, His141, and bridging N6-carboxylysine Lys222 (`MOD_RES 222`) + His365 (`BINDING 365`, Asp365)
    - $\text{Ni}_2$: bridging N6-carboxylysine Lys222, His251, His277
    - Substrate binding: His224; General acid proton donor: His325 (`ACT_SITE 325`) [UniProtKB:C5CY00, "Note=Binds 2 nickel ions per subunit. {ECO:0000255|HAMAP-Rule:MF_01953};"].

## 2. Pathway Context & Module Linkage
- **Existing Reusable Module:** [`modules/urease_biogenesis_urea_hydrolysis.yaml`](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-variovorax/modules/urease_biogenesis_urea_hydrolysis.yaml) (`MODULE:urease_biogenesis_urea_hydrolysis`).
- **Mechanism:** `UreC` (alpha) combines with `UreA` (gamma) and `UreB` (beta) to form the $(\text{UreABC})_3$ apoenzyme (`GO:0035550` `urease complex`), which undergoes $\text{CO}_2$-dependent Lys222 carbamylation and GTP-dependent $\text{Ni}^{2+}$ insertion catalyzed by the `UreDFG`–`UreE` metallochaperone machinery [PMID:20046957, "The active site of urease contains two nickel atoms bridged by a carboxylated lysine and a solvent molecule, as shown for the K. aerogenes enzyme (Fig. 2).19 In addition, Ni1 is coordinated by two His residues plus a terminal water molecule while Ni2 is coordinated by two His, an Asp, and a terminal solvent."].
- **Rhizosphere & Biomineralization Significance:** In *Variovorax paradoxus* S110, urease-catalyzed urea hydrolysis ($\text{urea} + 2\text{H}_2\text{O} + \text{H}^+ \rightarrow \text{HCO}_3^- + 2\text{NH}_4^+$) both supplies bioavailable ammonium nitrogen to host plants and generates carbonate/hydroxide alkalinity that drives microbially induced carbonate precipitation (MICP) of toxic divalent heavy metals ($\text{Cd}^{2+}, \text{Ni}^{2+}, \text{Pb}^{2+}$) and rare earth elements, requiring intracellular $\text{Ni}^{2+}$ homeostasis coordinated with CzcA/CnrA RND efflux systems (`czcA3`, `cnrA`).

## 3. Review of Existing GOA Annotations
- **`GO:0009039` (`urease activity`, IEA) -> `ACCEPT`:** Core catalytic activity (EC 3.5.1.5, `RHEA:20557`).
- **`GO:0016151` (`nickel cation binding`, IEA) -> `ACCEPT`:** Core cofactor binding (2 $\text{Ni}^{2+}$ ions per subunit).
- **`GO:0043419` (`urea catabolic process`, IEA) -> `ACCEPT`:** Core biological process.
- **`GO:0016787` (`hydrolase activity`, IEA) -> `TOO_GENERAL`:** Subsumed by `GO:0009039`.
- **`GO:0016810` (`hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds`, IEA) -> `TOO_GENERAL`:** Subsumed by `GO:0009039`.
- **`GO:0005737` (`cytoplasm`, IEA) -> `MODIFY` to `GO:0005829` (`cytosol`) + `NEW` (`IC`):** Soluble cytosolic enzyme complex.
- **Added `NEW` (`IC`) `GO:0035550` (`urease complex`, `part_of`):** Captures assembly into the $(\text{UreABC})_3$ holoenzyme complex.
