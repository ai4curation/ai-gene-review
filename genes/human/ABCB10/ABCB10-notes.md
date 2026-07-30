# ABCB10 (mitochondrial inner-membrane ABC transporter) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`ABCB10-deep-research-affinage.md`; gates passed, `pairwise: win`) plus UniProt Q9NRK6, the
GOA TSV and the primary literature.

## The central curation issue: the substrate changed

ABCB10 has 35 GOA annotations, unusually rich for this campaign. The interesting problem is not
sparsity but **a superseded mechanistic model still embedded in the record**.

For years ABCB10 was assumed to export **5-aminolevulinic acid (ALA)**, the first committed heme
precursor, out of the mitochondrion — which would make it a direct participant in heme
biosynthesis. That model is **explicitly disproven**:

> [PMID:28808058, "our findings rule out that Abcb10
> transports ALA and indicate that Abcb10's ATP-hydrolysis activity is critical
> for hemoglobinization and that the substrate transported by Abcb10 provides a
> signal that optimizes hemoglobinization."]

and the same paper shows directly why:

> [PMID:28808058, "demonstrating that reductions in Abcb10 do not affect ALA
> export from mitochondria and indicating that Abcb10 does not transport ALA."]

The actual substrate is **biliverdin** — [PMID:34011630, "ABCB10 exports mitochondrial biliverdin, driving metabolic maladaptation in obesity."]

So ABCB10's effect on heme biosynthesis is real but **indirect**: its ATPase activity is required
for hemoglobinization, and loss of it represses the heme-biosynthesis transcriptional programme
through Bach1, partially rescuable by ALAS2 or GATA1 overexpression. It also stabilises
mitoferrin-1 to support mitochondrial iron import.

That distinction drives the main actions:

| Term | Evidence | Action | Why |
|---|---|---|---|
| `GO:0006783` heme biosynthetic process | IEA, NAS, ISS | **MODIFY → `GO:0070455`** | ABCB10 does not carry a heme-pathway intermediate; it *regulates* the pathway |
| `GO:0070455` positive regulation of heme biosynthetic process | ISS | ACCEPT | already the right term, and now the destination of the three above |

`involved_in heme biosynthetic process` invites exactly the reading the field spent a decade
holding and then discarded. The regulation term says what is actually shown.

## A genuine GO gap: no biliverdin transporter term

`GO:0140359 ABC-type transporter activity` (IDA ×2) is correct but generic. GO has
`GO:0015232 heme transmembrane transporter activity` for the related tetrapyrrole, but **no term
for biliverdin transport** — confirmed by OLS/oaklib search. ABCB10 is *the* characterised
biliverdin exporter, so this is filed under `proposed_new_terms` rather than forced into an
ill-fitting existing term.

The `GO:0140359` rows are `ACCEPT`ed as correct-but-general, with the gap noted, rather than
modified into something the ontology cannot yet express.

## The `protein binding` set — informative for once

Third gene in this campaign where the IPI partners are real biology rather than screen noise,
and here they are *central*:

| Partner | Papers | Status |
|---|---|---|
| **FECH** (ferrochelatase, P22830) | PMID:30765471 ×2, PMID:36836934 | the ABCB10–FECH–ABCB7 complex; mechanistically central |
| MUL1 (Q969V5) | PMID:40105103 | mitochondrial E3 ligase |
| PAAT (Q9H8K7) | PMID:25063848 | uncharacterised for this pair |

The FECH rows are `MODIFY`ed rather than dismissed. Note this gene *already* carries
`GO:0043190 ATP-binding cassette (ABC) transporter complex` (IPI, same paper), so the complex
membership is captured; what the bare binding rows add is the specific partner identity.

## Provider assessment

The best affinage record of the campaign so far: `self_evaluation_pairwise: win` with clear
trust gates, and the
narrative correctly foregrounds the substrate switch — *"biliverdin/bilirubin export rather than
direct ALA or dALA transport is the established substrate axis"*. It also assembles the
cardiolipin dependence, the glutathionylation at Cys547, the R232/R295 ATPase-stimulation
residues and the mitoferrin-1/FECH/ABCB7 organisation into one picture.

Unlike A1BG and AASDH, where the provider's silence merely failed to contradict a bad
annotation, here it **positively supplies the fact that overturns the existing model**. Its GO
grounding was still not imported.
