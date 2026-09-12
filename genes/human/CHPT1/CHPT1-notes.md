# CHPT1 (Cholinephosphotransferase 1) — review notes

UniProt: Q8WUD6 (CHPT1_HUMAN). Gene: CHPT1 (HGNC:17852); synonym CPT1; ORFName MSTP022.
Taxon: Homo sapiens (NCBITaxon:9606). 406 aa, ~45 kDa. EC 2.7.8.2.

## Core biology

CHPT1 is the choline-specific enzyme that catalyzes the **final (second) step of the
CDP-choline (Kennedy) branch of de novo phosphatidylcholine (PC) biosynthesis**. It
transfers a phosphocholine group from CDP-choline onto the free 3-hydroxyl of
1,2-diacyl-sn-glycerol (DAG), producing phosphatidylcholine + CMP (+ H+).

- UniProt FUNCTION: "Catalyzes the final step of de novo phosphatidylcholine (PC)
  synthesis, i.e. the transfer of choline phosphate from CDP-choline to the free
  hydroxyl of a diacylglycerol (DAG), producing a PC. It thereby plays a central role in
  the formation and maintenance of vesicular membranes."
  [file:human/CHPT1/CHPT1-uniprot.txt]
- UniProt CATALYTIC ACTIVITY: Reaction=CDP-choline + a 1,2-diacyl-sn-glycerol = a
  1,2-diacyl-sn-glycero-3-phosphocholine + CMP + H(+); EC=2.7.8.2; RHEA:32939.
  [file:human/CHPT1/CHPT1-uniprot.txt]
- UniProt PATHWAY: "Phospholipid metabolism; phosphatidylcholine biosynthesis;
  phosphatidylcholine from phosphocholine: step 2/2." (UniPathway UPA00753, UER00740)
  [file:human/CHPT1/CHPT1-uniprot.txt]
- Cofactor: Mg(2+) or Mn(2+) [file:human/CHPT1/CHPT1-uniprot.txt].
- Family: CDP-alcohol phosphatidyltransferase class-I family (CDP-OH_P_transf / Pfam
  PF01066; PROSITE PS00379 CDP_ALCOHOL_P_TRANSF); PANTHER PTHR10414:SF32
  CHOLINEPHOSPHOTRANSFERASE 1 [file:human/CHPT1/CHPT1-uniprot.txt].

## Choline-specificity vs the dual-specificity paralog CEPT1

The defining paper [PMID:10893425 Henneberry, Wistow & McMaster 2000 "Cloning, genomic
organization, and characterization of a human cholinephosphotransferase"] cloned hCPT1
and showed by in vitro enzyme assay and by reconstitution in yeast lacking endogenous
CPT/EPT activities that it is a **cholinephosphotransferase-specific enzyme** (it makes
PC but does not use CDP-ethanolamine), contrasting with the previously cloned dual
specificity hCEPT1. [PMID:10893425 abstract: "codes for a cholinephosphotransferase-
specific enzyme ... This contrasted with our previously cloned human
choline/ethanolaminephosphotransferase cDNA that was demonstrated to code for a dual
specificity choline/ethanolaminephosphotransferase."] hCPT1 and hCEPT1 share 60%
identity and differ by a single residue within the CDP-alcohol phosphotransferase
catalytic motif. The two enzymes also differ in diradylglycerol specificity, including
their capacity to synthesize platelet-activating factor (PAF) and PAF precursor.
[PMID:10893425: "revealed differences in diradylglycerol specificities including their
capacity to synthesize platelet-activating factor and platelet-activating factor
precursor."]

Notably, in the same paper, only hCEPT1-derived activity (not hCPT1) complemented the
yeast CPT1 gene in its SEC14 interaction and affected cell growth: [PMID:10893425:
"only hCEPT1-derived activity was able to complement the yeast CPT1 gene in its
interaction with SEC14 and affect cell growth."]. This is relevant to the
NAS `regulation of cell growth` (GO:0001558) annotation attributed to this paper (see
below): the growth effect in that study was a property of the paralog CEPT1, not CPT1,
so a growth-regulation role is not established for CHPT1 by this reference.

## Subcellular localization: Golgi

[PMID:12221122 Henneberry, Wright & McMaster 2002 "The major sites of cellular
phospholipid synthesis..."] localized CPT1 to the **Golgi** by immunofluorescence
(brefeldin A relocalized CPT1 but not CEPT1) plus co-immunofluorescence and subcellular
fractionation: [PMID:12221122: "brefeldin A treatment relocalizes CPT1, but not CEPT1,
implying CPT1 is found in the Golgi"] and [PMID:12221122: "confirmed that CPT1 was found
in the Golgi and CEPT1 was found in both the endoplasmic reticulum and nuclear
membranes."]. UniProt SUBCELLULAR LOCATION: "Golgi apparatus membrane ... Multi-pass
membrane protein." [file:human/CHPT1/CHPT1-uniprot.txt]. Reactome R-HSA-1482973 places
the reaction "at the Golgi membrane."

So the Golgi/Golgi-membrane localization is experimentally supported (GO:0000139 IDA;
GO:0005794 IBA). The `endoplasmic reticulum membrane` (GO:0005789, IBA) is a
phylogenetic call from PANTHER; in this specific paper CEPT1 (not CPT1) was the
ER-localized enzyme, so ER localization for human CHPT1 is not directly demonstrated —
kept as non-core / plausible for the family but not the primary site.

## Topology / active site (UniProt)

10 predicted TM helices (multi-pass); N- and C-termini cytoplasmic. Active site His-133
(proton acceptor) within the DGx2AR...G...D..D catalytic motif; Mg2+-coordinating
residues (Asp/Asn) at 111/114/132/136; CDP-choline binding at 64/119; all by similarity
to zebrafish ortholog Q4KLV1. [file:human/CHPT1/CHPT1-uniprot.txt]

## Interaction

UniProt INTERACTION: Q8WUD6–Q96MV1 (TLCD4), NbExp=3 (IntAct EBI-11337856/EBI-12947623).
The GOA `protein binding` IPI (GO:0005515) is attributed to PMID:32296183 (HuRI human
binary interactome, a systematic Y2H screen; with/from UniProtKB:Q96MV1 = TLCD4). This is
a bare, uninformative MF; the biological significance of a CHPT1–TLCD4 interaction is
unclear. Per policy the IPI is retained (MARK_AS_OVER_ANNOTATED, not removed).

## Platelet-activating factor

GO:0006663 `platelet activating factor biosynthetic process` (IDA, PMID:10893425): the
paper reports differences in the capacity of hCPT1 vs hCEPT1 to synthesize PAF and PAF
precursor, i.e. hCPT1 can contribute PAF/PAF-precursor-synthesizing cholinephospho-
transferase activity in vitro. This is a genuine, experimentally supported but
secondary/minor activity (the enzyme's core role is bulk PC synthesis), so kept as
non-core. [PMID:10893425: "their capacity to synthesize platelet-activating factor and
platelet-activating factor precursor."]

## Tissue expression (UniProt / PMID:12359261)

Highly expressed in testis, colon, small intestine, heart, prostate, spleen; also
kidney, skeletal muscle, pancreas, leukocytes, ovary, thymus; weak in brain, placenta,
lung; overexpressed in cancerous breast epithelial cell lines. Expression varies >100-fold
between tissues (vs the ubiquitously/uniformly expressed paralog CEPT1).
[file:human/CHPT1/CHPT1-uniprot.txt]

## Annotation-review summary

Core function (author synthesis):
- MF: GO:0004142 diacylglycerol cholinephosphotransferase activity (IDA PMID:10893425;
  IBA) — the defining, experimentally demonstrated activity.
- BP: GO:0006657 CDP-choline pathway (the final/2nd step) and GO:0006656
  phosphatidylcholine biosynthetic process (IDA PMID:10893425). GO:0006657 is a subclass
  of GO:0006656 (more specific).
- Location: GO:0000139 Golgi membrane (IDA PMID:12221122).

Actions:
- ACCEPT: GO:0004142 (IDA), GO:0006656 (IDA), GO:0000139 (IDA), GO:0004142 (IBA),
  GO:0005794 Golgi apparatus (IBA), GO:0000139 (TAS Reactome), GO:0006657 CDP-choline
  pathway (NAS), GO:0006629 lipid metabolic process (TAS — general but correct parent
  process, kept), GO:0004142 (IEA GO_REF:0000120 EC/RHEA/ARBA), GO:0006656 (IEA
  GO_REF:0000041 UniPathway).
- KEEP_AS_NON_CORE: GO:0006663 PAF biosynthetic process (IDA, real but minor);
  GO:0005789 ER membrane (IBA — family call, not shown for CHPT1 specifically);
  GO:0019992 diacylglycerol binding (NAS — DAG is the substrate; substrate binding is
  implied by the transferase activity but is not a core standalone MF).
- MARK_AS_OVER_ANNOTATED: GO:0005515 protein binding (IPI, bare/uninformative — never
  removed per policy); GO:0016780 phosphotransferase activity, for other substituted
  phosphate groups (IEA InterPro — a strict parent of the specific GO:0004142);
  GO:0008654 phospholipid biosynthetic process (IEA InterPro — general parent of the
  specific GO:0006656); GO:0016020 membrane (IEA InterPro and NAS — root-level location,
  superseded by Golgi membrane); GO:0043231 intracellular membrane-bounded organelle
  (NAS — very general location); GO:0012505 endomembrane system (IEA ARBA — general
  location).
- REMOVE: GO:0005737 cytoplasm (IEA GO_REF:0000117 ARBA) — CHPT1 is a multi-pass Golgi
  membrane protein; a bulk-cytoplasm localization is a wrong ARBA default (a clearly-wrong
  IEA), superseded by the Golgi-membrane experimental evidence.
- UNDECIDED / KEEP_AS_NON_CORE: GO:0001558 regulation of cell growth (NAS PMID:10893425)
  — the growth effect in that paper was specifically a property of hCEPT1, NOT hCPT1
  (see quote above); this NAS is therefore weakly supported for CHPT1. It is not an
  experimental annotation for this gene, so marked over-annotated.

## Provenance key
- file:human/CHPT1/CHPT1-uniprot.txt — UniProt Q8WUD6 record (authoritative).
- PMID:10893425 — cloning/characterization (abstract only in cache; full_text_available:
  false). Enzyme assay + yeast reconstitution establish choline specificity, PAF activity,
  cofactor, tissue expression.
- PMID:12221122 — Golgi localization (abstract only; full_text_available: false).
- PMID:32296183 — HuRI binary interactome (full text available); source of protein
  binding IPI (partner TLCD4/Q96MV1).
- Reactome:R-HSA-1482973 — "CDP-Cho and DAG are converted to PC by CHPT1 at the Golgi
  membrane".
