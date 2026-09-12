# CD320 (Q9NPF0) review notes

CD320 antigen = transcobalamin receptor (TCblR), aka 8D6 antigen / FDC-signaling molecule 8D6.
Single-pass type I plasma-membrane glycoprotein (282 aa; signal 1-35, extracellular 36-229,
TM 230-250, cytoplasmic 251-282). Member of the LDLR family: two LDLR class A (LDLR-A) domains
(53-90, 131-168) separated by an EGF/complement-like cysteine-rich region. Non-enzymatic.

## Core biology
- Cell-surface receptor that captures transcobalamin-bound cobalamin (holo-TC / TC-Cbl) from
  plasma and internalizes it by receptor-mediated endocytosis, supplying cobalamin (vitamin B12)
  to cells throughout the body; the only physiologic route for TC-bound Cbl uptake.
  [PMID:18779389 "The transcobalamin (TC, TCII) receptor (TCblR) on the plasma membrane binds TC- cobalamin (Cbl) and internalizes the complex by endocytosis"]
  [PMID:20524213 "TCblR expressed on the plasma membrane binds transcobalamin (TC) saturated with Cbl (holo-TC) and mediates cellular uptake of Cbl"; "The only route for physiologic transport of TC-bound Cbl into cells is via TCblR"]
- Uptake is Ca2+-dependent; each LDLR-A domain binds a central Ca2+ ion.
  [PMID:27411955 "transcobalamin (TC)-bound Cbl is transported into cells by receptor-mediated endocytosis, which requires Ca2+-dependent complex formation of TC with its cognate cell surface receptor CD320"]
  [PMID:27411955 "Both LDLR-A domains contain central Ca2+ ions bound by four conserved acidic residues and two backbone carbonyls in an octahedral coordination"]
- Expression is coupled to cell cycle; highest in actively proliferating cells and upregulated
  in cancer cells (drug-delivery target). [PMID:20524213; PMID:27411955]
- Binds TC with high affinity/specificity (KD ~1.5 nM); does NOT bind haptocorrin. [PMID:27411955]
- Ligand released at endosomal low pH; receptor recycles to plasma membrane. [PMID:27411955; Reactome R-HSA-3000112]

## Disease
- CD320-related transient/mild methylmalonic aciduria (MATR / MMATC; MIM:613646), autosomal
  recessive, detected on newborn screening. Common in-frame p.E88del (loss of Glu88 in LDLR-A1)
  decreases cobalamin-transport function; most patients clinically asymptomatic.
  [PMID:20524213 "identified a homozygous single codon deletion, c.262_264GAG (p.E88del) ... Inserting the codon by site-directed mutagenesis fully restored TCblR function"]
  UniProt DISEASE MATR; variants E88del, R129L, S142G, G220R.

## Immunology (historic first description; likely secondary/over-annotated)
- First cloned as "8D6 antigen" on follicular dendritic cells (FDCs); mAb 8D6 blocks FDC-mediated
  costimulation of germinal-center B-cell growth. [PMID:10727470]
- FDC-SM-8D6 augments plasma-cell generation from CD27+ precursors. [PMID:11418631]
  These immune roles predate the identification of the B12-receptor function and are plausibly
  downstream of proliferation-coupled B12 supply; kept as non-core. The Growth-factor keyword
  (UniProt-KW -> GO:0008083) derives from this 8D6/FDC work but CD320 is a membrane receptor,
  not a secreted growth factor -> not brought in.

## Interactions
- TCN2 (P20062): the physiological ligand; structural + IntAct evidence. [PMID:27411955]
- JAML/AMICA1 (Q86YT9): CD320-JAML pair from a large immune surface-interactome screen; CD320
  facilitates NK-cell activation in that assay. [PMID:35922511] Secondary immune adhesion role.

## GOA term choices (current labels verified against local go.db)
- GO:0038024 cargo receptor activity (MF) — core
- GO:0031419 cobalamin binding (MF) — core (binds Cbl via the TC-Cbl complex)
- GO:0015889 cobalamin transport (BP) — core
- GO:0006898 receptor-mediated endocytosis (BP) — core mechanism
- GO:0005886 plasma membrane (CC) — core location
- GO:0005509 calcium ion binding (MF) — accept (structural, LDLR-A Ca2+ sites)
- GO:0005783 endoplasmic reticulum — LIFEdb GFP overexpression artifact; over-annotated
- GO:0016020 membrane — accept but generic (subsumed by plasma membrane)
- GO:0005515 protein binding — uninformative; TCN2 IPI captured by cargo-receptor/cobalamin-binding MF; JAML IPI is a secondary immune interaction
</content>
