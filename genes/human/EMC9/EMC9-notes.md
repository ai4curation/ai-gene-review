# EMC9 (Q9Y3B6) review notes

## Identity / overview
- EMC9 = ER membrane protein complex subunit 9; AltName FAM158A; synonyms C14orf122, ORFName CGI-112. Human, 208 aa, chromosome 14.
- Belongs to the **EMC8/EMC9 family** [file:human/EMC9/EMC9-uniprot.txt "Belongs to the EMC8/EMC9 family"]. Contains an MPN (Mpr1/Pad1 N-terminal) domain [file:human/EMC9/EMC9-uniprot.txt "DOMAIN          4..139\n                   /note=\"MPN\""], but the MPN here is degenerate (UPF0172 / pseudo-isopeptidase; no catalytic activity expected — EMC8/9 lack the JAMM Zn-coordinating residues of active MPN/JAMM metalloproteases).
- EMC9 is a **paralog of EMC8** and the two are **mutually exclusive subunits** of the EMC: [file:human/EMC9/EMC9-uniprot.txt "EMC8 and EMC9 are\nCC       mutually exclusive subunits of the EMC complex (PubMed:32459176)"]. ComplexPortal lists a distinct "EMC9 variant" complex (CPX-5881).
- EMC9 is **cytosolic / peripheral**, on the cytoplasmic face of the ER membrane: [file:human/EMC9/EMC9-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"], [file:human/EMC9/EMC9-uniprot.txt "Peripheral membrane protein"], [file:human/EMC9/EMC9-uniprot.txt "Cytoplasmic side"]. Consistent with the IDA cytoplasm annotation (PMID:22119785).

## EMC complex function (whole-complex)
- The EMC is an ER membrane insertase/chaperone enabling energy-independent insertion of newly synthesized membrane proteins: [file:human/EMC9/EMC9-uniprot.txt "Part of the endoplasmic reticulum membrane protein complex\nCC       (EMC) that enables the energy-independent insertion into endoplasmic\nCC       reticulum membranes of newly synthesized membrane proteins"].
- Roles: cotranslational insertion of multipass membrane proteins (incl. GPCR N-exo topology) and post-translational insertion of tail-anchored (TA) proteins: [file:human/EMC9/EMC9-uniprot.txt "required for the post-translational insertion of tail-\nCC       anchored/TA proteins in endoplasmic reticulum membranes"].
- IMPORTANT CAVEAT: EMC9 is a **weakly characterized** subunit. The FUNCTION block describes the **whole EMC**, not EMC9 specifically. EMC9 is a peripheral, cytosolic, non-catalytic subunit and an EMC8 paralog. The membrane insertase activity is a property of the EMC core (notably the EMC3/EMC6 hydrophilic vestibule); EMC9's individual contribution is via complex membership.

## Annotation provenance analysis (GOA)
- **EMC complex membership (GO:0072546)**: IDA from PMID:22119785 (the ERAD network mapping that first identified the EMC and placed FAM158A/EMC9 in it), plus IBA and InterPro IEA. This is the best-supported EMC9-specific assertion — direct co-purification/identification in the complex. Treat as CORE membership.
- **Cytoplasm (GO:0005737) IDA, PMID:22119785** and **ER membrane (GO:0005789)** (IEA SubCell + NAS ComplexPortal): consistent with peripheral/cytoplasmic-side localization. CORE location is the ER membrane; cytoplasm IDA is accurate but less specific.
- **Membrane insertase activity (GO:0032977)**: annotated with `contributes_to` (IBA, and IMP from PMID:29809151/PMID:30415835). The `contributes_to` qualifier correctly attributes a complex-level activity to a subunit. These IMP studies are EMC-knockdown functional studies; EMC9 itself is not the catalytic subunit, so this is a complex-level contribution — KEEP_AS_NON_CORE (not EMC9's own enzymatic core function).
- **protein insertion by stop-transfer (GO:0045050)** and **tail-anchored insertion (GO:0071816)**: IBA + IDA (ComplexPortal/UniProt, PMID:29242231) + IMP (PMID:29809151, PMID:30415835). These are EMC whole-complex processes; EMC9 participates as a subunit. KEEP_AS_NON_CORE (true of the complex; EMC9's role is via membership, and EMC8/9 are interchangeable so neither is individually required for the core insertase reaction).
- **protein binding (GO:0005515) IPI** (many entries): the WITH/FROM is almost entirely **EMC2 (Q15006)** — EMC9 binds EMC2; the crystal structure 6Y4L is EMC9(1-200) in complex with EMC2 [file:human/EMC9/EMC9-uniprot.txt "X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) OF 1-200 IN COMPLEX WITH EMC2"], [file:human/EMC9/EMC9-uniprot.txt "INTERACTION WITH EMC2"]. One IPI (PMID:32296183) is to SCN5A isoform (Q14524-3), an EMC client/interactor. Per guidelines bare "protein binding" is uninformative -> KEEP_AS_NON_CORE. The EMC2 interaction is biologically meaningful (how EMC9 docks into the complex) but the GO term itself is uninformative.
- The IPI sources are high-throughput interactome screens (PMID:16189514, 25416956, 28514442, 32296183, 33961781, 35271311) plus the ERAD mapping (22119785). All point to EMC2 binding (and one SCN5A). None of the cached full texts mention "EMC9"/"EMC8"/"FAM158A" by string in the captured text — these are interactome datasets keyed by accession.

## Paralog caution
- Because EMC8 and EMC9 are mutually exclusive and paralogous, process/function annotations propagated by IBA across the EMC8/EMC9 PANTHER family (PTN000309985) cannot distinguish which paralog is required. EMC9's defensible CORE = EMC complex membership (GO:0072546, IDA) + ER membrane location (GO:0005789). The insertase activity and insertion processes are complex-level (contributes_to / via membership) -> KEEP_AS_NON_CORE.

## Structure
- Crystal structure (6Y4L, 2.2 Å) of EMC9 1-200 bound to EMC2; cryo-EM (6Z3W) of the EMC complex including EMC9 [file:human/EMC9/EMC9-uniprot.txt "STRUCTURE BY ELECTRON MICROSCOPY (6.40 ANGSTROMS) OF THE EMC COMPLEX"].

## Disease / expression
- Low tissue specificity (HPA), broadly expressed. Pharos Tdark (understudied). No established disease association.
