# fdx (O69222) review notes

## 2026-11-07 — comparative Isc consultation

Identity: original isc-region deposit AF010139.1, protein AAC24477.1, 113 residues. Its CDS translation exactly matches the fetched UniProt sequence. The original record identifies DJ116; the curated UniProt entries and original source record use differing strain annotations. See the shared [member map](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/member-map.yaml) for the explicit strain boundary. No Nif or alternative ferredoxin paralog was substituted.

Fdx, also characterized as FdIV or FdxD, is a monomeric, redox-active [2Fe-2S] ferredoxin encoded in the Azotobacter vinelandii housekeeping isc operon. Native Fdx is required for efficient iron-sulfur protein maturation under standard growth conditions. Its exact physiological electron-transfer partner in this organism remains unresolved. It is distinct from ferredoxin I encoded by fdxA.

PMID:10542283 identifies native FdIV by N-terminal sequence as the isc-operon fdxD product and measures one [2Fe-2S] cluster per monomer, with a -344 mV reduction potential. This supports electron-transfer capacity. In PMID:16964969 apo-Fdx receives a cluster: this is not an experiment demonstrating electron donation during assembly. The native genetic requirement does not identify its electron partner. E. coli Fdx persulfide-reduction evidence (PMID:39870763) provides a mechanistic hypothesis, not a target-organism measurement. Neither a defined electron transport chain nor P450 coupling follows from the ferredoxin fold. No NEW assembly BP was added solely from necessity.

Native requirement is conditional. PMID:16936042 distinguishes IscA oxygen dependence and partial low-oxygen rescue of HscBA depletion from the stronger IscS/U/Fdx requirements in those conditions. PMID:17237162 demonstrates conditional NifU-to-IscU replacement and failed tested NifS-to-IscS replacement; universal pathway or essentiality claims are therefore inappropriate.

Research provenance: configured Falcon was genuinely attempted and failed HTTP403 authentication; no provider output was written or substituted. `just paint-losses AZOVI fdx` ran, but this accession is absent from its cached family tree; no lineage-loss adjudication was possible. Full access attempts and primary source scopes are documented in the [consultation README](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/README.md). The repository publication caches remain unchanged.

### Annotation decisions

- GO:0005829 cytosol: **ACCEPT**. Native purification and its isc-operon identity support the inferred cytosolic assignment. No mitochondrial or membrane electron-transport localization is asserted.
- GO:0009055 electron transfer activity: **ACCEPT**. The native protein has a measured reduction potential of -344 mV and the expected [2Fe-2S](2+/+) redox states (PMID10542283), supporting electron-transfer capacity. This does not identify its physiological electron acceptor.
- GO:0022900 electron transport chain: **UNDECIDED**. PMID10542283 establishes a redox-active ferredoxin and PMID16936042 establishes a native ISC requirement. Neither identifies a series of physiological electron carriers. In PMID16964969 Fdx is a cluster recipient, not an electron donor. The specific TreeGrafter placement could not be traced because this accession is absent from the cached tree.
- GO:0051536 iron-sulfur cluster binding: **MODIFY**. Native FdIV spectroscopy and composition directly establish cluster type, so refine generic Fe-S binding to GO0051537, already present in this review.
- GO:0051537 2 iron, 2 sulfur cluster binding: **ACCEPT**. UV/visible, CD and EPR studies in PMID10542283 identify the cofactor and its redox properties. This activity is directly supported rather than inferred solely from domain similarity.
- GO:0140647 P450-containing electron transport chain: **MARK_AS_OVER_ANNOTATED**. IPR001055/IPR018298 recognize the bacterial ferredoxin class shared with P450 redox partners; that fold does not identify a cytochrome P450 recipient. Native FdIV identity, redox characterization and ISC-dependent phenotype support a different characterized context. No direct P450 electron-transfer evidence was found, but an uncharacterized secondary role is not experimentally excluded.

Core synthesis: Supports electron-transfer capacity through the redox-active [2Fe-2S] cofactor of native FdIV.

No NEW annotations or retirements were introduced. Ordered source payloads were frozen before review and checked independently after editing. Unresolved rows reflect evidence limits, not unfinished row review.


## 2026-11-07 PR6175 round1 evidence review

Replaced recycled evidence with the native FdIV spectroscopy, redox and sequence-identity clauses. Cytosolic localization remains explicitly inferred; native ISC electron-donor reconstitution is not claimed.

Full adjudication and fresh ontology provenance: `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/azovi-consultation/scientific-findings.md`. All ordered annotation payloads and existing row presence are preserved. No NEW, deleted or retired rows are introduced; source/provider files remain immutable. Existing Falcon attempt/failure provenance is reused.
