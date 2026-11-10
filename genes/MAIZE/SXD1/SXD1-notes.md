# SXD1 (MAIZE, Q94FY8) review notes

## 2026-10-26 session

- fetch-gene resolved Q94FY8 correctly (folder genes/MAIZE/SXD1). Note: UniProt cross-refs
  NCBI GeneID 541877, while the task brief gave 541928; I used the UniProt record.
- No deep-research provider; manual synthesis in SXD1-deep-research-manual.md.
- Key papers read: PMID:12913173 (abstract only; activity of recombinant SXD1, Synechocystis
  complementation), PMID:11340186 (abstract only; chloroplast localization), PMID:17924136 (full
  text; sxd1 lacks tocopherols, callose occlusion of plasmodesmata), PMID:12213958 (Arabidopsis
  VTE1, full text), PMID:16414959 (VTE1 plastoglobule localization, abstract).

Key evidence:
- [PMID:12913173 "Recombinant SXD1 and VTE1 proteins are able to convert DMPBQ to gamma-tocopherol in vitro."]
- [PMID:11340186 "The SXD1 protein was localized to chloroplasts, in both bundle sheath and mesophyll cells."]
- [PMID:17924136 "sxd1 mutants had undetectable levels of tocopherols as previously reported"]
- [PMID:17924136 "It is not known how lack of tocopherols causes callose deposition."]

Decisions:
- tocopherol cyclase activity (EXP, IBA, IEA): ACCEPT, core.
- vitamin E biosynthetic process (IBA, IEA): ACCEPT, core (GO has no more specific tocopherol
  biosynthesis term).
- chloroplast (IEA): ACCEPT; experimentally supported by Provencher 2001 (no IDA in GOA).
- plastoglobule (IBA, IEA): ACCEPT; based on VTE1 proteomics; no maize-specific data.
- No NEW process terms for sucrose export / plasmodesma / callose: these are indirect
  consequences of tocopherol deficiency (necessity, not participation). Tocotrienol cyclase
  activity was shown for VTE1 only, not SXD1, so not proposed.
