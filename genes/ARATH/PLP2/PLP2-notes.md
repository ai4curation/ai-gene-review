# PLP2 (O48723, At2g26560) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PLP2 is reviewed as the closest experimentally characterised relative of the
wheat ProtNLM2 benchmark protein A0A3B6GK97. ProtNLM2 output was not opened or used.

### Deep research

`just deep-research-falcon ARATH PLP2 --fallback perplexity-lite` failed on 2026-10-21:
falcon raised "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists; the review is based on the cached
primary literature and the UniProt record listed below.

### Literature read

- PMID:16297072 (La Camera 2005, abstract only in cache). PLP2 is induced by B. cinerea and
  avirulent P. syringae in a JA/ET-dependent, SA-independent manner; GFP fusion and
  recombinant protein show "PLP2 encodes a cytoplasmic lipid acyl hydrolase with wide
  substrate specificity". Silencing increases resistance to B. cinerea and avirulent
  bacteria; overexpression increases susceptibility, and PLP2 levels correlate with cell
  death after paraquat or avirulent P. syringae.
- PMID:19271961 (La Camera 2009, abstract only). PLP2 "contributes to resistance to Cucumber
  mosaic virus"; alpha-dioxygenase-pathway oxylipins "accumulate in a PLP2-dependent manner"
  in Botrytis-infected leaves; PLP2 "strongly promotes necrotic symptoms in vad1 leaves";
  authors conclude "PLP2 is an integral component of the plant cell death execution
  machinery".
- PMID:22259021 (Yang 2012, full text). Purified recombinant pPLAIIalpha releases fatty acids
  at both sn-1 and sn-2 of PC, PE, PG, PA, PS and PI, and hydrolyses nearly all MGDG/DGDG
  species, including OPDA-containing arabidopsides, to lyso-galactolipids. The T-DNA KO
  (Salk_059119) has ~30% less LPC and ~15% less LPE, more free linolenic acid, ~2x JA and MeJA,
  more 13-HPOT and OPDA, and loses water faster (complemented). Authors: "pPLAIIα negatively
  regulates oxylipin production", possibly via removal of oxidised fatty acids from membranes.
  So the sign of the oxylipin effect differs between the basal-state KO (Yang) and the
  Botrytis-challenged state (La Camera 2009, alpha-DOX products).
- PMID:12226489 (Holk 2002, full text). AtPLA IIA (= PLP2) transcripts are mainly in roots;
  GFP fusion in tobacco leaves is cytosolic, not vacuolar; "association with membranes (e.g.
  plasma membrane or ER) cannot be excluded"; only AtPLA I-GFP (a different gene) was seen on
  chloroplasts. No signal peptide in any Arabidopsis pPLA.
- PMID:14634163 (Narusaka 2003, abstract). AtPLA IIA promoter induced by many biotic and
  abiotic stresses.
- PMID:17075075, PMID:21398256 (abstract only): proteome/expression screens (Cd2+, hypoxia);
  PLP2 is not named in the abstracts; curators' IEP rows kept as non-core.
- PMID:21798944, PMID:32612234: Y2H interactome screens (self-interaction; CYCB2-2, SCL23).
- PMID:28887381: membrane-proteome SEC profiling; peroxisome HDA cannot be verified from
  the cached text (assignment is in supplemental tables).

### Evolutionary placement (for transfer to A0A3B6GK97)

- PANTHER 19: PTHR32176:SF109 "PATATIN-LIKE PROTEIN 2" (UniProt DR line and
  `interpro/panther/PTHR32176/PTHR32176-entries.csv`). PLP1, PLP4 and PLP5 are in SF89
  (PATATIN-LIKE PROTEIN 1-RELATED). Together these form the Arabidopsis pPLAII clade.
- PAINT (`interpro/panther/PTHR32176/PTHR32176-paint.tsv`):
  - PTN001282408 (taxon:2759) IBD for GO:0004620 glycerophospholipase activity and
    GO:0047372 monoacylglycerol lipase activity, seeded by AT4G37050/AT4G37060/AT4G37070.
    This is a deep node, so these MF terms are expected across the pPLAII clade including
    the grass SF103 proteins.
  - PTN004927362 (taxon:3700, Brassicaceae) IBD for GO:0009626 plant-type hypersensitive
    response seeded only by AT2G26560 (PLP2 itself). Its taxon scope is Brassicaceae, so the
    PAINT curator deliberately did not extend the HR claim to the grass branch. That
    restriction should be respected when transferring to A0A3B6GK97.
- Per the task brief, A0A3B6GK97 (SF103) and rice PLP2 Q6ZJD3 (SF26) join the Arabidopsis
  pPLAII clade at duplication node PTN009133995, so they are out-paralogs of AtPLP2. Only
  deep-node, catalytic properties (patatin/PNPLA acyl hydrolase activity on glycerolipids)
  are reasonable to transfer. The PLP2-specific stress, cell-death and oxylipin phenotypes
  are not.

### Sequence features (UniProt O48723)

PNPLA domain 22-228, GXGXXG 26-31, GXSXG 64-68 with nucleophile S66, DGA/G 215-217 with
proton-acceptor D215 (ProRule). The Ser-Asp dyad is the patatin catalytic dyad, consistent
with the measured activity in PMID:22259021.

### Decisions summary

- MF: lipase activity rows MODIFY to glycerophospholipase activity + galactolipase activity
  (both measured on purified protein, PMID:22259021). The glycerophospholipase IBA is ACCEPTED.
  The monoacylglycerol lipase IBA is KEPT as non-core: it was not tested for PLP2 and comes
  from paralog seeds.
- BP: lipid metabolic process MODIFY to phospholipid catabolic process (in vivo KO lyso-lipid
  decrease) and galactolipid catabolic process. Programmed cell death (IGI with vad1) ACCEPT.
  HR rows, oxylipin biosynthesis, defense to virus, Cd and hypoxia responses KEEP_AS_NON_CORE.
- CC: cytoplasm ACCEPT; membrane ACCEPT (curator IDA; consistent with Holk caveat); chloroplast
  ISM REMOVE (GFP is cytosolic, no transit peptide); peroxisome HDA UNDECIDED.
- IPI protein binding REMOVE (policy); identical protein binding KEEP_AS_NON_CORE.
