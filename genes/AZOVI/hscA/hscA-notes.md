# hscA (O69221) review notes

## 2026-11-07 — comparative Isc consultation

Identity: original isc-region deposit AF010139.1, protein AAC24478.1, 619 residues. Its CDS translation exactly matches the fetched UniProt sequence. The original record identifies DJ116; the curated UniProt entries and original source record use differing strain annotations. See the shared [member map](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/member-map.yaml) for the explicit strain boundary. No Nif or alternative ferredoxin paralog was substituted.

HscA is the specialized Hsp70-family ATPase of the Azotobacter vinelandii iron-sulfur maturation machinery. Together with the J-protein HscB, it interacts with the IscU scaffold and couples ATP hydrolysis to efficient [2Fe-2S] cluster transfer to acceptor proteins. Its chaperone cycle supports cofactor-dependent protein maturation.

PMID:16964969 uses Azotobacter proteins and directly measures ATP hydrolysis coupled to enhanced cluster-transfer kinetics. HscA is not itself assigned iron-sulfur cluster chaperone activity because it does not bind/deliver the cluster directly like IscU. GO:0006457 remains UNDECIDED because transfer and cofactor acquisition do not establish the required correct-tertiary-structure endpoint. Specialization is not evidence that all folding assistance is absent. The native 2006 HscBA depletion is a paired experiment, not a separate HscA-versus-HscB requirement measurement.

Native requirement is conditional. PMID:16936042 distinguishes IscA oxygen dependence and partial low-oxygen rescue of HscBA depletion from the stronger IscS/U/Fdx requirements in those conditions. PMID:17237162 demonstrates conditional NifU-to-IscU replacement and failed tested NifS-to-IscS replacement; universal pathway or essentiality claims are therefore inappropriate.

Research provenance: configured Falcon was genuinely attempted and failed HTTP403 authentication; no provider output was written or substituted. `just paint-losses AZOVI hscA` ran, but this accession is absent from its cached family tree; no lineage-loss adjudication was possible. Full access attempts and primary source scopes are documented in the [consultation README](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/README.md). The repository publication caches remain unchanged.

### Annotation decisions

- GO:0005524 ATP binding: **ACCEPT**. ATP-dependent transfer and concomitant hydrolysis were measured using A. vinelandii HscA/HscB in PMID16964969. ATP binding is intrinsic to the directly demonstrated motor activity.
- GO:0006457 protein folding: **UNDECIDED**. GO0006457 requires assisting assembly into correct tertiary structure. PMID16964969 measures ATP-dependent cluster transfer by CD/EPR and ATP turnover, not a folding endpoint for IscU or the recipient. This is genuine specialized maturation work, but neither a general folding function nor its absence follows. Retain unresolved rather than equate cluster transfer with folding or reject the annotation merely because the chaperone is specialized.
- GO:0016226 iron-sulfur cluster assembly: **ACCEPT**. The ATP-dependent HscA/HscB reaction contributes work to cluster transfer, beyond the native depletion phenotype. Cluster synthesis on IscU and chaperone-assisted delivery are distinct steps within the overall assembly machinery.
- GO:0016887 ATP hydrolysis activity: **ACCEPT**. PMID16964969 monitors phosphate production and ATP-dependent rate enhancement using the target organism proteins. The hydrolysis activity belongs to HscA; HscB stimulates it rather than being assigned ATPase activity itself.

Core synthesis: Hydrolyzes ATP in the HscB/IscU-directed chaperone cycle that accelerates cluster delivery.

No NEW annotations or retirements were introduced. Ordered source payloads were frozen before review and checked independently after editing. Unresolved rows reflect evidence limits, not unfinished row review.


## 2026-11-07 PR6175 round1 evidence review

Replaced recycled evidence with target-organism ATP-coupled cluster transfer and curated HscB stimulation. Protein folding remains UNDECIDED: recipient maturation is not itself a tertiary-fold recovery assay. E. coli model-substrate negatives are comparative, not AZOVI measurements.

Full adjudication and fresh ontology provenance: `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/azovi-consultation/scientific-findings.md`. All ordered annotation payloads and existing row presence are preserved. No NEW, deleted or retired rows are introduced; source/provider files remain immutable. Existing Falcon attempt/failure provenance is reused.
