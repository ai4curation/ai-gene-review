

## Acetoin audit: primary-source reassessment

Reviewed all 11 inherited rows without changing source payloads; retained inherited proposals, added no new rows. Current UniProt and native papers identify pedE, Q88JH5, PP_2674. Genuine existing Falcon/OpenScientist research was reused only for retrieval, and primary texts were read independently. New normal publication retrieval passed; actual FEBA fitness retrieval failed (see acquisition log), so no fitness result is inferred. Raw records and provider reports remain unchanged.

GO:0052934 denotes primary-alcohol oxidation to aldehydes; GO:0016614 independently preserves the secondary-alcohol chemistry. PMID:28655819 assays use artificial PMS/DCPIP, not an identified native cytochrome. PMID:34513815 Figure 5 establishes native S,S entry through PedE/PedH and metal-dependent rescue, not a new purified stereospecificity assay. Its sentence reversing the lanthanide expression switch is inconsistent with its own phenotypes and PMID:30158283. Broad alcohol-metabolism proposals already cover the catalytic process; no redundant NEW butanediol term is added.

The earlier assertion that GO:0030288 requires outer-membrane association is false: it is the periplasmic compartment. General membrane inference is over-annotation for these soluble type I enzymes, without pretending that missing transmembrane helices exclude every peripheral contact. Heme mapping conflates quinoproteins with quinohemoproteins. Calcium inactivity in PedH does not prove absolute inability to bind calcium. Source-qualified periplasm and measured metal/cofactor roles supersede stronger older notes.

Curated filename and gene_symbol casing are standardized from pede to pedE. Historical raw/provider filenames remain unchanged; prior history records are not rewritten.

Git-index correction: the historical directory itself was lowercase `genes/PSEPK/pede`, despite case-insensitive APFS lookups accepting `pedE`. The entire directory is canonicalized to `genes/PSEPK/pedE` for case-sensitive systems. Raw and provider filenames and hashes remain unchanged; their parent directory changes. Existing historical records are not rewritten. The parent authorized staging only these nine path renames through two-step git mv.


## PR 5588 follow-up — 2026-10-26

Completed the exact-case pedE source filenames using two-step git mv; all raw and provider bytes are unchanged. The provider-generated OpenScientist artifact directory retains its legacy spelling because immutable provider text links to that exact relative path. Old history identities remain frozen, with successor metadata and records relocated to the pedE directory. Two inherited metabolic-process proposals now use IC with PMID:28655819, reflecting inference from measured target turnover rather than an electronic annotation. The durable supersession JSON separates these author-controlled changes from unchanged GOA payloads.

## 2026-11-02 — acetoin/butanediol module completion pass

- Cited the falcon deep-research file for Ca2+/PQQ dependence on the calcium ion binding row.
