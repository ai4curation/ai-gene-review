# UPP2 (uridine phosphorylase 2, human, O95045) — review notes

## Identity and core biology

- UPP2 encodes **uridine phosphorylase 2 (UPase-2 / UrdPase 2)**, EC 2.4.2.3, a 317-aa cytosolic
  enzyme of the PNP/UDP phosphorylase family [file:human/UPP2/UPP2-uniprot.txt "RecName: Full=Uridine phosphorylase 2"; "Belongs to the PNP/UDP phosphorylase family"].
- It catalyzes the **reversible phosphorolytic cleavage of uridine to uracil and ribose-1-phosphate**,
  feeding pyrimidine salvage and catabolism [file:human/UPP2/UPP2-uniprot.txt "Catalyzes the reversible phosphorylytic cleavage of uridine"].
  Reactions (UniProt/Rhea): uridine + phosphate = alpha-D-ribose 1-phosphate + uracil (RHEA:24388);
  2'-deoxyuridine + phosphate = 2-deoxy-alpha-D-ribose 1-phosphate + uracil (RHEA:22824)
  [file:human/UPP2/UPP2-uniprot.txt "Reaction=uridine + phosphate = alpha-D-ribose 1-phosphate + uracil"].
- Pathway (UniProt): "Pyrimidine metabolism; UMP biosynthesis via salvage pathway; uracil from uridine
  (phosphorylase route): step 1/1" [file:human/UPP2/UPP2-uniprot.txt "UMP biosynthesis via salvage pathway"].
- **Broad substrate specificity**: accepts uridine, deoxyuridine, thymidine, and the analogs
  5-fluorouridine and 5-fluoro-2'-deoxyuridine [PMID:12849978 "showed broad substrate specificity and accepted uridine, deoxyuridine, and thymidine as well as the two pyrimidine nucleoside analogs 5-fluorouridine and 5-fluoro-2(')-deoxyuridine"].
  Kinetics (UniProt): KM 76 uM uridine, 300 uM deoxyuridine, 73 uM thymidine, 24 uM 5-fluorouridine
  [file:human/UPP2/UPP2-uniprot.txt "KM=76 uM for uridine"].

## Discovery and paralog relationship

- UPP2 was cloned by Johansson 2003 as a **novel human uridine phosphorylase ~60% identical to UPP1**
  [PMID:12849978 "a novel 317 amino acid human uridine phosphorylase approximately 60% identical to the previously identified human uridine phosphorylase was cloned"].
- Humans (and most vertebrates) have two paralogs, UPP1 (ubiquitous, better studied) and UPP2
  [PMID:21855639 "most vertebrates possessing two versions of the phosphorylase, UPP1 (Watanabe and Uchida, 1995) and UPP2 (Johansson, 2003)"], ~62% identity
  [PMID:21855639 "the two human homologues retain ~62% sequence identity"].
- **Tissue-restricted expression**: human UPP2 mRNA is predominantly in kidney
  [PMID:12849978 "the 2.2-kb mRNA was predominantly expressed in kidney"; file:human/UPP2/UPP2-uniprot.txt "Predominantly expressed in kidney"]; UniProt HPA notes "Group enriched (kidney, liver)".
  Mouse UPP2 is predominantly liver [PMID:12849978 "The mouse UPase-2 cDNA was also identified and shown to be predominantly expressed in liver"].
- Note: "Not as much is known about the specific role of human UPP2 (hUPP2)"
  [PMID:21855639 "Not as much is known about the specific role of human UPP2 (hUPP2)"]. The human UPP2
  evidence base is thin relative to UPP1; several downstream/derived catabolic annotations rest on a
  single paper (Johansson 2003, MGI-assigned IDA) or on IEA propagation.

## Structure and regulation

- Homodimer [file:human/UPP2/UPP2-uniprot.txt "Homodimer"]; crystal structures 2XRF, 3P0E, 3P0F.
- **Redox regulation** unique to UPP2: a conditional intramolecular disulfide bridge (Cys95–Cys102)
  dislocates the catalytic phosphate-coordinating Arg100, inactivating the enzyme
  [PMID:21855639 "a conditional intramolecular disulfide bridge can form within the protein that dislocates a critical phosphate-coordinating arginine residue (R100) away from the active site, disabling the enzyme"].
  This feature is conserved in UPP2 but absent from UPP1 (which lacks the necessary cysteine)
  [PMID:21855639 "this feature is conserved among UPP2 homologs and lacking in all UPP1 proteins due to the absence of a necessary cysteine residue"]. In vitro, hUPP2 activity is abolished by GSSG and
  protected by DTT; native mouse liver UPP2 activity nearly doubles under anaerobic conditions
  [PMID:21855639 "Uridine phosphorylase activity was nearly double in those liver samples protected from oxygen exposure"].
- The authors speculate UPP2 "may have additional functions in sensing and initiating cellular
  responses to oxidative stress" [PMID:21855639 "suggest UPP2 may have additional functions in sensing and initiating cellular responses to oxidative stress"] — a hypothesis, not an established function.

## Pharmacology

- Relevant to fluoropyrimidine chemotherapy: UPP activates 5-fluorouracil / capecitabine
  [PMID:21855639 "plays an important pharmacological role in activating fluoropyrimidine nucleoside chemotherapeutic agents such as 5-fluorouracil and capecitabine"]. UniProt DrugBank links: Capecitabine, Fluorouracil.

## Annotation-specific notes

### Molecular function
- **GO:0004850 uridine phosphorylase activity** — CORE. Directly measured for recombinant hUPP2
  (Johansson 2003 IDA; Roosild 2011 IDA) and the enzyme's defining activity. IBA and IEA (ARBA/Rhea)
  duplicates are consistent → ACCEPT.
- **GO:0047847 deoxyuridine phosphorylase activity**, **GO:0009032 thymidine phosphorylase activity**,
  **GO:0016154 pyrimidine-nucleoside phosphorylase activity** — all supported by the measured broad
  substrate specificity in Johansson 2003 (IDA). ACCEPT the parent MF (GO:0016154) as core; keep the
  substrate-specific MFs (accept — they are correct, though thymidine/deoxyuridine are minor/analog
  substrates; Vmax toward thymidine is low per UniProt kinetics).
- **GO:0003824 catalytic activity** (IEA, InterPro) — correct but uninformative parent; MARK_AS_OVER_ANNOTATED.
- **GO:0016763 pentosyltransferase activity** (IEA, InterPro) — this is the correct EC 2.4.2 parent
  (glycosyl/pentosyl transfer); accurate but general. KEEP_AS_NON_CORE (it is the true parent term).
- **GO:0005515 protein binding** (IPI, PMID:25416956, with SIAH1) and **GO:0042802 identical protein
  binding** (IPI; homodimer, PMIDs 25416956/29892012/31515488/21855639) — the homodimer is real
  [file:human/UPP2/UPP2-uniprot.txt "Homodimer"]. Bare "protein binding" is uninformative →
  MARK_AS_OVER_ANNOTATED. Identical protein binding reflects the biologically real homodimer → ACCEPT/KEEP_AS_NON_CORE.

### Biological process
- **GO:0006218 uridine catabolic process** — CORE (multiple IDA + IBA). ACCEPT.
- **GO:0044206 UMP salvage** (IEA UniPathway) — matches the UniProt PATHWAY statement → ACCEPT.
- **GO:0046050 UMP catabolic process**, **GO:0046074 dTMP catabolic process**, **GO:0046079 dUMP
  catabolic process**, **GO:0006249 dCMP catabolic process** — MGI-assigned IDA (Johansson 2003).
  These are inferences from the demonstrated phosphorylase activities on the corresponding nucleosides
  (the paper measured nucleoside phosphorolysis, not nucleotide (monophosphate) catabolism directly).
  Experimental → not REMOVE; the mononucleotide-level catabolism is a downstream/indirect framing →
  KEEP_AS_NON_CORE.
- **GO:0006248 CMP catabolic process** (IEA Ensembl) — cytidine/CMP is not a demonstrated UPP2 substrate
  (substrates are uridine/deoxyuridine/thymidine). Wrong-substrate IEA propagation → this row is NOT in
  the seeded YAML/GOA export (Ensembl row present in UniProt DR but not in the 36-annotation GOA TSV),
  so no action needed. (Documented here for completeness.)
- **GO:0042178 xenobiotic catabolic process** (IDA, Johansson 2003) — reflects phosphorolysis of the
  fluoropyrimidine analogs (5-fluorouridine, 5-fluoro-2'-deoxyuridine). Correct but peripheral →
  KEEP_AS_NON_CORE.
- **GO:0009116 nucleoside metabolic process** (IEA + NAS) and **GO:0046108 uridine metabolic process**
  (NAS, from PMID:11278417) — correct but general/parent terms. MARK_AS_OVER_ANNOTATED (nucleoside
  metabolic process) / KEEP_AS_NON_CORE (uridine metabolic process, more specific & correct but the
  catabolic child GO:0006218 is the better representation).
- **GO:0009166 nucleotide catabolic process** (IEA InterPro) — UPP2 acts on nucleoSIDEs, not
  nucleoTIDEs; the InterPro-derived nucleotide framing is a mis-generalization → MARK_AS_OVER_ANNOTATED.

### Cellular component
- **GO:0005829 cytosol** (IBA, and TAS Reactome ×2) — CORE localization. ~60-70% of UPP is soluble
  cytosolic [PMID:11278417 "Approximately 60-70% of the total UPase exists in the cytosol as a soluble protein"] (that paper is UPP1, but cytosolic localization is expected for UPP2 too and supported by IBA). ACCEPT.
- **GO:0005737 cytoplasm** (IEA InterPro) — correct parent of cytosol; KEEP_AS_NON_CORE (redundant with cytosol).
- **GO:0045098 type III intermediate filament** (IDA, PMID:11278417) — **CAUTION**: PMID:11278417
  (Russell et al. 2001) is about **UPP1** ("Uridine phosphorylase association with vimentin"), published
  two years BEFORE UPP2 was cloned (Johansson 2003). The vimentin association was demonstrated for UPP1,
  not UPP2 [PMID:11278417 "We demonstrate for the first time that UPase is associated with vimentin"].
  This annotation appears to be a paralog mis-attribution to UPP2. Per curation policy, experimental
  (IDA) annotations are not REMOVEd on the basis of an abstract; the full text was read by the curator.
  However the abstract is unambiguous that the studied enzyme predates UPP2's discovery, so this is
  flagged as a likely over-annotation → MARK_AS_OVER_ANNOTATED, with a reference_review noting the
  probable UPP1 mis-attribution. (Also flagged: PMID:11278417 as the source of the NAS cytosol and NAS
  uridine metabolic process rows — same UPP1 paper.)

## Core functions summary

1. **Uridine phosphorylase activity (GO:0004850)** — reversible phosphorolysis of uridine (and
   deoxyuridine/thymidine) to uracil + (deoxy)ribose-1-phosphate; the defining, experimentally
   demonstrated MF. Parent enzymatic class = pyrimidine-nucleoside phosphorylase activity (GO:0016154).
2. **Uridine catabolic process (GO:0006218)** / pyrimidine salvage — the BP context; UPP2 contributes
   the "uracil from uridine" step of the pyrimidine salvage/UMP biosynthesis pathway (GO:0044206).
3. **Cytosol (GO:0005829)** — localization.
