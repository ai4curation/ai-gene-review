# CSK (human, P41240) review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were compiled manually from the UniProt
record, the cached publications in `publications/`, the Reactome cache, QuickGO
and the PANTHER PAINT files. No `*-deep-research-*.md` file was created.

## Identity and domain architecture

- C-terminal Src kinase, 450 aa, SH3 - SH2 - tyrosine kinase domain; no
  N-terminal fatty acylation signal, no activation-loop autophosphorylation
  tyrosine [PMID:1945408 "Furthermore, cyl lacks the highly conserved tyrosine autophosphorylation site (Y416src) in the tyrosine kinase catalytic domain."].
- Originally cloned as "cyl" from K562 cells [PMID:1945408 "The deduced cyl protein lacks signal and transmembrane sequences but contains features of known cytoplasmic tyrosine kinases, including amino-terminal SH3 and SH2 domains"].

## Core molecular function: inhibitory C-terminal tail phosphorylation of Src-family kinases

- Human CSK phosphorylates Lck Tyr-505 and suppresses Lck activity
  [PMID:1639064 "Here we characterize a human cytosolic 50 kDa protein tyrosine kinase, p50csk, which specifically phosphorylates Tyr-505 of p56lck and a synthetic peptide containing this site"; PMID:1639064 "Phosphorylation of Tyr-505 suppressed the catalytic activity of p56lck"].
- Inactivates Yes [PMID:9281320 "we show that the enzyme is inactivated by incubation with protein tyrosine kinase Csk in an ATP-Mg-dependent manner, indicating that cellular Yes can be regulated by Csk phosphorylation"].
- Autophosphorylation and activity on artificial substrates (rat Csk in E. coli)
  [PMID:7683130 "The GST-Csk fusion protein also phosphorylates exogenous substrates, including the heteropolymer poly-Glu/Tyr and enolase"].
- Substrate specificity is set by a docking interface between the two kinase
  domains, not by the conventional peptide-binding site
  [PMID:18614016 "Csk cannot phosphorylate substrates that lack this docking mechanism because the conventional substrate binding site used by most tyrosine kinases to recognize substrates is destabilized in Csk by a deletion in the activation loop"].
- SH3 and SH2 domains are needed for full activity but not for Src recognition
  [PMID:15683240 "the SH3 and SH2 domains were crucial in maintaining the full activity of Csk, but were not directly involved in Csk recognition of its physiological substrate, Src"].
- Reported non-SFK substrates: CD45 (PMID:7507203), PD-1 (Reactome R-HSA-389762),
  bacterial EPIYA effectors (PMID:24902122). These are minor/contextual.

## Membrane recruitment via SH2 binding to phosphotyrosine adaptors

- CSK is mainly cytosolic and is brought to its membrane-anchored SFK substrates
  by SH2-mediated binding to tyrosine-phosphorylated adaptors and receptors.
  - PAG/Cbp: [PMID:10790433 "Expression of PAG in COS cells results in recruitment of endogenous Csk, altered Src kinase activity, and impaired phosphorylation of Src-specific substrates"].
  - IGF-1R/IR: [PMID:10026153 "We found that the SH2 domain of CSK binds to the tyrosine-phosphorylated form of IGF-IR and IR"].
  - H. pylori CagA: [PMID:12446738 "Csk selectively binds tyrosine-phosphorylated CagA via its SH2 domain"].
  - SCIMP: [PMID:21930792 "When phosphorylated, SCIMP binds to the SLP65 adaptor protein and also to the inhibitory kinase Csk"].
  - H. ducreyi LspA1: [PMID:24902122 "Phosphorylated YL2 increased Csk catalytic activity"].
- PKA phosphorylates and activates CSK in T-cell lipid rafts
  [PMID:17911601 "which in turn phosphorylates and activates C-terminal Src kinase (Csk) in T cell lipid rafts"].

## SH3 domain: PEP/PTPN22 binding and homodimerization

- [PMID:8890164 "this interaction was mediated by the Csk SH3 domain and by a proline-rich region (PPPLPERTP) in the non-catalytic C-terminal portion of PEP"].
- [PMID:19888460 "We have discovered that Csk forms homodimers through interactions mediated by the SH3 domain in a manner that buries the recognition surface for SH3 ligands"].

## Physiological processes (animal context)

- Negative regulation of antigen-receptor signalling in T cells
  [PMID:8890164 "We previously showed that Csk is a potent negative regulator of antigen receptor signaling in T lymphocytes"].
- Phagocytosis: CSK activity inhibits SFK-dependent Fc-gamma-R phagocytosis
  [PMID:24902122 "LspA virulence factors of H. ducreyi inhibit phagocytosis by stimulating the catalytic activity of C-terminal Src kinase (Csk), which itself inhibits Src family protein tyrosine kinases (SFKs) that promote phagocytosis"].
- Golgi export of Lyn [PMID:20605918 "Formation of a closed conformation by CSK prevents Lyn from associating with ACSL3, resulting in blockade of Lyn export from the Golgi"].
- Many of the IEA (Ensembl Compara) process rows derive from rat Csk experiments
  (QuickGO, P32577): bone resorption, IL-6 and proliferation from adenoviral Csk
  overexpression in arthritic joints (PMID:10411542); LDL clearance and phagocytosis
  from Csk-transfected J774 macrophages (PMID:10884975); Fc-epsilon-R and ERK from
  PMID:9325302; oligodendrocyte differentiation (IEP, PMID:15504915); adherens
  junction organization (IEP, PMID:15389520, rat seminiferous epithelium). These
  rat papers were identified from QuickGO and PubMed esummary titles only; they
  were not read.

## IBA rows

- GO:0004715 from PTN001231168 (Bilateria node, PTHR24418, seeded by fly Csk
  FBgn0262081). Sound.
- GO:0034332 adherens junction organization and GO:0060368 regulation of Fc
  receptor mediated stimulatory signaling pathway from PTN002815304 (taxon
  Euteleostomi, 117571), both seeded only by rat Csk (RGD:1308800). The adherens
  junction seed is an IEP annotation (expression in rat testis), which is weak
  for a process claim. Kept as non-core.
- GO:0005886 plasma membrane IBA: broad SFK/CSK node; fine.

## GO-CAM

- No entry for CSK / P41240 in `gocams/index.tsv`, so no GO-CAM role to reconcile.

## Premetazoan context (ancestral vs animal-specific)

- Phosphotyrosine signalling machinery predates animals
  [PMID:18273011 "These findings support a model in which the full set of pTyr signalling machinery evolved before the separation of the choanoflagellate and metazoan lineages."].
- Choanoflagellate M. ovata has a functional Csk ortholog that phosphorylates Src
  tail tyrosines [PMID:16873552 "we show that the src gene family and its C-terminal Src kinase (Csk)-mediated regulatory system already were established in the unicellular M. ovata"; PMID:16873552 "These observations demonstrate that MoCsk and EfCsk are functional orthologs of Csk and that both Src and Csk functions are, at least partially, complementary between E. fluviatilis , M. ovata , and vertebrates."].
  But choanoflagellate Src is only weakly inhibited by it.
- M. brevicollis Csk: active, phosphorylates the MbSrc1 tail, but the phosphorylation
  does not inhibit MbSrc1 [PMID:18390552 "We cloned and expressed the M. brevicollis homolog of c-Src C-terminal kinase (MbCsk) and showed that it phosphorylates the C terminus of MbSrc1, yet this phosphorylation does not inhibit MbSrc to the same degree seen in the mammalian Src/Csk pair"].
- Contrary result (abstract only read): inhibition of Src by Csk demonstrated for
  Capsaspora and M. brevicollis proteins in yeast/in vitro assays
  [PMID:28939764 "Our results suggest that negative regulation of Src by Csk is more ancient than previously thought and that it might be conserved across all holozoan species"].
- Summary: CSK's catalytic activity (tyrosine kinase that phosphorylates the
  Src C-terminal tail) is ancestral to Holozoa, verified biochemically in two
  choanoflagellates and (per an abstract) Capsaspora and Corallochytrium. Whether
  that phosphorylation was already inhibitory before animals is disputed
  (PMID:16873552, PMID:18390552 vs PMID:28939764). The adaptor-mediated
  recruitment system (PAG/Cbp, SCIMP, PTPN22/PEP), and all the process rows
  (T-cell receptor, Fc receptor, bone resorption, adherens junctions, phagocytosis
  by immune cells) are animal-specific contexts. I did not find evidence for
  choanoflagellate or Capsaspora orthologs of PAG/Cbp in the papers read, so
  that point is left open.

## Action summary rationale

- protein binding (GO:0005515) rows: REMOVE unless the paper supports a specific
  MF; MODIFY to GO:0001784 phosphotyrosine residue binding for SH2-mediated
  binding to phospho-IGF1R/IR (PMID:10026153), phospho-CagA (PMID:12446738),
  phospho-SCIMP (PMID:21930792), phospho-LspA1 (PMID:24902122); MODIFY TAS PEP row
  (PMID:8890164) to proline-rich region binding / protein phosphatase binding.
