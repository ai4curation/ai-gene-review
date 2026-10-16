# CDKN1B (p27Kip1) — curation notes

UniProt: P46527 · HGNC: CDKN1B · 198 aa · CDI family (Pfam PF02234, InterPro IPR003175)

## 1. What the protein is

p27Kip1 is a Cip/Kip-family cyclin-dependent kinase regulator, related to p21/CDKN1A and
p57/CDKN1C. It is not an enzyme and has no chemical substrate; it acts stoichiometrically by
binding cyclin–CDK complexes. It is largely intrinsically disordered in isolation, and the
disorder is functional rather than an artefact: the kinase-inhibitory domain folds on binding
[PMID:11790096 "inhibition domain and full-length p27 are active as cyclin A-Cdk2 inhibitors."],
and preforming its helix slows complex formation, so p27 "derives a kinetic advantage from
intrinsic structural disorder" in the authors' phrasing.

Mechanism of inhibition, from the crystal structure of the KID bound to phospho-cyclin A–CDK2
[PMID:8684460 "p27Kip1 binds the complex as an extended structure"] — it engages both subunits:
on the cyclin, [PMID:8684460 "On cyclin A, it binds in a groove"] formed by conserved cyclin-box
residues (the MRAIL groove); on the kinase it rearranges the N-terminal lobe and
[PMID:8684460 "inserts into the catalytic cleft, mimicking ATP."]

Binding is sequential and this is what sets specificity
[PMID:15024385 "Binding to Cdk2-cyclin A is accompanied by p27 folding, and kinetic"] data
support cyclin-first engagement, and
[PMID:15890360 "p27/cyclin interactions are an important determinant of p27 specificity towards"]
cell-cycle CDKs. The negative control is informative:
[PMID:15890360 "p27 fails to interact with p25 within the"] CDK5–p25 complex, because p25 lacks
the MRAIL motif — hence p27 does not regulate CDK5 in neurons despite binding CDK5 itself.
The same logic explains the Spy1/RINGO escape:
[PMID:28666995 "explaining why Cdk-Spy1 is poorly inhibited"] — Spy1 lacks the cyclin-binding
site that mediates p27 affinity. This is the basis of the UniProt statement that p27 has little
inhibitory activity on SPDYA-bound CDK2.

## 2. Core function: G1/S restraint via cyclin E/A–CDK2

The cloning paper is still the cleanest statement of the core activity
[PMID:8033212 "p27Kip1 associates with cyclin E-Cdk2"] complexes in vivo and in vitro,
[PMID:8033212 "prevents their activation, and inhibits"] previously activated complexes, and
[PMID:8033212 "p27Kip1 overexpression obstructs cell entry"] into S phase. Substrate-level:
[PMID:8033212 "p27Kip1 potently inhibits Rb phosphorylation by cyclin E-Cdk2,"] cyclin A-Cdk2,
and cyclin D2-Cdk4. Physiological trigger:
[PMID:8033212 "a cyclin-dependent kinase inhibitor implicated in G1 phase"] arrest by TGF-beta
and cell–cell contact.

Independent in-cell readout at a defined CDK2 substrate: p27 blocks CDK2-dependent
phosphorylation of p220/NPAT and histone H4 promoter activation, and is more effective than p21
[PMID:19170105 "effective than p27(KIP1) and p57(KIP2) in inhibiting the CDK2 dependent"].

Adenoviral delivery is pRb-dependent, placing p27 upstream of Rb
[PMID:10208428 "induced growth arrest, inhibited DNA synthesis, and prevented"]
[PMID:10208428 "phosphorylation of the retinoblastoma protein (pRb) in cell lines expressing"]
functional pRb — in pRb-deficient cells the CKIs did not arrest growth.

## 3. Second genuine function: cyclin D–CDK4/6 assembly (not inhibition)

This is why p27 must not be described as a pure inhibitor:
[PMID:9106657 "p21(CIP), p27(KIP), and p57(KIP2) all promote the association of cdk4 with the"]
D-type cyclins, mostly by decreasing k_off; and
[PMID:9106657 "we find that all three CIP/KIP inhibitors target cdk4 and cyclin D1 to"] the
nucleus. LaBaer et al. drew the adaptor conclusion themselves — the p21 family,
[PMID:9106657 "originally identified as inhibitors, may also have roles as"] adaptor proteins
that assemble and program kinase complexes. Tyr74/Tyr88 phosphorylation is required for CDK4
binding (UniProt SUBUNIT) and can leave CDK4 active. Consequence for curation: the parent term
GO:0019914 *cyclin-dependent protein kinase regulator activity* is the right shape for this gene
and should not be collapsed into the inhibitor child; both signs are real.

## 4. Regulation (mostly post-translational)

**Thr187 / SCF(SKP2)–CKS1.** The switch that destroys p27 at G1/S:
[PMID:16209941 "Thr187 phosphorylation, which leads to the binding of the SCF(Skp2)"]
(Skp1-Cul1-Rbx1-Skp2) complex, with CKS1 obligatory —
[PMID:16209941 "phosphorylated Thr187 side chain of p27(Kip1) is recognized by a Cks1 phosphate"]
binding site, and Glu185 inserts into the SKP2–CKS1 interface. Note the direction of the
relationship: **p27 is the substrate**; the structure gives no evidence of p27 activating the
ligase (see §6).

**Ser10 / UHMK1(KIS) and CRM1 export.**
[PMID:12093740 "hKIS is a nuclear protein that binds the C-terminal domain of"] p27 and
phosphorylates Ser10, promoting [PMID:12093740 "nuclear export to the cytoplasm"];
[PMID:12093740 "and expression of hKIS overcomes growth arrest induced by p27(Kip1)."] KIS-siRNA
enhances arrest, and p27-null cells are refractory,
[PMID:12093740 "implicating p27(Kip1) as the"] critical target.
Export itself is CRM1/Ran-driven: [PMID:12529437 "p27 is nuclear in G0 and early G1 and appears"]
transiently cytoplasmic at G1/S;
[PMID:12529437 "p27-CRM1 binding and nuclear export were inhibited by S10A mutation"] but not by
T187A; the model is that [PMID:12529437 "p27 undergoes active, CRM1-dependent nuclear export and"]
cytoplasmic degradation in early G1. **p27 is the cargo here, not part of the export machinery.**

**Thr157/Thr198, AKT/RSK, 14-3-3.** AKT
[PMID:15057270 "phosphorylates Thr 157 of p27 and this reduces the nuclear import activity of"]
p27, and [PMID:15057270 "14-3-3 suppresses importin alpha/beta-dependent nuclear"] localisation
by competing with importin alpha5 for the phospho-NLS.
[PMID:17053782 "Phosphorylation of p27 at T198 prevents"] ubiquitin-dependent degradation of free
p27, synergising with the T187 route
[PMID:17053782 "Turnover of p27 at the G1/S transition is regulated through phosphorylation at"]
T187. T198 also matters for motility: [PMID:21423803 "T198 phosphorylation favors"]
p27/stathmin interaction.

**Tyrosine phosphorylation.** A
[PMID:17254966 "conserved tyrosine residue (Y88) in the Cdk-binding domain of p27 can be"]
phosphorylated by LYN and BCR-ABL; this does not prevent binding but
[PMID:17254966 "causes phosphorylated Y88 and the entire inhibitory 3(10)-helix of p27 to be"]
ejected from the CDK2 active site, restoring partial activity and enabling Thr187
phosphorylation. Src acts similarly:
[PMID:17254967 "Src-phosphorylated p27 is shown to inhibit cyclin E-Cdk2 poorly in vitro, and"]
Src transfection reduces p27–cyclin E–CDK2 complexes.

**SKP2-independent turnover.** In Wnt10b mammary tumours,
[PMID:19056892 "Wnt-induced turnover of p27(KIP1) was independent from classical"]
SCF(SKP2)-mediated degradation; CUL4A
[PMID:19056892 "interacted with p27(KIP1) in Wnt-responding cells"] and
[PMID:19056892 "both Cul4A and Cul4B were required for Wnt-induced p27(KIP1) degradation"].
Again: substrate, not ligase subunit (see §6). Lithium in that work is a GSK3 inhibitor used to
turn Wnt on — a reagent, not a biological stimulus for p27.

## 5. Cytoplasmic, CDK-independent functions

RhoA: [PMID:19470470 "increase RhoA-p27 binding and cell motility."] RSK1 transfectants show
[PMID:19470470 "increased motility, and reduced RhoA-GTP, phospho-cofilin,"] and loss of actin
stress fibres, all reversed by p27 shRNA. Stathmin: p27 acts through
[PMID:15652749 "ability to bind and impair the function of the MT-destabilizing protein"]
stathmin, and [PMID:15652749 "upregulation of p27(kip1) or downregulation of stathmin"] inhibits
mesenchymal motility. Note the **directional conflict**: the RhoA axis makes cytoplasmic p27
pro-migratory, the stathmin axis anti-migratory. I therefore annotated the molecular activity
(small GTPase binding, GO:0031267 — the old "Rho GTPase binding" GO:0017048 is merged into it)
and the cytosolic location, and deliberately proposed **no** directional migration process term;
raised as a question for experts instead.

MCM7 is a further CDK-independent route:
[PMID:16289477 "to inhibit initiation of DNA replication"], where the p27 C-terminus
[PMID:16289477 "inhibits DNA replication independent of its function as a"] CDK inhibitor.

## 6. Curation decisions that needed an argument

**Substrate ≠ participant.** Three annotations invert the direction of a relationship in which
p27 is the thing being acted on. Applying the participation test from CLAUDE.md (which entity
performs the step?):

- `GO:1990757 ubiquitin ligase activator activity` (EXP, PMID:16209941) → **REMOVE**. The
  structure shows substrate recognition, not ligase activation; SCF(SKP2)–CKS1 works on other
  substrates without p27. The supportable claim from the same paper, `GO:0031625 ubiquitin protein
  ligase binding`, is separately annotated, so nothing is lost.
- `GO:0051168 nuclear export` (IMP, PMID:12529437) → **REMOVE**. CRM1/RanGTP does the work; p27
  contributes only the NES that CRM1 reads, and exports nothing else.
- `GO:0045732 positive regulation of protein catabolic process` (IDA, PMID:19056892) → **REMOVE**.
  p27 is the protein catabolised by the Wnt-induced CUL4A/4B ligase.
- `GO:0031464 Cul4A-RING E3 ubiquitin ligase complex` (IDA, part_of) → **MODIFY** →
  `GO:0031625`. part_of asserts subunit composition; CRL4 is CUL4A/B–RBX1–DDB1–DCAF and p27 is
  cargo. (The cited paper is also about p21 and Cdt1, but the argument stands on complex
  composition, not on the abstract's subject.)

**Sign errors.** `GO:0045740 positive regulation of DNA replication` (Reactome TAS) → **MODIFY**
→ `GO:0008156 negative regulation of DNA replication`: p27 appears in "Cyclin A:Cdk2-associated
events at S phase entry" as the inhibitor that must be degraded. Direct evidence for the negative
sign: the MCM7 paper above and S-phase-entry block. `GO:2000045 regulation of G1/S transition`
(IDA) → **MODIFY** → `GO:2000134` (negative), matching the pRb-dependent arrest data.

**Growth vs proliferation.** `GO:0030308 negative regulation of cell growth` and
`GO:0045926 negative regulation of growth` → **MODIFY** → `GO:0008285`. In GO, "growth" is
increase in size/mass; every underlying assay measured division (arrest, DNA synthesis, Rb
phosphorylation, tumour latency). No evidence p27 controls cell size.

**Too general in the inhibitor hierarchy.** `GO:0004860 protein kinase inhibitor activity` (IMP)
and `GO:0140678 molecular function inhibitor activity` (IMP) → **MODIFY** → `GO:0004861`. p27 does
not inhibit kinases generally; the cited papers are cyclin–CDK2 experiments.

**p53-class DDR.** Both `GO:0030330` TAS rows → **MARK_AS_OVER_ANNOTATED**. The p53-responsive CKI
is p21: [PMID:19170105 "gamma-irradiation induces p21(CIP1/WAF1) but not the other two CKIs, while"]
reducing histone H4 mRNA. The annotation comes from pathway membership (p27/p21 CDK2 inactivation
is a sub-event of the p53-dependent G1 checkpoint), not from evidence that p27 transduces damage
signals. Not removed outright because p27 can contribute to arrest downstream of damage.

**Overexpression phenotypes.** `GO:0048102 autophagic cell death` (IDA, PMID:12698196) →
**MARK_AS_OVER_ANNOTATED**: adenoviral p27
[PMID:12698196 "overexpression of p27(KIP1) induced autophagic cell death, but"] not apoptosis,
and [PMID:12698196 "ability to suppress the growth of all tumour cells tested than other CDKIs."]
— yet the same construct neither killed nor induced autophagy in normal astrocytes. Dose- and
context-dependent, not a physiological function. `GO:0071285 cellular response to lithium ion` →
**MARK_AS_OVER_ANNOTATED** (reagent, see §4). `GO:0007165 signal transduction` (ARBA) →
**MARK_AS_OVER_ANNOTATED**: p27 is the endpoint of antimitogenic signalling, not a transducer, and
a root-level term invites bad propagation.

**Pleiotropic / tissue-specific process terms → KEEP_AS_NON_CORE**, graded consistently: heart
development (×2) and negative regulation of cardiac muscle tissue regeneration (×2), both from the
mouse cardiomyocyte study — [PMID:24380855 "cyclin E, cyclin A and CDK2 at postnatal stages."] and
[PMID:24380855 "showed failure in the cell cycle exit at G1-phase, and endoreplication."], where the
organ-level consequence follows because
[PMID:24380855 "cycle exit inhibits cardiac regeneration by the proliferation of pre-existing"]
cardiomyocytes; negative regulation of vSMC proliferation
([PMID:19088079 "miR-221 is critical for PDGF-mediated induction of cell proliferation."]);
cellular senescence (Reactome TAS; p16/p21 are the principal senescence CKIs); endosome (UniProt
SL-0101 is a degradative colocalisation with SNX6, and "By similarity" at that).

**Protein binding (126 rows).** Per the repo policy, `GO:0005515` is never ACCEPT/
KEEP_AS_NON_CORE. Graded by partner class: cyclin partners (CCNA1/A2, CCNB1, CCND1/2/3, CCNE1/E2)
→ **MODIFY** → `GO:0030332 cyclin binding`; CDK partners (CDK1/2/4/5) → **MODIFY** →
`GO:0019901 protein kinase binding`; RHOA → **MODIFY** → `GO:0031267 small GTPase binding`
(the paper supports the specific activity); all other partners → **REMOVE** as uninformative,
explicitly noting that removal concerns the term, not the reality of the interaction.

**Deferred to curators** (rule: do not overrule an experimental annotation from an abstract-only
cache): `GO:0005634 nucleus` IDA from PMID:11800646 (cached abstract reports p18INK4C/p14ARF
staining — ACCEPTed anyway, since p27's nuclear localisation is not in doubt and is corroborated by
PMID:12529437 and PMID:15057270); `GO:0004861` IDA from PMID:10918569 (PTEN/p27 thyroid paper,
abstract shows only the p27-dependence of growth suppression); `GO:0019903 protein phosphatase
binding` with PTPN6/SHP-1 (abstract states
[PMID:19838216 "increases p27(Kip1) (p27) protein stability, its nuclear localization and p27"]
gene transcription and an SHP-1–PI3K interaction, but no direct p27–SHP-1 complex — kept as
non-core on the curator's reading; note also PPM1H genuinely dephosphorylates Thr187 per UniProt).

**IBA rows** (GO:0004861, GO:0005634, GO:0005737, GO:2000134; PANTHER:PTN004142838) all ACCEPTed.
Human P46527 appears in its own WITH/FROM for three of them, which is expected: the gene's own
experimental annotation is one of the descendant evidences used to place the IBD node, so this
marks experimental grounding on the target and adds the claim that the function is inherited.
Descendant evidence spans Drosophila dacapo and C. elegans cki-1/cki-2, consistent with a
Cip/Kip-wide function.

## 7. Open points

- Direction of cytoplasmic p27's effect on motility (RhoA vs stathmin) is unresolved; no
  directional process term proposed.
- GO has no clean term for the Cip/Kip assembly-factor activity; `GO:0060090 molecular adaptor
  activity` is the closest and was ACCEPTed, but a cyclin-CDK-complex-assembly term would be
  better. Raised in `suggested_questions` rather than as `proposed_new_terms`.
- `proposed_new_terms: []` — no NEW annotations added. Everything supportable is either already
  present or covered by a proposed replacement, and the tempting additions (substrate of SCF/CRL4,
  cargo of CRM1) fail the participation test.


---

# 2026-10-10 — substantive audit superseding prior conclusions

This audit starts from the existing review on main `10eda3330253be3140fe764020499de4f8ce8bf3`. All 214 original annotation objects, including evidence codes, references, partners and isoforms, are preserved. No NEW annotation is added. The preceding journal is preserved verbatim as historical provenance. This dated section supersedes its conclusions about generic-binding removals, phosphorylation being required for CDK4 binding, organismal growth, lithium response, signal transduction, source-specific substrate/transport roles and unresolved interaction evidence. Earlier scientific statements and quotation totals are historical rather than current conclusions. Only introduced excerpts are counted in the new quote audit; repeated old-paper excerpts are not reintroduced here.

The applicable [standing project instruction](https://github.com/ai4curation/ai-gene-review/blob/10eda3330253be3140fe764020499de4f8ce8bf3/projects/CLINGEN_MENDELIAN.md#curation-instructions) explicitly says to retain supported, biologically correct generic protein binding as `KEEP_AS_NON_CORE` when no evidence-backed specific replacement is established. It also requires `MODIFY` for supported refinements and `UNDECIDED` for inaccessible or unadjudicated evidence. This supersedes the prior notes' genericity-only removal rule; it does not manufacture a molecular activity from a screen association.

## Inhibition, recognition and assembly

p27 is a largely disordered Cip/Kip regulator whose N-terminal region folds on cyclin–CDK complexes. It is not a protein kinase. The cyclin A–CDK2 structure establishes two contacts and blockade of the kinase cleft (PMID:8684460). Sequential binding measurements distinguish cyclin engagement from subsequent kinase contact (PMID:15024385), while the isolated inhibitory region and full-length p27 inhibit cyclin A–CDK2 (PMID:11790096). Cyclin recognition helps explain why CDK5 binding does not imply inhibition of CDK5–p25 (PMID:15890360), and why CDK2–Spy1 is comparatively resistant (PMID:28666995). These are specificity limits, not evidence that the binding partners are absent.

The original human cloning/biochemistry study connects p27 to cyclin E–CDK2 inhibition and S-phase-entry restraint (PMID:8033212). In-cell work links p27 to reduced CDK2-dependent NPAT phosphorylation and histone-promoter activity (PMID:19170105). Adenoviral CKI delivery inhibits DNA synthesis and Rb phosphorylation in cells with functional Rb (PMID:10208428). These support the nuclear inhibitory core. The latter study's accessible abstract measures division-related readouts, not individual-cell size; the source-specific cell-growth annotation is refined to proliferation without denying other growth functions.

Assembly and catalytic activation are separable. The original assembly study reports p27-dependent cyclin D–CDK4 association and nuclear targeting (PMID:9106657; protected cache abstract-only). Its low-concentration kinase experiment specifically naming p21 is not transferred to p27. The independent full human study [PMID:31831640](https://doi.org/10.1126/science.aaw2106) directly resolves p27-containing trimers: “the trimer with unphosphorylated p21 or unphosphorylated p27 demonstrated poor activity.” Unphosphorylated p27 therefore already binds the complex. Tyr74 phosphorylation weakens its inhibitory contact; the roles of Tyr88/Tyr89 are less pronounced than in CDK2. Improved ATP processing does not mean every substrate is phosphorylated more efficiently, because p27 can also occlude cyclin docking sites. The genuine full XML cache and [author-hosted publisher PDF](https://shokatlab.ucsf.edu/pdfs/31831640.pdf), Results/Figures 1–4 and Methods, were inspected. Recombinant human constructs and the CDK4 T172E comparison are distinguished from native cellular complexes; CDK4 conclusions are not indiscriminately assigned to CDK6.

The molecular-adaptor core is retained with this corrected mechanism. GO:0019914 remains a valid broad regulator assertion: the live ontology graph places GO:0004861 beneath GO:0016538 and GO:0019914. The broad term's inconsistent activating-kinase wording is not treated as evidence that the inherited biological assertion is false.

## Modification, transport and turnover

Human UHMK1/hKIS binds p27 and phosphorylates Ser10; selected full Results/Figure 1B support the human recombinant pair, while the endogenous comparison in Figure 6 uses mouse fibroblasts (PMID:12093740). AKT-dependent Thr157 phosphorylation and 14-3-3 competition alter nuclear import (PMID:15057270); Thr198 affects stability and partner association (PMID:17053782, PMID:21423803). LYN/ABL and Src-mediated tyrosine phosphorylation alter CDK2 inhibition (PMID:17254966, PMID:17254967). The source partner in the ABL row is explicitly mouse P00520. These interactions support kinase binding by p27, without transferring kinase activity to it.

For nuclear export, the full [PMID:12529437 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC140238/) was read at Methods and Results/Figures 2, 3 and 6. It uses human p27 constructs in MCF-7 cells, measures nuclear p27 loss/export, and compares NES and Ser10 variants. Figure 6 also exports a FITC-BSA fusion carrying the p27 NES, demonstrating a transferable cargo-recognition signal rather than native p27 transporting another molecule. The demonstrated p27 role is that of cargo transported by CRM1/Ran. The original nuclear-export process assertion is removed on that exact assay boundary; the localization and interaction evidence remain. No universal claim is made that a transported protein could never also act as an export cofactor.

SCF(SKP2)–CKS1 recognizes the phosphorylated p27 degron (PMID:16209941). The normal cache is abstract-only, but selected full [publisher Results, Figure 4 and Methods](https://www.sciencedirect.com/science/article/pii/S1097276505016035) were read through indexed primary text. Purified ligase is assembled before p27 is added, and the readouts quantify p27 ubiquitin conjugates. These assays support substrate recognition and ligase binding, not a separately demonstrated activator role performed by p27. The activator assertion is removed without the prior unsupported claims about other substrates or an absolute substrate-versus-regulator rule. The complete supplementary archive and figure pixels were not inspected.

The complete [PMID:19056892 primary Results and Methods](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2593606/?report=xml) were recovered as authentic HTML, SHA256 `1bad42e8824852459272256f882cc5dc24048e9528574cd8bd2980f1bb2d9e17`. Figure 6G/H and the human 293T/MCF7 experiments show CUL4-dependent p27 turnover; the catabolic regulator assertion is removed because the measured p27 role is the substrate, with no demonstrated catalytic/cofactor contribution to proteolysis. Figure 3C compares human Flag-p27 WT/T187A after LiCl 25/50 mM versus NaCl 50 mM and shows p27 loss. The contextual lithium-response assertion is retained as non-core, without claiming lithium sensing or p27-specific necessity. Pharmacological lithium is a valid GO stimulus; the earlier categorical exclusion was wrong. The protected extraction contains Abstract/Discussion despite its full-text flag. A genuine isolated refresh returned only an abstract, so it does not replace the protected cache; external full access remains documented. Supplement S7 was read only through its description in Results, not its pixels. Separately, selected PMID:21628527 Methods/Results were accessed, but the precise p27 evidence behind Cul4A-complex membership was not recovered. A paper emphasizing p21/Cdt1 is not proof of a p27 misattribution, and an independently observed substrate encounter does not alone establish stable complex membership.

## Cytoplasmic functions and broader phenotypes

The RSK1 study reports p27–RhoA association, altered RhoA-GTP/cofilin/stress fibers and p27-depletion effects on motility (PMID:19470470; primary abstract and target figure legends inspected). Small-GTPase binding is a core activity, not GTP hydrolysis by p27. Separate p27–stathmin work supports microtubule-related regulation and context-dependent motility effects (PMID:15652749, PMID:21423803). Stathmin is not folded into the RhoA-binding activity description. MCM7 association provides a further route to replication restraint (PMID:16289477); p27's removal from an inhibitory complex is not a positive replication activity performed by the inhibitor itself.

The broad signal-transduction annotation is retained as non-core: the GO definition does not exclude an intracellular effector that couples phosphorylation-dependent changes to kinase or cytoskeletal outputs. Tissue-specific cardiac, vascular smooth-muscle and senescence assertions remain contextual, rather than defining additional core molecular activities. The cardiomyocyte source is a mouse p21/p27 study; its G1-exit/endoreplication findings and discussion of regeneration are not described as direct human regeneration experiments (PMID:24380855). The p53-pathway assignments remain over-annotated because the shared Reactome p27/p21 inhibitory event does not establish a p27-specific p53 signaling step; absence of p27 induction in one irradiation experiment is not a universal exclusion of a damage-response role.

Organismal growth is distinct from individual-cell growth. The primary mouse inhibitory-domain study reports enlarged animals attributable to increased cell number; increased growth “occurs without an increase in the amounts of either growth hormone or IGF-I.” [PMID:8646780]. This supports retaining the broad negative-growth assertion as non-core with explicit ortholog scope. It corrects the prior claim that no organism-size evidence exists.

For autophagic cell death, full PMID:12698196 Methods/Results were inspected. Human p27 overexpression in human glioma cells produced viability loss and acidic vesicles; the normal astrocyte comparison was rat RNB. The inspected evidence does not establish an autophagy-dependent execution step supplied by p27. The over-annotation judgment concerns that mechanistic and assay limit, rather than treating cancer-cell or overexpression experiments as intrinsically invalid.

## Exact interaction evidence and remaining gaps

The [durable interaction extract](CDKN1B-interaction-evidence.json) contains literal accession pairs, source PMIDs, taxa, methods, features, record URLs and original-response hashes for the exact IntAct/MINT joins, the official OpenCell CDK2–CDKN1B row, and publisher Table S3 target cells. These are source-linked records, frequently sharing provenance with GOA, not independent experimental replication. Co-IP, AP-MS, pull-down and proximity assays retain their resolution limits; absent feature fields do not establish wild-type sequence. Shared BioPlex releases are not counted as new biological replicates. [The executable generator](CDKN1B-extract-interactions.py) recomputes this projection from the downloaded MITAB, official CSV, genuine workbook and unchanged annotation source objects; it does not infer curation actions.

The [2015 publisher Table S3](https://ars.els-cdn.com/content/image/1-s2.0-S0092867415004304-mmc3.xlsx), SHA256 `c401dffd03b173062a91ecb9dfcbd424319582d70498cef269bbce0af13492ec`, is decisive for four pairs. Table S3A rows 504–511 show wild-type p27 Y2H scores of zero and I119T scores of one for BANP, CCND2, THAP1 and TRAF2. The exact BANP isoform remains Q8N9N5-2. Table S3B independently gives high CCND2 complementation values for both WT and I119T. Mutant-only screen positives are retained at their tested scope; feature-free pooling records are not mislabeled as WT positives. The 2019 TRAF2 comparison is independent evidence, while the 2022 FBXW7 mutations belong to the partner, not p27 (PMID:31515488, PMID:35512704). No numeric threshold is invented for unclassified complementation scores.

Several earlier generic-only removals now become supported non-core associations; UHMK1, ABL/LYN, short PIM1, RSK1, JAK2 and CHUK interactions support kinase-binding refinements, and HSC70 supports Hsp70 binding. The latter is a client interaction, not a chaperone activity assigned to p27. SKP2 recognition in the directly inspected phosphodegron study supports ligase binding. Some source-specific screens remain uninspected even where independent canonical cyclin/CDK experiments firmly establish the same biological pair; the corresponding reasons explicitly separate those evidence routes.

The exact PIM1 long-isoform assay, mapping of the paper's SCML2B construct to original Q9UQR0-1, p27–SHP-1 association and original Cul4A membership remain unresolved. No wrong-gene, wrong-isoform or negative-binding conclusion is inferred from failed access. The SHP-1 abstract's effect on p27 abundance and its explicit SHP-1–PI3K interaction do not substitute for the p27 partner experiment. A different phosphatase acting on p27 is not evidence for that exact source tuple.

## Research provenance

The existing genuine Falcon report and all original machine source files are protected. A fresh isolated normal fetch confirmed 214 assertions and reused the existing 69 PMID caches. A genuine default Falcon attempt timed out; explicit Perplexity-lite fallback returned an actual quota error. Neither attempt produced a new provider report. The manual primary-source audit proceeded independently, with two bounded scientific consultations on kinase assembly/substrate roles and six mutation-context interactions. Authentic supplemental publication caches were generated by the unchanged normal tool. Full-text availability is described by what was actually accessed, not inferred solely from a cache flag; source receipts and access limits accompany the publication packet.
