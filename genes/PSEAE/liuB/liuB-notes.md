# liuB (PA2012, Q9I297) review notes

## Review session 2026-11-13 (PseudoCAP tier 3, shared-claim group liuB/liuD)

Fetched with `just fetch-gene PSEAE liuB`. No deep-research provider file was generated. Both key
papers are in the cache **with full text**, which is what let this group be settled rather than
deferred.

Beta subunit of 3-methylcrotonyl-CoA carboxylase (MCC). Two independent sources agree on the
subunit assignment: [PMID:18469096 "These enzymes are composed of two subunits, i.e., LiuB and
AtuC (β subunits) and LiuD and AtuF (α subunits)"] and the UniProt domain content
([file:PSEAE/liuB/liuB-uniprot.txt "Pfam; PF01039; Carboxyl_trans; 1."], plus both
CoA-carboxyltransferase InterPro domains).

### Why both GO:0004485 rows are ACCEPT with a qualifier defect

The holoenzyme reaction is split between the chains: [PMID:22158123 "BC catalyzes the
MgATP-dependent carboxylation of biotin, and then a carboxyltransferase (CT) activity, supplied by
the β subunit, catalyzes the transfer of the carboxyl group to the acceptor"], with
[PMID:22158123 "The distance between the active sites of BC and CT is approximately 80 Å in MCC"].

The decisive point for the qualifier is how the IDA was obtained:
[PMID:18469096 "The α and β subunits (2 mg each) were mixed and renatured by dialysis"] after
[PMID:18469096 "Reconstitution of MCCase and GCCase was carried out using the subunits purified as
described above"]. The activity was therefore measured on a reconstituted two-subunit enzyme and
no single chain was shown active. That is why the defect is CONFIRMED here, where the cbb3 group's
equivalent defect could only be PROBABLE from an abstract.

### Annotation decisions

- ACCEPT: GO:0004485 (IDA and IMP), both with a WRONG_QUALIFIER PseudoCAP defect
  (enables -> contributes_to); GO:0006552 (IBA); GO:0008300 (IMP, kept because this entry has no
  GO:0046247 row, unlike liuD); GO:1905202 (IBA and IDA).
- TOO_GENERAL: GO:0016874 ligase activity. GO:0004485 is_a GO:0016874, checked in QuickGO.
- REMOVE: GO:0005515 protein binding, per the project policy. Nothing is lost -- the interaction it
  records is the alpha-beta pairing, which the GO:1905202 complex rows state precisely.
- NEW: GO:0016743 carboxyl- or carbamoyltransferase activity (IC). The entry had no annotation of
  the half-reaction LiuB itself performs; the full text names it and the Pfam domain matches.

## Correction, 2026-11-13 (PR #6341 review): GO:0008300 is MODIFY, not ACCEPT

The first version of this review kept `GO:0008300 isoprenoid catabolic process` as ACCEPT on the
ground that this entry, unlike liuD, carries no `GO:0046247` row. That argued from what GOA
happens to assert rather than from the evidence, and it contradicted the liuD review's own
sentence that "the asymmetry is in GOA, not in the biology" -- an ACCEPT while arguing the term is
too general, which CLAUDE.md rules out. The replacement term is *preferably* one the gene already
carries, not necessarily.

Now MODIFY to `GO:0046247 terpene catabolic process`, matching liuD, with
`core_functions.directly_involved_in` updated to match. Worth noting where this slipped through:
the shared-claim grouping exists precisely to stop two halves of one enzyme drifting apart, and
this pair drifted anyway, inside the group.
