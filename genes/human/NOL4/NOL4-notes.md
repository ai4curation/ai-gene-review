# NOL4 (human, O94818) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Provenance / process
- `just fetch-gene human NOL4` created the UniProt, GOA (4 rows) and stub files.
- Deep research FAILED: `just deep-research-falcon human NOL4 --fallback perplexity-lite`
  failed with falcon "Exception: Failed to authenticate" and perplexity-lite
  "HTTP error: 401 ... You exceeded your current quota". The review is based on the
  literature I could read directly (PubMed search `NOL4[tiab]`, 29 hits, key papers cached).
- ProtNLM2 predictions were not consulted.

### Identity and evolutionary grounding
- 638 aa nuclear protein, four splice isoforms; PANTHER PTHR12449:SF17 (NUCLEOLAR PROTEIN 4);
  InterPro IPR039788 NOL4/NOL4L, IPR056549 HTH_NOL4; Pfam PF23079 HTH_NOL4_2nd.
- Mouse Nol4 (P60954) is also SF17 and 93.6% identical (452/483 aligned positions);
  human paralog NOL4L (Q96MY1) is SF19 and 62.1% identical
  [file:human/NOL4/NOL4-bioinformatics/RESULTS.md]. Mouse Nol4 is a 1:1 ortholog; NOL4L is not.
- No PAINT/IBA node: UniProt "PAN-GO; O94818; 0 GO annotations based on evolutionary models."
- Original cDNA (BAA34576) was truncated/frameshifted (UniProt sequence caution), so the
  "524 amino acid" protein and residue numbers in PMID:9813152 refer to that clone.

### Experimental findings in human
- Nucleolar localization with separable nucleolar (aa 342-371) and nuclear (aa 372-401)
  targeting segments, GFP-fusion deletion mapping in COS-7 cells
  [PMID:9813152 "a region of 30 amino acids (position 342-371), which overlaps the first and second NLS, is sufficient for nucleolar localization"].
- Expression: brain and testis [PMID:9813152 "Tissue distribution analysis demonstrated a predominant expression in brain and testis."].
- Nuclear immunostaining in SCLC and neuroendocrine neoplasms; cancer/testis antigen
  [PMID:34065612 "brown nucleus staining of NOL4 is visible in tumor cells"];
  [PMID:36282054 "NOL4 retains its nuclear immunoreactivity in areas of crush artifact or necrosis"].
- Promoter hypermethylation in HNSCC and PTC (biomarker, not function) [PMID:24337411; PMID:33613681].
- Human isoform 2 has Y2H interactions with CTBP1/CTBP2 and others (IntAct, UniProt CC INTERACTION);
  no GO annotation derived.

### Ortholog (mouse) findings — not experimentally established in human
- Mouse NOL4 splice variants bind Mlr1/Mlr2 (Mblk-1 family TFs) and modulate their
  transactivation in luciferase assays in Drosophila S2 cells [PMID:25366156]. Overexpression
  in heterologous cells; MGI annotates mouse Nol4 only ND for MF/BP, i.e. curators did not
  derive a GO MF/BP term from this paper. I did not add a NEW transcription-regulator term.

### Annotation decisions
- RNA binding (TAS, PMID:9813152): abstract mentions no RNA binding, only "a short Escherichia coli
  DNA helicase homologous region"; no RNA-binding domain is recognized; full text unavailable -> UNDECIDED.
- nucleolus (IEA + TAS): ACCEPT, core location.
- nucleoplasm (IDA, HPA): ACCEPT (consistent with nuclear staining in tumors and nuclear NLS region).
