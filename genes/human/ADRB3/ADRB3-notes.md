# ADRB3 (human, P13945) curation notes

**Deep research status:** falcon (Edison) deep research failed with an authentication
error on 2026-10-24; no other provider key was available. No `-deep-research-*.md`
file exists for this gene. The notes below come from the cached publications in
`publications/`, the UniProt record, Reactome summaries, and targeted web searches
(used only to find PMIDs, which were then fetched with `just fetch-pmid` and read).

## Why this gene was reviewed

Flagged by rule FRR:0010 (projects/FUNCTION_REQUIREMENT_RULES.md: "GTPase activity:
needs a P-loop or tubulin/FtsZ GTPase domain") because it carries `GO:0003925 G protein
activity` (IDA PMID:10207024; IEA GO_REF:0000120).

## Identity and structure

- Beta-3 adrenergic receptor, 408 aa, class A (rhodopsin-like) GPCR with seven TM
  helices [file:human/ADRB3/ADRB3-uniprot.txt "Belongs to the G protein-coupled receptor 1 family"].
- Domains: InterPro IPR000276 (GPCR_Rhodpsn), IPR017452 (7TM), IPR002233 (ADR_fam),
  IPR000681 (ADRB3_rcpt); Pfam PF00001 7tm_1; Gene3D 1.20.1070.10 only. No P-loop NTPase
  (Gene3D 3.40.50.300) or Ras-like GTPase domain (checked UniProt cross-references via
  REST, 2026-10-24).
- Expressed mainly in adipose tissue [file:human/ADRB3/ADRB3-uniprot.txt "Expressed mainly in adipose tissues."];
  also detrusor smooth muscle [PMID:10188996], human ventricle [PMID:9769330], vasculature
  and gallbladder [Reactome:R-HSA-9611839].

## Molecular function

- Catecholamine GPCR; couples to both Gs and Gi [file:human/ADRB3/ADRB3-uniprot.txt
  "G protein-coupled receptor for catecholamines that couples to both G(s) and G(i) proteins"].
- Human ADRB3 cloned; adrenaline/noradrenaline stimulate cAMP; atypical pharmacology,
  resistant to most beta-blockers [PMID:2570461 "Exposure of eukaryotic cells transfected
  with this gene to adrenaline or noradrenaline promotes the accumulation of adenosine
  3',5'-monophosphate"].
- Rank order norepinephrine > epinephrine (UniProt, citing PMID:10188996, 2570461, 8641219).
- Gs/Gi dual coupling demonstrated by agonist-stimulated 8-azido-GTP labeling of both
  Galpha-s and Galpha-i [PMID:10207024 "directly demonstrating that beta3AR stimulation
  results in Gi-GTP exchange"]. This is the receptor catalysing nucleotide exchange on the
  G protein alpha subunit (= the definition of GO:0004930 GPCR activity: "promotes the
  exchange of GDP for GTP on the alpha subunit of a heterotrimeric G-protein complex").
  It is NOT evidence that ADRB3 is itself a G protein.
- W64R variant is pharmacologically indistinguishable in CHO cells [PMID:8641219].

## The GO:0003925 problem (FRR:0010 lead)

- GO:0003925 "G protein activity": "A molecular function regulator that cycles between
  active GTP-bound and inactive GDP-bound states ... Intrinsic GTPase activity returns the
  G protein to its GDP..." (oaklib sqlite:obo:go, 2026-10-24); is_a GO:0003924 GTPase
  activity. That is the activity of Galpha (and small GTPases), not of a receptor.
- The IDA row (PMID:10207024, assigned_by UniProt, 2025-05-22) misreads "receptor
  stimulates GTP exchange on Gi" as "receptor has G protein activity". Correct term:
  receptor activity (GO:0015052 beta3-adrenergic receptor activity; or parent GO:0004930).
  The same paper already supports the existing GO:0015052 IDA and GO:0007193 IDA rows.
- UniProt applied the same IDA (PMID:10207024) to mouse P25962 and rat P26255 (QuickGO,
  2026-10-24). These rodent rows then fan out by ISO (RGD, GO_Central) and by Ensembl
  Compara (GO_REF:0000107) - the human IEA row's WITH/FROM is rat P26255 /
  ENSRNOP00000016907 plus ARBA:ARBA00088750.
- ARBA00088750 annotates GO:0003925; all 9 of its current condition sets require a
  Gene3D 3.40.50.300 (P-loop NTPase) FunFam (UniProt REST, 2026-10-24). ADRB3 has only
  Gene3D 1.20.1070.10, so it is unclear how the ARBA component was credited; possibly an
  earlier rule version learned from the erroneous receptor IDA rows. Flagged as a
  source defect to UniProt (CHECK).

## Signaling outputs

- Gs -> adenylyl cyclase -> cAMP (PMID:2570461; PMID:7493988 KO loses CL316,243-stimulated
  adenylate cyclase and lipolysis).
- Gi -> restrains AC and drives ERK1/2 via a PTX-sensitive, PKA-independent,
  EGFR/tyrosine-kinase dependent route [PMID:10207024 "constitutive beta3AR coupling to Gi
  proteins serves both to restrain Gs-mediated activation of adenylyl cyclase and to
  initiate additional signal transduction pathways, including the ERK1/2 MAP kinase cascade"].
- Heart: negative inotropy through eNOS/NO/cGMP [PMID:9769330 "beta3-adrenoceptor
  stimulation decreases cardiac contractility through activation of an NOS pathway"].
- Bladder: detrusor relaxation is mainly beta3 [PMID:10188996 "relaxation induced by
  adrenergic stimulation of the human detrusor is mediated mainly through beta3-AR
  activation"]; basis of mirabegron/vibegron therapy for overactive bladder
  [Reactome:R-HSA-9611839].

## Trafficking / oligomerization

- Resistant to agonist-promoted endocytosis; hetero-oligomerizes with beta2AR, blocking
  beta2AR internalization and Gi/o coupling of the heteromer [PMID:15123695 "Given that the
  beta(3)AR is resistant to agonist-promoted endocytosis"]. Supports the NOT
  receptor-mediated endocytosis row.
- Interacts with ARRDC3, an alpha-arrestin regulating beta-adrenergic responses
  [PMID:21982743 "ARRDC3 interacted directly with β-adrenergic receptors"].
- RAMP2/RAMP3 interactions from a multiplexed GPCR-RAMP screen (PMID:39083597); generic
  protein binding, no functional consequence for ADRB3 shown in the cached text.

## Physiology

- Rodent: beta3AR KO mice lack CL316,243 responses (lipolysis, energy expenditure,
  reduced food intake), have modestly increased fat [PMID:7493988]. Triple beta1/2/3 KO
  mice are obese and cold-intolerant [PMID:12387862].
- Human brown fat: contested. Cero et al. 2021 show beta3-AR silencing impairs lipolysis
  and UCP1-mediated thermogenesis in human brown/beige adipocytes [PMID:34100382 "we
  demonstrate that the β3-AR plays a critical role in regulating lipolysis, glycolysis, and
  thermogenesis"]; Blondin et al. 2020 conclude human BAT thermogenesis is beta2-driven
  [PMID:32755608 "in contrast to rodents, human BAT thermogenesis is not mediated by the
  stimulation of β3-AR"].
- Eating behaviour (IEA from rat): only a pharmacological agonist effect (reduced food
  intake with CL316,243) in mice [PMID:7493988]; treated as over-annotation.

## Decisions summary

- GO:0003925 (IDA, IEA): MODIFY -> GO:0015052 beta3-adrenergic receptor activity, with
  source_defects (UniProt; WRONG_TERM).
- Generic receptor/signaling parents (GPCR activity, adrenergic, beta-adrenergic,
  GPCR signaling, AC-modulating/activating/inhibiting GPCR signaling, membrane):
  MODIFY to the specific beta3 / adrenergic-receptor terms already carried.
- Core: GO:0015052 at plasma membrane; GO:0071880 (Gs) and GO:0071881 (Gi) signaling;
  positive regulation of ERK1/2 cascade; positive regulation of lipid catabolism and
  cold-induced thermogenesis (rodent-strong, human contested).
