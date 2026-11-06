# sseJ (STM1631, UniProtKB:Q9FD10) notes

Reviewer notes, 2026-11-06. No deep-research provider file was generated for this
gene; the notes below come from my own reading of the primary literature. The
SPI-2 papers are in the cache: PMID:19887681 (Christen 2009) and PMID:16177296
(Ohlson 2005) have PMC full text, PMID:12496192 (Freeman 2003) and PMID:18996344
(Ohlson 2008) have full text, and PMID:18333886 (Nawabi 2008) and PMID:22740689
(LaRock 2012) are abstract-only in the cache (`full_text_available: false`).

This review was commissioned to test, on a leaf, the argument made in
`genes/PSEAE/estA/estA-notes.md` that the PAINT IBD for GO:0008610 lipid
biosynthetic process at PANTHER node PTN005219546 does not hold for its clade.
That argument was made largely from leaf names. The verdict on this leaf is at
the bottom, and it is not the one the estA review assumed.

## What SseJ is

- SPI-2 type III secretion system effector of *Salmonella* Typhimurium, 408 aa.
  The N-terminal ~140 residues carry the translocation signal; the C-terminal
  domain is a GDSL/SGNH lipolytic-enzyme fold
  [file:SALTY/sseJ/sseJ-uniprot.txt "Belongs to the 'GDSL' lipolytic enzyme
  family."].
- Within the GDSL superfamily its closest functional relatives are the
  glycerophospholipid:cholesterol acyltransferases (GCATs) of *Aeromonas* and
  *Vibrio*, not the carboxylesterases
  [PMID:16177296 "SseJ has the most conservation of catalytic regions with
  glycerophospholipid-cholesterol acyltransferase (GCAT) enzymes"].
- Catalytic triad Ser151 / Asp247 / His384, established by mutagenesis
  [PMID:16177296 "These results suggest that Ser151, Asp247, and His384 residues
  are members of a catalytic triad"]; each single substitution gives
  [PMID:16177296 "an approximately fivefold reduction in activity compared to
  that of wild-type His-SseJ"]. Ser153, the other serine of the G-D-S-L-S motif,
  is not catalytic.

## Localization

- Translocated across the vacuolar membrane into the host cytosol and retained on
  the cytoplasmic face of the *Salmonella*-containing vacuole (SCV), then
  redistributes along *Salmonella*-induced filaments (Sifs)
  [PMID:12496192 "SseJ and SifB, localize to the SCV membrane in infected HEp-2
  cells and subsequently traffic away from the SCV along"];
  [PMID:12496192 "SseJ-HA colocalizes with LAMP-1 on Sifs upon bacterial
  intracellular growth"].
- Ectopically expressed SseJ goes to late endosomes/lysosomes
  [PMID:18996344 "SseJ alone localized to membranous LAMP1 positive, late
  endosomal/lysosomal vesicles"].
- The side of the membrane matters for the activity: SseJ is activated by
  cytosolic RhoA-GTP
  [PMID:22740689 "SseJ is recruited to the cytoplasmic face of the host cell
  phagosome membrane where it is activated upon binding the small GTPase, RhoA"].
- Catalytic-triad mutants still translocate and still localize correctly
  [PMID:16177296 "the ability to localize to vacuolar membranes is not a
  consequence of enzymatic activity"], so localization and catalysis are
  separable.
- UniProt's "Secreted" subcellular location (SL-0243, mapped to GO:0005576
  extracellular region by GO_REF:0000044) records T3SS export. No study places a
  pool of SseJ free in the SCV lumen or in the extracellular medium; the
  flat file itself frames the export as delivery into the host cytosol
  [file:SALTY/sseJ/sseJ-uniprot.txt "Secreted via type III secretion system 2
  (SPI-2 T3SS), and delivered into the host cytoplasm."].

## Biochemistry

Three activities have been reported, and they are not of equal standing.

1. **Deacylase / carboxylesterase (hydrolase).** Purified His-SseJ hydrolyses
   *p*-nitrophenyl butyrate [PMID:16177296 "demonstrating that SseJ functions as
   a deacylase"], and *p*-nitrophenyl palmitate hydrolysis is the readout used
   for RhoA activation [PMID:19887681 "Lipase activity was strongly stimulated in
   the presence of RhoA with an activation profile corresponding to fractions
   containing the SseJ-RhoA complex"]. Both substrates are chromogenic surrogates,
   not lipids, and the authors say so [PMID:16177296 "The PNPB substrate is not
   likely to be physiologic for either protein but was chosen because it is water
   soluble"]. The rate is also low: [PMID:16177296 "indicating that the activity of
   SseJ in this assay is approximately 10-fold lower"] than purified *A.
   salmonicida* GCAT. So "lipase activity" (GO:0016298, hydrolysis of a lipid) is
   not what was measured; carboxylesterase activity is.

2. **Glycerophospholipid:cholesterol acyltransferase (GCAT).** This is the
   physiological reaction, and it is directly demonstrated with identified
   products. Liposomes of DOPC/cholesterol/oleic acid plus purified SseJ and
   GTP-gamma-S-loaded RhoA, analysed by TLC:
   [PMID:19887681 "SseJ efficiently converted DOPC and cholesterol to
   lyso-phosphatidylcholine (lyso-PC) and cholesterol ester (CE)"], with no
   activity for SseJ alone. The acyl donor is the sn-1 position of the
   glycerophospholipid [PMID:19887681 "We found that the GCAT activity of
   activated SseJ specifically cleaved the sn-1 position"], and the acyl acceptor
   is cholesterol, with the product confirmed chemically
   [PMID:19887681 "Analysis of the fluorescent reaction products by TLC confirmed
   the formation of a fluorescent BODIPY"] ...
   [PMID:19887681 "modified cholesterol ester species in the presence of PEDA1"].
   No CoA is present in these assays: the acyl donor is the phospholipid. The
   reaction is therefore EC 2.3.1.43 (phosphatidylcholine-sterol
   O-acyltransferase, GO:0004607), **not** the CoA-dependent sterol
   O-acyltransferase reaction of SOAT/ACAT (GO:0034736: "acyl-CoA + cholesterol =
   a cholesterol ester + CoA").
   Independently, in cells and during infection:
   [PMID:18333886 "Here we show that the SPI-2 effector SseJ esterifies
   cholesterol in vitro, in cells and during infection."], and wild type versus
   DeltasseJ infection [PMID:18333886 "led to higher levels of cholesterol ester
   production in HeLa cells and RAW macrophages and were shown to increase levels
   of lipid droplets"]. UniProt's own synthesis:
   [file:SALTY/sseJ/sseJ-uniprot.txt "Has both deacylase and esterification
   activities in vitro, but esterification is probably the dominant activity in
   host cells."]

3. **Phospholipase A1.** Asserted in the literature as part of the family
   repertoire [PMID:19887681 "SseJ belongs to the GDSL like lipolytic enzyme
   family and exhibits basal deacylase, phospholipase and
   glycerophospholipid-cholesterol acyltransferase (GCAT) activity in vitro"], but
   I did not find an assay on SseJ in which a free fatty acid is the product. The
   sn-1 cleavage experiments were run with cholesterol present and gave the
   cholesteryl ester, i.e. transesterification. I have not asserted a
   phospholipase A1 GO term on that basis.

## Regulation by RhoA

- SseJ is a sensor, not a modifier, of the Rho switch: it binds GTP-loaded RhoA
  and RhoC but has no GEF or GAP activity
  [PMID:19887681 "indicating that SseJ does not function as a GAP or GEF for
  RhoA"], and RhoA-GTP stimulates its activity ~5-fold over RhoA-GDP.
- [PMID:22740689 "only the GTP-bound form of RhoA family members stimulates
  enzymatic activity"]; the binding site overlaps the mammalian effector site
  [PMID:22740689 "SseJ competes effectively with Rhotekin, ROCK, and PKN1 in
  binding to a similar RhoA surface"].
- Binding is needed for both targeting and virulence
  [PMID:22740689 "SseJ binding to RhoA is required for recruitment of SseJ to the
  endosomal network and for full Salmonella virulence"].
- So the GTPase-binding is a genuine, informative molecular function (allosteric
  activation + membrane targeting), not a bare interaction. GO:0017048 "Rho GTPase
  binding" has been merged into GO:0031267 small GTPase binding (checked via
  QuickGO, 2026-11-06), so GO:0031267 is the most specific available term.

## Cellular consequences and virulence

- Esterifying membrane cholesterol depletes free cholesterol
  [PMID:18333886 "Ectopic expression of SseJ reduced cholesterol levels in
  cellular membranes"], which antagonizes SifA
  [file:SALTY/sseJ/sseJ-uniprot.txt "abrogates the ability of SifA to associate
  with cholesterol and LAMP-1 vesicles."].
- Catalysis, not mere presence, drives the phenotypes: catalytic mutants fail to
  down-regulate Sif formation and fail to restore vacuolar-membrane loss to a
  *sifA sseJ* double mutant [PMID:16177296 "provides strong evidence that the
  function of SseJ is to modify the SCV membrane"], and
  [PMID:16177296 "catalytically inactive SseJ mutants demonstrated a virulence
  defect in mice"].
- Co-expression with SifA drives endosomal tubulation, and that too needs the
  triad [PMID:18996344 "These results demonstrate that the enzymatic activity of
  SseJ is essential for ET formation"].

## PANTHER placement (checked 2026-11-06)

`projects/PSEUDOCAP/panther_tree.py node PTN005219546 --contains Q9FD10,O33407`
and `node PTN005220548 --family PTHR45642`:

- PTN005219546 is the LUCA node of PTHR45642, 960 leaves. 952 are eukaryotic (940
  plant GDSL esterase/lipases under PTN005219553, 12 Dikarya); only 8 leaves are
  bacterial, under PTN005220548.
- Those 8 split into two subfamilies:
  - **PTHR45642:SF139** — the autotransporter / surface carboxylesterases:
    *P. aeruginosa* EstA (O33407), *P. aeruginosa* ChoE (Q9HUP2), *Salmonella*
    ApeE (H9L479), two *Gloeobacter* proteins. Both IBD seeds at PTN005219546 are
    here.
  - **PTHR45642:SF141** — a Gammaproteobacteria clade PTN005220549 of three
    leaves: *Salmonella* SseJ (Q9FD10), *Vibrio cholerae* VC_A0218
    "thermolabile hemolysin" (Q9KMV0), and *Xanthomonas campestris* estA
    (Q8P634).
- So SseJ is **not** in EstA's subfamily. The smallest clade containing both is
  PTN008693336 (5 leaves, a DUPLICATION node). SF141 is the GCAT-like branch,
  which is exactly what Ohlson 2005 concluded from the catalytic-region alignment,
  and the *Vibrio* thermolabile hemolysin that sits beside SseJ is the Vibrio
  GCAT homolog.

## Verdict on the GO:0008610 lipid biosynthetic process IBA

**The claim is supported for this gene product; the IBD that delivers it is
still not.** Those are two separate findings and both should be recorded.

Supported, on SseJ's own evidence:

- SseJ itself catalyses the acyl-transfer step that forms cholesteryl ester. The
  product was identified by TLC from purified protein and defined substrates
  (PMID:19887681), by BODIPY-cholesteryl-ester formation in transfected cells
  (PMID:19887681), and by raised cholesteryl ester and lipid droplets in infected
  HeLa and RAW cells with wild type versus DeltasseJ (PMID:18333886). Cholesteryl
  ester is a lipid, and GO:0008610 is "the chemical reactions and pathways
  resulting in the formation of lipids".
- This passes the participation test in root `CLAUDE.md`: the entity that
  performs the step is SseJ, not something else. This is not a necessity
  phenotype. It is the opposite of the EstA case, where an *estA* deletion lacks
  rhamnolipid but RhlA/RhlB/RhlC do the chemistry.
- There is no more specific BP term. QuickGO (2026-11-06) has no "cholesteryl
  ester biosynthetic process" or "sterol ester biosynthetic process";
  GO:0010872/GO:0010873 (regulation of cholesterol esterification) are obsolete.
  GO:0008610 is therefore the most specific existing term, and I have raised a
  `proposed_new_terms` entry for the missing child. Action: ACCEPT.

Comparator check (as root `CLAUDE.md` requires before trusting a lipid-process
claim). Human LCAT (P04180), the eukaryotic phosphatidylcholine-sterol
O-acyltransferase that runs the same reaction, is **not** annotated to GO:0008610;
its BP rows are GO:0008203 cholesterol metabolic process, GO:0046470
phosphatidylcholine metabolic process, GO:0006644 and GO:0034375 HDL remodeling
(QuickGO, 2026-11-06). SOAT1 (P35610) likewise carries GO:0008203, not GO:0008610.
So GO's habit for cholesterol-esterifying enzymes is the *metabolic* branch rather
than *biosynthetic*. I read this as a convention that follows from the absence of a
cholesteryl-ester biosynthesis term rather than a denial that a cholesteryl ester
is made: both enzymes also carry transferase MF terms whose definitions state that
a sterol ester is the product. GO:0008610 is not wrong for SseJ, but a curator
preferring GO:0008203-style terms would be following precedent, and the proposed
new term would resolve the discrepancy. Recorded as a `suggested_questions` entry.

Not supported, as a node assertion:

- The IBD at PTN005219546 sits at LUCA with two seeds, both in SF139, and for
  GO:0008610 only one, EstA, whose evidence is the rhamnolipid-deficient deletion
  phenotype. Nothing about SseJ's GCAT chemistry is inherited from that seed, and
  nothing in the estA evidence predicts it. That SseJ happens to make a lipid is
  independent of why the node was annotated.
- The node's reach is still wrong: 940 plant GDSL esterase/lipase leaves receive
  GO:0008610 IBA with no experimental function annotation of any kind. The
  recommendation in `genes/PSEAE/estA/estA-ai-review.yaml` (withdraw the IBD)
  stands, with one correction: the GO_CENTRAL defect report states that the
  bacterial leaves, "among them Salmonella SseJ (Q9FD10)", offer "no positive
  evidence for a biosynthetic process". That is wrong for SseJ. The right move is
  not to keep the LUCA IBD but to place an IBD for the GCAT chemistry at
  **PTN005220549** (PTHR45642:SF141 — SseJ, Vibrio VC_A0218, Xanthomonas estA),
  seeded by SseJ's own IDA rows, where the phylogenetic claim would actually be
  defensible. Recorded as a `source_defects` entry on the IBA row and as a
  `suggested_questions` entry.

## Molecular-function term choices

- **GO:0034736 cholesterol O-acyltransferase activity** (IDA, PMID:19887681) is
  the wrong reaction: its definition is CoA-dependent ("acyl-CoA + cholesterol"),
  and SseJ's assays contain no CoA — the acyl donor is phosphatidylcholine.
- **GO:0047178 glycerophospholipid acyltransferase (CoA-dependent) activity**
  (IDA, PMID:19887681) is also a different reaction: its definition is
  transacylation between phosphatidylethanolamine and phosphatidylcholine, with
  no sterol acceptor.
- Both describe one half of what SseJ does and neither describes the reaction
  that was measured. **GO:0004607 phosphatidylcholine-sterol O-acyltransferase
  activity** ("phosphatidylcholine + a sterol = a sterol ester +
  1-acylglycerophosphocholine", EC 2.3.1.43, the LCAT/GCAT term) is exactly it.
  Both rows are MODIFYed to it. These are lateral corrections, not refinements.
- **GO:0016298 lipase activity**, **GO:0052689 carboxylic ester hydrolase
  activity** and **GO:0016788 hydrolase activity, acting on ester bonds** all
  describe the real but secondary hydrolase side. The assayed substrates are
  p-nitrophenyl esters, so **GO:0106435 carboxylesterase activity** is the
  accurate term; it is a strict descendant of GO:0052689 and GO:0016788
  (refinement) and a sibling of GO:0016298 (lateral: pNPP is not a lipid).

## Open questions

- Does SseJ have genuine phospholipase A1 activity (free fatty acid as product)
  in the absence of a sterol acceptor, or is hydrolysis only the first half-reaction
  of transesterification?
- What is the in-host acyl acceptor spectrum — only cholesterol, or other sterols
  and alcohols?
- Why is the GCAT rate so low relative to *Aeromonas* GCAT; is it tuned to avoid
  destroying the SCV, as Ohlson 2005 speculates?
