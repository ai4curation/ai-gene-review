"""Configuration for the septal-junction module genome scan.

All identifiers are grounded in modules/septal_junction.yaml and the per-gene
reviews under genes/NOSS1/. Nothing here is a result; results are computed by
scan.py and written to TSV / RESULTS.md.
"""

# Module components: gene -> (Nostoc PCC 7120 exemplar UniProt acc, InterPro family
# term used in the module, or None if the component has no dedicated family model).
# "family_specific" flags whether that InterPro entry is a SPECIFIC family (a good
# genome marker) or a BROAD domain shared by many unrelated paralogs.
COMPONENTS = {
    "FraD":  {"exemplar": "P46079",     "interpro": "IPR020360", "family_specific": True,
              "note": "SJ membrane/periplasmic anchor; FraD-specific family"},
    "FraC":  {"exemplar": "P46078",     "interpro": "IPR054663", "family_specific": True,
              "note": "septal integral-membrane protein; FraC-specific family"},
    "SepN":  {"exemplar": "A0ACD7RWW5", "interpro": None,        "family_specific": False,
              "note": "SJ plug; NO Pfam/InterPro/PANTHER model -> homology only"},
    "SepJ":  {"exemplar": "A0ACD7RSI0", "interpro": "IPR000620", "family_specific": False,
              "note": "SepJ/FraG; EamA/DMT domain is broad (many DMT paralogs)"},
    "FraE":  {"exemplar": "A0ACD7RSN5", "interpro": "IPR032688", "family_specific": False,
              "note": "ABC-2/NosY-like permease; broad ABC-2 permease family"},
    "AmiC1": {"exemplar": "A0ACD7S1M0", "interpro": "IPR050695", "family_specific": False,
              "note": "septal amidase; Amidase_3 family is broad"},
    "AmiC2": {"exemplar": "A0ACD7S2F2", "interpro": "IPR050695", "family_specific": False,
              "note": "septal amidase (principal nanopore driller); Amidase_3 broad"},
}

# Target genomes: taxon_id -> (label, reference-proteome UPID, expected class)
# POS = filamentous heterocyst-forming cyanobacterium (should carry the SJ module)
# NEG = unicellular cyanobacterium (should lack FraD/SepN)
# SELF = Nostoc PCC 7120, the organism the module was built from
TARGETS = {
    "103690":  ("Nostoc sp. PCC 7120",              "UP000002483", "SELF"),
    "63737":   ("Nostoc punctiforme PCC 73102",     "UP000001191", "POS"),
    "240292":  ("Anabaena variabilis ATCC 29413",   "UP000002533", "POS"),
    "1111708": ("Synechocystis sp. PCC 6803",       "UP000001425", "NEG"),
    "1140":    ("Synechococcus elongatus PCC 7942", "UP000889800", "NEG"),
}

# phmmer significance threshold for calling a homolog "detected"
EVALUE_CUTOFF = 1e-5
