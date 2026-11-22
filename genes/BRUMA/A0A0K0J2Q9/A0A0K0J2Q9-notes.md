# BRUMA A0A0K0J2Q9 notes

## 2026-11-22

### Setup

`A0A0K0J2Q9` is the Brugia malayi TrEMBL record named `avr-14` with
`AVR-14B` as a synonym. I fetched it directly with
`just fetch-gene BRUMA avr-14 --uniprot-id A0A0K0J2Q9 --alias A0A0K0J2Q9`
to avoid conflating it with the paired `E5KGC8` avr-14 transcript; UniProt maps
`A0A0K0J2Q9` to `HQ123447` from PMID:21041637 and to `MW196269` from the
Lamassiaude et al. Bma-AVR-14B cloning.

The seeded GOA had seven automated InterPro, SubCell and combined IEA rows and
no PMID rows. `just fetch-gene-pmids BRUMA A0A0K0J2Q9` therefore had no PMIDs
to cache from GOA. I cached the two Bma-AVR-14B papers directly:

- PMID:21041637, Moreno et al., is abstract-only in the local cache. Its
  accessible abstract reports native B. malayi GluCl immunolocalization around
  the microfilarial excretory-secretory vesicle, and the UniProt record maps
  `A0A0K0J2Q9` to the paper's `HQ123447` avr-14 cDNA.
- PMID:34623639, Lamassiaude et al., is full text and gives the direct
  Xenopus-oocyte functional data for Bma-AVR-14B/Bma-GLC-2.

`just deep-research-falcon BRUMA A0A0K0J2Q9 --fallback perplexity-lite` failed
because `agentapi` was not on `PATH`: the deep-research client reported only
`claude_code` as an available provider for both `falcon` and the
`perplexity-lite` fallback. I did not hand-write a provider-named deep-research
file.

`just paint-losses BRUMA A0A0K0J2Q9` reported that `A0A0K0J2Q9` is in
PTHR18945 but is not a leaf of the cached PAINT tree, so no IRD or IKR loss
applies to this accession.

### Accession Resolution

UniProt currently has two B. malayi `avr-14` TrEMBL records tied to the Moreno
et al. 2010 cloning study:

- `E5KGC8`, 419 aa, mapped to `HQ123446`/`ADR74384.1`.
- `A0A0K0J2Q9`, 427 aa, mapped to `HQ123447`/`ADR74385.1` and to the later
  `MW196269`/`QRW38687.1` Bma-AVR-14B record from Lamassiaude et al.

I selected `A0A0K0J2Q9` first because it is the AVR-14B sequence used in the
later heteromeric GluCl pharmacology study. The review stays in an
accession-named directory to keep the two avr-14 transcript records distinct.

### Annotation Decisions

Lamassiaude et al. found that none of the four cloned B. malayi GluCl subunits
formed robust homomeric channels in Xenopus oocytes, but Bma-AVR-14B plus
Bma-GLC-2 produced robust glutamate-sensitive receptors and the
Bma-AVR-14B/GLC-2 receptor was sensitive to ivermectin and moxidectin.

The review therefore adds `GO:0008068 extracellularly glutamate-gated chloride
channel activity` with `qualifier: contributes_to` and represents the core
function as `contributes_to_molecular_function`: Bma-AVR-14B contributes to
the heteromeric Bma-AVR-14B/Bma-GLC-2 GluCl, but has not been shown to enable
full receptor activity by itself.

The InterPro Cys-loop receptor activity rows are broad but correct and were
accepted. The generic InterPro transport rows were marked `TOO_GENERAL` because
the review asserts chloride transmembrane transport from the Brugia-specific
functional GluCl assay. `GO:0016020 membrane` was also marked `TOO_GENERAL`
because the A0A0K0J2Q9 record has a signal peptide and four predicted
transmembrane helices and the functional heteromer reaches the oocyte surface,
supporting the more informative plasma-membrane row.
