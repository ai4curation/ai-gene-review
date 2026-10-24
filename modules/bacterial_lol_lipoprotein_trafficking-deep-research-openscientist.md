---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:22:27.886785'
end_time: '2026-09-01T02:41:08.920949'
duration_seconds: 1121.03
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial Lol-dependent outer-membrane lipoprotein trafficking
  module_summary: A species-neutral diderm-bacterial module for ATP-dependent release
    of outer-membrane-destined mature lipoproteins from the inner membrane by LolCDE,
    periplasmic carriage by LolA, and delivery into the outer membrane by LolB. Lipoprotein
    maturation and inner-membrane retention decisions are upstream of this module.
  module_outline: "- Bacterial Lol-dependent outer-membrane lipoprotein trafficking\n\
    \  - 1. ATP-dependent inner-membrane extraction and release\n  - LolCDE lipoprotein\
    \ release\n    - LolCDE lipoprotein-release complex (molecular player: LolCDE\
    \ ABC lipoprotein-release complex; activity or role: ATP-dependent lipoprotein\
    \ extraction and release activity)\n  - 2. Periplasmic lipoprotein carriage\n\
    \  - LolA periplasmic carriage\n    - LolA periplasmic lipoprotein carrier (molecular\
    \ player: LolA family; activity or role: periplasmic lipoprotein carrier activity)\n\
    \  - 3. Outer-membrane delivery and incorporation\n  - LolB outer-membrane delivery\n\
    \    - LolB outer-membrane lipoprotein receptor (molecular player: LolB family;\
    \ activity or role: outer-membrane lipoprotein delivery activity)"
  module_connections: '- LolCDE lipoprotein release feeds into LolA periplasmic carriage:
    LolCDE loads released lipoprotein onto LolA.

    - LolA periplasmic carriage feeds into LolB outer-membrane delivery: LolA presents
    its lipoprotein cargo to LolB.'
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
citation_count: 25
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_lol_lipoprotein_trafficking-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_lol_lipoprotein_trafficking-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial Lol-dependent outer-membrane lipoprotein trafficking

## Working Scope

A species-neutral diderm-bacterial module for ATP-dependent release of outer-membrane-destined mature lipoproteins from the inner membrane by LolCDE, periplasmic carriage by LolA, and delivery into the outer membrane by LolB. Lipoprotein maturation and inner-membrane retention decisions are upstream of this module.

## Provisional Biological Outline

- Bacterial Lol-dependent outer-membrane lipoprotein trafficking
  - 1. ATP-dependent inner-membrane extraction and release
  - LolCDE lipoprotein release
    - LolCDE lipoprotein-release complex (molecular player: LolCDE ABC lipoprotein-release complex; activity or role: ATP-dependent lipoprotein extraction and release activity)
  - 2. Periplasmic lipoprotein carriage
  - LolA periplasmic carriage
    - LolA periplasmic lipoprotein carrier (molecular player: LolA family; activity or role: periplasmic lipoprotein carrier activity)
  - 3. Outer-membrane delivery and incorporation
  - LolB outer-membrane delivery
    - LolB outer-membrane lipoprotein receptor (molecular player: LolB family; activity or role: outer-membrane lipoprotein delivery activity)

## Known Relationships Among Steps

- LolCDE lipoprotein release feeds into LolA periplasmic carriage: LolCDE loads released lipoprotein onto LolA.
- LolA periplasmic carriage feeds into LolB outer-membrane delivery: LolA presents its lipoprotein cargo to LolB.

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

# Bacterial Lol-Dependent Outer-Membrane Lipoprotein Trafficking

*A commissioned review-style synthesis*

---

## 1. Executive Summary

Gram-negative (diderm) bacteria confront a topological problem that monoderm bacteria do not: many of their lipoproteins are synthesized and lipid-anchored at the inner (cytoplasmic) membrane, yet must be delivered across an aqueous periplasm to the inner leaflet of the outer membrane. The **localization of lipoproteins (Lol) pathway** solves this problem as a dedicated, three-step relay. An ATP-binding-cassette (ABC) transporter, **LolCDE**, recognizes and extracts mature, triacylated, outer-membrane-destined lipoproteins from the inner membrane using the energy of ATP hydrolysis. The extracted cargo is handed to the soluble periplasmic chaperone **LolA**, which shields the hydrophobic acyl chains from water and ferries the lipoprotein across the periplasm. LolA then presents its cargo to the outer-membrane receptor **LolB**, which inserts the lipoprotein into the inner leaflet of the outer membrane. This can be summarized as a directional "mouth-to-mouth" transfer relay: LolCDE → LolA → LolB.

Three features define the system's logic and are strongly supported by convergent biochemical, genetic, and structural data. First, **energy input is confined to the LolCDE extraction step**; all downstream transfers (LolC→LolA→LolB→outer membrane) proceed spontaneously down an affinity gradient without further ATP. Second, **entry into the pathway is gated upstream** by two independent checkpoints — obligatory Lnt-dependent N-acylation of the lipoprotein's N-terminal cysteine (maturation), and a "+2 rule" sorting/avoidance signal that determines whether a lipoprotein is retained in the inner membrane or released for outer-membrane trafficking. Third, the system shows **architectural and phylogenetic variation**: LolCDE is a heterodimeric LolC/LolE transmembrane pair in *E. coli* but a homodimeric LolDF/LolF transporter in many critical pathogens, LolB appears to be a comparatively recent, lineage-restricted elaboration, and the whole extractor module is an evolutionary specialization of the ancient **MacB/type VII "mechanotransmission" ABC superfamily**.

Perhaps the most important conceptual refinement to emerge from recent work is a re-drawing of what is truly "essential." **LolCDE-catalyzed extraction is the single obligatory, non-bypassable step** and is a validated, actively pursued antibiotic target. In contrast, LolA and LolB — long considered individually essential — can be genetically bypassed when the toxic consequences of lipoprotein mislocalization are neutralized and the Cpx envelope-stress response is activated. This implies their essentiality is largely a matter of preventing lethal mislocalization rather than performing an irreplaceable chemical step in transfer. The remainder of this review develops these points, delineates the system's boundaries against neighboring pathways, and flags where the evidence is strong, indirect, or genuinely contested.

---

## 2. Definition and Biological Boundaries

### What the system is

The Lol pathway, in the species-neutral sense intended by this brief, is the **post-maturation, ATP-dependent module that moves outer-membrane-destined mature lipoproteins from the inner membrane, across the periplasm, to the outer membrane** of diderm bacteria. Its canonical components are five proteins: the inner-membrane ABC transporter subunits LolC, LolD, and LolE (assembled as LolCDE), the periplasmic carrier LolA, and the outer-membrane receptor LolB ([PMID: 15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/); [PMID: 21663440](https://pubmed.ncbi.nlm.nih.gov/21663440/)). The module's core outputs are (i) selective release of the correct subset of lipoproteins from the inner membrane and (ii) their correct insertion into the outer membrane.

### What lies upstream (and should not be conflated)

Lipoprotein **biogenesis and maturation** are prerequisites but are mechanistically distinct from Lol trafficking. Precursor lipoproteins are lipid-modified in three enzymatic steps at the inner membrane: diacylglyceryl transfer (Lgt), signal-peptide cleavage (LspA), and N-acylation of the newly exposed N-terminal cysteine (Lnt). N-acylation by Lnt is **obligatory** for Lol-dependent release: aminoacylation of the N-terminal cysteine is required for LolCDE to detach the lipoprotein, and this requirement is independent of the downstream sorting signal ([PMID: 12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/)). Maturation enzymes (Lgt, LspA, Lnt) are therefore best treated as an **upstream boundary** of the module, not part of the relay itself, even though they are frequently discussed together and are also antibiotic targets.

### The sorting checkpoint as the pathway's "gate"

The **inner-membrane-retention / Lol-avoidance decision** is likewise upstream of, but tightly coupled to, LolCDE recognition. In *E. coli* the residue at position +2 (immediately after the lipidated Cys) determines destiny: Asp at +2, together with a permissive residue at +3, retains a lipoprotein in the inner membrane by blocking LolCDE recognition ([PMID: 11592971](https://pubmed.ncbi.nlm.nih.gov/11592971/); [PMID: 15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/)). This "avoidance" is not a passive property of the peptide alone: the Asp+2 carboxylate must ion-pair with the amine of phosphatidylethanolamine (PE), and chemical modification of either partner abolishes avoidance ([PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)). Thus the gate is a lipid–protein co-recognition event that decides whether a lipoprotein is even a substrate for the module.

### Neighboring pathways often confused with Lol

- **Lpt (lipopolysaccharide transport) pathway.** Lpt is frequently described in parallel with Lol because it is another inner-membrane-to-outer-membrane trafficking system with an ABC transporter (LptB₂FG) that "detaches" its substrate from the inner membrane, and the analogy is explicitly drawn in the literature ([PMID: 21670534](https://pubmed.ncbi.nlm.nih.gov/21670534/)). However, Lpt moves LPS via a continuous periplasmic protein bridge, not a diffusible chaperone, and shares no components with Lol. It should be treated separately.
- **Bam (β-barrel assembly machinery).** Bam folds and inserts outer-membrane β-barrel proteins and itself depends on Lol-delivered lipoprotein subunits (e.g., BamB–E), so it is a *downstream client* of Lol rather than part of it ([PMID: 19270402](https://pubmed.ncbi.nlm.nih.gov/19270402/)).
- **Surface-exposure / "flipping" machineries.** A subset of lipoproteins is further translocated to the cell surface or undergoes topological change in the outer membrane after Lol delivery ([PMID: 27871940](https://pubmed.ncbi.nlm.nih.gov/27871940/); [PMID: 27720009](https://pubmed.ncbi.nlm.nih.gov/27720009/)). These surface-targeting steps are distinct terminal events and are not part of the Lol relay proper.

### Competing definitions

There is no serious dispute over the five canonical components, but there are two definitional tensions. One is **whether LolA and LolB are "core essential machinery" or accessory safeguards** — recent bypass experiments argue for the latter interpretation ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)). The other is **how broadly "LolCDE" should be defined**, given that the physiological transporter in many lineages is the homodimeric LolDF/LolF rather than the *E. coli* heterodimer ([PMID: 42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/)). A species-neutral definition should treat "the Lol extractor" as a family of related ABC transporters rather than a single fixed subunit composition.

---

## 3. Mechanistic Overview

### The best current model, step by step

**Step 0 — Gating (upstream).** A mature, triacylated lipoprotein bearing a permissive +2/+3 signal (i.e., *not* Asp+2/PE-paired) is available at the inner-membrane surface. Lnt-mediated N-acylation has already occurred and is required for what follows ([PMID: 12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/); [PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)).

**Step 1 — Recognition and ATP-driven extraction (obligatory).** LolCDE recognizes the substrate through both its lipid moiety and its N-terminal peptide, with the amide-linked acyl chain acting as a key contact. Cryo-EM of nanodisc-embedded *E. coli* LolCDE, solved in nucleotide-free (3.8 Å) and nucleotide-bound (3.5 Å) states, shows that ATP binding drives large-scale, **asymmetric** movements of the transmembrane helices and periplasmic domains that **extrude** the captured lipoprotein upward and outward ([PMID: 34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/)). Notably, LolCDE does not translocate its substrate *across* the membrane; instead it performs work in the periplasmic space — the hallmark of "mechanotransmission" (see Section 4).

**Step 2 — Recruitment and priming of LolA (decoupled from ATP).** The periplasmic domain of LolC recruits LolA from the periplasm using a solvent-exposed β-hairpin loop (the "**Hook**") and a trio of surface residues (the "**Pad**"), which capture LolA and prime it to receive cargo ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)). Critically, LolA association with the transporter is **independent of nucleotide binding and hydrolysis**, and the recruitment site sits at least ~50 Å above the inner membrane ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)). Photo-cross-linking independently maps the LolA docking surface specifically to **LolC — not LolE or LolD** — establishing directionality ([PMID: 19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/)). Recruitment (spatial positioning of the acceptor) is therefore mechanistically separable from extrusion (ATP-driven release of cargo).

**Step 3 — Cargo transfer to LolA and periplasmic carriage.** The extruded lipoprotein is transferred to LolA's hydrophobic cavity, forming a soluble 1:1 LolA–lipoprotein complex that diffuses across the periplasm ([PMID: 15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/)). LolA's α-helical "lid" over its β-barrel cavity opens and closes to admit and sequester acyl chains, a motion characterized by molecular-dynamics studies ([PMID: 23962984](https://pubmed.ncbi.nlm.nih.gov/23962984/)).

**Step 4 — Hand-off to LolB and outer-membrane insertion.** LolA presents its cargo to LolB, an outer-membrane-anchored lipoprotein with a fold remarkably similar to LolA (an unclosed β-barrel plus α-helical lid enclosing a hydrophobic cavity) despite low sequence identity ([PMID: 12839983](https://pubmed.ncbi.nlm.nih.gov/12839983/); [PMID: 15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/)). Transfer proceeds because LolB has higher affinity for the lipoprotein than LolA — the transfer is energy-independent and effectively irreversible. A protruding loop on LolB (absent from LolA), including a critical leucine (Leu68 in *E. coli*), is required not for accepting cargo but for the final **insertion** into the outer membrane; mutants that accept but cannot localize lipoproteins dissect these two sub-steps ([PMID: 24569999](https://pubmed.ncbi.nlm.nih.gov/24569999/)).

### Which steps are obligatory, conditional, or accessory

| Step | Status | Basis |
|---|---|---|
| Lnt N-acylation (maturation) | Obligatory prerequisite | N-acylation required for release ([PMID: 12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/)) |
| Correct +2/+3 sorting | Conditional gate | Determines substrate vs. non-substrate ([PMID: 11592971](https://pubmed.ncbi.nlm.nih.gov/11592971/); [PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)) |
| LolCDE ATP-driven extraction | **Obligatory, non-bypassable** | Essential, druggable; the one irreplaceable step ([PMID: 34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/); [PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)) |
| LolA carriage | Normally essential, **bypassable** | Bypass via stress response ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)) |
| LolB insertion | Normally essential, **bypassable** | Bypass via stress response ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)) |

### The energetic logic

The system is best understood as **one pump feeding a downhill affinity cascade**. ATP hydrolysis at LolD's nucleotide-binding domains does all the thermodynamic work of prying a lipid-anchored protein out of a bilayer. Everything after that — LolC→LolA, LolA→LolB, LolB→outer membrane — is driven by a stepwise increase in binding affinity for the cargo, requiring no further energy input ([PMID: 15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/); [PMID: 21670534](https://pubmed.ncbi.nlm.nih.gov/21670534/)). This is why LolA and LolB can be modeled as passive-but-directional carriers rather than motors.

---

## 4. Major Molecular Players and Active Assemblies

### LolCDE — the ATP-dependent extractor

LolCDE is an ABC transporter with two nucleotide-binding subunits (LolD, cytoplasmic ATPases) and two transmembrane subunits. In *E. coli* the transmembrane subunits are the **heterodimeric pair LolC and LolE**; each has a large periplasmic domain. The central lipoprotein-binding cavity is formed by four helices, and photo-cross-linking of the peptidoglycan-associated lipoprotein Pal across these helices has mapped substrate contacts and shown that at least one LolCDE inhibitor promotes dissociation of bound lipoprotein rather than blocking initial binding ([PMID: 38156779](https://pubmed.ncbi.nlm.nih.gov/38156779/)). The cryo-EM structures define the ATP-driven, asymmetric conformational cycle that extrudes cargo ([PMID: 34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/)). LolC additionally carries the LolA recruitment machinery (Hook and Pad) on its periplasmic domain ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)).

LolCDE is a **validated antibiotic target**. Multiple chemically distinct inhibitors map to LolC or LolE: pyridineimidazoles ([PMID: 25583975](https://pubmed.ncbi.nlm.nih.gov/25583975/)), the pyrrolopyrimidinedione G0507 ([PMID: 29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/)), pyrazole compounds identified in a cell-wall reporter screen ([PMID: 25733621](https://pubmed.ncbi.nlm.nih.gov/25733621/)), and SMT-738 targeting Enterobacteriaceae ([PMID: 38084954](https://pubmed.ncbi.nlm.nih.gov/38084954/)). These inhibitors block LolA-dependent release of lipoproteins such as Lpp from spheroplasts, confirming LolCDE extraction as their mechanism of action ([PMID: 25583975](https://pubmed.ncbi.nlm.nih.gov/25583975/)).

### LolA — the periplasmic carrier

LolA is a soluble, monomeric periplasmic chaperone with an unclosed β-barrel capped by an α-helical lid, enclosing a hydrophobic cavity sized to accept acyl chains ([PMID: 12839983](https://pubmed.ncbi.nlm.nih.gov/12839983/)). It shields the lipid moiety from water during transit. Its lid undergoes open→closed conformational transitions that regulate cargo loading and release ([PMID: 23962984](https://pubmed.ncbi.nlm.nih.gov/23962984/)). LolA docks specifically onto the LolC periplasmic domain via the Hook/Pad interface and is primed there nucleotide-independently before cargo transfer ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/); [PMID: 19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/)).

### LolB — the outer-membrane receptor/inserter

LolB is itself an outer-membrane lipoprotein whose fold closely mirrors LolA — the two share the unclosed-β-barrel-plus-lid architecture despite low sequence identity, a striking case of structural conservation enabling cavity-to-cavity lipid transfer ([PMID: 12839983](https://pubmed.ncbi.nlm.nih.gov/12839983/)). LolB has two separable activities: **accepting** cargo from LolA and **inserting** it into the outer membrane. A protruding hydrophobic loop unique to LolB (critical residue Leu68) mediates the insertion step; acidic substitutions there generate receptors that bind but cannot localize lipoproteins ([PMID: 24569999](https://pubmed.ncbi.nlm.nih.gov/24569999/)). Interestingly, LolB's own membrane anchor is functionally dispensable, indicating the protruding-loop insertion chemistry, not the anchor, is the essential feature.

### The relay interface — a shared "mouth"

In-vivo photo-cross-linking (pBPA) identifies a shared "hot area" at the mouth of the hydrophobic cavities of LolA and LolB through which they interact; the same LolA surface engages LolC ([PMID: 19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/)). This defines a single, reused **mouth-to-mouth transfer geometry** across the entire relay and explains its directionality.

```
   INNER MEMBRANE                PERIPLASM                 OUTER MEMBRANE
 ┌───────────────┐
 │   LolC / LolE │   Hook/Pad
 │   (TMDs)      │──recruits──►  LolA ──diffuses──►  LolB ──inserts──►  OM inner leaflet
 │      │        │  (no ATP)   (lid opens/       (mouth-to-      (protruding loop,
 │   LolD/LolD   │              closes cavity)    mouth transfer)  Leu68)
 │  (ATPase)     │
 └──────┬────────┘
        │ ATP hydrolysis → asymmetric TMH/periplasmic-domain motion → EXTRUSION
        ▼
   (the ONE obligatory energy-requiring step)
```

---

## 5. Evolutionary and Cell-Biological Variation

### Deep origin: LolCDE as a specialized MacB-family mechanotransmitter

The most robust evolutionary statement is that **LolCDE is a specialization of the ancient MacB / type VII ABC transporter superfamily**. MacB adopts a fold distinct from other structurally characterized ABC transporters and uses "**mechanotransmission**": it couples cytoplasmic ATP hydrolysis to transmembrane conformational changes that perform work in the extra-cytoplasmic space, *without* transporting substrate across the membrane ([PMID: 29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/)). This superfamily is functionally diverse — tripartite drug efflux (MacAB–TolC), antibiotic sensing, cell division, and lipoprotein trafficking — and the reviews that define the family explicitly place lipoprotein trafficking (LolCDE) within it ([PMID: 29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/)). The cryo-EM LolCDE mechanism — extrusion via asymmetric TMH/periplasmic-domain motion — is directly compared to MacB, cementing LolCDE as a type VII ABC transporter ([PMID: 34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/)). The implication is that the **ancestral capability** was mechanotransmission (moving/manipulating things in the periplasm), and lipoprotein extraction is a derived, specialized application of it. For understanding the ancestral role, generic MacB-family mechanotransmitters — not the lipoprotein-specialized LolCDE — are the best representatives.

### Transporter architecture varies across lineages

The extractor's subunit composition is **not universal**. *E. coli* and related enterobacteria use a **heterodimeric LolC/LolE** transmembrane pair. However, many critical Gram-negative pathogens — notably *Acinetobacter baumannii* — use a **homodimeric LolDF/LolF** transporter, whose recent cryo-EM structure reveals a distinct druggable conformation and the mechanism of the antibiotic abaucin ([PMID: 42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/)). This is the single most important lineage-level variation for both mechanism and drug discovery: inhibitors optimized against the LolC/LolE heterodimer may not translate to LolDF-type transporters, and vice versa.

### LolB is comparatively restricted; the carrier/receptor as "add-ons"

Whereas the LolCDE-type extractor is broadly conserved, **LolB appears to be a later, lineage-restricted elaboration**, most clearly established in γ-proteobacteria such as *E. coli*. The consensus emerging from cross-organism comparisons is that the **extractor is the ancient core** and that the soluble carrier (LolA) and outer-membrane receptor (LolB) are **later additions** to the module. This is consistent with the observation that LolA/LolB are genetically bypassable, whereas the extractor is not ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)). Some lineages likely accomplish periplasmic carriage and outer-membrane delivery with non-orthologous or additional factors; the *E. coli* LolA/LolB solution should not be assumed universal.

### Cross-species portability of the sorting logic

The *E. coli* LolCDE system can correctly sort lipoproteins into the inner and outer membranes of *Pseudomonas aeruginosa*, indicating that the recognition logic is portable across at least some γ-proteobacterial lineages ([PMID: 30992347](https://pubmed.ncbi.nlm.nih.gov/30992347/)). This supports a conserved core recognition mechanism even where peripheral details differ.

### Physiological-state variation

The clearest "physiological-state" variation is the **Cpx envelope-stress-dependent bypass** of LolA/LolB: under conditions that remove toxic mislocalized substrates and activate the stress response, trafficking of essential lipoproteins proceeds without LolA or LolB ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)). This shows the pathway's apparent "hard-wiring" is partly conditional on cellular state.

---

## 6. Constraints, Dependencies, and Failure Modes

### Obligatory ordering

1. **Maturation before release.** Lnt N-acylation must precede LolCDE recognition; unacylated lipoproteins are not released ([PMID: 12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/)).
2. **Recognition/gating before extraction.** The +2/+3 signal (and its PE dependence) is evaluated before, and determines, extraction ([PMID: 11592971](https://pubmed.ncbi.nlm.nih.gov/11592971/); [PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)).
3. **Extraction before carriage before delivery.** The relay is strictly directional — LolC→LolA→LolB→OM — as enforced by the reused mouth-to-mouth interface and the affinity gradient ([PMID: 19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/)).
4. **Recruitment can precede/parallel extrusion but is decoupled from it.** LolA is recruited nucleotide-independently, so acceptor positioning is not slaved to the ATPase cycle ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)).

### Compartment- and substrate-specificity

- **Compartment specificity:** LolD ATPase activity is cytoplasmic; recruitment/transfer are periplasmic (≥50 Å above the membrane); insertion is at the outer membrane. Each sub-reaction is confined to its compartment ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)).
- **Substrate specificity by lipid+peptide:** Recognition requires the amide-linked acyl chain plus N-terminal peptide; the avoidance signal is a lipid–protein ion pair (Asp+2·PE) ([PMID: 34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/); [PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)).
- **Mutual exclusivity:** A lipoprotein is either retained (avoidance signal present) or trafficked; the PE-dependent avoidance complex (effectively five acyl chains) cannot be recognized by LolCDE ([PMID: 15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/)).

### Failure modes

- **Loss of LolCDE** → lethal accumulation of outer-membrane lipoproteins in the inner membrane; no bypass known — hence its value as a drug target ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)).
- **Loss of LolA/LolB** → normally lethal *because* substrates mislocalize toxically, but bypassable when that toxicity is removed and Cpx is active ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)).
- **LolB insertion-loop mutation** → cargo is accepted but not inserted, trapping lipoprotein on a competent receptor ([PMID: 24569999](https://pubmed.ncbi.nlm.nih.gov/24569999/)).
- **Maturation failure (e.g., Lgt inhibition)** → outer-membrane permeabilization, increased antibiotic/serum sensitivity ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)).

### Evidence ruling out otherwise-plausible paths

The specific LolA→LolC (not LolE/LolD) cross-linking rules out a symmetric or LolE-mediated hand-off, constraining the geometry of extraction-to-carriage coupling ([PMID: 19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/)). The nucleotide-independence of LolA recruitment rules out models in which acceptor docking is itself ATP-gated ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)).

---

## 7. Controversies and Open Questions

**1. Are LolA and LolB truly essential machinery or safeguards against mislocalization?** The bypass experiments strongly argue that LolCDE extraction is the only irreplaceable chemical step, and that LolA/LolB essentiality reflects prevention of toxic mislocalization plus stress-response buffering ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)). This reframing is well supported but still being integrated into textbook models; how substrates reach the outer membrane in the bypass state (diffusion? alternative factors?) is unresolved.

**2. What is the exact substrate-transfer chemistry at each interface?** The mouth-to-mouth model and affinity-gradient logic are well supported ([PMID: 19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/); [PMID: 12839983](https://pubmed.ncbi.nlm.nih.gov/12839983/)), but the atomic choreography of acyl-chain threading from LolCDE→LolA and LolA→LolB — and how the LolCDE inhibitor that promotes lipoprotein *dissociation* fits in — remains incompletely resolved ([PMID: 38156779](https://pubmed.ncbi.nlm.nih.gov/38156779/)).

**3. How generalizable is the *E. coli* paradigm?** Much of the mechanism is anchored in *E. coli*. The existence of homodimeric LolDF/LolF transporters ([PMID: 42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/)) and the restricted distribution of LolB caution against overgeneralizing. Whether all diderms use a LolA-type soluble carrier, and what receptor (if any) substitutes for LolB in lineages lacking it, are open.

**4. How does the +2/PE avoidance rule vary across species?** The Asp+2·PE ion-pair model is elegantly demonstrated in *E. coli* ([PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)), but sorting rules and membrane-lipid contexts differ across taxa; the extent to which this specific chemistry is conserved is not established.

**5. Is the MacB-family origin the whole story?** The mechanotransmission framework unifies LolCDE with MacB convincingly ([PMID: 29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/); [PMID: 34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/)), but the order and timing of when the soluble carrier and receptor were recruited to build the full three-step relay is inferred, not directly demonstrated by ancestral reconstruction.

**Caveats on the evidence base.** Structural mechanism rests on a small number of cryo-EM/crystal structures; some mechanistic inferences combine data from *E. coli*, *Pseudomonas*, and *Acinetobacter*, which may not be strictly comparable. Several claims (affinity-gradient directionality; bypass physiology) are supported by strong but indirect genetic/biochemical logic rather than direct single-molecule measurement.

---

## 8. Key References

| PMID | Contribution to this review |
|---|---|
| [15276320](https://pubmed.ncbi.nlm.nih.gov/15276320/) | Authoritative overview: LolCDE release → LolA complex → LolB insertion; shared LolA/LolB fold; energy-independent transfer; Lol-avoidance signal and PE dependence |
| [19307584](https://pubmed.ncbi.nlm.nih.gov/19307584/) | Mouth-to-mouth transfer model; LolA docks on LolC not LolE; directional relay |
| [34344901](https://pubmed.ncbi.nlm.nih.gov/34344901/) | Cryo-EM of LolCDE; ATP-driven asymmetric extrusion; type VII "mechanotransmitter" akin to MacB |
| [12839983](https://pubmed.ncbi.nlm.nih.gov/12839983/) | Crystal structures of LolA and LolB; shared unclosed-β-barrel + α-helical-lid architecture |
| [30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/) | LolA–LolC complex; Hook/Pad recruitment; nucleotide-independent, ≥50 Å from membrane |
| [12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/) | Lnt N-acylation obligatory for Lol-dependent release, independent of sorting signal |
| [11592971](https://pubmed.ncbi.nlm.nih.gov/11592971/) | +2/+3 sorting-signal rule gating pathway entry |
| [12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/) | Asp+2·phosphatidylethanolamine ion pair as physical basis of Lol avoidance |
| [28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/) | LolA and LolB genetically bypassable via envelope-stress response; redefines essentiality |
| [42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/) | Homodimeric LolDF/LolF transporter in critical pathogens (A. baumannii); druggable conformation |
| [29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/) | MacB ABC superfamily; mechanotransmission; places lipoprotein trafficking within the family |
| [24569999](https://pubmed.ncbi.nlm.nih.gov/24569999/) | LolB protruding loop / Leu68 required for insertion; separates acceptance from localization |
| [38156779](https://pubmed.ncbi.nlm.nih.gov/38156779/) | Photo-cross-linking dissection of LolCDE substrate cavity; inhibitor promotes dissociation |
| [23962984](https://pubmed.ncbi.nlm.nih.gov/23962984/) | MD simulations of LolA lid open→closed dynamics |
| [30992347](https://pubmed.ncbi.nlm.nih.gov/30992347/) | E. coli LolCDE correctly sorts lipoproteins in P. aeruginosa (portable recognition logic) |
| [25583975](https://pubmed.ncbi.nlm.nih.gov/25583975/) | Pyridineimidazole LolCDE inhibitors mapping to LolC/LolE |
| [29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/) | G0507 LolCDE inhibitor |
| [38084954](https://pubmed.ncbi.nlm.nih.gov/38084954/) | SMT-738 lipoprotein-transport inhibitor for Enterobacteriaceae |
| [25733621](https://pubmed.ncbi.nlm.nih.gov/25733621/) | Pyrazole inhibitors mapping to LolC/LolE; block IM lipoprotein release |
| [33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/) | Lgt (maturation) inhibition permeabilizes OM — upstream boundary |
| [21663440](https://pubmed.ncbi.nlm.nih.gov/21663440/), [19270402](https://pubmed.ncbi.nlm.nih.gov/19270402/), [27871940](https://pubmed.ncbi.nlm.nih.gov/27871940/), [27720009](https://pubmed.ncbi.nlm.nih.gov/27720009/), [21670534](https://pubmed.ncbi.nlm.nih.gov/21670534/) | Reviews: lipoprotein sorting, OM biogenesis, quality control, surface exposure, ABC transporters in OM biogenesis (boundary-setting vs. Lpt/Bam) |

---

## Limitations and Knowledge Gaps (consolidated)

- The mechanistic core is **E. coli-centric**; cross-species generality of LolA/LolB usage, the +2/PE rule, and the affinity-gradient model is inferred, not universally demonstrated.
- **No ancestral-sequence reconstruction** directly dates the recruitment of the carrier/receptor onto the MacB-derived extractor; the "extractor-ancient, carrier/receptor-later" model is a well-motivated inference.
- The **atomic choreography** of cargo hand-off at each interface, and the physiological route in the LolA/LolB-bypass state, remain unresolved.
- Structural coverage is thin (a handful of structures) and mixes organisms; caution is warranted when combining *E. coli*, *Pseudomonas*, and *Acinetobacter* data.

## Proposed Follow-up Experiments / Actions

1. **Cross-lineage structural/functional comparison of LolDF vs LolC/LolE** to define shared vs. divergent extrusion mechanics and inform broad-spectrum vs. pathogen-specific inhibitor design ([PMID: 42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/)).
2. **Time-resolved / single-molecule capture of cargo hand-off** (LolCDE→LolA and LolA→LolB) to test the mouth-to-mouth and affinity-gradient models directly.
3. **Systematic phylogenomic survey** of LolA/LolB presence/absence across diderm phyla to map where the carrier/receptor were added or replaced, and to identify candidate LolB substitutes in LolB-lacking lineages.
4. **Dissect the bypass physiology**: determine how essential lipoproteins reach the OM without LolA/LolB and which Cpx-regulated factors substitute ([PMID: 28416660](https://pubmed.ncbi.nlm.nih.gov/28416660/)).
5. **Test the Asp+2·PE avoidance rule in non-enterobacterial species** with differing membrane lipid compositions to assess conservation of the gating chemistry ([PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)).
6. **Ancestral-sequence reconstruction of the MacB→LolCDE transition** to test the "specialization of an ancient mechanotransmitter" hypothesis directly ([PMID: 29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/)).


## Artifacts

- [OpenScientist final report](bacterial_lol_lipoprotein_trafficking-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_lol_lipoprotein_trafficking-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15276320
2. PMID:21663440
3. PMID:12198129
4. PMID:11592971
5. PMID:12896969
6. PMID:21670534
7. PMID:19270402
8. PMID:27871940
9. PMID:27720009
10. PMID:28416660
11. PMID:42091888
12. PMID:34344901
13. PMID:30012603
14. PMID:19307584
15. PMID:23962984
16. PMID:12839983
17. PMID:24569999
18. PMID:38156779
19. PMID:25583975
20. PMID:29339384
21. PMID:25733621
22. PMID:38084954
23. PMID:29892271
24. PMID:30992347
25. PMID:33875545