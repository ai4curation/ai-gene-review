# Reactome Black Box Event Gap-Filling

## Overview

Reactome, like most pathway databases, contains reactions where the biochemistry is understood but the protein catalyst or transporter has not been identified. These "black box events" (BBEs) represent genuine gaps in biological knowledge — reactions that must occur based on metabolite flux, but where the molecular identity of the enzyme or transporter remains unknown or uncertain.

Many BBEs involve membrane transport. A metabolic intermediate needs to move between compartments (cytosol to mitochondria, cytosol to peroxisomes, ER to Golgi), and while the substrate and directionality are clear from metabolic logic, the transporter gene has not been definitively assigned. Some of these gaps have persisted for decades, even as structural genomics, cryo-EM, and human genetics have generated data that could resolve them.

This project uses AI-assisted literature mining, structural analysis, and genetic evidence integration to systematically identify candidate proteins for Reactome BBEs. The approach combines the AIGR gene review pipeline with targeted deep research to converge on candidates at varying confidence levels.

## Collaboration Context

Peter D'Eustachio and Lisa Matthews at Reactome have been exploring how Claude can assist with identifying missing catalysts and transporters in pathway reactions. Reactome curators frequently encounter reactions where metabolic logic demands a specific transport or catalytic step, but the literature does not provide a clean assignment. The traditional approach — manual literature searching and expert consultation — scales poorly across the ~2,000 human metabolic pathways in Reactome.

The AIGR pipeline offers a complementary approach: systematic gene reviews that synthesize GO annotations, UniProt function descriptions, recent structural papers, and genetic evidence into a unified picture of gene function. When a gene review identifies a transport or catalytic activity with strong evidence, that finding can feed back into Reactome to resolve a BBE.

## Pilot Case: Bile Acid Metabolism (R-HSA-194068)

The bile acid biosynthesis and transport pathway provides an ideal pilot. The pathway involves approximately 15 transport reactions moving bile acid intermediates between four compartment boundaries:

| Boundary | Direction | Substrates | Known Transporters | BBEs |
|----------|-----------|------------|-------------------|------|
| Cytosol → Mitochondria | Import | Cholesterol, C27 intermediates | StAR/STARD1, TSPO (partial) | Several |
| Mitochondria → Cytosol | Export | C27-bile acid intermediates | Unknown | Yes |
| Cytosol → Peroxisome | Import | DHCA-CoA, THCA-CoA | **ABCD3** | **Resolved** |
| Peroxisome → Cytosol | Export | Mature C24 bile acids, CoA | Unknown | Yes |

### ABCD3: The Success Story

The AIGR review of ABCD3 ([PR #285](https://github.com/ai4curation/ai-gene-review/pull/285)) demonstrates the convergence of evidence that can resolve a BBE:

1. **Genetic evidence (PMID:25168382)**: An ABCD3-deficient patient accumulated C27-bile acid intermediates (DHCA, THCA) in plasma, establishing that ABCD3 is required for bile acid maturation. Abcd3 knockout mice confirmed this with elevated hepatic C27 intermediates and reduced C24 bile acids.

2. **Biochemical evidence (PMID:24333844)**: Yeast complementation assays showed ABCD3 preferentially transports hydrophilic substrates including branched-chain fatty acids and dicarboxylic acids, distinguishing it from ABCD1 (which prefers VLCFAs).

3. **Structural evidence (PMID:39223112)**: Cryo-EM structures of ABCD3 captured both inward-facing (substrate-bound) and outward-facing (ATP-bound) conformations. The study identified DHCA-CoA and THCA-CoA as ABCD3-specific substrates — distinct from those of ABCD1 or ABCD2.

4. **Knockout mouse metabolomics (PMID:34564857)**: Abcd3-/- mice showed increased hepatic long-chain dicarboxylic acids, confirming ABCD3's role in dicarboxylic acid import beyond bile acids.

The Reactome entry R-HSA-382575 already captures ABCD3's role in LCFA transport but does not yet reflect the bile acid specificity established by these recent studies. The AIGR review proposes updating this annotation.

### Remaining Gaps

Several bile acid transport steps lack assigned transporters:

- **Mitochondrial export of C27 intermediates**: After CYP27A1 side-chain hydroxylation in the mitochondrial matrix, the C27-bile acid intermediates must return to the cytosol. No transporter has been identified. Candidates might include SLC25 family members.

- **Peroxisomal export of mature bile acids**: After peroxisomal beta-oxidation shortens C27 intermediates to C24 bile acids, the products must exit the peroxisome. The export mechanism is unknown. Passive diffusion of the free acid is possible if thioesterase activity releases CoA inside the peroxisome.

- **Hepatocyte canalicular export**: While ABCB11 (BSEP) is the primary canalicular bile salt export pump, the handling of conjugated vs. unconjugated species at this step has nuances that Reactome BBEs reflect.

## Methodology

The gap-filling workflow proceeds in stages:

**Stage 1 — Identify BBEs.** Query Reactome for reactions annotated as "black box" or lacking a catalyst assignment within a target pathway. Categorize by reaction type (transport, catalysis) and compartment boundary.

**Stage 2 — Candidate identification.** For each BBE, generate candidate genes through:
- GO annotation queries (genes annotated to relevant transport/catalytic terms)
- Expression data (tissue-appropriate expression, e.g., liver for bile acid metabolism)
- Domain architecture (ABC transporter domains, SLC family signatures)
- Literature deep research (AI-assisted search for recent papers identifying new transporters)

**Stage 3 — Evidence convergence.** For each candidate, run a full AIGR review to assess:
- Does direct experimental evidence support the proposed activity?
- Does loss-of-function data show substrate accumulation consistent with the transport step?
- Do structural studies reveal a substrate-binding site compatible with the proposed substrate?
- Is the subcellular localization consistent with the compartment boundary?

**Stage 4 — Confidence assignment and Reactome feedback.** Assign candidates to confidence tiers and report back to Reactome curators for integration.

## Evidence Hierarchy for Transport Annotation

Not all evidence for transporter assignment carries equal weight. The following hierarchy guides confidence assessment, from strongest to weakest:

**Tier 1 — Direct reconstitution.** Purified transporter reconstituted into proteoliposomes demonstrates ATP-dependent (or gradient-driven) transport of the specific substrate. This is the gold standard but exists for relatively few transporters. Example: ABCD1-4 ATPase activity in proteoliposomes (PMID:29397936).

**Tier 2 — Genetic loss-of-function with metabolite accumulation.** Patient mutations or knockout animals show accumulation of the predicted substrate on the source side of the membrane, or depletion on the destination side. Example: ABCD3-deficient patient with C27-bile acid intermediate accumulation (PMID:25168382).

**Tier 3 — Structural mechanism.** Cryo-EM or X-ray structures show the substrate bound in the translocation pathway, with conformational states consistent with an alternating-access mechanism. Example: ABCD3 cryo-EM with phytanoyl-CoA and bile acid intermediates (PMID:39223112).

**Tier 4 — Phylogenetic inference.** Ortholog in a model organism has demonstrated transport activity for the substrate class, transferred by ISS or IBA. Appropriate for well-conserved transport systems but less reliable for substrate specificity.

**Tier 5 — Computational prediction.** InterPro domain-based functional prediction, machine learning classifiers, or docking simulations. Useful for generating candidates but insufficient for annotation without experimental support.

Most resolved BBEs will require evidence from at least two tiers. ABCD3's assignment to bile acid CoA-ester transport draws on Tiers 2, 3, and 4 — a robust combination even without Tier 1 reconstitution data for the bile acid substrates specifically.

## Expansion Targets

Beyond bile acid metabolism, several Reactome pathway areas are rich in BBEs amenable to this approach:

**Cholesterol biosynthesis and trafficking.** Intracellular cholesterol movement between ER, plasma membrane, and mitochondria involves multiple poorly characterized transport steps. NPC1/NPC2 handle lysosomal export, but ER-to-mitochondria cholesterol transfer for steroidogenesis has several candidate mechanisms (StAR, STARD3, membrane contact sites) without definitive transporter assignments.

**Sphingolipid metabolism.** Ceramide transport from ER to Golgi (CERT/CERTL) is partially characterized, but several inter-organelle sphingolipid transport steps lack assigned proteins. The diversity of sphingolipid headgroups creates substrate-specificity questions similar to bile acid transport.

**Mitochondrial metabolite transport.** The SLC25 family (~53 members in humans) includes many poorly characterized transporters. Several Reactome reactions for mitochondrial metabolite exchange cite SLC25 family members tentatively or leave the transporter unassigned. Systematic AIGR reviews of SLC25 family members could resolve multiple BBEs simultaneously.

**Other ABC transporter families.** The ABCD family pilot can extend to ABCG (sterol transport), ABCA (lipid export), and ABCB (peptide/drug transport) families, each containing members with incompletely characterized substrate specificity.

**SLC transporters in peroxisomal metabolism.** Beyond ABC transporters, SLC family members may handle export of peroxisomal beta-oxidation products (acetyl-CoA, shortened fatty acids). The peroxisomal membrane proteome remains incompletely catalogued.

## Related Resources

- [ABCD3 gene review](../genes/human/ABCD3/ABCD3-ai-review.yaml) — Full annotation review with 79 GO annotations assessed
- [PR #285](https://github.com/ai4curation/ai-gene-review/pull/285) — ABCD3 review pull request
- [Reactome R-HSA-382575](https://reactome.org/content/detail/R-HSA-382575) — ABCD1-3 dimers transfer LCFAs
- [Reactome R-HSA-194068](https://reactome.org/content/detail/R-HSA-194068) — Bile acid metabolism pathway
- [Reactome R-HSA-1369062](https://reactome.org/content/detail/R-HSA-1369062) — ABC transporters in lipid homeostasis
