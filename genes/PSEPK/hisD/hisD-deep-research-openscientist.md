---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:40:51.597726'
end_time: '2026-07-17T05:57:08.477380'
duration_seconds: 976.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hisD
  gene_symbol: hisD
  uniprot_accession: P59400
  protein_description: 'RecName: Full=Histidinol dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01024};
    Short=HDH {ECO:0000255|HAMAP-Rule:MF_01024}; EC=1.1.1.23 {ECO:0000255|HAMAP-Rule:MF_01024};'
  gene_info: Name=hisD {ECO:0000255|HAMAP-Rule:MF_01024}; OrderedLocusNames=PP_0966;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the histidinol dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Histidinol_DH_CS. (IPR001692);
    Histidinol_DH_monofunct. (IPR022695); Hstdl_DH. (IPR012131); Histidinol_dh (PF00815)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hisD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hisD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P59400
- **Protein Description:** RecName: Full=Histidinol dehydrogenase {ECO:0000255|HAMAP-Rule:MF_01024}; Short=HDH {ECO:0000255|HAMAP-Rule:MF_01024}; EC=1.1.1.23 {ECO:0000255|HAMAP-Rule:MF_01024};
- **Gene Information:** Name=hisD {ECO:0000255|HAMAP-Rule:MF_01024}; OrderedLocusNames=PP_0966;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the histidinol dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Histidinol_DH_CS. (IPR001692); Histidinol_DH_monofunct. (IPR022695); Hstdl_DH. (IPR012131); Histidinol_dh (PF00815)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hisD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hisD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hisD** (gene ID: hisD, UniProt: P59400) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hisD* (PP_0966, UniProt P59400) in *Pseudomonas putida* KT2440

## Summary

**HisD (UniProt P59400, ordered locus PP_0966) of *Pseudomonas putida* strain KT2440 is L-histidinol dehydrogenase (HDH; EC 1.1.1.23), the enzyme that catalyzes the final, committed step of de novo L-histidine biosynthesis.** The gene symbol *hisD*, the protein description, the organism, and the protein-family/domain signatures supplied in the research brief are all mutually consistent and were confirmed at every level of evidence examined: HAMAP rule MF_01024, InterPro IPR022695 (monofunctional histidinol dehydrogenase), Pfam PF00815, KEGG ortholog K00013, and curated UniProt residue-level annotations all converge on the same assignment. There is no gene-symbol ambiguity for this target — *hisD* is a conserved, near-universally distributed housekeeping gene of amino-acid metabolism.

In a single active site, HisD performs an unusual **four-electron oxidation** of the amino alcohol L-histidinol to the amino acid L-histidine, proceeding through a bound L-histidinaldehyde intermediate and reducing two molecules of NAD⁺. This is formally the last two chemical steps of the histidine pathway (histidinol → histidinaldehyde → histidine) executed by one enzyme without releasing the aldehyde intermediate. The enzyme is a **homodimeric Zn²⁺ metalloenzyme**, carrying one Zn²⁺ cation per monomer that is required for substrate binding rather than for the redox chemistry itself. Catalysis proceeds by general acid-base chemistry involving conserved active-site histidine residues and a glutamate that activates a catalytic water molecule, with hydride transfer to NAD⁺.

The functionally characterized residues from the well-studied *Escherichia coli* and *Salmonella* orthologs map with exact conservation onto the *P. putida* sequence (E. coli Glu326/His327/His262/His419 → P. putida Glu333/His334/His268/His426), and these assignments are independently corroborated by curated UniProt features for P59400. The enzyme is cytoplasmic (no signal peptide or transmembrane segment), and its gene lies in a co-oriented *hisG–hisD–hisC* cluster in the KT2440 chromosome, consistent with the operonic organization typical of bacterial histidine-biosynthesis genes. In short, HisD/PP_0966 is a soluble cytoplasmic biosynthetic oxidoreductase that funnels the histidine pathway to its final product, and its mechanism, cofactor requirements, and catalytic residues are established by convergent structural, enzymological, bioinformatic, and genomic evidence.

## Gene/Protein Identity Verification

Before presenting the functional analysis, the mandatory identity checks from the research brief were completed and **all passed**:

| Verification step | Result |
|---|---|
| Does gene symbol "hisD" match the protein description (histidinol dehydrogenase)? | **Yes** — *hisD* is the canonical symbol for histidinol dehydrogenase across bacteria. |
| Is the organism correct (*P. putida* KT2440)? | **Yes** — PP_0966 is the KT2440 ordered locus name; KEGG organism code `ppu`. |
| Do the protein family/domains align with the literature? | **Yes** — Pfam PF00815 (Histidinol_dh), InterPro IPR022695/IPR001692/IPR016161/IPR012131, HAMAP MF_01024 all denote histidinol dehydrogenase. |
| Any conflicting literature for a different gene with the same symbol? | **No** — *hisD* is unambiguous in this context. |

The gene symbol is **not** ambiguous, and the literature for histidinol dehydrogenase is directly applicable to P59400.

## Key Findings

### Finding 1 — HisD is L-histidinol dehydrogenase, catalyzing the terminal four-electron oxidation of the histidine pathway

HisD (P59400, PP_0966) is assigned EC 1.1.1.23 and belongs to the histidinol dehydrogenase family (HAMAP rule MF_01024; InterPro IPR022695, monofunctional histidinol DH). The enzyme catalyzes the **last two steps** of L-histidine biosynthesis as a single, coupled transformation: two sequential NAD⁺-dependent oxidations of one substrate, L-histidinol → L-histidinaldehyde → L-histidine. Because the aldehyde is an obligatory intermediate that is not released, the overall reaction is an **unusual four-electron oxidation of an amino alcohol to an amino acid**, consuming two molecules of NAD⁺ at a single active site.

This mechanism is not merely inferred from sequence — it is established by two independent enzymological/structural studies of orthologous enzymes. The *E. coli* crystallographic study states explicitly that "*l-histidinol dehydrogenase (HisD, EC ) catalyzes the last two steps in the biosynthesis of l-histidine: sequential NAD-dependent oxidations of l-histidinol to l-histidinaldehyde and then to l-histidine*" ([PMID: 11842181](https://pubmed.ncbi.nlm.nih.gov/11842181/)). The *Salmonella* mutagenesis study independently describes an enzyme that "*catalyzes an unusual four-electron oxidation of the amino alcohol histidinol via the histidinaldehyde intermediate to the acid product histidine with the reduction of two molecules of NAD*" ([PMID: 10353848](https://pubmed.ncbi.nlm.nih.gov/10353848/)). The overall balanced reaction annotated for P59400 by UniProt — L-histidinol + 2 NAD⁺ + H₂O = L-histidine + 2 NADH + 3 H⁺ — matches this description exactly.

**Substrate specificity:** the substrate is L-histidinol (with L-histidinaldehyde as the bound intermediate); the cosubstrate/electron acceptor is NAD⁺; the product is L-histidine. This is a highly specific biosynthetic enzyme with a dedicated substrate-binding pocket (see Finding 6).

### Finding 2 — HisD is a homodimeric Zn²⁺ metalloenzyme; the metal supports substrate binding, not catalysis

Crystal structures of *E. coli* HisD — solved in apo form and in complexes with substrate, Zn²⁺, and NAD⁺ (best resolution 1.7 Å) — reveal an **intertwined homodimer** that "*requires the presence of one Zn(2+) cation per monomer*" ([PMID: 11842181](https://pubmed.ncbi.nlm.nih.gov/11842181/)). Critically, the same study demonstrates that "*Zn(2+) plays a crucial role in substrate binding but is not directly involved in catalysis*" — an important mechanistic distinction from classic zinc-dependent alcohol dehydrogenases, where the metal polarizes the substrate carbonyl. In HisD, the zinc instead organizes the substrate-binding pocket.

The identity of the zinc ligands was probed by mutagenesis in the *Salmonella* enzyme, where analysis of chelator sensitivity and reduced metal affinity upon substitution "*suggested that these two residues (His-261 and His-418) are candidates for zinc ion ligands*" ([PMID: 10353848](https://pubmed.ncbi.nlm.nih.gov/10353848/)). UniProt independently annotates Zn²⁺ as a cofactor of P59400. The homodimeric, one-Zn²⁺-per-monomer architecture is therefore expected to be preserved in the *P. putida* enzyme.

### Finding 3 — Acid-base catalysis at a shared dimer interface; the fold reflects ancient gene duplication

The chemistry of HisD proceeds by general acid-base catalysis, with conserved residues contributed to each active site by **both monomers** of the dimer. In *E. coli* HisD, "*the active site residue His-327 participates in acid-base catalysis, whereas Glu-326 activates a water molecule*" ([PMID: 11842181](https://pubmed.ncbi.nlm.nih.gov/11842181/)) — the water being required for the hydration/oxidation of the aldehyde intermediate to the carboxylic acid. Kinetic dissection in *Salmonella* quantified the catalytic weight of these residues: "*Substitution of His-261 and His-326 by asparagine caused about 7000- and 500-fold decreases in kcat, respectively, with little change in KM values*" ([PMID: 10353848](https://pubmed.ncbi.nlm.nih.gov/10353848/)). The small change in KM with a large change in kcat pinpoints these histidines as catalytic (proton-transfer) rather than binding residues; complementary isotope, pH, and stopped-flow data implicate an essential base of pKa ~8.

Structurally, each monomer comprises four domains, and the enzyme carries **two incomplete Rossmann-fold domains** — "*Two domains display a very similar incomplete Rossmann fold that suggests an ancient event of gene duplication*" ([PMID: 11842181](https://pubmed.ncbi.nlm.nih.gov/11842181/)). The intertwined dimer arises by domain swapping, which is why catalytically competent active sites are only assembled at the dimer interface. These conserved motifs are captured by InterPro IPR001692 (Histidinol_DH_CS) and Pfam PF00815, both of which are present in P59400 — providing the bioinformatic bridge from the characterized enzymes to the *P. putida* protein.

### Finding 4 — Catalytic and Zn-binding residues are conserved in the *P. putida* enzyme

A global pairwise alignment of P59400 (441 aa) against *E. coli* HisD (P06988, 434 aa) yields **43.4% identity**, with exact conservation of every functionally characterized residue. The mapping is:

| Function | *E. coli* (P06988) | *Salmonella* equivalent | *P. putida* (P59400) |
|---|---|---|---|
| Catalytic Glu (activates water) | Glu326 | — | **Glu333** |
| Catalytic His (acid-base / proton transfer) | His327 | His326 | **His334** |
| Zn ligand / proton-transfer His | His262 | His261 | **His268** |
| Zn ligand His | His419 | His418 | **His426** |

This one-to-one residue conservation across a >40%-identity alignment is strong evidence that the *P. putida* enzyme uses the identical catalytic machinery. UniProt P59400 independently annotates: the reaction "L-histidinol + 2 NAD⁺ + H₂O = L-histidine + 2 NADH + 3 H⁺"; cofactor Zn²⁺; the pathway assignment "L-histidine biosynthesis from PRPP, final step (9/9)"; and keywords Oxidoreductase / NAD / Zinc / Metal-binding. Importantly, **no signal peptide and no transmembrane feature** are present, consistent with a soluble cytoplasmic enzyme.

### Finding 5 — *hisD* (PP_0966) lies in a co-oriented *hisG–hisD–hisC* cluster in the KT2440 chromosome

KEGG genomic annotation for organism `ppu` places three consecutive, **same-strand** histidine-biosynthesis genes around the PP_0966 locus:

| Locus | Gene | Enzyme (EC) | KEGG ortholog | Coordinates | Pathway role |
|---|---|---|---|---|---|
| PP_0965 | *hisG* | ATP phosphoribosyltransferase (2.4.2.17) | K00765 | 1104599..1105234 | First / committed step |
| PP_0966 | *hisD* | Histidinol dehydrogenase (1.1.1.23) | K00013 | 1105521..1106846 | **Final step (this gene)** |
| PP_0967 | *hisC* | Histidinol-phosphate aminotransferase (2.6.1.9) | K00817 | 1106849..1107895 | Transamination step |

*hisD* and *hisC* are separated by only **3 bp** (stop at 1106846, next start at 1106849), indicative of translational coupling within an operon. The flanking genes PP_0964 (*murA*) and PP_0968–PP_0970 are unrelated to histidine biosynthesis, defining the local boundary of the *his* cluster. KEGG assigns PP_0966 to pathway **ppu00340** (Histidine metabolism) and module **M00026** (Histidine biosynthesis, PRPP ⇒ histidine). This genomic context reinforces the functional assignment: a gene physically embedded among the first and intermediate his-pathway enzymes and encoding the last-step enzyme is exactly what is expected for a bona fide histidine biosynthetic operon.

### Finding 6 — Curated UniProt residue-level features define the catalytic dyad, Zn²⁺ site, and cofactor/substrate pockets

Beyond the alignment-derived mapping, UniProt provides curated residue-level features for P59400 that specify the complete active-site architecture:

| Feature class | Residues (P59400 numbering) |
|---|---|
| Active site (proton acceptor) | **Glu333, His334** |
| Zn²⁺-binding ligands | Gln265, His268, Asp367, His426 |
| Substrate-binding residues | Ser243, Gln265, His268, His334, Asp367, Glu421, His426 |
| NAD⁺-binding residues | Tyr136, Gln197, Asn220 |

Two features of this annotation are mechanistically telling. First, the catalytic dyad Glu333/His334 matches the alignment-derived mapping of *E. coli* Glu326/His327 exactly (Finding 4), providing orthogonal confirmation. Second, **four of the Zn²⁺ ligands are shared with the substrate-binding set** (Gln265, His268, Asp367, His426), and His334 is annotated as both the catalytic proton acceptor and a substrate-contacting residue. This overlap is the molecular explanation for the experimental observation (Finding 2) that Zn²⁺ is essential for *substrate binding* rather than for the redox chemistry: the metal and its ligands literally build the substrate pocket.

## Mechanistic Model / Interpretation

The evidence assembles into a coherent, well-supported mechanistic picture of HisD/PP_0966 as the terminal enzyme of histidine biosynthesis in *P. putida*.

**Pathway context (last step of a 9-step pathway):**

```
 PRPP ──hisG──► ... (intermediate steps) ... ──► L-histidinol-P ──hisC/hisB──► L-histidinol
                                                                                   │
                                                                          hisD (PP_0966)
                                                                                   │
                                                                                   ▼
                        L-histidinol ──[NAD+]──► L-histidinaldehyde ──[NAD+]──► L-histidine
                        (bound intermediate, not released)
```

**Single-active-site, four-electron oxidation:**

```
   L-histidinol
       │  + NAD+   (1st hydride transfer; oxidation of alcohol)
       ▼
   L-histidinaldehyde  ── stays bound at active site
       │  + H2O (activated by Glu333) → gem-diol
       │  + NAD+   (2nd hydride transfer; oxidation of aldehyde hydrate)
       ▼
   L-histidine   +  2 NADH  +  3 H+
```

**Active-site organization (assembled across the dimer interface):**

- **Redox chemistry:** hydride is transferred from substrate to NAD⁺ (nicotinamide positioned by Tyr136/Gln197/Asn220). His334 acts as the general base/acid for proton transfers; Glu333 activates the catalytic water needed to hydrate the aldehyde before its oxidation to the carboxylate.
- **Substrate binding / metal site:** one Zn²⁺ per monomer is chelated by Gln265, His268, Asp367, and His426; these same ligands, together with Ser243, His334, and Glu421, form the substrate-binding pocket. The metal therefore organizes binding rather than performing catalysis — explaining why chelation abolishes activity via loss of substrate binding, not loss of a catalytic metal.
- **Quaternary structure:** the enzyme is an intertwined, domain-swapped **homodimer**; two incomplete Rossmann folds per monomer betray an ancient internal gene duplication, and each competent active site draws residues from both subunits.

**Localization:** HisD carries out its function in the **cytoplasm**. This is inferred from (i) the absence of any signal peptide or transmembrane segment in P59400, (ii) the soluble character of all characterized HisD orthologs (crystallized as soluble homodimers), and (iii) the general principle that amino-acid biosynthesis in bacteria is a cytoplasmic process. There is no evidence for periplasmic, membrane, or secreted localization.

**Biological role:** HisD provides the cell with L-histidine for protein synthesis and as a precursor for downstream metabolites. Because it executes the committed final step and works immediately downstream of *hisC* (with which it is operonically coupled), its activity gates the flux of the entire pathway toward finished amino acid. The pathway is anabolic and cytoplasmic; we found no evidence implicating this specific enzyme in signaling or in the pleiotropic two-component-system biology that dominates a keyword-driven literature search for "histidine kinase" (those papers concern unrelated His-kinase signaling proteins, not histidinol dehydrogenase).

## Evidence Base

The functional assignment rests on **four independent data layers** — enzymology/structure of orthologs, sequence conservation, curated database annotation, and genomic context — that all agree.

| PMID | Title (abbrev.) | Contribution | Supports |
|---|---|---|---|
| [11842181](https://pubmed.ncbi.nlm.nih.gov/11842181/) | *Mechanism of action and NAD⁺-binding mode revealed by the crystal structure of L-histidinol dehydrogenase* | Defines the two-step reaction, homodimer, 1 Zn²⁺/monomer (substrate-binding role), catalytic His-327/Glu-326, and two-Rossmann-fold architecture (*E. coli*) | F001, F002, F003 |
| [10353848](https://pubmed.ncbi.nlm.nih.gov/10353848/) | *Mutagenesis of histidinol dehydrogenase reveals roles for conserved histidine residues* | Confirms four-electron oxidation and histidinaldehyde intermediate; quantifies catalytic His mutations (kcat ↓7000×, ↓500×); nominates His-261/His-418 as Zn ligands (*Salmonella*) | F001, F002, F003 |
| KEGG `ppu` (PP_0965–0967) | Genomic annotation | Establishes co-oriented *hisG–hisD–hisC* cluster, 3-bp *hisD–hisC* spacing, module M00026 | F005 |
| UniProt P59400 | Curated entry | Reaction, Zn²⁺ cofactor, pathway "final step 9/9", residue-level active/binding sites, no signal/TM feature | F001, F004, F006 |

**Key primary/structural papers:**

- ***Mechanism of action and NAD⁺-binding mode revealed by the crystal structure of L-histidinol dehydrogenase*** ([PMID: 11842181](https://pubmed.ncbi.nlm.nih.gov/11842181/)) — the single most informative study. Multiple crystal forms (apo; complexes with substrate, Zn²⁺, and NAD⁺; up to 1.7 Å) directly establish the reaction, the metal's substrate-binding (not catalytic) role, the acid-base catalytic residues, and the evolutionary two-Rossmann-fold architecture.
- ***Mutagenesis of histidinol dehydrogenase reveals roles for conserved histidine residues*** ([PMID: 10353848](https://pubmed.ncbi.nlm.nih.gov/10353848/)) — provides orthogonal, solution-phase kinetic evidence (site-directed mutants, isotope/pH/stopped-flow) that pinpoints the catalytic histidines and candidate zinc ligands, complementing the crystallographic model.

**Genome-context references for KT2440.** The revisited/annotated KT2440 genome ([PMID: 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/)) and the transcriptomic genome update ([PMID: 21355971](https://pubmed.ncbi.nlm.nih.gov/21355971/)) underpin confidence in the PP_0966 locus assignment and the surrounding gene models, although neither studies *hisD* specifically. Comparative-genomics work on *P. putida* strains ([PMID: 25401060](https://pubmed.ncbi.nlm.nih.gov/25401060/)) documents the conservation of housekeeping genes across the species.

**On apparently off-target literature.** Several papers retrieved during the investigation concern **histidine kinases** and two-component signaling (e.g., [PMID: 41400398](https://pubmed.ncbi.nlm.nih.gov/41400398/), [PMID: 41413053](https://pubmed.ncbi.nlm.nih.gov/41413053/), [PMID: 40631272](https://pubmed.ncbi.nlm.nih.gov/40631272/)). These are **not** relevant to HisD/histidinol dehydrogenase — the shared word "histidine" is coincidental. One recent title, *Histidinol dehydrogenase (HisD): a critical regulator of…* ([PMID: 41294339](https://pubmed.ncbi.nlm.nih.gov/41294339/)), concerns HisD as an antibacterial drug target in a drug-resistant pathogen; the enzyme's essentiality and absence in humans make it a plausible target, but this does not alter the biochemical assignment for the *P. putida* ortholog.

## Limitations and Knowledge Gaps

1. **No direct biochemical study of the *P. putida* enzyme.** The mechanistic conclusions are transferred from *E. coli* and *Salmonella* orthologs by sequence homology (43.4% identity to *E. coli*) and curated annotation. While the residue-level conservation is complete and the family assignment is unambiguous, no purified-enzyme kinetics, crystal structure, or knockout phenotype has been reported specifically for PP_0966. Direct KM/kcat values, Zn²⁺ stoichiometry, and quaternary structure for the *P. putida* protein remain to be measured experimentally.

2. **Localization is inferred, not demonstrated.** Cytoplasmic localization is a high-confidence inference from the absence of targeting signals and from ortholog behavior, but has not been shown experimentally (e.g., by fractionation or fluorescent tagging) in *P. putida*.

3. **Operon structure is annotation-based.** The *hisG–hisD–hisC* co-orientation and 3-bp intergenic spacing strongly imply an operon, but the transcriptional start sites, promoter(s), and any attenuation/regulatory control (as classically seen in enteric *his* operons) have not been mapped in KT2440.

4. **Regulation and flux control are uncharacterized.** How *hisD* expression and HisD activity respond to histidine availability, growth phase, or stress in *P. putida* is unknown. Whether the enzyme participates in any moonlighting or regulatory role beyond biosynthesis is untested (no evidence suggests it does).

5. **NAD⁺/NADP⁺ cofactor preference** for the *P. putida* enzyme was taken as NAD⁺ from annotation and ortholog data; this has not been verified experimentally for PP_0966.

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzymology.** Clone PP_0966, purify the recombinant protein, and measure steady-state kinetics (KM for L-histidinol and NAD⁺, kcat), confirm the four-electron stoichiometry (2 NADH per histidinol), and verify NAD⁺ vs NADP⁺ preference. Determine Zn²⁺ content by ICP-MS/PAR assay and test chelator (EDTA/1,10-phenanthroline) sensitivity to confirm the substrate-binding role of the metal.

2. **Structure determination.** Solve the crystal (or cryo-EM) structure of *P. putida* HisD, ideally with substrate/NAD⁺/Zn²⁺, to confirm the homodimeric domain-swapped architecture and validate the predicted active-site residues (Glu333, His334, His268, His426, Asp367, Gln265).

3. **Site-directed mutagenesis.** Substitute Glu333, His334, His268, and His426 (Asn or Ala) and measure the effect on kcat/KM, replicating the *Salmonella* mutagenesis logic to confirm catalytic vs binding roles in the *P. putida* enzyme.

4. **Genetics and phenotyping.** Construct a clean PP_0966 deletion and test for **histidine auxotrophy** (no growth on minimal medium without histidine, rescued by supplementation), the definitive in vivo confirmation of function. Complement with the wild-type gene.

5. **Operon mapping.** Use RT-PCR/5′-RACE or RNA-seq/dRNA-seq to define the *hisG–hisD–hisC* transcript(s), promoter, and any regulatory features; test histidine-dependent regulation of expression.

6. **Localization.** Confirm cytoplasmic localization via subcellular fractionation and/or a functional fluorescent fusion.

7. **Comparative/target relevance.** Given interest in HisD as an antibacterial target ([PMID: 41294339](https://pubmed.ncbi.nlm.nih.gov/41294339/)), benchmark inhibitor sensitivity of the *P. putida* enzyme to place it in the broader structure-activity landscape of the family.

---

### Conclusion

Every line of evidence — ortholog crystal structures and kinetics, complete residue-level sequence conservation, curated UniProt annotation, and chromosomal operon context — converges on a single, confident assignment: **HisD/PP_0966 (P59400) is the cytoplasmic, homodimeric, Zn²⁺-dependent L-histidinol dehydrogenase (EC 1.1.1.23) that catalyzes the terminal four-electron NAD⁺-linked oxidation of L-histidinol to L-histidine, completing de novo histidine biosynthesis in *Pseudomonas putida* KT2440.** The gene symbol is unambiguous, and no conflicting identity was encountered.


## Artifacts

- [OpenScientist final report](hisD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hisD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11842181
2. PMID:10353848
3. PMID:26913973
4. PMID:21355971
5. PMID:25401060
6. PMID:41400398
7. PMID:41413053
8. PMID:40631272
9. PMID:41294339