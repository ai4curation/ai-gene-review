# LBR (lamin B receptor, Q14739) — review notes

Literature work done manually from cached `publications/` (PubMed MCP used to
locate additional PMIDs, which were then fetched with `just fetch-pmid`).

## Enzymatic function (core)
- Sterol C14 reductase: human LBR complements yeast erg24 (C14 reductase)
  mutants but not erg4 [PMID:9630650 "the sterol C14 reduction step and
  ergosterol prototrophy were restored in LBR-producing erg24 transformants which
  lack endogenous sterol C14 reductase."].
- Expressed LBR has Delta14-reductase activity in vitro [PMID:16784888 "Both
  human C14SR and LBR expressed in COS-1 cells exhibit 3beta-hydroxysterol
  Delta(14)-reductase activity in vitro."]; the same paper argued TM7SF2 (C14SR)
  is the sterol-regulated, ER enzyme and that LBR's role "remains unclear".
- Greenberg/HEM dysplasia: patient fibroblasts accumulate
  cholesta-8,14-dien-3beta-ol and are complemented by wild-type LBR
  [PMID:12618959 "Functional complementation of the HEM cells by transfection with
  control LBR cDNA confirmed that LBR encoded the defective sterol
  delta(14)-reductase."].
- Greenberg missense alleles at conserved sterol-reductase residues fail yeast
  complementation [PMID:21327084 "both mutations failed to rescue C14 sterol
  reductase deficient yeast, indicating an enzymatic defect."].
- LBR is essential for cholesterol synthesis in human cells despite TM7SF2
  [PMID:27336722 "we observed a near-complete loss of cholesterol synthesis in LBR
  KO cells"]; disease point mutants lose NADPH affinity [PMID:27336722
  "Disease-associated LBR point mutants LBR N547D and LBR R583Q show a decreased
  affinity for NADPH compared to wild-type LBR."].

## Localization
- Inner nuclear membrane integral protein [PMID:8157662]; an ER pool
  [PMID:21327084 "The cytoplasmatic LBR staining co-localized with ER-markers"].

## Structural / chromatin functions (non-core for GO purposes but real)
- N-terminal domain binds lamin B and DNA [PMID:8157662], linker DNA with high
  affinity [PMID:10828963], HP1 proteins [PMID:8663349] via a variant PxVxL
  chromo-shadow-domain-binding motif [PMID:15882967].
- Dosage-dependent control of neutrophil nuclear shape; heterozygous loss =
  Pelger-Huet anomaly [PMID:12118250 "We found that expression of the lamin B
  receptor affects neutrophil nuclear shape and chromatin distribution in a
  dose-dependent manner."].
- Xist binds LBR to recruit the inactive X to the lamina (mouse) [PMID:27492478].

## Curation decisions
- GO:0005515 protein binding: HP1 paper (PMID:8663349) MODIFY to chromo shadow
  domain binding; all others REMOVE as uninformative.
- GO:0140463 chromatin-protein adaptor activity (IEA, ortholog): marked
  over-annotated — geometry is the reverse of the definition.
- Oxidoreductase class IEA terms: MODIFY to GO:0050613.

## Pathway placement
- Post-squalene cholesterol synthesis; C14 reduction of
  4,4-dimethylcholesta-8,14,24-trienol (FF-MAS -> T-MAS) in the Bloch branch
  (Reactome R-HSA-194674). Module `cholesterol_synthesis_post_lanosterol` is
  owned by another group (W2-CHOL-A).

## Deep research
`just deep-research-falcon human LBR` was attempted on 2026-10-09 and failed
("All providers failed"); the literature review above was done manually instead.
