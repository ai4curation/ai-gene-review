# LMAN1 (P49257) / Protein ERGIC-53 — review notes

## Identity and overview
LMAN1 (gene synonyms ERGIC53, F5F8D) encodes Protein ERGIC-53, a 510-aa type I
single-pass transmembrane protein of the early secretory pathway. UniProt names it
"Protein ERGIC-53", "ER-Golgi intermediate compartment 53 kDa protein", "Gp58",
"Intracellular mannose-specific lectin MR60", and "Lectin mannose-binding 1".

It is an **L-type (leguminous-type) lectin** cargo receptor, NOT a glycosidase/mannosidase.
Its luminal carbohydrate-recognition domain (CRD; L-type lectin-like domain, residues 44-267)
binds high-mannose N-glycans in a Ca2+-dependent manner; carbohydrate ligand-binding residues
include 88, 121, 156, 178, 251-253 and Ca2+-binding residues 152, 154, 156, 181
[file:human/LMAN1/LMAN1-uniprot.txt "ligand="Ca(2+)""].

## Core molecular function: mannose-specific lectin
- ERGIC-53 = MR60, an intracellular mannose-specific lectin
  [file:human/LMAN1/LMAN1-uniprot.txt "is identical to MR60, an intracellular mannose-"].
- UniProt FUNCTION: "Mannose-specific lectin. May recognize sugar residues of glycoproteins..."
  [file:human/LMAN1/LMAN1-uniprot.txt "Mannose-specific lectin"].
- The F5F8D1 variant W67S (in the CRD) abolishes both MCFD2 interaction and the
  ability to bind D-mannose [file:human/LMAN1/LMAN1-uniprot.txt "ability to bind D-mannose"];
  the paper shows recombinant WT LMAN1 binds D-mannose but the mutant cannot
  [PMID:19787799 "wild-type LMAN1 could bind to D-mannose, but that of the mutant could not"].
- ERGIC-53 and VIP36 are L-type lectins functioning as cargo receptors for N-linked glycoproteins;
  ERGIC-53 has broad specificity / lower affinity for high-mannose oligosaccharides
  [PMID:24498414 "function as cargo receptors for trafficking certain N-linked glycoproteins"].

## Core cellular component: ERGIC / ER / COPII vesicle
- Cycles between ER, ERGIC and cis-Golgi. UniProt SUBCELLULAR LOCATION:
  ERGIC membrane (single-pass type I), Golgi apparatus membrane, ER membrane
  [file:human/LMAN1/LMAN1-uniprot.txt "Endoplasmic reticulum-Golgi intermediate"].
- LMAN1 is "a mannose-binding type 1 transmembrane protein localized to the endoplasmic
  reticulum-Golgi intermediate compartment (ERGIC)" [PMID:12717434 "localized to the
  endoplasmic reticulum-Golgi intermediate compartment"].
- ERGIC proteomics enriched ERGIC-53 in ERGIC membranes [PMID:15308636 "enriched 110-fold
  over the homogenate for ERGIC-53"].

## Core biological process: ER-to-Golgi cargo receptor transport of FV/FVIII
- LMAN1 + MCFD2 form a cargo receptor that transports coagulation factors V and VIII
  from the ER to the Golgi. MCFD2 is localized to the ERGIC by a Ca2+-dependent interaction
  with LMAN1 [PMID:12717434 "MCFD2-LMAN1 complex forms a specific cargo receptor for the
  ER-to-Golgi transport of selected proteins"].
- cargo receptor complex (GO:0062137) — LMAN1-MCFD2 (ComplexPortal CPX-8001).
- Both proteins required, but they have separable roles: cargo binding/transport is
  carried out by MCFD2, with LMAN1 acting primarily as a shuttling carrier of MCFD2;
  N-glycan binding by LMAN1 is not essential for FV/FVIII transport
  [PMID:36490287 "cargo binding and transport are carried out by MCFD2 and that LMAN1
  primarily serves as a shuttling carrier of MCFD2"].
- Structural basis: crystal structures of LMAN1-CRD/MCFD2 complex with Ca2+
  [PMID:20138881 "crystal structure of the LMAN1/MCFD2 complex"]; ERGIC-53-CRD binds MCFD2
  through a surface remote from the sugar-binding site, sugar-binding independent
  [PMID:20142513 "ERGIC-53-CRD binds MCFD2 through its molecular surface remote from the
  sugar-binding site"].

## Disease: combined factor V and factor VIII deficiency (F5F8D1, MIM 227300)
- ERGIC-53 mutations cause combined deficiency of coagulation factors V and VIII; the protein
  may function as a chaperone/receptor for ER-to-Golgi transport of a subset of secreted
  proteins including FV and FVIII [PMID:9546392 "ERGIC-53 may function as a molecular
  chaperone for the transport from ER to Golgi of a specific subset of secreted proteins,
  including coagulation factors V and VIII"].
- F5F8D is due to mutations in either LMAN1 or MCFD2 [PMID:16304051 "LMAN1 and MCFD2 form a
  protein complex that functions as a cargo receptor ferrying FV and FVIII from the
  endoplasmic reticulum to the Golgi"].
- MCFD2 C-terminal deletion impairs ERGIC-53 binding and causes F5F8D
  [PMID:17971482 "The ERGIC-53/MCFD2 protein complex functions as transport receptor of
  coagulation factors V and VIII"].
NOTE: protein folding and blood coagulation are downstream/physiological consequences of
the cargo-transport role; ERGIC-53 is not itself a folding enzyme. Keep as non-core.

## Golgi/ERGIC architecture
- Cargo receptors Surf4, ERGIC-53, and p25 are required to maintain the architecture of
  ERGIC and Golgi by controlling COPI recruitment; silencing Surf4+ERGIC-53 reduces ERGIC
  clusters and fragments the Golgi without affecting anterograde transport
  [PMID:18287528 "cargo receptors are essential for maintaining the architecture of ERGIC
  and Golgi by controlling COP I recruitment"].
- Golgi organization (GO:0007030, IMP) is supported here. The same paper underpins the
  negated GO:0034498 (early endosome to Golgi transport): ERGIC-53 acts in the ER/ERGIC/Golgi
  early secretory pathway and retrograde COPI recycling, NOT in endosome-to-Golgi traffic,
  consistent with the GOA NOT|involved_in qualifier.

## Interactors (bare GO:0005515 protein binding — keep as non-core)
From UniProt INTERACTION block and references:
- MCFD2 (Q8NI22) — co-receptor; many IPI papers (16304051, 17971482, 19787799, 20138881,
  20142513, 33961781, 35271311) record the LMAN1-MCFD2 interaction
  [file:human/LMAN1/LMAN1-uniprot.txt "MCFD2; NbExp=15"].
- ERP44 (Q9BS26) — thiol-mediated retention; binds the hexameric lectin
  [PMID:17805346 "ERp44...interacts with ERGIC-53"].
- SURF4 (O15260) — cargo receptor [PMID:18287528].
- RAB3GAP1/RAB3GAP2 (Q15042/Q9H2M9) and UBXN6 (Q9BZV1) — via C-terminal tail (UBXD1/p97)
  [PMID:22337587 "novel (Rab3GAP1/2 complex...) interactions"].
- SERPINA1/alpha-1 antitrypsin (P01009) [PMID:31142615].
- BET1 (O15155) — ER-to-Golgi SNARE [PMID:34779586 "we establish BET1...identified ERGIC-53
  as a novel interaction partner of BET1"].
- TMEM115 (Q12893) — Golgi retrograde [PMID:24806965].
- O75612 (PMID:9774442) — oncofetal bile salt-dependent lipase cloning paper; IntAct capture.

## Peripheral / over-annotation calls
- metal ion binding (GO:0046872, EXP DisProt PMID:24498414): Ca2+ is a structural cofactor
  of the CRD; keep as non-core.
- extracellular matrix (GO:0031012 HDA), extracellular exosome (GO:0070062 HDA),
  membrane (GO:0016020 HDA/TAS), sarcomere (GO:0030017 IEA), endomembrane system
  (GO:0012505 IEA): proteomics/electronic over-annotations; mark over-annotated or non-core.
- negative regulation of protein localization to mitochondrion (GO:1903748, HMP PMID:24270810):
  high-content parkin RNAi screen hit; peripheral, keep as non-core.

## Reactome localization (TAS)
Reactome curates ERGIC-53 in COPII vesicle budding/transport (ER membrane, ERGIC membrane,
ER-to-Golgi transport vesicle membrane). Correct compartments; redundant. Reactome
R-HSA-5694431 "Hexameric LMAN1:MCFD2 bind glycosylated Factor V and VIII precursors" and
R-HSA-947991 "Transport of glycoproteins with Man8 (or Man9) N-glycans to the Golgi" directly
reflect the cargo-receptor function.
