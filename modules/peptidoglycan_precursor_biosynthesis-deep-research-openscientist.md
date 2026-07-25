---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T06:56:26.687715'
end_time: '2026-07-23T08:23:28.072645'
duration_seconds: 5221.39
template_file: templates/module_research.md.j2
template_variables:
  module_title: Peptidoglycan precursor biosynthesis and lipid II export
  module_summary: A reusable bacterial pathway that converts UDP-N-acetylglucosamine
    to UDP-MurNAc-pentapeptide, transfers that nucleotide precursor to the undecaprenyl
    carrier to form lipid I, glycosylates lipid I to form lipid II, and translocates
    lipid II across the cytoplasmic membrane. D-Ala-D-Ala synthesis is modeled as
    a convergent input to MurF. The module ends at lipid II export and does not include
    glycan polymerization, peptide cross-linking, carrier recycling, or cell-wall
    remodeling.
  module_outline: "- Peptidoglycan precursor biosynthesis and lipid II export\n  -\
    \ 1. enolpyruvyl transfer to UDP-GlcNAc\n  - MurA enolpyruvyl transfer\n    -\
    \ UDP-N-acetylglucosamine 1-carboxyvinyltransferase (molecular player: PSEPK canonical\
    \ MurA; activity or role: UDP-N-acetylglucosamine 1-carboxyvinyltransferase activity)\n\
    \  - 2. UDP-MurNAc formation\n  - MurB UDP-MurNAc formation\n    - UDP-N-acetylmuramate\
    \ dehydrogenase (molecular player: PSEPK canonical MurB; activity or role: UDP-N-acetylmuramate\
    \ dehydrogenase activity)\n  - 3. L-alanine addition\n  - MurC L-alanine ligation\n\
    \    - UDP-N-acetylmuramate-L-alanine ligase (molecular player: PSEPK canonical\
    \ MurC; activity or role: UDP-N-acetylmuramate-L-alanine ligase activity)\n  -\
    \ 4. D-glutamate addition\n  - MurD D-glutamate ligation\n    - UDP-N-acetylmuramoylalanine-D-glutamate\
    \ ligase (molecular player: PSEPK canonical MurD; activity or role: UDP-N-acetylmuramoylalanine-D-glutamate\
    \ ligase activity)\n  - 5. meso-diaminopimelate addition\n  - MurE meso-diaminopimelate\
    \ ligation\n    - MurE meso-diaminopimelate ligase (molecular player: PSEPK canonical\
    \ MurE; activity or role: UDP-N-acetylmuramoylalanyl-D-glutamate-2,6-diaminopimelate\
    \ ligase activity)\n  - 6. D-Ala-D-Ala synthesis\n  - D-Ala-D-Ala synthesis\n\
    \    - D-alanine-D-alanine ligase (molecular player: PSEPK DdlB exemplar; activity\
    \ or role: D-alanine-D-alanine ligase activity)\n  - 7. UDP-MurNAc-pentapeptide\
    \ formation\n  - MurF pentapeptide ligation\n    - UDP-MurNAc-tripeptide-D-Ala-D-Ala\
    \ ligase (molecular player: PSEPK canonical MurF; activity or role: UDP-N-acetylmuramoyl-tripeptide-D-alanyl-D-alanine\
    \ ligase activity)\n  - 8. lipid I formation\n  - MraY lipid I synthesis\n   \
    \ - Phospho-MurNAc-pentapeptide transferase (molecular player: PSEPK canonical\
    \ MraY; activity or role: phospho-N-acetylmuramoyl-pentapeptide-transferase activity)\n\
    \  - 9. lipid II formation\n  - MurG lipid II synthesis\n    - Lipid I N-acetylglucosaminyltransferase\
    \ (molecular player: PSEPK canonical MurG; activity or role: undecaprenyldiphospho-muramoylpentapeptide\
    \ beta-N-acetylglucosaminyltransferase activity)\n  - 10. lipid II translocation\n\
    \  - MurJ lipid II export\n    - Lipid-linked peptidoglycan transporter (molecular\
    \ player: PSEPK canonical MurJ; activity or role: lipid-linked peptidoglycan transporter\
    \ activity)"
  module_connections: '- MurA enolpyruvyl transfer feeds into MurB UDP-MurNAc formation:
    MurA produces the enolpyruvyl substrate reduced by MurB.

    - MurB UDP-MurNAc formation feeds into MurC L-alanine ligation: MurB produces
    UDP-MurNAc for MurC.

    - MurC L-alanine ligation feeds into MurD D-glutamate ligation: MurC produces
    the mono-amino-acid precursor for MurD.

    - MurD D-glutamate ligation feeds into MurE meso-diaminopimelate ligation: MurD
    produces the dipeptide precursor for MurE.

    - MurE meso-diaminopimelate ligation feeds into MurF pentapeptide ligation: MurE
    supplies UDP-MurNAc-tripeptide to MurF.

    - D-Ala-D-Ala synthesis feeds into MurF pentapeptide ligation: Ddl supplies the
    D-Ala-D-Ala substrate to MurF.

    - MurF pentapeptide ligation feeds into MraY lipid I synthesis: MurF produces
    UDP-MurNAc-pentapeptide for MraY.

    - MraY lipid I synthesis feeds into MurG lipid II synthesis: MraY produces lipid
    I for MurG.

    - MurG lipid II synthesis feeds into MurJ lipid II export: MurG produces lipid
    II for MurJ-mediated export.'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: peptidoglycan_precursor_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: peptidoglycan_precursor_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Peptidoglycan precursor biosynthesis and lipid II export

## Working Scope

A reusable bacterial pathway that converts UDP-N-acetylglucosamine to UDP-MurNAc-pentapeptide, transfers that nucleotide precursor to the undecaprenyl carrier to form lipid I, glycosylates lipid I to form lipid II, and translocates lipid II across the cytoplasmic membrane. D-Ala-D-Ala synthesis is modeled as a convergent input to MurF. The module ends at lipid II export and does not include glycan polymerization, peptide cross-linking, carrier recycling, or cell-wall remodeling.

## Provisional Biological Outline

- Peptidoglycan precursor biosynthesis and lipid II export
  - 1. enolpyruvyl transfer to UDP-GlcNAc
  - MurA enolpyruvyl transfer
    - UDP-N-acetylglucosamine 1-carboxyvinyltransferase (molecular player: PSEPK canonical MurA; activity or role: UDP-N-acetylglucosamine 1-carboxyvinyltransferase activity)
  - 2. UDP-MurNAc formation
  - MurB UDP-MurNAc formation
    - UDP-N-acetylmuramate dehydrogenase (molecular player: PSEPK canonical MurB; activity or role: UDP-N-acetylmuramate dehydrogenase activity)
  - 3. L-alanine addition
  - MurC L-alanine ligation
    - UDP-N-acetylmuramate-L-alanine ligase (molecular player: PSEPK canonical MurC; activity or role: UDP-N-acetylmuramate-L-alanine ligase activity)
  - 4. D-glutamate addition
  - MurD D-glutamate ligation
    - UDP-N-acetylmuramoylalanine-D-glutamate ligase (molecular player: PSEPK canonical MurD; activity or role: UDP-N-acetylmuramoylalanine-D-glutamate ligase activity)
  - 5. meso-diaminopimelate addition
  - MurE meso-diaminopimelate ligation
    - MurE meso-diaminopimelate ligase (molecular player: PSEPK canonical MurE; activity or role: UDP-N-acetylmuramoylalanyl-D-glutamate-2,6-diaminopimelate ligase activity)
  - 6. D-Ala-D-Ala synthesis
  - D-Ala-D-Ala synthesis
    - D-alanine-D-alanine ligase (molecular player: PSEPK DdlB exemplar; activity or role: D-alanine-D-alanine ligase activity)
  - 7. UDP-MurNAc-pentapeptide formation
  - MurF pentapeptide ligation
    - UDP-MurNAc-tripeptide-D-Ala-D-Ala ligase (molecular player: PSEPK canonical MurF; activity or role: UDP-N-acetylmuramoyl-tripeptide-D-alanyl-D-alanine ligase activity)
  - 8. lipid I formation
  - MraY lipid I synthesis
    - Phospho-MurNAc-pentapeptide transferase (molecular player: PSEPK canonical MraY; activity or role: phospho-N-acetylmuramoyl-pentapeptide-transferase activity)
  - 9. lipid II formation
  - MurG lipid II synthesis
    - Lipid I N-acetylglucosaminyltransferase (molecular player: PSEPK canonical MurG; activity or role: undecaprenyldiphospho-muramoylpentapeptide beta-N-acetylglucosaminyltransferase activity)
  - 10. lipid II translocation
  - MurJ lipid II export
    - Lipid-linked peptidoglycan transporter (molecular player: PSEPK canonical MurJ; activity or role: lipid-linked peptidoglycan transporter activity)

## Known Relationships Among Steps

- MurA enolpyruvyl transfer feeds into MurB UDP-MurNAc formation: MurA produces the enolpyruvyl substrate reduced by MurB.
- MurB UDP-MurNAc formation feeds into MurC L-alanine ligation: MurB produces UDP-MurNAc for MurC.
- MurC L-alanine ligation feeds into MurD D-glutamate ligation: MurC produces the mono-amino-acid precursor for MurD.
- MurD D-glutamate ligation feeds into MurE meso-diaminopimelate ligation: MurD produces the dipeptide precursor for MurE.
- MurE meso-diaminopimelate ligation feeds into MurF pentapeptide ligation: MurE supplies UDP-MurNAc-tripeptide to MurF.
- D-Ala-D-Ala synthesis feeds into MurF pentapeptide ligation: Ddl supplies the D-Ala-D-Ala substrate to MurF.
- MurF pentapeptide ligation feeds into MraY lipid I synthesis: MurF produces UDP-MurNAc-pentapeptide for MraY.
- MraY lipid I synthesis feeds into MurG lipid II synthesis: MraY produces lipid I for MurG.
- MurG lipid II synthesis feeds into MurJ lipid II export: MurG produces lipid II for MurJ-mediated export.

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

# Peptidoglycan Precursor Biosynthesis and Lipid II Export: A Mechanistic Review

*A commissioned review-style synthesis. Scope: the reusable bacterial module that
converts UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-MurNAc-pentapeptide, transfers
it to the undecaprenyl carrier to make lipid I, glycosylates lipid I to lipid II, and
flips lipid II across the cytoplasmic membrane. The module ends at lipid II export and
excludes glycan polymerization, cross-linking, carrier recycling, and wall remodeling.*

---

## 1. Executive Summary

Peptidoglycan (PG) precursor biosynthesis is a linear, largely universal bacterial
assembly line that builds the membrane-anchored disaccharide-pentapeptide monomer,
**lipid II**, and delivers it to the outer face of the cytoplasmic membrane for
polymerization. The pathway partitions cleanly into three physical regimes: (i) a
**soluble cytoplasmic phase** in which six enzymes (the enolpyruvyl transferase MurA, the
flavin-dependent reductase MurB, and the four ATP-dependent amide ligases MurC–MurF),
together with a convergent D-Ala–D-Ala branch (Ddl), elaborate the nucleotide-sugar
UDP-MurNAc-pentapeptide; (ii) a **membrane-embedded
biosynthetic phase** in which MraY transfers the phospho-MurNAc-pentapeptide unit to the
polyprenyl carrier undecaprenyl phosphate (C55-P) to form lipid I, and MurG adds GlcNAc to
form lipid II; and (iii) a **translocation phase** in which the flippase MurJ moves lipid
II to the periplasmic leaflet.

The cytoplasmic chemistry is mechanistically well understood and enzymologically
conserved; its enzymes have no eukaryotic counterparts and are validated or aspirational
antibiotic targets (fosfomycin→MurA; D-cycloserine→Ddl/Alr; nucleoside natural products
such as muraymycins/tunicamycin→MraY). The membrane and translocation steps are more
contested. The identity of the lipid II flippase was, for over a decade, one of the most
disputed questions in bacterial cell biology, with **FtsW, MurJ, and AmJ** all proposed
before genetic and biochemical trapping experiments established **MurJ (a MOP-superfamily
transporter)** as the primary flippase acting by an alternating-access cycle (PMIDs
26792999, 30482840, 35660157, 32129990) — though not the universal sole translocase, since
*B. subtilis* carries an unrelated, stress-inducible backup flippase, Amj (PMID 25918422).
A recurring theme is that much "lipid II"
biology is inferred from a handful of model organisms (chiefly *E. coli*, *B. subtilis*,
*S. aureus*, *M. tuberculosis*) and should not be over-generalized.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The module is the **"Mur pathway plus the two lipid transferases plus the flippase"**:

| Step | Enzyme (PSEPK canonical) | Reaction | Compartment |
|------|--------------------------|----------|-------------|
| 1 | **MurA** | UDP-GlcNAc + PEP → enolpyruvyl-UDP-GlcNAc | cytoplasm |
| 2 | **MurB** | (NADPH-dependent reduction) → UDP-MurNAc | cytoplasm |
| 3 | **MurC** | + L-Ala → UDP-MurNAc-L-Ala | cytoplasm |
| 4 | **MurD** | + D-Glu → UDP-MurNAc-L-Ala-D-Glu | cytoplasm |
| 5 | **MurE** | + *meso*-DAP (or L-Lys) → UDP-MurNAc-tripeptide | cytoplasm |
| (conv.) | **Ddl** (DdlB exemplar) | 2 D-Ala → D-Ala-D-Ala | cytoplasm |
| 7 | **MurF** | + D-Ala-D-Ala → UDP-MurNAc-**pentapeptide** | cytoplasm |
| 8 | **MraY** | + C55-P → **lipid I** (+ UMP release) | inner leaflet |
| 9 | **MurG** | + UDP-GlcNAc → **lipid II** | inner leaflet |
| 10 | **MurJ** | flip lipid II → outer leaflet | transmembrane |

The pathway is **reusable**: the same lipid II is consumed by both the elongation
(elongasome) and division (divisome) machineries. It is a metabolic converging funnel —
all downstream wall growth depends on flux through this single set of enzymes.

### 2.2 Neighboring processes often conflated but excluded here

- **Glycan polymerization / transglycosylation** (aPBPs and SEDS proteins RodA/FtsW) —
  begins *after* export. Notably, the discovery that **RodA and FtsW are themselves PG
  glycosyltransferases** (SEDS family) reorganized the downstream field (PMID 35274942);
  this is downstream of our boundary but historically entangled with the flippase debate
  because FtsW was itself a flippase candidate.
- **Transpeptidation / cross-linking** (DD- and LD-transpeptidases, PBPs) — extracytoplasmic.
- **Undecaprenyl-phosphate recycling** (UppP/BacA, UppS synthesis; C55-PP dephosphorylation
  after transglycosylation) — the carrier-regeneration loop that *feeds* MraY but is not part
  of monomer assembly.
- **UDP-GlcNAc supply** (GlmS/GlmM/GlmU) — the shared amino-sugar node feeding both PG and
  LPS/teichoic acid; it is the *substrate source*, upstream of MurA.
- **Stem-peptide tailoring** (e.g., MurT/GatD amidation of D-Glu to D-iso-Gln in
  *S. aureus*/mycobacteria; FemABX branch-peptide addition; DAP amidation) — lineage-specific
  decorations layered onto the core precursor.
- **Cell-wall remodeling / autolysins / recycling (Amp, Mpl)** — turnover, not synthesis.

### 2.3 Competing definitions

Some reviews draw the cytoplasmic boundary at MurF (the "Mur pathway" *sensu stricto*),
treating MraY/MurG/MurJ as a separate "membrane cycle." Others fold MurJ into the
polymerization machinery because it is functionally coupled to the divisome/elongasome.
The brief's boundary (through lipid II export) is defensible and increasingly standard: it
captures a self-contained "make and deliver the monomer" unit and stops before the
combinatorial complexity of wall growth.

---

## 3. Mechanistic Overview

**Best current model of the sequence of events.** The pathway is an obligate linear
cascade with one convergent input:

```
UDP-GlcNAc ─MurA→ EP-UDP-GlcNAc ─MurB→ UDP-MurNAc ─MurC→ ─MurD→ ─MurE→ UDP-MurNAc-tripeptide
                                                                              │
                              2 D-Ala ─Ddl→ D-Ala-D-Ala ─────────────────────┤ (MurF)
                                                                              ▼
                                              UDP-MurNAc-pentapeptide ─MraY→ Lipid I
                                              ─MurG→ Lipid II ─MurJ→ Lipid II (periplasmic)
```

**Obligatory steps.** MurA→MurB→MurC→MurD→MurE→MurF→MraY→MurG→MurJ are each individually
essential in the canonical model organisms; there is no bypass within a single cell for the
core reactions. Substrate ordering is strict because each ligase recognizes the product of
the previous one (see §6).

**Conditional / variant steps.** The *identity of the amino acid at position 3* (MurE
substrate: *meso*-DAP in most Gram-negatives and bacilli/mycobacteria vs L-Lys in many
Gram-positive cocci) is lineage-dependent. The *terminal dipeptide* is usually D-Ala-D-Ala
but is remodeled to D-Ala-D-Lac or D-Ala-D-Ser in glycopeptide-resistant organisms (Van
ligases). The **MurB redox chemistry** uses FAD/NADPH but the mechanism differs between
class I (flavin) enzymes across taxa.

**Accessory / tailoring reactions** (outside strict boundary but mechanistically coupled):
amidation of D-Glu (MurT/GatD) and of *meso*-DAP; interpeptide bridge attachment
(FemABX) occurs on lipid II in *S. aureus*, i.e., *after* MurG but *before* export — an
important caveat that some tailoring happens on the carrier-lipid intermediate.

**Chemical logic.** The cascade alternates chemistries: an enolpyruvyl transfer (MurA,
addition–elimination via a covalent PEP intermediate, inhibited by fosfomycin), a flavin
reduction (MurB), four **ATP-dependent amide ligations** sharing the Mur-ligase fold
(each proceeds through an acyl-phosphate intermediate: carboxyl activation by ATP → ADP,
then nucleophilic attack by the incoming amine), a **prenyl-phosphate transfer** (MraY,
Mg2+-dependent, releasing UMP), a **glycosyl transfer** (MurG, retaining GT-B fold), and
finally an **ATP-independent, conformationally driven lipid flip** (MurJ).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 Cytoplasmic phase

- **MurA (UDP-GlcNAc enolpyruvyl transferase).** Transfers the enolpyruvyl group of PEP to
  the 3′-OH of UDP-GlcNAc. Two-domain enzyme with a large inter-domain loop closure; Cys115
  (E. coli numbering) forms the covalent adduct targeted by the epoxide antibiotic
  **fosfomycin** (PMID 8994972). Notably, structural/kinetic analysis of the C115S mutant
  showed Cys115 is essential for **product release rather than the enolpyruvyl-transfer
  chemistry itself**, correcting an earlier assumption; consistently, **Cys115→Asp**
  substitutions confer intrinsic fosfomycin resistance in *Mycobacterium* and *Chlamydia*
  (PMID 15531591). Numerous covalent-warhead inhibitors beyond fosfomycin have since been
  designed against Cys115 (PMID 35936791). MurA is the committed first step and a flux-
  control point. Mechanistically and structurally it is one of only two known enolpyruvyl
  transferases, the other being **EPSP synthase** of the shikimate pathway (fosfomycin/
  glyphosate parallel) — a deep evolutionary kinship discussed in §5 (PMID 8994972).
- **MurB (UDP-MurNAc dehydrogenase).** FAD-dependent, NADPH-driven reduction of the
  enolpyruvyl to D-lactyl, yielding UDP-MurNAc. Completes formation of the muramic-acid
  scaffold.
- **MurC/D/E/F (ATP-dependent Mur ligases).** A structurally and mechanistically related
  family (three-domain fold, central ATP-binding Rossmann-like domain) adding L-Ala, D-Glu,
  *meso*-DAP/L-Lys, and D-Ala-D-Ala respectively. All require divalent cations and share the
  acyl-phosphate mechanism (PMID 23555903). They are enzymologically tractable as a
  reconstituted "one-pot" cascade (PMID 27734910), and are inhibited by rationally designed
  and natural-product inhibitors (e.g., MurD D-Glu-mimetics, PMID 21703731). In some taxa
  (mycobacteria, corynebacteria) the ligases are regulated by **Ser/Thr protein-kinase
  phosphorylation** (PknA/PknB), linking wall synthesis to signaling (PMID 23555903).
- **Ddl (D-Ala-D-Ala ligase) + Alr (alanine racemase).** ATP-dependent condensation of two
  D-Ala into the terminal dipeptide, a convergent input to MurF. **D-cycloserine** inhibits
  both Alr and Ddl. Ddl specificity is exquisitely tunable: a single active-site residue
  (Phe vs Tyr) switches output between the depsipeptide D-Ala-D-Lac and the dipeptide
  D-Ala-D-Ala (PMID 29686137), the molecular basis of **VanA-type vancomycin resistance**
  (PMID 10529248) and observed natively in glycopeptide-producing actinomycetes (PMID 9435111).

### 4.2 Membrane biosynthetic phase

- **MraY (phospho-MurNAc-pentapeptide transferase).** Polytopic integral membrane enzyme of
  the polyprenyl-phosphate transferase (PNPT) superfamily. Transfers the phospho-
  MurNAc-pentapeptide moiety onto C55-P, releasing UMP and forming lipid I. Crystal
  structures (e.g., *Aquifex aeolicus* MraY, alone and with the natural inhibitor muraymycin
  D2) show a cytoplasmic active site with essential acidic residues and a Mg2+ cofactor, and
  large ligand-induced conformational changes (PMID 27088606). Kinetics support ternary-
  complex catalysis with a conserved catalytic histidine (PMID 27226570). MraY is the target
  of several nucleoside natural-product antibiotic classes (muraymycins, tunicamycin,
  liposidomycins/caprazamycins) (PMIDs 29386462, 33607457).
- **MurG (UDP-GlcNAc:lipid I β-1,4-N-acetylglucosaminyltransferase).** Membrane-associated
  GT-B–fold glycosyltransferase that adds GlcNAc to lipid I to complete lipid II. It follows
  a **compulsory ordered Bi Bi mechanism** (donor UDP-GlcNAc binds first) and, revealingly,
  does *not* require the full C55 chain for catalysis in vitro — the carrier lipid is
  important for pathway context, not for the chemistry (PMID 12022887). Higher-order
  oligomeric/functional-unit organization has been proposed from crystallographic work
  (PMID 34258006).

### 4.3 Translocation phase

- **MurJ (lipid II flippase).** A **MOP (Multidrug/Oligosaccharidyl-lipid/Polysaccharide)
  superfamily** transporter with an inner amphipathic cavity. Multiple crystal structures
  capture **inward-facing, outward-facing, and "squeezed"** conformations, and MD plus
  in-cell cross-linking support an **alternating-access** cycle in which conserved cavity
  residues (e.g., Arg residues; A29, D269) bind the lipid II head group and drive the
  conformational transition (PMIDs 30482840, 35660157, 32129990, 29461535). Substrate
  recognition appears **coupled to conformational opening** — engineered MOP paralogs (WzxC)
  can be rewired to flip PG precursors, arguing that specificity is encoded in which
  substrate destabilizes the inward-open state (PMID 29907971). Endogenous lipids
  (cardiolipin) and antibiotics (ramoplanin, vancomycin) modulate lipid II occupancy of MurJ
  (PMID 29461535).

### 4.4 Higher-order organization

The cytoplasmic enzymes are encoded largely within the conserved **dcw (division and cell
wall) gene cluster** and co-transcribed with division genes (ftsQ/ftsW), physically and
transcriptionally linking precursor supply to the cell cycle (PMID 23555903). Protein–protein
interaction and structural studies suggest the Mur enzymes and their membrane partners are
spatially organized rather than freely diffusing, plausibly channeling intermediates toward
the divisome/elongasome (PMID 27136593).

---

## 5. Evolutionary and Cell-Biological Variation

**Deep conservation.** The Mur pathway is one of the most broadly conserved biosynthetic
routes in the Bacteria; the cytoplasmic ligases share a common fold consistent with ancestral
gene duplication and functional divergence (a canonical example of paralog expansion:
MurC/D/E/F are best understood as descendants of a single ATP-dependent amide-ligase
ancestor, with **MurC/MurD the most tractable representatives of the ancestral single-amino-
acid-adding activity**). The entry step reaches even deeper: **MurA is one of only two known
enolpyruvyl transferases**, sharing a two-domain architecture and PEP chemistry with
**EPSP synthase** of the aromatic-amino-acid (shikimate) pathway — both enzymes are found
essentially only in plants and microbes and absent from animals, and both are exploited
agrochemically/therapeutically (fosfomycin vs glyphosate) (PMID 8994972). This roots the
pathway's first committed step in an ancient PEP-utilizing enzyme family predating the
peptidoglycan-specific role. The undecaprenyl-phosphate carrier logic (nucleotide-sugar →
lipid-linked oligosaccharide → flip → polymerize) is shared with **eukaryotic N-glycosylation
and O-antigen/capsule biogenesis** — a deep, convergent or homologous "lipid-carrier"
strategy for building glycoconjugates across a membrane (PMID 26792999). MraY likewise
belongs to a broadly distributed polyprenyl-phosphate transferase superfamily (with WecA and
eukaryotic GPT relatives), indicating the membrane-transfer chemistry is itself ancient.

**Lineage variation.**
- *Position-3 residue:* *meso*-DAP (Gram-negatives, bacilli, mycobacteria/actinobacteria) vs
  L-Lys (many Gram-positive cocci, e.g., *S. aureus*, streptococci) — a MurE substrate-
  specificity difference (PMID 18194336).
- *Stem-peptide tailoring:* amidation of D-Glu (MurT/GatD) and of DAP; interpeptide bridges
  (e.g., pentaglycine via FemABX in *S. aureus*) — added on the UDP or lipid-linked precursor
  and highly lineage-specific (PMID 18194336).
- *Terminal dipeptide plasticity:* D-Ala-D-Ala → D-Ala-D-Lac/D-Ala-D-Ser in glycopeptide-
  resistant enterococci/staphylococci and glycopeptide producers (PMIDs 10529248, 9435111).
- *MraY/MurG homologs:* MraY belongs to a superfamily including WecA (which primes O-antigen
  with GlcNAc-1-P) and WbpL/GPT — the transferase step is ancient and paralogously expanded;
  the **PG-specific MraY** is the best representative for the ancestral peptidoglycan role.

**Cell-biological / physiological state variation.** The *same* lipid II pool supplies
**elongation** (MreB-guided elongasome) and **division** (FtsZ-guided divisome). Flux and
localization of MurG and MurJ are spatially patterned with the cell cycle; MurJ activity at
the division site is regulated within the divisome. Sporulating and dormant states (spores,
*M. tuberculosis* persistence), L-forms (transient wall-less states), and endosymbionts with
reduced genomes (e.g., *Arsenophonus*, from which a MurJ structure was solved, PMID 35660157)
represent physiological/compartmental variants — with **cell-wall-less lineages (Mollicutes,
*Chlamydia*'s reduced wall, most Archaea) representing lineage-specific loss or replacement**
(archaea use pseudomurein or other envelopes and lack the canonical Mur pathway).

**Alternative routes to the same outcome.** Beyond the Van ligase depsipeptide bypass, the
key example within our boundary is the flippase question itself: **different organisms and
assays implicated different proteins (FtsW/Amj/MurJ)** for the same translocation outcome.
The most striking demonstration is that *B. subtilis* cells lacking **all ten MOP-superfamily
members (including MurJ)** remain viable, because they encode an unrelated backup flippase,
**Amj (alternate to MurJ; *ydaH*)**, that is synthetic-lethal with MurJ and, like MurJ, can
support lipid II flipping and viability when expressed in *E. coli* lacking its own MurJ
(PMID 25918422). Amj is induced by the envelope-stress σ^M regulon, so loss or inhibition of
MurJ can trigger a compensatory translocase. MOP paralogs can also be *engineered* to
substitute (PMID 29907971). Together these show the transport function is **not uniquely tied
to one protein family across all lineages** — an important caveat for MurJ-targeted drugs and
for extrapolating *E. coli* flippase biology to all bacteria.

---

## 6. Constraints, Dependencies, and Failure Modes

**Mandatory ordering (why it cannot be reshuffled).**
- Each Mur ligase is a **product-templated recognition** enzyme: MurD requires the MurC
  product, MurE the MurD product, MurF the MurE product. The stepwise amide bonds cannot be
  formed out of order because the enzyme active sites read the growing UDP-MurNAc-peptide.
- **MraY must follow MurF:** it transfers a *pentapeptide*-bearing phospho-MurNAc; the
  nucleotide precursor must be complete first. (Some tailoring, e.g., FemABX bridges, is the
  exception — it occurs on lipid I/II after MraY.)
- **MurG must follow MraY:** MurG glycosylates lipid I, not the soluble precursor, and binds
  donor sugar first (ordered Bi Bi) (PMID 12022887).
- **MurJ must follow MurG:** only the complete disaccharide-pentapeptide (lipid II) is the
  physiological flippase substrate.

**Compartment / topology constraints.**
- Lipid I and lipid II are **synthesized on the inner (cytoplasmic) leaflet**; polymerization
  occurs on the **outer leaflet** — hence an obligatory flip (PMID 26792999). This
  topological inversion is the raison d'être of MurJ and the reason the flippase step is
  non-negotiable.
- The **carrier lipid is limiting.** C55-P is present in low copy and shared with LPS,
  teichoic acid, and capsule pathways; sequestration of lipid II (e.g., by nisin,
  vancomycin, ramoplanin, or a stalled flippase) is lethal because it **starves the recycling
  pool**, a major failure mode exploited by antibiotics.

**Mutually exclusive / substrate-specific events.**
- Ddl's D-Ala-D-Ala vs D-Ala-D-Lac outputs are mutually exclusive per enzyme variant and
  determine vancomycin susceptibility (PMIDs 29686137, 10529248).
- MurE's DAP vs Lys specificity is fixed per organism.

**Evidence ruling out otherwise plausible paths.**
- In-cell cross-linking trapped lipid II *on* MurJ and showed Arg mutants bind but fail to
  transport — ruling out a purely passive/spontaneous flip and supporting an active,
  residue-dependent conformational cycle (PMID 32129990).
- The "squeezed" MurJ conformation (cavity collapsed) argues against a static open channel and
  for alternating access (PMID 35660157).
- MurG's indifference to the full C55 chain in vitro rules out the hypothesis that the long
  isoprenoid is chemically required for glycosyl transfer (PMID 12022887).

**Failure modes / therapeutic vulnerabilities.** Fosfomycin (MraA... MurA), D-cycloserine
(Alr/Ddl), tunicamycin/muraymycins/caprazamycins (MraY), and lipid-II–sequestering
glycopeptides/lantibiotics (vancomycin, nisin, ramoplanin) all act within or immediately at
the boundary of this module; MurB, the Mur ligases, and MurJ are actively pursued but
lack clinically approved inhibitors — a standing opportunity given their essentiality and
absence of human homologs (PMIDs 27734910, 27136593).

---

## 7. Controversies and Open Questions

1. **Flippase identity and mechanism.** Although MurJ is now accepted as the primary lipid II
   flippase, the historical FtsW/MurJ/AmJ dispute (PMID 26792999) reflected genuinely
   conflicting evidence: purified **FtsW was shown biochemically to induce transbilayer
   movement of lipid II** in model membranes and E. coli vesicles (PMID 21386816), whereas
   **MurJ** carried the essential in-vivo flippase phenotype and the conformational-trapping
   data (PMIDs 30482840, 32129990). This is a textbook in-vitro-vs-in-vivo discordance rather
   than a fully reconciled model. Compounding this, MurJ is **not the universal sole flippase**:
   *B. subtilis* uses the unrelated, stress-inducible **Amj** as a redundant translocase
   (PMID 25918422), so the "flippase" is lineage-dependent rather than a single conserved
   protein. Open: Does **FtsW retain any flippase-like or "hand-off" role** now that it is
   established as a SEDS glycosyltransferase (PMID 35274942)? How many bacteria carry Amj-like
   backups, and are they induced clinically when MurJ is inhibited? How is MurJ energized — is
   the conformational cycle coupled to the membrane potential/ion gradients, and if so, which
   ion?
2. **Where does the flip physically hand off to polymerization?** The spatial/temporal
   coupling of MurJ to RodA/FtsW-PBP complexes at the divisome/elongasome is not resolved at
   the structural level (PMID 27136593).
3. **Metabolic channeling vs free diffusion.** Whether Mur enzymes form a bona fide
   multienzyme complex that channels intermediates, or simply co-localize via the dcw operon
   and membrane recruitment, remains debated (PMID 23555903, 27136593).
4. **Regulation.** Ser/Thr-kinase phosphorylation of Mur ligases is documented in
   actinobacteria (PMID 23555903), but the systemic logic coupling precursor flux to growth
   rate, nutrient status, and the cell cycle is incompletely mapped, and may not generalize
   across phyla.
5. **Organism-comparability caveat.** Much mechanism is stitched together from *E. coli*
   (MurJ genetics), *Aquifex*/*Bacillus* (MraY structure/kinetics), *S. aureus* (tailoring),
   and *M. tuberculosis* (ligase regulation). Cross-organism extrapolation is a standing
   source of over-generalization; claims should be qualified by the source system.
6. **Structural gaps.** High-resolution structures of MraY and MurG *with intact lipid-linked
   substrates*, and of MurJ *caught mid-flip with lipid II*, remain incomplete — the central
   barrier to a fully atomistic model of the membrane phase.

---

## 8. Key References

- Ruiz N. *Lipid Flippases for Bacterial Peptidoglycan Biosynthesis.* Lipid Insights / review, 2015. **PMID 26792999.** (Flippase controversy: FtsW, MurJ, AmJ; carrier-lipid strategy.)
- Kumar S, Rubino FA, Mendoza AG, Ruiz N. *The bacterial lipid II flippase MurJ functions by an alternating-access mechanism.* J Biol Chem, 2019. **PMID 30482840.**
- Kohga H, et al. *Crystal structure of the lipid flippase MurJ in a "squeezed" form...* Structure, 2022. **PMID 35660157.**
- Rubino FA, et al. *Detection of Transport Intermediates in the Peptidoglycan Flippase MurJ...* J Am Chem Soc, 2020. **PMID 32129990.**
- Sham LT, et al. *Loss of specificity variants of WzxC... MOP-family flippases.* Mol Microbiol, 2018. **PMID 29907971.**
- Bolla JR, et al. *Direct observation of the influence of cardiolipin and antibiotics on lipid II binding to MurJ.* Nat Chem, 2018. **PMID 29461535.**
- Kumar S, Mollo A, Kahne D, Ruiz N. *The Bacterial Cell Wall: From Lipid II Flipping to Polymerization.* Chem Rev, 2022. **PMID 35274942.** (SEDS RodA/FtsW polymerases; MurJ.)
- Chung BC, et al. *Structural insights into inhibition of lipid I production... (MraY–muraymycin D2).* Nature, 2016. **PMID 27088606.**
- Liu Y, et al. *New Insight into the Catalytic Mechanism of Bacterial MraY...* Biochemistry, 2016. **PMID 27226570.**
- van Heijenoort J. *Lipid intermediates in the biosynthesis of bacterial peptidoglycan.* Microbiol Mol Biol Rev, 2007. **PMID 18063720.**
- Chen L, et al. (Walker lab). *Intrinsic lipid preferences and kinetic mechanism of E. coli MurG.* Biochemistry, 2002. **PMID 12022887.** (Ordered Bi Bi.)
- Jung Y, et al. *Putative hexameric glycosyltransferase functional unit... (MurG crystal structure).* 2021. **PMID 34258006.**
- Munshi T, et al. *Characterisation of ATP-dependent Mur ligases... M. tuberculosis.* PLoS One, 2013. **PMID 23555903.** (dcw operon; divalent-cation requirement; PknA/B regulation.)
- Laddomada F, Miyachiro MM, Dessen A. *Structural Insights into Protein–Protein Interactions... cell wall biogenesis.* Int J Mol Sci, 2016. **PMID 27136593.**
- Eniyan K, et al. *One-pot assay... Mur pathway inhibitors in M. tuberculosis.* Sci Rep, 2016. **PMID 27734910.** (Reconstituted MurA–MurF cascade; D-cycloserine.)
- Tomašič T, et al. *Novel... inhibitors of bacterial MurD ligase...* Bioorg Med Chem, 2011. **PMID 21703731.**
- Lessard IAD, Walsh CT. *Determinants for differential effects on D-Ala-D-lactate vs D-Ala-D-Ala formation by VanA...* 1999. **PMID 10529248.**
- Zhang S, et al. *d-Alanyl-d-Alanine Ligase as a... counterselection marker in vancomycin-resistant lactic acid bacteria.* 2018. **PMID 29686137.** (Single Phe/Tyr residue determines depsi- vs dipeptide.)
- Marshall CG, Wright GD. *The glycopeptide antibiotic producer S. toyocaensis has both D-Ala-D-Ala and D-Ala-D-Lac ligases.* 1997. **PMID 9435111.**
- Vollmer W, Blanot D, de Pedro MA. *Peptidoglycan structure and architecture.* FEMS Microbiol Rev, 2008. **PMID 18194336.** (Compositional diversity; DAP vs Lys; tailoring.)
- Katsuyama A, Ichikawa S. *Synthesis and Medicinal Chemistry of Muraymycins, Nucleoside Antibiotics (MraY inhibitors).* 2018. **PMID 29386462.**
- Mohammadi T, et al. *Identification of FtsW as a transporter of lipid-linked cell wall precursors across the membrane.* EMBO J, 2011. **PMID 21386816.** (Biochemical FtsW flippase evidence.)
- Meeske AJ, et al. *MurJ and a novel lipid II flippase are required for cell wall biogenesis in Bacillus subtilis.* PNAS, 2015. **PMID 25918422.** (Amj as an alternate, stress-inducible flippase; MOP redundancy.)
- Skarzynski T, et al. *Structure of UDP-N-acetylglucosamine enolpyruvyl transferase (MurA) complexed with UDP-GlcNAc and fosfomycin.* Structure, 1996. **PMID 8994972.** (MurA structure; EPSP-synthase homology.)
- Eschenburg S, Priestman M, Schönbrunn E. *Evidence that the fosfomycin target Cys115 in MurA is essential for product release.* J Biol Chem, 2005. **PMID 15531591.** (Cys115 role; Cys→Asp fosfomycin resistance.)
- de Oliveira RG, et al. *Advances in UDP-N-Acetylglucosamine Enolpyruvyl Transferase (MurA) Covalent Inhibition.* 2022. **PMID 35936791.**

*Search date: 2026-07-23 (PubMed). This review synthesizes primary literature and authoritative
reviews; it is explanatory rather than encyclopedic and flags organism-comparability limits
throughout.*


## Artifacts

- [OpenScientist final report](peptidoglycan_precursor_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](peptidoglycan_precursor_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)