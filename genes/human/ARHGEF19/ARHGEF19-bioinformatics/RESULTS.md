# ARHGEF19 bioinformatics

Two questions, two scripts, both reproducible from this directory:

```
uv run python dh_competence_check.py        # -> RESULTS_raw.txt   (exit 0 = all assertions held)
uv run python selftest_guards.py            # mutation tests for the above
uv run python go_coverage_by_reference.py   # -> COVERAGE_raw.txt
```

Every sequence, profile, structure and annotation count is fetched live at run
time (UniProt REST, InterPro/Pfam, RCSB, QuickGO, PubMed E-utilities). Nothing
below is transcribed by hand from a database page; the raw output files are the
scripts' own stdout.

---

## 1. Is the ARHGEF19 DH–PH module a competent Dbl-family GEF?

`dh_competence_check.py`. The honest answer has to run in both directions, so
the panel carries both: five Dbl-family GEFs that have **both** a co-crystal
structure with their substrate GTPase **and** measured exchange activity, and
three negative controls.

### Published residue claims, checked against the current UniProt sequence

| Claim | Source | Result |
|---|---|---|
| Y295 is the N-terminal inhibitory-domain tyrosine that locks the DH domain; Y295E is autoinhibition-free | PMID:38714795 | position 295 **is** Y |
| The Dvl2-PDZ-binding internal motif spans residues 349–359 | PMID:38714795 | 349–359 **is** `GSTFSLWQDIP` |
| PDB 8YR7 fuses a WGEF peptide to the Dvl2 PDZ domain | RCSB 8YR7 | the deposited peptide `TFSLWQDIP` occurs **once**, at 351 |

Q8IW93 is 802 aa; the script aborts with exit 2 if that ever changes, because
every position above would then need re-checking.

### The profile fires on the module — and on a module that cannot work

Pfam PF00621 (RhoGEF / Dbl homology) at the gathering threshold:

| role | protein | DH envelope | bitscore |
|---|---|---|---|
| target | ARHGEF19 / WGEF / Ephexin-2 | 382–558 | 137.0 |
| paralogue | NGEF / Ephexin-1 | 278–455 | 139.2 |
| paralogue | ARHGEF5 / Ephexin-3 / TIM | 1180–1356 | 145.8 |
| paralogue | ARHGEF16 / Ephexin-4 | 289–466 | 140.1 |
| paralogue | ARHGEF15 / Ephexin-5 | 422–598 | 135.3 |
| paralogue | ARHGEF26 / SGEF | 444–621 | 141.6 |
| positive | ARHGEF12 / LARG (1X86 with RhoA) | 791–975 | 138.1 |
| positive | Dbs / Mcf2l (1LB1 with RhoA) | 636–810 | 134.6 |
| positive | ITSN1 (1KI1 with Cdc42) | 1242–1421 | 166.9 |
| positive | Tiam1 (1FOE with Rac1) | 1044–1232 | 142.5 |
| positive | TRIO (2NZ8 with Rac1) | 1973–2143 | 146.8 |
| control | **ARHGEF19 isoform 2** (484–783 deleted) | **382–496** | **65.5** |
| control | BTK (PH + SH3, no DH) | none | – |
| control | RHOA (the substrate) | none | – |

The truncation control is the useful one. Isoform 2 deletes residues 484–783 —
the C-terminal half of the DH domain plus all of PH and SH3 — and **still clears
the Pfam gathering threshold** on its surviving N-terminal half. A DH-profile hit
is therefore not evidence that a protein can catalyse exchange.

### The exchange surface, taken from structures rather than asserted

GEF-side residues within 4.5 Å of the GTPase were computed from the deposited
coordinates of **1X86** (LARG DH–PH : RhoA) and **1LB1** (Dbs DH–PH : RhoA), the
two complexes whose GTPase is ARHGEF19's own demonstrated substrate. Author
numbering in both structures was verified residue-by-residue against the
corresponding UniProt entry before anything was mapped (40 and 44 positions
respectively). Contacts inside the DH envelope were projected onto PF00621 match
states; 25 states are contacts in **both** complexes.

| role | protein | contact positions spanned / 25 | identical to LARG | % |
|---|---|---|---|---|
| target | ARHGEF19 | 24 | 9 | 36% |
| paralogue | NGEF / Ephexin-1 | 24 | 10 | 40% |
| paralogue | ARHGEF5 / Ephexin-3 | 24 | 11 | 44% |
| paralogue | ARHGEF16 / Ephexin-4 | 24 | 9 | 36% |
| paralogue | ARHGEF15 / Ephexin-5 | 23 | 8 | 32% |
| paralogue | ARHGEF26 / SGEF | 24 | 10 | 40% |
| positive | LARG (RhoA GEF) | 25 | 25 | 100% |
| positive | Dbs (RhoA GEF) | 25 | 14 | 56% |
| positive | ITSN1 (Cdc42 GEF) | 24 | 11 | 44% |
| positive | Tiam1 (Rac1 GEF) | 25 | 9 | 36% |
| positive | TRIO (Rac1 GEF) | 25 | 12 | 48% |
| control | ARHGEF19 isoform 2 | **5** | 2 | 8% |

The pass/fail threshold is taken from the data, not chosen: the weakest
verified-active comparator spans 24/25, and the script asserts (a) that the
target reaches that floor and (b) that the truncation control falls below it.
Both hold.

### What this does and does not establish

**It does** establish that ARHGEF19 presents a complete, canonical Dbl-family
exchange surface: 24 of the 25 RhoA-contacting positions are present, the same
coverage as ITSN1 and one position short of LARG, Dbs, Tiam1 and TRIO. There is
no residue-level reason to suspect a pseudo-GEF.

**It does not** establish that ARHGEF19 exchanges nucleotide, and it emphatically
does not establish *which* GTPase. Identity at the exchange surface is 36% for
ARHGEF19 against LARG — and **36% for Tiam1**, a GEF for a different GTPase
(Rac1) entirely. A measure that scores a Rac1 GEF exactly like ARHGEF19 cannot be
read as evidence that ARHGEF19 is a RhoA GEF. That question is settled by
biochemistry, not by this table: hWGEF activates RhoA and not Rac1 or Cdc42 in
side-by-side pulldowns (PMID:18256687, Fig. 2A–B), and binds RhoA strongly, Rac1
weakly and Cdc42 not at all (Fig. 2C).

The two directions therefore agree here — intact surface, demonstrated activity —
but they agree by coincidence of evidence, not because either implies the other.

### Guards

`selftest_guards.py` breaks one thing at a time and asserts the matching guard
fires with its expected message. 12 cases, including a negative control that must
stay silent and a duplicate-accession case (FASTA names are the join key for
hmmsearch/hmmalign, so a duplicated panel entry would silently merge two rows).
All 12 behave as specified. Mutation is done by rebinding a named module
attribute, so each anchor matches exactly once by construction.

---

## 2. How much of the ARHGEF19 literature has reached GO?

`go_coverage_by_reference.py` queries QuickGO by reference for every primary
paper on the gene and counts annotations in **any** species. The paper list comes
from two independent sources — the Affinage record's citations and a live PubMed
sweep over the gene's synonyms — so it does not depend on either being complete.
`"GEF19"` is one of the queries on purpose: PMID:21686262 is titled *"Grhl3 and
GEF19 in the front rho"* and no `ARHGEF19` or `WGEF` query returns it.

Of **14 primary experimental papers**:

- **11 have produced no GO annotation of any gene in any species.** That includes
  the paper that first demonstrated exchange activity (PMID:15485661), the paper
  that mapped autoinhibition relief (PMID:18537266), the 2024 structural and
  activity study (PMID:38714795), all three cancer-pathway papers
  (PMID:29164615, PMID:32993957, PMID:34813497), the ciliogenesis paper
  (PMID:31469868), and the only published *negative* result (PMID:20810787).
- **12 have produced no GO annotation of ARHGEF19 in any species.**
- **1** has produced an ARHGEF19 annotation to anything other than
  `GO:0005515 protein binding` — PMID:20643356, and that is a mouse genetics
  paper whose subject is GRHL3.

The single richest paper on this gene, PMID:18256687 (EMBO J), yielded exactly
**one** ARHGEF19 annotation: `GO:0005515 protein binding` with RhoA. The same
figure panel that supports that IPI (Fig. 2C) sits beside a RhoA activation assay
(Fig. 2A), a Rac1/Cdc42 negative (Fig. 2B), a Dvl2-domain mapping (Fig. 5C), a
Daam1 co-IP (Fig. 5D), a human MCF-7 RNAi experiment (Fig. 5B) and an
autoinhibition mapping (Fig. 6) — none of which reached GO.

This is a coverage problem, not an over-annotation problem. The review's actions
follow from that: almost nothing to remove, a great deal missing.
