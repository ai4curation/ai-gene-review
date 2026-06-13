# Concepts

This directory holds **pathway- and concept-level curations**: biological pathways,
multi-gene processes, or biosynthetic gene clusters captured as a single unit for a
**representative species**, rather than one gene at a time.

A concept entry complements:
- `genes/<SPECIES>/<GENE>/` — individual gene reviews (the authoritative per-gene curation), and
- `projects/` — thematic/methodology projects spanning many genes/organisms.

Each concept aligns to an external authority where one exists (e.g. **MIBiG** for
biosynthetic gene clusters, Reactome/KEGG for metabolic pathways), maps the member genes
to UniProt, lays out the reaction sequence (mermaid), and tracks which members have been
fully reviewed under `genes/`. Concepts also surface **discrepancies** between the external
authority and the synthesized curation (candidate corrections to push upstream).

## Entries

| Concept | Representative species | External ref | File |
|---|---|---|---|
| Erythromycin biosynthesis | *Saccharopolyspora erythraea* NRRL 2338 | MIBiG BGC0000055 | `erythromycin_biosynthesis.md` |
