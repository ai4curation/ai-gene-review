# Srebf1 (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Srebf1` resolved P56720 (SRBP1_RAT; RGD:69423; GeneID 78968);
  GOA file keyed to P56720, 152 rows. No accession switch.
- No deep-research API key; literature synthesis written by hand in
  `Srebf1-deep-research-manual.md`. Also fetched PMID:19332540 (requested),
  PMID:7739539 (rat ADD1 dual DNA specificity, cited by UniProt) and PMID:8336713
  (ADD1 cloning).
- PMID:19332540 (palmitate/H4IIEC3): SREBP-1c is peripheral; palmitate down-regulates
  SREBP-1c mRNA [PMID:19332540 "palmitate dramatically down-regulated the expression of
  SREBP-1c in H4IIEC3 hepatocytes"]. Supports only the IEP cellular response to fatty
  acid row.
- PMID:19158095 (full text): SCAP-SREBP-1c complex binds Sar1-Sec23/24; insulin
  increases this. Supports SREBP-SCAP complex and COPII association.

## Decisions

- Core MF: DNA-binding transcription activator activity, RNAPII-specific (GO:0001228),
  with sterol response element binding (GO:0032810) and RNAPII cis-regulatory DNA
  binding (GO:0000978). General DNA-binding / TF rows MODIFY to these.
- NEW: E-box binding (GO:0070888) from rat ADD1 PMID:7739539 (direct DNA-binding assay).
- Nuclear receptor activity (ISO/IEA from human ParkinsonsUK-UCL IDA PMID:23610160):
  REMOVE, wrong class of TF; derived IEA intracellular receptor signaling pathway REMOVE.
- Negative regulation of triglyceride metabolic process (ISO from human BHF-UCL IDA
  PMID:28483554): sign inversion, MODIFY to GO:0010867.
- Mitophagy / protein localization to mitochondrion / protein stability rows (from
  human ParkinsonsUK-UCL IMP PMID:24912190): indirect lipid-supply effect, over-annotated.
- IEP response rows: kept as non-core (true expression responses, rat data). Lung
  development IEP over-annotated (expression timing only). Response to xenobiotic row
  from PMID:17526932 UNDECIDED: abstract is about SREBP-2 and full text unavailable.
- Consistent with the human SREBF1 review where applicable.
