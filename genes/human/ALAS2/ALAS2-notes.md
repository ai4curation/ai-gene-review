# ALAS2 (human) — review notes

UniProtKB: P22557 (HEM0_HUMAN). Gene: ALAS2 (HGNC:397; synonyms ALASE, ASB). X chromosome (Xp11.21).
EC 2.3.1.37. Belongs to the class-II PLP-dependent aminotransferase family.

## Core biology (grounded in ALAS2-uniprot.txt + cached publications)

- ALAS2 is the **erythroid-specific 5-aminolevulinate synthase**, the **first and rate-limiting
  enzyme of heme biosynthesis** in erythroid cells.
  [PMID:32499479 "The first and rate-limiting step is carried out by 5′-aminolevulinate synthase (ALAS; EC 2.3.1.37) in the mitochondria"]
  [PMID:34492704 "itaconyl-CoA is a competitive inhibitor of the erythroid-specific 5-aminolevulinate synthase (ALAS2), the first and rate-limiting step in heme synthesis"]
- Catalyses the **PLP-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid
  (ALA), with CoA and CO2 as by-products.**
  [file:human/ALAS2/ALAS2-uniprot.txt "Catalyzes the pyridoxal 5'-phosphate (PLP)-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid (ALA), with CoA and CO2 as by-products"]
  [PMID:32499479 "ALAS catalyses the pyridoxal 5′-phosphate (PLP)-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid (ALA), with CoA and CO2 as by-products"]
  Rhea:RHEA:12921; EC=2.3.1.37.
- ALAS2 is **PLP-dependent**; PLP is covalently attached to active-site Lys391 as an internal aldimine
  [PMID:32499479 "PLP is covalently attached to the active site lysine (Lys391 in human ALAS2 (hsALAS2)) as an internal aldimine adduct"].
  UniProt: MOD_RES 391 N6-(pyridoxal phosphate)lysine; COFACTOR pyridoxal 5'-phosphate.
- Two isozymes: ALAS1 (housekeeping/ubiquitous, 3p21.2) and ALAS2 (erythroid, Xp11.21).
  [PMID:32499479 "ALAS1 (gene location 3p21.2) is the housekeeping enzyme ... ALAS2 (gene location Xp11.21) is predominantly expressed in erythroid progenitor cells, and synthesizes 85–90% of total body heme specifically for hemoglobin production during erythropoiesis"]
- **Homodimer** (obligate; each active site formed from both subunits).
  [PMID:32499479 "Like its orthologs, hsALAS2 is an obligate homodimer in that each active site is formed from both monomeric subunits, with one PLP molecule bound per active site"]
- **Localization: mitochondrion.** UniProt SUBCELLULAR LOCATION = Mitochondrion inner membrane,
  peripheral membrane protein; localizes to the **matrix side** of the inner membrane.
  [file:human/ALAS2/ALAS2-uniprot.txt "Localizes to the matrix side of the mitochondrion inner membrane"]
  Reactome (R-HSA-189442) and InterPro place it in the mitochondrial matrix. The N-terminal 49-aa
  transit peptide targets the protein to mitochondria.
- **Regulation:** IRE in the 5'UTR couples translation to iron availability
  [PMID:2050125 "An iron-responsive element (IRE) motif has been identified in the 5'-untranslated region of the human erythroid ALAS mRNA"];
  protein stabilized by hypoxia / proteasome inhibition (LXXLAP prolyl-hydroxylation/vHL pathway)
  [PMID:16234850 "Hypoxia (1% O2) and inhibition of the proteasome increased both the stability and the specific activity of ALAS2"];
  competitively inhibited by itaconyl-CoA [PMID:34492704]; C-terminal autoinhibitory loop
  [PMID:32499479 "C-terminus is a self-inhibitory loop"].
- **Interactions:** SUCLA2 (β subunit of ATP-specific succinyl-CoA synthetase; UniProt Q9P2R7) —
  physiologically meaningful (channels/supplies succinyl-CoA).
  [PMID:10727444 "mitochodrially expressed SCS-betaA associates specifically with ALAS-E and not with ALAS-N"]
  BANP (Q8N9N5) from a large-scale Y2H interactome map [PMID:25416956] — not functionally characterized.

## Disease
- Loss-of-function missense mutations → **X-linked sideroblastic anemia (XLSA / SIDBA1, MIM 300751)**;
  many characterized in vitro to reduce enzyme activity (K156E [PMID:21252495]; 10 missense in
  [PMID:21309041]).
- C-terminal frameshift/deletion **gain-of-function** mutations → **X-linked (dominant) protoporphyria
  (XLDPT/XLDPP, MIM 300752)**; can also aggravate other erythropoietic disorders (e.g. CEP modifier,
  Y586F [PMID:21653323]).

## GOA MF term
- GOA carries **GO:0003870 5-aminolevulinate synthase activity** (verified in ALAS2-goa.tsv).
  This is the exact current term; used for core_functions molecular_function.

## Annotation review disposition summary
- MF 5-aminolevulinate synthase activity (GO:0003870): core; multiple EXP/IDA/IMP + IBA/IEA → ACCEPT.
- BP heme biosynthetic process (GO:0006783): core; ACCEPT (IBA/IEA/ISS/NAS).
- BP heme B biosynthetic process (GO:0006785, IDA): more specific; ACCEPT (heme b is the product of the pathway ALAS2 initiates).
- CC mitochondrion / mitochondrial matrix / mitochondrial inner membrane: ACCEPT (matrix is most informative; IMM is where it sits peripherally on the matrix side).
- BP hemoglobin biosynthetic process (GO:0042541): keep as non-core (downstream physiological role; heme feeds hemoglobin).
- BP erythrocyte differentiation (GO:0030218): keep as non-core (heme flux governs erythroid maturation).
- BP protein binding (GO:0005515, IPI): uninformative MF term → MARK_AS_OVER_ANNOTATED (SUCLA2, BANP, vHL interactions are real but the bare term adds nothing).
- MF transferase activity (GO:0016740, IEA InterPro): too general vs the specific acyltransferase → MODIFY to GO:0003870.
- BP porphyrin-containing compound metabolic process (GO:0006778) / tetrapyrrole biosynthetic process (GO:0033014): broad IEA parents of heme biosynthesis → ACCEPT (correct but general).
- MF pyridoxal phosphate binding (GO:0030170): secondary MF, correct cofactor → ACCEPT.
- BP intracellular iron ion homeostasis (GO:0006879, ISS): mark as non-core (ALAS2 consumes iron pathway indirectly via heme; ISS from ALAS1 ortholog); KEEP_AS_NON_CORE.
- BP response to hypoxia (GO:0001666, IDA) / intracellular oxygen homeostasis (GO:0032364, NAS): O2-dependent stability regulation from PMID:16234850 → KEEP_AS_NON_CORE (regulatory response, not core catalytic function).
