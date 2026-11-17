# hscB (O69220) review notes

## 2026-11-07 — comparative Isc consultation

Identity: original isc-region deposit AF010139.1, protein AAC24479.1, 171 residues. Its CDS translation exactly matches the fetched UniProt sequence. The original record identifies DJ116; the curated UniProt entries and original source record use differing strain annotations. See the shared [member map](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/member-map.yaml) for the explicit strain boundary. No Nif or alternative ferredoxin paralog was substituted.

HscB is a J-domain co-chaperone that activates HscA and supports IscU-dependent iron-sulfur protein maturation in Azotobacter vinelandii. HscB participates with HscA and IscU in an ATP-dependent cluster-transfer system, promoting delivery of scaffold-bound [2Fe-2S] clusters to acceptor proteins.

PMID:16964969 supports HscB stimulation of HscA and the requirement for HscB in efficient ATP-dependent cluster transfer. Hydrolysis belongs to HscA; HscB is the activator. HscB complex membership is functional participation in a transfer assembly, not evidence that every subunit in the human example of GO:1990230 occurs in bacteria. GO:0006457 remains UNDECIDED because transfer is not a measured folding endpoint. A domain name containing oligomerization does not establish the separate oligomerization BP. The chaperone-specific binding annotation describes the documented partnership with specialized HscA, without independently assigning a generic foldase activity.

Native requirement is conditional. PMID:16936042 distinguishes IscA oxygen dependence and partial low-oxygen rescue of HscBA depletion from the stronger IscS/U/Fdx requirements in those conditions. PMID:17237162 demonstrates conditional NifU-to-IscU replacement and failed tested NifS-to-IscS replacement; universal pathway or essentiality claims are therefore inappropriate.

Research provenance: configured Falcon was genuinely attempted and failed HTTP403 authentication; no provider output was written or substituted. `just paint-losses AZOVI hscB` ran, but this accession is absent from its cached family tree; no lineage-loss adjudication was possible. Full access attempts and primary source scopes are documented in the [consultation README](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/README.md). The repository publication caches remain unchanged.

### Annotation decisions

- GO:0001671 ATPase activator activity: **ACCEPT**. PMID16964969 measures HscB-dependent stimulation of HscA hydrolysis and enhanced transfer; the J-domain and curated HscA interaction agree. This is activation of another enzyme, not intrinsic HscB ATP hydrolysis.
- GO:0006457 protein folding: **UNDECIDED**. GO0006457 requires assisting assembly into correct tertiary structure. PMID16964969 measures ATP-dependent cluster transfer by CD/EPR and ATP turnover, not a folding endpoint for IscU or the recipient. This is genuine specialized maturation work, but neither a general folding function nor its absence follows. Retain unresolved rather than equate cluster transfer with folding or reject the annotation merely because the chaperone is specialized.
- GO:0044571 [2Fe-2S] cluster assembly: **ACCEPT**. The purified A. vinelandii system directly demonstrates HscB-dependent enhancement of cluster transfer. This supports participation in cluster assembly/maturation through its cofactor role, while distinguishing transfer from initial synthesis on IscU.
- GO:0051087 protein-folding chaperone binding: **ACCEPT**. The J-protein-HscA partnership is functionally established in the reconstituted system and conserved domain assignment. Retain the informative chaperone-specific binding term; it describes a core partnership rather than generic protein association.
- GO:0051259 protein complex oligomerization: **MARK_AS_OVER_ANNOTATED**. IPR009073/IPR036386 identify a domain historically named for oligomerization, but the relevant positive evidence establishes HscA activation and IscU-assisted cluster transfer. Participation in a transient heterocomplex is not itself evidence that HscB drives formation of protein oligomers. Broader oligomerization activity remains unsupported rather than experimentally disproved.
- GO:1990230 iron-sulfur cluster transfer complex: **ACCEPT**. The GO1990230 definition permits a protein complex that catalyzes cluster transfer; its human example does not require bacterial HscB to share mitochondrial partners. The target-organism HscA/HscB/IscU transfer system meets this function, although its native occupancy and lifetime were not measured.

Core synthesis: Activates HscA ATP hydrolysis to promote transfer of IscU-bound clusters to recipient proteins.

No NEW annotations or retirements were introduced. Ordered source payloads were frozen before review and checked independently after editing. Unresolved rows reflect evidence limits, not unfinished row review.


## 2026-11-07 PR6175 round1 evidence review

Replaced recycled evidence with target-system interaction and ATPase stimulation. Folding remains UNDECIDED, while chaperone binding is compatible with the current GO definition including transport. Oligomerization remains mapping-specific overannotation, not a measured negative.

Full adjudication and fresh ontology provenance: `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/azovi-consultation/scientific-findings.md`. All ordered annotation payloads and existing row presence are preserved. No NEW, deleted or retired rows are introduced; source/provider files remain immutable. Existing Falcon attempt/failure provenance is reused.
