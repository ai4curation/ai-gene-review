# SEPHS2 (human) — review notes

UniProt: Q99611 (SPS2_HUMAN). Gene: SEPHS2 (synonym SPS2). 448 aa. HGNC:19686.

## Identity and core function

SEPHS2 = **Selenide, water dikinase 2** (EC 2.7.9.3), also "Selenium donor protein 2" /
"Selenophosphate synthase 2". It is the catalytically active human selenophosphate
synthetase.

- UniProt FUNCTION: "Selenophosphate synthase that generates the selenium donor
  for selenocysteine biosynthesis by catalyzing formation of selenophosphate from
  selenide and ATP." [file:human/SEPHS2/SEPHS2-uniprot.txt]
- Catalytic activity (Rhea RHEA:18737, EC 2.7.9.3): hydrogenselenide + ATP + H2O =
  selenophosphate + AMP + phosphate + 2 H(+). Evidence ECO:0000305|PubMed:15534230.
  [file:human/SEPHS2/SEPHS2-uniprot.txt]
- Cofactor: binds 1 Mg(2+) per monomer (by similarity to P49903).
  [file:human/SEPHS2/SEPHS2-uniprot.txt]

The reaction product, monoselenophosphate, is the activated selenium donor used
downstream by SEPSECS to convert O-phosphoseryl-tRNA(Sec) to selenocysteyl-tRNA(Sec),
supplying Sec for all selenoproteins.

- PMID:15534230 (Tamura et al. 2004, abstract only): "A labile selenium donor compound
  monoselenophosphate is synthesized from selenide and ATP by selenophosphate synthetase
  (SPS)." Sps2 was cloned from human lung adenocarcinoma cells; the in-frame TGA was
  mutated to TGT (Cys) for expression; Sps2Cys effectively complemented an E. coli selD
  mutant, restoring formate dehydrogenase H activity, whereas Sps1 only weakly
  complemented. Conclusion: "the Sps2 enzyme can function with a selenite assimilation
  system" (Sps1 recycles L-selenocysteine). This is the IMP support for involvement in
  L-selenocysteine biosynthetic process (GO:0016260) and the EC=2.7.9.3 basis.

- PMID:8986768 (Guimarães et al. 1996, full text): original cloning of human/mouse Sps2
  (selD homolog). "Escherichia coli selenophosphate synthetase (SPS, the selD gene
  product) catalyzes the production of monoselenophosphate, the selenium donor compound
  required for synthesis of selenocysteine (Sec) and seleno-tRNAs." Sps2 has an in-frame
  TGA at the putative active site. Using a FLAG-tagged mouse SPS2 they documented
  "readthrough of the in-frame TGA codon and the incorporation of 75Se into SPS2",
  concluding "SPS2 is a selenoenzyme" and proposing an autoregulatory loop ("the
  incorporation of Sec into SPS2"). NAS support for MF and BP.

## SEPHS2 is itself a selenoprotein (autoregulation)

UniProt FT NON_STD 60 = Selenocysteine; ACT_SITE 60; KW "Selenocysteine", "Selenium".
The catalytic residue is a Sec (U) at position 60. Thus SEPHS2's own synthesis depends
on the selenocysteine biosynthesis pathway it feeds — an autoregulatory feature
[PMID:8986768 "is there an autoregulatory mechanism in selenocysteine metabolism?"].
MUTAGEN U60->C "Does not affect the selenophosphate synthase activity"
(ECO:0000269|PubMed:15534230), so the Cys mutant is catalytically competent — this is why
the recombinant Sps2Cys form was used for the E. coli complementation assay.

Human paralog SEPHS1 (SPS1, P49903) does NOT contain Sec (has Thr/Arg at the homologous
position) and is proposed to act in a selenium salvage/recycling role rather than de novo
selenophosphate synthesis; its exact enzymatic function is debated. SEPHS2 is the
Sec-containing, catalytically active enzyme for de novo selenophosphate synthesis.

## Complex membership / interactions

UniProt SUBUNIT: "Homodimer (By similarity). Component of a complex composed of SEPHS1,
SEPHS2, SEPSECS and TRNAU1AP" (PubMed:16508009, PubMed:28414460).
[file:human/SEPHS2/SEPHS2-uniprot.txt]

- PMID:28414460 (Oudouhou et al. 2017, abstract only): BRET in mammalian cells showed
  "selenophosphate synthetases SEPHS1 and SEPHS2 form oligomers in eukaryotic cells";
  "SEPHS2 interacts with SEPSECS and SEPHS1; these interactions were confirmed by
  co-immunoprecipitation." Also reports SEPHS2 SUBCELLULAR LOCATION (cytoplasm) — the
  source of the IDA cytoplasm annotation.

- PMID:33961781 (Huttlin et al. 2021, BioPlex 3.0): the source of the IPI "protein
  binding" (GO:0005515) annotation. GOA WITH/FROM = UniProtKB:P49903 (SEPHS1), consistent
  with the SEPHS1–SEPHS2 interaction. This is a high-throughput AP-MS screen; "BioPlex
  suggests function, localization, and complex membership for thousands of proteins". The
  IPI captures a real, corroborated interaction (SEPHS1) but "protein binding" is
  uninformative as a molecular function; kept as non-core (interaction detail).

## Localization

- Cytoplasm / cytosol. IDA from PMID:28414460 (located_in cytoplasm). Reactome places the
  reaction in cytosol (GO:0005829). UniProt SUBCELLULAR LOCATION: "Cytoplasm
  {ECO:0000269|PubMed:28414460}." [file:human/SEPHS2/SEPHS2-uniprot.txt]

## PTMs / regulation (context, not core function)

- N-terminal Met removed; N-acetylalanine at Ala-2 (PubMed:22814378).
- Phosphoserine at Ser-46 (by similarity) and Ser-97 (PubMed:24275569).
- Ubiquitination: truncated SEPHS2 from failed UGA/Sec decoding is ubiquitinated by
  CRL2(KLHDC3), recognizing the C-terminal Gly (PubMed:26138980) — quality control of a
  selenoprotein, not core catalysis.

## Family / domain

SIMILARITY: "Belongs to the selenophosphate synthase 1 family. Class I subfamily."
PurM-like fold (Pfam AIRS / AIRS_C; CDD SelD; TIGR selD; PANTHER PTHR10256:SF1 "SELENIDE,
WATER DIKINASE 2"). ATP- and Mg2+-binding residues annotated by similarity to P49903;
ATP is "ligand shared between dimeric partners" (consistent with the functional
homodimer). [file:human/SEPHS2/SEPHS2-uniprot.txt]

## Curation summary of existing annotations

Core:
- MF GO:0004756 selenide, water dikinase activity (enables) — ACCEPT (IBA/ISS); the two
  literature-supported instances (Reactome TAS R-HSA-8959510; NAS PMID:8986768) ACCEPT;
  the redundant IEA also ACCEPT.
- BP GO:0016260 L-selenocysteine biosynthetic process (involved_in) — ACCEPT (IMP
  PMID:15534230 is the strongest); IBA/IEA/TAS/NAS instances ACCEPT.
- CC cytoplasm/cytosol — ACCEPT (IDA PMID:28414460 strongest; IBA is_active_in and
  IEA/TAS ACCEPT).
- MF GO:0005524 ATP binding (IEA, InterPro) — ACCEPT; ATP is a genuine substrate/ligand
  (FT BINDING; Rhea reaction), directly part of catalysis.

Non-core:
- MF GO:0005515 protein binding (IPI PMID:33961781, with SEPHS1) — MARK_AS_OVER_ANNOTATED
  (uninformative bare protein binding; per policy never REMOVE an IPI). Real interaction,
  but no specific MF conveyed.

No REMOVE actions: all annotations are biologically consistent with SEPHS2 as the
Sec-containing selenophosphate synthetase.

## GO term id/label checks (EBI OLS4, 2026-07)

- GO:0004756 "selenide, water dikinase activity" — current, not obsolete.
- GO:0016260 "L-selenocysteine biosynthetic process" — current.
- GO:0005737 cytoplasm; GO:0005829 cytosol; GO:0005524 ATP binding — current.
- GO:0016259 "selenocysteine metabolic process" — OBSOLETE (unnecessary grouping term);
  appears only in UniProt DR / Reactome, NOT in the GOA-seeded set, so not used here.
