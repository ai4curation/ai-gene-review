# PCSK1N (ProSAAS / Q9UHG2) — review notes

This review is in response to upstream curator question
[geneontology/go-annotation#6407](https://github.com/geneontology/go-annotation/issues/6407)
("term suitable to describe PCSK1N (ProSAAS)") asking which GO term best captures
ProSAAS's emerging "chaperone activity".

## Gene identity

- HGNC symbol: **PCSK1N** (HGNC:17301)
- UniProt: **Q9UHG2**, human ProSAAS, 260 aa precursor; signal peptide 1–33; chain
  ProSAAS 34–260
- Gene names / aliases: ProSAAS, pro-SAAS, Proprotein convertase subtilisin/kexin type 1
  inhibitor
- Family: PANTHER PTHR15531 (PROSAAS), Pfam PF07259, InterPro IPR010832
- Closest functional/structural homolog in mammals: **SCG5/7B2** (similar small
  neuroendocrine secretory protein with both convertase-regulatory and anti-aggregant
  chaperone activities) [PMID:24102330].
- Tissue specificity: brain and pancreas; neurons (not glia); pituitary, adrenal,
  pancreas; widespread in CNS [UniProt; PMID:10632593; PMID:24102330].

## Curated proteolytic processing

ProSAAS is processed at paired-basic sites in the regulated secretory pathway
(Golgi/TGN, secretory granules) into multiple bioactive peptides
[UniProt; PMID:10632593; PMID:11435430; PMID:12914799]:

- KEP (34–40)
- Big SAAS (34–59) → Little SAAS (42–59)
- ProSAAS(1–180) [≈21 kDa intermediate; major secreted form]
- Big PEN-LEN (221–260) — contains the C-terminal **convertase-inhibitory domain**
  - PEN (221–242) — endogenous **GPR83** ligand (food intake) [UniProt: by similarity]
  - Big LEN (245–260) → Little LEN (245–254) — endogenous **GPR171** ligand
    (feeding) [UniProt: by similarity]

The motif **L-L-R-V-K-R** (residues 239–244) within the C-terminal inhibitory
domain is necessary and sufficient for PCSK1 inhibition; alanine substitutions of
K243 or R244 abolish inhibition [PMID:11435430].

## Function 1 — Endogenous PCSK1 (PC1/3) inhibitor

The original characterization showed that:

- "Purified proSAAS inhibits prohormone convertase 1 activity with an IC50 of 590 nM
  but does not inhibit prohormone convertase 2"
  [PMID:10632593, "Purified proSAAS inhibits prohormone convertase 1 activity with
  an IC(50) of 590 n m but does not inhibit prohormone convertase 2"]
- "Overexpression of proSAAS in the AtT-20 cells substantially reduces the rate of
  processing of the endogenous prohormone proopiomelanocortin"
  [PMID:10632593, "Overexpression of proSAAS in the AtT-20 cells substantially
  reduces the rate of processing of the endogenous prohormone proopiomelanocortin"]
- Mutagenesis maps the inhibitory determinants to the LLRVKR motif:
  "K->A: Abolishes inhibition of PCSK1" / "R->A: Abolishes inhibition of PCSK1"
  for K243 and R244 [PMID:11435430, UniProt MUTAGEN annotations]
- ProSAAS and Big PEN-LEN, but not the further-processed peptides, reduce PCSK1
  activity in the ER and Golgi [UniProt FUNCTION: by similarity, citing Q9QXV0]

PCSK1/PC1/3 is a serine endopeptidase (subtilisin-like, MEROPS S8). Therefore the
appropriate molecular function for the C-terminal inhibitory peptide / Big PEN-LEN
is **GO:0004867 serine-type endopeptidase inhibitor activity** (already on the
record, IEA), with the parent **GO:0004866 endopeptidase inhibitor activity**
(already there as IBA/TAS) acceptable as a less specific synonym. The biological
process is **GO:0010955 negative regulation of protein processing** and/or
**GO:0060570 negative regulation of peptide hormone processing**.

## Function 2 — Anti-aggregant / extracellular chaperone activity (the topic of issue #6407)

A coherent body of work, primarily from the Lindberg laboratory, establishes that
full-length ProSAAS or its 21-kDa N-terminal fragment (residues ~1–180) acts as a
secreted brain chaperone that **prevents aggregation of multiple amyloidogenic
client proteins**, but does **not** refold proteins and does **not** disaggregate
preformed fibrils.

### β-amyloid (Aβ1–42)

Hoshino et al. 2014 [PMID:24102330]:

- "We here describe a novel anti-aggregant chaperone function for the
  neuroendocrine protein proSAAS"
  [PMID:24102330, "We here describe a novel anti-aggregant chaperone function for
  the neuroendocrine protein proSAAS"]
- "In vitro, proSAAS efficiently prevented the fibrillation of Aβ(1-42) at molar
  ratios of 1 : 10, and this anti-aggregation effect was dose dependent. Structure-
  function studies showed that residues 97-180 were sufficient for the anti-
  aggregation function against Aβ"
  [PMID:24102330, "In vitro, proSAAS efficiently prevented the fibrillation of
  Aβ(1-42) at molar ratios of 1 : 10..."]
- "proSAAS immunoreactivity was highly colocalized with amyloid pathology…
  Immunoreactive proSAAS co-immunoprecipitated with Aβ immunoreactivity in lysates
  from APdE9 mouse brains"
  [PMID:24102330, "proSAAS immunoreactivity was highly colocalized with amyloid
  pathology"]
- "inclusion of recombinant proSAAS in the medium of Neuro2a cells, as well as
  lentiviral-mediated proSAAS over-expression, blocked the neurocytotoxic effect
  of Aβ(1-42) in Neuro2a cells"
  [PMID:24102330, "blocked the neurocytotoxic effect of Aβ(1-42) in Neuro2a cells"]

This evidence supports MF **GO:0001540 amyloid-beta binding** and
**GO:0051787 misfolded protein binding**, plus BP **GO:1905907 negative
regulation of amyloid fibril formation** (and more specifically
**GO:1902430 negative regulation of amyloid-beta formation** is *not* appropriate
because GO:1902430's parent describes the secretase-driven *generation* of Aβ
peptide from APP, not aggregation; Hoshino et al. measured fibrillation, not APP
processing). MF **GO:0044183 protein folding chaperone** is **not** appropriate
because the curators (Hoshino et al., Jarvela et al.) explicitly state it does
not refold; the analogous CLU (clusterin) review in this repo also annotates
GO:0051787 misfolded protein binding rather than GO:0044183 for this kind of
"holdase-like" activity.

### α-synuclein (aSyn)

Jarvela et al. 2016 [PMID:27457957]:

- "proSAAS, widely expressed in neurons throughout the brain, is associated with
  aggregated synuclein deposits in the substantia nigra of patients with Parkinson's
  disease"
  [PMID:27457957, "associated with aggregated synuclein deposits in the substantia
  nigra of patients with Parkinson's disease"]
- "Recombinant proSAAS potently inhibits the fibrillation of α-synuclein in an in
  vitro assay; residues 158-180, containing a largely conserved element, are
  critical to this bioactivity"
  [PMID:27457957, "Recombinant proSAAS potently inhibits the fibrillation of
  α-synuclein in an in vitro assay"]
- "proSAAS-encoding lentivirus blocks α-synuclein-induced cytotoxicity in primary
  cultures of nigral dopaminergic neurons, and recombinant proSAAS blocks
  α-synuclein-induced cytotoxicity in SH-SY5Y cells"
  [PMID:27457957, "proSAAS-encoding lentivirus blocks α-synuclein-induced
  cytotoxicity in primary cultures of nigral dopaminergic neurons"]

Lindberg et al. 2022, in vivo extension [PMID:35527562]:

- "Coinjection of proSAAS-encoding lentivirus profoundly reduced the motor
  asymmetry caused by unilateral nigral AAV-mediated human aSyn overexpression.
  This was accompanied by significant amelioration of the human aSyn-induced loss
  of both nigral TH-positive cells and striatal TH-positive terminals"
  [PMID:35527562, "Coinjection of proSAAS-encoding lentivirus profoundly reduced
  the motor asymmetry…"]
- "Following vagal administration of human aSyn-encoding AAV, the number of human
  aSyn-positive neurites in the pons and caudal midbrain was considerably reduced
  in mice coinjected with proSAAS-, but not GFP-encoding AAV, supporting proSAAS-
  mediated blockade of transsynaptic aSyn transmission"
  [PMID:35527562, "supporting proSAAS-mediated blockade of transsynaptic aSyn
  transmission"]

This supports MF **GO:0051787 misfolded protein binding** (binding aSyn
aggregates) and BP **GO:1905907 negative regulation of amyloid fibril formation**
in vivo, plus the neuroprotective phenotype (process: protection against
neurodegeneration, captured by parent terms below).

### TDP-43 — caveats about cytoplasmic activity

Peinado et al. 2022 [PMID:35549000]:

- "We previously demonstrated that proSAAS, a small secreted neuronal protein,
  exhibits potent chaperone activity against protein aggregation in vitro and
  blocks the cytotoxic effects of amyloid and synuclein oligomers in cell culture
  systems"
  [PMID:35549000, "exhibits potent chaperone activity against protein aggregation
  in vitro"]
- "expression of proSAAS within the cytoplasm generates dense, membraneless 2 μm
  proSAAS spheres which progressively fuse to form larger spheres, suggesting
  liquid droplet-like properties"
  [PMID:35549000, "expression of proSAAS within the cytoplasm generates dense,
  membraneless 2 μm proSAAS spheres"]
- "we demonstrate that proSAAS expression results in cytoprotection against
  full-length TDP-43 toxicity in yeast. We conclude that proSAAS can act as a
  functional holdase for TDP-43 via this phase-separation property"
  [PMID:35549000, "proSAAS can act as a functional holdase for TDP-43 via this
  phase-separation property"]

**Important caveat:** the TDP-43-encapsulating sphere phenotype was obtained by
forcing **non-physiological cytoplasmic** expression of proSAAS (signal peptide
removed). ProSAAS is normally a secreted protein that resides in the secretory
pathway (TGN, secretory granules) and the extracellular space. Therefore the
TDP-43 sphere data should not be used to support a *cytoplasmic* localization
annotation, but it does corroborate the protein's intrinsic capacity to bind
prion-like / aggregation-prone clients. The "holdase" characterization in this
paper is the strongest single piece of textual support for using
**GO:0140309 unfolded protein holdase activity** as a chaperone MF; however,
GO:0140309's definition emphasizes a *carrier* function ("escorts it to an
acceptor molecule or to a specific location"), which is not strictly demonstrated
for proSAAS in vivo.

### Disaggregation: what proSAAS does NOT do

The upstream issue notes "Cannot disaggregate preformed fibrils (27457957)" and
this is consistent with the broader literature: proSAAS prevents *initial*
aggregation but does not disassemble preformed fibrils, and it does not refold
denatured proteins. Therefore terms in the **disaggregase** branch (e.g. ATPase
disaggregase activity) and **protein folding chaperone** GO:0044183 are **not**
appropriate.

### Summary of recommended chaperone-related terms

Recommended additions / new annotations for the chaperone activity:

| Aspect | GO term | Rationale |
| --- | --- | --- |
| MF | GO:0051787 misfolded protein binding | Binds Aβ, aSyn, TDP-43 aggregates |
| MF | GO:0001540 amyloid-beta binding | Direct Aβ co-IP and binding [PMID:24102330] |
| MF | GO:0140309 unfolded protein holdase activity | Used by Lindberg 2022 for TDP-43; partial fit |
| BP | GO:1905907 negative regulation of amyloid fibril formation | In vitro and in vivo Aβ + aSyn fibrillation block |
| BP | GO:0050821 protein stabilization | Holdase-like maintenance of soluble client state |

GO:0044183 (protein folding chaperone) is **not** recommended — proSAAS does not
refold clients. GO:1902430 (negative regulation of amyloid-beta *formation*) is
**not** recommended — that term is for APP cleavage, not Aβ aggregation.

## Function 3 — Bioactive peptide ligand activity (after processing)

Big LEN and PEN, generated by paired-basic processing of proSAAS, are
GPCR ligands [UniProt FUNCTION: by similarity, Q9QXV0]:

- Big LEN → endogenous ligand for **GPR171**, regulates feeding
- PEN → endogenous ligand for **GPR83**, regulates feeding

This supports the existing **GO:0005102 signaling receptor binding** annotation
(TAS, PMID:10632593), although the literature actually supporting GPR171/GPR83
binding is more recent (e.g. Wardman et al., Gomes et al.) than the cited
PMID:10632593, which itself does not demonstrate receptor binding. The annotation
is therefore better re-evidenced. The peptide-receptor interaction can also
support **GO:0007218 neuropeptide signaling pathway** (already keyword-derived
on record).

## Function 4 — Disease association markers (not function per se)

- Big SAAS / Little SAAS N-terminal fragments deposit with cytoplasmic tau
  inclusions in Pick's disease, Alzheimer's disease, and amyotrophic lateral
  sclerosis-parkinsonism/dementia complex of Guam [UniProt; PMID:12914799;
  PMID:14746899]. This is a localization context rather than a discrete cellular
  function, and should NOT be turned into a localization annotation (the deposit
  is pathological).
- ProSAAS is a recurrent CSF biomarker in dementia [reviewed in PMID:35549000].

## Existing annotations — proposed actions

| GOA term | Evidence | Proposed action | Rationale |
| --- | --- | --- | --- |
| GO:0004866 endopeptidase inhibitor activity | IBA, IEA, TAS | KEEP_AS_NON_CORE / MODIFY → GO:0004867 | Parent of more-specific GO:0004867 (which is also already on record as IEA). PCSK1 is a serine endopeptidase (subtilisin) so the specific term is preferable. |
| GO:0004867 serine-type endopeptidase inhibitor activity | IEA | ACCEPT | Mutagenesis maps inhibitory determinants to LLRVKR (PMID:11435430); appropriate for the C-terminal inhibitory peptide. |
| GO:0005102 signaling receptor binding | TAS (PMID:10632593) | KEEP_AS_NON_CORE | Refers to processed peptides PEN/Big LEN binding GPR83/GPR171. Cited PMID does not directly demonstrate this; better refs exist (Wardman, Gomes). Not the dominant/core function. |
| GO:0005576 extracellular region | IEA, ISS, TAS | ACCEPT | Secreted; well-established. |
| GO:0005794 Golgi apparatus | IEA | ACCEPT | True (parent of TGN). |
| GO:0005802 trans-Golgi network | IEA | ACCEPT | More specific Golgi sublocation; consistent with regulated secretion / processing site. |
| GO:0030141 secretory granule | IEA | ACCEPT | Stored in regulated secretory granules in neurons / endocrine cells [PMID:10632593, PMID:24102330]. |

## Suggested new (proposed) annotations

- MF GO:0051787 misfolded protein binding (extracellular anti-aggregant chaperone activity)
- MF GO:0001540 amyloid-beta binding (direct Aβ binding/co-IP)
- BP GO:1905907 negative regulation of amyloid fibril formation
- BP GO:0050821 protein stabilization (parent for chaperone-mediated client stabilization)
- (Optionally) MF GO:0140309 unfolded protein holdase activity — debatable; the
  Lindberg group calls proSAAS a "holdase" [PMID:35549000] but the GO definition
  emphasizes carrier/delivery, which is not formally demonstrated for proSAAS.

## Open questions for upstream curators (issue #6407)

1. Should "anti-aggregant" chaperones that prevent fibrillation but do not refold
   be annotated to **GO:0051787 misfolded protein binding** + BP GO:1905907, or
   to **GO:0140309 unfolded protein holdase activity** when there is no documented
   carrier-to-acceptor handoff? A precedent in this repository is CLU/clusterin,
   which uses the GO:0051787 + GO:1905907 + GO:0050821 combination for a closely
   analogous extracellular anti-aggregant chaperone activity.
2. Is there an MF term capturing "holdase-like activity that prevents amyloid
   fibrillation" that does not require either folding (GO:0044183) or carrier
   delivery (GO:0140309)? If not, would a new term be warranted? (See similar
   discussion in the SCG5/7B2 literature — Lindberg lab uses "anti-aggregant
   chaperone" language for both 7B2 and ProSAAS.)
3. The TDP-43 sphere data [PMID:35549000] is from forced cytoplasmic expression
   and may not reflect physiological ProSAAS function. Should this evidence be
   limited to "demonstrates capacity for prion-like client binding" rather than
   used to support a normal cellular MF?

## Relevant PMIDs

- PMID:10632593 — Identification and characterization of proSAAS (PCSK1 inhibitor; tissue distribution; secretion)
- PMID:11435430 — Mutagenesis of LLRVKR motif sufficient for PCSK1 inhibition
- PMID:12914799 — N-terminal proSAAS fragment in tau deposits (Pick's disease)
- PMID:14746899 — proSAAS in tau inclusions of AD and Guam
- PMID:24102330 — Anti-aggregant chaperone for Aβ
- PMID:27457957 — Anti-aggregant chaperone for α-synuclein (in vitro + neuronal cytoprotection)
- PMID:35527562 — In vivo neuroprotection in PD models; blocks transsynaptic aSyn spread
- PMID:35549000 — Holdase for TDP-43 via cytoplasmic phase separation; sphere formation
