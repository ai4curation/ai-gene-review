# MtrC (SO_1778, UniProtKB:Q8EG34) — review notes

Research done by hand (no deep-research provider available in this environment; no
`-deep-research-<provider>.md` file was created). All assertions below carry provenance.

## Identity and nomenclature

- UniProt entry is TrEMBL (Q8EG34_SHEON), name taken from the EMBL submission
  AAN54831.1: "Extracellular iron oxide respiratory system surface decaheme cytochrome
  c component MtrC", gene `mtrC`, locus `SO_1778`. Protein existence is "Evidence at
  protein level" and there are seven PDB entries (4LM8, 7O7G, 7QTH, 8QBQ, 8QBZ, 8QC9,
  9EOV).
- **Nomenclature trap.** In the Myers & Myers literature SO_1778 is called *OmcB*, not
  MtrC [PMID:11133454 "OMCA1 and OMCB1 were 45 and 75% slower than MR-1, respectively,
  at reducing MnO(2)"], and the Fur modulon paper uses the same naming
  [PMID:15576789 "omcA (SO1779; 5.9- and 4.8-fold), omcB (SO1778; 5.3- and 4-fold)"].
  Any claim quoted from those papers about "OmcB" is about this gene. Conversely,
  `omcB` in *Geobacter* is a different protein.
- Features on the entry that the review relies on: SignalP signal peptide 1..21, lipobox
  with LIPID 25 (N-palmitoyl / S-diacylglycerol cysteine, PROSITE-ProRule PRU00303),
  ten heme c BINDING sites and several Ca(2+) sites from the crystal structures, and
  `DISULFID 444..453` — which is the CX8C pair described in PMID:26126857.

## What the evidence supports

- Decaheme cytochrome: ten hemes counted in purified protein [PMID:16788180 "Each
  purified cytochrome was confirmed to contain 10 hemes and exhibited Fe(III)-NTA
  reductase activity."] and resolved in the 1.8 Å structure [PMID:26126857 "The 1.8 Å
  x-ray crystal structure of the decaheme MtrC revealed a highly conserved CX8C
  disulfide"].
- Metal reductase: Fe(III)-NTA (above), U(VI) [PMID:16875436 "the outer membrane (OM)
  decaheme cytochrome MtrC (metal reduction), previously implicated in Mn(IV) and
  Fe(III) reduction, directly transferred electrons to U(VI)"], Cr(VI) with kinetics
  [PMID:21498755 "purified MtrC and OmcA reduced Cr(VI) with apparent k(cat) values of
  1.2 ± 0.2 (mean ± standard deviation) and 10.2 ± 1 s(-1)"].
- Conduit subunit: [PMID:20018742 "demonstrate its capacity to move electrons across a
  lipid bilayer after incorporation into proteoliposomes"]; stoichiometry
  [PMID:17675441 "We show for the first time that MtrC, MtrA, and MtrB form a 198-kDa
  complex with a 1:1:1 stoichiometry."].
- Surface location: [PMID:18502849 "MtrC and OmcA are cell surface-exposed lipoproteins
  important for reducing solid metal oxides."].
- Partner binding with OmcA: [PMID:16788180 "Upon titration with OmcA, there was a
  marked increase in fluorescence polarization indicating the formation of a
  high-affinity protein complex"]. Not annotated here as `protein binding`
  (uninformative per the repository policy); it is used as evidence for the electron
  transfer role instead.

## Annotation decisions

GOA has exactly one row for this protein: `GO:0016491 oxidoreductase activity` (IBA,
GO_REF:0000033, node PTN002858933 of PTHR35038, seeded by E. coli NrfB P0ABL1 and
S. oneidensis MccA/SirA Q8EJI6). PAINT data was fetched with
`just fetch-panther-paint PTHR35038`; the IBD row is in
`interpro/panther/PTHR35038/PTHR35038-paint.tsv`.

- MODIFY the IBA to `GO:0016722 oxidoreductase activity, acting on metal ions`: the node
  placement is right, the term is simply generic because the family's characterized
  members reduce sulfite and nitrite rather than metals.
- Four NEW rows, each from direct experiment on this protein: heme binding
  (GO:0020037), electron transfer activity (GO:0009055), external side of cell outer
  membrane (GO:0031240), anaerobic electron transport chain (GO:0019645).
- No `NEW` term was proposed for Cr/U/Mn reduction specifically: GO has no term for
  terminal reduction of an extracellular or insoluble acceptor, and inventing one was
  not warranted here. It is raised as a `suggested_questions` entry instead.

## Relation to the CMMMech records

CMMMech cites UniProtKB:Q8EG34 in `data/records/{selenium,uranium,uraninite,chromium,
vanadium,silver,rhodochrosite,nontronite,montmorillonite,chlorite}.yaml`, with
`functional_role` text such as "terminal extracellular electron-transfer reductase
during anaerobic metal reduction".

Where that is stronger than the evidence this review found (CMMMech was not edited):

- **Silver, vanadium, rhodochrosite, nontronite, montmorillonite, chlorite.** The
  records mark `supports: partial` and say so explicitly ("individual cytochrome genes
  were not mutated"), which matches what is published: MtrC is a *representative*
  pathway component for those systems, with no MtrC-specific assay or mutant. The
  evidence found here supports Fe(III), Mn(IV), U(VI) and Cr(VI) only.
- **Selenium** (`supports: partial`): the record is careful — MtrC is listed as
  "evaluated as an outer-membrane" component alongside FccA and CymA. Published
  selenite reduction in MR-1 is attributed mainly to the periplasmic FccA route, so an
  MtrC selenite-reductase claim would not be supported.
- **Chromium and uraninite/uranium** (`supports: support`): this is the best-grounded
  of the set. Both the purified-protein kinetics and the deletion phenotypes exist
  (PMID:21498755, PMID:16875436), so the records' claims are proportionate, with the
  caveat that U(VI) evidence is a rate effect plus colocalization rather than
  Michaelis-Menten kinetics on purified MtrC.
- None of the records implies industrial performance for this protein, and nothing in
  this review would support such a claim.

## Not done

- `just fetch-fitness SHEON mtrC` fails in this environment (no local FEBA database and
  fit.genomics.lbl.gov unreachable), so no RB-TnSeq fitness evidence was used.
- No GO-CAM model covers the Mtr pathway in `gocams/index.tsv` for this accession.
