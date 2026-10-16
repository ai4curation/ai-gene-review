# SKP1 (human, UniProt P63208) — curation notes

Working journal for the GO annotation review in `SKP1-ai-review.yaml`. Sources: `SKP1-uniprot.txt`,
`SKP1-goa.tsv`, `SKP1-deep-research-falcon.md`, cached publications in `publications/`, cached
Reactome reactions in `reactome/`, and the cached GO-CAM models listed in `gocams/index.tsv`.

## 1. Identity, and the one thing to keep straight

P63208 is **SKP1**, the small adaptor subunit of SCF ligases — *not* SKP2, which is one of the ~69
F-box substrate receptors that dock onto it. The deep-research report flags this explicitly, and it
matters because a large fraction of the GOA rows cite papers whose titles name a receptor
(SKP2, FBXW7, beta-TrCP, cyclin F, FBXO7…) rather than SKP1
[file:human/SKP1/SKP1-deep-research-falcon.md "SKP1 is not **SKP2**. SKP2 is an F-box substrate receptor that binds SKP1 in the SCF^SKP2 complex"].
Aliases in the record: p19skp1, OCP2/OCP-II (organ of Corti protein 2), TCEB1L, SKP1A.

## 2. What SKP1 actually does

Two contacts, no chemistry:

- N-terminal BTB/POZ-like region → the first cullin repeat at the CUL1 N-terminus.
- Adaptable C-terminal helices → the ~40-residue F-box motif of a substrate receptor.

[file:human/SKP1/SKP1-deep-research-falcon.md "Human SKP1 contains an N-terminal BTB/POZ-like region participating in CUL1 association and a helical, conformationally adaptable C-terminal region that binds F-box domains."]
[file:human/SKP1/SKP1-uniprot.txt "In the SCF complex, serves as an adapter that links the F-box protein to CUL1."]

The SCF crystal structure is the anchor: CUL1's stalk "binds the Skp1-F boxSkp2 protein
substrate-recognition complex at its tip"
[PMID:11961546 "The long stalk, which consists of three repeats of a novel five-helix motif, binds the Skp1-F boxSkp2 protein substrate-recognition complex at its tip"],
and the beta-TrCP1-SKP1-beta-catenin structure shows the substrate being read by the **receptor's**
WD40 domain
[PMID:12820959 "The 3.0 A structure of a beta-TrCP1-Skp1-beta-catenin complex reveals the basis of substrate recognition by the beta-TrCP1 WD40 domain"].

SKP1 is catalytically inert and has no substrate specificity of its own
[file:human/SKP1/SKP1-deep-research-falcon.md "SKP1 provides structural connectivity rather than catalytic chemistry. It has no established intrinsic enzymatic reaction, catalytic substrate, or transporter function."]
[file:human/SKP1/SKP1-deep-research-falcon.md "SKP1 therefore supports a large repertoire of SCF complexes but does not possess a single meaningful “substrate specificity” of its own."].
Its flexibility is what lets one adaptor accept structurally diverse F-box domains (NMR, PDB 5XYL;
mobile loop 1 35–49, loop 2 67–84, partly formed H7, disordered C-tail)
[file:human/SKP1/SKP1-deep-research-falcon.md "This mixture of a stable core and mobile interaction surfaces provides a plausible physical basis for accommodating many structurally distinct F-box domains."].

Beyond canonical SCF, SKP1 sits in:

- **CRL7(FBXW8)** — SKP1-FBXW8 docks onto CUL7 and links it to a neddylated CUL1-RBX1 catalytic module
  [PMID:35982156 "our data indicate that CRL7 serves as a substrate receptor linked via SKP1-FBXW8 to a neddylated CUL1-RBX1 catalytic module mediating ubiquitination"].
- **CUL1-RING(FBXL4)**, mitochondrial, degrading BNIP3/BNIP3L
  [file:human/SKP1/SKP1-uniprot.txt "Also acts as a core component of the Cul1- RING(FBXL4) ubiquitin ligase complex, which mediates the ubiquitination and subsequent proteasomal degradation of BNIP3 and BNI3L"].
- **MYCBP2/PAM-FBXO45-SKP1**, with *no cullin at all*, where SKP1 does more than scaffold
  [PMID:29997255 "forms a noncanonical Skp/Cullin/F-box (SCF) complex that contains the F-box protein FBXO45 and SKP1 but lacks CUL1"]
  [PMID:29997255 "we demonstrate a novel role for SKP1 as an auxiliary component of the target recognition module that enhances binding of FBXO45 to NMNAT2"].
- **PRC1.1 / BCOR** variant Polycomb complexes, via the F-box/JmjC protein KDM2B/FBXL10
  [file:human/SKP1/SKP1-uniprot.txt "The KDM2B-SKP1 heterodimeric complex interacts with the PCGF1-BCORL heterodimeric complex to form a homotetrameric polycomb repression complex 1 (PRC1.1)"]
  [PMID:16943429 "the BCOR complex contains components of a second ubiquitin E3 ligase, namely, SKP1 and FBXL10 (JHDM1B)"].

A genuinely **non-degradative** activity, which I treated as a third core function: the nuclear
export signal of FBXO7 lies *inside* its F-box, so SKP1 and CRM1 compete for the same surface
[PMID:21378169 "the NES was embedded within the F-box domain, which is bound by Skp1 and enables the F-box protein to form part of an E3 ubiquitin ligase"]
[PMID:21378169 "Skp1 binding prevented Fbxo7 from contacting CRM1"]
[PMID:21378169 "We propose that this competitive binding allowed Fbxo7 to accumulate within the nucleus starting at the G1/S transition"].
More than ten other F-box proteins share this NES placement, so it is not a one-receptor quirk, and
SKP1 itself is the entity doing the occluding — participation, not mere necessity.

## 3. Localization

Nucleus/nucleoplasm, cytosol/cytoplasm, chromatin (via PRC1.1) and centrosome
[file:human/SKP1/SKP1-deep-research-falcon.md "SKP1 is intracellular and has been detected in the **cytoplasm, nucleus, and centrosome**, fitting the locations of its many SCF partners and substrates."].
The centrosome data are strong quantitatively
[file:human/SKP1/SKP1-deep-research-falcon.md "approximately **97% of purified centriole doublets** stained for SKP1, centrosome preparations were estimated to contain at least approximately **500 SKP1 molecules per centrosome**"]
[file:human/SKP1/SKP1-deep-research-falcon.md "Anti-Skp1 or anti-Cul1 antibodies inhibited centriole separation in a cell-free system"],
but the targeting is receptor-driven (cyclin F, FBXW5, FBXL13), so I kept centrosome **non-core**,
matching how RBX1 was handled on the same reference (PMID:20596027).

## 4. Decisions and why

**The 265 bare `GO:0005515` IPI rows** (already adjudicated before I picked this up; I spot-checked a
sample and left them intact). Repository policy: resolve to an informative MF where the evidence
supports one, otherwise REMOVE as uninformative without asserting the interaction is false. The
prior reviewer's split is consistent — F-box partners from focused SCF-assembly/substrate studies
→ MODIFY to GO:1990444 + GO:0160072; CUL1 → GO:0097602; high-throughput interactome hits
(BioPlex 3.0, HuRI, HI-II-14, PcG complexome) → REMOVE. All 195 REMOVEs in the file are
`GO:0005515` rows, and each carries the "removal records that the generic term is uninformative,
not that the interaction is false" wording.

**Core MF: GO:0160072, not GO:1990756.** SKP1 carries three overlapping MF rows from the *same*
beta-TrCP1-SKP1-beta-catenin structure: scaffold activity (GO:0160072), ligase-substrate adaptor
activity (GO:1990756) and ligase activator activity (GO:1990757). The term definitions separate
cleanly: GO:1990756 is "brings together a ubiquitin-like ligase and **its substrate**", which is what
the *F-box protein* does (SKP2 and BTRC both carry it — see `genes/human/SKP2`), while GO:0160072 is
"brings together an ubiquitin ligase and an ubiquitin **ligase-substrate adaptor**", which is exactly
SKP1's position. So I ACCEPTed GO:0160072 and MODIFY'd both GO:1990756 and GO:1990757 to it. The
"activator" framing does fit the cullin-less PAM/FBXO45 case, and that is separately and correctly
annotated as GO:0140677 — which the GO-CAM model `gomodel:63c0ac2b00000506` also uses for the SKP1
node, so I ACCEPTed it rather than folding it into the scaffold term.

**GO:0008013 beta-catenin binding (IDA) → MARK_AS_OVER_ANNOTATED.** SKP1 is in a ternary complex with
beta-catenin, but the specific contact is beta-TrCP1's WD40 domain reading the DpSGphiXpS degron.
Not REMOVE: the curator saw a real structure containing both proteins, and SKP1's informative
functions (GO:1990444, GO:0160072) are already annotated.

**GO:0019904 protein domain specific binding (IPI, with mouse Cacybp/SIP Q9CXW3) → MODIFY to
GO:0160072.** Verified the partner via UniProt REST: Q9CXW3 = mouse Cacybp (calcyclin-binding
protein = SIP). The paper maps the contact to SIP's CS domain
[PMID:15996101 "Skp1 engages the SIP CS domain exclusively through weak interactions that are not coupled to the other domains"]
and describes SKP1 doing its usual job in a non-cullin assembly
[PMID:15996101 "The principal role of the modular structure of SIP appears to be in bringing these two proteins into physical proximity and orchestrating the orientation required for polyubiquitination of beta-catenin in the intact SCF-type complex"].

**Ortholog-transfer rows (GO:0000775 centromeric region, GO:0007129 meiotic pairing) →
KEEP_AS_NON_CORE, not REMOVE.** Checked the source via QuickGO: mouse Skp1 (Q9WTX5) carries
GO:0000775 by **IDA** and GO:0007129 by **IMP**, both from PMID:39244596, a mouse meiosis study.
These are real experimental annotations on a near-identical ortholog, so the transfer is not mine to
overrule; but a germline/stage-restricted context is not the core adaptor function. Same logic for
GO:0005813 centrosome IEA (mouse IDA source, PMID:10485847).

**IBA rows (GO:0005634, GO:0005737, GO:0031146, GO:0097602) → ACCEPT.** All sit at
PANTHER:PTN000126179 with descendants across fly, mouse, fission yeast, budding yeast, Dictyostelium
and Arabidopsis. Human P63208 appears in its own WITH/FROM on three of them — that is the marker
that experimental grounding exists on the target itself, and is explicitly *not* to be called
circular. No target-specific evidence of loss or divergence exists for SKP1, so the node placement
stands.

**Receptor-driven process rows.** The recurring judgement on this gene: does the process belong to
the adaptor or to whichever F-box protein it is carrying? Kept as **non-core** where the
SKP1-containing ligase demonstrably acts (iron homeostasis via FBXL5; circadian period via
FBXL3/FBXL21; TOR signalling via FBXO9; BMP via FBXL15; inflammation via FBXO3; xenophagy via FBXO2 —
where SKP1 was explicitly shown to be required
[PMID:34515398 "SCF components such as SKP1, CUL1, and ROC1 are required for ubiquitin-mediated xenophagy against GAS"];
mitophagy via the FBXL4 ligase of which SKP1 is a *core* subunit per UniProt; centrosome duplication
regulation; DNA-damage checkpoint via FBX4; NMJ/synapse assembly via the MYCBP2-FBXO45-SKP1 module).
Marked **over-annotated** where the claim is a distal organismal phenotype of one receptor or where
the executing entity is plainly another subunit: limb development (mouse dactylin/FBXW4), neural
crest differentiation (FBXL17), regulation of apoptosis (FBXL18→FBXL7), generic regulation of
DNA-templated transcription and negative regulation of transcription, and heterochromatin formation
(done by the Polycomb catalytic/reader subunits, not by SKP1). This grading mirrors CUL1 and RBX1 on
the identical NAS references.

**Two MODIFYs for altitude,** both matching the correction already applied to CUL1:
- GO:0051298 centrosome duplication → GO:0010824 *regulation of* centrosome duplication. The SCF
  ligases restrain and time duplication (SCF(FBXW5)→SAS-6, SCF(cyclin F)→CP110); they do not perform
  it. Note the cited reference (PMID:34388369) is the human **signal peptidase complex** structure
  and does not address centrosomes at all, so it cannot carry the direct term either.
- GO:0060271 cilium assembly → GO:1902017 *regulation of* cilium assembly. SCF(FBXW5) removes the
  depolymerase MCAK whose excess blocks ciliogenesis
  [PMID:34368969 "loss of Fbxw5 leads to increased MCAK levels at basal bodies and impairs ciliogenesis in the following G1"].

**GO:0000151 ubiquitin ligase complex → ACCEPT (not MODIFY to GO:0019005).** The general parent is
the right level here precisely because SKP1 is *not* confined to SCF: CRL7(FBXW8) and the
cullin-less PAM/FBXO45 ligase would both fall outside GO:0019005.

**Reactome TAS rows (22 nucleoplasm + 46 cytosol) → ACCEPT**, each summarised with its own reaction
name, as done for CUL1. Every reaction is a curated SCF step in the stated compartment.

## 5. `proposed_new_terms: []` — and the comparator check behind it

Tempting candidates and why each was rejected:

- *Protein complex assembly / ubiquitin ligase complex assembly.* SKP1 is a constitutive **subunit**
  of the complexes in question, not an assembly factor acting on them from outside; the assembly-factor
  role in this pathway belongs to CAND1, which exchanges receptors, and to SGT1/HSP90. Comparator
  check: CUL1 and RBX1 — the other two invariant SCF subunits, in the same structural role — carry no
  such term in human, mouse or rat. A systematic absence across three MODs is a convention, not a gap.
- *Positive regulation of ubiquitin-protein transferase activity.* This is the "activator" framing
  again; GO:0140677 already covers the one case where an enhancement was actually measured
  (FBXO45-NMNAT2), and extending it to SCF generally would assert an allosteric role the structures
  do not show.
- *Centriole separation / chromosome stability process terms.* SKP1 depletion does cause replication
  stress, micronuclei and chromothripsis
  [file:human/SKP1/SKP1-deep-research-falcon.md "Human SKP1 depletion increases Cyclin E1 and produces replication stress, DNA double-strand-break markers, micronuclei, altered chromosome numbers, and chromothriptic events."],
  but this is necessity evidence for assembling the whole SCF repertoire, not participation in a
  distinct process — as the deep-research report itself concludes
  [file:human/SKP1/SKP1-deep-research-falcon.md "the most precise interpretation is not that SKP1 constitutes a stand-alone “genome-stability pathway,” but that an adequate pool of SKP1 is required to assemble multiple SCFs whose coordinated substrate turnover prevents replication and mitotic errors."]
  Existing GO:0031146 / GO:0043161 / GO:0000082 already express what SKP1 contributes.

## 6. Consistency with partners and models

- Grading kept in line with the completed reviews of the other SCF subunits: `genes/human/CUL1`
  (scaffold, GO:0160072 core), `genes/human/RBX1` (catalysis, GO:0061630 core), `genes/human/SKP2`
  (substrate recognition, GO:1990756 core). SKP1 takes GO:0160072 as its core MF with
  `contributes_to` GO:0061630 — it has no catalytic activity of its own.
- `modules/g1_s_transition.yaml` cites SKP1 (UniProtKB:P63208) as the SCF adaptor exemplar; consistent.
- GO-CAM models containing SKP1 (`gocams/index.tsv`): FBXO9/CARM1, FBXO7/SIRT7, cyclin F/CP110,
  cyclin F/EXO1, cyclin F/RRM2, FBXO28/RAB27A all type the SKP1 node as **GO:0160072**, and the
  PAM/FBXO45/NMNAT2 model (`gomodel:63c0ac2b00000506`) types it as **GO:0140677**. Both terms are
  ACCEPTed here, so the review and the models agree.

## 7. Outcome

Status `COMPLETE`; 443/443 annotations reviewed. Actions: 195 REMOVE (all bare `GO:0005515`),
139 ACCEPT, 75 MODIFY, 27 KEEP_AS_NON_CORE, 7 MARK_AS_OVER_ANNOTATED. Three core functions
(SCF adaptor/scaffold; substrate-receptor-module partner in cullin-less and CRL7 ligases; nuclear
retention of F-box proteins). `just validate human SKP1` passes with no errors and no warnings.
