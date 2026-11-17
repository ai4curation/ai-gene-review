# DciA construct identity

PDB 9TZF identifies PMID:42927770 as its primary publication. Its deposited entity 2 is DciA/VC_2395 from Vibrio cholerae O1 El Tor N16961 (taxon243277), and maps to UniProt Q9KPH3. The complete157-aa entity sequence matches both the frozen dciA UniProt sequence and GenBank AAF95538.1 exactly. Entity1 similarly matches Q9KUY7/VC_0371 (468aa). This latter comparison identifies the assayed partner; it is not a new gene review.

Run `uv run python genes/VIBCH/dciA/dciA-source-analysis/verify_identity.py` from the repository root. The helper regenerates identity-proof.yaml using only the unchanged downloaded records and frozen UniProt file. URLs and SHA256 values are recorded in provenance.yaml. The alignment accession in the article was only a discovery lead; the deposited polymer identity and source taxonomy provide the construct mapping.

Methods describe an N-terminal His6-MBP-TEV fusion for DciA, followed by TEV cleavage and removal of the tag, protease and uncleaved protein. Both the full-length DciA and selected domain/mutant constructs were tested; the reviewed native sequence corresponds to the full-length protein. Deposited sequence equality does not imply every residue is resolved in the cryo-EM model or establish an unreported cleavage scar. No full article PDF or XML is redistributed here.
