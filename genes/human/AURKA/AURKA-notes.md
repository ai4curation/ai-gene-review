# AURKA (Aurora kinase A, O14965) - curation notes

## Deep research status

- Falcon deep research first launched with `--fallback perplexity-lite` (600 s timeout; fallback unavailable in
  this environment), then relaunched with `--timeout 2400`. See "Deep research outcome" at the end of this file.
- The review was written from the cached publications (`publications/PMID_*.md`), UniProt O14965 and Reactome
  entries. Most AURKA papers in the cache are abstract-only.

## Summary of function

- Mitotic Ser/Thr kinase of the Aurora/Ipl1 family; expression and kinase activity peak in G2/M
  [PMID:9153231 "Both of these levels are low in G1/S, accumulate during G2/M, and reduce rapidly after mitosis"].
- Localizes to spindle poles from prophase to anaphase
  [PMID:9153231 "Aik is localized to the spindle pole during mitosis, especially from prophase through anaphase"]
  and to centrosomes from just before mitosis onward
  [PMID:19774610 "Aurora A is associated with centrosomes, being localized at the centrosome just prior to the onset of mitosis and for the duration of mitosis"].
- Activation: Thr288 autophosphorylation promoted by TPX2, which also targets AURKA to spindle MTs
  [PMID:14580337 "It is activated by phosphorylation and by the microtubule-associated protein TPX2, which also localizes the kinase to spindle microtubules"];
  Ajuba and BORA are additional activators [PMID:13678582; PMID:16890155].
- Mitotic entry: [PMID:13678582 "initial activation of Aurora-A in late G2 phase of the cell cycle is essential for recruitment of the cyclin B1-Cdk1 complex to centrosomes"];
  AURKA phosphorylates PLK1 T210 with BORA [PMID:18615013 "We find that aurora A can directly phosphorylate PLK1 on Thr 210"].
- Centrosome maturation / spindle assembly: [PMID:25657325 "Aurora A is required for centrosome maturation and bipolar spindle formation"];
  [PMID:14580337 "Aurora-A is an oncogenic kinase essential for mitotic spindle assembly"]; substrate MCRS1
  [PMID:27192185 "We show that MCRS1 is phosphorylated by the Aurora-A kinase in mitosis on Ser35/36"].
- Other substrates/effects: HURP stabilization [PMID:15987997], RALA S194 and mitochondrial fission [PMID:21822277],
  hnRNPK/p53 [PMID:21821029], p73 [PMID:22340593], PHLDA1 [PMID:21807936], FOXP1-FBXL7-Survivin axis [PMID:28218735].
- Kinase-independent stabilization of N-Myc [PMID:27837025 "N-Myc protein (the product of the MYCN oncogene) is stabilized in neuroblastoma by the protein kinase Aurora-A"].

## Cilium disassembly (non-mitotic, non-dominant function)

- [PMID:17604723 "interactions between the prometastatic scaffolding protein HEF1/Cas-L/NEDD9 and the oncogenic Aurora A (AurA) kinase at the basal body of cilia causes phosphorylation and activation of HDAC6, a tubulin deacetylase, promoting ciliary disassembly"]
- [PMID:17604723 "it constitutes an unexpected nonmitotic activity of AurA in vertebrates"]
- Pitchfork/CIMAP3 is a second activator [PMID:20643351 "PIFO, but not R80K PIFO, is sufficient to activate Aurora A, a protooncogenic kinase that induces cilia retraction"].
- Interpretation: the ciliary role is real and experimentally grounded, but it reuses the same kinase activity
  that dominates AURKA biology in mitosis. In core_functions it is listed third and labelled secondary.

## Key curation decisions

- 49 `protein binding` IPI rows: REMOVE (uninformative), noting that interactions are real. `protein kinase
  binding` (PLK1) kept as non-core; `protein heterodimerization activity` (GADD45A) marked over-annotated.
- `protein serine/threonine/tyrosine kinase activity` (ARBA IEA, TAS review): MODIFY to GO:0004674 - AURKA is a
  Ser/Thr kinase (EC 2.7.11.1).
- `chromosome passenger complex` IBA: REMOVE - CPC membership is Aurora B/C-specific; wild-type Aurora A lacks
  INCENP/Survivin binding, which requires a G198N swap [PMID:19357306]. propagation_review added.
- Kinetochore, spindle midzone, cytokinesis IBAs: kept as non-core (Aurora B-dominant, but some AURKA evidence).
- `response to wounding` and `liver regeneration` (IDA, transgenic overexpression in mouse liver [PMID:19435814]):
  MARK_AS_OVER_ANNOTATED.
- `molecular function activator activity` EXP [PMID:12237287] (crystal structure paper): UNDECIDED; cannot verify.
- Nuclear, cytosolic (Reactome), basolateral, neuron projection, midbody: KEEP_AS_NON_CORE.

## HPA cilium atlas vs module role

- HPA v25 (member_evidence.md): Basal body (Supported); Centrosome (Supported); main locations Basal body;
  Centrosome; Mitotic spindle. GOA carries GO_REF:0000052 IDA rows for centrosome and ciliary basal body
  (both ACCEPTed).
- Module (stage 7, cilium disassembly): AURKA as the basal-body kinase activated by NEDD9/Pitchfork that
  phosphorylates HDAC6. The HPA basal-body call (Supported) is consistent with this role, and the HPA
  centrosome/mitotic spindle calls reflect AURKA's dominant mitotic biology. HPA does not report an axonemal
  (primary cilium) call, consistent with AURKA acting at the ciliary base.
- PMID:41005307 (Hansen et al. 2025, HPA cilium atlas) does not mention AURKA in its cached text.
- No disagreement with the module's GO terms (GO:0004674 kinase, GO:0061523 cilium disassembly, GO:0036064
  basal body). Caveat for the module: AURKA should not be read as a cilium-dedicated protein; its disassembly role
  is a redeployment of the mitotic kinase.

## Deep research outcome

- Falcon succeeded on the second run (`--timeout 2400`; the run took about 2410 s and the wrapper log reported a
  timeout, but a complete report was written): `AURKA-deep-research-falcon.md`. Its conclusion matches this review:
  AURKA is primarily a spatially regulated Ser/Thr kinase for mitotic entry and bipolar spindle assembly, with
  basal-body AURKA-HDAC6 cilium resorption as a validated non-mitotic function
  [file:human/AURKA/AURKA-deep-research-falcon.md "Its basal-body AURKA–HDAC6 activity regulates cilium resorption"].
