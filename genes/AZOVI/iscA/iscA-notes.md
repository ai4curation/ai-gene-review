# iscA (O31271) review notes

## 2026-11-07 — comparative Isc consultation

Identity: original isc-region deposit AF010139.1, protein AAC24474.1, 107 residues. Its CDS translation exactly matches the fetched UniProt sequence. The original record identifies DJ116; the curated UniProt entries and original source record use differing strain annotations. See the shared [member map](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/member-map.yaml) for the explicit strain boundary. No Nif or alternative ferredoxin paralog was substituted.

IscA is an A-type iron-sulfur assembly accessory protein encoded in the Azotobacter vinelandii housekeeping isc operon. Its conserved cysteines and A-type protein domains support a metal/cluster-handling role. Native depletion compromises aconitase maturation and becomes lethal under elevated oxygen, while its precise chemical contribution remains unresolved. This IscA is distinct from the NifIscA paralog encoded in the nitrogen-fixation region.

The individual housekeeping iscA phenotype is supported by PMID:16936042: elevated-oxygen dependence, a small reproducible aconitase defect and conserved cysteine dependence. The 2006 authors explicitly leave the chemical role open. These findings and independent A-type classifications support broad Fe-S handling, but do not choose cluster delivery versus iron delivery or repair, nor establish a specific cluster nuclearity. PMID:11705400 and PMID:23003563 are often retrieved for Azotobacter IscA, but their abstracts identify the separate NifIscA protein; their biochemical results were not imported as O31271 measurements. No new chemical activity was proposed.

Native requirement is conditional. PMID:16936042 distinguishes IscA oxygen dependence and partial low-oxygen rescue of HscBA depletion from the stronger IscS/U/Fdx requirements in those conditions. PMID:17237162 demonstrates conditional NifU-to-IscU replacement and failed tested NifS-to-IscS replacement; universal pathway or essentiality claims are therefore inappropriate.

Research provenance: configured Falcon was genuinely attempted and failed HTTP403 authentication; no provider output was written or substituted. `just paint-losses AZOVI iscA` ran, but this accession is absent from its cached family tree; no lineage-loss adjudication was possible. Full access attempts and primary source scopes are documented in the [consultation README](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/README.md). The repository publication caches remain unchanged.

### Annotation decisions

- GO:0005737 cytoplasm: **MODIFY**. The protein lacks a membrane-targeting architecture and belongs to the intracellular assembly system. The more precise cytosol annotation is already present; refine the broad cytoplasm row to that supported location.
- GO:0005829 cytosol: **ACCEPT**. The soluble A-type domain architecture and native ISC function support cytosol as a localization inference. This is not a fractionation measurement.
- GO:0016226 iron-sulfur cluster assembly: **ACCEPT**. PMID16936042 establishes impaired aconitase maturation and an elevated-oxygen requirement. Combined with its conserved A-type cluster-handling domain, this supports an assembly accessory role. It does not establish IscA as the obligatory initial scaffold or universally essential under ambient oxygen.
- GO:0051536 iron-sulfur cluster binding: **ACCEPT**. Independent InterPro IPR011302/IPR016092 and NCBIfam TIGR02011 classifications identify a conserved IscA cluster-handling protein; native conserved-cysteine dependence in PMID16936042 supports the functional site. Retain this broad inferred activity without treating NifIscA measurements as assays of O31271. The exact native ligand and delivery mechanism remain unresolved.
- GO:0051537 2 iron, 2 sulfur cluster binding: **UNDECIDED**. The A-type family supports broad Fe-S cluster handling, but native genetic cysteine dependence does not identify cluster nuclearity. Biochemical work often cited as A. vinelandii IscA assays the separate NifIscA paralog. The TreeGrafter PTN002225865 leaf was absent from the cached tree, so its source placement could not resolve this extra specificity.

Core synthesis: Provides an inferred A-type cluster-handling activity that supports native Fe-S protein maturation, particularly during oxygen challenge.

No NEW annotations or retirements were introduced. Ordered source payloads were frozen before review and checked independently after editing. Unresolved rows reflect evidence limits, not unfinished row review.
