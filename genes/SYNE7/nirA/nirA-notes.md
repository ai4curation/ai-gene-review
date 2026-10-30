# nirA review notes

## 2026-10-27: PCC 7942 native-system review

Reviewed all 4 seeded annotation rows for P39661, NCBITaxon:1140 (PCC 7942). Original annotation fields and both raw files were snapshotted before editing and retained. No NEW rows were introduced.

NirA is the ferredoxin-dependent assimilatory nitrite reductase of Synechococcus elongatus PCC 7942. It reduces nitrite to ammonium using six electrons supplied by reduced ferredoxin. Its conserved iron-sulfur/siroheme architecture supports a coupled [4Fe-4S]-siroheme catalytic center, completing the reductive part of nitrate assimilation before ammonium incorporation into organic nitrogen.

One normal Falcon deep-research attempt with perplexity-lite fallback failed; no synthetic provider file was created. Manual primary-source review supplies the evidence below. Normal acquisition logs are in `.cache/module-audit-logs/nitrate-syne7-review/`.

Family grounding: target UniProt membership is PTHR32439:SF0, official PANTHER label **FERREDOXIN--NITRITE REDUCTASE, CHLOROPLASTIC**, checked against `interpro/panther/panther.obo`. Broad family labels do not determine substrate specificity; a chloroplastic family name does not place a cyanobacterial protein in a chloroplast.

- [PMID:8490140 Nitrite reductase gene from Synechococcus sp. PCC 7942: homology between cyanobacterial and higher-plant nitrite reductases.] Primary PCC 7942 nir sequence study. Abstract read; supports gene identity and conserved Fe-S/siroheme architecture by comparison, not direct measurement of cofactor occupancy or donor kinetics in purified PCC 7942 NirA.
  The PCC 7942 nitrite reductase gene was identified and sequenced. Supporting text: "The gene encoding nitrite reductase (nir) from the cyanobacterium Synechococcus sp. PCC 7942 has been identified and sequenced."
  Sequence conservation supports a coupled [4Fe-4S]-siroheme center. Supporting text: "Identities found at positions corresponding to those amino acids which in the above-mentioned proteins hold the Fe4S4-siroheme active center suggest that nitrite reductase from Synechococcus bears an active site much alike that present in those reductases."
- [url:https://idus.us.es/bitstream/handle/11441/129668/Involvement%20of%20the%20C-terminal%20Domain.pdf?sequence=1 Involvement of the C-terminal Domain of an ATP-binding Subunit in the Regulation of the ABC-type Nitrate/Nitrite Transporter of the Cyanobacterium Synechococcus sp. Strain PCC 7942*] Full-text copy of PMID:9341163 from the author institution. R2-SPc is a PCC 7942 derivative cured of pUH24. Transport was separated from reduction using narB mutants and intracellular nitrate measurements. Table I measures native NR/NiR with artificial reduced methyl viologen; it does not establish a native ferredoxin partner.
  Deletion/complementation establishes that NrtC itself is essential for nitrate transport. Supporting text: "NrtC itself is essential for nitrate transport."
  The truncated NrtC remains associated with the cytoplasmic membrane. Supporting text: "These findings confirmed the expression of the N-termi- nal portion of NrtC and its incorporation into the cytoplasmic membrane in NC2."
  Native-cell nitrate and nitrite reductase activities were assayed with an artificial electron donor. Supporting text: "NR and NiR activities were determined at 30 °C, using toluene-permeabilized cells with dithionite-reduced methylviolo- gen as the electron donor"

Annotation decisions:

- GO:0016491 oxidoreductase activity: MODIFY. PCC 7942 nir sequencing identifies the nitrite reductase and its conserved catalytic architecture; native-cell assays verify nitrite reductase activity, while the verified ferredoxin-NiR classification supports the donor-specific enzyme identity. GO:0048307 is already present and is the supported specific descendant. Native assays in PMID:9341163 used methyl viologen, so they are not claimed as a direct physiological-donor test.
- GO:0020037 heme binding: ACCEPT. The target sequence study identifies the conserved Fe4S4-siroheme architecture (PMID:8490140), corroborated by the target InterPro iron-sulfur/siroheme signatures. This is a homology-supported cofactor assignment rather than a claim of direct cofactor analysis of PCC 7942 NirA. Heme binding is retained because no more specific siroheme-binding GO term was established by the ontology lookup.
- GO:0048307 ferredoxin-nitrite reductase activity: ACCEPT. The sequenced PCC 7942 nir product, nitrite reductase assays in native PCC 7942-derived cells and the verified ferredoxin-NiR family assignment jointly support this catalytic identity. The original sequence paper does not directly measure donor specificity or cofactor occupancy, and the native assay used methyl viologen; these limits are kept explicit. This is distinct from the NADH-linked heterotrophic NirBD system and from Anabaena NirB accessory maturation proteins.
- GO:0051536 iron-sulfur cluster binding: MODIFY. The conserved target architecture described in PMID:8490140 supports the four-iron/four-sulfur cluster coupled to siroheme. Refine the general iron-sulfur binding term to GO:0051539. The evidence is sequence-based conservation, not direct target EPR or metal-stoichiometry measurement.

The primary sequence study is not a purified-enzyme donor assay. Native NiR measurements in the NrtC study use reduced methyl viologen. Target donor specificity rests on synthesis of gene identity, enzyme class and homologous architecture; Anabaena NirB maturation-factor phenotypes are not substituted for evidence about PCC 7942 NirA.
