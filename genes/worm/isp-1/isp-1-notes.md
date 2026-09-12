# isp-1 (C. elegans) — Gene Review Notes

UniProt: O44512 (O44512_CAEEL) · WormBase: WBGene00002162 / F42G8.12 · NCBI Gene: 177609
Locus: Chromosome IV · Protein: 276 aa · EC 7.1.1.8

## Summary / identity

`isp-1` encodes the **Rieske iron-sulfur protein (ISP)**, the [2Fe-2S]-cluster-bearing
subunit of **mitochondrial respiratory complex III** (cytochrome *bc1* / ubiquinol–cytochrome
*c* oxidoreductase). Within complex III it accepts electrons from ubiquinol at the Qo site and
passes them to cytochrome c1, as part of the protonmotive Q-cycle.

- UniProt names it "Cytochrome b-c1 complex subunit Rieske, mitochondrial"; EC 7.1.1.8;
  belongs to the Rieske iron-sulfur protein family; binds 1 [2Fe-2S] cluster per subunit;
  localized to the mitochondrion inner membrane (`isp-1-uniprot.txt`, RuleBase RU004494/RU004495).
- PANTHER family PTHR10134 "CYTOCHROME B-C1 COMPLEX SUBUNIT RIESKE, MITOCHONDRIAL"
  (`interpro/panther/PTHR10134/`).
- Independent literature confirmation of identity: "The Caenorhabditis elegans isp-1 gene
  encodes the Rieske iron-sulfur protein subunit of cytochrome c oxidoreductase (complex III of
  the electron transport chain)." [PMID:26504246 "encodes the Rieske iron-sulfur protein subunit of cytochrome c oxidoreductase (complex III of the electron transport chain)"]
- "The nuo-6 and isp-1 genes of C. elegans encode, respectively, subunits of complex I and III
  of the mitochondrial respiratory chain." [PMID:21151885 "subunits of complex I and III of the mitochondrial respiratory chain"]

## KNOWN (well established)

### Core molecular function / localization
- Rieske [2Fe-2S] iron-sulfur subunit of complex III; electron transfer from ubiquinol to
  cytochrome c1; part of the ubiquinol–cytochrome c reductase reaction (EC 7.1.1.8).
  Cofactor: one [2Fe-2S] cluster (Rieske high-potential type). Source: UniProt
  (`isp-1-uniprot.txt`: CATALYTIC ACTIVITY, COFACTOR, MISCELLANEOUS "The Rieske protein is a
  high potential 2Fe-2S protein"), Rieske-family conservation (PANTHER PTHR10134, InterPro
  IPR017941 Rieske_2Fe-2S). Reactome R-CEL-611105 (Respiratory electron transport),
  R-CEL-9865881 (Complex III assembly).
- Mitochondrial inner membrane localization (UniProt SUBCELLULAR LOCATION; single-pass membrane
  anchor + Rieske catalytic head).

### Biological process (respiration) — experimentally supported in worm
- The complex III mutant `isp-1(qm150)` reduces mitochondrial respiration: it shows impaired
  complex I-dependent (malate) and diminished complex II-dependent (succinate) oxidative
  phosphorylation capacity — expected because complex III is the common downstream acceptor.
  [PMID:16920626 "in isp-1 (complex III mutant)"] and
  [PMID:16920626 "somewhat diminished in the complex III ( isp-1 ) mutant"]. This is the basis of
  the WormBase IMP annotation to GO:0006122.

### The isp-1(qm150) longevity mutant (downstream phenotype, NOT the core MF)
- `isp-1(qm150)` is a partial (hypomorphic) loss-of-function missense allele. Phenotypes:
  "low oxygen consumption, decreased sensitivity to ROS, and increased life span."
  [PMID:11709184 "low oxygen consumption, decreased sensitivity to ROS, and increased life span"]
- It is one of the classic *Mit* longevity mutants: "longevity is increased by a partial
  loss-of-function mutation in the mitochondrial complex III subunit gene isp-1."
  [PMID:20346072 "longevity is increased by a partial loss-of-function mutation in the mitochondrial complex III subunit gene isp-1"]
- Additional pleiotropic phenotypes of qm150 (developmental rate, pharyngeal pumping, brood
  size, movement, constitutive UPR-mt reporter, CO2 production, OXPHOS, lifespan). [PMID:26504246 "developmental rate, pharyngeal pumping rate, brood size, body movement, activation of the mitochondrial unfolded protein response reporter, CO2 production, mitochondrial oxidative phosphorylation, and lifespan extension"]
- Mechanism of longevity is a **mitohormetic superoxide signal**, not reduced oxidative damage:
  "the generation of superoxide is elevated in the nuo-6 and isp-1 mitochondrial mutants ...
  this elevation is necessary and sufficient to increase longevity." [PMID:21151885 "the generation of superoxide is elevated in the nuo-6 and isp-1 mitochondrial mutants, although overall ROS levels are not, and oxidative stress is low"] and [PMID:21151885 "this elevation is necessary and sufficient to increase longevity"]
- qm150 mutation and isp-1(RNAi) act via **distinct, separable mechanisms** (additive lifespan
  effects). [PMID:20346072 "the increase induced by isp-1(RNAi) is fully additive to that induced by nuo-6(qm200)"]

## NOT KNOWN / knowledge gaps

- **Mechanism linking the Rieske perturbation to the retrograde longevity signal.** How the
  specific `qm150` substitution in ISP-1 is converted into the elevated-superoxide signal that
  drives the pro-longevity transcriptional program is not molecularly defined. Kaeberlein and
  colleagues localized intragenic suppressors to a conserved six-residue "tether" region and
  proposed a "spring-loaded" gating model, but this is a hypothesis: "The focus on a single
  subunit as causal both in generation and in suppression of diverse pleiotropic phenotypes
  points to a common underlying molecular mechanism, for which we propose a 'spring-loaded'
  model." [PMID:26504246 "for which we propose a"]. The causal chain from tether-region dynamics
  → altered Qo-site electron transfer/superoxide → downstream gene expression remains open
  (BIOLOGY gap, RESIDUAL_SUBGAP; the textbook complex III function itself is solid).
- Whether ISP-1 has any function beyond complex III electron transfer (moonlighting) is not
  established; no evidence supports one, and none is claimed here.

## GOA annotation review plan (9 annotations)

| # | Term | Evid | Action | Rationale |
|---|------|------|--------|-----------|
| 1 | GO:0016491 oxidoreductase activity | IBA | MODIFY→GO:0009055 | correct but over-general; subunit MF is electron transfer |
| 2 | GO:0045275 respiratory chain complex III | IBA | ACCEPT | core CC (complex membership) |
| 3 | GO:0006122 mito electron transport ubiquinol→cyt c | IBA | ACCEPT | core BP |
| 4 | GO:0005743 mitochondrial inner membrane | IEA | ACCEPT | core CC |
| 5 | GO:0008121 quinol-cytochrome-c reductase activity | IEA | ACCEPT | complex-level MF ISP-1 contributes to (core) |
| 6 | GO:0016020 membrane | IEA | MARK_AS_OVER_ANNOTATED | uninformative; subsumed by GO:0005743 |
| 7 | GO:0051537 2 iron, 2 sulfur cluster binding | IEA | ACCEPT | core MF (defining Rieske cofactor) |
| 8 | GO:1902600 proton transmembrane transport | IEA | KEEP_AS_NON_CORE | Q-cycle proton translocation is a complex-level consequence, not ISP-1's direct MF |
| 9 | GO:0006122 (IMP, PMID:16920626) | IMP | ACCEPT | experimentally supported in worm (complex III respiration defect) |

No aging/longevity/behavioral GO annotations are present in the GOA (they are mutant phenotypes,
not curated normal roles), so none need down-weighting there; the longevity biology is captured
in `description` and `knowledge_gaps` only.

## References verified against PubMed (identity confirmed)
- PMID:11709184 — Feng, Bussière, Hekimi 2001 Dev Cell 1:633-44 (isp-1(qm150) discovery). VERIFIED.
  NOTE: my first guessed PMID "11740940" for this paper was WRONG (that PMID is a Drosophila
  neuralized paper); corrected to 11709184 via PubMed search + metadata.
- PMID:21151885 — Yang & Hekimi 2010 PLoS Biol 8:e1000556 (superoxide longevity signal). VERIFIED, full text.
- PMID:20346072 — Yang & Hekimi 2010 Aging Cell 9:433-47 (two modes; qm150 vs RNAi). VERIFIED.
- PMID:26504246 — Jafari...Kaeberlein 2015 PNAS 112:E6148-57 (tether suppressors; spring-loaded model). VERIFIED.
- PMID:16920626 — Falk et al 2006 Curr Biol 16:1641-5 (complex III mutant respiration; IMP source). VERIFIED, full text.
