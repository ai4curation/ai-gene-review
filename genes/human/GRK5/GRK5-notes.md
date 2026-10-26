# GRK5: signaling-regulator evidence review

All original annotation payloads, evidence codes, references and qualifiers were preserved. No new annotations were manufactured to populate a module. Actual Falcon and fallback research attempts failed authentication/quota; this is manual literature research, not provider-generated prose.

The whole record was reviewed, including secondary physiology and localization. Existing assertion specificity is judged independently of evidence code. Native, heterologous, mutant and orthology-based results are distinguished below.

## GO:0004672 protein kinase activity — MODIFY
GRK5 is a serine/threonine kinase with GPCR and non-receptor substrates, including p53. Refine the generic kinase term to the supported residue specificity rather than restrict every catalytic row to GPCR substrates.
Sources: PMID:20124405, PMID:8288567

## GO:0004674 protein serine/threonine kinase activity — ACCEPT
Purified GRK5 phosphorylates activated beta2-adrenergic, M2-muscarinic and rhodopsin receptors using ATP, and independent experiments establish non-receptor serine/threonine substrates. Retain catalytic and ATP-binding functions with substrate-specific assay scope.
Sources: PMID:8288567, PMID:20038610, PMID:20124405

## GO:0004703 G protein-coupled receptor kinase activity — ACCEPT
Purified GRK5 phosphorylates activated beta2-adrenergic, M2-muscarinic and rhodopsin receptors using ATP, and independent experiments establish non-receptor serine/threonine substrates. Retain catalytic and ATP-binding functions with substrate-specific assay scope.
Sources: PMID:8288567, PMID:20038610, PMID:20124405

## GO:0047696 beta-adrenergic receptor kinase activity — ACCEPT
Purified GRK5 phosphorylates activated beta2-adrenergic, M2-muscarinic and rhodopsin receptors using ATP, and independent experiments establish non-receptor serine/threonine substrates. Retain catalytic and ATP-binding functions with substrate-specific assay scope.
Sources: PMID:8288567, PMID:20038610, PMID:20124405

## GO:0005524 ATP binding — ACCEPT
Purified GRK5 phosphorylates activated beta2-adrenergic, M2-muscarinic and rhodopsin receptors using ATP, and independent experiments establish non-receptor serine/threonine substrates. Retain catalytic and ATP-binding functions with substrate-specific assay scope.
Sources: PMID:8288567, PMID:20038610, PMID:20124405

## GO:0005080 protein kinase C binding — UNDECIDED
The source establishes phosphorylation/regulation of GRK5 by protein kinase C, but the accessible text does not resolve whether an independently demonstrated binary PKC-binding interaction supports this specific binding term. Substrate phosphorylation alone does not specify the affinity/association claim; it remains unresolved.
Sources: PMID:9813065

## GO:0005515 protein binding — REMOVE
Remove bare protein binding as uninformative under the project policy, while preserving specific catalytic, lipid-binding and receptor-regulatory functions.
Source handling: original payload retained; no fabricated supporting quote.

## GO:0005543 phospholipid binding — ACCEPT
The C-terminal region directly mediates phospholipid interaction and membrane-dependent regulation. This binding is integral to localization and catalysis rather than a peripheral annotation.
Sources: PMID:9813065, PMID:14976207

## GO:0005634 nucleus — KEEP_AS_NON_CORE
Nuclear GRK5 activity and p53 regulation support a nuclear pool independently of the predominant plasma-membrane role. Retain the compartment without asserting exclusively nuclear localization.
Sources: PMID:20124405

## GO:0005737 cytoplasm — ACCEPT
GRK5 has an intracellular cytoplasmic pool and membrane-associated activity. Cellular localization studies support the broad cytoplasmic assertion without excluding the separately supported nuclear pool.
Sources: PMID:14976207, PMID:17986524

## GO:0005886 plasma membrane — ACCEPT
Full-length GRK5 localization and C-terminal amphipathic-region mutagenesis establish plasma-membrane targeting; NK1 experiments additionally show receptor preassociation. Retain this experimentally supported compartment.
Sources: PMID:14976207, PMID:17986524

## GO:0007165 signal transduction — MODIFY
The protein has specifically established regulation of GPCR signaling, more informative than generic signal transduction or its regulation. Refine those broad terms while retaining separate non-receptor nuclear functions.
Sources: PMID:8288567, PMID:17986524

## GO:0009966 regulation of signal transduction — MODIFY
The protein has specifically established regulation of GPCR signaling, more informative than generic signal transduction or its regulation. Refine those broad terms while retaining separate non-receptor nuclear functions.
Sources: PMID:8288567, PMID:17986524

## GO:0007186 G protein-coupled receptor signaling pathway — ACCEPT
Direct phosphorylation of activated receptors and functional desensitization/coupling assays establish GPCR regulation as a core role. Regulatory outcomes depend on receptor and cellular context.
Sources: PMID:8288567, PMID:17986524

## GO:0008277 regulation of G protein-coupled receptor signaling pathway — ACCEPT
Direct phosphorylation of activated receptors and functional desensitization/coupling assays establish GPCR regulation as a core role. Regulatory outcomes depend on receptor and cellular context.
Sources: PMID:8288567, PMID:17986524

## GO:0007188 adenylate cyclase-modulating G protein-coupled receptor signaling pathway — KEEP_AS_NON_CORE
The rat thyroid-cell study demonstrates GRK5-dependent regulation of TSH receptor/cAMP responsiveness. Retain this comparative receptor-specific cyclase-modulating implementation, not direct phosphorylation or catalysis of adenylyl cyclase itself.
Sources: PMID:8626574

## GO:0007217 tachykinin receptor signaling pathway — KEEP_AS_NON_CORE
The NK1 study shows GRK5 preassociation and kinase-dependent receptor interaction changes, providing a tachykinin signaling implementation distinct from GRK2 recruitment.
Sources: PMID:17986524

## GO:0008284 positive regulation of cell population proliferation — KEEP_AS_NON_CORE
Human prostate-cancer cell knockdown/rescue experiments link GRK5 kinase activity to proliferation and cell-cycle progression. Retain these tested cellular effects without making them universal properties of every GRK5-expressing tissue.
Sources: PMID:22099983

## GO:0051726 regulation of cell cycle — KEEP_AS_NON_CORE
Human prostate-cancer cell knockdown/rescue experiments link GRK5 kinase activity to proliferation and cell-cycle progression. Retain these tested cellular effects without making them universal properties of every GRK5-expressing tissue.
Sources: PMID:22099983

## GO:0016607 nuclear speck — UNDECIDED
The HPA fine-localization annotations are preserved, but target-specific images for nuclear speckles/nuclear membrane were not inspected. Independent nuclear function supports nucleus, not either finer microdomain by itself; neither precise claim is rejected on the basis of plasma-membrane localization.
Sources: PMID:20124405

## GO:0031965 nuclear membrane — UNDECIDED
The HPA fine-localization annotations are preserved, but target-specific images for nuclear speckles/nuclear membrane were not inspected. Independent nuclear function supports nucleus, not either finer microdomain by itself; neither precise claim is rejected on the basis of plasma-membrane localization.
Sources: PMID:20124405

## GO:0043066 negative regulation of apoptotic process — KEEP_AS_NON_CORE
The paper concludes that GRK5 phosphorylation of p53 promotes p53 degradation and reduces p53-dependent apoptosis, with increased irradiation-induced apoptosis in GRK5-deficient mice. Retain the negative regulatory outcome; the abstract contains inconsistent knockdown wording, so this judgment follows the mechanistic results/discussion rather than that isolated sentence.
Sources: PMID:20124405

## GO:0045444 fat cell differentiation — KEEP_AS_NON_CORE
Grk5-null mouse fibroblasts and preadipocytes show impaired adipogenic differentiation under induction, supporting a conserved regulatory role. Retain the native-mouse/orthology scope rather than infer human adipogenesis from expression alone.
Sources: PMID:22507984

## Research and access
Normal publication fetches and targeted refreshes are logged under `.cache/module-audit-logs/acetylcholine-*`. Canonical abstract-only caches were not manually rewritten. Full publisher recovery for cone localization is cited separately. PAINT assertions are treated as ancestral-node judgments, not pairwise transfers; target appearance among descendant evidence is not circular.

## Validation
Focused strict/schema, source/quote and ontology checks, record-section backfill, rendering and helper-generated history are recorded in the final panel proof.

## Final source and propagation audit

Original machine payloads and all qualifiers were compared with the authoritative baseline. There are no NOT assertions or new annotation rows in this 15-target panel. Full sources were inspected where a source-specific sign/mechanism challenge required them; unresolved fine-localization/source claims are retained as UNDECIDED rather than inferred absent. Bare binding removals apply the project policy and do not dispute experimental interactions.

UniProt/PANTHER placement inspected: `PTHR24355:SF27`. Broad G-alpha family PTHR10218 is GTP-BINDING PROTEIN ALPHA SUBUNIT; GRK PTHR24355 is G PROTEIN-COUPLED RECEPTOR KINASE/RIBOSOMAL PROTEIN S6 KINASE. Surprising official family names were not mechanically repointed. RGS6 current PTHR45746 placement does not invalidate a historical PAINT PTHR10845 assertion by itself.
