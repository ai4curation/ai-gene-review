# FNTB (Protein farnesyltransferase subunit beta) — review notes

UniProt: P49356 (FNTB_HUMAN), 437 aa, human (NCBITaxon:9606). EC 2.5.1.58.
Gene on chromosome 14. HGNC:3785.

## Core biology (from UniProt + primary literature)

FNTB is the **beta (catalytic) subunit** of **protein farnesyltransferase (FTase)**, a
zinc-dependent heterodimeric CaaX prenyltransferase. FTase is a heterodimer of the alpha
subunit **FNTA** (shared with GGTase-I) and the beta subunit **FNTB**
[file:human/FNTB/FNTB-uniprot.txt "SUBUNIT: Heterodimer of FNTA and FNTB"].

Function: "Essential subunit of the farnesyltransferase complex. Catalyzes the transfer of
a farnesyl moiety from farnesyl diphosphate to a cysteine at the fourth position from the
C-terminus of several proteins having the C-terminal sequence Cys-aliphatic-aliphatic-X"
[file:human/FNTB/FNTB-uniprot.txt CC FUNCTION].

Catalytic reaction (Rhea RHEA:13345, EC 2.5.1.58):
"L-cysteinyl-[protein] + (2E,6E)-farnesyl diphosphate = S-(2E,6E)-farnesyl-L-cysteinyl-[protein] + diphosphate"
[file:human/FNTB/FNTB-uniprot.txt CC CATALYTIC ACTIVITY].

Cofactor: "Binds 1 zinc ion per subunit" — catalytic Zn2+ coordinated by the beta subunit
(residues His297, Asp299, His362 per FT BINDING lines)
[file:human/FNTB/FNTB-uniprot.txt CC COFACTOR / FT BINDING 297,299,362].

FPP substrate binding is mediated by the beta subunit: neither FNTA nor FNTB alone binds
isoprenoid, but "a radiolabeled farnesyl diphosphate analog could be specifically
photo-cross-linked to the beta subunit of FPTase holoenzyme"
[PMID:8494894 "photo-cross-linked to the beta subunit of FPTase holoenzyme"].

### Substrate proteins / biological role
FTase farnesylates >60 CaaX proteins involved in signal transduction, notably H/N/K-Ras
and other Ras-superfamily GTPases, nuclear lamins, and centromeric proteins:
"FTase catalyzes the transfer of a 15-carbon isoprenoid lipid moiety to the C terminus of
more than 60 signal transduction proteins in the eukaryotic cell, including members of the
Rho and Ras superfamily of G proteins" [PMID:19246009 "more than 60 signal transduction proteins in the eukaryotic cell"].
Substrate set includes "members of the Ras superfamily, heterotrimeric G-proteins,
centromeric proteins, and a number of proteins involved in nuclear integrity"
[PMID:16893176 "members of the Ras superfamily, heterotrimeric G-proteins, centromeric proteins, and a number of proteins involved in nuclear integrity"].
This is why FTase is a major anticancer drug target (FTIs: Lonafarnib/Tipifarnib) and a
Hutchinson-Gilford progeria therapeutic target — the UniProt DrugBank cross-references list
Lonafarnib, Tipifarnib, BMS-214662, etc. [file:human/FNTB/FNTB-uniprot.txt DR DrugBank].

### Isoprenoid selectivity (FPP vs GGPP)
The beta subunit selects FPP over GGPP. Trp102β provides steric hindrance; W102T removes it:
"W->T: Removes the steric hindrance that normally precludes geranylgeranyl diphosphate
binding. Reduces farnesyltransferase activity and confers geranylgeranyltransferase activity"
[file:human/FNTB/FNTB-uniprot.txt FT MUTAGEN 102]. This is the subject of PMID:16893176
("Conversion of protein farnesyltransferase to a geranylgeranyltransferase"; specificity
"dependent upon two enzyme residues in the beta subunits ... W102beta and Y365beta in FTase")
[PMID:16893176 "W102beta and Y365beta in FTase"].

## Structural / catalytic references (X-ray, in complex with Zn, FNTA, FPP, inhibitors)
- PMID:11687658 — first human FTase crystal structure, basis for CaaX-mimetic inhibition; in
  complex with zinc, FNTA, FPP, inhibitor L-739,750. IntAct source for FNTA binding.
- PMID:12036349, PMID:12825937, PMID:19246009 — inhibitor co-crystal structures; UniProt cites
  these as EXP support for CATALYTIC ACTIVITY and FUNCTION. All confirm the heterodimer,
  catalytic Zn2+ in the beta subunit, and FPP binding site.
- PMID:15451670 — CaaX prenyltransferase substrate selectivity rules from co-crystal structures.
- PMID:16893176 — the FPP/GGPP selectivity determinant paper (see above); UniProt IDA source
  for GO:0004660, GO:0008270, GO:0018343, GO:0005965.

## HDAC6 / microtubule (moonlighting, non-catalytic)
PMID:19228685 (abstract only): FTase and HDAC6 co-exist "in a protein complex together with
microtubules in vivo and in vitro"; "FTase binds microtubules directly via its alpha subunit,
and this association requires the C terminus of tubulin"; "removal of FTase from microtubules
abrogated HDAC6 activity, as did a stable knockdown of the alpha subunit of FTase"
[PMID:19228685 abstract]. BHF-UCL made three FNTB annotations from this paper:
GO:0010698 acetyltransferase activator activity (IDA), GO:0060632 regulation of
microtubule-based movement (IDA), GO:0005875 microtubule associated complex (IDA),
GO:0019899 enzyme binding to HDAC6/UniProtKB:Q9UBN7 (IPI), plus contributes_to GO:0004660.
Note the abstract explicitly attributes the microtubule/tubulin binding to the **alpha
subunit (FNTA)**, and HDAC6 lacks a farnesylation motif — so these are indirect/complex-level
effects. These are legitimate experimental annotations (do not REMOVE) but represent a
secondary, non-core (moonlighting) activity of the FTase complex; kept as non-core.

## Protein-binding (IPI) partners
Most GO:0005515 IPI annotations use with/from UniProtKB:P49354 = FNTA (the obligate partner),
from the structural/IntAct papers (11687658, 12036349, 12825937, 15170324, 15248757, 15451670,
24981860, 31209342, 33961781). This is the biologically meaningful FTase heterodimer
interaction. High-throughput interactome screens (32296183 HuRI, 32814053 neurodegeneration
interactome, 33961781 BioPlex) add many partners (AGXT, APOL6, ATPAF2, CCDC24, DMWD, HOXC8,
KRBA1, SMG9, SPRED1, TLX3 — matching the UniProt INTERACTION block). Per curation policy, bare
"protein binding" (GO:0005515) IPI is not informative as a core MF; marked over-annotated (not
removed). The FNTA interaction is better captured by the FTase complex CC + farnesyltransferase MF.

PMID:31209342 (GGTase3 paper) uses FNTA (P49354) as the with/from — the paper is about
PTAR1/RabGGTB (GGTase3), and FNTB appears in comparison/IntAct context, not as a functional
finding about FNTB catalysis. PMID:24981860 is a chromatin-demethylase interactome (RCCD1/KDM8),
FNTB captured as an AP-MS interactor; again FNTA is the recorded partner. Neither adds a new
core FNTB function.

## Action summary rationale
- Catalytic core (protein farnesyltransferase activity, zinc ion binding, protein farnesylation,
  FTase complex): ACCEPT the experimental IDA/EXP annotations.
- IBA (GO:0004660 contributes_to, GO:0005965 part_of): consistent with experimental data; ACCEPT.
  Note contributes_to on GO:0004660 is appropriate — the activity is a property of the FNTA:FNTB
  heterodimer, and FNTB is the catalytic subunit contributing that activity.
- IEA to less-specific ancestors (catalytic activity GO:0003824, prenyltransferase activity
  GO:0004659, protein prenyltransferase activity GO:0008318): correct but subsumed by the specific
  GO:0004660 → MODIFY / MARK as less informative (kept; replaced by the specific term).
- IEA GO:0004660 (GO_REF:0000120, from Q02293 rat ortholog / RHEA / EC): correct, redundant with
  the experimental term → ACCEPT (redundant but correct).
- cytosol (TAS Reactome): ACCEPT — FTase is a soluble cytosolic enzyme.
- Ensembl-projected BP (positive regulation of cell population proliferation GO:0008284, positive
  regulation of cell cycle GO:0045787) and MF (peptide binding GO:0042277) from rat ortholog
  Q02293 (GO_REF:0000107/IEA): these are over-reaching electronic projections. Proliferation/
  cell-cycle effects are downstream consequences of Ras farnesylation, not FNTB's molecular
  function; MARK_AS_OVER_ANNOTATED. peptide binding is a generic descriptor of CaaX-substrate
  recognition — subsumed by farnesyltransferase activity; MARK_AS_OVER_ANNOTATED.

## Core functions (final)
- MF: GO:0004660 protein farnesyltransferase activity (catalytic subunit; FPP + CaaX cysteine)
- MF: GO:0008270 zinc ion binding (catalytic Zn2+ coordinated by beta subunit)
- BP: GO:0018343 protein farnesylation
- CC/in_complex: GO:0005965 protein farnesyltransferase complex; located_in cytosol GO:0005829
