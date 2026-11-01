# rfth-1 (ZK180.3; UniProt Q23444) - manual literature research

No deep-research provider was available; this summary was assembled by hand from PubMed searches and
cached publications. Searches for "ZK180.3" or "rfth-1" in C. elegans in PubMed returned no articles
(2026-10-28), so all functional knowledge is inferred from orthologs.

## Identity of the gene

- rfth-1 = "RFT1 homolog", ORF ZK180.3, chromosome IV, three splice isoforms (a/b/c). UniProt Q23444 is
  Swiss-Prot reviewed but PE 3 (inferred from homology). Function text is by similarity to human
  Q96AA3 and yeast P38206 [file:worm/rfth-1/rfth-1-uniprot.txt "RFT1 could mediate the translocation of
  the cytosolically oriented intermediate DolPP-GlcNAc2Man5"].
- Member of Pfam PF04506 (Rft-1), InterPro IPR007594, PANTHER PTHR13117:SF5 "PROTEIN RFT1 HOMOLOG".
- About 31% identity to human RFT1 and 25% to yeast Rft1 over the whole length
  [file:worm/rfth-1/rfth-1-bioinformatics/RESULTS.md].
- Predicted multi-pass membrane protein (UniProt TRANSMEM features, ECO:0000255).

## Nomenclature hazard: rfth-1 is not rft-1

- C. elegans rft-1 (Y47D7A.16) and rft-2 (Y47D7A.14) are riboflavin transporters, orthologs of human
  SLC52A (RFVT3), and are unrelated to the RFT1 dolichol-linked oligosaccharide family
  [PMID:23483992 "we assign them the names rft-1 (for Y47D7A.16) and rft-2 (for Y47D7A.14)"].
  PMID:23483992 does not mention ZK180.3 or rfth-1 and provides no evidence about this gene.

## Ortholog biology (RFT1 family)

- Yeast Rft1 genetics: required for appearance of Man5GlcNAc2-PP-Dol (M5-DLO) on the luminal side
  of the ER [PMID:11807558 "yeast RFT1 encodes an evolutionarily conserved protein required for the
  translocation of Man5GlcNAc2-PP-Dol from the cytoplasmic to the lumenal leaflet of the ER membrane"].
- Human RFT1-CDG: loss of RFT1 stalls LLO assembly at M5-DLO; human RFT1 complements yeast deletion
  [PMID:18313027 "RFT1 deficiency in both yeast and human cells leads to the accumulation of incomplete
  DolPP-GlcNAc(2)Man(5)"].
- Controversy: Rft1 is dispensable for M5-DLO flipping in reconstituted vesicles and sealed microsomes
  [PMID:18668045 "a specific ER protein(s), but not Rft1, is required to flip"],
  [PMID:19494107 "no difference was seen in the level of M5-DLO flippase activity in sealed wild type and
  Rft1-depleted microsomal vesicles"]; Rft1-null trypanosomes are viable
  [PMID:23720757 "TbRft1-null procyclic trypanosomes grow nearly normally"].
- Reconstitution: purified yeast, human and archaeal Rft1/Agl23 translocate M5-DLO in liposomes,
  ATP-independently [PMID:38886340 "Translocation was ATP-independent ... and importantly, was dependent
  on addition of purified Rft1 or archaeal Agl23"].
- Human Rft1 is a polytopic ER protein with cytosolic termini [PMID:39025454].
- A portal-blocking yeast mutant predicted to lack scramblase activity still supports growth, suggesting
  M5-DLO binding/chaperoning may be the essential role [PMID:42417535 "while M5-DLO binding is important
  for Rft1's essential function, scrambling activity is dispensable"].

## Summary for the worm gene

All GO annotations for rfth-1 are IBA/ISS/IEA. The family-level picture (ER membrane, required for
dolichol-linked oligosaccharide assembly at the M5-DLO step, M5-DLO translocase activity in vitro)
transfers with reasonable confidence; worm-specific localization, phenotype and activity are untested.
