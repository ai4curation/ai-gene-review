# UROS (P10746) review notes

## Function (verified)
UROS = uroporphyrinogen-III synthase (URO-synthase / URO3S / U3S), EC 4.2.1.75,
hydroxymethylbilane hydro-lyase (cyclizing). It is the **fourth enzyme of the heme
biosynthetic pathway**. It catalyzes the cyclization of the linear tetrapyrrole
**hydroxymethylbilane (HMB)** into the macrocyclic **uroporphyrinogen III**, with
concurrent **inversion/flipping of ring D** — producing the physiological III isomer.
Without UROS, HMB spontaneously (non-enzymatically) cyclizes to the useless
uroporphyrinogen I isomer.

- [PMID:3805019 abstract, "the fourth enzyme in the heme biosynthetic pathway"]
- [PMID:3174619 abstract, "the fourth enzyme in the heme biosynthetic pathway, is responsible for conversion of the linear tetrapyrrole, hydroxymethylbilane, to the cyclic tetrapyrrole, uroporphyrinogen III"]
- [PMID:11689424 full text, "catalyzes ring closure of the linear tetrapyrrole hydroxymethylbilane (HMB), with concurrent flipping of the D ring, to form uro'gen III"]
- [PMID:18004775 abstract, "catalyzes the cyclization and D-ring isomerization of hydroxymethylbilane (HMB) to uroporphyrinogen (URO'gen) III"]
- UniProt PATHWAY: "Porphyrin-containing compound metabolism; protoporphyrin-IX biosynthesis" step 3/4 (from ALA); URO'gen III is the branch point for heme, chlorophyll, corrins (B12), siroheme, F430.

## Localization
Cytosol (Cytoplasm, cytosol per UniProt SUBCELLULAR LOCATION). One of the four cytosolic
steps of heme biosynthesis (Reactome R-HSA-189451). The old ISS mitochondrion annotation
(from P51163) is inconsistent with UniProt and Reactome and should be removed.

## Oligomeric state
Monomer [PMID:3805019 abstract, "consistent with the enzyme being a monomer"; PMID:11689424 "U3S exists as a monomer"].

## Disease
Deficiency causes **congenital erythropoietic porphyria (CEP / Gunther disease)**,
autosomal recessive; severe cutaneous photosensitivity from accumulation of the
uroporphyrin(ogen) I isomer. Numerous CEP missense variants documented in UniProt
(C73R hotspot, etc.).

## Annotation decisions summary
- MF **GO:0004852 uroporphyrinogen-III synthase activity** — core; supported by IDA
  (PMID:3805019, 3174619, 18004775), EXP (PMID:11689424), IBA, IEA, TAS. ACCEPT all.
- BP **GO:0006780 uroporphyrinogen III biosynthetic process** — direct product; ACCEPT.
- BP **GO:0006783 heme biosynthetic process** — the pathway UROS serves; ACCEPT (core).
- BP **GO:0033014 tetrapyrrole biosynthetic process** — correct broader parent; ACCEPT.
- CC **GO:0005829 cytosol** — ACCEPT all (IBA/ISS/TAS/NAS/IEA).
- **GO:0006785 heme B biosynthetic process** — heme b is a specific downstream product;
  UROS acts upstream at the branch point (its product feeds ALL porphyrins, not
  specifically heme b). Over-annotation (both the IEA and the IDA); MARK_AS_OVER_ANNOTATED,
  prefer the general GO:0006783.
- **GO:0005542 folic acid binding** (IEA from rat ortholog) — no evidence UROS binds
  folate; substrate is a tetrapyrrole, not a pterin; spurious ortholog electronic
  inference. REMOVE.
- **GO:0070541 response to platinum ion / GO:0071243 cellular response to arsenic /
  GO:0071418 cellular response to amine** (IEA from rat ortholog) — generic stress/
  perturbation-response terms transferred electronically from rat; not a core molecular
  role of this heme-biosynthesis enzyme. MARK_AS_OVER_ANNOTATED.
- **GO:0005739 mitochondrion** (ISS, 2009) — UROS is cytosolic; contradicted by UniProt
  and Reactome. Not an experimental annotation. REMOVE.

## Core functions
1. MF GO:0004852 uroporphyrinogen-III synthase activity
2. directly_involved_in BP GO:0006783 heme biosynthetic process
3. located_in CC GO:0005829 cytosol
