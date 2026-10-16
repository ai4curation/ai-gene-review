# LRRC8A (SWELL1) — review journal

UniProt: Q8IWT6. HGNC: LRRC8A. Synonyms: SWELL1, LRRC8, KIAA1437.

## 1. What the protein is

LRRC8A is a four-transmembrane protein with a large cytosolic leucine-rich-repeat (LRR)
domain. It is the **obligatory subunit** of the volume-regulated anion channel (VRAC, also
called VSOAC / I(Cl,swell)), a hexameric channel of the plasma membrane that opens on cell
swelling and on lowering of cytoplasmic ionic strength.

Founding genetic evidence (two independent screens, 2014):

- [PMID:24725410 "We identified SWELL1 (LRRC8A), a member of a four-transmembrane protein
  family with unknown function, as essential for hypotonicity-induced iodide influx."]
- [PMID:24725410 "SWELL1 is localized to the plasma membrane, and its knockdown
  dramatically reduces endogenous VRAC currents and regulatory cell volume decrease in
  various cell types."]
- [PMID:24725410 "point mutations in SWELL1 cause a significant change in VRAC anion
  selectivity, demonstrating that SWELL1 is an essential VRAC component"]
- [PMID:24790029 "Genomic disruption of LRRC8A ablated VRAC currents."]
- [PMID:24790029 "Cells with disruption of all five LRRC8 genes required LRRC8A
  cotransfection with other LRRC8 isoforms to reconstitute VRAC currents."]

The last quote is the key fact for the *subunit* question: in cells LRRC8A **alone** does
not reconstitute VRAC current — it must heteromerize with LRRC8B–E, and the isoform
combination sets inactivation kinetics and substrate preference
[PMID:24790029 "The isoform combination determined VRAC inactivation kinetics."].

Reconstitution and structure nuance the picture: purified LRRC8 complexes form
osmolality-gated anion channels in bilayers
[PMID:26824658 "When reconstituted into bilayers, LRRC8 complexes are sufficient to form
anion channels activated by osmolality gradients."],
and a **homo**-hexameric LRRC8A channel conducts
[PMID:29769723 "This protein conducts ions and has properties in common with endogenous
heteromeric channels."].
Cryo-EM confirms the homo-hexamer and, importantly, that a residue at the narrowest
constriction of the homomeric channel is a pore determinant of the *heteromeric* channel
[PMID:30095067 "mutational analysis demonstrates that a charged residue at the narrowest
constriction of the homomeric channel is an important pore determinant of heteromeric VRAC"].

So LRRC8A is **pore-forming**, not merely a chaperone or accessory subunit — but the
physiological channel is a heteromer. Curation consequence: in `core_functions` I recorded
the channel activity with `contributes_to_molecular_function` plus `in_complex`
(GO:0034702), rather than asserting `molecular_function` outright, and stated the
homohexamer caveat in the description.

## 2. Substrates: it is a broadly permeable large-pore channel

VRAC is not a chloride-specific channel. Beyond Cl-/I-, it passes organic osmolytes and
signalling molecules:

- taurine and regulatory volume decrease [PMID:24790029 "Taurine flux and regulatory volume
  decrease also depended on LRRC8 proteins."]
- [PMID:28193731 "We show that, besides the osmolytes taurine and myo-inositol, LRRC8
  channels transport the neurotransmitters glutamate, aspartate and γ-aminobutyric acid
  (GABA) and the co-activator D-serine."]
- substrate spectrum is subunit-dependent [PMID:28193731 "Whereas LRRC8D was crucial for the
  translocation of overall neutral compounds like myo-inositol, taurine and GABA, and
  sustained the transport of positively charged lysine, flux of negatively charged aspartate
  was equally well supported by LRRC8E."]

UniProt records Rhea reactions for chloride, iodide, taurine, L-aspartate, L-glutamate,
myo-inositol and 2',3'-cGAMP.

There is also an intracellular pool: LRRC8 proteins on lysosomal membranes carry Lyso-VRAC
currents [PMID:33139539 "LRRC8 proteins on lysosome membranes generate large lysosomal
volume-regulated anion channel (Lyso-VRAC) currents in response to low cytoplasmic ionic
strength conditions."].

## 3. The contested question: is cGAMP transport real, or an overexpression artifact?

### Evidence FOR (and it is substantial, and largely *not* overexpression-based)

- Lahey et al. 2020, the GOA IDA source:
  [PMID:33171122 "Here, we identify LRRC8A heteromeric channels, better known as
  volume-regulated anion channels (VRAC), as widely expressed cGAMP transporters."],
  [PMID:33171122 "LRRC8A forms complexes with LRRC8C and/or LRRC8E, depending on their
  expression levels, to transport cGAMP and other 2'3'-cyclic dinucleotides."],
  [PMID:33171122 "We demonstrate that cGAMP is effluxed or influxed via LRRC8 channels, as
  dictated by the cGAMP electrochemical gradient."],
  and a subunit-specific negative control
  [PMID:33171122 "In contrast, LRRC8D inhibits cGAMP transport."].
  A subunit-composition dependence with a *suppressive* paralog is hard to explain as a
  nonspecific overexpression leak.
- Zhou et al. 2020 (Immunity), independent group, with **in vivo** loss-of-function:
  LRRC8A/LRRC8E-containing VRACs transport cGAMP and cyclic dinucleotides across the plasma
  membrane, and Lrrc8e-deficient mice show impaired IFN responses and compromised immunity
  to HSV-1 (PMID:32277911; abstract-only in cache, so no verbatim quote is asserted in the
  YAML).
- Concepcion et al. 2022 (Nat Immunol), third group, T-cell-intrinsic in vivo phenotype
  attributable to LRRC8C-dependent cGAMP uptake and downstream STING signalling
  (PMID:35105987).
- Zheng et al. 2025 (Mol Cell), the PSA/NPEPPS paper, treats VRAC-mediated cGAMP import as
  an established, tunable function and uses endogenous-level manipulations (PSA knockout /
  re-expression), not VRAC overexpression:
  [PMID:41371222 "Electrophysiology demonstrated that PSA suppresses VRAC activity, and
  functional assays showed that PSA correspondingly modulates cGAMP transport."],
  [PMID:41371222 "Extracellular cGAMP, released from damaged or diseased cells, can enter
  neighboring host cells through VRACs under physiological conditions, where it activates
  the innate immune STING pathway"].
  They are explicit about their own limits:
  [PMID:41371222 "In addition, our analyses of cGAMP transport and STING signaling were
  carried out in cell lines, and further in vivo studies will be needed to assess the
  physiological and pathological relevance of PSA-mediated VRAC regulation in cGAMP
  transport and STING signaling."]

### Evidence AGAINST — read carefully, because it does not say what the title suggests

Thöne et al. 2026 (J Biol Chem, Jentsch lab) is titled "A protective cGAMP-mediated
anti-tumor immune response can proceed without LRRC8/VRAC channels" and its abstract states
[PMID:41419196 "However, tumor growth and the cGAMP-mediated antitumor immune response were
independent of both tumor- and host-expressed VRAC."] and
[PMID:41419196 "Disruption of any of the non-essential subunits, LRRC8B-LRRC8E, had no
discernible effect on T or B cell development in mice."].

**But the same paper, in its own results, confirms the molecular function.** Using
Lrrc8a-disrupted MC38 cells at endogenous expression:
[PMID:41419196 "We conclude that VRAC is the dominant PM cGAMP transporter of MC38 cells."]
and
[PMID:41419196 "Taken together, MC38 cells produce cGAMP endogenously and use VRAC as the
dominant cGAMP transporter."].
Their own summary of scope is
[PMID:41419196 "We conclude that VRAC is not the major pathway for cGAMP transmission, at
least in our model."], and they explicitly accept the T-cell result of others
[PMID:41419196 "To explain the role of VRAC in irradiated tumors or virus-infected cells, we
suggest that under these conditions extracellular cGAMP levels are highly increased."].
They also note cell-type dependence: B16-F10 melanoma cells, unlike MC38, barely use VRAC
[PMID:41419196 "Hence, cGAMP uptake by B16-F10 cells occurs primarily through pathways
distinct from VRAC."].

### Adjudication

The logical shape matters. A knockout showing that a *physiological outcome* (tumour growth,
antitumour immunity in MC38/B16-F10 syngeneic grafts) proceeds normally without the protein
does **not** show that the protein cannot transport the substrate. Thöne et al. refute a
*requirement* for VRAC in one in vivo process; in the same experiments they positively
demonstrate the transport. Nothing in the 2026 paper supports an "overexpression artifact"
reading, and no paper I found claims one.

Curation call:
- `GO:0140360` cyclic-GMP-AMP transmembrane transporter activity (IDA + IEA) — **not**
  removed, **not** an artifact. Marked `KEEP_AS_NON_CORE`.
- `GO:0140361` cyclic-GMP-AMP transmembrane import across plasma membrane (IBA + IEA + IDA)
  — same treatment, `KEEP_AS_NON_CORE`.

Non-core rather than core because (i) it is one permeant among many for a large-pore,
broadly selective channel, (ii) it requires LRRC8C or LRRC8E and is *suppressed* by LRRC8D,
so it is a property of particular heteromers rather than of LRRC8A as such, and (iii) its in
vivo weight is demonstrably context-dependent — dominant in MC38, negligible in B16-F10,
pivotal in irradiated tumours and in T cells, dispensable for the MC38 antitumour response.
Removing or demoting the IDA would also violate the project rule against overruling an
experimental annotation from an abstract; here I have the full text of both contested papers
and they agree with the annotation at the molecular-function level.

## 4. Other annotation notes

- `GO:0005515 protein binding` (4 IPI rows, PMIDs 24790029, 28514442, 33961781, 40205054) —
  `MARK_AS_OVER_ANNOTATED` per project guidance. The biology behind them (LRRC8A–LRRC8B/C/D/E
  heteromerization) is already captured by GO:0034702 and GO:0034214.
- `GO:0042802 identical protein binding` — kept as non-core. Unlike bare protein binding this
  is informative (LRRC8A homohexamer, PMID:30095067, PMID:30127360), but it is an assembly
  property, not the channel function.
- `GO:0005253 monoatomic anion channel activity` (IMP, `contributes_to`) — `MODIFY` to
  GO:0005225. The `contributes_to` qualifier is apt; the term is simply the generic parent of
  the volume-sensitive term the same experiments established.
- `GO:0006820 monoatomic anion transport` (IMP x2) — `MODIFY` to GO:0098656 (transmembrane).
- `GO:0016020 membrane` (IDA, HDA) — `MODIFY` to GO:0005886.
- `GO:0005737 cytoplasm` (IBA, `is_active_in`) — kept as non-core, not corrected. Defensible
  in the trivial sense (the LRR domains are cytosolic and the Lyso-VRAC pool lies within the
  cytoplasm) but uninformative next to plasma membrane / lysosomal membrane. I did not
  inspect the PAINT tree, so per project rules I did not issue a corrective IBA action with
  fabricated propagation metadata.
- Organismal/tissue phenotypes transferred from mouse or rat (`GO:0001678` glucose
  homeostasis, `GO:0032024` insulin secretion, `GO:0002329` pre-B cell differentiation,
  `GO:0007283` spermatogenesis, `GO:0045663` myoblast differentiation) — all
  `KEEP_AS_NON_CORE`. They are real downstream consequences of VRAC activity, well documented
  ([PMID:29371604 "SWELL1 depletion in MIN6 cells and islets significantly impairs
  glucose-stimulated insulin secretion."]; [PMID:14660746 "These results indicate that LRRC8
  is responsible for the B cell deficiency in this patient and is required for B cell
  development."]) but they are not the molecular activity.
- `GO:0015734` taurine and `GO:0015810` aspartate transmembrane transport — accepted; these
  are the classic VSOAC organic-osmolyte fluxes (PMID:24790029, PMID:28193731).

## 5. Verification log

PMIDs confirmed via PubMed MCP (title/journal/year) or the cached PubMed record header:
24725410 (Cell 2014), 24790029 (Science 2014), 26824658 (Cell 2016), 29769723 (Nature 2018),
30095067 (eLife 2018), 30127360 (Nat Struct Mol Biol 2018), 33139539 (PNAS 2020),
33171122 (Mol Cell 2020), 14660746 (J Clin Invest 2003), 24782309 (J Biol Chem 2014),
19946888 (J Mass Spectrom 2010), 28514442, 33961781, 40205054, 28193731 (J Cell Sci 2017),
29371604 (Nat Commun 2018), 32277911 (Immunity 2020), 35105987 (Nat Immunol 2022),
41371222 (Mol Cell 2025), 41419196 (J Biol Chem 2026).
