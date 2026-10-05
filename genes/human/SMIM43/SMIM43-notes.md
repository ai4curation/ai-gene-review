# SMIM43 (NEMEP; formerly TMEM155) — curation notes

## 2026-09-30 — initial review (claude-code)

### Identity
- UniProt Q4W5P6; 63 aa; single predicted TM helix (res 9-29). UniProt CAUTION: formerly
  TMEM155, a 130-residue ORF now considered the wrong CDS; an upstream ORF encodes the
  63-aa product. Mouse ortholog: Gm11549 / Nemep (A0A286YD83).
- The human 63-aa product was experimentally shown to be translated
  [PMID:35810171 "TMEM155 likewise encodes a 63 aa peptide (“hNEMEP”, sharing 93.6% identity with mNEMEP)"].

### Literature search
- PubMed E-utilities query `NEMEP OR SMIM43 OR TMEM155 OR Gm11549` -> 4 hits. Only
  PMID:35810171 (Fu et al. 2022 Nat Commun) is functional. Others are transcriptomic
  biomarker lists naming TMEM155 (PMID:41548166 Sjogren/MALT/thyroid; PMID:37077524
  acute HIV PBMC upregulation) or unrelated (PMID:28835756). Not cited in the review.
  Note: the user's brief said "Fu et al. 2020"; the actual paper is 2022 (PMID:35810171,
  verified by title/DOI in PubMed record).

### Key findings (Fu et al. 2022, PMID:35810171; full text cached)
Mostly MOUSE (mESC / embryoid body) data:
- Nodal target, required for mesendoderm differentiation of mESCs
  [PMID:35810171 "The absence of NEMEP in EBs dramatically impaired the expression of well-known mesendoderm LDTFs including Gsc, Mixl1, T, Eomes, Foxa2, and Sox17"].
- Plasma membrane (mouse, tagged overexpression)
  [PMID:35810171 "Immunostaining of ectopically expressed, FLAG-tagged NEMEP in mouse ES cells revealed that NEMEP was localized at the plasma membrane"].
- Binds GLUT1/GLUT3; HUMAN proteins tested in HEK293T co-IP (basis of human IPI rows)
  [PMID:35810171 "Then, we confirmed that the homologous human NEMEP protein also interacts with the human GLUT1 and GLUT3 proteins"].
- TMD and H51-F57 required for binding
  [PMID:35810171 "These results demonstrate that the TMD domain and NEMEP residues H51-F57 are essential for NEMEP-GLUT1 and -GLUT3 interactions."].
- KO reduces glucose uptake, rescued by NEMEP
  [PMID:35810171 "Compared to WT EBs, the Nemep KO EBs displayed significant reductions in glucose uptake, glycolytic function, and mitochondrial respiration"].
- Binding-deficient mutants fail to boost uptake in GLUT1/3-overexpressing cells; authors hedge
  [PMID:35810171 "Therefore, NEMEP’s boosting glucose uptake likely through interactions with the known glucose transporters GLUT1 and GLUT3."].
- HUMAN functional data: only overexpression of hNEMEP in HepG2
  [PMID:35810171 "the overexpression of human NEMEP in HepG2 cells (Supplementary Fig. 7d) also significantly increased glucose consumption, lactate excretion, glycolysis activity"].

### Mouse GOA (A0A286YD83) for comparison
IDA plasma membrane, IMP GO:0010828 and GO:0048382, IPI GLUT binding — all PMID:35810171.
Human IEA/ISS rows are projections from these.

### Decisions
- Plasma membrane: ACCEPT (both rows).
- Transmembrane transporter binding (IPI x2, human proteins): ACCEPT; IEA ACCEPT.
- GO:0010828: MODIFY -> GO:0046326 positive regulation of D-glucose import across plasma
  membrane (uptake of glucose/2-DG into cells is what was measured).
- Mesendoderm development: KEEP_AS_NON_CORE. Mouse-only necessity evidence; NEMEP acts by
  supplying glucose uptake (metabolic support), not as a developmental regulator per se.
  Not tested in human cells.
- NEW MF GO:0141109 transporter activator activity: proposed. Binds GLUT1/3 and increases
  their transport activity in a binding-dependent manner. Comparator (QuickGO, 2026-09-30): the SERCA-regulating
  microproteins carry regulator-type MFs on their pump partner: DWORF P0DN84 GO:0008047
  enzyme activator activity (ISS); SLN O00631 and PLN P26678 GO:0004857 enzyme inhibitor
  activity (ISS). For a non-enzymatic transporter partner the analogous term is GO:0141109.
  Caveat: authors say "likely"; no reconstituted/proteoliposome assay.
