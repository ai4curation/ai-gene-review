# DPYSL3 review notes


## 2026-09-20 full-gene IBA re-review

All 56 annotations assessed, including paired ortholog-derived annotations for actin bundling/crosslinking, projections/migration, binding partners and cellular locations; catalytic/negative IBA claims; all interaction and Reactome rows.

No target-specific OpenScientist report was present. Existing DPYSL2 cyclic-amide report was used explicitly as family-level comparative evidence, together with the DPYSL3 UniProt metal-cofactor caution. PMID:28044206 is direct CRMP2 structural evidence and PMID:23373749 a CRMP5 negative assay; neither is described as a direct DPYSL3 enzyme assay. Specific catalytic rejections remain.

All generic protein binding rows were normalized to REMOVE as uninformative without denying measured interactions. Both self-binding rows now ACCEPT because homotetramer assembly is a conserved CRMP structural feature. Established actin bundling, filamin interaction, growth-cone/cytoplasmic location and projection-regulation functions remain accepted; secondary phosphoprotein/SH3/chondroitin binding, extracellular and synaptic/vesicle contexts remain non-core.

PMID:25358863 title/abstract emphasize CRMP1, but the UniProt evidence explicitly includes FLNA interaction for DPYSL3. The experimental source was retained rather than alleging misattribution from an abstract-only cache. Detailed ortholog functions were not rejected merely because a separate human assay was absent.

Verified the proximate IBA PANTHER nodes from cached WITH/FROM fields and revised structured propagation metadata to match final decisions; no relationship-field reasoning, donor-count argument, or invented topology reconstruction was used.
