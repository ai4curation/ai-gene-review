> Note correction provenance: this version explicitly corrects the outdated conclusions in the inherited sections below. The complete previously published notes (SHA-256 92656c345c721f9d337cb8d6daec3e8118af8b4b06d92c2595a5e132a32ae140) and the earlier original notes are preserved in the immutable review packet. Corrections are itemized at the end; no old history record is rewritten. Earlier quotations remain faithful cited paraphrases where restoring them would exceed the per-source quotation budget.

# COA6 (Q5JTJ3) review notes

Human COA6 (C1orf31), HGNC:18025. 125 aa, ~14 kDa. Chromosome 1.
COA6 has a CHCH fold with a noncanonical C-X9-C-Xn-C-X10-C motif; it is an assembly factor rather than a structural COX6B subunit. The three preserved products have lengths 125, 155 and 79 residues. Product identity does not establish equivalent functional testing.

## Function summary

COA6 is a small mitochondrial intermembrane-space protein whose disulfide-reductase activity supports MT-CO2/COX2 copper-site maturation and respiratory complex-IV assembly. Recombinant human isoform 3 reduces SCO1, SCO2 and COX2; cellular SCO1/SCO2 responses differ with the experimental system [PMID:31851937; PMID:32061935].

The 2015 authors explicitly concluded that COA6 belongs to the “mitochondrial copper relay system” [PMID:25959673, abstract; https://doi.org/10.1016/j.cmet.2015.04.012]. Their positive COA6/SCO2/COX2 assembly evidence is retained. This is the authors' conclusion, not a claim that isolated human COA6 was shown to transfer copper autonomously.

Human copper-binding capacity is positive [PMID:26160915; PMID:31515291]. The yeast mitochondrial-fraction experiment in PMID:31851937 does not establish a universal human copper-negative result; that study also detects binding after recombinant human protein reconstitution. The physiological carrier model remains unresolved. The former blanket negative in this section is withdrawn, without discarding either experimental result.

## Localization

Human mitochondrial fractionation and protease-accessibility evidence supports soluble intermembrane-space localization [PMID:25959673; PMID:25339201 Supplement Figure S1 legend]. Association with COX2 assembly factors occurs near the inner membrane; it does not make COA6 an integral membrane or stable mature-complex-IV subunit.

PMID:24549041 discusses yeast Coa6 import through the MIA pathway, citing prior work, and shows that cysteine-motif substitutions can affect import or stability. This is retained as the source-specific import context, not recast as a direct human import assay or an import-catalyst function of COA6. The exact twin-CX9C wording is replaced by the noncanonical motif above.

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
[PMID:25339201].
The W59C variant is associated with mistargeting and disturbed assembly-factor association. Copper rescue in PMID:24549041 is a yeast result; it is not presented as established treatment of affected children. Product and assay boundaries remain explicit in the current assessment below.

## Schema notes

- core_functions[].directly_involved_in is a LIST of Term.
- suggested_questions is a list of Question objects (key: question, optional experts).
- suggested_experiments is a list of Experiment objects (key: description, optional
  hypothesis/experiment_type).

## Current annotation judgments

- Protein-disulfide reductase activity is the integrated molecular core; its direct human activity evidence and inherited annotation are retained.
- Copper ion binding is retained as non-core measured capacity, with physiological carriage unresolved.
- General complex-IV assembly terms are refined to mitochondrial complex-IV assembly without altering original term IDs.
- Positive generic protein interactions remain non-core unless a verified partner class supports refinement. They are not marked over-annotated solely because the label is broad.
- The RNA-capture observation remains non-core at its measured contact scope; no RNA-processing function is proposed. The earlier categorical dismissal is withdrawn.
- Broad mitochondrial annotations are preserved or refined according to source and product scope, with IMS localization supported independently.

## Current source-grounded assessment — 2026-10-11

The source set contains 32 review assertions: all 27 historical objects, including two unscoped aggregates, plus five exact current GOA objects for SCO2, MT-CO2, TTC19, DTX2 and CABP2. These are imported machine assertions, not five proposed biological annotations. All 30 current normal tuples are covered. The original three products and 17 reference identities remain intact.

COA6 has one integrated redox/assembly core: protein-disulfide reduction in the mitochondrial intermembrane space, contributing directly to mitochondrial complex-IV assembly. Recombinant human isoform 3 reduces SCO1, SCO2 and COX2. Patient fibroblasts in PMID:31851937 show a SCO1 redox shift with unchanged SCO2 distribution; complete HEK293T knockout and complementation in PMID:32061935 show effects on both SCO proteins. The latter study could not assess COX2 reduction in vivo because COX2 was depleted. Complex-I and import phenotypes do not establish additional direct COA6 activities.

The copper-binding result is retained as non-core. PMID:31515291 measures human isoform-3 Cu(I) binding after purification and copper loading, with competition and cysteine-mutant controls. Its C58S/C90S mutant fails cell rescue while mislocalizing, so that outcome cannot isolate a copper-binding defect from import or folding. PMID:31851937 compares copper peaks in yeast mitochondrial fractions and separately detects binding after recombinant human protein reconstitution. It therefore challenges an autonomous metallochaperone model without disproving measured human binding. Direct physiological copper carriage remains an open question.

Original human fractionation/protease experiments in PMID:25959673 support soluble IMS localization. Its native and two-dimensional separation supports a COA6/SCO2/nascent-COX2 intermediate; this positive simultaneous association is retained without assuming a four-member complex containing SCO1. The official publisher page for PMID:25339201 exposes the original Supplement Figure S1 localization legend, which was read; its inaccessible supplementary PDF was not counted as inspected. HPA XML and MitoCoP proteomics remain broader mitochondrial evidence. The MitoCoP original Table S1 contains Q5JTJ3-3 and a canonical COA6 consensus-gene row, without proving every product was measured.

Positive protein interactions remain supported even when their native role is unresolved. Human COX20 co-isolation is refined to protein-folding chaperone binding based on its nascent-COX2 stabilization role, retaining complex-mediated assay scope. The HuRI DTX2 pair is refined to ubiquitin protein ligase binding from its verified E3 class; this does not imply COA6 ubiquitination. TTC19 includes a tested 108–380 region, and CABP2 is not calmodulin. The historical aggregate rows remain separate from the exact imported partner-scoped objects. These decisions apply the campaign's supported-binding policy; genericity alone does not negate a positive experiment.

RNA contact is also retained as non-core. The authentic PMID:22658674 supplementary table identifies C1orf31/COA6 in the mRNA-interactome set by significant ion-count analysis, although its DESeq result is not significant. The original procedure combines the two statistical outputs after UV crosslinking and stringent oligo-dT isolation. This evidence does not establish a native RNA-processing function, but the inherited nonspecific-capture dismissal lacked target-level support.

All three official alternative products are preserved. Deterministic reconstruction gives lengths 125, 155 and 79 residues; these are sequence facts, not equivalent functional testing. The structural studies use isoform 3, corresponding to canonical residues 47–125, and keep canonical numbering. The motif is noncanonical C-X9-C-Xn-C-X10-C, rather than an exact twin-CX9C repeat. The historical family/import/disease prose above must be read within this corrected scope; clinical necessity does not supply additional performed biological processes.

Access was checked source by source. Existing main publication caches remain exact. Separate genuine full variants provide the missing Results/Methods for PMID:24549041 and PMID:28330871. PMID:25959673 was read from its authentic repository-hosted publisher article and supplement; PMID:26160915 remains abstract-only. The two new genuine full caches are PMID:31515291 and PMID:32061935. Short literal anchors appear only in the YAML; the source index contains records, URLs, hashes and paraphrases, not duplicate quotations.

The genuine default Falcon attempt timed out, and the recorded fallback returned an insufficient-quota error. No provider report was fabricated. This manual assessment and the original primary evidence underpin the review. The GO-CAM index has no target match; this absence does not justify a new process assertion.

## PR #4857 follow-up — source and policy dispositions

The supported-binding rule comes from the ClinGen campaign's explicit project/user override, reproduced in the current project policy at [CLINGEN_MENDELIAN.md](../../../projects/CLINGEN_MENDELIAN.md). It supersedes the generic instruction to remove uninformative protein binding. This does not waive evidence review: the nine HuRI records, mapped sequences and official partner classes were checked again. Comparable assay counts do not require identical partner-class terms.

The review intentionally retains 32 historical-plus-current assertions covering 30 current GOA rows. Historical aggregates 6 and 24 overlap current partner rows 29–31 and 27–28 respectively. Their supporting entities are not silently rewritten; these rows preserve source history and must not be counted as independent experimental replication.

The superseded early note statements have now been corrected in place, with exact old/new text retained in the follow-up provenance: COX6B-family wording, universal copper negation, exact motif and import scope, HuRI false/indirect language, blanket binding/RNA overannotation, and unqualified copper-rescue wording. The prior current-assessment section remains intact. The original authors' copper-relay conclusion is stated explicitly above with one short verbatim anchor; larger inherited quotations are not restored. Public DOI/repository and source-index locators keep the evidence checkable without duplicating quotations.

PAINT comments now identify the actual reductase, assembly and mitochondrial-location premises separately. Current experimental grounding on the target is not circular evidence, while the historical ancestral node remains unresolved. No source objects, products, core terms or old history records change. The publication history for this amendment will be created by ROOT and can link PR #4857; existing records with an empty PR list remain append-only.

### Validation disposition

Ordinary validation, derived-status check and rendering passed on the finite candidate with nine advisories: eight positive generic-binding NC decisions retained under the explicit campaign override, plus the source-specific broad mitochondrial ACCEPT/IMS-refinement difference. The derived status is unchanged. These are reviewed scientific dispositions, not bypassed checks. No new cache, source object or history edit is included in this owner packet.
