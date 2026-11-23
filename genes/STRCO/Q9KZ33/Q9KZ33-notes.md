# Q9KZ33 (SCO7099) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

**Identity.** Q9KZ33 is the full-length 300-aa product of SCO7099 (TrEMBL, PE 4; single
sequence version). It is not a fragment, isoform or alternative gene model: it carries the
complete ECF sigma2/sigma4 regions (IPR052704, IPR013324, SSF88659) and a ~130-aa C-terminal
NTF2-like extension (IPR032710 / SSF54427). Length matches the characterised M. tuberculosis
relatives SigI (290 aa) and SigJ (312 aa).

**Group.** The NTF2-like (SnoaL-type) C-terminal extension is the hallmark of ECF41 sigma
factors [PMID:22950025 "In contrast to other ECF σ factors, proteins of group ECF41 contain a
large C-terminal extension, which is crucial for σ factor activity."]. PANTHER puts Q9KZ33 in
PTHR30173:SF43 "ECF RNA POLYMERASE SIGMA FACTOR SIGI-RELATED" together with M. tuberculosis SigI
(P9WGH3), which is ECF41 [PMID:32180013 "Mtb-SigI belongs to the ECF41 family of sigma
factor"]. Streptomyces carries several ECF41 copies [PMID:22950025 "Especially the genus
Streptomyces contains large numbers of ECF41 σ factors with at least four copies per genome"].
Group ECF41 membership is my inference, not stated by a source for SCO7099.

**Evolutionary grounding of the IBA.** The GO:0016987 IBA comes from PTN001249270 seeded by
M. tuberculosis SigJ (L0TCG5), which PANTHER places in SF36, not SF43. So the IBD node is above
the SF36/SF43 split; sigma factor activity is family-wide, so the transfer is sound. PAINT
propagated only sigma factor activity — no stress-response or oxidative-stress terms from SigJ
(SigJ knockout is H2O2-sensitive per PMID:26249679 background) — and such SigJ-specific
phenotypes should not be transferred to SCO7099, which is in a different subfamily anyway.

**Pairwise check** (`Q9KZ33-bioinformatics/RESULTS.md`): ~33% identity to SigI and ~35% to
SigJ over ~270 aligned residues, including the C-terminal extension; pairwise identity does not
resolve the subfamily, so I rely on PANTHER's HMM placement.

**Experimental data on SCO7099.** Only one: overexpression transformants could not be obtained
[PMID:39264300 "Transformants were not obtained for three sigma factors: ... and SCO7099
(unknown function)"]. Caution: the "SigI" in that paper is the S. coelicolor SigB-family factor,
unrelated to M. tuberculosis ECF SigI. Sekurova et al. 2024 (PMID:39026318, cached) on deletions
of conserved Streptomyces ECF genes does not mention SCO7099 or ECF41; not cited.

**Genomic context (UniProt, strand not checked):** SCO7097 MarR-family regulator, SCO7098
uncharacterised 178 aa, SCO7100 alpha/beta-hydrolase-fold "oxidoreductase", SCO7101
dehydrogenase. No carboxymuconolactone decarboxylase neighbour; no conclusion drawn.

**Annotation decisions.** GO:0016987 IBA ACCEPT (core). GO:2000142 IEA ACCEPT (process
counterpart of the MF; as specific as evidence allows). Core function unchanged in terms;
description rewritten to add probable ECF41 membership and fused-regulatory-domain model.
Cytoplasm location retained in core_functions (no GOA row).

**Relative to review next.** M. tuberculosis SigI (P9WGH3, Rv1189), same PANTHER subfamily SF43;
no review in repo (genes/MYCTU has no sigI). The family review
interpro/panther/PTHR30173/PTHR30173-review.yaml lists only Q9KZ33 under SF43; it agrees with the
placement but does not note that the IBA seed SigJ is in SF36 or list SigI as an SF43 member.
No modules reference this family.
