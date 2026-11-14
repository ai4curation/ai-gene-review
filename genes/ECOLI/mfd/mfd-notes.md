# mfd (P30958, Escherichia coli K-12) curation notes

## 2026-11-10 review pass (Claude, AI-assisted)

Provider deep research was not available for this gene (no provider API keys in this
campaign), so no `-deep-research-<provider>.md` file exists. These notes are based on the
cached publications in `publications/`, the UniProt record (`mfd-uniprot.txt`) and the
PTHR47964 PAINT table.

### Identity and domain architecture

- Mfd/TRCF is a 1148-aa monomeric SF2 ATPase with an N-terminal UvrB-homology module, a
  central RNAP-interacting domain (RID, CarD-like) and a C-terminal RecG-like translocase
  motor [file:ECOLI/mfd/mfd-uniprot.txt "The N-terminal region interacts with UvrA,
  the central region interacts with RNAP, and the C-terminal DNA translocase region possesses
  ATPase activity."].
- Family placement: InterPro IPR004576 (Mfd), NCBIfam TIGR00580 (mfd), HAMAP MF_00969 (TRCF).
  UniProt cross-references PANTHER PTHR47964:SF1; the PAINT Mfd node is PTN008553567 in
  PTHR47964 (seed P30958 itself, taxon:2) carrying DNA binding, DNA translocase activity,
  RNA polymerase core enzyme binding, TC-NER damage recognition and regulation of
  DNA-templated transcription.

### Mechanism (core)

- Selby & Sancar showed Mfd is the transcription-repair coupling factor: mfd mutant extracts
  lack strand-specific repair and are complemented by purified TRCF [PMID:1763073
  "mfd- cells are incapable of strand-specific repair"].
- Purified Mfd displaces lesion-stalled RNAP in an ATP-dependent reaction, binds UvrA and
  stimulates transcribed-strand repair only during transcription [PMID:8465200 "The Mfd
  protein was shown to (i) displace RNAP stalled at a lesion in an adenosine
  triphosphate-dependent reaction"].
- Binding properties: nonspecific dsDNA binding, ATP-dependent [PMID:7876261 "TRCF bound
  nonspecifically to double stranded DNA"]; residues 1-378 bind UvrA [PMID:7876261
  "residues 1-378 bind to UvrA"].
- No helicase activity [PMID:7876262 "We found that TRCF does not have a helicase activity
  on any of the substrates tested."]; it delivers UvrA2B to the lesion [PMID:7876262
  "Stimulation of repair occurs via facilitating the delivery of the A2B1 complex to the
  lesion site by the TCRF"].
- Translocase: Mfd rewinds upstream DNA and pushes RNAP forward [PMID:12086674 "Mfd may act
  through a translocase activity that rewinds upstream DNA"]; it is described as an
  ATP-dependent DNA translocase in single-molecule work [PMID:22960746 "Bacterial
  transcription-coupled repair is initiated when RNA polymerase stalled at a DNA lesion is
  removed by Mfd, an ATP-dependent DNA translocase."]; continues to translocate after RNAP
  displacement [PMID:24554077]; forms a long-lived Mfd-RNAP complex that translocates on DNA
  [PMID:25961799]; and translocates autonomously [PMID:29224782 "discovered that Mfd
  translocates autonomously on DNA"].
- Structure: cryo-EM of Mfd-EC complexes [PMID:33480355 "Mfd mediates TCR in bacteria by
  removing the stalled RNAP concealing the lesion and recruiting Uvr(A)BC."]; Mfd binds the
  RNAP beta subunit via its RID [PMID:33480355 "Mfd binds to the RNAP β subunit via its
  RNAP-Interacting Domain RID"].
- The TRCF-UvrA core complex was crystallized and the C-terminal domain autoinhibits UvrA
  binding [PMID:22331906 "the C-terminal domain of TRCF is inhibitory for UvrA binding, but
  not RNA polymerase release"]. GO:1990250 (TC-NER DNA damage recognition complex) cites
  this same paper in its definition, so it is the better term for the ComplexPortal
  "DNA repair complex" row.

### Transcription roles (non-core)

Mfd also rescues backtracked or arrested complexes and releases RNAP stalled by other
roadblocks [PMID:12086674 "arrested complexes are rescued into productive elongation"];
[PMID:29224782 "Mfd prevents RNAP backtracking or rescues a severely backtracked RNAP"].
These are kept as non-core regulation-of-transcription annotations.

### Annotation issues found

- GO:0003684 damaged DNA binding (InterPro2GO, IPR004576): Mfd is targeted to damage by the
  stalled RNAP, not by binding the lesion; a transcription bubble was bound no better than
  duplex DNA [PMID:7876261]. Removed; recorded as an InterPro source defect.
- GO:0005515 protein binding (UvrA, IPI): uninformative; the interaction is captured by
  the TC-NER damage recognition complex (GO:1990250) proposal.
- PMID:18304323 (cytosol proteomics) is accessible but Mfd is not named in the cached main
  text; the identification is presumably in a supplementary table, so the EcoCyc curator is
  deferred to.
