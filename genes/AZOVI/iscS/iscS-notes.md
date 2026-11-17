# iscS (O31269) review notes

## 2026-11-07 — comparative Isc consultation

Identity: original isc-region deposit AF010139.1, protein AAC24472.1, 404 residues. Its CDS translation exactly matches the fetched UniProt sequence. The original record identifies DJ116; the curated UniProt entries and original source record use differing strain annotations. See the shared [member map](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/member-map.yaml) for the explicit strain boundary. No Nif or alternative ferredoxin paralog was substituted.

IscS is a cytoplasmic, pyridoxal-phosphate-dependent cysteine desulfurase that mobilizes sulfur from L-cysteine through a protein-bound persulfide. It supplies sulfur to IscU for housekeeping iron-sulfur cluster biosynthesis in Azotobacter vinelandii. It is distinct from the nitrogenase-associated desulfurase NifS.

PMID:9582371 isolates the desulfurase from a nifS-deletion background, so the catalytic evidence is not an undifferentiated NifS/IscS assignment. PMID:16165131 supports sulfur delivery without requiring a covalent heterodisulfide. PMID:25447670 concerns archaeal IscS, which lacks normal desulfurase activity; its shared cluster-ligand precedent cannot be treated as native Azotobacter proof. The UniRule cluster-binding claim remains unresolved. Broader tRNA/cofactor sulfur trafficking was not tested in the native 2006 study and is not newly asserted.

Native requirement is conditional. PMID:16936042 distinguishes IscA oxygen dependence and partial low-oxygen rescue of HscBA depletion from the stronger IscS/U/Fdx requirements in those conditions. PMID:17237162 demonstrates conditional NifU-to-IscU replacement and failed tested NifS-to-IscS replacement; universal pathway or essentiality claims are therefore inappropriate.

Research provenance: configured Falcon was genuinely attempted and failed HTTP403 authentication; no provider output was written or substituted. `just paint-losses AZOVI iscS` ran, but this accession is absent from its cached family tree; no lineage-loss adjudication was possible. Full access attempts and primary source scopes are documented in the [consultation README](../../../analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/azotobacter-consultation/README.md). The repository publication caches remain unchanged.

### Annotation decisions

- GO:0005515 protein binding: **MODIFY**. PMID18562278 measures IscS cysteine desulfurization as well as complex formation. The functional sulfur-delivery activity is more informative than generic protein binding and is independently established in PMID9582371; this refinement does not deny the interaction.
- GO:0005737 cytoplasm: **ACCEPT**. The characterized soluble enzyme and its intracellular scaffold interaction support cytoplasmic localization, consistent with the curated UniRule assignment. No organelle or membrane localization is inferred.
- GO:0030170 pyridoxal phosphate binding: **ACCEPT**. Purification of native IscS established its PLP-containing homodimeric state in PMID9582371. Cofactor binding is integral to the cysteine desulfurase activity.
- GO:0031071 cysteine desulfurase activity: **ACCEPT**. The activity was measured for protein purified from an A. vinelandii nifS deletion strain (PMID9582371). Both experimental and electronic assertions describe the same established function.
- GO:0031071 cysteine desulfurase activity: **ACCEPT**. The activity was measured for protein purified from an A. vinelandii nifS deletion strain (PMID9582371). Both experimental and electronic assertions describe the same established function.
- GO:0044571 [2Fe-2S] cluster assembly: **ACCEPT**. PMID10891064 directly follows IscS-mediated cluster assembly. IscS performs sulfur mobilization rather than merely being required genetically, satisfying participation in this process.
- GO:0051537 2 iron, 2 sulfur cluster binding: **UNDECIDED**. UniRule UR000084057/HAMAP MF_00331 annotates C328 as a persulfide ligand shared with IscU. The native PMID18562278 complex contains a substituted IscU and does not locate cluster ligands. The identifiable structural precedent in PMID25447670 concerns catalytically divergent Archaeoglobus fulgidus IscS with mutant IscU. This does not establish native A. vinelandii IscS cluster binding, nor exclude a transient shared intermediate. Retain unresolved rather than call the source mapping demonstrably false.

Core synthesis: Mobilizes cysteine sulfur through a PLP-dependent persulfide intermediate and supplies the IscU assembly scaffold.

No NEW annotations or retirements were introduced. Ordered source payloads were frozen before review and checked independently after editing. Unresolved rows reflect evidence limits, not unfinished row review.


## 2026-11-07 PR6175 round1 evidence review

Assigned row-specific purified-enzyme, PLP, curated FUNCTION and HAMAP localization evidence. The IscU-IscS complex and divergent archaeal ligand precedent do not resolve native AZOVI IscS cluster ligation.

Full adjudication and fresh ontology provenance: `analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/azovi-consultation/scientific-findings.md`. All ordered annotation payloads and existing row presence are preserved. No NEW, deleted or retired rows are introduced; source/provider files remain immutable. Existing Falcon attempt/failure provenance is reused.
