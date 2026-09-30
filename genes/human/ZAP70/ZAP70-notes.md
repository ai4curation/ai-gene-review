# ZAP70 (human, P43403) curation notes

Project: ADAPTIVE_IMMUNITY (T cell receptor trunk).

## Biology summary

- Syk-family cytoplasmic PTK; tandem N-SH2/C-SH2, interdomain B (Y292, Y315, Y319), C-terminal kinase domain (active fragment 327-606) [PMID:15292186 "utilizing an active kinase domain containing residues 327-606"].
- Recruitment: Lck phosphorylates both ITAM tyrosines; ZAP70 binds via both SH2 domains [PMID:7509083 "This phosphorylation leads to the recruitment of a second cytoplasmic PTK, ZAP-70, through both of the ZAP-70 Src homology 2 domains and its phosphorylation."]. Binding needs both ITAM tyrosines phosphorylated [PMID:7528772 "the ZAP-70 interaction with the TCR requires prior phosphorylation of both tyrosine residues within a TAM motif"]. Kd ~25 nM for CD3 epsilon ITAM [PMID:7761456].
- Activation: SH2 engagement relieves autoinhibition [PMID:10704231; PMID:8901551]; Lck phosphorylates Y493 and pY319 binds the Lck SH2 domain [PMID:10318843 "Tyr319-mediated binding of the SH2 domain of Lck is crucial for ZAP-70 activation"].
- Substrates: LAT [PMID:9489702; PMID:11368773 "Zap-70 efficiently phosphorylates LAT on tyrosine residues at positions 226, 191, 171, 132 and 127."], SLP-76/LCP2 [Reactome:R-HSA-202216], VAV1 [PMID:23620790], DUSP3/VHR Y138 [PMID:12447358].
- Negative regulation: PTPN22 dephosphorylates Y493 [PMID:16461343]; UBASH3B/Sts-1 [PMID:24256567]; CBL TKBD binds pY292 [PMID:22266821].
- Disease: selective T cell deficiency/SCID with absent CD8 SP T cells [PMID:8613493 "zap-70 kinase appears to be indispensable for the development of CD8 single-positive T cells"]; combined hypomorphic + activating alleles cause autoimmunity [PMID:26783323].

## Annotation review decisions (98 rows)

- MF kinase terms (GO:0004672, GO:0004713, GO:0004715; all evidence types incl. Reactome TAS): ACCEPT. Four Reactome TAS rows are SYK-centred reactions (DAP12 signaling) where ZAP70 is presumably in a candidate set; the MF itself is correct.
- GO:0001784 phosphotyrosine residue binding (IEA): ACCEPT; core.
- protein binding (28 IPI rows): 12 MODIFY -> GO:0001784 (11 rows) (SH2-pITAM binding to CD247/CD3E; FCRL3 phospho-ITAM-like motif) or GO:0019901 protein kinase binding (1 row, LCK via pY319); 16 REMOVE (substrate-trap/phosphatase, E3 ligase, kinase-substrate, high-throughput SH2 screens with EGFR/MET/KIT, and abstracts that do not describe a ZAP70 function).
- Locations: cytoplasm/cytosol/plasma membrane/membrane/immunological synapse ACCEPT; cell-cell junction, membrane raft (colocalizes_with) and TCR complex (recruited, not a constitutive subunit) KEEP_AS_NON_CORE.
- Processes: TCR signaling pathway ACCEPT (core; ZAP70 performs the phosphorylation steps). Protein phosphorylation / peptidyl-tyrosine phosphorylation / intracellular signal transduction ACCEPT (general but correct). Adaptive immune response, immune response, T cell activation, T cell differentiation, positive thymic selection, positive regulation of T cell differentiation, leukocyte adhesion/migration, T cell aggregation/migration: KEEP_AS_NON_CORE (necessity or downstream outcomes per project rule 3). B cell activation: MARK_AS_OVER_ANNOTATED.

## Issues noted

- PMID:22732588 (peptidyl-tyrosine phosphorylation IDA): full text says "Src kinases (Lck or Fyn) but not the ZAP-70 kinase can phosphorylate both Themis1 and Themis2", and Themis1 was phosphorylated in ZAP70-deficient P116 cells; the reference weakly supports this row. Kept (ACCEPT) because the term is correct for ZAP70, flagged reference as MISCITED.
- PMID:12150984 and PMID:8648092 are abstract-only and the abstracts do not mention ZAP70; deferred to curators on location, removed the generic protein binding row.
- THEMIS: PMID:23460737 reports ZAP70 phosphorylates THEMIS in vitro and with Lck in HEK293, while PMID:22732588 reports it does not; conflicting.

## Deep research

- `just deep-research-falcon human ZAP70 --fallback perplexity-lite` launched in background at the start of the review. The wrapper reported a falcon timeout after 600s and the perplexity-lite fallback failed (provider not available), but the falcon job itself completed (~1218 s, 29 citations) and wrote `ZAP70-deep-research-falcon.md`. Its content (tandem SH2 binding of doubly phosphorylated ITAMs, LCK-dependent activation via Y315/Y319/Y493, LAT and SLP-76 as principal substrates, ZAP70 not phosphorylating ITAMs) is consistent with this review and it is cited in core_functions.
