# B9D2 notes

## 2026-10-05 review (PAINT, affinage)

- B9 complex: [PMID:32726168 "We here demonstrate the interaction mode of these B9D proteins to be MKS1-B9D2-B9D1 and demonstrate their interdependent localization to the TZ."]. The diffusion barrier is lost in knockouts (GPR161 absent from cilia), and ciliogenesis defects are mild.
- Meckel syndrome: [PMID:21763481 "We identified a homozygous c.301A>C (p.Ser101Arg) B9D2 mutation that segregates with MKS, affects an evolutionarily conserved residue, and is absent from controls."]
- 18 Reactome cytosol TAS rows are kept as non-core. Fifteen come from mitotic kinetochore events: Reactome's "Kinetochore [cytosol]" complex (R-HSA-375305) lists B9D2 without a literature reference (ContentService, checked 2026-10-05). It may be worth raising with Reactome.
- Gamma-tubulin binding (mouse ISS/IEA) and nucleus are by similarity only, so they are kept as non-core. Membrane and axoneme are also non-core.
- 19 GO:0005515 rows are removed under policy. The MKS1/B9D1 partners are captured by the MKS complex rows.

## 2026-10-05 revision (reviewer round 1)

- Added PMID:41165761 (J Clin Invest 2026): [PMID:41165761 "We also found that the B9 complex interacts with and anchors TMEM67 to the TZ membrane, thereby stabilizing the MKS module and maintaining the integrity of the TZ diffusion barrier."]. It also shows a pre-ciliogenesis mother-centriole role (CP110 removal), so the centrosome row is now ACCEPT.
- NEW GO:0030674 protein-macromolecule adaptor activity (IDA, PMID:32726168). B9D2 is the middle subunit of MKS1-B9D2-B9D1. MKS1 and B9D1 carry only protein binding in GOA.
- Corrected the GO:0005515 count to 19; the first history record said 20.
