# CERS2 (ceramide synthase 2, Q96G23) — review notes

## Summary of function
CERS2 (ceramide synthase 2; formerly LASS2/LAG1 longevity assurance homolog 2;
also TMSG1) catalyzes the N-acylation step of ceramide biosynthesis: transfer of
a fatty acyl chain from acyl-CoA onto the amino group of a sphingoid base
(sphinganine in the de novo pathway; sphingosine in the salvage pathway) to form
(dihydro)ceramide. It is a multi-pass ER membrane protein of the sphingosine
N-acyltransferase (Lag1/Lac1, TLC-domain) family. Its defining biochemical
feature is high selectivity for **very-long-chain (VLC) acyl-CoAs (C22-C26)**,
producing VLC-ceramides. It is the most highly and broadly expressed of the six
mammalian ceramide synthases.

## Key provenance (verbatim-quotable)
- Broadest/highest expression + VLC specificity: [PMID:18165233 "CerS2 mRNA is
  found at the highest level of all CerS and has the broadest tissue distribution"];
  [PMID:18165233 "rather utilizing longer acyl-chain CoAs (C20-C26) for ceramide synthesis"].
- N-acylation mechanism (family-level): [PMID:17977534 "ceramide is synthesized by
  N-acylation of a sphingoid long-chain base by a family of ceramide synthases (CerS),
  each of which displays a high specificity towards acyl CoAs of different chain lengths"].
- Essential for C24 sphingolipids / links to ELOVL1: [PMID:20937905 "the ceramide
  synthase CERS2, an enzyme essential for C24 sphingolipid synthesis"].
- Acyl-chain specificity resides in an 11-residue loop in the TLC domain:
  [PMID:29632068 "CerS2 (which generates C22-C24-ceramides)"].
- S1P inhibition via S1P-receptor-like motif; mutagenesis R230/R325:
  [PMID:18165233 "the activity of CerS2 can be regulated by another bioactive
  sphingolipid, sphingosine 1-phosphate (S1P)"].
- Cloning as LASS2, high liver/kidney expression, interacts with membrane
  receptors/transporters: [PMID:11543633 "The LASS2 transcript is highly expressed
  in liver and kidney"]; [PMID:11543633 "the LASS2 protein interacts with several
  membrane-associated receptors or transporters"].
- ER membrane localization + multi-pass: UniProt SUBCELLULAR LOCATION
  "Endoplasmic reticulum membrane {ECO:0000269|PubMed:18165233}; Multi-pass
  membrane protein" (file:human/CERS2/CERS2-uniprot.txt).

## Domains / topology (UniProt)
- TLC domain (TRAM_LAG1_CLN8; Pfam PF03798) 131..332 — catalytic.
- Homeobox-like region 67..128: UniProt explicitly states the predicted Homeobox
  domain "lacks important residues for DNA-binding" and, given ER-membrane
  localization, "does not constitute a canonical homeobox domain." => The InterPro
  IEA GO:0003677 "DNA binding" is a spurious homeodomain-signature transfer; REMOVE.
- 6 TRANSMEM helices; N-term lumenal, C-term (325-380) cytoplasmic (site of
  regulatory phosphorylation S341/T346/S348/S349 by CK2).

## Annotation decisions (rationale)
- Core MF = **GO:0050291 sphingosine N-acyltransferase activity** (exact GOA term;
  multiple IDA/EXP/IBA/TAS). This is the ceramide-synthase activity term GO uses.
- Core BP = **GO:0046513 ceramide biosynthetic process** (IDA/IBA). Also
  GO:0030148 sphingolipid biosynthetic process (TAS, more general) KEEP_AS_NON_CORE.
- Core CC = **GO:0005789 endoplasmic reticulum membrane** (EXP PMID:18165233).
  GO:0005783 ER (IDA/IBA) accept; GO:0098554 cytoplasmic side of ER membrane and
  GO:0031965 nuclear membrane are finer/secondary CC.
- **GO:0003677 DNA binding (IEA, InterPro homeodomain)**: REMOVE — degenerate
  homeobox-like signature, no DNA binding (UniProt explicit).
- **GO:0016020 membrane** (IEA/HDA): over-general vs ER membrane; MARK_AS_OVER_ANNOTATED.
- **protein binding (GO:0005515) IPIs**: bare, uninformative; per policy
  MARK_AS_OVER_ANNOTATED (do not REMOVE). PMID:11543633 and PMID:20937905 partners
  are real functional interactors (ELOVL1/HSD17B12/TECR elongase complex; membrane
  receptors); HT interactome hits (32296183, 21988832, 32911434, 33961781, 20195357)
  are lower-value.
- **Schwann cell / axon-regeneration terms** (GO:0010626, GO:0048681, GO:1900148,
  and the ISS/IEA from rat Q3T1K1): peripheral, orthology-transferred developmental
  roles, not core; KEEP_AS_NON_CORE.
- **regulation of lipid metabolic process (GO:0019216)**: broad ISS/IEA;
  KEEP_AS_NON_CORE.
- **GO:0006688 glycosphingolipid biosynthetic process (EXP, PMID:34080016)**: the
  cited paper is a general GlcCer/GalCer review not mentioning CERS2; CERS2 supplies
  the VLC-ceramide backbone but does not catalyze glycosylation => MARK_AS_OVER_ANNOTATED.
- **PMID:36170811 (Spears et al.)** cited for GO:0046513 (IDA) and GO:0098554 (IDA):
  the cached full text is entirely about SPT/KDSR (first two pathway enzymes) and
  never mentions CERS2 — cannot verify CERS2-specific evidence => UNDECIDED (do not
  REMOVE experimental annotation whose full text I cannot map to CERS2).
</content>
</invoke>
