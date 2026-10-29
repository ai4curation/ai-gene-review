# Sec71 (DROME) review notes

## Session 2026-10-28

- `just fetch-gene DROME Sec71` timed out repeatedly on the UniProt stream endpoint
  (gene-symbol lookup). Fetched by accession instead: `just fetch-gene DROME Q9VJW1 --alias Sec71`;
  the folder is genes/DROME/Sec71 and the entry is Q9VJW1 as expected. 22 GOA rows.
- Cached PMID:22291037 (full text), and additionally PMID:31649044 and PMID:40208939 (full
  text), PMID:33262309 and PMID:37567172 (abstract only). PMID:28420712 and PMID:15901661 are
  abstract only.
- See Sec71-deep-research-manual.md for the literature summary with quotes.

### Key decisions

- GEF activity (IBA/IDA/IEA/IPI): ACCEPT. GO:0005086 ARF GEF activity is obsolete, so
  GO:0005085 is the most specific term.
- Three NAS rows from ComplexPortal CPX-26617 (Sec62/Sec63 complex, rough ER membrane,
  post-translational protein targeting to membrane, translocation): REMOVE, with
  source_defects (symbol collision with yeast Sec71 = Sec66). Checked live:
  CPX-26617 participants are Q9VJW1 Sec71, Q9VS57 Sec63, Q9VL49 Trp1
  [file:DROME/Sec71/Sec71-bioinformatics/RESULTS.md "SEC71 is a synonym of yeast SEC66, the Sec63-complex subunit."].
  PMID:15901661 is about CrebA-dependent secretory gene expression and is miscited.
- membrane IEA: MODIFY to trans-Golgi network membrane (peripheral, Arl1-recruited).
- vesicle-mediated transport IBA: MODIFY to Golgi to plasma membrane protein transport.
- regulation of ARF protein signal transduction IEA: MODIFY to positive regulation.
- perinuclear region IEA (ARBA): MARK_AS_OVER_ANNOTATED.
- Neuron remodelling (dendrite pruning) and positive regulation of endocytosis:
  KEEP_AS_NON_CORE (indirect, downstream of Golgi trafficking).
- No NEW terms. Golgi organization (stack separation, PMID:33262309) was considered but the
  evidence is perturbation/BFA-phenotype and abstract-only, so it was not added.
