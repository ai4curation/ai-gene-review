# HKT1 (AtHKT1;1, At4g10310, UniProt Q84TI7) — research notes

## Summary

AtHKT1;1 is the single HKT-family member in *Arabidopsis thaliana*. It is a Class I
HKT transporter that functions in planta as a **Na+-selective uniporter** in the
plasma membrane. Its physiological role is **Na+ retrieval/recirculation**: it unloads
Na+ from the xylem sap into xylem-parenchyma cells (and is also implicated in Na+
loading into phloem in shoots / unloading in roots), thereby limiting Na+ accumulation
in photosynthetic shoot tissue and conferring salt tolerance. It does NOT transport
K+ in planta; the "high-affinity K+ transporter" name is historical, inherited from
the wheat ortholog (TaHKT1), and does not reflect the Arabidopsis protein's selectivity.

## Identity / structure

- UniProt Q84TI7, RecName "Sodium transporter HKT1"; Short=AtHKT1; gene HKT1 /
  At4g10310. 506 aa. Member of TrkH potassium transport family, HKT (TC 2.A.38.3)
  subfamily [UniProt Q84TI7].
- Topology: four transmembrane-pore-transmembrane (4-TM-pore) repeats, i.e. a
  K-channel-like architecture but as a single subunit [PMID:11344270 title
  "Evidence in support of a four transmembrane-pore-transmembrane topology model for
  the Arabidopsis thaliana Na+/K+ translocating AtHKT1 protein, a member of the
  superfamily of K+ transporters"]. UniProt feature table lists 8 TM helices.
- Cryo-EM structures available: PDB 8W9N, 8W9O (2.7-2.8 Å) [UniProt Q84TI7 DR PDB lines].
- N-glycosylated at Asn-429; glycosylation not essential for function/targeting
  [PMID:11344270; UniProt PTM].

## Selectivity: Na+ not K+ (key point)

- UniProt FUNCTION: "Sodium transporter protein, which plays a central role in plant
  tolerance to salt... Does not transport K(+) but regulates K(+) nutrient status via
  its ability to facilitate Na(+) homeostasis. Probably not involved in root uptake
  of Na(+)." [UniProt Q84TI7]
- UniProt MISCELLANEOUS: "In contrast to K(+) channel proteins, it lacks a conserved
  Gly at position 68, explaining why it does not act as a K(+) transporter." [UniProt Q84TI7]
- CATALYTIC ACTIVITY (Rhea RHEA:34963): Na(+)(in) = Na(+)(out); ChEBI:29101
  [UniProt Q84TI7].
- Heterologous characterization: "AtHKT1 functioned as a selective Na+ uptake
  transporter in Xenopus laevis oocytes, and the presence of external K+ did not
  affect the AtHKT1-mediated ion conductance (unlike that of HKT1)... in contrast to
  HKT1, AtHKT1 did not complement the growth of yeast cells deficient in K+ uptake...
  AtHKT1 can mediate Na+ and, to a small degree, K+ transport in heterologous
  expression systems." [PMID:10759522 abstract]. Note: a "less than 2-fold" K+
  stimulation in E. coli K+-uptake mutants is the only K+ activity seen, and only in
  heterologous systems — not in planta.
- The Ser-68 → Gly mutation gives "some permeability to potassium" [UniProt MUTAGEN 68;
  PMID:11959905 title "Glycine residues in potassium channel-like selectivity filters
  determine potassium selectivity in four-loop-per-subunit HKT transporters from plants"],
  i.e. WT AtHKT1 is Na+-selective and a single residue governs the K+/Na+ distinction.

## Physiological function (in planta)

- Salt-tolerance determinant controlling Na+ entry; loss-of-function hkt1 alleles
  suppress NaCl hypersensitivity of sos3-1 and reduce intracellular Na+
  [PMID:11698666 "These results indicate that AtHKT1 is a salt tolerance determinant
  that controls Na+ entry and high affinity K+ uptake"]. (Note: the "high affinity K+
  uptake" phrasing in this 2001 abstract reflects an indirect K+/Na+ ratio effect, not
  direct K+ transport; later structural/functional work clarified AtHKT1 does not
  transport K+ in planta.)
- Na+ recirculation by the phloem: sas2-1/sas2-2 = AtHKT1; expression "restricted to
  the phloem tissues in all organs"; sas2-1 reduces phloem-sap Na+, causes Na+
  overaccumulation in aerial organs and underaccumulation in roots; "AtHKT1 is
  involved in Na+ recirculation from shoots to roots, probably by mediating Na+ loading
  into the phloem sap in shoots and unloading in roots... playing a crucial role in
  plant tolerance to salt." Critically: "Na+ influx was 20% higher in sas2-1 than in
  wild-type roots... This indicates that AtHKT1 is not involved in Na+ uptake by roots
  in Arabidopsis." [PMID:12727868 full text]
- Xylem Na+ unloading: "AtHKT1 is targeted to the plasma membrane in xylem parenchyma
  cells in leaves... AtHKT1 disruption alleles caused large increases in the Na+ content
  of the xylem sap and conversely reduced the Na+ content of the phloem sap. The athkt1
  mutant alleles had a smaller and inverse influence on the potassium (K+) content...
  suggesting that K+ transport may be indirectly affected... AtHKT1 selectively unloads
  sodium directly from xylem vessels to xylem parenchyma cells... reduces the sodium
  content in xylem vessels and leaves, thereby playing a central role in protecting plant
  leaves from salinity stress." [PMID:16359386 abstract]
- Independent confirmation by deletion mutant: FN1148 = 523-bp deletion in AtHKT1;
  "responsible for the sodium overaccumulation in shoots and leaf sodium sensitivity";
  "Na+ overaccumulation in stems and rosette leaves... in roots... less Na+ detected
  compared to the WT"; AtHKT1 cDNA complements salt sensitivity [PMID:15486089 full text].

## Subcellular localization

- Plasma membrane (cell membrane), multi-pass membrane protein [UniProt SUBCELLULAR
  LOCATION]. Direct evidence: immunoelectron microscopy localizes AtHKT1 to the plasma
  membrane of xylem parenchyma cells [PMID:16359386 abstract, IDA in GOA].
- A GOA ISM annotation (GO:0005739 mitochondrion, GO_REF:0000122 AtSubP) is a
  prediction-only annotation contradicted by direct PM localization; treated as
  over-annotation/unsupported.

## Tissue specificity

- "Highly expressed in roots. Expressed in flowers, leaves and stems. Expressed in the
  vascular tissues of every organs. In roots, leaves and flower peduncles, it is only
  expressed in the phloem tissues. Not expressed in root peripheral cells."
  [UniProt TISSUE SPECIFICITY; PMID:10759522, PMID:12727868]

## GO term definition checks (QuickGO API)

- GO:0015081 sodium ion transmembrane transporter activity: "Enables the transfer of
  sodium ions (Na+) from one side of a membrane to the other." — matches in-planta
  function; CORE MF.
- GO:0015079 potassium ion transmembrane transporter activity: "Enables the transfer of
  potassium ions (K+) from one side of a membrane to the other." — NOT supported in
  planta (AtHKT1 does not transport K+); IEA InterPro family-level inference.

## Curation reasoning for K+ annotations

The K+ molecular-function and K+-transport process annotations (GO:0015079, GO:0006813,
GO:0071805) are electronic (IEA InterPro/ARBA) inherited from the HKT/Trk/Ktr family
and from the wheat ortholog's high-affinity K+ behavior. The Arabidopsis protein is
Na+-selective; UniProt explicitly states it "does not transport K(+)" and the lone
Gly-68 absence is the structural explanation. These are therefore mapped toward the
Na+ counterparts (MODIFY) or marked as over-annotation rather than accepted, but not
blanket-removed as "wrong gene." The one TAIR IMP K+ annotation (GO:0006813,
PMID:16359386) reflects the *indirect* K+ effect ("K+ transport may be indirectly
affected") — kept as non-core / over-annotated since it is a downstream/indirect
consequence, not a direct K+ transport function.
