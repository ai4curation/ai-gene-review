# MCEE (Q96PE7) review notes

Human methylmalonyl-CoA epimerase, mitochondrial. HGNC:16732. EC 5.1.99.1.

## Deep research status
`just deep-research-falcon human Q96PE7 --alias MCEE` failed in this environment:
`scripts/deep_research_wrapper.py` uses `dict | None` annotation syntax and raised
`TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'` (Python-version
incompatibility). No `MCEE-deep-research-*.md` was produced. Per instructions I did NOT
fabricate one. Review is grounded in UniProt (`MCEE-uniprot.txt`), the seeded GOA TSV,
cached `publications/PMID_*.md`, the two cached Reactome entries, and the dismech
Methylmalonic_Acidemia disorders KB (which covers MMUT/MMAA/MMAB; MCEE not detailed there).

## Core verified biology
- Function: methylmalonyl-CoA epimerase / DL-methylmalonyl-CoA racemase. Catalyses
  (R)-methylmalonyl-CoA = (S)-methylmalonyl-CoA (Rhea:RHEA:20553; ChEBI 57326/57327).
  [UniProt CATALYTIC ACTIVITY; ECO:0000269|PubMed:11481338]. This is the epimerisation
  step between propionyl-CoA carboxylase (PCC) and methylmalonyl-CoA mutase (MMUT),
  providing the (2S)/(R)-configured isomer that MMUT requires.
- PMID:11481338 (Bobik & Rasche 2001) identified the human gene and confirmed
  DL-methylmalonyl-CoA racemase activity biochemically ("both encode
  DL-methylmalonyl-CoA racemases"). This is the IDA basis for GO:0004493, GO:0046491,
  and GO:1901290 (succinyl-CoA biosynthetic process — the pathway outcome).
- Localisation: mitochondrion / mitochondrial matrix. UniProt: TRANSIT 1..36
  (Mitochondrion), CHAIN 37..176. SUBCELLULAR LOCATION Mitochondrion. Supported by
  HTP mito-proteome (PMID:34800366) and Reactome (matrix). Multiple concordant lines.
- Fold/cofactor: VOC (vicinal-oxygen-chelate) / glyoxalase superfamily (PROSITE VOC
  PS51819; Pfam Glyoxalase_4; CDD MMCE cd07249; InterPro IPR029068/IPR017515). Binds a
  divalent metal — Co(2+) modelled in crystal structure (PDB 3RMU, 6QH4; BINDING 50,122,172
  to Co2+, Ref.8 SGC). UniProt keywords: Cobalt, Metal-binding. Note GO:0046872 "metal ion
  binding" IEA-UniProtKB-KW appears in the UniProt DR block but is NOT in the GOA TSV, so it
  is not an existing_annotation line; captured as a proposed_new_term instead.
- Disease: Methylmalonyl-CoA epimerase deficiency (MCEED, MIM:251120), a usually mild
  methylmalonic aciduria; homozygous nonsense mutation (PMID:16752391, INVOLVEMENT IN MCEED).

## GOA annotation dispositions
- GO:0004493 methylmalonyl-CoA epimerase activity — IBA / IEA(EC 5.1.99.1) / TAS(Reactome)
  / IDA(PMID:11481338). All ACCEPT; IDA is the experimental core; EC/RHEA IEA is a correct
  mapping. Core MF.
- GO:0046491 L-methylmalonyl-CoA metabolic process — IBA and IDA(11481338). ACCEPT.
  Directly describes the substrate/product it metabolises. Core BP.
- GO:1901290 succinyl-CoA biosynthetic process — IDA(11481338). Involved_in: MCEE is an
  intermediate step feeding succinyl-CoA production (via MMUT). ACCEPT as the pathway
  outcome (keep; slightly downstream but curator-attributed experimental, correct pathway).
- GO:0019626 short-chain fatty acid catabolic process — TAS(Reactome R-HSA-71032
  "Propionyl-CoA catabolism"). ACCEPT; this is the pathway MCEE genuinely acts in
  (propionyl-CoA is a short-chain acyl/fatty-acid-derived species). Keep.
- GO:0005739 mitochondrion (IEA-SubCell, TAS is_active_in PMID:11481338, HTP PMID:34800366)
  and GO:0005759 mitochondrial matrix (TAS Reactome) — ACCEPT all; matrix is most specific
  and is the core location.
- GO:0005515 protein binding — 4 IPI lines from large-scale interactome maps
  (PMID:25416956 proteome-scale map; 25910212 macromolecular perturbations; 31515488
  variant PPI disruption; 32296183 HuRI binary interactome). Interactors AGTRAP, CD81,
  CMTM5, STX8 are membrane/trafficking proteins — no plausible functional relationship to
  a soluble mitochondrial-matrix epimerase; these are almost certainly Y2H systematic-screen
  artifacts. Bare "protein binding" is uninformative. Per curation policy: MARK_AS_OVER_ANNOTATED
  (not REMOVE — they are experimental IPI).
