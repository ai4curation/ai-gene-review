# AcrIF8 family identity verification

Official responses retrieved on 2026-10-26 are preserved byte-for-byte; `manifest.json` records their URLs and SHA-256 hashes. Run `python3 fetch_family_evidence.py` to refresh them with the standard library.

- InterPro `entry.json` identifies IPR057730 as **Anti-CRISPR protein AcrF8**, a family integrating Pfam **PF25699**. Its mechanistic description concerns the type I-F Csy complex and crRNA contacts.
- The official protein/entry endpoint in `membership.json` explicitly places **H9C181**, the 92-residue Pectobacterium phage ZF40 protein, in **IPR057730**, with a continuous match at residues **1–92**. This verifies the actual representative, not merely a plausible adjacent accession.
- `cdd.json` identifies **cd22241** as **Anti-CRISPR type I subtype F8 (AcrIF8)**. The independent NCBI CDD page (`ncbi-cdd.html`) identifies the same signature and includes structure **6VQW**. The existing, unchanged `genes/BPZF4/AcrF8/AcrF8-uniprot.txt` has `DR CDD; cd22241; AcrIF8; 1.` and PDB 6VQW chain I, residues 1–92.
- CDD is corroborating evidence, **not** the integrated signature returned for IPR057730: the InterPro response lists Pfam PF25699, while its CDD entry has `integrated: null`. No CDD-to-InterPro equivalence is inferred from neighboring IDs.

The existing module family ID and official label are therefore retained. Family membership does not establish susceptibility of every host Csy ortholog. These database responses establish classification; the existing primary papers remain the evidence for the inhibitory mechanism.
