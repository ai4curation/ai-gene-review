# ATCAY notes

## 2026-10-05 review (PAINT, affinage)

- Kinesin-1 cargo adaptor [PMID:19861499 "The tetratricopeptide-repeat region of KLC1 recognizes the ELEWED sequence (amino acids 115-120) of caytaxin."]; [PMID:26343454 "Here, we demonstrate that ataxia-related protein BNIP-H/Caytaxin links kinesin-1 (KLC1) to ATP citrate lyase (ACL), a key enzyme for ACh synthesis, and transports it toward neurite terminals."]. Kinesin binding (IPI) is accepted as the core MF. No NEW cargo-adaptor MF: the comparator kinesin adaptors (MAPK8IP1, CLSTN1) carry kinesin binding, not GO:0140312.
- KGA [PMID:16899818 "It also reduced the steady-state levels of glutamate by inhibiting KGA enzyme activity."]. The IDA row GO:0062133 (negative regulation of L-glutamine *biosynthesis*) has the direction inverted, because glutaminase consumes glutamine. Changed it to GO:0140387 negative regulation of L-glutamate biosynthetic process.
- GO:0005515 rows: STUB1 → ubiquitin protein ligase binding (caytaxin is its substrate); the three GLS orthologs → enzyme binding; KLC1 (HuRI) → kinesin binding; PIN1 removed under policy.
- Mitochondrion ISS and mitochondrial membrane ISS are over-annotated. Only partial colocalization is seen, and the human IDA row is NOT colocalizes_with mitochondrion.
- Apoptotic process (IBA, donor BNIPL) is over-annotated. Caytaxin is a caspase-3 substrate, which is not participation in apoptosis.
- PMID:14556008 has an erratum (Nat Genet 2005;37:555), a correction; its text was not retrieved.

## 2026-10-05 revision (reviewer round 1)

- The reviewer flagged GO:0140387 as possibly nonexistent because it is absent from the repo's `cache/enums/*.csv`. Verified today: OLS4, QuickGO and the GO API all return GO:0140387 "negative regulation of L-glutamate biosynthetic process", biological_process, not obsolete. The local enum cache is incomplete for this term. The MODIFY is kept. The genes/human/GLS notes flag the same GO:0062133 direction problem.
- Added propagation_review to all ISS and rodent-projection IEA rows. Donors: rat Q1M168 and mouse Q8BHE3. The mitochondrion and mitochondrial-membrane over-annotations are scored as TERM_SCOPING_PROBLEM.
- PIN1 row: MODIFY to enzyme binding, consistent with the GLS and CHIP rows, instead of REMOVE.
- NOT colocalizes_with mitochondrion: the reasoning now reconciles the PC12 (curator, full text uncached) and hippocampal-neuron (partial colocalization) results.
- Added a second core function for the glutaminase axis (enzyme binding), and a suggested question on whether caytaxin directly inhibits glutaminase (GO:0004857).
- The PIN1-paper GLS row now quotes its own reference. Donor wording now names the species actually listed in WITH/FROM.
