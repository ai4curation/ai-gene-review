# katG (Catalase-peroxidase) — Pseudomonas putida KT2440 (PSEPK)

UniProt: Q88GQ0 (KATG_PSEPK), locus PP_3668, 751 aa, EC 1.11.1.21.

## Function summary

KatG is a bifunctional, heme b-dependent catalase-peroxidase (hydroperoxidase, HPI-type).
It decomposes hydrogen peroxide by two coupled activities at a single heme active site:
a catalatic reaction (2 H2O2 -> O2 + 2 H2O) and a broad-spectrum peroxidatic reaction
(H2O2 + AH2 -> A + 2 H2O), oxidizing diverse electron-donor substrates. These activities
make KatG a central component of the cellular defense against oxidative/H2O2 stress.

## Provenance (verbatim)

- FUNCTION: [UniProt "Bifunctional enzyme with both catalase and broad-spectrum"] /
  [UniProt "peroxidase activity."]
- CATALYTIC ACTIVITY (peroxidatic): [UniProt "Reaction=H2O2 + AH2 = A + 2 H2O"]
- CATALYTIC ACTIVITY (catalatic): [UniProt "Reaction=2 H2O2 = O2 + 2 H2O"]
- EC number: [UniProt "EC=1.11.1.21"]
- COFACTOR: [UniProt "Name=heme b; Xref=ChEBI:CHEBI:60344"] with
  [UniProt "Binds 1 heme b (iron(II)-protoporphyrin IX) group per dimer."]
- Heme iron ligation: BINDING residue 285 is the
  [UniProt "axial binding residue"] for the heme b Fe.
- Active site: [UniProt "ACT_SITE        91"] noted as
  [UniProt "Proton acceptor"].
- SUBUNIT: [UniProt "Homodimer or homotetramer."]
- PTM / Trp-Tyr-Met crosslink: [UniProt "Formation of the three residue Trp-Tyr-Met cross-link is important"]
  / [UniProt "for the catalase, but not the peroxidase activity of the enzyme."]
  This signature covalent crosslink (residues 90/244/270) is the hallmark of the
  catalase-peroxidase subfamily and is required specifically for catalatic turnover.
- SIMILARITY: [UniProt "Belongs to the peroxidase family. Peroxidase/catalase"] /
  [UniProt "subfamily."]
- Keywords: [UniProt "Heme; Hydrogen peroxide; Iron; Metal-binding; Oxidoreductase; Peroxidase;"]

## Annotation assessment notes

Core molecular functions: catalase activity (GO:0004096) and peroxidase activity
(GO:0004601) — both directly supported by the two UniProt catalytic-activity reactions
and the bifunctional FUNCTION statement.

Core biological processes: response to oxidative stress (GO:0006979), hydrogen peroxide
catabolic process (GO:0042744), cellular response to hydrogen peroxide (GO:0070301),
and cellular oxidant detoxification (GO:0098869) — all consistent with H2O2-decomposing
function. These are accepted; the cellular-response/detoxification terms are reasonable
but more peripheral than the direct catabolic process.

Broad terms relative to specific function: heme binding (GO:0020037) and metal ion
binding (the keyword-derived GO:0046872, not separately listed in the GOA TSV but
present in the UniProt cross-references) describe cofactor binding rather than the
catalytic function. Heme binding is a real, mechanistically essential property
(supported by the COFACTOR and axial-binding-residue evidence) and is informative for a
heme enzyme, so it is retained but flagged as non-core/over-annotated relative to the
specific catalase and peroxidase activity terms. "metal ion binding" is the broadest
of these and over-annotated when heme binding is present.

Cellular component: cytosol (GO:0005829) is a reasonable TreeGrafter prediction for a
soluble bacterial catalase-peroxidase; retained as non-core (IEA, no direct localization
evidence for KT2440).

Caveat: evidence for this entry is "Inferred from homology" (PE 3) and all GO
annotations are IEA. No KT2440-specific experimental publication characterizing KatG was
available; the only cited reference (PMID:12534463) is the genome sequencing paper.
