# SLC2A5 (GLUT5) — curation notes

UniProt: P22732 (GTR5_HUMAN). Gene: SLC2A5 / GLUT5. 501 aa, 12-TM major
facilitator superfamily (MFS) sugar transporter, Glucose transporter subfamily
(TC 2.A.1.1.13), class II GLUT. Human chromosome 1p36.2.

## Core biology (synthesized)

GLUT5 is the **fructose-specific facilitative (uniport) transporter** — it moves
D-fructose down its concentration gradient by facilitated diffusion, with **no
Na+/proton coupling and no energy input**. It is the principal apical
(brush-border) entry route for dietary fructose in small-intestinal enterocytes.

- Substrate specificity: fructose-specific, with only low activity toward other
  monosaccharides. UniProt FUNCTION: "Functions as a fructose transporter that
  has only low activity with other monosaccharides"; the curated catalytic
  activity is the symmetric facilitated reaction "D-fructose(out) = D-fructose(in)"
  (Rhea:RHEA:60372) [P22732 UniProt].
- The original cloning paper called GLUT5 a "cytochalasin B-sensitive glucose
  carrier" [PMID:1695905 "the GLUT5 protein is a cytochalasin B-sensitive glucose carrier"],
  but this was superseded: human GLUT5 expressed in Xenopus oocytes "exhibits
  selectivity for fructose transport ... with a Km of 6 mM" and "fructose transport
  by GLUT5 is not inhibited by cytochalasin B" [PMID:1634504]. Glucose handling is
  negligible/low-efficiency (UniProt: "Can mediate the uptake of 2-deoxyglucose,
  but with low efficiency (PubMed:1695905)"). Reported kinetics: KM=30.1 mM for
  D-fructose [PMID:28083649]; a KM=0.63 mM for D-glucose figure is recorded
  [PMID:17710649] but physiological glucose transport is not a GLUT5 function —
  dedicated transporters GLUT1-4 (SLC2A1-4) handle glucose.
- Substrate selectivity determinant: a conserved hydrophobic NXI/NXV motif in TM7
  (Ile at the position equivalent to GLUT7 Ile-314; GLUT5 Ile-296) governs fructose
  access. Mutation to Val removes fructose transport in GLUT7/2/5 without affecting
  glucose [PMID:16186102; PMID:17710649]. The human GLUT5 p.I296V variant,
  however, "remained unaffected" for fructose uptake [PMID:28083649], and
  I296V "does not affect D-fructose or D-glucose transport" (UniProt VARIANT).
- Structure: rat and bovine GLUT5 crystal structures (outward- and inward-open)
  confirm the MFS fold and a fructose-selective binding cavity [Nomura et al. 2015
  Nature, PMID:26416735 — not cited as supporting_text; used for background].

## Localization

- Plasma membrane, multiple independent experimental lines (immunofluorescence,
  oocyte/fibroblast surface expression, HPA): EXP/IDA [PMID:1695905, PMID:7619085,
  PMID:8333543, PMID:28083649, GO_REF:0000052 HPA]. ACCEPT.
- Apical/brush-border membrane of jejunal enterocytes is the primary functional
  location (UniProt: "Localized on the apical membrane of jejunum villi, but also
  on lateral plasma membranes of the villi"; By similarity to mouse Q9WV38). GLUT5
  is also present on the basolateral membrane of human jejunum [PMID:7619085].
- Sarcolemma (muscle PM) and specific-granule membrane (neutrophil) are peripheral,
  low-expression/By-similarity/Reactome-sourced locations → non-core.
- Extracellular exosome (HDA, urinary/prostatic secretion proteomics) — typical for
  a membrane protein; non-core.

## Physiology (mouse ortholog Q9WV38, By similarity)

GLUT5 is required for intestinal fructose absorption; its loss causes fructose
malabsorption. Mouse studies link GLUT5 to dietary-fructose-induced salt
reabsorption and hypertension — the basis for the "response to fructose",
"cellular response to fructose stimulus", and "regulation of systemic arterial
blood pressure mediated by a chemical signal" annotations (ISS/IEA from Q9WV38).
These are genuine but downstream/systemic physiological roles, not the core
molecular function → KEEP_AS_NON_CORE.

## Annotation-review decisions (summary)

- Core MF: **GO:0005353 fructose transmembrane transporter activity** (IBA+IDA×3+
  IEA+TAS×2) → ACCEPT. The IBA node PTN000627437 carries P22732 in its own
  WITH/FROM (experimental grounding on the target). GO:0070061 fructose binding
  (ISS) → KEEP_AS_NON_CORE (supported by curated D-fructose BINDING-site features).
- Core BP: **GO:0015755 fructose transmembrane transport** + **GO:1990539 fructose
  import across plasma membrane** + **GO:0106001 intestinal hexose absorption**
  (Reactome TAS) → ACCEPT.
- Glucose terms are cross-paralog over-propagation from the broad GLUT node
  (PTN008599990, the class I GLUT1-4 node) and the superseded 1990 "glucose
  carrier" description: GO:0055056 D-glucose transmembrane transporter activity
  (IBA+TAS), GO:0098708 D-glucose import across plasma membrane (IBA),
  GO:1904659 D-glucose transmembrane transport (TAS) → MARK_AS_OVER_ANNOTATED
  (real but low/negligible glucose activity; dedicated GLUT1-4 exist).
  GO:0070837 dehydroascorbic acid transport (IBA, same class-I node) → GLUT5 is
  not a DHA transporter (that is GLUT1/3/4) → MARK_AS_OVER_ANNOTATED.
- GO:0005975 carbohydrate metabolic process (TAS) → MARK_AS_OVER_ANNOTATED: GLUT5
  is a facilitative transporter and catalyses no metabolic step.
- GO:0016020 membrane (IEA) → MODIFY → GO:0005886 plasma membrane.
- Root transporter terms entailed by the accepted fructose activity:
  GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane
  transport → TOO_GENERAL.
- GO:0005515 protein binding ×12 (HuRI Y2H, SLC interactome; IPI) → REMOVE per
  protein-binding policy (uninformative; interactions not false, just not a
  function). Interactors: ARL13B(Q3SXY8), ATP6V0B(Q99437), COMT(P21964),
  EVI2B(P34910-2), FCRL3(Q96P31-6), MGST3(O14880), MTERF3(Q96E29), PAGE1(O75459),
  SCN3B(Q9NY72), TMEM130(Q8N3G9), TMEM237(Q96Q45-2).

ISS donor P22732 cross-references: Q9WV38 (mouse Slc2a5 ortholog) and P43427
(UniProt ISS donor used for sarcolemma + fructose binding).
