# PA5208 (Q9HTY2) notes

## Identity

- UniProt Q9HTY2, unreviewed, 225 aa; locus PA5208, no gene name. Name
  "TIGR00153 family protein" is ProtNLM-generated. Domains: Pfam PF01865
  PhoU_div (DUF47), InterPro IPR018445 Put_Phosphate_transp_reg, IPR038078
  PhoU-like superfamily, NCBIfam TIGR00153, PANTHER PTHR36536 (UPF0111
  protein HI_1603). No TM segment, no signal peptide in the entry.
- Neighbour PA5207 is annotated "Phosphate transporter" (Pit family) in the
  PAO1 UniProt list (.cache/paint/pao1.tsv); TIGR00153/DUF47 proteins are
  commonly encoded next to Pit transporters and described as putative
  Pit-accessory, PhoU-like regulators. No experimental characterisation of
  PA5208 or of any member of the family was found (PubMed search for PA5208,
  TIGR00153, UPF0111, "Pit accessory protein").

## Literature

- The only paper is the Overhage et al. 2007 mini-Tn5-lux swarming screen of
  PAO1 (PMID:17158671; full text cached). PA5208 is one of 36
  swarming-deficient insertion mutants
  [PMID:17158671 "36 mutants were identified with Tn5 insertions in genes for
  the synthesis or function of flagellin and type IV pilus, in genes for the
  Xcp-related type II secretion system, and in regulatory, metabolic,
  chemosensory, and hypothetical genes with unknown functions."], and has a
  growth defect [PMID:17158671 "and a PA5208 mutant that had a slight growth
  defect"]. Biofilm: most non-flagellar, non-pilus mutants made somewhat less
  biofilm [PMID:17158671 "all but five of the non-flagellum- or
  non-pilus-related mutants showed a statistically significant"]. The screen
  used a 62 mM phosphate medium; Table 1 records possible polar effects of each
  insertion on downstream genes (the cached text does not include the table
  values), and PA5208 lies next to the Pit transporter gene PA5207.

## Participation test

What entity performs swarming? The flagellum, its stators, pili and
rhamnolipid surfactant. PA5208 is a cytoplasmic PhoU-like protein of unknown
activity; a single insertion with a growth defect reduces swarming and biofilm,
which is necessity evidence at most, and possibly a polar or
phosphate-homeostasis effect. Neither row passes the participation test.

Clade check: the PTN002194937 leaves are Coxiella burnetii CBU_0015 (Pit
accessory protein; non-motile), Haemophilus influenzae HI_1603 (non-motile,
no flagellar genes), Shewanella SO_3770, Vibrio cholerae VC_2441 ("phosphate
transport regulator") and PA5208. A flagellum-dependent swarming term cannot
hold for organisms without flagella, so the IBD is wrong for the clade as well
as for the seed.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002194937 | GO:0071978 bacterial-type flagellum-dependent swarming motility | 1 (sole) | 5 (5 taxa) | GO:0071978, IMP, PMID:17158671 (PseudoCAP) | INDIRECT-PHENOTYPE | A transposon-screen hit with a growth defect; PA5208 is a PhoU-like putative Pit-transporter accessory protein, not a motility component. The node also propagates a flagellar term to non-flagellated Haemophilus and Coxiella. Withdraw the IBD. |

## Decisions summary

- REMOVE: swarming IBA (over-propagation to non-motile taxa, unsupported seed).
- MARK_AS_OVER_ANNOTATED: swarming IMP and single-species biofilm formation
  IMP (screen phenotypes), with PSEUDOCAP defects.
- No core function: the molecular activity is unknown (PhoU-like domain,
  putative Pit regulator).

## Leaf evidence check (2026-11-06)

Audit of the `GO_CENTRAL` defect on PTN002194937, which made two claims that
needed separating: that the family is "a putative Pit phosphate transporter
accessory/regulator" (a prediction) and that two leaves are in organisms that
lack flagella (a taxon fact, and the load-bearing one). Leaf membership
confirmed with `panther_tree.py node PTN002194937 --leaves`: 5 leaves, all
PTHR36536:SF3.

| Leaf | Name and its evidence | Experimental annotations found | Verdict |
|---|---|---|---|
| P44271 (Haemophilus influenzae HI_1603) | Curated `RecName` "UPF0111 protein HI_1603" — a family placeholder, asserting no function; PE 1 | None. `GO:0071978` IBA is its **only** GO row | Taxon claim SURVIVES (verified below) |
| Q83FC5 (Coxiella burnetii CBU_0015) | `SubName` "Pit accessory protein" ECO:0000313|EMBL:AAO89585.2 — submitter name, unvetted; PE 3 | None. `GO:0071978` IBA is its only GO row | Taxon claim SURVIVES; the "Pit accessory" phosphate role is **not** used as evidence |
| Q9KPD1 (Vibrio cholerae VC_2441) | `RecName` "Phosphate transport regulator" ECO:0008006|Google:ProtNLM — machine-generated name | None. `GO:0071978` IBA only | Phosphate claim dropped as an unvetted prediction |
| Q8EAX1 (Shewanella oneidensis SO_3770) | `RecName` ECO:0008006|Google:ProtNLM; PE 1 | None. `GO:0071978` IBA only | Flagellated organism; no objection from this leaf |
| Q9HTY2 (PA5208, the seed) | `RecName` "TIGR00153 family protein" ECO:0008006|Google:ProtNLM | PseudoCAP IMP rows only (screen phenotypes) | Seed assessment unchanged |

**Family description, marked as predicted.** All five leaves match Pfam
PF01865 `PhoU_div`, NCBIfam TIGR00153 and InterPro IPR018445, whose own name
is "putative phosphate transport regulator". No leaf has any experimental
annotation, and two of the five "phosphate" names are a submitter SubName and
a ProtNLM name. The entry no longer asserts that the family regulates
phosphate transport; it asserts only that no leaf carries a flagellar
component or motor domain.

**Taxon fact, verified.** UniProt proteome query (`rest.uniprot.org`,
2026-11-06) for the six core flagellar structural and motor genes `fliF`,
`flgB`, `flgE`, `flhA`, `fliC`, `motA`:

| Organism (taxon) | Entries | Core flagellar genes found |
|---|---|---|
| Haemophilus influenzae Rd KW20 (71421) | 1704 | 0 |
| Coxiella burnetii RSA 493 (227377) | 1812 | 0 |
| Pseudomonas aeruginosa PAO1 (208964) | 5583 | 6 (all) |
| Shewanella oneidensis MR-1 (211586) | 4070 | 6 (all) |

A free-text `flagell*` search over the H. influenzae and C. burnetii
proteomes likewise returns no flagellar structural protein. Both organisms are
non-motile. So two of the five leaves cannot perform a flagellum-dependent
process at all.

Confidence raised PROBABLE -> CONFIRMED: the decisive fact is a live resource
query run here, not an inference from a protein name.
