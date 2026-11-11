# vps1302 (O42926, SPBC16C6.02c) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed in its own right as the sequence relative of SCHPO/spo2. ProtNLM2
output was not consulted.

### Deep research
- `just deep-research-falcon SCHPO vps1302 --fallback perplexity-lite` failed: falcon
  (Edison) returned 403 on authentication and the perplexity-lite fallback returned
  401 (insufficient quota). No deep-research file exists; the review is based on the
  cached literature listed below and PomBase/UniProt/PANTHER data.

### Identity and evolutionary placement
- 3131 aa VPS13-family protein; UniProt PE=2 (transcript level); Chorein N-terminal
  domain (2-115) and SHR-BD domain (2085-2363) predicted (ECO:0000255).
- PANTHER: PTHR16166:SF93 (VPS13), same subfamily as S. cerevisiae VPS13 (Q07878).
  The other S. pombe family member in the repo PANTHER table, vps1301 (P87319), is in
  a different subfamily (SF145). PomBase lists S. cerevisiae YLL040C (VPS13) as the
  ortholog, and human VPS13A/VPS13C. So transfer from S. cerevisiae Vps13 is
  phylogenetically grounded at the subfamily level, and PAINT nodes PTN000414878 and
  PTN000414879 cover it.
- Spo2 (C6Y4C2) is 100% identical to Vps1302 residues 2999-3131
  (file:SCHPO/vps1302/vps1302-bioinformatics/RESULTS.md). A meiotic transcript from
  the 3' end of the locus encodes Spo2; vps1302 deletions remove the Spo2 ORF too.

### S. pombe experimental data (PomBase API, 2026-10-21)
- No GO annotation with experimental evidence. All GO terms are IBA/ISS/IEA/TAS.
- Deletion viable (PMID:20473289, PMID:23697806).
- FK506 screen [PMID:21850271 "The results showed that in Δapm1, Δvps1302 and Δgos1
  cells the acid phosphatase secretion index was dramatically decreased to
  approximately 50% of that in wild-type cells (Figure 4)."]; moderate micafungin
  sensitivity; normal vacuole fusion [PMID:21850271 "Only 6 of the 16 genes (Aps3,
  Apl6, Vps1302, Vps71, Erv15 and Myo1) showed normal vacuole fusion."]. The paper's
  "vacuole protein sorting" category for Vps1302 comes from GeneDB annotation, not an
  assay [PMID:21850271 "Table 1 lists the intracellular localization and
  intracellular transport steps that these genes are involved in based on our
  previous reports [23], [29], [33] and on the S. pombe GeneDB"]. ORFeome GFP
  localization: "no apparent signal".
- Meiotic chromosome segregation phenotype (PMID:29259000) and tunicamycin
  sensitivity (PMID:28945192) per PomBase; not used for GO (downstream phenotypes;
  meiotic phenotypes confounded by the nested spo2 ORF).

### S. cerevisiae Vps13 (same subfamily) — basis for transferred functions
- Lipid binding and transfer: Kumar 2018 (PMID:30093493) yeast Vps13 N-terminal
  fragment binds ~10 glycerophospholipids per molecule and transfers them in vitro;
  Li 2020 (PMID:32182622) cryo-EM groove.
- Contact sites: endosome/vacuole-mitochondria and NVJ (PMID:27280386,
  PMID:26370498), Mcp1 adaptor (PMID:28864540), competitive adaptors (PMID:30018089).
- TGN-to-PVC transport and PA/PIP binding (PMID:28122955); Golgi localization via
  Arf1 (PMID:34830155); ER-phagy (PMID:32690699); prospore membrane (PMID:22442115).

### Decisions (summary)
- Core: phospholipid transfer activity (IBA+ISS), intermembrane phospholipid transfer
  (TAS; IBA/ISS lipid transfer rows refined to it), endosome membrane and
  mitochondrial outer membrane (IBA).
- Non-core: phospholipid binding, Golgi apparatus (IEA from by-similarity text),
  mitochondrion organization, macroautophagy.
- No NEW terms: no S. pombe experimental data supports any additional term, and
  S. cerevisiae terms that PAINT did not propagate (prospore membrane, Golgi to
  endosome transport, NVJ, reticulophagy) were treated as deliberate.
