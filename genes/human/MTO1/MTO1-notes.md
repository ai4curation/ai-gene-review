# MTO1 notes

## Deep research

`MTO1-deep-research-claude-code.md` was produced by `just deep-research-claude-code human MTO1 --timeout 1700`.
It finished in 47 s with only 2 web searches (`web_search_requests: 2`) and 4 citations, and the
report states that most full texts were not available to it and that several older papers were cited
from memory. It was used only as a list of leads; every claim in the review is quoted from cached
publications or the UniProt record.

## Function

- MTO1 is the human MnmG/GidA homolog (UniProt: "Belongs to the MnmG family"). It carries an
  FAD/NAD-binding Rossmann domain; the FAD cofactor is assigned by similarity to Aquifex MnmG
  (UniProt COFACTOR, ECO:0000250|UniProtKB:O66962).
- With GTPBP3 (MnmE homolog) it forms the GTPBP3-MTO1 complex that installs 5-taurinomethyluridine
  (taum5U) at U34 of mt-tRNAs Leu(UUR), Trp, Lys, Glu, Gln.
  [PMID:29390138 "Here, we elucidated τm5U biogenesis by confirming that 5,10-methylene-tetrahydrofolate and taurine are metabolic substrates for τm5U formation catalyzed by MTO1 and GTPBP3."]
  [PMID:29390138 "We here clearly demonstrated that τm5(s2)U34 was absent from mt-tRNAs isolated from GTPBP3 KO cells, Mto1 KO cells, as well as fibroblasts of a patient with pathogenic mutations in GTPBP3."]
- In vitro reconstitution used the GTPBP3-MTO1-FLAG complex with taurine, 5,10-CH2-THF, GTP, FAD and K+.
- Endogenous MTO1 co-immunoprecipitates with endogenous GTPBP3 [PMID:33619562 "Using an anti-hGTPBP3 antibody in Co-IP, we confirmed that endogenous hMTO1 was indeed coprecipitated (Figure 1E)."]
- Human MTO1 cDNA complements yeast mto1 [PMID:12011058].

## Disease

- COXPD10: hypertrophic cardiomyopathy + lactic acidosis, combined RC deficiency, rescued by WT MTO1 cDNA
  in patient cells [PMID:22608499]; further families and yeast model [PMID:23929671]; spectrum review
  PMID:29331171; Mto1 mouse model [PMID:25506927]; zebrafish [PMID:33836087].

## Curation decisions

- GO:0160236 contributes_to (IBA, IMP) accepted: activity of the complex; MTO1 is the putative
  FAD-dependent catalytic (methylene transfer) subunit, but the activity is defined only for the complex.
- GO:0050660 FAD binding (IEA, InterPro): accepted as cofactor binding inferred from MnmG family; no direct
  human binding assay found.
- GO:0003723 RNA binding (HDA, mRNA interactome capture): kept as non-core; its physiological RNA ligand
  is tRNA, but no human tRNA-binding assay was found, so no NEW tRNA binding term proposed.
- No NEW mitochondrial translation (GO:0032543) annotation: MTO1 modifies tRNAs that translation then uses;
  translation defects in KO/patient cells are necessity evidence, not participation.
