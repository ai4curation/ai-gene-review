# Icam1 (rat, UniProt Q00238) - manual literature research

No deep-research API was available for this review; this file summarises literature read
directly from the cached publications (`publications/PMID_*.md`) and the UniProt record.
It was written by hand and is not output from a deep-research provider.

## Identity and structure

- Rat ICAM-1 (CD54, RICAM-I), 545 aa precursor, gene Icam1 (RGD:2857, GeneID 25464).
  Immunoglobulin superfamily, ICAM family; single-pass type I membrane protein
  [UniProt Q00238 "Belongs to the immunoglobulin superfamily. ICAM family."].
- Human ICAM-1 primary structure: "The amino acid sequence specifies an integral membrane
  protein with an extracellular domain of 453 residues containing five immunoglobulin-like
  domains." [PMID:3349522]

## Molecular function: integrin counter-receptor

- ICAM-1 is the ligand of LFA-1 (ITGAL:ITGB2): "ICAM-1 is a ligand of lymphocyte
  function-associated antigen-1 (LFA-1), an alpha beta complex that is a member of the
  integrin family of cell-cell and cell-matrix receptors." [PMID:3349522]
- Mac-1 (ITGAM:ITGB2) binds a distinct site in Ig domain 3: "Both the integrins LFA-1 and
  Mac-1 bind to ICAM-1, an immunoglobulin superfamily member." [PMID:1675157]
- Rat-specific binding: "binding of purified rat LFA-1 to immobilized ICAM-1 was successfully
  detected" [PMID:10556544]; rat T-lymphoma cells "bound avidly to immobilized ICAM-1 and the
  binding was abolished with anti-LFA-1 monoclonal antibodies (mAbs)" [PMID:10556544].

## Biological roles in the rat (antibody/antisense blocking studies)

- Leukocyte adhesion to and extravasation through vascular endothelium:
  - "Intercellular adhesion molecule-1 [ICAM-1 (or CD54)] is expressed by endothelium and
    mediates adhesion and extravasation of leukocytes." [PMID:12097510]; anti-ICAM-1 "markedly
    decreased the migration of opioid-containing leukocytes and of granulocytes,
    monocytes-macrophages, and T cells to the inflamed tissue" [PMID:12097510].
  - "Induction by IL-1beta of endogenous ICAM-1 and KC contributes to leucocyte adhesion to
    inflamed mesenteric vessels." [PMID:10517906]
  - NK (pit) cell recruitment to liver: "Anti-CD54, supposed to block CD54 expression on
    sinusoidal endothelial cells, also decreased the number of pit cells." [PMID:8938183]
  - Endotoxin-induced uveitis blocked by anti-ICAM-1 [PMID:7641842].
- Downstream/indirect consequences of leukocyte recruitment (vasospasm [PMID:12296653],
  gut endothelial barrier dysfunction in pancreatitis [PMID:10201790], Kupffer cell NO
  production [PMID:9062344], cardiomyocyte contractility [PMID:15087287]).

## Outside-in signalling in endothelial cells

- In rat brain endothelial RBE4 cells, "ICAM-1 cross-linking induced the formation of
  numerous actin stress fibers across RBE4 cells" [PMID:17662049]; the pathway runs through
  Src-mediated cortactin phosphorylation and RhoA, requires SHP-2, and is counteracted by
  PECAM-1 engagement [PMID:17662049 "SHP-2 is positively involved in ICAM-1 signaling,
  upstream of the tyrosine phosphorylation of cortactin by Src and of RhoA-mediated actin
  cytoskeleton rearrangements"].
- Note: SHP-2 co-immunoprecipitation with ICAM-1 was weak and ICAM-1 itself was not
  tyrosine phosphorylated [PMID:17662049 "this result suggested a non-conventional or
  indirect interaction between ICAM-1 and SHP-2"].

## Other contexts

- Blood-testis barrier: "overexpression of ICAM-1 in Sertoli cells in vitro enhanced barrier
  function when monitored by transepithelial electrical resistance measurements" while
  soluble ICAM-1 (Ig domains only) perturbs it [PMID:22976294].
- Soluble ICAM-1 is detectable in rat serum [PMID:18413153].
- Expression is strongly inducible by inflammatory cytokines (IL-1, IL-6, IFN-gamma, TNF),
  LPS, hypoxia, glucose, etc.; this accounts for the many IEP "response to X" annotations,
  which document transcriptional regulation of Icam1, not a function of the protein
  [e.g. PMID:7865494, PMID:20643106, PMID:20951496].
