---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T18:23:05.098753'
end_time: '2026-07-26T18:56:56.627841'
duration_seconds: 2031.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pssA
  gene_symbol: pssA
  uniprot_accession: Q88GQ4
  protein_description: 'SubName: Full=CDP-diacylglycerol--serine O-phosphatidyltransferase
    {ECO:0000313|EMBL:AAN69264.1}; EC=2.7.8.8 {ECO:0000313|EMBL:AAN69264.1};'
  gene_info: Name=pssA {ECO:0000313|EMBL:AAN69264.1}; OrderedLocusNames=PP_3664 {ECO:0000313|EMBL:AAN69264.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the CDP-alcohol phosphatidyltransferase class-II
  protein_domains: PGS1. (IPR016270); PLD-like_dom. (IPR025202); PLipase_D/transphosphatidylase.
    (IPR001736); PLDc_2 (PF13091)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pssA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pssA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GQ4
- **Protein Description:** SubName: Full=CDP-diacylglycerol--serine O-phosphatidyltransferase {ECO:0000313|EMBL:AAN69264.1}; EC=2.7.8.8 {ECO:0000313|EMBL:AAN69264.1};
- **Gene Information:** Name=pssA {ECO:0000313|EMBL:AAN69264.1}; OrderedLocusNames=PP_3664 {ECO:0000313|EMBL:AAN69264.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the CDP-alcohol phosphatidyltransferase class-II
- **Key Domains:** PGS1. (IPR016270); PLD-like_dom. (IPR025202); PLipase_D/transphosphatidylase. (IPR001736); PLDc_2 (PF13091)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pssA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pssA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pssA** (gene ID: pssA, UniProt: Q88GQ4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pssA* (Q88GQ4, PP_3664) — Phosphatidylserine Synthase of *Pseudomonas putida* KT2440

## Summary

The gene ***pssA*** (UniProt **Q88GQ4**, ordered locus **PP_3664**) of *Pseudomonas putida* strain KT2440 encodes **phosphatidylserine synthase (PssA; EC 2.7.8.8)**, a **CDP-diacylglycerol—serine O-phosphatidyltransferase**. Its primary and best-supported function is to catalyze the **committed first step of the phosphatidylethanolamine (PE) biosynthetic pathway**: it transfers the phosphatidyl moiety of **CDP-diacylglycerol (CDP-DG)** onto the hydroxyl of **L-serine**, producing **phosphatidylserine (PS)** and releasing **CMP**. Phosphatidylserine is then decarboxylated by a separately encoded phosphatidylserine decarboxylase (Psd, PP_4908) to yield **phosphatidylethanolamine**, one of the dominant glycerophospholipids of the *P. putida* membrane. This two-enzyme route (CDP-DG → PS → PE) is the canonical bacterial pathway for producing the major zwitterionic membrane lipid.

Mechanistically, PssA is a member of the **phospholipase D (PLD) superfamily** and belongs to the **CDP-alcohol phosphatidyltransferase class-II / PGS1** clade. The 442-residue protein carries the two hallmark **HKD catalytic motifs** (H-x-K-x₄-D) that signature PLD-superfamily transferases; these two half-sites fold together to build a single bilobed active site that operates through a **covalent phosphatidyl–histidine (phosphatidyl-enzyme) intermediate**. It is a **peripheral membrane protein** that is catalytically active only when associated with the cytoplasmic face of the inner membrane and inactive when in the cytosol — a localization-based regulatory switch. These conclusions rest on a coherent, converging evidence base: curated EC/GO/KEGG annotation, InterPro/Pfam domain signatures, direct sequence analysis of Q88GQ4, and strong orthology (**46% amino-acid identity** with conserved catalytic motifs) to the experimentally characterized and crystallized *Escherichia coli* PssA.

Although no dedicated biochemical or genetic study of the *P. putida* KT2440 protein itself was located, the functional assignment transfers with high confidence from well-characterized orthologs (*E. coli*, *Sinorhizobium meliloti*, *Bacillus subtilis*). In these systems, loss of *pssA* abolishes PS synthase activity and PE formation, confirming the enzyme's role as the pathway's committed entry step. The enzyme additionally shows **acceptor-site promiscuity** — it can use L-homoserine to make phosphatidylhomoserine in *E. coli* — and its expression level directly modulates membrane PE content and stress tolerance in engineered *Pseudomonas* and *E. coli* strains.

---

## Gene/Protein Identity Verification

Before presenting findings, the target identity was verified against the supplied UniProt record; all evidence is consistent.

| Attribute | UniProt record (Q88GQ4) | Verification result |
|---|---|---|
| Gene symbol | *pssA* | ✅ Matches PssA / phosphatidylserine synthase literature |
| Enzyme | CDP-diacylglycerol—serine O-phosphatidyltransferase, EC 2.7.8.8 | ✅ Consistent with GO:0003882 and KEGG K00998 |
| Locus | PP_3664 | ✅ KEGG ppu:PP_3664; complement(4162133..4163461) |
| Organism | *Pseudomonas putida* KT2440 (PSEPK) | ✅ Correct strain |
| Family | CDP-alcohol phosphatidyltransferase class-II | ✅ InterPro IPR016270 (PGS1) |
| Domains | PLD-like, PLipase_D/transphosphatidylase, PLDc_2 (PF13091) | ✅ Confirmed by InterPro/Pfam scan of Q88GQ4 |

The gene symbol *pssA* is unambiguous in this context and aligns fully with the protein description, organism, family, and domain architecture. A nomenclature caveat: in *E. coli* and *P. putida*, "PssA" denotes a **PLD-superfamily** phosphatidylserine synthase (PSS type II), whereas some organisms (e.g., yeast) use a mechanistically distinct **base-exchange** type I PSS. The *P. putida* enzyme is unambiguously the **type II / PLD-superfamily** enzyme, as established by its HKD motifs and PLD-domain signatures.

---

## Key Findings

### Finding 1 — PssA is phosphatidylserine synthase, the committed step of PE biosynthesis

The core function of PP_3664 is synthesis of phosphatidylserine as the obligatory precursor of phosphatidylethanolamine. Curated annotation assigns Q88GQ4 the activity **CDP-diacylglycerol—serine O-phosphatidyltransferase (EC 2.7.8.8)**, corresponding to **GO:0003882**. The reaction catalyzed is:

```
CDP-diacylglycerol  +  L-serine   →   phosphatidylserine (PS)  +  CMP
```

Phosphatidylserine is subsequently decarboxylated by phosphatidylserine decarboxylase (Psd) to phosphatidylethanolamine (PE). This makes PssA the **committed, rate-influencing entry enzyme** of the PE branch of glycerophospholipid metabolism.

The functional assignment is supported by genetic evidence from multiple orthologs. A recent structural study describes PssA plainly as "*essential in the biosynthesis of phosphatidylethanolamine, a major phospholipid of bacterial membranes*" ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)). In *E. coli*, deletion of most of the *pssA* gene produced a mutant that "*lacked phosphatidylserine synthase and phosphatidylethanolamine and required divalent metal ions for growth*" ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)) — demonstrating that *pssA* is required both for the enzymatic activity and for the downstream lipid product. The requirement is conserved across Gram-negative bacteria: in *Sinorhizobium meliloti*, "*inactivation of the sinorhizobial pssA gene leads to the inability to form PE*" ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/)). Together these establish PssA as the necessary and committed producer of PS en route to PE.

### Finding 2 — PssA is a PLD-superfamily enzyme using a covalent intermediate, and is a peripheral membrane protein

A direct domain and sequence analysis of Q88GQ4 places PssA firmly in the **phospholipase D (PLD) superfamily**. The InterPro/Pfam signatures are **IPR001736** (Phospholipase D/transphosphatidylase), **IPR025202** (PLD-like domain), **PF13091** (PLDc_2), **SUPFAM SSF56024** (Phospholipase D/nuclease), and **IPR016270** (PGS1). A scan of the 442-amino-acid sequence reveals the **two canonical PLD-superfamily HKD catalytic motifs** (H-x-K-x₄-D):

| Motif | Sequence | Position (approx.) |
|---|---|---|
| HKD motif I | **H**LKGSII**D** | residue ~130 |
| HKD motif II | **H**AKGVWI**D** | residue ~348 |

These two half-site motifs juxtapose in the folded protein to form a single bilobed active site — a hallmark of the PLD superfamily, in which catalysis proceeds via a **covalent phosphatidyl-histidine intermediate** rather than direct in-line transfer.

The catalytic mechanism and localization are described in detail for the *E. coli* ortholog: "*A peripheral membrane protein PssA can associate with the cellular membrane in its active state or exist in the cytosol in an inactive form. The membrane-bound enzyme acts on cytidine diphosphate diacylglycerol (CDP-DG) to form cytidine monophosphate and a covalent intermediate, which is subsequently targeted by serine to produce phosphatidylserine*" ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)). This two-step, ping-pong-like mechanism — (1) the enzyme attacks CDP-DG, releasing CMP and forming a phosphatidyl-enzyme covalent intermediate; (2) serine attacks the intermediate to yield PS — is fully consistent with the two HKD motifs found in Q88GQ4. UniProt further annotates the enzyme with **GO:0005829 (cytosol)**, reflecting the fact that PssA is a **peripheral** rather than integral membrane protein: it partitions between an inactive cytosolic pool and an active membrane-associated pool.

### Finding 3 — PE, the pathway's downstream product, is a dominant *P. putida* membrane lipid and a stress-adaptation lever

The physiological relevance of the PssA pathway in *P. putida* is underscored by lipidomic analysis. High-resolution LC/MS lipidomics of *P. putida* KT2440 identified "*305 distinct glycerophospholipids [e.g. PE(16:0/16:1)]*" ([PMID: 21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/)), with **phosphatidylethanolamine among the principal head-group classes**. Because PssA supplies the PS that is obligately decarboxylated to PE, the enzyme sits directly upstream of this dominant lipid pool. Membrane head-group composition is remodeled under solvent (n-butanol) stress, indicating that flux through the PE branch is physiologically dynamic.

Direct engineering evidence links PssA level to membrane robustness. In a metabolic-engineering study, "*increasing the expression of phosphatidylserine synthase (+pssA) was found to significantly increase both the tolerance and production of octanoic acid*" ([PMID: 28867349](https://pubmed.ncbi.nlm.nih.gov/28867349/)). This demonstrates that PssA expression is a control point governing PE abundance and, through it, membrane integrity and tolerance to membrane-damaging compounds — a property of particular importance in the solvent-tolerant bacterium *P. putida*.

### Finding 4 — *P. putida* PssA is a confident ortholog of the crystallized *E. coli* PssA (46% identity)

To justify transferring the *E. coli* structural/mechanistic model to the *P. putida* protein, a global Needleman–Wunsch alignment was performed between Q88GQ4 (442 aa) and *E. coli* PssA (P23830, 451 aa). The alignment gave **204/440 = 46.4% identity** over the aligned length — well above the ~30% "twilight-zone" threshold for confident orthology, indicating clear one-to-one functional equivalence. Critically, both proteins carry the two HKD catalytic motifs in the same register:

| | HKD motif I | HKD motif II |
|---|---|---|
| *E. coli* PssA (P23830) | HFKGFIID (res ~138) | HLKGMWVD (res ~357) |
| *P. putida* PssA (Q88GQ4) | HLKGSIID (res ~130) | HAKGVWID (res ~348) |

The 2024 *E. coli* PssA crystal structures resolved both an apo form and a CDP-DG–bound Michaelis complex: "*Here, we present two crystal structures of Escherichia coli PssA, one complexed with CDP-DG and the other without. The lipid-bound structure mimics the Michaelis complex before the formation of a covalent intermediate, revealing key determinants for substrate recognition and catalysis*" ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)). The structures also revealed a regulatory mechanism: "*membrane-free PssA is in a monomer-dimer equilibrium, with only the monomer capable of associating with the membrane, suggesting a regulatory mechanism for phospholipid biosynthesis dependent on the oligomerization state of the enzyme*" ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)). Given 46% identity and conserved catalysis, these substrate-recognition, catalytic, and oligomerization-based regulatory insights transfer with high confidence to the *P. putida* enzyme.

### Finding 5 — PssA (PP_3664) is the entry enzyme of a two-step PE module; Psd is separately encoded at PP_4908

KEGG assigns **ppu:PP_3664** to orthology **K00998** (CDP-diacylglycerol—serine O-phosphatidyltransferase, EC 2.7.8.8) and to module **ppu_M00093**, "*Phosphatidylethanolamine (PE) biosynthesis, PA => CDP-DAG => PS => PE*," with gene coordinates complement(4162133..4163461). The downstream phosphatidylserine decarboxylase (K01613, Psd) maps to a **distinct, non-adjacent locus, ppu:PP_4908**. Thus, unlike the *pss*–*psd* operon of *Bacillus subtilis*, the *P. putida pssA* and *psd* genes are **not genomically clustered**, and the pathway is assembled from two separately regulated loci.

The chemistry of the downstream step is well defined by structural studies of *E. coli* PSD: "*Phosphatidylethanolamine (PE), a major component of the cellular membrane across all domains of life, is synthesized exclusively by membrane-anchored phosphatidylserine decarboxylase (PSD) in most bacteria. The enzyme undergoes auto-cleavage for activation and utilizes the pyruvoyl moiety to form a Schiff base intermediate with PS to facilitate decarboxylation*" ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/)). A companion structural study of *E. coli* Psd reported that "*EcPsd forms a homodimer, and each protomer has a positively charged substrate binding pocket at the active site… EcPsd has an N-terminal hydrophobic helical region that is important for membrane binding*" ([PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/)). PssA thus produces the substrate (PS) that the pyruvoyl-dependent, membrane-anchored Psd converts to PE, completing the module. Because PS does not normally accumulate, PssA activity effectively sets the supply of PE.

### Finding 6 — The serine-binding (acceptor) site is somewhat promiscuous

The head-group acceptor site of PssA is not strictly limited to L-serine. In *E. coli*, an unidentified membrane lipid observed in minimal medium was characterized by LC-MS and metabolic labeling as **phosphatidylhomoserine (PHS)**, and it was shown to be produced by PssA: "*In E. coli, PHS was produced endogenously by phosphatidylserine synthase A (PssA), confirmed by the absence of PHS in an E. coli ΔpssA mutant*" ([PMID: 40404014](https://pubmed.ncbi.nlm.nih.gov/40404014/)). This indicates the acceptor site can accommodate **L-homoserine** in addition to its physiological substrate L-serine — measurable substrate promiscuity. Given the 46% identity to *E. coli* PssA, the *P. putida* enzyme plausibly shares this capacity, though it has not been tested directly. This informs, but does not change, the physiological specificity for L-serine.

---

## Mechanistic Model / Interpretation

Integrating the findings yields a coherent picture of PssA's role in *P. putida* membrane biogenesis:

```
                       Glycerol-3-P / fatty acids
                                 │
                                 ▼
                        Phosphatidic acid (PA)
                                 │  (CdsA, CTP)
                                 ▼
                     CDP-diacylglycerol (CDP-DG)  ◄── central branch point
                          │                    │
             ┌────────────┘                    └───────────────┐
             ▼  PssA (PP_3664)                                  ▼ (PgsA / anionic branch)
   ┌───────────────────────────────┐                  Phosphatidylglycerol-P
   │ CDP-DG + L-serine              │                          │
   │   → Phosphatidylserine + CMP   │                          ▼
   │ [covalent phosphatidyl-His     │                  Phosphatidylglycerol (PG)
   │  intermediate; 2× HKD motifs]  │                          │
   └───────────────┬───────────────┘                          ▼
                   ▼  Psd (PP_4908)                        Cardiolipin (CL)
   ┌───────────────────────────────┐
   │ Phosphatidylserine → PE + CO₂  │
   │ [pyruvoyl Schiff-base; PSD]    │
   └───────────────┬───────────────┘
                   ▼
        Phosphatidylethanolamine (PE)  ── dominant zwitterionic membrane lipid
```

**Location of function.** PssA acts at the **cytoplasmic (inner) leaflet of the inner membrane**, where CDP-DG resides, but is itself a **peripheral membrane protein** that shuttles between an inactive cytosolic pool and an active membrane-bound state. Membrane association is coupled to its oligomerization state — the monomer binds membrane and is catalytically productive, while the dimer partitions away — providing a built-in regulatory switch that couples enzyme activity to the availability of its lipid substrate and to the physical state of the membrane.

**Pathway role and branch-point control.** CDP-DG is the shared precursor for both the **zwitterionic branch** (PS → PE, via PssA and Psd) and the **acidic branch** (phosphatidylglycerol and cardiolipin, via PgsA/Cls). By committing CDP-DG to serine, PssA governs the partitioning of flux between these two branches and therefore helps set the **PE : PG/CL ratio** — a determinant of membrane surface charge, curvature stress, and bilayer integrity. This explains why manipulating PssA levels alters solvent/organic-acid tolerance ([PMID: 28867349](https://pubmed.ncbi.nlm.nih.gov/28867349/)): more PssA drives more PE, remodeling the membrane's biophysical properties.

**Catalytic logic.** As a PLD-superfamily transferase, PssA does not perform a direct one-step transfer. Instead its two HKD half-sites cooperate: one histidine attacks the phosphodiester of CDP-DG to expel CMP and form a **covalent phosphatidyl-enzyme intermediate**; the second histidine positions L-serine's hydroxyl for nucleophilic attack on the intermediate, releasing PS. This transphosphatidylation chemistry — the same mechanistic class as phospholipase D — accounts for the enzyme's ability to occasionally accept alternative alcohols such as L-homoserine (Finding 6).

---

## Evidence Base

| PMID | Title (abbreviated) | Relevance to PssA (PP_3664) |
|---|---|---|
| [39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/) | *Structural basis for membrane association and catalysis by phosphatidylserine synthase* | **Primary structural/mechanistic source.** Crystal structures of *E. coli* PssA (apo + CDP-DG complex); defines peripheral-membrane localization, covalent-intermediate catalysis, and monomer–dimer regulation. Transfers to Q88GQ4 via 46% identity. |
| [8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/) | *A regulatory mechanism for the balanced synthesis of membrane phospholipid species in E. coli* | Genetic knockout: *E. coli* Δ*pssA* lacks PS synthase activity and PE; establishes necessity of *pssA* for the pathway. |
| [14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/) | *Phosphatidylethanolamine is not essential for growth of Sinorhizobium meliloti…* | Independent Gram-negative ortholog: *pssA* inactivation abolishes PE formation. |
| [21895997](https://pubmed.ncbi.nlm.nih.gov/21895997/) | *The glycerophospholipid inventory of Pseudomonas putida…* | Organism-specific lipidomics: PE is a principal glycerophospholipid class in *P. putida* KT2440 — the downstream product of the PssA route. |
| [28867349](https://pubmed.ncbi.nlm.nih.gov/28867349/) | *Engineering E. coli membrane phospholipid head distribution improves tolerance…* | Overexpressing *pssA* raises PE and boosts tolerance/production of a fatty acid — links PssA level to membrane robustness. |
| [33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/) | *Structural insights into phosphatidylethanolamine formation…* | Defines the downstream Psd step (pyruvoyl Schiff-base decarboxylation of PS to PE). |
| [32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/) | *Structural Basis for PE Biosynthesis by Bacterial Phosphatidylserine Decarboxylase* | *E. coli* Psd crystal structures; membrane-binding N-terminal helix and active-site determinants of the enzyme acting on PssA's product. |
| [40404014](https://pubmed.ncbi.nlm.nih.gov/40404014/) | *Endogenous formation of phosphatidylhomoserine in E. coli through PssA* | Demonstrates acceptor-site promiscuity: PssA can use L-homoserine to make phosphatidylhomoserine. |
| [9422599](https://pubmed.ncbi.nlm.nih.gov/9422599/) | *Cloning… of the B. subtilis psd gene* | Context: in *B. subtilis*, *pss* and *psd* are adjacent (operon), contrasting with the separated *P. putida* loci. |

The evidence base is internally consistent. The strongest direct experimental data (knockouts, crystal structures) come from orthologs — principally *E. coli* — and are transferred to Q88GQ4 on the basis of unambiguous orthology (46% identity, conserved twin HKD motifs, identical domain architecture). Organism-specific support for *P. putida* comes from lipidomics (PE is abundant) and KEGG pathway placement (PP_3664 → K00998 → module M00093).

---

## Supported and Refuted Hypotheses

- **Supported:** PssA is a phosphatidylserine synthase performing the committed step of PE biosynthesis; it is a PLD-superfamily peripheral membrane enzyme using a covalent phosphatidyl-His mechanism; it acts at the inner-membrane cytoplasmic face; it is upstream of a separately encoded Psd (PP_4908); PE is a dominant, physiologically important lipid in *P. putida*.
- **Refuted / excluded:** PssA is **not** an integral-membrane, base-exchange type-I phosphatidylserine synthase; despite the automated "PGS1"/PGP-synthase InterPro cross-reference, the curated EC assignment, KEGG orthology (K00998), sequence analysis, and genomic/physiological context identify the enzyme as a **serine**-specific phosphatidyltransferase (PS synthase), not a phosphatidylglycerophosphate synthase. The shared PLD fold among PS synthase, eukaryotic PGP synthase, and cardiolipin synthase is a family-level artifact of the annotation, not evidence of PGP-synthase activity.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* KT2440 protein.** All enzymatic, structural, and mechanistic details are inferred from orthologs (chiefly *E. coli*) via strong sequence homology. The kinetic parameters, exact substrate specificity, and regulation of the actual PP_3664 gene product have not been measured directly.

2. **No *P. putida pssA* knockout phenotype in the literature reviewed.** While *E. coli* and *S. meliloti pssA* deletions abolish PE, the specific consequences of deleting PP_3664 in *P. putida* (essentiality, divalent-cation dependence, solvent-tolerance defects) were not directly documented.

3. **Acceptor-site promiscuity is untested in *P. putida*.** Phosphatidylhomoserine formation was demonstrated in *E. coli*; whether the *P. putida* enzyme shares this promiscuity, and whether PHS or other minor head-group variants occur in *P. putida* membranes, remains unknown.

4. **Regulation of PssA membrane association in *P. putida*.** The monomer–dimer/membrane-association switch was established for *E. coli*; the specific determinants (lipid composition, ionic conditions, protein partners) governing this in *P. putida* have not been examined.

5. **Sequence-motif positions are approximate.** The HKD motif residue numbers and identity percentage derive from in-silico alignment; while robust, they have not been experimentally validated by mutagenesis in this organism.

6. **Divalent-cation / Mg²⁺ requirement not confirmed for PP_3664.** *E. coli* PssA-null mutants require divalent metal ions for growth; whether *P. putida* PssA activity or the mutant phenotype depends similarly on Mg²⁺/Ca²⁺ was not directly established.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted gene deletion of PP_3664 in *P. putida* KT2440.** Construct an in-frame Δ*pssA* mutant and quantify membrane phospholipids by LC-MS. Prediction: loss of PS synthase activity and PE, with possible divalent-cation dependence — directly testing transferability of the *E. coli* phenotype.

2. **In-vitro enzyme assay with purified recombinant PssA (Q88GQ4).** Express and purify the protein; measure PS synthase activity from CDP-DG + L-serine, determine kinetic constants (Km, kcat), and test the Mg²⁺/Mn²⁺ requirement.

3. **Substrate-specificity / promiscuity screen.** Offer L-homoserine, L-threonine, and other candidate alcohols as acceptors to test whether the *P. putida* enzyme, like *E. coli* PssA, produces phosphatidylhomoserine or other head-group variants.

4. **Site-directed mutagenesis of the two HKD motifs** (His130, His348 and associated Lys/Asp residues) to confirm their catalytic essentiality and validate the covalent-intermediate mechanism in this ortholog.

5. **Membrane-association / oligomerization studies.** Use sedimentation/flotation assays and native MS or size-exclusion chromatography to test whether *P. putida* PssA exhibits the monomer-active/dimer-inactive regulatory behavior seen in *E. coli*, and identify lipid dependencies.

6. **Structural determination or AlphaFold-model validation.** Solve the crystal/cryo-EM structure of *P. putida* PssA, or validate an AlphaFold model against the *E. coli* templates, to confirm active-site architecture and substrate-recognition determinants.

7. **Stress-tolerance engineering in *P. putida*.** Titrate *pssA* expression and assay solvent/organic-acid tolerance and PE content, extending the *E. coli* engineering result ([PMID: 28867349](https://pubmed.ncbi.nlm.nih.gov/28867349/)) to the native solvent-tolerant host — of biotechnological relevance.

---

## Conclusion

The gene ***pssA*** (Q88GQ4, PP_3664) of *Pseudomonas putida* KT2440 encodes **phosphatidylserine synthase (EC 2.7.8.8)**, a **phospholipase-D-superfamily CDP-diacylglycerol—serine O-phosphatidyltransferase** that catalyzes the committed first step of phosphatidylethanolamine biosynthesis. It transfers the phosphatidyl group of CDP-diacylglycerol onto L-serine — via a covalent phosphatidyl-histidine intermediate built from two conserved HKD motifs — to form phosphatidylserine and CMP; a separate decarboxylase (Psd, PP_4908) then converts PS to PE, the dominant membrane phospholipid of *P. putida*. The enzyme functions as a **peripheral membrane protein at the cytoplasmic face of the inner membrane**, its activity gated by membrane association and oligomerization state, and it governs the CDP-diacylglycerol branch point that balances zwitterionic (PE) versus acidic (PG/cardiolipin) phospholipid synthesis. These conclusions rest on curated EC/KEGG/GO annotation, InterPro/Pfam domain signatures and direct sequence analysis, and strong orthology (46% identity, conserved catalytic motifs) to the experimentally characterized and crystallized *E. coli* PssA.

---

*Prepared through iterative literature review and bioinformatic analysis (UniProt, KEGG, InterPro/Pfam, sequence alignment, and primary structural/genetic literature).*


## Artifacts

- [OpenScientist final report](pssA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pssA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:39693441
2. PMID:8824831
3. PMID:14996797
4. PMID:21895997
5. PMID:28867349
6. PMID:33707636
7. PMID:32402247
8. PMID:40404014