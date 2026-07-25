---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:12:40.717460'
end_time: '2026-07-20T20:45:14.705069'
duration_seconds: 1953.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemD
  gene_symbol: hemD
  uniprot_accession: Q88RE4
  protein_description: 'RecName: Full=Uroporphyrinogen-III synthase {ECO:0000256|ARBA:ARBA00040167,
    ECO:0000256|RuleBase:RU366031}; EC=4.2.1.75 {ECO:0000256|ARBA:ARBA00013109, ECO:0000256|RuleBase:RU366031};'
  gene_info: Name=hemD {ECO:0000313|EMBL:AAN65820.1}; OrderedLocusNames=PP_0187 {ECO:0000313|EMBL:AAN65820.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the uroporphyrinogen-III synthase family.
  protein_domains: 4pyrrol_syn_uPrphyn_synt_sf. (IPR036108); 4pyrrol_synth_uPrphyn_synth.
    (IPR003754); UROS/Hem4. (IPR039793); HEM4 (PF02602)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hemD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88RE4
- **Protein Description:** RecName: Full=Uroporphyrinogen-III synthase {ECO:0000256|ARBA:ARBA00040167, ECO:0000256|RuleBase:RU366031}; EC=4.2.1.75 {ECO:0000256|ARBA:ARBA00013109, ECO:0000256|RuleBase:RU366031};
- **Gene Information:** Name=hemD {ECO:0000313|EMBL:AAN65820.1}; OrderedLocusNames=PP_0187 {ECO:0000313|EMBL:AAN65820.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the uroporphyrinogen-III synthase family.
- **Key Domains:** 4pyrrol_syn_uPrphyn_synt_sf. (IPR036108); 4pyrrol_synth_uPrphyn_synth. (IPR003754); UROS/Hem4. (IPR039793); HEM4 (PF02602)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemD** (gene ID: hemD, UniProt: Q88RE4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# hemD (Q88RE4) in *Pseudomonas putida* KT2440: Uroporphyrinogen-III Synthase — Functional Annotation Report

## Summary

The gene **hemD** (ordered locus **PP_0187**; UniProt **Q88RE4**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125) encodes **uroporphyrinogen-III synthase** (U3S; also called uroporphyrinogen-III cosynthase; **EC 4.2.1.75**). This is the **fourth enzyme of the tetrapyrrole (heme) biosynthetic pathway**. It catalyzes the asymmetric cyclization of the linear tetrapyrrole **hydroxymethylbilane** (also called preuroporphyrinogen) into the macrocyclic **uroporphyrinogen III**, a reaction that requires **inversion of ring D** of the substrate to produce the physiologically relevant type-III isomer rather than the non-enzymatic, biologically useless type-I isomer. The gene assignment is unambiguous: the protein family (uroporphyrinogen-III synthase family), the Pfam domain (PF02602, HEM4), the InterPro signatures (IPR003754, IPR039793, IPR036108), and the EC number all converge on this single enzymatic identity, and the genomic neighborhood in *P. putida* independently corroborates it.

Mechanistically, U3S is unusual: it appears to be a **substrate-orienting enzyme** rather than a classical acid/base catalyst. The reaction is thought to proceed through a **spirocyclic pyrrolenine intermediate**, and site-directed mutagenesis of every invariant titratable residue in the human ortholog failed to abolish activity, arguing that the enzyme works primarily by holding the flexible linear substrate in a conformation that channels ring-D inversion, aided by a conserved tyrosine that may initiate the reaction by promoting loss of a hydroxyl group. Structurally, U3S is a two-domain (α/β) protein connected by a β-ladder hinge that permits large open/closed conformational motions during catalysis.

The enzyme is a **soluble, cytoplasmic monomer** of ~27 kDa (255 residues) with no membrane-spanning segment and no cleavable secretion signal, consistent with the known cytosolic localization of uroporphyrinogen-III synthases across biology. Its product, **uroporphyrinogen III**, is the **universal branch-point precursor** for all cellular modified tetrapyrroles — heme, siroheme, chlorophyll, coenzyme F430, and vitamin B12 (cobalamin). In the aerobic, non-photosynthetic bacterium *P. putida*, HemD's principal physiological role is to supply uroporphyrinogen III for **heme biosynthesis**, with a secondary contribution toward **siroheme and cobalamin** synthesis. This role is reinforced by genomic synteny: PP_0187 sits between **PP_0186 (hemC**, the enzyme that makes its substrate) and **PP_0188** (a uroporphyrin(ogen)-III C-methyltransferase that consumes its product toward the siroheme/cobalamin branch).

---

## Key Findings

### Finding 1 — HemD is uroporphyrinogen-III synthase, catalyzing cyclization of hydroxymethylbilane to uroporphyrinogen III

UniProt Q88RE4 assigns **EC 4.2.1.75** and membership in the **uroporphyrinogen-III synthase family** to *P. putida* KT2440 hemD/PP_0187, supported by the Pfam domain **PF02602 (HEM4)** and InterPro signatures **IPR003754**, **IPR039793**, and **IPR036108**. This enzyme catalyzes the **fourth step of tetrapyrrole biosynthesis**: the asymmetric cyclization of the linear tetrapyrrole hydroxymethylbilane (preuroporphyrinogen) into the macrocycle uroporphyrinogen III, with inversion of ring D.

The reaction and pathway position are firmly established by primary structural and biochemical literature on orthologous enzymes. Schubert et al. (2008), reporting the structure of a U3S–product complex, state that "*Uroporphyrinogen III synthase (U3S) catalyzes the asymmetrical cyclization of a linear tetrapyrrole to form the physiologically relevant uroporphyrinogen III (uro'gen III) isomer during heme biosynthesis*" ([PMID: 18651750](https://pubmed.ncbi.nlm.nih.gov/18651750/)). Mathews et al. (2001), describing the crystal structure of human U3S, specify both substrate and product and locate the enzyme in the pathway: "*Uroporphyrinogen III synthase, U3S, the fourth enzyme in the porphyrin biosynthetic pathway, catalyzes cyclization of the linear tetrapyrrole, hydroxymethylbilane, to the macrocyclic uroporphyrinogen III*" ([PMID: 11689424](https://pubmed.ncbi.nlm.nih.gov/11689424/)).

The distinction between the type-III and type-I isomers is functionally critical. Without the enzyme, hydroxymethylbilane cyclizes spontaneously (non-enzymatically) to **uroporphyrinogen I**, a symmetric isomer that cannot be converted into functional heme. Only the enzyme-directed ring-D inversion yields **uroporphyrinogen III**, the sole isomer that feeds the productive tetrapyrrole pathway. HemD therefore acts as a **fidelity-enforcing enzyme** that ensures flux is committed to physiologically useful tetrapyrroles.

### Finding 2 — Catalytic mechanism: substrate-directed cyclization via a spirocyclic intermediate with ring-D inversion, without classical acid/base catalysis

The defining chemical feature of the reaction is **inversion of ring D** of the linear tetrapyrrole. Leeper (1994) established the evidence for the reaction intermediate, noting that among possible mechanisms "*the most economical is one involving a spirocyclic pyrrolenine*" and confirming that "*ring D of the bilane becomes inverted*" ([PMID: 7842849](https://pubmed.ncbi.nlm.nih.gov/7842849/)). The spirocyclic pyrrolenine hypothesis is strongly supported by the observation that a synthetic spirolactam analog acts as a powerful inhibitor of the enzyme — a classic transition-state/intermediate-mimic argument.

Structural work reinforces a **conformational, substrate-orienting** picture of catalysis. Schubert et al. (2008) solved a U3S–product complex from *Thermus thermophilus* and described a two-domain (α/β) fold connected by a β-ladder that permits large interdomain conformational flexibility, capturing a "closed" product complex in which the product is held between the domains by hydrogen bonds to main-chain amides. They identified a candidate catalytic residue: "*A conserved tyrosine residue is potentially positioned to facilitate loss of a hydroxyl from the substrate to initiate the catalytic reaction*" ([PMID: 18651750](https://pubmed.ncbi.nlm.nih.gov/18651750/)).

Crucially, U3S does **not** appear to rely on classical acid/base chemistry. Mathews et al. (2001) mutated every invariant titratable residue in human U3S and none abolished activity, "*suggesting that the mechanism does not require acid/base catalysis*" ([PMID: 11689424](https://pubmed.ncbi.nlm.nih.gov/11689424/)). Together these results support a model in which the enzyme's main catalytic contribution is to **bind and orient the highly flexible linear substrate** so that ring-D inversion (via the spirocyclic intermediate) is favored over the spontaneous, non-inverting cyclization that would produce uroporphyrinogen I.

### Finding 3 — Pathway context and localization: cytosolic fourth enzyme producing the universal branch-point precursor

U3S is the fourth enzyme of the tetrapyrrole pathway, acting downstream of 5-aminolevulinic acid formation, porphobilinogen synthase (ALA dehydratase / HemB), and porphobilinogen deaminase / hydroxymethylbilane synthase (HemC). Its product, **uroporphyrinogen III**, is the common precursor from which all modified tetrapyrroles diverge. Mathews et al. (2001) describe uroporphyrinogen III as the metabolite "*which is used in several different pathways to form heme, siroheme, chlorophyll, F(430) and vitamin B(12)*" ([PMID: 11689424](https://pubmed.ncbi.nlm.nih.gov/11689424/)).

The enzyme is **soluble and cytosolic**. Cunha et al. (2008), developing NMR-based active-site mapping and expression/purification methods, refer to U3S among "*these cytosolic enzymes of heme biosynthesis*" ([PMID: 18004775](https://pubmed.ncbi.nlm.nih.gov/18004775/)). In *P. putida* KT2440, hemD (PP_0187) is a single-domain soluble protein of the UROS/HEM4 family (PF02602), fully consistent with cytoplasmic localization. In an aerobic heterotroph such as *P. putida*, the dominant fate of uroporphyrinogen III is **heme** (respiratory cytochromes, catalases, etc.), with additional flux toward **siroheme** (required as a cofactor for assimilatory sulfite and nitrite reductases) and potentially **cobalamin**.

### Finding 4 — Genomic synteny places hemD in a heme-biosynthesis gene neighborhood, flanked by substrate-supplying and product-consuming enzymes

Database annotation converges on the same enzymatic identity and situates the gene within a coherent metabolic neighborhood. KEGG/UniProt annotate PP_0187 as uroporphyrinogen-III synthase (KEGG Orthology **K01719**, EC 4.2.1.75), with the reaction captured in **Rhea RHEA:18965** (hydroxymethylbilane = uroporphyrinogen III + H2O), UniPathway **UPA00251** (protoheme biosynthesis, step 4 of 4), and orthology group eggNOG **COG1587**. The protein is a **255-residue monomer** with a single UROS/HEM4 domain spanning residues ~17–242.

The genomic neighborhood is diagnostic:

| Locus | Gene | Enzyme | KO / EC | Relationship to HemD |
|-------|------|--------|---------|----------------------|
| PP_0186 | hemC | Porphobilinogen deaminase / hydroxymethylbilane synthase | K01749 / EC 2.5.1.61 | **Immediately upstream** — produces HemD's substrate (hydroxymethylbilane) |
| **PP_0187** | **hemD** | **Uroporphyrinogen-III synthase** | **K01719 / EC 4.2.1.75** | **Target enzyme** |
| PP_0188 | — | Uroporphyrin(ogen)-III C-methyltransferase | K02496 / EC 2.1.1.107 | **Immediately downstream** — consumes HemD's product toward siroheme/cobalamin |

All three genes map to KEGG pathway **ppu00860 (Porphyrin metabolism)**. This physical clustering — the substrate-supplying enzyme (HemC) directly upstream and a product-consuming branch enzyme directly downstream — is exactly what would be expected for a functional heme-pathway operon and provides strong, independent (genomic) corroboration of the biochemical assignment.

### Finding 5 — Sequence analysis confirms a soluble cytoplasmic ~27 kDa monomer with no membrane anchor or signal peptide

Direct sequence analysis of Q88RE4 supports the localization inferred from homology. A **Kyte–Doolittle hydropathy analysis** (window 19) of the 255-residue sequence gives a maximum score of **1.39**, below the ~1.6 threshold typically required for a transmembrane helix — indicating **no membrane-spanning segment**. The estimated molecular weight is **≈27.0 kDa**. The N-terminus (MSQWRLLLTRPAEDC…) is charged/polar and lacks a cleavable secretion signal peptide. These features are all consistent with a **soluble cytoplasmic enzyme**, matching the established cytosolic localization of uroporphyrinogen-III synthases ([PMID: 18004775](https://pubmed.ncbi.nlm.nih.gov/18004775/)).

---

## Mechanistic Model / Interpretation

HemD occupies a precise, well-defined position in the tetrapyrrole biosynthetic pathway. The reaction it catalyzes, and its place in the pathway, can be summarized as follows:

```
   Glutamate / ALA
        │
        ▼
   5-Aminolevulinic acid (ALA)
        │  HemB (ALA dehydratase)
        ▼
   Porphobilinogen (PBG)
        │  HemC / PP_0186 (PBG deaminase / HMB synthase)
        ▼
   Hydroxymethylbilane  ── (spontaneous) ──▶  Uroporphyrinogen I  (dead-end, type-I)
   (linear tetrapyrrole)
        │
        │  ★ HemD / PP_0187  (Uroporphyrinogen-III synthase, EC 4.2.1.75) ★
        │     - cyclization + inversion of RING D
        │     - via spirocyclic pyrrolenine intermediate
        ▼
   Uroporphyrinogen III  ◀── UNIVERSAL BRANCH POINT
        │
        ├───────────────► Heme  (dominant fate in aerobic P. putida)
        │                 (via HemE/HemF/HemG/HemH etc.)
        │
        └──► PP_0188 (uroporphyrin-III C-methyltransferase, EC 2.1.1.107)
                    │
                    ├──► Siroheme  (cofactor for sulfite/nitrite reductases)
                    └──► Cobalamin / Vitamin B12
```

The central mechanistic insight is that HemD is a **fidelity enzyme operating at a kinetically vulnerable step**. Its substrate, hydroxymethylbilane, is chemically unstable and, in the absence of enzyme, cyclizes non-enzymatically to the symmetric type-I isomer, which is a metabolic dead end. HemD prevents this loss by binding the flexible linear substrate and enforcing the asymmetric cyclization with ring-D inversion, producing the sole isomer (type III) that can proceed to functional tetrapyrroles.

The enzyme achieves this not through classical acid/base catalysis but through **substrate orientation and conformational control**. The two-domain α/β architecture with a flexible β-ladder hinge lets the enzyme open to admit the linear substrate and close around it, positioning it so that a spirocyclic pyrrolenine intermediate forms and ring D flips before macrocyclization. A conserved tyrosine likely initiates the chemistry by facilitating loss of the substrate hydroxyl. The failure of titratable-residue mutants to abolish catalysis is the strongest evidence that the enzyme's power derives primarily from **geometry and substrate steering** rather than from a discrete catalytic dyad or triad.

In *P. putida* KT2440 specifically, the combination of (i) an unambiguous family/domain assignment, (ii) a soluble cytoplasmic sequence signature, and (iii) a syntenic gene arrangement flanked by HemC and a downstream methyltransferase collectively establish that PP_0187 performs the canonical U3S reaction in the cytoplasm, feeding heme (primarily) and siroheme/cobalamin (secondarily). Because *P. putida* is an aerobic, non-photosynthetic organism, chlorophyll and F430 branches are not relevant here; heme for respiration and siroheme for assimilatory reductases are the physiologically meaningful downstream endpoints.

---

## Evidence Base

| PMID | Study (paraphrased) | How it supports the annotation |
|------|---------------------|--------------------------------|
| [18651750](https://pubmed.ncbi.nlm.nih.gov/18651750/) | *Structure and mechanistic implications of a uroporphyrinogen III synthase–product complex* (Schubert et al., 2008) | Defines the reaction (asymmetric cyclization → uroporphyrinogen III), reveals the two-domain flexible fold, and identifies a conserved tyrosine positioned to initiate catalysis by hydroxyl loss |
| [11689424](https://pubmed.ncbi.nlm.nih.gov/11689424/) | *Crystal structure of human uroporphyrinogen III synthase* (Mathews et al., 2001) | Specifies substrate (hydroxymethylbilane), product (uroporphyrinogen III), and pathway position (fourth enzyme); mutagenesis shows the mechanism does not require acid/base catalysis; names uroporphyrinogen III as the universal branch-point precursor for heme, siroheme, chlorophyll, F430, and B12 |
| [7842849](https://pubmed.ncbi.nlm.nih.gov/7842849/) | *The evidence for a spirocyclic intermediate in the formation of uroporphyrinogen III by cosynthase* (Leeper, 1994) | Establishes ring-D inversion and the spirocyclic pyrrolenine intermediate as the most economical catalytic mechanism |
| [18004775](https://pubmed.ncbi.nlm.nih.gov/18004775/) | *Human uroporphyrinogen III synthase: NMR-based mapping of the active site* (Cunha et al., 2008) | Identifies U3S among the cytosolic enzymes of heme biosynthesis, supporting soluble cytoplasmic localization |
| [15522295](https://pubmed.ncbi.nlm.nih.gov/15522295/) | *Structure/function of a SAM-dependent uroporphyrinogen III C-methyltransferase (SUMT)* | Characterizes the downstream branch-point enzyme (analogous to PP_0188) that consumes uroporphyrinogen III toward siroheme/B12, contextualizing HemD's product fate |
| [1548705](https://pubmed.ncbi.nlm.nih.gov/1548705/) | *Crystallization of E. coli porphobilinogen deaminase* | Characterizes the upstream enzyme (HemC/PP_0186) that produces hydroxymethylbilane, HemD's substrate |

The four core references (18651750, 11689424, 7842849, 18004775) are direct structural, mechanistic, and biochemical studies of uroporphyrinogen-III synthase itself, providing high-confidence, precise (non–high-throughput) evidence for the reaction, mechanism, and localization. The two additional references bracket HemD within its pathway by characterizing the immediately adjacent upstream and downstream activities.

A note on the human-disease literature also encountered during the investigation: several case reports (e.g., [PMID: 41428578](https://pubmed.ncbi.nlm.nih.gov/41428578/), [PMID: 41121706](https://pubmed.ncbi.nlm.nih.gov/41121706/)) concern **congenital erythropoietic porphyria (CEP)**, the human disease caused by loss-of-function mutations in *UROS* (the human ortholog of hemD). These reports confirm the essentiality and identity of the enzyme in humans but pertain to the human ortholog, not directly to the *P. putida* protein. They are consistent with — and reinforce — the functional assignment (loss of U3S activity leads to accumulation of the type-I isomer and its downstream porphyrins) but are not species-specific evidence for Q88RE4.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** All mechanistic and structural evidence derives from orthologs (human, *Thermus thermophilus*) and general biochemical studies of U3S. There is no published enzyme kinetics, crystal structure, or knockout phenotype specifically for *P. putida* KT2440 HemD (PP_0187). The assignment rests on homology, domain/family membership, sequence analysis, and synteny — strong but inferential evidence.

2. **Localization is inferred, not measured.** Cytoplasmic localization is supported by sequence features (no transmembrane helix, no signal peptide) and the universal cytosolic character of U3S enzymes, but has not been experimentally confirmed for this protein (e.g., by fractionation or fluorescent tagging).

3. **Quantitative substrate specificity unknown for this ortholog.** While the reaction (hydroxymethylbilane → uroporphyrinogen III) is certain by family assignment, kinetic parameters (Km, kcat) and any regulatory features specific to *P. putida* have not been determined.

4. **Downstream flux partitioning is unquantified.** The relative allocation of uroporphyrinogen III between the heme branch and the siroheme/cobalamin branch (via PP_0188) in *P. putida* under different growth conditions is not established.

5. **Oligomeric state.** The protein is annotated as a monomer based on sequence and size (~27 kDa), but the oligomeric state under physiological conditions in *P. putida* has not been experimentally verified.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_0187, express in *E. coli*, purify the soluble protein, and assay U3S activity by supplying hydroxymethylbilane (generated in situ from porphobilinogen using HemC) and measuring uroporphyrinogen III formation (vs. the non-enzymatic type-I product). Determine Km and kcat.

2. **Complementation test.** Test whether PP_0187 complements an *E. coli* or *P. putida* hemD-deficient strain, confirming in vivo function and essentiality.

3. **Structural determination.** Solve the crystal or cryo-EM structure of *P. putida* HemD, ideally as a product complex, to verify the two-domain fold, the conserved tyrosine, and the substrate-orienting active-site geometry inferred from orthologs.

4. **Subcellular localization.** Confirm cytoplasmic localization by cell fractionation or fluorescent-protein fusion imaging.

5. **Pathway flux analysis.** Use metabolic labeling or targeted metabolomics under aerobic/anaerobic and sulfur-/nitrogen-limited conditions to quantify how uroporphyrinogen III is partitioned between heme and siroheme/cobalamin branches, clarifying HemD's physiological output in *P. putida*.

6. **Mutagenesis of the conserved tyrosine.** Mutate the tyrosine predicted to initiate catalysis (by homology to the *T. thermophilus* structure) and measure the effect on activity and isomer specificity, testing the substrate-orienting mechanistic model directly in this ortholog.

---

## Conclusion

HemD / PP_0187 / Q88RE4 of *Pseudomonas putida* KT2440 is confidently identified as **uroporphyrinogen-III synthase (EC 4.2.1.75)**, the fourth enzyme of the tetrapyrrole/heme biosynthetic pathway. It is a **soluble cytoplasmic ~27 kDa monomer** that catalyzes the **asymmetric cyclization of hydroxymethylbilane to uroporphyrinogen III with inversion of ring D**, producing the type-III isomer that is the universal precursor of all cellular tetrapyrroles. The mechanism is best explained by **substrate orientation and a spirocyclic pyrrolenine intermediate** rather than classical acid/base catalysis, aided by a conserved active-site tyrosine. In *P. putida*, its product primarily feeds **heme** biosynthesis, with a secondary route (via the neighboring methyltransferase PP_0188) toward **siroheme and cobalamin**. The gene assignment is corroborated by convergent evidence from protein family/domain signatures, sequence-based localization analysis, database reaction annotations, and genomic synteny with its substrate-supplying (HemC/PP_0186) and product-consuming (PP_0188) neighbors.


## Artifacts

- [OpenScientist final report](hemD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18651750
2. PMID:11689424
3. PMID:7842849
4. PMID:18004775
5. PMID:41428578
6. PMID:41121706