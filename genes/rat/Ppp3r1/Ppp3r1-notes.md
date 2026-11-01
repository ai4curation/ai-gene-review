# Ppp3r1 (rat, P63100) notes

## Re-review 2026-10-04

**GOA changes.** None in substance: the refreshed GOA has the same 10 rows (4 IBA: calcineurin complex, calcium-dependent protein serine/threonine phosphatase regulator activity, calcineurin-NFAT signaling cascade, phosphatase binding; IEA InterPro calcium ion binding; IEA SubCell cytosol, plasma membrane, sarcolemma; ISS plasma membrane from human P63098; Reactome TAS cytosol). No PENDING, no retired rows. `qualifier`/`supporting_entities` were backfilled by the refresh.

**Row audit.** All actions unchanged (5 ACCEPT, 5 KEEP_AS_NON_CORE).
- The four IBA rows and calcium ion binding remain ACCEPT; CnB1 is the Ca2+-binding regulatory subunit [UniProtKB:P63100 "Regulatory subunit of calcineurin, a calcium-dependent, calmodulin stimulated protein phosphatase. Confers calcium sensitivity."; "This protein has four functional calcium-binding sites."]. GO:0019902 phosphatase binding is informative here (constitutive binding to the catalytic A subunit; UniProt "Interacts with catalytic subunit PPP3CA/calcineurin A (PubMed:24018048)"), so it is not treated as generic binding.
- The five localization rows were supported only by the FUNCTION sentence, which says nothing about location. Their `supported_by` now quotes the UniProt SUBCELLULAR LOCATION block ("Cytoplasm, cytosol"; "Cell membrane ... Lipid-anchor"; "Translocates from the cytosol to the sarcolemma in a CIB1-dependent manner during cardiomyocyte hypertrophy") and, for cytosol, the Falcon report.

**Other fixes.**
- `description` contained curation commentary ("The review accepts...", "The fetched GOA set contains no rat-specific IDA/IMP annotation..."); rewritten as standalone biology.
- The first core function quoted UniProt text that is not in the current record ("Regulatory subunit of calcineurin; forms a complex with calcineurin A and confers calcium sensitivity."); replaced with the verbatim FUNCTION sentence plus the SUBUNIT sentence on PPP3CA binding.

**Open question.** UniProt cites rat experimental data (PubMed:24018048: complex with PPP3CA, four functional Ca2+ sites, N-myristoylation at Gly-2), yet GOA carries no rat IDA/IPI rows from it. A curator could consider direct annotation from that paper.
