"""Per-row curation decisions for the AGT review, keyed by GOA row number.

Row numbers are 1-based over `AGT-goa.tsv` after the header, i.e. the same
numbering `build_review.py` prints. Keeping the decisions here rather than typed
into the YAML means `supporting_entities` and `propagation_review.source_entities`
are generated from the GOA WITH/FROM field itself and cannot drift from it.

Each value is a dict with:
  summary, action, reason        - prose (required)
  supported_by                   - list of (reference_id, verbatim quote)
  replace                        - [(go_id, label)] for MODIFY
  prop                           - propagation_review: dict(root_cause=..., modes=[...],
                                   status={token: (source_status, comment)},
                                   default=(source_status, comment_template),
                                   residue_claims=[...], not_applicable=str)
                                   `comment_template` may use {gene}, {organism},
                                   {protein}, {merops}, filled from the resolved
                                   WITH/FROM table.
"""

# ---------------------------------------------------------------------------
# Quotes used in more than one row, defined once so they cannot drift apart.
# ---------------------------------------------------------------------------

Q_NONINHIB = (
    "PMID:20927107",
    "angiotensinogen-a non-inhibitory member of the serpin family of protease "
    "inhibitors",
)
Q_NO_SR = (
    "PMID:30563843",
    "To confirm conclusions from biochemical experiments that cleavage of the reactive "
    "center loop of AGT does not trigger the stressed-to-relaxed (S-to-R) transition "
    "characteristic of inhibitory serpins, we solved the structure of AGT cleaved by "
    "thermolysin treatment and compared it with that of intact AGT.",
)
Q_LOST_SR = (
    "PMID:30563843",
    "In contrast, it has been shown that AGT has lost the ability to undergo this "
    "typical serpin S-to-R transition (29), confirmed here by our structure of "
    "loop-cleaved AGT, so it was very puzzling why the serpin framework was selected "
    "in the course of evolution as an angiotensin carrier.",
)
Q_MEROPS = (
    "file:human/AGT/AGT-bioinformatics/RESULTS.md",
    "All 7 resolvable seed proteins of IBD node `PTN008970140` are MEROPS inhibitors (7/7).",
)
Q_SECRETED = ("file:human/AGT/AGT-uniprot.txt", "SUBCELLULAR LOCATION: Secreted")
Q_LIVER = (
    "file:human/AGT/AGT-uniprot.txt",
    "TISSUE SPECIFICITY: Expressed by the liver and secreted in plasma.",
)
Q_670 = (
    "PMID:20927107",
    "there is a substantial contact surface of 670Å2 between the bodies of the two "
    "proteins, primarily hydrophobic in nature",
)
Q_TAIL = (
    "PMID:30563843",
    "These structures revealed that AGT undergoes profound conformational changes and "
    "binds renin through a tail-into-mouth allosteric mechanism that inserts the N "
    "terminus into a pocket equivalent to a hormone-binding site on other serpins.",
)
Q_BURIED = (
    "PMID:20927107",
    "The 63-residue amino-terminal tail of angiotensinogen is seen as an ordered "
    "superstructure, anchored by two new helices, and with the renin-cleavage site, "
    "Leu10-Val11 in humans, held in an inaccessibly buried position.",
)
Q_KO = (
    "PMID:7989296",
    "These mice do not produce angiotensinogen in the liver, resulting in the complete "
    "loss of plasma immunoreactive angiotensin I.",
)
Q_KO_BP = (
    "PMID:7989296",
    "The systolic blood pressure of the homozygous mutant mice was 66.9 +/- 4.1 mm Hg, "
    "significantly lower than that of wild-type mice (100.4 +/- 4.4 mm Hg).",
)
Q_RESCUE = (
    "PMID:25691624",
    "High plasma renin concentrations in hepAGT-/- mice were suppressed equally by both "
    "forms of AGT, which were accompanied by comparable increases of plasma AngII "
    "concentrations similar to hepAGT+/+ mice.",
)
Q_RESCUE_BP = (
    "PMID:25691624",
    "AAV-driven expression of both forms of AGT led to equivalent increases of systolic "
    "blood pressure and augmentation of atherosclerotic lesion size in hepAGT-/- mice.",
)
Q_AT1_CLONE = (
    "PMID:1567413",
    "Ligand binding studies of the cloned receptor expressed in COS cells suggested that "
    "it is pharmacologically a type 1 angiotensin II receptor subtype.",
)
Q_AT1_CA = (
    "PMID:1567413",
    "Electrophysiological studies of the receptor expressed in Xenopus laevis oocytes "
    "revealed that it could functionally couple to a second messenger system leading to "
    "the mobilization of intracellular stores of calcium.",
)
Q_AT1A = (
    "PMID:1378723",
    "The expressed gene exhibited high-affinity AII and Dup753 binding and was "
    "functionally coupled to inositol phosphate turnover.",
)
Q_AT2_APOP = (
    "PMID:10406457",
    "Deletion of residues 240-244 within the intermediate portion of the i3 loop resulted "
    "in a complete loss of AT2-mediated apoptosis, inhibition of extracellular "
    "signal-regulated kinases (ERK), and SHP-1 activation.",
)
Q_AT2_SHP1 = (
    "PMID:10406457",
    "Our data demonstrate that the intermediate portion of the i3 loop is important for "
    "AT2 function and that SHP-1 is a proximal effector of the AT2 receptor that is "
    "implicated in the inhibition of ERKs and in the apoptotic effect of this receptor.",
)
Q_HUVEC_NOPROLIF = (
    "PMID:15652490",
    "Moreover, Ang II induces a time- and dose-dependent augmentation in cell migration, "
    "but does not affect HUVEC proliferation.",
)
Q_HUVEC_FAK = (
    "PMID:15652490",
    "In the present study, we demonstrated that Ang II provokes a transitory enhancement "
    "of focal adhesion kinase (FAK) and paxillin phosphorylation in human umbilical "
    "endothelial cells (HUVEC).",
)
Q_DTGR = (
    "PMID:17416596",
    "Rats harboring the human renin and angiotensinogen genes (dTGR) feature angiotensin "
    "(ANG) II/hypertension-induced cardiac damage and die suddenly between wk 7 and 8.",
)
Q_CX43 = (
    "PMID:17416596",
    "Left-ventricular mRNA expression of potassium channel subunit Kv4.3 and gap-junction "
    "protein connexin 43 were significantly reduced in dTGR compared with Los-treated "
    "dTGR and SD.",
)
Q_RTD = (
    "PMID:16116425",
    "We studied 11 individuals with renal tubular dysgenesis, belonging to nine families, "
    "and found that they had homozygous or compound heterozygous mutations in the genes "
    "encoding renin, angiotensinogen, angiotensin converting enzyme or angiotensin II "
    "receptor type 1.",
)
Q_RTD_MECH = (
    "PMID:16116425",
    "We propose that renal lesions and early anuria result from chronic low perfusion "
    "pressure of the fetal kidney, a consequence of renin-angiotensin system inactivity.",
)
Q_Y2H = (
    "PMID:32814053",
    "candidate interactions and is generated by systematic yeast two-hybrid interaction "
    "screening of",
)
Q_Y2H_COMPART = (
    "file:human/AGT/AGT-bioinformatics/RESULTS.md",
    "All ten PMID:32814053 partners are intracellular",
)
Q_SERPIN_SIM = (
    "file:human/AGT/AGT-uniprot.txt",
    "SIMILARITY: Belongs to the serpin family.",
)
Q_1988 = (
    "PMID:3397061",
    "Because angiotensinogen is homologous to other members of the serine protease "
    "inhibitor family, we aligned the putative reactive center of angiotensinogens from "
    "various species.",
)
Q_1988_DIVERGE = (
    "PMID:3397061",
    "This alignment shows that the inhibitor site in human angiotensinogen is different "
    "from its rodent counterpart, but the role of this sequence divergence in the "
    "pathogenesis of human disease remains to be established.",
)

# Standard propagation-source comment templates.
T_SERPIN_SECRETED = (
    "SUPPORTS_TRANSFER",
    "{gene} ({organism}), a secreted serpin; extracellular localisation is correct for "
    "it and transfers correctly to AGT, which is likewise secreted.",
)
T_SERPIN_INHIB = (
    "SUPPORTS_SOURCE_BUT_NOT_TARGET",
    "{gene} ({organism}): {merops_phrase}. A genuine inhibitory serpin with an intact "
    "reactive centre, so the term is right for this seed. It does not transfer to AGT, "
    "which is MEROPS I04.953 - the range reserved for non-inhibitor homologues - and which "
    "has no annotated reactive bond and a proline at the P12 hinge position.",
)


# ---------------------------------------------------------------------------
# Per-row decisions.
# ---------------------------------------------------------------------------

DECISIONS: dict[int, dict] = {}

# ---- IBA rows ------------------------------------------------------------

DECISIONS[1] = dict(
    summary=(
        "Correct family inference. PANTHER node PTN000156123 is the secreted-serpin node "
        "of PTHR11461, and its 49 seeds span the whole functional range of the family - "
        "inhibitory members (SERPINA1, SERPINC1, SERPINE1, SERPINF2) alongside "
        "non-inhibitory ones (SERPINF1/PEDF, SERPINA6/corticosteroid-binding globulin, "
        "SERPINA7/thyroxine-binding globulin, chicken ovalbumin-related protein Y). What "
        "those proteins actually share is secretion, not inhibition, so the node is both "
        "correctly placed and correctly broad. AGT is a liver-secreted plasma protein with "
        "a cleaved signal peptide (residues 1-24) and no transmembrane segment, so it sits "
        "squarely inside the clade that inherited this property."
    ),
    action="ACCEPT",
    reason=(
        "Extracellular localisation is a core, directly evidenced property of AGT and the "
        "phylogenetic inference is sound. That the same family node carries both inhibitory "
        "and non-inhibitory serpins is exactly why this term transfers where GO:0004867 "
        "does not."
    ),
    supported_by=[Q_SECRETED, Q_LIVER],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "PANTHER:PTN000156123": (
                "SUPPORTS_TRANSFER",
                "Secreted-serpin IBD node of PTHR11461, seeded by 49 extant serpins across "
                "plants, insects and vertebrates. Its seeds include non-inhibitory serpins, "
                "so the node captures secretion rather than inhibition and transfers "
                "correctly to AGT.",
            ),
            "UniProtKB:P01019": (
                "SUPPORTS_TRANSFER",
                "AGT itself, the target. Its own IDA (PMID:4300938) and HDA plasma-proteomics "
                "evidence are among the descendant evidences the PAINT curator used to place "
                "this IBD, which is expected and is not circular.",
            ),
        },
        default=T_SERPIN_SECRETED,
    ),
)

DECISIONS[2] = dict(
    summary=(
        "Well-placed, angiotensinogen-specific inference. Node PTN008518321 is not a "
        "family-wide node: it is seeded by mouse Agt (MGI:MGI:87963 = P11859) and human AGT "
        "itself, at taxon 117571 (Euteleostomi). The term describes the pathway initiated "
        "when angiotensin II binds AGTR1/AGTR2, and angiotensin II exists only as a cleavage "
        "product of angiotensinogen, so no other gene could seed it."
    ),
    action="ACCEPT",
    reason=(
        "This is the core biological process of the gene and the node is tightly and "
        "correctly drawn around the angiotensinogens. The three-token WITH/FROM is short "
        "because the clade is small, not because the evidence is thin."
    ),
    supported_by=[Q_AT1_CLONE, Q_KO],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "PANTHER:PTN008518321": (
                "SUPPORTS_TRANSFER",
                "Angiotensinogen-specific IBD node (taxon:117571), seeded by mouse and human "
                "angiotensinogen. Confirmed in the committed PAINT slice for PTHR11461, where "
                "it also carries GO:0042981.",
            ),
            "MGI:MGI:87963": (
                "SUPPORTS_TRANSFER",
                "Mouse Agt (P11859), the 1:1 orthologue. Its own knockout abolishes plasma "
                "angiotensin I (PMID:7989296), which is the strongest possible descendant "
                "evidence that this pathway depends on angiotensinogen.",
            ),
            "UniProtKB:P01019": (
                "SUPPORTS_TRANSFER",
                "Human AGT, the target's own accession. Its five direct GO:0038166 "
                "annotations are among the descendant evidences behind the IBD; the target "
                "appearing in its own WITH/FROM is expected and marks experimental grounding "
                "on the target, not circularity.",
            ),
        },
    ),
)

DECISIONS[3] = dict(
    summary=(
        "Over-propagated family inference, and the clearest defect in this gene's record. "
        "GO:0004867 is defined as 'Binds to and stops, prevents or reduces the activity of a "
        "serine-type endopeptidase'. Angiotensinogen does none of that. It is the SUBSTRATE "
        "of renin, an ASPARTYL protease - wrong catalytic class and wrong role. The serpin "
        "inhibitory mechanism requires cleavage at the reactive centre loop followed by a "
        "stressed-to-relaxed transition that traps the protease, and AGT has been shown "
        "crystallographically to have lost that transition. Sequence analysis agrees: AGT "
        "carries no UniProt 'Reactive bond' site (10 of 12 inhibitors in the panel do), its "
        "P17-P9 hinge is ADEREPTES against SERPINA1's EKGTEAAGA with a helix-breaking Pro430 "
        "at the P12 position that must be small for beta-sheet A insertion, and MEROPS "
        "classes it I04.953, in the range reserved for non-inhibitor homologues. Every one of "
        "the 7 resolvable seed proteins of node PTN008970140 is a MEROPS inhibitor."
    ),
    action="REMOVE",
    reason=(
        "A family-level inference contradicted by the target's own structure and sequence. "
        "The IBD node PTN008970140 is the SERPINA-clade node and every seed that donated the "
        "term is a genuine inhibitory serpin; AGT is the one non-inhibitory member of that "
        "clade and inherits the activity mechanically. No seed annotation is wrong, so this "
        "is a propagation failure, not a source failure, and removing it overrules no "
        "experimental annotation. Note that PAINT already uses IRD in this same family "
        "(node PTN002606963 blocks GO:0005576 for the intracellular subclade); an IRD at the "
        "angiotensinogen node would fix every inherited copy at once."
    ),
    supported_by=[Q_NONINHIB, Q_NO_SR, Q_LOST_SR, Q_MEROPS],
    prop=dict(
        root_cause="PROPAGATION_BAD",
        modes=["FUNCTIONAL_DIVERGENCE", "PSEUDO_OR_SUBACTIVITY_LOSS"],
        status={
            "PANTHER:PTN008970140": (
                "SOURCE_BAD",
                "SERPINA-clade IBD node (taxon:7711) seeded exclusively by inhibitory serpins. "
                "The node assertion is correct for those seeds but its placement covers "
                "angiotensinogen, the one clade member that lost the inhibitory mechanism, so "
                "as an assertion about the clade as a whole it is wrong.",
            ),
        },
        default=T_SERPIN_INHIB,
        residue_claims=[
            dict(
                claim_type="SUBSTITUTED",
                anchor=dict(accession="UniProtKB:P01009", position=371, residue="A",
                            sequence_version=3),
                target=dict(accession="UniProtKB:P01019", position=430, residue="P",
                            sequence_version=4),
                role=("hinge P12; serpin reactive-centre-loop insertion into beta-sheet A "
                      "requires a small residue here"),
                method="MSA",
                comment=(
                    "Global pairwise alignment of P01019 to P01009 anchored on SERPINA1's "
                    "UniProt 'Reactive bond' SITE (P1 = Met382), computed in "
                    "AGT-bioinformatics/serpin_inhibitory.py. AGT's P17-P9 hinge is ADEREPTES "
                    "(P01019 residues 425-433) against SERPINA1's EKGTEAAGA, with 2/4 small "
                    "residues at P12-P9 versus 4/4 for SERPINA1 and a mean 3.58/4 across the "
                    "12 inhibitors in the panel. AGT additionally has no UniProt 'Reactive "
                    "bond' SITE at all, where 10 of those 12 inhibitors do."
                ),
            ),
        ],
    ),
)

DECISIONS[4] = dict(
    summary=(
        "Defensible but peripheral and deliberately generic. The node is the same "
        "angiotensinogen-specific PTN008518321 seeded by mouse Agt, rat Agt and human AGT, "
        "so the inference is not over-propagated. The bare parent term is however the right "
        "level rather than a granularity failure: angiotensin II is pro-apoptotic through "
        "AGTR2 (PMID:10406457, and AGT already carries GO:2001238 positive regulation of "
        "extrinsic apoptotic signaling pathway) and anti-apoptotic/proliferative through "
        "AGTR1, so the effect has no single sign to inherit - not because the donor "
        "angiotensinogens disagree with one another, but because the biology itself is "
        "bidirectional and receptor-dependent. The neutral parent is therefore the "
        "correct least common ancestor. GO's own comment on the term endorses this use."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real but secondary: apoptotic regulation is one downstream consequence of "
        "angiotensin receptor engagement, not what angiotensinogen is for. Kept at the parent "
        "level deliberately - this is not a GRANULARITY_MISMATCH, because a more specific "
        "term would have to pick a sign the biology does not support family-wide."
    ),
    supported_by=[Q_AT2_APOP, Q_AT2_SHP1],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        status={
            "PANTHER:PTN008518321": (
                "SUPPORTS_TRANSFER",
                "Angiotensinogen-specific IBD node, the same node that correctly seeds "
                "GO:0038166. Correctly placed; the reservation is about the term's breadth, "
                "not the node.",
            ),
            "MGI:MGI:87963": (
                "SUPPORTS_TRANSFER",
                "Mouse Agt (P11859); angiotensin II regulates apoptosis in mouse tissues in "
                "both directions depending on receptor subtype.",
            ),
            "RGD:2069": (
                "SUPPORTS_TRANSFER",
                "Rat Agt (P01015), a 1:1 orthologue whose GO record carries experimentally "
                "grounded angiotensin phenotypes (verified live in QuickGO).",
            ),
            "UniProtKB:P01019": (
                "SUPPORTS_TRANSFER",
                "Human AGT, the target itself; its GO:2001238 IDA is one of the descendant "
                "evidences behind the node. Expected, not circular.",
            ),
        },
        residue_claims_not_applicable=(
            "The reservation is about term granularity and biological centrality, not about "
            "any sequence feature of AGT."
        ),
    ),
)

# ---- IEA rows ------------------------------------------------------------

DECISIONS[5] = dict(
    summary=(
        "Correctly scoped InterPro2GO inference, and the control that shows what went wrong "
        "with the GO:0004867 IEA. The two signatures in the WITH/FROM are IPR000227 "
        "(Angiotensinogen) and IPR033834 (Angiotensinogen_serpin_dom) - angiotensinogen-"
        "specific, not family-wide - and they map to the angiotensinogen-specific process "
        "term. This is exactly what AGT does."
    ),
    action="ACCEPT",
    reason=(
        "Gene-level InterPro signatures mapped to the gene's core physiological process. The "
        "same protein matches the generic serpin signature IPR000215 as well, and that route "
        "produces the wrong molecular function - the contrast is diagnostic of where "
        "InterPro2GO fails and where it works."
    ),
    supported_by=[Q_KO_BP, Q_RESCUE_BP],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "InterPro:IPR000227": (
                "SUPPORTS_TRANSFER",
                "InterPro 'Angiotensinogen' - a signature specific to this gene, not to the "
                "serpin family, so its GO mapping cannot leak across the family.",
            ),
            "InterPro:IPR033834": (
                "SUPPORTS_TRANSFER",
                "InterPro 'Angiotensinogen_serpin_dom' - the angiotensinogen-specific serpin "
                "domain, again gene-level rather than family-level.",
            ),
        },
    ),
)

DECISIONS[6] = dict(
    summary=(
        "The InterPro route to the same false claim as the GO:0004867 IBA. The single "
        "signature is IPR000215 'Serpin_fam', which matches the whole serpin family "
        "including its many non-inhibitory members (corticosteroid-binding globulin, "
        "thyroxine-binding globulin, PEDF, ovalbumin, HSP47, and angiotensinogen). The "
        "interpro2go mapping IPR000215 -> GO:0004867 is therefore only as good as the "
        "assumption that every serpin inhibits, which is false, and AGT is one of the "
        "members where it fails."
    ),
    action="REMOVE",
    reason=(
        "A demonstrably over-broad InterPro2GO mapping applied to a member that lacks the "
        "activity. Removing it is safe on exactly the grounds the guidelines allow for IEA "
        "rows: AGT has no reactive bond, a proline-blocked hinge, MEROPS non-inhibitor "
        "classification, and a published crystal structure showing it cannot undergo the "
        "stressed-to-relaxed transition. Note that AGT's own gene-level signatures "
        "(IPR000227, IPR033834) give a correct annotation via the same pipeline."
    ),
    supported_by=[Q_NONINHIB, Q_LOST_SR, Q_SERPIN_SIM],
    prop=dict(
        root_cause="PROPAGATION_BAD",
        modes=["FUNCTIONAL_DIVERGENCE"],
        status={
            "InterPro:IPR000215": (
                "SUPPORTS_SOURCE_BUT_NOT_TARGET",
                "InterPro 'Serpin_fam' - a whole-family signature. It correctly identifies AGT "
                "as a serpin (UniProt agrees: 'Belongs to the serpin family'), but the "
                "activity its interpro2go mapping carries is not a property of every family "
                "member and is not a property of this one.",
            ),
        },
        residue_claims_not_applicable=(
            "The residue argument is made once, on the GO:0004867 IBA row; this row is the "
            "same claim reaching AGT by a different pipeline and rests on the same evidence."
        ),
    ),
)

DECISIONS[7] = dict(
    summary=(
        "Correct. Two independent automatic routes agree: the serpin family signature "
        "IPR000215 (secretion is genuinely typical of the family) and, more directly, "
        "UniProtKB-SubCell SL-0243, which is the curated 'Secreted' subcellular location on "
        "this very entry. The second is essentially a re-expression of AGT's own curated "
        "annotation rather than an inference from anything else."
    ),
    action="ACCEPT",
    reason=(
        "Correct location, and the SubCell route is grounded in AGT's own curated record. "
        "Not independent of the IBA, ISS, IDA and HDA rows for the same term, but not wrong."
    ),
    supported_by=[Q_SECRETED],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "InterPro:IPR000215": (
                "SUPPORTS_TRANSFER",
                "Serpin family signature. Over-broad for molecular function, but secretion is "
                "a real family-wide tendency and is correct for AGT.",
            ),
            "UniProtKB-SubCell:SL-0243": (
                "SUPPORTS_TRANSFER",
                "The 'Secreted' SubCell term drawn from AGT's own curated SUBCELLULAR LOCATION "
                "line, which cites PubMed:4300938, 7259779 and 7539791. Not an inference from "
                "another gene.",
            ),
        },
    ),
)

# ---- protein binding IPI rows -------------------------------------------

DECISIONS[8] = dict(
    summary=(
        "Real interaction, uninformative term. The partner is rat Agtr1 (P25095), the type-1 "
        "angiotensin II receptor - UniProt records the pair as a cross-species IntAct entry "
        "with 10 experiments. The molecule on the AGT side is the angiotensin II octapeptide, "
        "and what it does to AGTR1 is act as its agonist. 'Protein binding' says none of "
        "that, and GO curation guidance is to replace bare GO:0005515 with an informative "
        "molecular function wherever the partner is known."
    ),
    action="MODIFY",
    reason=(
        "The specific term GO:0031702 type 1 angiotensin receptor binding is available, is "
        "already used elsewhere in this gene's record for the same interaction from a "
        "different reference, and states what the bare parent hides."
    ),
    replace=[("GO:0031702", "type 1 angiotensin receptor binding")],
    supported_by=[
        ("PMID:18202720",
         "Here, we show that cell stretch leads to activation of the AT(1) receptor, which "
         "undergoes an anticlockwise rotation and a shift of transmembrane (TM) 7 into the "
         "ligand-binding pocket."),
        ("file:human/AGT/AGT-uniprot.txt", "P01019; P25095: Agtr1; Xeno; NbExp=10"),
    ],
)

DECISIONS[9] = dict(
    summary=(
        "The single most important interaction in this gene's record, recorded as bare "
        "'protein binding'. The partner is renin (P00797), and the association is not a "
        "transient enzyme-substrate encounter: the crystal structure of the human "
        "angiotensinogen-renin complex shows a 670 A^2 body-to-body interface outside the "
        "active-site cleft, with helix A of AGT lying across renin's active site and helix C "
        "and the CD-loop contacting renin's N-terminal lobe. The follow-up structures show a "
        "tail-into-mouth allosteric mechanism and demonstrate by mutagenesis and kinetics "
        "that specificity is set by AGT residues and glycans outside that cleft."
    ),
    action="MODIFY",
    reason=(
        "GO:0002020 protease binding is the informative molecular function this interaction "
        "supports and is the only term in AGT's whole record that describes what the "
        "full-length precursor itself does. The interface is extensive, structurally "
        "characterised, and functionally load-bearing rather than incidental to catalysis."
    ),
    replace=[("GO:0002020", "protease binding")],
    supported_by=[Q_670, Q_TAIL,
                  ("PMID:30563843",
                   "Mutagenesis and kinetic analyses confirmed that renin-mediated production "
                   "of angiotensin I is controlled by interactions of amino acid residues and "
                   "glycan components outside renin's active-site cleft.")],
)

DECISIONS[10] = dict(
    summary=(
        "A cross-phylum enzyme-substrate co-crystal reported as a protein-protein "
        "interaction. The partner Q10714 is AnCE, the Drosophila melanogaster "
        "angiotensin-converting enzyme homologue, and UniProt flags the pair 'Xeno'. What "
        "was actually crystallised is the insect enzyme with the mammalian angiotensin I "
        "decapeptide (and bradykinin, and a snake-venom peptide) sitting in its active site. "
        "That is a peptide in a catalytic cleft, not an interaction of human angiotensinogen "
        "with a human partner."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Structurally real but of no interpretive value for human AGT: a 10-residue cleavage "
        "product of AGT bound in the active site of a Drosophila enzyme, used as a structural "
        "model for human ACE. Human ACE processing of angiotensin I is already represented "
        "properly in this record by the Reactome reactions. Kept rather than removed because "
        "the structure is genuine."
    ),
    supported_by=[
        ("PMID:23082758",
         "Here, we report the structures of an ACE homologue from Drosophila melanogaster "
         "(AnCE; a proven structural model for the more complex human ACE) co-crystallized "
         "with mammalian peptide substrates (bradykinin, Thr(6) -bradykinin, angiotensin I "
         "and a snake venom peptide inhibitor, bradykinin-potentiating peptide-b)."),
        ("file:human/AGT/AGT-uniprot.txt", "P01019; Q10714: Ance; Xeno; NbExp=2"),
    ],
)

DECISIONS[71] = dict(
    summary=(
        "Could not be verified against the cited paper. The row asserts that AGT binds the "
        "hepatitis C virus F/ARFP protein (P0C045), from a yeast two-hybrid screen of a liver "
        "cDNA library, and was assigned by AgBase. The cached full text of that paper is "
        "complete - abstract, introduction, results and the whole discussion, in which every "
        "hit is discussed in turn - and the word 'angiotensinogen' does not appear anywhere "
        "in it. The paper enumerates all 36 positive colonies by identity and angiotensinogen "
        "is not among them; the serpin it does report is C1 inhibitor. Independently, the "
        "assay is a poor fit: AGT is a secreted, signal-peptide-cleaved, disulfide-bonded, "
        "four-site N-glycosylated plasma protein and yeast two-hybrid reconstitutes a "
        "transcription factor in the yeast nucleus, while UniProt places the F protein in "
        "host cytoplasm."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Bare 'protein binding' with no functional follow-up, a compartment mismatch, and a "
        "citation in which I could not locate the claim despite having the complete text. "
        "Not removed, because a table that did not survive text extraction cannot be excluded "
        "and I will not overrule an experimental annotation on a cache I cannot fully "
        "guarantee. Raised as a question for the assigning group instead."
    ),
    supported_by=[
        ("PMID:16237761",
         "Thirty-six colonies were selected and sequenced. Among them, 11 colonies were "
         "zymogen granule protein, 5 colonies were zinc finger protein, 4 colonies were "
         "zinc-alpha-2-glycoprotein, 1 colony was sialyltransferase, 1 colony was complement "
         "control protein factor I, 1 colony was vitronectin, and 2 colonies were new genes "
         "with unknown function."),
        Q_SECRETED,
    ],
)

# ---- experimental rows on the released peptides --------------------------

_ANG_SIG = (
    "Angiotensin-activated signalling is the core biological process of this gene: "
    "angiotensin II is produced from angiotensinogen and from nothing else, and this term "
    "names the pathway it initiates. "
)

DECISIONS[48] = dict(
    summary=(
        _ANG_SIG + "Here it is evidenced in primary human monocyte-macrophages, where added "
        "angiotensin II raises ACAT1 through AGTR1 and the effect is abolished by AT1 "
        "antagonists but not by an AT2 antagonist - a clean receptor-specific demonstration "
        "of the pathway."
    ),
    action="ACCEPT",
    reason="Core process, correctly evidenced with receptor-subtype controls.",
    supported_by=[
        ("PMID:18971559",
         "Two-fold increases in ACAT1 protein expression and ACAT activity with Ang II "
         "treatment were completely inhibited by AT(1) receptor antagonists"),
        ("PMID:18971559",
         "Application of an Ang II type 1 (AT(1)) receptor agonist (L162313), but not an Ang "
         "II type 2 (AT(2)) receptor agonist (CGP42112A), mimicked the effects of Ang II "
         "treatment in inducing ACAT1 protein expression."),
    ],
)

DECISIONS[49] = dict(
    summary=(
        "A downstream cellular response to added angiotensin II, correctly qualified. "
        "Angiotensin II raises ACAT1, which esterifies free cholesterol for storage in lipid "
        "droplets. AGT is not itself a participant in cholesterol metabolism; it is the source "
        "of a hormone whose receptor engagement changes the expression of a cholesterol "
        "enzyme. The 'acts_upstream_of' qualifier is what makes this defensible, and it is "
        "the qualifier several sibling rows from the same class of experiment should have "
        "used but did not."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real and reproducible, but two steps removed from anything angiotensinogen does: "
        "hormone -> receptor -> transcriptional change in an unrelated enzyme. Peripheral to "
        "the gene's function and correctly marked as upstream rather than participatory."
    ),
    supported_by=[
        ("PMID:18971559",
         "Ang II significantly increased ACAT1 protein expression in a time- or "
         "concentration-dependent manner."),
    ],
)

DECISIONS[67] = dict(
    summary=(
        "Same experiment, one step further downstream: raised ACAT1 activity drives "
        "cholesteryl-ester accumulation and foam-cell formation in cultured "
        "monocyte-macrophages loaded with acetylated LDL. This is atherosclerosis cell "
        "biology driven by an added peptide hormone, not a function of the precursor."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Genuine downstream physiology of angiotensin II in macrophages and worth keeping, "
        "but well outside the gene's core role. Note the qualifier here is 'involved_in' "
        "while the cholesterol row from the same paper and the same experiment uses "
        "'acts_upstream_of' - the two should agree."
    ),
    supported_by=[
        ("PMID:18971559",
         "Ang II significantly increased ACAT1 protein expression in a time- or "
         "concentration-dependent manner."),
    ],
)

DECISIONS[85] = dict(
    summary=(
        "The term is right but this reference does not establish it. PMID:18971559 is a "
        "study in which synthetic angiotensin II was added to cultured human "
        "monocyte-macrophages and ACAT1 expression measured; it contains no localisation "
        "experiment on angiotensinogen. AGT's extracellular location is abundantly evidenced "
        "elsewhere in this record - by direct plasma protein chemistry (PMID:4300938), by "
        "four independent HDA proteomics datasets, by the curated UniProt SUBCELLULAR "
        "LOCATION, and by the IBA and ISS rows."
    ),
    action="ACCEPT",
    reason=(
        "The term is correct and is core for this gene, so the action follows the biology "
        "rather than the citation: extracellular localisation is accepted here as it is on "
        "every other row for this term. The defect is in the evidence attribution alone - "
        "this reference contains no localisation experiment - and it is recorded in the "
        "reference_review for PMID:18971559 rather than by downgrading a correct term."
    ),
    supported_by=[Q_SECRETED],
)

DECISIONS[50] = dict(
    summary=(
        "Real but indirect, and from a paper about a different gene. The study transfects "
        "ACE2 into an endothelial cell line and asks what that does to insulin signalling; "
        "the AGT-side observation is that angiotensin II and angiotensin IV induce macrophage "
        "migration inhibitory factor, which ACE2 transfer then suppresses. So the evidence "
        "for AGT is 'added peptide raises a cytokine in a cell line', which is genuine but "
        "sits at the far end of the hormone's action."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Angiotensin II is genuinely pro-inflammatory and cytokine-inducing, so the biology is "
        "sound, but this is a cellular response to the hormone rather than a function of "
        "angiotensinogen, and the citation's subject is ACE2."
    ),
    supported_by=[
        ("PMID:17906677",
         "Gene transfer of ACE2 suppressed the expression of p22phox and MIF induced by "
         "angiotensin (Ang) II and Ang IV, accompanied by a decreased level of malondialdehyde "
         "in cells."),
    ],
)

DECISIONS[51] = dict(
    summary=(
        "The inflammatory arm of the same experiment. Angiotensin II induces MIF, a "
        "pro-inflammatory cytokine, in the EAhy926 endothelial line; ACE2 over-expression, "
        "which degrades angiotensin II, reverses it. Duplicated by a TAS row for the same "
        "term from the PMID:17159080 editorial."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "A well-established consequence of angiotensin II signalling, but a response of the "
        "target cell rather than an activity of angiotensinogen, and evidenced here only in "
        "an immortalised endothelial line."
    ),
    supported_by=[
        ("PMID:17906677",
         "Gene transfer of ACE2 suppressed the expression of p22phox and MIF induced by "
         "angiotensin (Ang) II and Ang IV, accompanied by a decreased level of malondialdehyde "
         "in cells."),
    ],
)

DECISIONS[52] = dict(
    summary=(
        "The oxidative arm of the same experiment: angiotensin II induces p22phox, an NADPH "
        "oxidase subunit, raising malondialdehyde, and ACE2 transfer reverses it. Angiotensin "
        "II-driven NADPH oxidase activation is one of the best-replicated effects in vascular "
        "biology, so the direction is not in doubt; the reservation is the same as for the "
        "sibling rows."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real downstream redox signalling initiated by the hormone, not a molecular or "
        "cellular role of the precursor protein."
    ),
    supported_by=[
        ("PMID:17906677",
         "In addition, Ang II diminished insulin-stimulated phosphorylation of Akt (at "
         "Ser(473)) and eNOS (at Ser(1177)) and NO generation, effects which were reversed by "
         "ACE2 gene transfer and anti-MIF treatment in endothelial cells."),
    ],
)

DECISIONS[53] = dict(
    summary=(
        "Contradicted by the paper it cites. GO:0008083 is defined as 'The function that "
        "stimulates a cell to grow or proliferate'. PMID:10406457 is an AT2-receptor "
        "intracellular-loop mutagenesis study in PC12 cells, and everything it measures runs "
        "the other way: AT2-mediated apoptosis, inhibition of ERK, and SHP-1 activation. It "
        "contains no growth or proliferation assay. A second paper cited elsewhere in this "
        "same record independently reports that angiotensin II does not increase "
        "proliferation in its system."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Angiotensin II is genuinely mitogenic for vascular smooth muscle through AGTR1, so "
        "the term is not absurd for the gene and I am not removing it. But the cited evidence "
        "is an apoptosis-and-ERK-inhibition study, which cannot support a growth factor "
        "activity, and no growth-factor assay on AGT or its peptides is cited anywhere in the "
        "record. GO's own comment on this term also suggests considering GO:0048018 receptor "
        "agonist activity, which would fit angiotensin II far better."
    ),
    supported_by=[Q_AT2_APOP, Q_AT2_SHP1, Q_HUVEC_NOPROLIF],
)

DECISIONS[80] = dict(
    summary=(
        "Supported, and the specific term the growth-factor row should have been. The same "
        "PC12 study maps AT2 residues Lys240, Asn242 and Ser243 as required for AT2-induced "
        "apoptosis and shows SHP-1 is the proximal effector. Angiotensin II acting through "
        "AGTR2 is genuinely pro-apoptotic."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real peptide pharmacology, but demonstrated in a transfected PC12 neuroendocrine "
        "line with mutant receptors, and peripheral to the gene's cardiovascular core."
    ),
    supported_by=[Q_AT2_APOP, Q_AT2_SHP1],
)

DECISIONS[109] = dict(
    summary=(
        "Plausible and consistent with the cited data, in a specialised context. PC12 cells "
        "are the classic NGF/TrkA model, and this study shows AT2 engagement activates SHP-1 "
        "and inhibits ERK - the pathway TrkA signals through. So angiotensin II acting on AT2 "
        "does dampen neurotrophin receptor signalling in these cells."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "A genuine but narrow cross-talk effect, shown in one transfected cell line, far from "
        "the gene's core cardiovascular role."
    ),
    supported_by=[Q_AT2_SHP1],
)

DECISIONS[105] = dict(
    summary=(
        "Term plausible for the gene, citation does not support it. PMID:10406457 is an "
        "AT2-receptor i3-loop deletion study in PC12 cells measuring apoptosis, ERK and "
        "SHP-1. It contains no vessel, no vascular smooth muscle and no remodelling "
        "measurement. Angiotensin II certainly does drive vascular remodelling, but not in "
        "this paper."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "A TAS whose traceable source contains nothing about blood vessels. Retained rather "
        "than removed because the biology is real and well documented elsewhere, but this row "
        "carries no usable evidence."
    ),
    supported_by=[Q_AT2_APOP],
)

DECISIONS[106] = dict(
    summary=(
        "Correct term, wrong citation. Maintenance of blood vessel diameter by the "
        "renin-angiotensin system is exactly what angiotensinogen exists for, and the same "
        "term is independently annotated by IDA from PMID:1567413. This particular TAS points "
        "at the PC12 AT2 apoptosis paper, which measures nothing of the kind."
    ),
    action="ACCEPT",
    reason=(
        "Accepted on the biology: this is a core function of angiotensinogen and it is "
        "independently evidenced on this gene by IDA. Core-versus-non-core is a judgement "
        "about the term, not about the citation, so a weak citation is not a reason to "
        "downgrade a correct core term. The citation problem - a PC12-cell AT2 apoptosis "
        "study standing behind a vascular-diameter term - is recorded in the reference_review "
        "for PMID:10406457."
    ),
    supported_by=[Q_AT1_CLONE],
)

DECISIONS[107] = dict(
    summary=(
        "True but uninformative parent. Angiotensin receptors are GPCRs, so any angiotensin "
        "signalling is GPCR signalling - but AGT already carries the specific child "
        "GO:0038166 angiotensin-activated signaling pathway five times over, which says the "
        "same thing and names the ligand."
    ),
    action="MODIFY",
    reason=(
        "Too general. The specific term is available, is already in use on this gene, and is "
        "what the evidence actually shows; the bare parent adds nothing and dilutes the "
        "record."
    ),
    replace=[("GO:0038166", "angiotensin-activated signaling pathway")],
    supported_by=[Q_AT2_APOP],
)

DECISIONS[108] = dict(
    summary=(
        "Correct and informative. Angiotensin II binds AGTR2 (P50052); UniProt encodes the "
        "interaction precisely, on the angiotensin chain rather than the whole precursor "
        "(PRO_0000032459 with AGTR2). This and the AGTR1 row are the two molecular functions "
        "in the record that name a real, specific partner."
    ),
    action="ACCEPT",
    reason=(
        "Core molecular function of the gene product's principal peptide, with a named "
        "partner and a specific term."
    ),
    supported_by=[Q_AT2_APOP,
                  ("file:human/AGT/AGT-uniprot.txt",
                   "PRO_0000032459; P50052: AGTR2; NbExp=2")],
)

DECISIONS[111] = dict(
    summary=(
        "Correct and informative, the AGTR1 counterpart. The cited paper clones the human "
        "AT1a receptor and shows high-affinity angiotensin II binding coupled to inositol "
        "phosphate turnover. UniProt again attaches the interaction to the angiotensin-2 "
        "chain (PRO_0000032458 with AGTR1) rather than to full-length angiotensinogen, which "
        "is the correct reading: the binding entity is the octapeptide."
    ),
    action="ACCEPT",
    reason=(
        "Core molecular function. AGTR1 is the receptor through which essentially all of the "
        "pressor, aldosterone-releasing and proliferative actions of the pathway run."
    ),
    supported_by=[Q_AT1A,
                  ("file:human/AGT/AGT-uniprot.txt",
                   "PRO_0000032458; P30556: AGTR1; NbExp=2")],
)

# ---- hormone activity, the angiotensin-signalling cluster, ISS, IC --------

DECISIONS[61] = dict(
    summary=(
        "Correct, with a caveat about what the annotation unit means. GO:0005179 requires a "
        "substance formed in one tissue and carried to another where it has a specific "
        "regulatory action through a receptor. That describes angiotensin II exactly, and "
        "does not describe the 476-residue precursor, which is inert until renin cleaves it. "
        "But GOA's annotation unit is the UniProt accession, angiotensin II has no gene of "
        "its own, and UniProt itself carries the peptide functions on P01019 as "
        "'FUNCTION: [Angiotensin-2]' and as PRO_ chain-level interactions. So the hormone "
        "activity belongs here. This GOA row is exactly duplicated (it appears twice with "
        "identical term, evidence, reference and qualifier), which is why 114 GOA rows "
        "reconcile to 113 review entries."
    ),
    action="ACCEPT",
    reason=(
        "Core molecular function of the gene product, understood as including its cleavage "
        "products - the convention GOA and UniProt both follow. The evidence is thin for an "
        "IDA (the cited paper is a receptor-cloning study whose angiotensin II is synthetic "
        "peptide), but the claim is correct and is independently supported by the ISS from "
        "rat Agt and by the IC from receptor binding."
    ),
    supported_by=[Q_AT1_CLONE, Q_AT1_CA],
)

DECISIONS[62] = dict(
    summary=(
        _ANG_SIG + "The cited receptor-cloning paper shows the human AT1 receptor coupling to "
        "calcium mobilisation on angiotensin II binding, which is the pathway this term names."
    ),
    action="ACCEPT",
    reason="Core process with direct receptor-coupling evidence.",
    supported_by=[Q_AT1_CA, Q_AT1_CLONE],
)

DECISIONS[64] = dict(
    summary=(
        "The gene's defining physiological role, stated at the right level of specificity. "
        "This is a renin-angiotensin-specific term rather than a generic vascular one, and "
        "the human genetics is unambiguous: loss of angiotensinogen in mice abolishes plasma "
        "angiotensin I and drops systolic pressure by a third, and re-expression restores it."
    ),
    action="ACCEPT",
    reason=(
        "Core biological process. Among the strongest claims in the whole record and one of "
        "the few where perturbation evidence exists in both directions."
    ),
    supported_by=[Q_KO_BP, Q_RESCUE_BP, Q_AT1_CLONE],
)

DECISIONS[54] = dict(
    summary=(
        _ANG_SIG + "Evidenced here in mouse embryonic renal cell lines, where added "
        "angiotensin II upregulates Pax-2 through AGTR2 and the effect is blocked by the AT2 "
        "antagonist PD123319 but not by the AT1 antagonist losartan. The receptor-subtype "
        "pharmacology is clean. The IMP code is loose - the perturbations are receptor "
        "antagonists and kinase inhibitors, not mutations in AGT - but the pathway claim holds."
    ),
    action="ACCEPT",
    reason=(
        "Core process, correctly identified, with receptor-specific antagonist controls. The "
        "evidence-code choice is questionable but the annotation is not."
    ),
    supported_by=[
        ("PMID:15153556",
         "Angiotensin II (AngII) upregulated Pax-2 protein and Pax-2 mRNA expression via the "
         "AngII type 2 (AT(2)) receptor in MK4 but not in MK3 cells."),
    ],
)

DECISIONS[59] = dict(
    summary=(
        _ANG_SIG + "Here in primary human umbilical vein endothelial cells, where angiotensin "
        "II drives FAK and paxillin phosphorylation and migration through PI3K, Src and EGFR "
        "transactivation."
    ),
    action="ACCEPT",
    reason="Core process, in a primary human cell type, with pathway inhibitor dissection.",
    supported_by=[Q_HUVEC_FAK],
)

DECISIONS[60] = dict(
    summary=(
        "A downstream signalling response to added angiotensin II. Wortmannin and LY294002 "
        "attenuate the FAK/paxillin phosphorylation, placing PI3K in the pathway. This is a "
        "property of the AGTR1-bearing endothelial cell, not of angiotensinogen."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real and well-controlled, but a generic intracellular signalling module engaged "
        "downstream of the receptor. Every GPCR agonist that transactivates a receptor "
        "tyrosine kinase would earn this term."
    ),
    supported_by=[
        ("PMID:15652490",
         "The effect of Ang II on FAK and paxillin phosphorylation was markedly attenuated in "
         "cells pretreated with wortmannin and LY294002, indicating that phosphoinositide "
         "3-kinase (PI3K) plays an important role in regulating FAK activation."),
    ],
)

DECISIONS[92] = dict(
    summary=(
        "EGFR transactivation downstream of AGTR1 - a genuine and much-replicated "
        "phenomenon, demonstrated here by AG1478 blocking angiotensin II-induced FAK and "
        "paxillin phosphorylation in HUVEC."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real receptor cross-talk, but a property of the responding cell's signalling "
        "architecture rather than a function of the hormone's precursor."
    ),
    supported_by=[
        ("PMID:15652490",
         "Furthermore, FAK and paxillin phosphorylation was markedly blocked after treatment "
         "of HUVEC with AG1478, a selective inhibitor of epidermal growth factor receptor "
         "(EGFR) phosphorylation."),
    ],
)

DECISIONS[89] = dict(
    summary=(
        "Directly measured in the cited paper: angiotensin II increases HUVEC migration in a "
        "time- and dose-dependent way, through PI3K, Src and EGFR. The same sentence records "
        "that proliferation was unaffected, which is a useful negative given that the record "
        "elsewhere claims growth factor activity."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "A real, directly measured cellular response to the hormone in primary human "
        "endothelial cells, but downstream physiology rather than a core role of the gene."
    ),
    supported_by=[Q_HUVEC_NOPROLIF],
)

DECISIONS[82] = dict(
    summary=(
        "A generic term that casts a hormone as a transcriptional regulator. What the paper "
        "shows is that added angiotensin II raises Pax-2 mRNA and protein in mouse MK4 cells "
        "through AGTR2 and JAK2/STAT signalling. Angiotensinogen does not regulate "
        "transcription; it is the source of a ligand whose receptor engages a signalling "
        "cascade that ends in changed transcription. The record already carries GO:0038166, "
        "which states that chain correctly and is annotated from this very paper."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "'Positive regulation of DNA-templated transcription' is the terminal readout of "
        "almost any signalling experiment and is uninformative here. It also mis-assigns the "
        "role: the substrate that supplies a receptor agonist is not the agent of the "
        "transcriptional change. GO:0038166 from the same experiment carries the real content."
    ),
    supported_by=[
        ("PMID:15153556",
         "Moreover, embryonic kidney explants in culture confirmed that AngII upregulates "
         "Pax-2 gene expression via the AT(2) receptor."),
    ],
)

DECISIONS[83] = dict(
    summary=(
        "The same generic transcription term from the companion study, which uses AT2-receptor "
        "knockout mice and shows that angiotensin II raises Pax-2 and N-myc in wild-type "
        "embryonic kidney but not in AT2R-null kidney. Good genetics for the receptor; still "
        "the wrong role assignment for angiotensinogen."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Same objection as the sibling row: an uninformative terminal-readout term that "
        "represents the hormone's precursor as a transcriptional regulator. The specific and "
        "defensible content of this experiment is the ureteric-bud branching row."
    ),
    supported_by=[
        ("PMID:18607644",
         "In ex vivo studies, Ang II stimulated Pax-2 and N-myc mRNA expression in embryonic "
         "kidneys of wild-type mice, but this stimulatory effect was absent in embryonic "
         "kidneys of AT(2)R KO mice."),
    ],
)

DECISIONS[84] = dict(
    summary=(
        "Specific, developmentally meaningful, and properly controlled by receptor genetics: "
        "AT2R-null embryonic kidneys have smaller glomeruli and reduced Pax-2 and N-myc, and "
        "do not respond to angiotensin II. This is the defensible annotation from the paper, "
        "and it aligns with the human loss-of-function phenotype (renal tubular dysgenesis)."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "A real developmental role of angiotensin signalling in nephrogenesis, but downstream "
        "developmental physiology rather than the gene's core function, and demonstrated in "
        "mouse explants."
    ),
    supported_by=[
        ("PMID:18607644",
         "Glomerular size was significantly smaller, and Pax-2 and N-myc expression "
         "down-regulated, in kidneys of AT(2)R KO mice compared with those of wild-type mice."),
    ],
)

DECISIONS[110] = dict(
    summary=(
        "The strongest human loss-of-function evidence in the record. Biallelic mutations in "
        "AGT - alongside REN, ACE and AGTR1 - cause autosomal recessive renal tubular "
        "dysgenesis, with absent proximal tubules, fetal anuria and perinatal death. The "
        "authors' own mechanism is haemodynamic rather than a direct developmental "
        "instruction: chronic low perfusion pressure of the fetal kidney as a consequence of "
        "an inactive renin-angiotensin system."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Unambiguous human genetics, kept without hesitation. Marked non-core rather than "
        "core because the paper's own reading makes kidney development a downstream "
        "consequence of losing the pathway's haemodynamic output, not a separate "
        "developmental activity of angiotensinogen. The core role that produces it is already "
        "annotated as GO:0003081 and GO:0002034."
    ),
    supported_by=[Q_RTD, Q_RTD_MECH],
)

DECISIONS[63] = dict(
    summary=(
        "Sequence-similarity transfer from mouse Agt (P11859), a true 1:1 orthologue, not a "
        "paralogue. I confirmed against QuickGO that the donor still carries this exact term "
        "with experimental evidence (IMP, PMID:34615811), so the transfer is not stale and the "
        "source is not itself an inference."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Defensible orthologue transfer, but epithelial-mesenchymal transition is a "
        "context-specific fibrotic/oncogenic response to angiotensin signalling rather than a "
        "core function of the gene."
    ),
    supported_by=[Q_KO],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        status={
            "UniProtKB:P11859": (
                "SUPPORTS_TRANSFER",
                "Mouse Agt, the 1:1 orthologue. Verified live in QuickGO to still hold "
                "GO:0010718 by IMP from PMID:34615811, so this is an experimentally grounded "
                "donor rather than a chain of inferences.",
            ),
        },
        residue_claims_not_applicable=(
            "Whole-protein orthologue transfer between angiotensinogens; no residue-level "
            "argument is involved."
        ),
    ),
)

_ISS_RAT = (
    "Sequence-similarity transfer from rat Agt (P01015), a 1:1 orthologue. I confirmed "
    "against QuickGO that the donor still holds this term with experimental evidence, so "
    "the source is neither stale nor itself inferred. "
)

DECISIONS[87] = dict(
    summary=_ISS_RAT + "Donor evidence: IDA from PMID:8348686. Corroborates the two direct "
                       "IDA rows and the IC row for the same term.",
    action="ACCEPT",
    reason=(
        "Core molecular function, independently supported on the orthologue by direct assay. "
        "Together with the human IDA rows this is the best-evidenced molecular function in "
        "the record."
    ),
    supported_by=[Q_AT1_CLONE],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "UniProtKB:P01015": (
                "SUPPORTS_TRANSFER",
                "Rat Agt, 1:1 orthologue; holds GO:0005179 by IDA from PMID:8348686 in the "
                "current QuickGO record.",
            ),
        },
    ),
)

DECISIONS[88] = dict(
    summary=_ISS_RAT + "Donor evidence: two independent IDA rows (PMID:12242043, "
                       "PMID:8252633) plus IBA and ISO. Rat angiotensinogen is, like the "
                       "human protein, a liver-secreted plasma protein.",
    action="ACCEPT",
    reason="Correct location, well grounded on the orthologue and directly evidenced on the "
           "human protein as well.",
    supported_by=[Q_SECRETED, Q_LIVER],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "UniProtKB:P01015": (
                "SUPPORTS_TRANSFER",
                "Rat Agt; holds GO:0005576 by IDA from PMID:12242043 and PMID:8252633 in the "
                "current QuickGO record.",
            ),
        },
    ),
)

DECISIONS[90] = dict(
    summary=_ISS_RAT + "Donor evidence: IDA from PMID:8348686. Angiotensin II-driven cardiac "
                       "hypertrophy is one of the best-replicated effects of the pathway and "
                       "the dTGR rows in this same record show the same biology in vivo.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real and well replicated, but a pathological/adaptive tissue response to sustained "
        "angiotensin II rather than a core function of angiotensinogen."
    ),
    supported_by=[Q_DTGR],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        status={
            "UniProtKB:P01015": (
                "SUPPORTS_TRANSFER",
                "Rat Agt; holds GO:0010613 by IDA from PMID:8348686 in the current QuickGO "
                "record. Experimentally grounded, not an inference chain.",
            ),
        },
    ),
)

DECISIONS[91] = dict(
    summary=_ISS_RAT + "Donor evidence: IMP from PMID:8252633. A narrow, "
                       "physiology-specific term about muscle adaptation to activity.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Defensible orthologue transfer of a specific rat physiological observation, but "
        "peripheral to the gene's function and not independently established in human."
    ),
    supported_by=[Q_LIVER],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        status={
            "UniProtKB:P01015": (
                "SUPPORTS_TRANSFER",
                "Rat Agt; holds GO:0014873 by IMP from PMID:8252633 in the current QuickGO "
                "record.",
            ),
        },
        residue_claims_not_applicable=(
            "Orthologue-level physiological transfer; no residue argument applies."
        ),
    ),
)

DECISIONS[93] = dict(
    summary=_ISS_RAT + "Donor evidence: IDA from PMID:8348686, the same rat study behind the "
                       "hormone-activity and cardiac-hypertrophy transfers. Angiotensin II is "
                       "a well-documented fibroblast mitogen.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real proliferative effect of the hormone on fibroblasts, and consistent with the "
        "fibrosis seen in the dTGR model, but a downstream tissue response rather than a core "
        "function. Worth noting that three of the six ISS rows trace to this single donor "
        "paper, so they are not three independent findings."
    ),
    supported_by=[Q_DTGR],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        status={
            "UniProtKB:P01015": (
                "SUPPORTS_TRANSFER",
                "Rat Agt; holds GO:0048146 by IDA from PMID:8348686 in the current QuickGO "
                "record. Same donor study as the GO:0005179 and GO:0010613 transfers.",
            ),
        },
    ),
)

_IC_NOTE = (
    "Curator inference from GO:0031702 type 1 angiotensin receptor binding, which AGT holds "
    "by IPI from this same reference. "
)

DECISIONS[98] = dict(
    summary=_IC_NOTE + "The inference is sound - a molecule that binds a cell-surface "
                       "angiotensin receptor with high affinity and triggers inositol "
                       "phosphate turnover is acting as a hormone. It is however entirely "
                       "redundant: AGT already holds GO:0005179 twice by IDA and once by ISS "
                       "from rat, all of which are stronger.",
    action="ACCEPT",
    reason=(
        "Accepted: hormone activity is a core molecular function of this gene product and the "
        "inference behind this row is valid. Its redundancy is a property of the evidence "
        "route rather than of the term, so it is recorded in propagation_review as "
        "EVIDENCE_CIRCULAR_OR_REDUNDANT instead of by giving a core term a non-core action."
    ),
    supported_by=[Q_AT1A],
    prop=dict(
        root_cause="EVIDENCE_CIRCULAR_OR_REDUNDANT",
        status={
            "GO:0031702": (
                "CIRCULAR_OR_REDUNDANT",
                "The IC is drawn from another GO term on the same gene from the same "
                "reference. The inference itself is sound; it simply restates, at lower "
                "evidential strength, a conclusion the target already holds by IDA and ISS.",
            ),
        },
        residue_claims_not_applicable=(
            "A term-to-term curator inference; nothing residue-level is at stake."
        ),
    ),
)

DECISIONS[99] = dict(
    summary=_IC_NOTE + "Equally sound and equally redundant: binding a cell-surface receptor "
                       "implies being extracellular. The record already carries GO:0005576 "
                       "more than thirty times, including by direct assay, four HDA proteomics "
                       "datasets, IBA, ISS and the curated UniProt location.",
    action="ACCEPT",
    reason=(
        "Accepted: the localisation is correct and core, and the inference is sound. As with "
        "the companion hormone-activity IC row, the redundancy is a property of the evidence "
        "route and is recorded in propagation_review, not in the action."
    ),
    supported_by=[Q_SECRETED],
    prop=dict(
        root_cause="EVIDENCE_CIRCULAR_OR_REDUNDANT",
        status={
            "GO:0031702": (
                "CIRCULAR_OR_REDUNDANT",
                "Same-gene, same-reference term-to-term inference. Valid reasoning, but the "
                "target already has direct experimental and curated evidence for this "
                "location.",
            ),
        },
    ),
)

# ---- dTGR double-transgenic IGI rows -------------------------------------

_DTGR = (
    "From the dTGR model: rats carrying BOTH the human renin and the human angiotensinogen "
    "transgenes. Human renin cleaves human angiotensinogen efficiently and rat "
    "angiotensinogen poorly, so the phenotype requires the two transgenes together - which "
    "is precisely what IGI with UniProtKB:P00797 is for, and an unusually well-justified "
    "use of the code. "
)

DECISIONS[73] = dict(
    summary=_DTGR + "Blood pressure rises progressively in dTGR alongside cardiac "
                    "hypertrophy, and losartan reverses the whole syndrome, tying it to "
                    "AGTR1. This is the gene's central physiological output measured in vivo "
                    "with the human genes.",
    action="ACCEPT",
    reason=(
        "Core biological process, demonstrated in vivo with the human gene products and with "
        "receptor-blockade rescue. One of the best-supported rows in the record."
    ),
    supported_by=[Q_DTGR, Q_KO_BP],
    prop=dict(
        root_cause="NO_FAILURE_CORE",
        status={
            "UniProtKB:P00797": (
                "SUPPORTS_TRANSFER",
                "Human renin, the obligate genetic partner in the dTGR model. Correct IGI "
                "partner: neither transgene produces the phenotype alone, because human renin "
                "is species-selective for human angiotensinogen.",
            ),
        },
    ),
)

DECISIONS[72] = dict(
    summary=_DTGR + "Ventricular tachycardia was inducible in 88% of untreated dTGR versus "
                    "33% of losartan-treated dTGR and none of the controls, with prolonged "
                    "and inhomogeneous depolarisation and repolarisation on cardiac magnetic "
                    "field mapping.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "A genuine in vivo consequence of sustained angiotensin II exposure, but arrhythmic "
        "remodelling is downstream target-organ damage rather than a core function of "
        "angiotensinogen."
    ),
    supported_by=[Q_DTGR,
                  ("PMID:17416596",
                   "Untreated dTGR show electrical remodeling and probably die from VT.")],
    prop=dict(
        root_cause="NO_FAILURE_NON_CORE",
        status={
            "UniProtKB:P00797": (
                "SUPPORTS_TRANSFER",
                "Human renin; required alongside the human AGT transgene to generate the "
                "angiotensin II exposure that produces the electrical remodelling.",
            ),
        },
    ),
)

DECISIONS[74] = dict(
    summary=_DTGR + "dTGR show increased perivascular and interstitial fibrosis and raised "
                    "connective tissue growth factor from week 5 onwards, progressing with "
                    "time and ameliorated by losartan. The term used is the neutral parent, "
                    "but the paper determines the direction.",
    action="MODIFY",
    reason=(
        "The sign is determined by the data - matrix accumulation increases - so the neutral "
        "parent understates what was shown. GO:1901203 positive regulation of extracellular "
        "matrix assembly is the accurate term and is already used elsewhere in this record "
        "for the same direction of effect."
    ),
    replace=[("GO:1901203", "positive regulation of extracellular matrix assembly")],
    supported_by=[
        ("PMID:17416596",
         "Already by wk 5, untreated dTGR showed increased perivascular and interstitial "
         "fibrosis, connective tissue growth factor expression, and monocyte infiltration "
         "compared with SD rats, differences that progressed through time."),
    ],
    prop=dict(
        root_cause="TERM_SCOPING_PROBLEM",
        modes=["GRANULARITY_MISMATCH"],
        status={
            "UniProtKB:P00797": (
                "SUPPORTS_TRANSFER",
                "Human renin; correct IGI partner. The problem is the term's granularity, not "
                "the genetic interaction.",
            ),
        },
        residue_claims_not_applicable=(
            "A term-granularity issue on an in vivo phenotype; no residue-level claim is "
            "involved."
        ),
    ),
)

DECISIONS[75] = dict(
    summary=(
        _DTGR + "This row has the sign backwards. GOA asserts POSITIVE regulation of gap "
        "junction assembly, but what the paper measured is that left-ventricular connexin 43 "
        "- the ventricular gap-junction protein - was significantly REDUCED in dTGR relative "
        "to both losartan-treated dTGR and normal controls. More angiotensinogen-derived "
        "angiotensin II means less connexin 43, and that gap-junction loss is part of the "
        "electrical remodelling that makes these animals arrhythmic."
    ),
    action="MODIFY",
    reason=(
        "Regulatory sign inversion, verifiable against the abstract of the cited paper. The "
        "correct term is GO:1903597 negative regulation of gap junction assembly. The genetic "
        "interaction and the reference are both right; only the direction is wrong."
    ),
    replace=[("GO:1903597", "negative regulation of gap junction assembly")],
    supported_by=[Q_CX43, Q_DTGR],
    prop=dict(
        root_cause="TERM_SCOPING_PROBLEM",
        modes=["REGULATORY_SIGN_INVERSION"],
        status={
            "UniProtKB:P00797": (
                "SUPPORTS_TRANSFER",
                "Human renin; the IGI partner is correct and the model is the right one. The "
                "defect is entirely in the direction of the term chosen from it.",
            ),
        },
        residue_claims_not_applicable=(
            "A sign error in term selection from an in vivo transcript measurement; no "
            "sequence feature is at issue."
        ),
    ),
)

# ---- rows from the PMID:17159080 editorial -------------------------------

_EDITORIAL = (
    "Sourced from PMID:17159080, which PubMed types as Comment / Editorial / Review. It is a "
    "two-page commentary on another paper and the cached record contains no abstract text at "
    "all - only the citation line. It is the sole source for eleven GOA rows on this gene, "
    "four of them coded TAS. "
)

for _row, _term, _act, _extra, _reason in [
    (95, "regulation of blood volume by renin-angiotensin", "ACCEPT",
     "The term is renin-angiotensin-specific and is straightforwardly correct: angiotensin "
     "II raises blood volume through aldosterone-driven sodium retention, vasopressin release "
     "and thirst.",
     "Core physiology of the pathway, accepted on the biology. The citation is weak and is "
     "flagged in reference_review, but the claim itself is not in doubt and is corroborated "
     "by the knockout and rescue data."),
    (96, "renin-angiotensin regulation of aldosterone production", "ACCEPT",
     "Angiotensin II stimulating adrenal zona glomerulosa cells to make and release "
     "aldosterone is the canonical endocrine output of this pathway, and UniProt states it "
     "directly in the FUNCTION line for the angiotensin-2 chain.",
     "Core physiology, and the one term here that names the pathway's endocrine arm. "
     "Accepted on the biology despite the weak citation."),
    (97, "regulation of renal output by angiotensin", "ACCEPT",
     "Another pathway-specific term. Angiotensin II constricts the efferent arteriole, alters "
     "glomerular filtration and promotes proximal sodium reabsorption; loss of the pathway in "
     "humans produces fetal anuria.",
     "Core renal physiology of the pathway, independently corroborated by the renal tubular "
     "dysgenesis genetics in this same record."),
    (102, "regulation of vasoconstriction", "ACCEPT",
     "Angiotensin II is the archetypal endogenous vasoconstrictor; UniProt keywords the "
     "entry 'Vasoactive' and 'Vasoconstrictor'.",
     "Core function. The weak citation does not put the claim in question."),
    (81, "regulation of renal sodium excretion", "ACCEPT",
     "Sodium handling is where the pathway's blood-pressure effect is finally executed, via "
     "direct proximal tubular action and via aldosterone.",
     "Core physiology of the pathway, accepted on the biology with the citation flagged."),
]:
    DECISIONS[_row] = dict(
        summary=_EDITORIAL + _extra,
        action=_act,
        reason=_reason,
        supported_by=[
            ("file:human/AGT/AGT-uniprot.txt",
             "potent regulator of blood pressure, body fluid and electrolyte"),
            Q_KO_BP,
        ],
    )

DECISIONS[55] = dict(
    summary=_EDITORIAL + "The commentary's subject is AGTR1/AGTR2 cross-talk in vascular "
                         "remodelling, and the AT2 arm is conventionally described as "
                         "signalling through bradykinin, nitric oxide and cGMP. That is a "
                         "receptor-level statement about AGTR2, applied here to the ligand's "
                         "precursor.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "The AT2/NO-cGMP arm is real and is the counter-regulatory limb of the pathway, so "
        "the term is not wrong. But it is a statement about receptor signalling taken from an "
        "editorial with no primary data, and it is peripheral to the gene's core role."
    ),
    supported_by=[
        ("PMID:17906677",
         "In addition, Ang II diminished insulin-stimulated phosphorylation of Akt (at "
         "Ser(473)) and eNOS (at Ser(1177)) and NO generation, effects which were reversed by "
         "ACE2 gene transfer and anti-MIF treatment in endothelial cells."),
    ],
)

DECISIONS[100] = dict(
    summary=_EDITORIAL + "Asserts that angiotensin signalling proceeds through a "
                         "cGMP-coupled GPCR pathway. AGTR1 is a Gq/PLC receptor and AGTR2 "
                         "reaches cGMP indirectly, through bradykinin and nitric oxide "
                         "rather than by direct cyclase coupling, so the term overstates the "
                         "directness of the link.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Not wrong in outcome - the AT2 limb does raise cGMP - but the coupling it implies is "
        "indirect, and the only source is an editorial I cannot read. Kept at low confidence "
        "rather than removed, since I cannot inspect the text that supports it."
    ),
    supported_by=[Q_AT2_SHP1],
)

DECISIONS[101] = dict(
    summary=_EDITORIAL + "This one names the canonical mechanism correctly: AGTR1 is a "
                         "Gq/11-coupled receptor and angiotensin II binding activates "
                         "phospholipase C. The cited AT1 cloning papers in this same record "
                         "demonstrate it directly, with inositol phosphate turnover and "
                         "calcium mobilisation.",
    action="ACCEPT",
    reason=(
        "Mechanistically informative and independently demonstrated by two receptor-cloning "
        "papers already cited on this gene. The evidence code and source are weak but the "
        "annotation is the textbook mechanism."
    ),
    supported_by=[Q_AT1A, Q_AT1_CA],
)

DECISIONS[104] = dict(
    summary=_EDITORIAL + "Duplicates the IDA row for the same term from PMID:17906677, where "
                         "angiotensin II is shown to induce MIF in endothelial cells.",
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real biology, but redundant with the IDA row for the identical term and sourced from "
        "a commentary with no data of its own."
    ),
    supported_by=[
        ("PMID:17906677",
         "Gene transfer of ACE2 suppressed the expression of p22phox and MIF induced by "
         "angiotensin (Ang) II and Ang IV, accompanied by a decreased level of malondialdehyde "
         "in cells."),
    ],
)

DECISIONS[94] = dict(
    summary=_EDITORIAL + "'Regulation of cell growth' is about as uninformative as a "
                         "biological process term can be, and the source contains no data. "
                         "The record's one attempt to say something specific in this area - "
                         "GO:0008083 growth factor activity - is contradicted by its own "
                         "citation, and a paper cited elsewhere here reports that angiotensin "
                         "II does not affect proliferation in HUVEC.",
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "An uninformative parent term with a non-traceable author statement from an editorial "
        "as its only support. It conveys nothing that the specific growth-related rows do not, "
        "and those are themselves poorly supported."
    ),
    supported_by=[Q_HUVEC_NOPROLIF],
)

DECISIONS[103] = dict(
    summary=_EDITORIAL + "Same objection as 'regulation of cell growth': a top-level "
                         "regulatory term with no direction, no cell type and no primary "
                         "data behind it. The specific proliferation claims in this record "
                         "are the rat-orthologue fibroblast transfer (which is kept) and the "
                         "growth-factor row (which is contradicted).",
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Generic, direction-free, and sourced from a commentary. Adds nothing over the "
        "specific rows and dilutes the record."
    ),
    supported_by=[Q_HUVEC_NOPROLIF],
)

# ---- proteomics (HDA), remaining localisation, and the rest --------------

DECISIONS[66] = dict(
    summary=(
        "The oldest and, for the 'is_active_in' qualifier, the most apt localisation row: a "
        "1968 study of the enzymatic degradation and electrophoresis of human angiotensin I, "
        "i.e. the peptide chemistry done on circulating material. UniProt cites this paper "
        "for both the signal peptide (residues 1-24) and the 'Secreted' subcellular location. "
        "PubMed holds no abstract for it, so the underlying experiment cannot be inspected "
        "here, but the conclusion is not in question."
    ),
    action="ACCEPT",
    reason=(
        "AGT is a liver-secreted plasma protein and the extracellular compartment is where it "
        "is cleaved by renin and where its peptides meet their receptors, so 'is_active_in' "
        "is the right qualifier. Corroborated by four HDA proteomics datasets, the curated "
        "UniProt location, the IBA and the ISS."
    ),
    supported_by=[Q_SECRETED, Q_LIVER],
)

DECISIONS[112] = dict(
    summary=(
        "A non-traceable author statement drawn from the 2004 consolidated human plasma "
        "proteome list, which merged four methodologies into 1175 non-redundant gene "
        "products. It is a catalogue entry rather than an experiment, but angiotensinogen is "
        "one of the least controversial members of that catalogue."
    ),
    action="ACCEPT",
    reason=(
        "Correct localisation from a weak evidence type. Adds breadth of corroboration rather "
        "than new evidence."
    ),
    supported_by=[
        ("PMID:14718574",
         "We have merged four different views of the human plasma proteome, based on "
         "different methodologies, into a single nonredundant list of 1175 distinct gene "
         "products."),
        Q_SECRETED,
    ],
)

DECISIONS[69] = dict(
    summary=(
        "High-throughput proteomics detection of angiotensinogen in a study of extracellular "
        "matrix remodelling in venous hypertension. The compartment assigned is the correct "
        "general one for a plasma protein."
    ),
    action="ACCEPT",
    reason=(
        "Correct term. Detection of an abundant plasma protein in a tissue proteome is weak "
        "evidence in itself, but 'extracellular region' is broad enough to be right whatever "
        "the source of the material."
    ),
    supported_by=[Q_SECRETED],
)

DECISIONS[77] = dict(
    summary=(
        "High-throughput proteomics detection in the aqueous phase of human colostrum. "
        "Angiotensinogen is a normal constituent of extracellular fluids, so the general "
        "compartment term is correct."
    ),
    action="ACCEPT",
    reason=(
        "Correct term from a weak but unobjectionable observation; 'extracellular region' "
        "cannot be wrong for a secreted plasma protein found in a body fluid."
    ),
    supported_by=[Q_SECRETED],
)

DECISIONS[68] = dict(
    summary=(
        "High-throughput mass spectrometry of extracellular matrix preparations from human "
        "primary and metastatic colon cancers. Angiotensinogen is among the most abundant "
        "proteins in plasma, and plasma proteins are the standard background of any "
        "tissue-derived ECM proteome. Nothing in the study distinguishes matrix-incorporated "
        "angiotensinogen from blood carried in the tissue, and no matrix function has ever "
        "been reported for it."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Detection is not localisation of function. A specific structural compartment term is "
        "being assigned to an abundant soluble plasma protein on the basis of its presence in "
        "a tissue proteome. The general term GO:0005576, which the record already carries "
        "many times over, is what this observation supports."
    ),
    supported_by=[Q_SECRETED, Q_LIVER],
)

DECISIONS[76] = dict(
    summary=(
        "High-throughput proteomics of exosomes isolated from expressed prostatic secretions. "
        "Abundant plasma and body-fluid proteins co-purify with extracellular vesicles by "
        "density and by adsorption, and this term is assigned to hundreds of such proteins on "
        "exactly this basis. No exosomal sorting signal, no vesicle-associated function and no "
        "follow-up exists for angiotensinogen."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "A specific vesicle compartment assigned from co-purification with an abundant "
        "soluble protein. Reproducible but uncharacterised, which is what this action is for."
    ),
    supported_by=[Q_SECRETED],
)

DECISIONS[78] = dict(
    summary=(
        "High-throughput proteomics of microvesicles from the plasma of healthy donors. The "
        "same co-purification argument applies, and rather more forcefully here: the source "
        "material is plasma, where angiotensinogen is present at microgram-per-millilitre "
        "concentrations, so its appearance in any plasma-derived vesicle preparation is "
        "expected regardless of whether it is vesicle-associated."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Assigns a specific particle compartment on the basis of abundance in the starting "
        "material. The soluble plasma pool, already captured by GO:0005576, is the "
        "parsimonious explanation."
    ),
    supported_by=[Q_SECRETED, Q_LIVER],
)

DECISIONS[79] = dict(
    summary=(
        "The evidence is an autoantibody biomarker screen, not a renal-process experiment. "
        "Protein microarrays found raised anti-angiotensinogen autoantibody titres in the "
        "serum of patients with chronic kidney disease. The authors are explicit that they "
        "cannot say what the antibodies bind, cannot establish pathogenicity, and suspect the "
        "titres reflect kidney damage rather than cause it. Nothing in the paper measures a "
        "renal system process attributable to angiotensinogen."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "An IDA whose 'direct assay' is an antibody titre in patient sera. The gene's genuine "
        "renal biology is already carried, and far better, by GO:0002019 regulation of renal "
        "output by angiotensin, GO:0035813 regulation of renal sodium excretion, and the "
        "renal tubular dysgenesis genetics. Marked rather than removed, in keeping with not "
        "overruling an experimental annotation outright, and raised as a question for the "
        "assigning group."
    ),
    supported_by=[
        ("PMID:21183621",
         "We cannot distinguish whether these auto-Ab are targeting angiotensinogen or "
         "angiotensin I, as cross-reactivity in antibodies against these two antigens has "
         "been described ( 33 )."),
        ("PMID:21183621",
         "Significant elevations in the titer of novel auto-Ab were noted against "
         "angiotensinogen and PRKRIP1 in renal insufficiency."),
    ],
)

DECISIONS[70] = dict(
    summary=(
        "Correct, and about a genuinely different peptide. The negative regulation comes from "
        "angiotensin-(1-7), an AGT-derived peptide acting through MAS1, which suppresses the "
        "p38 MAPK activation that angiotensin II induces in vascular smooth muscle cells. So "
        "angiotensinogen is the source of peptides that both activate and inhibit MAP kinase "
        "signalling, and this row captures the counter-regulatory limb."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real peptide pharmacology of the Ang-(1-7)/MAS1 axis, worth retaining because it is "
        "the only row in the record representing that limb. Non-core because it is one "
        "downstream signalling consequence among many. The IMP code is loose - the "
        "perturbations are peptide agonists and the MAS1 antagonist A779, not AGT mutations."
    ),
    supported_by=[
        ("PMID:28283184",
         "Furthermore, Ang II induced p38 MAPK activation, and this was inhibited by the "
         "treatment of Ang-(1-7)."),
    ],
)

DECISIONS[56] = dict(
    summary=(
        "Three steps removed from angiotensinogen. In this atrial fibrosis model angiotensin "
        "II raises miR-23b-3p and miR-27b-3p in human atrial fibroblasts; those miRNAs target "
        "TGFBR3; loss of TGFBR3 activates Smad3; and it is over-expression of the miRNAs, not "
        "angiotensin II, that raises COL1A1, COL3A1 and ACTA2. The 'acts_upstream_of' "
        "qualifier is doing necessary work here."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Real fibrotic biology downstream of angiotensin II and correctly qualified as "
        "upstream rather than participatory, but too indirect to be a function of the gene."
    ),
    supported_by=[
        ("PMID:30729664", "A cell model of atrial fibrosis was achieved in Ang-II-induced HAFs."),
        ("PMID:30729664",
         "Moreover, Smad3 was activated in HAFs in response to Ang-II treatment and "
         "inactivation of Smad3 attenuated up-regulation of miR-23b-3p and miR-27b-3p in "
         "Ang-II-treated HAFs."),
    ],
)

DECISIONS[57] = dict(
    summary=(
        "Directly measured: miR-23b-3p and miR-27b-3p rise in angiotensin II-treated human "
        "atrial fibroblasts, and Smad3 inactivation blocks that rise. This is the most "
        "immediate of the three rows from this paper."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "A real transcriptional response to the hormone in a primary human cell type, "
        "correctly qualified as upstream. Peripheral to the gene's function. The IMP code sits "
        "oddly on an experiment whose perturbation is peptide addition rather than a mutation "
        "in AGT."
    ),
    supported_by=[
        ("PMID:30729664",
         "We found that miR-23b-3p and miR-27b-3p were markedly increased in atrial appendage "
         "tissues of AF patients and in Ang-II-treated HAFs."),
    ],
)

DECISIONS[58] = dict(
    summary=(
        "Nearly tautological as written: angiotensinogen 'acts upstream of' the response to "
        "angiotensin. It is true - angiotensinogen is the sole source of the ligand, so it "
        "necessarily precedes any response to it - but it conveys no information beyond what "
        "GO:0038166 already states, and it would be equally true of every angiotensin "
        "experiment ever done."
    ),
    action="KEEP_AS_NON_CORE",
    reason=(
        "Not wrong, and the qualifier is the correct one, but uninformative: it restates the "
        "definitional relationship between the precursor and its own peptide. Kept because it "
        "is harmless and correctly qualified."
    ),
    supported_by=[
        ("PMID:30729664", "A cell model of atrial fibrosis was achieved in Ang-II-induced HAFs."),
    ],
)

DECISIONS[86] = dict(
    summary=(
        "Two steps removed and a non-traceable author statement. The cited work shows that "
        "angiotensin II acting through AGTR1 raises secretory phospholipase A2 type IIA in rat "
        "aortic smooth muscle cells, and that sPLA2-IIA is what modifies and peroxidises LDL - "
        "an effect abolished by the sPLA2 inhibitor LY311727. So the LDL remodelling is the "
        "enzyme's activity, with angiotensin II two steps upstream of it."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "Role conflation: the term names what sPLA2-IIA does to LDL particles, and assigns it "
        "to the hormone precursor that induces the enzyme. The paper's own inhibitor control "
        "shows the activity is the enzyme's."
    ),
    supported_by=[
        ("PMID:17069818",
         "Stimulation of rat aortic smooth muscle cells with ANG II (10(-7) mol/L) enhanced "
         "sPLA2-IIA protein expression, activity as well as LDL-peroxidation, determined by "
         "western blot, activity assay and malondialdehyde (MDA)-assay and diene formation, "
         "respectively, and were blunted by AT1-receptor blockade (Losartan, 10(-5) mol/L)."),
    ],
)

DECISIONS[114] = dict(
    summary=(
        "A generic term from a genetic association study. PMID:8513325 is the classic report "
        "linking the T235 angiotensinogen variant to preeclampsia in Caucasian and Japanese "
        "cohorts. It is a case-control association, containing no signalling experiment. The "
        "structural work also argues that this variant acts by raising angiotensinogen "
        "concentration rather than by changing what the protein does."
    ),
    action="MARK_AS_OVER_ANNOTATED",
    reason=(
        "'Cell-cell signalling' is an uninformative high-level term, and the traceable source "
        "is an allele-frequency study. The specific and correct version of this claim, "
        "GO:0038166 angiotensin-activated signaling pathway, is already annotated five times "
        "on this gene from papers that actually measured signalling."
    ),
    supported_by=[
        ("PMID:8513325",
         "In a series of Caucasian women with pregnancy-induced hypertension, we have observed "
         "a significant association of preeclampsia with a molecular variant of "
         "angiotensinogen, T235, found previously to be associated with essential "
         "hypertension."),
        ("PMID:20927107",
         "This strengthens previous deductions5,6 that the predisposition to hypertension "
         "results from the small increase in concentration of the polymorphic angiotensinogen "
         "rather than a change in its function."),
    ],
)

DECISIONS[113] = dict(
    summary=(
        "The origin of the serpin-inhibitor claim, and its own wording shows it was never an "
        "activity measurement. This is a 1988 paper reporting the cloning and sequencing of "
        "the MOUSE angiotensinogen gene. Its statement about inhibition is a sequence "
        "alignment: because angiotensinogen is homologous to serpins, the authors aligned the "
        "putative reactive centre across species. The same abstract then notes that the human "
        "site differs from the rodent one and that the significance of that divergence was "
        "unknown. No inhibition assay, no protease, no kinetics - a homology observation "
        "recorded as a traceable author statement and thereafter read as a molecular function."
    ),
    action="REMOVE",
    reason=(
        "The claim is false and its source does not even assert it. Angiotensinogen does not "
        "inhibit serine endopeptidases: it has no reactive bond, a proline-blocked hinge at "
        "P12, MEROPS non-inhibitor classification I04.953, and a crystal structure of "
        "loop-cleaved protein showing it cannot undergo the stressed-to-relaxed transition "
        "that the inhibitory mechanism requires. Its protease partner renin is an aspartyl "
        "protease and AGT is its substrate. Removing this, the IBA and the IEA together "
        "eliminates the claim from the record; no experimental annotation is being overruled, "
        "because none exists."
    ),
    supported_by=[Q_1988, Q_1988_DIVERGE, Q_NONINHIB, Q_LOST_SR],
)

# ---- generated groups ----------------------------------------------------
# The 27 Reactome rows and the 10 rows from one yeast two-hybrid screen say the
# same thing 27 and 10 times respectively, differing only in which reaction or
# which partner is named. Generating them keeps each row specific to its own
# reaction/partner without pretending the reasoning differs.

REACTOME_INTRO = (
    "One of 27 Reactome TAS rows on this gene, all asserting the same term - "
    "located_in extracellular region - and differing only in which reaction is cited. "
    "Together they are 24% of AGT's entire GOA record expressing a single correct claim "
    "once per reaction the protein or one of its peptides participates in. This row cites "
)

REACTOME_REASON = (
    "The term is correct: angiotensinogen and all of its peptide products act in the "
    "extracellular compartment, and this reaction takes place there. Accepted on that basis. "
    "The caveat is about reading the record rather than about this row: 27 identical "
    "assertions from one source database are one projection, not 27 independent findings, "
    "and the count should not be mistaken for weight of evidence."
)

Y2H_INTRO = (
    "One of ten GO:0005515 rows from a single large-scale yeast two-hybrid interactome of "
    "neurodegenerative disease proteins. Angiotensinogen is not a neurodegeneration protein "
    "and appears here as library prey. The partner in this row is "
)

Y2H_REASON = (
    "Bare 'protein binding' from one high-throughput screen, with no functional follow-up, "
    "no orthogonal validation, and a systematic compartment mismatch: AGT is a secreted, "
    "signal-peptide-cleaved, disulfide-bonded, four-site N-glycosylated plasma protein, while "
    "yeast two-hybrid reconstitutes a transcription factor in the yeast nucleus. Across all "
    "ten partners, 0 of 10 share a secreted or extracellular compartment with AGT. The paper "
    "itself calls these candidate interactions, and UniProt's NbExp=3 is replicates within "
    "this one study rather than three independent studies. Marked over-annotated rather than "
    "removed: the screen is reproducible, it is simply uncharacterised for this gene."
)

# ---- NEW rows ------------------------------------------------------------

NEW_ROWS = [
    dict(
        term=("GO:0002003", "angiotensin maturation"),
        evidence_type="IMP",
        reference="PMID:7989296",
        qualifier="involved_in",
        summary=(
            "The GO term whose definition names angiotensinogen does not annotate "
            "angiotensinogen. GO:0002003 is defined as 'The process leading to the attainment "
            "of the full functional capacity of angiotensin by conversion of angiotensinogen "
            "into mature angiotensin in the blood.' Querying QuickGO for it across human, "
            "mouse and rat returns 110 annotations covering essentially every other "
            "participant in the cascade - REN, ACE, ACE2, ENPEP, ANPEP, MME, PREP, PRCP, "
            "CTSG, LVRN, Ace3, and even ATP6AP2, the (pro)renin receptor. Querying the same "
            "endpoint for human AGT (P01019), rat Agt (P01015) and mouse Agt (P11859) "
            "together returns zero annotations to this term - not one angiotensinogen in "
            "any of the three species. Every enzyme that acts on angiotensinogen is "
            "annotated to the process; the protein they act on is invisible. The evidence runs in both "
            "directions: deleting angiotensinogen in mouse abolishes plasma angiotensin I, "
            "and re-expressing it by AAV in hepatocyte-specific Agt-null mice restores plasma "
            "angiotensin II and suppresses the compensatory renin rise."
        ),
        reason=(
            "A pathway-completeness gap rather than a doubtful inference. AGT is not merely "
            "adjacent to this process, it is the substrate the process is defined as acting "
            "on, and the same 'involved_in' qualifier is what every other participant uses. "
            "Adding it makes the renin-angiotensin cascade traversable in GO from its source "
            "protein rather than only from its enzymes."
        ),
        supported_by=[Q_KO, Q_RESCUE, Q_BURIED],
    ),
    dict(
        term=("GO:0002002", "regulation of angiotensin levels in blood"),
        evidence_type="IMP",
        reference="PMID:25691624",
        qualifier="involved_in",
        summary=(
            "The companion gap. GO:0002002 is defined as modulating 'the level of any of the "
            "various angiotensinogen proteolytic products in the blood... by the proteolytic "
            "cleavage of angiotensinogen, and its proteolytic products'. Like GO:0002003 it "
            "is annotated to the cascade's enzymes and receptors (117 annotations across "
            "human, mouse and rat) and to no angiotensinogen in any of those three "
            "species - the same zero-hit query result as for GO:0002003. Angiotensinogen concentration "
            "is rate-influencing rather than merely permissive: plasma AGT sits near the Km "
            "for renin, the hypertension-associated M235T variant acts by raising "
            "angiotensinogen concentration rather than by changing its function, and graded "
            "restoration of AGT in null mice produces graded restoration of angiotensin II "
            "and blood pressure."
        ),
        reason=(
            "Distinct from GO:0002003: maturation is the conversion process, whereas this term "
            "is about setting how much product there is. Both are absent, both are supported "
            "by the same bidirectional perturbation data, and the concentration-dependence is "
            "the specific reason angiotensinogen is a therapeutic target in its own right."
        ),
        supported_by=[Q_RESCUE, Q_RESCUE_BP,
                      ("PMID:20927107",
                       "This strengthens previous deductions5,6 that the predisposition to "
                       "hypertension results from the small increase in concentration of the "
                       "polymorphic angiotensinogen rather than a change in its function.")],
    ),
]

# ---------------------------------------------------------------------------
# Document-level synthesis.
# ---------------------------------------------------------------------------

DESCRIPTION = (
    "Angiotensinogen is the liver-secreted plasma glycoprotein that is the sole source of "
    "the angiotensin peptides, and through them the origin of the renin-angiotensin system "
    "that sets blood pressure, blood volume and electrolyte balance. It is synthesised with "
    "a cleaved 24-residue signal peptide, carries N-glycans at four sites, and circulates in "
    "plasma at high, physiologically rate-influencing concentration. Structurally it belongs "
    "to the serpin superfamily and retains the serpin fold despite only about 22% identity to "
    "its closest serpin relatives, but it is a non-inhibitory serpin: it has no functional "
    "reactive-centre bond, its reactive centre loop does not undergo the stressed-to-relaxed "
    "transition by which inhibitory serpins trap proteases, and it inhibits no protease. The "
    "fold instead serves as a carrier and delivery device for the hormone held in its "
    "N-terminal tail.\n\n"
    "The rate-limiting step of the whole cascade is cleavage of that tail by renin, an "
    "aspartyl protease. Angiotensinogen is not a passive substrate in this reaction. The "
    "scissile Leu-Val bond is buried in an ordered 63-residue N-terminal superstructure and "
    "becomes accessible only through a large conformational change: renin binds through a "
    "tail-into-mouth allosteric mechanism that threads the N terminus into a pocket "
    "equivalent to the hormone-binding site of the carrier serpins, unwinds helix H, and "
    "forms an extensive body-to-body interface with the protease outside its catalytic cleft. "
    "Cleavage specificity and rate are set by angiotensinogen residues and glycans in that "
    "interface. A labile disulfide bridge between Cys42 and Cys162 (Cys18-Cys138 in mature "
    "numbering), the only two cysteines conserved across species, links the tail to the body "
    "of the molecule and gives plasma angiotensinogen a mixture of reduced and oxidised "
    "forms; the oxidised form is more efficiently cleaved by receptor-bound renin, although "
    "removing the bridge in mice does not measurably change angiotensin II production or "
    "blood pressure.\n\n"
    "Renin cleavage releases angiotensin I, which ACE converts to the vasoconstrictor "
    "octapeptide angiotensin II, and further processing by ACE2, aminopeptidases, neprilysin "
    "and other peptidases generates angiotensin III, angiotensin IV, angiotensin-(1-9) and "
    "angiotensin-(1-7). Angiotensin II acts on the AGTR1 and AGTR2 G-protein-coupled "
    "receptors: through AGTR1 it constricts arterioles, drives aldosterone secretion from the "
    "adrenal zona glomerulosa, promotes renal sodium and water retention, and stimulates "
    "cardiac, vascular and fibroblast growth and matrix deposition, while through AGTR2 it "
    "engages SHP-1, inhibits ERK and can promote apoptosis. Angiotensin-(1-7), acting on "
    "MAS1, opposes several of these effects. Loss of angiotensinogen is profound and "
    "informative: knockout mice have no circulating angiotensin I and are markedly "
    "hypotensive, and biallelic human loss-of-function mutations cause autosomal recessive "
    "renal tubular dysgenesis, with absent proximal tubules, fetal anuria and perinatal "
    "death, attributed to chronically low fetal renal perfusion pressure. Common coding "
    "variants, notably M235T, associate with essential hypertension and pre-eclampsia and "
    "appear to act by raising circulating angiotensinogen concentration rather than by "
    "altering the protein's function."
)

REFERENCES = [
    dict(
        id="PMID:20927107",
        title="A redox switch in angiotensinogen modulates angiotensin release.",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The single most important paper for this gene and absent from the deep "
                "research report. Crystal structures of angiotensinogen at 2.1 A and of the "
                "human angiotensinogen-renin complex at 4.4 A. Verified against the cached "
                "full text: it states in its own abstract that angiotensinogen is a "
                "non-inhibitory serpin, which is the basis for removing the three GO:0004867 "
                "rows, and it supplies the 670 A^2 renin interface behind the GO:0002020 "
                "MODIFY. Its redox-switch model is treated as structurally sound but "
                "physiologically contested, because PMID:25691624 tested it in vivo."
            ),
        ),
    ),
    dict(
        id="PMID:30563843",
        title="Structural basis for the specificity of renin-mediated angiotensinogen cleavage.",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "Also missed by the deep research report. Four structures including "
                "loop-cleaved AGT, solved specifically to test whether the reactive centre "
                "loop triggers the stressed-to-relaxed transition; it does not. This is the "
                "experimental demonstration, rather than the assertion, that AGT lacks the "
                "serpin inhibitory mechanism, and it is what makes the GO:0004867 removals "
                "safe. Also the source of the tail-into-mouth mechanism and of the finding "
                "that specificity is set outside renin's active-site cleft."
            ),
        ),
    ),
    dict(
        id="PMID:7989296",
        title="Angiotensinogen-deficient mice with hypotension.",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The foundational loss-of-function evidence, cited by GOA for this gene "
                "nowhere at all. Homozygous Agt-null mice have no plasma immunoreactive "
                "angiotensin I and a systolic pressure of 66.9 mm Hg against 100.4 in "
                "wild-type. Supports both NEW rows and the core blood-pressure functions. "
                "Abstract only; the quantitative result is in the abstract."
            ),
        ),
    ),
    dict(
        id="PMID:25691624",
        title=("Cys18-Cys137 disulfide bond in mouse angiotensinogen does not affect "
               "AngII-dependent functions in vivo."),
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The measured negative that kept a GO term out of this review. AAV delivery "
                "of wild-type versus Cys18Ser/Cys137Ser angiotensinogen into "
                "hepatocyte-specific Agt-null mice gave equivalent plasma angiotensin II, "
                "systolic blood pressure and atherosclerotic lesion size. Directly tests the "
                "PMID:20927107 redox model in vivo and finds the disulfide dispensable. Also "
                "the source of the gain-of-function direction for both NEW rows."
            ),
        ),
    ),
    dict(
        id="PMID:3397061",
        title="Molecular cloning of the mouse angiotensinogen gene.",
        review=dict(
            relevance="MEDIUM",
            correctness="MISCITED",
            notes=(
                "Cited by GOA as a TAS for GO:0004867 serine-type endopeptidase inhibitor "
                "activity, which it does not assert. Its own abstract says only that "
                "angiotensinogen is homologous to serpins and that the authors aligned a "
                "putative reactive centre - and then notes that the human site differs from "
                "the rodent one. A sequence-alignment observation in a mouse gene-cloning "
                "paper became a molecular function annotation on the human gene. Correctly "
                "identified and correctly titled; it simply does not support the claim made "
                "from it."
            ),
        ),
    ),
    dict(
        id="PMID:17159080",
        title=("Cross-talk between angiotensin II receptor types 1 and 2: potential role in "
               "vascular remodeling in humans."),
        review=dict(
            relevance="LOW",
            correctness="LOW_QUALITY",
            notes=(
                "PubMed types this Comment / Editorial / Review; it is a two-page commentary "
                "on another paper, and the cached record contains no abstract text at all. It "
                "is nonetheless the sole source of eleven GOA rows on this gene, four of them "
                "coded TAS. Several of the terms it supports are correct RAS physiology and "
                "are accepted here on the biology rather than on this citation; the generic "
                "ones are marked over-annotated. Flagged so the weight of eleven rows is not "
                "mistaken for eleven findings."
            ),
        ),
    ),
    dict(
        id="PMID:10406457",
        title=("Analysis of functional domains of angiotensin II type 2 receptor involved in "
               "apoptosis."),
        review=dict(
            relevance="MEDIUM",
            correctness="MISCITED",
            notes=(
                "Sound paper, over-extended in GOA. It is an AT2 intracellular-loop "
                "mutagenesis study in PC12 cells measuring apoptosis, ERK inhibition and "
                "SHP-1 activation, and it properly supports the AGTR2-binding, apoptosis and "
                "TRK rows. It cannot support GO:0008083 growth factor activity, which it "
                "contradicts, nor GO:0001974 blood vessel remodeling, which it does not "
                "measure. Abstract only, but the abstract is unambiguous about what was done."
            ),
        ),
    ),
    dict(
        id="PMID:17416596",
        title="Angiotensin II-induced sudden arrhythmic death and electrical remodeling.",
        review=dict(
            relevance="HIGH",
            correctness="MISCITED",
            notes=(
                "An unusually well-justified IGI source: dTGR rats carry both the human renin "
                "and the human angiotensinogen transgenes, and neither alone produces the "
                "phenotype, which is exactly what IGI encodes. Three of its four rows are "
                "sound. The fourth has the sign inverted - GOA reads it as POSITIVE regulation "
                "of gap junction assembly, while the abstract states that connexin 43 was "
                "significantly REDUCED in dTGR. Verified against the cached abstract."
            ),
        ),
    ),
    dict(
        id="PMID:21183621",
        title=("Protein microarrays discover angiotensinogen and PRKRIP1 as novel targets for "
               "autoantibodies in chronic renal disease."),
        review=dict(
            relevance="LOW",
            correctness="MISCITED",
            notes=(
                "Cited as an IDA for GO:0003014 renal system process. The cached full text is "
                "complete and contains no renal-process experiment: it is an autoantibody "
                "biomarker screen, and the authors state they cannot tell whether the "
                "antibodies target angiotensinogen or angiotensin I, nor establish "
                "pathogenicity. Correct paper, correct title, wrong use."
            ),
        ),
    ),
    dict(
        id="PMID:32814053",
        title=("Interactome Mapping Provides a Network of Neurodegenerative Disease Proteins "
               "and Uncovers Widespread Protein Aggregation in Affected Brains."),
        review=dict(
            relevance="LOW",
            correctness="LOW_QUALITY",
            notes=(
                "A competent large-scale study whose output is unsuitable for functional "
                "annotation of this gene. It yields ten bare protein-binding rows on AGT, a "
                "protein unrelated to neurodegeneration; the paper itself calls the results "
                "candidate interactions. All ten partners are intracellular while AGT is "
                "secreted (0/10 shared compartment, computed in AGT-bioinformatics), and "
                "UniProt's NbExp=3 on each is replicates within this study."
            ),
        ),
    ),
    dict(
        id="PMID:16237761",
        title=("Screening of hepatocyte proteins binding to F protein of hepatitis C virus by "
               "yeast two-hybrid system."),
        review=dict(
            relevance="LOW",
            correctness="UNVERIFIED",
            notes=(
                "GOA cites this (via AgBase) for an AGT-HCV F protein interaction. The cached "
                "full text is complete - abstract through the full discussion, in which each "
                "hit is treated in turn - and the word 'angiotensinogen' does not appear in "
                "it. The paper enumerates its 36 positive colonies by identity and "
                "angiotensinogen is not among them; the serpin it does report is C1 "
                "inhibitor. Left UNVERIFIED rather than WRONG_IDENTIFIER because a table lost "
                "in text extraction cannot be excluded."
            ),
        ),
    ),
    dict(
        id="PMID:23082758",
        title=("Structural basis of peptide recognition by the angiotensin-1 converting enzyme "
               "homologue AnCE from Drosophila melanogaster."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited and a good structural paper, but what it shows about AGT is "
                "a 10-residue cleavage product sitting in the active site of a Drosophila "
                "enzyme. UniProt flags the pair 'Xeno'. Recorded on human AGT as bare protein "
                "binding, where it carries no interpretive weight."
            ),
        ),
    ),
    dict(
        id="PMID:16116425",
        title=("Mutations in genes in the renin-angiotensin system are associated with "
               "autosomal recessive renal tubular dysgenesis."),
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The human loss-of-function genetics, and the basis of the UniProt DISEASE "
                "entry for renal tubular dysgenesis. Biallelic AGT mutations among 11 "
                "affected individuals from nine families. The authors' own mechanism is "
                "haemodynamic, which is why the kidney-development row is kept as non-core "
                "rather than as a core developmental function."
            ),
        ),
    ),
    dict(
        id="PMID:1567413",
        title="Cloning and characterization of a human angiotensin II type 1 receptor.",
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "A receptor-cloning paper that is the source of four AGT rows including two "
                "identical GO:0005179 IDA rows. The molecule assayed on the AGT side is "
                "synthetic angiotensin II in ligand-binding studies, so the evidence for "
                "'hormone activity' is real but indirect. The claims are correct and "
                "independently supported; the coding is generous."
            ),
        ),
    ),
    dict(
        id="PMID:1378723",
        title=("Cloning, expression, and characterization of a gene encoding the human "
               "angiotensin II type 1A receptor."),
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "The AT1a receptor cloning paper behind the GO:0031702 IPI and the two IC "
                "rows derived from it. High-affinity angiotensin II binding coupled to "
                "inositol phosphate turnover is directly shown."
            ),
        ),
    ),
    dict(
        id="PMID:15652490",
        title=("Angiotensin II induces focal adhesion kinase/paxillin phosphorylation and cell "
               "migration in human umbilical vein endothelial cells."),
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "Four AGT rows, all from adding synthetic angiotensin II to primary HUVEC. "
                "Well controlled with pathway inhibitors. Also supplies a useful negative - "
                "angiotensin II did not affect HUVEC proliferation - which bears on the "
                "growth-factor-activity row."
            ),
        ),
    ),
    dict(
        id="PMID:18971559",
        title=("Angiotensin II upregulates acyl-CoA:cholesterol acyltransferase-1 via the "
               "angiotensin II Type 1 receptor in human monocyte-macrophages."),
        review=dict(
            relevance="MEDIUM",
            correctness="MISCITED",
            notes=(
                "Good receptor-subtype pharmacology in primary human macrophages, supporting "
                "the angiotensin-signalling, cholesterol and foam-cell rows. It cannot support "
                "the GO:0005576 localisation row also drawn from it: no localisation "
                "experiment on angiotensinogen appears in the study."
            ),
        ),
    ),
    dict(
        id="PMID:17906677",
        title=("Enhanced angiotensin converting enzyme 2 regulates the insulin/Akt signalling "
               "pathway by blockade of macrophage migration inhibitory factor expression."),
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "The paper's subject is ACE2 gene transfer; the AGT-relevant observation is "
                "that angiotensin II and angiotensin IV induce MIF and p22phox in an "
                "endothelial cell line. Correctly cited for the cytokine, inflammation and "
                "ROS rows, but the evidence is a cellular response to an added peptide in an "
                "immortalised line."
            ),
        ),
    ),
    dict(
        id="PMID:15153556",
        title="Angiotensin II increases Pax-2 expression in fetal kidney cells via the AT2 receptor.",
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "Clean AT2-specific pharmacology in mouse embryonic renal cell lines. Supports "
                "the angiotensin-signalling row; the generic transcription row drawn from the "
                "same experiment is marked over-annotated."
            ),
        ),
    ),
    dict(
        id="PMID:18607644",
        title=("Deficiency of intrarenal angiotensin II type 2 receptor impairs paired homeo "
               "box-2 and N-myc expression during nephrogenesis."),
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "AT2R-knockout mouse embryonic kidneys, with an ex vivo angiotensin II "
                "response absent in the nulls. Good genetics for the receptor. Supports the "
                "ureteric-bud branching row; the generic transcription row from the same "
                "experiment is marked over-annotated."
            ),
        ),
    ),
    dict(
        id="PMID:30729664",
        title=("Novel role of the clustered miR-23b-3p and miR-27b-3p in enhanced expression of "
               "fibrosis-associated genes by targeting TGFBR3 in atrial fibroblasts."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited. Three AGT rows, all properly qualified 'acts_upstream_of'. "
                "The most immediate observation - angiotensin II raises miR-23b-3p and "
                "miR-27b-3p in primary human atrial fibroblasts - is direct; the matrix row is "
                "three steps downstream, since the collagen induction is driven by miRNA "
                "over-expression rather than by angiotensin II."
            ),
        ),
    ),
    dict(
        id="PMID:28283184",
        title=("Angiotensin-(1-7) regulates angiotensin II-induced matrix metalloproteinase-8 "
               "in vascular smooth muscle cells."),
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "The only row in the record representing the counter-regulatory "
                "angiotensin-(1-7)/MAS1 limb, which is why it is kept. Correctly cited; the "
                "IMP evidence code is loose, since the perturbations are peptide agonists and "
                "the MAS1 antagonist A779 rather than mutations in AGT."
            ),
        ),
    ),
    dict(
        id="PMID:17069818",
        title=("Angiotensin II type 1-receptor antagonism prevents type IIA secretory "
               "phospholipase A2-dependent lipid peroxidation."),
        review=dict(
            relevance="LOW",
            correctness="MISCITED",
            notes=(
                "Correct paper, wrong agent. The LDL modification it reports is the activity "
                "of sPLA2-IIA, confirmed by the paper's own inhibitor control; angiotensin II "
                "is two steps upstream, inducing the enzyme. Cited on AGT as NAS for LDL "
                "particle remodeling."
            ),
        ),
    ),
    dict(
        id="PMID:8513325",
        title="A molecular variant of angiotensinogen associated with preeclampsia.",
        review=dict(
            relevance="MEDIUM",
            correctness="MISCITED",
            notes=(
                "A historically important genetic association study, cited on AGT as a TAS for "
                "the generic term 'cell-cell signaling', which it contains no experiment "
                "bearing on. The variant it identifies is also now understood to act through "
                "angiotensinogen concentration rather than function."
            ),
        ),
    ),
    dict(
        id="PMID:18202720",
        title=("Conformational switch of angiotensin II type 1 receptor underlying mechanical "
               "stress-induced activation."),
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "Correctly cited for an AGT-AGTR1 interaction (UniProt records the pair as a "
                "cross-species IntAct entry with 10 experiments), but recorded under the "
                "uninformative GO:0005515. MODIFIED to type 1 angiotensin receptor binding."
            ),
        ),
    ),
    dict(
        id="PMID:4300938",
        title="Enzymatic degradation and electrophoresis of human angiotensin I.",
        review=dict(
            relevance="MEDIUM",
            correctness="UNVERIFIED",
            notes=(
                "A 1968 paper cited by UniProt for the signal peptide and the 'Secreted' "
                "location, and by GOA as the IDA behind is_active_in extracellular region. "
                "PubMed holds no abstract for it, so the experiment cannot be inspected here. "
                "The conclusion is not in doubt and is corroborated many times over, but the "
                "evidence itself is unread."
            ),
        ),
    ),
    dict(
        id="PMID:14718574",
        title=("The human plasma proteome: a nonredundant list developed by combination of "
               "four separate sources."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "A consolidated catalogue of 1175 plasma gene products rather than an "
                "experiment. Correctly cited as NAS for extracellular localisation, where it "
                "adds breadth of corroboration and nothing else."
            ),
        ),
    ),
    dict(
        id="PMID:25037231",
        title=("Extracellular matrix signatures of human primary metastatic colon cancers and "
               "their metastases to liver."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited HDA detection. The objection is to the inference, not the "
                "citation: an abundant plasma protein detected in a tissue ECM proteome is "
                "the expected blood background, and no matrix function has been reported for "
                "angiotensinogen."
            ),
        ),
    ),
    dict(
        id="PMID:27068509",
        title=("Extracellular matrix remodelling in response to venous hypertension: proteomics "
               "of human varicose veins."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited HDA detection, assigned to the broad and unobjectionable "
                "GO:0005576 rather than to a specific structure. Accepted."
            ),
        ),
    ),
    dict(
        id="PMID:23533145",
        title=("In-depth proteomic analyses of exosomes isolated from expressed prostatic "
               "secretions in urine."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited HDA detection. Abundant body-fluid proteins routinely "
                "co-purify with extracellular vesicles, and no vesicle-associated function or "
                "sorting signal is known for angiotensinogen."
            ),
        ),
    ),
    dict(
        id="PMID:16502470",
        title=("Human colostrum: identification of minor proteins in the aqueous phase by "
               "proteomics."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited HDA detection in a body fluid, supporting the broad "
                "extracellular term. Accepted."
            ),
        ),
    ),
    dict(
        id="PMID:22516433",
        title=("Proteomic analysis of microvesicles from plasma of healthy donors reveals high "
               "individual variability."),
        review=dict(
            relevance="LOW",
            correctness="VERIFIED",
            notes=(
                "Correctly cited HDA detection, but the starting material is plasma, where "
                "angiotensinogen is present at microgram-per-millilitre concentrations, so its "
                "appearance in a plasma-derived vesicle fraction carries no localisation "
                "information."
            ),
        ),
    ),
    dict(
        id="file:human/AGT/AGT-deep-research-affinage.md",
        title="Affinage mechanistic annotation for AGT (human)",
        review=dict(
            relevance="LOW",
            correctness="LOW_QUALITY",
            notes=(
                "The script's trust gate tripped (self_evaluation_pairwise: tie, not win), and "
                "the record fails independently of that. It confuses AGT with AGXT: the "
                "narrative asserts that AGT has peroxisomal alanine:glyoxylate aminotransferase "
                "activity, citing a primary hyperoxaluria type 1 study in AgxtQ84-/- rats. "
                "'AGT' is also the common abbreviation for that enzyme, whose HGNC symbol is "
                "AGXT (P21549) - a different gene, a different protein, a different "
                "compartment. The error propagates into its own GO grounding, which lists "
                "GO:0016740 transferase activity and GO:0005777 peroxisome for a secreted "
                "plasma serpin; none of that grounding was imported. Recall is also poor: none "
                "of its 11 citations appears in AGT's GOA record, and it misses every paper "
                "that matters for the molecular biology (PMID:20927107, PMID:30563843, "
                "PMID:7989296, PMID:25691624, PMID:12045255). Nothing from it is used as "
                "supporting_text for a mechanistic claim."
            ),
        ),
    ),
    dict(
        id="file:human/AGT/AGT-uniprot.txt",
        title="UniProtKB P01019 (ANGT_HUMAN) flat file",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The curated record, used for the signal peptide and chain boundaries, the "
                "eight angiotensin PEPTIDE features, the Cys42-Cys162 disulfide, the four "
                "N-glycosylation sites, the 'Secreted' location, the serpin similarity "
                "statement, the MEROPS I04.953 cross-reference, and the IntAct entries. The "
                "last of those matter for the review's framing: UniProt attaches the receptor "
                "interactions to PRO_ chain identifiers (PRO_0000032458 with AGTR1, "
                "PRO_0000032459 with AGTR2) rather than to full-length angiotensinogen."
            ),
        ),
    ),
    dict(
        id="file:human/AGT/AGT-bioinformatics/RESULTS.md",
        title="AGT (P01019) - bioinformatics support for the annotation review",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "Three analyses written for this review, all fetching live from UniProt, "
                "QuickGO and the committed PANTHER PAINT slice. They establish that AGT is "
                "MEROPS I04.953 while all 7 resolvable seeds of the donating IBD node are "
                "MEROPS inhibitors; that AGT has no UniProt reactive bond and a "
                "proline-blocked hinge at P12 (Pro430); and that 0 of the 10 partners from "
                "the large-scale yeast two-hybrid screen share a compartment with a secreted "
                "protein. The document states its own limits, including that the "
                "receptor-binding rows are deliberately excluded from the compartment metric."
            ),
        ),
    ),
    dict(
        id="GO_REF:0000033",
        title="Annotation inferences using phylogenetic trees",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The PAINT route behind all four IBA rows. Three of the four are correctly "
                "placed. The fourth, GO:0004867, descends from node PTN008970140, a "
                "SERPINA-clade node seeded exclusively by inhibitory serpins; the pipeline is "
                "applied correctly and the node placement is what fails. The same family "
                "already demonstrates the remedy, since node PTN002606963 carries an IRD "
                "blocking GO:0005576 for the intracellular serpin subclade."
            ),
        ),
    ),
    dict(
        id="GO_REF:0000002",
        title="Gene Ontology annotation through association of InterPro records with GO terms",
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "Behind two IEA rows that make an instructive pair. From the "
                "angiotensinogen-specific signatures IPR000227 and IPR033834 it produces "
                "GO:0003081, which is exactly right. From the family-wide signature IPR000215 "
                "(Serpin_fam) it produces GO:0004867, which is wrong for this member. The "
                "pipeline is correctly applied in both cases; the defect is in the breadth of "
                "the second signature's GO mapping."
            ),
        ),
    ),
    dict(
        id="GO_REF:0000024",
        title=("Manual transfer of experimentally-verified manual GO annotation data to "
               "orthologs by curator judgment of sequence similarity"),
        review=dict(
            relevance="HIGH",
            correctness="VERIFIED",
            notes=(
                "The route behind all six ISS rows, transferring from rat Agt (P01015) and "
                "mouse Agt (P11859), both 1:1 orthologues rather than paralogues. I checked "
                "each donor in QuickGO and all six still carry the transferred term with "
                "experimental evidence, so none is stale or itself inferred. Worth noting that "
                "three of the six trace to a single rat study, PMID:8348686, so they are not "
                "three independent observations."
            ),
        ),
    ),
    dict(
        id="GO_REF:0000120",
        title="Combined Automated Annotation using Multiple IEA Methods",
        review=dict(
            relevance="MEDIUM",
            correctness="VERIFIED",
            notes=(
                "Behind the GO:0005576 IEA row. One of its two inputs, UniProtKB-SubCell "
                "SL-0243, is AGT's own curated 'Secreted' location, so this row is not "
                "independent of the UniProt record - but it is correct."
            ),
        ),
    ),
]

for _reactome in [
    "R-HSA-1989774", "R-HSA-2022403", "R-HSA-2022412", "R-HSA-2065357", "R-HSA-2022368",
    "R-HSA-2022378", "R-HSA-2022379", "R-HSA-2022381", "R-HSA-2022383", "R-HSA-2022396",
    "R-HSA-2022398", "R-HSA-2022399", "R-HSA-2022405", "R-HSA-2022411", "R-HSA-2028294",
    "R-HSA-2065355", "R-HSA-374173", "R-HSA-379048", "R-HSA-380073", "R-HSA-749448",
    "R-HSA-749452", "R-HSA-749454", "R-HSA-749456", "R-HSA-9615348", "R-HSA-9944473",
    "R-HSA-9944540", "R-NUL-2022369",
]:
    REFERENCES.append(dict(id=f"Reactome:{_reactome}"))

PROPOSED_NEW_TERMS: list = []

CORE_FUNCTIONS = [
    dict(
        description=(
            "Renin substrate and angiotensin delivery device. Angiotensinogen holds the "
            "angiotensin sequence in an ordered 63-residue N-terminal tail with the scissile "
            "Leu-Val bond buried, and presents it to renin through a tail-into-mouth "
            "conformational change that threads the N terminus into a pocket equivalent to "
            "the hormone-binding site of the carrier serpins. Binding is not confined to the "
            "catalytic cleft: there is an extensive, largely hydrophobic body-to-body "
            "interface with the protease, and mutagenesis and kinetics show that the rate and "
            "specificity of angiotensin I release are set by angiotensinogen residues and "
            "glycans outside renin's active site. This is the molecular function of the "
            "full-length precursor itself, as opposed to that of the peptides cleaved from "
            "it, and it is the rate-limiting step of the whole renin-angiotensin cascade."
        ),
        supported_by=[
            dict(reference_id=Q_670[0], supporting_text=Q_670[1]),
            dict(reference_id=Q_TAIL[0], supporting_text=Q_TAIL[1]),
            dict(reference_id=Q_BURIED[0], supporting_text=Q_BURIED[1]),
            dict(reference_id="PMID:30563843",
                 supporting_text=(
                     "Mutagenesis and kinetic analyses confirmed that renin-mediated "
                     "production of angiotensin I is controlled by interactions of amino acid "
                     "residues and glycan components outside renin's active-site cleft.")),
        ],
        molecular_function=dict(id="GO:0002020", label="protease binding"),
        directly_involved_in=[
            dict(id="GO:0002003", label="angiotensin maturation"),
            dict(id="GO:0002002", label="regulation of angiotensin levels in blood"),
        ],
        locations=[dict(id="GO:0005576", label="extracellular region")],
    ),
    dict(
        description=(
            "Source of the angiotensin peptide hormones, and through them the effector of "
            "systemic blood pressure and fluid-electrolyte homeostasis. Angiotensin II, "
            "released from angiotensinogen by the sequential action of renin and ACE, binds "
            "the AGTR1 and AGTR2 G-protein-coupled receptors; through AGTR1 it activates "
            "phospholipase C and mobilises calcium, constricts arterioles, drives adrenal "
            "aldosterone production and renal sodium retention, and so sets arterial pressure "
            "and blood volume. Because angiotensin II has no gene of its own, this activity "
            "is recorded on the precursor, which is also what UniProt does. The dependence is "
            "absolute and demonstrated in both directions: deleting angiotensinogen abolishes "
            "circulating angiotensin I and drops systolic pressure by a third, and restoring "
            "it restores angiotensin II and pressure."
        ),
        supported_by=[
            dict(reference_id=Q_KO[0], supporting_text=Q_KO[1]),
            dict(reference_id=Q_KO_BP[0], supporting_text=Q_KO_BP[1]),
            dict(reference_id=Q_RESCUE_BP[0], supporting_text=Q_RESCUE_BP[1]),
            dict(reference_id=Q_AT1A[0], supporting_text=Q_AT1A[1]),
            dict(reference_id=Q_AT1_CA[0], supporting_text=Q_AT1_CA[1]),
        ],
        molecular_function=dict(id="GO:0005179", label="hormone activity"),
        directly_involved_in=[
            dict(id="GO:0038166", label="angiotensin-activated signaling pathway"),
            dict(id="GO:0003081",
                 label="regulation of systemic arterial blood pressure by renin-angiotensin"),
            dict(id="GO:0002034",
                 label="maintenance of blood vessel diameter homeostasis by renin-angiotensin"),
            dict(id="GO:0002018",
                 label="renin-angiotensin regulation of aldosterone production"),
            dict(id="GO:0002016", label="regulation of blood volume by renin-angiotensin"),
        ],
        locations=[dict(id="GO:0005576", label="extracellular region")],
    ),
    dict(
        description=(
            "Receptor ligand for the two angiotensin receptors, with opposing outputs. The "
            "released octapeptide binds AGTR1, the receptor through which the pressor, "
            "aldosterone-releasing and growth-promoting actions run, and AGTR2, through which "
            "it engages SHP-1, inhibits ERK and can promote apoptosis. UniProt records both "
            "interactions on the peptide chains rather than on full-length angiotensinogen "
            "(PRO_0000032458 with AGTR1, PRO_0000032459 with AGTR2), which is the correct "
            "reading of what does the binding. Further processing generates "
            "angiotensin-(1-7), which acts through MAS1 and opposes several angiotensin II "
            "effects, so a single gene supplies ligands for both limbs of the system."
        ),
        supported_by=[
            dict(reference_id=Q_AT1A[0], supporting_text=Q_AT1A[1]),
            dict(reference_id=Q_AT2_APOP[0], supporting_text=Q_AT2_APOP[1]),
            dict(reference_id="file:human/AGT/AGT-uniprot.txt",
                 supporting_text="PRO_0000032458; P30556: AGTR1; NbExp=2"),
            dict(reference_id="file:human/AGT/AGT-uniprot.txt",
                 supporting_text="PRO_0000032459; P50052: AGTR2; NbExp=2"),
        ],
        molecular_function=dict(id="GO:0031702", label="type 1 angiotensin receptor binding"),
        directly_involved_in=[
            dict(id="GO:0038166", label="angiotensin-activated signaling pathway"),
            dict(id="GO:0007200",
                 label="phospholipase C-activating G protein-coupled receptor signaling pathway"),
        ],
        locations=[dict(id="GO:0005576", label="extracellular region")],
    ),
]

KNOWLEDGE_GAPS = [
    dict(
        gap_statement=(
            "Whether the Cys42-Cys162 (mature Cys18-Cys138) redox switch has any "
            "physiological role is unresolved, and the two decisive experiments disagree."
        ),
        boundary=(
            "Firmly established: the disulfide exists and is the only cysteine pair conserved "
            "across species; it is labile, with plasma holding a near 40:60 reduced:oxidised "
            "mixture; the oxidised form is preferentially cleaved by receptor-bound renin, "
            "giving a 4-fold increase in angiotensin release in vitro; and the oxidised form "
            "is elevated in the maternal circulation in pre-eclampsia. Equally firmly "
            "established: removing the bridge in mice changes nothing measurable."
        ),
        gap_kind=["BIOLOGY"],
        dark_aspect="RESIDUAL_SUBGAP",
        status="OPEN",
        significance=(
            "This is the only proposed mechanism by which angiotensinogen itself, rather than "
            "renin abundance, could regulate the cascade's output, and it is the stated "
            "rationale for antioxidant approaches to pre-eclampsia. If real it would justify a "
            "molecular function on the precursor; if not, angiotensinogen is a concentration "
            "variable and nothing more. No GO term is proposed here for exactly this reason."
        ),
        resolution=(
            "The in vitro and in vivo experiments differ in more than species: the in vitro "
            "effect requires the prorenin receptor and cell-surface renin, while the mouse "
            "experiment measured whole-animal plasma angiotensin II, blood pressure and "
            "lesion size, which are strongly buffered by renin feedback. A tissue-level or "
            "prorenin-receptor-dependent readout in the Cys-to-Ser mice, or a pregnancy "
            "challenge, would discriminate."
        ),
        provenance=[
            dict(reference_id="PMID:25691624",
                 supporting_text=(
                     "These data indicate that the Cys18-Cys137 disulfide bond in AGT is "
                     "dispensable for AngII production and AngII-dependent functions in "
                     "mice.")),
            dict(reference_id="PMID:20927107",
                 supporting_text=(
                     "the prorenin receptor whilst having little effect on the reduced form "
                     "gives a 4-fold increase in the renin-binding affinity (Km) of the "
                     "oxidised form, with a consequent 4-fold increase in the catalytic "
                     "release of angiotensin")),
        ],
    ),
    dict(
        gap_statement=(
            "Why the angiotensin peptides are carried on a serpin scaffold at all is unknown. "
            "The fold is retained but the mechanism that defines the superfamily has been "
            "lost, and no function has been assigned to the retained body of the molecule "
            "beyond providing the renin-binding surface."
        ),
        boundary=(
            "Established: angiotensinogen retains the typical serpin fold at only about 22% "
            "identity to its closest serpin relatives; it has no functional reactive centre "
            "and loop cleavage does not trigger the stressed-to-relaxed transition; and the "
            "related non-inhibitory serpins SERPINA6 and SERPINA7 do use that transition to "
            "release their bound hormones, which angiotensinogen cannot. The 400-odd residues "
            "C-terminal to the angiotensin sequence have no assigned activity."
        ),
        gap_kind=["BIOLOGY"],
        dark_aspect="MF_DARK",
        status="OPEN",
        significance=(
            "The authors of the structural work call this puzzling in print. If the serpin "
            "body has a function beyond presenting the tail to renin - a second ligand, a "
            "clearance receptor, a protein partner - it would be the first molecular activity "
            "of the precursor beyond protease binding, and would change what should be "
            "annotated on this gene."
        ),
        resolution=(
            "Structure-guided mutagenesis separating the renin-presentation surface from the "
            "rest of the serpin body, combined with an unbiased interaction screen using "
            "correctly folded, glycosylated, secreted angiotensinogen rather than a yeast "
            "two-hybrid system."
        ),
        provenance=[
            dict(reference_id="PMID:30563843",
                 supporting_text=(
                     "In contrast, it has been shown that AGT has lost the ability to undergo "
                     "this typical serpin S-to-R transition (29), confirmed here by our "
                     "structure of loop-cleaved AGT, so it was very puzzling why the serpin "
                     "framework was selected in the course of evolution as an angiotensin "
                     "carrier.")),
            dict(reference_id="PMID:20927107",
                 supporting_text=(
                     "Although angiotensinogen has only 22% sequence identity to its closest "
                     "relatives amongst other serpins3, it substantially retains the typical "
                     "serpin fold")),
        ],
    ),
    dict(
        gap_statement=(
            "Angiotensinogen has no curated protein interaction partner outside the "
            "renin-angiotensin cascade that is supported by anything better than a "
            "large-scale yeast two-hybrid screen."
        ),
        boundary=(
            "Established: the renin interaction is structurally solved, and UniProt records a "
            "disulfide-linked 2:2 heterotetramer with the proform of PRG2 and a probable "
            "2:2:2 complex with pro-PRG2 and C3dg during pregnancy. Beyond those, all sixteen "
            "GO:0005515 IPI rows are either angiotensin receptors, a Drosophila enzyme "
            "co-crystallised with the peptide, or the ten partners of one interactome screen, "
            "none of which shares a compartment with a secreted protein and none of which has "
            "functional follow-up."
        ),
        gap_kind=["BIOLOGY", "CURATION"],
        dark_aspect="MF_DARK",
        status="OPEN",
        significance=(
            "The pregnancy heterotetramer with pro-PRG2 and C3dg is a genuine, curated complex "
            "that appears nowhere in this gene's GO record - no complex term, no interaction "
            "row - while ten unvalidated yeast two-hybrid pairings do appear. The record's "
            "interaction content is therefore close to inverted with respect to evidence "
            "quality."
        ),
        resolution=(
            "Curation of the pro-PRG2/C3dg complex from PMID:20927107 and PMID:7539791, and "
            "an interaction screen using native or correctly processed secreted "
            "angiotensinogen from plasma."
        ),
        provenance=[
            dict(reference_id="file:human/AGT/AGT-uniprot.txt",
                 supporting_text=(
                     "heterotetramer with the proform of PRG2 and as a complex (probably a")),
            dict(reference_id="file:human/AGT/AGT-bioinformatics/RESULTS.md",
                 supporting_text="All ten PMID:32814053 partners are intracellular"),
        ],
    ),
    dict(
        gap_statement=(
            "GO cannot express the distinction between a precursor protein and the peptides "
            "cleaved from it, so every function of angiotensin I, II, III, IV and (1-7) is "
            "recorded indistinguishably on the 476-residue precursor."
        ),
        boundary=(
            "Established, and handled better elsewhere: UniProt separates the layers "
            "explicitly, with eight PEPTIDE features, per-chain FUNCTION blocks for "
            "angiotensin-2, angiotensin-3 and angiotensin-(1-7), and IntAct entries keyed to "
            "PRO_ chain identifiers rather than to P01019. Reactome likewise names its "
            "participants AGT(25-32), AGT(25-31) and so on. GOA has only the accession, so "
            "roughly forty rows on this gene describe the peptides while a handful describe "
            "the protein, with nothing to tell them apart."
        ),
        gap_kind=["ONTOLOGY", "CURATION"],
        dark_aspect="MF_DARK",
        status="OPEN",
        significance=(
            "This is why the record looks the way it does. A reader cannot tell from GOA that "
            "'hormone activity' and 'type 1 angiotensin receptor binding' belong to an "
            "octapeptide while 'protease binding' belongs to the precursor, nor that the "
            "precursor has essentially no annotated activity of its own. The same problem "
            "affects every prohormone and polyprotein."
        ),
        resolution=(
            "Annotation against PRO identifiers, which already exist for these chains "
            "(PRO_0000032456 through PRO_0000032463) and which UniProt already uses for the "
            "receptor interactions. No new ontology term is needed; what is needed is for GOA "
            "to accept the finer-grained entity."
        ),
        provenance=[
            dict(reference_id="file:human/AGT/AGT-uniprot.txt",
                 supporting_text="PRO_0000032458; P30556: AGTR1; NbExp=2"),
            dict(reference_id="file:human/AGT/AGT-uniprot.txt",
                 supporting_text=(
                     "PTM: In response to low blood pressure, the enzyme renin/REN cleaves")),
        ],
    ),
]

SUGGESTED_QUESTIONS = [
    dict(question=(
        "For the PAINT curators of PTHR11461: would an IRD at the angiotensinogen node block "
        "GO:0004867 the way the existing IRD at PTN002606963 blocks GO:0005576 for the "
        "intracellular serpin subclade? Angiotensinogen is the one non-inhibitory member of "
        "the SERPINA clade that node PTN008970140 covers, and the same leak will reach every "
        "angiotensinogen orthologue in the family, not just the human gene.")),
    dict(question=(
        "For InterPro: should the interpro2go mapping IPR000215 (Serpin_fam) -> GO:0004867 "
        "exist at all? The family contains many non-inhibitory members - corticosteroid-binding "
        "globulin, thyroxine-binding globulin, PEDF, ovalbumin, angiotensinogen - and MEROPS "
        "already distinguishes them by reserving the I04.9xx range. The gene-level "
        "angiotensinogen signatures IPR000227 and IPR033834 produce a correct annotation "
        "through the same pipeline.")),
    dict(question=(
        "For BHF-UCL: GO:1903598 positive regulation of gap junction assembly is annotated to "
        "AGT by IGI from PMID:17416596, but that paper reports connexin 43 significantly "
        "REDUCED in the double-transgenic rats. Should this be GO:1903597, negative regulation "
        "of gap junction assembly?")),
    dict(question=(
        "For AgBase: can the AGT-HCV F protein interaction annotated from PMID:16237761 be "
        "traced? The full text of that paper enumerates its 36 positive colonies by identity "
        "and does not mention angiotensinogen anywhere; the serpin it reports is C1 inhibitor. "
        "If the supporting data are in a table not present in the retrievable text, a pointer "
        "would settle it.")),
    dict(question=(
        "For UniProt and GOA jointly: the pregnancy-specific disulfide-linked 2:2 "
        "heterotetramer of angiotensinogen with pro-PRG2, and the probable 2:2:2 complex with "
        "pro-PRG2 and C3dg, are curated in UniProt from PMID:20927107 and PMID:7539791 but "
        "appear nowhere in the GO record. What is the barrier - a missing complex term, or "
        "simply that no one has curated it?")),
    dict(question=(
        "Would GOA accept annotations against the PRO chain identifiers that already exist for "
        "this entry? Roughly forty rows on AGT describe the pharmacology of an octapeptide, "
        "and UniProt already keys the receptor interactions to PRO_0000032458 and "
        "PRO_0000032459 rather than to P01019.")),
    dict(question=(
        "Is the eleven-row dependence of this gene's record on PMID:17159080, a two-page "
        "editorial with no primary data and no abstract, intentional? Four of those rows are "
        "coded TAS, which implies traceability to a primary source that the commentary itself "
        "would have to supply.")),
]

SUGGESTED_EXPERIMENTS = [
    dict(description=(
        "Test directly whether angiotensinogen inhibits any serine endopeptidase. Incubate "
        "purified plasma-derived and recombinant glycosylated angiotensinogen with a panel of "
        "serine proteases spanning the targets of its SERPINA clade-mates - neutrophil "
        "elastase and proteinase 3 for SERPINA1, thrombin and activated protein C for "
        "SERPINA5, cathepsin G for SERPINA3 - and look for both residual activity loss and, "
        "critically, the SDS-stable covalent acyl-enzyme complex that is diagnostic of the "
        "serpin mechanism. The prediction from the structure and from MEROPS I04.953 is that "
        "no complex forms with any of them. This is the experiment that would convert the "
        "GO:0004867 removal from an argument into a measurement, and its absence from the "
        "literature is why the claim survived for nearly forty years.")),
    dict(description=(
        "Discriminate the redox switch's physiology from its biochemistry. The in vitro effect "
        "requires cell-surface renin bound to the prorenin receptor, while the in vivo test "
        "used whole-animal plasma angiotensin II and blood pressure, both strongly buffered by "
        "renin feedback. Cross the Cys18Ser/Cys137Ser knock-in onto a background with "
        "tissue-specific prorenin receptor readouts and measure local angiotensin generation "
        "in kidney and vascular wall, rather than circulating levels; add a pregnancy challenge, "
        "since the human observation that motivated the model is pre-eclampsia.")),
    dict(description=(
        "Ask what the serpin body is for. Use the renin-complex structure to design "
        "angiotensinogen variants that retain the N-terminal tail and the renin-binding "
        "surface but disrupt distinct patches elsewhere on the molecule, express them as "
        "correctly glycosylated secreted protein, and test each for renin cleavage kinetics "
        "(to confirm the presentation function is intact) and then for binding partners, "
        "cellular uptake and plasma half-life. Any patch whose disruption changes clearance or "
        "partner binding without changing cleavage would be the first evidence of a second "
        "function for the 400 residues C-terminal to the angiotensin sequence.")),
    dict(description=(
        "Replace the ten yeast two-hybrid interactions with something interpretable. Pull down "
        "native angiotensinogen from human plasma with a monoclonal antibody raised against "
        "the body of the molecule rather than the angiotensin tail, and identify co-eluting "
        "proteins by mass spectrometry, in plasma from non-pregnant donors and from pregnant "
        "donors with and without pre-eclampsia. The positive control is built in: the "
        "pro-PRG2/C3dg complex should appear in the pregnancy samples and not the others, "
        "which both validates the method and would supply the curation that the GO record "
        "currently lacks.")),
]
