# COA6 (Q5JTJ3) review notes

Human COA6 (C1orf31), HGNC:18025. 125 aa, ~14 kDa. Chromosome 1.
COA6 has a CHCH fold with a noncanonical C-X9-C-Xn-C-X10-C motif; it is an assembly factor rather than a structural COX6B subunit. The three preserved products have lengths 125, 155 and 79 residues. Product identity does not establish equivalent functional testing.

## Function summary

COA6 is a small mitochondrial intermembrane-space protein whose disulfide-reductase activity supports MT-CO2/COX2 copper-site maturation and respiratory complex-IV assembly. Recombinant human isoform 3 reduces SCO1, SCO2 and COX2; cellular SCO1/SCO2 responses differ with the experimental system [PMID:31851937; PMID:32061935]. The original redox interpretation includes [PMID:31851937, "allowing for copper binding"].

The 2015 authors explicitly concluded that COA6 belongs to the “mitochondrial copper relay system” [PMID:25959673, abstract; https://doi.org/10.1016/j.cmet.2015.04.012]. Their positive COA6/SCO2/COX2 assembly evidence is retained. This is the authors' conclusion, not a claim that isolated human COA6 was shown to transfer copper autonomously.

Human copper-binding capacity is positive [PMID:26160915; PMID:31515291]. The yeast mitochondrial-fraction experiment in PMID:31851937 does not establish a universal human copper-negative result; that study also detects binding after recombinant human protein reconstitution. The physiological carrier model remains unresolved. The former blanket negative in this section is withdrawn, without discarding either experimental result. The 2019 authors concluded [PMID:31851937, "not a Cu-binding protein under physiological conditions"]; this physiological interpretation is distinct from the demonstrated loaded-protein capacity. The earlier study reports [PMID:26160915, "has the capacity to bind copper"] and [PMID:26160915, "subsequent accumulation of complex IV assembly intermediates"].

The initial cross-species study reports a requirement for respiratory-complex-IV biogenesis [PMID:24549041, "shown its requirement for respiratory complex IV biogenesis"], with its experimental organisms distinguished from later human biochemical work.

## Localization

Human mitochondrial fractionation and protease-accessibility evidence supports soluble intermembrane-space localization [PMID:25959673; PMID:25339201 Supplement Figure S1 legend]. Association with COX2 assembly factors occurs near the inner membrane; it does not make COA6 an integral membrane or stable mature-complex-IV subunit.

PMID:24549041 discusses yeast Coa6 import through the MIA pathway, citing prior work [PMID:24549041, "the mitochondrial import of Coa6 is dependent on MIA import machinery"], and shows that cysteine-motif substitutions can affect import or stability. This is retained as the source-specific import context, not recast as a direct human import assay or an import-catalyst function of COA6. The exact twin-CX9C wording is replaced by the noncanonical motif above.

## Interactions (all IPI GO:0005515 in GOA)

- SCO1 (O75880), PMID:26160915 — copper chaperone client
- SCO2 (O43819) + MT-CO2/COX2 (P00403), PMID:25959673 — copper relay partners/client
- COX20 (Q5RI15), PMID:28330871 and PMID:29154948 — COX2 maturation module chaperone
- COX16 (Q9P0S2), PMID:29381136 — COX2 metallation/assembly
- TTC19 (Q6DKK2), DTX2 (Q86UW9), CABP2 (Q9NPB3), PMID:32296183 — positive HuRI binary interactions. Each has three literal records, including validated two-hybrid evidence; the TTC19 record specifies residues 108–380. The earlier unsupported false/indirect characterization is withdrawn.

Supported generic interactions are retained as non-core under the campaign policy. DTX2's verified E3 class supports ubiquitin-protein-ligase binding; TTC19 and CABP2 do not acquire that class merely because their record counts match. COX20's nascent-COX2 stabilization role supports protein-folding-chaperone binding. COX16's recruitment/module-merger function supports assembly association without establishing that chaperone class. These are assay-scoped classifications, not claims of native contact or downstream COA6 signaling.

## Disease

Mitochondrial complex IV deficiency, nuclear type 13 (MC4DN13, MIM:616501):
autosomal recessive fatal infantile hypertrophic cardiomyopathy, left-ventricular
non-compaction, lactic acidosis, complex IV deficiency
[PMID:25339201]. The source concludes [PMID:25339201, "COA6 is required for complex IV subunit stability"].
The W59C variant is associated with mistargeting and disturbed assembly-factor association. Copper rescue in PMID:24549041 is a yeast result; it is not presented as established treatment of affected children. Product and assay boundaries remain explicit in the current assessment below.

## Current annotation judgments

- Protein-disulfide reductase activity is the integrated molecular core; its direct human activity evidence and inherited annotation are retained.
- Copper ion binding is retained as non-core measured capacity, with physiological carriage unresolved.
- General complex-IV assembly terms are refined to mitochondrial complex-IV assembly without altering original term IDs.
- Positive generic protein interactions remain non-core unless a verified partner class supports refinement. They are not marked over-annotated solely because the label is broad.
- The RNA-capture observation remains non-core at its measured contact scope; no RNA-processing function is proposed. The earlier categorical dismissal is withdrawn.
- Broad mitochondrial annotations are preserved or refined according to source and product scope, with IMS localization supported independently.

## Current source-grounded assessment — 2026-10-11

COA6 has one integrated redox/assembly core: protein-disulfide reduction in the mitochondrial intermembrane space, contributing directly to mitochondrial complex-IV assembly. Recombinant human isoform 3 reduces SCO1, SCO2 and COX2. Patient fibroblasts in PMID:31851937 show a SCO1 redox shift with unchanged SCO2 distribution; complete HEK293T knockout and complementation in PMID:32061935 show effects on both SCO proteins. The latter study could not assess COX2 reduction in vivo because COX2 was depleted. Complex-I and import phenotypes do not establish additional direct COA6 activities.

The copper-binding result is retained as non-core. PMID:31515291 measures human isoform-3 Cu(I) binding after purification and copper loading, with competition and cysteine-mutant controls. Its C58S/C90S mutant fails cell rescue while mislocalizing, so that outcome cannot isolate a copper-binding defect from import or folding. PMID:31851937 compares copper peaks in yeast mitochondrial fractions and separately detects binding after recombinant human protein reconstitution. It therefore challenges an autonomous metallochaperone model without disproving measured human binding. Direct physiological copper carriage remains an open question.

Original human fractionation/protease experiments in PMID:25959673 support soluble IMS localization. Its native and two-dimensional separation supports a COA6/SCO2/nascent-COX2 intermediate; this positive simultaneous association is retained without assuming a four-member complex containing SCO1. The official publisher page for PMID:25339201 exposes the original Supplement Figure S1 localization legend, which was read; its inaccessible supplementary PDF was not counted as inspected. HPA XML and MitoCoP proteomics remain broader mitochondrial evidence. The MitoCoP original Table S1 contains Q5JTJ3-3 and a canonical COA6 consensus-gene row, without proving every product was measured.

Positive protein interactions remain supported even when their native role is unresolved. Human COX20 co-isolation is refined to protein-folding chaperone binding based on its nascent-COX2 stabilization role, retaining complex-mediated assay scope. The HuRI DTX2 pair is refined to ubiquitin protein ligase binding from its verified E3 class; this does not imply COA6 ubiquitination. TTC19 includes a tested 108–380 region, and CABP2 is not calmodulin. The historical aggregate rows remain separate from the exact imported partner-scoped objects. These decisions apply the campaign's supported-binding policy; genericity alone does not negate a positive experiment.

RNA contact is also retained as non-core. The authentic PMID:22658674 supplementary table identifies C1orf31/COA6 in the mRNA-interactome set by significant ion-count analysis, although its DESeq result is not significant. The original procedure combines the two statistical outputs after UV crosslinking and stringent oligo-dT isolation. This evidence does not establish a native RNA-processing function, but the inherited nonspecific-capture dismissal lacked target-level support.

All three official alternative products are preserved. Deterministic reconstruction gives lengths 125, 155 and 79 residues; these are sequence facts, not equivalent functional testing. The structural studies use isoform 3, corresponding to canonical residues 47–125, and keep canonical numbering. The motif is noncanonical C-X9-C-Xn-C-X10-C, rather than an exact twin-CX9C repeat. The historical family/import/disease prose above must be read within this corrected scope; clinical necessity does not supply additional performed biological processes.

Separate full-text versions provide the Results and Methods for PMID:24549041 and PMID:28330871. PMID:25959673 was read from its repository-hosted publisher article and supplement; PMID:26160915 remains abstract-only. Full text is available for PMID:31515291 and PMID:32061935. The source index provides the source URLs and locations.

The GO-CAM index has no target match; this absence does not justify a new process assertion.

## Reconciliation of historical annotations

The review intentionally retains 32 historical-plus-current assertions covering 30 current GOA rows. The unscoped HuRI and SCO2/MT-CO2 aggregates overlap the current TTC19/DTX2/CABP2 and SCO2/MT-CO2 partner assertions. They now carry `retired: true`, preserving all original fields and historical actions while leaving 30 active assertions. The active DTX2 decision is the specific ligase-binding refinement; the retired aggregate is not a competing active verdict.

PAINT comments identify the reductase, assembly and mitochondrial-location premises separately. Current experimental grounding on the target is not circular evidence, while the historical ancestral node remains unresolved.

## Source-specific clarifications

The two unscoped aggregate records are historical representations, retired from the active set rather than deleted or rewritten as different GOA assertions. Each of the 30 current source tuples maps once to an active review object. Twelve older active objects lack a supporting-entity list; their complete current WITH/FROM values remain in the source index. This is unique source-compatible coverage, not equality of every field. Original source fields and historical records remain inspectable.

The DTX2 yeast interaction supports a partner-class statement. It does not establish a native route between mature IMS COA6 and cytosolic/nuclear DTX2. Similarly, the RNA-capture experiment does not identify which COA6 cellular pool or product contacted poly(A) RNA. These are biological limits, not evidence that the positive records are false. The exact supplementary p.adj.IC value is an adjusted P value; FDR 0.01 is the authors' selection threshold. Public original source URLs, hashes and locators are in the source-evidence index.

Copper binding was measured after deliberate copper loading under reducing conditions. The two 2019 studies agree that reconstituted recombinant protein can bind copper, while differing in their physiological interpretation. Their assays do not constitute a direct matched-condition refutation of one another; neither is marked invalid or experimentally overturned. Physiological copper carriage remains unresolved alongside the established reductase function.
