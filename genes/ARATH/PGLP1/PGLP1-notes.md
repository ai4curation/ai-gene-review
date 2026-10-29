# PGLP1 (PGLP1A; At5g36700; UniProtKB:P0DKC3) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are a manual literature summary built only from cached publications in `publications/`
and the UniProt record (`PGLP1-uniprot.txt`). No `-deep-research-*.md` file exists for
this gene.

## Identity

- UniProt P0DKC3, "Phosphoglycolate phosphatase 1A, chloroplastic", gene name PGLP1A,
  locus At5g36700; 362 aa precursor, transit peptide 1-54 (proteomics-defined), HAD-like
  hydrolase superfamily, CbbY/CbbZ/Gph/YieH family (UniProt SIMILARITY, InterPro
  IPR006349 PGP_euk, NCBIfam TIGR01452).
- The literature name is PGLP1. A second UniProt entry, P0DKC4 (PGLP1B, At5g36790),
  carries an identical gene model; the original paper notes a genome double annotation in
  this region [PMID:17478634 "Closer inspection of the corresponding region on chromosome
  5, however, indicated double annotation in this region, including the corresponding two
  PGLP genes."]. All functional work cited here is on At5g36700.

## Molecular function: 2-phosphoglycolate phosphatase (EC 3.1.3.18)

- Recombinant PGLP1 (mature form, without the transit peptide) has PGLP activity
  [PMID:17478634 "Both semipurified proteins showed PGLP activity, 420 μ mol min −1 mg −1
  for PGPL1 and 690 μ mol min −1 mg −1 for PGPL2."].
- Knockout (pglp1-1, SALK_130837) reduces leaf PGLP activity by 97%
  [PMID:17478634 "Enzyme measurements with protein extracts from mutant plants grown under
  0.9% CO 2 revealed a 97% reduction of leaf PGLP activity in Atpglp1-1 plants"].
- UniProt curated function and catalytic activity (ECO:0000269 PubMed:17478634):
  "Photorespiratory enzyme that dephosphorylates the 2-phosphoglycolate produced by the
  RuBisCO oxygenation reaction."; Rhea:14369, 2-phosphoglycolate + H2O = glycolate +
  phosphate.
- Enzyme properties (from plant/algal enzymes; review) [PMID:17478634 "The enzyme is
  highly specific for 2PG ( Husic and Tolbert, 1984 ) and requires Cl − ( Seal and Rose,
  1987 ) and Mg 2+ ions ( Christeller and Tolbert, 1978a ) for its full activity."].
- Redox regulation: H2O2 sulfenylates PGLP1 at Cys-86 and inhibits it under heat stress
  [PMID:38409783 "H2O2 stimulates sulfenylation of the chloroplast-localized
  photorespiratory enzyme 2-phosphoglycolate phosphatase 1 (PGLP1) at cysteine 86,
  inhibiting its activity and promoting the accumulation of the toxic metabolite
  2-phosphoglycolate"].

## Biological process: photorespiration (entry step of the C2 cycle)

- [PMID:17478634 "The chloroplastidal enzyme 2-phosphoglycolate phosphatase (PGLP), PGLP1,
  catalyzes the first reaction of the photorespiratory C(2) cycle"]
- Conditional lethality in air, rescued by high CO2 [PMID:17478634 "The mutant is unviable
  in normal air but grows well in air enriched with 0.9% CO(2)."]; the classical EMS
  mutant CS119 carries a missplicing mutation in At5g36700 [PMID:17478634 "Sequencing of
  genomic DNA from another PGLP-deficient mutant revealed a combined missense and
  missplicing point mutation in At5g36700."].
- Review [PMID:22303256 "2-Phosphoglycolate phosphatase (PGLP, EC 3.1.3.18) catalyzes the
  entry reaction of photorespiration, dephosphorylation of phosphoglycolate formed by the
  oxygenase activity of RUBISCO to glycolate."] and [PMID:22303256 "Thus, At5g36700
  encodes the photorespiratory PGLP in Arabidopsis."].
- The paralog PGLP2 (At5g47760) is active but non-photorespiratory, putatively cytosolic
  [PMID:17478634 "It encodes a putatively cytosolic enzyme, AtPGLP2, which shows PGLP
  activity."].
- Physiological consequence: 2PG that PGLP1 removes inhibits Calvin-Benson enzymes
  [PMID:28947491 "2PG mechanistically achieves this by inhibiting the Calvin-Benson cycle
  enzymes triose-phosphate isomerase and sedoheptulose 1,7-bisphosphate phosphatase."].
  This is a regulatory consequence of the metabolite, not an additional PGLP1 activity; no
  regulatory process term is proposed.
- Thermotolerance: antisense lines are heat-sensitive and overexpressors more tolerant
  [PMID:38409783 "PGLP1 antisense lines have greater heat sensitivity and PGLP1-overexpressing
  plants have higher heat-stress tolerance than the wild type"]. This is a downstream
  consequence of 2PG detoxification; I did not propose a "response to heat" annotation.

## Location: chloroplast stroma

- Predicted 62-aa transit peptide [PMID:17478634 "The protein harbors a predicted 62-amino
  acid chloroplast-targeting peptide"]; the transit peptide cleavage after Met-54 and
  N-acetylation of Thr-55 were mapped by proteomics (UniProt FT TRANSIT, ECO:0007744
  PubMed:22223895).
- Found in the chloroplast proteome [PMID:17478634 "Most recently, protein At5g36700 has
  been detected in the chloroplast proteome ( Peltier et al., 2006 ), which fully supports
  our conclusion."]. Peltier et al. 2006 is the stromal oligomeric proteome (PMID:16207701).
- Mature protein ~34 kDa in vivo after import [PMID:38409783 "its N-terminal chloroplast
  transit peptide is removed when the protein is transported into chloroplasts; thus, the
  molecular weight of mature PGLP1 protein is approximately 34 kD in vivo"].
- TAIR RCA NOT cytosol (PMID:21166475) is consistent: the cytosolic proteome paper set
  aside plastid-targeted proteins.

## Annotation decisions (summary)

- MF GO:0008967 (IMP, IEA): ACCEPT, core.
- MF GO:0016791 phosphatase activity (IBA, IEA): MODIFY to GO:0008967.
- CC chloroplast / plastid / stroma HDA rows: ACCEPT (proteomic screens; stroma is the
  precise compartment). Cytoplasm IBA: MODIFY to chloroplast stroma (PAINT node is a mostly
  cytosolic HAD-phosphatase clade; PGLP1 is plastid-targeted).
- BP ND root: MODIFY to GO:0009853 photorespiration (GOA lacks any photorespiration row
  for P0DKC3 although the IMP paper establishes it).
- PANTHER: UniProt places P0DKC3 in PTHR19288:SF46; no PANTHER id is asserted in the
  review.
