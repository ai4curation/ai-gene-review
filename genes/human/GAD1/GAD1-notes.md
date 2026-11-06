# GAD1 (Q99259) review notes

Deep research: falcon provider was OUT OF CREDITS (HTTP 402) at review time, so no
`GAD1-deep-research-falcon.md` was generated. This review is grounded in the UniProt
record (`GAD1-uniprot.txt`), the seeded GOA (`GAD1-goa.tsv`), and cached
`publications/PMID_*.md`.

## Identity / core biology

- GAD1 = glutamate decarboxylase 1, a.k.a. GAD67 / 67 kDa glutamic acid decarboxylase
  (UniProt DCE1_HUMAN, Q99259; HGNC:4092; chromosome 2q31).
- Pyridoxal-5'-phosphate (PLP)-dependent enzyme; EC 4.1.1.15; group II decarboxylase
  family. PLP is covalently bound at Lys405 (N6-(pyridoxal phosphate)lysine)
  [GAD1-uniprot.txt FT MOD_RES 405].
- Catalyzes L-glutamate -> 4-aminobutanoate (GABA) + CO2 (RHEA:17785)
  [GAD1-uniprot.txt CATALYTIC ACTIVITY].
- GAD67 is the **constitutively active** isoform responsible for basal GABA production;
  the paralog GAD2/GAD65 is the synaptic-vesicle-associated form that is transiently
  activated on demand [PMID:17384644 abstract: "GAD67 is constitutively active and is
  responsible for basal GABA production. In contrast, GAD65 ... is transiently
  activated"].
- Homodimer [GAD1-uniprot.txt SUBUNIT; PMID:17384644].
- Localization: cytosolic (neuronal). Note GOA cytoplasm (IBA) and Reactome CC terms
  (plasma membrane, clathrin-sculpted GABA transport vesicle membrane, vesicle
  membrane) describe pathway/vesicle-context localization rather than the enzyme's own
  soluble cytosolic activity; GAD67 lacks the N-terminal palmitoylation-based membrane
  anchoring that targets GAD65 to vesicles.

## Structure / mechanism references (cited in UniProt)

- PMID:17384644 (Fenalti 2007, Nat Struct Mol Biol): crystal structures of GAD67 &
  GAD65; GAD67 has a tethered catalytic loop covering the active site sustaining GABA
  production. Provides CATALYTIC ACTIVITY, COFACTOR (PLP), SUBUNIT (homodimer), FUNCTION.
  Source of IDA for glutamate decarboxylase activity, GABA shunt, identical protein binding.
- PMID:23126365 (Langendorf 2013): GAD auto-activation structure. Not in GOA/references
  list; not cited.
- PMID:10671565 (Chessler & Lernmark 2000): describes GAD25 (isoform 3), a
  catalytically **inactive** splice variant in non-neural tissue; establishes GAD67
  enzymatic activity and L-glutamate catabolic role. Note isoform 3 = enzymatically
  inactive; the IDA glutamate decarboxylase / L-glutamate catabolic annotations refer
  to full-length GAD67 (isoform 1).

## Disease

- Bi-allelic GAD1 variants -> developmental and epileptic encephalopathy 89 (DEE89,
  MIM:619124), autosomal recessive [PMID:32282878, cited in UniProt; not cached].
- Homozygous missense S12C associated with autosomal recessive spastic cerebral palsy
  [PMID:15571623, cited in UniProt; not cached]; note PMID:33634263 later attributes
  CPSQ1 to HPDL, so the cerebral-palsy attribution is caveated. Consistent with GAD1's
  role in supplying the major inhibitory neurotransmitter GABA.

## GOA annotation assessment summary

- MF glutamate decarboxylase activity (GO:0004351): CORE. Supported by IDA (PMID:17384644,
  PMID:10671565), IBA, and IEA(ARBA EC 4.1.1.15 / RHEA:17785). ACCEPT.
- MF pyridoxal phosphate binding (GO:0030170) IEA(InterPro): CORE cofactor. ACCEPT
  (PLP is the essential cofactor, Lys405 Schiff base).
- MF carbon-carbon lyase / carboxy-lyase (GO:0016830 / GO:0016831) IEA(InterPro):
  correct parents of glutamate decarboxylase activity but less informative; MARK_AS_OVER_ANNOTATED.
- BP GABA biosynthetic process (GO:0009449) IBA + IEA: CORE. ACCEPT.
- BP GABA shunt (GO:0006540) IDA/TAS/IEA: KEEP (metabolic-context process); the IDA
  (PMID:17384644) reflects the decarboxylation step feeding the shunt.
- BP L-glutamate catabolic process (GO:0006538) TAS(PMID:10671565): ACCEPT as broader
  correct process (glutamate is consumed).
- BP chemical synaptic transmission (GO:0007268) TAS: KEEP_AS_NON_CORE — downstream
  physiological role via GABA, not GAD1's own molecular action.
- CC cytoplasm (GO:0005737) IBA: ACCEPT (soluble/cytosolic enzyme).
- CC presynaptic active zone (GO:0048786) IBA: KEEP_AS_NON_CORE (mostly GAD65-context;
  GAD67 basal cytosolic, only partly synaptically localized).
- CC plasma membrane (GO:0005886) TAS Reactome, vesicle membrane (GO:0012506) NAS,
  clathrin-sculpted GABA transport vesicle membrane (GO:0061202) TAS: these are Reactome
  pathway-context / vesicle-membrane placements; GAD67 (unlike palmitoylated GAD65) is
  soluble cytosolic, so these overstate GAD67's own localization. MARK_AS_OVER_ANNOTATED.
- MF protein binding (GO:0005515) IPI x11: all from large-scale interactome / SH3-array /
  variant-interactome screens (PMID:16189514, 17474147, 21516116, 25416956, 26871637,
  31515488, 32296183) and one small-scale (PMID:10671565). Uninformative bare
  `protein binding`; per policy MARK_AS_OVER_ANNOTATED (not REMOVE).
- MF identical protein binding (GO:0042802) IDA (PMID:17384644): supports the homodimer;
  ACCEPT (structurally verified homodimer).
</content>


## 2026-11-02: source-grounded augmentation (private proposal)

This dated entry supersedes the biological interpretations above where they differ; the earlier journal remains unchanged as historical provenance. The proposed review now covers all 50 current literal GOA contexts, four declared products and one catalytic core. No NEW annotation is proposed. Genuine native reconciliation and target validation have not yet been performed.

The catalytic core is GAD67-mediated, PLP-dependent conversion of L-glutamate to GABA and carbon dioxide. Original activity experiments compare active full-length GAD67 with inactive GAD25, rather than supporting a gene-wide loss of enzyme function (PMID:10671565, original Methods/Results/Figure 4). Human clone activity (PMID:1549570) and structural/catalytic evidence (PMID:17384644; official PDB 2OKJ) corroborate this. The crystallization entity is an engineered 504-residue truncation with terminal HH, distinct from natural products. Current sequences are 594, undescribed, 224 and 425 residues; Q99259-2 has no described sequence, and the 425-residue product is not assigned untested catalytic equivalence.

The old exclusive soluble-versus-vesicle contrast was too strong. Actual GAD67 immunostaining supports cytoplasm and inhibitory presynaptic terminals (PMID:15347806, 23258346, 24613359), while the exact official Q99259 Reactome component R-HSA-888580 participates in a vesicle-associated GAD1:GAD2 model. This does not prove every product is membrane-bound or that reaction-level plasma-membrane compartments locate every participant. Active-zone placement retains actual PAINT and donor curatorial provenance, with the inaccessible original marker panels explicitly distinguished from independently read broader terminal staining. Perinuclear, cell-cortex and event-level plasma-membrane specificity remain unresolved. GFP cell identity is not silently substituted for a protein-localization assay.

The NCK1 screen supports SH3-domain binding by a GAD1 peptide (PMID:17474147, Table S2). Other positive binary pairs remain supported with actual clone/suffix scope, while their generic protein-binding annotations are removed as uninformative. This policy decision does not negate the experiments or establish a more specific molecular function. PMID:21516116 does not recover the incoming AGTRAP pair in its complete available table; independent positives elsewhere are preserved without pretending to repair that citation. HAAO variants belong to HAAO, and study GAD1 clone numbers are not current UniProt suffixes. See the source guide for the exact target-table and original-access limits.

GAD1 performs the first chemical step of the GABA shunt, but the broader complete-pathway flux is not measured by every cited assay. The chemical-synaptic-transmission term concerns release and receptor activation; neurotransmitter synthesis alone does not establish GAD1's own participation in those steps, so the specific PMID:8954991 TAS remains uncertain. No new developmental process is inferred from knockout necessity.

The original 32-row review and all 37 quotation associations remain preserved by immutable Git/private copies and public hash/locator provenance. The old cytosol NEW is archived rather than silently treated as incoming GOA: the actual ancestral assertion is cytoplasm, its family-membership quote is not a localization assay, and a new descendant would duplicate existing coverage. Two precise inherited excerpts remain active; 35 old associations remain historical only. Earlier source descriptions and action summaries above are historical, not the current judgments. Current decisions and all 32 manual reference assessments appear only in the review; the compact source archive preserves raw contexts, products, source inventory and history without a second current-review copy.

## 2026-11-02: generic interaction-term policy

The thirteen resolved positive interaction contexts retain their source-specific pair, assay and construct evidence, but use REMOVE for the uninformative GO:0005515 term. The NCK1-domain interaction retains its supported SH3-binding refinement; two unresolved source-specific binding claims remain UNDECIDED. Earlier journal statements about a different generic-binding policy are historical. No interaction is declared false by this policy correction.

## 2026-11-02: genuine native reconciliation

The actual UniProt snapshot and 50-row, 16-column GOA export match the independently inspected inputs. A private genuine native seed resolves all 50 current joins without seeding over the inherited review. The four product records, including undescribed Q99259-2, are exact. All 46 normal sources are present: 21 reused main files remain unchanged and 25 previously missing files were acquired. A transient UniProt HTTP 500 stopped the first target fetch before target writes; one ordinary retry succeeded, with the original diagnostic retained.

Both actively reused historical excerpts are exact native-cache substrings. All 37 original quotation associations and the inherited 32-row review remain available through the immutable historical locators. Newly available cache full text does not imply a broader primary reading than the reference assessments state. The six source-specific uncertainties remain; no NEW assertion is added. Scoped validation and rendering outcomes are pending.

## 2026-11-02: scoped validation outcomes

Default schema, ontology, reference and best-practice validation passed with zero advisories. Strict GOA reconciliation confirms all 50 current annotations and no NEW. The status audit computed COMPLETE, preserving all six UNDECIDED scientific judgments; the initial DRAFT mismatch remains in the execution record. Native EDIT history, final status and the private 50-row/one-core/32-reference render passed. All 46 scientific sources remain unchanged by authored curation, and the GO term cache is unchanged.


## 2026-11-04 — Catalysis, products and the vesicle-associated pool

GAD67 supplies basal GABA by PLP-dependent glutamate decarboxylation. Human GAD67 cDNA yields active enzyme in bacterial expression; the GAD65/GAD67 catalytic study distinguishes constitutive GAD67 activity from the more regulated GAD65 enzyme ([PMID:1549570](https://pubmed.ncbi.nlm.nih.gov/1549570/), [PMID:17384644](https://pubmed.ncbi.nlm.nih.gov/17384644/)). The human GAD1 structure is a catalytic homodimer. Its crystallization construct spans canonical residues 93–594 plus two histidines and is not a naturally spliced product. GAD25 inactivity belongs to that specific alternative product and does not negate full-length GAD67 catalysis ([PMID:10671565](https://pubmed.ncbi.nlm.nih.gov/10671565/), [PDB 2OKJ](https://www.rcsb.org/structure/2OKJ)).

The curated human Q99259 component [R-HSA-888580](https://reactome.org/content/detail/R-HSA-888580) supplies one consistent vesicle-membrane pool. It occurs in the GAD1 homodimer reaction and in GAD1:GAD2 vesicle assemblies. The broad vesicle row is now non-core, matching the four specialized transport-vesicle rows. Neither this placement nor the tentative microvesicle discussion in the GAD25 paper makes all GAD67 membrane-bound, proves exclusively heterodimer-mediated recruitment, or assigns targeting to every splice product. Cytoplasmic and inhibitory presynaptic GAD67 remain supported independently.

The six unresolved annotations remain explicit source-access or source-join questions. In particular, GABA production alone cannot recover the uninspected experiment underlying the transmission TAS annotation; this is uncertainty rather than a conclusion that transmission participation is absent. The two unresolved generic-binding claims also retain their source-specific uncertainty. Positive, verified but uninformative interaction annotations remain removed under the binding policy without denying the underlying interactions.

Six concise, exact source excerpts now anchor the review, with no source exceeding 25 quoted words across the current review and this appended section. The excerpts occur only in the review; the [source guide](GAD1-source-guide.md) supplies public source and supplement locators, and the [historical review](https://github.com/ai4curation/ai-gene-review/blob/b89135d957068000f0eac9919c9d75a41bf474c5/genes/human/GAD1/GAD1-ai-review.yaml) preserves all 37 original quotation associations. Earlier journal entries above describe their own historical stages.

The amendment passed target validation with zero advisories, strict matching of all 50 GOA rows, native EDIT history validation, the COMPLETE status audit, private rendering and whitespace checks. All six scientific uncertainties remain explicit. All 50 original machine records, 46 scientific sources and four product records are unchanged.


## 2026-11-04 — Participant compartments and enzyme chemistry

The GABA-release model distinguishes the membrane that a vesicle approaches from the compartment of each molecular participant. Its summary assigns SNAP25 and syntaxin to the plasma membrane, while the human Q99259 component is assigned to the GABA transport-vesicle membrane. The plasma-membrane TAS mapping therefore exceeds this specific participant evidence, without implying that GAD1 is absent from the release event or biologically excluded from the cell surface ([Reactome:R-HSA-888589](https://reactome.org/content/detail/R-HSA-888589); [Reactome:R-HSA-888580](https://reactome.org/content/detail/R-HSA-888580)).

The UniProt SUBUNIT statement supplies a direct curated homodimer anchor with experimental evidence from PMID:17384644; the PDB cross-reference separately identifies the engineered chain range. The pathway model includes both GAD1 homodimer and GAD1:GAD2 assemblies. Full-length GAD67 directly consumes L-glutamate in the radiolabeled conversion assay as it produces GABA, so the single catalytic core now includes both established process facets. These GO terms have no is_a or part_of ancestry relationship to each other; no additional annotation is manufactured ([PMID:10671565](https://pubmed.ncbi.nlm.nih.gov/10671565/); [PMID:17384644](https://pubmed.ncbi.nlm.nih.gov/17384644/); [Reactome:R-HSA-888572](https://reactome.org/content/detail/R-HSA-888572)).

The remaining five uncertain judgments are unchanged. In particular, the unresolved PMID:21516116 GAD1–AGTRAP source join remains distinct from independent positive interaction evidence in other papers. Access to a whole paper does not by itself settle every source-specific attribution.

Target validation passed with zero advisories; strict GOA matched all 50 originals. Native EDIT history, COMPLETE status audit, private 50-row/one-core/32-reference rendering and whitespace checks passed. Five source-specific UNDECIDED judgments remain; all 46 scientific sources are unchanged.
