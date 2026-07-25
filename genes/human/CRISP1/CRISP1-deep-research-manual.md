# Manual literature synthesis for human CRISP1 (P54107)

## Scope and provenance

This report was prepared manually from the project-cached UniProt record, GOA rows, PANTHER PAINT trace, ontology lookups, and primary publications after the configured automated providers failed on 2026-07-18 (Falcon/Edison HTTP 402; Perplexity-lite HTTP 401 insufficient quota). It is intentionally named `deep-research-manual` rather than after a provider.

## Molecular identity and localization

Human CRISP1 is a 249-amino-acid secreted glycoprotein precursor in the CAP/CRISP family. UniProt annotates a signal peptide at residues 1–21, a CAP domain, a cysteine-rich domain, multiple disulfide bonds, and two splice isoforms. Direct human tissue studies identify an epididymis-enriched protein in distal ductus efferentes and epididymal epithelium/lumen, ductus deferens, sperm, and seminal plasma. Immunohistochemistry places it on the postacrosomal sperm-head region [PMID:8543280]. Sequential extraction additionally demonstrates a tightly sperm-surface-associated population [PMID:11566719]. These data establish extracellular-region and sperm-plasma-membrane pools.

An early biochemical study found epididymis-specific CRISP1 but reported no significant sperm association [PMID:8665901], whereas later immunolocalization, sequential extraction, and functional antibody studies support a sperm-associated population [PMID:8543280; PMID:8838800; PMID:11566719]. This apparent difference may reflect extraction, antibody, sample, or pool-specific sensitivity and should not be converted into an isoform-specific claim without direct testing.

The sperm-nucleus proteomics annotation from PMID:21630459 cannot be fully assessed from the cached abstract. The abstract reports a highly purified sperm-nuclear preparation and 403 identified proteins but does not list CRISP1. Nuclear localization is therefore unresolved, not disproven.

## Direct human reproductive functions

Human CRISP1 acts at two successive stages of gamete interaction:

1. Human sperm-zona pellucida binding: blocking sperm CRISP1 with antibody or occupying zona sites with recombinant CRISP1 reduces human sperm binding in hemizona assays. Recombinant CRISP1 binds ZP3 preferentially, dose-dependently, and saturably compared with ZP2 and ZP4 [PMID:24334245]. This directly supports GO:0007339 binding of sperm to zona pellucida.
2. Sperm-egg plasma-membrane fusion: anti-CRISP1 inhibits penetration of zona-free hamster eggs by capacitated human sperm without reducing motility, viability, acrosome reaction, or initial oolemma binding. Recombinant human CRISP1 also binds complementary sites across the surface of zona-free human oocytes [PMID:11566719]. Together these experiments support the existing GO:0007342 fusion annotation while placing CRISP1 after initial oolemma attachment rather than treating it as the sole essential fusogen.

The 1995–1996 characterization papers established epididymal secretion and postacrosomal localization and proposed functional equivalence to rodent AEG/DE [PMID:8543280; PMID:8838800]. Their functional interpretation was initially inferential, but it is corroborated by the later direct human experiments above.

## Calcium-homeostasis mechanism

In co-transfected cells, human CRISP1 and CRISP3 both interact with human PMCA4b through their N-terminal domains, but only human CRISP1 and rat CRISP4 delay PMCA4b-mediated calcium extrusion [PMID:37882330]. This supports GO:1903170 negative regulation of calcium ion transmembrane transport for human CRISP1. Whether this interaction regulates endogenous PMCA4b in human sperm, which CRISP1 pool is responsible, and how it integrates with capacitation remain open.

Native rat CRISP1 inhibits mouse sperm CatSper and TRPM8 currents and modulates hyperactivation/orientation [PMID:26416967]. These findings motivate testing human CRISP1 for GO:0005246 calcium channel regulator activity, but they are not treated as direct human evidence because the experimental protein and sperm were nonhuman.

## Mammalian genetic context and transfer boundary

Mouse Crisp1 single-gene deletion leaves natural fertility intact but lowers capacitation-associated tyrosine phosphorylation and reduces sperm penetration of both zona-intact and zona-free eggs in vitro [PMID:18571638]. Combined Crisp1/Crisp4 deletion produces fertility defects in most males and epididymal epithelial differentiation, luminal-pH, and inflammatory phenotypes in a subset [PMID:30510210]. These data establish redundancy among rodent epididymal CRISPs and caution against describing human CRISP1 as an indispensable standalone fusogen. Humans lack rodent CRISP4, and human CRISP1 has been proposed as a functional counterpart of both rodent proteins, but rodent tissue-level phenotypes are not direct human annotations.

## PAINT inference assessment

The cached PANTHER trace places GO:0060090 molecular adaptor activity at the broad PTHR10334 node PTN000036124 from only MGI:MGI:1916536, mouse `Glipr1l1`. That source protein is a distinct GPI-anchored sperm/acrosomal CAP-family paralog involved in IZUMO1 redistribution. Human CRISP1 has direct evidence for ligand interaction and calcium-transport regulation, but no study demonstrates that it brings multiple macromolecules together as required for molecular adaptor activity. The root-family IBA is therefore over-propagated and should be removed from CRISP1.

## Evidence boundaries and open questions

- The direct human studies support participation in zona binding and fusion, not absolute requirement for natural fertility.
- The molecular identity of CRISP1's human oolemma binding partner remains unknown.
- The relative contributions, processing, and fate of loosely versus tightly sperm-associated CRISP1 pools are not resolved at isoform level.
- Endogenous human-sperm PMCA4b regulation has not been demonstrated, and conserved CatSper/TRPM8 regulation remains an orthology-based hypothesis.
- The sperm-nuclear HDA annotation cannot be verified from the abstract-only cached source.
