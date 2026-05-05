# Dnaja3 curation notes

Deep research status: `just deep-research-falcon mouse Dnaja3 --fallback perplexity-lite --timeout 60` was first run on 2026-05-03 after the Dnajb11 default run had already shown provider failure. Falcon timed out, and the requested `perplexity-lite` fallback failed with a 401 insufficient-quota error. Per course correction, `just deep-research-falcon mouse Dnaja3 --timeout 1800 --fallback perplexity-lite` was then run one gene at a time and succeeded, producing `Dnaja3-deep-research-falcon.md`.

Core evidence: Dnaja3/Tid1 is a mitochondrial DnaJ/Hsp40 co-chaperone for HSPA9/mortalin. Its core role is protein folding chaperone activity coupled to mitochondrial proteostasis, mitochondrial DNA maintenance, and mitochondrial organization.

Falcon synthesis: The Falcon report verifies Dnaja3/Tid1 as a predominantly mitochondrial DnaJ/Hsp40 co-chaperone for mtHsp70/HSPA9, emphasizing stimulation of Hsp70 ATP hydrolysis and mitochondrial protein-folding/anti-aggregation functions. It adds strong support for coupling to LONP1-dependent mitochondrial protein folding, with DNAJA3 knockdown causing aggregation of mitochondrial proteins such as OXA1L and NDUFA9, and highlights recent B-cell immunometabolic and frataxin/FXN client-regulatory evidence [file:mouse/Dnaja3/Dnaja3-deep-research-falcon.md].

Embryonic and mitochondrial evidence: The Dnaja3 knockout paper reports that "mTid-1 deficiency results in increased apoptosis and embryonic lethality" and supports mitochondrial localization and survival roles [PMID:14993262].

Cardiac mitochondrial evidence: The cardiac conditional knockout paper states that "Progressive respiratory chain deficiency and decreased copy number of mitochondrial DNA were evident in cardiomyocytes lacking Dnaja3" [PMID:16327803]. This directly supports mitochondrial DNA replication/maintenance and mitochondrion organization annotations.

T cell evidence: The T-cell conditional knockout study states that "tid1 is critical in early thymocyte development, especially during transition from the DN3 to double-positive stages" [PMID:15879105]. This is valid developmental/immune biology but non-core for the gene's conserved molecular function.

MuSK evidence: The neuromuscular-junction paper states that the authors used two-hybrid screens to identify Tid1 as a protein "that binds to the cytoplasmic domain of muscle-specific kinase (MuSK)" [PMID:19038220]. This supports kinase binding and postsynaptic/NMJ annotations as context-specific.

Curation rule: Dnaja3 should not be annotated as ATP binding solely because it has a DnaJ domain; DnaJ proteins stimulate the ATPase cycle of Hsp70 partners. GO:0005515 protein binding and GO:0044877 protein-containing complex binding are too generic when Hsp70 binding or protein folding chaperone function is available.
