# PIK3R4 review notes

Review started from `just fetch-gene human PIK3R4`. The proteostasis network places PIK3R4 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Class 3 PI3K complex 1, direct > Class 3 PI3K complex 1 component`.

Falcon deep research was requested with `just deep-research-falcon human PIK3R4`, but the provider timed out after 600 seconds and no `PIK3R4-deep-research-falcon.md` file was produced. I am completing the review using the cached primary literature, UniProt record, GOA seed, Reactome context, and notes below.

PIK3R4/VPS15/p150 is the regulatory/scaffolding subunit of class III PI3K complexes with PIK3C3/VPS34 and BECN1. The original human p150 paper showed that p150 is homologous to yeast Vps15p, stably associates with PtdIns 3-kinase, increases lipid kinase activity, and conserves the Vps15p/Vps34p protein-trafficking complex from yeast to human [PMID:8999962 "Recombinant p150 associated with PtdIns 3-kinase in vitro in a stable manner" and "Vps15p.Vps34p complex has been conserved from yeast to man"].

The PN leaf is the ATG14-containing PI3KC3-C1/autophagy-initiation branch. PI3KC3-C1 consists of VPS34, VPS15, BECN1, and ATG14; VPS15 organizes the complex and bridges VPS34 to the ATG14:BECN1 subcomplex [PMID:25490155 "PI3KC3-C1 ... consists of the lipid kinase VPS34, the scaffolding protein VPS15, the tumor suppressor BECN1, and the autophagy-specific subunit ATG14" and "VPS15 organizes the complex and serves as a bridge"]. A recent structural paper places VPS15/PIK3R4 in the ULK1C:PI3KC3-C1 initiation supercomplex and states that canonical bulk and selective autophagy are initiated by PI3KC3-C1 recruitment/activation [PMID:40442316 "All forms of canonical autophagy, bulk and selective, are initiated upon the recruitment and activation ... PI3KC3-C1" and "PI3KC3-C1 contains one copy each of ... VPS15"].

PIK3R4 should be modeled as contributing to complex-level PI3P production, not as the catalytic phosphatidylinositol kinase. Reactome says the ATG14:PIK3C3:PIK3R4:BECN1 complex phosphorylates phosphatidylinositol to PI3P for autophagosome formation [Reactome:R-HSA-5672012 "The Beclin-1 complex (ATG14:PIK3C3:PIK3R4:BECN1) is essential for autophagosome formation" and "PIK3C3 ... phosphorylates phosphatidylinositol (PI) producing phosphatidylinositol 3-phosphate (PI3P)"]. Reactome also describes PIK3R4 as necessary for PIK3C3 catalytic activity, localization, and stability in PI3P-producing complexes [Reactome:R-HSA-6798174 "PIK3C3, Vps34 ... is found in intracellular membrane complexes with ... PIK3R4, Vps150, necessary for catalytic activity, localization and stability"].

The UVRAG-containing PI3KC3-C2 branch is also real but is secondary to this PN leaf. The Rab7 paper supports late-endosome localization and early/late endosomal PI3K cycling [PMID:14617358 "The hVPS34/p150 complex colocalized with rab7 on late endosomes" and "link rab7 to the regulation of phosphatidylinositol 3'-kinase cycling between early and late endosomes"]. The UVRAG/BIF-1 paper supports receptor degradation and cytokinesis through a VPS15/VPS34/BECN1/UVRAG/BIF-1 subcomplex, while ATG14L is not required for those C2-like functions [PMID:20643123 "a specific sub-complex containing VPS15, VPS34, Beclin 1, UVRAG and BIF-1 regulates both receptor degradation and cytokinesis" and "ATG14L ... is not required"].

Autophagy process rows are supportable at the macroautophagy/autophagosome-assembly level, but cargo-specific pexophagy is too specific for the accessible human PIK3R4 evidence. The class III PI3K macroautophagy paper showed that increasing PI3P by overexpressing p150 stimulates macroautophagy and class III PI3K antisense inhibits macroautophagy [PMID:10625637 "overexpressing the p150 adaptor, stimulates macroautophagy" and "specific class III PI3K antisense oligonucleotide greatly inhibited the rate of macroautophagy"]. NRBF2 studies further support the ATG14-linked Vps34/Vps15 complex in starvation-induced autophagy [PMID:24785657 "NRBF2 binds to complexes that include Vps34, Vps15, Beclin-1 and ATG-14L" and PMID:24849286 "assembly of the specific Atg14L-Beclin 1-Vps34-Vps15 complex for autophagy induction"].

PIK3R4 also carries protein kinase annotations. UniProt currently curates catalytic protein serine/threonine reactions, Mn(2+) cofactor, and probable autophosphorylation, but the recent structural literature describes VPS15 as a pseudokinase [file:human/PIK3R4/PIK3R4-uniprot.txt "Probably autophosphorylated" and PMID:40442316 "the pseudokinase VPS15"]. I am retaining the protein kinase/ATP-binding rows as non-core rather than making them the central functional claim.

Generic `protein binding` annotations are not useful molecular-function annotations here. NRBF2, ATG14, BECN1, UVRAG, RAB7A, and high-throughput interactome rows should be interpreted as PI3KC3 complex/subcomplex evidence or interaction context, not as a core generic binding function [PMID:19270696 "Atg14L and UVRAG bind to Beclin 1 in a mutually exclusive manner"; PMID:24785657 "NRBF2 directly interacts with Vps15"; PMID:14617358 "hVPS34 and its adaptor protein p150 are rab7 interacting partners"].

Curation stance:
- Core: PI3KC3-C1 and PI3KC3-C2 complex membership, contribution to complex-level 1-phosphatidylinositol-3-kinase activity/PI3P biosynthesis, autophagosome assembly and macroautophagy, autophagosome maturation/endosomal trafficking context, late endosome/autophagosome/membrane/cytosol localization.
- Modify: pexophagy to autophagosome assembly; vacuole terms to human lysosomal/endosomal equivalents; PI3K/AKT signaling to autophagosome maturation.
- Keep as non-core: protein kinase/ATP-binding/protein phosphorylation rows, cilium/axoneme/cytoskeleton context, glucose-starvation response, phagocytic vesicle membrane, cytokinesis.
- Remove: nucleus-vacuole junction as a yeast/vacuole-specific cellular component that does not map to human PIK3R4.
- Mark over-annotated: generic protein binding rows.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording identified PI3KC3 complex regulation, not independent catalytic signaling, as the central PN function.
