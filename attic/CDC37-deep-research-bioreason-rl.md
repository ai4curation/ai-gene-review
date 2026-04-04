# BioReason Chat Export
*Exported on March 22, 2026 at 02:07 AM*

---

**Organism:** Saccharomyces cerevisiae

**Sequence:**
```
MAIDYSKWDKIELSDDSDVEVHPNVDKKSFIKWKQQSIHEQRFKRNQDIKNLETQVDMYSHLNKRVDRILSNLPESSLTDLPAVTKFLNANFDKMEKSKGENVDPEIATYNEMVEDLFEQLAKDLDKEGKDSKSPSLIRDAILKHRAKIDSVTVEAKKKLDELYKEKNAHISSEDIHTGFDSSFMNKQKGGAKPLEATPSEALSSAAESNILNKLAKSSVPQTFIDFKDDPMKLAKETEEFGKISINEYSKSQKFLLEHLPIISEQQKDALMMKAFEYQLHGDDKMTLQVIHQSELMAYIKEIYDMKKIPYLNPMELSNVINMFFEKVIFNKDKPMGKESFLRSVQEKFLHIQKRSKILQQEEMDESNAEGVETIQLKSLDDSTELEVNLPDFNSKDPEEMKKVKVFKTLIPEKMQEAIMTKNLDNINKVFEDIPIEEAEKLLEVFNDIDIIGIKAILENEKDFQSLKDQYEQDHEDATMENLSLNDRDGGGDNHEEVKHTADTVD
```

### Thinking Trace
I begin by dissecting the InterPro architecture. The polypeptide is assigned to IPR004918 (Cdc37 family, residues 1–474), establishing a dedicated co-chaperone scaffold. Its N-terminus is organized by IPR013855 (Cdc37, N-terminal domain, residues 2–183), a module typically used to engage client proteins—particularly unstable kinases. The central region carries IPR013874 (Cdc37, Hsp90 binding, residues 186–371), reinforced by IPR038189 (Cdc37, Hsp90-binding domain superfamily, residues 232–365). This central core causally defines the protein’s role: it binds and positions Hsp90 to form a productive chaperone assembly. The C-terminus is structured by IPR013873 (Cdc37, C-terminal domain, residues 388–491), a region that commonly stabilizes the co-chaperone fold and mediates additional client or cofactor contacts. The ordered layout—N-terminal client-capture domain, central Hsp90-binding engine, and C-terminal stabilizer—creates a tri-partite machine that recruits specific substrates and couples them to Hsp90-dependent folding cycles.

From this architecture, the molecular function resolves as selective protein binding. The N-terminal domain confers affinity for labile client proteins, while the central module binds Hsp90; together they enforce high-avidity interactions characteristic of co-chaperone assemblies. This supports protein binding (GO:0005515) as the operative molecular function, with binding specificity arising from coordinated recognition of both chaperone and client.

The biological process follows directly: by tethering kinase-like clients to an Hsp90-centered machine, this co-chaperone drives chaperone-mediated folding and maturation of metastable proteins. This mechanism underlies protein folding (GO:0006457), ensuring that clients attain and maintain their active conformations required for signaling and cell-cycle control.

Cellular placement is inferred from function and modularity. Such chaperone-cofactor systems operate where nascent and stress-labile proteins accumulate and where signaling hubs reside—predominantly the cytosol. The absence of transmembrane features and the soluble, multi-interface architecture point to a cytosolic environment, aligning with cytosol (GO:0005829) as the most parsimonious cellular component.

Mechanistically, the protein acts as a targeting and stabilizing hub: the N-terminal domain captures kinase-class clients; the central Hsp90-binding region docks Hsp90 and aligns ATP-driven conformational cycles; and the C-terminal domain consolidates the assembly for efficient folding. This suggests transient assemblies with Hsp90 and the Hsp70 system, and preferential handoff to kinase clients. I therefore hypothesize interactions with the core Hsp90/Hsp70 machinery and kinase substrates, forming a dynamic chaperone module that stabilizes and matures metastable signaling proteins in the cytosol.

### Functional Summary
A soluble co-chaperone that assembles with the Hsp90 system to stabilize and mature metastable client proteins—especially kinase-class substrates—in baker’s yeast. Its N-terminal module captures labile clients, a central region docks Hsp90 to drive ATP-dependent folding cycles, and the C-terminal domain consolidates the assembly. By orchestrating chaperone-mediated folding in the cytosol, it promotes the attainment and maintenance of functional conformations central to cellular signaling and proteostasis.

### UniProt Summary
Co-chaperone that binds to the molecular chaperone Hsp90 and promotes the maturation of specific Hsp90 client proteins.

### InterPro Domains
- **Cdc37** (`IPR004918`, family) — residues 1-474
- **Cdc37, N-terminal domain** (`IPR013855`, domain) — residues 2-183
- **Cdc37, Hsp90 binding** (`IPR013874`, domain) — residues 186-371
- **Cdc37, Hsp90-binding domain superfamily** (`IPR038189`, homologous_superfamily) — residues 232-365
- **Cdc37, C-terminal** (`IPR013873`, domain) — residues 388-491

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), protein binding (`GO:0005515`), unfolded protein binding (`GO:0051082`)

**Biological Process:** biological_process (`GO:0008150`), biological regulation (`GO:0065007`), positive regulation of biological process (`GO:0048518`), response to stimulus (`GO:0050896`), regulation of biological process (`GO:0050789`), cellular process (`GO:0009987`), signaling (`GO:0023052`), response to abiotic stimulus (`GO:0009628`), regulation of biological quality (`GO:0065008`), positive regulation of signaling (`GO:0023056`), response to chemical (`GO:0042221`), positive regulation of response to stimulus (`GO:0048584`), cell cycle process (`GO:0022402`), regulation of cellular process (`GO:0050794`), cell cycle (`GO:0007049`), regulation of response to stimulus (`GO:0048583`), cellular response to stimulus (`GO:0051716`), cellular component organization or biogenesis (`GO:0071840`), regulation of signaling (`GO:0023051`), response to stress (`GO:0006950`), microtubule-based process (`GO:0007017`), cell communication (`GO:0007154`), signal transduction (`GO:0007165`), positive regulation of cellular process (`GO:0048522`), regulation of cell cycle (`GO:0051726`), positive regulation of signal transduction (`GO:0009967`), cellular response to environmental stimulus (`GO:0104004`), cellular component biogenesis (`GO:0044085`), intracellular signal transduction (`GO:0035556`), spindle pole body organization (`GO:0051300`), regulation of cell communication (`GO:0010646`), cellular response to chemical stimulus (`GO:0070887`), cellular response to stress (`GO:0033554`), cellular response to abiotic stimulus (`GO:0071214`), regulation of signal transduction (`GO:0009966`), response to osmotic stress (`GO:0006970`), cellular component organization (`GO:0016043`), positive regulation of cell communication (`GO:0010647`), microtubule cytoskeleton organization (`GO:0000226`), microtubule organizing center organization (`GO:0031023`), regulation of protein stability (`GO:0031647`), cellular response to chemical stress (`GO:0062197`), cellular response to osmotic stress (`GO:0071470`), MAPK cascade (`GO:0000165`), osmosensory signaling pathway (`GO:0007231`), positive regulation of intracellular signal transduction (`GO:1902533`), protein stabilization (`GO:0050821`), organelle organization (`GO:0006996`), regulation of intracellular signal transduction (`GO:1902531`), stress-activated protein kinase signaling cascade (`GO:0031098`), cellular component assembly (`GO:0022607`), cytoskeleton organization (`GO:0007010`), regulation of MAPK cascade (`GO:0043408`), stress-activated MAPK cascade (`GO:0051403`), positive regulation of MAPK cascade (`GO:0043410`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), cytoplasm (`GO:0005737`), intracellular anatomical structure (`GO:0005622`)

---
*Generated by [BioReason](https://bioreason.net)*
