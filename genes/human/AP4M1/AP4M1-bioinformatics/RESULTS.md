# AP4M1 (mu4) bioinformatics

Reproducible analyses supporting the AP4M1 GO annotation review. All sequences and
features are fetched live from the UniProt REST API at run time; nothing is hardcoded
except accessions and the two UniProt-annotated mutagenesis positions under test.

Run with:

```bash
uv run python mu_signal_site.py       # writes mu_signal_site.tsv / .json
uv run python goa_reconciliation.py   # checks the GOA tsv against the review YAML
```

## 1. The mu4 cargo-signal site: what the sequence does and does not show

`mu_signal_site.py` tests the two positions UniProt annotates on human mu4 as required
for binding the APP YKFFE signal (`FT MUTAGEN 255 F->A: Abolishes interaction with APP`;
`FT MUTAGEN 283 R->D: Strongly reduced interaction with APP`, both
`ECO:0000269|PubMed:20230749`), then asks whether those positions are conserved in mu4
orthologs and in the clathrin-adaptor mu paralogs.

Checks that passed as assertions:

- O00189 is 453 aa (sequence version 2) and carries **F at 255** and **R at 283**.
- Both positions fall inside the annotated MHD domain, UniProt `FT DOMAIN 184..452`.

Alignment results (global Needleman-Wunsch, BLOSUM62, gap open -11 / extend -1; each
subject aligned pairwise to O00189):

| group | accession | protein | length | % id to mu4 | aligned to 255 | aligned to 283 |
|---|---|---|---|---|---|---|
| ortholog | Q9JKC7 | Ap4m1 (mouse) | 449 | 93.8 | F255 | R283 |
| ortholog | Q2PWT8 | Ap4m1 (rat) | 453 | 92.9 | F255 | R283 |
| ortholog | E2RED8 | AP4M1 (dog) | 452 | 94.9 | F255 | R283 |
| ortholog | Q9SB50 | AP4M (*Arabidopsis*) | 451 | 36.6 | F261 | N289 |
| paralog | Q9BXS5 | AP1M1 / mu1A | 423 | 31.3 | F238 | S266 |
| paralog | Q9Y6Q5 | AP1M2 / mu1B | 423 | 31.8 | F238 | S266 |
| paralog | Q96CW1 | AP2M1 / mu2 | 435 | 31.0 | F248 | R276 |
| paralog | Q9Y2T2 | AP3M1 / mu3A | 418 | 26.2 | F233 | S261 |
| paralog | P53677 | AP3M2 / mu3B | 418 | 24.5 | F233 | S261 |

Two conclusions, one of them negative and worth stating plainly:

1. **The site is conserved across mammalian mu4.** F255 and R283 are present in mouse,
   rat and dog mu4 at the same native positions. This is the sequence-level condition
   under which the UniProt ISS rows that transfer dog (E2RED8) and mouse (Q9JKC7)
   annotations onto human AP4M1 are safe: the donor and the target share the
   cargo-recognition surface that those annotations depend on. *Arabidopsis* AP4M keeps
   the phenylalanine but not the arginine (N289), so the site is not pan-eukaryotic.

2. **The alignment does not, on its own, show that mu4 binds cargo at a site distinct
   from the clathrin adaptors.** F255 has a phenylalanine counterpart in every mu
   subunit tested, including all five clathrin-adaptor paralogs, so it is a family-wide
   feature and carries no mu4-specific information. R283 does separate mu4 from mu1A,
   mu1B, mu3A and mu3B (all serine), but mu2 has an arginine at the aligned position
   (R276). The claim that the APP-binding site on mu4 is *located differently* from the
   canonical mu2 YXXPhi site rests on the crystallography in PMID:20230749, not on this
   alignment, and the review cites it that way.

The pairwise identities independently reproduce the figure from the original cloning
paper: mu4 is 24.5-31.8% identical to the mu1/mu2/mu3 subunits here, against
"27-31%, identity with mu1-adaptin (ap47) and mu2-adaptin (ap50)" reported in
PMID:9013859.

## 2. GOA-to-review reconciliation

`goa_reconciliation.py` re-derives the seeding key from `AP4M1-goa.tsv` (GO id, evidence
code, reference, WITH/FROM split on `|` and normalised) and checks that every GOA row
maps onto exactly one non-`NEW` entry in `AP4M1-ai-review.yaml` with an identical
normalised `supporting_entities` list, and vice versa. It reports the one legitimate
many-to-one case: GOA carries two `GO:0005515 IPI PMID:32073997 UniProtKB:Q9UJC3` rows
that differ only in their DATE column, which the deterministic seeder collapses into a
single YAML entry. No GO term, evidence code, reference or WITH/FROM value is lost by
that collapse.

## 3. Are the three cited ARBA rules reproducible on AP4M1?

`arba_conditions.py` fetches each ARBA rule named in a GOA WITH/FROM column
(`rest.uniprot.org/arba/<id>`), fetches AP4M1's own signature cross-references from its
UniProt record (7 InterPro, 2 Pfam, 2 PROSITE, 1 PANTHER, 1 PIRSF, 1 PRINTS, 2 SUPFAM,
2 CDD, 2 FunFam; 90 cross-reference ids in total), and counts how many of the rule's
condition sets are fully satisfied by those signatures plus the human taxonomic lineage.

| rule | asserts | condition sets | condition types | sets satisfied by AP4M1 |
|---|---|---|---|---|
| ARBA00026971 | GO:0005737 cytoplasm | 2388 | FunFam, InterPro, PANTHER, taxon | **0** |
| ARBA00028630 | GO:0006605 protein targeting | 16 | FunFam, taxon | 1 |
| ARBA00028253 | GO:0008104 intracellular protein localization | 126 | FunFam, InterPro, PANTHER, taxon | 1 |

The two protein-trafficking rules reproduce cleanly: each has exactly one condition set
satisfied by AP4M1, so those IEA rows follow from the rule as published. The cytoplasm
rule does not reproduce - of its 2388 condition sets, two mention an AP4M1 signature and
none is fully satisfied.

A non-reproducing rule is not thereby a wrong annotation. AP4M1 is cytoplasmic on
independent grounds, ARBA condition sets can key on evidence the entry's cross-reference
list does not expose, and the GOA row for GO:0005737 is a broad true parent either way.
The point of recording it is that the review's statement about that row should not claim
more than was checked.
