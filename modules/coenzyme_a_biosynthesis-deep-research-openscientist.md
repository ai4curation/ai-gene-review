---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T15:01:56.277446'
end_time: '2026-07-18T15:33:26.070594'
duration_seconds: 1889.79
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pantothenate and coenzyme A biosynthesis
  module_summary: 'Synthesis of pantothenate and its conversion to coenzyme A (CoA).
    The pantoate branch transfers a hydroxymethyl group to 3-methyl-2-oxobutanoate,
    reduces 2-dehydropantoate to (R)-pantoate, and condenses pantoate with beta-alanine
    to form pantothenate. Five subsequent reactions phosphorylate pantothenate, add
    and decarboxylate cysteine, adenylylate 4''-phosphopantetheine, and phosphorylate
    dephospho-CoA. Enzyme architecture varies across taxa: pantothenate kinases occur
    in three unrelated families, CoaB and CoaC may be separate or fused, and the final
    CoaD and CoaE activities may be separate or fused in CoA synthase. Beta-alanine
    supply is an upstream dependency because organisms use different routes, including
    PanD-dependent aspartate decarboxylation, pyrimidine degradation, and uptake.
    CoA salvage, phosphopantetheine release from acyl carrier proteins, and downstream
    CoA-dependent metabolism are outside the module boundary.'
  module_outline: "- Pantothenate and coenzyme A biosynthesis\n  - 1. 2-dehydropantoate\
    \ formation\n  - 3-methyl-2-oxobutanoate to 2-dehydropantoate\n    - PanB ketopantoate\
    \ hydroxymethyltransferase (molecular player: PanB family; activity or role: 3-methyl-2-oxobutanoate\
    \ hydroxymethyltransferase activity)\n  - 2. pantoate formation\n  - 2-dehydropantoate\
    \ to (R)-pantoate\n    - PanE-like ketopantoate reductase (molecular player: canonical\
    \ PanE ketopantoate reductase family; activity or role: 2-dehydropantoate 2-reductase\
    \ activity)\n  - 3. pantothenate formation\n  - (R)-pantoate and beta-alanine\
    \ to pantothenate\n    - PanC pantothenate synthetase (molecular player: PanC\
    \ pantothenate synthetase family; activity or role: pantoate-beta-alanine ligase\
    \ activity)\n  - 4. pantothenate phosphorylation\n  - Pantothenate to 4'-phosphopantothenate\n\
    \    - Alternative versions by enzyme family: Pantothenate kinase family variants\n\
    \      - Type I bacterial CoaA implementation\n        - Type I pantothenate kinase\
    \ (molecular player: type I pantothenate kinase family; activity or role: pantothenate\
    \ kinase activity)\n      - Type II eukaryotic PANK implementation\n        -\
    \ Type II pantothenate kinase (molecular player: type II pantothenate kinase family;\
    \ activity or role: pantothenate kinase activity)\n      - Type III bacterial\
    \ CoaX implementation\n        - Type III pantothenate kinase (molecular player:\
    \ type III pantothenate kinase family; activity or role: pantothenate kinase activity)\n\
    \  - 5. phosphopantothenoylcysteine synthesis\n  - 4'-phosphopantothenate to phosphopantothenoylcysteine\n\
    \    - Alternative versions by protein architecture: Phosphopantothenate--cysteine\
    \ ligase architectures\n      - Standalone PPCS implementation\n        - Standalone\
    \ phosphopantothenate--cysteine ligase (molecular player: PPCS family; activity\
    \ or role: phosphopantothenate--cysteine ligase activity)\n      - Fused bacterial\
    \ CoaB implementation\n        - CoaB domain of bifunctional CoaBC (molecular\
    \ player: bifunctional CoaBC family; activity or role: phosphopantothenate--cysteine\
    \ ligase activity)\n  - 6. phosphopantetheine formation\n  - Phosphopantothenoylcysteine\
    \ to 4'-phosphopantetheine\n    - Phosphopantothenoylcysteine decarboxylase (molecular\
    \ player: phosphopantothenoylcysteine decarboxylase family; activity or role:\
    \ phosphopantothenoylcysteine decarboxylase activity)\n  - 7. dephospho-CoA formation\n\
    \  - 4'-phosphopantetheine to dephospho-CoA\n    - Alternative versions by protein\
    \ architecture: Phosphopantetheine adenylyltransferase architectures\n      -\
    \ Standalone bacterial CoaD implementation\n        - Standalone phosphopantetheine\
    \ adenylyltransferase (molecular player: bacterial CoaD family; activity or role:\
    \ pantetheine-phosphate adenylyltransferase activity)\n      - Fused CoA synthase\
    \ PPAT implementation\n        - PPAT domain of bifunctional CoA synthase (molecular\
    \ player: bifunctional CoA synthase family; activity or role: pantetheine-phosphate\
    \ adenylyltransferase activity)\n  - 8. coenzyme A formation\n  - Dephospho-CoA\
    \ to coenzyme A\n    - Dephospho-CoA kinase (molecular player: CoaE/CoA synthase\
    \ kinase family; activity or role: dephospho-CoA kinase activity)"
  module_connections: '- 3-methyl-2-oxobutanoate to 2-dehydropantoate feeds into 2-dehydropantoate
    to (R)-pantoate: PanB supplies 2-dehydropantoate to the PanE-like reductase.

    - 2-dehydropantoate to (R)-pantoate feeds into (R)-pantoate and beta-alanine to
    pantothenate: The reductase supplies (R)-pantoate to PanC.

    - (R)-pantoate and beta-alanine to pantothenate feeds into Pantothenate to 4''-phosphopantothenate:
    Pantothenate becomes the substrate for the first CoA-specific reaction.

    - Pantothenate to 4''-phosphopantothenate feeds into 4''-phosphopantothenate to
    phosphopantothenoylcysteine: 4''-phosphopantothenate is conjugated with cysteine.

    - 4''-phosphopantothenate to phosphopantothenoylcysteine feeds into Phosphopantothenoylcysteine
    to 4''-phosphopantetheine: Phosphopantothenoylcysteine is decarboxylated to phosphopantetheine.

    - Phosphopantothenoylcysteine to 4''-phosphopantetheine feeds into 4''-phosphopantetheine
    to dephospho-CoA: 4''-phosphopantetheine is adenylylated to dephospho-CoA.

    - 4''-phosphopantetheine to dephospho-CoA feeds into Dephospho-CoA to coenzyme
    A: Dephospho-CoA is phosphorylated to coenzyme A.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: coenzyme_a_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: coenzyme_a_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Pantothenate and coenzyme A biosynthesis

## Working Scope

Synthesis of pantothenate and its conversion to coenzyme A (CoA). The pantoate branch transfers a hydroxymethyl group to 3-methyl-2-oxobutanoate, reduces 2-dehydropantoate to (R)-pantoate, and condenses pantoate with beta-alanine to form pantothenate. Five subsequent reactions phosphorylate pantothenate, add and decarboxylate cysteine, adenylylate 4'-phosphopantetheine, and phosphorylate dephospho-CoA. Enzyme architecture varies across taxa: pantothenate kinases occur in three unrelated families, CoaB and CoaC may be separate or fused, and the final CoaD and CoaE activities may be separate or fused in CoA synthase. Beta-alanine supply is an upstream dependency because organisms use different routes, including PanD-dependent aspartate decarboxylation, pyrimidine degradation, and uptake. CoA salvage, phosphopantetheine release from acyl carrier proteins, and downstream CoA-dependent metabolism are outside the module boundary.

## Provisional Biological Outline

- Pantothenate and coenzyme A biosynthesis
  - 1. 2-dehydropantoate formation
  - 3-methyl-2-oxobutanoate to 2-dehydropantoate
    - PanB ketopantoate hydroxymethyltransferase (molecular player: PanB family; activity or role: 3-methyl-2-oxobutanoate hydroxymethyltransferase activity)
  - 2. pantoate formation
  - 2-dehydropantoate to (R)-pantoate
    - PanE-like ketopantoate reductase (molecular player: canonical PanE ketopantoate reductase family; activity or role: 2-dehydropantoate 2-reductase activity)
  - 3. pantothenate formation
  - (R)-pantoate and beta-alanine to pantothenate
    - PanC pantothenate synthetase (molecular player: PanC pantothenate synthetase family; activity or role: pantoate-beta-alanine ligase activity)
  - 4. pantothenate phosphorylation
  - Pantothenate to 4'-phosphopantothenate
    - Alternative versions by enzyme family: Pantothenate kinase family variants
      - Type I bacterial CoaA implementation
        - Type I pantothenate kinase (molecular player: type I pantothenate kinase family; activity or role: pantothenate kinase activity)
      - Type II eukaryotic PANK implementation
        - Type II pantothenate kinase (molecular player: type II pantothenate kinase family; activity or role: pantothenate kinase activity)
      - Type III bacterial CoaX implementation
        - Type III pantothenate kinase (molecular player: type III pantothenate kinase family; activity or role: pantothenate kinase activity)
  - 5. phosphopantothenoylcysteine synthesis
  - 4'-phosphopantothenate to phosphopantothenoylcysteine
    - Alternative versions by protein architecture: Phosphopantothenate--cysteine ligase architectures
      - Standalone PPCS implementation
        - Standalone phosphopantothenate--cysteine ligase (molecular player: PPCS family; activity or role: phosphopantothenate--cysteine ligase activity)
      - Fused bacterial CoaB implementation
        - CoaB domain of bifunctional CoaBC (molecular player: bifunctional CoaBC family; activity or role: phosphopantothenate--cysteine ligase activity)
  - 6. phosphopantetheine formation
  - Phosphopantothenoylcysteine to 4'-phosphopantetheine
    - Phosphopantothenoylcysteine decarboxylase (molecular player: phosphopantothenoylcysteine decarboxylase family; activity or role: phosphopantothenoylcysteine decarboxylase activity)
  - 7. dephospho-CoA formation
  - 4'-phosphopantetheine to dephospho-CoA
    - Alternative versions by protein architecture: Phosphopantetheine adenylyltransferase architectures
      - Standalone bacterial CoaD implementation
        - Standalone phosphopantetheine adenylyltransferase (molecular player: bacterial CoaD family; activity or role: pantetheine-phosphate adenylyltransferase activity)
      - Fused CoA synthase PPAT implementation
        - PPAT domain of bifunctional CoA synthase (molecular player: bifunctional CoA synthase family; activity or role: pantetheine-phosphate adenylyltransferase activity)
  - 8. coenzyme A formation
  - Dephospho-CoA to coenzyme A
    - Dephospho-CoA kinase (molecular player: CoaE/CoA synthase kinase family; activity or role: dephospho-CoA kinase activity)

## Known Relationships Among Steps

- 3-methyl-2-oxobutanoate to 2-dehydropantoate feeds into 2-dehydropantoate to (R)-pantoate: PanB supplies 2-dehydropantoate to the PanE-like reductase.
- 2-dehydropantoate to (R)-pantoate feeds into (R)-pantoate and beta-alanine to pantothenate: The reductase supplies (R)-pantoate to PanC.
- (R)-pantoate and beta-alanine to pantothenate feeds into Pantothenate to 4'-phosphopantothenate: Pantothenate becomes the substrate for the first CoA-specific reaction.
- Pantothenate to 4'-phosphopantothenate feeds into 4'-phosphopantothenate to phosphopantothenoylcysteine: 4'-phosphopantothenate is conjugated with cysteine.
- 4'-phosphopantothenate to phosphopantothenoylcysteine feeds into Phosphopantothenoylcysteine to 4'-phosphopantetheine: Phosphopantothenoylcysteine is decarboxylated to phosphopantetheine.
- Phosphopantothenoylcysteine to 4'-phosphopantetheine feeds into 4'-phosphopantetheine to dephospho-CoA: 4'-phosphopantetheine is adenylylated to dephospho-CoA.
- 4'-phosphopantetheine to dephospho-CoA feeds into Dephospho-CoA to coenzyme A: Dephospho-CoA is phosphorylated to coenzyme A.

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

# Pantothenate and Coenzyme A Biosynthesis: A Mechanistic and Evolutionary Review

*Commissioned review synthesis. Citations are given as PubMed IDs (PMID). Claims are anchored to primary literature and authoritative reviews; where evidence is indirect or organism-specific this is stated explicitly.*

---

## 1. Executive summary

Coenzyme A (CoA) is a universal acyl-group carrier required for the tricarboxylic acid cycle, fatty-acid and polyketide metabolism, and protein acylation. Its biosynthesis is conventionally described as an eight-reaction linear pathway with two clearly separable sub-modules: (i) a **pantoate/pantothenate branch** (PanB → PanE-like reductase → PanC, fed by a β-alanine supply) that assembles the vitamin **pantothenate (vitamin B5)**, and (ii) a **five-step CoA-assembly branch** (PanK → PPCS/CoaB → PPCDC/CoaC → PPAT/CoaD → DPCK/CoaE) that converts pantothenate into CoA. The chemistry of the pathway is largely invariant across the tree of life, but the **protein architecture is strikingly plastic**: the first committed CoA step (pantothenate kinase) is catalysed by three unrelated enzyme families (types I/II/III), the ketopantoate-reductase step is served by at least three non-homologous enzymes (PanE, IlvC, PanG), consecutive activities are fused in some lineages (CoaBC; the bifunctional CoA synthase COASY), and the upstream β-alanine supply is delivered by several non-orthologous routes (PanD, pyrimidine degradation, promiscuous diamine metabolism, or uptake). The plasticity extends even to reaction order: **most archaea abolish free pantothenate as an intermediate**, phosphorylating pantoate first (pantoate kinase, PoK) and then condensing 4-phosphopantoate with β-alanine (phosphopantothenate synthetase, PPS) to reach 4′-phosphopantothenate by a route that inverts the canonical "condense-then-phosphorylate" logic (PMID 24638914; PMID 22940806). CoA itself is an ancient cofactor traceable to the last universal common ancestor (LUCA), so the pathway represents a deeply conserved metabolic core onto which lineage-specific enzyme replacements, fusions, losses, and step-reorderings have been layered. The pathway is regulated principally at two post-translational nodes — feedback inhibition of PanK by CoA/acyl-CoA thioesters, and control of β-alanine output by the PanD–PanZ·acetyl-CoA complex — and is a validated antibacterial, antifungal, and antiparasitic drug target, most notably through pantothenamide antimetabolites. In humans, partial loss of PANK2 or COASY causes tissue-restricted neurodegeneration with brain iron accumulation (PKAN, CoPAN), a still-unexplained tissue selectivity that is among the field's key open questions.

---

## 2. Definition and biological boundaries

**What is inside the module.** The system comprises the eight enzymatic conversions from 3-methyl-2-oxobutanoate (α-ketoisovalerate, a valine-pathway intermediate) and β-alanine to CoA:

1. 3-methyl-2-oxobutanoate → 2-dehydropantoate (ketopantoate) — **PanB**, ketopantoate hydroxymethyltransferase (KPHMT)
2. 2-dehydropantoate → (R)-pantoate — **PanE-like ketopantoate reductase (KPR)**
3. (R)-pantoate + β-alanine → pantothenate — **PanC**, pantothenate synthetase
4. pantothenate → 4′-phosphopantothenate — **PanK**, pantothenate kinase
5. 4′-phosphopantothenate + cysteine → 4′-phosphopantothenoylcysteine — **PPCS/CoaB**
6. 4′-phosphopantothenoylcysteine → 4′-phosphopantetheine — **PPCDC/CoaC**
7. 4′-phosphopantetheine → dephospho-CoA — **PPAT/CoaD**
8. dephospho-CoA → CoA — **DPCK/CoaE**

A useful conceptual division is between the **pantothenate-synthesis sub-module** (steps 1–3 plus β-alanine supply), which is restricted to bacteria, fungi, plants and some protists, and the **CoA-assembly sub-module** (steps 4–8), which is universal because animals and many parasites that cannot make pantothenate still must build CoA from salvaged vitamin B5 (PMID 34969059; PMID 38871981).

**What is adjacent but should be treated separately.** Several processes are routinely conflated with the pathway:

- **Phosphopantetheine handoff to carrier proteins.** The 4′-phosphopantetheine prosthetic arm of acyl carrier protein (ACP) and peptidyl/polyketide carrier proteins is installed not by the CoA pathway but by **Sfp-/AcpS-type phosphopantetheinyl transferases (PPTases)**, which transfer the phosphopantetheine moiety from CoA onto a conserved serine of apo-carrier proteins (PMID 36618868). This is a downstream, CoA-consuming reaction, not a biosynthetic step.
- **CoA salvage.** Extracellular CoA/dephospho-CoA and pantetheine can be degraded and re-imported; salvage feeds the same pool but uses transporters and ectoenzymes outside the de novo module (PMID 34969059).
- **Downstream CoA-dependent metabolism** (acyl-CoA thioester formation, acetylation, etc.) and **β-alanine's non-CoA fates** are out of scope.
- **The upstream branch-point.** Step 1 draws its carbon skeleton from α-ketoisovalerate, shared with branched-chain (valine) amino-acid biosynthesis, and its hydroxymethyl group from **5,10-methylenetetrahydrofolate**, tying the pathway to one-carbon/folate metabolism (PMID 6463). These are supplying pathways, not part of the module.

**Competing definitions.** Textbooks often present a fixed "universal five-step" CoA route with named *E. coli* genes. This is an oversimplification: the number of polypeptides (fusions), the identity of the enzymes (non-orthologous displacement), the nucleotide cofactor (CTP vs ATP at step 5), the ordering of phosphorylation vs β-alanine condensation (canonical vs archaeal), and the very presence of the pantothenate branch all vary. Even the intermediate set differs — in most archaea free pantothenate is never formed (Section 5). The most defensible definition is therefore **reaction-outcome-based** (conversion of pantoate + β-alanine + cysteine, via 4′-phosphopantothenate, to CoA) rather than **gene-based** or tied to a fixed intermediate list.

---

## 3. Mechanistic overview

**Obligatory linear order.** The pathway is a strict metabolic assembly line: each product is the sole substrate of the next enzyme, so the sequence 1→8 is obligatory for de novo synthesis. The only branch is the **entry of β-alanine at step 3**, which is supplied in parallel and can originate from several routes (Section 5). Steps 1–3 are conditional/accessory in organisms that salvage pantothenate; steps 4–8 are obligatory wherever CoA is made from pantothenate.

**Step 1 — PanB (KPHMT).** A folate-dependent aldol-type transfer: the hydroxymethyl group of 5,10-methylenetetrahydrofolate is added to C3 of α-ketoisovalerate to give ketopantoate, with Mg²⁺ orienting the substrate for deprotonation (PMID 12906829; PMID 6463). PanB is a **(βα)₈ TIM-barrel of the phosphoenolpyruvate/pyruvate superfamily** that assembles into a decamer via C-terminal helix swapping (PMID 12842039; PMID 12837791).

**Step 2 — ketopantoate reductase.** NAD(P)H-dependent stereospecific reduction of the C2 keto group to give **(R)-pantoate**. Canonical PanE is a monomeric, NADPH-preferring enzyme of the 6-phosphogluconate-dehydrogenase C-terminal-domain superfamily with a Rossmann N-terminal domain; catalysis requires an induced-fit domain closure over the nicotinamide cofactor (PMID 11724562; PMID 31136784).

**Step 3 — PanC (pantothenate synthetase).** An ATP-dependent amide ligation of (R)-pantoate and β-alanine. The mechanism is a well-characterised **Bi-Uni-Uni-Bi ping-pong**: ATP binds first, then pantoate; PPi is released as a **pantoyl-adenylate intermediate** forms; β-alanine then binds and attacks, releasing pantothenate and AMP (PMID 11669627). The pantoyl-adenylate was confirmed by ³¹P NMR and shown to be kinetically competent.

**Step 4 — PanK (pantothenate kinase).** ATP-dependent phosphorylation of the terminal hydroxyl of pantothenate to 4′-phosphopantothenate. This is the **first committed and generally rate-limiting step**, and the major regulatory node (PMID 40754168; PMID 38871981).

**Archaeal alternative to steps 3–4.** Most archaea lack both PanC and PanK and instead reach the shared intermediate 4′-phosphopantothenate by a reordered two-enzyme route: **pantoate kinase (PoK, COG1829)** phosphorylates (R)-pantoate to 4-phosphopantoate, and **phosphopantothenate synthetase (PPS, COG1701)** then performs ATP-dependent condensation of 4-phosphopantoate with β-alanine (via a phosphopantoyl-adenylate intermediate) to give 4′-phosphopantothenate directly (PMID 24638914; PMID 22940806; PMID 23200110). Free pantothenate is therefore never formed in these organisms; phosphorylation precedes amide-bond formation, the reverse of the canonical order.

**Step 5 — PPCS/CoaB.** Nucleotide-dependent ligation of cysteine to 4′-phosphopantothenate via an **acyl-nucleotidyl intermediate**. Bacterial enzymes are **CTP-dependent** and proceed through a 4′-phosphopantothenoyl-CMP intermediate; eukaryotic PPCS is **ATP-dependent** (PMID 15530362; PMID 12140293).

**Step 6 — PPCDC/CoaC.** **FMN-dependent oxidative decarboxylation** of the cysteinyl carboxylate to give the thioethanolamine (phosphopantetheine). It proceeds through an oxidatively decarboxylated **aminoenethiol intermediate** that is then re-reduced by a redox-active active-site cysteine — mechanistically distinct from PLP-dependent decarboxylation (PMID 11358972; PMID 11923307).

**Step 7 — PPAT/CoaD.** Reversible adenylyl transfer from ATP to the phosphate of 4′-phosphopantetheine, forming dephospho-CoA and PPi. Bacterial CoAD is a hexameric member of the nucleotidyltransferase (α/β phosphodiesterase) superfamily and is a feedback-controlled regulatory node in bacteria (PMID 38456905; PMID 29551072).

**Step 8 — DPCK/CoaE.** ATP-dependent phosphorylation of the 3′-OH of the dephospho-CoA ribose to yield CoA. CoaE is a **P-loop NTPase** with CoA-domain, nucleotide-binding, and lid subdomains (PMID 21264299; PMID 21731728).

---

## 4. Major molecular players and active assemblies

| Step | Activity | Representative enzyme(s) | Fold / assembly | Cofactor / co-substrate | Key refs (PMID) |
|------|----------|--------------------------|-----------------|--------------------------|-----------------|
| 1 | KPHMT | PanB | (βα)₈ barrel, decamer; PEP/pyruvate superfamily | 5,10-CH₂-THF, Mg²⁺ | 12906829, 12842039, 6463 |
| 2 | KPR | PanE; IlvC (moonlight); PanG | 6-PGDH-like (PanE); KARI (IlvC); distinct (PanG) | NADPH/NADH | 11724562, 29791499, 23243306 |
| 3 | Pantothenate synthetase | PanC (canonical); PoK+PPS (archaea, steps 3–4 combined) | Rossmann-like nucleotide-binding N-domain; homodimer | ATP → pantoyl-adenylate | 11669627, 17932772, 24638914 |
| 4 | Pantothenate kinase | Type I (CoaA), Type II (PanK1–4), Type III (CoaX) | actin/ASKHA (I, II); ASKHA (III) | ATP | 18186650, 17631502, 24784177 |
| 5 | PPCS (CoaB) | Standalone PPCS; CoaB domain of CoaBC | dinucleotide-binding fold; dimer | CTP (bact.) / ATP (euk.) | 15530362, 12140293 |
| 6 | PPCDC (CoaC) | Standalone PPCDC; CoaC domain of CoaBC; AtHAL3a | HFCD flavoprotein, trimer | FMN | 11358972, 11923307 |
| 7 | PPAT (CoaD) | Bacterial CoaD; PPAT domain of COASY | nucleotidyltransferase, hexamer (bact.) | ATP | 38456905, 11980892 |
| 8 | DPCK (CoaE) | Bacterial CoaE; DPCK domain of COASY | P-loop NTPase | ATP | 21264299, 11923312 |

**Architectural packaging varies by lineage.** In most bacteria steps 5 and 6 are fused into a single bifunctional **CoaBC (Dfp)** flavoprotein (N-terminal decarboxylase CoaC + C-terminal ligase CoaB) (PMID 12140293), and steps 7 and 8 are catalysed by separate CoaD and CoaE. In higher eukaryotes the reverse fusion is seen: steps 5 and 6 are separate (PPCS, PPCDC), while steps 7 and 8 are fused into the bifunctional **CoA synthase (COASY, ~60 kDa)** carrying both PPAT and DPCK domains (PMID 11980892; PMID 11923312). The complete human enzyme set was defined by comparative genomics and reconstituted in vitro (PMID 11923312).

*Table note:* in most archaea, steps 3 and 4 are replaced by **pantoate kinase (PoK, COG1829)** + **phosphopantothenate synthetase (PPS, COG1701)**, which phosphorylate pantoate before condensing it with β-alanine and thus never form free pantothenate (structures: PMID 31697438, 24638914, 24021277; see Section 5).

**β-Alanine supply enzyme.** The canonical supplier, **PanD (L-aspartate-α-decarboxylase)**, is unusual: a tetrameric β-barrel translated as an inactive proenzyme that matures by **autocatalytic self-cleavage through an ester intermediate**, generating a catalytic **pyruvoyl** group (not PLP) (PMID 9546220; PMID 30073608).

---

## 5. Evolutionary and cell-biological variation

**Three unrelated pantothenate-kinase families (step 4).** Type I (e.g., *E. coli* CoaA), Type II (predominantly eukaryotic PanK, four human isoforms PANK1–4), and Type III (CoaX) are **distinct in sequence, fold and kinetics**; Type III belongs to the ASKHA/acetate-and-sugar-kinase superfamily, has an unusually high Kₘ for ATP, is resistant to CoA feedback inhibition, and cannot activate pantothenamide analogues (PMID 18186650). This is a textbook case of **non-orthologous gene displacement**, and some bacteria (*B. subtilis*, *M. tuberculosis*) encode both type I and III enzymes with type I contributing the larger share of the CoA pool (PMID 24784177). Which PanK is essential is organism-dependent: type III CoaX is essential in *Bacillus anthracis* (PMID 18641144) but dispensable in *M. tuberculosis*, where type I CoaA is essential (PMID 20576686) — a well-documented cross-organism discrepancy.

**Multiple reductases (step 2).** Canonical **PanE**, the moonlighting ketol-acid reductoisomerase **IlvC** (which rescues *panE* loss in *Zymomonas* and *Salmonella*; PMID 29791499), and the non-homologous **PanG** (sole KPR in *Francisella*, with homologs in *Enterococcus*, *Coxiella*, *Clostridioides*; PMID 23243306) independently perform the same reduction. Genome surveys show pantothenate-pathway genes are frequently duplicated and horizontally transferred, and *panE*/*panD* are frequently lost or replaced (PMID 31136784).

**Archaeal reordering of steps 3–4 (a distinct route to 4′-phosphopantothenate).** Whereas bacteria and eukaryotes make free pantothenate (PanC) and then phosphorylate it (PanK), most archaea encode neither enzyme and instead use **pantoate kinase (PoK)** followed by **phosphopantothenate synthetase (PPS)**, phosphorylating pantoate *before* condensing it with β-alanine (PMID 24638914; PMID 22940806). Both enzymes are structurally characterized (PoK and PPS from *Thermococcus kodakarensis* / *T. onnurineus*; PMID 31697438; PMID 24021277) and their homologs are widely conserved across archaeal genomes (PMID 23200110). Regulation also differs: archaeal PPS is not feedback-inhibited by CoA/acetyl-CoA, while PoK shows product inhibition by 4-phosphopantoate (PMID 22940806) — so the CoA-feedback node has shifted relative to the PanK-centred control of bacteria/eukaryotes. This is the deepest example in the pathway of achieving the same outcome (4′-phosphopantothenate) by different molecular means *and* in a different order.

**Variable β-alanine routes.** PanD-dependent aspartate decarboxylation is canonical, but β-alanine is also produced by **β-alanine synthase of the reductive uracil-degradation (pyrimidine catabolism) pathway** (*Rhizobium etli*; PMID 32112625) and by a **promiscuous route via 2,4-diaminobutyrate and 1,3-diaminopropane** (*Acinetobacter baylyi*; PMID 35623386). Loss of *panD* alone renders *Zymomonas mobilis* pantothenate-auxotrophic (PMID 28655181).

**Compartmentalization.** In plants, KPHMT is mitochondrial while pantothenate synthetase is cytosolic, requiring intermediate transporters; plants also lack a recognizable PanD, implying an alternative β-alanine source (PMID 14675432). In humans, PANK2 acquired a **primate-specific mitochondrial targeting signal** (mouse PanK2 is cytosolic), an important caveat when modelling human PANK2 disease in mice (PMID 17825826). The four human PanK isoforms differ in tissue expression, subcellular localization, and feedback sensitivity (PanK3 is the most acetyl-CoA-sensitive, IC₅₀ ≈ 1 µM; PMID 16040613; PMID 12095677).

**Deep origin.** CoA is among the cofactors inferred to have been present in **LUCA** (PMID 27562259), and CoA metabolism is under strong purifying selection in deep-branching methanogens (Tajima's D ≈ −2.86; PMID 40051064). The pathway is therefore ancient, with the PanK family expansions, enzyme fusions, and non-orthologous replacements representing **later, lineage-specific elaborations** on a conserved chemical core. For the universal CoA-assembly branch, the standalone bacterial CoaD/CoaE most closely mirror the minimal ancestral gene set and are the most informative single-domain representatives, whereas the fused eukaryotic COASY is derived. For the pantothenate-to-4′-phosphopantothenate conversion, however, the ancestral state is genuinely **unresolved**: the bacterial/eukaryotic PanC+PanK route and the archaeal PoK+PPS route are non-homologous, so it is not clear which (if either) was present in LUCA, and the deep split between them cautions against treating any one of Type I PanK, Type III CoaX, or archaeal PoK as "the" ancestral kinase.

---

## 6. Constraints, dependencies, and failure modes

**Order constraints — and where they break down.** Within the CoA-assembly branch the order is genuinely fixed: cysteine must be attached (step 5) **before** decarboxylation (step 6), and adenylylation (step 7) precedes 3′-phosphorylation (step 8), because each intermediate is the unique substrate of the next enzyme. By contrast, the ordering of *pantothenate condensation vs its phosphorylation* is **not** fixed across life: bacteria/eukaryotes condense pantoate + β-alanine first (PanC) and phosphorylate the product (PanK), whereas most archaea phosphorylate pantoate first (PoK) and then condense (PPS), never forming free pantothenate (PMID 24638914; PMID 22940806). This archaeal route directly rules out the intuitive assumption that free pantothenate is an obligatory universal intermediate. β-Alanine must be available before the condensation step (step 3 / PPS) can complete, regardless of route.

**Substrate/cofactor constraints.** Step 1 cannot proceed without folate-derived one-carbon units; step 3 requires ATP and forms an obligatory pantoyl-adenylate; bacterial step 5 specifically requires CTP whereas eukaryotic step 5 requires ATP — a nucleotide specificity that rules out simple interchange of bacterial and eukaryotic PPCS in heterologous systems (PMID 15530362). Step 6 requires FMN and a redox-active cysteine; loss of the oxidative machinery blocks decarboxylation.

**Regulatory nodes (flux control is post-translational, not transcriptional).** (i) **PanK** is feedback-inhibited by CoA and acyl-CoA thioesters, coupling CoA synthesis to demand (PMID 16040613; PMID 17631502). (ii) **β-Alanine supply** is throttled by the **PanD–PanZ·acetyl-CoA complex**, in which PanZ binding sequesters PanD's pyruvoyl cofactor as a ketone hydrate when CoA/acetyl-CoA is abundant (PMID 28832133). (iii) In bacteria, **CoaD/PPAT** is additionally feedback-regulated, and mycobacterial **CoaE** is inhibited by CTP and modulated by monomer–trimer equilibrium (PMID 21731728).

**Failure modes.** All eight activities are individually essential where de novo synthesis operates: *panC* and *panK* are essential in *M. tuberculosis* (PMID 22840772; PMID 20576686), and *coaD*/*coaE* are essential despite earlier annotation ambiguity (PMID 22954585). In humans, **partial** loss of PANK2 causes PKAN and partial loss of COASY causes CoPAN — both **neurodegeneration with brain iron accumulation (NBIA)** with globus-pallidus iron deposits (PMID 30740736) — while **near-complete** COASY loss is prenatally lethal (pontocerebellar hypoplasia, microcephaly, arthrogryposis; PMID 30089828). Drosophila models link CoASY decline to impaired mitochondrial integrity and reduced complex I/III activity (PMID 39985665). Conversely, PanK/CoA **excess** is also deleterious: transgenic PANK2 overexpression elevates muscle CoA and impairs performance (PMID 28189602).

**Therapeutic exploitation.** The pathway is a validated drug target in bacteria, fungi, and apicomplexan parasites (PMID 41914741; PMID 34969059; PMID 37762222). **Pantothenamides** are pantothenate analogues that are phosphorylated by PanK and elaborated into inactive CoA/ACP antimetabolites; their clinical development has been limited by serum **pantetheinase** degradation, motivating pantetheinase-resistant "inverted-amide" and bioisostere analogues with Gram-positive and antiplasmodial activity (PMID 31171848; PMID 29332383; PMID 40801835). Because *Plasmodium* salvages pantothenate and depends on CoA assembly, steps 4–8 (but not 1–3) are the exploitable targets there (PMID 34969059).

---

## 7. Controversies and open questions

1. **Tissue selectivity of human disease.** Why do PANK2 (PKAN) and COASY (CoPAN) defects, in a universally essential pathway, selectively injure the CNS and cause iron accumulation? Whether iron accumulation is primary or secondary remains debated, and the mechanistic link to CoA is unresolved (PMID 30740736).
2. **Which PanK is "the" essential kinase.** Essentiality of type I vs type III CoaX is genuinely organism-specific (essential type III in *B. anthracis*; essential type I in *M. tuberculosis*), and generalizing from one species is a recurring error (PMID 18641144; PMID 20576686).
3. **β-Alanine supply is under-mapped.** The frequency and identity of non-PanD routes (pyrimidine degradation, promiscuous diamine metabolism, uptake) across taxa are incompletely catalogued; plant β-alanine sourcing in the absence of PanD is still not fully defined (PMID 14675432; PMID 35623386).
4. **Regulation in eukaryotes.** Feedback control is best characterised in bacterial and mammalian PanK; whether CoaD/CoaE-equivalent nodes regulate flux through the fused COASY, and the physiological role of COASY's interaction with the P-body scaffold EDC4, remain open (PMID 22982864).
5. **Cross-organism data mixing.** Much mechanistic detail is drawn from *E. coli*, *M. tuberculosis*, and human isoforms; kinetic and structural parameters (e.g., NAD(P)H preference of KPR, CTP vs ATP at step 5) are not safely transferable between lineages (PMID 31136784; PMID 15530362). The archaeal PoK/PPS route is a stark reminder that even the intermediate set and step order can differ, so "the CoA pathway" cannot be assumed identical across domains (PMID 24638914).
6. **Annotation reliability.** Non-orthologous displacement (PanE/IlvC/PanG; three PanK families) means genome annotations based on homology systematically miss or mis-assign pathway genes, complicating comparative and drug-target genomics (PMID 23243306).
7. **Ancestral route to 4′-phosphopantothenate.** Because the bacterial/eukaryotic (PanC+PanK) and archaeal (PoK+PPS) solutions are non-homologous, whether LUCA made free pantothenate at all — and which route is derived — remains an open evolutionary question (PMID 22940806).

---

## 8. Key references

- Barritt SA, DuBois-Coyne S, Dibble CC. Coenzyme A biosynthesis: mechanisms of regulation, function and disease. **PMID 38871981** (2024).
- Daugherty M, et al. Complete reconstitution of the human coenzyme A biosynthetic pathway via comparative genomics. **PMID 11923312** (2002).
- Zhyvoloup A, et al. Molecular cloning of CoA synthase — the missing link. **PMID 11980892** (2002).
- von Delft F, et al. Structure of *E. coli* ketopantoate hydroxymethyltransferase (KPHMT). **PMID 12906829** (2003); Chaudhuri BN, et al. Mtb KPHMT decamer. **PMID 12842039** (2003); Powers SG, Snell EE. KPHMT properties (folate donor). **PMID 6463** (1976).
- Matak-Vinković D, et al. *E. coli* ketopantoate reductase structure. **PMID 11724562** (2001); Khanppnavar B, et al. HGT/duplication in pantothenate pathways. **PMID 31136784** (2019); Miller CN, et al. PanG, a new ketopantoate reductase. **PMID 23243306** (2013); Ernst DC, et al. IlvC moonlighting. **PMID 29791499** (2018).
- Zheng R, Blanchard JS. Kinetics of Mtb pantothenate synthetase (PanC). **PMID 11669627** (2001).
- Yang K, et al. Structural basis of type III PanK catalysis. **PMID 18186650** (2008); Hong BS, et al. Human PanK structures / allosteric regulation. **PMID 17631502** (2007); Zhang Y-M, et al. PanK3 feedback by CoA thioesters. **PMID 16040613** (2005); Rock CO, et al. Pank1 isoforms. **PMID 12095677** (2002); Awasthy D, et al. Mtb coaA/coaX essentiality. **PMID 20576686** (2010); Paige C, et al. *B. anthracis* coaX essential. **PMID 18641144** (2008); Ogata Y, et al. *B. subtilis* type I/III. **PMID 24784177** (2014).
- Stanitzek S, et al. CTP-dependent PPC synthetase structure. **PMID 15530362** (2004); Kupke T. CoaB domain of Dfp. **PMID 12140293** (2002); Kupke T. Dfp decarboxylase (HFCD). **PMID 11358972** (2001); Hernández-Acosta P, et al. AtHAL3a mechanism. **PMID 11923307** (2002).
- Ahmad S, et al. PPAT (CoaD) structures. **PMID 38456905** (2024); Skepper CK, et al. PPAT inhibitors. **PMID 29551072** (2018); Walia G, Surolia A. Mycobacterial CoaE regulation. **PMID 21731728** (2011); Ambady A, et al. Mtb CoaD/CoaE essentiality. **PMID 22954585** (2012).
- Albert A, et al. Aspartate decarboxylase (PanD) structure / pyruvoyl self-processing. **PMID 9546220** (1998); Mo Q, et al. PanD self-cleavage classes. **PMID 30073608** (2018); Arnott ZLP, et al. PanD–PanZ·AcCoA regulation. **PMID 28832133** (2017); López-Sámano M, et al. β-alanine from uracil degradation. **PMID 32112625** (2020); Perchat N, et al. promiscuous β-alanine route. **PMID 35623386** (2022); Gliessman JR, et al. *Zymomonas* panD auxotrophy. **PMID 28655181** (2017).
- Weiss MC, et al. Physiology and habitat of LUCA (CoA in LUCA). **PMID 27562259** (2016); Saranya V, Chellapandi P. Coenzyme metabolism in *Methanosarcina*. **PMID 40051064** (2025).
- Kishimoto Y, et al. Phosphopantothenate synthetase (PPS) structure, *T. kodakarensis*. **PMID 24638914** (2014); Ishibashi Y, et al. Biochemical characterization of archaeal PPS. **PMID 22940806** (2012); Kita A, et al. Pantoate kinase (PoK) structure. **PMID 31697438** (2020); Kim JH, et al. Archaeal PPS structure, *T. onnurineus*. **PMID 24021277** (2013); Katoh H, et al. PoK/PPS in *Methanospirillum hungatei*. **PMID 23200110** (2013).
- Di Meo I, Carecchio M, Tiranti V. Inborn errors of CoA metabolism and neurodegeneration. **PMID 30740736** (2019); van Dijk T, et al. COASY loss / PCH. **PMID 30089828** (2018); Shao Y, et al. CoASY Drosophila mitochondrial phenotype. **PMID 39985665** (2025); Corbin DR, et al. PANK2 overexpression. **PMID 28189602** (2017).
- de Vries LE, et al. Pantothenate and CoA biosynthesis in Apicomplexa as drug targets. **PMID 34969059** (2021); Riske BF, et al. Limiting CoA biosynthesis in malaria. **PMID 37762222** (2023); Jansen PAM, et al. Stable pantothenamide bioisosteres. **PMID 31171848** (2019); Barnard L, et al. Pantetheinase-resistant pantothenamides. **PMID 29332383** (2018).
- Ottenhof HH, et al. Pantothenate pathway organization in higher plants. **PMID 14675432** (2004); Leonardi R, et al. Mouse PanK2 localization/regulation. **PMID 17825826** (2007).
- Deng Z, et al. Sfp-type PPTase and ACP phosphopantetheinylation (module boundary). **PMID 36618868** (2022).

---

*Prepared as an autonomous discovery-agent synthesis. Uncertainty is flagged in Sections 6–7; broad claims are anchored to the primary literature cited above, and organism-specific results are not generalized beyond their evidentiary basis.*


## Artifacts

- [OpenScientist final report](coenzyme_a_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](coenzyme_a_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)