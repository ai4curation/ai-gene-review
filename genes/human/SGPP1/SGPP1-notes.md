# SGPP1 (human) — gene review notes

UniProt: Q9BX95 (SGPP1_HUMAN). HGNC:17720. Chromosome 14. 441 aa, ~49 kDa.

## Identity and family

SGPP1 is **sphingosine-1-phosphate phosphatase 1** (SPPase1 / SPP-1 / hSPP1).
It belongs to the **type 2 lipid phosphate phosphatase (LPP / PAP2) family**
[file:human/SGPP1/SGPP1-uniprot.txt "Belongs to the type 2 lipid phosphate phosphatase family"].
InterPro/CDD confirm the PAP2 fold: `CDD; cd03388; PAP2_SPPase1`, `Pfam; PF01569; PAP2`,
`SMART; SM00014; acidPPc` [file:human/SGPP1/SGPP1-uniprot.txt].

Domain architecture: an N-terminal disordered/cytosolic region (~1-110, containing the
regulatory phosphosites), followed by up to nine predicted transmembrane helices
(TRANSMEM 132-152, 163-183, 204-224, 227-247, 257-277, 290-310, 322-342, 359-379, 420-440)
[file:human/SGPP1/SGPP1-uniprot.txt]. The three conserved PAP2 phosphatase sequence motifs
(motif I 178-186, motif II 205-208, motif III 248-259) form the catalytic site with
ACT_SITE His-208 (proton donor) and His-255 (nucleophile), plus stabilizing Arg-259
[file:human/SGPP1/SGPP1-uniprot.txt]. The catalytic His-208 is essential: the H208A mutant
abolishes phosphatase activity [file:human/SGPP1/SGPP1-uniprot.txt "H->A: Abolishes phosphatase activity"; PMID:18583713].

## Catalytic activity / molecular function

Specifically dephosphorylates **sphingosine 1-phosphate (S1P)**, dihydro-S1P and phyto-S1P;
does NOT act on ceramide 1-phosphate, lysophosphatidic acid or phosphatidic acid
[file:human/SGPP1/SGPP1-uniprot.txt "Specifically dephosphorylates sphingosine 1-phosphate (S1P), dihydro-S1P, and phyto-S1P. Does not act on ceramide 1-phosphate, lysophosphatidic acid or phosphatidic acid (PubMed:16782891)"].

Two Rhea-defined reactions (both experimentally supported):
- sphing-4-enine 1-phosphate + H2O = sphing-4-enine + phosphate (RHEA:27518) → **S1P phosphatase, GO:0042392** [PMID:12815058; PMID:16782891]
- sphinganine 1-phosphate + H2O = sphinganine + phosphate (RHEA:27514) → **dihydro-S1P phosphatase, GO:0070780** [PMID:12815058]

Experimental support:
- Cloned human SPPase1; transient overexpression gave a "2-fold increase in phosphatase
  activity against S1P and dihydro-S1P" and siRNA knockdown lowered membrane phosphatase
  activity and raised cellular/secreted S1P with a concomitant fall in sphingosine
  [PMID:12815058 "Transient overexpression of hSPPase1 exhibited a 2-fold increase in phosphatase activity against S1P and dihydro-S1P"; "Sphingolipid mass measurements in hSPPase1 siRNA knockdown cells revealed a 2-fold increase of S1P levels and concomitant decrease in sphingosine"].
- IDA S1P-phosphatase activity confirmed in the ceramide-trafficking study [PMID:16782891].

This is the reverse of sphingosine kinase, so SGPP1 is a key node of the **sphingolipid
rheostat**: dephosphorylation recycles sphingosine for re-acylation to ceramide, lowers
S1P signalling, and thereby modulates ceramide levels
[file:human/SGPP1/SGPP1-uniprot.txt "Sphingosine-1-phosphate phosphatase activity is needed for efficient recycling of sphingosine into the sphingolipid synthesis pathway"].

## Subcellular location

Endoplasmic reticulum membrane, multi-pass, experimentally verified by confocal
co-localization with the ER marker calreticulin
[PMID:12815058 "green fluorescent protein-tagged hSPPase1, expressed in either MCF7 or HEK293 cells, co-localized to endoplasmic reticulum with calreticulin"; file:human/SGPP1/SGPP1-uniprot.txt "Endoplasmic reticulum membrane {ECO:0000269|PubMed:12815058}; Multi-pass membrane protein"].
A "Cell membrane" location is only asserted `By similarity` to mouse Q9JI99
[file:human/SGPP1/SGPP1-uniprot.txt "Cell membrane {ECO:0000250|UniProtKB:Q9JI99}; Multi-pass membrane protein"], i.e. not experimentally demonstrated for the human protein.

An HPA IDA nucleoplasm annotation (GO:0005654) exists but is inconsistent with a nine-TM
ER-membrane enzyme; treated as over-annotation (likely antibody cross-reactivity /
high-throughput IF artifact), not removed because it is experimental (IDA).

## Biological roles

- **Sphingosine/S1P metabolism and recycling** — core; feeds sphingosine back to ceramide
  via ceramide synthase [file:human/SGPP1/SGPP1-uniprot.txt "Converts S1P to sphingosine, which is readily metabolized to ceramide via ceramide synthase"].
- **Regulation of ER-to-Golgi ceramide (and protein) trafficking** — S1P treatment of
  SPP-1-overexpressing cells raised long-chain ceramides by inhibiting ER-to-Golgi
  trafficking [PMID:16782891 "SPP-1 regulates ceramide levels in the ER and thus influences the anterograde membrane transport of both ceramide and proteins from the ER to the Golgi apparatus"]. IMP annotation to GO:0035621 (ER to Golgi ceramide transport).
- **Cell viability / apoptosis** — SPPase1 knockdown conferred resistance to TNF-alpha and
  daunorubicin [PMID:12815058 "siRNA-induced knockdown of hSPPase1 endowed resistance to tumor necrosis factor-alpha and the chemotherapeutic agent daunorubicin"].
- **Resistance-artery tone / myogenic vasoconstriction** — via S1P levels
  [file:human/SGPP1/SGPP1-uniprot.txt "modulates resting tone, intracellular Ca(2+) and myogenic vasoconstriction in resistance arteries (PubMed:18583713)"; PMID:18583713].
- **ER stress / unfolded protein response and ER-stress-induced autophagy** — via
  intracellular S1P [file:human/SGPP1/SGPP1-uniprot.txt "Also involved in unfolded protein response (UPR) and ER stress-induced autophagy via regulation of intracellular S1P levels"; PMID:20798685].
- **Epidermal homeostasis / keratinocyte differentiation** — asserted only `By similarity`
  to mouse [file:human/SGPP1/SGPP1-uniprot.txt "Involved in the regulation of epidermal homeostasis and keratinocyte differentiation (By similarity)"]. Human GO annotations for these are ISS/IEA from mouse ortholog Q9JI99.

## Regulation

Multiple mapped phosphoserine/phosphothreonine sites in the N-terminal cytosolic region
(Ser-101, Ser-112, Thr-114) from large-scale phosphoproteomics
[file:human/SGPP1/SGPP1-uniprot.txt MOD_RES 101/112/114].

## Annotation review summary (actions)

- Experimental MF (S1P-phosphatase GO:0042392; dihydro-S1P-phosphatase GO:0070780;
  PMID:12815058/16782891) → ACCEPT as core.
- IBA/IEA/TAS/Reactome MF duplicates of the same activities → ACCEPT (redundant, correct).
- ER membrane location: EXP PMID:12815058 → ACCEPT core; IBA/IEA/TAS duplicates → ACCEPT.
- Plasma / cell membrane (IEA-SubCell, ISS from mouse) → MARK_AS_OVER_ANNOTATED (no human
  experimental evidence; ER is the demonstrated site).
- Nucleoplasm (HPA IDA) → MARK_AS_OVER_ANNOTATED (inconsistent with multipass ER enzyme;
  not removed, experimental).
- sphingosine metabolic process (IBA) → ACCEPT core.
- sphingolipid catabolic process (Reactome TAS; ARBA IEA) → KEEP_AS_NON_CORE (S1P
  dephosphorylation is a recycling/catabolic step but the net biology is recycling into
  synthesis, not net catabolism).
- phospholipid dephosphorylation (IBA) → KEEP_AS_NON_CORE (over-general parent; the
  specific MF term is better).
- ER to Golgi ceramide transport (IMP PMID:16782891) → KEEP_AS_NON_CORE (regulatory /
  downstream, experimentally supported).
- regulation of keratinocyte differentiation & regulation of epidermis development
  (ISS + IEA from mouse Q9JI99) → KEEP_AS_NON_CORE (ortholog-transferred developmental role,
  not the core enzymatic function).
