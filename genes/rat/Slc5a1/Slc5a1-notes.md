# Slc5a1 notes

## Re-review 2026-10-10

GOA refresh changes:
- 7 new rows seeded: GO:0005412 D-glucose:sodium symporter activity ISO, GO:0016324 apical plasma membrane ISO, GO:0055056 D-glucose transmembrane transporter activity ISO, and two GO:1904659 D-glucose transmembrane transport ISO rows (acts_upstream_of_or_within and involved_in), all with human SGLT1 (UniProtKB:P13866) as donor; GO:0016324 ISS from mouse SGLT1 (UniProtKB:Q8C3K6); GO:0006812 monoatomic cation transport IEA (ARBA).
- 4 rows retired (all IEA): GO:0015293 symporter activity, GO:0008324 monoatomic cation transmembrane transporter activity, GO:0006814 sodium ion transport, GO:0006811 monoatomic ion transport. Kept with a note.

Decisions:
- Donor-split P13866 rows reviewed consistently with their mouse-sourced siblings (ACCEPT, or KEEP_AS_NON_CORE for GO:0055056). GO:0016324 ISS ACCEPT. GO:0006812 MODIFY to GO:0098719 sodium ion import across plasma membrane.
- GO:1902476 chloride transmembrane transport (ISO) is a NOT annotation; the earlier review treated it as a positive claim. UNDECIDED -> ACCEPT [PMID:10973981 "In contrast, Cl(-) was not transported by SGLT1."].
- GO:0015151 alpha-glucoside transmembrane transporter activity and GO:0000017 alpha-glucoside transport (ISO): MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE. The GO definition covers methyl-alpha-D-glucopyranoside, the standard SGLT substrate [PMID:20980548 "In these experiments the sugar used was nonmetabolizable and SGLT-specific, αMDG."]; correct, but a model substrate.
- GO:0001656 metanephros development (ISO, mouse): UNDECIDED -> KEEP_AS_NON_CORE after tracing the donor evidence [PMID:10997927 "Treatment with SGLT-1 antisense selectively decreased the population of tubules in the metanephric explants."].
- GO:0016323 basolateral plasma membrane (TAS, PMID:14986005): REMOVE -> UNDECIDED. Only the abstract is cached; the author statement used may concern another context.
- GO:0031526 brush border membrane (IDA, PMID:14986005): kept ACCEPT, but removed the claim that the reference is misassigned; we cannot see the full text.
- GO:0016020 membrane, GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport (IEA): MARK_AS_OVER_ANNOTATED -> MODIFY to the specific terms (apical plasma membrane, D-glucose:sodium symporter activity, D-glucose transmembrane transport); generic terms are uninformative rather than overreaching.
- Added supported_by (UniProt CC lines or donor papers) to 28 rows and to all three core_functions entries that previously had none; replaced a meaningless deep-research quote ("model: Edison Scientific Literature").

Open questions:
- Basolateral plasma membrane (TAS, PMID:14986005): what statement in the full text did the curator rely on?
- Is water transmembrane transporter activity best treated as a core function or as a biophysical property of the transporter? Kept as core, following UniProt and PMID:26945065.
