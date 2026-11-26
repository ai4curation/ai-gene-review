# E. coli ManXYZ source and construct assessment

Read on 2026-11-07. Original publication/provider/UniProt caches remain unchanged. Full acquired HTML/PDF/extracted text remains in ignored cache; source-access.json records URLs, status and hashes. Existing Falcon reports were read as literature leads, not substituted for primary evidence.

## PMID:31209249 — structure versus coupled chemistry

Official full article: https://pmc.ncbi.nlm.nih.gov/articles/PMC6796895/?report=xml . Publisher supplementary methods: https://static-content.springer.com/esm/art%3A10.1038%2Fs41422-019-0194-z/MediaObjects/41422_2019_194_MOESM1_ESM.pdf . The protected publication extraction omits several main-text paragraphs; the external complete article and supplement were read without refreshing it.

Exact primary excerpts:

> Each protomer is composed of a ManY and ManZ

> CoreY and CoreZ clamp the substrate to form the Core domain

> The mannose transporter of E. coli has a broad substrate specificity, including glucose, mannose, fructose, glucosamine, N-acetylglucosamine, and N-acetylmannosamine

> The C6 hydroxyl on the substrate can be phosphorylated by IIB

Exact supplementary excerpts:

> Overexpression of ManYZ was induced in E. coli knock out BL21(DE3)

> Liposomes without protein were tested as a negative control.

The inward-facing ManYZ structure is a trimer of ManY/ManZ protomers (3:3 membrane subunits), not a measured complete ManXYZ stoichiometry. Both proteins contribute the substrate-binding core. The supplement measures mannose counterflow in reconstituted ManYZ proteoliposomes: 0.6 micromolar external radiolabel, 15 minutes, 25 degrees C, protein-free liposome control. It does not reconstitute the complete ManX/HPr/EI/PEP reaction. The construct-expression host is knockout BL21(DE3). Official PDB 6K1H entity1 equals frozen P69805/ManZ (283 residues); entity2 equals frozen P69801/ManY (266 residues) plus His8. The deposited source labels are MG1655 and K-12 respectively; this sequence bridge is distinct from calling the BL21 expression experiment native K-12 physiology. Identity/results.json contains the independently checked exact comparisons.

## PMID:2681202 and PMID:8262947 — ManX chemistry

Protected abstracts explicitly report transfer between domains on the same ManX subunit and between different dimer subunits; separated domains also support transfer in1989. HPr transfers to EIIA His10, then EIIA transfers to EIIB His175, which donates to sugar with membrane partners. These statements establish catalytic ManX activity without asserting ManX-alone transmembrane transport. Dimerization is directly established by1985/1989 studies. The accessible1993 abstract does not establish the old review claim that H10C abolishes dimerization; that claim is omitted, without asserting the opposite.

## PMID:2951378, PMID:2999119 and historical nomenclature

Protected abstracts directly distinguish sugar phosphorylation (all three subunits) from lambda DNA penetration (membrane components sufficient). ManX is IIIMan/ptsL; the1985 IIMan preparation predates the resolved ManY/ManZ nomenclature and cannot simply be relabeled purified ManZ. The1987 article assigns II-PMan/ManY and II-MMan/ManZ explicitly. UniProt ManX FUNCTION saying the protein is required for lambda infection/pore formation overextends complex context onto the soluble subunit; a source-specific defect is recorded without altering the raw entry.

PMID:353494 maps pel and ptsM and explicitly allows a closely linked-gene explanation. It does not on its own prove that historical ptsM is uniquely manZ. PMID:4604906 correlates enzyme-II transport specificity with sugar taxis in mutants; its abstract does not identify a modern direct receptor-signaling mechanism for each separate protein. These remain qualified complex-level biological contexts, with no new chemotaxis or phage annotation manufactured.

## Historical topology and sugar evidence

PMID:8774730 used fusion reporters and proposed six ManY spanning segments and a single C-terminal ManZ anchor. The latter is a historical model, not proof of modern multipass topology;2019 structure now grounds the membrane architecture. Existing experimental proteomic rows are retained with explicit source-table access limits and independent target topology corroboration.

PMID:6252281 explicitly establishes PtsM-dependent N-acetylglucosamine utilization as one of two pathways. Early1974 fructose papers and1971 individual fractionation tables remain inaccessible here; independently accessible2019 primary context supports the broad sugar repertoire, so experimental curator annotations are retained with that limitation. No physiological substrate rank is inferred merely from the name mannose permease or the existence of other transporters. Glucose/fructose/GlcNAc are retained peripheral substrate contexts for this mannose-centered core synthesis, not claimed absent or mere assay noise.

## Ontology and phylogeny

QuickGO current term and is_a/part_of ancestor snapshots are in ontology/. GO0022870 explicitly combines histidyl-phosphate transfer with mannose group translocation and is a descendant of GO0008982 and GO0016773. GO0016301 defines phosphate transfer, usually (not exclusively) from ATP; it is not false because the donor is phosphohistidine. Its specific reaction replacement is not described as a verified kinase descendant. Generic membrane and cytoplasm rows refine to supported plasma membrane and cytosol; carbohydrate transport refines to all four supported substrate processes. PAINT-loss commands report no IRD/IKR on the three recovered lineages; this is not evidence for an invented ancestral gain or universal substrate specificity.
