# hsd17b3 notes

## 2026-05-09 review notes

Reviewed GOA, UniProt Q6QA32, PMID:16216911, and PANTHER family cache. The direct core annotation is endoplasmic-reticulum Hsd17b3 testosterone dehydrogenase activity in androgen/testosterone biosynthesis.

## Re-review 2026-09-29

The whole review was templated: every annotation carried the same UniProt FUNCTION line as `supporting_text`, including the three localization terms. All eleven rows were rewritten against the primary paper and the UniProt record, and the three PENDING rows were resolved.

**ZFIN remapping.** Current QuickGO attaches ZFIN's three experimental rows (GO:0005783 IDA, GO:0006702 IDA, GO:0047045 IDA, all from PMID:16216911) to a newer TrEMBL accession of the same zebrafish gene, so they are absent from the refreshed `hsd17b3-goa.tsv` obtained under Q6QA32. They are legitimate annotations of this gene product and were retained and reviewed on their merits; this is noted in the summary of each of those rows.

**Evidence used.** PMID:16216911 is abstract-only in the cache, but the abstract states each of the facts relied on:
- catalysis: [PMID:16216911 "The zebrafish enzyme in vitro effectively catalyzed the conversion of androstenedione to testosterone by use of NADPH as cofactor"]
- substrate scope: [PMID:16216911 "Among further tested androgens epiandrosterone and dehydroepiandrosterone were accepted as substrates and reduced at C-17 by the human and the zebrafish enzyme. Androsterone and androstanedione though, were only substrates of human 17beta-HSD type 3, not the zebrafish enzyme."] and [PMID:16216911 "we found that both enzymes can reduce 11-ketoandrostenedione as well as 11beta-hydroxyandrostenedione at C-17 to the respective testosterone forms"] — this is the route toward 11-ketotestosterone, the principal teleost androgen
- localization: [PMID:16216911 "At the subcellular level, both human and zebrafish 17beta-HSD type 3 localize to the endoplasmic reticulum"]
- expression: [PMID:16216911 "Interestingly, expression was not highest in male testis but in male liver. In female adults, strongest expression was observed in ovaries."]

PMID:27927697 (Tsachaki et al., J Endocrinol 2017) was newly cached and added to `references:`. UniProt cites it (ECO:0000269) for the EC 1.1.1.64 reaction and for 11-ketoandrostenedione reduction; its abstract does not name hsd17b3, so it is used only as corroboration, never as sole support, and `reference_review` records that.

**Action changes.**
- GO:0016020 membrane (IEA, SL-0162): KEEP_AS_NON_CORE -> MODIFY to GO:0005789 endoplasmic reticulum membrane. Experimental ER localization plus the UniProt-predicted helical TRANSMEM at residues 6-26 supports the specific child.
- GO:0005737 cytoplasm (IEA GO_REF:0000117) and a duplicate GO:0005783 (IEA GO_REF:0000044) were removed from the yaml: validation reported both as "not in GOA", i.e. they are no longer in the refreshed record. No other row lost.
- GO:0008610 lipid biosynthetic process (IEA, ARBA00027236, PENDING): MODIFY to GO:0006702 androgen biosynthetic process. True but a very distant ancestor; the specific descendants are already annotated by IDA.
- GO:0033764 steroid dehydrogenase activity, CH-OH donors, NAD/NADP acceptor (IEA, ARBA00084320, PENDING): MODIFY to GO:0047045. The exact reaction is experimentally established, so the grouping parent adds nothing.
- GO:0005783 endoplasmic reticulum (IEA GO_REF:0000120, PENDING): ACCEPT, concordant with the IDA.
- The two IBA rows (GO:0005783 is_active_in, GO:0047045 enables) were kept as ACCEPT with reasoning about node placement rather than donor count. ZFIN:ZDB-GENE-040426-1339 appears in both WITH/FROM lists because this gene's own IDA seeded the IBD — expected, not circular.
- The three IDA rows remain ACCEPT; GO:0006702 passes the participation test because the enzyme itself catalyses a step of androgen synthesis rather than merely being required for it.

**Definitions verified** via QuickGO REST for GO:0033764, GO:0008610, GO:0047045, GO:0061370, GO:0006702, GO:0005789 and GO:0005783; none obsolete.

**Caveat recorded, not acted on.** The deep-research file reports that hsd17b3 transcripts are low or undetected in juvenile gonads at 19 and 30 dpf, so another Hsd17b may supply the 17beta-reduction at those stages. This tempers the in vivo weight of the testosterone-biosynthesis annotation but does not contradict the demonstrated enzymology, so GO:0061370 stays ACCEPT with the caveat in `reason`, and the question is raised in `suggested_questions`.

`description` was rewritten as standalone biology (SDR fold, ER anchor, NADPH-dependent 17beta-reduction, substrate scope including 11-oxygenated androgens, non-testis-restricted expression). Validation: zero errors.
