# epg-9 (Q95XH2) notes

Deep research failed on 2026-10-08 (falcon exit 137; perplexity provider unavailable). No
deep-research file; review based on PMID:22885670 (abstract only) and UniProt.

## Accession choice
Y69A2AR.7 (WBGene00022078) has three unreviewed TrEMBL entries, one per WormBase isoform:
Q95XH2 (Y69A2AR.7a, 260 aa), H2L0S0 (Y69A2AR.7b, 214 aa), Q86DD3 (Y69A2AR.7c, 187 aa). All three
carry the same IMP/IPI annotations; only Q95XH2 also carries the IBA annotations (8 GOA rows
versus 4). Q95XH2 is the "a" isoform, the longest entry, and is used here.

## Key findings
- ATG101 homolog [PMID:22885670 "epg-9 encodes a protein with significant homology to mammalian ATG101"].
- Binds EPG-1/ATG-13 and forms a complex [PMID:22885670 "EPG-9 directly interacts with EPG-1/Atg13"].
- Aggrephagy defect [PMID:22885670 "loss of function causes defective autophagic degradation of a variety of protein aggregates during C. elegans embryogenesis"].
- Transcriptional regulation by MML-1/MXL-2 [PMID:27001890] and HSF-1 [PMID:27688402].

## Curation decisions
- Protein binding IPI (EPG-1) -> REMOVE; protein kinase binding (IPI with UNC-51, IBA) -> ACCEPT.
- All other rows ACCEPT. Core MF uses GO:0019901 protein kinase binding (no better ATG101 MF term exists).
