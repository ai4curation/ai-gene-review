# Reproduce ELN database evidence

Run `python3 reproduce.py` from any working directory. The program requires only Python's standard library, checks the archive hash and every internal input hash, safely extracts to a temporary directory, reconstructs the evidence and removes the temporary files afterward. It performs no network calls and does not modify the saved evidence.

The archive contains frozen official Reactome, QuickGO, UniProt, InterPro and Ensembl records, sequence FASTA files, retrieval receipts, the literal 48 source assertions and all 50 raw contexts. The inner program reconstructs typed target paths and current donor joins, checks product sequences and ontology relations, and exposes raw-context multiplicity. Its expected projection is compared against freshly derived results rather than used to generate them.

Only private absolute file locators in the expected projection were converted to relative archive paths; all scientific objects and ordered graph edges remain unchanged. Original publication bodies, figure images, supplementary article workbooks and provider logs are not redistributed. See the source guide for independently assessed primary evidence and access limits. A successful replay verifies the saved database reconstruction, not biological equivalence of all natural products or completeness of unexpanded graph branches.
