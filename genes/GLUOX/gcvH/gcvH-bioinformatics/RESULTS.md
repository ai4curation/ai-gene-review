# Genomic context of gcvH (Q5FRY1, GOX1096) in Gluconobacter oxydans 621H

Run: `python3 survey_gcs_and_lipoylation.py` (UniProtKB REST, no API key needed).
Output captured 2026-10-28. The script is the sole source of the table below; nothing
here is hand-entered.

## Question 1: is the glycine cleavage system complete?

| Role | Accession | Gene / locus | UniProt protein name |
|---|---|---|---|
| P protein (glycine dehydrogenase, decarboxylating) | Q5FRY0 | gcvP / GOX1097 | Glycine dehydrogenase (decarboxylating) |
| H protein (lipoyl carrier) | Q5FRY1 | gcvH / GOX1096 | Glycine cleavage system H protein |
| T protein (aminomethyltransferase) | Q5FRY2 | GOX1095 | aminomethyltransferase |
| L protein (dihydrolipoyl dehydrogenase) | Q5FNM2 | GOX2292 | Dihydrolipoyl dehydrogenase |

All four subunits of the glycine cleavage system are encoded. The T, H and P genes occupy
three consecutive locus tags, GOX1095-GOX1096-GOX1097, i.e. the canonical bacterial
`gcvTHP` gene cluster; the shared L protein lies elsewhere (GOX2292, adjacent to lipoyl
synthase GOX2293).

Consequence for the review: the `glycine cleavage complex` (GO:0005960) and
`glycine decarboxylation via glycine cleavage system` (GO:0019464) annotations on
Q5FRY1 are not family membership alone. The organism encodes partners for every step
of the pathway, and the H protein sits in an operon with the two subunits its lipoyl
arm shuttles between.

## Question 2: which lipoyl-attachment route does the organism use?

| Probe | Result |
|---|---|
| LipB-type octanoyltransferase (*E. coli* route) | Q5FUX5, lipB / GOX0046, Octanoyltransferase |
| LipA lipoyl synthase | Q5FNM1, lipA / GOX2293, Lipoyl synthase |
| LipM-type octanoyltransferase (*B. subtilis* route) | no entry matched |
| LipL octanoyl-[GcvH]:E2 amidotransferase (*B. subtilis* route) | no entry matched |

G. oxydans 621H carries the *E. coli*-type de novo lipoylation pair LipB + LipA. In that
route LipB octanoylates each lipoyl-acceptor domain directly from octanoyl-ACP, and
GcvH is one acceptor among several. It does not carry the *Bacillus subtilis*-type
LipM/LipL pair, which is the route in which octanoyl-GcvH is an obligate relay
intermediate for lipoylating the E2 subunits of the 2-oxoacid dehydrogenases, and which
is why *B. subtilis* GcvH holds an experimental `protein lipoylation` annotation while
*E. coli* GcvH holds none.

**Limitation, stated plainly.** The LipM/LipL probes search UniProt gene names and
protein names in this proteome, not profile HMMs against the genome. G. oxydans 621H is
a TrEMBL proteome where many entries carry only a locus tag, so a negative probe is
suggestive, not proof of absence. The positive finding — that a LipB octanoyltransferase
is present and annotated — does not depend on the negative probes, and LipB alone is
sufficient for lipoyl-domain modification (Christensen et al. 2011, PMID:21338421,
showed that expressing *E. coli* lipB rescues a B. subtilis `gcvH` deletion). The
conservative reading is therefore that no GcvH-dependent lipoyl relay has been
established for this organism, not that one has been excluded.

## What this analysis does not show

No measurement here speaks to glycine cleavage flux, lipoylation state, or any
phenotype in G. oxydans. These are annotation-level genomic-context observations drawn
from UniProtKB records, and none of the entries surveyed is manually reviewed
(Swiss-Prot) except where the table says so.
