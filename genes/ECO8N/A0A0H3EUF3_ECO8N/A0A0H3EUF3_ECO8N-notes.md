# Notes: A0A0H3EUF3_ECO8N (MphB, macrolide 2'-phosphotransferase II)

## Identity
- UniProt: A0A0H3EUF3 (TrEMBL, unreviewed), 302 aa, ~34.5 kDa.
- Organism: *Escherichia coli* O83:H1 strain NRG 857C (adherent-invasive E. coli, AIEC). NCBITaxon:685038.
- Encoded on plasmid pO83_CORR (OrderedLocusName NRG857_30123). Mobile/plasmid-borne resistance gene.
- UniProt SubName: "Macrolide 2'-phosphotransferase II protein MphB".
- CARD/ARO: ARO:3000318 (mphB); resistance mechanism = antibiotic inactivation [DR line in uniprot.txt].
- NCBIfam HMM: NF000242 (macrolide_MphB) — a curated family HMM specifically for MphB.
- RefSeq WP_000031017.1 (widely distributed, conserved sequence).

## Domain / fold
- Pfam PF01636 (APH, aminoglycoside phosphotransferase) domain, aa 23–265.
- PANTHER PTHR21310 (Aminoglycoside Phosphotransferase Enzymes), subfamily SF15.
- CDD cd05152 (MPH2).
- Gene3D 3.90.1200.10 + 3.30.200.20 (Phosphorylase Kinase domain 1); SUPFAM SSF56112 Protein kinase-like (PK-like).
- => Protein-kinase-like (ePK/APH) fold; this is the structural superfamily shared by aminoglycoside
  phosphotransferases and Ser/Thr/Tyr protein kinases. MphB is a small-molecule (macrolide) kinase, NOT a
  protein kinase and NOT an aminoglycoside kinase despite the family name.

## Function (well established in literature)
- MphB = macrolide 2'-phosphotransferase II (MPH(2')II). Transfers the γ-phosphate of a purine nucleoside
  triphosphate to the 2'-OH of macrolide antibiotics, producing the inactive macrolide 2'-O-phosphate. This
  detoxifies/inactivates the antibiotic and confers macrolide resistance.
  [PMID:10428938 "Macrolide 2'-phosphotransferase [MPH(2')] transfers the gamma phosphate of ATP to the 2'-OH group of macrolide antibiotics."]
- Reaction matches GO:0050073 "macrolide 2'-kinase activity": ATP + oleandomycin = ADP + 2 H+ + oleandomycin 2'-O-phosphate.
- Inactivated product confirmed as oleandomycin 2'-phosphate by TLC.
  [PMID:1330822 "Inactivated oleandomycin was identified as oleandomycin 2'-phosphate by thin-layer chromatography."]

## Substrate / cofactor specificity
- Broad macrolide substrate range: active on BOTH 14-membered (e.g. oleandomycin, erythromycin) AND
  16-membered (e.g. spiramycin, tylosin, josamycin) ring macrolides; also 15-membered. mphB confers
  high-level resistance to spiramycin (16-membered) when expressed in S. aureus.
  [PMID:1330822 "MPH(2')II ... showed high levels of activity with both 14-member-ring and 16-member-ring macrolides."]
  [PMID:9503630 "The gene endowed S. aureus with high-level resistance to spiramycin, a macrolide antibiotic with a 16-membered ring."]
- Phosphate donor: purine nucleotides ITP, GTP and ATP all effective as cofactors.
  [PMID:1330822 "Purine nucleotides, such as ITP, GTP and ATP, were effective as cofactors in the inactivation of macrolides."]
- Divalent metal cation involvement: activity affected by iodine, EDTA, or divalent cations (EDTA inhibition
  is consistent with a Mg2+-dependent phosphotransfer, as for the protein-kinase-like fold).
  [PMID:1330822 "An inhibitory effect of iodine, EDTA, or divalent cations on MPH(2')II activity was observed."]
- Constitutive, intracellular enzyme; pI 5.3, optimum pH 8.2, optimum temp 40°C.
  [PMID:1330822 "MPH(2')II was a constitutive intracellular enzyme ..."]

## Catalytic residues (site-directed mutagenesis)
- Conserved aspartates in the ATP-binding/catalytic region are essential:
  D200, D209, D219, D231 — alanine substitution abolishes oleandomycin inactivation.
  D227A retains ~7% activity (non-essential; involved in recognizing 16-membered macrolides).
  [PMID:10428938 "D200A, D209A, D219A, and D231A mutant strains were unable to inactivate the substrate oleandomycin, while a D227A mutant retained 7% of the activity of the original enzyme."]
  (D200 proposed as catalytic base activating the 2'-OH; D219/D231 implicated in ATP binding — consistent with
  the protein-kinase-like fold catalytic/Mg2+-binding aspartates.)

## mphA vs mphB
- Two distinct enzymes in E. coli: mphA (type I, MPH(2')I) and mphB (type II, MPH(2')II). Both phosphorylate
  the macrolide 2'-OH. mphA is inducible and is regulated by a repressor mphR(A); mphB (this gene) is
  constitutive. mphB has broad activity across 14/15/16-membered macrolides.
  [PMID:9503630 "The genes mphA and mphB encode macrolide 2'-phosphotransferases I and II, respectively, and they confer resistance to macrolide antibiotics in Escherichia coli."]

## GOA status
- QuickGO GOA file is EMPTY (header only) for this TrEMBL accession → existing_annotations starts empty.
- The only electronic GO term on the UniProt record is GO:0016740 "transferase activity" (IEA:UniProtKB-KW),
  which is far too general. The correct specific MF is GO:0050073 (macrolide 2'-kinase activity).

## GO terms to assign (NEW)
- MF: GO:0050073 macrolide 2'-kinase activity (exact; supported by all biochemical refs).
- BP: GO:0046677 response to antibiotic (resistance/detoxification). Possibly GO:0017001 antibiotic catabolic
  process — but phosphorylation inactivates (modifies) rather than catabolizes/degrades the macrolide, so
  "response to antibiotic" is the safer/standard resistance BP; antibiotic catabolic process is arguable.
- MF supporting: GO:0016301 kinase activity / phosphotransferase; ATP binding (GO:0005524) — but uses
  ITP/GTP too, so a narrow ATP-binding term is not ideal; the specific GO:0050073 already captures the activity.

## References (PMIDs cached)
- PMID:21108814 — AIEC NRG857C genome (source of this sequence/accession).
- PMID:1330822 — Purification & characterization of MPH(2')II (Kono et al. 1992). KEY biochemistry.
- PMID:9503630 — mphB expression in S. aureus; 16-membered macrolide (spiramycin) resistance (Noguchi 1998).
- PMID:10428938 — Functional amino acids (catalytic Asp residues) of MPH(2')II (Taniguchi 1999). KEY mechanism.

## Update: falcon deep research (2026-06-12) — additional references incorporated

Falcon deep research completed (genes/ECO8N/.../A0A0H3EUF3_ECO8N-deep-research-falcon.md, 24 citations)
and surfaced three additional high-value primary papers, now cached and added to the review:

- PMID:28416110 — Fong et al. 2017, Structure. "Structural Basis for Kinase-Mediated Macrolide Antibiotic
  Resistance." First crystal structures of MPH(2')-I and MPH(2')-II (the MphB class), apo and with GTP analogs
  + six macrolides. Confirms the bi-lobed APH/protein-kinase-like fold with a large interdomain linker forming
  an expanded, hydrophobic macrolide-binding pocket (conserved aspartate negative patch) → rationalizes broad
  spectrum. Structures captured with GTP analogs (GTP a preferred donor in vitro).
  [PMID:28416110 "We present structures for MPH(2')-I and MPH(2')-II in the apo state, and in complex with GTP analogs and six different macrolides."]
- PMID:29317655 — Pawlowski et al. 2018, Nat Commun (PMC5760710, full text). "The evolution of substrate
  discrimination in macrolide antibiotic resistance enzymes." Mass-spec confirms MphB phosphorylates the
  desosamine 2'-OH of erythromycin; revises older narrow-spectrum view — MphB inactivates azithromycin AND
  telithromycin and confers resistance to all macrolides tested. MphB widespread/mobilized in Gram-negatives.
  [PMID:29317655 "we found that MphB confers resistance to all macrolides tested...and inactivates both telithromycin and azithromycin"]
  [PMID:29317655 "Using tandem mass spectrometry, we also confirmed that MphB phosphorylates the desosamine 2′-OH of erythromycin"]
- PMID:15033229 — Taniguchi et al. 2004, FEMS Microbiol Lett. "The role of histidine residues conserved in the
  putative ATP-binding region of macrolide 2'-phosphotransferase II." His205 critical (H205A <1% activity).
  [PMID:15033229 "the specific activity of the H205A mutant enzyme was reduced to less than 1% of that of the wild enzyme."]

Net effect on review: description strengthened (broad spectrum incl. azithromycin/telithromycin; crystal
structures; GTP preference; His205). GO calls unchanged (GO:0050073 MF, GO:0046677 BP) — now multiply
supported. suggested_questions/experiments revised since the structure (Fong 2017) and broad-spectrum
question (Pawlowski 2018) are now answered.

Note on providers: perplexity not configured in this container (only openai/falcon); openai API key invalid
(401). falcon's wrapper reported a 600s timeout but the Edison run actually completed and wrote the report +
artifacts. `just` is not installed here, so underlying `uv run ai-gene-review ...` commands were used directly.

## Update: CARD ARO:3000318 (mphB) — curated AMR data incorporated

CARD entry https://card.mcmaster.ca/ARO:3000318 (AMR Gene Family: Macrolide phosphotransferase (MPH);
mechanism: antibiotic inactivation; Protein Homolog Model, BLASTP bitscore cutoff 600). Curated drug list:
erythromycin, roxithromycin, clarithromycin, dirithromycin, oleandomycin (14-membered), azithromycin
(15-membered), spiramycin, tylosin (16-membered), and the ketolide telithromycin. Mechanism: phosphorylation
at the 2'-OH of the desosamine sugar of 14- and 16-membered macrolides. Two CARD-cited PMIDs newly added:

- PMID:8900063 — Noguchi et al. 1996, FEMS Microbiol Lett. Original cloning/sequencing of mphB. KEY identity
  anchor: encodes a 302-aa / 34483-Da protein, matching this UniProt entry (302 aa, 34485 MW) exactly.
  [PMID:8900063 "mphB encoded a protein of 302 amino acids with a molecular mass of 34483 Da."]
- PMID:17302923 — Chesneau et al. 2007, FEMS Microbiol Lett. Resistance phenotypes of mph genes in an
  efflux-deficient E. coli AG100A host. mphB confers spiramycin + telithromycin resistance; in this older
  study azithromycin resistance was attributed uniquely to mphA — the narrow-spectrum view of MphB later
  overturned by Pawlowski 2018 (PMID:29317655).
  [PMID:17302923 "The mph(C) gene, as reported for mph(B), also conferred resistance to spiramycin"]
  [PMID:17302923 "The four investigated genes conferred resistance to telithromycin."]

Net effect: identity now triple-anchored (UniProt SubName + CARD ARO:3000318 + cloning paper exact 302aa/
34483Da match + NCBIfam NF000242 macrolide_MphB HMM). Description substrate range expanded to the full
curated CARD drug list and the historical narrow→broad spectrum reassessment documented. GO calls unchanged.
