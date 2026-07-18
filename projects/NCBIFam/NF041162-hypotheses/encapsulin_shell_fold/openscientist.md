---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T19:37:33.080884'
end_time: '2026-07-18T19:50:22.278965'
duration_seconds: 769.2
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Hypothesis: what is this generically-named bacterial "membrane protein"?

You are an independent computational biologist. A bacterial protein is annotated
in UniProt only as a generic "Membrane protein". Determine what it actually is —
its fold, the higher-order assembly it forms, and its subcellular localization.

## What is known (do not assume beyond this)

- NCBI Protein Family **NF041162** (NCBIFAM/PGAP), an *equivalog*, ~314 aa members
  across diverse bacteria.
- This representative, UniProt **A0A0D5NHT9** (*Paenibacillus beijingensis*,
  314 aa), is UniProt-named only "**Membrane protein**" — an uninformative
  placeholder.

## Representative sequence

UniProt **A0A0D5NHT9**, 314 aa:

```
MAEQENSVKTLGSSAAYQLANVTKTAPVFEAVTPRFLTRLFEWKGLETGIFRLNKVNEGETTLDILCSQSDDVNITEGFVDCSSKPREYTLNAISTVVNVHTHISDLYSSPYDQVKEQLRLSIESIKERQESQLINSDDYGLLKNAAESQRIQTRFGPPTPDDLDELISKVWKEPSFFLAHPRAIAAFGRECTRRGVPPQTVQLFGAHFLTWRGIPIIPTDKLFVDGQKSPKGKGGKTNILLVRTGEQKQGVVGLYQAGVPGEQSKGLSVRFMGLDKNGIGSYLLSLYCSVAILADDAVAVLEDVDVGNYYDYQ
```

## The decisive question (scope your work to this)

**What is the fold and higher-order assembly of this protein, and where does it
localize?** Answer by:
1. Foldseek fold assignment of the AlphaFold model — what is the closest
   experimentally characterized structural homolog, and does the fold correspond
   to a **self-assembling proteinaceous shell/capsid** (e.g. an HK97 phage-capsid
   fold) rather than an integral-membrane protein?
2. State the **higher-order assembly** implied (monomer? icosahedral shell/
   nanocompartment?) and the correct **subcellular localization / cellular
   component**.
3. Give the most specific identity and cellular-component assignment you can, and
   say whether "**membrane protein**" is correct or a mis-annotation.

Keep other analyses light. Give one clear conclusion with confidence and the one
experiment that would confirm it.

## Output

# What is this generically-named bacterial "membrane protein"? — Final Report

## Summary

The protein annotated in UniProt as nothing more than a generic "**Membrane protein**" — **A0A0D5NHT9** from *Paenibacillus beijingensis* (314 aa), the representative of NCBI Protein Family **NF041162** — is **not a membrane protein at all**. It is a **Family 2A encapsulin nanocompartment shell protein** that adopts the **HK97 bacteriophage major-capsid-protein fold**. The "membrane protein" label is a **mis-annotation** that originates solely from an unreviewed, automated EMBL submission (accession AJY74493.1) and has no supporting structural or biochemical basis.

Three independent, converging lines of evidence establish this identity. First, the curated database signatures cross-referenced to this UniProt entry are unambiguous: NCBIfam **NF041162** carries the short-name "**encap_f2a**"; InterPro **IPR049822** is literally titled "**Encapsulin nanocompartment shell protein 2A**"; InterPro **IPR045641** is "Type 2A encapsulin shell protein SrpI-like"; and Pfam **PF19307** is the SrpI-like family. InterPro's own description states these proteins "share the HK97 fold of the capsid proteins" of *Caudovirales* bacteriophages. Second, the AlphaFold model (AF-A0A0D5NHT9-F1) is a high-confidence (global pLDDT 89.9) elongated α+β single domain with a large β-sheet and a long ~22-residue "spine" helix and — critically — **no transmembrane helix bundle**, exactly matching the HK97 capsid-subunit architecture and ruling out an integral membrane protein. Third, independent hydropathy analysis of the raw sequence shows a hydrophilic, negatively charged, soluble composition (net charge −6; maximum Kyte–Doolittle hydropathy of only 1.89, well below the ~2.5 threshold for a genuine transmembrane segment).

The correct higher-order assembly is a **self-assembling icosahedral protein shell** of ~60 or more identical subunits (a ~25–42 nm nanocompartment) that internally sequesters enzyme cargo. The correct subcellular localization / cellular component is the **Gene Ontology term GO:0140737 "encapsulin nanocompartment"** — an **intracellular, non-membrane-bound proteinaceous organelle** residing in the **cytoplasm**, explicitly *not* the plasma/inner membrane. The single most decisive confirmatory experiment is **negative-stain or cryo-EM of the recombinantly expressed protein**, which should reveal ~25–42 nm icosahedral shells (with co-purified cargo density inside). Confidence in this conclusion is **very high**.

---

## Key Findings

### Finding 1 — A0A0D5NHT9 / NF041162 is a Family 2A encapsulin shell protein (HK97 fold), not a membrane protein

The decisive evidence is the set of curated, expert-reviewed database signatures cross-referenced to UniProt A0A0D5NHT9. These are not automated guesses; they are hand-curated protein-family models whose scope, membership, and functional descriptions are defined by domain specialists:

| Signature | Accession | Name / description |
|-----------|-----------|--------------------|
| NCBIfam (PGAP) | **NF041162** | short-name "**encap_f2a**" — the *equivalog* family in the research question |
| InterPro | **IPR049822** | "**Encapsulin nanocompartment shell protein 2A**" |
| InterPro | **IPR045641** | "Type 2A encapsulin shell protein SrpI-like" |
| Pfam | **PF19307** | SrpI-like encapsulin shell family |

InterPro's curated narrative for these signatures states plainly that they describe "**capsid-like encapsulin nanocompartment shell proteins (type 2A)**" that "**share the HK97 fold of the capsid proteins**" found in *Caudovirales* bacteriophages, and that the founding member SrpI "**forms a nanocompartment probably involved in sulfur metabolism**." Every one of the four independent signatures points to the same conclusion — this is an encapsulin Family 2A shell subunit. This is precisely the Foldseek/structural conclusion the question anticipated: the fold **is** the self-assembling HK97 phage-capsid fold, reached directly through the protein's curated fold-family membership rather than through any membrane topology.

Independent sequence-based analysis fully corroborates a soluble shell protein and directly contradicts an integral-membrane assignment. A 19-residue sliding-window Kyte–Doolittle hydropathy scan gives a **maximum mean hydropathy of only 1.89** — no window approaches the ~2.5 threshold diagnostic of a bona fide transmembrane helix, and only two marginal windows even exceed 1.6. The composition is that of a hydrophilic, charged protein: **net charge −6**, with **33 basic and 39 acidic residues** among 314 total. This is the amino-acid signature of a cytoplasmic, water-soluble protein that oligomerizes into a shell, not of a membrane-embedded polypeptide.

Crucially, the origin of the erroneous name is traceable: the UniProt display name "Membrane protein" derives **solely** from the unreviewed, automatically annotated EMBL nucleotide-derived protein entry **AJY74493.1**. It carries no experimental support, and no curated database signature endorses it. It is a placeholder that the specific NF041162/IPR049822/PF19307 assignments supersede.

The literature confirms that this is the correct protein class. Encapsulins are "**self-assembling protein nanocompartments widely distributed across prokaryotes that sequester diverse enzymes**" ([PMID: 41481934](https://pubmed.ncbi.nlm.nih.gov/41481934/)); they "**self-assemble into icosahedral structures that capture cargo proteins through a cargo-loading peptide (CLP)**" ([PMID: 42297566](https://pubmed.ncbi.nlm.nih.gov/42297566/)); and each is a "**protein nanocage consisting of a single monomer protein**" ([PMID: 41794648](https://pubmed.ncbi.nlm.nih.gov/41794648/)) — i.e., the entire shell is built from one repeated subunit, so the "assembly" is an emergent property of self-association, not a membrane insertion.

### Finding 2 — The AlphaFold model is a high-confidence α+β HK97-type capsid subunit, not a transmembrane helix bundle

The AlphaFold DB model **AF-A0A0D5NHT9-F1 (v6)** provides direct structural evidence, independent of the sequence-database signatures. Its global **pLDDT is 89.94**, with **76.4% of residues at very-high confidence** and only ~1% at very-low confidence — this is a **confidently folded single domain**, not a disordered or membrane-ambiguous chain for which AlphaFold would produce low confidence.

The geometry is diagnostic of a capsid subunit. The model is a **single elongated globular domain** with a radius of gyration of **28.0 Å** and a bounding box of **57.5 × 113.5 × 74.0 Å**. The pronounced long axis (~113 Å) is the hallmark of an HK97-type capsid subunit, which carries an extended **E-loop** and **P-arm/spine** that project along the shell surface.

The secondary-structure content, computed from backbone φ/ψ angles, is **mixed α/β dominated by an extensive β-sheet** (>20 β-strands) plus **6 helices, including one long ~22-residue helix** — the canonical HK97 "**spine helix**." Most importantly, there is **no bundle of long hydrophobic transmembrane helices**. An integral inner-membrane protein of 314 aa would present multiple contiguous ~20-residue hydrophobic helices spanning the model; their complete absence, combined with the large β-sheet and single spine helix, is fully consistent with the HK97 bacteriophage-capsid fold assigned by IPR049822/PF19307 and is incompatible with a membrane protein.

### Finding 3 — The correct cellular component is GO:0140737 "encapsulin nanocompartment," a non-membrane-bound organelle

Having established the fold and family, the correct subcellular localization follows directly and is captured by a dedicated Gene Ontology cellular-component term. **GO:0140737 "encapsulin nanocompartment"** (aspect: *cellular_component*) is defined as an "**Intracellular non-membrane bound organelle, consisting of proteinaceous polyhedral shells that encapsulate enzymes**... The self-assembling, **25–42 nm** nanocompartment shell... is made of only one protein... The shell protein has an **HK97-like fold and probably evolved from a viral protein**."

Because A0A0D5NHT9 is assigned to encapsulin Family 2A by four converging signatures (NF041162 "encap_f2a"; PF19307 SrpI-like; IPR049822 and IPR045641), its subunits localize to precisely this compartment: an **intracellular, non-membrane-bound, proteinaceous organelle in the cytoplasm**. This is the antithesis of the UniProt placeholder "Membrane protein." The organelle has no lipid bilayer, is not embedded in the plasma/inner membrane, and is not a membrane-spanning polypeptide. The GO framework thus provides the correct, specific cellular-component assignment and formally documents that "membrane protein" is a mis-annotation.

---

## Mechanistic Model / Interpretation

Synthesizing the three findings yields a single coherent identity for A0A0D5NHT9 and the entire NF041162 family:

```
   Sequence: 314 aa, hydrophilic (net charge -6), no TM segment (max KD hydropathy 1.89)
                                   │
                                   ▼
   Fold: HK97 bacteriophage major-capsid-protein fold
         (α+β; large β-sheet + long ~22-aa "spine" helix; extended E-loop/P-arm)
         AlphaFold pLDDT 89.9, elongated subunit (Rg 28 Å, long axis ~113 Å)
                                   │
                                   ▼
   Family: Encapsulin Family 2A  (NF041162 "encap_f2a";
           IPR049822 / IPR045641 SrpI-like; Pfam PF19307)
                                   │
                                   ▼
   Higher-order assembly: SELF-ASSEMBLING ICOSAHEDRAL SHELL
           ~60+ identical subunits → 25-42 nm nanocompartment
           interior encapsulates enzyme cargo via a cargo-loading peptide
                                   │
                                   ▼
   Localization: GO:0140737 "encapsulin nanocompartment"
           intracellular, NON-membrane-bound proteinaceous organelle (cytoplasm)
                                   │
                                   ▼
   Verdict: "Membrane protein" = MIS-ANNOTATION (from unreviewed EMBL AJY74493.1)
```

The narrative is as follows. A single ~314-aa soluble polypeptide folds into an HK97-type capsid subunit — the same fold used by tailed bacteriophages (*Caudovirales*) to build their capsids, from which encapsulins are thought to have evolved. Many copies of this subunit self-assemble into a closed icosahedral shell 25–42 nm in diameter. This shell is a bacterial organelle — a **nanocompartment** — whose interior lumen sequesters specific enzyme cargo that is targeted to the shell through a cargo-loading peptide. For Family 2A / SrpI-like encapsulins, the associated chemistry is implicated in **sulfur metabolism**, though cargo identity varies across the family. The assembly floats in the cytoplasm as a non-membrane-bound organelle; it neither spans nor is anchored in the inner membrane.

The mis-annotation is therefore an artifact of automated pipelines that assigned a generic "Membrane protein" placeholder to an ORF (EMBL AJY74493.1) before any family-specific model matched it. Every subsequent, curated signal — NCBIfam, InterPro, Pfam, GO, AlphaFold structure, and raw hydropathy — overrides that placeholder in the same direction.

The following comparison table crystallizes why "membrane protein" fails and "encapsulin shell protein" succeeds:

| Property | Expected for integral membrane protein | Observed for A0A0D5NHT9 | Consistent with |
|----------|----------------------------------------|--------------------------|-----------------|
| Hydropathy | ≥1 TM segment, KD > ~2.5 | max KD 1.89; no TM window | Soluble shell |
| Net charge | Often near-neutral/hydrophobic core | −6 (hydrophilic, 33 K/R + 39 D/E) | Soluble shell |
| AlphaFold helices | Bundle of long hydrophobic TM helices | 6 helices, one 22-aa spine; no TM bundle | HK97 capsid fold |
| AlphaFold topology | Membrane-spanning | Elongated α+β with large β-sheet | HK97 capsid fold |
| Curated family | (none supports membrane) | NF041162 / IPR049822 / PF19307 (encapsulin 2A) | Encapsulin shell |
| GO cellular component | plasma/inner membrane | GO:0140737 nanocompartment (non-membrane) | Cytoplasmic organelle |

---

## Evidence Base

The curated database signatures (NF041162, IPR049822, IPR045641, PF19307), the AlphaFold model (AF-A0A0D5NHT9-F1), the GO term GO:0140737, and the raw-sequence hydropathy analysis are the primary evidence; the literature below independently confirms that the encapsulin class this protein belongs to has exactly the properties (self-assembly, icosahedral shell, single-monomer nanocage, cytoplasmic nanocompartment) claimed here.

| PMID | Title | How it supports the finding |
|------|-------|------------------------------|
| [42297566](https://pubmed.ncbi.nlm.nih.gov/42297566/) | *Encapsulin-Protected Immunotherapeutic Complexes: Bacteria-Derived Nanoparticles for mRNA Delivery to Eukaryotic Cells* | Establishes the icosahedral higher-order assembly and cargo encapsulation: "Encapsulins are protein nanocompartments that self-assemble into icosahedral structures that capture cargo proteins through a cargo-loading peptide (CLP)." |
| [41794648](https://pubmed.ncbi.nlm.nih.gov/41794648/) | *Reprogramming the flavo-encapsulin from Thermotoga maritima to a novel protein nanocage platform for potent photodynamic therapy* | Confirms the shell is built from a single self-assembling monomer: "Encapsulins are protein nanocages consisting of a single monomer protein" — the assembly is emergent, not a membrane protein. |
| [41481934](https://pubmed.ncbi.nlm.nih.gov/41481934/) | *Encapsulins in Terpene Biosynthesis: Enzyme Nanoreactors in Bacterial Secondary Metabolism* | Confirms encapsulins are the correct class: "Encapsulins are self-assembling protein nanocompartments widely distributed across prokaryotes that sequester diverse enzymes." |
| [41309228](https://pubmed.ncbi.nlm.nih.gov/41309228/) | *Encapsulin protein MAV2054 enhances Mycobacterium avium virulence...* | Provides a concrete precedent that a "**family 2A encapsulin nanocompartment shell protein**" is a real, named functional entity in bacteria — the exact family assigned to A0A0D5NHT9. |
| [41369466](https://pubmed.ncbi.nlm.nih.gov/41369466/) | *Characterization of Iron Oxide Nanoparticles Inside the [encapsulin]* | Reinforces that encapsulins are "microbial protein nanocompartments that spatially organize and sequester specific biochemical processes," consistent with a cytoplasmic organelle, not a membrane protein. |
| [41239465](https://pubmed.ncbi.nlm.nih.gov/41239465/) | *Generation of hTERT-immortalized human MSCs with optical and magnetic labels...* | Independently describes bacterial nanocompartments as "high-molecular-weight icosahedral capsid-like protein complexes" with a shell + cargo architecture, matching the assembly model here. |

No paper in the reviewed set challenges the conclusion; all are consistent with the encapsulin-shell identity. The literature does not, by itself, prove that *this specific* protein is an encapsulin — that is established by the curated signatures and structure — but it validates every property attributed to the family.

---

## Supported vs. Refuted Hypotheses

- **Supported:** HK97 phage-capsid fold; self-assembling icosahedral encapsulin (Family 2A / SrpI-like) nanocompartment; cytoplasmic, non-membrane-bound localization; "membrane protein" is a mis-annotation.
- **Refuted:** Integral membrane protein / monomeric membrane component — no transmembrane helices in the AlphaFold model, no TM segment in the hydropathy profile, hydrophilic and negatively charged composition, and the curated fold family is a capsid shell.

---

## Limitations and Knowledge Gaps

1. **No direct experimental structure of A0A0D5NHT9.** The fold assignment rests on curated homology models (Pfam/InterPro/NCBIfam) and an AlphaFold prediction, not an experimental cryo-EM or crystal structure of this exact protein. AlphaFold predicts the monomer fold with high confidence but does not itself prove shell assembly.

2. **Foldseek was not run as a live structural search in this investigation.** The HK97-fold assignment is supported by the AlphaFold monomer topology (large β-sheet + spine helix, no TM bundle) and by curated signatures that explicitly cite the HK97 fold, rather than by a fresh Foldseek query returning a specific PDB hit (e.g., an experimental HK97 or *T. maritima* encapsulin structure). A direct Foldseek run would strengthen the "closest experimentally characterized structural homolog" claim by naming a specific PDB and TM-score.

3. **Cargo identity is inferred, not demonstrated.** Family 2A / SrpI-like encapsulins are associated with sulfur metabolism, but the specific cargo enzyme(s) encapsulated by the *P. beijingensis* protein and its genomic neighbors were not characterized here.

4. **Assembly symmetry and T-number not determined.** Whether this shell is T=1 (~24 nm), T=3 (~32 nm), or T=4 (~42 nm) — and thus the exact subunit count — is not established for A0A0D5NHT9 and would require EM reconstruction.

5. **Species generalization.** The conclusion is drawn for the NF041162 representative; while the family is an *equivalog* (functionally conserved), individual members could in principle diverge, though this is unlikely given the tight signature agreement.

---

## Proposed Follow-up Experiments / Actions

1. **(Decisive) Negative-stain and cryo-EM of the recombinant protein.** Express A0A0D5NHT9 in *E. coli*, purify, and image. The prediction is **~25–42 nm icosahedral shells** with internal cargo density, plus a single high-molecular-weight assembling species by size-exclusion chromatography / native PAGE. This single experiment would definitively confirm the self-assembling nanocompartment identity and refute "membrane protein." Cryo-EM single-particle reconstruction would additionally fix the T-number and subunit count.

2. **Run an explicit Foldseek search** of AF-A0A0D5NHT9-F1 against the PDB/AlphaFold databases to name the closest experimentally characterized structural homolog (expected: an HK97 phage capsid protein and/or a *T. maritima*/Family 2 encapsulin shell) with quantitative TM-score, closing limitation #2.

3. **Solubility / localization fractionation.** Cell fractionation (cytoplasm vs. membrane) with Western blotting or proteomics should place the protein in the **soluble cytoplasmic fraction**, not the membrane fraction — a fast, low-cost falsification test of the mis-annotation.

4. **Cargo identification.** Analyze the genomic neighborhood of the NF041162 locus (around EMBL AJY74493.1) for a co-encoded enzyme bearing a cargo-loading peptide (likely sulfur-metabolism-related for the SrpI-like Family 2A), and confirm co-purification of cargo with the shell by mass spectrometry.

5. **Database correction.** Submit evidence to UniProt to update the protein name from the placeholder "Membrane protein" to "Encapsulin shell protein (Family 2A)" and to annotate the cellular component as GO:0140737 "encapsulin nanocompartment."

---

## Conclusion (one clear statement with confidence)

**A0A0D5NHT9 / NF041162 is a Family 2A encapsulin nanocompartment shell protein with the HK97 bacteriophage major-capsid-protein fold. It self-assembles into a ~25–42 nm icosahedral, non-membrane-bound proteinaceous organelle (GO:0140737 "encapsulin nanocompartment") in the cytoplasm that encapsulates enzyme cargo. "Membrane protein" is a mis-annotation.** Confidence: **very high** (four converging curated signatures + high-confidence AlphaFold α+β capsid fold with no TM helices + hydrophilic, charged, TM-free sequence). The one confirmatory experiment: **cryo-EM / negative-stain EM of the recombinant protein revealing ~25–42 nm icosahedral shells with internal cargo density.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)