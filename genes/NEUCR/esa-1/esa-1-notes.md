# NEUCR esa-1 manual review notes

## 2026-10-10

`just fetch-gene NEUCR esa-1` seeded 34 GOA rows for UniProtKB `Q7S9B6`, a
reviewed Neurospora ESA1/MYST histone acetyltransferase in PANTHER
`PTHR10615:SF218` (`HISTONE ACETYLTRANSFERASE ESA1`).

The local PAINT cache has two relevant IBA nodes:

- `PANTHER:PTN000834946`: fungal ESA1-node
  `GO:0010485 histone H4 acetyltransferase activity`, seeded by
  `CGD:CAL0000179231`, `SGD:S000005770`, and `UniProtKB:C8VBH4`.
- `PANTHER:PTN004172926`: eukaryotic MYST-root node with broad chromatin,
  nucleus, chromatin-binding, transcription-coregulator, and Pol II regulation
  calls.

Newer literature search found one direct Neurospora ESA-1/NuA4 paper not
represented in GOA: Wang et al. 2023, "A crucial role for dynamic expression of
components encoding the negative arm of the circadian clock." The paper
identified BRD-8-associated NuA4 subunits, verified BRD-8 interactions with
ESA-1 and other NuA4 components by immunoprecipitation, and directly assayed
ESA-1V5 from Neurospora on recombinant histones H4 and H2A. Key direct support:
"To test whether Neurospora ESA-1 can acetylate histones H4 and H2A, ESA-1V5
was affinity-purified and tested in an in vitro acetylation assay using
recombinant histones H4 and H2A" and "ESA-1V5 strongly modified histones H4 at
lysines 5, 8, 12, and 16 and H2A at lysine 9" [PMID:37291101].

Manual web search for `Neurospora crassa esa-1`, `NCU05218`, `hat-4`, and
`NuA4 ESA-1` surfaced the 2023 paper as the only new primary paper directly
assaying Neurospora ESA-1. A 2025 Neurospora histone-deacetylase paper and
2026 Neurospora genome-organization news items appear to be broader chromatin
context rather than direct ESA-1 functional evidence.

Main row-level calls:

- Keep all six IBA rows. `PTN000834946` is core H4 HAT support; the five
  `PTN004172926` rows are broad but biologically sound.
- Accept NuA4 complex membership from the direct AP-MS/IP work.
- Add a new `GO:0043998 histone H2A acetyltransferase activity` row because
  Wang et al. directly showed H2A K9 acetylation by ESA-1V5.
- Remove `GO:0000786 nucleosome`: ESA-1 acts on nucleosomes but is not a
  nucleosome component.
- Modify `GO:0032777 piccolo histone acetyltransferase complex` to
  `GO:0035267 NuA4 histone acetyltransferase complex`; Neurospora full NuA4 is
  directly supported, but a separate ESA1/EPL1/YNG2-like Piccolo core is not.
- Mark yeast-specific EnsemblCompara process rows for rDNA heterochromatin,
  triglyceride biosynthesis, and macroautophagy as over-annotated or remove
  them, leaving the conserved catalytic and chromatin-regulatory function as
  the main Neurospora assertion.

Follow-up cleanup: kept the H2A core-function text biological rather than
GOA-facing, and expanded several UniProt continuation-fragment
`supporting_text` snippets to the complete relevant lines.
