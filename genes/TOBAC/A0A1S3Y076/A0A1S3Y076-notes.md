# A0A1S3Y076 (Nicotiana tabacum LOC107770656) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No notes file existed before this session; this is the first entry. ProtNLM2 files were not opened.

### Identity
- UniProt A0A1S3Y076 (TrEMBL, PE 3), 540 aa, RefSeq XP_016445475.1, chromosome 22. Full-length: PROP1-like PPR
  domain 4-208, PRORP nuclease domain 251-476, disordered C-terminal tail. Not a fragment or isoform.
- PANTHER PTHR13547:SF13 "PROTEINACEOUS RNASE P 2". The SF13 member list in
  `interpro/panther/PTHR13547/PTHR13547-entries.csv` includes Arabidopsis PRORP2 (Q680B9); PRORP3 (F4JKB6) is
  in SF20 and PRORP1 (Q66GI4) with animal mitochondrial PRORP in SF1.
- Own analysis (`A0A1S3Y076-bioinformatics/RESULTS-rereview.md`): 57% identity to PRORP2, 59% to PRORP3, 50%
  to PRORP1; all 8 PRORP1 Zn/Mn ligands conserved (D310, D386, D387, D405 catalytic); no transit-peptide
  extension. So the tobacco protein is the nuclear-type PRORP.

### Literature (Arabidopsis PRORP2, the characterized SF13 member)
- Karasik 2016 [PMID:26655022 "PRORP2 and PRORP3 localize to the nucleus and PRORP1 localizes to the chloroplast and the mitochondria"]; crystal structure and Mg2+-dependent catalysis [PMID:26655022 "PRORP2 requires Mg(2+) for catalysis and catalyzes the maturation of nuclear encoded substrates"].
- Gutmann 2012 [PMID:22549728 "protein-only RNase P enzymes called PRORP (for proteinaceous RNase P) support RNase P activity in vivo in both organelles and the nucleus in Arabidopsis"] (abstract only).
- Arrivé 2023 [PMID:37945696 "PRORP2 occurs in a complex with the tRNA methyl transferases TRM1A and TRM1B in vivo"]; TRM1A/B facilitate nuclear RNase P activity. Not transferred to tobacco as a GO term.
- Gobert 2010 (PMID:20473316) and Gobert 2013 E. coli complementation (PMID:28499021) cached for context.

### Problems found in the previous review
- The falcon deep research run states "no contexts were retrieved" — it is ungrounded, and it predicted
  organellar localization, which contradicts the SF13 placement and the lack of a transit peptide.
- Two supporting_text quotes attributed to the deep-research file were not present in that file (fabricated
  bracketed paraphrases). Replaced with verifiable PMID quotes.
- The description claimed Mg2+ cofactor and organellar/nuclear options without resolving compartment; now resolved
  to nucleus by subfamily.

### Decisions
- GO:0004526 ribonuclease P activity (IBA, IEA): ACCEPT, core.
- GO:0001682 tRNA 5'-leader removal (IBA, IEA): ACCEPT, core.
- NEW GO:0005634 nucleus, by transfer from PRORP2 within SF13 (supported by no transit peptide). PAINT made no
  plant CC assertion at PTN001005190 (a eukaryote-wide node with mixed compartments), so this is not
  contradicting a curator decision.
- No TRM1 interaction or snoRNA/mRNA processing terms added (one-species, not PAINT-propagated).

### Relative
- Arabidopsis PRORP2 (Q680B9, AT2G16650), same PANTHER subfamily SF13; no review in repo (genes/ARATH has no
  PRORP folder).
