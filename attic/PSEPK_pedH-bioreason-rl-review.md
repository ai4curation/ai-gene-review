# BioReason-Pro RL Review: pedH (Pseudomonas putida)

Source: pedH-deep-research-bioreason-rl.md

- **Correctness**: 2/5
- **Completeness**: 2/5

## What It Got Right

BioReason correctly identifies pedH as a PQQ-dependent alcohol dehydrogenase based on the domain architecture (IPR017512 methanol/ethanol family, IPR034119 type I alcohol dehydrogenase, IPR002372 PQQ repeat domain). The beta-propeller structural description is accurate. The general inference that this enzyme oxidizes primary and secondary alcohols as part of alcohol metabolic processes is correct. Quinone binding (GO:0048038) is correctly predicted. The broad enzymatic activity assignment to oxidoreductase activity acting on CH-OH donors is accurate.

## Major Errors

**Calcium ion binding (GO:0005509) predicted — the defining error.** BioReason predicts calcium ion binding as a molecular function. This is precisely wrong for pedH: the defining biochemical feature of PedH is that it requires **lanthanide ions** (La³⁺, Ce³⁺, Pr³⁺, Nd³⁺, Sm³⁺) for activity, not calcium. This is the central research finding that distinguishes PedH from its paralog PedE (which is calcium-dependent). The curated review explicitly removes the calcium ion binding annotation (IEA) as incorrect. BioReason replicates exactly the automated annotation error that the expert curator identified as the most important fix needed. This is a high-profile error because the lanthanide-dependence is the single most scientifically distinctive feature of this protein.

**Wrong cellular localization — cytoplasm instead of periplasm.** BioReason assigns PedH to the cytoplasm (GO:0005737), reasoning from "the absence of transmembrane segments." However, PedH has a signal peptide (residues 1–25) for periplasmic export. The mature protein is a soluble enzyme functioning in the **periplasmic space** (GO:0042597). This is the correct localization for all PQQ-dependent alcohol dehydrogenases (MxaF, XoxF, ExaA, PedE, PedH), which transfer electrons to periplasmic cytochrome c. BioReason incorrectly calls the signal peptide's hydrophobic segment a transmembrane helix indicator for cytoplasmic topology, inverting the actual subcellular location.

**Thylakoid listed as cellular component.** The predicted GO includes thylakoid (GO:0009579) as a cellular component. Pseudomonas putida has no thylakoids; this is a photosynthetic organelle. This is a spurious annotation that was not filtered.

**Heme binding (GO:0020037) predicted.** BioReason predicts heme binding as a molecular function. PedH does not bind heme — it transfers electrons to the external electron acceptor cytochrome c550, but PedH itself is not a heme protein. The curated review explicitly removes this annotation as incorrect.

**Wrong electron acceptor assumption.** The model assigns GO:0004098 (alcohol dehydrogenase NAD activity) as the "formal label for alcohol oxidation chemistry." PedH is a quinoprotein ADH that uses cytochrome c as electron acceptor — the correct term is GO:0052934 (alcohol dehydrogenase cytochrome c activity). PedH does not use NAD as electron acceptor. This is a fold-bias error: the model correctly identifies the enzyme class but then defaults to the NAD-dependent form rather than the cytochrome-linked quinoprotein form.

## What Was Missed

- **Lanthanide-dependence** (the central biology): PedH requires lanthanide ions, not calcium, for activity. This is the defining characteristic documented in PMID:28655819.
- **Regulatory/sensory role**: PedH functions as a lanthanide sensor that influences transcription of pedH and pedE via the PedS2/PedR2 two-component system. The model has no concept of this dual catalytic/sensory role.
- **2-phenylethanol degradation (Ped) pathway context**: PedH is central to the Ped pathway, converting 2-phenylethanol to phenylacetaldehyde as part of aromatic alcohol catabolism.
- **Cytochrome c as electron acceptor**: The model assumes NAD-dependent chemistry; the actual electron acceptor is cytochrome c550 in the periplasm.
- **Inverse regulation with PedE**: pedH and pedE (the calcium-dependent paralog) are inversely regulated depending on lanthanide availability. This switch is mediated by PedS2/PedR2.
- **Growth on volatile organic compounds**: PedH is essential for growth on volatile alcoholic VOCs — an ecologically important phenotype.
- **PQQ cofactor specificity**: While quinone binding is predicted, the specific PQQ cofactor (GO:0070968 pyrroloquinoline quinone binding) — a core annotation in the curated review — is absent from the output.

## Summary

BioReason's pedH output is substantially incorrect. The two most critical errors — predicting calcium ion binding (when the protein is specifically lanthanide-dependent) and assigning cytoplasmic localization (when the protein is periplasmic) — are exactly the automated annotation errors that expert curation exists to correct. BioReason replicates and reinforces these errors rather than catching them. Additional errors include wrong electron acceptor (NAD instead of cytochrome c), heme binding, and thylakoid assignment. The defining biology of pedH — lanthanide-dependent catalysis, periplasmic location, cytochrome c electron acceptor, sensory/regulatory role, Ped pathway context — is almost entirely absent.
