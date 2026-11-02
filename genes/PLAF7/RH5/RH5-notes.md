# RH5 (PfRH5, Q8IFM5, PF3D7_0424100) — curation notes

**Provenance note:** automated deep research was *not available* in this environment
(Falcon authentication failed; the OpenAI key was invalid). No `-deep-research-*.md`
file was generated. What follows is a **manual literature review** compiled from the
UniProt record (`RH5-uniprot.txt`), the cached publications in `publications/`, and GO
term definitions checked against OLS. Quotes are verbatim from the cited cached source.

## 1. Identity and architecture

- Reticulocyte-binding protein homolog 5, 526 aa precursor, signal peptide 1–24, chain
  25–526; no transmembrane domain and no GPI anchor (UniProt Q8IFM5; `KW   Signal`,
  `FT   SIGNAL          1..24`).
- An atypical member of the PfRh (reticulocyte-binding-like homolog) family: much
  smaller than the other members and lacking the C-terminal TM/cytoplasmic region
  [PMID:19000690 "This protein is an atypical PfRh family member, being much smaller
  than others and lacking a transmembrane and cytosolic region at the C-terminus."].
  Pfam PF18515 (Rh5); the fold is a kite-shaped, largely helical structure solved to
  2.18 Å [PMID:25296023 "In this study, we have determined the crystal structure of PfRh5
  using diffraction data to 2.18 Å resolution."].
- Proteolytically processed: cleaved at 140/141 to a ~45 kDa form during invasion
  (UniProt PTM; PMID:21909261, PMID:28186186).

## 2. Expression and localization

- Blood-stage specific: schizonts and free merozoites (UniProt DEVELOPMENTAL STAGE,
  at protein level).
- Stored in the **rhoptries** (a genuine apicomplexan secretory organelle, not a
  generic vesicle) of developing merozoites, shown by IFA against a rhoptry marker and
  by immuno-EM [PMID:18827878 "Thus, like the other RH ligands, PfRH5 is localized
  within the rhoptries, strongly suggesting a role in merozoite invasion."].
- Released at invasion and found at the merozoite–erythrocyte interface, and shed into
  the medium [PMID:21909261 "The PfRipr protein localises to the apical end of the
  merozoites in micronemes whilst PfRh5 is contained within rhoptries and both are
  released during invasion when they form a complex that is shed into the culture
  supernatant."].
- Colocalizes with CyRPA and PfRipr at the junction with the host cell
  [PMID:27374406 "Super-resolution microscopy revealed that PfRipr, CyRPA, and PfRh5
  colocalize at the junction between merozoites and erythrocytes during invasion."].
- The complex inserts into the host membrane [PMID:30542156 "this binding occurs through
  the insertion of Rh5 and Ripr into host membranes as a complex with high molecular
  weight."].

**Protist-specific caution.** The invasion literature calls the merozoite–erythrocyte
interface a "tight junction" (the apicomplexan *moving junction*). This is **not** the
metazoan occluding junction that `GO:0005923 bicellular tight junction` describes
("An occluding cell-cell junction that is composed of a branching network of sealing
strands that completely encircles the apical end of each cell in an epithelial sheet",
OLS). The GOA row carrying `GO:0005923` for RH5 is an animal-specific term imported on
the strength of that shared word. The underlying IDA observation is nevertheless real, so
the row is reviewed as MODIFY to a proposed new `moving junction` term (parent
`GO:0030054 cell junction`, confirmed in OLS as "a specialized region of connection
between two or more cells"), matching the term proposed in the PLAF7 AMA1 review, rather
than as REMOVE, which would discard a genuine localisation.

## 3. Molecular function: host receptor binding

- The host receptor is **basigin (BSG/CD147, Ok blood group antigen)**
  [PMID:22080952 "By systematically screening a library of erythrocyte proteins, we have
  found that the Ok blood group antigen, basigin, is a receptor for PfRh5, a parasite
  ligand that is essential for blood stage growth."]. Invasion is blocked by soluble
  BSG, BSG knockdown and anti-BSG antibodies across all strains tested
  [PMID:22080952 "Erythrocyte invasion was potently inhibited by soluble basigin or by
  basigin knockdown, and invasion could be completely blocked using low concentrations of
  anti-basigin antibodies; importantly, these effects were observed across all
  laboratory-adapted and field strains tested."].
- The RH5–BSG interaction is a **host-tropism determinant**: PfRH5 binds chimpanzee BSG
  weakly and gorilla BSG not at all [PMID:24297912 "we next investigated the contribution
  of the recently discovered Reticulocyte-binding protein Homolog 5 (RH5)-Basigin (BSG)
  interaction in host-species selectivity and found that P. falciparum RH5 bound
  chimpanzee BSG with a significantly lower affinity than human BSG and did not bind
  gorilla BSG, mirroring the known host tropism of P. falciparum."] — this is the basis
  for the IPI rows with the *Pan troglodytes* BSG accession A0A0M5L610, which are
  cross-species binding measurements, not an assertion that RH5 acts in chimpanzees.
- Earlier work, before BSG was identified, reported binding to an unknown glycosylated
  erythrocyte receptor [PMID:19000690 "called PfRh5, which binds to an unknown class of
  glycosylated receptors on the erythrocyte surface."].

## 4. The RH5–CyRPA–PfRipr invasion complex and its membrane tether

- PfRipr (O97302, PF3D7_0323400) forms a complex with PfRh5 [PMID:21909261 "The
  PfRh5/PfRipr complex was stably purified by ion-exchange chromatography and 350 mM NaCl
  in the elution buffer did not disrupt their association, suggesting the tight
  interaction of two proteins."].
- CyRPA (Q8IFM8, PF3D7_0423800) is the GPI-linked member that holds the trimer together
  [PMID:25583518 "Here we have identified a conserved GPI-linked parasite protein,
  Cysteine-rich protective antigen (CyRPA) as an interacting partner of PfRH5-PfRipr that
  tethers the PfRH5/PfRipr/CyRPA multiprotein complex on the merozoite surface."]; a
  direct CyRPA–PfRh5 contact is demonstrated biochemically [PMID:28195530 "We show CyRPA
  interacts directly with PfRh5."] and structurally [PMID:30542156 "Our structure
  identifies blades 4-6 of the β-propeller of CyRPA as contact sites for Rh5 and Ripr."].
- P113 (Q8ILP3) binds the RH5 N-terminus and anchors it to the merozoite surface
  [PMID:28186186 "Here we use a sensitive assay that detects interactions between
  recombinant proteins to show that the glycosylphosphatidylinositol (GPI)-linked protein
  P113 interacts directly with the N terminus of unprocessed RH5, providing a mechanism by
  which the RH5 invasion complex is tethered to the merozoite surface."], a releasable
  tether [PMID:28186186 "we establish the binding interdependencies of all the other known
  RH5 complex components and conclude that the RH5Nt-P113 interaction provides a releasable
  mechanism for anchoring RH5 to the merozoite surface."].
- GO has no term for this complex; a `proposed_new_terms` entry is made for it.

## 5. Biological process: erythrocyte invasion, and what RH5 itself does

- RH5 is the only essential member of the PfRh family: all other *dbl*/*rbl* genes can be
  knocked out [PMID:24212193 "The function of the DBL and RBL proteins are redundant
  because knockout strains of all of the dbl and rbl genes except for PfRH5 have been
  generated and show insignificant loss of invasion efficiency7."].
- RH5 is needed for *irreversible* attachment, not for initial contact
  [PMID:28195038 "While merozoites deficient in PfCyRPA or PfRH5 can still bind to
  erythrocytes, they do not attach irreversibly and cannot invade the host cells (Volz et
  al., 2016)."] — i.e. the gene genuinely participates in adhesion as well as entry.
- Downstream of binding, RH5–BSG engagement itself triggers a host Ca²⁺ signal and
  cytoskeletal remodelling [PMID:28409866 "We show that RH5-Basigin interaction on its own
  triggers a Ca2+ signal in the RBC resulting in changes in RBC cytoskeletal proteins
  phosphorylation and overall alterations in RBC cytoskeleton architecture."], and the
  complex is required for Ca²⁺ release and junction formation [PMID:27374406 "PfRipr,
  CyRPA, and PfRipr/CyRPA/PfRh5-basigin complex is required for triggering the Ca(2+)
  release and establishing the tight junction."]. This is RH5 acting *on the host*: the
  appropriate framing is a symbiont-mediated activation of host signalling via agonism of
  a host cell-surface receptor (`GO:0141134`, verified in OLS), not a parasite-intrinsic
  signalling process. Note the mechanism is still described cautiously in the field
  [PMID:31204103 "Although the precise function of PfRH5 is not known, it is linked to
  calcium influx into the erythrocyte, followed by cytoskeleton remodeling and is necessary
  for establishing a tight junction between parasites and RBCs (Weiss et al., 2015, Volz et
  al., 2016)."].

**Host-vs-symbiont term use.** Every process claim here is written from the parasite's
side: `GO:0085017 entry into host cell by a symbiont-containing vacuole` (the specific
term), `GO:0044650 adhesion of symbiont to host cell`, `GO:0141134` for the action on host
signalling. The broader `GO:0044409 symbiont entry into host` rows, and the intermediate
`GO:0046718 symbiont entry into host cell` rows the gene already carries, are correct but
less specific than the evidence supports, so all are MODIFYed to `GO:0085017`. OLS
confirms `GO:0085017` is a descendant of both, and its definition is invasion that forms
"a vacuole in which the symbiont resides", beginning with attachment to a host membrane
that invaginates and closing when the host membrane seals behind the new vacuole -- i.e.
exactly moving-junction merozoite invasion and formation of the parasitophorous vacuole.
`GO:0046718` is instead framed around breaching the membrane and releasing the symbiont or
its genome into the cytoplasm (its definition still carries a virus-specific comment), so
it is a poorer fit. `GO:0085017` is also what GOA itself uses for the other P. falciparum
invasion proteins in this project (MSP1 by IDA, CSP by IMP), so this aligns RH5 with
MSP1, CSP and MIC2. Locations
are likewise split correctly between parasite-side (`GO:0005576`, `GO:0020008`,
`GO:0034591`) and host-side (`GO:0043655`, `GO:0020002`) terms; note that
`GO:0043655 host extracellular region` sits under `GO:0018995 host cellular component`
(checked in OLS), *not* under `GO:0005576`, so the two are independent claims and both are
retained.

## 6. Heparin binding

PfRH5 binds heparin with very high affinity in a pull-down/elution assay
[PMID:24212193 "Two of these proteins, BAEBL and PfRH5, were eluted incompletely by 10
mg/mL heparin, suggesting that they have an extremely high affinity for heparin."], and
heparin disrupts its erythrocyte binding [PMID:24212193 "Erythrocyte binding of some
parasite ligands, including full-length MSP1, the C-terminal 42-kDa fragment of MSP1
(MSP1–42), and PfRH5 is disrupted by heparin101123, raising the possibility that
heparin-induced inhibition of the binding of multiple ligands results in invasion
inhibition."]. The observation is real, but heparin/heparan sulfate is not a mature
erythrocyte surface component, so this is treated as a genuine but non-core *in vitro*
binding property (likely reflecting the basic surface that also engages BSG), not as the
physiological ligand interaction. Kept, marked non-core.

## 7. Vaccine relevance (context only, not annotated)

RH5 is the leading blood-stage vaccine target; antibodies neutralize invasion
[PMID:31204103 "We isolated a panel of human monoclonal antibodies (mAbs) against PfRH5
from peripheral blood B cells from vaccinees in the first clinical trial of a PfRH5-based
vaccine."], and engineered stabilized variants exist [PMID:28096331]. Vaccine candidacy is
not itself a GO-annotatable function and is recorded here only as context.

## 8. Curation decisions taken (summary)

- `GO:0005923 bicellular tight junction` → MODIFY to a proposed `moving junction` term
  (animal epithelial term; the merozoite "tight junction" is the apicomplexan moving
  junction, but the IDA localisation itself stands).
- `GO:0044409 symbiont entry into host` (9 rows) and `GO:0046718 symbiont entry into host
  cell` (2 EXP rows) → MODIFY to `GO:0085017 entry into host cell by a symbiont-containing
  vacuole`, the descendant that describes vacuole-mediated apicomplexan invasion and the
  term GOA uses for MSP1 and CSP.
- `GO:0033644 host cell membrane` → MODIFY to `GO:0020002 host cell plasma membrane`
  (the gene already carries the descendant with EXP evidence).
- `GO:0005515 protein binding` rows naming basigin → MODIFY to `GO:0046789 host cell
  surface receptor binding`; rows naming the parasite partners CyRPA, PfRipr and P113 →
  REMOVE. The interactions are real and specific, but the bare term carries no functional
  information and, the partners being parasite proteins, there is no informative MF child
  to refine to. What those rows encode — RH5's place in the trimeric invasion complex — is
  carried instead by the proposed complex term below and by the core functions, so nothing
  is lost. (Repo policy: a protein-binding row is either MODIFYed or REMOVEd, never kept.)
- `GO:0032991 protein-containing complex` → MODIFY to a proposed new term for the
  RH5–CyRPA–PfRipr invasion complex.
- `GO:0008201 heparin binding` → kept, non-core (see §6).
- One `NEW` process annotation, `GO:0141134`, for the RH5→basigin agonism that triggers
  host Ca²⁺ signalling (§5). Participation test: RH5 itself performs the receptor-binding
  step that activates the pathway, and two independent studies attribute the trigger to
  the RH5–BSG interaction specifically.
