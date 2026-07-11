# PHKA1 review notes

UniProtKB:P46020 (KPB1_HUMAN). Gene: PHKA1 (HGNC:8925), X chromosome. 1223 aa.
Phosphorylase b kinase regulatory subunit alpha, skeletal muscle isoform ("alpha M").

## Core biology

PHKA1 is the **muscle isoform of the alpha regulatory subunit** of phosphorylase
kinase (PhK). PhK is a large (αβγδ)4 hexadecameric holoenzyme:

- **gamma (PHKG1/PHKG2)** = the catalytic protein kinase (EC 2.7.11.19)
- **alpha (PHKA1/PHKA2)** and **beta (PHKB)** = large **regulatory** subunits (NOT kinases)
- **delta** = calmodulin (Ca2+ sensor)

UniProt SUBUNIT: "Hexadecamer of 4 heterotetramers, each composed of alpha, beta,
gamma, and delta subunits. Alpha (PHKA1 or PHKA2) and beta (PHKB) are regulatory
subunits, gamma (PHKG1 or PHKG2) is the catalytic subunit, and delta is calmodulin."

The cryo-EM structure of human muscle PhK [PMID:38548794] directly establishes the
non-catalytic, regulatory nature of the alpha subunit:
- "The α- and β-subunits possess glucoamylase-like domains, but exhibit no detectable
  enzyme activities." (i.e. PHKA1 has a glucoamylase-like fold but is NOT catalytically active)
- "The α-subunit serves as a bridge between the β-subunit and the γδ subcomplex, and
  facilitates the γ-subunit to adopt an autoinhibited state."
- Ca2+ binding to calmodulin triggers de-inhibition of gamma via a spring-loaded mechanism.

PhK phosphorylates glycogen phosphorylase (b -> a), triggering glycogenolysis; in muscle
this supplies glucose-1-phosphate for glycolytic ATP during contraction (Reactome
R-HSA-71541: "The cytosolic phosphorylase kinase complex catalyzes the phosphorylation of
the subunits of the glycogen phosphorylase (PYGM) dimer.").

PHKA1's own molecular role is regulatory: it bridges beta and gamma-delta, holds gamma
autoinhibited, and binds calmodulin (UniProt: "The alpha chain may bind calmodulin";
two Calmodulin-binding regions annotated at 810-840 and 1046-1086). PhK activity is
switched on by PKA phosphorylation of serines in the alpha and beta subunits together with
Ca2+/calmodulin (UniProt ACTIVITY REGULATION: "By phosphorylation of various serine
residues. Allosteric regulation by calcium.").

The alpha subunit carries a "multiphosphorylation domain" that is a hotspot of differential
mRNA splicing and evolution; the human alpha M lacks part of the rabbit
multiphosphorylation domain including the main PKA site [PMID:8226841].

## Disease

Deficiency causes **glycogen storage disease type IXd** (GSD9D / GSD VIII; X-linked muscle
phosphorylase kinase deficiency; MIM:300559) — exercise intolerance, myalgia, cramps,
occasional myoglobinuria, slowly progressive distal muscle weakness. First human PHKA1
mutation was a nonsense mutation in alpha M [PMID:7874115]. A novel PHKA1 mutation
associating myopathy with cognitive impairment expands the spectrum [PMID:33799212].

## Localization

Cytosolic (Reactome; TAS GO:0005829). UniProt lists Cell membrane / Lipid-anchor /
Cytoplasmic side (ECO:0000305, inferred from a possible C-terminal farnesylation of the
final Cys, though UniProt notes the terminal tripeptide is probably not removed and the
C-terminus is not methylated). The plasma-membrane SubCell mapping is thus weakly
supported inference; the functional and structural consensus is that PhK is a cytosolic
complex. Treated as over-annotation.

## Annotation actions (summary)

- GO:0005964 phosphorylase kinase complex (IBA part_of) — ACCEPT (core; structurally confirmed)
- GO:0005964 phosphorylase kinase complex (IPI ComplexPortal PMID:38548794) — ACCEPT (core)
- GO:0004689 phosphorylase kinase activity (IEA ARBA, enables) — MARK_AS_OVER_ANNOTATED
  (PHKA1 non-catalytic; activity belongs to holoenzyme/gamma)
- GO:0004689 phosphorylase kinase activity (TAS PMID:8226841, enables) — MARK_AS_OVER_ANNOTATED
- GO:0005516 calmodulin binding (IEA InterPro, enables) — ACCEPT
- GO:0005737 cytoplasm (IEA ARBA, located_in) — ACCEPT (broad but correct)
- GO:0005886 plasma membrane (IEA SubCell, located_in) — MARK_AS_OVER_ANNOTATED (weak lipid-anchor inference; PhK is cytosolic)
- GO:0005975 carbohydrate metabolic process (IEA InterPro, involved_in) — MODIFY -> glycogen catabolic process
- GO:0005977 glycogen metabolic process (IEA GO_REF:0000120) — ACCEPT
- GO:0005977 glycogen metabolic process (TAS PMID:7874115) — ACCEPT
- GO:0005980 glycogen catabolic process (IDA ComplexPortal PMID:38548794) — ACCEPT (core)
- GO:0045819 positive regulation of glycogen catabolic process (IMP PMID:33799212) — ACCEPT (regulatory role)
- GO:0006091 generation of precursor metabolites and energy (TAS PMID:7874115) — KEEP_AS_NON_CORE (high-level)
