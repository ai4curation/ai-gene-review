"""Curation decisions for every GOA row of human AP3D1, keyed by row position.

Kept separate from ``build_review.py`` so the writer stays mechanical: the
builder never invents a ``supporting_entities`` list and never types a
``source_entities`` id -- it derives both from the seeded row. Each decision
supplies only the judgement (action, reason, quotes) plus, for propagated rows,
a per-source status/comment map whose keys are checked against that row's own
``supporting_entities``.

``KEY`` guards the positional indexing: if the seeded order ever changes, the
builder fails instead of applying a decision to the wrong row.
"""

from __future__ import annotations

# --- reusable source labels and comments -------------------------------------

MOUSE = ("mouse Ap3d1 (MGI:MGI:107734)", "SUPPORTS_TRANSFER")
ENSMUS_NOTE = (
    "Ensembl Compara protein id for the same mouse Ap3d1 record as UniProtKB:O54774 "
    "(Ensembl reports ENSMUSP00000020420 as a 1199-aa mouse translation, the length of "
    "O54774) -- one donor under two identifiers, not two independent sources."
)

NODE_25 = "PTHR22781 Eukaryota (taxon:2759) IBD node PTN000513025"
NODE_28 = "PTHR22781 Bilateria (taxon:33213) IBD node PTN000513028"

IN_CLADE_25 = (
    "Human AP3D1 is a PTHR22781:SF12 member and therefore descends from this "
    "pan-eukaryotic node; the family contains only AP-3 delta subunits (the beta "
    "subunits are PTHR11134, the alpha/gamma/epsilon subunits PTHR22780), so no "
    "AP-1/AP-2/AP-4 or beta-3 annotation can reach the target through it."
)
IN_CLADE_28 = (
    "Bilateria-level node; human AP3D1 is inside the inheriting clade. The node "
    "carries only the neuronal terms, while the complex and compartment terms sit on "
    "the deeper PTN000513025 -- the split is correct, because yeast has no synaptic "
    "vesicles. No IRD or IKR appears anywhere in the PTHR22781 PAINT slice."
)

# Residue claims re-used on the Bilateria-node rows. Anchor positions are the
# mouse native positions reported by delta_interfaces.py, which come out identical
# to human's for all eleven residues.
ARF1_SITE1 = [
    {
        "claim_type": "RETAINED",
        "anchor": {"accession": "UniProtKB:O54774", "position": p, "residue": r},
        "target": {"accession": "UniProtKB:O14617", "position": p, "residue": r},
        "role": "ARF1 site 1 interface residue on the delta trunk",
        "method": "MSA",
        "comment": (
            "MAFFT alignment of the nine reviewed PTHR22781 members plus four "
            "out-of-family adaptin large subunits "
            "(AP3D1-bioinformatics/delta_interfaces.tsv); mouse and human native "
            "positions coincide."
        ),
    }
    for p, r in [(77, "F"), (110, "M"), (111, "L")]
]

VAMP7_HINGE = [
    {
        "claim_type": "RETAINED",
        "anchor": {"accession": "UniProtKB:O54774", "position": p, "residue": r},
        "target": {"accession": "UniProtKB:O14617", "position": p, "residue": r},
        "role": "delta-adaptin hinge residue at the VAMP7 longin-domain interface",
        "method": "MSA",
        "comment": (
            "Mutated as mut1 (I702S/V704S) and mut2 (L709S/L713S) in PMID:22521722; "
            "positions verified directly against O14617 before alignment in "
            "AP3D1-bioinformatics/delta_interfaces.py."
        ),
    }
    for p, r in [(702, "I"), (704, "V"), (709, "L"), (713, "L")]
]

NOT_RESIDUE = (
    "Not a point-residue question: the annotation turns on which compartment or "
    "cell type the complex acts in, not on whether a functional residue was kept."
)

Q_MOCHA = (
    "PMID:9697856",
    "Here, we show that mocha is a null allele of the delta subunit of the "
    "adaptor-like protein complex AP-3, which is associated with coated vesicles "
    "budding from the trans-Golgi network, and that AP-3 is missing in mocha tissues.",
)
Q_DELTA_BOTH = (
    "PMID:26744459",
    "AP3D1 codes for the AP3delta subunit of the complex, which is essential for "
    "both forms.",
)
Q_TWO_FORMS = (
    "PMID:17349999",
    "Two forms of AP-3 have been characterized: a ubiquitous form, containing the "
    "δ, β3A, μ3A and σ3(A/B) subunits, and a brain-specific form, "
    "containing β3B and μ3B in addition to the common δ and "
    "σ3(A/B) subunits",
)
Q_ENDO_LYSO = (
    "PMID:42139345",
    "The AP3 complex mediates cargo sorting and carrier assembly for the trafficking "
    "of transmembrane proteins from endosomes to lysosomes.",
)
Q_TUBULAR = (
    "PMID:15051738",
    "Based on these data, we propose that AP-3 defines a novel pathway by which "
    "lysosomal membrane proteins are transported from tubular sorting endosomes to "
    "lysosomes.",
)

# --- the 59 GOA rows ---------------------------------------------------------

KEY = [
    ("GO:0000139", "IEA", "GO_REF:0000044"),
    ("GO:0005515", "IPI", "PMID:15598649"),
    ("GO:0005737", "IEA", "GO_REF:0000044"),
    ("GO:0005765", "HDA", "PMID:17897319"),
    ("GO:0005769", "NAS", "PMID:23247405"),
    ("GO:0005794", "IEA", "GO_REF:0000117"),
    ("GO:0005794", "TAS", "PMID:9151686"),
    ("GO:0006623", "IBA", "GO_REF:0000033"),
    ("GO:0006886", "IEA", "GO_REF:0000120"),
    ("GO:0006886", "TAS", "PMID:9151686"),
    ("GO:0006896", "IBA", "GO_REF:0000033"),
    ("GO:0006901", "IEA", "GO_REF:0000107"),
    ("GO:0007041", "IEA", "GO_REF:0000117"),
    ("GO:0008089", "IEA", "GO_REF:0000107"),
    ("GO:0008089", "ISS", "GO_REF:0000024"),
    ("GO:0010008", "IBA", "GO_REF:0000033"),
    ("GO:0010008", "IDA", "PMID:16162817"),
    ("GO:0010008", "IEA", "GO_REF:0000120"),
    ("GO:0010496", "IEA", "GO_REF:0000117"),
    ("GO:0015031", "IEA", "GO_REF:0000002"),
    ("GO:0016020", "HDA", "PMID:19946888"),
    ("GO:0016050", "IEA", "GO_REF:0000117"),
    ("GO:0016182", "IBA", "GO_REF:0000033"),
    ("GO:0016182", "IEA", "GO_REF:0000120"),
    ("GO:0016183", "NAS", "PMID:15537701"),
    ("GO:0016192", "IEA", "GO_REF:0000002"),
    ("GO:0016192", "NAS", "PMID:23247405"),
    ("GO:0030117", "IEA", "GO_REF:0000002"),
    ("GO:0030123", "IBA", "GO_REF:0000033"),
    ("GO:0030123", "IEA", "GO_REF:0000002"),
    ("GO:0030123", "NAS", "PMID:9151686"),
    ("GO:0030424", "IEA", "GO_REF:0000107"),
    ("GO:0032438", "IC", "PMID:22511774"),
    ("GO:0032502", "IEA", "GO_REF:0000117"),
    ("GO:0035646", "IMP", "PMID:22511774"),
    ("GO:0035651", "IEA", "GO_REF:0000107"),
    ("GO:0035654", "NAS", "PMID:9545220"),
    ("GO:0036465", "NAS", "PMID:15537701"),
    ("GO:0043195", "IBA", "GO_REF:0000033"),
    ("GO:0043195", "IEA", "GO_REF:0000107"),
    ("GO:0048490", "IBA", "GO_REF:0000033"),
    ("GO:0048490", "IEA", "GO_REF:0000107"),
    ("GO:0048490", "ISS", "GO_REF:0000024"),
    ("GO:0048499", "IBA", "GO_REF:0000033"),
    ("GO:0048840", "IEA", "GO_REF:0000107"),
    ("GO:0060155", "NAS", "PMID:23247405"),
    ("GO:0072657", "IEA", "GO_REF:0000120"),
    ("GO:0072657", "IMP", "PMID:22511774"),
    ("GO:0098793", "IEA", "GO_REF:0000107"),
    ("GO:0098794", "IEA", "GO_REF:0000107"),
    ("GO:0098830", "IBA", "GO_REF:0000033"),
    ("GO:0098830", "IEA", "GO_REF:0000107"),
    ("GO:0098943", "IBA", "GO_REF:0000033"),
    ("GO:0098943", "IEA", "GO_REF:0000107"),
    ("GO:0098978", "IEA", "GO_REF:0000107"),
    ("GO:0140916", "IMP", "PMID:17349999"),
    ("GO:1903232", "NAS", "PMID:23247405"),
    ("GO:1904115", "IEA", "GO_REF:0000120"),
    ("GO:1990742", "IEA", "GO_REF:0000107"),
]


def _mouse_ensembl_sources(status="SUPPORTS_TRANSFER", note="", ens="ensembl:ENSMUSP00000020420"):
    return {
        "UniProtKB:O54774": (MOUSE[0], status, note or "Mouse Ap3d1, the Ensembl Compara donor."),
        ens: ("mouse Ap3d1 (Ensembl translation)", status, ENSMUS_NOTE),
    }


DECISIONS: dict[int, dict] = {}

# 0 GO:0000139 Golgi membrane, IEA UniProt SubCell
DECISIONS[0] = dict(
    summary="Golgi-membrane association inferred from the UniProt subcellular-location keyword. AP-3 does associate with the Golgi region, but its demonstrated mammalian budding site is the tubular sorting endosome.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The UniProt SUBCELLULAR LOCATION block that seeds SL-0134 is itself flagged By similarity, "
        "and the primary human observation behind it is Simpson et al.'s anti-delta immunofluorescence, "
        "which places AP-3 at the Golgi region AND at peripheral structures. Yeast AP-3 does bud from "
        "the late Golgi, but in mammalian cells the site where AP-3 is caught budding is a tubular "
        "endosome (PMID:15051738), and the reconstituted human coat is described as an endosome-to-lysosome "
        "carrier (PMID:42139345). Keeping the location as real but peripheral to the core role."
    ),
    supported_by=[
        ("PMID:9151686", "Immunofluorescence using anti-delta antibodies reveals that the AP-3 complex is associated with the Golgi region of the cell as well as with more peripheral structures."),
        Q_TUBULAR,
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        sources={"UniProtKB-SubCell:SL-0134": ("Golgi apparatus membrane (UniProt subcellular location)", "SOURCE_WEAK_OR_INFERRED", "The UniProt Golgi-membrane statement carries ECO:0000250 (By similarity), so the keyword mapping inherits an inferred source rather than a human observation.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 1 GO:0005515 protein binding, IPI CLN3
DECISIONS[1] = dict(
    summary="Bare protein binding from the CLN3 interaction. The informative statement is that AP-3 recognises a dileucine sorting signal in cargo, a site formed by the delta/sigma-3 hemicomplex.",
    action="MODIFY",
    reason=(
        "GO:0005515 records only that something was bound. The experiment is a dileucine-motif binding "
        "assay: the CLN3 dileucine motif bound AP-3 in vitro and both AP-1 and AP-3 are required for "
        "CLN3 to reach lysosomes. The 2026 coat structure locates the dileucine cargo pocket at the "
        "sigma-3/delta interface, so delta contributes directly to cargo recognition. "
        "GO:0140312 cargo adaptor activity is the informative replacement and is already used for the "
        "equivalent non-clathrin large subunit AP4E1 (IBA). The partner is CLN3/battenin "
        "(UniProtKB:Q13286, resolved via the UniProt REST record)."
    ),
    supported_by=[
        ("PMID:15598649", "The dileucine motif of CLN3 bound both AP-1 and AP-3 in vitro, and expression of mutated CLN3 in AP-1- or AP-3-deficient mouse fibroblasts showed that both adaptor complexes are required for sequential sorting of CLN3 via this motif."),
        ("PMID:42139345", "The known cargo binding sites on C-μ3 and σ3/δ are adjacent to the membrane, and the electron microscopy density suggests that they are occupied by cargo"),
    ],
    proposed_replacement_terms=[("GO:0140312", "cargo adaptor activity")],
    additional_reference_ids=["PMID:42139345"],
)

# 2 GO:0005737 cytoplasm
DECISIONS[2] = dict(
    summary="AP-3 is a cytosolic coat that cycles on and off membranes; a cytoplasmic pool is exactly what is expected and what is seen when ARF1 binding is abolished.",
    action="ACCEPT",
    reason=(
        "Not a throwaway location for this protein. AP-3 has low intrinsic affinity for membranes and is "
        "recruited by ARF1-GTP; when both ARF1 interfaces on delta are mutated the protein redistributes "
        "to the cytosol, which is the direct demonstration that a cytoplasmic pool exists and is the "
        "resting state."
    ),
    supported_by=[
        ("PMID:42139345", "Mutations in AP3D1 that abolish interaction with ARF1 sites relocalize δ-WT-SG to the cytosol."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={"UniProtKB-SubCell:SL-0086": ("Cytoplasm (UniProt subcellular location)", "SUPPORTS_TRANSFER", "Keyword mapping of the UniProt Cytoplasm location; independently confirmed in human cells by the ARF1-interface mutants.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 3 GO:0005765 lysosomal membrane, HDA
DECISIONS[3] = dict(
    summary="Detected in a placental lysosomal-membrane proteome. Plausible as a peripheral, transient association, but AP-3's productive site is the endosome upstream.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "A reference-projection check on PMID:17897319 (QuickGO reference= query, paginated fully) "
        "returns 242 distinct gene products, so this is a compartment survey rather than a targeted "
        "localisation claim. It is not over-annotation in the way the NK membrane proteome is, because "
        "AP-3 is genuinely an endolysosomal coat and the paper explicitly reports peripheral, "
        "lysosome-associated proteins as a category. But the compartment where AP-3 is caught doing "
        "work is the tubular sorting endosome, not the lysosomal membrane, so this is context."
    ),
    supported_by=[
        ("PMID:17897319", "Finally, our results identified a particular set of proteins with known functions in signaling and targeting to be at least partially associated with lysosomes."),
        Q_TUBULAR,
    ],
)

# 4 GO:0005769 early endosome, NAS
DECISIONS[4] = dict(
    summary="AP-3 is on tubular domains of early/recycling endosomes; consistent with the human IDA for endosome membrane.",
    action="ACCEPT",
    reason=(
        "The ComplexPortal NAS is drawn from a review whose own statement places AP-3 on early/recycling "
        "endosome tubules, and it is independently supported by direct imaging in melanocytes and by the "
        "immuno-EM that defines the AP-3 endosomal exit site. This is the compartment from which AP-3 "
        "carriers bud."
    ),
    supported_by=[
        ("PMID:23247405", "Rab32 and Rab38 interact with AP-1, AP-3 and BLOC-2 on early/recycling endosome tubules, where cargo such as tyrosinase and Tyrp1 are loaded into vesicles or transport intermediates."),
        ("PMID:16162817", "AP-3 and AP-1 localize in melanocytes primarily to clathrin-coated buds on tubular early endosomes near melanosomes."),
    ],
)

# 5 GO:0005794 Golgi apparatus, ARBA
DECISIONS[5] = dict(
    summary="ARBA rule ARBA00028708 firing on the AP3D1-specific CATH FunFam. True but peripheral, for the same reason as the Golgi-membrane row.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "I fetched ARBA00028708 from the UniProt REST ARBA endpoint and evaluated all 146 condition sets "
        "against AP3D1's full signature complement: exactly one is satisfied, "
        "'FunFam 3.30.450.50:FF:000001 + taxon Eukaryota'. That FunFam is named 'AP-3 complex subunit "
        "delta-1, putative' in the UniProt record, so the rule is effectively AP3D1-specific rather than "
        "a fold-level over-generalisation, and the term it assigns is one Simpson et al. observed "
        "directly with an anti-delta antibody. Kept as context rather than core."
    ),
    supported_by=[
        ("PMID:9151686", "Immunofluorescence using anti-delta antibodies reveals that the AP-3 complex is associated with the Golgi region of the cell as well as with more peripheral structures."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        sources={"ARBA:ARBA00028708": ("ARBA00028708 (GO:0005794 rule)", "SUPPORTS_TRANSFER", "146 condition sets; one satisfied by AP3D1 -- FunFam 3.30.450.50:FF:000001 with taxon Eukaryota. The FunFam is the delta-1 specific one, so the rule is not fold-level over-reach.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 6 GO:0005794 Golgi apparatus, TAS
DECISIONS[6] = dict(
    summary="The original anti-delta immunofluorescence: AP-3 at the Golgi region and at peripheral structures.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "This is the human primary observation, and it was made with an antibody against delta itself, so "
        "the annotation is about this gene product rather than about the complex by inference. The same "
        "paper immediately qualifies the Golgi signal by reporting peripheral structures with limited "
        "endosomal-marker overlap, and the later immuno-EM localises the budding profiles to a tubular "
        "endosome. Real location, not the core site of action."
    ),
    supported_by=[
        ("PMID:9151686", "Immunofluorescence using anti-delta antibodies reveals that the AP-3 complex is associated with the Golgi region of the cell as well as with more peripheral structures."),
        ("PMID:9151686", "These peripheral structures show only limited colocalization with endosomal markers and may correspond to a postTGN biosynthetic compartment."),
    ],
)

# 7 GO:0006623 protein targeting to vacuole, IBA
DECISIONS[7] = dict(
    summary="Pan-eukaryotic IBD node, seeded by the yeast APL5 experiments. Correct and core: delivering cargo to the lytic compartment is what AP-3 is for, and 'vacuole' is the compartment-agnostic parent that covers the lysosome.",
    action="ACCEPT",
    reason=(
        "The IBD sits on PTN000513025 at taxon:2759 (Eukaryota) and is seeded by SGD:S000006116 = "
        "UniProtKB:Q08951, yeast APL5, which carries its own IMP for this term from PMID:17895371 "
        "(vacuolar targeting of scNcr1p perturbed in AP-3-deficient yeast). Human AP3D1 is a "
        "PTHR22781:SF12 member and so descends from that node. GO's vacuole subsumes the lysosome "
        "(GO:0006622 protein targeting to lysosome is_a GO:0006623, confirmed via the QuickGO ancestors "
        "endpoint), so nothing about the term is yeast-specific; the compartment-specific human child is "
        "added as a separate NEW row. PTHR22781 contains only AP-3 delta subunits, so this cannot be a "
        "leak from another adaptin."
    ),
    supported_by=[
        ("PMID:17895371", "Targeting of scNcr1p to the vacuole was perturbed in AP-3-deficient yeast cells, whereas the delivery of scNpc2p was affected by deficiencies in either AP-3 or GGA."),
        Q_ENDO_LYSO,
    ],
    additional_reference_ids=["file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md"],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={
            "PANTHER:PTN000513025": (NODE_25 + " (seeded by yeast APL5)", "SUPPORTS_TRANSFER", IN_CLADE_25),
            "SGD:S000006116": ("yeast APL5 (UniProtKB:Q08951)", "SUPPORTS_TRANSFER", "Sole gene-level donor on this row; QuickGO shows APL5 carries GO:0006623 IMP from PMID:17895371, an experimental annotation, not a propagated one."),
        },
        residue_claims=ARF1_SITE1,
    ),
)

# 8 GO:0006886 intracellular protein transport, IEA ARBA+InterPro
DECISIONS[8] = dict(
    summary="Correct but uninformative parent of everything AP-3 does.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "ARBA00027179 has 53 condition sets, of which AP3D1 satisfies one (bare FunFam "
        "3.30.450.50:FF:000001, no taxon guard); InterPro IPR002553 is the adaptin-like N-terminal "
        "domain shared with AP-1/AP-2/AP-4, so this arm of the row is fold-level. The term is true - "
        "AP-3 moves proteins between intracellular compartments - but it sits far above the specific "
        "endosome-to-lysosome route that the specific rows capture."
    ),
    supported_by=[Q_ENDO_LYSO],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={
            "ARBA:ARBA00027179": ("ARBA00027179 (GO:0006886 rule)", "SUPPORTS_TRANSFER", "One of 53 condition sets satisfied: FunFam 3.30.450.50:FF:000001 with no taxon condition."),
            "InterPro:IPR002553": ("IPR002553 Clathrin/coatomer adaptor, adaptin-like, N-terminal", "SUPPORTS_TRANSFER", "A domain shared by the large subunits of AP-1, AP-2, AP-3 and AP-4, so it can only support a term at this level of generality."),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 9 GO:0006886 intracellular protein transport, TAS
DECISIONS[9] = dict(
    summary="Author statement from the AP-3 characterisation paper; correct, general.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Simpson et al. proposed that AP-3 works in trafficking to lysosomes or in a related pathway, "
        "which is the origin of this general transport term. It is right, and superseded in specificity "
        "by the endosome-to-lysosome and vacuole-targeting rows."
    ),
    supported_by=[
        ("PMID:9151686", "Because pigment granules are believed to be similar to lysosomes, this suggests either that the AP-3 complex may be directly involved in trafficking to lysosomes or alternatively that it may be involved in another pathway, but that missorting in that pathway may indirectly lead to defects in pigment granules."),
    ],
)

# 10 GO:0006896 Golgi to vacuole transport, IBA
DECISIONS[10] = dict(
    summary="The yeast ALP pathway propagated to the Eukaryota node. The process transfers; the donor compartment does not - the mammalian AP-3 exit site is the tubular endosome, not the Golgi.",
    action="MODIFY",
    reason=(
        "PTN000513025 carries this term on a single gene-level donor, SGD:S000006116 (yeast APL5), whose "
        "own IMP is PMID:9335339 - the screen that defined AP-3 as the machinery carrying alkaline "
        "phosphatase and Vam3p FROM THE LATE GOLGI to the vacuole. That route is genuinely how yeast AP-3 "
        "works. In mammals it is not: immuno-EM catches AP-3 budding from a tubular endosomal compartment "
        "and AP-3-deficient cells missort LAMP-1/LAMP-2 from that compartment (PMID:15051738); in "
        "melanocytes AP-3 is on early-endosomal buds (PMID:16162817); and the reconstituted human coat is "
        "described as an endosome-to-lysosome carrier (PMID:42139345). So the biology is conserved "
        "(deliver cargo to the lytic compartment, which GO:0006623 on the same node states correctly) "
        "while the term names a compartment pair that does not transfer. Proposing GO:0008333 endosome to "
        "lysosome transport. This is a term-scoping call, not a challenge to the node: the seed is sound "
        "for yeast and the target is inside the clade. Residual uncertainty - Peden et al. call the "
        "mammalian site 'controversial' and a minor TGN pool is not excluded - is recorded in "
        "knowledge_gaps rather than resolved here."
    ),
    supported_by=[
        ("PMID:9335339", "A screen for factors specifically involved in transport of alkaline phosphatase (ALP) from the Golgi to the vacuole/lysosome has identified Ap16p and Ap15p of the yeast AP-3 complex."),
        ("PMID:15051738", "we show by immuno-electron microscopy that AP-3 is associated with budding profiles evolving from a tubular endosomal compartment that also exhibits budding profiles positive for AP-1"),
        Q_TUBULAR,
        Q_ENDO_LYSO,
        ("PMID:23247405", "Transport of newly synthesized tyrosinase and Tyrp1 to the maturing melanosome requires a sorting step at specialized tubular domains of early/recycling endosomes, rather than direct transport from the trans-Golgi network"),
    ],
    proposed_replacement_terms=[("GO:0008333", "endosome to lysosome transport")],
    prop=dict(
        root_cause="TERM_SCOPING_PROBLEM",
        failure_modes=["COMPARTMENT_OR_COMPLEX_MISMATCH"],
        sources={
            "PANTHER:PTN000513025": (NODE_25 + " (seeded by yeast APL5)", "SUPPORTS_SOURCE_BUT_NOT_TARGET", "Node placement and clade membership are correct; what does not transfer is the Golgi donor compartment named in the term. The sibling GO:0006623 on the same node states the conserved claim without the compartment commitment."),
            "SGD:S000006116": ("yeast APL5 (UniProtKB:Q08951)", "SUPPORTS_SOURCE_BUT_NOT_TARGET", "Sole gene-level donor; its IMP (PMID:9335339) is specifically the Golgi-to-vacuole ALP pathway, which is a yeast route."),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 11 GO:0006901 vesicle coat assembly
DECISIONS[11] = dict(
    summary="AP-3 is itself a vesicle coat, and the delta subunit templates its polymerisation with ARF1. Core.",
    action="ACCEPT",
    reason=(
        "The mouse donor carries this as IDA from PMID:16760431. It is now structurally explicit for the "
        "human protein: AP-3 with two bound ARF1 molecules dimerises, and the coat is built from spiralling "
        "rows of AP-3 arches linked by ARF1 dimers, with delta-ARF1-delta among the linkages modelled. "
        "Coat assembly is not a downstream consequence of AP-3 function - it is the function."
    ),
    supported_by=[
        ("PMID:39705307", "Finally, binding of the second Arf1 molecule provides the template for AP-3 dimerization, providing a glimpse into the first step of coat polymerization."),
        ("PMID:42139345", "we demonstrate that AP3:ARF1 spontaneously remodels membranes containing cargo and the phosphoinositide PI(3,5)P2 into tubular structures coated in spiraling rows of AP3 arches and ARF1 dimers"),
    ],
    additional_reference_ids=["PMID:16760431"],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 carries GO:0006901 as IDA from PMID:16760431 (AP-3-containing vesicles generated from PC12 membranes); the claim is now independently established for the human protein by cryo-EM."),
        residue_claims=ARF1_SITE1,
    ),
)

# 12 GO:0007041 lysosomal transport
DECISIONS[12] = dict(
    summary="Broad but correct: AP-3 moves cargo into the lysosome.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "ARBA00033548 has only 9 condition sets and AP3D1 satisfies one of them, "
        "'FunFam 3.30.450.50:FF:000001 + taxon Craniata' - i.e. the AP3D1-specific FunFam with a "
        "vertebrate guard, which is a tight rule rather than a fold-level sweep. The term is a parent of "
        "the specific endosome-to-lysosome statement."
    ),
    supported_by=[Q_ENDO_LYSO],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={"ARBA:ARBA00033548": ("ARBA00033548 (GO:0007041 rule)", "SUPPORTS_TRANSFER", "One of 9 condition sets satisfied: FunFam 3.30.450.50:FF:000001 with taxon Craniata. The narrowest of the eight ARBA rules on this gene.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 13 GO:0008089 anterograde axonal transport, IEA
DECISIONS[13] = dict(
    summary="Neuronal context transferred from mouse, where AP-3 is needed for PI4KIIalpha to leave the cell body for neurites.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Mouse Ap3d1 carries GO:0008089 as IMP from PMID:21998198: PI4KIIalpha reaches processes in "
        "wild-type neurons but not in AP-3-null or BLOC-1-null cells. The transfer is sound - delta is "
        "the shared large subunit of both AP-3A and the neuronal AP-3B, so it is present wherever the "
        "phenotype was measured - but this is the neuron-specific manifestation of AP-3's generic "
        "endosomal sorting step, not an independent axonal-transport activity of delta."
    ),
    supported_by=[
        ("PMID:21998198", "PI4KIIα was targeted to processes in wild-type primary cultured cortical neurons and PC12 cells but failed to reach neurites in cells lacking either AP-3 or BLOC-1."),
        Q_TWO_FORMS,
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IMP for GO:0008089 from PMID:21998198; an experimental donor annotation, but one measured only in neurons."),
        residue_claims=VAMP7_HINGE,
    ),
)

# 14 GO:0008089 anterograde axonal transport, ISS
DECISIONS[14] = dict(
    summary="Curator-judged sequence-similarity transfer of the same mouse phenotype.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Same donor and same underlying mouse IMP as the Ensembl-Compara row, transferred by curator "
        "judgement instead of by automatic orthology. Human and mouse delta are 1:1 orthologs in "
        "PTHR22781:SF12 and align residue-for-residue through the entire cargo-binding hinge, so there is "
        "no divergence argument against the transfer; the reservation is the same as before, that this is "
        "a neuron-specific readout."
    ),
    supported_by=[
        ("PMID:21998198", "PI4KIIα was targeted to processes in wild-type primary cultured cortical neurons and PC12 cells but failed to reach neurites in cells lacking either AP-3 or BLOC-1."),
    ],
    additional_reference_ids=["file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={"UniProtKB:O54774": (MOUSE[0], "SUPPORTS_TRANSFER", "The sole donor on this row; mouse Ap3d1 IMP from PMID:21998198.")},
        residue_claims=VAMP7_HINGE,
    ),
)

# 15 GO:0010008 endosome membrane, IBA
DECISIONS[15] = dict(
    summary="Pan-eukaryotic node for the compartment AP-3 acts on. Core, and the target's own IDA is one of the descendant evidences behind the node.",
    action="ACCEPT",
    reason=(
        "The IBD on PTN000513025 is seeded by MGI:MGI:107734 (mouse Ap3d1, IDA PMID:16162817) and by "
        "UniProtKB:O14617 - human AP3D1 itself, which carries the same IDA. The target appearing in its "
        "own WITH/FROM is the expected marker that experimental grounding exists on the target, and the "
        "IBA then adds that the localisation is inherited rather than lineage-specific. The endosomal "
        "membrane is where AP-3 is caught budding and where the reconstituted AP3:ARF1 coat forms "
        "carriers, so this is the core compartment."
    ),
    supported_by=[
        ("PMID:16162817", "AP-3 and AP-1 localize in melanocytes primarily to clathrin-coated buds on tubular early endosomes near melanosomes."),
        Q_TUBULAR,
    ],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "Resolves to UniProtKB:O54774 (Swiss-Prot) via the UniProt xref search; carries GO:0010008 IDA from PMID:16162817."),
            "PANTHER:PTN000513025": (NODE_25, "SUPPORTS_TRANSFER", IN_CLADE_25),
            "UniProtKB:O14617": ("human AP3D1 (the target itself)", "SUPPORTS_TRANSFER", "Self-reference is correct and expected: the target's own IDA (PMID:16162817) is one of the descendant evidences the PAINT curator used to place this IBD. Not circular and not redundant."),
        },
        residue_claims=ARF1_SITE1,
    ),
)

# 16 GO:0010008 endosome membrane, IDA
DECISIONS[16] = dict(
    summary="Direct imaging of AP-3 on tubular early endosomes in melanocytes.",
    action="ACCEPT",
    reason=(
        "This is the human experimental anchor for the compartment, and it is the same observation that "
        "seeds the IBD node. AP-3-deficient melanocytes accumulate tyrosinase in vacuolar and "
        "multivesicular endosomes, which is the loss-of-function counterpart to the localisation."
    ),
    supported_by=[
        ("PMID:16162817", "AP-3 and AP-1 localize in melanocytes primarily to clathrin-coated buds on tubular early endosomes near melanosomes."),
        ("PMID:16162817", "In AP-3-deficient melanocytes, tyrosinase accumulates inappropriately in vacuolar and multivesicular endosomes."),
    ],
)

# 17 GO:0010008 endosome membrane, IEA combined
DECISIONS[17] = dict(
    summary="Combined ARBA + Ensembl-Compara route to the same, well-supported compartment.",
    action="ACCEPT",
    reason=(
        "Three independent arms agree and all are sound: ARBA00028306 fires on the AP3D1-specific FunFam "
        "with a Eukaryota guard (1 of 27 condition sets satisfied), and the Ensembl arm transfers the "
        "mouse Ap3d1 IDA from PMID:16162817. The same term is separately supported by a human IDA and by "
        "the IBA, so nothing here rests on the electronic route alone."
    ),
    supported_by=[
        ("PMID:16162817", "AP-3 and AP-1 localize in melanocytes primarily to clathrin-coated buds on tubular early endosomes near melanosomes."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={
            "ARBA:ARBA00028306": ("ARBA00028306 (GO:0010008 rule)", "SUPPORTS_TRANSFER", "One of 27 condition sets satisfied: FunFam 3.30.450.50:FF:000001 with taxon Eukaryota."),
            "UniProtKB:O54774": (MOUSE[0], "SUPPORTS_TRANSFER", "Mouse Ap3d1 IDA for GO:0010008 from PMID:16162817."),
            "ensembl:ENSMUSP00000020420": ("mouse Ap3d1 (Ensembl translation)", "SUPPORTS_TRANSFER", ENSMUS_NOTE),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 18 GO:0010496 intercellular transport -- REMOVE
DECISIONS[18] = dict(
    summary="'The movement of substances between cells' - AP3D1 is a cytosolic coat subunit acting on intracellular membranes. The rule fires on a single unguarded FunFam.",
    action="REMOVE",
    reason=(
        "GO:0010496 is defined as the movement of substances between cells. Nothing in the AP-3 "
        "literature has AP3D1 transferring material from one cell to another; every characterised cargo "
        "(LAMP1/LAMP2, CD63, tyrosinase, VAMP7, ZnT2/ZnT3, PI4KIIalpha, CLN3) moves between intracellular "
        "compartments of the same cell. I fetched ARBA00092758 and evaluated all 99 condition sets against "
        "AP3D1's complete signature complement: exactly one is satisfied, a bare "
        "'FunFam 3.30.450.50:FF:000001' with no taxon guard - the same AP3D1-specific FunFam that "
        "correctly yields 'lysosomal transport' and 'endosome membrane' under other rules. The identical "
        "evidence therefore produces a term with the wrong topology. This is the one electronic row here "
        "removed on a positive biological argument rather than for generality."
    ),
    supported_by=[
        Q_ENDO_LYSO,
        Q_TUBULAR,
    ],
    prop=dict(
        root_cause="SOURCE_BAD",
        failure_modes=["COMPARTMENT_OR_COMPLEX_MISMATCH"],
        sources={"ARBA:ARBA00092758": ("ARBA00092758 (GO:0010496 rule)", "SOURCE_BAD", "99 condition sets; the only one AP3D1 satisfies is an unguarded 'FunFam 3.30.450.50:FF:000001'. A delta-adaptin-specific FunFam cannot support a between-cells transport term.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 19 GO:0015031 protein transport, InterPro2GO
DECISIONS[19] = dict(
    summary="InterPro2GO from the two delta-specific InterPro entries. Correct, general.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Unlike the IPR002553 arm elsewhere in this record, both signatures here are delta-specific: "
        "IPR017105 is the AP-3 delta-subunit family entry and IPR010474 the metazoan delta domain. The "
        "mapping is therefore well grounded; the term is simply a high-level parent of the specific "
        "endosome-to-lysosome cargo route."
    ),
    supported_by=[Q_ENDO_LYSO],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={
            "InterPro:IPR010474": ("IPR010474 AP-3 complex subunit delta domain, metazoa", "SUPPORTS_TRANSFER", "Delta-specific and metazoan; it contains the VAMP7-binding hinge, so it is a signature of AP-3 cargo capture rather than of a generic fold."),
            "InterPro:IPR017105": ("IPR017105 Adaptor protein complex AP-3, delta subunit", "SUPPORTS_TRANSFER", "The family-level delta entry, integrated with PTHR22781; as specific a signature as this protein has."),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 20 GO:0016020 membrane, HDA -- over-annotated
DECISIONS[20] = dict(
    summary="From an NK-cell membrane proteome that projects onto 1142 distinct gene products. A survey hit, not a localisation claim.",
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Reference-projection test: querying QuickGO with reference=PMID:19946888 and paginating fully "
        "returns 1142 distinct gene products. The paper itself says roughly 40% of its identifications "
        "were predicted membrane proteins and that the remainder are things transiently associated with "
        "membranes - which is exactly what AP-3 is. The term is not false (a peripheral coat is attached "
        "to a membrane) but it carries no information about AP3D1 that the endosome-membrane rows do not "
        "carry better."
    ),
    supported_by=[
        ("PMID:19946888", "The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."),
    ],
)

# 21 GO:0016050 vesicle organization
DECISIONS[21] = dict(
    summary="Parent term; AP-3 does organise vesicles, and in neurons its loss changes synaptic-vesicle size.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "ARBA00028845 fires on the AP3D1-specific FunFam with a Euarchontoglires guard (1 of 33 condition "
        "sets). The claim is independently true: in mouse, loss of AP-3 changes synaptic-vesicle size in "
        "a brain-region-specific way, and AP-3 is the coat that shapes its own carriers. Kept as the "
        "uninformative parent of the specific coat-assembly and SV rows."
    ),
    supported_by=[
        ("PMID:20089890", "Quantitative immunoelectron microscopy demonstrated that the majority of AP-3 immunoreactivity in both wild-type striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size."),
    ],
    additional_reference_ids=["PMID:20089890"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={"ARBA:ARBA00028845": ("ARBA00028845 (GO:0016050 rule)", "SUPPORTS_TRANSFER", "One of 33 condition sets satisfied: FunFam 3.30.450.50:FF:000001 with taxon Euarchontoglires.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 22 GO:0016182 SV budding from endosome, IBA
DECISIONS[22] = dict(
    summary="Bilateria node seeded by mouse and rat Ap3d1, both with IDA and IMP. Delta is in the neuronal AP-3B as well as the ubiquitous AP-3A, so the term belongs on it.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "PTN000513028 sits at taxon:33213 (Bilateria) and carries two gene-level donors here, "
        "MGI:MGI:107734 (mouse Ap3d1, IDA+IMP PMID:11588176) and RGD:1308659 (rat Ap3d1, resolving to "
        "UniProtKB:B5DFK6, IDA+IMP PMID:22539861). Both are real experimental annotations. The subtlety "
        "the reviewer must not get wrong is that the in vitro budding activity is a property of the "
        "NEURONAL AP-3B complex - only the neuronal form makes synaptic vesicles from endosomes - but "
        "delta is the shared large subunit of both forms, so a delta annotation is correct rather than a "
        "beta-3 leak. Non-core because it is the neuronal instance of the same endosomal budding step "
        "that the coat-assembly and endosome-membrane rows state generically."
    ),
    supported_by=[
        ("PMID:11588176", "However, only the neuronal form of AP-3 can produce synaptic vesicles from endosomes in vitro."),
        Q_TWO_FORMS,
        ("PMID:22539861", "We have identified an essential requirement for both adaptor protein complexes 1 and 3 in this process by employing morphological and optical tracking of bulk endosome-derived synaptic vesicles in rat primary neuronal cultures."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "Mouse Ap3d1 carries GO:0016182 as both IDA and IMP from PMID:11588176."),
            "PANTHER:PTN000513028": (NODE_28, "SUPPORTS_TRANSFER", IN_CLADE_28),
            "RGD:1308659": ("rat Ap3d1 (UniProtKB:B5DFK6)", "SUPPORTS_TRANSFER", "The UniProt xref search returns five rat Ap3d1 entries, all TrEMBL, of which B5DFK6 is the one GOA uses; QuickGO shows IDA+IMP for this term from PMID:22539861. A second, independent gene-level donor on this row -- so 'the IBD seed' would be wrong here."),
        },
        residue_claims=VAMP7_HINGE,
    ),
)

# 23 GO:0016182 SV budding from endosome, IEA
DECISIONS[23] = dict(
    summary="Same mouse and rat donors by the automatic route.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Four supporting entities that are two donors: UniProtKB:B5DFK6 with its Ensembl translation "
        "ENSRNOP00000025878 (rat), and UniProtKB:O54774 with ENSMUSP00000020420 (mouse). Both donors "
        "carry experimental annotations for this term. Same verdict as the IBA row - correct, and "
        "neuron-specific context rather than the core molecular role."
    ),
    supported_by=[
        ("PMID:11588176", "However, only the neuronal form of AP-3 can produce synaptic vesicles from endosomes in vitro."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "UniProtKB:B5DFK6": ("rat Ap3d1", "SUPPORTS_TRANSFER", "Rat donor; IDA+IMP from PMID:22539861."),
            "ensembl:ENSRNOP00000025878": ("rat Ap3d1 (Ensembl translation)", "SUPPORTS_TRANSFER", "Ensembl Compara id for the same rat Ap3d1 as UniProtKB:B5DFK6 -- one donor under two identifiers."),
            "UniProtKB:O54774": (MOUSE[0], "SUPPORTS_TRANSFER", "Mouse donor; IDA+IMP from PMID:11588176."),
            "ensembl:ENSMUSP00000020420": ("mouse Ap3d1 (Ensembl translation)", "SUPPORTS_TRANSFER", ENSMUS_NOTE),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 24 GO:0016183 synaptic vesicle coating -- MODIFY
DECISIONS[24] = dict(
    summary="The GO term means clathrin-coated pit formation at the presynaptic plasma membrane. AP-3 does not act there; the cited paper is about endosomal sorting of synaptic-vesicle proteins.",
    action="MODIFY",
    reason=(
        "GO:0016183 is defined as 'The formation of clathrin coated pits in the presynaptic membrane "
        "endocytic zone, triggered by the presence of high concentrations of synaptic vesicle components' "
        "- clathrin-mediated endocytosis at the plasma membrane. Seong et al., the cited source, report "
        "nothing of the kind: they compare beta3A- and beta3B-containing AP-3 complexes and measure the "
        "synaptic-vesicle content of ZnT3 and ClC-3, i.e. sorting into vesicles derived from endosomes. "
        "AP-3 vesicle budding is also demonstrably clathrin-independent (PMID:23761069, PMID:42139345). "
        "The process the source actually supports is GO:0016182 synaptic vesicle budding from endosome, "
        "which is proposed as the replacement (a term already on the gene by IBA - a duplicate GO id is "
        "acceptable and is preferable to leaving a mis-scoped term standing)."
    ),
    supported_by=[
        ("PMID:15537701", "Consistently, beta3B deficiency compromised synaptic zinc stores assessed by Timm's staining and the synaptic vesicle targeting of membrane proteins involved in zinc uptake (ZnT3 and ClC-3)."),
        ("PMID:23761069", "These findings indicate that AP-3-clathrin association is dispensable for endosomal AP-3 vesicle budding and suggest that endosomal AP-3-clathrin interactions differ from those by which AP-1 and AP-2 adaptors productively engage clathrin in vesicle biogenesis."),
    ],
    proposed_replacement_terms=[("GO:0016182", "synaptic vesicle budding from endosome")],
    additional_reference_ids=["PMID:23761069"],
)

# 25 GO:0016192 vesicle-mediated transport, InterPro
DECISIONS[25] = dict(
    summary="Fold-level InterPro2GO mapping to a very high-level term.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "IPR002553 is the adaptin-like N-terminal domain shared by the large subunits of AP-1, AP-2, AP-3 "
        "and AP-4, so it can only justify a term at the level of 'vesicle-mediated transport'. True, and "
        "entirely uninformative about which vesicles or which route."
    ),
    supported_by=[Q_ENDO_LYSO],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={"InterPro:IPR002553": ("IPR002553 Clathrin/coatomer adaptor, adaptin-like, N-terminal", "SUPPORTS_TRANSFER", "Shared across all four adaptin large-subunit families; supports only a top-level trafficking term.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 26 GO:0016192 vesicle-mediated transport, NAS
DECISIONS[26] = dict(
    summary="Complex-level author statement; correct and general.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The ComplexPortal NAS records that AP-3 is part of the ubiquitous machinery that loads cargo "
        "into vesicles at endosomal tubules. Correct, but a parent of the specific rows."
    ),
    supported_by=[
        ("PMID:23247405", "Rab32 and Rab38 interact with AP-1, AP-3 and BLOC-2 on early/recycling endosome tubules, where cargo such as tyrosinase and Tyrp1 are loaded into vesicles or transport intermediates."),
    ],
)

# 27 GO:0030117 membrane coat
DECISIONS[27] = dict(
    summary="AP-3 is a membrane coat in the literal, structural sense: spiralling arches linked by ARF1 dimers on a tubulated membrane.",
    action="ACCEPT",
    reason=(
        "The InterPro2GO route is fold-level, but the conclusion is now established directly for human "
        "AP-3 rather than inferred from the adaptin fold: cryo-ET shows AP3:ARF1 remodelling cargo-bearing "
        "membranes into tubules coated in spiralling rows of AP3 arches, and mutating the lattice "
        "interfaces breaks carrier formation in cells. Core."
    ),
    supported_by=[
        ("PMID:42139345", "we demonstrate that AP3:ARF1 spontaneously remodels membranes containing cargo and the phosphoinositide PI(3,5)P2 into tubular structures coated in spiraling rows of AP3 arches and ARF1 dimers"),
        ("PMID:42139345", "Targeted point mutations disrupting critical AP3:ARF1 and AP3:AP3 lattice interfaces disrupt AP3 recruitment, carrier formation, and lysosomal cargo trafficking in cells."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={"InterPro:IPR002553": ("IPR002553 Clathrin/coatomer adaptor, adaptin-like, N-terminal", "SUPPORTS_TRANSFER", "A fold-level signature, but one whose GO mapping happens to be exactly right here: the adaptin N-terminal trunk is the arch that forms the AP-3 lattice.")},
        residue_claims=ARF1_SITE1,
    ),
)

# 28 GO:0030123 AP-3 adaptor complex, IBA
DECISIONS[28] = dict(
    summary="Complex membership at the Eukaryota node, seeded by yeast and Dictyostelium. The defining, core statement about this protein.",
    action="ACCEPT",
    reason=(
        "PTN000513025 carries this with two gene-level donors: SGD:S000006116 (yeast APL5, IMP+IPI from "
        "PMID:9250663, the suppressor screen that showed the four yeast AP-related proteins form one "
        "high-molecular-weight complex) and dictyBase:DDB_G0279537 (UniProtKB:Q54WN0, IDA from "
        "PMID:18634783). Human delta was shown to be a subunit of the same complex in the founding papers. "
        "Note that the GO definition of this term itself records that 'AP-3 does not appear to associate "
        "with clathrin in all organisms', which is consistent with the mammalian clathrin-independence "
        "established since."
    ),
    supported_by=[
        ("PMID:9151686", "Antibodies raised against recombinant delta and sigma3 show that they are the other two subunits of the adaptor-like complex."),
        ("PMID:9250663", "The four yeast subunits are associated in a high-molecular-weight complex."),
        ("PMID:9303295", "Biochemical analyses demonstrated that delta-adaptin is a component of the adaptor-like complex AP-3 in human cells."),
    ],
    additional_reference_ids=["PMID:9303295", "PMID:9250663", "PMID:18634783"],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={
            "PANTHER:PTN000513025": (NODE_25 + " (seeded by yeast APL5 and Dictyostelium ap3d1)", "SUPPORTS_TRANSFER", IN_CLADE_25),
            "SGD:S000006116": ("yeast APL5 (UniProtKB:Q08951)", "SUPPORTS_TRANSFER", "IMP and IPI for this term from PMID:9250663. One of two gene-level donors on this row."),
            "dictyBase:DDB_G0279537": ("Dictyostelium ap3d1 (UniProtKB:Q54WN0)", "SUPPORTS_TRANSFER", "Single Swiss-Prot hit on the UniProt xref search; IDA for this term from PMID:18634783."),
        },
        residue_claims=ARF1_SITE1,
    ),
)

# 29 GO:0030123 AP-3 adaptor complex, InterPro
DECISIONS[29] = dict(
    summary="InterPro2GO from the two delta-specific entries; the mapping is as specific as it could be.",
    action="ACCEPT",
    reason=(
        "IPR017105 is the AP-3 delta-subunit family entry (integrated with PTHR22781) and IPR010474 the "
        "metazoan delta domain. Neither is shared with another adaptin, so the complex assignment is "
        "not a fold-level guess. Independently established experimentally."
    ),
    supported_by=[
        ("PMID:9303295", "Biochemical analyses demonstrated that delta-adaptin is a component of the adaptor-like complex AP-3 in human cells."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        sources={
            "InterPro:IPR010474": ("IPR010474 AP-3 complex subunit delta domain, metazoa", "SUPPORTS_TRANSFER", "Delta-specific metazoan domain."),
            "InterPro:IPR017105": ("IPR017105 Adaptor protein complex AP-3, delta subunit", "SUPPORTS_TRANSFER", "The delta-subunit family entry; integrated with PTHR22781, the family that contains only AP-3 delta proteins."),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 30 GO:0030123 AP-3 adaptor complex, NAS
DECISIONS[30] = dict(
    summary="The paper that named AP-3 and identified delta as one of its four subunits, using an antibody against delta.",
    action="ACCEPT",
    reason=(
        "Recorded as NAS but the paper is the primary human evidence: the p160 band that co-precipitates "
        "with mu3 and beta3 was cloned, shown to be a homolog of the alpha/gamma adaptins, and confirmed "
        "as a complex subunit with a specific antibody. This is the anchor for the whole record."
    ),
    supported_by=[
        ("PMID:9151686", "Antibodies raised against recombinant delta and sigma3 show that they are the other two subunits of the adaptor-like complex."),
        ("PMID:9151686", "The other two proteins that coimmunoprecipitate with μ3 and β3, p160 and p25, are labeled δ and σ3, respectively."),
    ],
)

# 31 GO:0030424 axon
DECISIONS[31] = dict(
    summary="Mouse immuno-EM places most AP-3 in presynaptic axonal compartments; transferred by orthology.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Mouse Ap3d1 carries GO:0030424 as IDA from PMID:20089890, where quantitative immuno-EM put the "
        "majority of AP-3 immunoreactivity in presynaptic axonal compartments of striatum and "
        "hippocampus. Sound transfer, neuron-specific context."
    ),
    supported_by=[
        ("PMID:20089890", "Quantitative immunoelectron microscopy demonstrated that the majority of AP-3 immunoreactivity in both wild-type striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA for GO:0030424 from PMID:20089890."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 32 GO:0032438 melanosome organization, IC
DECISIONS[32] = dict(
    summary="Inferred by the curator from the endosome-to-melanosome transport annotation on the same paper. Real, and cell-type specific.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The IC is drawn from GO:0035646 on the same reference, and the underlying biology is among the "
        "best-established facts about AP-3 delta: garnet flies have reduced eye pigment granules, mocha "
        "mice have coat and eye colour dilution, and HPS10 patients have oculocutaneous albinism. It is "
        "kept as non-core because melanosome biogenesis is the melanocyte instance of the single generic "
        "sorting step AP-3 performs, not a separate evolved activity of delta."
    ),
    supported_by=[
        Q_MOCHA,
        ("PMID:9303295", "Examination by light and electron microscopy indicated that these mutant flies have reduced numbers of eye pigment granules, which correlates with decreased levels of both pteridine (red) and ommachrome (brown) pigments."),
    ],
    additional_reference_ids=["PMID:9697856", "PMID:9303295"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={"GO:0035646": ("GO:0035646 endosome to melanosome transport (the annotation this IC was inferred from)", "SUPPORTS_TRANSFER", "The curator's stated basis is the gene's own transport annotation on the same reference, which is itself an IMP. Not a gene-product donor, so no donor tracing applies.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 33 GO:0032502 developmental process -- over-annotated
DECISIONS[33] = dict(
    summary="A root-adjacent term carrying no information, from a rule whose published condition sets do not account for it.",
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "ARBA00028739 has 893 condition sets and AP3D1 satisfies none of them: no set names PTHR22781, "
        "and none of AP3D1's three FunFams (1.25.10.10:FF:000785, 1.25.10.10:FF:000808, "
        "3.30.450.50:FF:000001) appears. I am not claiming the annotation is biologically false - HPS10 "
        "patients do have neurodevelopmental delay - only that the published rule cannot be shown to "
        "produce it, and that 'developmental process' is one step below the biological_process root and "
        "tells a reader nothing. The same provenance gap has been recorded for other ARBA rules in this "
        "repository."
    ),
    supported_by=[
        ("PMID:26744459", "AP3δ deficiency thus causes a severe neurologic disorder with immunodeficiency and albinism that we propose to classify as HPS10."),
    ],
    prop=dict(
        root_cause="SOURCE_WEAK_OR_INFERRED",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={"ARBA:ARBA00028739": ("ARBA00028739 (GO:0032502 rule)", "SOURCE_WEAK_OR_INFERRED", "893 condition sets, none satisfiable by AP3D1's InterPro/Pfam/SMART/SUPFAM/PANTHER/FunFam complement as listed in the UniProt record and cross-checked against the InterPro API. The annotation cannot be reproduced from the rule as published.")},
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 34 GO:0035646 endosome to melanosome transport, IMP
DECISIONS[34] = dict(
    summary="Melanocyte instance of the AP-3 endosomal sorting step: tyrosinase and Tyrp1 reach maturing melanosomes from endosomal tubules via AP-3.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The cached record for PMID:22511774 is abstract-only, so I am deferring to the curator on the "
        "experimental detail rather than second-guessing it; the annotation is in any case corroborated "
        "by direct AP-3-deficient melanocyte work showing tyrosinase mis-accumulation in endosomes. Kept "
        "as non-core for the same reason as melanosome organization: this is the melanocyte-specific "
        "readout of the generic endosome-to-lysosome sorting activity, which the core rows state "
        "directly."
    ),
    supported_by=[
        ("PMID:22511774", "These protein complexes control sorting and transport of newly synthesized integral membrane proteins from early endosomes to both lysosomes and LROs such as the melanosome."),
        ("PMID:16162817", "In AP-3-deficient melanocytes, tyrosinase accumulates inappropriately in vacuolar and multivesicular endosomes."),
    ],
    additional_reference_ids=["PMID:16162817"],
)

# 35 GO:0035651 AP-3 adaptor complex binding -- over-annotated
DECISIONS[35] = dict(
    summary="A binding term applied to a constituent subunit of the very complex it names. AP3D1 is AP-3; GO:0030123 part_of already states the relation correctly.",
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "GO:0035651 is 'Binding to an AP-3 adaptor complex' - a function for proteins that engage AP-3 "
        "from outside it, such as BLOC-1 or PI4KIIalpha. The mouse source annotation is IDA from "
        "PMID:19010779, a crosslinking/mass-spectrometry study in which AP-3 complexes were purified and "
        "the associated proteins identified; the finding is that PI4KIIalpha and the BLOC complexes bind "
        "AP-3, not that delta binds AP-3 as an external partner. Applying the term to a subunit inverts "
        "the part/whole relation and duplicates, less accurately, what the three GO:0030123 part_of rows "
        "already say. Not removed, because delta does contact the other subunits, but it is an inverted "
        "and uninformative framing."
    ),
    supported_by=[
        ("PMID:19010779", "AP-3 was co-isolated with BLOC-1, BLOC-2, and homotypic fusion and vacuole protein sorting complex subunits; clathrin; and phosphatidylinositol-4-kinase type II alpha (PI4KIIalpha)."),
        ("PMID:26744459", "AP3 complex formation and the degranulation defect in patient T cells were restored by retroviral reconstitution."),
    ],
    additional_reference_ids=["PMID:19010779"],
    prop=dict(
        root_cause="TERM_SCOPING_PROBLEM",
        failure_modes=["ROLE_CONFLATION"],
        sources=_mouse_ensembl_sources(status="SUPPORTS_SOURCE_BUT_NOT_TARGET", note="Mouse Ap3d1 carries GO:0035651 as IDA from PMID:19010779. The experiment is sound; the term assigns the binder role to a subunit of the complex being bound, and that misframing transfers with it."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 36 GO:0035654 clathrin-coated vesicle cargo loading, AP-3-mediated -- MODIFY
DECISIONS[36] = dict(
    summary="Cargo loading is right; the clathrin-coated-vesicle framing is not, and the clathrin contact that generated it was beta-3's, not delta's.",
    action="MODIFY",
    reason=(
        "Two independent problems with the same term. First, subunit attribution: the cited paper "
        "localises the clathrin interaction to the beta3 appendage domain, i.e. to AP3B1/AP3B2, proteins "
        "in a different PANTHER family (PTHR11134); nothing in it places clathrin on delta. Second, and "
        "decisively, the functional premise has since failed - acute chemical-genetic inactivation of "
        "clathrin leaves AP-3 endosomal budding intact, and the reconstituted human coat forms carriers "
        "from AP-3 arches and ARF1 dimers with no clathrin lattice at all. The GO definition of "
        "GO:0030123 already concedes that AP-3 does not associate with clathrin in all organisms. The "
        "cargo-loading claim survives intact, so the parent GO:0035459 vesicle cargo loading is proposed. "
        "Colocalisation of AP-3 with clathrin is not disputed (PMID:15051738, PMID:16162817) - the "
        "rejected claim is the functional one."
    ),
    supported_by=[
        ("PMID:9545220", "In vitro binding assays showed that mammalian AP-3 did associate with clathrin by interaction of the appendage domain of its beta3 subunit with the amino-terminal domain of the clathrin heavy chain."),
        ("PMID:23761069", "These findings indicate that AP-3-clathrin association is dispensable for endosomal AP-3 vesicle budding and suggest that endosomal AP-3-clathrin interactions differ from those by which AP-1 and AP-2 adaptors productively engage clathrin in vesicle biogenesis."),
        ("PMID:42139345", "By demonstrating that AP3:ARF1 can generate carriers without using a clathrin lattice, we explain the clathrin independence of AP3-mediated trafficking."),
    ],
    proposed_replacement_terms=[("GO:0035459", "vesicle cargo loading")],
    additional_reference_ids=["PMID:23761069", "PMID:42139345", "PMID:15051738"],
)

# 37 GO:0036465 synaptic vesicle recycling, NAS
DECISIONS[37] = dict(
    summary="AP-3 regenerates synaptic vesicles from endosomes, which is part of the recycling cycle; a broad but defensible parent.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Unlike the synaptic-vesicle-coating row from the same reference, this term does not commit to a "
        "mechanism AP-3 lacks. Rat neurons require AP-1 and AP-3 to regenerate vesicles from "
        "activity-dependent bulk endosomes, which is a recycling step, and the source paper's own result "
        "is about the membrane-protein content of synaptic vesicles. Kept as neuronal context."
    ),
    supported_by=[
        ("PMID:22539861", "A key event in this endocytosis mode is the generation of new vesicles from bulk endosomes, which replenish the reserve vesicle pool."),
        ("PMID:15537701", "Our results suggest that concerted nonredundant functions of neuronal and ubiquitous AP-3 provide a mechanism to control the levels of selected membrane proteins in synaptic vesicles."),
    ],
    additional_reference_ids=["PMID:22539861"],
)

# 38 GO:0043195 terminal bouton, IBA
DECISIONS[38] = dict(
    summary="Bilateria node, single mouse donor with a direct immuno-EM annotation. Correct, neuron-specific.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "PTN000513028 carries this on one gene-level donor, MGI:MGI:107734 (mouse Ap3d1, IDA from "
        "PMID:20089890), which put most AP-3 immunoreactivity in presynaptic axonal compartments. A "
        "single well-characterised donor is not weak evidence: the PAINT curator had the whole tree and "
        "alignment in view and placed the node at Bilateria, where synapses exist. Human is inside that "
        "clade and retains every mouse residue at the delta cargo-binding hinge."
    ),
    supported_by=[
        ("PMID:20089890", "Quantitative immunoelectron microscopy demonstrated that the majority of AP-3 immunoreactivity in both wild-type striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "The only gene-level donor on this row; IDA from PMID:20089890."),
            "PANTHER:PTN000513028": (NODE_28, "SUPPORTS_TRANSFER", IN_CLADE_28),
        },
        residue_claims=VAMP7_HINGE,
    ),
)

# 39 GO:0043195 terminal bouton, IEA
DECISIONS[39] = dict(
    summary="Same mouse IDA by the automatic orthology route.",
    action="KEEP_AS_NON_CORE",
    reason="Ensembl Compara transfer of the mouse Ap3d1 IDA from PMID:20089890; same verdict as the IBA row.",
    supported_by=[
        ("PMID:20089890", "Quantitative immunoelectron microscopy demonstrated that the majority of AP-3 immunoreactivity in both wild-type striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA for GO:0043195 from PMID:20089890."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 40 GO:0048490 anterograde synaptic vesicle transport, IBA
DECISIONS[40] = dict(
    summary="Bilateria node, mouse IMP donor: AP-3 is needed for cargo to leave the cell body for the synapse.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Single gene-level donor MGI:MGI:107734, with its own IMP from PMID:21998198 showing that "
        "AP-3-BLOC-1 sorting acts in cell bodies upstream of nerve terminals. Correctly placed at "
        "Bilateria; correctly on delta, which is in both AP-3 forms. Neuron-specific context."
    ),
    supported_by=[
        ("PMID:21998198", "Reduction of PI4KIIα in the dentate reflects a failure to traffic from the cell body."),
        ("PMID:21998198", "PI4KIIα was targeted to processes in wild-type primary cultured cortical neurons and PC12 cells but failed to reach neurites in cells lacking either AP-3 or BLOC-1."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "The only gene-level donor on this row; IMP from PMID:21998198."),
            "PANTHER:PTN000513028": (NODE_28, "SUPPORTS_TRANSFER", IN_CLADE_28),
        },
        residue_claims=VAMP7_HINGE,
    ),
)

# 41 GO:0048490 anterograde synaptic vesicle transport, IEA
DECISIONS[41] = dict(
    summary="Same mouse IMP by Ensembl Compara.",
    action="KEEP_AS_NON_CORE",
    reason="Automatic orthology transfer of the mouse Ap3d1 IMP from PMID:21998198; same verdict as the IBA and ISS rows for this term.",
    supported_by=[
        ("PMID:21998198", "PI4KIIα was targeted to processes in wild-type primary cultured cortical neurons and PC12 cells but failed to reach neurites in cells lacking either AP-3 or BLOC-1."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IMP for GO:0048490 from PMID:21998198."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 42 GO:0048490 anterograde synaptic vesicle transport, ISS
DECISIONS[42] = dict(
    summary="Curator sequence-similarity transfer of the same mouse IMP.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "One donor, mouse Ap3d1. The similarity judgement is easy to defend here: human and mouse delta "
        "are reciprocal 1:1 orthologs in PTHR22781:SF12 and align residue-for-residue over the ARF1 "
        "interfaces and the VAMP7-binding hinge, so no divergence argument stands against the transfer. "
        "Non-core for the tissue-context reason only."
    ),
    supported_by=[
        ("PMID:21998198", "PI4KIIα was targeted to processes in wild-type primary cultured cortical neurons and PC12 cells but failed to reach neurites in cells lacking either AP-3 or BLOC-1."),
    ],
    additional_reference_ids=["file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={"UniProtKB:O54774": (MOUSE[0], "SUPPORTS_TRANSFER", "The sole donor; mouse Ap3d1 IMP from PMID:21998198.")},
        residue_claims=VAMP7_HINGE,
    ),
)

# 43 GO:0048499 synaptic vesicle membrane organization, IBA
DECISIONS[43] = dict(
    summary="Bilateria node, mouse IMP: AP-3 sets the membrane-protein composition of synaptic vesicles.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Single gene-level donor MGI:MGI:107734, IMP from PMID:15860731 (Vglut1 and ZnT3 co-targeting to "
        "vesicles in PC12 cells). Corroborated by the beta3A/beta3B knockout comparison, in which "
        "synaptic-vesicle ZnT3 and ClC-3 content moves in opposite directions depending on which AP-3 "
        "form is missing - a result only interpretable if delta is in both. Neuronal context."
    ),
    supported_by=[
        ("PMID:15537701", "Surprisingly, despite the lack of neurological symptoms, beta3A-deficient mouse brain possessed significantly increased synaptic zinc stores and synaptic vesicle content of ZnT3 and ClC-3."),
        Q_TWO_FORMS,
    ],
    additional_reference_ids=["PMID:15860731"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "The only gene-level donor on this row; IMP from PMID:15860731."),
            "PANTHER:PTN000513028": (NODE_28, "SUPPORTS_TRANSFER", IN_CLADE_28),
        },
        residue_claims=VAMP7_HINGE,
    ),
)

# 44 GO:0048840 otolith development
DECISIONS[44] = dict(
    summary="From the mouse otoconia phenotype of the mocha allele. Inside the term's Vertebrata constraint, and matched by hearing loss in AP3D1 patients - but an organismal outcome, not a molecular role.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Mouse Ap3d1 carries GO:0048840 as IMP from PMID:15109702, a gravity-receptor study in which "
        "mocha is one of the otoconia-deficient strains. GO:0048840 carries an only_in_taxon constraint "
        "to Vertebrata (taxId 7742, checked on the QuickGO constraints endpoint), so a human annotation "
        "violates nothing. The transfer is also independently plausible: inner-ear degeneration is part "
        "of the original mocha description, impaired hearing is part of the HPS10 phenotype, and a "
        "homozygous AP3D1 missense variant presents as sensorineural hearing loss. Non-core because this "
        "is several steps downstream of what delta does molecularly."
    ),
    supported_by=[
        Q_MOCHA,
        ("PMID:15109702", "The purpose of the present study was to examine gravity receptor function in mutant mouse strains with variable deficits in otoconia: lethal milk (lm), pallid (pa), tilted (tlt), mocha (mh), and muted (mu)."),
        ("PMID:36445457", "Loss-of-function variants in AP3D1 have been linked to Hermansky-Pudlak syndrome (HPS) 10, a severe multisystem disorder characterized by oculocutaneous albinism, immunodeficiency, neurodevelopmental delay, hearing loss (HL), and neurological abnormalities, fatal in early childhood."),
    ],
    additional_reference_ids=["PMID:15109702", "PMID:36445457", "PMID:9697856"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IMP for GO:0048840 from PMID:15109702; the mocha allele is one of five otoconia-deficient strains assayed."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 45 GO:0060155 platelet dense granule organization, NAS
DECISIONS[45] = dict(
    summary="Platelet dense granules are lysosome-related organelles built by the AP-3 pathway; the storage-pool defect is documented in mocha mice and in HPS10 patients.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The ComplexPortal NAS comes from a review, and that review states the HPS link rather than "
        "assaying AP-3 in platelets. The claim is nonetheless well supported by primary work not cited in "
        "the annotation: mocha is a platelet storage-pool deficiency model, and the second HPS10 family "
        "was shown to have an abnormal platelet storage pathway. Cell-type-specific outcome of the core "
        "sorting step."
    ),
    supported_by=[
        ("PMID:23247405", "For example, Hermansky-Pudlak Syndrome (HPS) patients and the corresponding animal models have abnormal melanosomes, platelet dense granules and lamellar bodies of lung type II epithelial cells."),
        Q_MOCHA,
        ("PMID:30472485", "We further demonstrated an abnormal storage pathway in the platelets."),
    ],
    additional_reference_ids=["PMID:9697856", "PMID:30472485"],
)

# 46 GO:0072657 protein localization to membrane, IEA
DECISIONS[46] = dict(
    summary="Broad but correct parent; the mouse donor arm has a real IMP behind it, while the ARBA arm cannot be reproduced.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Two different kinds of support on one row. The Ensembl arm transfers mouse Ap3d1's IMP from "
        "PMID:16760431, where AP-3 deficiency mistargets LAMP1, PI4KIIalpha and VAMP7-TI - real evidence. "
        "The ARBA arm is weaker: ARBA00029167 has 26 condition sets, all FunFam-based, and none of "
        "AP3D1's three FunFams appears in any of them, so the rule as published does not account for the "
        "annotation. The term stands on the mouse arm."
    ),
    supported_by=[
        ("PMID:16760431", "Mouse mutants that cause BLOC-1 or AP-3 deficiencies affected the targeting of LAMP1, phosphatidylinositol-4-kinase type II alpha, and VAMP7-TI."),
    ],
    additional_reference_ids=["PMID:16760431"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["GRANULARITY_MISMATCH"],
        sources={
            "ARBA:ARBA00029167": ("ARBA00029167 (GO:0072657 rule)", "SOURCE_WEAK_OR_INFERRED", "26 condition sets, all FunFam-based; none names any of AP3D1's three FunFams, so this arm cannot be reproduced from the published rule."),
            "UniProtKB:O54774": (MOUSE[0], "SUPPORTS_TRANSFER", "Mouse Ap3d1 IMP for GO:0072657 from PMID:16760431 -- this arm is what the annotation actually rests on."),
            "ensembl:ENSMUSP00000020420": ("mouse Ap3d1 (Ensembl translation)", "SUPPORTS_TRANSFER", ENSMUS_NOTE),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 47 GO:0072657 protein localization to membrane, IMP
DECISIONS[47] = dict(
    summary="Human experimental row from the melanocyte trafficking study; correct, and very general.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The cached record is abstract-only, so I defer to the curator on the experimental detail. The "
        "claim itself - AP-3 controls where integral membrane proteins end up - is the generic "
        "description of the complex's job, and is stated more informatively by the endosome-to-lysosome "
        "and cargo-adaptor rows."
    ),
    supported_by=[
        ("PMID:22511774", "These protein complexes control sorting and transport of newly synthesized integral membrane proteins from early endosomes to both lysosomes and LROs such as the melanosome."),
    ],
)

# 48 GO:0098793 presynapse
DECISIONS[48] = dict(
    summary="Mouse immuno-EM; presynaptic localisation of AP-3 in striatum and hippocampus.",
    action="KEEP_AS_NON_CORE",
    reason="Mouse Ap3d1 carries GO:0098793 as IDA from PMID:20089890. Sound orthology transfer of a neuron-specific localisation.",
    supported_by=[
        ("PMID:20089890", "Quantitative immunoelectron microscopy demonstrated that the majority of AP-3 immunoreactivity in both wild-type striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA for GO:0098793 from PMID:20089890."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 49 GO:0098794 postsynapse
DECISIONS[49] = dict(
    summary="Postsynaptic AP-3 acts in AMPA-receptor traffic to late endosomes/lysosomes during LTD.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Mouse Ap3d1 carries GO:0098794 as IDA from PMID:20089890, and the postsynaptic role is "
        "independently established: stargazin binds AP-3A and that interaction routes AMPA receptors from "
        "early endosomes to late endosomes/lysosomes. A genuine second compartment for AP-3 in neurons, "
        "still neuron-specific context."
    ),
    supported_by=[
        ("PMID:24217640", "Here we show that stargazin, a transmembrane AMPA receptor regulatory protein, forms a ternary complex with adaptor proteins AP-2 and AP-3A in hippocampal neurons, depending on its phosphorylation state."),
    ],
    additional_reference_ids=["PMID:24217640"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA for GO:0098794 from PMID:20089890; the postsynaptic function is separately documented in PMID:24217640."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 50 GO:0098830 presynaptic endosome, IBA
DECISIONS[50] = dict(
    summary="Bilateria node, mouse IDA: the early-endosomal compartment from which synaptic vesicles are regenerated.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Single gene-level donor MGI:MGI:107734, IDA from PMID:19144828, which used high-resolution "
        "deconvolution microscopy to identify early endosomes where synaptic-vesicle and lysosomal "
        "membrane proteins coexist with AP-3 in neuronal cells. This is the neuronal version of the same "
        "endosomal compartment the Eukaryota node asserts generically, which is why the two nodes carry "
        "different terms for what is mechanistically one location."
    ),
    supported_by=[
        ("PMID:19144828", "Using high-resolution deconvolution microscopy, we identified early endosomal compartments where both selected synaptic vesicle and lysosomal membrane proteins coexist with the adaptor protein complex 3 (AP-3) in neuronal cells."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "The only gene-level donor on this row; IDA from PMID:19144828."),
            "PANTHER:PTN000513028": (NODE_28, "SUPPORTS_TRANSFER", IN_CLADE_28),
        },
        residue_claims=VAMP7_HINGE,
    ),
)

# 51 GO:0098830 presynaptic endosome, IEA
DECISIONS[51] = dict(
    summary="Same mouse IDA by Ensembl Compara.",
    action="KEEP_AS_NON_CORE",
    reason="Automatic orthology transfer of the mouse Ap3d1 IDA from PMID:19144828; same verdict as the IBA row.",
    supported_by=[
        ("PMID:19144828", "Using high-resolution deconvolution microscopy, we identified early endosomal compartments where both selected synaptic vesicle and lysosomal membrane proteins coexist with the adaptor protein complex 3 (AP-3) in neuronal cells."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA for GO:0098830 from PMID:19144828."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 52 GO:0098943 NT receptor transport postsynaptic endosome to lysosome, IBA
DECISIONS[52] = dict(
    summary="Bilateria node; the mouse donor carries IDA, IEP and IMP for this term from the stargazin/AMPA-receptor LTD study.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "MGI:MGI:107734 is the single gene-level donor, and it is unusually well evidenced for this term "
        "- QuickGO shows IDA, IEP and IMP, all from PMID:24217640. That paper shows the "
        "stargazin-AP-3A interaction is required for AMPA receptors to reach late endosomes/lysosomes, "
        "and that blocking it upregulates surface recycling instead. Delta is a subunit of AP-3A, so the "
        "annotation is correctly placed. Neuron-specific context."
    ),
    supported_by=[
        ("PMID:24217640", "Inhibiting the stargazin-AP-2 interaction disrupts NMDA-induced AMPA receptor endocytosis, and inhibiting that of stargazin-AP-3A abrogates the late endosomal/lysosomal trafficking of AMPA receptors, thereby upregulating receptor recycling to the cell surface."),
    ],
    additional_reference_ids=["PMID:24217640"],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "MGI:MGI:107734": (MOUSE[0], "SUPPORTS_TRANSFER", "The only gene-level donor; carries IDA, IEP and IMP for this term from PMID:24217640."),
            "PANTHER:PTN000513028": (NODE_28, "SUPPORTS_TRANSFER", IN_CLADE_28),
        },
        residue_claims=VAMP7_HINGE,
    ),
)

# 53 GO:0098943 NT receptor transport, IEA
DECISIONS[53] = dict(
    summary="Same mouse evidence by Ensembl Compara.",
    action="KEEP_AS_NON_CORE",
    reason="Automatic orthology transfer of the mouse Ap3d1 IDA/IEP/IMP from PMID:24217640; same verdict as the IBA row.",
    supported_by=[
        ("PMID:24217640", "Inhibiting the stargazin-AP-2 interaction disrupts NMDA-induced AMPA receptor endocytosis, and inhibiting that of stargazin-AP-3A abrogates the late endosomal/lysosomal trafficking of AMPA receptors, thereby upregulating receptor recycling to the cell surface."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA/IEP/IMP for GO:0098943 from PMID:24217640."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 54 GO:0098978 glutamatergic synapse
DECISIONS[54] = dict(
    summary="The synapse type in which the AP-3A/stargazin AMPA-receptor work was done.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Mouse Ap3d1 carries GO:0098978 with IDA, IEP and IMP, all from PMID:24217640 - CA1 hippocampal "
        "glutamatergic synapses. A correct SynGO-style location annotation and a narrow one: it records "
        "where the experiment was done rather than a delta-specific property."
    ),
    supported_by=[
        ("PMID:24217640", "Similarly, stargazin's interaction with AP-2 or AP-3A is necessary for low-frequency stimulus-evoked LTD in CA1 hippocampal neurons."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources=_mouse_ensembl_sources(note="Mouse Ap3d1 IDA/IEP/IMP for GO:0098978 from PMID:24217640."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 55 GO:0140916 zinc ion import into lysosome -- MODIFY
DECISIONS[55] = dict(
    summary="The delta-specific knockdown is sound, but AP-3 is not the zinc importer - it delivers the ZnT transporters that are.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The experiment is squarely about this gene product: the siRNA targeted delta and depleted the "
        "complex, and vesicular zinc fell. The caveat worth recording is that AP-3 is not itself the "
        "zinc importer - GO:0140916 is 'The directed import of zinc(2+) from the cytosol, across an "
        "organelle membrane, into a lysosome', a transmembrane transport event that ZnT2/ZnT3 perform - "
        "and the paper's own decisive result makes the point, since overexpressing GFP-ZnT2 RESCUES the "
        "AP-3-depleted phenotype, which is only interpretable if the AP-3 defect is a failure to deliver "
        "the transporter. I first proposed replacing the term with GO:0061462 protein localization to "
        "lysosome and have withdrawn that: GO:0061462 is an ancestor of GO:0006622 protein targeting to "
        "lysosome, which this review adds as a NEW row, so the substitution would have traded the "
        "zinc-specific content for a parent the file already carries, and no zinc-preserving alternative "
        "exists in GO for an upstream trafficking factor. For a biological process, involved_in also "
        "tolerates indirect-but-required participation in a way that a molecular-function term would "
        "not, and this is a curator IMP made from the full text. Kept, marked non-core: it is a "
        "downstream consequence of the generic AP-3 sorting step rather than delta's own activity."
    ),
    supported_by=[
        ("PMID:17349999", "For AP-3 protein complex knockdown, the target was the δ subunit of the complex."),
        ("PMID:17349999", "Moreover, GFP-ZnT2 overexpression elicited a significant accumulation of zinc within mature lysosomes, which in untransfected M1 cells contained little or no chelatable zinc, and restored the zinc storage capability of AP-3-deficient cells."),
    ],
)

# 56 GO:1903232 melanosome assembly, NAS
DECISIONS[56] = dict(
    summary="Complex-level statement that AP-3 is part of the machinery building melanosomes.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Same review source and the same reasoning as the platelet dense granule row: correct, and "
        "strongly corroborated by primary work (garnet, mocha, HPS10 albinism, AP-3-deficient melanocytes). "
        "Cell-type-specific outcome rather than the core molecular role, and partly redundant with the "
        "melanosome organization IC."
    ),
    supported_by=[
        ("PMID:23247405", "Packaging of the tyrosinases into transport vesicles at early/recycling endosome-associated tubules is dependent on ubiquitous adaptor protein complex (AP)-1 and AP-3, and biogenesis of lysosome-related organelles complex (BLOC)-1 and BLOC-2."),
        ("PMID:16162817", "In AP-3-deficient melanocytes, tyrosinase accumulates inappropriately in vacuolar and multivesicular endosomes."),
    ],
    additional_reference_ids=["PMID:16162817"],
)

# 57 GO:1904115 axon cytoplasm
DECISIONS[57] = dict(
    summary="A GOC term-to-term inference from the two axonal-transport process annotations, not a localisation observation.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The supporting entities on this row are GO terms, not gene products: GO:0008089 and GO:0048490, "
        "i.e. the inference is 'a protein involved in anterograde axonal transport is in axon cytoplasm'. "
        "That is sound as far as it goes, and the conclusion is corroborated by mouse immuno-EM placing "
        "AP-3 in presynaptic axonal compartments. But its content is entirely derived from the two "
        "process rows, both of which are themselves non-core neuronal context."
    ),
    supported_by=[
        ("PMID:20089890", "Quantitative immunoelectron microscopy demonstrated that the majority of AP-3 immunoreactivity in both wild-type striatum and hippocampus localizes to presynaptic axonal compartments, where it regulates synaptic vesicle size."),
    ],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        failure_modes=["CONTEXT_OR_TISSUE_MISMATCH"],
        sources={
            "GO:0008089": ("GO:0008089 anterograde axonal transport (the process annotation this was inferred from)", "SUPPORTS_TRANSFER", "A GO term, not a gene-product donor: the row is a term-to-term inference, so there is no donor record to trace. The underlying process row is itself an orthology transfer of a mouse IMP."),
            "GO:0048490": ("GO:0048490 anterograde synaptic vesicle transport (the process annotation this was inferred from)", "SUPPORTS_TRANSFER", "As above; the second process term feeding the same inference."),
        },
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)

# 58 GO:1990742 microvesicle -- REMOVE
DECISIONS[58] = dict(
    summary="GO:1990742 means an EXTRACELLULAR vesicle shed from the plasma membrane. The donor annotation uses 'microvesicle' in the source paper's sense of small INTRACELLULAR AP-3/BLOC-1 vesicles.",
    action="REMOVE",
    reason=(
        "The GO definition is explicit: 'An extracellular vesicle released from the plasma membrane and "
        "ranging in size from about 100 nm to 1000 nm.' The mouse donor annotation (IDA and IMP, "
        "PMID:16760431) is about a very different object - small vesicles isolated from cell homogenates "
        "that carry BLOC-1, AP-3 subunits and the AP-3 cargoes LAMP1, PI4KIIalpha and VAMP7-TI. A vesicle "
        "loaded with LAMP1 and a PI 4-kinase, recovered from a PC12 membrane fraction, is an intracellular "
        "transport intermediate, not a shed extracellular vesicle, and no AP-3 literature places delta on "
        "extracellular microvesicles. The defect is on the donor side and it propagates unchanged through "
        "Ensembl Compara. Mouse Ap3d1 has no review in this repository, so there is no upstream file to "
        "correct; the problem is recorded here instead."
    ),
    supported_by=[
        ("PMID:16760431", "we show that the BLOC-1 complex resides on microvesicles that also contain AP-3 subunits and membrane proteins that are known AP-3 cargoes"),
        ("PMID:16760431", "Mouse mutants that cause BLOC-1 or AP-3 deficiencies affected the targeting of LAMP1, phosphatidylinositol-4-kinase type II alpha, and VAMP7-TI."),
    ],
    additional_reference_ids=["PMID:16760431"],
    prop=dict(
        root_cause="SOURCE_BAD",
        failure_modes=["COMPARTMENT_OR_COMPLEX_MISMATCH"],
        sources=_mouse_ensembl_sources(status="SOURCE_BAD", note="Mouse Ap3d1 carries GO:1990742 as IDA and IMP from PMID:16760431. The experiment is real; the GO term chosen for it denotes an extracellular vesicle, while the paper's 'microvesicles' are intracellular AP-3/BLOC-1 transport intermediates."),
        residue_claims_not_applicable=NOT_RESIDUE,
    ),
)


# --- rows to add ------------------------------------------------------------

NEW_ROWS = [
    dict(
        term=("GO:0031267", "small GTPase binding"),
        evidence_type="IPI",
        original_reference_id="PMID:39705307",
        qualifier="enables",
        summary="Delta carries the primary ARF1-GTP binding site of AP-3 - two interfaces on the trunk, both required for membrane recruitment in cells.",
        action="NEW",
        reason=(
            "AP3D1 has no informative molecular function in GOA, yet its best-characterised subunit-level "
            "activity is binding the small GTPase ARF1. Reconstituted human AP-3 hemicomplexes show the "
            "binding is delta's, not beta-3's; the cryo-EM series resolves AP-3 engaging the membrane "
            "through the delta-ARF1 interface first; and in HeLa cells, mutating either of the two delta "
            "ARF1 interfaces (F77/M110/L111 and H157/K159/R163/R187) relocalises delta to the cytosol. "
            "All seven residues are present at those positions in O14617 "
            "(AP3D1-bioinformatics/delta_interfaces.tsv), and site 1 is conserved 3/3 across the "
            "PTHR22781 family from budding yeast to human while scoring 1/3 in every out-of-family "
            "adaptin large subunit. GO:0031267 is already used this way for the AP-1 large subunit "
            "AP1G1 and for AP3M1, both by IPI."
        ),
        supported_by=[
            ("PMID:39705307", "This suggests that the primary Arf1 binding site on AP-3 is on δ"),
            ("PMID:39705307", "it is apparent that the δ-σ3 complex binds nearly as well as the full complex, with binding of the β3-μ3 hemicomplex barely above background levels in the Arf1GTP state"),
            ("PMID:42139345", "These data indicate that δ requires both ARF1 interfaces for correct membrane recruitment"),
            ("PMID:42139345", "Mutations in AP3D1 that abolish interaction with ARF1 sites relocalize δ-WT-SG to the cytosol."),
        ],
        additional_reference_ids=["PMID:42139345", "PMID:9679139", "file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md"],
    ),
    dict(
        term=("GO:0000149", "SNARE binding"),
        evidence_type="IPI",
        original_reference_id="PMID:22521722",
        qualifier="enables",
        summary="The delta hinge (residues 680-729) is a dedicated receptor for the longin domain of VAMP7, and only when VAMP7 is engaged in a cis-SNARE complex.",
        action="NEW",
        reason=(
            "A second missing molecular function, and one that is delta's alone rather than the complex's: "
            "the crystal structure (PDB 4AFI, whose chains A/B UniProt maps to O14617 680-729) resolves "
            "the delta linker bound to the VAMP7 longin domain, with a measured KD of 14 uM, and mutating "
            "I702/V704 or L709/L713 abolishes binding in vitro and in vivo while leaving complex assembly "
            "intact. In melanocytes the same interface is required for sorting: cells expressing "
            "VAMP7-non-binding delta fail to load a STX13-VAMP7 cis-SNARE complex into transport carriers "
            "and are hypopigmented. The four hinge residues are present in O14617 and are conserved 4/4 in "
            "mouse and bovine delta but 0/4 or 1/4 in AP3B1, AP1G1, AP2A1 and AP4E1, i.e. the interface is "
            "delta-private (AP3D1-bioinformatics/delta_interfaces.tsv)."
        ),
        supported_by=[
            ("PMID:22521722", "We show that the linker of the δ-adaptin subunit of AP3 binds the VAMP7 longin domain and determines the structure of their complex."),
            ("PMID:22521722", "Mutation to serine of residues Ile702 and Val704 (mut1) and of Leu709 and Leu713 (mut2) in the δ-adaptin, which play key roles in the VAMP7:δ-adaptin interface"),
            ("PMID:22521722", "The binding of VAMP7 to δ-adaptin requires the VAMP7 SNARE motif to be engaged in SNARE complex formation and hence AP3 must transport VAMP7 when VAMP7 is part of a cis-SNARE complex."),
            ("PMID:33886957", "Sorting requires either recognition of VAMP7 by the AP-3δ subunit of AP-3 or of STX13 by the pallidin subunit of BLOC-1, but not both."),
        ],
        additional_reference_ids=["PMID:33886957", "file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md"],
    ),
    dict(
        term=("GO:0006622", "protein targeting to lysosome"),
        evidence_type="IMP",
        original_reference_id="PMID:42139345",
        qualifier="involved_in",
        summary="The human-specific child of the IBA term: AP-3 delta delivers integral membrane cargo to lysosomes, and point mutants that break the coat break lysosomal cargo traffic in human cells.",
        action="NEW",
        reason=(
            "GOA carries the compartment-agnostic parent GO:0006623 protein targeting to vacuole by IBA "
            "from a yeast-seeded node, but not the lysosomal child that applies to human "
            "(GO:0006622 is_a GO:0006623, confirmed on the QuickGO ancestors endpoint). There is direct "
            "human loss-of-function evidence: HeLa cells in which endogenous delta was removed by "
            "transient CRISPR-KO and complemented with interface point mutants show disrupted lysosomal "
            "cargo trafficking. Independent support comes from AP-3-deficient cells mistargeting LAMP1 "
            "and from CLN3 requiring AP-3 for lysosomal delivery via its dileucine motif. The "
            "affinage deep-research record is cited on this row because its entire narrative is "
            "AP3D1 selecting cargo for lysosomal delivery (IFNGR1, DRAM2, RNF13). It is a lead, "
            "not evidence: no supporting_text is drawn from it, and each lead it offered was "
            "re-checked against its own PMID before being used."
        ),
        supported_by=[
            ("PMID:42139345", "Targeted point mutations disrupting critical AP3:ARF1 and AP3:AP3 lattice interfaces disrupt AP3 recruitment, carrier formation, and lysosomal cargo trafficking in cells."),
            ("PMID:15598649", "The dileucine motif of CLN3 bound both AP-1 and AP-3 in vitro, and expression of mutated CLN3 in AP-1- or AP-3-deficient mouse fibroblasts showed that both adaptor complexes are required for sequential sorting of CLN3 via this motif."),
            Q_TUBULAR,
        ],
        additional_reference_ids=["PMID:15598649", "PMID:15051738", "file:human/AP3D1/AP3D1-deep-research-affinage.md"],
    ),
    dict(
        term=("GO:0005198", "structural molecule activity"),
        evidence_type="IMP",
        original_reference_id="PMID:26744459",
        qualifier="enables",
        summary="Delta is a structural constituent of AP-3: without it the heterotetramer does not assemble, and restoring it restores the complex.",
        action="NEW",
        reason=(
            "AP3D1's only molecular-function rows in GOA are bare protein binding and an inverted "
            "AP-3-adaptor-complex-binding IEA, so the plainest subunit-level fact about the protein is "
            "unstated: delta holds the complex together. GO:0005198 is defined as 'The action of a "
            "molecule that contributes to the structural integrity of a complex', which is exactly the "
            "observation. The evidence is human and loss-and-restore: a homozygous AP3D1 mutation "
            "destabilises AP-3 in patient cells and retroviral re-expression of wild-type AP3D1 restores "
            "complex formation. The mouse mocha counterpart is the same result in reverse - the complex "
            "is destabilised in mocha fibroblasts and rescued by transfected delta, including by "
            "VAMP7-non-binding delta mutants, which shows the structural role is separable from the "
            "cargo-binding role. Added because core_functions asserts this activity and it should be "
            "traceable to an annotation."
        ),
        supported_by=[
            ("PMID:26744459", "Whole exome sequencing identified a homozygous mutation in AP3D1 that leads to destabilization of the adaptor protein 3 (AP3) complex."),
            ("PMID:26744459", "AP3 complex formation and the degranulation defect in patient T cells were restored by retroviral reconstitution."),
            ("PMID:22521722", "The absence of delta-adaptin causes destabilization of the AP3 complex in mouse mocha fibroblasts and mislocalization of VAMP7."),
            ("PMID:22521722", "Re-expression of wt and mutant δ-adaptin led to similar levels of stabilization of the other subunits of the complex"),
        ],
        additional_reference_ids=["PMID:22521722"],
    ),
    dict(
        term=("GO:0043316", "cytotoxic T cell degranulation"),
        evidence_type="IMP",
        original_reference_id="PMID:26744459",
        qualifier="involved_in",
        summary="HPS10 patient CD8+ T cells fail to degranulate, and retroviral re-expression of wild-type AP3D1 fully restores the response.",
        action="NEW",
        reason=(
            "Lytic granules are lysosome-related organelles, so this is the immune-cell instance of the "
            "AP-3 sorting pathway, and it is the phenotype that defined HPS10. The evidence is as clean "
            "as a human IMP gets: a homozygous AP3D1 mutation destabilises the complex, patient CD8+ T "
            "cell degranulation is reduced, and transduction with an AP3D1-containing vector - but not "
            "the empty vector - restores it to wild-type levels in two independent experiments. UniProt "
            "records the same conclusion in its FUNCTION block. Not currently in GOA for this gene."
        ),
        supported_by=[
            ("PMID:26744459", "AP3 complex formation and the degranulation defect in patient T cells were restored by retroviral reconstitution."),
            ("PMID:26744459", "Importantly, transduction with the AP3D1 containing vector fully restored the degranulation response of patient cells to levels of wild-type cells in two independent experiments"),
        ],
        additional_reference_ids=["file:human/AP3D1/AP3D1-uniprot.txt"],
    ),
    dict(
        term=("GO:0043320", "natural killer cell degranulation"),
        evidence_type="IMP",
        original_reference_id="PMID:26744459",
        qualifier="involved_in",
        summary="The degranulation defect in the HPS10 patient was most severe in fresh NK cells.",
        action="NEW",
        reason=(
            "Recorded separately from the T-cell term because the paper reports the NK phenotype "
            "separately and more severely, and because UniProt's FUNCTION block names both cell types. "
            "The evidence is the patient's own cells rather than the reconstitution experiment, which was "
            "done on T cells, so this row is the weaker of the two - but it is a direct loss-of-function "
            "observation in human NK cells and the cell biology (lytic granules are lysosome-related "
            "organelles built by AP-3) is the same."
        ),
        supported_by=[
            ("PMID:26744459", "It was most evident in fresh NK cells, where the response was very low and indistinguishable from that of patients with familial HLH, GS2 or CHS"),
            ("PMID:26744459", "Since a number of immunodeficiencies with albinism are associated with impaired lymphocyte cytotoxicity, we analyzed expression of the degranulation marker CD107a on fresh"),
        ],
        additional_reference_ids=["file:human/AP3D1/AP3D1-uniprot.txt"],
    ),
]
