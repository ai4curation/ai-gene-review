"""Sequence panel for the ARHGEF15 DH-domain specificity analysis.

Kept in one module so the fetcher, the analysis and the self-test cannot drift apart
in what they believe the panel is.

Roles
-----
TARGET       the human protein under review
ANCHOR       mouse Ephexin5 — the protein in which Margolis et al. 2010 (PMID:21029865)
             numbered the alpha5-helix residues L562/Q566/R567 and the EphB2 site Y361
FAMILY       the other human ephexins; these are also the PANTHER PTHR12845 IBA donors
             named in the GOA WITH/FROM fields
RHOA_SPEC    GEFs whose measured specificity is RhoA (positive comparators: if the
             alpha5 signature means what Margolis says, these should carry it)
RAC_CDC42    GEFs whose measured specificity is Rac1 or Cdc42 (negative comparators:
             these should NOT carry it)

The two comparator classes exist so the signature can FAIL. A signature present in
every Dbl-family GEF would say nothing about substrate choice.
"""

TARGET = "O94989"
ANCHOR = "Q5FWH6"

PANEL = {
    # accession: (label, role, measured_specificity_note)
    "O94989": ("human ARHGEF15 / Ephexin5", "TARGET", "see review"),
    "Q5FWH6": (
        "mouse Arhgef15 / Ephexin5",
        "ANCHOR",
        "RhoA yes; Rac1/Cdc42 no by GST-PBD pulldown (PMID:21029865). "
        "RhoA and Cdc42 both yes in whole brain by effector pulldown (PMID:40138406).",
    ),
    "Q8N5V2": ("human NGEF / Ephexin1", "FAMILY", "RhoA, Rac1 and Cdc42 (PMID:11336673)"),
    "Q8IW93": ("human ARHGEF19 / Ephexin2", "FAMILY", "not established here"),
    "Q12774": ("human ARHGEF5 / Ephexin3", "FAMILY", "not established here"),
    "Q5VV41": ("human ARHGEF16 / Ephexin4", "FAMILY", "RhoG (PMID:33597305)"),
    "Q92888": ("human ARHGEF1 / p115RhoGEF", "RHOA_SPEC", "RhoA-specific"),
    "O15085": ("human ARHGEF11 / PDZ-RhoGEF", "RHOA_SPEC", "RhoA-specific"),
    "Q9NZN5": ("human ARHGEF12 / LARG", "RHOA_SPEC", "RhoA-specific"),
    "Q13009": ("human TIAM1", "RAC_CDC42", "Rac1-specific"),
    "P98174": ("human FGD1", "RAC_CDC42", "Cdc42-specific"),
    "Q15811": ("human ITSN1", "RAC_CDC42", "Cdc42-specific"),
}

# Positions are 1-based in the ANCHOR (mouse Ephexin5, Q5FWH6) as published.
# alpha5-helix triad: mutating all three to alanine (the "E5-LQR" construct) abolished
# RhoA activation in PMID:21029865 -- i.e. this is the published loss-of-function control.
ANCHOR_SITES = {
    562: ("L", "alpha5 triad; RhoA-vs-Rac/Cdc42 specificity residue (PMID:21029865)"),
    566: ("Q", "alpha5 triad; RhoA-vs-Rac/Cdc42 specificity residue (PMID:21029865)"),
    567: ("R", "alpha5 triad; RhoA-vs-Rac/Cdc42 specificity residue (PMID:21029865)"),
    361: ("Y", "EphB2 phosphorylation site controlling degradation (PMID:21029865) "
               "and Cdc42-vs-RhoA selectivity (PMID:40138406)"),
}

# BSVD5 missense variants, 1-based in the TARGET (human O94989) as UniProt lists them.
# PMID:36929019 names its knock-in mouse "Arhgef15-e(V368M)", which does not match
# UniProt's human V360M; mapping the human position onto the mouse protein tests
# whether that is the same residue in the other species' numbering or a real discrepancy.
TARGET_VARIANTS = {
    21: ("R", "BSVD5 R21C; decreased GEF activity (PMID:36929019)"),
    360: ("V", "BSVD5 V360M; knock-in mouse recapitulates CSVD + osteoporosis (PMID:36929019)"),
    604: ("R", "R604C, sporadic epilepsy, uncertain significance (PMID:23647072)"),
}
