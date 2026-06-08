# DNAJC1 (MTJ1 / ERdj1 / HTJ1) research notes

UniProt: Q96KC8. 554 aa, precursor. Single-pass type I ER-membrane protein: lumenal N-term
(48-153) with J-domain (65-129) facing ER lumen; TM 154-174; large cytosolic C-term (175-554)
with two SANT domains (325-379, 492-547) and disordered/phospho-rich region. ER membrane / nuclear
membrane / microsome membrane.

## Core function: ER-membrane BiP (HSPA5) co-chaperone + ribosome-associated translation regulator
- [UniProt FUNCTION "May modulate protein synthesis."] (sparse; By similarity).
- J domain (lumenal) stimulates BiP/HSPA5 ATPase: [PMID:14668352 "its lumenal J-domain stimulates the
  ATPase activity of the molecular chaperone BiP/GRP78"] (citing Chevalier 2000). => GO:0001671 ATPase
  activator activity TAS PMID:14668352. CORE MF.
- Cytosolic domain interacts with ribosomes (By similarity) — basis of translation/protein-synthesis
  modulation (ERdj1/MTJ1 is the classic ribosome-associated ER membrane J-protein). UniProt SUBUNIT
  "Interacts (via cytosolic domain) with ribosomes (By similarity)."

## SANT2 domain functions (serpin/protease regulation)
- [PMID:14668352 "The second SANT domain of HTJ1 (SANT2) was found to be sufficient for binding to
  ACT... Preincubation of ACT with... SANT2 wild-type... results in an apparent loss of ACT inhibitory
  activity toward chymotrypsin."] SERPINA3/ACT (P01011). => GO:0045861 negative regulation of
  proteolysis TAS; GO:0050708 regulation of protein secretion IDA PMID:14668352.
- [PMID:16271702 "BIP co-chaperone MTJ1/ERDJ1 interacts with inter-alpha-trypsin inhibitor heavy
  chain 4"] ITIH4 (Q14624); SANT2 protects ITIH4 from kallikrein cleavage. Protein binding IPI.

## Localization
- ER membrane (single-pass type I) — CORE. Nuclear membrane, microsome membrane (UniProt). ISS ER.
- Ensembl-projected plasma membrane (GO:0005886, GO_REF:0000107) — CONFLICTS; DNAJC1 is an
  ER/nuclear membrane protein. MARK_AS_OVER_ANNOTATED.
- Generic membrane HDA PMID:19946888 (NK membrane proteome) — KEEP_AS_NON_CORE.
- endomembrane system IBA — ACCEPT (general, correct).

## Protein-binding IPIs (mostly HT)
- SERPINA3/ACT (P01011) PMID:14668352, P80294 — specific SANT2 (functional). 
- ITIH4 (Q14624) PMID:16271702 — specific SANT2 (functional).
- CFTR (P13569) PMID:35156780, 36012204 — CFTR interactome HT (CFTR is an ERAD substrate, plausible
  client of the BiP/ERdj1 system but HT).
- RMND1 (Q9NWS8), TNFRSF10C (O14798), ATP6V0C (P27449), CYP4F2, PLP2, etc. PMID:28514442/32296183/
  32814053/33961781 — HT interactome.
None of the bare protein-binding HT calls are core; KEEP_AS_NON_CORE.

## MF/BP assignment
- Core MF: GO:0001671 ATPase activator activity (lumenal J-domain stimulates BiP ATPase).
- Core BP: regulation of translation / protein synthesis (ribosome-associated) — GOA has only
  GO:0051246 regulation of protein metabolic process IEA (ARBA); DR line has GO:0006417 regulation of
  translation IEA:Ensembl (not in GOA TSV). The protein-synthesis modulation is the classic ERdj1 role.
- SANT2 serpin/protease modulation: GO:0045861 neg reg proteolysis, GO:0050708 reg protein secretion —
  genuine but specialized; KEEP_AS_NON_CORE / ACCEPT as documented.
