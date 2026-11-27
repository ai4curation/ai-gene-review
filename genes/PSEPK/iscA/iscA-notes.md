# iscA curation notes

- Q88PK6 is a KT2440 IscA-family protein implicated in later Fe-S assembly or transfer. Its precise physiological role is condition dependent and should not be collapsed into the initial IscU scaffold step.
- *E. coli* work supports an aerobic iron-chaperone role: IscA binds iron and IscA/SufA are required for efficient cluster biogenesis under aerobic but not anaerobic conditions [PMID:20942799 "The results provide in vivo evidence that IscA may act as an iron chaperone for the biogenesis of iron-sulfur clusters in E. coli cells under aerobic conditions"].
- In vitro comparison supports delivery of IscA-bound iron to IscU under aerobic conditions [PMID:16877383 "IscA acts as an iron chaperon that recruits \"free\" iron and delivers the iron for biogenesis of iron-sulfur clusters in IscU under aerobic conditions"].
- Cytoplasm and cytosol annotations are plausible but non-core; neither is direct KT2440 localization evidence.


## Isc comparative-evidence audit (2026-11-07)

IscA (PP_0844) is a small A-type iron-sulfur cluster carrier of Pseudomonas putida KT2440. Its IscA-specific sequence signatures support transient cluster binding and transfer within the Isc maturation network. Homologs can carry different cluster types and exchange clusters with other carriers; neither an obligatory linear IscU-IscA-client route nor a unique target-protein repertoire is established for KT2440.

The target remains KT2440; no purified target assay is claimed. Specific curated HAMAP/RuleBase statements or independent NCBIfam/InterPro signatures ground the target inference. ARBA names are not used as proof. All original ordered source payloads are retained. The rows are IEA or historical NEW, not IBA; no donor-count argument, PAINT loss or new evolutionary node placement is asserted.

A genuine Falcon request failed with HTTP 403 authentication/access failure. Existing OpenScientist reports, where present, were preserved; no provider-branded replacement was fabricated. The log is `.cache/module-audit-logs/isc-20261107/psepk-consultation/falcon-iscA.log`.

### Evidence and biological limits

- [PMID:34781750] Bacterial IscA homologs are A-type cluster carriers; E. coli interactions support carrier-to-carrier handoff, while structural and biochemical studies in other bacteria demonstrate cluster coordination. Quoted support: “This suggests that the ATC-II carriers pass their Fe-S clusters to ATC-I for delivery to their final destinations”.
- [PMID:16730357] Thermosynechococcus elongatus IscA coordinates a partially exposed 2Fe-2S cluster across two protomers. Quoted support: “one partially exposed [2Fe-2S] cluster is coordinated by two conformationally distinct IscA protomers”.

### Decisions

- GO:0005737 cytoplasm: MODIFY. The existing cytosol annotation is the supported specific compartment for the small soluble IscA carrier acting with intracellular assembly machinery. This is a functional/localization inference, not direct KT2440 imaging; refine the parent to the existing part_of descendant.
- GO:0005829 cytosol: ACCEPT. The specific IscA family and soluble intracellular cluster-transfer role support cytosolic function. An inferred core location is not peripheral merely because it lacks target imaging.
- GO:0016226 iron-sulfur cluster assembly: ACCEPT. Independent IscA-specific NCBIfam/InterPro signatures support a carrier role. Comparative bacterial evidence permits alternative carrier handoffs; operon context alone does not establish an essential linear step or direct delivery to every final apoprotein.
- GO:0051536 iron-sulfur cluster binding: MODIFY. The specific IscA classification and characterized A-type carrier mechanisms support iron-sulfur cluster chaperone activity, meaning cluster binding and delivery rather than polypeptide folding. Exact donors and recipients remain target-specific gaps.
- GO:0051537 2 iron, 2 sulfur cluster binding: ACCEPT. The specific target IscA signatures support conserved cluster-binding capacity; the Thermosynechococcus IscA structure is homolog evidence, not a KT2440 structure. Retain 2Fe-2S binding without asserting exclusivity, since other IscA homologs can also carry 4Fe-4S clusters.
