# SLC7A8 (LAT2 / Q9UHI5) curation notes

De-novo review, canonical-reviews-batch7. Same pipeline as the merged SLC12/SLC1/SLC2
transporter batches. Biology verified against UniProt Q9UHI5 and the cited primary
literature (all GOA-cited PMIDs are cached).

## Identity and core function

SLC7A8 encodes LAT2 (L-type amino acid transporter 2; "large neutral amino acids
transporter small subunit 2"), the catalytic **light chain** of a heteromeric amino-acid
transporter (HAT). It is disulfide-linked to the **heavy chain SLC3A2 (4F2hc/CD98hc)**,
which it needs for plasma-membrane trafficking and stability.

- Obligate, Na+-independent amino-acid **antiporter** with **1:1 exchange stoichiometry**:
  [PMID:11847106 "Quantification of amino acid influx and efflux by HPLC demonstrated an obligatory amino acid exchange with 1:1 stoichiometry"].
- Broad specificity for **small and large neutral (zwitterionic) amino acids**; Na+-independent;
  trans-stimulated (exchanger): [PMID:10391915 "sodium-independent and showed broad specificity for small and large zwitterionic amino acids"]; [PMID:10391915 "highly trans-stimulated, suggesting an exchanger mechanism of transport"].
- Low intracellular affinity / high extracellular affinity → it **equilibrates relative amino-acid
  concentrations across the membrane rather than mediating net uptake**:
  [PMID:11847106 "obligatory exchangers with relatively symmetrical substrate selectivities but strongly asymmetrical substrate affinities such that the intracellular amino acid concentration controls their activity"];
  [PMID:29355479 "the role of SLC7A8 is to equilibrate the relative concentrations of different amino acids across the plasma membrane instead of mediating their net uptake"].
  This is the key caveat for the GO "import across plasma membrane" rows: influx of each
  substrate is real and experimentally shown, but obligately coupled to counter-efflux.

## Heterodimer with SLC3A2 (4F2hc)

- Light chain of HAT; needs 4F2hc for surface expression and stability:
  [PMID:33298890 "The 4F2 cell-surface antigen heavy chain (4F2hc) is the heavy chain for LAT1 and LAT2, playing roles in plasma membrane localization of LATs4 and required for the stability and the transport activity of HATs10"].
- Disulfide-linked heterodimer (HAT family), from the LAT1 structure paper used by ComplexPortal:
  [PMID:33758168 "As a light chain protein, LAT1 is covalently linked with the heavy chain protein 4F2hc (also known as SLC3A2) through a conserved disulfide bond, forming a heterodimeric LAT1-4F2hc complex that belongs to the heteromeric amino acid transporters (HAT) family"].
- UniProt SUBUNIT: "Disulfide-linked heterodimer composed of the catalytic light chain subunit
  SLC7A8 and the heavy chain subunit SLC3A2." ICAM-1 (P05362) associates with the heterodimer and
  regulates activity [PMID:12716892].
- Cryo-EM structures of the LAT2-4F2hc complex: PDB 7CMH/7CMI (PMID:33298890), 7B00 (PMID:34848541).
- Modeled as `in_complex` GO:1902495 transmembrane transporter complex (ComplexPortal CPX-8186);
  heterodimerization captured by GO:0046982 (IDA, PMID:33298890).

## Localization

- **Basolateral** plasma membrane of epithelia (kidney proximal tubule, small intestine):
  [PMID:15918515 "the hLAT2 and hTAT1 proteins coexist in the basolateral membrane of the renal proximal tubules"]; also EXP in PMID:10391915, PMID:10574970. Core location for transepithelial
  neutral-AA reabsorption.
- Cytoplasmic when expressed alone; plasma membrane only when co-expressed with SLC3A2
  (UniProt; [PMID:29355479 "Co-expression of the light (SLC7A8) and the heavy (CD98hc) subunits in the same cell increases the plasma membrane localization of the transporter"]).
- Placenta: predominantly **microvillous (apical-facing) membrane**, also detected in basal
  membrane at lower level: [PMID:26050671 "While predominantly expressed in the MVM, LAT2 isoform was also detected in the BM, albeit at a much lower expression level"]. Supports GO:0031528
  microvillus membrane, GO:0009925 basal plasma membrane, and the ISS GO:0016324 apical PM
  (tissue-specific; distinct from the canonical basolateral location). All kept as non-core.

## Substrates (physiological reabsorption + secondary)

- Neutral amino acids, small and large: Gly, Ala, Ser, Cys, Gln, Met, Leu, Ile, Val, Phe, Trp, Tyr,
  His (UniProt CATALYTIC ACTIVITY Rhea exchange half-reactions, ECO:0000269|PubMed:11847106 etc.;
  Km values in UniProt). Supports the substrate-level MF/BP rows (Leu, Ala, Gly, Trp, Val transport).
  **Proline is NOT an established human LAT2 substrate** — the GO:0035524 proline-transmembrane-transport
  row is ISS/IEA from the mouse ortholog (Q9QXW9) only; marked over-annotated.
- **Thyroid hormone** (secondary): imports 3,3'-diiodothyronine (T2) and, to a lesser extent, T3, plus
  the iodotyrosine MIT; not T4/rT3: [PMID:26305885 "LAT2 showed a net uptake of T3, 3,3'-T2, and MIT"].
  Genuine secondary activity → KEEP_AS_NON_CORE (GO:0015349 MF, GO:0070327 BP).
- **Methylmercury-L-cysteine** (xenobiotic, molecular mimicry): transported as a methionine mimic:
  [PMID:12117417 "the methylmercury-L-cysteine complex is a substrate for human L-type large neutral amino acid transporter (LAT) 1 and LAT2"]. Real in-vitro activity but an incidental mimicry
  substrate, not an evolved function → GO:0019534 "toxin transmembrane transporter activity"
  marked MARK_AS_OVER_ANNOTATED.
- L-nitrosocysteine, L-DOPA (UniProt): further broad-specificity substrates.

## Physiology / disease

- Renal/intestinal basolateral efflux arm of transepithelial neutral-AA reabsorption (paired with
  apical B0AT1/SLC6A19 and with TAT1/SLC16A10) [PMID:15918515].
- Age-related hearing loss: Slc7a8-knockout mice show ARHL; human SLC7A8 variants (V302I, T402M,
  R418H, V460E) reduce transport: [PMID:29355479 "its ablation resulted in ARHL"].
- Blood-brain barrier: the cited NAS reference (PMID:30280653, a general BBB physiology review) does
  **not** mention SLC7A8/LAT2 by name; LAT1 (SLC7A5) is the dominant system-L carrier at the BBB.
  GO:0150104 "transport across blood-brain barrier" marked MARK_AS_OVER_ANNOTATED.

## Protein-binding / interactome rows

~29 GO:0005515 "protein binding" IPI rows: the SLC3A2 (P08195) and ICAM-1 (P05362) interactions are
functionally real but are captured by GO:0046982 / GO:1902495; the remainder are high-throughput
binary-interactome hits (PMID:32296183 reference interactome; PMID:32814053 neurodegenerative-disease
interactome / Y2H). Per the protein-binding policy, bare GO:0005515 is uninformative → REMOVE (removal
does not assert the interactions are false). The functional 4F2hc partnership is retained via the
heterodimerization and complex annotations.

## GO:0042605 peptide antigen binding (ISS, Q9N1Q4)

Biologically implausible for an SLC7 amino-acid-transporter light chain (an MHC/immune MF with no
support for this family); over-propagation from a non-human ortholog source → REMOVE + source_defect.

## Action summary rationale

- Core MF: GO:0015175 neutral L-amino acid transmembrane transporter activity; mechanism
  GO:0015297 antiporter activity; core location basolateral PM (GO:0016323) / PM (GO:0005886);
  in_complex GO:1902495 (with SLC3A2).
- General parent transport terms entailed by the specific neutral-AA antiporter function
  (GO:0003333, GO:0006865, GO:0055085, GO:0022857, GO:0015171, GO:0015179) → TOO_GENERAL.
- GO:0016020 membrane (IEA) → MODIFY to GO:0005886 plasma membrane.
