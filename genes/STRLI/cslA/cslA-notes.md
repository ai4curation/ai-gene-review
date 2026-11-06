# CslA evidence and identity audit

## Identity and source strain

The active record is A0ABM5R5V5, SLIV_23475, Streptomyces lividans TK24 (taxon457428; UniProt species codeSTRLI), 653 residues. The biochemical source is S. lividans1326, not TK24. Official TableS3 of [PMID:38557137](https://pmc.ncbi.nlm.nih.gov/articles/PMC11022532/) identifies source1326 CslA as A0A7U9DT44/SLI_3187. That accession has been deleted because it is not in a reference proteome. The normal fetch was attempted and returned empty UniProt text plus a zero-row stub; these generated files remain byte-preserved only in the ignored audit cache, not as a fabricated live gene record.

The official UniParc entryUPI0001B50C52 connects the retired1326 entry, activeTK24 entry and GenBankEOY47900.1. The reproducible `cslA-source-analysis/verify_identity.py` proves complete native protein-sequence equality between the frozenTK24 record, archivedUniSave1326 record, GenBank1326 protein, UniParc sequence and translation of the1326 genomic CDS. Source primers3187-F/R match that genomic locus exactly. Complete identity supports biochemical transfer, not native regulation, expression or phenotype in TK24. The legacy GenBank product name “Dolichol-phosphate mannosyltransferase” is not functional evidence and is contradicted by the characterized activity.

The official supplementary DOCX, text extraction and FigureS2 are preserved under STRL6/glxA source-analysis. FigureS1's caption inconsistently names S. coelicolor Q9RDB5 despite its S. lividans title; it is not used as the sole source identity. TableS3, methods locus, genomic sequence and primer checks provide the identity chain. CslA in pXZ10/pXZ13 has C-terminal6His/12His tags. The NdeI primer design can introduce an initiating methionine before the native CslA; no independently deposited complete engineered plasmid sequence was available.

## Demonstrated chemistry versus native product

[PMID:38557137](https://pmc.ncbi.nlm.nih.gov/articles/PMC11022532/) coexpressed source1326 CslA with PelB-GlxA(12–645) in E. coli, purified the complex, measured UDP-glucose consumption/UDP release and characterized the insoluble product by selective enzyme digestion and MALDI FT-ICR mass spectrometry. The authors establish beta-1,4-glucan cellulose synthesis in vitro. They explicitly leave the native glycan composition open. Therefore the specific molecular function refines the broad hexosyltransferase source row, but a separate native cellulose-biosynthesis process annotation is not manufactured. This is coherent glycan-synthase biochemistry, not an isolated promiscuous reaction detached from the protein's native glycan-production role.

c-di-GMP enhances the complex activity, but the binding site is unresolved and the proposed role of GlxA region2 is hypothetical. No direct c-di-GMP-binding annotation is added to either subunit. The current CslA record is in PANTHER SF2 but lacks IPR003919 and a recognized PilZ domain, illustrating why those signatures cannot be universal cellulose-synthase requirements.

## Annotation and ontology checks

Three source rows retain every original non-review field. Plasma membrane is accepted; membrane is refined to plasma membrane; hexosyltransferase is refined to cellulose synthase (UDP-forming). Live QuickGO ancestry confirms both replacements are descendants. Same-role comparator Q9RDB5 (S. coelicolor CslA) carries a cellulose-biosynthesis annotation, but that does not establish native TK24 polymer composition. No target GO-CAM was found. No NEW row or proposed term is required for the supported catalytic refinement.

## Research and validation provenance

Normal fetch completed for the active record before review. The pristine document, all three annotation payloads and raw hashes were saved in `.cache/module-audit-logs/cellulose-20261105/streptomyces-baseline.json`. Raw UniProt and GOA files were not edited. Default Falcon research failedHTTP403; the log is preserved and no provider report was fabricated. These are manual research notes. The primary2024 paper is normally cached in full. Exact sources and hashes are recorded in the adjacent provenance files. Reproduce the identity report with `uv run python genes/STRLI/cslA/cslA-source-analysis/verify_identity.py`.
