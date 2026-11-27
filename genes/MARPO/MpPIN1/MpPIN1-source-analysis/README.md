# MpPIN1 identity analysis

Run `uv run python genes/MARPO/MpPIN1/MpPIN1-source-analysis/verify_clone_identity.py` from the repository root. The script compares the normally seeded A0A2R6WHW5 UniProt flat-file sequence against unchanged UniProt REST JSON for A0A075ILB5. The latter cross-references published clone KJ664532/AIF28545.1. Result: identical719aa sequences. The raw JSON is retained with a checksum; the analysis does not infer function from submitted sequence names. Functional evidence is separately reviewed from PMID:37528584 and PMID:36880411.
