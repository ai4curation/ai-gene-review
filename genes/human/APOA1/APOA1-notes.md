# APOA1 (human, P02647) curation notes

## Provenance and method

No deep-research provider keys were available for this session, so no
`-deep-research-<provider>.md` file exists. The literature search was done
manually (2026-11-23) with PubMed (queries: "apolipoprotein A-I ABCA1 JAK2
STAT3"; "Janus kinase 2 modulates the apolipoprotein interactions with ABCA1")
plus the abstracts/full texts of every PMID cited in the GOA file, cached under
`publications/`. Most cached papers are abstract-only; full text was available
for PMID:23726972, PMID:21481393 and the interactome screens.

## Biology summary

- APOA1 encodes the 267-residue preproprotein of apolipoprotein A-I, the major
  protein of plasma HDL, made by liver and small intestine and secreted
  [file:human/APOA1/APOA1-uniprot.txt "Major protein of plasma HDL, also found in
  chylomicrons. Synthesized in the liver and small intestine."].
- Core roles: reverse cholesterol transport by accepting cellular phospholipid
  and cholesterol through ABCA1 and acting as LCAT cofactor
  [file:human/APOA1/APOA1-uniprot.txt "Participates in the reverse transport of
  cholesterol from tissues to the liver for excretion by promoting cholesterol
  efflux from tissues and by acting as a cofactor for the lecithin cholesterol
  acyltransferase (LCAT)."].
- ABCA1-dependent lipid efflux to apoA-I: [PMID:11162594 "ApoA-I and all of the
  other exchangeable apolipoproteins tested (apoA-II, apoA-IV, apoC-I, apoC-II,
  apoC-III, apoE) showed greater than a threefold increase in cholesterol and
  phospholipid efflux from ABCAI-GFP transfected cells compared to control
  cells."]; [PMID:14703508 "ABCA1-mediated free cholesterol and phospholipid
  efflux to apolipoprotein A-I (apoA-I) were tightly coupled to each other both
  temporally and after treatment with ABCA1 inhibitors."].
- LCAT cofactor: [PMID:4335615 "A protein cofactor of lecithin:cholesterol
  acyltransferase."] (abstract-only record; activation of LCAT by apoA-I is
  textbook biochemistry).
- HDL reconstitution: [PMID:190223 "The two types incorporated all of the lipid
  constituents of native HDL and contained 2 and 3 mol of apo A-I,
  respectively."].
- SR-BI ligand on HDL: [PMID:10764676 "free apoAI,
  palmitoyl-oleoyl-phosphatidylcholine (POPC)-AI, and HDL are good ligands for
  human SR-BI"].
- Human genetics: L178P heterozygotes have ~50% apoA-I and low HDL-C
  [PMID:15464323 "Heterozygotes exhibited lower plasma levels of apoA-I (-50%; p
  < 0.0001) and high-density lipoprotein cholesterol (-63%; p < 0.0001)."].
- ABCA1 protein stabilization by apoA-I: [PMID:16210729 "In contrast, apoA-I and
  peptides stabilized ABCA1 protein even in the absence of an active JAK2"]; the
  same for ABCA7 [PMID:20495215 "apoA-I and apoA-II stabilize ABCA7 against
  degradation"].
- Amyloid: apoA-I itself forms amyloid (AApoAI amyloidosis)
  [PMID:27992182 "In the presence of heparin, the rate and thioflavin T
  responsiveness of the aggregates formed at pH 4 increase and short
  amyloid-like fibrils are observed"].

## Ligand verdict: apoA-I-mediated signaling pathway (GO:0038027)

Question (LIGANDS_IN_SIGNALING section 3, category A): does APOA1 do work in
the signaling step as ligand, or is it only necessary?

Evidence that apoA-I is the initiating ligand, with ABCA1 as its receptor:

1. ApoA-I binding to ABCA1 stimulates JAK2 autophosphorylation
   [PMID:14668333 "Acute incubation of ABCA1-expressing cells with apoA-I had no
   effect on ABCA1 phosphorylation but stimulated JAK2 autophosphorylation."].
2. ApoA-I activates Cdc42/PAK1/JNK through ABCA1; abolished in Tangier
   fibroblasts and with glyburide [PMID:16443932 "We conclude that ABCA1
   transduces signals from apoA-I by complexing and activating Cdc42 and
   downstream kinases and, therefore, acts as a full apoA-I receptor."].
3. ApoA-I/ABCA1 activates JAK2-STAT3 via STAT3 docking sites on ABCA1, and this
   is separable from lipid transport [PMID:19783654 "Here we show that the
   ABCA1-mediated activation of JAK2 also activates STAT3, which is independent
   of the lipid transport function of ABCA1."]; [PMID:26989082 "We showed that
   activation of STAT3 by the interaction of apoA-I/ABCA1 without cholesterol
   efflux could significantly decrease proinflammatory cytokine expression in
   macrophages."].
4. In human THP-1 macrophages, apoA-I induces tristetraprolin via JAK2/STAT3,
   and blocking the apoA-I/ABCA1 interaction abolishes it [PMID:21339300 "When
   blocking interaction of apoA-I with ATP-binding membrane cassette transporter
   A1 (ABCA1), a major receptor for apoA-I in macrophages, it would almost
   totally abolish the effect of apoA-I on tristetraprolin expression."].

Participation test: the step is ligand binding to the receptor. ApoA-I is the
extracellular protein that binds ABCA1 and triggers the intracellular cascade;
the pathway is named after it, and the GO definition begins with "apolipoprotein
A-I binding to its receptor". This is the ligand role GO assigns to every other
receptor ligand (receptor ligand activity is part_of signal transduction), not
mere necessity or substrate status. The STAT3 branch is separable from lipid
efflux (point 3), so apoA-I is not only the lipid acceptor whose removal
abolishes a downstream readout. Verdict: **yes, APOA1 acts as the receptor
ligand**; NEW involved_in GO:0038027 (IDA, PMID:19783654) is proposed, the GPCR
row from PMID:16443932 is MODIFIED to GO:0038027 (ABCA1 is not a GPCR), and the
receptor-specific binding rows (GO:0034190, GO:0034191, GO:0005102) are MODIFIED
to receptor ligand activity (GO:0048018) per LIGANDS_IN_SIGNALING decision 4.

Caveats: much of the downstream work comes from two groups (Oram/Tang and
C.-K. Tang); several papers use apoA-I mimetic peptides; much is in mouse
macrophages or BHK cells with purified human apoA-I. The role is a secondary,
anti-inflammatory facet; lipid efflux and LCAT activation remain the core.

Comparator: ABCA1 already carries GO:0038027 (IEA, GO_REF:0000108 from
apolipoprotein A-I receptor activity), and ligands in other modules carry their
pathway term (project section 1), so the NEW row follows the established
ligand convention.

## Wrong-gene annotations: PMID:23726972 (apolipoprotein(a), LPA)

Eight UniProt rows (2014-07-30) cite Riches et al. 2013, "Apolipoprotein(a) acts
as a chemorepellent to human vascular smooth muscle cells via integrin alphaVbeta3
and RhoA/ROCK-mediated mechanisms". The cached full text studies recombinant
apo(a), the LPA gene product (UniProtKB:P08519); apoA-I is not mentioned
anywhere in the full text. The rows (chemorepellent activity, negative
chemotaxis, integrin-mediated signaling, positive regulation of Rho signal
transduction, stress fiber assembly, substrate adhesion-dependent cell
spreading, NOT TGF-beta receptor signaling, NOT ERK1/2 cascade) belong to LPA;
QuickGO (queried 2026-11-23) shows none of them on P08519. Recorded as
WRONG_GENE_PRODUCT, CONFIRMED, REPOINT to UniProtKB:P08519.

## Other notable decisions

- GO:0034205 amyloid-beta formation (DisProt, PMID:27992182): the GO term
  comment restricts it to APP cleavage and points to GO:1990000 amyloid fibril
  formation; the paper is on apoA-I's own amyloid. MODIFY to GO:1990000.
- GO:0006656 phosphatidylcholine biosynthetic process (PMID:4335615): LCAT
  consumes phosphatidylcholine (transfers an acyl chain to cholesterol), so a
  cofactor of LCAT is not part of PC biosynthesis. REMOVE.
- Protein oxidation / peptidyl-methionine modification (PMID:12576517): apoA-I
  is the substrate of oxidation, not a participant. MARK_AS_OVER_ANNOTATED.
- Cytosol (Reactome chylomicron reactions): apoA-I is a secreted protein made in
  the secretory pathway; REMOVE.
- Generic protein binding rows: REMOVE per protein-binding policy; the
  informative interactions (ABCA1, LCAT, SR-BI) are captured by other rows.
