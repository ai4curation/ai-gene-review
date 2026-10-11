# Cd48 (rat, P10252) notes

## 2026-10-04 initial review

- Deep research NOT run: all providers are broken in this environment (falcon 402, openai 401, perplexity missing). Review based on UniProt entry, cached GOA PMIDs, PMID:9841922 (full text) and PMID:16803907 (fetched; verified against UniProt P10252 RX citation, abstract-only).
- bgpt literature search hit its free-tier limit, so the classic van der Merwe et al. rat CD2-CD48 SPR kinetics paper was not added (PMID not verified).
- Key facts:
  - Rat OX-45 = CD48; GPI-anchored glycoprotein of leukocytes and endothelium [PMID:3181129 "The MRC OX-45 cell surface antigen is a glycoprotein of 45,000 apparent mol. wt of rat leukocytes and endothelium."]. The abstract numbers the GPI serine as 195 (mature numbering) = Ser-217 in UniProt precursor numbering.
  - In rodents CD2 and CD244 share CD48 as ligand; rat CD48 also binds 2B4R [PMID:16803907 "In mice and rats, CD2 and CD244 (2B4), which are expressed predominantly on T cells and natural killer cells, respectively, bind the same, broadly expressed ligand, CD48."].
  - 2B4 binding to rat cells blocked by rat CD48 mAb [PMID:9841922 "This binding was completely inhibited by a rat CD48 mAb"].
- Decisions: protein-containing complex (IDA, PMID:9576909) marked over-annotated; NEW cell adhesion molecule binding (GO:0050839) for CD2 binding. Heterotypic cell-cell adhesion ACCEPTed (core in rodents, unlike human where CD58 is the main CD2 ligand).
