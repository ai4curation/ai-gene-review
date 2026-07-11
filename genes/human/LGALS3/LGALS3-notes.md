# LGALS3 (Galectin-3, P17931) — Gene Review Notes

## Summary of identity
- Human galectin-3 / Mac-2 antigen / CBP35 / IgE-binding protein / L-29 / L-31. HGNC:6563, UniProt P17931, 250 aa, chromosome 14.
- The **only chimera-type galectin** in mammals: a single C-terminal carbohydrate-recognition domain (CRD, ~residues 113–250) fused to an intrinsically disordered, proline/glycine-rich N-terminal tail (collagen-like repeats) that enables oligomerization.
- The CRD binds β-galactosides (lactose, N-acetyllactosamine/LacNAc), structurally solved at high resolution (e.g. PDB 1A3K, 2.1 Å; UniProt RN[25] PMID:9582341).

## Core molecular function: β-galactoside / carbohydrate binding + lattice formation
- "Galactose-specific lectin which binds IgE" (UniProt FUNCTION). Cloned as a galactose-specific macrophage lectin [PMID:2402511 "Molecular cloning of a human macrophage lectin specific for galactose"] and as a galactoside-binding lectin homologous to mouse Mac-2 [UniProt RN3 PMID:2022338].
- Gal-3 is monomeric but achieves functional **multivalency** via N-terminal self-association: "galectin-3 is monomeric, and its functional multivalency therefore is somewhat of a mystery... the disordered N-terminal domain (residues ∼20-100) interacts with itself and with a part of the CRD... forming a fuzzy complex" and "galectin-3 can also undergo liquid-liquid phase separation" [PMID:28893908]. This is the molecular basis for lattice/agglutination.
- Extracellular agglutination/lattice: "The mechanism through which galectin-3 agglutinates (acting as a 'bridge' to aggregate glycosylated molecules)... Our data show that its N-terminal domain (NTD) undergoes LLPS... aggregate LPS micelles. Aggregation is reversed when interactions between the LPS and the carbohydrate recognition domains are blocked by lactose" [PMID:32144274]. → DisProt annotated GO:0140693 molecular condensate scaffold activity from these two papers.
- Polysaccharide binding to NT: a novel binding site within the N-terminal tail in addition to two CRD sites [PMID:28973299 "two within its carbohydrate recognition domain (CRD) and one at a novel site within the NT"]. → supports GO:0030246 carbohydrate binding EXP DisProt.

This carbohydrate-binding + lattice-forming activity is the CORE function; nearly all downstream biology (adhesion, immune modulation, chemoattraction, apoptosis regulation) is mediated by cross-linking glycoconjugates.

## Localization (intracellular + extracellular)
- UniProt SUBCELLULAR LOCATION: Cytoplasm; Nucleus; Secreted (non-classical). Nuclear and cytoplasmic well-supported experimentally [PMID:7682704 nucleus IDA; PMID:14961764, PMID:22761016].
- Secreted by a non-classical (leaderless) pathway facilitated by cargo receptor TMED10 → translocation cytoplasm→ERGIC→secretion [UniProt; PMID:32272059].
- Acts both intracellularly and at the cell surface/ECM. Many HDA proteomics annotations place it in extracellular exosome/ECM/extracellular region — consistent with abundant secretion, but these are localization-by-detection (mass spec) not function.
- Nuclear role as pre-mRNA splicing factor (UniProt FUNCTION; spliceosomal complex keyword); RNA binding HDA from mRNA interactome [PMID:22658674].

## Damaged-endomembrane sensing / autophagy (lysophagy)
- "Together with TRIM16, coordinates the recognition of membrane damage with mobilization of the core autophagy regulators ATG16L1 and BECN1 in response to damaged endomembranes" [UniProt FUNCTION; PMID:27693506]. Gal-3 detects exposed luminal glycans on ruptured endo/lysosomal membranes and recruits autophagy machinery (a glycan-sensing function). Important, increasingly recognized intracellular role.

## Immune / inflammatory roles (downstream, pleiotropic)
- Chemoattractant for monocytes/macrophages: "galectin-3 is a novel chemoattractant for monocytes and macrophages... mediated at least in part through a PTX-sensitive (G protein-coupled) pathway"; blocked by lactose [PMID:10925302]. This one paper underpins many BHF-UCL IDA annotations (monocyte/eosinophil/macrophage/neutrophil chemotaxis, positive chemotaxis, mononuclear cell migration, Ca2+ influx, chemoattractant activity).
- T-cell modulation: overexpression increases T-cell growth and confers resistance to apoptosis (Bcl-2-like NWGR motif, interacts with Bcl-2) [PMID:8692888]. Underpins regulation of T cell proliferation (IMP) and regulation of T cell apoptotic process / extrinsic apoptotic signaling.
- Negatively regulates TCR signaling at the immunological synapse, reduces TCR clustering, drives endocytosis-related changes [PMID:19706535]. Underpins immunological synapse localization (IDA) and the human IDA negative-regulation-of-endocytosis annotation; the ISS T-cell terms are transferred from mouse ortholog P16110.
- Acts as a soluble inhibitory ligand of NKp30/NCR3, blocking B7-H6–NKp30 activation → inhibits NK / NKT / ILC2 activation [PMID:25315772 tumor escape; PMID:26582946 ILC2/NKp30, where Gal-3 = "an inhibitory ligand"]. Underpins receptor ligand inhibitor activity (GO:0141069 IDA) and negative regulation of NK T cell activation.
- Anti-apoptotic in tumor cells; EGF downregulates cytoplasmic Gal-3 to permit apoptosis [PMID:22761016] → negative regulation of extrinsic apoptotic signaling pathway (IDA).
- NOT annotation: Gal-3 does NOT positively regulate dendritic cell differentiation [PMID:16116184 — this paper is about galectin-9 inducing DC maturation; the NOT|involved_in for Gal-3 reflects that Gal-3 lacks this activity]. Keep negated annotation.

## Glycosylation / lattice at the cell surface (mechanistic exemplar)
- β1,6-GlcNAc-branched N-glycans (GnT-V products) on receptors are recognized by Gal-3, retaining them at the surface and modulating their function: "GnT-V overexpression enhances galectin-3's cell-surface retention and promotes PTPRT's dimerization mediated by galectin-3" [PMID:24846175]. Underpins protein phosphatase binding (IPI, PTPRT/O14522), positive regulation of protein localization to plasma membrane, positive regulation of protein-containing complex assembly. The "protein phosphatase inhibitor activity" (GO:0004864 IDA) is indirect (it promotes PTPRT dimerization which lowers PTPRT activity) — this is a glycan-lattice effect, not a direct enzyme-inhibitor MF; flag as over-annotation/keep-non-core.

## Interactions ("protein binding", GO:0005515)
~25 GO:0005515 IPI annotations, mostly from high-throughput interactome screens (PMID:25416956, 28514442, 31515488, 32296183, 33961781, 40205054) or single-partner IPI (MMP7 PMID:20812334 — MMP7 cleaves Gal-3; CD6/ALCAM PMID:24945728; CHI3L1/IL13RA2 PMID:29427412; endoglin/ENG PMID:31540324; MICA PMID:21712812; SARS-CoV-2 spike PMID:32915505; F1F0-ATP synthase ATP5B PMID:19016746). Generic "protein binding" is uninformative per curation guidelines — mark as over-annotated; the informative MF is carbohydrate/galactoside binding (many of these are glycan-dependent contacts). Do NOT remove (experimental IPI), but down-grade to over-annotated.

## Verdict logic applied
- CORE: carbohydrate binding (GO:0030246), galactoside binding (GO:0016936), molecular condensate scaffold activity / lattice (GO:0140693), and the glycan-sensing endomembrane-damage role.
- Generic GO:0005515 protein binding → MARK_AS_OVER_ANNOTATED (uninformative).
- HDA proteomics localizations (exosome, ECM, membrane, mitochondrial inner membrane, extracellular region) → mostly KEEP_AS_NON_CORE; the mitochondrial inner membrane IDA (PMID:19016746) is a single ATP-synthase-interaction study, treat as non-core/over-annotated.
- Immune/chemotaxis/apoptosis BP terms → KEEP_AS_NON_CORE (real but pleiotropic, downstream of lattice function).
- IBA, IDA core lectin & nucleus/cytoplasm localizations → ACCEPT.
- Redundant IEA/IBA that duplicate experimental annotations → ACCEPT or KEEP_AS_NON_CORE.
- ARBA IEA broad T-cell process terms (GO_REF:0000117) → KEEP_AS_NON_CORE (real but transferred/pleiotropic).
- GO:0048018 receptor ligand activity (ARBA IEA) → the better-supported MF is the inhibitory-ligand activity (GO:0141069, IDA); generic receptor ligand activity is borderline — MARK_AS_OVER_ANNOTATED in favor of the specific IDA term.

## GO terms verified for core_functions (hard-validated, MF/BP/CC branch)
- GO:0030246 carbohydrate binding — MF (in GOA already)
- GO:0016936 galactoside binding — MF (QuickGO verified, def "Binding to a glycoside in which the sugar group is galactose")
- GO:0140693 molecular condensate scaffold activity — MF (in GOA, DisProt)
- GO:0061684 (chaperone-mediated autophagy? no) — not used
- locations: GO:0005634 nucleus, GO:0005737 cytoplasm, GO:0005576 extracellular region, GO:0009986 cell surface, GO:0031012 extracellular matrix (all CC, in GOA)
- BP: GO:0061709 (reticulophagy? no). Endomembrane damage response — GO:0061912 selective autophagy? Will use GO:0007165 sparingly. For lattice/adhesion will keep BP minimal.

## Falcon integration (2026-06-21)

Integrated the FutureHouse Falcon deep-research report (LGALS3-deep-research-falcon.md, 23 citations)
into the existing, already-complete review. Conservative enrichment only — no `action` flips on the
105 reviewed annotations.

### References added (resolved to PMID via NCBI ID converter, fetched with `fetch-pmid`, full text cached)
- **PMID:32521192** — Jia et al. 2020, *Autophagy*, "MERIT, a cellular system coordinating lysosomal
  repair, removal and replacement" (DOI 10.1080/15548627.2020.1779451; Falcon key `jia2020meritacellular`).
  HIGH/VERIFIED. Landmark lysophagy paper. Verbatim: [PMID:32521192 "LGALS3 (galectin 3) detects
  membrane damage by detecting exposed lumenal glycosyl groups, recruits and organizes ESCRT components
  PDCD6IP/ALIX, CHMP4A, and CHMPB at damaged sites on the lysosomes, and facilitates ESCRT-driven repair
  of lysosomal membrane. At later stages, LGALS3 cooperates with TRIM16, an autophagy receptor-regulator,
  to engage autophagy machinery in removal of excessively damaged lysosomes."]
- **PMID:34612142** — Burbidge et al. 2022, *Autophagy*, "LGALS3 (galectin 3) mediates an unconventional
  secretion of SNCA/α-synuclein…" (DOI 10.1080/15548627.2021.1967615; Falcon `burbidge2022lgals3(galectin3)`).
  HIGH/VERIFIED. Verbatim: [PMID:34612142 "We demonstrate that LGALS3 (galectin 3) mediates the release of
  SNCA following vesicular damage."]
- **PMID:41194217** — Liu et al. 2025, *Biol Direct*, "Galectin-3 directs mitophagy…" (DOI
  10.1186/s13062-025-00692-1; Falcon `liu2025galectin3directsmitophagy`). MEDIUM/VERIFIED. Ties LLPS to
  intracellular organelle QC. Verbatim: [PMID:41194217 "mutations in key residues that confer the
  liquid-liquid phase separation (LLPS) properties of Galectin-3 abrogates its mitochondrial
  relocalization, ULK1 recruitment, and mitophagy"].

Note: Falcon also cites the TMED10 secretion paper (zhang2020atranslocationpathway, Cell 2020); this is the
SAME paper already in the review as PMID:32272059 (the title there reads "A Translocation Pathway for
Vesicle-Mediated Unconventional Protein Secretion"). Not re-added.

### Annotation / core_function enrichment
- Added a NEW existing_annotation **GO:0062093 lysophagy** (involved_in, IDA, PMID:32521192), with
  supporting_text from Jia 2020 and a second verbatim quote on glycan-recognition being required to
  initiate autophagy. This captures the damaged-endomembrane glycan-sensing → ESCRT repair →
  TRIM16-dependent lysophagy role, which was previously only in `description` and `proposed_new_terms`
  but absent from GOA/existing_annotations. GO:0062093 verified via QuickGO ("the selective autophagy
  process in which a damaged lysosome is degraded by macroautophagy").
- Strengthened core_function GO:0140693 (molecular condensate scaffold activity) with the Liu 2025
  verbatim quote showing LLPS-disrupting mutations abolish galectin-3 mitophagy — direct functional
  evidence that the LLPS/condensate activity drives intracellular organelle quality control.
- Strengthened the `proposed_new_terms` "damaged endomembrane glycan sensor activity" with the Jia 2020
  verbatim "detects membrane damage by detecting exposed lumenal glycosyl groups" (previously only a weak
  title-fragment quote from PMID:27693506).

### Falcon claims NOT integrated (with reasons)
- **Pyroptosis**: Falcon explicitly argues galectin-8 (not galectin-3) couples endomembrane damage to
  noncanonical inflammasome/pyroptosis (shivcharan2025). The existing review already contains no LGALS3
  pyroptosis annotation, so nothing to add or change — consistent with Falcon's caution.
- **Direct synaptic remodeling / Lewy-body localization**: Falcon flags both as over-extensions (indirect
  / pathology-specific). No such annotations exist in the review; not added (would be over-annotation).
- **Integrin (αvβ1/αvβ5/αvβ6) and TGFβRII binding in fibrosis** (calver2024): real but context-specific
  fibrosis mechanism. Not added as a new annotation — would be generic "protein binding"/context-specific
  signaling that the review already deliberately down-weights; left for the notes only.
- **Mitophagy as an existing_annotation**: kept the Liu 2025 paper as a reference and folded its LLPS
  evidence into the condensate-scaffold core_function, but did NOT add a standalone mitophagy
  existing_annotation — it is emerging/single-study and more context-specific than lysosomal lysophagy,
  per Falcon's own "moderate / emerging" grading.
- Falcon's cancer/heart-failure review citations (radziejewska2023, zaborska2023, tan2021, lozinski2024,
  mukherjee2025, zhang2025) are secondary reviews restating known lectin/lattice biology already covered
  by primary citations in the review; not added as top-level references.

## 2026-06-22 — asta IBA-support sift (manual)

Ran `just gene-iba-support-research asta human LGALS3` over the 15 IBA annotations that lacked
independent literature support (outputs in `LGALS3-hypotheses/function-support-*/asta.md`). asta
(Semantic Scholar relevance + snippet retrieval) returned 11–16 papers per term with verbatim
snippets, PMIDs/DOIs and scores. I manually sifted every report.

**Outcome: no supported_by added from this pass.** None of asta's candidates are adequate,
term-specific *primary* evidence for the GO term in question. The hits fall into three
false-positive classes:

1. **Frequency bias toward recent disease papers.** The same modern cancer/disease studies recur
   across many unrelated terms (HCC prognosis PMID:38643145; periplocin/CRC lysophagy PMID:37471054;
   glioma prognosis PMID:32528967), surfaced because they use the symbol "LGALS3" plus a process word,
   not because they assay that function.
2. **Review / family-level statements**, not primary, gene-specific evidence (e.g. Liu & Rabinovich
   2010 PMID:20146714 "Galectins, beta-galactoside-binding animal lectins"; Pregnancy Galectinology
   review PMID:31231368). True but family-level orientation only.
3. **Right gene, wrong specific process.** PMID:35230372 is "Macrophages secrete … galectin-3 to
   regulate neutrophil **degranulation** after myocardial infarction" — asta's snippet paraphrased it
   as neutrophil "migration", but the paper assays degranulation, so it does **not** support
   GO:0030593 *neutrophil chemotaxis*. (This is the receptor/process-mismatch trap to watch for.)

Crucially, asta **failed to surface the foundational primary literature** that actually established
these galectin-3 functions — e.g. galectin-3 as a monocyte/macrophage chemoattractant (Sano et al.
2000), the εBP/IgE-binding-protein biochemistry, and Mac-2/laminin binding. No laminin-, IgE/εBP-,
or chemoattractant-titled primary paper appeared in any report; the only "disaccharide binding" hit
was an incidental bone-phenotype study (PMID:36062328).

**Tuning leverage for next runs** (the query is the prompt, truncated to ~500 chars, so wording
matters): include legacy synonyms (`galectin-3`, `Mac-2`, `εBP`) alongside `LGALS3`, and consider
asta date/citation params — the relevance model here skews to recent, highly-cited genomics-era
papers and misses pre-2005 foundational biochemistry. For a well-studied gene like LGALS3, a targeted
classic-literature lookup is more productive than asta; asta's recall value is likely higher for
poorly-studied genes.

## 2026-06-22 — manual PubMed curation of IBA support

Followed the rule: *first check whether the deep-research (asta) report already surfaced the right
paper; if not, iterate manually; if so, curate the snippet.* The asta report surfaced the correct
foundational paper in **0 of 11** checked functions, so all support below was found by manual PubMed
(NCBI E-utilities) search and verified verbatim against the fetched abstract in `publications/`.

Added `supported_by` to **12 of 15** IBA annotations:

| Term | GO | Reference | Note |
|---|---|---|---|
| monocyte chemotaxis | GO:0002548 | PMID:10925302 (Sano 2000) | galectin-3 induces monocyte migration, chemotactic |
| macrophage chemotaxis | GO:0048246 | PMID:10925302 | "chemoattractant for monocytes and macrophages" |
| positive chemotaxis | GO:0050918 | PMID:10925302 | parent of the above |
| positive regulation of calcium ion import | GO:0090280 | PMID:10925302 | "galectin-3 caused a Ca2+ influx in monocytes" (same paper) |
| laminin binding | GO:0043236 | PMID:2332426 (Woo 1990) | Mac-2 = laminin-binding protein = galectin-3 |
| disaccharide binding | GO:0048030 | PMID:11434930 | ITC of galactose/poly-LacNAc binding; lactose/LacNAc are the disaccharide ligands |
| IgE binding | GO:0019863 | PMID:8347574 | εBP (=Mac-2=galectin-3) "by virtue of its affinity for IgE"; ortholog (rat εBP) evidence, acceptable for an IBA |
| nucleus | GO:0005634 | PMID:12070075 | galectin-3 in nuclear/cytoplasmic SMN complex; pre-mRNA splicing factor |
| cytoplasm | GO:0005737 | PMID:12070075 | nucleocytoplasmic shuttling |
| immunological synapse | GO:0001772 | PMID:19706535 | "recruited to the cytoplasmic side of the immunological synapse" |
| eosinophil chemotaxis | GO:0048245 | PMID:23576987 | Gal-3−/− mice show decreased airway eosinophil recruitment |
| neutrophil chemotaxis | GO:0030593 | PMID:11823514 | galectin-3 promotes neutrophil extravasation/recruitment (mechanism is adhesion-mediated transmigration, not a soluble chemoattractant gradient — supporting, not definitive, for the chemotaxis term) |

**Not curated (3) — left honestly unsupported:**

- **GO:0031012 extracellular matrix** — galectin-3 is clearly secreted/extracellular, but I did not
  find a clean primary statement that it localises to the *extracellular matrix* specifically (vs
  extracellular fluids / cell surface). Needs a dedicated ECM-deposition paper.
- **GO:0045806 negative regulation of endocytosis** — the galectin-lattice-restricts-receptor-
  endocytosis concept (Partridge/Dennis 2004; Lajoie 2007) is plausible but no clean primary paper
  surfaced in a quick search; not added.
- **GO:2001237 negative regulation of extrinsic apoptotic signaling pathway** — galectin-3 is broadly
  anti-apoptotic (intracellular, NWGR/BH1 motif), but a paper tying it specifically to the *extrinsic*
  (death-receptor) pathway was not located in a quick search; not added.

Net: manual PubMed cleanly recovered the foundational literature (Sano 2000, Woo 1990, the εBP/IgE
papers, the shuttling papers) that asta entirely missed — reinforcing the deprecation recommendation
(issue #1599).
