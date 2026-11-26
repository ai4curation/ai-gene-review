# Curatorial Notes for Human `ACCS` (`UniProtKB:Q96QU6`)

## 1. Gene & Family Identity
- **HGNC symbol**: `ACCS` (`HGNC:23989`; synonym `PHACS`, putative human 1-aminocyclopropane-1-carboxylate synthase)
- **UniProtKB**: `Q96QU6` (`1A1L1_HUMAN`, reviewed, 501 aa, sequence version 1)
- **Genomic locus**: Human chromosome 11p11.2 (`ENSG00000110455`), arranged in a conserved mammalian tandem gene pair with its paralog `ACCSL` (`Q4AC99`, 50% sequence identity)
- **PANTHER classification**: `PANTHER:PTHR43795` (*BIFUNCTIONAL ASPARTATE AMINOTRANSFERASE AND GLUTAMATE/ASPARTATE-PREPHENATE AMINOTRANSFERASE-RELATED*), subfamily `PANTHER:PTHR43795:SF17` (*1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 1*)
- **Isoforms**:
  - `Q96QU6-1` (canonical, 501 aa): Full-length fold-type I PLP-dependent carbon-sulfur beta-lyase.
  - `Q96QU6-2` (158 aa, `VSP_055800` + `VSP_055801`): Replaces residues 117-158 and lacks residues 159-501, deleting the catalytic PLP-binding domain (`Asp286`, `Lys323`, `Arg351`, `Arg457`).

## 2. Literature & Biochemical Synthesis
1. **Koch et al. 2001 (`PMID:11470512`, *Gene* 272:75-84)**:
   - Cloned full-length human `PHACS` (`ACCS`, 501 aa), sharing 58% identity with *Takifugu rubripes* ACS-like protein (`PMID:10767549`) and ~30% identity with plant ACC synthases (`EC 4.4.1.14`).
   - Purified recombinant `PHACS` expressed in *Pichia pastoris* contains bound pyridoxal 5'-phosphate (`PLP`) and catalyzes weak in vitro deamination of the mechanism-based plant ACS inhibitor `L-vinylglycine`, but **does not** catalyze the conversion of `S-adenosyl-L-methionine` (`SAM`) to `1-aminocyclopropane-1-carboxylate` (`ACC`), because two key plant ACS active-site residues (`Tyr` and `Ile` in apple ACS-1) are not conserved in human `ACCS` [PMID:11470512, "Purified recombinant PHACS, expressed in Pichia pastoris, contains bound pyridoxal-5'-phosphate (PLP), but does not catalyze the synthesis of ACC. PHACS does, however, catalyze the deamination of L-vinylglycine, a known side-reaction of apple ACS."].
2. **Gao et al. 2025 (`PMID:39876065`, *FEBS J* 292:2272-2286)**:
   - Purified full-length human `ACCS` (`Q96QU6`) from *Saccharomyces cerevisiae* with stoichiometric bound PLP (~330 nm enolimine peak shifting to ~390 nm upon NaOH release; `hACCS-K323A` lacks protein-bound PLP).
   - Confirmed weak L-vinylglycine deaminase activity (`kcat = 1.4 min^-1`, `Km = 3.6 mM`, `kcat/Km = 6.5 M^-1 s^-1`), used L-vinylglycine competition screening across proteinogenic amino acids to identify `L-cysteine` as a competitive active-site binder, and profiled a panel of cysteine S-conjugates and sulfoxides.
   - Discovered that human `ACCS` catalyzes PLP-dependent `C-beta-S lyase` (`alpha,beta-elimination`) cleavage of `S-alkyl/aryl-L-cysteine sulfoxides` (e.g. `S-phenyl-L-cysteine sulfoxide`, `kcat = 14 s^-1`, `kcat/Km ~ 700 M^-1 s^-1`; `L-(+/-)-alliin`) and `S-aryl-L-cysteines` (`S-phenyl-L-cysteine`, `Km = 0.5 mM`, `kcat = 0.4 s^-1`, `kcat/Km ~ 700 M^-1 s^-1`) to pyruvate, ammonia, and sulfenic acid/thiol products, exceeding L-vinylglycine deamination efficiency by two orders of magnitude, with no gamma-lyase (including on SAM or methionine sulfoxide) or beta-replacement activity [PMID:39876065, "In this study, through a biochemical profiling approach, we demonstrate that human ACCS possesses cysteine conjugate sulfoxide β-lyase activity."].
   - AlphaFold2 homodimer homology modeling, AutoDock Vina docking, and site-directed mutagenesis established the active-site architecture on `Q96QU6` (`sv: 1`):
     - `K323`: Schiff-base lysine and general base (`K323A` abolishes bound PLP and catalytic activity).
     - `D286`, `R331`, `N258`, `Y195`, and partner-chain `Y132(B)`: Modeled PLP cofactor contacts (`Y195F` reduces activity ~3.5-fold, matching C-beta-S lyases rather than plant ACCS; AlphaFold2/AutoDock Vina docking hypothesizes that `Y132(B)` sterically impedes productive SAM binding, distinct from the experimentally demonstrated absence of ACC synthase activity).
     - `R457`: Substrate alpha-carboxylate salt-bridge anchor (`R457C`, mimicking natural `C529` in human `ACCSL`, reduces activity 100-fold).
     - `W135(B)` and `R351(B)`: Partner-monomer side-chain pocket determinants across the homodimer interface (`W135A` and `R351A` cause >10-fold activity loss; `R351H`/`R351K` rescue activity whereas `R351Y`, mimicking `Y423` in human `ACCSL`, reduces activity ~40-fold; `W135Y` reduces activity ~5.5-fold).
3. **Binary Interactome Studies (`PMID:16189514`, `PMID:25416956`, `PMID:31515488`, `PMID:32296183`, `PMID:35156780`)**:
   - Four independent yeast two-hybrid studies (`CCSB-HI1`, `HI-II-14`, ExAC SNV-interactome, and `HuRI`) detect `Q96QU6`-`Q96QU6` self-interaction (`GO:0042802`), directly matching the obligate homodimer active-site architecture where `Y132(B)`, `W135(B)`, and `R351(B)` come from the partner subunit.
   - Heterotypic screen hits with mitochondrial `UQCRB` (`PMID:25416956`) and plasma-membrane `CFTR` (`PMID:35156780`) lack functional validation and are removed on bare `GO:0005515` per the protein-binding policy.

## 3. Targeted Literature Search Log (BP & CC Aspects)
- Systematic PubMed and corpus searches conducted on 2026-11-12 for `"ACCS" AND ("human" OR "lyase" OR "cysteine")`, `"PHACS" AND "vinylglycine"`, `"Q96QU6"`, and `"ENSG00000110455"` identified `PMID:11470512` and `PMID:39876065` as the sole primary biochemical studies on human `ACCS`, alongside proteome-scale interaction screens (`PMID:16189514`, `PMID:25416956`, `PMID:31515488`, `PMID:32296183`, `PMID:35156780`). Neither endogenous physiological substrates/in vivo metabolic pathways (BP) nor experimentally validated endogenous subcellular localization (CC; `PMID:39876065` cites Human Protein Atlas cytoplasmic staining only as background) have been established in primary experimental studies.

## 4. Affinage Deep-Research Audit (`ACCS-deep-research-affinage.md`)
- Affinage (`faith_pct: 66.67`, `self_evaluation_pairwise: win`, 1 discovery citing `PMID:39876065`) accurately summarizes the cysteine conjugate sulfoxide beta-lyase activity, AlphaFold2-guided mutagenesis, lack of canonical ACC synthase activity, and absence of characterized cellular localization, physiological substrates, or pathway context.
- Limitations noted in `reference_review`: omits `PMID:11470512` (original cloning, PLP cofactor proof, L-vinylglycine deamination, and negative `IDA` proof against `GO:0016847`), omits homodimerization (`GO:0042802`), and grounds `molecular_activity` to coarse `goslim_generic` `GO:0016829` (`lyase activity`) rather than specific `GO:0047804` (`cysteine-S-conjugate beta-lyase activity`, `is_a` `GO:0016846` `carbon-sulfur lyase activity`).
