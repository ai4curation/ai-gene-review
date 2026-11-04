# exaC (Pseudomonas aeruginosa, Q9ZAA1) notes

## Gene and family context
- Cloned and sequenced together with the cytochrome c550 gene (exaB) of the ethanol oxidation system [PMID:10075429 "An ORF encoding a NAD(+)-dependent acetaldehyde dehydrogenase (exaC) was located downstream of the cytochrome c550 gene and in the same orientation."]
- The same region carries a truncated exaA (quinoprotein ethanol dehydrogenase, PQQ-dependent) and pqqA/pqqB-like ORFs; a cytochrome c550 insertion mutant cannot grow on ethanol [PMID:10075429 "A mutant of P. aeruginosa with an interrupted cytochrome c550 gene was unable to grow on ethanol, which proves that cytochrome c550 is an essential component of the ethanol oxidation system in this organism."]
- 506 aa; ALDH superfamily (Pfam PF00171 Aldedh, InterPro IPR015590 plus the ALDH Cys/Glu active-site signatures IPR016160/IPR029510, CDD cd07559 ALDH_ACDHII_AcoD-like); active sites annotated at residues 262 (Cys) and 301 (Glu); dedicated NCBIfam model NF050026 "AcaldDHExaC"; PANTHER PTHR43111 / PTHR43111:SF1.
- UniProt curated statements (ECO:0000269|PubMed:10075429): FUNCTION "Catalyzes the NAD(+)-dependent oxidation of acetaldehyde to acetate."; CATALYTIC ACTIVITY Rhea RHEA:25294 with PhysiologicalDirection=left-to-right; PATHWAY "Alcohol metabolism; ethanol degradation; acetate from ethanol: step 2/2."; INDUCTION by growth on ethanol. Protein existence level 1 (evidence at protein level) — not used as functional support.

## Review decisions (2026-11-04)
- Core: acetaldehyde dehydrogenase (NAD+) activity (GO:0140087), directly involved in ethanol catabolic process (GO:0006068). ExaC performs the second of the two oxidation steps itself, so the process annotation is participation, not mere necessity.
- Both GO:0140087 rows (EXP from PMID:10075429; IEA from the Rhea mapping of RHEA:25294) are ACCEPT and mutually consistent.
- GO:0004029 aldehyde dehydrogenase (NAD+) activity (ARBA) and GO:0016491 oxidoreductase activity (InterPro2GO) are TOO_GENERAL: both are entailed by the accepted GO:0140087, and nothing in the record supports a broader substrate range. The ARBA rule itself is an unvetted prediction and is not quoted as support; the InterPro signatures are quoted only for what they establish (an intact ALDH catalytic centre).
- No cellular-component annotation exists and none was proposed: the record states no subcellular location, and "soluble/cytoplasmic" is an inference from the NAD(+) cosubstrate, not evidence.
- PAINT: `just paint-losses PSEAE exaC` reports that Q9ZAA1 is not a leaf of the PTHR43111 tree, so no IRD/IKR loss applies and GOA carries no IBA row for this gene, although sibling members (E. coli aldB P37685 and paaZ P77455, S. aureus aldA, Streptococcus exaC Q8E915) do receive GO:0016491 IBA from PTN000916590.
- No source defects found.

## Literature status
- PMID:10075429 is the only primary reference and is cached **abstract-only** (`full_text_available: false`, `full_text_attempted: true`; Microbiology 1999, no PMC id). The enzyme assay behind UniProt's EXP annotation is in the full text, so the activity rows were accepted on the abstract plus the curator's ECO:0000269 statements, per the "do not overrule curators from incomplete evidence" rule. No other exaC-specific primary literature was identified; the UniProt entry cites no further papers.

## Deep research
- No `-deep-research-<provider>.md` file was generated: the repo's deep-research providers are unavailable in this environment. Sources used: the cached publication above, the UniProt record (Q9ZAA1), the PANTHER/PAINT slices for PTHR43111, and GO definitions checked with oaklib (GO:0140087, GO:0004029, GO:0016491, GO:0006068).

## PR #5970 review round (2026-11-04)

- PAO1 carries a near-identical exaC paralog, PA4022 (Q9HX05), the first gene of the
  PA4022-eat-eutBC ethanolamine-catabolic operon [PMID:27325678 "This pathway is encoded
  by the PA4022-eat-eutBC operon and consists of a transport protein (Eat), an
  ethanolamine-ammonia lyase (EutBC), and an acetaldehyde dehydrogenase (PA4022)."].
  Pairwise identities (genes/PSEAE/PA4022/PA4022-bioinformatics/RESULTS.md): PA4022 vs
  ExaC Q9ZAA1 98.2%, PA4022 vs PAO1 exaC/PA1984 (Q9I2C4) 98.4%, Q9ZAA1 vs PA1984 99.4%,
  so Q9ZAA1 (strain ATCC 17933) is the ortholog of PA1984 and PA4022 is a paralog.
  ExaC itself belongs to the ethanol-oxidation (exa) cluster; PA4022 is the
  ethanolamine-pathway enzyme and now has its own review, with GO:0140087 inferred by ISS
  from ExaC. The ethanolamine module uses both as representatives of the non-acylating
  acetaldehyde-oxidation route.
