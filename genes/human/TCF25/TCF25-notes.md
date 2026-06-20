# TCF25 (Ribosome quality control complex subunit TCF25; Nulp1/hnulp1) notes

UniProt: Q9BQ70 (TCF25_HUMAN). Despite the legacy name "Transcription Factor 25", TCF25 is
the human Rqc1-like subunit of the RQC complex. Also called Nulp1 (nuclear localized protein 1)
/ hnulp1. TCF25 family.

## Core function
Component of the RQC complex (LTN1 + TCF25 + NEMF on the 60S subunit). TCF25 is required to
promote formation of K48-linked polyubiquitin chains during LTN1-mediated ubiquitination of
stalled nascent chains.

- UniProt FUNCTION: "Component of the ribosome quality control complex (RQC) ... In the RQC
  complex, required to promote formation of 'Lys-48'-linked polyubiquitin chains during
  ubiquitination of incompletely synthesized proteins by LTN1 (PubMed:30244831)."
- [PMID:30244831 "We also found that TCF25, a poorly characterized RQC component, ensures preferential formation of the K48-ubiquitin linkage."]
- UniProt SUBUNIT: "Component of the ribosome quality control complex (RQC), composed of the
  E3 ubiquitin ligase LTN1, TCF25 and NEMF associated with the 60S ribosomal subunit
  (PubMed:30244831)."

## RQC context (PMID:30244831)
"60S RNCs associate with NEMF, which recruits the E3 ubiquitin ligase Listerin that
ubiquitinates NCs ... TCF25 ... ensures preferential formation of the K48-ubiquitin linkage."
GO terms (IDA, PMID:30244831): GO:0061945 regulation of protein K48-linked ubiquitination;
GO:0072344 rescue of stalled cytosolic ribosome; GO:1990112 RQC complex.

## Legacy nuclear / transcription / apoptosis roles
- Named "hnulp1" / "Nulp1" - reported as a bHLH protein with a transcriptional repressive
  domain (PMID:16574069) and as a nuclear protein that increases cell death and binds XIAP
  (PMID:18068114). UniProt: "Mainly nuclear."
- UniProt FUNCTION (By similarity): "May negatively regulate the calcineurin-NFAT signaling
  cascade by suppressing the activity of transcription factor NFATC4" and "May play a role in
  cell death control" - both By similarity, not human-experimentally established here.
- Nucleus localization (EXP PMID:16574069, PMID:18068114; IEA) - well-supported localization
  but the functional core relevant to GO MF/BP is the RQC role. Keep nucleus as NON_CORE given
  the predominant characterized molecular role is cytoplasmic RQC; however nuclear localization
  is experimentally real (mainly nuclear per UniProt).

## protein binding (IPI) annotations
All 14 IPI GO:0005515 annotations come from high-throughput interactome maps (Rual 2005, Venkatesan
2009, Yu 2011, Rolland 2014/HI-II-14, Luck 2020/HuRI, Huttlin BioPlex, OpenCell, neurodegeneration
interactome, LRRK1/2 interactome). WITH partners include SAT1 (P21673), MAGEA11 (P43364),
GPRASP2 (Q96D09), LRRK2 (Q5S007), DERL1 (Q9BUN8), GPX7, KASH5, KIF1B, WFS1, APPBP2. None of these
inform the core RQC function; bare "protein binding" is uninformative -> KEEP_AS_NON_CORE.

## Localization caveat
UniProt: Nucleus (mainly nuclear) AND Cytoplasm, cytosol. The RQC role is cytosolic/60S-associated.
Cytosol IEA/TAS -> ACCEPT (site of RQC action). Nucleus -> KEEP_AS_NON_CORE.

## Actions summary
- Core: GO:1990112 RQC complex (part_of, IDA); GO:0061945 regulation of K48 ubiquitination (IDA);
  GO:0072344 rescue of stalled ribosome (IDA); GO:1990116 RQC catabolism (NAS).
- Core MF: there is no specific MF annotation; TCF25's molecular role is as a RQC scaffold/cofactor
  promoting K48 chains. Best captured by the BP GO:0061945 + complex membership. Use core_functions
  with molecular_function = the most informative available term.
- protein binding IPI x14 -> KEEP_AS_NON_CORE.
- nucleus -> KEEP_AS_NON_CORE; cytosol -> ACCEPT.
