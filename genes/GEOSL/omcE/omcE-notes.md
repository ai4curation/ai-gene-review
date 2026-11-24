# omcE (GSU0618, UniProt Q74FJ0) — Geobacter sulfurreducens PCA

## Starting point

- Q74FJ0 is **unreviewed (TrEMBL)**, SubName "Cytochrome c", 232 aa, SignalP signal
  peptide 1-23, mature chain 24-232. No transmembrane feature, no lipid anchor.
- **Four CXXCH motifs**, at precursor positions 51, 103, 201 and 226 — a tetraheme
  cytochrome, matching the structure paper's "tetrahaem packing". Pfam PF09699
  ("Doubled CXXCH motif", IPR010177 Paired_CXXCH_1) covers 200-232, i.e. the last two.
- One structure: **PDB 7TFS**, cryo-EM at 4.30 Å, chain A = 1-232, from PMID:35798889.
- **GOA is empty** (`omcE-goa.tsv` is header only, checked 2026-11-10). Every row in the
  review is therefore `NEW`.
- No provider deep-research file; literature assembled by hand.

## Classification — the third variation on the same problem

| | PANTHER | InterPro family | CDD | TCDB |
|---|---|---|---|---|
| OmcS (Q74A86) | PTHR30333:SF1 "…NAPC" | IPR051174 (= the PANTHER family) | **cd21555 "C-type cytochrome OmcS and similar proteins"** | **5.B.3.1.1 G-NET** |
| **OmcE (Q74FJ0)** | **PTHR35038 "DISSIMILATORY SULFITE REDUCTASE SIRA" : SF6 "SURFACE LOCALIZED DECAHEME CYTOCHROME C LIPOPROTEIN"** | IPR010177 (a paired-CXXCH *domain*, not a family) | none | none |
| OmcZ (Q74BG5) | none | Ig-like + multiheme superfamily, both on the cleaved-off C-terminus | none | none |

OmcE's placement is the worst of the three. The family is named for a dissimilatory
sulfite reductase; the subfamily is named for a **decaheme lipoprotein**, and OmcE is a
**tetraheme** cytochrome with no lipid anchor. `PTHR35038-entries.csv` shows SF6 also
holds MtrA (P0DSN3, decaheme, periplasmic) and a hydroxylamine oxidoreductase (Q1PX48,
octaheme enzyme); the wider family mixes in NrfB (SF5), OmcC (SF8), photosynthetic
reaction-centre cytochrome c subunits and a perchlorate reductase gamma subunit. This
family looks at least as heterogeneous as PTHR30333 and is a clear candidate for its own
family review; it is not reviewed here.

PAINT for PTHR35038 carries a single IBD, `PTN002858933` / `GO:0016491` oxidoreductase
activity, seeded by NrfB (P0ABL1) and Q8EJI6, with no taxon recorded. **OmcE receives no
IBA from it** — consistent with the empty GOA.

## Biology, with provenance

### Identity and structure
- OmcE was found alongside OmcS among proteins sheared from the cell surface, at about
  30 kDa, and predicted then to be a tetraheme outer-membrane cytochrome
  [PMID:16332857 "The other abundant c-type cytochrome sheared from the outer surface of G. sulfurreducens, designated OmcE, has a molecular mass of ca. 30 kDa and is predicted to be an outer membrane tetraheme c-type cytochrome."].
- The 2022 cryo-EM structure showed OmcE is a second, thinner filament
  [PMID:35798889 "Here we report that G. sulfurreducens also produces a second, thinner appendage comprised of cytochrome OmcE subunits and solve its structure using cryo-electron microscopy at ~4.3 Å resolution."],
  about 40 Å across versus about 50 Å for OmcS.
- The convergence result is the interesting one: OmcE and OmcS share no sequence or
  backbone similarity, yet their polymerised heme arrangements match, including a heme in
  one subunit coordinated by a histidine from the next
  [PMID:35798889 "Although OmcE and OmcS subunits have no overall sequence or structural similarities, upon polymerization both form filaments that share a conserved haem packing arrangement in which haems are coordinated by histidines in adjacent subunits."].
  The authors call that cross-subunit coordination unique among c-type cytochrome
  structures solved to date, and generalise it into a proposal that conductive bacterial
  appendages form a class defined by heme packing rather than homology
  [PMID:35798889 "We propose that there is a broad class of conductive bacterial appendages with conserved haem packing (rather than sequence homology) that enable long-distance electron transport to chemicals or other microbial cells."].
- **Caveat that must not be dropped:** the filaments were enriched from *omcS-mutant*
  strains, not from wild type
  [PMID:35798889 "We constructed G. sulfurreducens strains containing three different omcS mutations, that were intended to alter the electronic structure of heme chains within OmcS, but a serendipitous outcome was that these omcS mutations resulted in an enrichment of extracellular OmcE filaments."],
  and the authors read this as compensation
  [PMID:35798889 "This suggested to us that cells were compensating for a partial or complete loss of function in OmcS by expressing a different cytochrome filament"].
  So OmcE demonstrably polymerises, but how much filament a wild-type cell makes, and
  whether that matters physiologically, is open.
- Extra surface densities are **hypothesised** to be glycans, not demonstrated
  [PMID:35798889 "Unlike OmcS, OmcE filaments have readily apparent multiple additional densities on the filament surface due to post-translational modifications, which we hypothesize are glycosylations"],
  with candidate sites S83, N86, N87, N132, T184 and a 17-gene glycosyltransferase cluster
  downstream of omcE. Note that the sequence contains **no N-X-S/T sequon at all**, so any
  N-linked modification would be non-canonical; S83 and T184 would be O-linked. No
  glycosylation annotation is made.

### Function
- Deleting omcE abolishes Fe(III) oxide reduction while leaving soluble acceptors intact,
  and complementation restores it
  [PMID:16332857 "When either omcS or omcE was deleted, G. sulfurreducens could no longer reduce Fe(III) oxide but could still reduce soluble electron acceptors, including Fe(III) citrate."],
  [PMID:16332857 "Expressing omcS or omcE in trans restored the capacity for Fe(III) oxide reduction."].
- The phenotype is specific to insoluble iron. Deleting omcE does **not** affect current
  production on an anode
  [PMID:19461962 "Deletion of omcS, omcB, or omcE had no impact on maximum current production (Table 4)."],
  and a later systematic comparison found the same split
  [PMID:37881251 "Deletion of omcE also impaired bacterial ability to reduce ferrihydrite, but its impacts on the ability for anode reduction and the co-culture of G. metallireducens-G. sulfurreducens were minimal."].
  So of the three nanowire cytochromes, OmcZ owns the electrode, OmcS owns Fe(III) oxide
  and DIET, and OmcE is Fe(III)-oxide-specific and dispensable elsewhere.
- OmcE is the specific binding partner for the artificial mediator resorufin: the redox
  shift seen in biofilms disappears in an omcE mutant but not in omcS or omcZ mutants
  [PMID:39278116 "this shift was attenuated by the mutation of outer-membrane cytochrome gene omcE but not by omcS and omcZ mutation, indicating that RR specifically interacted with OmcE"],
  and heterologously expressed OmcE monomers bind resorufin with Kd 720 nM
  [PMID:39278116 "By using heterologously expressed OmcE monomers in Escherichia coli, it was found that RR bonded with OmcE monomers with a moderate intensity (dissociation constant of 720 nM)"],
  apparently at heme II.

### What has *not* been measured
No one has purified OmcE and shown it reducing an acceptor, the way Qian did for OmcS.
Wang et al. did not measure OmcE filament conductivity either; they inferred similar
electron transport from the matching inter-heme distances, and warned that
"measures of conductivity attributed to a specific protein need to be treated with some caution"
[PMID:35798889]. This is why the molecular-function row below is `IC` rather than `IDA`.

## Annotation decisions

All rows are NEW (GOA is empty).
- `GO:0020037` heme binding — **IDA**. Four CXXCH motifs, bis-His coordination resolved in
  7TFS, UniProt BINDING features from the structure.
- `GO:0009055` electron transfer activity — **IC**. Authored inference, justified by the
  stacked bis-His heme chain in the structure, the Fe(III)-oxide phenotype, and the
  resorufin binding at a heme. Flagged explicitly because no direct transfer assay exists.
- `GO:0019645` anaerobic electron transport chain — **IMP**. Deletion plus complementation.
- `GO:0051258` protein polymerization — **IDA**, with the omcS-mutant caveat in the reason.
- `GO:0009986` cell surface — **IDA**. Sheared from the outer surface of intact cells;
  filaments are extracellular.

Not added:
- `GO:0009279` cell outer membrane. Same reasoning as the OmcS review, where the four
  existing rows were marked over-annotated: no transmembrane segment, no lipid anchor,
  recovered by shearing. Here there is no existing row to judge, so the term is simply not
  proposed.
- `GO:0016722` oxidoreductase activity, acting on metal ions — nothing has been assayed on
  purified OmcE at all.
- Any glycosylation term — the modification is hypothesised, unidentified, and the protein
  has no N-glycosylation sequon.
