# UGCG (Q16739) — Ceramide glucosyltransferase / Glucosylceramide synthase (GCS)

## Identity and core enzymology

- HGNC symbol UGCG; UniProt Q16739 (CEGT_HUMAN); EC 2.4.1.80. RecName "Ceramide glucosyltransferase"; AltNames GLCT-1, Glucosylceramide synthase (GCS), UDP-glucose ceramide glucosyltransferase, UDP-glucose:N-acylsphingosine D-glucosyltransferase [file:human/UGCG/UGCG-uniprot.txt "RecName: Full=Ceramide glucosyltransferase"; "EC=2.4.1.80"].
- 394 aa, ~44.9 kDa; glycosyltransferase family 2 (CAZy GT21) [file:human/UGCG/UGCG-uniprot.txt "Belongs to the glycosyltransferase 2 family"].
- Catalyzes the **first and committed glycosylation step of glycosphingolipid biosynthesis**: transfer of glucose from UDP-glucose to ceramide, producing glucosylceramide (GlcCer) + UDP + H+ [file:human/UGCG/UGCG-uniprot.txt "an N-acylsphing-4-enine + UDP-alpha-D-glucose = a beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine + UDP + H(+)"; "EC=2.4.1.80"].
- Cloned by expression cloning; original functional/enzymatic characterization: [PMID:8643456 "The enzyme catalyzes the first glycosylation step of glycosphingolipid synthesis and the product, glucosylceramide, serves as the core of more than 300 glycosphingolipids"]. This paper is the IDA source for both the MF (GO:0008120) and the BP (GO:0006679). Cache is abstract-only (full_text_available: false) but the abstract itself states the catalytic activity and pathway role directly.
- GlcCer is the precursor of lactosylceramide and hence of the ganglio-, globo- and (neo)lacto-series glycosphingolipids [file:human/UGCG/UGCG-uniprot.txt "GlcCer is the core component of glycosphingolipids/GSLs"].
- A secondary in vitro activity has been reported: UGCG can also transfer xylose from UDP-Xyl to ceramide, producing xylosylceramide (XylCer) [PMID:33361282; file:human/UGCG/UGCG-uniprot.txt "Catalyzes the synthesis of xylosylceramide/XylCer ... using UDP-Xyl as xylose donor"]. This is not in GOA and is a minor/side activity; not proposed as a core function.

## Localization and topology

- Golgi apparatus membrane; multi-pass membrane protein [file:human/UGCG/UGCG-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"; "Multi-pass membrane protein"].
- IDA Golgi-membrane localization from [PMID:12873973] (the RTN1 interaction paper), which reports subcellular location. Cache is abstract-only; abstract states GCS acts at the "Golgi/ER interface" [PMID:12873973 "RTN-1C not only interacts with GCS at Golgi/ER interface"].
- The catalytic (active) site is on the **cytosolic face** of the Golgi: GlcCer is synthesized at the cytosolic surface of Golgi subfractions [PMID:1532799 (UniProt ref [7]); file:human/UGCG/UGCG-uniprot.txt "Participates in the initial step of the glucosylceramide-based glycosphingolipid/GSL synthetic pathway at the cytosolic surface of the Golgi (PubMed:1532799, PubMed:8643456)"]. Note PMID:1532799 is cited by UniProt but is not among the GOA annotations.
- Topology in UniProt: 5 TRANSMEM helices; the large N-terminal catalytic domain (residues 33–195) is cytoplasmic, consistent with cytosolic-face catalysis [file:human/UGCG/UGCG-uniprot.txt "TOPO_DOM 33..195 /note=Cytoplasmic"].
- Active-site chemistry: D1/D2/D3 aspartates and the (Q/R)XXRW motif form the GCS active site (UDP-sugar binding + catalysis); ACT_SITE 236 proton acceptor [file:human/UGCG/UGCG-uniprot.txt "The D1, D2, D3, (Q/R)XXRW motif is a critical part of the GCS active site, involved in catalysis and UDP-sugar binding"].

## Interaction

- Interacts with RTN1 (reticulon-1, isoform RTN-1C), which modulates UGCG catalytic activity [PMID:12873973 "we have identified a member of the reticulon (RTN) family (RTN-1C) as the major GCS-protein partner"; "modulates its catalytic activity in situ"; file:human/UGCG/UGCG-uniprot.txt "Interacts with RTN1; regulates the ceramide glucosyltransferase activity of UGCG"]. The GOA IPI (GO:0005515 protein binding, with UniProtKB:Q16799 = RTN1) is this interaction. "protein binding" is uninformative; the informative functional description is a regulatory partner that modulates GCS activity. Bare GO:0005515 IPI is retained (never removed per policy) as non-core.

## Downstream / pleiotropic roles (mostly ISS/IEA from mouse ortholog O88693)

The single molecular function (making GlcCer) underlies a broad range of downstream processes. In GOA these are largely ISS (GO_REF:0000024, from mouse O88693) and mirrored IEA (GO_REF:0000107, Ensembl Compara from O88693). They are biologically defensible as consequences of loss of glycosphingolipids but are not the core function; they are downstream/context-dependent:

- Keratinocyte differentiation / epidermis development / establishment of skin barrier / cornified envelope assembly: GlcCer is the precursor of the ceramides forming the epidermal permeability barrier; GCS is up-regulated ~5-fold during keratinocyte differentiation [PMID:9545298 "GlcCer synthesis ... increased approximately 5-fold during keratinocyte differentiation"; "glucosylceramide (GlcCer), is thought to be synthesized, stored in intracellular lamellar granules and eventually extruded into the intercellular space where GlcCer is hydrolyzed to ceramide, a major component of the epidermal permeability barrier"]. The TAS "epidermis development" (GO:0008544) from PMID:9545298 is well supported. GO:0030216, GO:0061436, GO:1903575 are ISS/IEA orthology transfers of the same biology; keep as non-core.
- Neuron development / proper development of the nervous system: GSLs required for nervous-system development [file:human/UGCG/UGCG-uniprot.txt "required for instance in the proper development and functioning of the nervous system"]. ISS/IEA from mouse (neural-specific Ugcg KO is embryonic lethal / neurodegenerative). Keep as non-core.
- Leptin-mediated signaling pathway (GO:0033210): GSLs regulate the leptin receptor LEPR [file:human/UGCG/UGCG-uniprot.txt "they regulate the leptin receptor/LEPR in the leptin-mediated signaling pathway"]. Very specific downstream signaling role, ISS/IEA from mouse. Keep as non-core.
- Intestinal lipid absorption (GO:0098856): GSL biosynthesis needed for intestinal endocytic uptake of nutritional lipids [file:human/UGCG/UGCG-uniprot.txt "The biosynthesis of GSLs is also required for the proper intestinal endocytic uptake of nutritional lipids"]. ISS/IEA from mouse. Keep as non-core.
- Regulation of signal transduction (GO:0009966): GSLs are components of membrane microdomains mediating signal transduction [file:human/UGCG/UGCG-uniprot.txt "Glycosphingolipids are essential components of membrane microdomains that mediate membrane trafficking and signal transduction"]. Broad/indirect; ISS + IEA from mouse. Keep as non-core (or over-annotated given how general it is).
- Cell differentiation (GO:0030154): parent of keratinocyte differentiation; general ISS/IEA. Redundant with the more specific differentiation terms; keep as non-core.
- Protein lipidation (GO:0006497): ISS from mouse O88693 (GO_REF:0000024). UGCG glucosylates the **lipid** ceramide, not a protein; glucosylceramide is a glycolipid, not a lipidated protein. GO:0006497 "protein lipidation" = covalent attachment of a lipid to a protein. This looks like an incorrect ortholog transfer / mis-assignment (no protein substrate). Only an ISS (GO_REF:0000024, one paper's judgment), not experimental — flag as over-annotated. Retained (not removed) because it is an ISS with a curator's judgment; but biologically UGCG is not a protein-lipidating enzyme. Marked MARK_AS_OVER_ANNOTATED.

## Pharmacology / disease context (background, not for GO)

- UGCG is the target of substrate-reduction therapies: miglustat, eliglustat, venglustat [file:human/UGCG/UGCG-uniprot.txt "DrugBank; DB09039; Eliglustat"; "DrugBank; DB00419; Miglustat"; "DrugBank; DB14966; Venglustat"]. Used in Gaucher disease and other glycosphingolipidoses.
- GCS overexpression is associated with multidrug resistance in cancer [PMID:12873973 "Glucosylceramide synthase (GCS), the key enzyme in the biosynthesis of glycosphingolipids, has been implicated in many biological phenomena, including multidrug resistance"].

## Annotation-review summary (actions)

Core (ACCEPT):
- GO:0008120 ceramide glucosyltransferase activity — MF, IDA (PMID:8643456) core; IBA/IEA/TAS duplicates accepted.
- GO:0006679 glucosylceramide biosynthetic process — BP, IDA (PMID:8643456) core; IBA/IEA duplicates accepted.
- GO:0006688 glycosphingolipid biosynthetic process — BP, TAS Reactome; core (broader biosynthetic outcome).
- GO:0000139 Golgi membrane — CC, IDA (PMID:12873973) core; IEA/TAS duplicates accepted.

Non-core / over-annotation / other:
- GO:0016020 membrane (IBA, IEA) — accurate but less informative than Golgi membrane; KEEP_AS_NON_CORE.
- GO:0016757 glycosyltransferase activity (IEA, InterPro) — correct parent of GO:0008120 but too general; KEEP_AS_NON_CORE.
- GO:0006665 sphingolipid metabolic process (IEA, UniPathway) — correct parent; KEEP_AS_NON_CORE.
- GO:0008544 epidermis development (TAS, PMID:9545298) — supported downstream; KEEP_AS_NON_CORE.
- GO:0030216, GO:0061436, GO:1903575, GO:0030154, GO:0048666, GO:0033210, GO:0098856 (ISS + IEA) — downstream pleiotropic; KEEP_AS_NON_CORE.
- GO:0009966 regulation of signal transduction (ISS + IEA) — very general downstream; MARK_AS_OVER_ANNOTATED.
- GO:0006497 protein lipidation (ISS) — UGCG makes a glycolipid, not a lipidated protein; MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI, PMID:12873973, RTN1) — bare protein binding, uninformative; MARK_AS_OVER_ANNOTATED (per policy, never REMOVE an IPI protein-binding).
</content>
</invoke>
