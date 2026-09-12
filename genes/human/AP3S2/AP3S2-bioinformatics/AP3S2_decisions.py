"""All reviewer prose and verdicts for the AP3S2 review, keyed by GOA row number.

`build_review.py` merges this with the mechanical fields taken straight from
`AP3S2-goa.tsv`, so nothing here restates a GO id, evidence code, reference or
WITH/FROM list; those are copied from GOA and cannot drift.

Row numbers are 1-based positions in `AP3S2-goa.tsv` after the header.
"""

from __future__ import annotations

UNIPROT = "file:human/AP3S2/AP3S2-uniprot.txt"
BIOINF = "file:human/AP3S2/AP3S2-bioinformatics/RESULTS.md"
AFFINAGE = "file:human/AP3S2/AP3S2-deep-research-affinage.md"

# --------------------------------------------------------------------------
# Quotes. Every one is a verbatim substring of the cited cache file; `file:`
# quotes from the UniProt flat file sit on a single physical line.
# --------------------------------------------------------------------------

Q_COMPONENTS = ("PMID:9118953", (
    "sigma3A and sigma3B are components of a large complex, named AP-3, that also contains "
    "proteins of apparent molecular masses of 47, 140 and 160 kDa."))
Q_EXPRESSED = ("PMID:9118953", (
    "Northern and Western blot analyses demonstrate that the products of both the sigma3A "
    "and sigma3B genes are expressed in a wide variety of tissues and cell lines."))
Q_TGN = ("PMID:9118953", (
    "Immunofluorescence microscopy analyses show that the sigma3-containing complex is "
    "present both in the area of the TGN and in peripheral structures, some of which contain "
    "the transferrin receptor."))
Q_TYROSINE = ("PMID:9118953", (
    "These results suggest that the sigma3 chains are components of a novel, ubiquitous "
    "adaptor-like complex involved in the recognition of tyrosine-based sorting signals."))

Q_SUBUNITS = ("PMID:9151686", (
    "Antibodies raised against recombinant delta and sigma3 show that they are the other two "
    "subunits of the adaptor-like complex."))
Q_UBIQUITOUS = ("PMID:9151686",
                "Fig. 4 shows that δ, β3A, σ3A, and σ3B are all expressed ubiquitously.")
Q_DOUBLET = ("PMID:9151686", (
    "σ3 (which appears as a doublet, presumably because there are two isoforms of the "
    "protein)"))
Q_SIGMA_IP = ("PMID:9151686", "The σ3 antibodies bring down these four subunits as well")
Q_MOUSE_HUMAN = ("PMID:9151686",
                 "The mouse and human σ3B protein sequences are 100% identical in the region "
                 "of overlap.")

Q_Y3H = ("PMID:14691137", (
    "yeast three-hybrid analyses showed that the cytosolic tail of LIMP-II interacted with "
    "γ1–σ1A, δ–σ3A, and δ–σ3B"))
Q_ALASCAN = ("PMID:14691137", (
    "Of 12 residues that were mutated, only three were essential for interactions with "
    "γ1–σ1A, δ–σ3A, and δ–σ3B, the leucine-isoleucine pair and the glutamate residue at "
    "position −4"))
Q_NOVEL_MODE = ("PMID:14691137", (
    "These observations reveal a novel mode of recognition of sorting signals involving the "
    "gamma/delta and sigma subunits of AP-1 and AP-3."))
Q_CLONED_SEPARATELY = ("PMID:14691137", (
    "μ3A and σ1A (EcoRI–SalI), and σ2, σ3A, σ3B, and σ4 (BamHI–XhoI) were cloned into "
    "pGAD424."))

Q_COMPOSITE = ("PMID:21097499", (
    "signals, on the other hand, do not bind to any single AP subunit but to combinations of "
    "γ-σ1, α-σ2, and δ-σ3 subunits, as demonstrated by the use of yeast three-hybrid (Y3H) "
    "and in vitro binding assays"))
Q_RESIDUES = ("PMID:21097499", (
    "This is evidenced by the loss of signal binding by the σ2 V88D or L103S substitutions "
    "and the homologous σ1A V88D and I103S and σ3A V94D and L109S substitutions."))
Q_TWO_SIGMA3 = ("PMID:21097499",
                "two β3 (β3A and β3B), two μ3 (μ3A and μ3B), and two σ3 (σ3A and σ3B) for AP-3")
Q_NOT_KNOWN = ("PMID:21097499", (
    "It is not known, however, whether most of these combinations occur in cells and whether "
    "particular subunit isoforms endow the complexes with different functional properties."))

Q_ENDO_LYSO = ("PMID:39705307", (
    "Adaptor protein complex-3 (AP-3) mediates cargo sorting from endosomes to lysosomes and "
    "lysosome-related organelles."))
Q_POCKET_OCCLUDED = ("PMID:39705307", (
    "Surprisingly, the dileucine cargo-binding site on σ3 is occupied by the N-terminal "
    "extension of β3"))
Q_DELTA_SIGMA_ARF1 = ("PMID:39705307",
                      "it is apparent that the δ-σ3 complex binds nearly as well as the full "
                      "complex")

Q_NO_CLATHRIN = ("PMID:42139345", (
    "By demonstrating that AP3:ARF1 can generate carriers without using a clathrin lattice, "
    "we explain the clathrin independence of AP3-mediated trafficking."))
Q_NO_CCV = ("PMID:42139345", "AP3 does not copurify with clathrin-coated vesicles")
Q_TUBULAR = ("PMID:42139345", (
    "AP3:ARF1 spontaneously remodels membranes containing cargo and the phosphoinositide "
    "PI(3,5)P2 into tubular structures coated in spiraling rows of AP3 arches and ARF1 "
    "dimers"))
Q_STRUCT_USED_AP3S1 = ("PMID:42139345", (
    "AP3D1(1–1203) (Homo sapiens) and AP3S1(1–193) (H. sapiens) were cloned into the pFL "
    "vector"))

Q_CLATHRIN_1998 = ("PMID:9545220", (
    "In vitro binding assays showed that mammalian AP-3 did associate with clathrin by "
    "interaction of the appendage domain of its beta3 subunit with the amino-terminal domain "
    "of the clathrin heavy chain."))
Q_SIGNAL_SORTING = ("PMID:9545220", (
    "A heterotetrameric complex termed AP-3 is involved in signal-mediated protein sorting to "
    "endosomal-lysosomal organelles."))

Q_BETA3_ISOFORMS = ("PMID:15537701", (
    "Neurons express adaptor (AP)-3 complexes assembled with either ubiquitous (beta3A) or "
    "neuronal-specific (beta3B) beta3 isoforms."))
Q_ZNT3 = ("PMID:15537701", (
    "beta3B deficiency compromised synaptic zinc stores assessed by Timm's staining and the "
    "synaptic vesicle targeting of membrane proteins involved in zinc uptake (ZnT3 and "
    "ClC-3)"))
Q_SV_LEVELS = ("PMID:15537701", (
    "Our results suggest that concerted nonredundant functions of neuronal and ubiquitous "
    "AP-3 provide a mechanism to control the levels of selected membrane proteins in synaptic "
    "vesicles."))

Q_TYROSINASE = ("PMID:23247405", (
    "Packaging of the tyrosinases into transport vesicles at early/recycling "
    "endosome-associated tubules is dependent on ubiquitous adaptor protein complex (AP)-1 "
    "and AP-3"))
Q_ENDOSOME_TUBULES = ("PMID:23247405", (
    "Rab32 and Rab38 interact with AP-1, AP-3 and BLOC-2 on early/recycling endosome tubules, "
    "where cargo such as tyrosinase and Tyrp1 are loaded into vesicles or transport "
    "intermediates."))
Q_HPS = ("PMID:23247405", (
    "Hermansky-Pudlak Syndrome (HPS) patients and the corresponding animal models have "
    "abnormal melanosomes, platelet dense granules and lamellar bodies of lung type II "
    "epithelial cells."))
Q_HPS_SUBUNITS = ("PMID:23247405",
                  "Mutations in subunits of AP-3, BLOC-1, BLOC-2 and BLOC-3 underlie many "
                  "forms of HPS.")
Q_CLATHRIN_2013 = ("PMID:23247405", (
    "While it was initially suspected that AP-3 may be clathrin-independent, subsequent "
    "research has shown that AP-3 and AP-1 act as clathrin-binding adaptor proteins"))

Q_MOCHA = ("PMID:21998198", (
    "Synaptosome fractions from control brains (lanes 1–8) and AP-3–deficient mocha "
    "(Ap3d1mh/mh) brains"))
Q_PAN_SIGMA_AB = ("PMID:21998198", (
    "antibodies against synaptic vesicle markers (SV2, synaptophysin), AP-3–dependent "
    "synaptic vesicle cargoes (PI4KIIα, VAMP7, ZnT3), and AP-3 σ3 subunit"))
Q_SV_COMPOSITION = ("PMID:21998198",
                    "Deficiencies in AP-3 and BLOC-1 affect synaptic vesicle composition.")

Q_SV_VISITOR = ("PMID:33376223", (
    "This may explain the presence of endosomal-related proteins (e.g., Stx7, AP3) or "
    "proteins of the AZ (e.g., Piccolo, Bassoon) in the SV proteome."))

Q_TMEM163_MOTIF = ("PMID:41985787", (
    "A conserved N-terminal acidic dileucine motif (LEDRGL69L70) in TMEM163 is essential for "
    "interactions with BLOC-1 and AP-3 but dispensable for binding with AP-1, AP-2 and "
    "BLOC-2."))
Q_TMEM163_CARGO = ("PMID:41985787", (
    "our findings established TMEM163 as a cargo protein sequentially sorted by AP-3 and "
    "BLOC-1 via a shared dileucine-based sorting signal, which is essential for its proper "
    "trafficking to platelet dense granules"))
Q_TMEM163_PLATELET = ("PMID:41985787", (
    "Transmembrane protein 163 (TMEM163), a zinc transporter, is drastically reduced in "
    "platelets of AP-3-, BLOC-1-, and BLOC-2-deficient Hermansky-Pudlak syndrome mice and "
    "patients"))

Q_CROSSLINK = ("PMID:19010779", (
    "purification of cross-linked AP-3 complexes and mass spectrometric identification of "
    "associated proteins"))

Q_T2D_LOCUS = ("PMID:21874001", (
    "At 15q26, rs2028299 is nearest AP3S2, encoding a clathrin associated adaptor complex "
    "expressed in adipocytes, pancreatic islets and other tissues, which may be involved in "
    "vesicle transport and sorting"))
Q_T2D_C15ORF38 = ("PMID:21874001", (
    "SNP rs2028299 is associated with expression of C15orf38, encoding a member of an "
    "uncharacterised family of proteins."))
Q_T2D_PLIN1 = ("PMID:21874001",
               "Amongst the other genes at this locus, PLIN1 is also a possible candidate for "
               "the association with T2D.")

Q_UP_TISSUE = (UNIPROT, "CC   -!- TISSUE SPECIFICITY: Present in all adult tissues examined.")
Q_UP_PROTEIN_LEVEL = (UNIPROT, "PE   1: Evidence at protein level;")
Q_UP_TDARK = (UNIPROT, "DR   Pharos; P59780; Tdark.")
Q_UP_ORCS = (UNIPROT, "DR   BioGRID-ORCS; 10239; 20 hits in 1154 CRISPR screens.")
Q_UP_PANGO = (UNIPROT, "DR   PAN-GO; P59780; 1 GO annotation based on evolutionary models.")
Q_UP_PANTHER = (UNIPROT, "DR   PANTHER; PTHR11753; ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY; 1.")
Q_UP_HPA = (UNIPROT, "DR   HPA; ENSG00000157823; Low tissue specificity.")
Q_UP_CPX = (UNIPROT,
            "DR   ComplexPortal; CPX-5052; Ubiquitous AP-3 Adaptor complex, sigma3b variant.")
Q_UP_NOT_CLATHRIN = (UNIPROT, "CC       not clathrin-associated. The complex is associated with the Golgi")
Q_UP_LOCATION = (UNIPROT,
                 "CC   -!- SUBCELLULAR LOCATION: Golgi apparatus. Cytoplasmic vesicle membrane")
Q_UP_COAT = (UNIPROT,
             "CC       cytoplasmic face of coated vesicles located at the Golgi complex.")
Q_UP_SIGMA_SLOT = (UNIPROT,
                   "CC       a small adaptin (sigma-type subunit APS1 or AP3S2). Interacts with")
Q_UP_BLOC1 = (UNIPROT, "CC       cell bodies for delivery into neurites and nerve terminals.")
Q_UP_READTHROUGH = (UNIPROT, "CC         IsoId=Q7Z6K5-2; Sequence=External;")
Q_UP_FUNFAM = (UNIPROT, "DR   FunFam; 3.30.450.60:FF:000001; AP complex subunit sigma; 1.")

Q_BIO_POCKET = (BIOINF,
                "AP3S2 retains both pocket residues at the same native positions as AP3S1")
Q_BIO_IDENTICAL = (BIOINF, "Human and mouse AP3S2 are byte-for-byte identical proteins")
Q_BIO_ARBA = (BIOINF, "exactly the two AP-3 sigma subunits match")
Q_BIO_SEEDS = (BIOINF, "Two of the ten seeds are genuine AP-3 sigma orthologs")
Q_BIO_LCA = (BIOINF, (
    "Donors that disagree in destination are exactly the case in\nwhich the *parent* term is "
    "the correct least common ancestor"))
Q_AFFINAGE_LIMIT = (AFFINAGE, (
    "Beyond its role as an AP-3 subunit, no further mechanistic detail of AP3S2's own "
    "activity has been characterized in the available corpus."))

Q_BIO_STRUCTURES = (BIOINF, (
    "Every solved AP-3 structure to date is built on **sigma-3A**"))

# --------------------------------------------------------------------------
# Reusable prose
# --------------------------------------------------------------------------

SUBUNIT_PREAMBLE = (
    "AP3S2 is sigma-3B, one of the two interchangeable small subunits of the AP-3 coat "
    "adaptor; its membership of that complex is the one experimentally established fact "
    "about this protein [PMID:9118953]. "
)

NON_CORE_NEURONAL = (
    "Real AP-3 biology, but neuronal and complex-level rather than a function of this "
    "ubiquitously expressed subunit: the perturbation behind the mouse source annotation is "
    "the delta subunit (Ap3d1 mocha) and the sigma detection uses a pan-sigma-3 antibody that "
    "does not separate sigma-3A from sigma-3B [PMID:21998198]. Kept, marked non-core."
)

# --------------------------------------------------------------------------
# Per-source comments used in propagation_review.source_entities
# --------------------------------------------------------------------------

SRC_MOUSE = (
    "Mouse Ap3s2, the one-to-one ortholog and the only gene-product donor on this row. The "
    "transfer is as safe as an ortholog transfer gets: human and mouse AP3S2 are identical in "
    "sequence over all 193 residues. What the donor annotation itself rests on is a "
    "delta-subunit mutant read out with a pan-sigma-3 antibody, so the inherited claim is "
    "complex-level."
)
SRC_MOUSE_ENSEMBL = (
    "The Ensembl protein model for the same mouse gene as UniProtKB:Q8BSZ2 - one donor, two "
    "identifiers, not two independent lines of evidence."
)
SRC_RAT = (
    "Rat Ap3s2 (unreviewed). Its GO:0008021 rests on a SynGO EXP/IDA from a synaptic-vesicle "
    "proteome in which the authors themselves list AP3 among endosomal 'visitor' proteins "
    "rather than vesicle residents [PMID:33376223]."
)
SRC_RAT_ENSEMBL = (
    "The Ensembl protein model for the same rat gene as UniProtKB:A0A0G2K302 - one donor, two "
    "identifiers."
)
SRC_PTN = (
    "PTHR11753 IBD node PTN000204281, seeded by ten sigma subunits spanning AP-1, AP-2 and "
    "AP-3 across fungi, nematode, fly, rodent and human. Two seeds are AP-3 sigma orthologs "
    "(S. cerevisiae APS3, C. albicans APS3), so AP-3 is inside the clade the function is "
    "asserted for, and AP3S2 is an AP-3 sigma subunit. The remaining eight seeds act on "
    "different itineraries, which is why the node carries the parent process term rather than "
    "a destination-specific child."
)

# --------------------------------------------------------------------------
# Decisions, one per GOA row
# --------------------------------------------------------------------------

DECISIONS: dict[int, dict] = {

    1: dict(  # GO:0016192 vesicle-mediated transport, IBA
        summary=(
            "AP-3 is a vesicle coat adaptor, and vesicle-mediated transport is the process it "
            "acts in; sigma-3B is a constituent subunit of it [PMID:9118953]. The "
            "phylogenetic inference is sound at the node and general for the right reason."),
        action="ACCEPT",
        reason=(
            "The IBD behind this row sits on PTHR11753 node PTN000204281 and is seeded by ten "
            "sigma subunits, two of which (S. cerevisiae APS3, C. albicans APS3) are AP-3 "
            "sigma orthologs; the rest are AP-1 and AP-2 sigmas. AP3S2 sits squarely inside "
            "the clade, and there is no target-specific evidence of loss or divergence: the "
            "longin/roadblock fold is intact, the dileucine-binding pocket is intact at the "
            "same positions as in AP3S1, there are no NOT rows, and the protein is expressed "
            "in every adult tissue examined. The term's generality is not an under-call - the "
            "seeds disagree about destination (trans-Golgi/endosome for AP-1, plasma membrane "
            "for AP-2, endosome/lysosome for AP-3), so vesicle-mediated transport is the "
            "correct least common ancestor rather than a missed opportunity for a child term. "
            "One donor on the row, FB:FBgn0043012 (D. melanogaster AP-2sigma), is not in the "
            "current GO:0016192 seed list but is a seed of the same node's GO:0043231 IBD, "
            "whose slice line is three months older; that is a release-timing difference "
            "between GOA and the PAINT slice, not a donor the tree lacks. Core."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={
                "PANTHER:PTN000204281": ("SUPPORTS_TRANSFER", SRC_PTN),
                "CGD:CAL0000182525": ("SUPPORTS_TRANSFER", (
                    "Q59QC5 APS3_CANAL, the Candida albicans AP-3 sigma subunit - a seed from "
                    "the same complex as the target.")),
                "SGD:S000003561": ("SUPPORTS_TRANSFER", (
                    "P47064 AP3S_YEAST (APS3), the budding-yeast AP-3 sigma subunit. The most "
                    "directly relevant seed on the row: same subunit, same complex.")),
                "SGD:S000004160": ("SUPPORTS_TRANSFER", (
                    "P35181 AP1S1_YEAST (APS1), an AP-1 sigma. Supports the family-level "
                    "process term, not an AP-3-specific itinerary.")),
                "PomBase:SPAP27G11.06c": ("SUPPORTS_TRANSFER", (
                    "Q9P7N2 AP1S1_SCHPO (vas2/aps1), fission-yeast AP-1 sigma; same role.")),
                "MGI:MGI:1098244": ("SUPPORTS_TRANSFER",
                                    "P61967 AP1S1_MOUSE, mouse AP-1 sigma-1A."),
                "MGI:MGI:1889383": ("SUPPORTS_TRANSFER",
                                    "Q9DB50 AP1S2_MOUSE, mouse AP-1 sigma-1B."),
                "FB:FBgn0039132": ("SUPPORTS_TRANSFER",
                                   "Drosophila AP-1sigma (CG5864)."),
                "FB:FBgn0043012": ("SUPPORTS_TRANSFER", (
                    "Drosophila AP-2sigma (CG6056, Q9VDC3). Present on the GOA row but absent "
                    "from the current GO:0016192 seed list in the PAINT slice; it is a seed of "
                    "the same node's older GO:0043231 IBD line, so the tree does contain it.")),
                "RGD:620188": ("SUPPORTS_TRANSFER", "P62744 AP2S1_RAT, rat AP-2 sigma."),
                "UniProtKB:P53680": ("SUPPORTS_TRANSFER", (
                    "AP2S1_HUMAN, the human AP-2 sigma subunit - a within-species paralog of "
                    "the target, contributing the human experimental evidence to the node.")),
                "WB:WBGene00000157": ("SUPPORTS_TRANSFER", (
                    "C. elegans aps-2 (F02E8.3, Q19123), AP-2 sigma. Not resolvable through "
                    "UniProt's xref index; identified via the GO API bioentity record.")),
            },
            residue_claims_not_applicable=(
                "The row is accepted, so no residue-based loss argument is being made. The "
                "positive residue evidence that the target has not diverged at the "
                "cargo-binding site is recorded on the GO:0030674 NEW row instead."),
        ),
        supported_by=[Q_COMPONENTS, Q_ENDO_LYSO, Q_BIO_SEEDS, Q_UP_PANGO],
    ),

    2: dict(  # GO:0005794 Golgi apparatus, IEA from SubCell
        summary=(
            "UniProt places AP-3 at the Golgi apparatus, and the antibody localisation that "
            "underlies it saw the sigma-3-containing complex in the TGN area "
            "[PMID:9118953]."),
        action="ACCEPT",
        reason=(
            "The SubCell mapping reproduces the UniProt SUBCELLULAR LOCATION line faithfully, "
            "and that line is grounded in the original localisation of the sigma-3-containing "
            "complex to the TGN region and peripheral structures. Mammalian AP-3's main site "
            "of action is endosomal rather than Golgi, so this is the broader of the two "
            "compartments it occupies, but it is not wrong and the term is a parent of the "
            "TGN. Accepted as a genuine location."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={"UniProtKB-SubCell:SL-0132": ("SUPPORTS_TRANSFER", (
                "SubCell 'Golgi apparatus', mapped from the UniProt SUBCELLULAR LOCATION "
                "line, which is itself an ECO:0000250 by-similarity statement backed by the "
                "1997 immunofluorescence of the sigma-3 complex."))},
            residue_claims_not_applicable=(
                "A compartment assignment, not a sequence feature."),
        ),
        supported_by=[Q_UP_LOCATION, Q_TGN],
    ),

    3: dict(  # GO:0006886 intracellular protein transport, IEA InterPro
        summary=(
            "Moving transmembrane proteins between intracellular compartments is what AP-3 is "
            "for, so this term is core even though it is reached from a family signature "
            "[PMID:9545220]."),
        action="ACCEPT",
        reason=(
            "IPR000804 is the clathrin small-chain signature shared by all AP-complex sigma "
            "subunits, and intracellular protein transport is true of every one of them - but "
            "being family-wide is not the same as being peripheral. Signal-mediated sorting of "
            "membrane proteins between intracellular compartments is the function of AP-3 "
            "[PMID:9545220], and the term is carried in this review's core_functions as one of "
            "the processes the subunit is directly involved in. Accepted as core; the more "
            "specific destination is supplied by the replacement proposed on the GO:0006896 "
            "row, and there is no conflict between holding a parent and a child."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={"InterPro:IPR000804": ("SUPPORTS_TRANSFER", (
                "Clathrin adaptor small-chain signature, present on the target "
                "(PROSITE PS00989 / Pfam PF01217 on the same record). The mapped term is a "
                "family-wide generality and applies."))},
            residue_claims_not_applicable=(
                "A domain-presence mapping accepted as correct; no residue argument arises."),
        ),
        supported_by=[Q_SIGNAL_SORTING, Q_ENDO_LYSO],
    ),

    4: dict(  # GO:0006896 Golgi to vacuole transport, IEA InterPro
        summary=(
            "The right pathway for fungal AP-3, the wrong compartment of origin for the human "
            "complex. Mammalian AP-3 sorts from endosomes to lysosomes and lysosome-related "
            "organelles [PMID:39705307], not from the Golgi to the vacuole."),
        action="MODIFY",
        reason=(
            "IPR027155 is the APS3 signature, so the mapping is correctly targeted at AP-3 "
            "sigma subunits; the problem is that the GO term it maps to describes the "
            "budding-yeast ALP pathway, in which AP-3 genuinely does run Golgi-to-vacuole. In "
            "mammals the characterised itinerary begins at early/recycling endosomal tubules "
            "[PMID:23247405] and ends at lysosomes and lysosome-related organelles "
            "[PMID:39705307]. GO:0008333 endosome to lysosome transport states the human "
            "route without importing the fungal compartment. This is a term-scoping problem "
            "in the InterPro2GO mapping rather than a wrong family assignment."),
        replace=[("GO:0008333", "endosome to lysosome transport")],
        prop=dict(
            root_cause="TERM_SCOPING_PROBLEM",
            modes=["COMPARTMENT_OR_COMPLEX_MISMATCH"],
            status={"InterPro:IPR027155": ("SUPPORTS_SOURCE_BUT_NOT_TARGET", (
                "APS3, the AP-3 sigma signature; the family call is right and the target does "
                "carry it. What does not transfer is the mapped term's compartment of origin, "
                "which reflects the fungal Golgi-to-vacuole pathway rather than the mammalian "
                "endosome-to-lysosome one."))},
            residue_claims_not_applicable=(
                "The objection is to the compartment named by the mapped term, not to any "
                "residue or domain feature of AP3S2."),
        ),
        supported_by=[Q_ENDO_LYSO, Q_ENDOSOME_TUBULES, Q_TYROSINASE],
    ),

    5: dict(  # GO:0015031 protein transport, IEA InterPro
        summary="The most general true statement about an AP-complex subunit.",
        action="KEEP_AS_NON_CORE",
        reason=(
            "IPR016635 is the AP-complex small-subunit signature and protein transport is the "
            "process every member serves. Correct, and the UniProt keyword block carries the "
            "same claim, so there is nothing to remove or repair. But GO:0015031 is the parent "
            "of the intracellular transport term this review does take as core, and its "
            "definition extends to movement into, out of and between cells - a scope AP-3 does "
            "not cover. Kept, marked non-core, so that the grading matches the reasoning "
            "rather than promoting the broadest available parent to a core function."),
        prop=dict(
            root_cause="NO_FAILURE_NON_CORE",
            status={"InterPro:IPR016635": ("SUPPORTS_TRANSFER", (
                "AP_complex_ssu, the family signature listed on the target's own record. The "
                "mapped term is correct at family level."))},
            residue_claims_not_applicable="A family-level process mapping, accepted.",
        ),
        supported_by=[Q_SIGNAL_SORTING, Q_UP_PANTHER],
    ),

    6: dict(  # GO:0016192 vesicle-mediated transport, IEA InterPro
        summary=(
            "Same conclusion as the IBA row, reached from the domain signature rather than "
            "from the tree."),
        action="ACCEPT",
        reason=(
            "IPR000804 maps to vesicle-mediated transport for all AP-complex small chains, "
            "and AP-3 is a vesicle coat adaptor [PMID:42139345]. Duplication with the IBA and "
            "NAS rows for the same term is normal and not a defect."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={"InterPro:IPR000804": ("SUPPORTS_TRANSFER", (
                "Clathrin adaptor small-chain signature on the target. The mapped process is "
                "the same one the PANTHER node asserts, arrived at independently."))},
            residue_claims_not_applicable="Domain-based process mapping, accepted.",
        ),
        supported_by=[Q_TUBULAR, Q_ENDO_LYSO],
    ),

    7: dict(  # GO:0030117 membrane coat, IEA InterPro
        summary=(
            "AP-3 forms the inner layer of a membrane coat, and the GO definition explicitly "
            "covers non-clathrin coats."),
        action="ACCEPT",
        reason=(
            "GO:0030117 is defined to include coats other than clathrin's, which matters here "
            "because AP-3 builds carriers without a clathrin lattice [PMID:42139345]. "
            "Cryo-electron tomography shows AP-3 and ARF1 polymerising into spiralling arches "
            "on tubular membranes, which is a membrane coat in the literal sense. UniProt "
            "makes the same statement. Accepted."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={"InterPro:IPR000804": ("SUPPORTS_TRANSFER", (
                "Clathrin adaptor small-chain signature. The mapped CC term is deliberately "
                "coat-agnostic, so it survives the finding that AP-3 coats are "
                "clathrin-free."))},
            residue_claims_not_applicable="A complex/coat assignment, not a residue question.",
        ),
        supported_by=[Q_TUBULAR, Q_UP_COAT],
    ),

    8: dict(  # GO:0030123 AP-3 adaptor complex, IEA GO_REF:0000120
        summary=(
            "The automatic route to the same conclusion as the IDA row, and both halves of "
            "its evidence were checked and hold."),
        action="ACCEPT",
        reason=(
            "InterPro:IPR027155 is the APS3 signature, which is AP-3-sigma-specific. The "
            "other half, ARBA00033921, fires on FunFam 3.30.450.60:FF:000001 plus taxon "
            "Primates - the shape of rule that can over-generalise, because FunFam signatures "
            "carry family-level names. Tested against the complete set of reviewed human "
            "AP-complex sigma subunits, it does not: AP1S1 and AP1S3 carry FF:000005, AP1S2 "
            "FF:000009, AP2S1 FF:000004, AP4S1 FF:000010 and AP5S1 none at all, while only "
            "AP3S1 and AP3S2 carry FF:000001. Zero non-AP-3 subunits would be mis-called. The "
            "row is sound."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={
                "ARBA:ARBA00033921": ("SUPPORTS_TRANSFER", (
                    "Fetched from the UniProt ARBA service: conditions are FunFam "
                    "3.30.450.60:FF:000001 AND taxon Primates, asserting GO:0030123. The "
                    "FunFam discriminates - among the eight reviewed human AP-complex sigma "
                    "subunits only AP3S1 and AP3S2 carry it.")),
                "InterPro:IPR027155": ("SUPPORTS_TRANSFER", (
                    "APS3, the AP-3 sigma subunit signature, present on the target. "
                    "AP-3-specific, so it grounds the complex assignment directly.")),
            },
            residue_claims_not_applicable=(
                "The rule fires on a FunFam signature, not on individual residues; the check "
                "performed was of the signature's discriminating power."),
        ),
        supported_by=[Q_BIO_ARBA, Q_UP_FUNFAM, Q_COMPONENTS],
    ),

    9: dict(  # GO:0030659 cytoplasmic vesicle membrane, IEA SubCell
        summary=(
            "AP-3 is a peripheral membrane protein on the cytoplasmic face of coated vesicles; "
            "the UniProt record says so and the SubCell mapping reproduces it."),
        action="ACCEPT",
        reason=(
            "The location is intrinsic to what a coat adaptor is: it sits on the cytosolic "
            "leaflet of the carrier it coats, which the 2026 tomography visualises directly "
            "as rows of AP-3 arches on tubular membranes [PMID:42139345]. Accepted as a core "
            "location."),
        prop=dict(
            root_cause="NO_FAILURE_CORE",
            status={"UniProtKB-SubCell:SL-0089": ("SUPPORTS_TRANSFER", (
                "SubCell 'Cytoplasmic vesicle membrane', mapped from the UniProt SUBCELLULAR "
                "LOCATION line, whose Note describes the protein as a component of the coat "
                "on the cytoplasmic face of coated vesicles."))},
            residue_claims_not_applicable="A compartment assignment.",
        ),
        supported_by=[Q_UP_COAT, Q_TUBULAR],
    ),

    10: dict(  # GO:1904115 axon cytoplasm, IEA GO_REF:0000108
        summary=(
            "A mechanical inter-ontology inference off the anterograde axonal transport row; "
            "it inherits that row's grade rather than adding evidence of its own."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "GO_REF:0000108 derives a location from a process annotation: if the protein is "
            "involved in anterograde axonal transport, it is in the axon cytoplasm. The "
            "inference is valid, and AP-3 is genuinely present in neuronal processes, so the "
            "row is not wrong. But it is only as strong as its input, and that input is a "
            "complex-level, neuron-specific claim derived from a delta-subunit mutant "
            "[PMID:21998198]. Kept, non-core: a ubiquitously expressed Golgi/endosomal coat "
            "subunit is not characterised by its presence in axoplasm."),
        prop=dict(
            root_cause="NO_FAILURE_NON_CORE",
            status={"GO:0008089": ("SUPPORTS_TRANSFER", (
                "The source is a GO term, not a gene product: this row is a logical inference "
                "from AP3S2's own anterograde axonal transport annotation, which is reviewed "
                "on rows 12 and 24 and kept as non-core. The inference step itself is sound; "
                "its strength is inherited."))},
            residue_claims_not_applicable=(
                "An inter-ontology inference, with no sequence content to test."),
        ),
        supported_by=[Q_SV_COMPOSITION, Q_MOCHA],
    ),

    11: dict(  # GO:0008021 synaptic vesicle, IEA Ensembl from rat
        summary=(
            "Transferred from a rat synaptic-vesicle proteomic detection whose own authors "
            "list AP3 among endosomal 'visitor' proteins rather than vesicle residents "
            "[PMID:33376223]."),
        action="MARK_AS_OVER_ANNOTATED",
        reason=(
            "The ortholog transfer is mechanically fine - the donor is rat Ap3s2 - but the "
            "donor annotation is a mass-spectrometric detection in a purified synaptic-vesicle "
            "fraction, and the paper reporting it explicitly offers endosomal contamination "
            "and transient visitors as the explanation for AP3's presence. A qualifier of "
            "is_active_in asks for more than detection: it asks that the protein performs its "
            "function there. AP-3's function is to bud carriers from endosomal membranes, "
            "which is upstream of the mature vesicle. The detection is real and reproducible, "
            "so this is over-annotation rather than error; not removed."),
        prop=dict(
            root_cause="SOURCE_WEAK_OR_INFERRED",
            modes=["COMPARTMENT_OR_COMPLEX_MISMATCH"],
            status={
                "UniProtKB:A0A0G2K302": ("SOURCE_WEAK_OR_INFERRED", SRC_RAT),
                "ensembl:ENSRNOP00000072451": ("SOURCE_WEAK_OR_INFERRED", SRC_RAT_ENSEMBL),
            },
            residue_claims_not_applicable=(
                "A localisation over-call; nothing about it turns on sequence."),
        ),
        supported_by=[Q_SV_VISITOR, Q_ENDO_LYSO],
    ),

    12: dict(  # GO:0008089 anterograde axonal transport, IEA Ensembl from mouse
        summary=(
            "AP-3 packages synaptic cargo at neuronal cell bodies for delivery to nerve "
            "terminals, so its subunits participate in the process - but as the packaging "
            "step, not as the motor, and the underlying genetics is on the delta subunit."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "The donor is mouse Ap3s2, which is identical in sequence to the human protein, "
            "so there is no orthology objection at all. The mouse annotation traces to "
            "PMID:21998198, where the AP-3 loss is Ap3d1 mocha and the sigma subunit is "
            "detected with a pan-sigma-3 antibody - the same antibody class that resolves "
            "sigma-3A and sigma-3B only as a doublet [PMID:9151686]. The claim that reaches "
            "AP3S2 is therefore complex-level and neuronal. GO:0008089 is moreover defined as "
            "movement along microtubules from cell body to periphery, a motor-driven process "
            "in which a coat adaptor participates by loading the cargo rather than by moving "
            "it. Correct to keep, wrong to call core for a ubiquitously expressed subunit."),
        prop=dict(
            root_cause="NO_FAILURE_NON_CORE",
            modes=["CONTEXT_OR_TISSUE_MISMATCH"],
            status={
                "UniProtKB:Q8BSZ2": ("SUPPORTS_TRANSFER", SRC_MOUSE),
                "ensembl:ENSMUSP00000075082": ("SUPPORTS_TRANSFER", SRC_MOUSE_ENSEMBL),
            },
            residue_claims_not_applicable=(
                "Donor and target are the same sequence, so no residue divergence exists to "
                "argue from; the reservation is about experimental scope, not sequence."),
        ),
        supported_by=[Q_MOCHA, Q_PAN_SIGMA_AB, Q_UP_BLOC1, Q_BIO_IDENTICAL],
    ),

    13: dict(  # GO:0035651 AP-3 adaptor complex binding, IEA Ensembl from mouse
        summary=(
            "AP3S2 is not a binder of AP-3; it is a constituent of AP-3, which the same record "
            "already states experimentally as part_of GO:0030123 [PMID:9118953]."),
        action="MARK_AS_OVER_ANNOTATED",
        reason=(
            "GO:0035651 is defined as binding to an AP-3 adaptor complex. Applying it to a "
            "core subunit of that complex conflates being a part with binding a partner, and "
            "it adds nothing the part_of IDA row does not already say more precisely. The "
            "mouse source is an MGI IDA from a study that purified cross-linked AP-3 complexes "
            "and identified associated proteins by mass spectrometry [PMID:19010779] - an "
            "experiment in which a constituent subunit necessarily appears, so the curator's "
            "reading of the assay is not in question; what does not follow is that the subunit "
            "enables complex binding. Marked over-annotated rather than removed: the "
            "underlying observation is genuine and the ortholog transfer is faithful."),
        prop=dict(
            root_cause="TERM_SCOPING_PROBLEM",
            modes=["ROLE_CONFLATION"],
            status={
                "UniProtKB:Q8BSZ2": ("SUPPORTS_SOURCE_BUT_NOT_TARGET", (
                    "Mouse Ap3s2, identical in sequence to the human protein, so the ortholog "
                    "step is faultless. The problem is upstream of it: the donor term casts a "
                    "constituent subunit as a binder of its own complex.")),
                "ensembl:ENSMUSP00000075082": ("SUPPORTS_SOURCE_BUT_NOT_TARGET",
                                               SRC_MOUSE_ENSEMBL),
            },
            residue_claims_not_applicable=(
                "A part-versus-binder typing problem; no sequence claim is involved."),
        ),
        supported_by=[Q_CROSSLINK, Q_COMPONENTS, Q_SUBUNITS],
    ),

    14: dict(  # GO:0048490 anterograde synaptic vesicle transport, IEA Ensembl
        summary=(
            "The synaptic-vesicle-specific form of the axonal transport row, with the same "
            "source and the same limits."),
        action="KEEP_AS_NON_CORE",
        reason=NON_CORE_NEURONAL + (
            " The specific process - movement of synaptic vesicles along axonal microtubules "
            "to the presynapse - again describes motor-driven transport, whereas the AP-3 "
            "contribution demonstrated in the source is the loading of vesicle membrane "
            "proteins at the cell body [PMID:21998198]. Real, inherited, peripheral."),
        prop=dict(
            root_cause="NO_FAILURE_NON_CORE",
            modes=["CONTEXT_OR_TISSUE_MISMATCH"],
            status={
                "UniProtKB:Q8BSZ2": ("SUPPORTS_TRANSFER", SRC_MOUSE),
                "ensembl:ENSMUSP00000075082": ("SUPPORTS_TRANSFER", SRC_MOUSE_ENSEMBL),
            },
            residue_claims_not_applicable=(
                "Donor and target sequences are identical; the reservation is about "
                "experimental scope."),
        ),
        supported_by=[Q_SV_COMPOSITION, Q_ZNT3, Q_UP_BLOC1],
    ),

    15: dict(  # GO:0005769 early endosome, NAS
        summary=(
            "Early/recycling endosomal tubules are where AP-3 loads cargo, which the cited "
            "review states directly [PMID:23247405]."),
        action="ACCEPT",
        reason=(
            "This is the compartment modern work puts AP-3 in: cargo packaging occurs at "
            "early/recycling endosome-associated tubules, and the complex sorts from there to "
            "lysosomes and lysosome-related organelles [PMID:39705307]. The original "
            "localisation of the sigma-3-containing complex already showed peripheral "
            "structures alongside the TGN, some of them transferrin-receptor positive "
            "[PMID:9118953] - i.e. early/recycling endosomes. A ComplexPortal NAS is an "
            "author-statement-grade annotation made on the complex, but the statement is "
            "well founded and the subunit is in the complex. Core location."),
        supported_by=[Q_ENDOSOME_TUBULES, Q_TYROSINASE, Q_TGN],
    ),

    16: dict(  # GO:0016183 synaptic vesicle coating, NAS
        summary=(
            "The term means clathrin-coated pit formation at the presynaptic plasma membrane, "
            "which is not what AP-3 does and not what the cited paper reports."),
        action="MODIFY",
        reason=(
            "Read by its definition rather than its label, GO:0016183 is about the formation "
            "of clathrin-coated pits in the presynaptic membrane endocytic zone. AP-3 acts on "
            "endosomal membranes, and the cited paper measured the synaptic-vesicle content of "
            "ZnT3 and ClC-3 in beta-3 isoform knockout mice [PMID:15537701] - vesicle cargo "
            "composition, not presynaptic pit formation. Two further facts point away from the "
            "term: AP-3 does not copurify with clathrin-coated vesicles and builds its "
            "carriers without a clathrin lattice [PMID:42139345]. GO:0016182 synaptic vesicle "
            "budding from endosome names the step AP-3 is actually credited with and keeps the "
            "annotation in the synaptic-vesicle domain the source paper is about. Two caveats "
            "on the replacement. It is as neuronal and as complex-level as the GO:0008089, "
            "GO:0048490 and GO:0036465 rows this review grades KEEP_AS_NON_CORE, and it should "
            "be read with the same reservation - MODIFY cannot carry the non-core marker, so "
            "it is stated here instead. And GO:0035459 vesicle cargo loading, the replacement "
            "chosen on the GO:0035654 row, arguably matches the cited paper's actual readout "
            "more literally, since it measured vesicle cargo content rather than budding; "
            "GO:0016182 is preferred because it keeps the annotation in the synaptic-vesicle "
            "branch, which is the whole point of the original term, and because endosomal "
            "budding is the step AP-3 is independently credited with in neurons."),
        replace=[("GO:0016182", "synaptic vesicle budding from endosome")],
        supported_by=[Q_ZNT3, Q_SV_LEVELS, Q_NO_CCV, Q_NO_CLATHRIN],
    ),

    17: dict(  # GO:0016192 vesicle-mediated transport, NAS
        summary=(
            "The same correct process term as the IBA and InterPro rows, asserted at complex "
            "level by ComplexPortal."),
        action="ACCEPT",
        reason=(
            "AP-3 loads cargo into vesicles and transport intermediates at endosomal tubules "
            "[PMID:23247405] and polymerises with ARF1 into membrane-deforming coats "
            "[PMID:42139345]. Vesicle-mediated transport is the process, and sigma-3B is in "
            "the complex. Duplicate evidence for a term is not a defect."),
        supported_by=[Q_ENDOSOME_TUBULES, Q_TUBULAR],
    ),

    18: dict(  # GO:0030123 AP-3 adaptor complex, NAS PMID:9151686
        summary=(
            "The second 1997 paper to identify sigma-3 as an AP-3 subunit, with antibodies "
            "raised separately against sigma-3A and sigma-3B [PMID:9151686]."),
        action="ACCEPT",
        reason=(
            "Simpson et al. cloned sigma-3B independently, raised an antibody against it, and "
            "showed by reciprocal immunoprecipitation from brain cytosol that the sigma-3 "
            "chains are subunits of the adaptor-like complex; the sigma-3 signal in the delta "
            "and beta-3 immunoprecipitates runs as a doublet because both isoforms are "
            "present. The GO definition of the term names sigma3A and sigma3B as alternative "
            "occupants of the sigma slot, so the annotation matches the term exactly. Core, "
            "and independent of the IDA row's evidence."),
        supported_by=[Q_SUBUNITS, Q_DOUBLET, Q_SIGMA_IP],
    ),

    19: dict(  # GO:0035654 clathrin-coated vesicle cargo loading, AP-3-mediated, NAS
        summary=(
            "Cargo loading by AP-3 is exactly what sigma-3B contributes to; the "
            "clathrin-coated-vesicle half of the term is the part that has since been "
            "overturned [PMID:42139345]."),
        action="MODIFY",
        reason=(
            "The term is defined as the formation of a complex between AP-3 subunits and the "
            "proteins that will be transported by a clathrin-coated vesicle. The first half is "
            "the best available description of what a sigma subunit does: it supplies the "
            "pockets that receive a dileucine sorting signal [PMID:21097499, PMID:39705307]. "
            "The second half rests on the 1998 finding that AP-3 binds clathrin through the "
            "beta-3 appendage [PMID:9545220], which became consensus by 2013 [PMID:23247405] "
            "and has now been reversed: AP-3 does not copurify with clathrin-coated vesicles, "
            "and reconstituted AP3:ARF1 builds carriers with no clathrin lattice at all "
            "[PMID:42139345]. UniProt already describes the complex as not clathrin-associated. "
            "GO:0035459 vesicle cargo loading is the same assertion with the superseded "
            "commitment removed. The alternative was considered and rejected: keeping "
            "GO:0035654 and pursuing the definition fix would preserve AP-3 specificity, and "
            "that fix is proposed in proposed_new_terms and knowledge_gaps. It is not the "
            "right call for this row, because an annotation should not assert a mechanism its "
            "own evidence contradicts while the ontology catches up; generalising loses "
            "granularity, whereas keeping it would keep a falsehood."),
        replace=[("GO:0035459", "vesicle cargo loading")],
        supported_by=[Q_CLATHRIN_1998, Q_NO_CCV, Q_NO_CLATHRIN, Q_UP_NOT_CLATHRIN,
                      Q_TMEM163_MOTIF, Q_TMEM163_CARGO],
    ),

    20: dict(  # GO:0036465 synaptic vesicle recycling, NAS
        summary=(
            "AP-3 regenerates synaptic vesicles from endosomes and sets their membrane protein "
            "content, which is part of the recycling cycle but is neuronal and complex-level."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "The cited paper shows that removing either the ubiquitous or the neuronal AP-3 "
            "changes the synaptic-vesicle content of ZnT3 and ClC-3, and concludes that the "
            "two complexes control the levels of selected membrane proteins in synaptic "
            "vesicles [PMID:15537701]. That places AP-3 in the endosomal arm of synaptic "
            "vesicle recycling, so the term is defensible for the complex. It is not a core "
            "function of a ubiquitously expressed sigma subunit: the isoform variable in that "
            "paper is beta-3, and nothing there distinguishes sigma-3B from sigma-3A."),
        supported_by=[Q_BETA3_ISOFORMS, Q_ZNT3, Q_SV_LEVELS],
    ),

    21: dict(  # GO:0060155 platelet dense granule organization, NAS
        summary=(
            "A genuine AP-3 function in a specialised cell type: dense granules are "
            "lysosome-related organelles, and AP-3 subunit mutations disrupt them in "
            "Hermansky-Pudlak syndrome [PMID:23247405]."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "AP-3 belongs to the machinery that builds lysosome-related organelles, and HPS "
            "patients and models carrying AP-3 subunit mutations have abnormal platelet dense "
            "granules alongside abnormal melanosomes and lamellar bodies. The annotation is "
            "therefore right about the complex. It is cell-type restricted and is one "
            "downstream output of the generic endosome-to-lysosome sorting activity rather "
            "than a distinct function, and no sigma-3B-specific evidence exists for it; "
            "non-core."),
        supported_by=[Q_HPS, Q_HPS_SUBUNITS, Q_TMEM163_PLATELET, Q_TMEM163_CARGO],
    ),

    22: dict(  # GO:1903232 melanosome assembly, NAS
        summary=(
            "The best-worked example of AP-3's lysosome-related-organelle role: tyrosinase and "
            "TYRP1 are packaged at endosomal tubules for delivery to maturing melanosomes "
            "[PMID:23247405]."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "Melanosome biogenesis depends on AP-3 acting with AP-1 and the BLOC complexes at "
            "early/recycling endosomal tubules, and loss of AP-3 produces a partial "
            "pigmentation defect. The complex-level claim is solid. As with the platelet "
            "dense granule row it is a specialised, cell-type-restricted expression of the "
            "same cargo-sorting activity, and is graded non-core for that reason rather than "
            "because it is doubted."),
        supported_by=[Q_TYROSINASE, Q_ENDOSOME_TUBULES, Q_HPS_SUBUNITS],
    ),

    23: dict(  # GO:0030123 AP-3 adaptor complex, IDA PMID:9118953
        summary=(
            "The one experimental annotation this gene has, and it is correct: sigma-3B was "
            "identified biochemically as a component of AP-3 [PMID:9118953]."),
        action="ACCEPT",
        reason=(
            "Dell'Angelica et al. cloned both human sigma-3 paralogs, raised antibodies, and "
            "showed by Western blot and immunoprecipitation that sigma-3A and sigma-3B are "
            "components of a large complex containing 47, 140 and 160 kDa chains, which they "
            "named AP-3. The GO term's definition names sigma3A and sigma3B explicitly as the "
            "alternative occupants of the sigma slot, so term and evidence match without "
            "interpretation. This is the anchor of the whole review and the core cellular "
            "component assignment. The identical row is assigned to AP3S1 from the same "
            "paper, which is correct - the paper identified both."),
        supported_by=[Q_COMPONENTS, Q_EXPRESSED, Q_TYROSINE],
    ),

    24: dict(  # GO:0008089 anterograde axonal transport, ISS
        summary=(
            "A manual ortholog transfer from mouse Ap3s2 - a paralogy-free transfer between "
            "sequence-identical proteins - carrying a complex-level neuronal claim."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "It is worth being explicit that the donor here is the mouse ortholog and not the "
            "within-species paralog AP3S1: no row in this gene's record transfers from AP3S1. "
            "Human and mouse AP3S2 are identical across all 193 residues, so the similarity "
            "premise of an ISS is satisfied about as completely as it can be, and a "
            "paralog-confusion objection does not arise. What limits the row is the donor "
            "evidence, not the transfer: the mouse IMP comes from Ap3d1 mocha brains probed "
            "with a pan-sigma-3 antibody [PMID:21998198], so it is a statement about neuronal "
            "AP-3. Kept as non-core, for the same reason as the Ensembl row for this term."),
        prop=dict(
            root_cause="NO_FAILURE_NON_CORE",
            modes=["CONTEXT_OR_TISSUE_MISMATCH"],
            status={"UniProtKB:Q8BSZ2": ("SUPPORTS_TRANSFER", SRC_MOUSE)},
            residue_claims_not_applicable=(
                "Donor and target are the same 193-residue sequence, so there is no residue "
                "difference on which a transfer objection could rest."),
        ),
        supported_by=[Q_BIO_IDENTICAL, Q_MOCHA, Q_PAN_SIGMA_AB],
    ),

    25: dict(  # GO:0048490 anterograde synaptic vesicle transport, ISS
        summary=(
            "The synaptic-vesicle form of the same manual mouse-to-human transfer, with the "
            "same strengths and the same ceiling."),
        action="KEEP_AS_NON_CORE",
        reason=(
            "Donor is mouse Ap3s2, sequence-identical to the human protein; the transfer step "
            "is unimpeachable. The donor annotation is a complex-level neuronal result "
            "[PMID:21998198], and the term names a microtubule-motor process rather than the "
            "cargo-loading step AP-3 performs. Real but peripheral for this gene."),
        prop=dict(
            root_cause="NO_FAILURE_NON_CORE",
            modes=["CONTEXT_OR_TISSUE_MISMATCH"],
            status={"UniProtKB:Q8BSZ2": ("SUPPORTS_TRANSFER", SRC_MOUSE)},
            residue_claims_not_applicable=(
                "Identical donor and target sequences; the reservation is about the scope of "
                "the donor experiment."),
        ),
        supported_by=[Q_BIO_IDENTICAL, Q_SV_COMPOSITION, Q_ZNT3],
    ),
}

# --------------------------------------------------------------------------
# NEW rows
# --------------------------------------------------------------------------

NEW_ROWS = [
    dict(
        term=("GO:0030674", "protein-macromolecule adaptor activity"),
        evidence_type="IPI",
        qualifier="contributes_to",
        reference="PMID:14691137",
        supporting_entities=["UniProtKB:O14617", "UniProtKB:Q14108"],
        summary=(
            "The activity the gene actually performs and that its GO record does not record "
            "at all: as part of a delta-sigma3B hemicomplex, sigma-3B brings a cargo protein's "
            "sorting signal into the AP-3 coat."),
        reason=(
            "AP3S2's molecular function is unrepresented in GOA - the only MF row it carries "
            "is AP-3 adaptor complex binding, which mis-types a constituent as a binder. The "
            "activity that is documented is cargo selection: acidic dileucine signals bind no "
            "single AP subunit but a composite site formed by the large and small chains "
            "together [PMID:21097499], and Janvier et al. cloned sigma-3A and sigma-3B "
            "separately and showed in a yeast three-hybrid assay that the LIMP-II cytosolic "
            "tail interacts with delta-sigma3B as well as with delta-sigma3A and "
            "gamma1-sigma1A, with the same three residues of the signal required in each case "
            "[PMID:14691137]. Sequence analysis confirms the structural basis transfers from "
            "the paralog: sigma-3A Val94 and Leu109, whose substitution abolishes signal "
            "binding, are present unchanged at the same positions in sigma-3B "
            "[file:human/AP3S2/AP3S2-bioinformatics/RESULTS.md]. The qualifier is "
            "contributes_to because the binding site is shared with delta and the coat "
            "function belongs to the tetramer. GO:0035615 clathrin-cargo adaptor activity, "
            "which the AP-1 sigma subunits use, is not available here: its definition commits "
            "to clathrin and to endocytic vesicles, and AP-3 builds carriers without a "
            "clathrin lattice [PMID:42139345]. GO:0030674 is the nearest term that states the "
            "adaptor activity without importing a contradicted mechanism; the precise activity "
            "- binding a dileucine sorting signal - has no GO term and is proposed as a new "
            "one. The IPI interactors are recorded: UniProtKB:O14617 (AP3D1, the delta chain "
            "that forms the hemicomplex) and UniProtKB:Q14108 (SCARB2/LIMP-II, whose cytosolic "
            "tail is the bait)."),
        supported_by=[Q_Y3H, Q_ALASCAN, Q_CLONED_SEPARATELY, Q_COMPOSITE, Q_RESIDUES,
                      Q_BIO_POCKET, Q_NO_CLATHRIN],
    ),
    dict(
        term=("GO:0005198", "structural molecule activity"),
        evidence_type="IC",
        qualifier="enables",
        reference="PMID:9118953",
        summary=(
            "Sigma-3B occupies the small-chain position of the AP-3 heterotetramer and holds "
            "that position in the assembled complex."),
        reason=(
            "Inferred by curator from this gene's own experimentally supported part_of "
            "GO:0030123 row: sigma-3B is one of the four chains of AP-3 [PMID:9118953], and a "
            "core subunit of a heterotetramer contributes to the structural integrity of that "
            "complex, which is what GO:0005198 states. Independent support that the subunit "
            "participates in forming the complex rather than merely copurifying with it comes "
            "from the yeast three-hybrid reconstitution, in which the LIMP-II interaction is "
            "read out only when delta and sigma-3B are co-expressed [PMID:14691137], and from "
            "the cryo-EM core, where sigma-3's pocket is capped by the beta-3 N-terminal "
            "extension - an intersubunit contact [PMID:39705307]."),
        supported_by=[Q_COMPONENTS, Q_SUBUNITS, Q_Y3H, Q_POCKET_OCCLUDED],
    ),
]

# --------------------------------------------------------------------------
# Description
# --------------------------------------------------------------------------

DESCRIPTION = (
    "AP3S2 encodes sigma-3B (also called sigma-2), one of the two interchangeable small "
    "subunits of adaptor protein complex 3 (AP-3), the heterotetrameric coat adaptor that "
    "selects transmembrane cargo for delivery from endosomes to lysosomes and to "
    "lysosome-related organelles such as melanosomes, platelet dense granules and lung "
    "lamellar bodies. AP-3 comprises two large adaptins (delta and beta-3), a medium adaptin "
    "(mu-3A or mu-3B) and a single small adaptin, which in human cells is either sigma-3A or "
    "sigma-3B, so the sigma-3B form is a variant of the same machine rather than a separate "
    "one. The complex is cytosolic at rest and is recruited onto endosomal membranes by "
    "ARF1-GTP acting principally through the delta subunit, together with phosphoinositides; "
    "it then polymerises with ARF1 into spiralling arrays that deform the membrane into "
    "tubular carriers. Unlike AP-1 and AP-2, AP-3 builds those carriers without a clathrin "
    "lattice.\n\n"
    "Within the complex the sigma subunit supplies half of the composite site that reads "
    "acidic dileucine sorting signals in the cytosolic tails of cargo proteins. Such signals "
    "bind neither the delta nor the sigma chain alone but the delta-sigma3 hemicomplex, and "
    "the hydrophobic pockets that receive the motif's two bulky residues lie on sigma: in "
    "sigma-3A, substituting Val94 or Leu109 abolishes signal binding, and sigma-3B carries "
    "both residues unchanged at the same positions. A delta-sigma3B hemicomplex binds the "
    "dileucine signal of the lysosomal membrane protein LIMP-II with the same sequence "
    "requirements as its sigma-3A counterpart. In the resting complex that pocket is capped "
    "by the N-terminal extension of beta-3, and cargo binding is part of what opens the "
    "complex up. Sigma-3B is a 193-residue longin/roadblock-fold protein with no catalytic "
    "activity; it is expressed in every adult tissue examined, and it is identical in "
    "sequence to its mouse ortholog.\n\n"
    "The biology AP-3 carries out through this subunit is cargo-specific rather than "
    "organelle-generic. In neurons it packages synaptic-vesicle membrane proteins such as "
    "ZnT3 and ClC-3 at cell bodies for delivery to nerve terminals; in pigment cells it routes "
    "tyrosinase and TYRP1 from early and recycling endosomal tubules to maturing melanosomes; "
    "and mutations in AP-3 subunits cause Hermansky-Pudlak syndrome, with abnormal "
    "melanosomes, platelet dense granules and lung lamellar bodies. What is not known is "
    "anything that distinguishes the sigma-3B form of AP-3 from the sigma-3A form: no cargo, "
    "tissue, phenotype or structure separates them."
)

# --------------------------------------------------------------------------
# Core functions
# --------------------------------------------------------------------------

CORE_FUNCTIONS = [
    {
        "description": (
            "Sigma-3B is the cargo-reading small chain of one of the two ubiquitous AP-3 "
            "variants. Within the assembled tetramer on endosomal membranes it supplies the "
            "hydrophobic pockets of the composite site that captures acidic dileucine sorting "
            "signals, thereby selecting transmembrane cargo for packaging into the "
            "clathrin-independent carriers AP-3 builds with ARF1, and routing that cargo from "
            "endosomes to lysosomes and lysosome-related organelles. The adaptor activity "
            "belongs to the complex rather than to this chain - the signal binds the "
            "delta-sigma3 pair, not either subunit alone - which is why it is recorded as a "
            "contribution. Structural molecule activity is the subunit-level function because "
            "it is the only one GO can currently express for this protein: the activity it "
            "performs on the cargo side, binding a dileucine sorting signal, has no GO term "
            "and is proposed here as a new one. Note that GO:0035615 clathrin-cargo adaptor "
            "activity, used for the AP-1 sigma subunits, is deliberately not used: its "
            "definition requires clathrin and endocytic vesicles, and AP-3 carriers have "
            "neither."),
        "molecular_function": {"id": "GO:0005198", "label": "structural molecule activity"},
        "contributes_to_molecular_function": {
            "id": "GO:0030674", "label": "protein-macromolecule adaptor activity"},
        "in_complex": {"id": "GO:0030123", "label": "AP-3 adaptor complex"},
        "directly_involved_in": [
            {"id": "GO:0016192", "label": "vesicle-mediated transport"},
            {"id": "GO:0006886", "label": "intracellular protein transport"},
            {"id": "GO:0008333", "label": "endosome to lysosome transport"},
            {"id": "GO:0035459", "label": "vesicle cargo loading"},
        ],
        "locations": [
            {"id": "GO:0005769", "label": "early endosome"},
            {"id": "GO:0030659", "label": "cytoplasmic vesicle membrane"},
            {"id": "GO:0005794", "label": "Golgi apparatus"},
        ],
        "supported_by": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_COMPONENTS, Q_Y3H, Q_ALASCAN, Q_COMPOSITE, Q_RESIDUES, Q_BIO_POCKET,
             Q_POCKET_OCCLUDED, Q_ENDO_LYSO, Q_NO_CLATHRIN, Q_ENDOSOME_TUBULES, Q_UP_COAT,
             Q_TMEM163_MOTIF, Q_AFFINAGE_LIMIT]
        ],
        "knowledge_gaps": [
            {
                "gap_statement": (
                    "No GO term expresses what the sigma subunit does on the cargo side - bind "
                    "an acidic dileucine sorting signal - and for AP-3 there is not even a "
                    "usable complex-level substitute, because the one GO offers commits to "
                    "clathrin."),
                "boundary": (
                    "The activity itself is settled. Dileucine signals bind the delta-sigma3 "
                    "hemicomplex and not either chain alone; the pockets are on sigma; "
                    "substituting sigma-3A Val94 or Leu109 abolishes binding; sigma-3B was "
                    "tested directly and behaves like sigma-3A; and a cryo-EM structure shows "
                    "the pocket on sigma-3 occluded in the resting complex. GO has the "
                    "tyrosine-motif counterpart (GO:0089710) and a clathrin-committed "
                    "complex-level term (GO:0035615). Only the dileucine term, and a "
                    "coat-agnostic parent of GO:0035615, are missing."),
                "gap_kind": ["ONTOLOGY"],
                "dark_aspect": "MF_DARK",
                "status": "OPEN",
                "significance": (
                    "Cargo-signal recognition is what makes an adaptor an adaptor. Without a "
                    "term for it, a subunit that selects cargo and a subunit that merely holds "
                    "the complex together look identical in GO, and the AP-3 case is worse "
                    "than the AP-1 case because the only complex-level term available names a "
                    "coat AP-3 does not use."),
                "resolution": (
                    "Create 'dileucine sorting signal binding' as a sibling of GO:0089710, and "
                    "a coat-agnostic parent for GO:0035615 so that non-clathrin coat adaptors "
                    "have somewhere to go. Both are proposed in proposed_new_terms."),
                "provenance": [
                    {"reference_id": r, "supporting_text": t} for r, t in
                    [Q_COMPOSITE, Q_RESIDUES, Q_Y3H, Q_NO_CLATHRIN]
                ],
            },
        ],
    },
]

# --------------------------------------------------------------------------
# Proposed new terms
# --------------------------------------------------------------------------

PROPOSED_NEW_TERMS = [
    {
        "proposed_name": "dileucine sorting signal binding",
        "proposed_definition": (
            "Binding to an acidic dileucine sorting signal, a [DE]XXXL[LI] peptide motif in "
            "the cytosolic tail of a transmembrane cargo protein, which directs that protein "
            "into carriers formed by heterotetrameric adaptor protein complexes."),
        "justification": (
            "GO can express the tyrosine-motif counterpart read by the medium adaptin "
            "(GO:0089710 endocytic targeting sequence binding, whose definition requires an "
            "essential tyrosine), but it has no term for the dileucine motif read by the "
            "small adaptin together with the large one. The result is that the one activity a "
            "sigma subunit demonstrably participates in cannot be stated: AP3S2's only "
            "molecular-function row in GOA is AP-3 adaptor complex binding, which describes "
            "the protein as binding the complex it is part of. The gap is not speculative - "
            "the site is mapped by substitution in all three complexes, and sigma-3B itself "
            "was assayed. The absence was checked against the GO release served by QuickGO by "
            "retrieving the definitions of GO:0035615, GO:0089710, GO:0060090, GO:0030674, "
            "GO:0038024 and GO:0035459; none of them names a dileucine or sorting-signal "
            "binding activity."),
        "proposed_parent": {"id": "GO:0005515", "label": "protein binding"},
        "supported_by": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_COMPOSITE, Q_RESIDUES, Q_Y3H, Q_ALASCAN, Q_POCKET_OCCLUDED, Q_TMEM163_MOTIF]
        ],
    },
    {
        "proposed_name": "coat-cargo adaptor activity",
        "proposed_definition": (
            "Bringing together a cargo protein and a membrane coat, thereby selecting that "
            "cargo for incorporation into a coated transport carrier."),
        "justification": (
            "GO:0035615 clathrin-cargo adaptor activity is the term GO uses for AP-complex "
            "cargo selection, but its definition - bringing a cargo protein together with "
            "clathrin, responsible for the formation of endocytic vesicles - has two "
            "commitments that AP-3 does not meet. AP-3 does not copurify with clathrin-coated "
            "vesicles and reconstituted AP3:ARF1 forms carriers with no clathrin lattice, "
            "which is now offered as the explanation for the clathrin independence of "
            "AP-3-mediated trafficking; and AP-3 acts on endosomes, not in endocytosis. UniProt "
            "already describes AP-3 as not clathrin-associated. The consequence is that the "
            "AP-3 subunits have no complex-level cargo-adaptor term at all and fall back on "
            "GO:0030674 protein-macromolecule adaptor activity, which does not say that the "
            "partner is a coat. A coat-agnostic parent, with GO:0035615 as its clathrin child, "
            "would serve AP-3 and AP-4 as well as any other non-clathrin coat adaptor. The "
            "same revision would fix GO:0035654, whose definition asserts that AP-3 loads "
            "cargo into clathrin-coated vesicles."),
        "proposed_parent": {"id": "GO:0060090", "label": "molecular adaptor activity"},
        "supported_by": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_NO_CCV, Q_NO_CLATHRIN, Q_TUBULAR, Q_UP_NOT_CLATHRIN]
        ],
    },
]

# --------------------------------------------------------------------------
# Knowledge gaps
# --------------------------------------------------------------------------

KNOWLEDGE_GAPS = [
    {
        "gap_statement": (
            "Nothing is known that distinguishes the sigma-3B form of AP-3 from the sigma-3A "
            "form. No cargo has been found that one selects and the other does not, no tissue "
            "or cell type is known to use one preferentially, and no phenotype has been "
            "assigned to loss of either paralog individually."),
        "boundary": (
            "What is established is that both paralogs exist, that both are incorporated into "
            "AP-3, and that both are expressed ubiquitously - measured by Northern and Western "
            "blot in 1997 and confirmed by a second group in the same year, with sigma-3 "
            "appearing as a two-isoform doublet in AP-3 immunoprecipitates. Combinatorial "
            "assembly would in principle give eight AP-3 variants from the beta-3, mu-3 and "
            "sigma-3 pairs, and the field has said in print that it does not know whether "
            "these variants occur in cells or differ functionally. Human AP3S2 also "
            "co-purifies with both mu-3 paralogs in high-throughput affinity-purification "
            "interactomes, so sigma-3B is not restricted to one mu-3 variant."),
        "gap_kind": ["BIOLOGY"],
        "dark_aspect": "RESIDUAL_SUBGAP",
        "status": "OPEN",
        "significance": (
            "This is the question that decides whether AP3S2 deserves any annotation of its "
            "own beyond the complex's. Every process and location term it now carries is "
            "inherited from AP-3; if the paralogs are fully redundant, that inheritance is the "
            "whole truth about the gene, and if they are not, the annotations are silently "
            "attributing sigma-3A results to sigma-3B."),
        "resolution": (
            "Comparative proteomics of AP-3 cargo in cells expressing only one sigma-3 paralog "
            "at a time, paired with quantification of the two proteins (not transcripts) "
            "across tissues, would either name the discriminating cargo or establish that the "
            "difference is quantitative."),
        "provenance": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_NOT_KNOWN, Q_TWO_SIGMA3, Q_UBIQUITOUS, Q_DOUBLET]
        ],
    },
    {
        "gap_statement": (
            "No structure, knockout, knockdown, patient allele or cargo screen has ever used "
            "sigma-3B. Every mechanistic statement about the AP-3 sigma subunit in the "
            "structural literature is an observation on sigma-3A that is assumed to transfer."),
        "boundary": (
            "The assumption is well supported but has been tested only in silico here: the two "
            "paralogs are 83.9% identical, and the two residues whose substitution abolishes "
            "dileucine-signal binding in sigma-3A are present unchanged at the same positions "
            "in sigma-3B, with only four differences anywhere in the 46-residue window around "
            "them. The single functional assay ever performed on sigma-3B - a yeast "
            "three-hybrid with the LIMP-II tail - gave the same result as sigma-3A. What is "
            "missing is any measurement on the sigma-3B protein itself: no affinity, no "
            "structure, no cellular phenotype."),
        "gap_kind": ["BIOLOGY", "CURATION"],
        "dark_aspect": "MF_DARK",
        "status": "NARROWING",
        "significance": (
            "The whole GO record for this gene rests on the transfer holding. A quantitative "
            "difference in cargo affinity between the paralogs, of the kind seen among the "
            "AP-1 sigma variants, would not be visible in any current annotation."),
        "resolution": (
            "Reconstitute delta-sigma3B alongside delta-sigma3A and measure binding to a panel "
            "of dileucine cargo tails; or solve the AP-3 core with sigma-3B substituted for "
            "sigma-3A, which is a single-subunit swap in an already-published expression "
            "system."),
        "provenance": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_STRUCT_USED_AP3S1, Q_Y3H, Q_BIO_POCKET, Q_RESIDUES]
        ],
    },
    {
        "gap_statement": (
            "The reason AP3S2 appears in the literature at all - a type 2 diabetes association "
            "at 15q26 - has never been connected to AP-3 function, and the evidence available "
            "points away from AP3S2 being the effector gene."),
        "boundary": (
            "The association itself is solid and has replicated in several populations. What "
            "is absent is any causal link to the protein: the lead variant rs2028299 is an "
            "eQTL for the neighbouring C15orf38 rather than for AP3S2, a second gene at the "
            "locus (PLIN1) is an equally plausible candidate on biological grounds, and the "
            "locus additionally produces a C15orf38-AP3S2 readthrough transcript, which UniProt "
            "lists among this entry's alternative products. The gene is pharmacologically dark "
            "and is not commonly required in CRISPR screens."),
        "gap_kind": ["BIOLOGY"],
        "dark_aspect": "BP_DARK",
        "status": "OPEN",
        "significance": (
            "A locus name is repeatedly read as a gene function. If AP-3 really does act in "
            "insulin-granule or adipocyte trafficking it would be a genuine biological process "
            "annotation for this subunit; if the effector is C15orf38 or PLIN1, then none of "
            "the diabetes literature should ever inform this gene's curation."),
        "resolution": (
            "Fine-mapping with allele-specific expression in pancreatic islet and adipocyte "
            "models, plus a test of whether the readthrough transcript produces a protein, "
            "would assign the effector. A direct test of AP-3 requirement for insulin granule "
            "biogenesis would settle the functional half independently of the locus."),
        "provenance": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_T2D_LOCUS, Q_T2D_C15ORF38, Q_T2D_PLIN1, Q_UP_READTHROUGH, Q_UP_TDARK, Q_UP_ORCS]
        ],
    },
    {
        "gap_statement": (
            "Whether AP-3's documented clathrin binding has any residual physiological role is "
            "unresolved, and GO currently encodes the superseded answer."),
        "boundary": (
            "The 1998 in vitro result is not disputed: the beta-3 appendage binds the clathrin "
            "heavy chain N-terminal domain, and AP-3 colocalises with clathrin by microscopy. "
            "By 2013 this was the consensus reading. The 2026 reconstitution shows AP3:ARF1 "
            "deforming membranes into coated tubules with no clathrin present, and notes that "
            "AP-3 does not copurify with clathrin-coated vesicles. Both observations stand; "
            "what is unsettled is whether the clathrin interaction does anything in cells."),
        "gap_kind": ["BIOLOGY", "ONTOLOGY"],
        "dark_aspect": "BP_DARK",
        "status": "NARROWING",
        "significance": (
            "GO:0035654 asserts in its definition that AP-3 loads cargo into clathrin-coated "
            "vesicles, so every gene annotated to it - including this one - carries a "
            "mechanism the field has moved away from. The annotation cannot be fixed at the "
            "gene level alone."),
        "resolution": (
            "A clathrin-box mutation in beta-3, assayed for AP-3-dependent cargo delivery in "
            "cells, would decide the biology; on the ontology side, revising GO:0035654 or "
            "migrating its annotations to GO:0035459 would decouple the two questions."),
        "provenance": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_CLATHRIN_1998, Q_CLATHRIN_2013, Q_NO_CCV, Q_NO_CLATHRIN]
        ],
    },
    {
        "gap_statement": (
            "It is not known which cargoes the ubiquitous, non-neuronal, non-pigment-cell "
            "AP-3 delivers, so the function of this ubiquitously expressed subunit in the "
            "tissues where it is most abundant is uncharacterised."),
        "boundary": (
            "The characterised AP-3 cargoes come from specialised systems: ZnT3 and ClC-3 in "
            "neurons, tyrosinase and TYRP1 in melanocytes, LAMP1 and PI4KIIalpha in cell "
            "lines. Sigma-3B, by contrast, is present in all adult tissues examined, has low "
            "tissue specificity in Human Protein Atlas, and its protein is detected by "
            "proteomics. Human affinity-purification data place it in complexes with a list of "
            "lysosomal and endolysosomal membrane transporters, which are candidate cargoes "
            "rather than established ones."),
        "gap_kind": ["BIOLOGY"],
        "dark_aspect": "BP_DARK",
        "status": "OPEN",
        "significance": (
            "All of this gene's process annotations are neuronal or pigment-cell specific and "
            "are graded non-core for that reason, which leaves the ubiquitous function - the "
            "one that matches the expression pattern - with no annotation at all."),
        "resolution": (
            "Quantitative proteomics of AP-3-coated carriers isolated from a non-specialised "
            "cell line, compared with AP3S1/AP3S2 double-depleted cells, would define the "
            "ubiquitous cargo set."),
        "provenance": [
            {"reference_id": r, "supporting_text": t} for r, t in
            [Q_UP_TISSUE, Q_UP_HPA, Q_UP_PROTEIN_LEVEL, Q_ZNT3, Q_TYROSINASE]
        ],
    },
]

# --------------------------------------------------------------------------
# Questions and experiments
# --------------------------------------------------------------------------

SUGGESTED_QUESTIONS = [
    {
        "question": (
            "Do delta-sigma3A and delta-sigma3B hemicomplexes differ quantitatively in "
            "affinity or specificity for dileucine cargo tails, as the AP-1 gamma-sigma1 "
            "variants do, or are they interchangeable?"),
        "experts": ["Bonifacino J.S.", "Mattera R.", "Janvier K."],
    },
    {
        "question": (
            "Is the sigma slot of AP-3 filled stochastically in a given cell, or do sigma-3A "
            "and sigma-3B partition between distinct AP-3 populations - for example between "
            "the beta-3A and beta-3B complexes, or between different endosomal subdomains?"),
        "experts": ["Robinson M.S.", "Faundez V.", "Dell'Angelica E.C."],
    },
    {
        "question": (
            "Given that reconstituted AP3:ARF1 forms carriers without clathrin, does the "
            "beta-3 clathrin box do anything in cells, and should GO:0035654 continue to "
            "assert that AP-3 loads cargo into clathrin-coated vesicles?"),
        "experts": ["Owen D.J.", "Kaufman J.G.G.", "Baker R.W."],
    },
    {
        "question": (
            "Is AP3S2 the effector gene at the 15q26 type 2 diabetes locus, or is the signal "
            "carried by C15orf38, by the C15orf38-AP3S2 readthrough, or by PLIN1?"),
        "experts": ["Kooner J.S.", "Chambers J.C."],
    },
]

SUGGESTED_EXPERIMENTS = [
    {
        "hypothesis": (
            "Sigma-3B and sigma-3A confer indistinguishable dileucine-cargo specificity on "
            "AP-3."),
        "description": (
            "Express and purify the human AP-3 core twice, once with AP3S1 and once with "
            "AP3S2, using the published baculovirus construct set in which the sigma subunit "
            "is a single interchangeable component. Measure binding to a panel of dileucine "
            "cargo tails (LIMP-II, TMEM163, RNF13, LAMP1) by surface plasmon resonance or "
            "isothermal titration calorimetry. A difference in any tail would be the first "
            "functional distinction between the paralogs; identity across the panel would "
            "justify treating the AP3S1 literature as transferable and would close the "
            "largest gap in this gene's record."),
    },
    {
        "hypothesis": (
            "The two sigma-3 paralogs are individually dispensable but jointly essential for "
            "AP-3-dependent cargo delivery."),
        "description": (
            "Generate single and double AP3S1/AP3S2 knockouts in a non-specialised human cell "
            "line and assay AP-3-dependent trafficking (LAMP1 and PI4KIIalpha distribution, "
            "delivery of a dileucine-tagged reporter to lysosomes) alongside AP-3 complex "
            "integrity by blue-native gel. Single knockouts that are silent and a double "
            "knockout that phenocopies AP3D1 loss would establish redundancy directly, which "
            "is currently assumed rather than shown."),
    },
    {
        "hypothesis": (
            "Sigma-3B occupies AP-3 complexes containing either mu-3 paralog and either beta-3 "
            "paralog, rather than partitioning into a defined subset."),
        "description": (
            "Endogenously tag AP3S1 and AP3S2 with distinguishable epitopes in the same cell "
            "line and in primary neurons, then determine the beta-3 and mu-3 composition of "
            "each purified complex by quantitative mass spectrometry. This tests the "
            "combinatorial-assembly hypothesis directly, on endogenous protein, in the one "
            "cell type where the beta-3 isoforms are known to differ."),
    },
    {
        "hypothesis": (
            "The lysosomal and endolysosomal membrane transporters that co-purify with AP3S2 "
            "in interactome datasets are genuine AP-3 cargoes selected through dileucine "
            "signals."),
        "description": (
            "Take the membrane proteins recovered with AP3S2 in affinity-purification "
            "interactomes, score their cytosolic tails for acidic dileucine motifs, and test "
            "the top candidates for AP-3-dependent localisation in AP3D1-null cells and for "
            "direct binding to a reconstituted delta-sigma3B hemicomplex. This would convert a "
            "list of high-throughput associations into the ubiquitous cargo set that the "
            "gene's expression pattern implies but that no study has defined."),
    },
]

# --------------------------------------------------------------------------
# References
# --------------------------------------------------------------------------

REFERENCES = [
    dict(id="GO_REF:0000002", review=dict(
        relevance="LOW", correctness="VERIFIED", notes=(
            "InterPro2GO. Correctly applied on all five rows that cite it; four map "
            "family-level generalities that hold, and the fifth (GO:0006896) maps a term "
            "whose compartment reflects the fungal AP-3 pathway rather than the human one, "
            "which is a defect of the mapping target rather than of the reference."))),
    dict(id="GO_REF:0000024", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Manual ISS transfer by curator judgment of sequence similarity. Used twice here, "
            "both times from mouse Ap3s2, a protein identical in sequence to the human target "
            "- about as safe as the method gets. The reservation recorded on those rows is "
            "about the scope of the donor experiment, not about the transfer."))),
    dict(id="GO_REF:0000033", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "PAINT/IBA. The node behind the single IBA row was traced in the committed "
            "PTHR11753 PAINT slice and its ten seeds resolved individually; two are AP-3 sigma "
            "orthologs and the target sits inside the clade. The inference and the level of "
            "the term are both right."))),
    dict(id="GO_REF:0000044", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "UniProt SubCell mapping. Both rows reproduce the SUBCELLULAR LOCATION block "
            "faithfully. That block is itself ECO:0000250 by-similarity, so the rows are no "
            "stronger than the UniProt inference - but the inference is supported by the 1997 "
            "immunofluorescence of the sigma-3-containing complex."))),
    dict(id="GO_REF:0000107", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Ensembl Compara ortholog transfer. Four rows; the orthology calls are correct "
            "(mouse and rat Ap3s2). Two of the four inherit a defect from the donor side - a "
            "part-versus-binder mis-typing on GO:0035651 and a proteomic visitor detection on "
            "GO:0008021 - which is a source problem, not a failure of the transfer method."))),
    dict(id="GO_REF:0000108", review=dict(
        relevance="LOW", correctness="VERIFIED", notes=(
            "Inter-ontology logical inference. Correctly derives axon cytoplasm from the "
            "anterograde axonal transport row; it adds no independent evidence and inherits "
            "that row's non-core grade."))),
    dict(id="GO_REF:0000120", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Combined automated IEA methods. Both components of its WITH/FROM were checked "
            "against their sources: InterPro IPR027155 is the AP-3-sigma-specific APS3 "
            "signature, and ARBA00033921 was fetched from the UniProt ARBA service and its "
            "FunFam condition shown to discriminate AP-3 sigma subunits from all other human "
            "AP-complex sigmas."))),

    dict(id="PMID:9118953", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "The founding paper for this gene and the source of its only experimental "
            "annotation. PubMed-verified; it cloned human sigma-3A and sigma-3B, showed both "
            "are components of AP-3, and measured their expression by Northern and Western "
            "blot. Cached record is abstract-only, but every claim drawn from it here is "
            "stated in the abstract."))),
    dict(id="PMID:9151686", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "Independent contemporaneous identification of the same subunits, with full text "
            "available. Directly relevant because it raised a sigma-3B-specific antibody and "
            "reports the sigma-3 doublet in AP-3 immunoprecipitates - the observation that "
            "sets the limit on every later pan-sigma-3 antibody experiment."))),
    dict(id="PMID:9545220", review=dict(
        relevance="MEDIUM", correctness="DISPUTED", notes=(
            "Correctly cited, and its in vitro finding that the beta-3 appendage binds the "
            "clathrin heavy chain is not in question. The conclusion built on it - that AP-3 "
            "function involves clathrin coats - has been contested by direct reconstitution "
            "and coat tomography [PMID:42139345], which is why the annotation it supports is "
            "modified to a coat-agnostic term rather than accepted as written. Flagged "
            "DISPUTED for the downstream claim, not for the citation."))),
    dict(id="PMID:15537701", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Correctly cited mouse genetics comparing beta-3A and beta-3B AP-3 complexes. "
            "Highly relevant to AP-3 in neurons; relevant to AP3S2 only through complex "
            "membership, since the isoform variable in the study is beta-3 and the paper says "
            "nothing about which sigma paralog is present. Cached record is abstract-only."))),
    dict(id="PMID:23247405", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "A commentary by the authors on their own primary study, not primary research, "
            "which is the right weight for the four NAS rows drawn from it. Its statements "
            "about AP-3 at endosomal tubules and about HPS are accurate. One passage is now "
            "out of date - it reports as settled that AP-3 acts as a clathrin-binding adaptor "
            "- and that is noted where it matters rather than being used as support."))),
    dict(id="PMID:14691137", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "The single most important paper for this gene and the one the automated deep "
            "research missed: it is the only study that assays sigma-3B in a functional "
            "readout, cloning sigma-3A and sigma-3B separately and showing that both form "
            "delta-sigma3 hemicomplexes that bind the LIMP-II dileucine signal with identical "
            "sequence requirements. Full text verified; the title names the hemicomplexes and "
            "HIV-1 Nef, which is why a symbol-driven search does not reach it."))),
    dict(id="PMID:21097499", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "Full text verified. Supplies the composite-site mechanism for all three AP "
            "complexes and the substitution map that makes the paralogy argument testable "
            "(sigma-3A V94D and L109S). Its statement that it is not known whether the "
            "subunit-isoform combinations differ functionally is quoted as the field's own "
            "admission of the central gap for this gene."))),
    dict(id="PMID:39705307", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "Full text verified. The human AP-3 cryo-EM core, and the source of two facts used "
            "here: that ARF1 is bound principally through delta with the delta-sigma3 "
            "hemicomplex binding nearly as well as the whole complex, and that the dileucine "
            "site on sigma-3 is occluded by the beta-3 N-terminal extension in the resting "
            "state. Built on sigma-3A, which is recorded as a limit rather than glossed."))),
    dict(id="PMID:42139345", review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "Full text verified. Decides the clathrin question for AP-3 by direct "
            "reconstitution and cryo-electron tomography, which is what makes two GOA rows "
            "modifiable rather than acceptable and rules out GO:0035615 as this gene's "
            "complex-level molecular function. Its methods section is also the source for the "
            "statement that the structure used AP3S1."))),
    dict(id="PMID:21998198", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Correctly cited, full text verified, and the source annotation behind the human "
            "GO:0008089 and GO:0048490 rows via mouse Ap3s2. Reading it is what establishes "
            "that those rows are complex-level: the AP-3 loss is an Ap3d1 mocha mutant and the "
            "sigma subunit is detected with a pan-sigma-3 antibody. Not a criticism of the "
            "paper, which makes no sigma-paralog claim."))),
    dict(id="PMID:19010779", review=dict(
        relevance="LOW", correctness="VERIFIED", notes=(
            "Correctly cited; it is the source of the mouse GO:0035651 IDA that reaches the "
            "human gene by Ensembl transfer. Cached record is abstract-only, and the abstract "
            "is sufficient to establish the assay type - cross-linking, AP-3 purification and "
            "mass spectrometry - which is what the over-annotation call rests on. The paper's "
            "own subject, PI4KIIalpha, is not at issue."))),
    dict(id="PMID:33376223", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Correctly cited, full text verified. Source of the rat SynGO synaptic-vesicle "
            "annotation that reaches the human gene. Quoted for the authors' own statement "
            "that AP3 is among the endosomal proteins whose presence in the synaptic-vesicle "
            "proteome is explained by visitors or preparation carry-over, which is the basis "
            "for marking the transferred row over-annotated."))),
    dict(id="PMID:21874001", review=dict(
        relevance="LOW", correctness="VERIFIED", notes=(
            "Correctly cited, full text verified. Relevant to the gene's name recognition "
            "rather than its function: it labels a 15q26 type 2 diabetes locus AP3S2 while "
            "stating that the lead variant is an eQTL for C15orf38 and that PLIN1 is also a "
            "candidate. Used only in knowledge_gaps, to record that the disease association is "
            "not evidence about this protein."))),
    dict(id="PMID:41985787", review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Correctly cited, full text verified. Recent primary evidence that AP-3 selects a "
            "cargo through an acidic dileucine motif and that this matters for a "
            "lysosome-related organelle, which is the mechanism this subunit contributes to. "
            "Relevant to AP3S2 at complex level only: the study works with AP3B1 and does not "
            "test which subunit contacts the motif, so it is cited for the cargo and the "
            "signal type, not for a sigma-specific claim."))),
    dict(id=UNIPROT, review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "The machine-fetched UniProt record for P59780, confirmed to be the expected "
            "accession and protein. Note that every FUNCTION, SUBUNIT and SUBCELLULAR "
            "LOCATION statement in it carries ECO:0000250 (by similarity), so it is a source "
            "for what UniProt asserts rather than for experimental fact. One defect worth "
            "reporting upstream: the SUBUNIT line gives the sigma slot as 'APS1 or AP3S2', "
            "where APS1 is the yeast AP-1 sigma gene name and the intended human symbol is "
            "AP3S1."))),
    dict(id=BIOINF, review=dict(
        relevance="HIGH", correctness="VERIFIED", notes=(
            "Local analysis written for this review. Fetches sequences, the ARBA rule and the "
            "donor records live, caches nothing that is not regenerable, and asserts no result "
            "that its scripts do not compute. Its three conclusions - the dileucine pocket is "
            "retained in sigma-3B, human and mouse AP3S2 are identical, and ARBA00033921 "
            "discriminates AP-3 sigmas - are each reproducible by deleting cache/ and "
            "re-running."))),
    dict(id=AFFINAGE, review=dict(
        relevance="MEDIUM", correctness="VERIFIED", notes=(
            "Machine-generated deep-research record; trust gates clear, self-evaluation 'win', "
            "and it describes the correct protein with no symbol collision. Both of its "
            "citations resolve and are about AP3S2. It is accurate as far as it goes and "
            "honest that it found no mechanism beyond complex membership, but its recall is "
            "narrow: it missed PMID:14691137, the only functional assay on sigma-3B, and with "
            "it PMID:21097499, PMID:39705307 and PMID:42139345. Its mechanism_profile GO "
            "grounding was not imported; of its three suggestions two were re-derived "
            "independently and the third, NTRK3 as a partner, is a fusion-transcript artefact "
            "rather than a protein interaction."))),
]
