---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:16:06.533020'
end_time: '2026-08-19T07:50:00.480154'
duration_seconds: 2033.95
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0747
  gene_symbol: PP_0747
  uniprot_accession: Q88PV1
  protein_description: 'SubName: Full=Hypoxanthine-guanine phosphoribosyltransferase
    {ECO:0000313|EMBL:AAN66372.1};'
  gene_info: OrderedLocusNames=PP_0747 {ECO:0000313|EMBL:AAN66372.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: HGPRT. (IPR050408); PRTase-like. (IPR029057); PRTase_dom. (IPR000836);
    Pribosyltran (PF00156)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0747-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0747-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PV1
- **Protein Description:** SubName: Full=Hypoxanthine-guanine phosphoribosyltransferase {ECO:0000313|EMBL:AAN66372.1};
- **Gene Information:** OrderedLocusNames=PP_0747 {ECO:0000313|EMBL:AAN66372.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** HGPRT. (IPR050408); PRTase-like. (IPR029057); PRTase_dom. (IPR000836); Pribosyltran (PF00156)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0747" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0747' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0747** (gene ID: PP_0747, UniProt: Q88PV1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_0747 (Q88PV1) — Hypoxanthine–Guanine Phosphoribosyltransferase of *Pseudomonas putida* KT2440

## Summary

**PP_0747** (UniProt **Q88PV1**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950; taxon PSEPK) encodes a **hypoxanthine–guanine phosphoribosyltransferase (HGPRT; EC 2.4.2.8)**, a soluble, cytosolic enzyme of the **purine salvage pathway**. Its primary catalytic role is the Mg²⁺-dependent transfer of the 5-phosphoribosyl group from **5-phospho-α-D-ribose 1-diphosphate (PRPP)** to the free 6-oxopurine bases **hypoxanthine** and **guanine**, generating **inosine 5′-monophosphate (IMP)** and **guanosine 5′-monophosphate (GMP)**, respectively, with release of inorganic pyrophosphate (PPi). This recycling of preformed purine bases into the nucleotide pool spares the energetically costly *de novo* purine biosynthetic route.

The molecular identity of PP_0747 is **unambiguous and internally consistent** across every major annotation resource. It is a compact 185-residue protein built on a single Pfam PF00156 (Pribosyltran) domain within the Rossmann-like phosphoribosyltransferase (PRTase) fold, carries the diagnostic tandem-aspartate PRPP-binding signature of the 6-oxopurine PRTase family, and is assigned to KEGG orthology **K00760** (HGPRT) and orthologous group **COG0634**. Comparative genomics of the KT2440 genome shows that PP_0747 is the **sole 6-oxopurine phosphoribosyltransferase** encoded by the organism — there is no separate xanthine-guanine PRT (*gpt*) or xanthine PRT (*xpt*) — so it functions as the single physiological gateway for salvaging both hypoxanthine and guanine. Adenine salvage is handled by a distinct enzyme, adenine phosphoribosyltransferase (*apt*/PP_4266, EC 2.4.2.7).

Mechanistically, PP_0747 is expected to follow the well-established HGPRT catalytic paradigm derived from crystallographic and kinetic studies of orthologs: an **ordered sequential mechanism** in which Mg-PRPP binds the free enzyme before the purine base, followed by an SN1-like (dissociative) ribosyl transfer through an oxocarbenium-like transition state, using **two Mg²⁺ ions** to orient and activate the PRPP pyrophosphate for in-line nucleophilic attack by the purine N9. Ordered product release (PPi before the nucleotide monophosphate) completes the cycle. It should be emphasized that **no enzyme-specific biochemical or structural study of the KT2440 protein itself has yet been published**; the functional assignment rests on concordant database annotation, conserved sequence motifs, genome context, and strong homology to experimentally characterized HGPRTs.

---

## Identity Verification (Mandatory Check)

All verification criteria are satisfied — this is a **genuine HGPRT**, not a same-symbol mismatch:

| Criterion | Finding |
|---|---|
| Gene symbol ↔ protein description | PP_0747 is annotated "Hypoxanthine-guanine phosphoribosyltransferase" in UniProt (Q88PV1), KEGG (ppu:PP_0747), and NCBI (AAN66372.1) — consistent. |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) — correct. |
| Domain architecture | Pfam **PF00156** (Pribosyltran); InterPro **IPR000836/IPR029057/IPR050408**; SCOP **SSF53271**; Gene3D **3.40.50.2020**; orthology **COG0634**, **PANTHER PTHR43340**. All consistent with a 6-oxopurine PRTase. |
| Diagnostic motif | 6-oxopurine-PRTase PRPP-binding signature with tandem-Asp (DD) motif present: `…LIVDDILDEG…` at residues ~104–113. |
| Length / features | 185 aa (~20.5 kDa); single catalytic domain; no signal peptide or transmembrane segment → soluble cytoplasmic protein. |

**Conclusion:** No literature conflict or symbol ambiguity was encountered. The protein is a canonical bacterial HGPRT.

---

## Key Findings

### Finding 1 — PP_0747 is a genuine hypoxanthine–guanine phosphoribosyltransferase (EC 2.4.2.8)

UniProt Q88PV1 describes the KT2440 locus PP_0747 as a 185-amino-acid HGPRT annotated with **two catalytic-activity reactions**, both under EC 2.4.2.8:

- hypoxanthine + PRPP → IMP + PPi (**RHEA:17973**)
- guanine + PRPP → GMP + PPi (**RHEA:25424**)

The domain architecture is fully consistent with this assignment: Pfam **PF00156 (Pribosyltran)**, InterPro **IPR000836 (PRTase_dom)**, **IPR029057 (PRTase-like)**, and **IPR050408 (HGPRT)**, together with SCOP superfamily **SSF53271** and Gene3D **3.40.50.2020**, all describing the Rossmann-like PRT fold. Orthology assignments (COG0634; PANTHER **PTHR43340**, "HGPRT") reinforce family membership. Critically, the **diagnostic 6-oxopurine-PRTase PRPP-binding signature** — the tandem-Asp "DD" motif (…LIVDDILDEG…) — is present at approximately residues 104–113, confirming at the sequence level that the PRPP-binding site is intact and of the H(X)GPRT type. There is **no evidence of a same-symbol conflict**; the ordered locus name, protein description, domain content, and organism all agree.

This assignment matches the canonical definition of the enzyme. As stated for the *Legionella pneumophila* ortholog: "*Hypoxanthine-guanine phosphoribosyltransferase (HGPRT) (EC 2.4.2.8) reversibly catalyzes the transfer of the 5-phophoribosyl group from 5-phosphoribosyl-alpha-1-pyrophosphate (PRPP) to hypoxanthine or guanine to form inosine monophosphate (IMP) or guanosine monophosphate (GMP) in the purine salvage pathway*" [PMID: 26968365](https://pubmed.ncbi.nlm.nih.gov/26968365/). This defines the EC number, both substrates, both products, and the pathway — exactly matching the two Rhea reactions annotated for Q88PV1.

### Finding 2 — Catalysis proceeds by an ordered sequential, two-metal-ion mechanism

Structural and kinetic work across HGPRT orthologs establishes a **sequential kinetic mechanism** in which PRPP binds the free enzyme prior to the base. For free human HGPRT: "*The mechanism is sequential, with PRib-PP binding to the free enzyme prior to the base*" [PMID: 15990111](https://pubmed.ncbi.nlm.nih.gov/15990111/). Catalysis proceeds through an SN1-like ribosyl transfer with ordered product release (PPi first, then the nucleotide monophosphate).

The hallmark of the 6-oxopurine (HGPRT-class) PRTases is the use of **two Mg²⁺ ions** to orient and activate the PRPP pyrophosphate. A high-resolution *Toxoplasma gondii* ternary complex "*shows how HGPRT uses two Mg(2+) ions to orient and activate the pyrophosphate moiety of PRPP for attack by a purine base*" [PMID: 10545171](https://pubmed.ncbi.nlm.nih.gov/10545171/). This two-metal strategy is diagnostic and distinguishes HGPRTs from adenine PRTases, which use a single Mg²⁺ plus an active-site arginine ([PMID: 12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/)). The Mg²⁺-binding annotation carried by Q88PV1 is consistent with this mechanism. Atomic-resolution ternary complexes further show catalysis is aided by **substrate deformation** (an unusual C2′-endo pucker of the PRPP ribose) and a **cation-π interaction** between an active-site tyrosine and the developing ribosyl oxocarbenium ion, stabilizing the transition state ([PMID: 11188695](https://pubmed.ncbi.nlm.nih.gov/11188695/)).

Because PP_0747 shares the conserved fold, the PRPP-binding DD motif, and the Mg²⁺-binding annotation, it is expected to operate by this same ordered, two-metal-ion mechanism.

### Finding 3 — PP_0747 is a soluble cytosolic "group I" 6-oxopurine PRTase within a gene-duplication-derived superfamily

The Gene Ontology annotation for Q88PV1 places the protein in the **cytosol (GO:0005829)**. Its small size (185 aa), single PF00156 domain, and absence of any signal peptide or transmembrane segment are consistent with a **soluble intracellular enzyme** carrying out catalysis in the cytoplasm — the compartment where PRPP and free purine bases are available.

Structurally, compact bacterial HGPRTs of this type correspond to the defined **"group I"** 6-oxopurine PRTases. As described for the *Thermus thermophilus* HB8 enzyme: "*these enzymes can be tentatively divided into groups I and II and that the T. thermophilus HB8 enzyme belongs to group I. The group II enzymes are characterized by an N-terminal extension with additional secondary elements*" [PMID: 20693661](https://pubmed.ncbi.nlm.nih.gov/20693661/). PP_0747's single-domain architecture with no N-terminal extension places it squarely in **group I**.

Evolutionarily, PP_0747 belongs to a broad, homologous PRTase superfamily that diverged by gene duplication, with substrate specificity as the principal divergent trait. The purine PRTases — "*adenine-, xanthine-, hypoxanthine- and guanine-phosphoribosyltransferases, which are all homologous among themselves, as well as to nucleoside phosphorylases*" [PMID: 9742728](https://pubmed.ncbi.nlm.nih.gov/9742728/) — share a common ancestor. This explains both the family membership of PP_0747 and the origin of the distinct adenine PRTase (*apt*) that handles the complementary salvage reaction in the same organism.

### Finding 4 — PP_0747 is the sole 6-oxopurine PRTase in KT2440, salvaging both hypoxanthine and guanine

KEGG assigns PP_0747 to KO **K00760** (hypoxanthine phosphoribosyltransferase, EC 2.4.2.8) within pathway **ppu00230 (Purine metabolism)** / **ppu01232 (Nucleotide metabolism)**, at CDS coordinates 865988..866545. Enumerating all purine-PRTase KOs across the KT2440 genome demonstrates that PP_0747 (K00760) is the **only 6-oxopurine PRTase present**:

| Salvage enzyme | KO | EC | Locus in KT2440 | Present? |
|---|---|---|---|---|
| Hypoxanthine-guanine PRT (*hpt*) | K00760 | 2.4.2.8 | **PP_0747** | ✅ Yes |
| Xanthine-guanine PRT (*gpt*) | K00769 | 2.4.2.22 | — | ❌ Absent |
| Xanthine PRT (*xpt*) | K02428 | 2.4.2.22 | — | ❌ Absent |
| Adenine PRT (*apt*) | K00759 | 2.4.2.7 | PP_4266 | ✅ Yes (adenine only) |

Because no separate *gpt* or *xpt* gene exists, PP_0747 must handle salvage of **both** hypoxanthine and guanine — consistent with the two catalytic reactions annotated for Q88PV1 and with a broad-specificity HGPRT. Adenine salvage is functionally partitioned to the distinct enzyme *apt*/PP_4266. This genomic "single-gateway" arrangement mirrors the salvage architecture seen in halophilic archaea, where "*A single phosphoribosyltransferase seemed to convert guanine as well as hypoxanthine to nucleoside monophosphates, and another phosphoribosyltransferase had specificity towards adenine*" [PMID: 9457844](https://pubmed.ncbi.nlm.nih.gov/9457844/).

### Finding 5 — Genetic evidence confirms hpt-type HGPRT physiologically salvages purine bases and activates cytotoxic base analogs

The physiological salvage role of *hpt*-type HGPRTs is supported by classical bacterial genetics. In *Escherichia coli*, loss of HPRT (*hpt*) and guanine-PRT (*gpt*) confers **resistance to the purine base analog 6-mercaptopurine**, demonstrating that these enzymes normally phosphoribosylate incoming purine bases — and their cytotoxic analogs — using PRPP. As reported: "*Mutants resistant to 6-mercaptopurine were found to have defects in HPRT, the purR repressor, or in both*" [PMID: 6787390](https://pubmed.ncbi.nlm.nih.gov/6787390/). The same study shows that an *hpt⁻ gpt⁻* double mutant becomes hypersensitive to adenine, and that base-salvage flux through these PRTases governs the intracellular purine nucleotide balance. This genetic logic — a salvage enzyme whose loss confers analog resistance — provides functional confirmation of the class of enzyme to which PP_0747 belongs.

---

## Mechanistic Model / Interpretation

### The reaction and its place in metabolism

PP_0747 catalyzes the committed salvage step for 6-oxopurines:

```
                       PP_0747 (HGPRT, EC 2.4.2.8)
   Hypoxanthine  +  PRPP  ───────────────────────────►  IMP  +  PPi
                              (Mg²⁺ × 2)

   Guanine       +  PRPP  ───────────────────────────►  GMP  +  PPi
                              (Mg²⁺ × 2)
```

IMP produced from hypoxanthine is the central branch-point purine nucleotide, feeding into both AMP (via adenylosuccinate) and GMP (via XMP) synthesis, while GMP produced directly from guanine enters the guanylate pool. By recovering preformed bases, PP_0747 spares the ~6-step, ATP-intensive *de novo* purine pathway (~6–7 ATP equivalents per IMP).

### Catalytic cycle (ordered sequential, two-metal)

```
  E (free)
    │  + Mg·PRPP        ← binds first (Finding 2)
    ▼
  E·Mg·PRPP
    │  + purine base (hypoxanthine / guanine)
    ▼
  E·Mg·PRPP·base  ──►  [oxocarbenium-like transition state]
    │                    • in-line attack of purine N9 on ribose C1'
    │                    • two Mg²⁺ orient/activate the PPi leaving group
    │                    • cation-π (Tyr) stabilizes the TS
    ▼
  E·NMP·PPi
    │  – PPi   (released first)
    ▼
  E·NMP
    │  – IMP / GMP
    ▼
  E (free)
```

This scheme is the consensus HGPRT mechanism assembled from ternary-complex crystallography and steady-state kinetics of orthologs ([PMID: 15990111](https://pubmed.ncbi.nlm.nih.gov/15990111/); [PMID: 10545171](https://pubmed.ncbi.nlm.nih.gov/10545171/); [PMID: 11188695](https://pubmed.ncbi.nlm.nih.gov/11188695/)). HGPRTs are functional **homodimers**, and interactions near the dimer interface (e.g., active-site loop I) modulate the balance between forward nucleotide synthesis and reverse pyrophosphorolysis ([PMID: 14698288](https://pubmed.ncbi.nlm.nih.gov/14698288/)); PP_0747 is expected to oligomerize similarly, though this has not been experimentally verified for the KT2440 protein.

### Localization and pathway context

PP_0747 acts in the **cytosol** (GO:0005829), the compartment containing its co-substrate PRPP and the free purine bases arising from nucleic-acid turnover and, in an environmentally versatile soil bacterium such as *P. putida*, potentially from exogenous purine uptake. Within KEGG purine metabolism (ppu00230), it occupies the salvage node converting free 6-oxopurine bases to nucleotide monophosphates, complementary to (and independent of) the adenine-salvage enzyme *apt*/PP_4266.

### Substrate specificity: why "hypoxanthine-guanine"

The 6-oxopurine PRTase family shows a specificity spectrum controlled by a few active-site residues. Strict xanthine PRTases of Gram-positive bacteria use residues such as Asn27 and Lys156 to recognize xanthine and react only weakly (~10⁴-fold lower efficiency) with guanine and hypoxanthine ([PMID: 16716072](https://pubmed.ncbi.nlm.nih.gov/16716072/)), whereas the *Giardia* GPRTase is uniquely guanine-specific ([PMID: 8813688](https://pubmed.ncbi.nlm.nih.gov/8813688/)). PP_0747, carrying the canonical H(X)GPRT PRPP-binding motif and being the organism's only 6-oxopurine PRTase, is expected to accept both hypoxanthine and guanine — a broad specificity that is metabolically necessary given the absence of a dedicated *gpt*/*xpt* gene in KT2440.

---

## Evidence Base

| PMID | Organism / topic | How it supports this report |
|---|---|---|
| [26968365](https://pubmed.ncbi.nlm.nih.gov/26968365/) | *Legionella pneumophila* HGPRT | Canonical EC 2.4.2.8 definition — substrates, products, pathway (Finding 1) |
| [15990111](https://pubmed.ncbi.nlm.nih.gov/15990111/) | Human HGPRT (free enzyme) | Ordered sequential mechanism, PRPP binds before base (Finding 2) |
| [10545171](https://pubmed.ncbi.nlm.nih.gov/10545171/) | *Toxoplasma gondii* HGPRT | Two-Mg²⁺ catalytic strategy (Finding 2) |
| [11188695](https://pubmed.ncbi.nlm.nih.gov/11188695/) | *T. gondii* HGPRT ternary complex | Substrate deformation + cation-π TS stabilization |
| [14698288](https://pubmed.ncbi.nlm.nih.gov/14698288/) | *Trypanosoma cruzi* HPRT | Dimer-interface residues tune synthesis vs pyrophosphorolysis |
| [20693661](https://pubmed.ncbi.nlm.nih.gov/20693661/) | *Thermus thermophilus* HGPRT | Group I vs II classification; PP_0747 = group I (Finding 3) |
| [9742728](https://pubmed.ncbi.nlm.nih.gov/9742728/) | Purine PRTase evolution | Gene-duplication origin & homology of purine PRTases (Finding 3) |
| [6787390](https://pubmed.ncbi.nlm.nih.gov/6787390/) | *E. coli hpt gpt* genetics | Physiological salvage role; analog activation/resistance (Finding 5) |
| [9457844](https://pubmed.ncbi.nlm.nih.gov/9457844/) | Halophilic archaea salvage | Single PRT for guanine+hypoxanthine, separate adenine PRT (Finding 4) |
| [16716072](https://pubmed.ncbi.nlm.nih.gov/16716072/) | *B. subtilis* XPRTase | Specificity determinants across 6-oxopurine PRTases |
| [12171925](https://pubmed.ncbi.nlm.nih.gov/12171925/) | *Giardia* APRTase | Single-Mg²⁺ APRT contrasts two-Mg²⁺ HGPRT (mechanistic contrast) |
| [8813688](https://pubmed.ncbi.nlm.nih.gov/8813688/) | *Giardia* GPRTase | Extreme guanine specificity example |
| [31160323](https://pubmed.ncbi.nlm.nih.gov/31160323/) | Human APRT | Shape-vs-base specificity; family context |
| [27479359](https://pubmed.ncbi.nlm.nih.gov/27479359/) | *P. falciparum* HGXPRT | Loop dynamics / hood closure in catalysis |

**Consistency check:** every line of evidence — UniProt/Rhea reactions, KEGG KO, InterPro/Pfam domains, COG/PANTHER orthology, the conserved DD PRPP-binding motif, cytosolic GO term, and genome-wide PRTase enumeration — converges on the same conclusion with no contradictions. The critical identity-verification requirement is satisfied: gene symbol, protein description, organism, and domain content all match, and no conflicting same-symbol literature was found.

---

## Supported and Refuted Hypotheses

**Supported:**
- PP_0747 is a genuine HGPRT (EC 2.4.2.8) — supported by concordant UniProt/KEGG/InterPro annotation, the diagnostic DD motif, and family literature.
- It catalyzes salvage of hypoxanthine and guanine using Mg·PRPP to form IMP and GMP — supported by UniProt Rhea reactions and mechanistic literature.
- It is a soluble cytosolic enzyme — supported by GO annotation and absence of localization signals.
- It is the sole 6-oxopurine PRTase in KT2440 (broad hypoxanthine+guanine role) — supported by genome-wide KO enumeration.

**Refuted / ruled out:**
- The gene is **not** ambiguous and does **not** correspond to an unrelated same-symbol gene.
- PP_0747 is **not** an adenine PRT (that role belongs to *apt*/PP_4266) and is **not** a dedicated xanthine PRT.

---

## Limitations and Knowledge Gaps

1. **No protein-specific experimental characterization.** There is, to date, no published biochemical or structural study of the KT2440 PP_0747 protein itself — no purified-enzyme kinetics (kcat, Km for hypoxanthine, guanine, PRPP, Mg²⁺), no crystal structure, and no direct activity assay. All mechanistic and specificity statements are **inferred** from orthologs and conserved motifs.
2. **Specificity toward xanthine is untested.** Whether PP_0747 has measurable xanthine PRTase activity (making it an HGXPRT rather than a strict HGPRT) is unknown. Given the absence of a dedicated *gpt/xpt* gene, low-level xanthine salvage by PP_0747 is plausible but unverified.
3. **Quaternary structure unconfirmed.** HGPRTs are typically homodimers/tetramers; the oligomeric state of PP_0747 has not been experimentally determined.
4. **Physiological/genetic role in *P. putida* not directly demonstrated.** No knockout, complementation, or purine-analog-resistance phenotype has been reported specifically for PP_0747 in KT2440. The salvage role is inferred from genome context and *E. coli* genetics.
5. **Regulation and flux unknown.** Expression control, feedback by nucleotide pools, and the quantitative contribution of PP_0747-mediated salvage vs. de novo synthesis in KT2440 remain uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone PP_0747, express in *E. coli*, purify, and measure activity with hypoxanthine, guanine, and xanthine, determining kcat and Km for each base plus PRPP and the Mg²⁺ dependence, using an IMP/GMP-formation or coupled PPi-release assay to confirm EC 2.4.2.8 activity and map the specificity spectrum.
2. **Genetic knockout and analog-resistance test.** Construct a ΔPP_0747 mutant and test (a) growth on hypoxanthine/guanine as purine sources in a *de novo*-blocked background, and (b) resistance to 6-mercaptopurine / 6-thioguanine. Following the *E. coli* logic ([PMID: 6787390](https://pubmed.ncbi.nlm.nih.gov/6787390/)), loss of analog toxicity would confirm the physiological salvage role.
3. **Structural determination.** Solve the crystal structure (or validate a high-confidence AlphaFold model against homologs), ideally as a ternary complex with Mg-PRPP and a 9-deazapurine analog, to confirm the two-metal active site, DD motif geometry, and specificity-determining residues.
4. **Oligomeric-state analysis.** Use SEC-MALS or analytical ultracentrifugation to establish the dimeric/tetrameric assembly expected for this family.
5. **Complementation assay.** Test whether cloned PP_0747 rescues an *E. coli hpt gpt* double mutant for growth on guanine and hypoxanthine — a rapid in vivo confirmation of dual specificity.
6. **Metabolic-flux context.** Quantify salvage vs. de novo contributions using ¹³C/¹⁵N-labeled purine bases and LC-MS nucleotide-pool measurements in wild-type vs. ΔPP_0747 KT2440.

---

## Conclusion

PP_0747 (Q88PV1) is the **hypoxanthine–guanine phosphoribosyltransferase** of *Pseudomonas putida* KT2440 — a soluble cytosolic purine-salvage enzyme that uses Mg²⁺ and PRPP to convert the free 6-oxopurine bases hypoxanthine and guanine into IMP and GMP via an ordered, two-metal-ion sequential mechanism. It is the organism's **sole 6-oxopurine PRTase**, making it the principal cytoplasmic gateway that recycles hypoxanthine and guanine into the purine nucleotide pool, with adenine salvage handled separately by *apt*/PP_4266. The functional assignment is robustly supported by concordant database annotation, the diagnostic tandem-Asp PRPP-binding motif, genome context, and homology to structurally characterized HGPRTs — although enzyme-specific biochemical and structural validation of this particular protein remains to be performed.


## Artifacts

- [OpenScientist final report](PP_0747-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0747-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26968365
2. PMID:15990111
3. PMID:10545171
4. PMID:12171925
5. PMID:11188695
6. PMID:20693661
7. PMID:9742728
8. PMID:9457844
9. PMID:6787390
10. PMID:14698288
11. PMID:16716072
12. PMID:8813688