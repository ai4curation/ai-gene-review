# TEX264 (Q9Y6I9) — curation notes

Gene: human `TEX264` (testis-expressed protein 264; legacy alias `ZSIG11`,
"putative secreted protein Zsig11"). UniProt Q9Y6I9, 313 aa, PANTHER
`PTHR15949` ("TESTIS-EXPRESSED PROTEIN 264"), InterPro `IPR011256`
(regulatory-factor effector-binding domain superfamily, i.e. the GyrI-like fold).

**Provenance note.** No deep-research provider was reachable in the environment
this review was prepared in (`just deep-research-*` failed with "Not logged in"
for every configured provider). Per `CLAUDE.md` this file therefore holds the
reviewer's own synthesis rather than a `-deep-research-<provider>.md` file; every
assertion below is sourced to a cached publication or to the fetched UniProt
record. A provider research file can be generated later without invalidating
anything here.

## 1. What TEX264 is

A small single-pass ER membrane protein with an unusual domain layout: a short
lumenal N-terminus, one transmembrane signal-anchor, and then the entire rest of
the protein in the cytosol.

UniProt feature table (`file:human/TEX264/TEX264-uniprot.txt`):

- `TOPO_DOM 1..6 /note="Lumenal"` (evidence `ECO:0000269|PubMed:31006538`)
- `TRANSMEM 7..31 /note="Helical; Signal-anchor for type III membrane protein"`
- `TOPO_DOM 32..313 /note="Cytoplasmic"`
- `REGION 193..313 /note="Disordered"`
- `MOTIF 273..276 /note="LIR motif"`
- `MUTAGEN 273 F->A: Completely abolishes the interaction with LC3B.`
- `MUTAGEN 276 L->A: Completely abolishes the interaction with LC3B.`

So only six residues face the ER lumen; the GyrI-like domain, the long
intrinsically disordered region and the LIR motif are all cytosolic. An et al.
describe the same architecture: TEX264 "contains an N-terminal hydrophobic
segment and a cytosolic gyrase inhibitor (Gyrl)-like domain followed by an
unstructured C-terminal region" [PMID:31006537]. Fielden et al. call the
N-terminal hydrophobic segment an "LRR" but agree it is the membrane tether:
"A recent study demonstrated that the N-terminal LRR of TEX264 is a
transmembrane segment that tethers it to the membrane of the ER" [PMID:32152270].

This topology matters for two annotation judgements made below: it is what makes
a *lumenal* / secreted localization for TEX264 implausible, and it is why the
LIR can engage ATG8 proteins on a cytosolic phagophore membrane.

## 2. Function 1 — major ER-phagy (reticulophagy) receptor

Two back-to-back 2019 *Molecular Cell* papers independently identified TEX264 as
an ER-phagy receptor.

**Chino et al.** [PMID:31006538, abstract only in cache]:

- "we performed a differential interactome screen using wild-type LC3B and a LIR
  recognition-deficient mutant and identified TEX264 as a receptor for
  autophagic degradation of the endoplasmic reticulum (ER-phagy)"
- "TEX264 is an ER protein with a single transmembrane domain and a LIR motif."
- "TEX264 interacts with LC3 and GABARAP family proteins more efficiently and is
  expressed more ubiquitously than previously known ER-phagy receptors."
- "ER-phagy is profoundly blocked by deletion of TEX264 alone and almost
  completely by additional deletion of FAM134B and CCPG1."
- "A long intrinsically disordered region of TEX264 is required for its ER-phagy
  receptor function to bridge the gap between the ER and autophagosomal
  membranes independently of its amino acid sequence."

**An et al.** [PMID:31006537, full text in cache]:

- "TEX264 uses an LC3-interacting region (LIR) to traffic into ATG8-positive
  puncta that often initiate from three-way ER tubule junctions and subsequently
  fuse with lysosomes."
- "Global proteomics and ER-phagy flux analysis revealed the stabilization of a
  cohort of ER proteins in TEX264-/- cells during nutrient stress."
- "This work reveals TEX264 as an unrecognized ER-phagy receptor that acts
  independently of other candidate ER-phagy receptors to remodel the ER during
  nutrient stress."
- trafficking kinetics: "in COS7 cells, TEX264 trafficking from the ER to
  autophagosomes and subsequent fusion with a lysosome can occur on the order of
  ~15 min."

UniProt's curated FUNCTION paragraph synthesises both and adds the mechanistic
model: the ATG8-containing isolation membrane cradles a tubular segment of
TEX264-positive ER near a three-way junction, "allowing the formation of a
synapse of 2 juxtaposed membranes with trans interaction between the TEX264 and
ATG8 proteins".

**Molecular function.** This is cargo-receptor/adaptor activity, not signal
transduction: the protein holds ER membrane (the cargo) against a phagophore by
binding ATG8-family proteins through its LIR, with the IDR acting as a spacer.
`GO:0160247` autophagy cargo adaptor activity ("the binding activity of a
molecule that brings together a cargo, targeted for degradation via autophagy,
to a phagophore") is the fitting term, and is already used this way for
CALCOCO1 in this repository. The `GO:0038023` signaling receptor activity rows
that MGI made from PMID:31006538 are a label-level mismatch — `GO:0038024`
cargo receptor activity carries the explicit note that signal-transduction
receptors are the ones that belong under `GO:0038023`. Recorded below as a
`WRONG_TERM` source defect against MGI.

**Partners.** ATG8-family binding is the functional interaction: MAP1LC3A,
MAP1LC3B, GABARAP, GABARAPL1 per UniProt SUBUNIT ("Interacts (via the LIR motif)
with ATG8 family proteins MAP1LC3A, MAP1LC3B, GABARAP and GABARAPL1"), plus a
GABARAPL2 (P60520) proximity interaction from the macroautophagy proximity
interactome [PMID:34524948].

## 3. Function 2 — TOP1cc / DNA-protein crosslink repair adaptor

A nuclear pool of TEX264 does something unrelated to autophagy: it is the p97
cofactor that targets p97 and SPRTN to trapped topoisomerase-1 cleavage
complexes (TOP1ccs). Fielden et al. [PMID:32152270, full text in cache]:

- "we find that TEX264 fulfils this role by forming a complex with the p97 ATPase
  and the SPRTN metalloprotease"
- "We show that TEX264 recognises both unmodified and SUMO1-modifed TOP1 and
  initiates TOP1cc repair by recruiting p97 and SPRTN."
- direct bridging, reconstituted in vitro: "This demonstrates that TEX264 can
  simultaneously bind both p97 and TOP1 and, thus, physically bridge p97 to
  TOP1."
- the bridge is required in cells: "Depletion of TEX264 strongly reduced the
  interaction between SPRTN and TOP1 without affecting total TOP1 levels or the
  interaction between SPRTN and p97 (Fig. 5a). This indicates that TEX264
  recruits p97–SPRTN sub-complexes to TOP1."
- the p97 contact is a SHP box: "a TEX264 variant lacking its putative SHP box
  (TEX264ΔSHP; amino acids 273–285), bound much less efficiently to p97 in
  vitro"
- the TOP1 contact is the GyrI-like surface: "Each variant displayed reduced
  binding to TOP1, but not p97, suggesting that they comprise a binding surface
  that enables TEX264 to bind TOP1"; the E194A point mutant "largely failed" to
  reverse TOP1cc accumulation
- SUMO1 binding via two SIMs: "We found that TEX264 bound to free SUMO1, but not
  SUMO2 (neither free SUMO2 nor poly-SUMO2 chains; Fig. 4d, Supplementary Fig.
  5D). Mutation of either of the putative SIMs strongly diminished SUMO1 binding"
- localization: "We found that TEX264 is present in the cytosol, nucleus, and on
  chromatin (Supplementary Fig. 2B)"; "TEX264 localises to the nuclear periphery,
  associates with DNA replication forks, and counteracts TOP1ccs during DNA
  replication."; "TEX264 was detected, along with p97 and SPRTN, at/near
  replication forks by iPOND"
- substrate scope is narrow: "we found that depletion of TEX264, unlike SPRTN,
  did not cause total DPCs to accumulate, suggesting that TEX264 may
  specifically promote SPRTN-dependent TOP1cc repair"

**Molecular function.** TEX264 does no chemistry here — p97 remodels and SPRTN
cleaves. It binds TOP1 (GyrI-like surface), p97 (SHP box) and SUMO1 (SIMs)
simultaneously, which is `GO:0030674` protein-macromolecule adaptor activity.
`GO:0032183` SUMO binding is separately and directly assayed, and is proposed as
a `NEW` row below.

The two functions are not obviously connected. Fielden et al. leave the question
open: "Whether TEX264’s role in autophagy is linked to the observations
presented here is an interesting line of future enquiry." They also note the
unresolved topological puzzle — a type III ER membrane protein should not reach
chromatin — and offer two possibilities: "There may otherwise be a mechanism of
releasing TEX264 from the nuclear envelope or alternative TEX264 isoforms which
lack the LRR." Deleting the tether does redistribute the protein: "When we
deleted this segment (TEX264ΔLRR; amino acids 1–33), TEX264 redistributed into
the cytoplasm as well as the nucleoplasm". No LRR-less isoform is listed in
Q9Y6I9, so this stays a genuine biological gap rather than a missing-isoform
source defect.

One in vitro DNA-binding result is reported but not pursued: "Like some other
GyrI-like proteins, recombinant TEX264 (purified without its LRR) binds DNA when
analysed by electrophoretic mobility shift assay (EMSA; Supplementary Fig. 7E)".
A single EMSA on a truncated recombinant protein of unknown in vivo relevance is
not enough to propose a DNA-binding MF, so no `NEW` row was added for it.

## 4. The Reactome platelet-granule rows

GOA carries two Reactome TAS rows from `Reactome:R-HSA-481007` ("Exocytosis of
platelet alpha granule contents"): `GO:0005576` extracellular region and
`GO:0031093` platelet alpha granule lumen. The cached Reactome entry holds only
the event summary, with no participant list, so the membership itself could not
be checked here.

Both are implausible for this protein on topology alone: with `TOPO_DOM 1..6
/note="Lumenal"` and everything from residue 32 cytosolic, TEX264 has no
secretable ectodomain and cannot be a soluble granule-lumen cargo. The likely
origin is the legacy identification of the gene as a secreted protein — UniProt
still carries `AltName: Full=Putative secreted protein Zsig11` from the secreted
protein discovery initiative [PMID:12975309], and flags the original deposit with
`SEQUENCE CAUTION ... Type=Erroneous initiation`. Marked over-annotated, with a
`SUSPECTED` / `CHECK` source defect to Reactome rather than a confident removal,
because the participant list could not be inspected.

## 5. IBA / PAINT rows

Six IBA rows come from `PTN002312623` (GO_REF:0000033): autophagosome membrane,
nucleus, replication fork, ER membrane, reticulophagy, protein-DNA covalent
cross-linking repair. All six match what the human protein was directly shown to
do, and the node's `WITH/FROM` lists `UniProtKB:Q9Y6I9` itself alongside a mouse
MGI gene — which is the expected marker of experimental grounding on the target
(the gene's own experimental annotations are among the descendant evidences the
PAINT curator used), not circularity. Accepted as made.

The two `GO_REF:0000107` Ensembl-Compara rows (autophagosome membrane, ER)
transfer from mouse `UniProtKB:E9Q137`; both restate claims the human protein
carries by IDA.

## 6. Core functions as reviewed

1. **ER-phagy receptor** — `GO:0160247` autophagy cargo adaptor activity, at the
   ER membrane (`GO:0005789`) and the autophagosome membrane (`GO:0000421`),
   driving `GO:0061709` reticulophagy.
2. **TOP1cc repair adaptor** — `GO:0030674` protein-macromolecule adaptor
   activity, in the nucleus (`GO:0005634`) at replication forks (`GO:0005657`),
   driving `GO:0106300` protein-DNA covalent cross-linking repair.

## 7. Open questions carried into the review

- Is the nuclear/TOP1cc pool the same molecules as the ER pool, and how do they
  get there (release from the inner nuclear membrane, or an untracked
  LRR-less form)?
- Does ER-phagy flux change TOP1cc repair capacity, or vice versa?
- What, if anything, does the lumenal six-residue N-terminus do?
- Why is TEX264 required for TOP1cc clearance but dispensable for bulk DPC
  clearance, given that SPRTN handles both?
