# bcsA research and review notes

## 2026-11-06 — type I cellulose audit

Applied annotation-reviewer and core-function-synthesizer guidance. Normal `just fetch-gene KOMXY bcsA --uniprot-id P19449` created a new review; all eight seeded annotation payloads and both raw-file hashes were frozen before editing in `.cache/module-audit-logs/cellulose-20261105/typeI-baseline.json`. Default Falcon research was attempted and failed with HTTP403 authentication; the genuine log is in that directory. These are manual notes, not a provider report.

P19449/BCSA1_KOMXY is 754 aa, current gene bcsA, species-level NCBITaxon28448. Its frozen curated primary sequence citation explicitly names strain1306-3 (PMID2146681). ENA M37202 CDS328..2592, protein AAA21884.1, exactly matches all754residues. Source EMBL and machine results are in bcsA-bioinformatics; the generic comparison script and independent tests are in the companion acsD/acsD-bioinformatics directory. This is a separate BcsA, not a fusion; the ATCC53582 acsAB fusion described in PMID8083166 is a different protein from a different strain.

PMID2146681, *Genetic organization of the cellulose synthase operon in Acetobacter xylinum*, is abstract-only after normal force retry. Its four-gene native operon genetics are relevant. However, it says “The second gene in the operon (bcsB) encodes the catalytic subunit of cellulose synthase” and leaves bcsA unknown. Do not silently rewrite this historical claim into a purified P19449 catalytic assay. The modern catalytic assignment is supported independently by the curated UniProt functional/reaction statement, GT2/cellulose-synthase family/domain evidence, and the modern mechanistic synthesis in full-text PMID26077867. No sequence naming shortcut was used to claim purified protein evidence.

PMID16920715, *The PilZ domain is a receptor for the second messenger c-di-GMP*, explicitly assays an isolated G. xylinus BcsA PilZ domain as well as YcgR. Cache remains abstract-only after normal force retry; JBC DOI, full-text and PDF routes returned403. Thus the title's emphasis on YcgR does not invalidate BcsA binding, but the precise BcsA construct/strain cannot be verified from the available methods. Retain the existing electronic binding annotation on combined curated/domain support without newly asserting a full-length1306-3 binding measurement or target-specific affinity. The30uM value is present in the curated record; the review does not treat that value as independently verified.

Actions: five ACCEPT, three MODIFY (membrane→plasma membrane; generic hexosyltransferase and generic cellulose synthase→UDP-forming cellulose synthase). Existing UDP-alpha-D-glucose metabolism denotes actual substrate conversion by the enzyme, not precursor biosynthesis. No NEW annotation is needed: catalytic MF, cellulose BP, specific ligand binding and membrane localization are already covered. No necessity-only biofilm/fibril process was added. There are no IBA rows requiring a PAINT loss audit. The core records polymerization; assembly of crystalline ribbons also depends on other components and is not an intrinsic purified-BcsA claim.

### Follow-up primary-text access

After the initial validation, the primary main text of PMID16920715 was readable in its [author-hosted ResearchGate copy](https://www.researchgate.net/publication/6866942_The_PilZ_domain_is_a_receptor_for_the_second_messenger_c-di-GMP_The_PilZ_domain_protein_YcgR_controls_motility_in_enterobacteria). Methods identify PCR amplification of the BcsA1 C-terminal PilZ fragment and a C-terminal His tag; strain/primer tables remain in the inaccessible supplement. Results report a 30 uM dissociation constant for this isolated domain, not full-length BcsA. The earlier access limitation therefore narrows to exact strain and construct sequence mapping. The normal publication cache remains untouched and abstract-only. Annotation actions and the catalytic core are unchanged.


## 2026-11-06 — round 16 follow-up

The accepted UDP-glucose metabolism claim now appears explicitly in the catalytic core, consistent across all five catalytic BcsA reviews carrying that term.

## PR2143 round17: bacterial process specificity

Refine the original general process using MODIFY and the authored core process. Preserve the distinction between operon genetics, curated chemistry and isolated-subunit assays; improve ATCC spacing only in authored prose.

QuickGO definitions checked on 2026-11-06 establish GO:0090540 as an is_a subtype of GO:0030244 with bacterial context. The parent and child share the cellulose chemistry criteria. Native output, intact-cell synthesis, crystallinity and fibrils are independent evidence questions, not extra requirements introduced by the bacterial subtype.

Original source/provider bytes and machine payloads are preserved. Supporting sources and target-specific limits are recorded in the reviewed annotation; no new annotation row is introduced in this follow-up.
