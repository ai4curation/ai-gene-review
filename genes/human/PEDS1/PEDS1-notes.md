# PEDS1 (Plasmanylethanolamine desaturase 1; formerly TMEM189 / KUA) — review notes

UniProt: A5PLL7 (PEDS1_HUMAN), HGNC:16735, chromosome 20, 270 aa.
EC 1.14.19.77. Gene synonyms: TMEM189, PEDS, KUA.

## Summary of function

PEDS1 is the long-sought **plasmanylethanolamine desaturase (PEDS)**, the enzyme that
catalyzes the **final, plasmalogen-defining step** of ether-phospholipid (plasmalogen)
biosynthesis: it introduces the characteristic **1-O-alk-1'-enyl (vinyl ether) double
bond** at the sn-1 position of plasmanylethanolamine to yield plasmenylethanolamine
(ethanolamine plasmalogen), using O2 and reduced cytochrome b5 as the electron donor.

- The reaction and EC are authoritative in UniProt: "EC=1.14.19.77" and the RHEA reaction
  "a 1-(1,2-saturated alkyl)-2-acyl-sn-glycero-3-phosphoethanolamine + 2 Fe(II)-[cytochrome b5]
  + O2 + 2 H(+) = a 1-O-(1Z-alkenyl)-2-acyl-sn-glycero-3-phosphoethanolamine + 2 Fe(III)-[cytochrome b5]
  + 2 H2O" [file:human/PEDS1/PEDS1-uniprot.txt].
- FUNCTION (UniProt): "Plasmanylethanolamine desaturase involved in plasmalogen biogenesis
  in the endoplasmic reticulum membrane" [file:human/PEDS1/PEDS1-uniprot.txt].

## Gene identity (PEDS1 = TMEM189)

Two independent 2019/2020 papers identified this orphan gene as PEDS:

- [PMID:31604315 "A bacterial light response reveals an orphan desaturase for human plasmalogen synthesis"]:
  "We discovered the plasmanylethanolamine desaturase activity that is essential for vinyl ether bond
  formation in a bacterial enzyme, CarF, which is a homolog of the human enzyme TMEM189." Human
  TMEM189 and other animal homologs functionally replaced the Myxococcus CarF, and
  "knockout of TMEM189 in a human cell line eliminated plasmalogens." (Science; abstract-only in cache,
  `full_text_available: false`.)
- [PMID:32209662 "The TMEM189 gene encodes plasmanylethanolamine desaturase which introduces the
  characteristic vinyl ether double bond into plasmalogens"]: "the transmembrane protein 189 gene
  (TMEM189 ...) encodes PEDS activity"; PEDS "introduces the alk-1′-enyl ether double bond (vinyl ether
  bond) into plasmanylethanolamines, yielding plasmenylethanolamines"; TMEM189 knockout HAP1 cells lose
  PEDS activity and plasmalogens and accumulate the plasmanylethanolamine substrates; Tmem189-KO mice
  also lack PEDS activity and plasmalogens. (PNAS; `full_text_available: true`.) Note this paper cites the
  historic EC as 1.14.99.19; the current UniProt/Rhea EC is 1.14.19.77.

## Enzyme family / mechanism

- Belongs to the **fatty acid desaturase CarF family** (UniProt SIMILARITY); Pfam PF10520
  (Lipid_desat), InterPro IPR052601 (Plasmalogen_desaturase).
- Non-heme **di-iron** desaturase type: [PMID:32209662] "the enzyme has properties similar to
  non–heme-containing di-iron desaturases", characterized by a motif of eight conserved histidines.
- Two histidine boxes (His box-1 186..190; His box-2 213..217) plus additional His residues are
  essential for catalysis; UniProt DOMAIN: "Histidine box-1 and -2 together with other histidine
  residues are essential for catalytic activity" (mutagenesis H95/H120/H121/H130/H186/H190/H214/H217/H218
  → loss of activity) [file:human/PEDS1/PEDS1-uniprot.txt; PMID:31604315]. In PNAS the equivalent murine
  eight histidines are "absolutely essential for PEDS activity" [PMID:32209662].

## Subcellular location

- Endoplasmic reticulum membrane, multi-pass. UniProt SUBCELLULAR LOCATION cites PMID:11076860 and
  PMID:31604315. A TMEM189-GFP fusion "showed localization in the endoplasmic reticulum by an overlay
  of the green fluorescence signal with ER Tracker Red" [PMID:32209662]. PEDS enzymatic activity is
  "membrane-bound and likely originating from the endoplasmic reticulum" (microsomal) [PMID:32209662].
- HPA IDA (GO_REF:0000052) localizes to endoplasmic reticulum [file:human/PEDS1/PEDS1-goa.tsv].

## Kua / KUA-UEV1 (PEDS1-UBE2V1) — historical

- [PMID:11076860 "Fusion of the human gene for the polyubiquitination coeffector UEV1 with Kua"]:
  named the "Kua" gene (=PEDS1/TMEM189), a "novel class of conserved proteins with juxtamembrane
  histidine-rich motifs"; PEDS1 and UBE2V1 are adjacent genes that can form a fused Kua-UEV protein.
  The abstract reports "both Kua and Kua-UEV localize to cytoplasmic structures" (not resolved to ER
  in the abstract; ER-membrane EXP annotation from this paper rests on full text not in cache). This
  is the origin of the EXP ER-membrane annotation and of the PEDS1-UBE2V1 fusion note in UniProt.

## Interactions

- IntAct/IPI protein binding (GO:0005515) to LAMP2 (P13473-2) and SH3GLB1 (Q9Y371), from
  [PMID:32814053], a large-scale neurodegenerative-disease **yeast two-hybrid** interactome
  ("systematic yeast two-hybrid interaction screening"). No functional interpretation for PEDS1;
  these are high-throughput binary interactions, uninformative about molecular function.

## Curation decisions (high level)

- Core MF: **GO:0050207 plasmanylethanolamine desaturase activity** (OLS-verified id; oxidoreductase
  branch; matches GOA + UniProt DR). Supported by IDA (PMID:31604315), IMP (PMID:32209662).
- Core BP: **GO:0008611 ether lipid biosynthetic process** (OLS-verified). Supported by IDA/IMP.
- Core CC: **GO:0005789 endoplasmic reticulum membrane** (IDA PMID:31604315; EXP PMID:11076860; IBA).
- ACCEPT the experimental MF/BP/CC and the well-supported IBA/IEA of the gene's own core functions.
- GO:0006631 fatty acid metabolic process (IEA UniPathway) — over-general parent of the real BP;
  MARK_AS_OVER_ANNOTATED (keep, but not core; PEDS1 does not act on free fatty acids).
- GO:0005515 protein binding (IPI, PMID:32814053) — bare "protein binding", HT-Y2H; MARK_AS_OVER_ANNOTATED.
- GO:0005783 endoplasmic reticulum (IDA HPA) — correct but less specific than ER membrane; KEEP_AS_NON_CORE.
