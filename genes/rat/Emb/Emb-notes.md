# Emb (rat) review notes

- Session: de novo review. GOA had 17 rows. Literature work done by hand
  (see Emb-deep-research-manual.md); no deep-research provider used.
- Core function: ancillary/chaperone subunit for MCT2 (Slc16a7), MCT1 (rat erythrocyte)
  and MCT7, required for plasma membrane expression and activity of the transporter
  [PMID:20695846 "expression of active MCT2 at the plasma membrane of oocytes was
  significantly enhanced by co-expression of exogenous embigin"].
- Bare protein binding (IPI, MCT2) -> MODIFY to GO:0140597 protein carrier activity; the
  comparator BSG (same ancillary role for MCT1/MCT4) carries GO:0140597 and GO:0072659 by
  IDA, so NEW GO:0072659 protein localization to plasma membrane passes the comparator
  check; embigin itself does the escort work.
- Synapse rows (IEA/ISS/ISO) -> MODIFY to neuromuscular junction (GO:0031594), the
  location stated in PMID:19164284.
- IBA rows from the broad IgSF node PTN001296633 (Dscam, Fas2, otk, BSG, NPTN...):
  plasma membrane accepted; axon, axon guidance, homophilic adhesion and adhesion-mediator
  activity marked over-annotated; dendrite self-avoidance removed (Dscam-specific function,
  embigin is a muscle/epithelial protein).
- Cell adhesion (IDA, PMID:9438341): abstract only; kept as non-core, consistent with mouse
  embigin promoting integrin-mediated cell-substratum adhesion [PMID:8432389].
- Did not propose NEW terms for NMJ sprouting or taurine transport (overexpression /
  co-expression phenotypes; strict NEW bar).
