# ddb-1 (Q21554) review notes

- Deep research failed (falcon timeout; perplexity unavailable). Review based on cached publications and UniProt.
- DDB-1 binds CUL-4 and CDT-1 [PMID:17145765 "DDB-1 physically associates with CDT-1, indicating that CDT-1 is a direct substrate of the CUL-4/DDB-1 complex."].
- WDR-23 interaction (GOA IPI rows; WITH P90794 and WB:WBGene00008419, both wdr-23) [PMID:19273594, abstract only].
- Protein binding IPIs -> MODIFY to GO:0160072 ubiquitin ligase complex scaffold activity, matching the human DDB1 review's core MF (note: the SKN-1 module uses GO:0030674 for DDB-1; GO:0160072 is under structural molecule activity in GO, not under GO:0030674).
- Nucleic acid binding (InterPro CPSF_A) removed, as in human DDB1 review. Site of DSB IBA (S. pombe-seeded) marked over-annotated.
- NEW: GO:0080008 Cul4-RING E3 ubiquitin ligase complex (IPI, PMID:17145765).

## WormBase description follow-up (2026-10-30): LET-23/EGFR signalling

WormBase says the CUL-4/DDB-1 complex "regulates ... LET-23/EGFR signalling in vulval
precursor cells". The source is Poulin and Ahringer (PMID:20977703), which shows that
cdt-2 and cul-4 RNAi enhance LET-23 signalling, but DDB-1 itself gave no phenotype:
[PMID:20977703 "However, RNAi of ddb-1 did not cause obvious LET-23 signalling
defects."]. The authors infer DDB-1 participation from complex membership
[PMID:20977703 "Because CDT-2 and CUL-4 normally work as part of the CDT-2/CUL-4/DDB-1
ubiquitin ligase complex, it seems likely that DDB-1 also participates in attenuation
of LET-23 signalling."] and note that CDT-2 and CUL-4 "could act independently of
DDB-1 in this context". The DDB-1 role is therefore an inference, not a finding, and
no annotation is proposed.
