# nicA: nicotinate entry-system audit

## Identity and scope

Accession Q88FX9; Pseudomonas putida KT2440. All 6 pre-existing rows reviewed; original non-review fields preserved. Nicotinate entry chemistry is distinct from nicotine oxidoreductases with similar gene names.

## Primary evidence and boundaries

PMID:18678916 full article was read at https://pmc.ncbi.nlm.nih.gov/articles/PMC2516282/ (NicAB results and Fig. 2). Supported force-refresh still yielded an abstract-only cache. The full study tests heterologously expressed KT2440 NicAB, including CytC truncation, artificial-acceptor bypass, heme staining and complementation in trans. It supports a functional cytochrome region, while the terminal oxidase identity remains proposed. Water supplies the inserted oxygen; oxygen dependence does not make NicAB a monooxygenase.

PMID:19118407 ["Gene knockout and recovery studies further confirmed the ndhSL function."] independently supports target-gene function; its cached abstract explicitly describes the small Fe-S and large molybdenum/cytochrome subunits. Cofactor stoichiometry and NicB topology are comparative/predicted assignments in UniProt, not newly measured target assays. The current NicA sequence is 157 aa / 16686 Da; the older paper/deep report 23.8-kDa value is not propagated.

## Function granularity

QuickGO GO:0050138 was checked live on 2026-10-25: its definition explicitly uses NADP+ and maps to EC1.17.1.5/RHEA12236. It is unsuitable for cytochrome-linked NicAB EC1.17.2.1/RHEA27417. Retain GO:0016725 as the defensible parent for contributed complex chemistry; an exact cytochrome-linked hydroxylase descriptor is warranted at module level. Fe-S and heme binding are core cofactor roles. True broad terms are refined, not marked over-annotated. NicB membrane is retained as a supported predicted core location without fabricating experimentally resolved sidedness.

## Comparative architecture

PMID:29485696 Table 1 maps RB50 BB1783/A0A0H3LKL9 to NicB2 and BB1776/A0A0H3LTT1 to NicB1. They are architectural comparators, not isolated-subunit enzyme demonstrations. BB1776 is 946 aa and includes MCD-related regions as well as three cytochrome domains; a clean split into two nonoverlapping halves is unsafe. No alternative native complex stoichiometry is asserted.

## Research provenance

Default Falcon plus Perplexity-lite fallback was requested concurrently with publication caching. Existing Falcon report returned from cache successfully; content was reviewed but primary/curated sources anchor the decisions. No fresh provider success is claimed. FEBA retrieval failed because neither local nor remote data was reachable; no fitness artifact was fabricated. No accession matches were found in gocams/index.tsv.

## Verified family membership

- DR   PANTHER; PTHR44379:SF6; BLR6046 PROTEIN; 1.
- DR   PANTHER; PTHR44379; OXIDOREDUCTASE WITH IRON-SULFUR SUBUNIT; 1.

Official labels were checked against interpro/panther/panther.obo. These broad family assignments do not alone establish nicotinate substrate specificity; no PTN ancestry was guessed.

## Annotation ledger

- GO:0016491 (IEA, GO_REF:0000120): MODIFY. Target-specific NicAB studies establish nicotinate hydroxylation. NicA supplies Fe-S electron transfer and NicB supplies the catalytic/cytochrome regions; activity is executed by the assembled enzyme. GO:0050138 is NADP-specific and is not an appropriate replacement for this cytochrome-linked system.
- GO:0046872 (IEA, GO_REF:0000002): MODIFY. These are true parent functions, not over-annotations. Conserved ferredoxin motifs and curated comparative cofactor assignment support the existing GO:0051537. Two-cluster stoichiometry is inferred rather than directly measured in isolated KT2440 NicA.
- GO:0051536 (IEA, GO_REF:0000002): MODIFY. These are true parent functions, not over-annotations. Conserved ferredoxin motifs and curated comparative cofactor assignment support the existing GO:0051537. Two-cluster stoichiometry is inferred rather than directly measured in isolated KT2440 NicA.
- GO:0051537 (IEA, GO_REF:0000002): ACCEPT. Ferredoxin domains and conserved ligand motifs independently support the cluster class. UniProt assigns two clusters by similarity; the primary complex experiments do not directly measure isolated NicA cluster occupancy.
- GO:1901848 (IDA, PMID:18678916): ACCEPT. PMID:18678916 and PMID:19118407 characterize the target KT2440 genes, including heterologous nicotinate conversion and knockout/recovery. The protein performs redox work in NicAB rather than merely responding to nicotinate.
- GO:0016725 (IDA, PMID:18678916): ACCEPT. The original PMID:18678916 studies the assembled target enzyme. This broad term accurately covers the cytochrome-linked chemistry; GO:0050138 instead specifies NADP+ and must not be substituted. Subunit contribution is explicit in core_functions; isolated-subunit turnover is not claimed.

An exact cytochrome-linked activity is recorded under proposed_new_terms. The schema has no proposed_contributes_to_molecular_function slot; core functions therefore retain the correct GO parent for the assembled reaction and specific subunit-level binding/electron-transfer functions.

## PR 5544 follow-up (2026-10-25)

Live QuickGO checks on 2026-10-25 found no exact terms using EC 1.17.2.1, EC 3.5.1.106, EC 3.5.1.107 or the corresponding substrate-specific activity names. Nicotinate dehydrogenase GO:0050138 remains the NADP-specific reaction. All 14 direct children of GO:0016725 were inspected: acceptor classes include NAD/NADP, oxygen, disulfide, quinone and iron-sulfur protein, but no generic cytochrome-acceptor child. GO:0047111 is formate-specific and cannot substitute. Thus GO:0016725 remains the supported parent for cytochrome-linked NicAB; search non-retrieval is reported as a current search result, not proof that no future ontology term can exist.

## PR 5544 follow-up (2026-10-25)

The optional source-defect suggestion about an ordinary enables qualifier was not applied: the active annotation-reviewer instructions treat those machine-sourced qualifiers as inert and prohibit editing or arguing from them. The review continues to distinguish independently supported subunit functions from the assembled-enzyme reaction through contributes_to_molecular_function in core_functions. No upstream qualifier defect is asserted.
