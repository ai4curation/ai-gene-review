# DDC (Aromatic-L-amino-acid decarboxylase / AADC / DOPA decarboxylase) — review notes

UniProt: P20711 (DDC_HUMAN). HGNC:2719. EC 4.1.1.28. 480 aa, 53.9 kDa.

## Core identity and function

DDC encodes **aromatic-L-amino-acid decarboxylase (AADC)**, also called **DOPA decarboxylase (DDC)**.
It is a **pyridoxal 5'-phosphate (PLP)-dependent** homodimeric decarboxylase of the group II
(fold type I / PLP-dependent transferase) decarboxylase family.

- FUNCTION (UniProt): "Catalyzes the decarboxylation of L-3,4-dihydroxyphenylalanine (DOPA) to
  dopamine and L-5-hydroxytryptophan to serotonin." [file:human/DDC/DDC-uniprot.txt]
- CATALYTIC ACTIVITY 1: "L-dopa + H(+) = dopamine + CO2" (Rhea:RHEA:12272; EC=4.1.1.28) [file:human/DDC/DDC-uniprot.txt]
- CATALYTIC ACTIVITY 2: "5-hydroxy-L-tryptophan + H(+) = serotonin + CO2" (Rhea:RHEA:18533; EC=4.1.1.28) [file:human/DDC/DDC-uniprot.txt]
- COFACTOR: "Name=pyridoxal 5'-phosphate" (ECO:0000269|PubMed:22143761) [file:human/DDC/DDC-uniprot.txt]
- PATHWAY: "Catecholamine biosynthesis; dopamine biosynthesis; dopamine from L-tyrosine: step 2/2." [file:human/DDC/DDC-uniprot.txt]
- SUBUNIT: "Homodimer." (ECO:0000269|PubMed:22143761) [file:human/DDC/DDC-uniprot.txt]
- KW: Catecholamine biosynthesis; Decarboxylase; Lyase; Pyridoxal phosphate [file:human/DDC/DDC-uniprot.txt]
- MOD_RES 303: "N6-(pyridoxal phosphate)lysine" — the catalytic PLP-Schiff-base lysine (PubMed:22143761) [file:human/DDC/DDC-uniprot.txt]

DDC sits at the **branch point** of monoamine neurotransmitter synthesis: it is the second/last step
of the **catecholamine (dopamine)** branch (after tyrosine hydroxylase makes L-DOPA) and of the
**serotonin/indoleamine** branch (after tryptophan hydroxylase makes 5-HTP). It is thus shared between
the dopamine, noradrenaline, adrenaline (catecholamine) and serotonin/melatonin pathways.
Reactome places it in both "Catecholamine biosynthesis" (R-HSA-209905) and "Serotonin and melatonin
biosynthesis" (R-HSA-209931).

## Structure / catalytic mechanism

- Crystal structure (open conformation) at 2.8 A: PMID:22143761 (Giardina et al. 2011, PNAS),
  "Open conformation of human DOPA decarboxylase reveals the mechanism of PLP addition to Group II
  decarboxylases." Established PLP-binding sites (residues 148, 149, 246, 300 bind PLP; Lys303 forms
  the internal aldimine) and homodimer subunit. [file:human/DDC/DDC-uniprot.txt]
- Belongs to the group II decarboxylase family (SIMILARITY). [file:human/DDC/DDC-uniprot.txt]

## Disease

- DISEASE (UniProt): "Aromatic L-amino-acid decarboxylase deficiency (AADCD) [MIM:608643]: An inborn
  error in neurotransmitter metabolism that leads to combined serotonin and catecholamine deficiency."
  Autosomal recessive; developmental/psychomotor delay, ptosis, oculogyric crises, autonomic
  dysfunction. [file:human/DDC/DDC-uniprot.txt] Numerous AADCD missense variants documented (e.g.
  G102S, S147R, S250F, F309L, R347Q) mapping to catalytic/PLP region.

## Interactions / regulation (moonlighting and modulatory)

- **DJ-1 (PARK7, Q99497)** directly binds DDC and positively regulates its activity in human
  dopaminergic cells [PMID:19703902 "we found that DJ-1 directly bound to TH and DDC and positively
  regulated their activities in human dopaminergic cells"]. This paper (full text available) also
  measured DDC / L-DOPA decarboxylase activity directly (IDA) and dopamine synthesis, and describes a
  ternary complex of DJ-1, TH (tyrosine hydroxylase, P07101) and DDC [PMID:19703902 "A ternary complex
  among DJ-1, TH, and DDC was found"]. This grounds the enzyme-binding IPI to TH (P07101).
- **Androgen receptor (AR, P10275)**: DDC was identified as an AR-interacting protein that enhances AR
  transactivation in prostate cancer cells [PMID:12864730 "DDC (L-dopa decarboxylase) was detected
  multiple times as a novel AR-interacting protein... transient transfection of DDC in prostate cancer
  cells strongly enhanced ligand-dependent AR transcriptional activity"]. This is a proposed
  moonlighting / coactivator role, not the core enzymatic function; captured in UniProt INTERACTION
  (P20711; P10275: AR). Non-core.

## Localization

- Cytosolic / cytoplasmic enzyme (Reactome cytosol TAS; PAN-GO/IBA cytoplasm). [file:human/DDC/DDC-uniprot.txt DR GO lines]
- Detected in **urinary exosomes** by large-scale proteomics [PMID:19056867], HDA extracellular
  exosome — consistent with a soluble cytosolic protein being captured in secreted vesicles;
  non-core localization.

## Enzyme-assay / activity references

- PMID:16338639 (Duan et al. 2005): assay of hTH, hGCH1 and hAADC activities for ex vivo PD gene
  therapy; measured AADC activity directly (IDA GO:0004058 / GO:0036467). Abstract focuses on dopamine
  synthesis; serotonin/5-HTP not explicitly assayed in the abstract, but this is an experimental (IDA)
  annotation — retained, not removed. [PMID:16338639]
- PMID:7567987 (Rorsman et al. 1995): identifies AADC (EC 4.1.1.28) as a beta-cell autoantigen and
  restates its catalytic role: "Aromatic L-amino acid decarboxylase catalyzes the decarboxylation of
  L-5-hydroxytryptophan to serotonin and that of L-3,4-dihydroxyphenylalanine to dopamine." TAS support
  for GO:0004058. [PMID:7567987]

## Annotation-review summary (actions)

Core molecular functions:
- GO:0004058 aromatic-L-amino-acid decarboxylase activity (the general MF; IDA/TAS/IBA) — ACCEPT.
- GO:0036468 L-dopa decarboxylase activity (dopamine branch, IDA/ISS) — ACCEPT.
- GO:0036467 5-hydroxy-L-tryptophan decarboxylase activity (serotonin branch, IDA/ISS) — ACCEPT.
- GO:0030170 pyridoxal phosphate binding (cofactor; IEA but structurally verified) — ACCEPT.

Core biological processes:
- GO:0042416 dopamine biosynthetic process (IDA/ISS/IEA) — ACCEPT.
- GO:0042427 serotonin biosynthetic process (IBA) — ACCEPT.
- GO:0006584 catecholamine metabolic process (IBA) — ACCEPT (parent process; core).

Location: GO:0005737 cytoplasm (IBA), GO:0005829 cytosol (TAS) — ACCEPT.

Non-core / general / moonlighting (KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED):
- GO:0006520 amino acid metabolic process; GO:0016830 carbon-carbon lyase; GO:0016831 carboxy-lyase;
  GO:0042401 biogenic amine biosynthetic process — general parent terms (IEA), non-core.
- GO:0005515 protein binding (x2, IPI, AR and DJ-1) — MARK_AS_OVER_ANNOTATED (uninformative bare term;
  underlying interactions real).
- GO:0019899 enzyme binding (IPI, TH via DJ-1 ternary complex) — KEEP_AS_NON_CORE.
- GO:0070062 extracellular exosome (HDA) — KEEP_AS_NON_CORE.
</content>
</invoke>


## 2026-10-17 source-based augmentation

The earlier notes above are retained as an immutable historical prefix, including their original quotations and formatting residue. This appendix supersedes the earlier summary where it treated true broad terms as over-annotations or counted PLP binding as a separate physiological core.

Two substrate-specific catalytic units summarize DDC: L-DOPA decarboxylation in dopamine biosynthesis, and 5-hydroxy-L-tryptophan decarboxylation in serotonin biosynthesis. The same PLP-dependent homodimer performs both. The human apoenzyme structural/kinetic study and the conserved pig-enzyme comparison support the catalytic model, while species and cofactor-occupancy differences are retained [PMID:22143761; PMID:8670114]. The general AADC and PLP annotations remain supported, but they do not become extra duplicate core units. The serotonin-specific annotation from the human assay paper is retained by curator deference; its full substrate-specific methods were not recovered [PMID:16338639]. The rat-insulinoma autoantigen source is TAS background for the conserved chemistry, not a human enzyme assay [PMID:7567987].

Four official products are reconciled at 480, 338, 402 and 387 residues. The 338-residue alt-DDC transcript has direct human placenta/kidney transcript evidence; this does not establish catalytic activity. The other short products are sequence-supported, without demonstrated functional equivalence or inactivity. No gene-level source is retrofitted with an isoform field [PMID:15532536; PMID:22143761].

DDC–DJ-1 binding is a positive contextual observation, supported by actual pulldown and cellular co-IP experiments; it is retained as non-core rather than rejected because the term is generic. The same original contains direct DDC–TH binding in addition to a ternary-complex experiment, so the enzyme-binding row has pair-specific evidence. None of these observations assigns DJ-1 regulation or TH chemistry to DDC [PMID:19703902]. The AR interaction is refined to current nuclear receptor binding. The obsolete androgen-receptor-binding term is excluded. Human curated pairs, the rat-AR fragment experiment and original-access limits are distinguished; reporter enhancement alone is not used to manufacture a chromatin coactivator core [PMID:12864730]. This follows the [actual main project binding instruction](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions).

The urinary-vesicle observation is grounded in the actual source-linked DDC/NP_000781 table row, with 11 listed peptides and reference 2. It supports contextual detection. It does not require extracellular catalytic activity, and it does not establish peptide uniqueness among natural splice products [PMID:19056867]. The table URL, column labels and primary assay locators are provided in [the primary-source notes](DDC-primary-source-notes.md).

The actual 725-node PTHR11999 tree and alignment recover the 480-residue human target exactly. All five relevant IBD nodes lie on its lineage; four correspond to the imported IBA assertions. Literal donor record joins use current typed ancestry. Donor count and target self-evidence are not treated as defects. All 81 branches of the three relevant current ARBA rules were evaluated; two match the target's actual family/domain and lineage features. The third current rule does not match human, but independent chemistry and the preserved historical EC source remain valid. The specific cytosol and dopamine annotations justify narrowing the broad cytoplasm and catecholamine-process coverage. Two fully traversed Reactome reactions identify the PLP-DDC reference homodimer in cytosol, and the actual target activities in two cached GO-CAM models are consistent with the two catalytic cores. Details and public records are in [the evidence guide](DDC-source-evidence.yaml).

The current 28-row query is distinguished from the 27 historical source objects. Normal fetch deterministically added supporting-entity metadata in a working copy; that genuine output was archived, and the original source objects were preserved for this augmentation. No current-query drift rewrites an old source tuple. Meaningful primary quotation anchors are retained once, while duplicated and label-only anchors are consolidated; the old notes prefix remains unchanged. The genuine default Falcon research attempt failed authentication and the configured perplexity-lite fallback failed HTTP 401/quota. No provider report was fabricated. Manual source reads and the independent substrate/product assessment supply this augmentation.


## 2026-10-17 review follow-up: current terms and original-source provenance

The current official QuickGO response confirms that GO:0050681 nuclear androgen receptor binding is obsolete and recommends GO:0016922 nuclear receptor binding with AR identified as the input. The earlier choice of GO:0016922 is retained. The repository ontology row cited in review is timestamped 2026-03-21; its non-obsolete value and historical ancestor table do not establish current term validity. The source guide records the fresh 2026-10-17 official responses, URLs and checksums. The AR claim remains limited to the abstract and curated human interaction records; complete original Methods and the separate historical rat construct are not presented as independently verified full-length human assays.

The sole action change is the existing amino acid metabolic process annotation: MODIFY to GO:0009072 aromatic amino acid metabolic process. DDC performs aromatic amino-acid decarboxylation, so this term is more precise. It refines the imported source assertion without adding a NEW process or another core. The two dopamine- and serotonin-producing core functions stay unchanged, with PLP binding integrated into both.

The short quotations in the primary-source note were independently checked against the separately recovered original HTML and target table. Their provenance does not depend on the normal publication caches containing full text. The guide now supplies structured original URLs, section locators and source digests; unquoted file references connect those assessments to the review. The existing quotation limits remain satisfied without adding or repeating a publication quote. The separate supplemental Figure 1B image remains unread, while its experiment is described in the inspected main Results.

Product descriptions now state the existing sequence and transcript facts directly. All four product IDs, names, sequence notes, lengths and deletion/replacement features are preserved. Activity, localization and physiological equivalence of the natural short products remain unestablished, and inactivity is not inferred. PMID:15532536 supports the alternative transcript isolated from placenta and detected in kidney. No additional human substrate list is inferred from the pig-enzyme abstract or the reviewer's suggestion.

All 27 source annotation dictionaries, cached publications, provider files and earlier journal/history remain unchanged. Apart from the single process refinement, the edits improve source discoverability and readability; no new annotation, core or product function is asserted.
