# A0A444Z7V7 (Arachis hypogaea, Ahy_B05g078721) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files or prediction-evidence folders were opened for this review.

### Identity
- UniProt TrEMBL entry A0A444Z7V7, 1139 aa. Its EMBL cross-references are three CDS records
  (RYR10247-RYR10249) in WGS contig SDMP01000015. The product is full length: it aligns over
  1131 columns to Arabidopsis CSLD3 (Q9M9M4, 1145 aa). All PIRSR catalytic and binding
  residues are retained (D410, D627, D842 and the UDP-glucose binding residues) and the QVLRW
  motif sits at 880-884. It is not a fragment, an isoform or an alternative gene model
  (`A0A444Z7V7-bioinformatics/RESULTS.md`).
- PANTHER PTHR13301 is "X-BOX TRANSCRIPTION FACTOR-RELATED", a misleading family name. Neither
  UniProt nor the InterPro API assigns a subfamily. The candidate subfamilies in panther.obo are
  SF58 "CELLULOSE SYNTHASE-LIKE PROTEIN D3" and SF40 "...D4". Without a subfamily call, the
  placement here comes from my MAFFT + NJ tree: the protein falls in the CSLD2/CSLD3 clade, with
  AtCSLD3 at 0.858 identity, AtCSLD2 at 0.852 and OsCSLD2 at 0.832.
- PAINT: node PTN001410221 propagates GO:0005886 plasma membrane and GO:0009833 plant-type primary
  cell wall biogenesis to AtCSLD3 (QuickGO, GO_REF:0000033). The peanut entry has no IBA rows.

### Literature on the closest characterised relative, AtCSLD3/KOJAK
- [PMID:11156607 "KOJAK encodes a cellulose synthase-like protein, AtCSLD3"]: the gene is needed
  for root hairs, which rupture at the tip in the mutant. The GFP fusion was seen in the ER.
- [PMID:21765420 "eYFP-CSLD3 proteins, but not CESA cellulose synthases, localize to a polarized plasma-membrane domain in root hairs"],
  and ["CSLD3 represents a distinct (1→4)-β-glucan synthase activity in apical plasma membranes"].
- [PMID:32169960 "CSLD3 is a UDP-glucose-dependent β-1,4-glucan synthase"]: shown by
  reconstitution. Abstract only.
- [PMID:21904114 "CSLD2, CSLD3 and CSLD5 are involved in mannan synthesis"] and PMID:21471331:
  mutant and microsomal evidence for mannan. This conflicts with PMID:32169960.
- [PMID:18768911 "the expression of both CSLD2 and CSLD3 is elevated at reduced temperatures"]:
  the probable basis of the cold-response ARBA rule.

### Changes from the previous review
- Cellulose synthase (UDP-forming) activity: MODIFY to mannan becomes ACCEPT. It is now the core
  MF, because its reaction definition matches the CSLD3 biochemistry.
- Cellulose biosynthetic process: MODIFY to cell wall organization becomes ACCEPT.
- Mannan synthase activity: ACCEPT (core) becomes MARK_AS_OVER_ANNOTATED, as a disputed claim. It
  is not removed, because TAIR holds an experimental annotation for AtCSLD3.
- Golgi membrane: ACCEPT becomes KEEP_AS_NON_CORE, because the Golgi is a transit compartment.
- Cytoplasm and endomembrane system become TOO_GENERAL, since both are entailed by Golgi membrane.
- Membrane becomes MODIFY to plasma membrane, and plasma membrane is added as NEW (ISS from AtCSLD3).
- The falcon deep-research report treats the protein as a generic CESA and misses the CSLD
  placement. It is now kept only as a low-relevance reference.

### Relative and modules
- Next relative to review: Arabidopsis CSLD3/KJK (Q9M9M4). No review exists in the repo.
- modules/cellulose_biosynthesis.yaml (plant CESA/CSC module) explicitly excludes CSL families,
  so this protein is not a part of it. It is related only through the shared beta-1,4-glucan chemistry.
