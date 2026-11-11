# GNA14: signaling-regulator evidence review

All original annotation payloads, evidence codes, references and qualifiers were preserved. No new annotations were manufactured to populate a module. Actual Falcon and fallback research attempts failed authentication/quota; this is manual literature research, not provider-generated prose.

The whole record was reviewed, including secondary physiology and localization. Existing assertion specificity is judged independently of evidence code. Native, heterologous, mutant and orthology-based results are distinguished below.

## GO:0003924 GTPase activity — ACCEPT
GNA14 is a guanine-nucleotide-binding G alpha subunit that switches between GDP- and GTP-bound states and hydrolyzes bound GTP. Receptor/effector biochemistry and nucleotide-state experiments support the intrinsic molecular switch. This is distinct from the GAP activity of RGS proteins; activated or nucleotide-defective mutants are controls, not substitutes for the wild-type function.
Sources: PMID:26377666, PMID:18406577

## GO:0003925 G protein activity — ACCEPT
GNA14 is a guanine-nucleotide-binding G alpha subunit that switches between GDP- and GTP-bound states and hydrolyzes bound GTP. Receptor/effector biochemistry and nucleotide-state experiments support the intrinsic molecular switch. This is distinct from the GAP activity of RGS proteins; activated or nucleotide-defective mutants are controls, not substitutes for the wild-type function.
Sources: PMID:26377666, PMID:18406577

## GO:0005525 GTP binding — ACCEPT
GNA14 is a guanine-nucleotide-binding G alpha subunit that switches between GDP- and GTP-bound states and hydrolyzes bound GTP. Receptor/effector biochemistry and nucleotide-state experiments support the intrinsic molecular switch. This is distinct from the GAP activity of RGS proteins; activated or nucleotide-defective mutants are controls, not substitutes for the wild-type function.
Sources: PMID:26377666, PMID:18406577

## GO:0005515 protein binding — REMOVE
The physical interactions are not denied. Remove bare protein binding under the project policy while retaining specific receptor, beta/gamma and effector functions supported independently.
Source handling: original payload retained; no fabricated supporting quote.

## GO:0005737 cytoplasm — ACCEPT
The G alpha protein is an intracellular peripheral-membrane signaling component with a cytoplasmic pool. Cytoplasm is compatible with membrane association and, where demonstrated, other intracellular pools; no exclusive localization is inferred.
Sources: PMID:26377666, PMID:18406577

## GO:0005834 heterotrimeric G-protein complex — ACCEPT
The GDP-state G alpha subunit associates with a G beta/gamma dimer to form a functional heterotrimer. Receptor-coupling and structural/reconstitution experiments support this assembly and beta/gamma binding as integral functions. A particular experimental beta/gamma combination does not imply universal interchangeability.
Sources: PMID:26377666, PMID:18406577

## GO:0031683 G-protein beta/gamma-subunit complex binding — ACCEPT
The GDP-state G alpha subunit associates with a G beta/gamma dimer to form a functional heterotrimer. Receptor-coupling and structural/reconstitution experiments support this assembly and beta/gamma binding as integral functions. A particular experimental beta/gamma combination does not imply universal interchangeability.
Sources: PMID:26377666, PMID:18406577

## GO:0005886 plasma membrane — MODIFY
The independently supported plasma-membrane signaling pool lies on the cytoplasmic side, already represented separately in this record. Refine this general membrane location while retaining other independently supported intracellular locations; the refinement does not assert exclusive residence.
Sources: PMID:26377666, PMID:18406577

## GO:0009898 cytoplasmic side of plasma membrane — ACCEPT
The intracellular G alpha–beta/gamma complex contacts the cytoplasmic receptor surface and intracellular effectors. Receptor-complex structures, membrane targeting and signaling experiments support the cytoplasmic plasma-membrane face.
Sources: PMID:26377666, PMID:18406577

## GO:0019001 guanyl nucleotide binding — MODIFY
The conserved guanine-nucleotide pocket binds GTP during activation and GDP in the inactive state. Refine the generic nucleotide-binding term to these two chemically defined ligands, preserving both halves of the switch.
Sources: PMID:26377666, PMID:18406577

## GO:0007165 signal transduction — MODIFY
The protein directly transduces signals through heterotrimeric G protein-coupled receptor signaling. Refine generic signal transduction to the established receptor pathway without excluding additional receptor-independent functions.
Sources: PMID:26377666, PMID:18406577

## GO:0007186 G protein-coupled receptor signaling pathway — ACCEPT
Receptor-dependent nucleotide exchange and effector coupling establish direct participation in GPCR signaling. Individual receptor preferences and physiological contexts must be established separately rather than inferred from the whole G protein family.
Sources: PMID:26377666, PMID:18406577

## GO:0001664 G protein-coupled receptor binding — ACCEPT
Human G14 receptor-coupling experiments and G14/Gz domain swaps establish selected GPCR coupling to PLCbeta/IP3 production. The helical domain is required for productive PLC activation; binding alone does not establish activation. The older genomic mapping citation is not itself a biochemical assay.
Sources: PMID:26377666, PMID:18406577

## GO:0007200 phospholipase C-activating G protein-coupled receptor signaling pathway — ACCEPT
Human G14 receptor-coupling experiments and G14/Gz domain swaps establish selected GPCR coupling to PLCbeta/IP3 production. The helical domain is required for productive PLC activation; binding alone does not establish activation. The older genomic mapping citation is not itself a biochemical assay.
Sources: PMID:26377666, PMID:18406577

## GO:0001508 action potential — KEEP_AS_NON_CORE
Retain the PAINT ancestral-node inference at PTN008303190, grounded in mouse G11 electrophysiology, as a peripheral conserved Gq-family capacity. It is not a direct G14 experiment or proof of an obligatory native human action-potential role; no target-specific functional loss was identified that would invalidate the curated node.
Sources: PMID:10818132, PMID:26377666

## GO:0007188 adenylate cyclase-modulating G protein-coupled receptor signaling pathway — KEEP_AS_NON_CORE
The ancestral cyclase-modulating pathway annotation is retained as an indirect Gq-family signaling inference. Direct human G14 evidence establishes PLC activation; calcium/PLC-dependent modulation must not be rewritten as purified G14 activation of an adenylyl cyclase.
Sources: PMID:8390980, PMID:26377666

## GO:0050729 positive regulation of inflammatory response — KEEP_AS_NON_CORE
CCR1/G14 signaling can activate transcriptional inflammatory outputs in the studied cells. Preserve this measured context without treating a heterologous receptor combination as universal native human leukocyte wiring.
Sources: PMID:23125416

## GO:0060158 phospholipase C-activating dopamine receptor signaling pathway — KEEP_AS_NON_CORE
The PAINT node PTN000026396 encodes a Gq-family dopamine–PLC signaling inference supported by mouse Gq/G11 experiments. Retain it as a contextual inherited capacity, not a G14-specific dopamine-receptor assay; donor count is not a reason to discard the ancestral assertion.
Sources: PMID:17194762, PMID:26377666

## GO:0060326 cell chemotaxis — UNDECIDED
Full PMID:26377666 measures human G14/Gz-chimera association and PLCbeta/IP3 signaling, not chemotaxis or migration. PMID:18406577 supports G14 chemokine-receptor coupling, whereas its native THP-1 migration evidence concerns G16. Receptor coupling alone does not establish that G14 performs the annotated cell-migration program. The biological G14 chemotaxis claim remains unresolved rather than negated from absence of one assay.
Sources: PMID:26377666, PMID:18406577

## GO:0070062 extracellular exosome — UNDECIDED
The prostate extracellular-vesicle proteomics source was not resolved to independently inspected G14-specific detection/enrichment. Its intracellular signaling role does not exclude extracellular-vesicle cargo, but it does not establish this precise HDA location.
Sources: PMID:23533145

## Research and access
Normal publication fetches and targeted refreshes are logged under `.cache/module-audit-logs/acetylcholine-*`. Canonical abstract-only caches were not manually rewritten. Full publisher recovery for cone localization is cited separately. PAINT assertions are treated as ancestral-node judgments, not pairwise transfers; target appearance among descendant evidence is not circular.

## Validation
Focused strict/schema, source/quote and ontology checks, record-section backfill, rendering and helper-generated history are recorded in the final panel proof.

## Final source and propagation audit

Original machine payloads and all qualifiers were compared with the authoritative baseline. There are no NOT assertions or new annotation rows in this 15-target panel. Full sources were inspected where a source-specific sign/mechanism challenge required them; unresolved fine-localization/source claims are retained as UNDECIDED rather than inferred absent. Bare binding removals apply the project policy and do not dispute experimental interactions.

UniProt/PANTHER placement inspected: `PTHR10218:SF213`. Broad G-alpha family PTHR10218 is GTP-BINDING PROTEIN ALPHA SUBUNIT; GRK PTHR24355 is G PROTEIN-COUPLED RECEPTOR KINASE/RIBOSOMAL PROTEIN S6 KINASE. Surprising official family names were not mechanically repointed. RGS6 current PTHR45746 placement does not invalidate a historical PAINT PTHR10845 assertion by itself.

See [source-analysis README](GNA14-source-analysis/README.md) for the exact vendor/method chain behind the human G14 BRET inference. The supplier accession and platform phylogenetic accession do not amount to sequencing the 2024 assayed plasmid.


## PR #5582 follow-up, 2026-10-26

Normalized human-facing citation identifiers and spacing, preserving every machine annotation field and existing supporting quotation. Removed exactly repeated summary prefixes from reasons where a separate substantive explanation remains. All annotation actions remain unchanged for this gene.
