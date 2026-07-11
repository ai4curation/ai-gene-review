---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T18:15:52.216745'
end_time: '2026-07-06T18:43:59.438568'
duration_seconds: 1687.22
template_file: templates/module_research.md.j2
template_variables:
  module_title: Galactose catabolism (Leloir pathway)
  module_summary: The Leloir pathway converts D-galactose to glucose-1-phosphate through
    a conserved UDP-sugar cycle, allowing galactose carbon to enter central carbohydrate
    metabolism. In the canonical four-step route, galactose mutarotase (GALM/aldose
    1-epimerase) equilibrates the beta- and alpha-anomers of D-galactose, galactokinase
    (GALK) phosphorylates alpha-D-galactose to alpha-D-galactose 1-phosphate, galactose-1-phosphate
    uridylyltransferase transfers a UMP group from UDP-glucose to produce glucose-1-phosphate
    and UDP-galactose, and UDP-galactose 4-epimerase interconverts UDP-galactose and
    UDP-glucose. The epimerase step regenerates the UDP-glucose co-substrate used
    by the transferase and also links galactose handling to the UDP-galactose pool
    used in cell-surface and glycoconjugate biosynthesis. Some bacteria and individual
    genomes carry only part of this reference route, so organism-level pathway curation
    should distinguish the strict Leloir steps from side nodes such as phosphoglucomutase,
    UDP-glucose pyrophosphorylase, and polysaccharide/nucleotide-sugar metabolism.
  module_outline: "- Galactose catabolism (Leloir pathway)\n  - 1. anomer preparation\
    \ (mutarotation)\n  - beta-D-galactose to alpha-D-galactose\n    - GALM: galactose\
    \ mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase)\
    \ family (GALM); activity or role: aldose 1-epimerase activity)\n  - 2. phosphorylation\
    \ (committed step)\n  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate\
    \ + ADP\n    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase)\
    \ family (GALK1); activity or role: galactokinase activity)\n  - 3. uridylyl transfer\
    \ (central step)\n  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate\
    \ + UDP-galactose\n    - GALT: galactose-1-phosphate uridylyltransferase (molecular\
    \ player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or\
    \ role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)\n  - 4. UDP-sugar\
    \ recycling (regenerates UDP-glucose for GALT)\n  - UDP-galactose to UDP-glucose\
    \ (reversible)\n    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose\
    \ 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)"
  module_connections: '- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose
    + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the
    substrate phosphorylated by GALK1.

    - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose
    1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose
    1-phosphate from GALK1 is the substrate of GALT.

    - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by
    GALT is epimerised by GALE to UDP-glucose.

    - UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate
    + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated
    by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop
    that makes the pathway catalytic in UDP-glucose.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 69
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: galactose_leloir_pathway-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: galactose_leloir_pathway-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Galactose catabolism (Leloir pathway)

## Working Scope

The Leloir pathway converts D-galactose to glucose-1-phosphate through a conserved UDP-sugar cycle, allowing galactose carbon to enter central carbohydrate metabolism. In the canonical four-step route, galactose mutarotase (GALM/aldose 1-epimerase) equilibrates the beta- and alpha-anomers of D-galactose, galactokinase (GALK) phosphorylates alpha-D-galactose to alpha-D-galactose 1-phosphate, galactose-1-phosphate uridylyltransferase transfers a UMP group from UDP-glucose to produce glucose-1-phosphate and UDP-galactose, and UDP-galactose 4-epimerase interconverts UDP-galactose and UDP-glucose. The epimerase step regenerates the UDP-glucose co-substrate used by the transferase and also links galactose handling to the UDP-galactose pool used in cell-surface and glycoconjugate biosynthesis. Some bacteria and individual genomes carry only part of this reference route, so organism-level pathway curation should distinguish the strict Leloir steps from side nodes such as phosphoglucomutase, UDP-glucose pyrophosphorylase, and polysaccharide/nucleotide-sugar metabolism.

## Provisional Biological Outline

- Galactose catabolism (Leloir pathway)
  - 1. anomer preparation (mutarotation)
  - beta-D-galactose to alpha-D-galactose
    - GALM: galactose mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase) family (GALM); activity or role: aldose 1-epimerase activity)
  - 2. phosphorylation (committed step)
  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP
    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase) family (GALK1); activity or role: galactokinase activity)
  - 3. uridylyl transfer (central step)
  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    - GALT: galactose-1-phosphate uridylyltransferase (molecular player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)
  - 4. UDP-sugar recycling (regenerates UDP-glucose for GALT)
  - UDP-galactose to UDP-glucose (reversible)
    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)

## Known Relationships Among Steps

- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the substrate phosphorylated by GALK1.
- alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose 1-phosphate from GALK1 is the substrate of GALT.
- alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by GALT is epimerised by GALE to UDP-glucose.
- UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop that makes the pathway catalytic in UDP-glucose.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Commissioned Review Brief

## Review Topic

Galactose catabolism (Leloir pathway)

## Working Scope

The Leloir pathway converts D-galactose to glucose-1-phosphate through a conserved UDP-sugar cycle, allowing galactose carbon to enter central carbohydrate metabolism. In the canonical four-step route, galactose mutarotase (GALM/aldose 1-epimerase) equilibrates the beta- and alpha-anomers of D-galactose, galactokinase (GALK) phosphorylates alpha-D-galactose to alpha-D-galactose 1-phosphate, galactose-1-phosphate uridylyltransferase transfers a UMP group from UDP-glucose to produce glucose-1-phosphate and UDP-galactose, and UDP-galactose 4-epimerase interconverts UDP-galactose and UDP-glucose. The epimerase step regenerates the UDP-glucose co-substrate used by the transferase and also links galactose handling to the UDP-galactose pool used in cell-surface and glycoconjugate biosynthesis. Some bacteria and individual genomes carry only part of this reference route, so organism-level pathway curation should distinguish the strict Leloir steps from side nodes such as phosphoglucomutase, UDP-glucose pyrophosphorylase, and polysaccharide/nucleotide-sugar metabolism.

## Provisional Biological Outline

- Galactose catabolism (Leloir pathway)
  - 1. anomer preparation (mutarotation)
  - beta-D-galactose to alpha-D-galactose
    - GALM: galactose mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase) family (GALM); activity or role: aldose 1-epimerase activity)
  - 2. phosphorylation (committed step)
  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP
    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase) family (GALK1); activity or role: galactokinase activity)
  - 3. uridylyl transfer (central step)
  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    - GALT: galactose-1-phosphate uridylyltransferase (molecular player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)
  - 4. UDP-sugar recycling (regenerates UDP-glucose for GALT)
  - UDP-galactose to UDP-glucose (reversible)
    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)

## Known Relationships Among Steps

- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the substrate phosphorylated by GALK1.
- alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose 1-phosphate from GALK1 is the substrate of GALT.
- alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by GALT is epimerised by GALE to UDP-glucose.
- UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop that makes the pathway catalytic in UDP-glucose.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

# Galactose Catabolism via the Leloir Pathway: A Mechanistic and Evolutionary Review

## 1. Executive Summary

The Leloir pathway is the principal route by which D-galactose is converted to glucose-1-phosphate in most organisms, channeling galactose carbon into central carbohydrate metabolism through a conserved UDP-sugar cycle. Named after the Nobel laureate Luis F. Leloir, who elucidated nucleotide-sugar intermediates in the 1950s (figueroa2021nucleotidesugarmetabolismin pages 2-3), the pathway comprises four enzymatic steps: (i) anomeric preparation by galactose mutarotase (GALM), (ii) ATP-dependent phosphorylation by galactokinase (GALK1), (iii) uridylyl transfer by galactose-1-phosphate uridylyltransferase (GALT), and (iv) UDP-sugar recycling by UDP-galactose 4-epimerase (GALE) (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 1-6). The pathway is catalytic in UDP-glucose: GALE regenerates the UDP-glucose co-substrate consumed by GALT, while simultaneously linking galactose handling to the broader nucleotide-sugar pools that supply glycoconjugate biosynthesis (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 47-49). Deficiency in any of the four enzymes causes one of four types of galactosemia, with GALT deficiency (classic galactosemia, type I) being the most clinically severe (haskovic2020pathophysiologyandtargets pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 1-2). Although the core Leloir enzymes are broadly conserved across bacteria, fungi, and animals, substantial evolutionary variation exists: plants have replaced the GALT step with UDP-sugar pyrophosphorylase (althammer2022overexpressionofudp‐sugar pages 1-2, figueroa2021nucleotidesugarmetabolismin pages 7-8), many bacteria and archaea utilize the alternative De Ley–Doudoroff oxidative pathway (peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7), and some fungi employ a parallel oxidoreductive route (peri2024modeldrivenelucidationof pages 10-13, peri2024modeldrivenelucidationof pages 6-10). This review synthesizes current understanding of the Leloir pathway's mechanistic logic, molecular players, evolutionary plasticity, and unresolved questions.

## 2. Definition and Biological Boundaries

### 2.1. What the Leloir Pathway Strictly Encompasses

The Leloir pathway is defined by four sequential enzymatic reactions that convert free D-galactose to glucose-1-phosphate (Glc-1-P) (succoio2022galactosemiabiochemistrymolecular pages 1-2, boulanger2021sugarphosphatetoxicities pages 10-12):

1. **Mutarotation**: β-D-galactose → α-D-galactose (GALM; EC 5.1.3.3)
2. **Phosphorylation**: α-D-galactose + ATP → α-D-galactose-1-phosphate + ADP (GALK1; EC 2.7.1.6)
3. **Uridylyl transfer**: α-D-Gal-1-P + UDP-glucose → Glc-1-P + UDP-galactose (GALT; EC 2.7.7.12)
4. **Epimerization**: UDP-galactose ⇌ UDP-glucose (GALE; EC 5.1.3.2)

Steps 3 and 4 form a catalytic cycle: GALE regenerates the UDP-glucose consumed by GALT, making the pathway catalytic rather than stoichiometric in UDP-glucose (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 47-49).

### 2.2. Boundaries and Neighboring Pathways

Several adjacent metabolic nodes are frequently conflated with the Leloir pathway but should be treated separately:

- **Phosphoglucomutase (PGM)**, which converts the Glc-1-P product to Glc-6-P for glycolysis, is downstream of the pathway proper (boulanger2021sugarphosphatetoxicities pages 10-12).
- **UDP-glucose pyrophosphorylase (UGP/GalU)**, which synthesizes UDP-glucose from UTP and Glc-1-P, supplies the initial UDP-glucose co-substrate but is not a Leloir step *per se* (althammer2022overexpressionofudp‐sugar pages 1-2, figueroa2021nucleotidesugarmetabolismin pages 2-3).
- **Polysaccharide and glycoconjugate biosynthesis** pathways draw upon the UDP-galactose pool maintained by GALE but are biosynthetic rather than catabolic (figueroa2021nucleotidesugarmetabolismin pages 6-7, figueroa2021nucleotidesugarmetabolismin pages 8-9).
- The **galactitol/aldose reductase pathway** is an alternative disposal route that becomes prominent when the Leloir pathway is impaired, producing the toxic polyol galactitol (succoio2022galactosemiabiochemistrymolecular pages 2-4, succoio2022galactosemiabiochemistrymolecular pages 1-2).

### 2.3. Competing Definitions

In budding yeasts, the term "GAL pathway" often encompasses the structural genes (GAL1/GALK, GAL7/GALT, GAL10/GALE) along with their regulatory apparatus (GAL4, GAL80, GAL3), galactose transporters (GAL2), and even melibiose utilization (MEL1) (harrison2022theevolutionof pages 7-12, harrison2022theevolutionof pages 1-7). In bacteria, the *gal* operon includes galactose transport genes (e.g., *galP*, *mglBAC*) and regulatory elements that are not part of the enzymatic Leloir core (boulanger2021sugarphosphatetoxicities pages 10-12). Organism-level pathway curation should therefore distinguish the strict four-enzyme Leloir route from these regulatory and transport layers.

## 3. Mechanistic Overview

### 3.1. Step-by-Step Biochemistry

**Step 1 — Anomeric Preparation (GALM).** Following lactose hydrolysis by β-galactosidase, the released D-galactose is predominantly in the β-anomeric form. GALM accelerates equilibration between β-D-galactose and α-D-galactose, the latter being the preferred substrate of GALK1 (wada2025galactosemutarotasedeficiency pages 1-3, wada2025galactosemutarotasedeficiency pages 3-4). Importantly, spontaneous mutarotation occurs non-enzymatically in aqueous solution, which partially compensates for GALM deficiency—explaining the milder clinical phenotype of type IV galactosemia compared to other forms (wada2025galactosemutarotasedeficiency pages 1-3, wada2025galactosemutarotasedeficiency pages 3-4). GALM belongs to the aldose 1-epimerase family and requires no redox cofactors (succoio2022galactosemiabiochemistrymolecular pages 1-2).

**Step 2 — Phosphorylation (GALK1).** Galactokinase phosphorylates α-D-galactose using ATP to produce α-D-galactose-1-phosphate (Gal-1-P) and ADP. GALK1 is a member of the GHMP kinase superfamily (galactokinase, homoserine kinase, mevalonate kinase, phosphomevalonate kinase) (succoio2022galactosemiabiochemistrymolecular pages 1-2). This is the committed step of the pathway: once phosphorylated, Gal-1-P must proceed through GALT or accumulate with toxic consequences. The human GALK1 crystal structure was solved in 2005 (delnoy2021currentandfuture pages 9-13).

**Step 3 — Uridylyl Transfer (GALT).** GALT catalyzes the central exchange reaction of the pathway through a double-displacement (ping-pong) mechanism. The enzyme is a homodimer (~379 amino acids per monomer) belonging to the histidine triad (HIT) superfamily, characterized by the conserved HXHXQφφ motif (succoio2022galactosemiabiochemistrymolecular pages 1-2, brenner2002hintfhitand pages 8-9). In the first half-reaction, UDP-glucose reacts with the active-site histidine (His166 in *E. coli*) to form a covalent UMP-enzyme intermediate, releasing Glc-1-P as the first product. In the second half-reaction, Gal-1-P attacks the UMP-enzyme intermediate to generate UDP-galactose, completing the transfer. Both steps proceed with inversion of configuration at the α-phosphate, yielding overall retention (brenner2002hintfhitand pages 8-9, brenner2002hintfhitand pages 9-10). The Q168R mutation in *E. coli* GALT reduces both uridylylation and deuridylylation rates by approximately one million-fold, underscoring the critical role of specific residues in the HIT motif (brenner2002hintfhitand pages 10-11).

**Step 4 — UDP-Sugar Recycling (GALE).** GALE catalyzes the reversible epimerization of UDP-galactose to UDP-glucose using a tightly bound NAD+ cofactor, belonging to the short-chain dehydrogenase/reductase (SDR) superfamily (succoio2022galactosemiabiochemistrymolecular pages 1-2). This step is essential for two reasons: it regenerates the UDP-glucose co-substrate that GALT requires, and it serves as a metabolic hub connecting catabolism to biosynthesis. Human GALE additionally catalyzes the interconversion of UDP-N-acetylgalactosamine (UDP-GalNAc) and UDP-N-acetylglucosamine (UDP-GlcNAc), directly linking galactose catabolism to glycoprotein and glycolipid synthesis (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 47-49, haskovic2020pathophysiologyandtargets pages 10-12). The human GALE structure was determined in 2000 (delnoy2021currentandfuture pages 9-13).

### 3.2. Obligatory Versus Conditional Steps

The GALK1-GALT-GALE triad constitutes the obligatory enzymatic core; all three are required for galactose carbon to enter central metabolism via Glc-1-P. GALM, while enhancing the rate of anomer equilibration, is conditionally required because spontaneous mutarotation provides partial compensation (wada2025galactosemutarotasedeficiency pages 1-3, wada2025galactosemutarotasedeficiency pages 3-4). In bacterial systems, some genomes carry only a subset of the Leloir genes, using alternative pathways (such as the De Ley–Doudoroff route) to handle galactose (peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7).

The following table summarizes the four canonical Leloir pathway enzymes, their structural features, and the clinical consequences of their deficiency:

| Enzyme (common name) | Gene (human) | EC Number | Protein Superfamily | Reaction Catalyzed | Cofactors/Co-substrates | Oligomeric State | Galactosemia Type | Key Clinical Features of Deficiency |
|---|---|---|---|---|---|---|---|---|
| Galactose mutarotase / aldose 1-epimerase (GALM) | **GALM** | **5.1.3.3** | Aldose 1-epimerase (mutarotase) family | Reversible anomerization of **β-D-galactose ⇌ α-D-galactose**, supplying the anomer preferred by GALK1 | No redox cofactor required; acts on free galactose anomers | Monomeric enzyme in the canonical pathway description; clinically functions as a soluble single-enzyme step | **Type IV galactosemia** | Usually milder than classic galactosemia; elevated blood galactose with low/normal Gal-1-P, cataracts that are often less frequent and milder than in GALK1 deficiency because spontaneous mutarotation partially compensates; early lactose restriction can prevent or reverse cataracts (succoio2022galactosemiabiochemistrymolecular pages 1-2, wada2025galactosemutarotasedeficiency pages 1-3, wada2025galactosemutarotasedeficiency pages 3-4, sanchezpintos2024clinicalandbiochemical pages 1-2) |
| Galactokinase (GALK1) | **GALK1** | **2.7.1.6** | GHMP kinase superfamily | **α-D-galactose + ATP → α-D-galactose-1-phosphate + ADP** | ATP; substrate is α-anomer of galactose generated by GALM/spontaneous mutarotation | Commonly described as a monomeric small-molecule kinase | **Type II galactosemia** | Classically causes early-onset cataracts due to galactitol accumulation; registry data and reviews indicate some patients also show elevated transaminases, bleeding diathesis, encephalopathy, and occasional developmental issues, though phenotype is generally milder than GALT deficiency (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 41-47, haskovic2020pathophysiologyandtargets pages 1-2, tisa2022theimportanceof pages 4-5, delnoy2021currentandfuture pages 1-6) |
| Galactose-1-phosphate uridylyltransferase (GALT) | **GALT** | **2.7.7.12** | HIT superfamily (histidine triad transferase branch) | **Galactose-1-phosphate + UDP-glucose → glucose-1-phosphate + UDP-galactose** via a ping-pong mechanism with a covalent uridylylated histidine intermediate | UDP-glucose as co-substrate; galactose-1-phosphate; catalytic His in HIT motif forms transient UMP-enzyme intermediate | **Homodimer**; ~379 aa per monomer; active-site architecture involves the subunit interface and HIT motif | **Type I (classic) galactosemia** | Most severe form: neonatal liver dysfunction/failure, jaundice, vomiting, hepatomegaly, feeding intolerance, hypoglycemia, cataracts, susceptibility to *E. coli* sepsis, later cognitive/neurological complications and ovarian insufficiency; pathophysiology involves Gal-1-P accumulation, UDP-hexose imbalance, impaired glycosylation, ER stress, and oxidative stress (succoio2022galactosemiabiochemistrymolecular pages 1-2, haskovic2020pathophysiologyandtargets pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4, panis2024brainfunctionin pages 2-3, tisa2022theimportanceof pages 4-5, tisa2022theimportanceof pages 2-4, brenner2002hintfhitand pages 8-9, brenner2002hintfhitand pages 9-10) |
| UDP-galactose 4-epimerase (GALE) | **GALE** | **5.1.3.2** | Short-chain dehydrogenase/reductase (SDR) superfamily | **UDP-galactose ⇌ UDP-glucose**; also interconverts **UDP-GalNAc ⇌ UDP-GlcNAc**, linking catabolism to glycoconjugate synthesis | Bound **NAD+** cofactor; UDP-hexose and UDP-hexosamine substrates | Commonly treated as a homodimeric soluble epimerase in the Leloir pathway literature | **Type III galactosemia** | Clinical spectrum ranges from peripheral/benign to generalized severe disease; severe deficiency can resemble classic galactosemia with liver disease, hypotonia, developmental delay, and neurological involvement; deficiency perturbs UDP-sugar balance and glycosylation in addition to blocking UDP-glucose regeneration (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 41-47, haskovic2020pathophysiologyandtargets pages 1-2, tisa2022theimportanceof pages 4-5, delnoy2021currentandfuture pages 47-49, haskovic2020pathophysiologyandtargets pages 10-12) |


*Table: This table summarizes the four canonical Leloir pathway enzymes, emphasizing their biochemical roles, structural classes, and the clinical phenotypes associated with deficiency. It is useful for distinguishing the core pathway steps from related sugar-nucleotide and toxicity pathways.*

## 4. Major Molecular Players and Active Assemblies

### 4.1. GALM — Galactose Mutarotase

GALM is a monomeric enzyme of the aldose 1-epimerase family that catalyzes the reversible interconversion between β- and α-anomers of D-galactose without requiring cofactors (succoio2022galactosemiabiochemistrymolecular pages 1-2). It was the last Leloir pathway enzyme to be linked to human disease: GALM deficiency was defined as type IV galactosemia in 2019 (wada2025galactosemutarotasedeficiency pages 1-3). A nationwide survey in Japan and other studies have identified a spectrum of GALM variants, with affected individuals typically showing elevated blood galactose, low galactose-1-phosphate levels (distinguishing it from GALT deficiency), and mildly elevated urinary galactitol (wada2025galactosemutarotasedeficiency pages 3-4). Cataracts are the primary clinical concern, but these occur less frequently and are generally milder than in GALK1 deficiency, and can be prevented or reversed by early lactose restriction (wada2025galactosemutarotasedeficiency pages 1-3, sanchezpintos2024clinicalandbiochemical pages 1-2). Two 9-year-old twins with a novel complete exon 4 deletion in GALM remained asymptomatic with normal growth and intellectual development after 7 years of partial dietary liberalization (sanchezpintos2024clinicalandbiochemical pages 1-2).

### 4.2. GALK1 — Galactokinase

GALK1 belongs to the GHMP kinase superfamily and catalyzes the ATP-dependent phosphorylation of α-D-galactose (succoio2022galactosemiabiochemistrymolecular pages 1-2). Deficiency causes type II galactosemia, classically presenting with early-onset cataracts due to galactitol accumulation via the aldose reductase pathway. Data from the GalNet registry (53 patients across 11 countries) revealed that beyond cataract, GALK1 deficiency may include neonatal elevation of transaminases (25.5%), bleeding diathesis (8.1% vs 2.17–5.9% in general population), and encephalopathy (3.9% vs 0.3%), suggesting a broader phenotypic spectrum than previously appreciated (tisa2022theimportanceof pages 4-5). Notably, GALK1 is now a therapeutic target: inhibition of GALK1 prevents the formation of Gal-1-P, theoretically reducing the toxic metabolite burden in classic galactosemia patients. Several classes of GALK1 inhibitors, including phenylsulfonamides and non-competitive inhibitors, have been identified through fragment screening and virtual screening approaches (succoio2022galactosemiabiochemistrymolecular pages 12-13, succoio2022galactosemiabiochemistrymolecular pages 8-9).

### 4.3. GALT — Galactose-1-Phosphate Uridylyltransferase

GALT is a homodimeric enzyme of the HIT superfamily with the active site located at the subunit interface (succoio2022galactosemiabiochemistrymolecular pages 1-2, brenner2002hintfhitand pages 8-9). Its ping-pong mechanism is remarkably symmetrical: the same active-site residues that recognize the Glc-1-P leaving group subsequently facilitate the return of Gal-1-P as the attacking nucleophile to reclaim the nucleotide as UDP-galactose (brenner2002hintfhitand pages 9-10). Crystallographic studies show that glucose and galactose bind at identical sites within the active site, with the enzyme displaying broad hexose-1-phosphate specificity constrained by the HIT motif architecture (brenner2002hintfhitand pages 9-10). The human GALT structure has not been solved directly, but homology models based on the *E. coli* crystal structure (determined at 1.8 Å resolution) have guided understanding of disease-associated variants (delnoy2021currentandfuture pages 9-13). Over 200 mutations have been identified in the human GALT gene, with the Q188R and K285N variants among the most common in European populations (delnoy2021currentandfuture pages 6-9). GALT deficiency causes classic galactosemia (type I), the most severe form, which is potentially lethal in the neonatal period and affects 85% of patients with brain dysfunction despite dietary treatment (haskovic2020pathophysiologyandtargets pages 1-2, panis2024brainfunctionin pages 2-3).

### 4.4. GALE — UDP-Galactose 4-Epimerase

GALE is a member of the SDR superfamily that uses tightly bound NAD+ as a cofactor for the reversible epimerization at the C-4 position of the hexose moiety of UDP-galactose (succoio2022galactosemiabiochemistrymolecular pages 1-2). Its dual substrate specificity—acting on both UDP-Gal/UDP-Glc and UDP-GalNAc/UDP-GlcNAc—makes it a critical metabolic hub linking catabolism to glycoconjugate biosynthesis (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 47-49, haskovic2020pathophysiologyandtargets pages 10-12). Studies in *C. elegans* and *Drosophila* have demonstrated that both enzymatic activities are essential for normal development and survival, with loss of either activity leading to metabolic abnormalities, reduced lifespan under galactose exposure, and reproductive impairment (haskovic2020pathophysiologyandtargets pages 10-12). GALE deficiency (type III galactosemia) presents as a clinical continuum, ranging from a benign peripheral form (restricted to red blood cells) to a generalized severe form resembling classic galactosemia with liver disease, hypotonia, and developmental delay (tisa2022theimportanceof pages 4-5, delnoy2021currentandfuture pages 6-9).

## 5. Evolutionary and Cell-Biological Variation

### 5.1. Variation in Budding Yeasts

The yeast GAL pathway has become a paradigm for studying eukaryotic metabolic gene evolution. In *Saccharomyces cerevisiae*, the core structural genes GAL1 (galactokinase), GAL7 (GALT), and GAL10 (a bifunctional mutarotase-epimerase) are physically clustered, and about half of ~350 surveyed yeast species contain these three genes and can utilize galactose (harrison2022theevolutionof pages 7-12). The GAL1-GAL7-GAL10 cluster has arisen independently at least twice in budding yeasts—once in the ancestor of *S. cerevisiae* and *C. albicans*, and again in *Lipomyces* (harrison2022theevolutionof pages 7-12). Some species possess "giant" GAL clusters containing additional genes such as GAL4, MEL1, GAL2, and HGT1, as seen in *Torulaspora* species (harrison2022theevolutionof pages 7-12, harrison2022theevolutionof pages 26-29).

A striking feature of GAL pathway evolution is the role of horizontal gene transfer (HGT). CUG-Ser1 clade yeasts have served as donors of GAL clusters to other budding yeast lineages and even to distantly related fission yeasts (harrison2022theevolutionof pages 17-22, harrison2022theevolutionof pages 12-17). Within *S. cerevisiae*, analysis of over 1,000 isolates revealed three distinct combinations of highly diverged GAL alleles, suggesting ancient balancing selection or introgression that maintains multiple pathway variants within a single species (harrison2022theevolutionof pages 17-22). *S. kudriavzevii* populations show extreme intraspecific variation: European isolates retain functional GAL pathways while Eastern Asian isolates possess only pseudogenes, representing local adaptation (harrison2022theevolutionof pages 17-22).

Regulatory networks also show remarkable divergence. *S. cerevisiae* employs a Gal3-Gal80-Gal4 regulatory system, *K. lactis* uses a bifunctional Gal1-Gal80-Lac9 mechanism, and *C. albicans* uses Rep1-Cga1 regulation (peri2024auniquemetabolic pages 13-16). *Candida intermedia* possesses a unique "GALLAC" cluster containing duplicated GAL1 and GAL10 genes alongside the transcriptional activator LAC9 and an aldose reductase (XYL1), representing a new example of metabolic network rewiring linked to efficient lactose assimilation (peri2024auniquemetabolic pages 2-6, peri2024auniquemetabolic pages 6-8).

### 5.2. Plants: A Modified Leloir Route

Plants represent a particularly notable departure from the canonical Leloir pathway. While they possess galactokinase and UDP-galactose 4-epimerase, they appear to lack or have very limited canonical GALT activity (althammer2022overexpressionofudp‐sugar pages 1-2, figueroa2021nucleotidesugarmetabolismin pages 7-8). Instead, plants employ UDP-sugar pyrophosphorylase (USP) to convert Gal-1-P directly to UDP-galactose using UTP (althammer2022overexpressionofudp‐sugar pages 1-2, figueroa2021nucleotidesugarmetabolismin pages 7-8). The Arabidopsis USP enzyme both relieves Gal-1-P accumulation and generates UDP-Gal for glycosylation reactions needed in cell wall synthesis; loss-of-function mutations in the single Arabidopsis USP gene cause sterility due to abnormal pollen development (figueroa2021nucleotidesugarmetabolismin pages 7-8, figueroa2021nucleotidesugarmetabolismin pages 6-7). Arabidopsis also possesses five genes encoding UDP-Glc 4-epimerase isoforms, with isoforms 2 and 4 specifically providing UDP-Gal for cell wall polysaccharide biosynthesis (figueroa2021nucleotidesugarmetabolismin pages 6-7). Notably, plants exhibit galactose toxicity even without inherited enzyme defects, unlike the enzyme-deficiency-dependent galactosemia paradigm in animals (althammer2022overexpressionofudp‐sugar pages 1-2).

### 5.3. Bacteria and Archaea

In bacteria, the Leloir pathway (galK, galT, galE) and the De Ley–Doudoroff (DLD) pathway represent two fundamentally different strategies for galactose catabolism. The Leloir pathway uses phosphorylation and cyclic UDP-sugar reactions, while the DLD pathway follows a linear oxidative route converting galactose to galactonate, then through 2-keto-3-deoxygalactonate (KDGal) intermediates to pyruvate and glyceraldehyde-3-phosphate (peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7). Among haloarchaea, the DLD pathway is more prevalent, being found in six of the ten genomes analyzed, while the Leloir pathway was unique to *H. utahensis* (anderson2011novelinsightsinto pages 6-7). Organisms such as *Pseudomonas putida* naturally lack the Leloir pathway but can be engineered to utilize galactose via the DLD route (peabody2019engineeredpseudomonasputida pages 1-2).

### 5.4. Filamentous Fungi: Oxidoreductive Pathway

Many filamentous fungi and some non-conventional yeasts possess a parallel oxidoreductive pathway that operates alongside the Leloir pathway. In this route, galactose is reduced to galactitol by aldose reductase, then further oxidized and reduced through L-xylo-3-hexulose to D-sorbitol, eventually feeding into glycolysis as D-fructose (peri2024modeldrivenelucidationof pages 6-10). In *Sungouiella intermedia*, the Leloir pathway dominates galactose metabolism under optimal growth conditions (carrying flux in >99% of simulations), but dual pathway usage becomes common under oxygen-limited and nitrogen-limited conditions (peri2024modeldrivenelucidationof pages 10-13). The oxidoreductive pathway provides only a modest ~3% decrease in simulated biomass yield compared to the Leloir pathway, suggesting it functions primarily for redox balancing and carbon overflow rather than as an energetically equivalent alternative (peri2024modeldrivenelucidationof pages 10-13).

The following table compares the major galactose catabolic pathways across organisms:

| Pathway Name | Key Enzymes | Primary Organisms | Substrate Entry Point | End Products | Cofactors | Distinguishing Features |
|---|---|---|---|---|---|---|
| Leloir pathway | GALM (optional in some systems due to spontaneous mutarotation), GALK/GALK1, GALT/GalT, GALE/GalE; often followed downstream by phosphoglucomutase outside the strict core pathway | Animals, many bacteria, many fungi/yeasts; also present in some archaea such as *Haloferax/Halorubrum*-type systems, though not universal (succoio2022galactosemiabiochemistrymolecular pages 1-2, peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7) | Free D-galactose enters as β/α anomer; committed entry is phosphorylation of α-D-galactose to galactose-1-phosphate | Glucose-1-phosphate + UDP-galactose; carbon then enters central metabolism after Glc-1-P conversion to Glc-6-P; UDP-glucose is regenerated by GALE (succoio2022galactosemiabiochemistrymolecular pages 1-2, peabody2019engineeredpseudomonasputida pages 1-2, boulanger2021sugarphosphatetoxicities pages 10-12) | ATP for GALK; UDP-glucose as GALT co-substrate; NAD+ for GALE; no redox cofactor for GALM (succoio2022galactosemiabiochemistrymolecular pages 1-2) | Conserved UDP-sugar cycle; catalytic in UDP-glucose because GALE regenerates the GALT co-substrate; tightly linked to nucleotide-sugar homeostasis and glycoconjugate biosynthesis via UDP-galactose/UDP-glucose pools (succoio2022galactosemiabiochemistrymolecular pages 1-2, delnoy2021currentandfuture pages 47-49) |
| De Ley-Doudoroff pathway | Galactose dehydrogenase, galactonate dehydratase, KDG/KDGal kinase, KDG(P)/KDPGal aldolase; in some descriptions includes transport and oxidation steps to galactonate | Diverse bacteria and some archaea; engineered into *Pseudomonas putida* and filamentous fungi; naturally prevalent in several haloarchaea (peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7, wang2021transcriptionalprofilingof pages 8-10) | Free galactose enters a linear oxidative route and is converted to galactonate rather than to galactose-1-phosphate | Pyruvate + glyceraldehyde-3-phosphate via 2-keto-3-deoxygalactonate intermediates (peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7, wang2021transcriptionalprofilingof pages 8-10) | Redox cofactor for the initial dehydrogenase step; ATP for KDG/KDGal kinase; no UDP-sugar cycle required (peabody2019engineeredpseudomonasputida pages 1-2, wang2021transcriptionalprofilingof pages 8-10) | Linear oxidative pathway analogous to the Entner-Doudoroff logic for glucose; bypasses galactose-1-phosphate and UDP-sugar intermediates entirely, distinguishing it sharply from the canonical Leloir pathway (peabody2019engineeredpseudomonasputida pages 1-2, anderson2011novelinsightsinto pages 6-7) |
| Oxidoreductive pathway | Aldose reductase (e.g., Xyl1-type), galactitol dehydrogenase, L-xylo-3-hexulose reductase, downstream steps funneling through sorbitol/fructose to glycolysis | Filamentous fungi and some nonconventional yeasts, including *Myceliophthora thermophila* and *Sungouiella intermedia*; often coexists with the Leloir pathway rather than replacing it completely (peri2024modeldrivenelucidationof pages 10-13, peri2024modeldrivenelucidationof pages 6-10, wang2021transcriptionalprofilingof pages 8-10, peri2024modeldrivenelucidationof pages 1-4) | Free galactose is reduced to galactitol rather than phosphorylated first | D-fructose-derived intermediates entering glycolysis; galactitol may also be secreted as an overflow metabolite under some conditions (peri2024modeldrivenelucidationof pages 6-10, peri2024modeldrivenelucidationof pages 1-4) | NADPH and/or NADH depending on enzyme specificity; in *S. intermedia*, upstream aldose reductase can use both NADH and NADPH, with NADH favored in most simulations (peri2024modeldrivenelucidationof pages 10-13, peri2024modeldrivenelucidationof pages 6-10) | Redox-balancing route; often condition-dependent and activated alongside Leloir flux, especially under oxygen or nitrogen limitation; can support growth but is usually not the stoichiometrically preferred route when the Leloir pathway is fully functional (peri2024modeldrivenelucidationof pages 10-13, peri2024modeldrivenelucidationof pages 6-10) |
| Plant modified Leloir pathway | Galactokinase, UDP-sugar pyrophosphorylase (USP/UDP-sugar PPase) replacing the canonical GALT step, UDP-glucose 4-epimerase/UGE; multiple plant UGE isoforms contribute to UDP-galactose supply | Plants, especially exemplified by *Arabidopsis thaliana*; differs from the canonical animal/fungal/bacterial Leloir route (figueroa2021nucleotidesugarmetabolismin pages 6-7, althammer2022overexpressionofudp‐sugar pages 1-2, figueroa2021nucleotidesugarmetabolismin pages 7-8) | Free galactose is phosphorylated to galactose-1-phosphate, which is then converted through USP rather than classical GALT | UDP-galactose and UDP-glucose pools used heavily for cell wall, glycoprotein, glycolipid, and galactolipid biosynthesis rather than only energy metabolism (figueroa2021nucleotidesugarmetabolismin pages 6-7, figueroa2021nucleotidesugarmetabolismin pages 8-9, figueroa2021nucleotidesugarmetabolismin pages 3-4) | ATP for galactokinase; UTP for USP-dependent nucleotide-sugar formation; NAD+ not central to the USP replacement step, though UGE catalysis supports UDP-Glc/UDP-Gal interconversion (figueroa2021nucleotidesugarmetabolismin pages 6-7, althammer2022overexpressionofudp‐sugar pages 1-2) | Plants appear to lack or have very limited canonical GALT activity; USP both relieves Gal-1-P accumulation and generates UDP-Gal for glycosylation, linking galactose handling directly to cell wall and developmental processes. Plant galactose toxicity can occur even without inherited Leloir-enzyme defects, unlike the classic galactosemia paradigm in animals (althammer2022overexpressionofudp‐sugar pages 1-2, figueroa2021nucleotidesugarmetabolismin pages 7-8, figueroa2021nucleotidesugarmetabolismin pages 6-7) |


*Table: This table compares the major known galactose catabolic routes across organisms, highlighting how the canonical Leloir pathway differs from the De Ley-Doudoroff, oxidoreductive, and plant-modified routes in enzymes, cofactors, and metabolic logic. It is useful for defining pathway boundaries and avoiding conflation of distinct galactose utilization strategies.*

## 6. Constraints, Dependencies, and Failure Modes

### 6.1. Obligatory Ordering

The Leloir pathway operates with strict sequential logic. Galactose must be phosphorylated by GALK1 before it can serve as a substrate for GALT; the resulting Gal-1-P cannot be processed by any other enzyme in the Leloir core. GALT requires UDP-glucose as a co-substrate, which must be supplied initially by UDP-glucose pyrophosphorylase and subsequently regenerated by GALE (succoio2022galactosemiabiochemistrymolecular pages 1-2). This creates an inherent dependency: without functional GALE, the GALT reaction would consume all available UDP-glucose and halt.

### 6.2. Sugar-Phosphate Toxicity

The most clinically significant constraint is the toxicity of accumulated Gal-1-P when GALT is non-functional. In *E. coli* galT mutants, Gal-1-P causes feedback inhibition of GalK, depletes ATP, and impairs UTP recycling (boulanger2021sugarphosphatetoxicities pages 12-14). Gal-1-P also acts as an anti-inducer, preventing derepression of glycerol utilization genes and rendering glycerol unable to rescue galT mutants (boulanger2021sugarphosphatetoxicities pages 3-6). In galE mutants, UDP-Gal accumulation traps uridine nucleotides, depleting UTP/CTP pools and starving the cell of UDP-GlcNAc needed for peptidoglycan synthesis, ultimately causing cell lysis—making galE deficiency the most acutely lethal form in bacteria (boulanger2021sugarphosphatetoxicities pages 12-14, boulanger2021sugarphosphatetoxicities pages 14-15).

In humans, GALT deficiency causes classic galactosemia with pathophysiology that extends beyond simple metabolite accumulation. The contributing mechanisms include: (i) Gal-1-P accumulation with inhibition of galactosyltransferases, (ii) UDP-hexose pool imbalance leading to impaired glycosylation, (iii) endoplasmic reticulum stress, (iv) oxidative stress from galactitol accumulation via the aldose reductase pathway, and (v) altered signaling pathways (haskovic2020pathophysiologyandtargets pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4). Critically, even with strict dietary galactose restriction, endogenous galactose synthesis continues to generate toxic phosphates, explaining why the diet fails to prevent long-term neurological and reproductive complications in most patients (boulanger2021sugarphosphatetoxicities pages 12-14, panis2024brainfunctionin pages 2-3).

### 6.3. GALE as a Metabolic Hub

The dual substrate specificity of GALE creates a point of vulnerability: its loss not only blocks UDP-glucose regeneration for GALT but also disrupts the UDP-GalNAc/UDP-GlcNAc balance essential for glycoprotein and glycolipid biosynthesis (boulanger2021sugarphosphatetoxicities pages 12-14, haskovic2020pathophysiologyandtargets pages 10-12). In *C. elegans*, reduced GALE activity causes increased UDP-Gal and decreased UDP-GalNAc levels, resulting in developmental defects attributed to impaired glycosylation rather than simple metabolite accumulation (haskovic2020pathophysiologyandtargets pages 10-12). This observation suggests that imbalanced nucleotide sugar ratios, rather than individual substrate accumulation, may drive the pathological phenotypes of GALE deficiency.

### 6.4. Directionality

Of the four Leloir enzymes, GALK1 is the only one that operates essentially irreversibly under physiological conditions. GALM, GALT, and GALE can all catalyze their reactions in both directions depending on substrate concentrations (panis2024brainfunctionin pages 2-3). This bidirectionality is particularly important for GALE, which can generate UDP-galactose from UDP-glucose when biosynthetic demand requires it, independent of dietary galactose supply. This has implications for treatment: dietary galactose restriction in GALE-deficient patients must be carefully balanced because GALE is also the source of UDP-galactose needed for essential glycosylation reactions (delnoy2021currentandfuture pages 9-13, delnoy2021currentandfuture pages 6-9).

## 7. Controversies and Open Questions

### 7.1. The Pathophysiology Puzzle

Despite decades of research, the precise mechanisms underlying long-term complications in classic galactosemia remain incompletely understood. While Gal-1-P was historically considered the sole pathophysiological agent, current evidence indicates that multiple factors contribute, including UDP-hexose alterations, impaired glycosylation, ER stress, altered signaling pathways, and oxidative stress (haskovic2020pathophysiologyandtargets pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4). The relative contribution of each mechanism, and why the diet fails to prevent neurological and reproductive complications in most patients, remains a central open question.

### 7.2. Endogenous Galactose Production

Mammals synthesize galactose endogenously, which continues to feed the Leloir pathway even under strict dietary restriction. The source and magnitude of endogenous galactose production, and whether it can be therapeutically targeted, is an active area of investigation. This endogenous production may explain why brain dysfunction affects 85% of classic galactosemia patients despite treatment (panis2024brainfunctionin pages 2-3, boulanger2021sugarphosphatetoxicities pages 12-14).

### 7.3. GALM Deficiency: How Benign?

GALM deficiency was only defined in 2019 and remains the most recently described galactosemia type. The milder phenotype—attributable to spontaneous mutarotation compensation—raises questions about whether it warrants inclusion in newborn screening programs and what the appropriate dietary management should be (wada2025galactosemutarotasedeficiency pages 1-3, sanchezpintos2024clinicalandbiochemical pages 1-2). The fact that two affected twins remained asymptomatic after 7 years of partial dietary liberalization is encouraging but not yet sufficient to establish definitive guidelines (sanchezpintos2024clinicalandbiochemical pages 1-2).

### 7.4. Evolutionary Questions

The repeated independent clustering of GAL genes in fungi, the multiple instances of HGT-mediated pathway acquisition, and the existence of three distinct allelic combinations within *S. cerevisiae* suggest that the Leloir pathway is subject to strong and complex selective pressures (harrison2022theevolutionof pages 7-12, harrison2022theevolutionof pages 17-22, harrison2022theevolutionof pages 26-29). The selective advantage of gene clustering—possibly related to preventing toxic intermediate accumulation through co-regulation—remains debated (harrison2022theevolutionof pages 26-29). The deep evolutionary origin of the Leloir pathway enzymes, which belong to ancient protein superfamilies (HIT, GHMP, SDR), suggests the pathway is among the oldest metabolic modules, though the question of whether the Leloir route preceded the DLD pathway or vice versa in the last common ancestor has not been resolved.

### 7.5. Emerging Therapies

Several novel therapeutic approaches are under development. AAV9-mediated GALT gene therapy has shown promise in preclinical models, reducing galactose metabolites and preventing cataracts (succoio2022galactosemiabiochemistrymolecular pages 12-13, succoio2022galactosemiabiochemistrymolecular pages 8-9). mRNA-based therapies using lipid nanoparticles have restored GALT activity and reduced mortality in mouse and zebrafish models (succoio2022galactosemiabiochemistrymolecular pages 8-9). GALK1 inhibitors aim to prevent Gal-1-P formation upstream of the block (succoio2022galactosemiabiochemistrymolecular pages 12-13, succoio2022galactosemiabiochemistrymolecular pages 8-9). Pharmacological chaperones that correct protein misfolding in GALT variants represent a personalized medicine approach but are limited to specific genotypes (succoio2022galactosemiabiochemistrymolecular pages 12-13, banford2021galactosemiatowardspharmacological pages 11-13, rodrigues2022currentunderstandingon pages 15-16). The AT-007 aldose reductase inhibitor is currently in clinical trials for galactosemia (succoio2022galactosemiabiochemistrymolecular pages 6-8). Whether any of these approaches will successfully prevent the long-term complications that dietary restriction cannot remains to be determined.

## 8. Key References

The evidence for this review draws on the following primary sources:

- Succoio et al. (2022) *Biomolecules* 12:968. Comprehensive review of galactosemia biochemistry, molecular genetics, screening, and treatment (succoio2022galactosemiabiochemistrymolecular pages 1-2, succoio2022galactosemiabiochemistrymolecular pages 2-4, succoio2022galactosemiabiochemistrymolecular pages 12-13, succoio2022galactosemiabiochemistrymolecular pages 8-9).
- Harrison et al. (2022) *Trends in Genetics* 38:97–106. Evolution of the GAL utilization pathway in budding yeasts (harrison2022theevolutionof pages 7-12, harrison2022theevolutionof pages 17-22, harrison2022theevolutionof pages 12-17, harrison2022theevolutionof pages 1-7, harrison2022theevolutionof pages 26-29).
- Haskovic et al. (2020) *J. Inherited Metabolic Disease* 43:392–408. Systematic review of pathophysiology and treatment targets in galactosemia (haskovic2020pathophysiologyandtargets pages 1-2, haskovic2020pathophysiologyandtargets pages 10-12).
- Wada et al. (2025) *J. Human Genetics*. Review of galactose mutarotase deficiency as type IV galactosemia (wada2025galactosemutarotasedeficiency pages 1-3, wada2025galactosemutarotasedeficiency pages 3-4).
- Delnoy et al. (2021) *J. Personalized Medicine* 11:75. Current and future treatments for classic galactosemia (delnoy2021currentandfuture pages 9-13, delnoy2021currentandfuture pages 1-6, delnoy2021currentandfuture pages 41-47, delnoy2021currentandfuture pages 6-9, delnoy2021currentandfuture pages 47-49).
- Panis et al. (2024) *Frontiers in Genetics* 15:1355962. Brain function in classic galactosemia (panis2024brainfunctionin pages 2-3).
- Brenner (2002) *Biochemistry* 41:9003–9014. HIT superfamily structure, evolution, and mechanism including GALT (brenner2002hintfhitand pages 8-9, brenner2002hintfhitand pages 9-10, brenner2002hintfhitand pages 10-11).
- Boulanger et al. (2021) *Microbiol. Mol. Biol. Rev.* 85:e00123-21. Sugar-phosphate toxicities including galactose metabolism (boulanger2021sugarphosphatetoxicities pages 12-14, boulanger2021sugarphosphatetoxicities pages 3-6, boulanger2021sugarphosphatetoxicities pages 14-15, boulanger2021sugarphosphatetoxicities pages 10-12).
- Figueroa et al. (2021) *J. Experimental Botany* 72:4053–4067. Nucleotide-sugar metabolism in plants and Leloir's legacy (figueroa2021nucleotidesugarmetabolismin pages 6-7, figueroa2021nucleotidesugarmetabolismin pages 8-9, figueroa2021nucleotidesugarmetabolismin pages 7-8, figueroa2021nucleotidesugarmetabolismin pages 3-4, figueroa2021nucleotidesugarmetabolismin pages 2-3, figueroa2021nucleotidesugarmetabolismin pages 12-13).
- Althammer et al. (2022) *The Plant Journal* 109:1416–1426. UDP-sugar pyrophosphorylase and galactose toxicity in plants (althammer2022overexpressionofudp‐sugar pages 1-2).
- Peri et al. (2024) *Applied and Environmental Microbiology* 90(10). GALLAC cluster in *C. intermedia* (peri2024auniquemetabolic pages 13-16, peri2024auniquemetabolic pages 2-6, peri2024auniquemetabolic pages 6-8).
- Peri et al. (2024) *bioRxiv* preprint. Oxidoreductive galactose pathway in *S. intermedia* (peri2024modeldrivenelucidationof pages 10-13, peri2024modeldrivenelucidationof pages 6-10, peri2024modeldrivenelucidationof pages 1-4).
- Peabody et al. (2019) *Biotechnology for Biofuels* 12. De Ley–Doudoroff pathway engineering in *P. putida* (peabody2019engineeredpseudomonasputida pages 1-2).
- Anderson et al. (2011) *PLoS ONE* 6:e20237. Galactose metabolism diversity in haloarchaea (anderson2011novelinsightsinto pages 6-7).
- Sánchez-Pintos et al. (2024) *BMC Pediatrics* 24. Clinical follow-up of GALM deficiency cases (sanchezpintos2024clinicalandbiochemical pages 1-2).
- Tișa et al. (2022) *Nutrients* 15:10. Neonatal screening for galactosemia (tisa2022theimportanceof pages 4-5, tisa2022theimportanceof pages 2-4, tisa2022theimportanceof pages 11-12).
- Banford et al. (2021) *J. Personalized Medicine* 11:106. Pharmacological chaperones for galactosemia (banford2021galactosemiatowardspharmacological pages 11-13).
- Quispe et al. (2022) *Current Research in Biotechnology* 4:350–358. Archaeal nucleotide sugar epimerases (quispe2022explorationofarchaeal pages 4-5).

References

1. (figueroa2021nucleotidesugarmetabolismin pages 2-3): Carlos M Figueroa, John E Lunn, and Alberto A Iglesias. Nucleotide-sugar metabolism in plants: the legacy of luis f. leloir. Journal of experimental botany, 72:4053-4067, May 2021. URL: https://doi.org/10.1093/jxb/erab109, doi:10.1093/jxb/erab109. This article has 56 citations and is from a domain leading peer-reviewed journal.

2. (succoio2022galactosemiabiochemistrymolecular pages 1-2): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

3. (delnoy2021currentandfuture pages 1-6): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

4. (delnoy2021currentandfuture pages 47-49): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

5. (haskovic2020pathophysiologyandtargets pages 1-2): Minela Haskovic, Ana I. Coelho, Jörgen Bierau, Jo M. Vanoevelen, Laura K. M. Steinbusch, Luc J. I. Zimmermann, Eduardo Villamor‐Martinez, Gerard T. Berry, and M. Estela Rubio‐Gozalbo. Pathophysiology and targets for treatment in hereditary galactosemia: a systematic review of animal and cellular models. Journal of Inherited Metabolic Disease, 43:392-408, Jan 2020. URL: https://doi.org/10.1002/jimd.12202, doi:10.1002/jimd.12202. This article has 61 citations and is from a peer-reviewed journal.

6. (althammer2022overexpressionofudp‐sugar pages 1-2): Martina Althammer, Christof Regl, Klaus Herburger, Constantin Blöchl, Elena Voglas, Christian G. Huber, and Raimund Tenhaken. Overexpression of udp‐sugar pyrophosphorylase leads to higher sensitivity towards galactose, providing new insights into the mechanisms of galactose toxicity in plants. Jan 2022. URL: https://doi.org/10.1111/tpj.15638, doi:10.1111/tpj.15638. This article has 14 citations.

7. (figueroa2021nucleotidesugarmetabolismin pages 7-8): Carlos M Figueroa, John E Lunn, and Alberto A Iglesias. Nucleotide-sugar metabolism in plants: the legacy of luis f. leloir. Journal of experimental botany, 72:4053-4067, May 2021. URL: https://doi.org/10.1093/jxb/erab109, doi:10.1093/jxb/erab109. This article has 56 citations and is from a domain leading peer-reviewed journal.

8. (peabody2019engineeredpseudomonasputida pages 1-2): George L. Peabody, Joshua R. Elmore, Jessica Martinez-Baird, and Adam M. Guss. Engineered pseudomonas putida kt2440 co-utilizes galactose and glucose. Biotechnology for Biofuels, Dec 2019. URL: https://doi.org/10.1186/s13068-019-1627-0, doi:10.1186/s13068-019-1627-0. This article has 32 citations.

9. (anderson2011novelinsightsinto pages 6-7): Iain Anderson, Carmen Scheuner, Markus Göker, Kostas Mavromatis, Sean D. Hooper, Iris Porat, Hans-Peter Klenk, Natalia Ivanova, and Nikos Kyrpides. Novel insights into the diversity of catabolic metabolism from ten haloarchaeal genomes. PLoS ONE, 6:e20237, May 2011. URL: https://doi.org/10.1371/journal.pone.0020237, doi:10.1371/journal.pone.0020237. This article has 105 citations and is from a peer-reviewed journal.

10. (peri2024modeldrivenelucidationof pages 10-13): Kameshwara. V. R. Peri, Ivan Domenzain, Hanna D Alalam, Abril Valverde Rascon, Jens Nielsen, and Cecilia Geijer. Model-driven elucidation of lactose and galactose metabolism via oxidoreductive pathway in sungouiella intermedia for cell factory applications. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.19.624258, doi:10.1101/2024.11.19.624258. This article has 0 citations.

11. (peri2024modeldrivenelucidationof pages 6-10): Kameshwara. V. R. Peri, Ivan Domenzain, Hanna D Alalam, Abril Valverde Rascon, Jens Nielsen, and Cecilia Geijer. Model-driven elucidation of lactose and galactose metabolism via oxidoreductive pathway in sungouiella intermedia for cell factory applications. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.19.624258, doi:10.1101/2024.11.19.624258. This article has 0 citations.

12. (boulanger2021sugarphosphatetoxicities pages 10-12): Erin F. Boulanger, Anice Sabag-Daigle, Pankajavalli Thirugnanasambantham, Venkat Gopalan, and Brian M. M. Ahmer. Sugar-phosphate toxicities. Dec 2021. URL: https://doi.org/10.1128/mmbr.00123-21, doi:10.1128/mmbr.00123-21. This article has 66 citations and is from a domain leading peer-reviewed journal.

13. (figueroa2021nucleotidesugarmetabolismin pages 6-7): Carlos M Figueroa, John E Lunn, and Alberto A Iglesias. Nucleotide-sugar metabolism in plants: the legacy of luis f. leloir. Journal of experimental botany, 72:4053-4067, May 2021. URL: https://doi.org/10.1093/jxb/erab109, doi:10.1093/jxb/erab109. This article has 56 citations and is from a domain leading peer-reviewed journal.

14. (figueroa2021nucleotidesugarmetabolismin pages 8-9): Carlos M Figueroa, John E Lunn, and Alberto A Iglesias. Nucleotide-sugar metabolism in plants: the legacy of luis f. leloir. Journal of experimental botany, 72:4053-4067, May 2021. URL: https://doi.org/10.1093/jxb/erab109, doi:10.1093/jxb/erab109. This article has 56 citations and is from a domain leading peer-reviewed journal.

15. (succoio2022galactosemiabiochemistrymolecular pages 2-4): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

16. (harrison2022theevolutionof pages 7-12): Marie-Claire Harrison, Abigail L. LaBella, Chris Todd Hittinger, and Antonis Rokas. The evolution of the galactose utilization pathway in budding yeasts. Trends in Genetics, 38:97-106, Jan 2022. URL: https://doi.org/10.1016/j.tig.2021.08.013, doi:10.1016/j.tig.2021.08.013. This article has 52 citations and is from a domain leading peer-reviewed journal.

17. (harrison2022theevolutionof pages 1-7): Marie-Claire Harrison, Abigail L. LaBella, Chris Todd Hittinger, and Antonis Rokas. The evolution of the galactose utilization pathway in budding yeasts. Trends in Genetics, 38:97-106, Jan 2022. URL: https://doi.org/10.1016/j.tig.2021.08.013, doi:10.1016/j.tig.2021.08.013. This article has 52 citations and is from a domain leading peer-reviewed journal.

18. (wada2025galactosemutarotasedeficiency pages 1-3): Yoichi Wada, Yu Aihara, Yasuko Mikami-Saito, Tomohisa Suzuki, Ryoji Fujiki, Osamu Ohara, Atsuo Kikuchi, and Shigeo Kure. Galactose mutarotase deficiency as the galactosemia type iv. Journal of Human Genetics, Dec 2025. URL: https://doi.org/10.1038/s10038-025-01439-6, doi:10.1038/s10038-025-01439-6. This article has 0 citations and is from a peer-reviewed journal.

19. (wada2025galactosemutarotasedeficiency pages 3-4): Yoichi Wada, Yu Aihara, Yasuko Mikami-Saito, Tomohisa Suzuki, Ryoji Fujiki, Osamu Ohara, Atsuo Kikuchi, and Shigeo Kure. Galactose mutarotase deficiency as the galactosemia type iv. Journal of Human Genetics, Dec 2025. URL: https://doi.org/10.1038/s10038-025-01439-6, doi:10.1038/s10038-025-01439-6. This article has 0 citations and is from a peer-reviewed journal.

20. (delnoy2021currentandfuture pages 9-13): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

21. (brenner2002hintfhitand pages 8-9): Charles Brenner. Hint, fhit, and galt: function, structure, evolution, and mechanism of three branches of the histidine triad superfamily of nucleotide hydrolases and transferases. Biochemistry, 41 29:9003-14, Jul 2002. URL: https://doi.org/10.1021/bi025942q, doi:10.1021/bi025942q. This article has 363 citations and is from a peer-reviewed journal.

22. (brenner2002hintfhitand pages 9-10): Charles Brenner. Hint, fhit, and galt: function, structure, evolution, and mechanism of three branches of the histidine triad superfamily of nucleotide hydrolases and transferases. Biochemistry, 41 29:9003-14, Jul 2002. URL: https://doi.org/10.1021/bi025942q, doi:10.1021/bi025942q. This article has 363 citations and is from a peer-reviewed journal.

23. (brenner2002hintfhitand pages 10-11): Charles Brenner. Hint, fhit, and galt: function, structure, evolution, and mechanism of three branches of the histidine triad superfamily of nucleotide hydrolases and transferases. Biochemistry, 41 29:9003-14, Jul 2002. URL: https://doi.org/10.1021/bi025942q, doi:10.1021/bi025942q. This article has 363 citations and is from a peer-reviewed journal.

24. (haskovic2020pathophysiologyandtargets pages 10-12): Minela Haskovic, Ana I. Coelho, Jörgen Bierau, Jo M. Vanoevelen, Laura K. M. Steinbusch, Luc J. I. Zimmermann, Eduardo Villamor‐Martinez, Gerard T. Berry, and M. Estela Rubio‐Gozalbo. Pathophysiology and targets for treatment in hereditary galactosemia: a systematic review of animal and cellular models. Journal of Inherited Metabolic Disease, 43:392-408, Jan 2020. URL: https://doi.org/10.1002/jimd.12202, doi:10.1002/jimd.12202. This article has 61 citations and is from a peer-reviewed journal.

25. (sanchezpintos2024clinicalandbiochemical pages 1-2): Paula Sánchez-Pintos, Maria José Camba-Garea, Beatriz Martin López-Pardo, Jose A. Cocho de Juan, M. Dolores Bóveda, Sofia Barbosa-Gouveia, Maria E Vázquez-Mosquera, Francisco Barros-Angueira, Raquel Fernández Patiño, and Maria L. Couce. Clinical and biochemical evolution after partial dietary liberalization of two cases of galactosemia due to galactose mutarotase deficiency. BMC Pediatrics, Sep 2024. URL: https://doi.org/10.1186/s12887-024-05074-6, doi:10.1186/s12887-024-05074-6. This article has 2 citations and is from a peer-reviewed journal.

26. (delnoy2021currentandfuture pages 41-47): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

27. (tisa2022theimportanceof pages 4-5): Ioana Badiu Tișa, Anca Cristina Achim, and Anamaria Cozma-Petruț. The importance of neonatal screening for galactosemia. Nutrients, 15:10, Dec 2022. URL: https://doi.org/10.3390/nu15010010, doi:10.3390/nu15010010. This article has 50 citations.

28. (panis2024brainfunctionin pages 2-3): Bianca Panis, E. Vos, Ivo Bari ć, A. Bosch, M. Brouwers, A. Burlina, D. Cassiman, David J Coman, María-Luz Couce, Anibh M. Das, D. Demirbas, A. Empain, Matthias Gautschi, Olga Grafakou, Stephanie Grűnewald, S. D. Kingma, I. Knerr, Elisa Leão-Teles, D. Möslinger, Elaine Murphy, K. Õunap, Adriana Pané, Sabrina Paci, Rossella Parini, Isabel Rivera, S. Scholl-Bürgi, I. V. D. Schwartz, Triantafyllia Sdogou, L. Shakerdi, A. Skouma, Karolina M. Stepien, Eileen P. Treacy, Susan E. Waisbren, Gerard T. Berry, M. Rubio-Gozalbo, P. Tanpaiboon, A. Gropman, Bosch Brouwers Burlina Cassiman Coman Couce Das Demirbas Bari ć, Rubio-Gozalbo. This, and Cyprus Nicosia. Brain function in classic galactosemia, a galactosemia network (galnet) members review. Frontiers in Genetics, Feb 2024. URL: https://doi.org/10.3389/fgene.2024.1355962, doi:10.3389/fgene.2024.1355962. This article has 14 citations and is from a peer-reviewed journal.

29. (tisa2022theimportanceof pages 2-4): Ioana Badiu Tișa, Anca Cristina Achim, and Anamaria Cozma-Petruț. The importance of neonatal screening for galactosemia. Nutrients, 15:10, Dec 2022. URL: https://doi.org/10.3390/nu15010010, doi:10.3390/nu15010010. This article has 50 citations.

30. (succoio2022galactosemiabiochemistrymolecular pages 12-13): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

31. (succoio2022galactosemiabiochemistrymolecular pages 8-9): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

32. (delnoy2021currentandfuture pages 6-9): Britt Delnoy, Ana I. Coelho, and Maria Estela Rubio-Gozalbo. Current and future treatments for classic galactosemia. Journal of Personalized Medicine, 11:75, Jan 2021. URL: https://doi.org/10.3390/jpm11020075, doi:10.3390/jpm11020075. This article has 55 citations.

33. (harrison2022theevolutionof pages 26-29): Marie-Claire Harrison, Abigail L. LaBella, Chris Todd Hittinger, and Antonis Rokas. The evolution of the galactose utilization pathway in budding yeasts. Trends in Genetics, 38:97-106, Jan 2022. URL: https://doi.org/10.1016/j.tig.2021.08.013, doi:10.1016/j.tig.2021.08.013. This article has 52 citations and is from a domain leading peer-reviewed journal.

34. (harrison2022theevolutionof pages 17-22): Marie-Claire Harrison, Abigail L. LaBella, Chris Todd Hittinger, and Antonis Rokas. The evolution of the galactose utilization pathway in budding yeasts. Trends in Genetics, 38:97-106, Jan 2022. URL: https://doi.org/10.1016/j.tig.2021.08.013, doi:10.1016/j.tig.2021.08.013. This article has 52 citations and is from a domain leading peer-reviewed journal.

35. (harrison2022theevolutionof pages 12-17): Marie-Claire Harrison, Abigail L. LaBella, Chris Todd Hittinger, and Antonis Rokas. The evolution of the galactose utilization pathway in budding yeasts. Trends in Genetics, 38:97-106, Jan 2022. URL: https://doi.org/10.1016/j.tig.2021.08.013, doi:10.1016/j.tig.2021.08.013. This article has 52 citations and is from a domain leading peer-reviewed journal.

36. (peri2024auniquemetabolic pages 13-16): Kameshwara V. R. Peri, Le Yuan, Fábio Faria Oliveira, Karl Persson, Hanna D. Alalam, Lisbeth Olsson, Johan Larsbrink, Eduard J. Kerkhoven, and Cecilia Geijer. A unique metabolic gene cluster regulates lactose and galactose metabolism in the yeast <i>candida intermedia</i>. Oct 2024. URL: https://doi.org/10.1128/aem.01135-24, doi:10.1128/aem.01135-24. This article has 8 citations and is from a peer-reviewed journal.

37. (peri2024auniquemetabolic pages 2-6): Kameshwara V. R. Peri, Le Yuan, Fábio Faria Oliveira, Karl Persson, Hanna D. Alalam, Lisbeth Olsson, Johan Larsbrink, Eduard J. Kerkhoven, and Cecilia Geijer. A unique metabolic gene cluster regulates lactose and galactose metabolism in the yeast <i>candida intermedia</i>. Oct 2024. URL: https://doi.org/10.1128/aem.01135-24, doi:10.1128/aem.01135-24. This article has 8 citations and is from a peer-reviewed journal.

38. (peri2024auniquemetabolic pages 6-8): Kameshwara V. R. Peri, Le Yuan, Fábio Faria Oliveira, Karl Persson, Hanna D. Alalam, Lisbeth Olsson, Johan Larsbrink, Eduard J. Kerkhoven, and Cecilia Geijer. A unique metabolic gene cluster regulates lactose and galactose metabolism in the yeast <i>candida intermedia</i>. Oct 2024. URL: https://doi.org/10.1128/aem.01135-24, doi:10.1128/aem.01135-24. This article has 8 citations and is from a peer-reviewed journal.

39. (wang2021transcriptionalprofilingof pages 8-10): Hanyu Wang, Tao Sun, Zhen Zhao, Shuying Gu, Qian Liu, Taju Wu, Depei Wang, Chaoguang Tian, and Jingen Li. Transcriptional profiling of myceliophthora thermophila on galactose and metabolic engineering for improved galactose utilization. Frontiers in Microbiology, Apr 2021. URL: https://doi.org/10.3389/fmicb.2021.664011, doi:10.3389/fmicb.2021.664011. This article has 13 citations and is from a peer-reviewed journal.

40. (peri2024modeldrivenelucidationof pages 1-4): Kameshwara. V. R. Peri, Ivan Domenzain, Hanna D Alalam, Abril Valverde Rascon, Jens Nielsen, and Cecilia Geijer. Model-driven elucidation of lactose and galactose metabolism via oxidoreductive pathway in sungouiella intermedia for cell factory applications. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.19.624258, doi:10.1101/2024.11.19.624258. This article has 0 citations.

41. (figueroa2021nucleotidesugarmetabolismin pages 3-4): Carlos M Figueroa, John E Lunn, and Alberto A Iglesias. Nucleotide-sugar metabolism in plants: the legacy of luis f. leloir. Journal of experimental botany, 72:4053-4067, May 2021. URL: https://doi.org/10.1093/jxb/erab109, doi:10.1093/jxb/erab109. This article has 56 citations and is from a domain leading peer-reviewed journal.

42. (boulanger2021sugarphosphatetoxicities pages 12-14): Erin F. Boulanger, Anice Sabag-Daigle, Pankajavalli Thirugnanasambantham, Venkat Gopalan, and Brian M. M. Ahmer. Sugar-phosphate toxicities. Dec 2021. URL: https://doi.org/10.1128/mmbr.00123-21, doi:10.1128/mmbr.00123-21. This article has 66 citations and is from a domain leading peer-reviewed journal.

43. (boulanger2021sugarphosphatetoxicities pages 3-6): Erin F. Boulanger, Anice Sabag-Daigle, Pankajavalli Thirugnanasambantham, Venkat Gopalan, and Brian M. M. Ahmer. Sugar-phosphate toxicities. Dec 2021. URL: https://doi.org/10.1128/mmbr.00123-21, doi:10.1128/mmbr.00123-21. This article has 66 citations and is from a domain leading peer-reviewed journal.

44. (boulanger2021sugarphosphatetoxicities pages 14-15): Erin F. Boulanger, Anice Sabag-Daigle, Pankajavalli Thirugnanasambantham, Venkat Gopalan, and Brian M. M. Ahmer. Sugar-phosphate toxicities. Dec 2021. URL: https://doi.org/10.1128/mmbr.00123-21, doi:10.1128/mmbr.00123-21. This article has 66 citations and is from a domain leading peer-reviewed journal.

45. (banford2021galactosemiatowardspharmacological pages 11-13): Samantha Banford, Thomas J. McCorvie, Angel L. Pey, and David J. Timson. Galactosemia: towards pharmacological chaperones. Journal of Personalized Medicine, 11:106, Feb 2021. URL: https://doi.org/10.3390/jpm11020106, doi:10.3390/jpm11020106. This article has 34 citations.

46. (rodrigues2022currentunderstandingon pages 15-16): Kenneth Francis Rodrigues, Wilson Thau Lym Yong, Md. Safiul Alam Bhuiyan, Shafiquzzaman Siddiquee, Muhammad Dawood Shah, and Balu Alagar Venmathi Maran. Current understanding on the genetic basis of key metabolic disorders: a review. Biology, 11:1308, Sep 2022. URL: https://doi.org/10.3390/biology11091308, doi:10.3390/biology11091308. This article has 25 citations.

47. (succoio2022galactosemiabiochemistrymolecular pages 6-8): Mariangela Succoio, Rosa Sacchettini, Alessandro Rossi, Giancarlo Parenti, and Margherita Ruoppolo. Galactosemia: biochemistry, molecular genetics, newborn screening, and treatment. Biomolecules, 12:968, Jul 2022. URL: https://doi.org/10.3390/biom12070968, doi:10.3390/biom12070968. This article has 90 citations.

48. (figueroa2021nucleotidesugarmetabolismin pages 12-13): Carlos M Figueroa, John E Lunn, and Alberto A Iglesias. Nucleotide-sugar metabolism in plants: the legacy of luis f. leloir. Journal of experimental botany, 72:4053-4067, May 2021. URL: https://doi.org/10.1093/jxb/erab109, doi:10.1093/jxb/erab109. This article has 56 citations and is from a domain leading peer-reviewed journal.

49. (tisa2022theimportanceof pages 11-12): Ioana Badiu Tișa, Anca Cristina Achim, and Anamaria Cozma-Petruț. The importance of neonatal screening for galactosemia. Nutrients, 15:10, Dec 2022. URL: https://doi.org/10.3390/nu15010010, doi:10.3390/nu15010010. This article has 50 citations.

50. (quispe2022explorationofarchaeal pages 4-5): Carlos Josue Alvarez Quispe, Matthieu Da Costa, Koen Beerens, and T. Desmet. Exploration of archaeal nucleotide sugar epimerases unveils a new and highly promiscuous gdp-gal4e subgroup. Current Research in Biotechnology, 4:350-358, Aug 2022. URL: https://doi.org/10.1016/j.crbiot.2022.08.003, doi:10.1016/j.crbiot.2022.08.003. This article has 3 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](galactose_leloir_pathway-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](galactose_leloir_pathway-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. figueroa2021nucleotidesugarmetabolismin pages 2-3
2. boulanger2021sugarphosphatetoxicities pages 10-12
3. succoio2022galactosemiabiochemistrymolecular pages 1-2
4. delnoy2021currentandfuture pages 9-13
5. brenner2002hintfhitand pages 10-11
6. wada2025galactosemutarotasedeficiency pages 1-3
7. wada2025galactosemutarotasedeficiency pages 3-4
8. sanchezpintos2024clinicalandbiochemical pages 1-2
9. tisa2022theimportanceof pages 4-5
10. brenner2002hintfhitand pages 9-10
11. delnoy2021currentandfuture pages 6-9
12. haskovic2020pathophysiologyandtargets pages 10-12
13. harrison2022theevolutionof pages 7-12
14. harrison2022theevolutionof pages 17-22
15. peri2024auniquemetabolic pages 13-16
16. figueroa2021nucleotidesugarmetabolismin pages 6-7
17. anderson2011novelinsightsinto pages 6-7
18. peabody2019engineeredpseudomonasputida pages 1-2
19. peri2024modeldrivenelucidationof pages 6-10
20. peri2024modeldrivenelucidationof pages 10-13
21. boulanger2021sugarphosphatetoxicities pages 12-14
22. boulanger2021sugarphosphatetoxicities pages 3-6
23. panis2024brainfunctionin pages 2-3
24. harrison2022theevolutionof pages 26-29
25. succoio2022galactosemiabiochemistrymolecular pages 8-9
26. succoio2022galactosemiabiochemistrymolecular pages 6-8
27. banford2021galactosemiatowardspharmacological pages 11-13
28. quispe2022explorationofarchaeal pages 4-5
29. delnoy2021currentandfuture pages 1-6
30. delnoy2021currentandfuture pages 47-49
31. haskovic2020pathophysiologyandtargets pages 1-2
32. figueroa2021nucleotidesugarmetabolismin pages 7-8
33. figueroa2021nucleotidesugarmetabolismin pages 8-9
34. succoio2022galactosemiabiochemistrymolecular pages 2-4
35. harrison2022theevolutionof pages 1-7
36. brenner2002hintfhitand pages 8-9
37. delnoy2021currentandfuture pages 41-47
38. tisa2022theimportanceof pages 2-4
39. succoio2022galactosemiabiochemistrymolecular pages 12-13
40. harrison2022theevolutionof pages 12-17
41. peri2024auniquemetabolic pages 2-6
42. peri2024auniquemetabolic pages 6-8
43. wang2021transcriptionalprofilingof pages 8-10
44. peri2024modeldrivenelucidationof pages 1-4
45. figueroa2021nucleotidesugarmetabolismin pages 3-4
46. boulanger2021sugarphosphatetoxicities pages 14-15
47. rodrigues2022currentunderstandingon pages 15-16
48. figueroa2021nucleotidesugarmetabolismin pages 12-13
49. tisa2022theimportanceof pages 11-12
50. https://doi.org/10.1093/jxb/erab109,
51. https://doi.org/10.3390/biom12070968,
52. https://doi.org/10.3390/jpm11020075,
53. https://doi.org/10.1002/jimd.12202,
54. https://doi.org/10.1111/tpj.15638,
55. https://doi.org/10.1186/s13068-019-1627-0,
56. https://doi.org/10.1371/journal.pone.0020237,
57. https://doi.org/10.1101/2024.11.19.624258,
58. https://doi.org/10.1128/mmbr.00123-21,
59. https://doi.org/10.1016/j.tig.2021.08.013,
60. https://doi.org/10.1038/s10038-025-01439-6,
61. https://doi.org/10.1021/bi025942q,
62. https://doi.org/10.1186/s12887-024-05074-6,
63. https://doi.org/10.3390/nu15010010,
64. https://doi.org/10.3389/fgene.2024.1355962,
65. https://doi.org/10.1128/aem.01135-24,
66. https://doi.org/10.3389/fmicb.2021.664011,
67. https://doi.org/10.3390/jpm11020106,
68. https://doi.org/10.3390/biology11091308,
69. https://doi.org/10.1016/j.crbiot.2022.08.003,