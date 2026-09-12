---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T12:25:25.807516'
end_time: '2026-07-23T12:49:18.361340'
duration_seconds: 1432.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murJ
  gene_symbol: murJ
  uniprot_accession: Q88Q94
  protein_description: 'RecName: Full=Probable lipid II flippase MurJ {ECO:0000256|HAMAP-Rule:MF_02078};'
  gene_info: Name=murJ {ECO:0000256|HAMAP-Rule:MF_02078, ECO:0000313|EMBL:AAN66227.1};
    OrderedLocusNames=PP_0601 {ECO:0000313|EMBL:AAN66227.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MurJ/MviN family.
  protein_domains: Lipid_II_flippase_MurJ/MviN. (IPR051050); MurJ. (IPR004268); MurJ
    (PF03023)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murJ-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88Q94
- **Protein Description:** RecName: Full=Probable lipid II flippase MurJ {ECO:0000256|HAMAP-Rule:MF_02078};
- **Gene Information:** Name=murJ {ECO:0000256|HAMAP-Rule:MF_02078, ECO:0000313|EMBL:AAN66227.1}; OrderedLocusNames=PP_0601 {ECO:0000313|EMBL:AAN66227.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MurJ/MviN family.
- **Key Domains:** Lipid_II_flippase_MurJ/MviN. (IPR051050); MurJ. (IPR004268); MurJ (PF03023)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murJ** (gene ID: murJ, UniProt: Q88Q94) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MurJ (PP_0601 / Q88Q94) — *Pseudomonas putida* KT2440

**Gene:** *murJ* (synonym *mviN*) — Ordered locus name **PP_0601**
**UniProt:** Q88Q94 (MURJ_PSEPK)
**Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440 (a Gram-negative, diderm soil bacterium)
**Protein family:** MurJ/MviN family (MOP exporter superfamily); Pfam **PF03023 (MurJ)**; InterPro **IPR004268 (MurJ)**, **IPR051050 (Lipid_II_flippase_MurJ/MviN)**; HAMAP rule **MF_02078**

---

## Summary

The gene **murJ** (ordered locus **PP_0601**; UniProt **Q88Q94**) of *Pseudomonas putida* KT2440 encodes the **probable lipid II flippase MurJ**, an essential polytopic integral protein of the **cytoplasmic (inner) membrane**. Its primary molecular function is to **translocate ("flip") the lipid-linked peptidoglycan precursor lipid II** — undecaprenyl-pyrophosphoryl-MurNAc-(pentapeptide)-GlcNAc — from the **inner (cytoplasmic) leaflet to the outer (periplasmic) leaflet** of the cytoplasmic membrane. This step delivers the cell-wall building block to the periplasmic face, where penicillin-binding proteins (PBPs) and SEDS-family glycosyltransferases polymerize and cross-link it into mature peptidoglycan. MurJ is therefore a central, essential component of the **peptidoglycan (murein) biosynthesis pathway**, and, because of its essentiality and surface accessibility, an actively pursued **antibiotic target**.

MurJ is a **transporter (flippase), not a classical enzyme** — it does not chemically modify its substrate; it moves lipid II vectorially across the bilayer. It operates by an **ion-dependent alternating-access mechanism**, cycling through inward-facing, occluded, "squeezed", and outward-facing conformations driven by essential cationic (arginine) residues and coupled to ion (chloride) binding. In dividing cells, MurJ localizes to **both the lateral membrane and the division septum (midcell)**, coupling lipid II delivery to both cell-wall elongation and septal synthesis.

The functional assignment for the *P. putida* protein is a **high-confidence orthology-based inference**. Q88Q94 carries the diagnostic family signatures (PF03023, IPR004268, IPR051050) and is annotated by curated HAMAP rule MF_02078 as a probable lipid II flippase. The supporting experimental literature derives from characterized orthologs (chiefly *E. coli*, plus thermophiles and endosymbionts used for structural work); the *P. putida* protein itself has **not been directly biochemically characterized**. Because MurJ is conserved across all peptidoglycan-producing bacteria and lipid II flipping is universally essential, the transfer of function to PP_0601 is well justified, while acknowledging that organism-specific details await experimental confirmation. No conflicting "same-symbol, different-gene" ambiguity was found: gene symbol, protein description, family, and domains all agree.

---

## Key Findings

### Finding 1 — MurJ is the essential lipid II flippase of peptidoglycan biosynthesis

MurJ (Q88Q94, PP_0601) is assigned as the **essential inner-membrane lipid II flippase** required for peptidoglycan (PG) biosynthesis. The identity of the bacterial lipid II flippase was historically contested, but the protein originally called **MviN** was identified in *E. coli* by bioinformatic analysis as the likely candidate and subsequently **renamed MurJ**; genetic and biochemical follow-up confirmed that it is the essential inner-membrane protein required for peptidoglycan biosynthesis, consistent with a flippase that translocates lipid II across the cytoplasmic membrane. As the original author stated, "*I have identified the essential inner-membrane protein MviN (renamed MurJ) as a likely candidate for the peptidoglycan flippase in Escherichia coli*" ([PMID: 18832143](https://pubmed.ncbi.nlm.nih.gov/18832143/)).

The reaction MurJ mediates is a **vectorial transport reaction** rather than covalent catalysis: it moves the amphipathic, undecaprenyl-anchored PG precursor from the cytoplasmic to the periplasmic leaflet of the inner membrane, making it accessible to the transglycosylases and transpeptidases that build the wall. This step is obligatory because the lipid II head group is large, charged, and cannot flip across the hydrophobic bilayer at physiologically useful rates without a dedicated transporter.

The assignment to the *P. putida* protein is an **orthology-based inference of high confidence**. Q88Q94 carries the diagnostic domain architecture of the family — **MurJ (PF03023)**, **IPR004268 (MurJ)**, and the family signature **IPR051050 (Lipid_II_flippase_MurJ/MviN)** — and is annotated by HAMAP rule **MF_02078** as a probable lipid II flippase. Because MurJ is **conserved across all peptidoglycan-producing bacteria** — "*This essential step is mediated by MurJ, the lipid II flippase conserved across all peptidoglycan-producing bacteria*" ([PMID: 42395403](https://pubmed.ncbi.nlm.nih.gov/42395403/)) — the *P. putida* ortholog is expected to perform the same essential role. This function makes MurJ a validated antibiotic target: blocking lipid II export halts PG synthesis and causes lethal cell-envelope failure.

| Claim | Basis | Source |
|-------|-------|--------|
| MurJ/MviN is the essential inner-membrane peptidoglycan flippase | Bioinformatic identification + genetic/biochemical validation in *E. coli* | [PMID: 18832143](https://pubmed.ncbi.nlm.nih.gov/18832143/) |
| MurJ is conserved across all PG-producing bacteria; mediates the essential lipid II flipping step | Comparative/structural review | [PMID: 42395403](https://pubmed.ncbi.nlm.nih.gov/42395403/) |
| *P. putida* Q88Q94 is a MurJ family member (probable flippase) | Pfam PF03023 / InterPro IPR004268 / HAMAP MF_02078 | UniProt annotation |

### Finding 2 — MurJ operates in the cytoplasmic membrane by an ion-dependent alternating-access mechanism

MurJ functions as a **flippase using an alternating-access mechanism**, the canonical scheme for solute transporters, in which a single central substrate-binding cavity is exposed alternately to the cytoplasmic and periplasmic sides of the membrane. As the mechanistic study states, "*The bacterial lipid II flippase MurJ functions by an alternating-access mechanism*" ([PMID: 30482840](https://pubmed.ncbi.nlm.nih.gov/30482840/)).

Crystal structures of MurJ orthologs have captured the transporter across the conformational cycle: "*we report crystal structures of MurJ captured in inward-closed, inward-open, inward-occluded and outward-facing conformations*" ([PMID: 30988294](https://pubmed.ncbi.nlm.nih.gov/30988294/)), directly visualizing the states that underlie lipid II flipping. More recently, an *E. coli* MurJ structure was solved in a **"squeezed" form** that lacks the substrate cavity because transmembrane helices 2 and 8 move into close proximity; molecular dynamics simulations supported this squeezed state as an on-pathway **intermediate conformation**, filling a mechanistic gap between the inward- and outward-facing forms ([PMID: 35660157](https://pubmed.ncbi.nlm.nih.gov/35660157/)). The architecture is a **V-shaped, central-cavity** fold that binds the polar lipid II head group, with the isoprenoid tail engaging a lateral, membrane-facing groove.

The transport cycle is **ion-dependent**. In *Thermosipho africanus* MurJ, "*Chloride Ions Are Required for Thermosipho africanus MurJ Function*" ([PMID: 36752629](https://pubmed.ncbi.nlm.nih.gov/36752629/)), indicating that anion binding is coupled to the conformational transitions that drive flipping. Complementary in vivo mechanistic work using **photo-cross-linking and biotin-tagging** captured lipid II transport intermediates on MurJ in living *E. coli* cells and probed a set of lethal **arginine mutants**; these mutants retained substantial substrate-binding ability but were defective in transport, showing that lipid II binding to essential cationic residues induces the conformational change needed to proceed through the cycle ([PMID: 32129990](https://pubmed.ncbi.nlm.nih.gov/32129990/)). Together these studies establish that MurJ works within the **cytoplasmic (inner) membrane** and that its transport power derives from ion-coupled, cationic-residue-driven conformational cycling. MurJ belongs to the MOP (Multidrug/Oligosaccharidyl-lipid/Polysaccharide) exporter superfamily; reviews summarize the structural mechanism across the flippase field ([PMID: 35320686](https://pubmed.ncbi.nlm.nih.gov/35320686/)).

**Conformational states captured for MurJ:**

| State | Description | Role in cycle |
|-------|-------------|---------------|
| Inward-closed | Cavity closed toward cytoplasm | Resting / pre-loading |
| Inward-open | Cavity open to cytoplasm | Lipid II head-group loading |
| Inward-occluded | Cavity sealed with substrate bound | Committed intermediate |
| "Squeezed" | Cavity collapsed (TM2–TM8 proximity) | Transition intermediate |
| Outward-facing | Cavity open to periplasm | Substrate release to outer leaflet |

### Finding 3 — MurJ localizes to the lateral membrane and is recruited to midcell during division

MurJ is distributed in **two functional pools** within the cell. In *E. coli*, "*MurJ localizes both in the lateral membrane and at midcell, and is recruited to midcell simultaneously with late-localizing divisome proteins and proteins MraY and MurG*" ([PMID: 30112777](https://pubmed.ncbi.nlm.nih.gov/30112777/)). The lateral (peripheral) membrane pool supports cell-wall elongation along the cylinder, while the midcell pool serves the division septum. Crucially, septal localization is not constitutive: it **requires a complete, active divisome, ongoing lipid II synthesis, and the activities of the septal PG synthase PBP3 (FtsI) and its SEDS partner FtsW**. This dependency positions MurJ to deliver lipid II precisely where and when septal peptidoglycan is being made, coupling precursor export to the spatiotemporal program of cell division ([PMID: 30112777](https://pubmed.ncbi.nlm.nih.gov/30112777/)).

This localization pattern reinforces the mechanistic model: MurJ acts at the **interface between cytoplasmic precursor synthesis and periplasmic wall assembly**, and its dual lateral/septal distribution mirrors the two modes of PG synthesis (elongation via the elongasome and division via the divisome). For *P. putida*, a rod-shaped Gram-negative bacterium with an analogous divisome and elongasome, the same spatial logic is expected to apply, although it has not been directly tested in *P. putida*.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent picture of MurJ as the **membrane gateway for peptidoglycan precursors**. Lipid II is synthesized on the cytoplasmic face of the inner membrane, must be flipped by MurJ, and is then polymerized on the periplasmic face:

```
   CYTOPLASM
   ┌─────────────────────────────────────────────────────────┐
   │  UDP-MurNAc-pentapeptide + UDP-GlcNAc                    │
   │            │ MraY (→ lipid I)                            │
   │            │ MurG (→ lipid II)                           │
   │            ▼                                             │
   │        Lipid II  (C55-PP-MurNAc(pentapeptide)-GlcNAc)   │
   ══════════════╪══════════════════════════════════════════  INNER
   INNER LEAFLET │                                            MEMBRANE
                 │  ┌──────────────┐                          (cytoplasmic
                 └─▶│    MurJ       │  alternating access      membrane)
                    │  V-shaped     │  + Cl⁻ / Arg-driven
                    │  cavity       │  conformational cycle
                    │  (PF03023)    │
   OUTER LEAFLET ◀──┴──────────────┘
   ══════════════╪══════════════════════════════════════════
   PERIPLASM     ▼
             Lipid II (outer leaflet)
                 │  RodA/FtsW (SEDS) + PBPs
                 ▼  (transglycosylation / transpeptidation)
             PEPTIDOGLYCAN (murein sacculus)
```

**Reaction (vectorial transport):**

```
Lipid II (inner leaflet, cytoplasmic face)
        ──[ MurJ, ion-coupled alternating access ]──▶
Lipid II (outer leaflet, periplasmic face)
```

**Pathway placement** — MurJ operates at the membrane-translocation junction of peptidoglycan biosynthesis:

1. **Cytoplasmic phase:** UDP-GlcNAc → UDP-MurNAc → UDP-MurNAc-pentapeptide (MurA–MurF).
2. **Membrane phase (inner leaflet):** MraY transfers phospho-MurNAc-pentapeptide to undecaprenyl phosphate → **lipid I**; MurG adds GlcNAc → **lipid II**.
3. **Translocation:** **MurJ flips lipid II to the periplasmic leaflet** ← *the step performed by PP_0601*.
4. **Periplasmic phase:** SEDS proteins (RodA in elongation, FtsW in division) and class A/B PBPs polymerize and cross-link lipid II into mature peptidoglycan; the undecaprenyl-pyrophosphate carrier is recycled.

Because its bulky, charged disaccharide-pentapeptide head cannot cross the bilayer unaided, MurJ captures the head group in its central cavity and, through ion-dependent conformational cycling (inward → occluded/squeezed → outward), delivers it to the periplasmic leaflet. The **dual localization** of MurJ — lateral membrane plus septum — matches the two PG-synthetic machineries, and its **divisome-dependent recruitment** ensures precursors are supplied at the septum in step with FtsI/FtsW activity.

For *P. putida* KT2440, the model is transferred by orthology: PP_0601 has the conserved MurJ fold signature and the essential-flippase annotation, and *P. putida* possesses a complete Gram-negative PG-synthesis pathway that requires exactly this export step. MurJ is therefore predicted to be **essential** in *P. putida*, to reside in the **inner membrane**, and to serve as the **primary lipid II flippase**, consistent with the pan-bacterial conservation of the function.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / relates to the annotation |
|------|-----------------|---------------------------------------------|
| [18832143](https://pubmed.ncbi.nlm.nih.gov/18832143/) | *Bioinformatics identification of MurJ (MviN) as the peptidoglycan lipid II flippase in E. coli* | Foundational: identifies and validates MurJ/MviN as the essential inner-membrane flippase. Direct basis for the family/function of Q88Q94. |
| [42395403](https://pubmed.ncbi.nlm.nih.gov/42395403/) | *The structure of the lipid II flippase from monoderm bacteria* | Establishes MurJ as the lipid II flippase conserved across **all** PG-producing bacteria, justifying orthologous transfer to *P. putida*. |
| [30482840](https://pubmed.ncbi.nlm.nih.gov/30482840/) | *The bacterial lipid II flippase MurJ functions by an alternating-access mechanism* | Defines the core transport mechanism. |
| [30988294](https://pubmed.ncbi.nlm.nih.gov/30988294/) | *Visualizing conformation transitions of the lipid II flippase MurJ* | Crystal structures of inward-closed, inward-open, inward-occluded, outward-facing states — structural basis of the cycle. |
| [35660157](https://pubmed.ncbi.nlm.nih.gov/35660157/) | *Crystal structure of MurJ in a "squeezed" form* | Adds the intermediate "squeezed" conformation; MD supports it as a transition state. |
| [36752629](https://pubmed.ncbi.nlm.nih.gov/36752629/) | *Chloride ions are required for T. africanus MurJ function* | Demonstrates the ion (chloride) dependence driving the transport cycle. |
| [32129990](https://pubmed.ncbi.nlm.nih.gov/32129990/) | *Detection of transport intermediates in the peptidoglycan flippase MurJ...* | In vivo capture of lipid II transport intermediates; identifies essential arginine residues for conformational cycling. |
| [30112777](https://pubmed.ncbi.nlm.nih.gov/30112777/) | *FtsW activity and lipid II synthesis are required for recruitment of MurJ to midcell* | Establishes subcellular localization (lateral + septal) and divisome-dependent recruitment. |
| [35320686](https://pubmed.ncbi.nlm.nih.gov/35320686/) | *Structure and mechanism of the lipid flippase MurJ* (review) | Synthesizes structural/mechanistic understanding across polysaccharide export systems. |
| [26792999](https://pubmed.ncbi.nlm.nih.gov/26792999/) | *Lipid flippases for bacterial peptidoglycan biosynthesis* (review) | Reviews the flippase controversy (FtsW/MurJ/AmJ) and the difficulty of flippase identification, contextualizing MurJ's role. |
| [41061077](https://pubmed.ncbi.nlm.nih.gov/41061077/) | *Phage lysis protein Lys* | Illustrates MurJ as an antibacterial vulnerability in the peptidoglycan biogenesis pathway. |

**Note on candidate controversy.** The historical debate over which protein flips lipid II (MurJ vs. FtsW vs. AmJ) is important context ([PMID: 26792999](https://pubmed.ncbi.nlm.nih.gov/26792999/)). The weight of subsequent structural, biochemical, and in vivo evidence supports **MurJ as the primary lipid II flippase** in the great majority of bacteria, with FtsW acting principally as a SEDS-family glycosyltransferase/septal partner. This does not detract from the MurJ annotation of Q88Q94 but should be noted for completeness.

---

## Limitations and Knowledge Gaps

1. **No direct characterization of the *P. putida* protein.** All mechanistic, structural, and localization data derive from orthologs — principally *E. coli*, and thermophiles/endosymbionts (*Thermosipho africanus*, *Arsenophonus* endosymbiont) used for crystallography. Q88Q94 has not been purified, assayed, deleted, or imaged in *P. putida* KT2440. Its function is inferred, with high confidence, from conserved sequence/domain features (PF03023, IPR004268, IPR051050, HAMAP MF_02078). The UniProt qualifier "Probable" reflects this rule-based (not organism-specific) assignment.

2. **Essentiality not experimentally confirmed in *P. putida*.** MurJ is essential in *E. coli*; essentiality in *P. putida* is predicted but not verified from primary data.

3. **Ion specificity may vary.** Chloride dependence was demonstrated for *T. africanus* MurJ ([PMID: 36752629](https://pubmed.ncbi.nlm.nih.gov/36752629/)); whether *P. putida* MurJ uses the same ion, a cation gradient, or the membrane potential differently is not established.

4. **Residue-level mapping absent.** The essential arginine residues and TM2/TM8 dynamics defined in *E. coli* have not been mapped onto the Q88Q94 sequence in this investigation; the specific transport-critical residues of the *P. putida* protein remain to be annotated by alignment.

5. **Redundancy/regulation and substrate scope unexplored.** Whether *P. putida* encodes accessory or backup flippases (e.g., AmJ-like), regulates MurJ under envelope stress, or can transport modified lipid II variants relevant to its envelope biology is not addressed.

---

## Proposed Follow-up Experiments / Actions

1. **Sequence-to-structure mapping.** Align Q88Q94 to characterized MurJ orthologs (*E. coli*, *T. africanus*) and solved structures; build an AlphaFold model and inspect the V-shaped cavity, TM2/TM8, essential arginines, and a putative chloride-coordinating site.

2. **Genetic essentiality test.** Attempt a chromosomal *murJ*/PP_0601 deletion or construct a conditional (depletion) allele in *P. putida* KT2440; the predicted phenotype is lethal cell lysis upon depletion, confirming essentiality.

3. **Functional complementation.** Test whether *P. putida murJ* rescues a conditional *E. coli murJ* mutant, providing a direct, transferable readout of flippase activity.

4. **Localization imaging.** Construct a functional fluorescent MurJ fusion in *P. putida* to test the predicted dual lateral/septal localization and divisome-dependent midcell recruitment.

5. **In vivo intermediate capture.** Adapt the photo-cross-linking/biotin-tagging assay ([PMID: 32129990](https://pubmed.ncbi.nlm.nih.gov/32129990/)) to *P. putida* to confirm lipid II binding and transport intermediates.

6. **Ion dependence.** Test chloride/ion requirements of purified *P. putida* MurJ reconstituted in proteoliposomes.

7. **Antibiotic-target validation.** Given MurJ's status as a validated target, screen MurJ-directed inhibitors (e.g., phage-lysis-derived or small-molecule conformational trappers) against *P. putida* MurJ to assess conservation of druggable sites.

---

## Conclusion

*Pseudomonas putida* KT2440 **murJ / PP_0601 (Q88Q94)** encodes the **essential lipid II flippase MurJ**, an inner-membrane transporter that flips the peptidoglycan precursor lipid II from the cytoplasmic to the periplasmic leaflet of the cytoplasmic membrane — the committed export step of cell-wall biosynthesis. It works by an **ion-dependent (chloride) alternating-access mechanism** driven by essential cationic residues and cycling through inward-, occluded/squeezed-, and outward-facing conformations, and it localizes to both the **lateral membrane** and the **division septum**, where its recruitment is coupled to the active divisome and lipid II synthesis. This annotation is a **high-confidence orthology transfer** (Pfam PF03023 / InterPro IPR004268 / HAMAP MF_02078; conserved across all PG-producing bacteria); the *P. putida* protein itself awaits direct experimental characterization.


## Artifacts

- [OpenScientist final report](murJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murJ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18832143
2. PMID:42395403
3. PMID:30482840
4. PMID:30988294
5. PMID:35660157
6. PMID:36752629
7. PMID:32129990
8. PMID:35320686
9. PMID:30112777
10. PMID:26792999