# Map2k6 (rat) - manual literature synthesis

No deep-research provider was available for this session. This synthesis was written by the
reviewer from cached publications (`publications/PMID_*.md`), the rat TrEMBL entry
A0ABK0M3C5 and the human Swiss-Prot entry P52564 (MAP2K6), with inline provenance.

## Identity

- Rat Map2k6 (RGD:620666), UniProtKB A0ABK0M3C5 (TrEMBL, Ensembl ENSRNOP00000112695.1),
  335 aa; one residue longer at the N-terminus than human MAP2K6 (334 aa), otherwise very
  close in sequence. Protein kinase domain 54-315, ATP-binding Lys83, catalytic Asp180
  [file:rat/Map2k6/Map2k6-uniprot.txt "ACT_SITE        180"].
- Activation-loop phosphorylation sites map to Ser208/Thr212 in this entry (motif
  DSVAKTIDAG), corresponding to human Ser207/Thr211 [PMID:19141286 "we mutated the two
  phosphorylation sites of MEK6, Ser207 and Thr211, to aspartic acid"].
- Family: STE group, MAP kinase kinase subfamily; CDD cd06617 PKc_MKK3_6; PANTHER
  PTHR48013:SF12 (dual specificity MAPKK 6).

## Core activity: MAP kinase kinase of the p38 cascade

- Human MKK6 is a dual-specificity kinase that phosphorylates the Thr and Tyr of p38 MAPKs
  [file:human/MAP2K6/MAP2K6-uniprot.txt "catalyzes the concomitant phosphorylation of a threonine
  and a tyrosine residue in the MAP kinases p38 MAPK11, MAPK12, MAPK13"].
- Activated MKK3 and MKK6 selectively increase p38 activity in cells [PMID:8622669 "Expression
  of activated MKK3 and MKK6 in cultured cells caused a selective increase in p38 MAP kinase
  activity"]. MKK3 and MKK6 are p38-specific, unlike MKK4 [PMID:10097111 "The MKK3 and MKK6
  protein kinases are specific for p38 MAP kinase"].
- Rat-specific: Harding et al. (full text, PMC2954285) immunoprecipitated endogenous MKK6 from
  isolated perfused rat hearts and neonatal cardiomyocytes and assayed it in a coupled
  GST-p38/GST-ATF2 immune-complex kinase assay [PMID:20550965 "1 μg GST-p38 and 4 μg GST-ATF2
  for MKK3 and MKK6"]; controls lacked activity [PMID:20550965 "No MKK activity was detected in
  immunoprecipitates using control antibody, or in assays lacking GST-MAPK or substrate"].
  MKK6 was activated late in global ischaemia [PMID:20550965 "MKK6 was also activated
  significantly by ischaemia but not until later"] and by sorbitol [PMID:20550965 "robust
  activation of all MKK isoforms assayed"]; ASK1 couples preferentially to MKK6 [PMID:20550965
  "activation of ASK1 leads to preferential activation of MKK6 and consequent activation of p38"].

## Upstream activators and binding

- TAO2 associates with MEK3/MEK6 and activates them [PMID:11279118 "endogenous TAO2
  specifically associates with MEK3 and MEK6"]. UniProt (human) lists MAP3K partners via the
  DVD domain and p38 substrates via the D domain.
- Unphosphorylated MKK6 forms an autoinhibitory dimer [PMID:19141286 "The dimer may also serve
  the function in unphosphorylated MEK6 of preventing activation loop phosphorylation by
  inappropriate kinases"].

## Localisation

- MKK3/MKK6 present in both nucleus and cytoplasm [PMID:9768359 "The p38 activators MKK3 and
  MKK6 were present in both the nucleus and the cytoplasm"]. No rat-specific localisation data
  found.

## Physiological contexts (downstream of p38)

- Rat cardiomyocytes: dominant-negative MKK6 blocks IL-1beta-induced COX-2 expression and PGE2
  release; wild-type or active MKK6 is sufficient for COX-2 induction [PMID:12649265].
- Rat FaO hepatoma: DN MKK6 suppresses TGF-beta1-induced cytochrome c release and apoptosis
  [PMID:12029621].
- Rat corpus luteum: MKK6 and p38 chronically activated during luteal maturation
  [PMID:11328854] (correlative).
- SHRSP rat aorta: MKK6 protein levels are elevated and lowered by amlodipine/enalapril
  [PMID:16755153] (correlative; the paper's conclusions concern MEK-ERK).
- Mouse: Mkk3 or Mkk6 deletion reduces bone mass from defective osteoblast differentiation
  [PMID:20551513]; Mkk6 loss increases UCP1 and WAT browning [PMID:29021624]; cardiac
  constitutively active MKK6bE depresses contractility [PMID:11593045] (gain of function);
  JIP4-driven p38 activation requires MKK3/MKK6 [PMID:15767678].

## Interpretation

The gene's one established molecular function is MAP kinase kinase activity directed at p38
MAPKs, within the stress-activated p38 cascade. Tissue phenotypes (bone, adipose browning,
COX-2/prostaglandin, apoptosis, cardiac remodelling) are downstream outcomes of p38 signalling
rather than activities of MKK6 itself.
