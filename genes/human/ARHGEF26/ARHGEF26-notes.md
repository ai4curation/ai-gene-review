# ARHGEF26 (SGEF) notes

## Biology
- RhoG-specific GEF (not Rac); drives dorsal ruffles and macropinocytosis [PMID:15133129].
- Scribble/Dlg1 ternary complex [PMID:31248911] (full text):
  - Scribble PDZ1 binds an *internal* PBM (crystal structure); the C-terminal ETNV PBM is dispensable for Scribble binding.
  - The Dlg1 GUK domain (not its PDZ or SH3) binds a conserved 50-aa N-terminal SGEF region.
  - SGEF bridges the two at apical junctions and regulates contractility, tight-junction barrier and adherens junctions.
- Follow-up on E-cadherin and ZO-1 stability [PMID:39350674].
- Endothelium:
  - RhoG activation at ICAM-1 docking structures; knockout mice have less atherosclerosis [PMID:23372835].
  - VEGFR2 macropinocytosis and angiogenesis [PMID:34849650].
- Src phosphorylation of Y530 inhibits activity [PMID:27437949].

## GOA calls
- **Protein binding (31 rows):**
  - DLG1 → MODIFY to adaptor activity (GUK-mediated; bridging).
  - Scribble → MODIFY to PDZ domain binding plus adaptor activity.
  - The other PDZ proteins → MODIFY to PDZ domain binding. Their pairs are in the PMID:36115835 fragmentomics supplementary data (PDZ vs PBM-peptide affinities).
- **GEF activity (IBA/IEA) and actin organization (IBA): ACCEPT.** The IBA node is PTN002656129 (ephexin-family seeds).
- **Plasma membrane: ACCEPT.** Cytosol and ruffle: non-core.
- Review round (PR #4163):
  - NEW positive regulation of macropinocytosis (IMP; PMID:34849650 VEGFR2 macropinocytosis, PMID:15133129 DH-dependent dextran uptake). Precedent: genes/DICDI/rasG.
  - The core function records RHOG (P84095) as substrate.
  - Affinage findings not annotated, with dispositions:
    - EGFR endosomal trafficking (PMID:23661635): GEF-independent, prostate cancer cells.
    - Salmonella invasion (PMID:34242364): pathogen-specific.
    - Nuclear BRCA1 complex (PMID:26764186): glioma; single study.
    - SOX2 stabilization (PMID:41936941): glioblastoma; single study.
    - None is a general function suited to a GO annotation here.
  - Isoforms:
    - Q96DR7-3 (CSGEF, VAR_SEQ 447..871) lacks the DH/PH, SH3 and PBM but keeps the N-terminal Dlg1 GUK-binding region, so it is a natural GEF-dead variant.
    - Q96DR7-4 (VAR_SEQ 790..871) lacks the SH3 and PBM.
  - Q86UT5 is NHERF4, its current UniProt/HGNC symbol (formerly PDZD3).
