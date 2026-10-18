# TSA1 annotation re-review notes

## 2026-08-28 dedicated re-review

TSA1 (P34760; SGD:S000004490) is the major cytosolic typical 2-Cys
peroxiredoxin in budding yeast. Its primary catalytic function is reduction of
hydrogen peroxide and organic hydroperoxides with reducing equivalents supplied
by thioredoxin [PMID:7961686, "The 25-kDa enzyme is now shown to be a peroxidase
that reduces H2O2 and alkyl hydroperoxides with the use of hydrogens provided by
thioredoxin, thioredoxin reductase, and NADPH."].

Tsa1 also has a stress-dependent chaperone function. Oxidative stress and heat
shock shift the protein into high-molecular-weight assemblies and switch the
dominant activity from peroxidase to chaperone [PMID:15163410, "Oxidative stress
and heat shock exposure of yeasts causes the protein structures of cPrxI and II
to shift from low MW species to high MW complexes. This triggers a
peroxidase-to-chaperone functional switch."]. Genetic evidence connects that
activity to prevention of ribosomal-protein aggregation [PMID:16251355, "We
propose that Tsa1 normally functions to chaperone misassembled ribosomal
proteins, preventing the toxicity that arises from their aggregation."], and a
separate study establishes that chaperone activity is especially important in
zinc-deficient cells [PMID:24022485, "In this report, we show that Tsa1
chaperone, and not peroxidase, activity is the more critical function in
zinc-deficient cells."]. All three cached records are abstract-only, so the
review accepts their explicit abstract-level conclusions without inventing
assay details from inaccessible full text.

### GOA reconciliation

The cached GOA contains 68 physical rows and 60 qualifier-aware signatures
(qualifier + GO term + evidence code + reference). Four signatures collapse
multiple physical rows: PMID:37968396 protein binding has two interaction
partners, PMID:15163410 protein folding IDA occurs twice, and the IGI rows for
PMID:19851444 and PMID:15051715 each have four distinct WITH/FROM partners. The
review represents each exact signature once, as required by the current review
schema; `just validate-goa yeast TSA1` checks this reconciliation. All physical
rows use positive relation qualifiers (enables, involved_in, located_in,
is_active_in); there are no NOT annotations or isoform-specific rows.

The four IPI protein-binding signatures were retained only as
MARK_AS_OVER_ANNOTATED because the generic term does not describe Tsa1's
peroxidase, redox-transfer or chaperone mechanisms. The two PMID:37968396 rows
correspond separately to TRX2 (P22803) and TSA2 (Q04120), rather than a duplicate
curation accident.

### PAINT audit

All five IBA annotations descend from PTHR10681 node PTN000073874. Current
`PTHR10681-paint.tsv` retains that same node for cytosol (GO:0005829),
thioredoxin peroxidase activity (GO:0008379), response to oxidative stress
(GO:0006979), hydrogen peroxide catabolic process (GO:0042744), and cell redox
homeostasis (GO:0045454). Current PAINT keeps TSA1 as an experimental seed for the
cytosol, oxidative-stress, and redox-homeostasis IBDs; this is valid
target-grounded IBD evidence, not circularity. The GOA 2025 WITH/FROM for
`GO:0008379` still listed TSA1/TSA2, but the 2026-08-28 PAINT row was narrowed to
fission-yeast, metazoan, and protist seeds. The hydrogen-peroxide-catabolism call is
also seeded by other experimentally characterized peroxiredoxins. Both molecular
activity and hydrogen-peroxide catabolism remain independently supported by TSA1
biochemistry. The only source-format drift is that current PAINT writes the two
Arabidopsis redox-homeostasis seeds as AGI_LocusCode identifiers whereas cached GOA
writes TAIR:locus identifiers. No node-placement failure or target-specific
loss/divergence was found.

### Obsolete unfolded-protein term

Live QuickGO was checked on 2026-08-28. GO:0051082 is obsolete. GO:0044183 is
current and defined as binding a protein or complex to assist protein folding;
it is therefore an evidence-matched replacement for the papers that explicitly
call Tsa1 a molecular chaperone and annotate protein folding. GO:0140309 is
currently labelled "unfolded protein holdase activity," but its unchanged
definition requires escorting the client to an acceptor or specific location.
Tsa1 prevents aggregation in situ and is not a carrier, so GO:0140309 was not
used. A general `holdase chaperone activity` remains an ontology gap; the review
uses the canonical project NTR name while retaining GO:0044183 as the available
current chaperone activity.

The final synthesis treats thioredoxin-dependent peroxiredoxin activity and the
stress-activated chaperone/holdase switch as TSA1's two core functions. Broad
parents, heat/zinc/DTT contexts, genome protection, gluconeogenic regulation,
ribosome association and generic binding are retained as non-core or
over-annotated rather than promoted into the core-function summary.

## 2026-09-29 IBA project alignment

All five IBA annotations are still present in the current local
`PTHR10681-paint.tsv` export at `PTN000073874`: `GO:0005829` cytosol,
`GO:0006979` response to oxidative stress, `GO:0008379` thioredoxin peroxidase
activity, `GO:0042744` hydrogen peroxide catabolic process, and `GO:0045454`
cell redox homeostasis. The existing `propagation_review` decisions remain
appropriate: four calls are core and the broad stress-response term is a valid
non-core parent.

The four `GO:0005515 protein binding` IPI review actions were migrated from
`MARK_AS_OVER_ANNOTATED` to `REMOVE`. This does not challenge the TRX2 or TSA2
physical associations; the generic molecular-function term just does not
describe TSA1's thioredoxin-dependent peroxidase, redox-relay, oligomeric, or
chaperone activities.

The 2025 literature refresh found additional work on metabolic regulation by
Tsa1, including its 2025 interactome in zinc-deficient cells (PMID:40748663),
wine-yeast acetic-acid metabolism (PMID:40120136), and dominant peroxide
scavenging/GSSG production (PMID:39515595). These refine TSA1's downstream
metabolic contexts but do not change the core GO model.
