# CEPT1 (human) — gene review notes

UniProt: Q9Y6K0 (CEPT1_HUMAN), 416 aa. HGNC:24289. Gene on chromosome 1.

## Summary of function

CEPT1 is **choline/ethanolamine phosphotransferase 1**, the dual-specificity enzyme
that catalyzes the **final (committed) step of both the CDP-choline and CDP-ethanolamine
(Kennedy) branches** of glycerophospholipid synthesis. It transfers a phosphobase from a
CDP-linked donor to diacylglycerol (DAG):

- CDP-choline + DAG → phosphatidylcholine (PC) + CMP  (EC 2.7.8.2; GO:0004142 diacylglycerol cholinephosphotransferase activity)
- CDP-ethanolamine + DAG → phosphatidylethanolamine (PE) + CMP  (EC 2.7.8.1; GO:0004307 ethanolaminephosphotransferase activity)

It is a polytopic integral membrane enzyme of the CDP-alcohol phosphatidyltransferase
class-I family, resident in the ER and nuclear (inner) membrane, requiring Mg2+ (or, less
efficiently, Mn2+) as cofactor.

## Key provenance (verbatim quotes)

### Dual specificity / final Kennedy step (PMID:10191259, Henneberry & McMaster 1999; abstract-only)
- [PMID:10191259 "Cholinephosphotransferase catalyses the final step in the synthesis of phosphatidylcholine (PtdCho) via the Kennedy pathway by the transfer of phosphocholine from CDP-choline to diacylglycerol."]
- [PMID:10191259 "Ethanolaminephosphotransferase catalyses an analogous reaction with CDP-ethanolamine as the phosphobase donor for the synthesis of phosphatidylethanolamine (PtdEtn)."]
- [PMID:10191259 "In vitro, hCEPT1p displayed broad substrate specificity, utilizing both CDP-choline and CDP-ethanolamine as phosphobase donors to a broad range of diacylglycerols, resulting in the synthesis of both PtdCho and PtdEtn."]
- [PMID:10191259 "In vivo, S. cerevisiae cells (HJ091, cpt1::LEU2 ept1-) expressing hCEPT1 efficiently incorporated both radiolabelled choline and ethanolamine into phospholipids"]
- 416 aa; ubiquitously expressed: [PMID:10191259 "Northern blot analysis revealed one hCEPT1 2.3 kb transcript that was ubiquitous"]
- Note: this abstract states "seven membrane-spanning domains" (the 2023 cryo-EM structure PMID:37137909 revises this to 10 TMs per protomer).

### CEPT1 vs CPT1 (dual vs choline-only) (PMID:10893425, Henneberry et al. 2000; abstract-only)
- CPT1 (a paralog) is choline-specific; CEPT1 is dual-specificity: [PMID:10893425 "This contrasted with our previously cloned human choline/ethanolaminephosphotransferase cDNA that was demonstrated to code for a dual specificity choline/ethanolaminephosphotransferase."]
- This paper is the primary source for the 1-alkenyl/alkyl-acylglycerol choline phosphotransferase (platelet-activating-factor precursor) activities: [PMID:10893425 "their capacity to synthesize platelet-activating factor and platelet-activating factor precursor."]

### Subcellular localization — ER + nuclear membrane, NOT Golgi (PMID:12221122, Henneberry et al. 2002; abstract-only)
- CEPT1 makes both PC and PE; CPT1 is Golgi and choline-only: [PMID:12221122 "CEPT1 transfers a phosphobase from either CDP-choline or CDP-ethanolamine to diacylglycerol to synthesize both phosphatidylcholine and phosphatidylethanolamine, whereas CPT1 synthesizes phosphatidylcholine exclusively."]
- Localization: [PMID:12221122 "brefeldin A treatment relocalizes CPT1, but not CEPT1, implying CPT1 is found in the Golgi."]
- [PMID:12221122 "confirmed that CPT1 was found in the Golgi and CEPT1 was found in both the endoplasmic reticulum and nuclear membranes."]
- Residue Gly156 governs dual specificity; residues 214–228 helix positions the catalytic site: [PMID:12221122 "This pinpointed glycine 156 within the catalytic motif as being responsible for the dual CDP-alcohol specificity of CEPT1"]
- UniProt confirms location: [file:human/CEPT1/CEPT1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"] and "Nucleus membrane ... Multi-pass membrane protein".

**Interpretation for the Golgi IBA annotation (GO:0005794):** the definitive human localization
study (PMID:12221122) explicitly shows CEPT1 is NOT in the Golgi (brefeldin A does not
relocalize it) and localizes it to ER + nuclear membrane. The Golgi IBA is a
phylogenetic/orthology inference driven partly by fly (FBgn0031948) and mouse orthologs; it
is retained as non-core, flagged as contradicted for human by direct evidence.

### Cryo-EM structure & mechanism (PMID:37137909, Wang et al. 2023; FULL TEXT available)
- Final step of PC/PE synthesis, dual specificity: [PMID:37137909 "Choline/ethanolamine phosphotransferase 1 (CEPT1) catalyzes the last step of the biosynthesis of PC and PE in the Kennedy pathway by transferring the substituted phosphate group from CDP-choline/ethanolamine to diacylglycerol."]
- Dimer, 10 TMs per protomer: [PMID:37137909 "CEPT1 is a dimer with 10 transmembrane segments (TMs) in each protomer."]
- Cofactor Mg2+ (Mn2+ ~50%): [PMID:37137909 "the enzymatic activity was nearly abolished when other divalent cations were added instead of Mg2+, except Mn2+; with the addition of Mn2+, the enzyme maintained approximately 50% of the activity"]
- CDP-choline preferred over CDP-ethanolamine (~2x): [PMID:37137909 "CMP release was approximately doubled when CDP-choline was used as the substrate compared with CDP-ethanolamine"]
- Catalytic aspartate D154 essential: [PMID:37137909 "Substitution of one conserved aspartate in the CDP-binding motif with alanine (D154A) completely abolished the enzymatic activity."]
- DAG required (no CMP release without it): [PMID:37137909 "No CMP release was detected in the absence of DAG, confirming that CMP was not produced by the hydrolysis of CDP-choline"]
- Note: the paper's title/abstract foreground PC (CDP-choline) because CDP-choline was used in all assays; both PC and PE production are established here and by PMID:10191259. Hence GO:0004307 (ethanolaminephosphotransferase) IDA is separately from PMID:10191259.

### Cofactor (UniProt)
- [file:human/CEPT1/CEPT1-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420;"] and Mn(2+) alternative — supports metal ion binding (GO:0046872, present in UniProt DR but not in GOA TSV; not among the 31 GOA annotations).

## Interactions (PMID:32296183 — HuRI reference interactome)
- GOA seeds two IPI "protein binding" (GO:0005515) annotations from the HuRI binary
  interactome (Luck et al. 2020), with SPG21 (Q9NZD8) and TMEM14B (Q9NUH8) as partners.
  UniProt INTERACTION block confirms both (NbExp=3, IntAct EBI-1237183).
- The HuRI paper is a genome-scale Y2H map; it establishes physical binary interactions but
  assigns no specific molecular function. Per policy, bare "protein binding" IPI is kept but
  MARK_AS_OVER_ANNOTATED (uninformative MF); the interactions themselves are not disputed.
  TMEM14B and SPG21 are both membrane-associated proteins, consistent with CEPT1 being a
  polytopic ER membrane protein, but no functional consequence is established.

## Core functions (author-supplied, validated against go.db)
1. GO:0004142 diacylglycerol cholinephosphotransferase activity (EC 2.7.8.2) — PC synthesis. IDA PMID:10191259, PMID:37137909.
2. GO:0004307 ethanolaminephosphotransferase activity (EC 2.7.8.1) — PE synthesis. IDA PMID:10191259.
   Both are descendants of GO:0016780 (verified) and of molecular_function GO:0003674.
Associated core BP: GO:0006656 (PC biosynthetic process) and GO:0006646 (PE biosynthetic process);
location GO:0005789 (ER membrane) [+ nuclear membrane GO:0031965].

## Annotation action rationale (high level)
- ACCEPT the experimental (IDA/EXP) MF and BP annotations for PC/PE synthesis and the ER-membrane
  localization (IDA PMID:12221122) — these are the core, well-supported functions.
- IBA MF/BP (GO:0004142, GO:0004307, GO:0006646) ACCEPT (consistent with experimental).
- IBA Golgi (GO:0005794): KEEP_AS_NON_CORE — contradicted for human by PMID:12221122 (ER+nuclear, not Golgi).
- IEA duplicates of the specific MF (GO:0004142/GO:0004307/GO:0047359 from EC/RHEA) ACCEPT (redundant but correct).
- IEA general terms: GO:0008654 phospholipid biosynthetic process, GO:0016780 phosphotransferase activity
  (parents of the specific terms) — MARK_AS_OVER_ANNOTATED / MODIFY toward the specific children.
- IEA/general cellular locations GO:0005737 cytoplasm, GO:0012505 endomembrane system, GO:0016020 membrane —
  MARK_AS_OVER_ANNOTATED (too general / cytoplasm imprecise for an integral membrane enzyme).
- IEA nuclear membrane GO:0031965 (UniProt-SubCell) ACCEPT — supported by PMID:12221122.
- TAS Reactome ER-membrane and PMID:10191259 MF/BP annotations ACCEPT.
- TAS GO:0006629 lipid metabolic process (ProtInc) — MARK_AS_OVER_ANNOTATED (too general vs specific PC/PE BPs).
- TAS GO:0016020 membrane (ProtInc) — MARK_AS_OVER_ANNOTATED (too general).
- 1-alkenyl-2-acylglycerol choline phosphotransferase (GO:0047359, EXP PMID:10191259 / IEA): KEEP_AS_NON_CORE —
  a real but minor side activity (plasmenylcholine/PAF-precursor synthesis), primarily characterized in PMID:10893425.
- protein binding IPI (GO:0005515) x2: MARK_AS_OVER_ANNOTATED (uninformative MF).
