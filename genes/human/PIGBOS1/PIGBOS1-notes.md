# PIGBOS1 (A0A0B4J2F0) review notes

## 2026-09-30 session (claude-code)

### Identity
- 54-aa microprotein encoded by a smORF in exon 2 of a transcript on the opposite strand of PIGB
  (chr15). UniProt: single TM helix (aa 5-25), N-terminus (1-4) in IMS, C-terminus (26-54)
  cytoplasmic; region 30-36 required for CLCC1 binding. Pfam PF23670 / InterPro IPR057394
  (PIGBOS1 family); PAN-GO has 0 IBA annotations. No paralogs.
- [PMID:31653868 "PIGBOS has no paralogs or homologs which prevents any molecular, cellular, or physiological function from being inferred, and requires the de novo characterization of PIGBOS."]
- Translation shown by a tryptic peptide and antibodies:
  [PMID:31653868 "During proteomic searches for microproteins, we identified a tryptic peptide, MQLVQESEEK, from the human 54-amino acid PIGB opposite strand 1 (PIGBOS) microprotein"]
- NB: the Chu et al. paper is Nat Commun 2019 (PMID:31653868), not Cell Chem Biol as in the task brief.
  PMID verified by E-utilities and cached full text (PMC6814811).

### Localization
- MOM by fractionation, IF colocalization with Tom20, proteinase K protection assay, split-GFP:
  [PMID:31653868 "Proteolysis of isolated mitochondria with proteinase K under conditions that retain MOM integrity led to the degradation of PIGBOS—an identical result to that of the MOM protein Tom20—indicating that PIGBOS is a MOM microprotein"]
- Signal-anchor topology:
  [PMID:31653868 "PIGBOS’s topology indicates that it belongs to a group of MOM proteins called signal-anchor proteins"]
- MitoCoP high-confidence mitochondrial proteome (HTP) includes PIGBOS1:
  [PMID:34800366 "the small open reading frames (smORF)-encoded proteins SMIM26, SLC35A4, and PIGBOS1"]
- ER-mitochondria contacts: PIGBOS-CLCC1 split-GFP signal peaks between the ER and MOM markers, but PIGBOS
  is not a tether (no ERMICC change in KO; overexpression does not remodel contacts).
  [PMID:31653868 "We observed no changes to ER-mitochondria contact sites"]
- GOA gives CLCC1 (Q96S66) GO:0044233 (MAM contact site, IDA, PMID:31653868) but gives PIGBOS only MOM.
  Comparator check: MOM-side contact-site proteins RMDN3/PTPIP51 (Q96TC7), MFN2 (O95140) and VAPA
  (Q9P0L0) carry no direct GO:0044233 annotation in QuickGO. So I do NOT propose GO:0044233 as NEW;
  the curator's choice (CLCC1 = MAM fraction; PIGBOS = MOM) is consistent with the data.

### Interaction with CLCC1
- IP-MS + SAINT/CRAPome, APEX proximity labelling, reciprocal co-IP, split-GFP, flow cytometry.
- Region 30-36 critical:
  [PMID:31653868 "Immunoprecipitation experiments identified amino acids 30–36 of PIGBOS to be critical for CLCC1 binding since mutation of these amino acids to alanine resulted in decreased CLCC1 enrichment"]
- Interaction not regulated by ER stress (IP and split-GFP after TM/TG).
- CLCC1 has GO:0005254 chloride channel activity (IDA PMID:37142673, plus IBA) in GOA, so it qualifies
  as a transmembrane transporter; GO:0044325 transmembrane transporter binding is the informative
  replacement for the bare protein binding row.
- Homo-oligomerization (human-human and human-rat co-IP); TMDOCK predicts TM homodimer. Not proposed
  as an MF term (binding term of little value).

### UPR phenotype (the one BP in GOA)
- Loss (siRNA KD, CRISPR KO) -> heightened XBP1 splicing, ATF6 reporter, all UPR target genes;
  rescue by siRNA-resistant PIGBOS; overexpression dampens UPR. Directional in both senses, so the
  annotation can be sharpened to negative regulation (GO:1900102).
  [PMID:31653868 "Overexpression of PIGBOS in WT cells resulted in the desensitization of cells to UPR with decreased XBP1 splicing"]
  [PMID:31653868 "Upon UPR induction with TM, the loss of PIGBOS led to dramatic increases in the levels of all UPR target genes measured, indicating increased UPR signaling across all the branches (IRE1, PERK, and ATF6)"]
- Requires CLCC1 binding: C-terminal truncation and 30-32 AAA mutant fail to rescue:
  [PMID:31653868 "Only full-length PIGBOS microprotein reversed the XBP1 splicing phenotype"]
- Specific to ER UPR (no effect on mitoUPR with CDDO); increased ER-stress apoptosis (caspase-3,
  PARP cleavage) in KD/KO cells, but staurosporine-induced death unchanged. The apoptosis effect is
  treated as a downstream consequence of heightened UPR; no NEW apoptosis term proposed.

### Newer work
- Aditya & Bera 2026 (PMID:42351194, single lab, HEK293T): PIGBOS promotes IP3R-mediated ER Ca2+
  release, ER-to-mitochondria Ca2+ transfer and SOCE, all dependent on CLCC1-binding C-terminus;
  loss impairs respiration and ATP.
  [PMID:42351194 "Deletion of the CLCC1-binding C-terminal region of PIGBOS abolishes its effect on Ca2+ signaling"]
  Mechanism is explicitly unresolved (direct vs via intermediaries), and much is expression-level
  change of Ca2+ machinery. Not proposed as NEW; raised as a suggested question.
- MitoCoP q-AP-MS (PMID:34800366): FLAG-PIGBOS1 copurified HIGD2A and complex III/IV subunits,
  [PMID:34800366 "The smORF protein of 6.3 kDa, PIGB opposite strand 1 (PIGBOS1), copurified the hypoxia inducible domain family member 2A (HIGD2A)"]
  Hard to reconcile with a MOM signal-anchor protein whose IMS-facing part is only ~4 residues;
  could reflect digitonin-solubilized overexpressed protein. Not used for annotation.

### Other PubMed hits (esearch "PIGBOS1 OR PIGBOS", 7 hits)
- 41465308 (review on microproteins), 41277184 (oocyte aging omics), 40287452 (horse astaxanthin),
  31858090 (AD hypothesis), 29100423 (lncRNA biomarker melanoma) - incidental mentions; not used.

### Decisions summary
- protein binding IPI (CLCC1) -> MODIFY to GO:0044325 transmembrane transporter binding
- mitochondrion HTP -> ACCEPT (less specific than MOM)
- MOM IDA -> ACCEPT (core)
- MOM IEA -> ACCEPT
- regulation of ER UPR IMP -> MODIFY to GO:1900102 negative regulation of ER UPR
- No NEW terms.
