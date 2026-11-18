# PMK (At1g31910, Q9C6T1) notes

## Identity

- UniProt Q9C6T1 (PMK_ARATH), name PMK (from Simkin et al. 2011); TAIR has no symbol
  (the record's TAIR line is `AT1G31910; -`), and NCBI Gene 840081 uses the locus code. Folder
  `genes/ARATH/PMK` as assigned.
- 505 aa, GHMP kinase superfamily, the fungal/plant (ERG8-type) phosphomevalonate kinase:
  InterPro IPR016005 (Erg8), NCBIfam TIGR01219, PIRSF017288, PANTHER PTHR31814:SF2. Unrelated in
  fold to animal PMVK. Isoform 2 (Q9C6T1-2) replaces 418-450 and lacks 451-505, i.e. part of the
  GHMP C-terminal domain; nothing is known about it.
- N-terminal Met removed and Ala2 acetylated in a proteome-wide N-terminomics survey (PMID:22223895,
  via UniProt; not used for any annotation).

## Literature search (2026-11-18)

PubMed queries (Europe PMC gave HTTP 503):
1. `(arabidopsis OR thaliana) AND ("phosphomevalonate kinase" OR ... decarboxylase ...)` -> 10 hits;
   none is a dedicated Arabidopsis PMK paper.
2. `arabidopsis AND (PMK OR AtPMK OR At1g31910 ...)` -> no PMK-specific paper.
3. `("phosphomevalonate kinase" OR "mevalonate diphosphate decarboxylase" ...) AND (plant OR rice OR tobacco OR Catharanthus ...)` -> 57 hits, mostly transcriptomics. Primary data on plant PMK: Dellas 2013 (PMID:24327557, Arabidopsis), Simkin 2011 (PMID:21655959, periwinkle + Arabidopsis), Guirimand 2012 (PMID:22459325, periwinkle), Clastre 2011 addendum (PMID:22080790), Henry 2018 (PMID:30127411, tobacco), mango MiPMK (PMID:36724702, not used).
4. `(plant OR arabidopsis) AND (mevalonate OR mevalonic) AND peroxisom*` -> 26 hits; adds Sapir-Mir 2008 (PMID:18988695, peroxisomal IDI1/IDI2; abstract not cached) and the older spinach fractionation work (Kreuz & Kleinig, PMID:6086332).
No Arabidopsis pmk mutant has been described.

## Activity (Arabidopsis protein)

- Dellas et al. 2013 expressed synthetic-gene His-tagged AtPMK in E. coli [PMID:24327557 "IPK, MDD, and PMK genes from A. thaliana, T. adhaerens, B. floridae, and R. castenholzii were ordered as synthetic genes from Genscript"]; [PMID:24327557 "PMKs from B. floridae and A. thaliana catalyze the efficient phosphorylation of MVAP as annotated (3) with similar kinetic constants (Table 3)."]. UniProt records Km 11.8 uM for MVAP and kcat 20.9 s-1 from this paper (table values not in the cached text).
- In vitro reconstitution with AtPMK + AtMDD and downstream enzymes [PMID:24327557 "The in vitro classical MVA pathway reactions for S. solfataricus, A. thaliana, and B. floridae yield 39%, 49%, and 52% conversion of MVAP (3) to 5-EA (7), respectively"]. This is the basis of the IDA GO:0019287 row: the enzyme performs step 2 of IPP formation in a reconstituted pathway.

## Localisation

- Simkin et al. 2011: YFP fusions in C. roseus cells; periwinkle PMK and MVD peroxisomal, MVK cytosolic, "confirmed using the Arabidopsis thaliana MVK, PMK and MVD sequences fused to YFP" [PMID:21655959]. Abstract only; the marker and the Arabidopsis images are not visible to me.
- Clastre et al. 2011 addendum [PMID:22080790 "we provide additional data describing the peroxisomal localization of 5-phosphomevalonate kinase and mevalonate 5-diphosphate decarboxylase"]. The full text (read through WebFetch of PMC3337203, not cached) says PTS2-like motifs lie in the N-terminal region of Arabidopsis and periwinkle PMK and MVD, and quotes the PTS2 consensus (R/K)(L/V/I/Q)X5(H/Q)(L/A/F).
- Guirimand et al. 2012, periwinkle orthologs with cycloheximide to clear cytosolic background from overexpression [PMID:22459325 "allowing us to clearly demonstrate that 5-phosphomevalonate kinase, mevalonate 5-diphosphate decarboxylase and a short isoform of farnesyl diphosphate synthase from Catharanthus roseus are exclusively localized to peroxisomes."]. Ortholog evidence, not Arabidopsis.
- Henry et al. 2018 (tobacco) [PMID:30127411 "the unpredicted peroxisomal localization of bacterial MPD led us to discover that the step catalysed by phosphomevalonate kinase (PMK) imposes a hidden constraint on flux through the classical MVA pathway"]. Abstract only; consistent with a peroxisomal PMK step but not a localisation of Arabidopsis PMK.
- Older fractionation (spinach) found PMK activity "as soluble activities in the cytoplasm" [PMID:6086332]. A soluble fraction from homogenised leaves would also contain released peroxisomal matrix, so this does not discriminate.
- Not detected in the Aryal 2014 leaf cytosolic-fraction proteome (absence uninformative).

### Sequence check (my analysis, `PMK-bioinformatics/RESULTS.md`)

- No PTS1 (C-terminus ...SIHLE). The UniProt "PTS2" motif 57-65 (DVKLTSPQL) does not match the PTS2
  consensus the Clastre addendum itself cites, and there is no consensus PTS2 in residues 1-60.
- Residues 57-65 sit in a plant-specific insertion relative to yeast ERG8.
- So the sequence neither supports nor rules out peroxisomal import; the YFP data are the only
  evidence. The mechanism of import (non-canonical PTS2, piggy-back with a partner) is unknown.
- Correction for the coordinator: the yeast ERG8 review and PTHR31814 family review describe
  Arabidopsis PMK as "PTS1-bearing". It has no PTS1; the proposed signal is a PTS2-like motif.

## GOA rows: decisions

- MF GO:0004631 (IBA, IEA, IDA): ACCEPT.
- BP GO:0019287 (IBA, IEA, IDA): ACCEPT.
- CC GO:0005777 peroxisome (IDA, IEA from UniProt SL-0204, IBA): ACCEPT under ORGANELLES rule 2/3.
  No sub-compartment row (rule 4 needs two agreeing lines; the PTS2-like motif is not canonical, so
  only "soluble enzyme" remains).
- CC GO:0005737 cytoplasm (ISM AtSubP, IEA ARBA): TOO_GENERAL. Cytoplasm includes the peroxisome, so the
  claim is true whatever the final verdict on the peroxisome, but it is imprecise once the
  peroxisome is asserted.
- MF GO:0005524 ATP binding (IEA): KEEP_AS_NON_CORE.

## IBA / PAINT

- PTN001274235 (MF GO:0004631, BP GO:0019287), seeded by AT1G31910 and yeast ERG8: sound.
- PTN000781523 (CC peroxisome), seeded only by AT1G31910, node taxon Eukaryota (taxon:2759). For PMK
  itself the claim rests on its own IDA, which is expected and not circular. The node is placed too
  deep: fungal ERG8 inherits a peroxisome it does not have (the ERG8 and erg8 reviews already REMOVE
  it). A plant-level node would keep the PMK claim and stop the fungal propagation.
- `just paint-losses ARATH PMK`: no IRD/IKR on the lineage.
- PTHR31814's family review calls it a "fungal" PMK family with a single fungal subfamily, but SF2
  contains Arabidopsis PMK, Sulfolobus PMK and Streptomyces PMK too.
