# SREBF1 (human, P36956) review notes

## Deep research status

- 2026-10-18: `just deep-research human SREBF1 --provider falcon` was attempted once and failed
  with `Exception: Failed to authenticate` (Falcon/Edison key not authorised). No
  `-deep-research-*.md` file exists for this gene; these notes were compiled manually from
  cached publications (`publications/PMID_*.md`), the UniProt record and Reactome entries.

## Identity and architecture

- SREBP-1, a bHLH-ZIP transcription factor of 1147 aa, cloned from human cells as the protein that
  binds SRE-1 of the LDLR promoter [PMID:8402897 "We report the cDNA cloning of human SREBP-1, a
  protein that binds SRE-1, activates transcription, and thereby mediates the final regulatory step
  in LDL metabolism"]. SRE-1 is a direct repeat, not a canonical E-box [PMID:8402897 "Instead of an
  inverted repeat (CANNTG), the target for all known bHLH-ZIP proteins, SRE-1 contains a direct
  repeat of CAC"].
- Dual DNA specificity (E-box and SRE-1) set by an atypical tyrosine in the basic region
  [PMID:7739539 "we demonstrate that ADD1/SREBP1 has dual DNA sequence specificity, binding to both
  an E-box motif (ATCACGTGA) and a non-E-box sequence previously shown to be important in
  cholesterol metabolism, sterol regulatory element 1 (SRE-1; ATCACCCCAC)"]. Study used rat ADD1;
  human data on the same Tyr->Arg switch in [PMID:12177166].
- UniProt topology: N-terminal transactivation + bHLH-ZIP (bHLH 323-373) cytosolic domain 1-487,
  two TM helices (488-508, 548-568) with a short luminal loop (S1P site 530-531), C-terminal
  regulatory domain 569-1147 that binds SCAP. S2P site 490-491. Processed chain PRO_0000314029
  (1-490) is the nuclear form.

## Activation pathway (SREBP signaling)

- Precursor in ER/nuclear envelope; cleaved in sterol-depleted cells to a soluble nuclear
  fragment [PMID:8156598 "is synthesized as a 125 kd precursor that is attached to the nuclear
  envelope and endoplasmic reticulum"; "In sterol-depleted cells, the membrane-bound precursor is
  cleaved to generate a soluble NH2-terminal fragment (apparent molecular mass, 68 kd) that
  translocates to the nucleus"].
- Two sequential cleavages (shown with SREBP-2) [PMID:8674110 "The first, regulated by sterols,
  occurs in the lumenal loop. The second, not regulated by sterols, occurs within the first
  transmembrane domain."].
- SCAP escort and INSIG retention [PMID:12202038 "In sterol-depleted cells, SCAP escorts SREBPs
  from ER to Golgi for proteolytic processing, thereby allowing SREBPs to stimulate cholesterol
  synthesis"]; INSIG-1/2 act the same on SREBP-1a [PMID:12242332 "Insig-1 and -2 had the same
  effect on the processing of SREBP-1a that they had on SREBP-2"].
- Human genetics: IFAP2 mutations at residues 527/528/530 block S1P cleavage [PMID:32497488 "In
  vitro investigation of SREBP1 variants demonstrated impaired S1P cleavage, which prohibited
  nuclear translocation of the transcriptionally active form of SREBP1"].
- Nuclear form turns over fast via ubiquitin-proteasome [PMID:11477106 "The active SREBPs
  translocate to the nucleus, induce the expression of responsive genes, and are degraded very
  rapidly"].
- PCK1-INSIG phosphorylation releases SCAP-SREBP in HCC cells [PMID:32322062].

## Isoforms

- 1a vs 1c differ in exon 1 (acidic activation domain) [PMID:9062341 "SREBP-1a and -1c are
  alternate transcripts from a single gene that differ in the first exon, which encodes part of an
  acidic activation domain"].
- 1a activates cholesterol + fatty acid genes; 1c much weaker and lipogenic-biased
  [PMID:9062341 "The mRNAs for the LDL receptor and several cholesterol biosynthetic enzymes were
  elevated in SREBP-la transgenic mice, but not in 1c transgenic mice"]; human HepG2 reporters
  [PMID:12177166 "cholesterogenic genes containing classic SREs in their promoters are strongly and
  efficiently activated by both SREBP-1a and SREBP-2, but not by SREBP-1c"].
- Review [PMID:11994399 "SREBP-1a is a potent activator of all SREBP-responsive genes, including
  those that mediate the synthesis of cholesterol, fatty acids, and triglycerides."; "SREBP-1c
  preferentially enhances transcription of genes required for fatty acid synthesis but not
  cholesterol synthesis."].
- 1c is transcriptionally induced by LXR and insulin, repressed by glucagon/cAMP and PUFA
  [PMID:11994399 "Three factors selectively regulate the transcription of SREBP-1c: liver
  X-activated receptors (LXRs), insulin, and glucagon."; PMID:11090130]. Insulin induction in
  adipocytes [PMID:9421459].
- SREBP-1aDelta / 1cDelta (P36956-5/-6) are truncated at 470 and lack the membrane anchor; nuclear
  and constitutively active (UniProt; PMID:18267114, not cached).

## GOA observations

- 128 rows. Many IEA "response to X" rows from rat Srebf1 (Ensembl Compara) reflect regulation of
  Srebf1 *expression* by nutrients/hormones/xenobiotics, not participation of the protein in the
  response. Marked as over-annotations except insulin (SREBP-1c mediates insulin's lipogenic
  transcription) kept non-core.
- GO:0004879 nuclear receptor activity (IDA, PMID:23610160) is categorically wrong for a bHLH-ZIP
  protein; the nuclear receptor in that paper is SF1 (NR5A1). The derived IEA GO:0030522 follows.
- GO:0090209 negative regulation of triglyceride metabolic process (PMID:28483554) has the wrong
  sign for SREBF1: the abstract shows SREBF1 induction drives steatosis and miR-192 suppresses it
  by suppressing SREBF1.
- Mitophagy rows (PMID:24912190) come from an RNAi screen; the block was bypassed by exogenous
  lipids, so the effect is indirect through lipogenesis.
- Process terms like cholesterol metabolic process / lipid biosynthetic process are modified to
  the positive-regulation terms, since SREBF1 is a transcriptional regulator and not an enzyme.
- GO-CAM gocams/6205c24300000880 models SREBF1 as GO:0000981 part_of GO:0045542; the review
  accepts both.
