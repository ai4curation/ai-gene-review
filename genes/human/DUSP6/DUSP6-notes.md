# DUSP6 (MKP-3, PYST1; UniProt Q16828) curation notes

## 2026-10-01 initial review

Context: reviewed as the representative ERK-specific DUSP for the DUSP/MKP
negative-feedback step (`mapk_negative_regulation` / `dusp_role`) in
`modules/erk_cascade.yaml` (module not edited).

### Core biology

- ERK-selective dual-specificity MKP. [PMID:8670865 "Like CL100/ MKP-1, Pyst1 dephosphorylates and inactivates MAP kinase in vitro and in vivo."]
  and [PMID:8670865 "Pyst1 displays very low activity towards the stress-activated protein kinases (SAPKs) or RK/p38 in vitro, indicating that these kinases are not physiological substrates for Pyst1"].
- ERK2 docking activates the enzyme. [PMID:11239467 "MKP-3, a prototypical MKP, achieves substrate specificity through its N-terminal domain binding to the MAPK ERK2, resulting in the activation of its C-terminal phosphatase domain."]
- Cytoplasmic via CRM1-dependent NES; shuttles; anchors ERK2 in cytoplasm.
  [PMID:15269220 "the cytoplasmic localization of MKP-3 is mediated by a chromosome region maintenance-1 (CRM1)-dependent nuclear export pathway"];
  [PMID:15269220 "the ability of MKP-3 to cause the cytoplasmic retention of ERK2 requires both a functional kinase interaction motif and NES"].
- ERK-driven feedback: FGF/ERK/Ets induce transcription.
  [PMID:18321244 "ERK signalling activates DUSP6/MKP-3 transcription to deliver ERK1/2-specific negative-feedback control of FGF signalling"];
  mouse knockout [PMID:17164422 "Targeted inactivation of Dusp6 increases levels of phosphorylated ERK"].
- Endogenous human knockdown (IMP): [PMID:18771677 "knockdown of MKP-3, via siRNA, increased ERK1/2 phosphorylation"].
- ERK phosphorylates DUSP6 (Ser159/Ser197) promoting degradation:
  [PMID:15632084 "ERK1/2 exert a positive feedback loop on their own activity by promoting the degradation of MKP-3, one of their major inactivators in the cytosol"].
- Deep research (falcon) also notes 2024 HER2 Y877 dephosphorylation in PDAC models
  (Bulle et al. 2024, not cached, not used for annotation) and BCI inhibitor non-selectivity.

New PMIDs fetched (all resolved from DOIs given in the deep-research report via NCBI
esearch, not guessed): 11239467, 15269220, 17164422, 18321244, 15632084.

### Decisions

- Core MF: GO:0017017 MAP kinase tyrosine/serine/threonine phosphatase activity
  (ACCEPT for IBA/IEA/IDA). Generic phosphatase MFs (GO:0004721, GO:0004722,
  GO:0004725, GO:0008138; EXP/IEA/TAS) MODIFY -> GO:0017017. IBA GO:0033550 and
  GO:0008330 ACCEPT (accurate partial descriptions).
- Core BP: GO:0070373 negative regulation of ERK1 and ERK2 cascade (ACCEPT IBA/IEA/IMP).
  GO:0043409 (IDA/IEA) MODIFY -> GO:0070373 (ERK-selective, does not block JNK/p38).
  GO:0000165, GO:0070371 (TAS/IEA) and GO:0007165 (IBA) MODIFY -> GO:0070373:
  DUSP6 terminates rather than propagates the cascade.
- Protein binding IPIs: ERK1/ERK2 partners MODIFY -> GO:0051019 MAP kinase binding
  (docking is functional: specificity, activation, anchoring). APP, PHB2, TXK
  (high-throughput screens) REMOVE as uninformative.
  PMID:18060821 cached abstract is on SpvC lyase and does not mention DUSP6; did not
  REMOVE, deferred to curator (MODIFY to MAPK binding, interaction well established).
- CC: cytoplasm/cytosol ACCEPT; nucleoplasm (Reactome TAS) MARK_AS_OVER_ANNOTATED
  (shuttles but excluded from nucleus at steady state).
- Non-core: positive regulation of apoptotic process (IDA, IBA), regulation of heart
  growth (IBA from mouse Dusp6 MGI:1914853, verified via UniProt Q9DBB1), cell
  differentiation and response to growth factor (IEA from rat).
- response to nitrosative stress (IEP, PMID:10846176): MARK_AS_OVER_ANNOTATED;
  expression/mRNA-stability readout, NO used as survival factor, phosphatase activity
  unaffected. response to xenobiotic stimulus (IEA from rat): REMOVE.
- No NOT (negated) annotations exist in GOA for DUSP6. A possible MF-shaped NOT
  (p38/JNK phosphatase) is raised as a suggested question only.

### Module-relevant summary

- Best MF for the erk_cascade DUSP step: GO:0017017.
- PANTHER: PTHR10159 "DUAL SPECIFICITY PROTEIN PHOSPHATASE"; subfamily PTHR10159:SF45
  "DUAL SPECIFICITY PROTEIN PHOSPHATASE 6" (UniProt DR line; names verified in
  interpro/panther/panther.obo; Q16828 not yet in panther-members.tsv index).
