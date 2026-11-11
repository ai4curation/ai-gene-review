# GPC3 (horse, Equus caballus; UniProt A0A3Q2L6D3) - review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This is the first review of this folder. It is part of the DONKEY40 / DONKEY40_HORSE_PARTNER cohort. ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon HORSE GPC3 --fallback perplexity-lite` failed. Falcon returned "Failed to authenticate", and perplexity-lite returned HTTP 401 (insufficient quota). No deep-research file exists. The review relies on cached publications and on the human UniProt record.

### Identity

- A0A3Q2L6D3 is an unreviewed TrEMBL entry (Ensembl ENSECAP00000034136.2, VGNC:18485 GPC3, chromosome X), 580 aa.
- It is the canonical full-length product, not a fragment or isoform. It is the same length as human P51654 (580 aa), and the alignment has no gaps and 96.21% identity [file:HORSE/GPC3/GPC3-bioinformatics/RESULTS.md "558 of 580 paired residues are identical (96.21%)"].
- PANTHER: PTHR10822:SF4 GLYPICAN-3 for both the horse entry and human P51654.
- Conserved features: all 18 cysteines, furin site RQYR355-358/S359, N-glycans N124/N241/N418, HS serines S495/S509, GPI omega-site N554.
- No PANTHER FamilyReview exists for PTHR10822. `interpro/panther/PTHR10822/` holds only entries, metadata and PAINT data. The PAINT nodes behind the horse IBAs (PTN002247069 Eumetazoa, PTN002585559 Euteleostomi, PTN000850517 Bilateria) are consistent with SF4 placement, so there is no subfamily-placement disagreement.

### Literature (cached)

- PMID:24496449 (human, abstract): "GPC3 and Frizzled interact directly through the glycosaminoglycan chains of GPC3"; "GPC3 stimulates HCC growth by promoting canonical Wnt signaling."
- PMID:14610063 (full text): "This processing is essential for GPC3 modulating Wnt signaling and cell survival in vitro and for supporting embryonic cell movements in zebrafish."
- PMID:18477453 (mouse, abstract): "GPC3 competes with Patched for Hedgehog binding"; "GPC3 induces Hedgehog endocytosis and degradation."
- PMID:8589713: GPC3 loss causes Simpson-Golabi-Behmel syndrome (context only).

### Decisions

- Plasma membrane (IBA and IEA) and cell surface: ACCEPT.
- Positive regulation of canonical Wnt signaling (IBA, human GPC3 among donors): ACCEPT, core.
- Extracellular region, cell migration, regulation of protein localization to membrane: KEEP_AS_NON_CORE (family-level PAINT; indirect or peripheral).
- Regulation of signal transduction (InterPro2GO): TOO_GENERAL.
- Extracellular matrix (InterPro2GO): MARK_AS_OVER_ANNOTATED.
- Hedgehog: negative regulation of smoothened signaling is well supported for mouse GPC3 (same SF4 subfamily). The PAINT node that carries GPC3 plasma membrane (PTN002585559, with mouse Gpc3 as a donor) does not propagate it, so I treat the omission as deliberate and did not add a NEW row. The Hedgehog function is kept as an ortholog-inferred core function, and the propagation question is raised in suggested_questions.
- Core-function MF terms (frizzled binding, hedgehog family protein binding) are not proposed as NEW GOA rows. Validation warns about this, which is expected.

### Relative

Human GPC3 (P51654) is the closest experimentally characterized ortholog in the same PANTHER subfamily SF4. The repo has no review for it (only human GPC2, GPC4 and GPC6). The donkey GPC3 (genes/EQUAS/GPC3, A0A9L0J2B1) is the paired cohort target.

### Modules

`modules/hedgehog_signaling.yaml` has a glypican ligand-distribution variant (PTHR10822 family selector; GPC3 is named in its description). No Wnt module names GPC3.
