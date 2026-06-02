# BECN2 review notes

Review started from `just fetch-gene human BECN2`. The proteostasis network places BECN2 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Class 3 PI3K complex 1, direct > Class 3 PI3K complex 1 component`.

Falcon deep research was requested with `just deep-research-falcon human BECN2`, but the provider timed out after 600 seconds and no `BECN2-deep-research-falcon.md` file was produced. I am completing the review using the cached primary literature, UniProt record, GOA seed, and notes below.

BECN2 is a mammalian Beclin-family protein with two supported lysosomal degradation roles: autophagy and G-protein-coupled receptor (GPCR) turnover. The primary Cell paper reports that Beclin 2 functions in autophagy, interacts with class III PI3K complex components and Bcl-2, and has an additional lysosomal degradation role not shared by BECN1 [PMID:23954414 "functions in autophagy and interacts with class III PI3K complex components and Bcl-2" and "functions in an additional lysosomal degradation pathway"].

BECN2's GPCR role is direct and should remain core. Beclin 2 is required for ligand-induced endolysosomal degradation of several GPCRs through interaction with GASP1/GPRASP1, and heterozygous knockout mice accumulate brain cannabinoid receptor 1 [PMID:23954414 "required for ligand-induced endolysosomal degradation of several G protein-coupled receptors (GPCRs) through its interaction with GASP1" and "increased levels of brain cannabinoid 1 receptor"].

The PI3KC3-C1/autophagy-initiation connection is supported by the Cell paper, UniProt, and the ATG14 structural abstract. UniProt lists BECN2 in class III PI3K type I/type II complexes and notes interactions with ATG14, AMBRA1, UVRAG, and PIK3C3/VPS34 [file:human/BECN2/BECN2-uniprot.txt "Interacts ... with ATG14" and "Interacts with AMBRA1, UVRAG and PIK3C3/VPS34"]. The structural paper reports that ATG14 binding to BECN/Beclin homologs is essential for autophagy and that BECN2:ATG14 forms a coiled-coil heterodimer [PMID:28218432 "ATG14 binding to BECN/Beclin homologs is essential for autophagy" and "the BECN2 CCD and ATG14 CCD form a parallel, curved heterodimer"].

Mitophagy is too specific for the accessible BECN2 evidence. BECN2 has general autophagy/autophagosome assembly support, but the cached human paper and UniProt summaries do not establish a BECN2-specific mitophagy role. I will modify the mitophagy row to autophagosome assembly rather than retaining cargo-specific mitophagy.

The vacuole transport row is a yeast-style transfer and should be converted to the directly supported human endosome-to-lysosome transport/GPCR degradation role. Generic protein binding rows are not useful as molecular-function annotations; the evidence should be captured as protein-macromolecule adaptor activity, phosphatidylinositol 3-kinase binding, complex membership, and GASP1-dependent GPCR catabolism.

Curation stance:
- Core: autophagy/autophagosome assembly, class III PI3K type I/type II complex context, phosphatidylinositol 3-kinase binding, protein-macromolecule adaptor activity, endosome-to-lysosome transport, GPCR catabolic process, cytoplasm.
- Modify: mitophagy to autophagosome assembly; late endosome-to-vacuole transport to endosome-to-lysosome transport; protein-containing complex binding to adaptor activity.
- Keep as non-core: cellular response to nitrogen starvation as autophagy context.
- Mark over-annotated: generic protein binding rows.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording tied the PI3KC3-C1 interpretation to a Proteostasis Network leaf and contrasted that shared role with the BECN2-specific GPCR catabolic branch.
