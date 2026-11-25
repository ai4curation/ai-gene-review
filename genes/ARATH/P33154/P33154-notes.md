# P33154 (PR1, At2g14610) review notes

## Session 1

- Fetched with `just fetch-gene ARATH P33154`; UniProt id confirmed P33154 (PR1_ARATH,
  TAIR AT2G14610, GeneID 815949). The GN line has no Name= field, so the folder and
  `gene_symbol` stay at the accession; TAIR symbol is PR1.
- No deep-research keys: synthesis in `P33154-deep-research-manual.md`.
- Key paper PMID:37542077 (full text): PR1 is the pro-protein of the phytocytokine CAPE9,
  released by XCP1 cleavage after the CNYD motif; pr1 CRISPR mutant lacks systemic
  immunity; complementation needs the cleavage site and the CAPE9 sequence
  [PMID:37542077 "both CNYD and CAPE domains for proteolytic production of AtCAPE9 from PR1
  are crucial for eliciting Arabidopsis systemic immunity"].
- PMID:23144921 (full text) read: PR1 only used as SA marker; transcript down under drought
  [PMID:23144921 "only the expression level of PR1, which is associated with the salicylic
  acid pathway, decreased under drought stress"].
- IPI protein binding row (PMID:37542077) has With/From = AGI_LocusCode:AT2G14610 (PR1
  itself). The paper does not test PR1 self-association; the interaction assayed is with
  XCP1 (At4g35350) (Fig. 5 "interaction with PR1-eYFP"). Recorded as WRONG_WITH_FROM.
- Molecular adaptor activity IBA rests on a single mouse CAP-family seed at the deep CAP
  node (PTN000036124); no plant evidence. Marked over-annotated.
- Sterol binding is a family-level property (tobacco/tomato PR-1, PMID:27747953 abstract);
  not proposed as NEW for Arabidopsis PR1 without gene-specific data; raised as a question.
- NEW-term bar: no NEW rows added. "Peptide hormone processing"-like terms would belong to
  XCP1, not PR1 (the substrate does none of the cleaving).
