# LOC541618 (ZmMPK5, K7VAM9) review notes

## 2026-10-28 session

- fetch-gene resolved K7VAM9 as requested; UniProt DR GeneID 541618 confirms the locus. 12 GOA rows,
  all IBA/IEA. No experimental GO annotations exist despite several functional papers.
- Confirmed ZmMPK5 = this gene: AB016802 translation matches K7VAM9 except residues ~75-98, and the
  antibody peptide (PMID:20693409) is the exact C-terminus of K7VAM9 (residues 379-398).
- Bioinformatics: TEY motif at 225-227, VAIK lysine 97, HRD Asp193; best Arabidopsis match MPK6 (86.7%).
  See LOC541618-bioinformatics/RESULTS.md.
- Decisions: MAP kinase activity is the core MF; generic kinase/transferase/Ser-Thr kinase rows MODIFY to
  GO:0004707 (verified is_a chain with OAK). intracellular signal transduction (IBA) MODIFY to MAPK
  cascade (is_a via GO:0141124). nucleotide binding MODIFY to ATP binding. Nucleus/cytoplasm IBA accepted
  (BiFC with ZmABA2 in nucleus and cytosol).
- No NEW BP terms: BR / ABA / H2O2 roles rest on inhibitor pharmacology, protoplast transient
  expression and heterologous overexpression; recorded as questions instead.
- Curation gap (not knowledge gap): kinase activity on MBP / ZmMAP65-1a / ZmABA2 (PMID:20693409,
  PMID:23956414, PMID:26096642) has no IDA row in GOA; could be added by a MaizeGDB curator.
