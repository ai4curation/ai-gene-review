# A0A6I8W805 (LOC117183218 isoform X1, Drosophila pseudoobscura) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. GOA has no annotations for this accession
(`A0A6I8W805-goa.tsv` is header-only), so the review covers identity,
description, core functions, questions and experiments. No NEW annotations are
proposed: there is no experimental or evolutionarily grounded evidence for any
function.

### Deep research
- `just deep-research-falcon DROPS A0A6I8W805 --fallback perplexity-lite` failed:
  falcon raised "Failed to authenticate" (Edison client), and the perplexity-lite
  fallback returned HTTP 401 "insufficient_quota". No deep-research file was
  produced. The review relies on UniProt, the sequence analyses below and the
  primary Herc4 literature.
- The sibling folder's falcon report (`genes/DROPS/A0A6I8W8A2/...-deep-research-falcon.md`)
  treats the gene as a HECT-containing HERC3 ortholog; that framing is wrong
  and it is not used here.

### Identity
- A0A6I8W805 is RefSeq isoform X1 (XP_033239510.1, 282 aa), the longest product
  of LOC117183218 (X chromosome). Other products: X2 A0A6I8W807, X3 A0A6I8W8A2
  (benchmark entry; residues 6-169 = X1 119-282), X4 A0A6I8W815
  [file:DROPS/A0A6I8W8A2/A0A6I8W8A2-bioinformatics/RESULTS.md].
- UniProt: RCC1 repeats 50-144, 145-200, 201-255; disordered 1-20; PE 4;
  PANTHER PTHR22872 family level only [file:DROPS/A0A6I8W805/A0A6I8W805-uniprot.txt].

### Evolutionary placement (new analysis: A0A6I8W805-bioinformatics/)
- `map_to_herc4.py`: X1 50-270 aligns to D. pseudoobscura Herc4 1-227 (76%) and
  D. melanogaster Herc4 7-231 (63%), i.e. roughly blades 1-4 of the 7-repeat
  Herc4 RCC1-like domain. X1 1-49 has no match in Herc4. Closest relative is the
  RCC1-only paralog LOC6903915 (91%). AlphaFold mean pLDDT 58.8.
- Herc4 is PTHR45622:SF76; this gene is PTHR22872 with no subfamily (and X2 of
  the same gene is PTHR22870:SF408). So the gene is in a different PANTHER family
  from its characterised relative, and its own family placement is unstable.
- PAINT: the PTHR22872 PAINT file has an IBD for ubiquitin protein ligase activity /
  protein ubiquitination at PTN002504778 seeded by FB:FBgn0035207 (Herc4), but no
  IBA reaches A0A6I8W805 (GOA is empty). Not an omission to fill: this protein
  lacks the HECT domain that performs the catalysis.

### Closest characterised relative: D. melanogaster Herc4
- Jiang et al. 2019 [PMID:30925584 "Through co-IP experiments, we found either RCC
  repeat domain or the HECT domain is sufficient to mediate its binding to Smo
  (Figure 2C–D)."] Herc4 is a HECT E3 ligase that ubiquitinates Smoothened and
  negatively regulates Hh signalling. The ligase and Hh-regulation functions
  need the HECT domain and are not transferred. RLD-mediated Smo binding is a
  hypothesis for the fragment only (suggested experiment), not an annotation.
- PMID:31010679 (human HERC4/Smo, abstract only) was cached but not used.

### What is experimentally established in this species
- Nothing. No expression, localization, interaction or activity data exist for
  any LOC117183218 product. All statements in the review are sequence-based.
