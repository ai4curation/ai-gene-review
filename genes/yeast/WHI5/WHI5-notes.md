# WHI5 (Q12416, YOR083W) - curation notes

Working journal for the GO annotation review of S. cerevisiae Whi5. Append; do not rewrite.

## 2026-09-25 - initial review

### Identity and family
- UniProt Q12416, "G1-specific transcriptional repressor WHI5", 295 aa, WHI5/NRM1 family, Pfam
  PF08528 (Whi5), InterPro IPR039198 (Srl3/Whi5) and IPR013734 (TF_Nrm1/Whi5). Features are
  disordered regions (1-171, 249-295) and compositionally biased acidic/low-complexity segments;
  no DNA-binding domain. Thirteen phosphosites recorded (T47, S59, S62, S161, S262 by
  PMID:15210110 plus phosphoproteomics).
- Paralog in S. cerevisiae: Whi7/Srl3 (SGD:S000001799), the second member of PANTHER node
  PTN002000919 that seeds the IBA rows. MBF has its own corepressor, Nrm1.

### Core biology (what the gene product does)
- SBF-bound G1/S corepressor. [PMID:15210110 "Whi5 was identified as a stably bound component
  of SBF but not MBF."] [PMID:15210110 "Whi5 associates with G1-specific promoters via SBF during
  early G1 phase, then dissociates coincident with transcriptional activation."]
- Recruited by the transcription factor, not by DNA. [PMID:15210111 "Whi5 is recruited to G1/S
  promoter elements via its interaction with SBF/MBF in vivo and in vitro."] [PMID:19823668
  "Whi5 associates indirectly with G1 phase-regulated promoters through interaction with SBF and
  MBF."]
- Mechanism of repression includes HDAC recruitment, redundantly with Stb1. [PMID:19745812
  "Rpd3(L) is recruited to SBF genes by both Stb1 and Whi5, and Rpd3(L) binding is only lost in
  the stb1 whi5 double mutant."] [PMID:19823668 "deletion of RPD3 partially restored growth in
  the cln3Δbck2Δ strain providing further evidence for an HDAC requirement in Whi5-mediated
  transcriptional repression"]
- CDK antagonism: Cln3-Cdc28 and Pcl9-Pho85 in early/mid G1, Cln1/2-Cdc28 for the feedback
  burst. [PMID:15210111 "In late G1 phase, CDK-dependent phosphorylation dissociates Whi5 from
  SBF and drives Whi5 out of the nucleus."] [PMID:19823668 "we identify Whi5, to our knowledge,
  as the first demonstrated physiological substrate for the G1-specific Pcl9-Pho85 CDK"]
- Export is Msn5-dependent, Crm1-independent. [PMID:19520826 "Yen1, Psy4, Pds1, and Whi5 were
  constitutively localized to the nucleus in an msn5 Δ mutant, but not by treatment with
  leptomycin B (LMB), a Crm1 inhibitor"] Re-import involves Ess1 acting on phospho-Ser-Pro
  motifs in the NLS/NES. [PMID:24470217 "In ess1H164R mutant cells, the fusion protein failed
  to localize to the nucleus and cytoplasmic staining was readily apparent"]
- Size control by dilution. [PMID:26390151 "In this model, cell growth dilutes the cell cycle
  inhibitor Whi5 to drive progression through the cell cycle, whereas Cln3 concentration
  remains constant."] whi5 is among the most potent size mutants genome-wide. [PMID:12089449
  "govern critical cell size at Start, the most potent of which were Sfp1, Sch9,"]
- Caveats worth remembering: whi5 single mutants can show near-normal CLN1/2 RNA in some
  backgrounds because of Stb1 redundancy [PMID:19745812 "However, RNA measurements show nearly
  normal expression of CLN1 and CLN2 in whi5 mutants"]; Cln3 has Whi5-independent targets
  [PMID:19823669 "Although Whi5 is clearly an important target of Cln3, and an important
  regulator of SBF, it may not be the only target."]; the dilution model is contested by
  titration/network models (deep research, Ravi et al. 2024; not cached).
- Peripheral 2025 report: whi5 deletion attenuates autophagy and Atg1 phosphorylates Whi5.
  [PMID:40365021 "Rgd1 and Whi5 were validated to be potentially positive autophagy
  regulators"] Single study, hedged by the authors; treated as non-core.

### Annotation decisions and why
- GO:0000082 (8 rows, IEA/IGI/IMP): ACCEPT. Considered MODIFY to GO:2000134 (the term used for
  human RB1) but the comparator check settles it: QuickGO shows GO:2000134 on a single yeast
  gene (YGR250C), whereas SGD puts the whole Start machinery, including the repressors STB1,
  SIC1, RPD3 and SRL3/Whi7, on GO:0000082 involved_in. The obsolete terms GO:0000083 and
  GO:0071930 (regulation of transcription involved in G1/S transition) were checked and are
  not usable. Raised as a suggested question rather than overruling the convention.
- GO:0000122 (5 rows): ACCEPT; core.
- GO:0000978 IBA (sequence-specific DNA binding): MODIFY -> GO:0061629. Whi5 has no DNA-binding
  domain and reaches promoters via Swi4-Swi6; the ChIP occupancy has been read as DNA binding.
  Fallback for a DNA-occupancy row would be GO:0001012, as used for the RB1 IBA in this repo.
- GO:0003712 IBA: ACCEPT (family-level coregulator; Whi5 in its own WITH/FROM is expected).
- GO:0003714 (IDA/IGI/IMP): ACCEPT; core MF.
- GO:0005634 (5 rows): ACCEPT. GO:0005737 (4 rows): KEEP_AS_NON_CORE (exported, inactive pool).
- GO:0006357 (IBA + 2 IGI from PMID:19823668): MODIFY -> GO:0000122; the evidence is
  specifically for repression, and both node members are repressors. Kept consistent across
  evidence codes to satisfy the consistency check.
- GO:0007089 IMP (PMID:26390151): ACCEPT; Whi5 is the inhibitory node of the Start feedback
  loop and its concentration is the integrated variable.
- GO:0008361 HMP: ACCEPT; core physiological output.
- GO:0010508 IMP (PMID:40365021): KEEP_AS_NON_CORE; hedged qualifier in GOA is appropriate.
- GO:0033309 IDA: ACCEPT; GO definition of the SBF complex names Whi5 as an associated protein.
- GO:0061629 IDA: ACCEPT; the informative MF for the Whi5-SBF interaction.
- No NEW terms proposed. A chromatin (GO:0000785) location was considered for core_functions
  on the strength of promoter ChIP but dropped because no GOA row exists and the nucleus term
  plus the SBF complex term already capture the site of action.

### Identifier resolution used for WITH/FROM
SGD:S000000038 = CLN3; SGD:S000002214 = MBP1; SGD:S000005952 = PHO85; SGD:S000005253 = STB1;
SGD:S000001799 = SRL3 (Whi7); SGD:S000005609 = WHI5 itself.

### Cache status
Abstract-only: PMID:12089449, PMID:14562095, PMID:15210110, PMID:15210111. Full text: PMID:19520826,
PMID:19745812, PMID:19823668, PMID:19823669, PMID:24470217, PMID:26390151, PMID:40365021.
Not cached (cited in deep research only): Skotheim 2008 (positive feedback), Taberner 2009 and
Wagner 2009 (Msn5 export/phosphosites), Travesa 2013 (SBF specificity), Xiao 2024
(hypo/hyper-phosphorylation), Irvali 2023 (reversible Start), Su 2024 (meiotic entry), Ravi
2024 (START-BYCC model).
