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
