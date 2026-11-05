# LOC541641 (ZmHK2) curation notes

## 2026-10-28 initial review

- fetch-gene resolved A0A1D6N2S4 as requested (GeneID 541641, "histidine kinase 2");
  GOA has 15 rows, all IBA/IEA. No experimental GOA rows exist for this entry even
  though ZmHK2 was characterised in PMID:15064375 and PMID:21778179 (both full text read).
- Identity of A0A1D6N2S4 with the published ZmHK2 (AB102956) confirmed by length
  (1,007 aa), N-terminal MTVTA encoded by the published cloning primer, and the
  Ala695-Gln1007 fragment in PMID:21778179.
- Curation gaps (not knowledge gaps): GOA lacks IDA rows for cytokinin receptor
  activity, cytokinin binding and cytokinin-activated signaling for ZmHK2; added as NEW.
- ARBA00028712 maps CHASE-domain cytokinin receptors to GO:0019955 cytokine binding
  (same defect recorded for ZmHK1); recorded as source defect.
- ARBA00002427 FUNCTION text ("transmits the stress signal to a downstream MAPK
  cascade") is AHK1-type osmosensor wording, unsupported for ZmHK2.
- Seed-germination and cold IBA rows come from Arabidopsis AHK2/3/4 mutant
  phenotypes; not established for maize, marked over-annotated.
- Plasma membrane: leaf membrane fractionation (ZmHK2-rich) shows denser tZ binding in
  PM-enriched fraction, yet most binding is endomembrane; kept as non-core.
