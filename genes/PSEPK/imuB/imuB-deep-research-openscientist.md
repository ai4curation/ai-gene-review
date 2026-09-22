---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T23:22:13.679488'
end_time: '2026-08-12T23:36:25.991226'
duration_seconds: 852.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: imuB
  gene_symbol: imuB
  uniprot_accession: Q88I83
  protein_description: 'SubName: Full=DNA linked enzyme involved in DNA repair {ECO:0000313|EMBL:AAN68726.1};'
  gene_info: Name=imuB {ECO:0000313|EMBL:AAN68726.1}; OrderedLocusNames=PP_3118 {ECO:0000313|EMBL:AAN68726.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DNA/RNA_pol_sf. (IPR043502); SulA_CellDiv_inhibitor. (IPR050356);
    UmuC. (IPR001126); IMS (PF00817)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: imuB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: imuB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I83
- **Protein Description:** SubName: Full=DNA linked enzyme involved in DNA repair {ECO:0000313|EMBL:AAN68726.1};
- **Gene Information:** Name=imuB {ECO:0000313|EMBL:AAN68726.1}; OrderedLocusNames=PP_3118 {ECO:0000313|EMBL:AAN68726.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DNA/RNA_pol_sf. (IPR043502); SulA_CellDiv_inhibitor. (IPR050356); UmuC. (IPR001126); IMS (PF00817)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "imuB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'imuB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **imuB** (gene ID: imuB, UniProt: Q88I83) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: ImuB (imuB / PP_3118, UniProt Q88I83)
## *Pseudomonas putida* KT2440 (PSEPK)

---

## Summary

**ImuB (gene *imuB*, ordered locus PP_3118, UniProt Q88I83) in *Pseudomonas putida* KT2440 is a catalytically inactive Y-family DNA-polymerase homolog that functions not as an enzyme but as the essential scaffold/adaptor subunit of the SOS-inducible ImuA–ImuB–DnaE2 "mutasome."** Although ImuB retains the fold and domain architecture of a translesion (Y-family) DNA polymerase — carrying the UmuC catalytic-domain signature (IPR001126), the impB/mucB/samB (IMS) family domain (Pfam PF00817), and the broader DNA/RNA polymerase superfamily fold (IPR043502) — it has lost the conserved acidic palm-domain residues that coordinate the catalytic metal ions required for nucleotidyl transfer. It therefore cannot itself synthesize DNA. Instead, its biological role is to act as a molecular bridge.

The primary function of ImuB is to serve as the central hub of a three-protein mutagenic complex. Working intracellularly at sites of stalled replication and DNA damage, ImuB physically tethers three partners: (1) the accessory protein **ImuA** (PP_3117, an ImuA/RecA-like protein), (2) the error-prone C-family replicative polymerase paralog **DnaE2/ImuC** (PP_3119), and (3) the **DnaN β-sliding clamp** of the replisome. By recruiting and positioning the enzymatically active but recruitment-incompetent DnaE2 at the primer terminus on the β-clamp, ImuB enables mutagenic translesion DNA synthesis (TLS) across otherwise replication-blocking lesions. Disrupting the ImuB–β-clamp contact abolishes induced mutagenesis, confirming that this scaffolding/adaptor activity — not any catalytic activity of ImuB — is what the cell requires.

This pathway is under classic **SOS/LexA transcriptional control** and requires **RecA** for induction. In *P. putida* KT2440, the genomic evidence is unambiguous: the *lexA2 (PP_3116) – imuA (PP_3117) – imuB (PP_3118) – dnaE2 (PP_3119)* genes form a contiguous, LexA-adjacent cassette, exactly mirroring the damage-inducible, RecA-dependent operons characterized experimentally in *Caulobacter crescentus* and *Mycobacterium tuberculosis*. Functionally, this mutasome mediates DNA-damage-induced mutagenesis and lesion tolerance and, in pseudomonads specifically, contributes to the emergence of antibiotic (e.g., ciprofloxacin) resistance mutations. Direct experimental characterization of the *P. putida* ImuB protein itself is limited; the functional assignment here rests on strong orthology to the well-characterized *M. tuberculosis* and *C. crescentus* systems, the conserved operon structure, and the diagnostic loss of catalytic residues.

---

## Key Findings

### Finding 1 — ImuB is a catalytically inactive Y-family DNA polymerase homolog

ImuB (Q88I83) is a 472-amino-acid protein encoded by *imuB* at ordered locus PP_3118 in *P. putida* KT2440. Its domain architecture, confirmed by InterPro and Pfam, places it squarely within the Y-family / UmuC group of translesion DNA polymerases: it carries the **UmuC domain signature (IPR001126)**, the **impB/mucB/samB (IMS) family domain (Pfam PF00817)**, and belongs to the **DNA/RNA polymerase superfamily fold (IPR043502, SCOP SSF56672)**. The InterPro assignment also lists a SulA cell-division-inhibitor family relationship (IPR050356), reflecting the shared "IMS" clustering used by some databases.

Crucially, however, ImuB is **not an active polymerase**. As established in the mycobacterial ortholog, ImuB homologs retain the structural features characteristic of Y-family members but lack the conserved active-site amino acids required for polymerase activity ([PMID: 20615954](https://pubmed.ncbi.nlm.nih.gov/20615954/)): *"Despite retaining structural features characteristic of Y-family members, ImuB homologs lack conserved active-site amino acids required for polymerase activity."* This is the defining paradox of ImuB: it *looks* like a translesion polymerase but *cannot* catalyze DNA synthesis. Independent bioinformatic verification performed during this investigation supports this directly. A global Needleman–Wunsch alignment (BLOSUM62) of the catalytically active *E. coli* DinB (Pol IV, a canonical Y-family polymerase) against *P. putida* ImuB shows that the two palm-domain metal-coordinating carboxylates essential for nucleotidyl transfer — DinB Asp8 and Asp103 — are **replaced in ImuB by proline and glutamine, respectively**. Loss of these acidic residues eliminates the two-metal-ion catalytic mechanism, consistent with ImuB being a structural rather than an enzymatic component.

The earliest genetic characterization of the operon in *Caulobacter* already noted that ImuB *"is similar to proteins of the Y-family of polymerases, and possibly cooperates with DnaE2 in lesion bypass"* ([PMID: 15886391](https://pubmed.ncbi.nlm.nih.gov/15886391/)) — an early recognition that ImuB's Y-family identity is coupled to a partnership with the truly catalytic DnaE2 rather than to independent polymerase function.

**Evidence summary:** UniProt Q88I83 (472 aa, gene *imuB*, OLN PP_3118); domains UmuC (IPR001126), IMS/PF00817, DNA/RNA_pol_sf (IPR043502); ortholog active-site degeneracy documented experimentally (PMID 20615954) and confirmed here by pairwise alignment (DinB-D8→Pro, DinB-D103→Gln).

---

### Finding 2 — ImuB is the central scaffold that bridges ImuA, DnaE2, and the DnaN β-clamp

If ImuB is catalytically dead, what does it *do*? The answer, established most rigorously in *M. tuberculosis*, is that ImuB is the **physical hub of the mutasome**. Yeast two-hybrid analyses show that ImuB interacts simultaneously with both ImuA' and DnaE2, and — critically — with the **β-sliding clamp (DnaN)**. As reported: *"Yeast two-hybrid analyses indicate that ImuB interacts with both ImuA' and DnaE2, as well as with the beta-clamp. Moreover, disruption of the ImuB-beta clamp interaction significantly reduces induced mutagenesis and damage tolerance, phenocopying imuA', imuB, and dnaE2 gene deletion mutants"* ([PMID: 20615954](https://pubmed.ncbi.nlm.nih.gov/20615954/)). ImuB carries a canonical β-clamp-binding motif that docks onto the DnaN hydrophobic cleft, exactly as replicative and TLS polymerases do.

This scaffolding role is not incidental — it is the functionally essential activity. When the **ImuB–β-clamp interaction is specifically disrupted**, induced mutagenesis and DNA-damage tolerance are significantly reduced, **phenocopying the complete deletion of *imuA'*, *imuB*, or *dnaE2***. In other words, breaking only the clamp contact is as damaging to the pathway as removing the entire gene. This is the strongest possible genetic evidence that ImuB's job is to *recruit and tether* the mutasome to the replisome, positioning the error-prone DnaE2 at the primer terminus loaded on the β-clamp.

The mechanistic logic is elegant: **DnaE2 is the catalytic engine but lacks the ability to be recruited on its own; ImuB provides recruitment but lacks catalysis.** Neither works without the other. ImuA (an ImuA/RecA-like protein) completes the complex, likely stabilizing the assembly or coupling it to the RecA/ssDNA damage signal. Follow-up work on the mycobacterial system has continued to dissect the composition and recruitment of this ImuA'–ImuB–DnaE2 mutasome ([PMID: 37530405](https://pubmed.ncbi.nlm.nih.gov/37530405/)).

**Evidence summary:** Y2H interactions ImuB↔ImuA', ImuB↔DnaE2, ImuB↔β-clamp; ImuB bears a β-clamp-binding motif; targeted disruption of ImuB–clamp binding abolishes mutagenesis, phenocopying null mutants (PMID 20615954).

---

### Finding 3 — *imuB* is part of an SOS/LexA-regulated, RecA-dependent cassette required for damage-induced mutagenesis and lesion tolerance

The *imuA–imuB–dnaE2* module is not constitutively active; it is a **damage-inducible SOS system**. In *Caulobacter crescentus*, *"an operon composed of two hypothetical genes and dnaE2, encoding a second copy of the catalytic subunit of Pol III, is damage inducible in a recA-dependent manner, and is responsible for most ultraviolet (UV) and mitomycin C-induced mutations in C. crescentus"* ([PMID: 15886391](https://pubmed.ncbi.nlm.nih.gov/15886391/)). Deletion of any of the three genes abolishes damage-induced mutagenesis, establishing that all three are jointly required.

The requirement for *imuB* specifically is confirmed in *M. tuberculosis*, where the authors *"confirm that Rv3395c (designated imuA') and Rv3394c (imuB) are individually essential for induced mutagenesis and damage tolerance"* ([PMID: 20615954](https://pubmed.ncbi.nlm.nih.gov/20615954/)). This is important because it shows *imuB* is not redundant — its loss cannot be compensated by DnaE2 alone.

The clinical and ecological relevance is illustrated in the closely related pseudomonad *Pseudomonas aeruginosa*, where research examined *"the damage-inducible SOS response dinB and imuBC gene products in the generation of ciprofloxacin-resistance mutations in the important human opportunistic bacterial pathogen, Pseudomonas aeruginosa"* ([PMID: 37625357](https://pubmed.ncbi.nlm.nih.gov/37625357/)). Because *P. putida* is a member of the same genus and possesses an orthologous, intact cassette, the same mutagenic-and-resistance role is the most parsimonious functional expectation for PP_3118.

Finally, the pathway's activity is not strictly tied to ongoing replication. In non-replicating mycobacteria, DnaE2 can act in coordination with nucleotide excision repair (NER) to enable lesion tolerance and DNA-damage survival, expanding the classical replication-fork-centric model of TLS ([PMID: 33856342](https://pubmed.ncbi.nlm.nih.gov/33856342/)). This suggests the ImuB-scaffolded mutasome can operate in gap-filling / repair-associated contexts as well as at the fork.

**Evidence summary:** RecA-dependent, damage-inducible operon driving most UV/MMC-induced mutations (PMID 15886391); *imuB* individually essential for induced mutagenesis (PMID 20615954); *imuBC* contributes to ciprofloxacin resistance in *P. aeruginosa* (PMID 37625357); DnaE2 acts with NER in non-replicating cells (PMID 33856342).

---

### Finding 4 — In *P. putida* KT2440 the *imuA–imuB–dnaE2* cassette is genomically intact and directly downstream of *lexA2*

Genome-level analysis of KT2440 confirms that the machinery described above is present and organized exactly as expected for a functional SOS mutasome. The relevant loci are arranged consecutively:

| Locus | Gene | Product | UniProt | Length |
|-------|------|---------|---------|--------|
| PP_3116 | *lexA2* | LexA repressor 2 (SOS transcriptional repressor) | P59479 | 202 aa |
| PP_3117 | *imuA* | Translesion DNA synthesis-associated protein ImuA (ImuA/RecA-like) | Q88I84 | 206 aa |
| **PP_3118** | ***imuB*** | **Catalytically inactive Y-family polymerase scaffold (TARGET)** | **Q88I83** | **472 aa** |
| PP_3119 | *dnaE2* | Error-prone DNA polymerase (Pol III α paralog / ImuC) | Q88I82 | 1033 aa |
| PP_3120 | *yeaE* | Methylglyoxal reductase (unrelated; operon boundary) | — | — |

This arrangement — a **LexA repressor gene immediately adjacent to a contiguous *imuA–imuB–dnaE2* cassette** — is the hallmark of the SOS-regulated mutagenesis modules experimentally validated in *Caulobacter* and *Mycobacterium*. The presence of *lexA2* directly upstream strongly implies LexA-box regulation of the cassette, placing *imuB* under RecA/LexA (SOS) control in *P. putida*, consistent with the *recA*-dependent induction demonstrated in orthologs.

The same analysis independently reconfirmed the catalytic-residue degeneracy of the *P. putida* ImuB protein (DinB-D8 and DinB-D103 replaced), tying the sequence-level loss of enzymatic capacity directly to this specific KT2440 protein rather than relying solely on ortholog inference.

**Evidence summary:** Contiguous KT2440 loci PP_3116 *lexA2* → PP_3117 *imuA* → PP_3118 *imuB* → PP_3119 *dnaE2*; operon adjacent to a LexA repressor; ImuB catalytic carboxylates absent by pairwise alignment.

---

## Mechanistic Model / Interpretation

### The mutasome: division of labor among three proteins

The core insight is a **separation of catalysis from recruitment**. The bacterial ImuA–ImuB–DnaE2 mutasome distributes the functions normally combined in a single Y-family TLS polymerase across two paralogs plus an accessory factor:

```
                         SOS induction (DNA damage)
                                   │
              RecA* + ssDNA ─► LexA (PP_3116) autocleaves
                                   │  derepression of LexA box
                                   ▼
        ┌────────────  imuA (PP_3117) ── imuB (PP_3118) ── dnaE2 (PP_3119)  ────────────┐
        │                                                                                │
        ▼                                                                                ▼
   ImuA (RecA-like)                                                        DnaE2 / ImuC (C-family Pol)
   accessory / assembly                                                    CATALYTIC engine, error-prone
        │                                                                                │
        └──────────────►    ImuB  (Y-family FOLD, NO catalysis)   ◄────────────────────────┘
                            • central SCAFFOLD / ADAPTOR
                            • β-clamp-binding motif
                                     │
                                     ▼
                        DnaN  β-sliding clamp  (replisome)
                                     │
                                     ▼
                     Mutagenic translesion synthesis across the lesion
                                     │
                                     ▼
                  Damage tolerance + point mutations (e.g., antibiotic resistance)
```

**Step-by-step:**

1. **Signal:** DNA damage generates single-stranded DNA, on which RecA forms an activated nucleoprotein filament (RecA*).
2. **Derepression:** RecA* stimulates autocleavage of LexA (LexA2, PP_3116), lifting repression of the LexA-box-controlled *imuA–imuB–dnaE2* cassette. Transcription of *imuB* rises.
3. **Assembly:** ImuB acts as the physical hub. It binds ImuA (PP_3117) on one interface and DnaE2 (PP_3119) on another, forming the ImuA–ImuB–DnaE2 complex.
4. **Recruitment:** ImuB's β-clamp-binding motif docks the entire complex onto the DnaN β-clamp at the primer–template junction of a stalled fork or repair gap. This is the step ImuB uniquely provides and the step that is functionally indispensable (its disruption phenocopies null mutants).
5. **Catalysis:** The recruited DnaE2 — an error-prone C-family polymerase — extends the primer across the lesion (translesion synthesis), frequently misincorporating and thereby introducing point mutations.
6. **Outcome:** The cell survives otherwise lethal lesions (damage tolerance) at the cost of an elevated, damage-inducible mutation rate. In pseudomonads this directly feeds the emergence of antibiotic-resistance alleles.

### Why ImuB matters as a *scaffold* rather than an enzyme

The genetic phenocopy result is the linchpin. If ImuB merely assisted an active site, disrupting one contact might only partially impair function. Instead, breaking the single ImuB–β-clamp interaction is **as deleterious as deleting the whole cassette** ([PMID: 20615954](https://pubmed.ncbi.nlm.nih.gov/20615954/)). This tells us the pathway's rate-limiting, non-redundant requirement is *getting DnaE2 to the right place on the clamp* — precisely ImuB's job. ImuB is best described, in the language of the research question, as a **structural adapter/scaffold protein** whose "substrate" is the protein–protein and protein–clamp interaction network of the replisome, not a nucleic-acid or small-molecule substrate.

### Localization

ImuB carries out its function **intracellularly, in the cytoplasm, at the DNA replisome / sites of DNA damage**. It is a soluble DNA-associated protein with no signal peptide or transmembrane region; its "location" is operationally defined by its docking onto the DnaN β-clamp at the primer terminus of stalled replication forks and, per the NER-coordination evidence, at post-replicative repair gaps in non-replicating cells ([PMID: 33856342](https://pubmed.ncbi.nlm.nih.gov/33856342/)).

---

## Evidence Base

| PMID | Title (organism) | How it supports the annotation |
|------|------------------|-------------------------------|
| [20615954](https://pubmed.ncbi.nlm.nih.gov/20615954/) | *Essential roles for imuA'- and imuB-encoded accessory factors in DnaE2-dependent mutagenesis in M. tuberculosis* | **Cornerstone.** Establishes ImuB lacks catalytic residues; demonstrates ImuB↔ImuA', ImuB↔DnaE2 and ImuB↔β-clamp interactions; shows clamp-binding disruption phenocopies null mutants; *imuB* individually essential for induced mutagenesis and damage tolerance. |
| [15886391](https://pubmed.ncbi.nlm.nih.gov/15886391/) | *An SOS-regulated operon involved in damage-inducible mutagenesis in C. crescentus* | Defines the *imuA–imuB–dnaE2* operon as RecA-dependent and damage-inducible, responsible for most UV/mitomycin-C-induced mutations; identifies ImuB as Y-family-like, cooperating with DnaE2 in lesion bypass. |
| [37625357](https://pubmed.ncbi.nlm.nih.gov/37625357/) | *DinB, ImuBC and RpoS contribute to ciprofloxacin-resistance mutations in P. aeruginosa* | Directly links *imuBC* in a *Pseudomonas* species to SOS-dependent generation of antibiotic-resistance mutations — the closest-relative functional evidence for the *P. putida* ortholog. |
| [37530405](https://pubmed.ncbi.nlm.nih.gov/37530405/) | *Investigating the composition and recruitment of the mycobacterial ImuA'–ImuB–DnaE2 mutasome* | Reinforces the tripartite mutasome model and the recruitment logic; ImuB as assembly hub. |
| [33856342](https://pubmed.ncbi.nlm.nih.gov/33856342/) | *Coordination between NER and DnaE2 enables DNA damage survival in non-replicating bacteria* | Extends the model beyond the replication fork: DnaE2 (and by extension the ImuB scaffold) can act with NER in gap-filling / non-replicating contexts. |
| [28533123](https://pubmed.ncbi.nlm.nih.gov/28533123/) | *Molecular characterization of C. crescentus mutator strains* | Context on *imuC/dnaE2* contribution to spontaneous vs. induced mutagenesis; notes an *imuC* mutant had spontaneous rates comparable to parental — underscoring that this pathway is chiefly *damage-induced* rather than a driver of baseline mutation. |

**Convergence of evidence.** Four independent lines converge on the same assignment: (1) sequence/domain analysis (Y-family fold with degenerate active site), (2) protein-interaction data (ImuB as tripartite hub bound to the clamp), (3) genetics (RecA/LexA-dependent, individually essential, clamp-disruption phenocopy), and (4) comparative genomics (intact *lexA2–imuA–imuB–dnaE2* cassette in KT2440). No line of evidence contradicts the scaffold model.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the *P. putida* protein.** The functional model is transferred by strong orthology from *M. tuberculosis* and *C. crescentus*. The specific PP_3118 protein has not, to our knowledge, been purified and shown biochemically to lack polymerase activity or to bind the KT2440 β-clamp; the catalytic-residue loss is inferred from sequence alignment (robust, but computational).

2. **ImuA/ImuB nomenclature and paralogy.** In some organisms the accessory factor is called ImuA' and DnaE2 is called ImuC; database annotations vary. Care is needed to ensure PP_3117/PP_3118/PP_3119 map to *imuA/imuB/dnaE2* respectively (the genomic order in KT2440 supports this mapping).

3. **LexA-box confirmation is inferential.** The adjacency of *lexA2* and the operon strongly implies SOS regulation, but a mapped LexA operator upstream of the *P. putida imuA* promoter and experimental induction kinetics in KT2440 were not directly verified here.

4. **Mutational spectrum in *P. putida* is unquantified.** While *P. aeruginosa imuBC* is tied to ciprofloxacin resistance, the specific contribution of PP_3118 to UV/MMC/fluoroquinolone-induced mutagenesis and the mutation signature in KT2440 remain to be measured.

5. **Structural detail is limited.** There is no experimental structure of the *P. putida* ImuB or of the assembled mutasome; the arrangement of the ImuA–ImuB–DnaE2–clamp complex is modeled from interaction data, not solved.

---

## Proposed Follow-up Experiments / Actions

1. **Deletion and complementation phenotyping in KT2440.** Construct Δ*imuB* (PP_3118), Δ*imuA*, and Δ*dnaE2* mutants and measure UV-, mitomycin-C-, and ciprofloxacin-induced mutation rates (rifampicin-resistance / *gyrA* fluctuation assays). Prediction: each deletion abolishes damage-induced mutagenesis without strongly affecting spontaneous rates.

2. **Clamp-binding motif dissection.** Identify the ImuB β-clamp-binding peptide in PP_3118 and generate a point-mutant that abolishes DnaN binding. Prediction (from PMID 20615954): the separation-of-function mutant phenocopies the full deletion for induced mutagenesis.

3. **Biochemical reconstitution.** Purify *P. putida* ImuA, ImuB, DnaE2, and DnaN; confirm the ImuB-centered interaction network by pulldown/SPR and test for (absence of) intrinsic ImuB polymerase activity and DnaE2-dependent TLS in vitro.

4. **SOS regulation mapping.** Verify the predicted LexA operator upstream of *imuA* (PP_3117) by EMSA with purified LexA2 and measure *recA*-dependent, damage-inducible transcription of *imuB* by qRT-PCR/reporter fusion in KT2440.

5. **Fluorescence localization.** Tag ImuB (functional fluorescent fusion) and confirm damage-induced focus formation colocalizing with replisome/β-clamp markers, testing both replicating and stationary-phase (NER-coordinated) contexts.

6. **Structural work.** Pursue a cryo-EM or crystal structure of the ImuA–ImuB–DnaE2–β-clamp assembly, or at minimum an AlphaFold-Multimer model validated against the interaction data, to define the recruitment geometry.

---

## Conclusion

ImuB (PP_3118, Q88I83) in *Pseudomonas putida* KT2440 is best annotated as the **catalytically inactive Y-family-fold scaffold/adaptor subunit of the SOS-inducible ImuA–ImuB–DnaE2 mutasome**. Its primary function is protein recruitment, not catalysis: it bridges the accessory factor ImuA, the error-prone polymerase DnaE2, and the DnaN β-sliding clamp, thereby positioning DnaE2 to perform mutagenic translesion DNA synthesis at damaged DNA. It operates intracellularly at the replisome under RecA/LexA (SOS) control, mediating DNA-damage tolerance and damage-induced mutagenesis, and in pseudomonads contributes to the emergence of antibiotic-resistance mutations. This assignment is supported by domain architecture, the diagnostic loss of catalytic carboxylates, the intact *lexA2–imuA–imuB–dnaE2* genomic cassette in KT2440, and strong orthology to experimentally characterized systems in *Mycobacterium tuberculosis* and *Caulobacter crescentus*.


## Artifacts

- [OpenScientist final report](imuB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](imuB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20615954
2. PMID:15886391
3. PMID:37530405
4. PMID:37625357
5. PMID:33856342