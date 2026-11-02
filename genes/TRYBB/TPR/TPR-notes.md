# TPR (trypanothione reductase), Trypanosoma brucei brucei, UniProt P39051

**Note:** Automated deep research was unavailable in this environment (Falcon auth
failure, invalid OpenAI key). These notes are a manual literature review built from the
UniProt record, PubMed-verified primary papers cached in `publications/`, and web searches.

## 2026-10-15 manual literature review

### Identity and family
- Swiss-Prot P39051, TYTR_TRYBB, 492 aa, EC 1.8.1.12; class-I pyridine nucleotide-disulfide
  oxidoreductase family (glutathione reductase / lipoamide dehydrogenase / mercuric
  reductase superfamily); PANTHER PTHR42737 (GLUTATHIONE REDUCTASE) SF2; InterPro
  IPR001864 Trypnth_redctse; NCBIfam TIGR01423 trypano_reduc.
- Gene cloned and sequenced from T. brucei and Crithidia
  [PMID:1453951 "Trypanothione reductase belongs to the family of flavoprotein disulphide oxidoreductases that include glutathione reductases, dihydrolipoamide dehydrogenases and mercuric reductases."]
  [PMID:1453951 "Trypanothione reductase and its substrate, trypanothione disulphide, are unique to parasitic trypanosomatids"]

### Substrate: trypanothione is lineage-specific
- Trypanothione (N1,N8-bis(glutathionyl)spermidine) discovered as the cofactor needed by the
  trypanosomatid "glutathione reductase" activity
  [PMID:3883489 "Glutathione reductase from trypanosomes and leishmanias, unlike glutathione reductase from other organisms, requires an unusual low molecular weight cofactor for activity."]
- Review: [PMID:1444271 "Together with the NADPH-dependent flavoprotein, trypanothione reductase, the dithiol form of trypanothione provides an intracellular reducing environment in these parasites, substituting for glutathione and glutathione reductase found in the mammalian host."]
  and [PMID:1444271 "Trypanothione and its related enzymes are involved in defense against damage by oxidants, certain heavy metals, and possibly xenobiotics."]

### Biochemistry of the T. brucei enzyme (PMID:19747949, full text)
- Recombinant TbTryR crystal structure 2.3 A (PDB 2WBA), nearly identical to T. cruzi.
- Homodimer, 1 FAD per subunit:
  [PMID:19747949 "TbTryR is a homodimer and each subunit of the final model comprises 489 amino acid residues, 1 FAD, 1 NADPH, 4 glycerol and 1 sulphate molecules."]
- Strict substrate specificity, NADPH over NADH and T(S)2 over GSSG:
  [PMID:19747949 "TbTryR was highly specific for the electron donor (NADPH) and electron acceptor (T(S)2) in the 412 nm assay."]
  [PMID:19747949 "the kinetic and physical properties of TbTryR are consistent with trypanothione reductases from other trypanosomatids such as T. cruzi and L. donovani, especially the striking preference for T(S)2 over glutathione disulphide"]
  [PMID:19747949 "However, the enzymes trypanothione reductase and glutathione reductase are highly specific for their respective disulphide substrates [5]"]
- Redox-active disulfide Cys52/Cys57; charge-transfer complex between FAD and Cys57.
- Consequence for GO: the TreeGrafter IEA "glutathione-disulfide reductase (NADPH) activity"
  is a paralog/family-level over-annotation; TbTryR does not appreciably reduce GSSG.

### In vivo role (PMID:10672177, abstract only)
- Tet-regulated single-allele line, Krieger et al. 2000:
  [PMID:10672177 "In Kinetoplastida, trypanothione and trypanothione reductase (TRYR) provide an intracellular reducing environment, substituting for the glutathione-glutathione reductase system found in most other organisms."]
  [PMID:10672177 "trypanosomes containing less than 10% of wild-type enzyme activity were unable to grow"]
  [PMID:10672177 "hypersensitivity towards hydrogen peroxide (EC50 = 3.5 microM) was observed compared with the wild type (EC50 = 223 microM)"]
  [PMID:10672177 "if the trypanosomes were injected into mice in the absence of tetracycline, no infection was detectable"]
- So TR is essential, needed for H2O2 resistance and for virulence in mice. The virulence
  phenotype is a necessity readout, not a host-interaction function; no host-process term
  is warranted.

### Localization
- UniProt: Cytoplasm (curated). Sequence starts directly with the FAD-binding Rossmann motif
  (MSKIFDLVVIGAGSGG...), so no N-terminal mitochondrial presequence; C-terminus ...ESSL is
  not a canonical PTS1, so no glycosomal targeting signal.
- Smith, Opperdoes & Fairlamb 1991 (PMID:1779986) studied subcellular distribution in BSF and
  PCF T. brucei, but the cached record has no abstract and I could not access the result.
  Mitochondrion (TreeGrafter, inherited from GR family members that are dual-targeted)
  therefore left UNDECIDED rather than removed.
- Kinetoplastid mitochondrion does use trypanothione-dependent peroxidases
  (PMID:11522350 title only, not cached) - whether TR itself is imported, or reduced
  trypanothione is supplied from the cytosol, is an open question.

### Drug target context
- [PMID:20735352 "most of the pathway enzymes involved in its synthesis, utilization and reduction have been proposed as drug targets for therapeutic intervention"]

### Annotation decisions summary
- MF: trypanothione-disulfide reductase (NADPH) activity GO:0015042 = core (ACCEPT).
  General parents (GO:0016491, GO:0015036, GO:0016668) -> MODIFY to GO:0015042.
  GSSG reductase GO:0004362 -> REMOVE (contradicted by substrate specificity).
  FAD binding -> KEEP_AS_NON_CORE.
- BP: cell redox homeostasis ACCEPT; cellular response to oxidative stress ACCEPT;
  glutathione metabolic process -> MODIFY to trypanothione metabolic process GO:0046206
  (OLS-verified); cellular oxidant detoxification KEEP_AS_NON_CORE (true downstream role,
  but the inference came from the incorrect GR MF).
- CC: cytosol ACCEPT; cytoplasm MODIFY -> cytosol; mitochondrion UNDECIDED.

## Deliberately short supporting_text (do not "complete")

One quote in this review stops before the end of its source sentence on
purpose, and was expanded by an automated pass twice before being restored
both times. Leave it as it is:

- PMID:19747949 `However, the enzymes trypanothione reductase and glutathione
  reductase are highly specific for their respective disulphide substrates` —
  this is the sentence backing the specificity argument. The source continues
  with a bracketed citation and a fused next paragraph, neither of which the
  row claims.
