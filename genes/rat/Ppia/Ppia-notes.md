# Ppia (rat) review notes

## 2026-10-28 session

- Fetched P10111 (PPIA_RAT; RGD:3372; GeneID 25518). 65 GOA rows: mostly ISO/ISS from human PPIA
  (P62937) and mouse Ppia (MGI:97749 / P17742); two rat IDA rows from PMID:19832699; IBA/IEA for PPIase,
  protein folding, nucleus.
- No deep-research provider; see Ppia-deep-research-manual.md.
- PMID:19832699 full text read: recombinant rat CyP-A PPIase activity and CsA Ki measured
  [PMID:19832699 "The binding affinities of CsA, SMBz-CsA and mtCsA to CyP-A were similar to those with
  CyP-D (Figure 1)."]. Calcineurin inhibition needs CsA; CyP-A alone slightly activated calcineurin
  [PMID:19832699 "whereas CyP-A alone produced a small (20%) activation of calcineurin"]. So the IDA
  "negative regulation of calcineurin-mediated signaling" row records a drug effect -> MARK_AS_OVER_ANNOTATED
  with a source_defects CHECK entry to RGD.
- Core: PPIase activity (cytosol/nucleus, also extracellular). Extracellular CyPA chemotaxis/EC
  activation signalling depends on rotamase site [PMID:11943775 "rotamase-defective CyPA mutants failed
  to initiate signaling events"] - kept as non-core process rows.
- Viral host-factor rows (influenza M1, HCV) and HCV-pan-cyclophilin-inhibitor rows (lipid droplet
  organization, protein secretion) marked over-annotated for rat.
- cytoplasm rows MODIFY -> cytosol (GO:0005829), which the gene already carries (ISS).
- No NEW rows proposed: candidate terms (cytokine activity, signaling receptor binding to BSG) would rest
  on human/mouse data only; left as a suggested question.
