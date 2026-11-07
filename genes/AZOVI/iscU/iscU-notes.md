# iscU (O31270) review notes

## 2026-11-07 — comparative Isc consultation

Identity: original isc-region deposit AF010139.1, protein AAC24473.1, 128 residues. Its CDS translation exactly matches the fetched UniProt sequence. The original record identifies DJ116; the curated UniProt entries and original source record use differing strain annotations. See the shared [member map](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/member-map.yaml) for the explicit strain boundary. No Nif or alternative ferredoxin paralog was substituted.

IscU is a soluble iron-sulfur cluster assembly scaffold in Azotobacter vinelandii. It accepts sulfur from IscS, binds nascent clusters, and donates clusters to recipient proteins. HscA and HscB accelerate [2Fe-2S] transfer from IscU through an ATP-dependent cycle. Its housekeeping function can be partially replaced by NifU under particular expression or oxygen conditions.

PMID:18562278 validates native scaffold occupancy and reversible association with IscS; its persistent complex uses a substituted scaffold. PMID:10891064 shows [2Fe-2S] and [4Fe-4S] in vitro; the former is observed natively in the 2008 study, whereas native accumulation of the latter was not demonstrated. PMID:16964969 directly supports cluster delivery, satisfying GO:0140132. The iron-ion claim uses a separate positive comparative experiment (E. coli PMID:39870763), not just iron already present in a cluster. Native and E. coli IscU are both 128 residues and retain C37/D39/C63/H105/C106; this supports a conserved-function inference without proving native loading order or donor. The local source sequences and the comparison are checked by the consultation checker.

Native requirement is conditional. PMID:16936042 distinguishes IscA oxygen dependence and partial low-oxygen rescue of HscBA depletion from the stronger IscS/U/Fdx requirements in those conditions. PMID:17237162 demonstrates conditional NifU-to-IscU replacement and failed tested NifS-to-IscS replacement; universal pathway or essentiality claims are therefore inappropriate.

Research provenance: configured Falcon was genuinely attempted and failed HTTP403 authentication; no provider output was written or substituted. `just paint-losses AZOVI iscU` ran, but this accession is absent from its cached family tree; no lineage-loss adjudication was possible. Full access attempts and primary source scopes are documented in the [consultation README](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/README.md). The repository publication caches remain unchanged.

### Annotation decisions

- GO:0005506 iron ion binding: **ACCEPT**. The A. vinelandii scaffold retains C37, D39, C63, H105 and C106 at the corresponding E. coli IscU positions. PMID39870763 directly demonstrates pre-sulfur iron loading in reconstituted E. coli ISC, providing positive comparative support alongside native A. vinelandii scaffold biochemistry in PMID10891064/18562278. This is a conserved-function inference, not a native apo-Fe(II) binding measurement; cluster-bound iron alone is not the evidence, and native loading order and iron donor remain unresolved.
- GO:0005515 protein binding: **MODIFY**. PMID18562278 establishes the native scaffold cycle and PMID16964969 directly demonstrates cluster donation to apoferredoxin. GO0140132 describes binding a cluster and delivering it to an acceptor, making the functional refinement supported beyond interaction alone.
- GO:0005737 cytoplasm: **ACCEPT**. Native intracellular IscU forms and its soluble sulfur-delivery partnership support the cytoplasmic claim. The electronic localization is compatible with the experimentally characterized machinery.
- GO:0016226 iron-sulfur cluster assembly: **ACCEPT**. IscU binds the assembly intermediates and supplies the platform for sulfur/iron incorporation and downstream donation. PMID10891064 demonstrates both [2Fe-2S] and [4Fe-4S] products in vitro; PMID18562278 establishes native [2Fe-2S] occupancy.
- GO:0051536 iron-sulfur cluster binding: **MODIFY**. The cluster-binding claim is true, but directly demonstrated delivery to apoferredoxin in PMID16964969 supports the more informative descendant GO0140132 iron-sulfur cluster chaperone activity. The refinement also covers the generic protein-interaction row.

Core synthesis: Scaffolds nascent Fe-S clusters and delivers them to recipient proteins.

No NEW annotations or retirements were introduced. Ordered source payloads were frozen before review and checked independently after editing. Unresolved rows reflect evidence limits, not unfinished row review.
