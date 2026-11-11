# Serinc (DROME) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Identity
- Benchmark accession M9PCT1 is **Serinc isoform C** (Serinc-PC, FBpp0302688, 458 aa), a TrEMBL entry
  (PE 3). The gene FBgn0028399 (CG4672, DmSERINC, TMS1) has six products: PA Q9VV58 (465 aa), PB M9PI80
  (462), PC M9PCT1 (458), PD M9PFH8 (461), PE M9PFW5 (456), PF M9PFR2 (467). None is Swiss-Prot reviewed.
  The gene-centric canonical (GCRP, AlphaFold, PANTHER HMM member) is **M9PFR2 (isoform F)**.
- `Serinc-bioinformatics/compare_isoforms.py` shows M9PCT1 = isoform A minus 7 residues (VLTEALS) in the
  cytosolic TM8-TM9 loop near residue 366. Isoform F shares residues 1-412 and has an alternative
  C-terminal segment from about 413 onward. M9PCT1 is a full native isoform, not a fragment or a defective
  gene model.
- `check_structure_residues.py`: Pye et al. 2020 (PMID:31907454; PDB 6SP2) numbering matches isoform A
  (18/18 named residues). M9PCT1 carries all of them, with the five C-terminal ones shifted by -7.

### Evidence
- The only primary fly-protein study is PMID:31907454 (full text). Purified DmSERINC is a hexamer of
  ten-TM protomers held together largely by lipid, with cardiolipin at the interfaces. An acyl chain sits
  in the subdomain-B groove, and PS/cholesterol/sulfatide stabilise the protein
  ["the cryo-EM map revealed presence of an acyl chain bound at this site"]. Ectopic expression in HEK293T
  restricts Nef-deficient HIV-1. That is a heterologous assay and is not annotated as a fly process.
- Scramblase activity was shown for human SERINC3/5 (PMID:37474505), but those sit in PANTHER subfamilies
  SF51/SF16, while fly Serinc is in SF9 with yeast TMS1, worm Y57E12AL.1 and S. pombe SPAPB1A10.07c.
  The PAINT IBD for PTHR10383 (PTN000043695, eukaryota) propagates only GO:0016020 membrane, which I treat
  as a deliberate decision. Scramblase activity is therefore not transferred.
- No fly loss-of-function phenotype or native localization was found (deep research agrees).

### Decisions
- GO:0016020 membrane (IEA): ACCEPT. No more specific compartment is supported for the fly protein.
- NEW GO:0008289 lipid binding (IDA, PMID:31907454). Generic rather than PS binding because several
  lipids stabilise the protein and no specificity was measured.
- Description rewritten to drop "native" isoform hedging and add the structural findings.

### Relatives / family
- PANTHER family review `interpro/panther/PTHR10383/PTHR10383-review.yaml` lists M9PCT1 as the SF9
  representative. The PANTHER 19.0 HMM classification lists the fly member as M9PFR2. This is the same
  gene and the same SF9, so there is no placement disagreement, only a different representative isoform.
- Next relative: the canonical product of the same gene, M9PFR2 (isoform F). No review exists
  (would be `genes/DROME/Serinc__M9PFR2`). The closest experimentally studied SF9 member in another
  species is yeast TMS1 (Q12116); no review exists for it either.
- No modules mention SERINC/Serinc.
