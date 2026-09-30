---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:02:54.725922'
end_time: '2026-09-01T10:23:01.794486'
duration_seconds: 1207.07
template_file: templates/module_research.md.j2
template_variables:
  module_title: L-arginine biosynthesis via acetylated ornithine (microbial)
  module_summary: De novo microbial L-arginine biosynthesis from L-glutamate through
    N-acetylated intermediates and L-ornithine. The module includes the linear route,
    in which ArgA initiates acetylation and ArgE hydrolyses N-acetyl-L-ornithine,
    and the cyclic route, in which bifunctional ArgJ can initiate the pathway and
    recycle the acetyl group from N-acetyl-L-ornithine. After ornithine formation,
    ArgF, ArgG, and ArgH convert it through L-citrulline and argininosuccinate to
    L-arginine. Carbamoyl-phosphate production is shared with pyrimidine metabolism
    and is intentionally outside the module boundary. Succinylated-intermediate, N-acetylcitrulline,
    and LysW-dependent arginine pathways are distinct implementations not expanded
    in this module.
  module_outline: "- L-arginine biosynthesis via acetylated ornithine\n  - 1. pathway-initiating\
    \ glutamate acetylation\n  - L-glutamate to N-acetyl-L-glutamate\n    - Alternative\
    \ versions by enzyme family: Glutamate acetylation enzyme variants\n      - Dedicated\
    \ ArgA implementation\n        - ArgA N-acetylglutamate synthase (molecular player:\
    \ ArgA N-acetylglutamate synthase family; activity or role: L-glutamate N-acetyltransferase\
    \ activity, acting on acetyl-CoA as donor)\n      - Bifunctional ArgJ initiation\
    \ implementation\n        - ArgJ acetyl-CoA-dependent initiating activity (molecular\
    \ player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase\
    \ activity, acting on acetyl-CoA as donor)\n  - 2. acetylglutamate kinase\n  -\
    \ N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate\n    - ArgB acetylglutamate\
    \ kinase (molecular player: ArgB acetylglutamate kinase family; activity or role:\
    \ acetylglutamate kinase activity)\n  - 3. acetylglutamyl-phosphate reductase\n\
    \  - N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde\n\
    \    - Alternative versions by enzyme family: ArgC reductase family variants\n\
    \      - Type 1 ArgC implementation\n        - Type 1 ArgC reductase (molecular\
    \ player: type 1 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate\
    \ reductase activity)\n      - Type 2 ArgC implementation\n        - Type 2 ArgC\
    \ reductase (molecular player: type 2 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate\
    \ reductase activity)\n  - 4. acetylornithine aminotransferase\n  - N-acetyl-L-glutamate\
    \ 5-semialdehyde to N-acetyl-L-ornithine\n    - ArgD acetylornithine aminotransferase\
    \ (molecular player: anabolic ArgD-like acetylornithine aminotransferase family;\
    \ activity or role: N2-acetyl-L-ornithine:2-oxoglutarate 5-transaminase activity)\n\
    \  - 5. ornithine release\n  - N-acetyl-L-ornithine to L-ornithine\n    - Alternative\
    \ versions by reaction mechanism: Ornithine-release enzyme variants\n      - Cyclic\
    \ ArgJ transacetylation\n        - ArgJ ornithine acetyltransferase (molecular\
    \ player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase\
    \ activity, acting on acetyl-L-ornithine as donor)\n      - Hydrolytic ArgE deacetylation\n\
    \        - ArgE acetylornithine deacetylase (molecular player: ArgE acetylornithine\
    \ deacetylase family; activity or role: acetylornithine deacetylase activity)\n\
    \  - 6. ornithine carbamoyltransferase\n  - L-ornithine to L-citrulline\n    -\
    \ Biosynthetic ornithine carbamoyltransferase (molecular player: biosynthetic\
    \ ArgF ornithine carbamoyltransferase family; activity or role: ornithine carbamoyltransferase\
    \ activity)\n  - 7. argininosuccinate synthase\n  - L-citrulline to argininosuccinate\n\
    \    - ArgG argininosuccinate synthase (molecular player: type 1 ArgG argininosuccinate\
    \ synthase family; activity or role: argininosuccinate synthase activity)\n  -\
    \ 8. terminal argininosuccinate lyase\n  - Argininosuccinate to L-arginine\n \
    \   - ArgH argininosuccinate lyase (molecular player: ArgH argininosuccinate lyase\
    \ family; activity or role: argininosuccinate lyase activity)"
  module_connections: '- L-glutamate to N-acetyl-L-glutamate precedes N-acetyl-L-glutamate
    to N-acetyl-L-glutamyl 5-phosphate

    - N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate precedes N-acetyl-L-glutamyl
    5-phosphate to N-acetyl-L-glutamate 5-semialdehyde

    - N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde precedes
    N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine

    - N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine precedes N-acetyl-L-ornithine
    to L-ornithine

    - N-acetyl-L-ornithine to L-ornithine precedes L-ornithine to L-citrulline

    - L-ornithine to L-citrulline precedes L-citrulline to argininosuccinate

    - L-citrulline to argininosuccinate precedes Argininosuccinate to L-arginine'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 34
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: arginine_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: arginine_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

L-arginine biosynthesis via acetylated ornithine (microbial)

## Working Scope

De novo microbial L-arginine biosynthesis from L-glutamate through N-acetylated intermediates and L-ornithine. The module includes the linear route, in which ArgA initiates acetylation and ArgE hydrolyses N-acetyl-L-ornithine, and the cyclic route, in which bifunctional ArgJ can initiate the pathway and recycle the acetyl group from N-acetyl-L-ornithine. After ornithine formation, ArgF, ArgG, and ArgH convert it through L-citrulline and argininosuccinate to L-arginine. Carbamoyl-phosphate production is shared with pyrimidine metabolism and is intentionally outside the module boundary. Succinylated-intermediate, N-acetylcitrulline, and LysW-dependent arginine pathways are distinct implementations not expanded in this module.

## Provisional Biological Outline

- L-arginine biosynthesis via acetylated ornithine
  - 1. pathway-initiating glutamate acetylation
  - L-glutamate to N-acetyl-L-glutamate
    - Alternative versions by enzyme family: Glutamate acetylation enzyme variants
      - Dedicated ArgA implementation
        - ArgA N-acetylglutamate synthase (molecular player: ArgA N-acetylglutamate synthase family; activity or role: L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
      - Bifunctional ArgJ initiation implementation
        - ArgJ acetyl-CoA-dependent initiating activity (molecular player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
  - 2. acetylglutamate kinase
  - N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate
    - ArgB acetylglutamate kinase (molecular player: ArgB acetylglutamate kinase family; activity or role: acetylglutamate kinase activity)
  - 3. acetylglutamyl-phosphate reductase
  - N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde
    - Alternative versions by enzyme family: ArgC reductase family variants
      - Type 1 ArgC implementation
        - Type 1 ArgC reductase (molecular player: type 1 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate reductase activity)
      - Type 2 ArgC implementation
        - Type 2 ArgC reductase (molecular player: type 2 ArgC family; activity or role: N-acetyl-gamma-glutamyl-phosphate reductase activity)
  - 4. acetylornithine aminotransferase
  - N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine
    - ArgD acetylornithine aminotransferase (molecular player: anabolic ArgD-like acetylornithine aminotransferase family; activity or role: N2-acetyl-L-ornithine:2-oxoglutarate 5-transaminase activity)
  - 5. ornithine release
  - N-acetyl-L-ornithine to L-ornithine
    - Alternative versions by reaction mechanism: Ornithine-release enzyme variants
      - Cyclic ArgJ transacetylation
        - ArgJ ornithine acetyltransferase (molecular player: bifunctional ArgJ family; activity or role: L-glutamate N-acetyltransferase activity, acting on acetyl-L-ornithine as donor)
      - Hydrolytic ArgE deacetylation
        - ArgE acetylornithine deacetylase (molecular player: ArgE acetylornithine deacetylase family; activity or role: acetylornithine deacetylase activity)
  - 6. ornithine carbamoyltransferase
  - L-ornithine to L-citrulline
    - Biosynthetic ornithine carbamoyltransferase (molecular player: biosynthetic ArgF ornithine carbamoyltransferase family; activity or role: ornithine carbamoyltransferase activity)
  - 7. argininosuccinate synthase
  - L-citrulline to argininosuccinate
    - ArgG argininosuccinate synthase (molecular player: type 1 ArgG argininosuccinate synthase family; activity or role: argininosuccinate synthase activity)
  - 8. terminal argininosuccinate lyase
  - Argininosuccinate to L-arginine
    - ArgH argininosuccinate lyase (molecular player: ArgH argininosuccinate lyase family; activity or role: argininosuccinate lyase activity)

## Known Relationships Among Steps

- L-glutamate to N-acetyl-L-glutamate precedes N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate
- N-acetyl-L-glutamate to N-acetyl-L-glutamyl 5-phosphate precedes N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde
- N-acetyl-L-glutamyl 5-phosphate to N-acetyl-L-glutamate 5-semialdehyde precedes N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine
- N-acetyl-L-glutamate 5-semialdehyde to N-acetyl-L-ornithine precedes N-acetyl-L-ornithine to L-ornithine
- N-acetyl-L-ornithine to L-ornithine precedes L-ornithine to L-citrulline
- L-ornithine to L-citrulline precedes L-citrulline to argininosuccinate
- L-citrulline to argininosuccinate precedes Argininosuccinate to L-arginine

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

# L-Arginine Biosynthesis via Acetylated Ornithine (Microbial): A Mechanistic Review

## 1. Executive Summary

De novo microbial L-arginine biosynthesis via acetylated ornithine is a compact, eight-step metabolic module that converts L-glutamate into L-arginine through a set of N-acetyl-protected intermediates and free L-ornithine. Its defining logic is chemical: the reactive glutamate 5-semialdehyde generated en route to ornithine would spontaneously cyclize to Δ¹-pyrroline-5-carboxylate (the proline route) if its α-amino group were left free. N-acetylation of glutamate's α-amino group blocks that cyclization, allowing the carbon skeleton to be carried all the way to N-acetyl-L-ornithine before the protecting group is removed and free ornithine is carbamoylated. This "amine-protection" strategy is the unifying principle of the module and the feature that distinguishes it from the neighboring proline pathway and from non-acetyl solutions to the same chemical problem.

The single most important axis of variation within the module is *acetyl-group management*. In the **linear route** (typified by *Escherichia coli*), a dedicated GNAT-fold N-acetylglutamate synthase (**ArgA/NAGS**) installs the acetyl group from acetyl-CoA at the start, and an M20-family dinuclear metallohydrolase (**ArgE**) hydrolyzes N-acetyl-L-ornithine to free ornithine plus acetate at step five — a stoichiometric, energetically wasteful arrangement. In the economical **cyclic route** (typified by many Gram-positives, thermophiles, and archaea), the bifunctional N-terminal-nucleophile (Ntn) hydrolase **ArgJ** recycles the acetyl group directly from N-acetyl-L-ornithine back onto a fresh glutamate via a covalent acetyl-threonine intermediate, so that acetyl-CoA is consumed only to prime the cycle. After ornithine is released by either route, three shared enzymes — ornithine carbamoyltransferase (**ArgF**), argininosuccinate synthase (**ArgG**), and argininosuccinate lyase (**ArgH**) — convert ornithine through citrulline and argininosuccinate to arginine. Feedback control operates chiefly at N-acetylglutamate kinase (**ArgB/NAGK**), whose arginine sensitivity is an emergent property of hexameric assembly and an N-terminal helix, and secondarily at ArgA/NAGS.

This review defines the module's boundaries, lays out the best current mechanistic model step-by-step, catalogues the molecular players and their folds, and maps how the system varies across evolutionary lineages. It treats explicitly as *outside the module* the shared carbamoyl-phosphate supply (co-owned with pyrimidine biosynthesis), the LysW carrier-protein route (a distinct, likely ancestral amine-protection chemistry), and the N-acetylcitrulline (AOTCase) and N-succinylornithine (SOTCase) bypass routes, which solve the same problem with different chemistry and are distinguished from the canonical enzymes by as little as a single active-site residue. Throughout, we flag where mechanistic claims are strongly supported by structure and kinetics, and where the literature mixes organisms that may not be directly comparable.

---

## 2. Definition and Biological Boundaries

### What is included

The module comprises eight enzymatic transformations, in obligatory order:

1. **L-glutamate → N-acetyl-L-glutamate** (acetylation; ArgA/NAGS or ArgJ)
2. **N-acetyl-L-glutamate → N-acetyl-L-glutamyl-5-phosphate** (ArgB/NAGK)
3. **N-acetyl-L-glutamyl-5-phosphate → N-acetyl-L-glutamate-5-semialdehyde** (ArgC)
4. **N-acetyl-L-glutamate-5-semialdehyde → N-acetyl-L-ornithine** (ArgD)
5. **N-acetyl-L-ornithine → L-ornithine** (ArgJ transacetylation *or* ArgE hydrolysis)
6. **L-ornithine → L-citrulline** (ArgF/OTCase)
7. **L-citrulline → argininosuccinate** (ArgG/ASS)
8. **argininosuccinate → L-arginine + fumarate** (ArgH/ASL)

The chemical rationale for steps 1–5 is that N-acetylation protects the α-amino group of the glutamate-derived skeleton so that the 5-semialdehyde intermediate cannot cyclize intramolecularly to a pyrroline, the reaction that commits carbon to proline in the parallel Pro pathway. This necessity of N-modification is explicit in the comparative literature: enzymes that modify the glutamate/α-aminoadipate amino group exist precisely "to avoid intramolecular cyclization of intermediates" [PMID: 19620981](https://pubmed.ncbi.nlm.nih.gov/19620981/).

### What is deliberately outside the boundary

- **Carbamoyl-phosphate synthesis.** The carbamoyl-phosphate consumed at step 6 (ornithine → citrulline) is produced by carbamoyl-phosphate synthetase and is *shared with pyrimidine biosynthesis*. It is intentionally outside the module boundary and is regulated by its own logic.
- **The proline pathway.** Free (unacetylated) glutamate-5-semialdehyde is the branch point to proline; the acetyl protection is precisely what keeps carbon inside the arginine module.
- **The urea cycle / arginine catabolism.** In ureotelic vertebrates the *same three terminal reactions* (OTC, ASS, ASL) operate, but the physiological direction, regulation, and even the sign of small-molecule effectors differ. A striking example: N-acetylglutamate is *feedback-inhibitory of biosynthesis in microbes* but becomes an *essential allosteric activator of carbamoyl-phosphate synthetase I* in ureotelic vertebrates, where it is made exclusively by NAGS [PMID: 12633501](https://pubmed.ncbi.nlm.nih.gov/12633501/). Mixing microbial and vertebrate data without care therefore risks inverting the regulatory logic.
- **Catabolic transcarbamylases.** Many organisms carry a *catabolic* ornithine (or putrescine) carbamoyltransferase that runs the reaction in the phosphorolytic (degradative) direction in vivo; these are distinct enzymes from the biosynthetic ArgF ([PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/)).

### Distinct implementations treated separately

Three alternative solutions to the amine-protection problem are *not* expanded within the module because they use non-homologous chemistry:

- **LysW-carrier route.** In *Thermus thermophilus* and various archaea, a small acidic protein (LysW) is covalently attached to the amino group of the pathway intermediate as a carrier/scaffold instead of an acetyl group; ArgA/ArgJ homologs are simply absent [PMID: 19620981](https://pubmed.ncbi.nlm.nih.gov/19620981/).
- **AOTCase (N-acetylcitrulline) route.** Some bacteria (e.g., *Xanthomonas campestris*) carbamoylate N-acetyl-ornithine directly, bypassing free ornithine, to make N-acetylcitrulline [PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/).
- **SOTCase (N-succinylornithine) route.** Others (e.g., *Bacteroides fragilis*) use a succinyl protecting group and a succinyl-specific transcarbamylase [PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/).

### Competing definitions

The principal definitional tension in the literature is whether ArgA and ArgJ represent "the same step done two ways" or two genuinely different enzymatic solutions. Mechanistically they are unrelated proteins (a GNAT acetyltransferase vs. an Ntn hydrolase; see §4), so the safest framing — adopted here — is that **step 1 is chemically identical (glutamate acetylation from acetyl-CoA) but is implemented by two non-homologous enzyme families**, and that **step 5 (ornithine release) is where the linear and cyclic routes truly diverge mechanistically** (hydrolysis vs. transacetylation).

---

## 3. Mechanistic Overview

### The best current model of the sequence of events

```
                         acetyl-CoA        (cyclic route recycles acetyl)
                             |                        ^
                             v                        |
  L-glutamate ---[ArgA/NAGS or ArgJ]---> N-acetyl-L-glutamate      (step 1)
                                              |
                                     ATP  [ArgB / NAGK]            (step 2, control node)
                                              v
                                 N-acetyl-L-glutamyl-5-phosphate
                                              |
                                  NADPH [ArgC reductase]           (step 3)
                                              v
                              N-acetyl-L-glutamate-5-semialdehyde
                                              |
                             glutamate [ArgD aminotransferase]     (step 4)
                                              v
                                    N-acetyl-L-ornithine
                                          /        \
                     [ArgJ transacetylase]          [ArgE hydrolase]   (step 5)
                     (acetyl -> glutamate)           (+ H2O -> acetate)
                                          \        /
                                        L-ornithine
                                              |
                          carbamoyl-P  [ArgF / OTCase]              (step 6)
                                              v
                                        L-citrulline
                                              |
                       ATP + aspartate [ArgG / ASS]                (step 7)
                                              v
                                     argininosuccinate
                                              |
                                     [ArgH / ASL]                   (step 8)
                                              v
                               L-arginine  (+ fumarate)
```

### Obligatory, conditional, and accessory steps

- **Obligatory and strictly ordered.** Steps 1→2→3→4→5→6→7→8 are linearly dependent: each substrate is the product of the previous reaction, so the ordering is enforced by chemistry, not merely by convention. In particular, phosphorylation (step 2) must precede reduction (step 3) because ArgC reduces the *acyl-phosphate*; transamination (step 4) must precede deacetylation/transacetylation (step 5) because ornithine release acts on N-acetyl-ornithine; and carbamoylation (step 6) requires free ornithine.
- **Conditional / mutually exclusive at step 1 and step 5.** An organism runs *either* the ArgA+ArgE linear pair *or* the ArgJ cyclic mechanism (or, rarely, both — see §5). These are alternative implementations, not additional steps.
- **Accessory / regulatory.** Feedback inhibition of NAGK (ArgB) and NAGS (ArgA), metabolon formation with NAGS, and PII-mediated relief of NAGK inhibition are accessory control features that tune flux without changing the core chemistry.

### The control node

In most bacteria the flux-controlling, arginine-feedback-inhibited step is **NAGK (ArgB)**, not the first committed step. This is mechanistically important: because the cyclic route regenerates N-acetylglutamate internally, the "first" acetylation is not always the natural control point, and NAGK sits at the true committed entry into the acetyl-protected phosphorylation/reduction sequence.

---

## 4. Major Molecular Players and Active Assemblies

### Step 1 — Glutamate acetylation: two non-homologous folds

**ArgA / NAGS (GNAT fold).** The dedicated N-acetylglutamate synthase of the linear route is a GCN5-related N-acetyltransferase. The *Mycobacterium tuberculosis* ArgA (Rv2747) structure adopts "a classic fold of the GCN5-related N-acetyltransferase (GNAT) family, characterized by a 'V'-shaped cleft and β-bulge," with activity dependent on dimerization to complete the glutamate-binding pocket and with glutamate binding distant from acetyl-CoA (separate capture and catalysis) [PMID: 28943401](https://pubmed.ncbi.nlm.nih.gov/28943401/). In many bacteria the "classical" NAGS is a two-domain enzyme with an N-terminal amino-acid-kinase (AAK) domain that binds arginine and a C-terminal GNAT domain; the AAK domain is evolutionarily close to NAGK, and a double mutation in the isolated NAGS AAK domain can even elicit NAGK activity ([PMID: 22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/)).

**ArgJ (Ntn hydrolase).** The bifunctional ornithine acetyltransferase is mechanistically unrelated. ArgJ "is a member of the N-terminal nucleophile (Ntn) hydrolase enzyme superfamily and catalyzes the reversible transfer of an acetyl group between the alpha-amino groups of ornithine and glutamate in a mechanism proposed to involve an acyl-enzyme complex" [PMID: 19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/). Mass spectrometry identified **Thr-181 as the residue acetylated during catalysis**, and ¹³C-NMR/IR confirmed a genuine acyl-enzyme intermediate whose carbonyl sits in an oxyanion hole [PMID: 19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/). Kinetically, ArgJ follows a **ping-pong bi-bi** mechanism in all thermophiles tested [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/), consistent with the covalent acetyl-enzyme.

### Step 2 — NAGK (ArgB): the regulatory keystone

NAGK is an amino-acid-kinase-family enzyme whose *arginine feedback sensitivity is an architectural property*. Arginine-insensitive *E. coli* NAGK is a homodimer, whereas arginine-inhibitable NAGKs (e.g., *P. aeruginosa*) are hexamers "in which an extra N-terminal kinked helix (N-helix) interlinks three dimers"; complete N-helix deletion (26 residues) abolishes arginine inhibition [PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/). The same logic holds in *Corynebacterium glutamicum*, where N-helix deletion abolishes inhibition and residues E19, H26, R209, H268, G287 are essential for feedback ([PMID: 22101454](https://pubmed.ncbi.nlm.nih.gov/22101454/)). This is directly exploitable for metabolic engineering: feedback-resistant NAGK mutants (E19R/H26E/H268D) raise L-arginine titers ~42% ([PMID: 21901472](https://pubmed.ncbi.nlm.nih.gov/21901472/)).

### Step 3 — ArgC: an acetyl-glutamyl-phosphate reductase descended from ProA

ArgC (N-acetyl-γ-glutamyl-phosphate reductase) reduces the acyl-phosphate using NADPH and shares ancestry with the proline-pathway reductase ProA. ProA "has a very low promiscuous activity with N-acetylglutamylphosphate, the normal substrate for ArgC," and a single E383A mutation raises this activity 12-fold — direct evidence that ArgC and ProA descend from a common reductase and that the ancestral state was a broader-specificity acyl-phosphate reductase [PMID: 18757760](https://pubmed.ncbi.nlm.nih.gov/18757760/). The provisional outline distinguishes Type-1 and Type-2 ArgC families; the functional basis of that split remains under-characterized (see §9).

### Step 4 — ArgD: a substrate-ambiguous PLP aminotransferase

Acetylornithine aminotransferase (ArgD) is a PLP-dependent transaminase homologous to ornithine aminotransferase. *E. coli* ArgD and *S. cerevisiae* ARG8 "resemble ornithine aminotransferase (OAT) sequences... the observed similarities are statistically significant, indicating that the enzymes are homologous" [PMID: 2199330](https://pubmed.ncbi.nlm.nih.gov/2199330/). Notably, ACOATs are *substrate-ambiguous*: unlike ornithine-specific OATs, they "transaminate ornithine about as efficiently" as their acetylated substrate [PMID: 2199330](https://pubmed.ncbi.nlm.nih.gov/2199330/), a fact relevant to pathway crosstalk.

### Step 5 — Ornithine release: transacetylase vs. metallohydrolase

**ArgJ (cyclic).** As above, ArgJ transfers the acetyl group from N-acetyl-ornithine to glutamate, releasing free ornithine and regenerating N-acetylglutamate — the acetyl group never leaves the pathway. ArgJ ranges from *monofunctional* (ornithine-release only) to *bifunctional* (also initiates by acetylating glutamate from acetyl-CoA): archaeal *M. jannaschii* ArgJ complements only an *E. coli argE* mutant, whereas *T. neapolitana* and *B. stearothermophilus* ArgJ complement both *argA* and *argE* [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/). L-ornithine acts as an inhibitor/regulator of the acetyl cycle.

**ArgE (linear).** Acetylornithine deacetylase is an M20-family dinuclear metallohydrolase related to DapE. *E. coli* ArgE is maximally active with one Mn(II) (k_cat = 550 s⁻¹, K_m = 0.8 mM, k_cat/K_m = 6.9 × 10⁵ M⁻¹ s⁻¹) [PMID: 17333302](https://pubmed.ncbi.nlm.nih.gov/17333302/), and EXAFS supports a dinuclear (Zn/Co) site with histidine ligation [PMID: 22459917](https://pubmed.ncbi.nlm.nih.gov/22459917/). Because ArgE consumes water and releases acetate irreversibly, the linear route is stoichiometrically more expensive than the cyclic route.

### Steps 6–8 — Three distinct terminal folds

The terminal enzymes are three unrelated protein families, a point worth emphasizing because they are often grouped simply as "the last three steps":

| Step | Enzyme | Fold / superfamily | Assembly | Catalytic essentials |
|------|--------|--------------------|----------|----------------------|
| 6 | ArgF / OTCase | transcarbamylase fold | trimer (anabolic); dodecamer (catabolic) | active site shared across subunits; allostery tunable by single residues |
| 7 | ArgG / ASS | "N-type" ATP pyrophosphatase (P-loop) | tetramer | catalytic Cys + Arg; ATP and citrulline/aspartate bind adjacently |
| 8 | ArgH / ASL | class-II fumarase/aspartase lyase | homotetramer | His162–Glu296 dyad; active site shared among three subunits |

**ArgF/OTCase.** The anabolic enzyme is a Michaelis–Menten trimer, whereas the catabolic *P. aeruginosa* OTCase is an allosteric dodecamer; despite extensive sequence similarity, "these enzymes function unidirectionally in vivo" [PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/). Remarkably, allostery is evolutionarily "one mutation away": a single active-site substitution (Arg106Gly) converts non-allosteric anabolic OTCase into a cooperative enzyme [PMID: 2667139](https://pubmed.ncbi.nlm.nih.gov/2667139/), and C-terminal modifications tune dodecameric cooperativity ([PMID: 8168544](https://pubmed.ncbi.nlm.nih.gov/8168544/), [PMID: 8790344](https://pubmed.ncbi.nlm.nih.gov/8790344/)).

**ArgG/ASS.** Argininosuccinate synthase couples ATP to condensation of citrulline and aspartate. Its small domain "has the same fold as that of a new family of 'N-type' ATP pyrophosphatases with the P-loop specific for the pyrophosphate of ATP" [PMID: 11844799](https://pubmed.ncbi.nlm.nih.gov/11844799/); ATP and citrulline bind adjacently with modest conformational change ([PMID: 11809762](https://pubmed.ncbi.nlm.nih.gov/11809762/)), and a catalytic Cys and Arg are essential ([PMID: 3863125](https://pubmed.ncbi.nlm.nih.gov/3863125/)).

**ArgH/ASL.** Argininosuccinate lyase is a homotetramer of the fumarase/aspartase/adenylosuccinase class-II lyase superfamily, with each active site shared among three subunits. It is a textbook "gene-sharing" case: avian/reptilian eye-lens δ-crystallin "shares approximately 90% sequence identity with the enzyme argininosuccinate lyase... an example of a 'hijacked' enzyme" [PMID: 7634077](https://pubmed.ncbi.nlm.nih.gov/7634077/), with the His162–Glu296 catalytic dyad and shared-subunit active site documented structurally ([PMID: 10029536](https://pubmed.ncbi.nlm.nih.gov/10029536/), [PMID: 15273245](https://pubmed.ncbi.nlm.nih.gov/15273245/)).

---

## 5. Evolutionary and Cell-Biological Variation

### Linear vs. cyclic tracks map onto gene organization

The choice of route is legible in genome structure. *E. coli* (linear, ArgE) has dispersed genes (*argECBH*, *argA*), whereas Gram-positives running the cyclic route carry compact operons — e.g., *Lactobacillus plantarum* and *Lactococcus lactis* carry *argCJDBF* clusters ([PMID: 15342575](https://pubmed.ncbi.nlm.nih.gov/15342575/), [PMID: 14762010](https://pubmed.ncbi.nlm.nih.gov/14762010/)). Regulation is by hexameric ArgR/AhrC repressors, frequently present as **two paralogs** in Gram-positives (ArgR1/ArgR2 in *L. plantarum*; ArgR + AhrC, interdependent and non-redundant, in *L. lactis*) ([PMID: 15342575](https://pubmed.ncbi.nlm.nih.gov/15342575/), [PMID: 14762010](https://pubmed.ncbi.nlm.nih.gov/14762010/)). In *E. coli*, ArgR represses *argCBH* with additional RpoS-dependent stationary-phase induction ([PMID: 16504055](https://pubmed.ncbi.nlm.nih.gov/16504055/)).

### Monofunctional vs. bifunctional ArgJ

ArgJ itself varies. Archaeal ArgJ tends to be *monofunctional* (ornithine-release only, requiring a separate NAGS to prime the pathway), while many bacterial ArgJ enzymes are *bifunctional* (both initiate and recycle) [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/). This is a clean, in-vivo-validated distinction from complementation of *E. coli argA* and *argE* mutants.

### Organisms carrying both routes

The linear/cyclic dichotomy is not absolute. *Sinorhizobium meliloti* 1021 is annotated as encoding *both* ornithine-producing enzymes: "N-acetylornithine (NAO) deacetylase (ArgE)... and glutamate N-acetyltransferase (ArgJ)," plus redundant aminoacylases [PMID: 26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/). Such redundancy complicates simple lineage rules.

### The two roles of N-acetylglutamate and its inversion in vertebrates

N-acetylglutamate can be produced by two enzymic reactions — NAGS (ArgA) or ornithine acetyltransferase (ArgJ) — in prokaryotes, lower eukaryotes and plants [PMID: 12633501](https://pubmed.ncbi.nlm.nih.gov/12633501/). Its regulatory sign then flips across the tree of life: "In lower organisms, NAGS is feedback-inhibited by L-arginine, whereas mammalian NAGS activity is significantly enhanced by this amino acid" [PMID: 12633501](https://pubmed.ncbi.nlm.nih.gov/12633501/). NAGS genes are described as more diverse than other arginine-biosynthesis genes, consistent with the first step being the most evolutionarily labile.

### Metabolon formation and nitrogen-status signaling

In yeast, NAGK forms a metabolon with NAGS (which exists only within the metabolon) and carries an extra DUF619 domain that stabilizes the enzyme and modulates arginine feedback; the tetrameric yeast NAGK architecture appears to be an adaptation to metabolon formation [PMID: 22529931](https://pubmed.ncbi.nlm.nih.gov/22529931/). In cyanobacteria and plants, NAGK is a node connecting arginine synthesis to nitrogen storage: "the signalling protein PII, an ancient and widely distributed nitrogen/carbon/ADP/ATP sensor, mediates feedback inhibition relief of NAGK by binding to this enzyme," with two PII trimers sandwiching one NAGK hexamer [PMID: 19013524](https://pubmed.ncbi.nlm.nih.gov/19013524/). Thus the same enzyme is embedded in different regulatory circuitry depending on lineage and physiological state (e.g., nitrogen storage as arginine in seeds/cyanobacteria).

### The LysW route as a separate, likely ancestral lineage

In *T. thermophilus* and related organisms, arginine and lysine biosynthesis share a carrier-protein (LysW/AmCP) strategy rather than acetylation. LysW-dependent enzymes LysZ and LysY also accept the arginine-pathway analogue LysW-Glu (~60% and ~15–20% of native activity), and phylogenetic reconstruction "suggested that an AmCP-mediated biosynthetic pathway represents a primitive route for the synthesis of lysine and [arginine]" [PMID: 41047751](https://pubmed.ncbi.nlm.nih.gov/41047751/). A conserved arginine and an extended LysW-recognition loop distinguish LysY from ArgC [PMID: 26966182](https://pubmed.ncbi.nlm.nih.gov/26966182/). This positions carrier-protein protection as a plausible deep ancestor to acetyl protection.

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering constraints (physical/chemical)

- **Acetylation must precede reduction/transamination.** The whole point of step 1 is to prevent cyclization of the semialdehyde produced downstream; running steps 3–4 without prior acetylation would divert carbon to proline. This rules out any "unprotected" path through the ornithine-forming half of the module — the evidence is the demonstrated necessity of N-modification to avoid intramolecular cyclization [PMID: 19620981](https://pubmed.ncbi.nlm.nih.gov/19620981/).
- **Phosphorylation precedes reduction.** ArgC is an acyl-*phosphate* reductase; it cannot act on the free acid (ProA/ArgC substrate identity, [PMID: 18757760](https://pubmed.ncbi.nlm.nih.gov/18757760/)).
- **Deacetylation/transacetylation precedes carbamoylation.** ArgF acts on *free* ornithine (in the canonical module); therefore step 5 must precede step 6. The AOTCase route is the exception that proves the rule — it carbamoylates the *acetylated* ornithine and thereby reorders the deprotection step ([PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/)).

### Mutually exclusive / substrate-specific implementations

- **Step 1/step 5 pairing.** Linear (ArgA + ArgE) and cyclic (ArgJ) are alternative implementations; an organism generally commits to one, though redundancy exists ([PMID: 26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/)).
- **Single-residue specificity switches at the transcarbamylase step.** The acetyl- vs. succinyl-citrulline routes are separated by essentially one active-site residue: in *X. campestris* AOTCase, Glu92 discriminates the two, and E92P/S/V/A each convert AOTCase into SOTCase, while the reciprocal P90E converts *B. fragilis* SOTCase into AOTCase [PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/). This shows how narrow the chemical boundary is between "canonical" and "bypass" routes.

### Directionality / unidirectionality

Anabolic and catabolic transcarbamylases "function unidirectionally in vivo" despite sequence similarity [PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/); the biosynthetic module relies on the anabolic (citrulline-synthesizing) trimeric ArgF, not the phosphorolytic dodecamer. Using catabolic enzyme data to infer biosynthetic behavior is a common comparability pitfall.

### Failure modes and their exploitation

- **Feedback inhibition as a flux ceiling.** Because NAGK (and, in some organisms, NAGS) is arginine-inhibited, wild-type flux is capped. Deregulation is the standard engineering lever: feedback-resistant NAGK (E19R/H26E/H268D) raises titer ~42% [PMID: 21901472](https://pubmed.ncbi.nlm.nih.gov/21901472/), and bypassing ArgA regulation entirely by feeding N-acetylglutamate to an *argA*-deletion strain sidesteps the control point ([PMID: 37495979](https://pubmed.ncbi.nlm.nih.gov/37495979/)).
- **ArgE as an antibacterial target.** Because ArgE is essential for growth and absent from the human proteome, its dinuclear metallo-active site is being pursued for inhibitor design ([PMID: 17333302](https://pubmed.ncbi.nlm.nih.gov/17333302/), [PMID: 22459917](https://pubmed.ncbi.nlm.nih.gov/22459917/), [PMID: 19649769](https://pubmed.ncbi.nlm.nih.gov/19649769/)).

---

## 7. Controversies and Open Questions

**Strongly supported claims.** The following are backed by convergent structural, kinetic, and genetic evidence: (i) ArgJ is an Ntn hydrolase using a Thr nucleophile and a ping-pong acetyl-enzyme mechanism ([PMID: 19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/), [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/)); (ii) NAGK arginine sensitivity requires an N-terminal helix and hexameric assembly ([PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/), [PMID: 22101454](https://pubmed.ncbi.nlm.nih.gov/22101454/)); (iii) the three terminal enzymes are three distinct folds ([PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/), [PMID: 11844799](https://pubmed.ncbi.nlm.nih.gov/11844799/), [PMID: 7634077](https://pubmed.ncbi.nlm.nih.gov/7634077/)); and (iv) the AOTCase/SOTCase specificity switch is a single-residue effect ([PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/)).

**Where the literature disagrees or relies on indirect evidence.**

1. **Direction of evolution (acetyl vs. carrier-protein first).** The phylogenetic case that the LysW/AmCP carrier route is *ancestral* to acetyl-based protection is suggestive but rests on reconstruction and substrate-promiscuity assays rather than direct ancestral resurrection [PMID: 41047751](https://pubmed.ncbi.nlm.nih.gov/41047751/). Whether acetylation is a derived simplification of a carrier-protein ancestor, or an independent invention, remains open.

2. **The "true" control point across lineages.** NAGK is the control node in many bacteria, but NAGS regulation dominates in others, and yeast couples both in a metabolon ([PMID: 22529931](https://pubmed.ncbi.nlm.nih.gov/22529931/)). Generalizing "NAGK is the rate-limiting step" from *Corynebacterium/Pseudomonas* to all microbes is unsafe.

3. **Monofunctional vs. bifunctional ArgJ boundaries.** The archaeal-monofunctional / bacterial-bifunctional dichotomy comes largely from a handful of thermophiles [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/); how cleanly it holds across the full diversity of archaea and bacteria is not established.

4. **Organism-mixing in the terminal steps.** Much OTCase/ASS/ASL mechanistic detail derives from vertebrate/urea-cycle or δ-crystallin systems ([PMID: 7634077](https://pubmed.ncbi.nlm.nih.gov/7634077/), [PMID: 15273245](https://pubmed.ncbi.nlm.nih.gov/15273245/)). Because effector signs and physiological direction differ between microbial biosynthesis and vertebrate ureagenesis (e.g., the NAG inversion, [PMID: 12633501](https://pubmed.ncbi.nlm.nih.gov/12633501/)), transferring regulatory conclusions requires caution.

**Most important open questions.**
- Is there a resurrectable ancestral N-modifying enzyme that clarifies whether acetyl or carrier-protein protection came first?
- What determines, mechanistically and ecologically, why some organisms retain both ArgE and ArgJ ([PMID: 26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/))?
- Type-1 vs. type-2 ArgC families are named in the module outline but remain poorly characterized functionally; what distinguishes them, and does the distinction matter for flux?
- Can the single-residue plasticity of transcarbamylase substrate specificity ([PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/)) and OTCase allostery ([PMID: 2667139](https://pubmed.ncbi.nlm.nih.gov/2667139/)) be leveraged to build designer bypass routes?

---

## 8. Mechanistic Model and Synthesis

The module is best understood as **a protected-intermediate assembly line** whose central innovation is reversible chemical masking of the glutamate α-amino group. Two logically independent design choices define an organism's implementation:

| Design axis | Linear implementation | Cyclic implementation |
|-------------|----------------------|-----------------------|
| **Acetyl source (step 1)** | Dedicated NAGS/ArgA (GNAT fold) from acetyl-CoA | Bifunctional ArgJ (Ntn hydrolase) from acetyl-CoA (priming) *or* recycled acetyl |
| **Deprotection (step 5)** | ArgE hydrolysis → acetate lost (M20 metallohydrolase) | ArgJ transacetylation → acetyl recycled onto glutamate |
| **Energetic cost** | 1 acetyl-CoA per ornithine (stoichiometric) | 1 acetyl-CoA only to prime the cycle (catalytic) |
| **Typical taxa / genes** | *E. coli*; dispersed *argA*, *argECBH* | Gram-positives, thermophiles, archaea; compact *argCJBD(F)* operons |
| **Flux control** | NAGS and/or NAGK, arginine feedback | NAGK, arginine feedback; ArgJ inhibited by ornithine |

Downstream of ornithine, the module converges on a single conserved three-enzyme cassette (ArgF→ArgG→ArgH) built from three unrelated folds, indicating that the terminal chemistry was assembled from independently evolved parts rather than duplicated from a common ancestor. The evolutionary picture is therefore of a **conserved core** (the phosphorylation–reduction–transamination sequence, steps 2–4, plus the terminal cassette) decorated with a **highly labile entry point** (step 1/step 5 acetyl management) and surrounded by **non-homologous alternatives** (LysW, AOTCase, SOTCase) that solve the same amine-protection problem with different chemistry, sometimes separated from the canonical enzymes by a single residue.

---

## 9. Limitations and Knowledge Gaps

- **This review is a literature synthesis, not a primary data analysis.** No sequence datasets or structures were computed here; conclusions rest on the cited primary and review literature.
- **Taxonomic sampling bias.** Much mechanistic detail comes from a small set of model organisms (*E. coli*, *P. aeruginosa*, *C. glutamicum*, a few thermophiles, yeast) and may not generalize.
- **Type-1/Type-2 ArgC distinction under-resolved.** The module outline names two ArgC families, but the literature reviewed does not cleanly delineate their functional differences beyond the ProA/ArgC ancestry evidence ([PMID: 18757760](https://pubmed.ncbi.nlm.nih.gov/18757760/)).
- **Vertebrate/microbial conflation risk.** Terminal-enzyme structural insight is partly borrowed from urea-cycle and δ-crystallin systems, where regulation differs.

## 10. Proposed Follow-up Actions

1. **Ancestral sequence reconstruction** of the step-1 enzymes (NAGS vs. bifunctional ArgJ) and of the LysW ligases to test directly whether carrier-protein protection preceded acetylation.
2. **Systematic biochemical comparison of Type-1 vs. Type-2 ArgC** families (kinetics, cofactor use, structure) to determine whether the split is functionally meaningful.
3. **Phylogenomic survey** of ArgE/ArgJ co-occurrence to explain the *S. meliloti*-type dual-route organisms and quantify how common redundancy is.
4. **Structure-guided engineering** exploiting the single-residue transcarbamylase specificity switch and NAGK feedback-resistance mutations to build high-titer, deregulated arginine producers.
5. **Antibacterial inhibitor development** against the dinuclear ArgE metallo-active site, capitalizing on its absence from humans.

---

## 11. Key References

- Marc et al. 2000 — mono/bifunctional ArgJ, ping-pong mechanism. [PMID: 10931207](https://pubmed.ncbi.nlm.nih.gov/10931207/)
- Iqbal et al. 2009 — ArgJ as Ntn hydrolase, Thr-181 acetyl-enzyme. [PMID: 19105697](https://pubmed.ncbi.nlm.nih.gov/19105697/)
- Yang et al. 2017 — *M. tuberculosis* ArgA GNAT fold. [PMID: 28943401](https://pubmed.ncbi.nlm.nih.gov/28943401/)
- Fernández-Murga & Rubio 2008 — NAGK hexamer/N-helix and arginine feedback. [PMID: 18263723](https://pubmed.ncbi.nlm.nih.gov/18263723/)
- Xu et al. 2012 — *C. glutamicum* NAGK feedback residues. [PMID: 22101454](https://pubmed.ncbi.nlm.nih.gov/22101454/)
- Feedback-resistant NAGK, ~42% titer increase. [PMID: 21901472](https://pubmed.ncbi.nlm.nih.gov/21901472/)
- Caldovic & Tuchman 2003 — N-acetylglutamate, two routes, vertebrate inversion. [PMID: 12633501](https://pubmed.ncbi.nlm.nih.gov/12633501/)
- Horie et al. 2009 — LysW N-modification, absence of ArgA/ArgJ. [PMID: 19620981](https://pubmed.ncbi.nlm.nih.gov/19620981/)
- Shi et al. 2026 — AmCP/LysW route as primitive ancestor. [PMID: 41047751](https://pubmed.ncbi.nlm.nih.gov/41047751/)
- Shimizu et al. 2016 — LysY vs. ArgC discrimination. [PMID: 26966182](https://pubmed.ncbi.nlm.nih.gov/26966182/)
- Heimberg et al. 1990 — ArgD/OAT homology, substrate ambiguity. [PMID: 2199330](https://pubmed.ncbi.nlm.nih.gov/2199330/)
- McLoughlin & Copley 2008 — ProA→ArgC promiscuity. [PMID: 18757760](https://pubmed.ncbi.nlm.nih.gov/18757760/)
- Genetic/biochemical characterization of *S. meliloti* dual ArgE+ArgJ. [PMID: 26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/)
- McGregor et al. 2007 — ArgE Mn(II) kinetics. [PMID: 17333302](https://pubmed.ncbi.nlm.nih.gov/17333302/)
- Tao et al. 2012 — ArgE dinuclear site EXAFS. [PMID: 22459917](https://pubmed.ncbi.nlm.nih.gov/22459917/)
- de Cima et al. 2012 — yeast NAGK metabolon/DUF619. [PMID: 22529931](https://pubmed.ncbi.nlm.nih.gov/22529931/)
- Llácer et al. 2008 — PII–NAGK nitrogen storage. [PMID: 19013524](https://pubmed.ncbi.nlm.nih.gov/19013524/)
- OTCase anabolic vs. catabolic unidirectionality. [PMID: 8617277](https://pubmed.ncbi.nlm.nih.gov/8617277/)
- OTCase allostery by point mutation. [PMID: 2667139](https://pubmed.ncbi.nlm.nih.gov/2667139/); C-terminus effects [PMID: 8168544](https://pubmed.ncbi.nlm.nih.gov/8168544/), [PMID: 8790344](https://pubmed.ncbi.nlm.nih.gov/8790344/)
- ArgG/ASS fold and mechanism. [PMID: 11844799](https://pubmed.ncbi.nlm.nih.gov/11844799/), [PMID: 11809762](https://pubmed.ncbi.nlm.nih.gov/11809762/), [PMID: 3863125](https://pubmed.ncbi.nlm.nih.gov/3863125/)
- ArgH/ASL and δ-crystallin gene sharing. [PMID: 7634077](https://pubmed.ncbi.nlm.nih.gov/7634077/), [PMID: 10029536](https://pubmed.ncbi.nlm.nih.gov/10029536/), [PMID: 15273245](https://pubmed.ncbi.nlm.nih.gov/15273245/)
- AOTCase/SOTCase single-residue switch. [PMID: 17600144](https://pubmed.ncbi.nlm.nih.gov/17600144/)
- ArgR/AhrC regulation, operon organization. [PMID: 15342575](https://pubmed.ncbi.nlm.nih.gov/15342575/), [PMID: 14762010](https://pubmed.ncbi.nlm.nih.gov/14762010/), [PMID: 16504055](https://pubmed.ncbi.nlm.nih.gov/16504055/)
- NAGS domain dissection / NAGK ancestry. [PMID: 22447897](https://pubmed.ncbi.nlm.nih.gov/22447897/)
- Engineering: external NAG feeding to *argA* strain. [PMID: 37495979](https://pubmed.ncbi.nlm.nih.gov/37495979/)
- ArgE inhibitor development. [PMID: 19649769](https://pubmed.ncbi.nlm.nih.gov/19649769/)


## Artifacts

- [OpenScientist final report](arginine_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](arginine_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19620981
2. PMID:12633501
3. PMID:8617277
4. PMID:17600144
5. PMID:28943401
6. PMID:22447897
7. PMID:19105697
8. PMID:10931207
9. PMID:18263723
10. PMID:22101454
11. PMID:21901472
12. PMID:18757760
13. PMID:2199330
14. PMID:17333302
15. PMID:22459917
16. PMID:2667139
17. PMID:8168544
18. PMID:8790344
19. PMID:11844799
20. PMID:11809762
21. PMID:3863125
22. PMID:7634077
23. PMID:10029536
24. PMID:15273245
25. PMID:15342575
26. PMID:14762010
27. PMID:16504055
28. PMID:26271664
29. PMID:22529931
30. PMID:19013524
31. PMID:41047751
32. PMID:26966182
33. PMID:37495979
34. PMID:19649769