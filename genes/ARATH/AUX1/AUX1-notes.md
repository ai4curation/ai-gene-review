# AUX1 (AUXIN RESISTANT 1) — curation notes

UniProt: Q96247 (AUX1_ARATH); locus AT2G38120; synonyms AUX, PIR1, WAV5.
Family: amino acid/polyamine transporter 2 family; amino acid/auxin permease
(AAAP) subfamily (TC 2.A.18.1). 485 aa, multi-pass (≈11 TM helices) integral
membrane protein. Founding member of the AUX1/LAX auxin influx carrier family
(AUX1, LAX1, LAX2, LAX3).

## Core molecular function: auxin influx transporter

- Heterologous expression in Xenopus oocytes confers saturable, pH-dependent
  high-affinity uptake of 3H-IAA; reduced by 2,4-D and 1-NOA; function-abrogating
  mutations reduce uptake [PMID:16677815 "Upon expression of AUX1 in Xenopus
  oocytes, saturable, pH-dependent uptake of 3H-IAA was measured."]
  [PMID:16677815 "Mutations in AUX1 that abrogate physiological responses to IAA
  in planta resulted in loss or reduction of 3H-IAA uptake in AUX1-expressing
  oocytes."]
- Direct binding of IAA to AUX1 (baculovirus/insect cell membranes), Kd ≈ 2.6 µM,
  matching transport Km; auxin analogues/influx inhibitors displace IAA
  [PMID:18614710 "enabled us to determine a K(d) of 2.6 mum, comparable with
  estimates for the K(m) for IAA transport."]
- Mechanism: IAA-H+ symporter (proton-driven), pH optimum 5.0–6.0
  [PMID:18614710 "Members of the AUX/LAX family of membrane transporters,
  conserved in all higher plant species, are believed to act as IAA-H +
  symporters."] UniProt KW "Symport" maps to GO:0015293 symporter activity (DR
  line in uniprot.txt).
- UniProt FUNCTION: "Carrier protein involved in proton-driven auxin influx."

### GO terms (verified in GOA / UniProt entry)
- GO:0010328 auxin influx transmembrane transporter activity (IDA, PMID:16677815) — CORE MF
- GO:0010011 auxin binding (IDA, PMID:18614710) — ACCEPT
- GO:0060919 auxin import into cell (IEA inferred from GO:0010328) — ACCEPT, core BP
- GO:0009926 auxin polar transport (TAS, PMID:16839804) — ACCEPT, core BP
- GO:0015293 symporter activity — added as NEW (mechanism), from UniProt KW DR line

## Substrate specificity caveat (amino acid transport)

AUX1 is homologous to amino acid permeases, which seeded amino-acid-transport
annotations, but the only demonstrated physiological substrate is auxin (IAA).
[PMID:8688077 "Polypeptide sequence similarity to amino acid permeases suggests
that AUX1 mediates the transport of an amino acid-like signaling molecule."]
No experimental amino acid transport demonstrated. Therefore:
- GO:0015171 amino acid transmembrane transporter activity (ISS, PMID:9484486) — MARK_AS_OVER_ANNOTATED. NB the cited PMID:9484486 is actually a study of aux1 mRNA processing / nonsense-mediated decay, not amino acid transport.
- GO:0003333 amino acid transmembrane transport (IEA, inferred from GO:0015171) — MARK_AS_OVER_ANNOTATED.

## Subcellular localization

- Functional site = plasma membrane (multi-pass), asymmetric/polar in protophloem
  [PMID:11641271 "AUX1, asymmetrically localized to the plasma membrane of root
  protophloem cells..."]; IDA PM also in [PMID:16690816].
  GO:0005886 plasma membrane — ACCEPT (IEA, ISM, IDA copies).
- GO:0009986 cell surface (IDA, PMID:11641271) — MODIFY → GO:0005886 (data support
  plasma membrane; cell surface is the less precise/external term).
- Endosome (GO:0005768) and Golgi (GO:0005794), IDA PMID:17114355 — KEEP_AS_NON_CORE:
  these are trafficking-itinerary pools, not the functional transport site.
  AUX1 trafficking is BFA-insensitive, actin-dependent, GNOM-independent, distinct
  from PIN [PMID:17114355 "AUX1 resides at the apical plasma membrane of protophloem
  cells and at highly dynamic subpopulations of Golgi apparatus and endosomes in
  all cell types."]
- Trafficking to PM requires ER protein AXR4 [PMID:16690816 "AXR4 is a previously
  unidentified accessory protein of the endoplasmic reticulum (ER) that regulates
  localization of AUX1 but not of PIN proteins."]

## Protein interaction

GO:0005515 protein binding (IPI, PMID:32612234), WITH/FROM UniProtKB:Q9FZ33 = AXR4.
PMID:32612234 is a large-scale phytohormone interactome (>2000 binary PPIs). Bare
"protein binding" is uninformative; the biology (AXR4 = ER chaperone for AUX1
trafficking) is captured elsewhere. Action: REMOVE.

## Developmental / physiological roles (downstream of transport; KEEP_AS_NON_CORE except gravitropism)

- GO:0009958 positive gravitropism (IMP, PMID:8688077) — ACCEPT, core process.
  Gene named for agravitropic aux1 root phenotype [PMID:8688077 "Mutations within
  the AUX1 gene confer an auxin-resistant root growth phenotype and abolish root
  gravitropic curvature."] [PMID:11641271 "AUX1 is necessary for root gravitropism
  by facilitating basipetal auxin transport to distal elongation zone tissues."]
- GO:0010311 lateral root formation (IGI PMID:18622388; IMP PMID:17215297) —
  KEEP_AS_NON_CORE; LAX3 redundancy and lateral root positioning correlate with
  gravitropic waving [PMID:17215297 "...depends on AUX1, an auxin influx carrier
  essential for gravitropic response."]
- GO:0001736 establishment of planar polarity & GO:0048765 root hair cell
  differentiation (IGI PMID:17084699) — KEEP_AS_NON_CORE; combinatorial AUX1+EIN2+
  GNOM shape auxin gradient for root hair positioning [PMID:17084699 "combinatorial
  action of the auxin influx carrier AUX1, ETHYLENE-INSENSITIVE2 (EIN2), and GNOM
  genes mediates the vector for coordinate hair positioning."]
- GO:0048829 root cap development (IMP PMID:19952011) — KEEP_AS_NON_CORE; AUX1/LAX
  redundant in embryonic root cap patterning [PMID:19952011 "aux1 lax mutants have
  a larger radicle root cap than the wild type..."]
- GO:0010262 somatic embryogenesis (IEP + IMP, PMID:36345646) — KEEP_AS_NON_CORE;
  AUX1/LAX influx + PIN1 efflux drive polar auxin transport in SE [PMID:36345646
  "polar auxin transport, with AUXIN/LIKE-AUX influx and PIN-FORMED1 efflux carriers
  as important drivers, is required for the transition of embryonic cells to
  proembryos..."]
- GO:0009624 response to nematode (HEP, PMID:16478044) — MARK_AS_OVER_ANNOTATED;
  AUX1 only shows altered expression in nematode galls, no functional requirement
  shown [PMID:16478044 "Expression of 50 transporter genes from 18 different gene
  families was significantly changed upon nematode infestation."]

## Action summary
ACCEPT: 6 (GO:0005886 IEA, GO:0060919, GO:0010011, GO:0010328, GO:0009958,
GO:0009926, GO:0005886 ISM, GO:0005886 IDA) — note 3 PM copies + gravitropism +
transporter MF + auxin import + auxin binding + polar transport.
KEEP_AS_NON_CORE: somatic embryogenesis x2, root cap development, lateral root x2,
planar polarity, root hair, endosome, Golgi.
MARK_AS_OVER_ANNOTATED: amino acid transport (BP), amino acid transporter (MF),
response to nematode.
MODIFY: cell surface → plasma membrane.
REMOVE: protein binding.
NEW: symporter activity (GO:0015293, mechanism).

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)

A Falcon deep-research report (`AUX1-deep-research-falcon.md`) was generated and
used to augment the review with `file:ARATH/AUX1/AUX1-deep-research-falcon.md`
supporting_text entries. Key corroborations (no decisions weakened):

- Core MF / auxin import / polar transport: "Direct functional evidence from
  heterologous expression in Xenopus oocytes demonstrates that AUX1 transports
  IAA with high affinity and saturable kinetics" (Yang 2006); AUX1/LAX are
  "major auxin influx carriers required to establish auxin gradients that drive
  development."
- Symporter (NEW GO:0015293) mechanism reinforced: AUX1 "operates as a
  proton-coupled symporter (H+:IAA−)"; commonly cited stoichiometry 2 H+ per IAA−
  (Singh 2018 review). Supports the NEW symporter annotation and the proposed
  auxin:proton symporter term.
- Auxin binding (GO:0010011): Kd ≈ 2.6 µM, Bmax ≈ 11,800 fmol/mg, binding optimum
  pH 5–6 (Carrier 2008), matching transport Km.
- Plasma membrane localization confirmed (EYFP-AUX1).
- AXR4 = ER accessory/chaperone-like factor; in axr4, AUX1 accumulates in the ER
  rather than reaching the PM; AXR4 physically interacts with AUX1 and reduces
  AUX1 aggregation dose-dependently (Tidy et al. 2024, Plant Physiol,
  doi:10.1093/plphys/kiad506). This 2024 mechanistic study reinforces REMOVE of
  the bare protein binding term (AXR4 interaction reflects trafficking/chaperone
  biology, not AUX1's own MF) and the KEEP_AS_NON_CORE Golgi/endosome trafficking
  pools.
- Gravitropism (core): AUX1 moves auxin from lateral root cap to elongation-zone
  epidermis (Tang 2024 review).
- Lateral root: aux1 mutants ~50% reduction in emerged lateral roots; root hair:
  ~30-fold higher double-hair frequency, shorter root hairs (Swarup & Péret 2012)
  — corroborate KEEP_AS_NON_CORE developmental roles.

No new GO IDs were introduced from the deep research (the only NEW term,
GO:0015293, was already present from the UniProt KW DR line). The amino-acid
transport annotations remain MARK_AS_OVER_ANNOTATED: the report consistently
identifies IAA (not amino acids) as the demonstrated substrate while placing AUX1
in the AAAP superfamily, supporting the over-annotation call. No UNDECIDED
actions were present to resolve. status kept DRAFT.

## Notes on resources
All 15 cited PMIDs are cached under publications/. A Falcon deep-research report
is now available (`AUX1-deep-research-falcon.md` + `..._artifacts/artifact-00.md`).
Recent cryo-EM structures of AUX1 exist (PDB 9JDR, 9M2H) per the UniProt entry but
the structure papers were not in the cached set, so not cited.
