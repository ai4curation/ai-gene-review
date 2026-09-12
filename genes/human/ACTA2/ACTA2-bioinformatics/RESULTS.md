# ACTA2 (P62736) — computed analysis

Regenerate with `uv run python analyze_acta2.py`; both this file and `results.json` are
rewritten in full, so `git diff` after a run is the check that nothing here was hand-edited.

## 1. GO:0005200 structural constituent of cytoskeleton: who still receives it

PAINT asserts GO:0005200 exactly once in PTHR11937, at node **PTN000940351** (IBD, 20250805, 10 seeds), and negates it by IRD at **8** descendant nodes. The assertion count is asserted by the script, so a change to the tree breaks the run rather than the argument.

Human GO:0005200 rows in QuickGO: **389** in total, of which **43** are IBA. The IBA rows resolve to 7 PANTHER nodes:

| PANTHER node | n human genes | genes |
|---|---|---|
| PTN000172598 | 21 | TUBA1A, TUBA1B, TUBA1C, TUBA3C, TUBA3D, TUBA3E, TUBA4A, TUBA8, TUBAL3, TUBB, TUBB1, TUBB2A, TUBB2B, TUBB3, TUBB4A, TUBB4B, TUBB6, TUBB8, TUBB8B, TUBD1, TUBE1 |
| PTN000580114 | 5 | DES, GFAP, NEFM, PRPH, VIM |
| PTN000940351 | 10 | ACTA1, ACTA2, ACTC1, ACTG2, ACTL10, ACTL9, ACTR10, ACTRT1, ACTRT2, ACTRT3 |
| PTN001145669 | 3 | LMNA, LMNB1, LMNB2 |
| PTN002753803 | 1 | PLEC |
| PTN002760594 | 2 | EPB41, EPB41L2 |
| PTN002932247 | 1 | SYNM |

So the set still receiving the term from the actin node PTN000940351 is **10 genes**: ACTA1, ACTA2, ACTC1, ACTG2, ACTL10, ACTL9, ACTR10, ACTRT1, ACTRT2, ACTRT3. ACTA2 is IN that set.

Evidence route per actin-family gene that holds the term at all — the distinction that
makes the IBA set and the holds-the-term set two different sets:

| gene | route(s) |
|---|---|
| ACTA1 | IBA (GO_REF:0000033, GO_Central); TAS (PMID:10508519, UniProt) |
| ACTA2 | IBA (GO_REF:0000033, GO_Central) |
| ACTB | TAS (PMID:6202424, UniProt) |
| ACTC1 | IBA (GO_REF:0000033, GO_Central) |
| ACTG1 | IC (PMID:16130169, UniProt) |
| ACTG2 | IBA (GO_REF:0000033, GO_Central) |
| ACTL10 | IBA (GO_REF:0000033, GO_Central) |
| ACTL6B | TAS (PMID:10380635, PINC) |
| ACTL7A | TAS (PMID:10373328, PINC) |
| ACTL7B | TAS (PMID:10373328, PINC) |
| ACTL9 | IBA (GO_REF:0000033, GO_Central) |
| ACTR10 | IBA (GO_REF:0000033, GO_Central) |
| ACTR2 | IDA (PMID:11741539, FlyBase) |
| ACTR3 | IDA (PMID:11741539, FlyBase) |
| ACTRT1 | IBA (GO_REF:0000033, GO_Central) |
| ACTRT2 | IBA (GO_REF:0000033, GO_Central) |
| ACTRT3 | IBA (GO_REF:0000033, GO_Central) |

### The seeds of the assertion, and what evidence each holds for the term it donated

| seed | resolves to | status | own codes on GO:0005200 | experimental? |
|---|---|---|---|---|
| `SGD:S000001855` | ACT1 (P60010, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 375 aa) | Swiss-Prot | IBAx1, IDAx1 | yes |
| `UniProtKB:P61160` | ACTR2 (P61160, Homo sapiens, 394 aa) | Swiss-Prot | IDAx1 | yes |
| `MGI:MGI:87906` | Actg1 (P63260, Mus musculus, 375 aa) | Swiss-Prot | IDAx1 | yes |
| `dictyBase:DDB_G0269234` | act1 (P07830, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx1 | yes |
| `SGD:S000002513` | ARP10 (Q04549, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 284 aa) | Swiss-Prot | IPIx3 | yes |
| `UniProtKB:P61158` | ACTR3 (P61158, Homo sapiens, 418 aa) | Swiss-Prot | IDAx1 | yes |
| `dictyBase:DDB_G0289811` | act10 (Q54GX7, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx1 | yes |
| `RGD:1304556` | Actg1 (P63259, Rattus norvegicus, 375 aa) | Swiss-Prot | ISOx1 | no |
| `UniProtKB:P60709` | ACTB (P60709, Homo sapiens, 375 aa) | Swiss-Prot | TASx1 | no |
| `SGD:S000001171` | ARP1 (P38696, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 384 aa) | Swiss-Prot | IDAx1 | yes |

### Is any seed of the assertion also inside a clade the same term was negated in?

**Yes — 2 of 10.** These proteins supply the experimental support that justifies GO:0005200 at the family root, and PAINT then exempts their own clades from the term it justified:

| seed | gene | organism | IRD-negated node(s) whose clade it seeds |
|---|---|---|---|
| `UniProtKB:P61160` | ACTR2 | Homo sapiens | PTN000233596 |
| `UniProtKB:P61158` | ACTR3 | Homo sapiens | PTN000233796 |


| IRD-negated node | date | IRD seed |
|---|---|---|
| PTN000233596 | 20260416 | PANTHER:PTN000940351 |
| PTN000233752 | 20250805 | PANTHER:PTN000940351 |
| PTN000233796 | 20260416 | PANTHER:PTN000940351 |
| PTN000233887 | 20250805 | PANTHER:PTN000940351 |
| PTN000234048 | 20250805 | PANTHER:PTN000940351 |
| PTN001732543 | 20250805 | PANTHER:PTN000940351 |
| PTN007551901 | 20260416 | PANTHER:PTN000940351 |
| PTN008986528 | 20250805 | PANTHER:PTN000940351 |

## 1b. Which node carries which term, and what is each node FOR

Two different questions. The first cannot find a node that gives a gene nothing it should
have; the second can.

**GO:0005884** - PANTHER nodes projecting it onto any conventional human actin:

| node | human conventional actins reached |
|---|---|
| PTN000233075 | ACTA1 |
| PTN000748220 | ACTC1 |
| PTN002631586 | ACTB, ACTBL2, ACTG1, ACTL8, POTEE, POTEF, POTEI, POTEJ, POTEKP |

| conventional actin | own annotations to this term or its descendants |
|---|---|
| ACTA1 | GO:0005884:IBA, GO:0005884:IDA |
| ACTA2 | **nothing, at any granularity** |
| ACTC1 | GO:0005884:IBA, GO:0005884:IDA |
| ACTG2 | **nothing, at any granularity** |
| ACTB | GO:0005884:IBA |
| ACTG1 | GO:0005884:IBA, GO:0005884:IDA |

**GO:0017022** - PANTHER nodes projecting it onto any conventional human actin:

| node | human conventional actins reached |
|---|---|
| PTN000748220 | ACTC1 |

| conventional actin | own annotations to this term or its descendants |
|---|---|
| ACTA1 | GO:0017022:TAS |
| ACTA2 | **nothing, at any granularity** |
| ACTC1 | GO:0017022:IBA, GO:0017022:IDA, GO:0017022:IPI |
| ACTG2 | **nothing, at any granularity** |
| ACTB | **nothing, at any granularity** |
| ACTG1 | **nothing, at any granularity** |

**GO:0033275** - PANTHER nodes projecting it onto any conventional human actin:

| node | human conventional actins reached |
|---|---|
| PTN000748220 | ACTC1 |

| conventional actin | own annotations to this term or its descendants |
|---|---|
| ACTA1 | **nothing, at any granularity** |
| ACTA2 | **nothing, at any granularity** |
| ACTC1 | GO:0033275:IBA, GO:0033275:IMP |
| ACTG2 | **nothing, at any granularity** |
| ACTB | **nothing, at any granularity** |
| ACTG1 | **nothing, at any granularity** |

**GO:0007015** - PANTHER nodes projecting it onto any conventional human actin:

| node | human conventional actins reached |
|---|---|
| PTN000748220 | ACTC1 |

| conventional actin | own annotations to this term or its descendants |
|---|---|
| ACTA1 | GO:0030240:IBA, GO:0030240:IMP |
| ACTA2 | **nothing, at any granularity** |
| ACTC1 | GO:0007015:IBA, GO:0030240:ISS |
| ACTG2 | **nothing, at any granularity** |
| ACTB | **nothing, at any granularity** |
| ACTG1 | **nothing, at any granularity** |

**GO:0005576** - PANTHER nodes projecting it onto any conventional human actin:

| node | human conventional actins reached |
|---|---|
| PTN004322804 | ACTA2, ACTG2 |

| conventional actin | own annotations to this term or its descendants |
|---|---|
| ACTA1 | GO:0005576:HDA, GO:0070062:HDA, GO:0072562:HDA |
| ACTA2 | GO:0005576:HDA, GO:0005576:IBA, GO:0005604:IEA, GO:0070062:HDA |
| ACTC1 | GO:0005576:HDA, GO:0070062:HDA, GO:0072562:HDA |
| ACTG2 | GO:0005576:HDA, GO:0005576:IBA, GO:0070062:HDA, GO:0072562:HDA |
| ACTB | GO:0005576:HDA, GO:0070062:HDA, GO:0072562:HDA |
| ACTG1 | GO:0005576:HDA, GO:0070062:HDA, GO:0070062:IDA, GO:0072562:HDA |

Reverse direction - the entire human reach of each node that appeared above:

| node | human annotations | human genes | terms | reach == ACTA2+ACTG2 only |
|---|---|---|---|---|
| PTN000233075 | 4 | ACTA1 | GO:0001725; GO:0005865; GO:0005884; GO:0030240 |  |
| PTN000748220 | 6 | ACTC1 | GO:0005884; GO:0007015; GO:0017022; GO:0030017; GO:0033275; GO:0060047 |  |
| PTN002631586 | 18 | ACTB, ACTBL2, ACTG1, ACTL8, POTEE, POTEF, POTEI, POTEJ, POTEKP | GO:0005884; GO:0098973 |  |
| PTN004322804 | 2 | ACTA2, ACTG2 | GO:0005576 | YES |

## 2. Residue tallies at the nucleotide site and the filament protomer interface

- **nucleotide_site**: PDB 2BTF chain A, ligands ATP, SR, 4.0 Å heavy-atom cutoff → 19 contact residues.
- **filament_interface**: PDB 6DJO chain C, 4.0 Å heavy-atom cutoff → 38 contact residues.

Reproduction check: this script reproduces the committed ACTL8 filament-interface tally for 9 shared panel members (ACTL8 (human actin-like 8); ACTB (human beta-actin; IBA donor); ACTG1 (human gamma-actin; IBA donor); ACTA1 (human alpha-skeletal actin; IBA donor); ACTC1 (human alpha-cardiac actin; IBA donor); ACTR2 (human Arp2); ACTR3 (human Arp3); ACTRT1 (human actin-related protein T1); Arp53D (Drosophila actin-like 53D; IBA donor)); a mismatch aborts the run.

Reference-length guard: panel median 376 aa, so anything below 338.4 aa cannot be scored as if every structural position were tested. Flagged: ACTL10 (245 aa, 0.65 of median). `outside_span` is reported as its own column below so an unreached position can never be added to a substitution count again.

### nucleotide site (19 positions)

| protein | ident | cons | non-cons | internal gap | outside span | positions present | compatible / present | %id to chain |
|---|---|---|---|---|---|---|---|---|
| ACTB (human beta-actin) - cytoplasmic actin, PTN000940351 IBD seed | 19 | 0 | 0 | 0 | 0 | 19 | 19/19 | 100.0 |
| ACTA1 (human alpha-skeletal actin) - shares ACTA2's IBA row | 18 | 1 | 0 | 0 | 0 | 19 | 19/19 | 93.6 |
| ACTA2 (human aortic smooth-muscle actin) - THIS GENE | 18 | 1 | 0 | 0 | 0 | 19 | 19/19 | 94.1 |
| ACTG2 (human enteric smooth-muscle actin) - shares ACTA2's IBA row | 18 | 1 | 0 | 0 | 0 | 19 | 19/19 | 93.6 |
| ACTC1 (human alpha-cardiac actin) - shares ACTA2's IBA row | 18 | 1 | 0 | 0 | 0 | 19 | 19/19 | 94.1 |
| ACTG1 (human gamma-cytoplasmic actin) - GO:0005200 by IC, not IBA | 19 | 0 | 0 | 0 | 0 | 19 | 19/19 | 98.9 |
| Arp53D (Drosophila actin-like 53D) - divergent actin that DOES polymerise | 16 | 3 | 0 | 0 | 0 | 19 | 19/19 | 64.4 |
| ACTR2 (human Arp2) - IBD seed AND IRD-negated at its own node | 16 | 3 | 0 | 0 | 0 | 19 | 19/19 | 48.7 |
| ACTR3 (human Arp3) - IBD seed AND IRD-negated at its own node | 14 | 4 | 1 | 0 | 0 | 19 | 18/19 | 40.9 |
| ACTRT1 (human actin-related protein T1) - shares ACTA2's IBA row | 14 | 2 | 3 | 0 | 0 | 19 | 16/19 | 48.7 |
| ACTL8 (human actin-like 8) - reviewed sibling, REMOVE verdict | 11 | 3 | 5 | 0 | 0 | 19 | 14/19 | 34.4 |
| ACTR10 (human Arp11) - shares ACTA2's IBA row, non-polymerising | 9 | 2 | 8 | 0 | 0 | 19 | 11/19 | 27.8 |
| ACTL10 (human actin-like 10) - shares ACTA2's IBA row; 245 aa Swiss-Prot entry | 7 | 3 | 4 | 0 | 5 | 14 | 10/14 | 33.5 |

### filament interface (38 positions)

| protein | ident | cons | non-cons | internal gap | outside span | positions present | compatible / present | %id to chain |
|---|---|---|---|---|---|---|---|---|
| ACTB (human beta-actin) - cytoplasmic actin, PTN000940351 IBD seed | 37 | 1 | 0 | 0 | 0 | 38 | 38/38 | 93.8 |
| ACTA1 (human alpha-skeletal actin) - shares ACTA2's IBA row | 38 | 0 | 0 | 0 | 0 | 38 | 38/38 | 100.0 |
| ACTA2 (human aortic smooth-muscle actin) - THIS GENE | 38 | 0 | 0 | 0 | 0 | 38 | 38/38 | 98.4 |
| ACTG2 (human enteric smooth-muscle actin) - shares ACTA2's IBA row | 38 | 0 | 0 | 0 | 0 | 38 | 38/38 | 98.7 |
| ACTC1 (human alpha-cardiac actin) - shares ACTA2's IBA row | 38 | 0 | 0 | 0 | 0 | 38 | 38/38 | 99.5 |
| ACTG1 (human gamma-cytoplasmic actin) - GO:0005200 by IC, not IBA | 37 | 1 | 0 | 0 | 0 | 38 | 38/38 | 94.1 |
| Arp53D (Drosophila actin-like 53D) - divergent actin that DOES polymerise | 29 | 4 | 5 | 0 | 0 | 38 | 33/38 | 63.2 |
| ACTR2 (human Arp2) - IBD seed AND IRD-negated at its own node | 15 | 7 | 16 | 0 | 0 | 38 | 22/38 | 48.4 |
| ACTRT1 (human actin-related protein T1) - shares ACTA2's IBA row | 13 | 8 | 17 | 0 | 0 | 38 | 21/38 | 47.8 |
| ACTR10 (human Arp11) - shares ACTA2's IBA row, non-polymerising | 9 | 5 | 12 | 12 | 0 | 38 | 14/38 | 28.5 |
| ACTL8 (human actin-like 8) - reviewed sibling, REMOVE verdict | 8 | 3 | 24 | 3 | 0 | 38 | 11/38 | 34.2 |
| ACTR3 (human Arp3) - IBD seed AND IRD-negated at its own node | 5 | 3 | 29 | 1 | 0 | 38 | 8/38 | 41.1 |
| ACTL10 (human actin-like 10) - shares ACTA2's IBA row; 245 aa Swiss-Prot entry | 3 | 2 | 13 | 0 | 20 | 18 | 5/18 | 32.7 |

Robustness: the same three proteins under a second substitution matrix and gap model.

| protein | scheme | surface | id/cons/non-cons/int-gap/outside |
|---|---|---|---|
| ACTA2 | BLOSUM62/-11/-1 | nucleotide_site | 18/1/0/0/0 |
| ACTA2 | BLOSUM62/-11/-1 | filament_interface | 38/0/0/0/0 |
| ACTB | BLOSUM62/-11/-1 | nucleotide_site | 19/0/0/0/0 |
| ACTB | BLOSUM62/-11/-1 | filament_interface | 37/1/0/0/0 |
| ACTL8 | BLOSUM62/-11/-1 | nucleotide_site | 11/3/5/0/0 |
| ACTL8 | BLOSUM62/-11/-1 | filament_interface | 8/3/24/3/0 |
| ACTA2 | BLOSUM45/-14/-2 | nucleotide_site | 18/1/0/0/0 |
| ACTA2 | BLOSUM45/-14/-2 | filament_interface | 38/0/0/0/0 |
| ACTB | BLOSUM45/-14/-2 | nucleotide_site | 19/0/0/0/0 |
| ACTB | BLOSUM45/-14/-2 | filament_interface | 37/1/0/0/0 |
| ACTL8 | BLOSUM45/-14/-2 | nucleotide_site | 11/3/5/0/0 |
| ACTL8 | BLOSUM45/-14/-2 | filament_interface | 8/3/24/3/0 |

## 3. ACTA2 disease variants against those two surfaces

19 FT VARIANT positions parsed from the cached UniProt entry, mapped onto each structure by the same alignment used for the tallies (never by an assumed offset).

The per-surface table below uses the SINGLE-chain contact sets, which is the right basis
for the cross-species panel in section 2 (every protein is scored on the same positions)
but the wrong basis for this question: chain C of the filament model has no i+2 neighbour,
and actin protomer contacts are not symmetric, so a residue reaching only 'upward' is
invisible from it. The derived counts that follow, and the distance table, use the minimum
over every chain. Reading the single-chain table alone would have said no pathogenic
variant touches another protomer; four do.

| surface | n contact res | chain len | % of chain | pathogenic on surface | which | non-pathogenic on surface |
|---|---|---|---|---|---|---|
| nucleotide site | 19 | 374 | 5.1% | 0/16 | - | 0/3 |
| filament interface | 38 | 372 | 10.2% | 0/16 | - | 1/3 |

All-chain derived counts (the headline figures):

| measure | n | ACTA2 positions |
|---|---|---|
| pathogenic within 4A of another protomer | 4 | 145, 292, 326, 353 |
| pathogenic within 5A of another protomer | 6 | 145, 179, 179, 292, 326, 353 |
| nonpathogenic within 4A of another protomer | 1 | 196 |
| nonpathogenic within 5A of another protomer | 1 | 196 |
| pathogenic within 5A of nucleotide | 2 | 185, 212 |
| nonpathogenic within 5A of nucleotide | 0 | - |

| ACTA2 pos | disease | on surface | interface partner chains | note |
|---|---|---|---|---|
| 39 | AAT6 | neither | - | R -> H (in AAT6; dbSNP:rs794728021) |
| 117 | AAT6 | neither | - | N -> T (in AAT6) ECO:0000269|PubMed:19409525 |
| 118 | AAT6 | neither | - | R -> Q (in AAT6; dbSNP:rs112602953) ECO:0000269|PubMed:19409 |
| 135 | AAT6 | neither | - | Y -> H (in AAT6; dbSNP:rs751300489) |
| 145 | AAT6 | neither | - | Y -> C (in AAT6) |
| 149 | AAT6 | neither | - | R -> C (in AAT6; dbSNP:rs121434526) ECO:0000269|PubMed:19409 |
| 154 | AAT6 | neither | - | V -> A (in AAT6; dbSNP:rs1554841298) ECO:0000269|PubMed:1940 |
| 179 | SMDYS | neither | - | R -> C (in SMDYS; dbSNP:rs886039303) |
| 179 | MYMY5, SMDYS | neither | - | R -> H (in MYMY5 and SMDYS; disease phenotype include smooth |
| 185 | AAT6 | neither | - | R -> Q (in AAT6; dbSNP:rs1057521105) |
| 196 | not disease-linked | filament interface | ['B'] | T -> S (in dbSNP:rs1803028) |
| 212 | AAT6 | neither | - | R -> Q (in AAT6; dbSNP:rs397516685) ECO:0000269|PubMed:19639 |
| 258 | AAT6 | neither | - | R -> C (in AAT6; dbSNP:rs121434528) ECO:0000269|PubMed:19409 |
| 258 | AAT6 | neither | - | R -> H (in AAT6; dbSNP:rs121434527) ECO:0000269|PubMed:19409 |
| 292 | AAT6 | neither | - | R -> G (in AAT6) |
| 320 | not disease-linked | neither | - | T -> A (in dbSNP:rs1803027) |
| 326 | AAT6 | neither | - | T -> N (in AAT6; dbSNP:rs777832794) |
| 353 | AAT6 | neither | - | T -> N (in AAT6) ECO:0000269|PubMed:19409525 |
| 373 | not disease-linked | neither | - | H -> P (in dbSNP:rs1062398) |

### Numbering and contact-set controls

P62736 is a 377-residue precursor and the structures use mature actin numbering, so the
offset should be -2. Verified against three sources that state both numbers, and the
contact set is itself checked against the residues PMID:26637293 names as R179's
inter-strand partners. Any failure aborts the run.

| control | provenance |
|---|---|
| nucleotide_site:86->84 | UniProt CC PTM line gives both numbers: "Monomethylation at Lys-86 (K84me1)" |
| nucleotide_site:75->73 | SETD3 methylates actin His73; UniProt annotates it at precursor position 75 |
| nucleotide_site:179->177 | PMID:26637293: "R179 (R177 in alpha1-actin)" |
| filament_interface:86->84 | UniProt CC PTM line gives both numbers: "Monomethylation at Lys-86 (K84me1)" |
| filament_interface:75->73 | SETD3 methylates actin His73; UniProt annotates it at precursor position 75 |
| filament_interface:179->177 | PMID:26637293: "R179 (R177 in alpha1-actin)" |

| residue named by PMID:26637293 | structure position | in contact set | partners |
|---|---|---|---|
| K193 | 191 | True | ['B'] |
| T196 | 194 | True | ['B'] |

### Closest approach, because an absence from a 4 Å set is not a finding

Measured over every chain of the filament model, not one: with four protomers no single
chain has both its i-2 and its i+2 neighbour, so a per-chain answer would silently omit
one strand relationship.

| ACTA2 pos | disease | min Å to another protomer | via | min Å to nucleotide |
|---|---|---|---|---|
| 326 | AAT6 | 2.82 | same-strand (i+/-2) | 30.86 |
| 145 | AAT6 | 3.04 | same-strand (i+/-2) | 14.2 |
| 292 | AAT6 | 3.21 | same-strand (i+/-2) | 24.0 |
| 196 | not disease-linked | 3.28 | cross-strand (i+/-1) | 17.55 |
| 353 | AAT6 | 3.53 | same-strand (i+/-2) | 23.44 |
| 179 | SMDYS | 4.42 | cross-strand (i+/-1) | 8.11 |
| 179 | MYMY5, SMDYS | 4.42 | cross-strand (i+/-1) | 8.11 |
| 149 | AAT6 | 5.16 | same-strand (i+/-2) | 17.36 |
| 135 | AAT6 | 5.7 | same-strand (i+/-2) | 14.49 |
| 39 | AAT6 | 6.53 | cross-strand (i+/-1) | 19.04 |
| 117 | AAT6 | 6.55 | cross-strand (i+/-1) | 12.58 |
| 258 | AAT6 | 7.0 | cross-strand (i+/-1) | 11.95 |
| 258 | AAT6 | 7.0 | cross-strand (i+/-1) | 11.95 |
| 373 | not disease-linked | 7.16 | cross-strand (i+/-1) | 19.79 |
| 118 | AAT6 | 8.21 | cross-strand (i+/-1) | 14.64 |
| 154 | AAT6 | 8.44 | same-strand (i+/-2) | 9.86 |
| 212 | AAT6 | 10.12 | same-strand (i+/-2) | 4.25 |
| 185 | AAT6 | 10.48 | cross-strand (i+/-1) | 4.24 |
| 320 | not disease-linked | 10.61 | same-strand (i+/-2) | 22.37 |

## 4b. GO:0005515 partners, resolved, and how the interactions were detected

| token | resolves to | status | UniProt subcellular location | GOA references |
|---|---|---|---|---|
| `UniProtKB:P11684` | SCGB1A1 (P11684, 91 aa) | Swiss-Prot | Secreted | PMID:28514442, PMID:33961781 |
| `UniProtKB:P17900` | GM2A (P17900, 193 aa) | Swiss-Prot | Lysosome | PMID:28514442, PMID:33961781 |
| `UniProtKB:Q8N4U5` | TCP11L2 (Q8N4U5, 519 aa) | Swiss-Prot | Cytoplasm, cytoskeleton | PMID:28514442, PMID:33961781 |
| `UniProtKB:Q9BWQ6` | YIPF2 (Q9BWQ6, 316 aa) | Swiss-Prot | Golgi apparatus, cis-Golgi network membrane; Golgi apparatus, trans-Golgi network membrane; Late endosome membrane | PMID:28514442, PMID:33961781 |
| `UniProtKB:Q9BXW4` | MAP1LC3C (Q9BXW4, 147 aa) | Swiss-Prot | Cytoplasm, cytoskeleton; Cytoplasmic vesicle, autophagosome membrane; Endomembrane system | PMID:28514442, PMID:33961781 |

IntAct holds **320** interactions for P62736. Detection methods:

| detection method | interaction rows |
|---|---|
| anti tag coip | 275 |
| tap | 20 |
| anti bait coip | 8 |
| two hybrid pooling | 3 |
| pull down | 3 |
| 2 hybrid | 2 |
| cosedimentation | 2 |
| two hybrid array | 1 |
| proximity labelling technology | 1 |
| proximity-dependent biotin identification | 1 |
| 2h fragment pooling | 1 |
| confocal microscopy | 1 |
| crosslink | 1 |
| clash | 1 |

172 of 239 IntAct partners are logged exactly once.

## Retraction / erratum / correction status of the PMIDs this review leans on

21 checked, **1** flagged. Both halves are read: the publication-type list AND the cited article's own CommentsCorrections block, because a Publisher Correction is invisible to a publication-type query.

| PMID | flags | retracted publication type | correction record |
|---|---|---|---|
| 17994018 | ErratumIn | no | ErratumIn -> no PubMed record; Crossref: 10.1038/ng0208-255c (erratum) |

## 4. WITH/FROM resolution and donor evidence

32 non-experimental GOA rows carry 69 WITH/FROM tokens in total. Counts are derived from the GOA field, with an assertion, because hand-maintained source lists drifted on three genes in this campaign.

**GO:0005576 extracellular region** (cellular_component, IBA, is_active_in, GO_REF:0000033, assigned by GO_Central) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `PANTHER:PTN004322804` | PANTHER internal tree node, not a protein - carries no evidence of its own | - | - |
| `RGD:621676` | Acta2 (P62738, Rattus norvegicus, 377 aa) [3 candidates] | Swiss-Prot | IBAx1, IDAx1 |

**GO:0015629 actin cytoskeleton** (cellular_component, IBA, is_active_in, GO_REF:0000033, assigned by GO_Central) — 25 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `CGD:CAL0000191211` | ACT1 (A0A1D8PFR4, Candida albicans (strain SC5314 / ATCC MYA-2876), 376 aa) | TrEMBL (unreviewed) | IBAx1, IDAx1 |
| `FB:FBgn0011743` | Arp53D (P45891, Drosophila melanogaster, 376 aa) | Swiss-Prot | IBAx1, IDAx1 |
| `MGI:MGI:87906` | Actg1 (P63260, Mus musculus, 375 aa) [5 candidates] | Swiss-Prot | IBAx2, IDAx3, IEAx1, ISOx5 |
| `MGI:MGI:87909` | Acta2 (P62737, Mus musculus, 377 aa) [4 candidates] | Swiss-Prot | IBAx1, IDAx1, IEAx2, ISOx2, ISSx1 |
| `PANTHER:PTN002631484` | PANTHER internal tree node, not a protein - carries no evidence of its own | - | - |
| `PomBase:SPBC32H8.12c` | act1 (P10989, Schizosaccharomyces pombe (strain 972 / ATCC 24843), 375 aa) | Swiss-Prot | IBAx1, IDAx4, TASx1 |
| `RGD:1304556` | Actg1 (P63259, Rattus norvegicus, 375 aa) [2 candidates] | Swiss-Prot | IBAx2, IDAx4, ISOx3 |
| `RGD:621676` | Acta2 (P62738, Rattus norvegicus, 377 aa) [3 candidates] | Swiss-Prot | IBAx1, IDAx2, ISOx1, ISSx1 |
| `RGD:628837` | Actb (P60711, Rattus norvegicus, 375 aa) [3 candidates] | Swiss-Prot | IBAx2, IDAx2, ISOx3 |
| `SGD:S000001855` | ACT1 (P60010, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 375 aa) | Swiss-Prot | IBAx1, IDAx9 |
| `UniProtKB:P08023` | ACTA2 (P08023, Gallus gallus, 377 aa) | Swiss-Prot | IBAx1, IDAx1 |
| `UniProtKB:P60709` | ACTB (P60709, Homo sapiens, 375 aa) | Swiss-Prot | IBAx2, IDAx3, IMPx1 |
| `UniProtKB:P63261` | ACTG1 (P63261, Homo sapiens, 375 aa) | Swiss-Prot | IBAx2, IDAx1 |
| `UniProtKB:P68032` | ACTC1 (P68032, Homo sapiens, 377 aa) | Swiss-Prot | IBAx2, IDAx2, ISSx1 |
| `UniProtKB:P68133` | ACTA1 (P68133, Homo sapiens, 377 aa) | Swiss-Prot | IBAx4, IDAx3, IMPx1, ISSx1 |
| `UniProtKB:Q6QAQ1` | ACTB (Q6QAQ1, Sus scrofa, 375 aa) | Swiss-Prot | IBAx2, IEAx2, IPIx1, ISSx1 |
| `UniProtKB:Q8I4X0` | ACT1 (Q8I4X0, Plasmodium falciparum (isolate 3D7), 376 aa) | Swiss-Prot | IBAx1, IDAx1, IEAx1, ISSx2 |
| `WB:WBGene00000064` | act-2 (P10984, Caenorhabditis elegans, 376 aa) | Swiss-Prot | IBAx1, IDAx1 |
| `WB:WBGene00000065` | act-3 (P0DM42, Caenorhabditis elegans, 376 aa) | Swiss-Prot | IBAx1, IDAx1 |
| `WB:WBGene00000066` | act-4 (P10986, Caenorhabditis elegans, 376 aa) [2 candidates] | Swiss-Prot | IBAx1, IDAx1 |
| `WB:WBGene00000067` | act-5 (O45815, Caenorhabditis elegans, 375 aa) | TrEMBL (unreviewed) | IBAx1, IDAx2 |
| `dictyBase:DDB_G0269234` | act1 (P07830, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx3, IEAx1 |
| `dictyBase:DDB_G0275023` | act22 (Q553U6, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx1, IEAx1, ISSx1 |
| `dictyBase:DDB_G0289487` | act3 (P07829, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx1, IEAx1, ISSx1 |
| `dictyBase:DDB_G0289811` | act10 (Q54GX7, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx3, IEAx1 |

**GO:0005200 structural constituent of cytoskeleton** (molecular_function, IBA, enables, GO_REF:0000033, assigned by GO_Central) — 11 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `MGI:MGI:87906` | Actg1 (P63260, Mus musculus, 375 aa) [5 candidates] | Swiss-Prot | IBAx1, IDAx1, ISOx2 |
| `PANTHER:PTN000940351` | PANTHER internal tree node, not a protein - carries no evidence of its own | - | - |
| `RGD:1304556` | Actg1 (P63259, Rattus norvegicus, 375 aa) [2 candidates] | Swiss-Prot | IBAx1, IDAx2, ISOx1 |
| `SGD:S000001171` | ARP1 (P38696, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 384 aa) | Swiss-Prot | IDAx1 |
| `SGD:S000001855` | ACT1 (P60010, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 375 aa) | Swiss-Prot | IBAx1, IDAx1 |
| `SGD:S000002513` | ARP10 (Q04549, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), 284 aa) | Swiss-Prot | IPIx3 |
| `UniProtKB:P60709` | ACTB (P60709, Homo sapiens, 375 aa) | Swiss-Prot | EXPx1, IBAx1, IDAx3, IMPx1, TASx1 |
| `UniProtKB:P61158` | ACTR3 (P61158, Homo sapiens, 418 aa) | Swiss-Prot | IDAx1 |
| `UniProtKB:P61160` | ACTR2 (P61160, Homo sapiens, 394 aa) | Swiss-Prot | IDAx1 |
| `dictyBase:DDB_G0269234` | act1 (P07830, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx1 |
| `dictyBase:DDB_G0289811` | act10 (Q54GX7, Dictyostelium discoideum, 376 aa) | Swiss-Prot | IBAx1, IDAx1 |

**GO:0005856 cytoskeleton** (cellular_component, IEA, located_in, GO_REF:0000044, assigned by UniProt) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB-SubCell:SL-0090` | a UniProt Subcellular Location vocabulary id, not a gene product | - | - |

**GO:0007010 cytoskeleton organization** (biological_process, IEA, involved_in, GO_REF:0000108, assigned by GOC) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `GO:0005200` | a GO term, not a gene product - this row is an inter-ontology inference | - | - |

**GO:0001725 stress fiber** (cellular_component, IEA, located_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IDAx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0005604 basement membrane** (cellular_component, IEA, located_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IDAx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0006936 muscle contraction** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IDAx1, ISOx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0015629 actin cytoskeleton** (cellular_component, IEA, located_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IBAx1, IDAx2, ISOx1, ISSx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0019901 protein kinase binding** (molecular_function, IEA, enables, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62737` | Acta2 (P62737, Mus musculus, 377 aa) | Swiss-Prot | IPIx1 |
| `ensembl:ENSMUSP00000048218` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0061870 positive regulation of hepatic stellate cell migration** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IMPx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0061874 positive regulation of hepatic stellate cell contraction** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IMPx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0070374 positive regulation of ERK1 and ERK2 cascade** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IMPx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0071560 cellular response to transforming growth factor beta stimulus** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IEPx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0072051 juxtaglomerular apparatus development** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IEPx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:2000491 positive regulation of hepatic stellate cell activation** (biological_process, IEA, involved_in, GO_REF:0000107, assigned by Ensembl) — 2 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62738` | Acta2 (P62738, Rattus norvegicus, 377 aa) | Swiss-Prot | IMPx1 |
| `ensembl:ENSRNOP00000073101` | Ensembl protein id; the UniProt token on the same row is the resolvable one | - | - |

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-445699, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-445700, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-445704, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-445705, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-9604664, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-9914537, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-9934294, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-9934410, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0005829 cytosol** (cellular_component, TAS, located_in, Reactome:R-HSA-9934486, assigned by Reactome) — 0 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|

**GO:0016887 ATP hydrolysis activity** (molecular_function, ISS, enables, GO_REF:0000024, assigned by UniProt) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P68137` | ACTA1 (P68137, Sus scrofa, 377 aa) | Swiss-Prot | EXPx1 |

**GO:0010628 positive regulation of gene expression** (biological_process, ISS, involved_in, GO_REF:0000024, assigned by AgBase) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P08023` | ACTA2 (P08023, Gallus gallus, 377 aa) | Swiss-Prot | IDAx1 |

**GO:0030027 lamellipodium** (cellular_component, ISS, located_in, GO_REF:0000024, assigned by AgBase) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P08023` | ACTA2 (P08023, Gallus gallus, 377 aa) | Swiss-Prot | IDAx1 |

**GO:0030175 filopodium** (cellular_component, ISS, located_in, GO_REF:0000024, assigned by AgBase) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P08023` | ACTA2 (P08023, Gallus gallus, 377 aa) | Swiss-Prot | IDAx1 |

**GO:0044297 cell body** (cellular_component, ISS, located_in, GO_REF:0000024, assigned by AgBase) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P08023` | ACTA2 (P08023, Gallus gallus, 377 aa) | Swiss-Prot | IDAx1 |

**GO:0090131 mesenchyme migration** (biological_process, ISS, involved_in, GO_REF:0000024, assigned by AgBase) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P08023` | ACTA2 (P08023, Gallus gallus, 377 aa) | Swiss-Prot | IMPx1 |

**GO:0019901 protein kinase binding** (molecular_function, ISS, enables, GO_REF:0000024, assigned by ParkinsonsUK-UCL) — 1 token(s)

| token | resolves to | status | own evidence for the donated term |
|---|---|---|---|
| `UniProtKB:P62737` | Acta2 (P62737, Mus musculus, 377 aa) | Swiss-Prot | IPIx1 |

## 5. Reference projection check

For each literature reference on an ACTA2 row: how many annotations does it carry across GOA, and how many DISTINCT entities? A reference that annotates a whole set with identical evidence is one finding projected, not N findings — but only if the phenotype spreads with it, so the per-term entity counts are given too.

| reference | annotations | distinct entities | evidence codes |
|---|---|---|---|
| PMID:11927518 | 7 | 4 | IDAx5, IMPx1, TASx1 |
| PMID:12355421 | 16 | 8 | IDAx12, ISOx4 |
| PMID:16548883 | 20 | 20 | IEPx20 |
| PMID:17464107 | 9 | 4 | IDAx4, IEPx5 |
| PMID:18468998 | 53 | 39 | IDAx20, IGIx1, IPIx13, ISOx19 |
| PMID:23533145 | 1046 | unavailable | - |
| PMID:23580065 | 95 | 95 | HDAx95 |
| PMID:28514442 | 3731 | unavailable | - |
| PMID:33961781 | 9514 | unavailable | - |

- `PMID:23533145`: unavailable: 1046 annotations exceed the 200-row page this script reads, and a page total is not a whole total; the projection test is unreliable for this reference and is not attempted
- `PMID:28514442`: unavailable: 3731 annotations exceed the 200-row page this script reads, and a page total is not a whole total; the projection test is unreliable for this reference and is not attempted
- `PMID:33961781`: unavailable: 9514 annotations exceed the 200-row page this script reads, and a page total is not a whole total; the projection test is unreliable for this reference and is not attempted

**PMID:11927518** — per-term entity counts:

| term | annotations | distinct entities |
|---|---|---|
| GO:0003720 None | 1 | 1 |
| GO:0004565 None | 1 | 1 |
| GO:0005737 None | 2 | 2 |
| GO:0005975 None | 1 | 1 |
| GO:2000773 None | 2 | 2 |

**PMID:12355421** — per-term entity counts:

| term | annotations | distinct entities |
|---|---|---|
| GO:0001750 None | 1 | 1 |
| GO:0005737 None | 12 | 6 |
| GO:0043005 None | 3 | 2 |

**PMID:16548883** — per-term entity counts:

| term | annotations | distinct entities |
|---|---|---|
| GO:0009615 None | 20 | 20 |

**PMID:17464107** — per-term entity counts:

| term | annotations | distinct entities |
|---|---|---|
| GO:0005737 None | 1 | 1 |
| GO:0005886 None | 3 | 3 |
| GO:0032836 None | 1 | 1 |
| GO:0072011 None | 2 | 2 |
| GO:0072015 None | 1 | 1 |
| GO:0072144 None | 1 | 1 |

**PMID:18468998** — per-term entity counts:

| term | annotations | distinct entities |
|---|---|---|
| GO:0003073 None | 3 | 3 |
| GO:0005515 None | 13 | 8 |
| GO:0005886 None | 1 | 1 |
| GO:0032991 None | 36 | 36 |

**PMID:23580065** — per-term entity counts:

| term | annotations | distinct entities |
|---|---|---|
| GO:0005576 None | 95 | 95 |

## Audit

| check | value |
|---|---|
| raw_reference_id_lines | 32 |
| raw_original_reference_id_lines | 53 |
| parsed_reference_id_count | 32 |
| balanced | True |
| goa_data_rows | 50 |
| goa_distinct_data_rows | 50 |
| existing_annotations | 53 |
| existing_annotations_marked_NEW | 3 |
| goa_rows_covered | 50 |
| coverage_balanced | True |

