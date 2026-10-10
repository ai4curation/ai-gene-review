"""Per-protein manual decisions for the 283 vesicle-type dossiers (vesicle_review/dossiers.yaml).

Written by a reviewer after reading each gene's dossier rows (UniProt location/function and
features, other location annotations as leads, source sample, current review). Nothing
here is computed. Decisions are per protein because every row of a gene asserts the same
thing (a vesicle-type location from an EV proteome); where the sample type would change
the call it is said in the basis, and R holds per-row overrides where a protein's rows
differ in sample (ALB). APOE's one row here is a plasma-microvesicle sample; its other
vesicle rows, from non-plasma samples, were reviewed in decisions_settled.py and kept.

Framework: MISEV2018 (PMID:30637094), section 4-b-1 and Table 3, used as a guide for each
judgement, not as a rule:
  * Category 1 (transmembrane/GPI proteins of the plasma membrane or endosomes) and
    Category 2 (cytosolic proteins, including promiscuous cargo such as cytosolic enzymes
    and cytoskeleton) are expected EV contents. The location is true but is not where the
    protein works -> KEEP_AS_NON_CORE.
  * Category 3 (major constituents of co-isolated non-EV structures; APOA1/2, APOB and ALB
    are the recommended negative markers for plasma/serum EVs) -> MARK_AS_OVER_ANNOTATED.
  * Category 4 (residents of nucleus, mitochondria, ER, Golgi, autophagosome, peroxisome:
    found in some EVs but not enriched in small EVs of plasma-membrane/endosome origin), for
    an *exosome* annotation -> MARK_AS_OVER_ANNOTATED.
  * Category 5 (secreted or lumenal proteins; association with EVs needs the cognate EV
    receptor to be explored) -> MARK_AS_OVER_ANNOTATED absent such evidence.
  * ACCEPT only where MISEV itself treats the protein as an EV marker actively incorporated
    by the biogenesis machinery (ALIX/PDCD6IP).
"""

CAT1 = ("KEEP_AS_NON_CORE", "Transmembrane/lipid-anchored protein of the plasma membrane or endosomal system "
        "(UniProt); such proteins are expected EV contents (MISEV2018 (PMID:30637094) category 1). True, but not its core location.")
CAT2 = ("KEEP_AS_NON_CORE", "Cytosolic protein (UniProt); cytosolic proteins, including abundant enzymes and "
        "cytoskeletal proteins, are expected and often promiscuous EV contents (MISEV2018 (PMID:30637094) category 2). True, but not "
        "its core location.")
CAT3 = ("MARK_AS_OVER_ANNOTATED", "MISEV2018 (PMID:30637094) category 3 covers non-EV structures that "
        "co-isolate with EVs, chiefly lipoproteins and albumin, from plasma, serum and serum-containing culture; "
        "detection does not establish EV localization.")
CAT4 = ("MARK_AS_OVER_ANNOTATED", "Resident of an intracellular compartment that MISEV2018 (PMID:30637094) lists as not enriched in "
        "small EVs of plasma-membrane/endosomal origin (category 4); an exosome annotation from a bulk EV proteome "
        "is not supported.")
CAT5 = ("MARK_AS_OVER_ANNOTATED", "Secreted or lumenal protein (UniProt); MISEV2018 (PMID:30637094) category 5 says EV association "
        "of such proteins needs the cognate EV-surface receptor to be shown, and none is shown for this protein.")


def note(base: tuple[str, str], extra: str) -> tuple[str, str]:
    return (base[0], f"{extra} {base[1]}")


G = {
    "AARS1": note(CAT2, "Cytoplasmic aminoacyl-tRNA synthetase."),
    "ABCB4": note(CAT1, "Canalicular plasma-membrane phospholipid flippase."),
    "ACLY": note(CAT2, "Cytosolic ATP-citrate lyase."),
    "ACSL4": note(CAT4, "UniProt places ACSL4 in mitochondrial outer, peroxisomal and ER membranes."),
    "ACTA1": note(CAT2, "Actin."),
    "ACTB": note(CAT2, "Cytoplasmic actin."),
    "ACTG2": note(CAT2, "Smooth-muscle actin."),
    "ACTR1A": note(CAT2, "Dynactin Arp1 subunit."),
    "ACTR1B": note(CAT2, "Dynactin Arp1 subunit."),
    "ADGRV1": note(CAT1, "Plasma-membrane adhesion GPCR."),
    "AGT": note(CAT5, "Secreted angiotensinogen."),
    "AHCTF1": note(CAT4, "Nuclear pore assembly factor (nucleus, nuclear envelope)."),
    "AHCY": note(CAT2, "Cytoplasmic adenosylhomocysteinase."),
    "AK2": note(CAT4, "Mitochondrial intermembrane-space adenylate kinase."),
    "ALB": note(CAT3, "Serum albumin, which MISEV2018 (PMID:30637094) names as a negative marker; see R for "
                      "each row's sample."),
    "ALDH7A1": note(CAT2, "Cytosolic isoform (UniProt isoform 2: cytosol)."),
    "ALDOB": note(CAT2, "Cytosolic aldolase."),
    "ALK": note(CAT1, "Plasma-membrane receptor tyrosine kinase."),
    "ALPL": note(CAT1, "GPI-anchored plasma-membrane alkaline phosphatase."),
    "ANXA11": note(CAT2, "Calcium-dependent membrane-binding annexin; annexins are classic category 2 EV proteins."),
    "AP2M1": note(CAT2, "Plasma-membrane clathrin adaptor subunit (peripheral, cytosolic face)."),
    "AP4M1": note(CAT4, "AP-4 coat subunit of the trans-Golgi network (UniProt ECO:0000269)."),
    "APAF1": note(CAT2, "Cytoplasmic apoptosome scaffold."),
    "APOB": note(CAT3, "Apolipoprotein B, named by MISEV2018 (PMID:30637094) as a negative marker."),
    "APOE": note(CAT3, "Apolipoprotein E recovered from a plasma microvesicle preparation. MISEV2018 "
                       "(PMID:30637094) names APOA1/2 and APOB, not APOE, as negative markers, but APOE is carried "
                       "on the same plasma lipoproteins, so this sample cannot separate the two. The earlier ACCEPT "
                       "described APOE's lipoprotein biology, not EV localization. (APOE's other vesicle rows, "
                       "from non-plasma samples, are KEEP_AS_NON_CORE; see decisions_settled.py.)"),
    "APOL1": note(CAT3, "HDL-associated apolipoprotein L1, recovered from a plasma microvesicle preparation."),
    "APP": note(CAT1, "Plasma-membrane/endosomal type I membrane protein; the earlier ACCEPT gave no basis for "
                      "exosomes being a core location."),
    "APPL2": note(CAT2, "Peripheral early-endosome adaptor."),
    "APRT": note(CAT2, "Cytosolic salvage enzyme."),
    "ARF1": note(CAT2, "Myristoylated cytosolic small GTPase that cycles onto membranes."),
    "ARHGAP23": note(CAT2, "Cytosolic Rho GAP."),
    "ARHGEF18": note(CAT2, "Cytoplasmic/cortical Rho GEF."),
    "ARL6": note(CAT2, "Peripheral ciliary-membrane GTPase (urinary EVs carry ciliary proteins)."),
    "ARL8A": note(CAT2, "Peripheral late-endosome/lysosome GTPase."),
    "ARL8B": note(CAT2, "Peripheral late-endosome/lysosome GTPase."),
    "ARMC9": note(CAT2, "Cytoplasmic ciliary basal-body protein."),
    "ARPC1B": note(CAT2, "Arp2/3 complex subunit."),
    "ARSA": note(CAT5, "Soluble lysosomal sulfatase."),
    "ARSB": note(CAT5, "Soluble lysosomal sulfatase."),
    "ASS1": note(CAT2, "Cytosolic urea-cycle enzyme."),
    "ATIC": note(CAT2, "Cytosolic purine-synthesis enzyme."),
    "ATP1A1": note(CAT1, "Plasma-membrane Na+/K+-ATPase."),
    "ATP1A2": note(CAT1, "Plasma-membrane Na+/K+-ATPase."),
    "ATP1A3": note(CAT1, "Plasma-membrane Na+/K+-ATPase."),
    "ATP2B2": note(CAT1, "Plasma-membrane Ca2+-ATPase."),
    "ATP6AP1": note(CAT4, "UniProt places ATP6AP1 in ER and ER-Golgi intermediate compartment membranes."),
    "ATP6AP2": note(CAT1, "Prorenin receptor / V-ATPase accessory protein, with UniProt lysosome-membrane and cell-surface "
                          "locations."),
    "ATP6V0A1": note(CAT1, "V-ATPase V0 a1 subunit of endosomal/vesicle membranes."),
    "ATP6V1A": note(CAT2, "V-ATPase V1 subunit, assembled on endosomal and apical membranes from the cytosol."),
    "ATP6V1B1": note(CAT2, "V-ATPase V1 subunit of the apical membrane of renal intercalated cells."),
    "ATP6V1B2": note(CAT2, "V-ATPase V1 subunit."),
    "ATP6V1C1": note(CAT2, "V-ATPase V1 subunit."),
    "ATP6V1C2": note(CAT2, "V-ATPase V1 subunit."),
    "ATP6V1D": note(CAT2, "V-ATPase V1 subunit."),
    "ATP6V1E1": note(CAT2, "V-ATPase V1 subunit."),
    "ATP6V1F": note(CAT2, "V-ATPase V1 subunit."),
    "ATP6V1H": note(CAT2, "V-ATPase V1 subunit."),
    "AUP1": note(CAT4, "ER-membrane and lipid-droplet protein (UniProt ECO:0000269)."),
    "BLVRB": note(CAT2, "Cytoplasmic reductase."),
    "BPGM": note(CAT2, "Cytosolic erythrocyte enzyme."),
    "BPTF": note(CAT4, "Nuclear chromatin-remodelling subunit."),
    "BTD": note(CAT5, "Secreted biotinidase."),
    "C1GALT1C1": note(CAT4, "ER-membrane chaperone (Cosmc)."),
    "C1QB": note(CAT5, "Secreted complement C1q subunit, recovered from a plasma microvesicle preparation."),
    "C3": note(CAT5, "Secreted complement C3."),
    "CACNA2D1": note(CAT1, "Plasma-membrane calcium-channel subunit."),
    "CACYBP": note(CAT2, "Cytoplasmic/nuclear calcyclin-binding protein."),
    "CAD": note(CAT2, "Cytoplasmic pyrimidine-synthesis enzyme."),
    "CAND1": note(CAT2, "Cytoplasmic cullin-exchange factor."),
    "CANT1": note(CAT4, "ER/Golgi-membrane nucleotidase."),
    "CANX": note(CAT4, "ER-membrane chaperone; calnexin is a commonly used ER (non-small-EV) marker."),
    "CAPN5": note(CAT2, "Cytosolic calpain."),
    "CARD11": note(CAT2, "Cytoplasmic/membrane-raft signalling scaffold."),
    "CC2D1A": note(CAT2, "Cytoplasmic protein that binds ESCRT-III."),
    "CD2AP": note(CAT2, "Cytoplasmic adaptor linking membrane proteins to actin."),
    "CHMP3": note(CAT2, "ESCRT-III subunit acting on the cytosolic face of endosomes; its presence in EVs follows from "
                        "ILV formation, but the exosome is a destination, not where it acts."),
    "CLU": note(CAT5, "Secreted clusterin (UniProt isoform 1: secreted); the earlier ACCEPT rested on its being "
                      "secreted, which does not establish EV localization. Applies to the plasma microvesicle row too."),
    "CR1": note(CAT1, "Plasma-membrane complement receptor (podocyte/erythrocyte)."),
    "CRYAB": note(CAT2, "Cytoplasmic small heat-shock protein."),
    "CSNK2B": note(CAT2, "CK2 regulatory subunit (cytoplasmic and nuclear)."),
    "CTH": note(CAT2, "Cytoplasmic enzyme."),
    "CTNNB1": note(CAT2, "Cytoplasmic/junctional beta-catenin."),
    "CUL3": note(CAT2, "Cullin scaffold with a cytoplasmic pool."),
    "DDB1": note(CAT2, "Cytoplasmic/nuclear CRL4 adaptor."),
    "DNAJC7": note(CAT2, "Cytoplasmic co-chaperone."),
    "DUT": note(CAT4, "Nuclear and mitochondrial dUTPase isoforms (UniProt)."),
    "DYNC1H1": note(CAT2, "Cytoplasmic dynein heavy chain."),
    "ENO3": note(CAT2, "Cytoplasmic enolase."),
    "ENPP4": note(CAT1, "Plasma-membrane ectoenzyme; the earlier ACCEPT asserted activity in exosomes without evidence."),
    "FASN": note(CAT2, "Cytoplasmic fatty-acid synthase."),
    "FTCD": note(CAT2, "Cytosolic enzyme."),
    "GAA": note(CAT5, "Soluble lysosomal alpha-glucosidase."),
    "GAPDH": note(CAT2, "Cytosolic glycolytic enzyme found in many EV proteomes; the exosome is a destination, not "
                        "GAPDH's core location, so the earlier ACCEPT is downgraded."),
    "GART": note(CAT2, "Cytosolic purine-synthesis enzyme."),
    "GATM": note(CAT4, "Mitochondrial intermembrane-space enzyme."),
    "GBE1": note(CAT2, "Cytosolic glycogen-branching enzyme."),
    "GGCT": note(CAT2, "Cytosolic enzyme."),
    "GLUL": note(CAT2, "Cytosolic glutamine synthetase."),
    "GPC4": note(CAT1, "GPI-anchored plasma-membrane glypican."),
    "GPD1": note(CAT2, "Cytoplasmic enzyme."),
    "GPX4": note(CAT2, "Cytoplasmic isoform of the peroxidase."),
    "GRHPR": note(CAT2, "Cytosolic reductase."),
    "GRID1": ("MARK_AS_OVER_ANNOTATED", "Postsynaptic glutamate-receptor delta subunit whose expression is essentially "
                                         "restricted to the CNS; detection in urinary exosomes is implausible for the "
                                         "native protein and more likely a peptide misassignment."),
    "HBS1L": note(CAT2, "Cytoplasmic GTPase."),
    "HEXB": note(CAT5, "Soluble lysosomal hexosaminidase."),
    "HSPA1A": note(CAT2, "Cytosolic Hsp70; Hsp70 is a classic category 2 EV protein. Expected EV cargo, not a core "
                         "location, so the earlier ACCEPT is downgraded. Applies to the plasma microvesicle row too."),
    "IMPDH2": note(CAT2, "Cytosolic enzyme."),
    "LDHA": note(CAT2, "Cytoplasmic lactate dehydrogenase."),
    "LDHB": note(CAT2, "Cytoplasmic lactate dehydrogenase."),
    "LMAN1": note(CAT4, "ERGIC/Golgi membrane lectin."),
    "LMAN2": note(CAT4, "ERGIC/Golgi membrane lectin."),
    "MDH1": note(CAT2, "Cytosolic malate dehydrogenase."),
    "MDH2": note(CAT4, "Mitochondrial matrix malate dehydrogenase."),
    "MGAT1": note(CAT4, "Golgi-membrane glycosyltransferase."),
    "MYH10": note(CAT2, "Non-muscle myosin II."),
    "MYH9": note(CAT2, "Non-muscle myosin II."),
    "NAGK": note(CAT2, "Cytosolic kinase."),
    "NANS": note(CAT2, "Cytosolic sialic-acid synthase."),
    "NEU1": note(CAT5, "Lysosomal sialidase (lysosome lumen/membrane)."),
    "NRAS": note(CAT1, "Lipid-anchored plasma-membrane GTPase (cytoplasmic face)."),
    "PAICS": note(CAT2, "Cytosolic purine-synthesis enzyme."),
    "PARK7": note(CAT2, "Cytoplasmic DJ-1; its EV presence matters as a biomarker, not as its site of action, so the "
                        "earlier ACCEPT is downgraded."),
    "PDCD6IP": ("ACCEPT", "ALIX is named by MISEV2018 (PMID:30637094) among proteins actively incorporated into EVs and is a standard EV "
                          "marker; with syntenin and ESCRT it sorts cargo into intraluminal vesicles, so exosome localization "
                          "follows directly from its function."),
    "PDXK": note(CAT2, "Cytosolic kinase."),
    "PEX1": note(CAT2, "Cytosolic AAA ATPase recruited to peroxisomes (UniProt cytosol, ECO:0000269)."),
    "PFAS": note(CAT2, "Cytoplasmic purine-synthesis enzyme."),
    "PGAM2": note(CAT2, "Cytosolic glycolytic enzyme."),
    "PGD": note(CAT2, "Cytoplasmic pentose-phosphate enzyme."),
    "PGLS": note(CAT2, "Cytoplasmic pentose-phosphate enzyme."),
    "PLCG2": note(CAT2, "Cytoplasmic/membrane-raft phospholipase."),
    "PMVK": note(CAT2, "Cytosolic kinase."),
    "PPP2R1A": note(CAT2, "Cytoplasmic PP2A scaffold."),
    "PTPN6": note(CAT2, "Cytoplasmic tyrosine phosphatase."),
    "PYGL": note(CAT2, "Cytosolic glycogen phosphorylase."),
    "PYGM": note(CAT2, "Cytosolic glycogen phosphorylase."),
    "RAB1B": note(CAT4, "Prenylated GTPase of the ER-to-Golgi pathway (early secretory compartments)."),
    "RACK1": note(CAT2, "Cytoplasmic/peripheral plasma-membrane scaffold and ribosomal protein."),
    "RPE": note(CAT2, "Cytosolic epimerase."),
    "RPS3": note(CAT2, "Cytosolic ribosomal protein."),
    "SCAMP3": note(CAT1, "Endosomal/post-Golgi membrane protein. The earlier ACCEPT said SCAMP3 is required for EV "
                         "biogenesis, but the cited work (PMID:19158374, PMID:23418353) shows it regulates ESCRT-dependent "
                         "MVB sorting of EGFR, not EV biogenesis."),
    "SCGB1A1": note(CAT5, "Secreted uteroglobin; the earlier ACCEPT rested on prostate expression, which does not establish "
                          "EV association."),
    "SERINC5": note(CAT1, "Plasma-membrane multipass protein."),
    "SGSH": note(CAT5, "Soluble lysosomal sulfamidase."),
    "SHMT1": note(CAT2, "Cytoplasmic serine hydroxymethyltransferase."),
    "SHMT2": note(CAT4, "Mitochondrial serine hydroxymethyltransferase."),
    "SLC22A5": note(CAT1, "Apical plasma-membrane carnitine transporter."),
    "SLC25A1": note(CAT4, "Mitochondrial inner-membrane carrier."),
    "SLC25A3": note(CAT4, "Mitochondrial inner-membrane carrier."),
    "SLC3A1": note(CAT1, "Apical plasma-membrane transporter subunit."),
    "SMS": note(CAT2, "Cytosolic spermine synthase."),
    "STOM": note(CAT1, "Peripheral plasma-membrane raft protein (stomatin), released in microvesicles; expected EV "
                       "content but not its core location, so the earlier ACCEPT is downgraded. Applies to the plasma "
                       "microvesicle row too."),
    "SYNE2": note(CAT4, "Nuclear-envelope (outer nuclear membrane) protein."),
    "TAX1BP1": note(CAT2, "Cytoplasmic autophagy adaptor."),
    "THBS1": note(CAT5, "Secreted matricellular thrombospondin-1; the earlier ACCEPT rested on its being secreted."),
    "THBS4": note(CAT5, "Secreted thrombospondin-4; the earlier ACCEPT rested on its being secreted."),
    "TKFC": note(CAT2, "Cytosolic kinase."),
    "TKT": note(CAT2, "Cytosolic transketolase."),
    "TMEM63A": note(CAT1, "Lysosome/endosome membrane channel."),
    "TOLLIP": note(CAT2, "Cytoplasmic/endosomal adaptor."),
    "UFC1": note(CAT2, "Cytosolic E2 enzyme."),
    "UGGT1": note(CAT4, "ER-lumenal glucosyltransferase with an ER-retrieval signal."),
    "UGP2": note(CAT2, "Cytoplasmic UDP-glucose pyrophosphorylase."),
    "VPS4A": note(CAT2, "ESCRT AAA ATPase acting on the cytosolic face of endosomes; the exosome is a destination, "
                        "not where it acts."),
    "VPS4B": note(CAT2, "ESCRT AAA ATPase acting on the cytosolic face of endosomes; the exosome is a destination, "
                        "not where it acts."),
}

# Rows taken over by a later, separate review on main; recorded in decisions.yaml, not edited.
SUPERSEDED = {
    "CD2AP": "ai4curation/ai-gene-review#4287 re-reviewed both rows (UNDECIDED pending the source tables)",
}

# Per-row overrides where a protein's rows differ in sample and the basis should say so.
_ALB = "Serum albumin, which MISEV2018 (PMID:30637094) names as a negative marker for EVs from plasma, serum and serum-containing culture."
R = {
    ("ALB", 52): note(CAT3, f"{_ALB} Here, urinary exosomes, where filtered plasma albumin is abundant."),
    ("ALB", 53): note(CAT3, f"{_ALB} Here, exosomes from cultured B cells, where serum albumin in the medium is a recognised co-isolate."),
    ("ALB", 54): note(CAT3, f"{_ALB} Here, exosomes from cultured trabecular meshwork cells, where serum albumin in the medium is a recognised co-isolate."),
    ("ALB", 55): note(CAT3, f"{_ALB} Here, exosomes from expressed prostatic secretions in urine."),
    ("ALB", 57): note(CAT3, f"{_ALB} Here, microvesicles isolated from plasma, the sample MISEV's marker is meant for."),
}

# supported_by entries that argued for the action this review overturned (a previous
# reviewer's own judgement rather than evidence); dropped from the row.
S = {
    ("ARF1", 44): ["file:human/ARF1/ARF1-notes.md"],
    ("ARF1", 50): ["file:human/ARF1/ARF1-notes.md"],
    ("ARF1", 51): ["file:human/ARF1/ARF1-notes.md"],
}
