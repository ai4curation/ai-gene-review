---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:23:27.025234'
end_time: '2026-08-31T09:10:49.100701'
duration_seconds: 2842.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pvdA
  gene_symbol: pvdA
  uniprot_accession: Q88GC8
  protein_description: 'SubName: Full=L-ornithine 5-monooxygenase {ECO:0000313|EMBL:AAN69390.1};
    EC=1.13.12.- {ECO:0000313|EMBL:AAN69390.1};'
  gene_info: Name=pvdA {ECO:0000313|EMBL:AAN69390.1}; OrderedLocusNames=PP_3796 {ECO:0000313|EMBL:AAN69390.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the lysine N(6)-hydroxylase/L-ornithine N(5)-
  protein_domains: FAD/NAD-bd_sf. (IPR036188); Lys/Orn_oxygenase. (IPR025700); Lys_Orn_oxgnase
    (PF13434)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pvdA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pvdA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GC8
- **Protein Description:** SubName: Full=L-ornithine 5-monooxygenase {ECO:0000313|EMBL:AAN69390.1}; EC=1.13.12.- {ECO:0000313|EMBL:AAN69390.1};
- **Gene Information:** Name=pvdA {ECO:0000313|EMBL:AAN69390.1}; OrderedLocusNames=PP_3796 {ECO:0000313|EMBL:AAN69390.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the lysine N(6)-hydroxylase/L-ornithine N(5)-
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); Lys/Orn_oxygenase. (IPR025700); Lys_Orn_oxgnase (PF13434)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pvdA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pvdA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pvdA** (gene ID: pvdA, UniProt: Q88GC8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pvdA* (L-Ornithine N⁵-Oxygenase) in *Pseudomonas putida* KT2440

**UniProt:** Q88GC8 | **Locus:** PP_3796 | **Gene:** *pvdA* | **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) | **EC:** 1.14.13.195 (L-ornithine N⁵-monooxygenase; historically 1.13.12.-)

---

## Summary

The gene **pvdA** (UniProt **Q88GC8**, ordered locus **PP_3796**) of *Pseudomonas putida* KT2440 encodes **L-ornithine N⁵-oxygenase (PvdA)**, a soluble, cytoplasmic, **FAD-dependent N-hydroxylating flavoprotein monooxygenase**. Its primary and defining biochemical function is to catalyze the **hydroxylation of the side-chain (Nδ / N⁵) primary amine of L-ornithine**, using **NADPH** as the electron donor and **molecular oxygen** as co-substrate, to yield **N⁵-hydroxy-L-ornithine**. This reaction is the **first committed, dedicated tailoring step** in the biosynthesis of **pyoverdine**, the principal high-affinity fluorescent siderophore of fluorescent pseudomonads. The gene symbol *pvdA*, the protein family assignment (lysine/ornithine N-hydroxylase; Pfam PF13434, InterPro IPR025700), and the organism (*P. putida* KT2440) all match the UniProt record, and the function transfers with high confidence from the well-characterized orthologs in *P. aeruginosa* and *Burkholderia* to Q88GC8.

Mechanistically, PvdA is a **class B flavoprotein monooxygenase** with a three-domain architecture (two Rossmann-like dinucleotide-binding domains for FAD and NADPH plus a substrate-binding domain), solved by X-ray crystallography for the near-identical *P. aeruginosa* ortholog. Its catalytic cycle is distinguished from classical aromatic hydroxylases: **substrate binding is not required to trigger flavin reduction**; instead, ornithine accelerates the reaction of O₂ with reduced flavin (FADH₂) roughly 80-fold, stabilizing a **C4a-(hydro)peroxyflavin intermediate** that transfers an oxygen atom to the ornithine amine. This substrate-triggered O₂ chemistry couples NADPH consumption to productive hydroxylation and minimizes wasteful production of hydrogen peroxide (uncoupling).

Biologically, PvdA operates **within the cytoplasm** as part of a **multi-enzyme "siderosome"** associated with the inner leaflet of the cytoplasmic membrane, supplying N⁵-hydroxy-L-ornithine that is subsequently **N-formylated** (by PvdF) to form the **formyl-hydroxamate groups** that serve as the bidentate Fe(III)-chelating ligands of pyoverdine. Expression of *pvdA* is **strictly iron-regulated**: it is induced under iron limitation via the extracytoplasmic-function (ECF) sigma factor **PvdS** acting on an "iron starvation box" promoter, and repressed under iron sufficiency by the **Fur** regulon. In *P. putida* KT2440 specifically, the downstream mature siderophore is exported by the dedicated **PvdRT-OpmQ** (ABC-type) and **MdtABC-OpmB** (RND-type) efflux systems. In sum, PvdA is the committed enzymatic entry point that channels ornithine into the high-affinity iron-acquisition pathway.

---

## Gene/Protein Identity Verification

Because gene symbols can be ambiguous for less-characterized proteins from non-model organisms, all identity checks were performed and are internally consistent:

- **Symbol:** "pvdA" is the canonical symbol for L-ornithine N⁵-oxygenase across fluorescent pseudomonads ([PMID: 8106324](https://pubmed.ncbi.nlm.nih.gov/8106324/), [PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/)) and *Burkholderia* ([PMID: 10456885](https://pubmed.ncbi.nlm.nih.gov/10456885/)). ✔
- **Organism:** PvdA homologs (~45–48 kDa) are conserved and iron-inducible specifically in *P. putida* among fluorescent pseudomonads ([PMID: 14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/)). ✔
- **Family/domains:** Class B FAD-dependent N-hydroxylating monooxygenase with two Rossmann dinucleotide-binding folds plus a substrate-binding domain, matching PF13434 / IPR025700 ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)). ✔

**Caveat noted up front:** The most detailed biochemical and structural studies were performed on the near-identical *P. aeruginosa* PAO1 ortholog (also named PvdA). Given strong sequence conservation and shared iron-inducible expression in *P. putida* ([PMID: 14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/)), these mechanistic conclusions transfer to the KT2440 protein (Q88GC8 / PP_3796). This is a genuine functional annotation, not a case of mistaken identity.

---

## Key Findings

### Finding 1 — pvdA encodes L-ornithine N⁵-oxygenase, catalyzing the first committed step of pyoverdine biosynthesis

The identity of Q88GC8/PP_3796 as **L-ornithine N⁵-oxygenase** is firmly established by convergent gene-symbol, protein-family, and organism matches to the UniProt record, and by transferable functional evidence from orthologs. The founding biochemical description came from *P. aeruginosa*, where the enzyme was defined as catalyzing "the hydroxylation of L-ornithine (L-Orn), which represents an early step in the biosynthesis of the peptidic moiety of the fluorescent siderophore pyoverdin in *Pseudomonas aeruginosa*" ([PMID: 8106324](https://pubmed.ncbi.nlm.nih.gov/8106324/)). Genetic evidence confirms causality: in *P. aeruginosa* PAO1, *pvdA* mutants lose both pyoverdine production and L-ornithine N⁵-oxygenase activity, and this is restored by trans-complementation.

The gene identity and its role as the committed entry point are corroborated in a second genus. In *Burkholderia cepacia*, *pvdA* was characterized as "a *pvdA* homolog, the gene for the enzyme L-ornithine N(5)-oxygenase, which catalyzes the hydroxylation of L-ornithine" ([PMID: 10456885](https://pubmed.ncbi.nlm.nih.gov/10456885/)); the mutant fails to make the siderophore ornibactin and is rescued by feeding the hydroxylated precursor L-N⁵-OH-ornithine — directly demonstrating that PvdA operates upstream of, and supplies the hydroxamate precursor to, siderophore assembly. This "rescue by intermediate" experiment is the strongest possible genetic proof that PvdA's product is an obligatory pathway intermediate.

Critically for the transfer of function to the *P. putida* KT2440 protein, immunochemical and *in silico* work showed that "45–48 kDa PvdA homologues are expressed in response to iron limitation by different species and strains of fluorescent pseudomonads" ([PMID: 14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/)), establishing that PvdA orthologs — including in *P. putida* — are conserved in size, sequence, and iron-regulated expression. Together, these three independent lines of evidence make the annotation of Q88GC8 as L-ornithine N⁵-oxygenase highly secure.

**Reaction catalyzed:**

```
L-ornithine + NADPH + H⁺ + O₂  →  N⁵-hydroxy-L-ornithine + NADP⁺ + H₂O
```

### Finding 2 — PvdA is a class B FAD-dependent N-hydroxylating flavoprotein monooxygenase with a three-domain architecture

PvdA belongs to the **class B flavoprotein monooxygenases**, the same mechanistic superfamily as the flavin-containing monooxygenases (FMOs) and Baeyer-Villiger monooxygenases. These enzymes "catalyze the oxidation of substrates using NADPH as the electron donor and molecular oxygen" ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)). PvdA therefore has an obligate requirement for three components: the **FAD** cofactor, the **NADPH** reductant, and **O₂** as the oxygen source for the hydroxyl group.

Two X-ray structures of the *P. aeruginosa* ortholog (oxidized FAD at 1.9 Å; reduced FAD at 3.03 Å) revealed the architecture: "PvdA has the two expected Rossmann-like dinucleotide-binding domains for FAD and NADPH and also a substrate-binding domain, with the active site at the interface between the three domains" ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)). NADP(H) and (hydroxy)ornithine were captured in a **solvent-exposed active site**, giving direct structural evidence for substrate and cosubstrate specificity and rationalizing PvdA's relatively weak FAD binding. This three-domain plan (FAD domain, NAD(P)H domain, substrate domain) is shared across the N-hydroxylating monooxygenase family, including the ornithine hydroxylases PvdA (*P. aeruginosa*) and SidA (*Aspergillus fumigatus*) and the lysine hydroxylase KtzI. PvdA/SidA/KtzI are **ornithine-specific and strictly NADPH-specific**, contrasting with the *Nocardia* lysine monooxygenase NbtG, which accepts both NADH and NADPH — underscoring that PvdA's substrate and cofactor selectivity is a defining, discriminating feature rather than a generic family trait.

| Property | PvdA (ornithine N⁵-oxygenase) |
|---|---|
| Enzyme class | Class B flavoprotein monooxygenase |
| Cofactor | FAD (relatively weakly bound) |
| Electron donor | NADPH (strictly; not NADH) |
| Oxygen source | Molecular O₂ |
| Substrate | L-ornithine (side-chain N⁵/Nδ amine) |
| Domains | FAD-binding, NADPH-binding (Rossmann-like) + substrate-binding |
| Active site | At the interface of the three domains; solvent-exposed |
| Approx. mass | ~45–48 kDa |

### Finding 3 — Catalysis proceeds via substrate-triggered O₂ addition (not substrate-triggered flavin reduction), coupling NADPH oxidation to hydroxylation

Transient-kinetic (stopped-flow) analysis of *P. aeruginosa* PvdA revealed a mechanism that departs from the classical paradigm of aromatic hydroxylases such as p-hydroxybenzoate hydroxylase. In PvdA, "binding of the hydroxylation target is not required to trigger reduction of the flavin by NADPH: the reductive half-reaction is equally facile in the presence and absence of ornithine" ([PMID: 19368334](https://pubmed.ncbi.nlm.nih.gov/19368334/)). This means the flavin can be reduced by NADPH before the substrate is present.

The point of substrate control lies instead in the **oxidative half-reaction**: "Reaction of O₂ with FADH₂ in the oxidative half-reaction is accelerated by ornithine 80-fold, providing a mechanism by which PvdA can ensure coupling of NADPH and ornithine oxidation" ([PMID: 19368334](https://pubmed.ncbi.nlm.nih.gov/19368334/)). When ornithine is present, a **C4a-hydroperoxyflavin intermediate** (absorbing near ~390 nm) accumulates and decays to the C4a-hydroxyflavin in a kinetically competent manner — this is the oxygen-transferring species that hydroxylates the amine. Without ornithine, the enzyme "uncouples," discharging the reactive oxygen as stoichiometric **H₂O₂** rather than making hydroxyornithine. The retained NADP⁺ shelters the reactive flavin intermediate from solvent, further coupling NADPH oxidation to productive hydroxylation ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)).

The ~80-fold acceleration therefore acts as a gating device: it ensures that the potentially damaging peroxyflavin oxidant is deployed for productive hydroxylation only when the substrate is bound, conserving NADPH and limiting reactive-oxygen byproducts. The importance of tight coupling is highlighted by contrast with the *Nocardia* homolog NbtG, which is "highly uncoupled, producing more superoxide and hydrogen peroxide than hydroxylated Lys" owing to an occluded NADPH-domain conformation ([PMID: 25802330](https://pubmed.ncbi.nlm.nih.gov/25802330/)).

### Finding 4 — pvdA is cytoplasmic and iron-starvation-regulated (Fur/PvdS), feeding a pathway whose product is exported by dedicated efflux systems in P. putida KT2440

PvdA functions as a **soluble cytoplasmic enzyme**. Its transcription is tightly coupled to iron status through two regulatory arms. Under iron limitation, *pvdA* is activated by the ECF (σ^E-like) sigma factor **PvdS**: promoter mapping in *P. aeruginosa* identified "a sequence motif resembling the −10 hexamer of AlgU-dependent promoters and the iron starvation box of pyoverdin genes controlled by the sigmaE-like factor PvdS ... 5′ of the T1 start site" ([PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/)). Under iron sufficiency, the ferric-uptake regulator **Fur** represses the system; "two fur mutants of *P. aeruginosa* were much less responsive than wild-type PAO1 to the iron-dependent regulation of pvdA expression" ([PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/)). This PvdS-on / Fur-off logic restricts PvdA production to conditions of iron starvation, consistent with its dedicated role in high-affinity iron acquisition.

PvdA's soluble product, N⁵-hydroxyornithine, is incorporated into the pyoverdine peptide backbone; the mature siderophore is then secreted. In *P. putida* KT2440 specifically, pyoverdine secretion is handled by dedicated efflux machinery — "the PvdRT-OpmQ system was shown to contribute to pyoverdine secretion in *P. putida* KT2440" ([PMID: 30346656](https://pubmed.ncbi.nlm.nih.gov/30346656/)) — together with the RND system MdtABC-OpmB. Biochemical work on the KT2440 transporter has provided "the first biochemical evidence for direct interactions between pyoverdine and PvdRT" ([PMID: 36807028](https://pubmed.ncbi.nlm.nih.gov/36807028/)), placing PvdA's upstream chemistry firmly within the KT2440 pyoverdine pathway.

### Finding 5 — PvdA's product N⁵-hydroxy-L-ornithine is N-formylated to the formyl-hydroxamate that constitutes pyoverdine's iron-chelating groups

The biological purpose of PvdA's hydroxylation becomes clear one step downstream: the newly installed side-chain hydroxylamine is **N-formylated** to build the iron-binding functional group of the siderophore. As stated for the family, PvdA performs "hydroxylation of the side chain amine of ornithine, which is subsequently formylated to generate the iron-chelating hydroxamates of the siderophore pyoverdin" ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)). Structural/NMR analysis of *Pseudomonas* pyoverdine precursors confirms the chemistry: the pyoverdine precursor "ferribactin is a nonapeptide that contains two residues each of lysine and N6-formyl-N6-hydroxyornithine" ([PMID: 6211451](https://pubmed.ncbi.nlm.nih.gov/6211451/)). These **formyl-hydroxamic acid** residues act as bidentate Fe(III) ligands (with the catechol-type chromophore completing the hexadentate coordination sphere). Thus, PvdA supplies the essential chemical precursor (the N-hydroxyl group) that, after formylation, forms the hydroxamate chelating "teeth" that give pyoverdine its extraordinary iron affinity.

### Finding 6 — PvdA acts within a cytoplasmic multi-enzyme "siderosome," preceding periplasmic maturation and export

The spatial context of PvdA's activity has been resolved to a specific subcellular organization. Pyoverdine (PVDI) "assembly requires the coordinated action of seven cytoplasmic enzymes and is followed by a periplasmic maturation before secretion of the siderophore into the extracellular medium by the efflux system PvdRT-OpmQ" ([PMID: 25697961](https://pubmed.ncbi.nlm.nih.gov/25697961/)). Moreover, "the cytoplasmic enzymes involved in each of these two siderophore biosynthesis pathways can form siderophore-specific multi-enzymatic complexes called siderosomes associated with the inner leaflet of the cytoplasmic membrane" ([PMID: 25697961](https://pubmed.ncbi.nlm.nih.gov/25697961/)). As the ornithine N⁵-hydroxylase, **PvdA is one of these cytoplasmic precursor-supplying enzymes**. The siderosome model proposes that substrate channeling between enzymes prevents metal-chelating intermediates (such as hydroxamate-bearing precursors) from diffusing freely through the cytoplasm, where they could sequester intracellular metals — an elegant solution to the hazard of manufacturing a powerful chelator inside the cell.

---

## Mechanistic Model / Interpretation

PvdA is best understood as the **committed enzymatic entry point** that channels a primary metabolite (L-ornithine, derived from arginine/glutamate metabolism) into the specialized secondary-metabolic pathway of pyoverdine iron acquisition. The following schematic integrates the six findings into a single narrative from gene regulation through extracellular iron capture:

```
        IRON-LIMITED ENVIRONMENT
                 │
        (Fur repression relieved; PvdS activates "iron starvation box")   [F004]
                 │
                 ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                    CYTOPLASM  (SIDEROSOME)   [F006]           │
   │                                                              │
   │   L-ornithine                                                │
   │        │                                                     │
   │        │  PvdA: class B FAD monooxygenase  [F001, F002]      │
   │        │  NADPH + O2 → C4a-(hydro)peroxyflavin               │
   │        │  substrate-triggered O2 addition (~80x)  [F003]     │
   │        ▼                                                     │
   │   N5-hydroxy-L-ornithine                                     │
   │        │                                                     │
   │        │  N-formylation (PvdF)   [F005]                      │
   │        ▼                                                     │
   │   N5-formyl-N5-hydroxy-L-ornithine  (formyl-hydroxamate)     │
   │        │                                                     │
   │        │  NRPS assembly into peptide backbone                │
   │        ▼                                                     │
   │   Ferribactin / pyoverdine precursor                         │
   └───────────────────────────────┬─────────────────────────────┘
                                    │ periplasmic maturation  [F006]
                                    ▼
                    PvdRT-OpmQ (ABC) / MdtABC-OpmB (RND)  [F004]
                                    │ export
                                    ▼
                     Extracellular PYOVERDINE ── Fe(III) ──► uptake
                     (hydroxamate teeth = PvdA's product)   [F005]
```

**Why the mechanism matters.** PvdA solves a specific chemical problem: primary amines are not intrinsically good metal ligands, but **hydroxamates are** — they are among the strongest bidentate O,O-chelators for hard Fe(III). By installing an N-hydroxyl on the ornithine side chain, PvdA creates the chemical handle that, after formylation, becomes the hydroxamate chelating group. The enzyme's kinetic design (Finding 3) is tuned to this biosynthetic responsibility: because the C4a-peroxyflavin oxidant is reactive and NADPH is metabolically expensive (siderophore production draws heavily on carbon and reducing power, especially in iron-starved cells), the ~80-fold substrate-triggered acceleration of O₂ addition ensures the oxidant is spent almost exclusively on productive hydroxylation rather than on futile H₂O₂ generation. The siderosome organization (Finding 6) complements this by keeping the nascent chelating precursors physically sequestered and channeled, protecting the cell from self-chelation of its own iron and other metals.

**Localization summary.** PvdA carries out its function **in the cytoplasm** (soluble, likely membrane-proximal within the inner-leaflet-associated siderosome). Its product is processed and matured through the cytoplasm and periplasm, and the finished siderophore acts **extracellularly** to scavenge Fe(III). The gene product itself does not leave the cytoplasm.

**Pathway placement.** PvdA is the **first committed tailoring enzyme** of pyoverdine biosynthesis (an "early step"), upstream of the formyltransferase (PvdF) and the non-ribosomal peptide synthetase (NRPS) machinery, and upstream of the periplasmic maturation and efflux (PvdRT-OpmQ / MdtABC-OpmB) steps. It sits at the interface between primary amino-acid metabolism and specialized siderophore biosynthesis.

**Biological significance (KT2440 context).** *P. putida* KT2440 is a non-pathogenic, plant-beneficial soil bacterium. Pyoverdine is its principal high-affinity iron-scavenging system, essential for growth and rhizosphere/soil colonization under the iron-limited conditions typical of natural environments. In *P. putida*, pyoverdine production is additionally modulated by arginine (ornithine-precursor) metabolism and linked to oxidative-stress adaptation ([PMID: 31451546](https://pubmed.ncbi.nlm.nih.gov/31451546/)), and siderophore biosynthesis is metabolically prioritized under iron scarcity via hierarchical carbon-flux routing ([PMID: 33273114](https://pubmed.ncbi.nlm.nih.gov/33273114/)). By providing the hydroxamate iron-ligand precursor, PvdA is indispensable for functional pyoverdine and therefore for iron homeostasis; the enzyme has no known role outside siderophore biosynthesis — its function is narrow and pathway-specific rather than pleiotropic.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [8106324](https://pubmed.ncbi.nlm.nih.gov/8106324/) | *Cloning and sequence of pvdA encoding L-ornithine N⁵-oxygenase (P. aeruginosa)* | **Foundational.** Defines the reaction and its role as an early step in pyoverdine biosynthesis (F001). |
| [10456885](https://pubmed.ncbi.nlm.nih.gov/10456885/) | *pvdA / L-ornithine N⁵-oxygenase in Burkholderia (ornibactin)* | Confirms gene identity across genera; mutant rescued by hydroxylated precursor (F001). |
| [14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/) | *Expression of PvdA in fluorescent Pseudomonas species* | Shows PvdA orthologs (incl. *P. putida*) are conserved and iron-regulated — supports transfer of function to Q88GC8 (F001). |
| [21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/) | *Two structures of ornithine hydroxylase (P. aeruginosa)* | **Structural cornerstone.** Class B assignment, three-domain architecture, cofactor requirements, and downstream formylation to hydroxamate (F002, F005). |
| [19368334](https://pubmed.ncbi.nlm.nih.gov/19368334/) | *Kinetic mechanism of ornithine hydroxylase (PvdA)* | **Mechanistic cornerstone.** Substrate-triggered O₂ addition (~80×), coupling of NADPH/ornithine oxidation, C4a-peroxyflavin (F003). |
| [8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/) | *Iron-regulated transcription of pvdA: Fur and PvdS* | Establishes PvdS activation via iron-starvation box and Fur repression (F004). |
| [30346656](https://pubmed.ncbi.nlm.nih.gov/30346656/) | *PvdRT-OpmQ and MdtABC-OpmB efflux in P. putida KT2440* | Places downstream product export in the specific KT2440 pathway (F004). |
| [36807028](https://pubmed.ncbi.nlm.nih.gov/36807028/) | *PvdRT-OpmQ ABC pump of P. putida KT2440* | Biochemical evidence for direct pyoverdine–PvdRT interaction (F004). |
| [6211451](https://pubmed.ncbi.nlm.nih.gov/6211451/) | *Siderochromes from P. fluorescens (NMR)* | Confirms formyl-hydroxyornithine as the chelating residue in the precursor ferribactin (F005). |
| [25697961](https://pubmed.ncbi.nlm.nih.gov/25697961/) | *Cellular organization of siderophore biosynthesis: siderosomes* | Cytoplasmic seven-enzyme assembly and inner-membrane-associated siderosome (F006). |
| [25802330](https://pubmed.ncbi.nlm.nih.gov/25802330/) | *Lysine monooxygenase NbtG structure* | **Contrast case.** Highlights PvdA's tight coupling and NADPH specificity vs. the uncoupled, dual-cofactor NbtG (F002, F003). |
| [21871647](https://pubmed.ncbi.nlm.nih.gov/21871647/) | *Review: N-hydroxylating flavoprotein monooxygenases* | Authoritative review synthesizing PvdA/SidA/IucD kinetics and structure. |
| [30386787](https://pubmed.ncbi.nlm.nih.gov/30386787/) | *The biosynthesis of pyoverdines (review)* | Contextualizes PvdA within the whole pyoverdine pathway and its ecological role. |
| [31451546](https://pubmed.ncbi.nlm.nih.gov/31451546/) | *Arginine biosynthesis modulates pyoverdine in P. putida* | Links ornithine/arginine precursor supply to pyoverdine output in KT2440. |
| [33273114](https://pubmed.ncbi.nlm.nih.gov/33273114/) | *Hierarchical carbon routing favors iron-scavenging in soil Pseudomonas* | Shows metabolic prioritization of siderophore biosynthesis under iron scarcity. |

**Consistency of the evidence.** The functional annotation is unusually robust for a non-model-organism protein because it rests on three independent pillars: (1) **genetic** evidence (loss-of-function mutants abolish siderophore production, rescued by trans-complementation or by the hydroxylated precursor), (2) **enzymological** evidence (purified enzyme activity, transient kinetics, defined cofactor requirements), and (3) **structural** evidence (two crystal structures with bound NADP(H) and (hydroxy)ornithine). No paper in the reviewed corpus challenges the core assignment; the only "contrast" case (NbtG, [PMID: 25802330](https://pubmed.ncbi.nlm.nih.gov/25802330/)) actually sharpens PvdA's annotation by showing which properties (strict NADPH use, tight coupling) are specific to the ornithine hydroxylases.

---

## Supported and Refuted Hypotheses

**Supported:**
- **H1:** pvdA / Q88GC8 = L-ornithine N⁵-oxygenase catalyzing L-Orn side-chain N-hydroxylation. **Supported** ([PMID: 8106324](https://pubmed.ncbi.nlm.nih.gov/8106324/), [PMID: 10456885](https://pubmed.ncbi.nlm.nih.gov/10456885/), [PMID: 14684153](https://pubmed.ncbi.nlm.nih.gov/14684153/)).
- **H2:** It is a class B FAD/NADPH/O₂ monooxygenase with a defined three-domain fold. **Supported** ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)).
- **H3:** Catalysis proceeds via a C4a-(hydro)peroxyflavin, with substrate-triggered O₂ addition ensuring coupling. **Supported** ([PMID: 19368334](https://pubmed.ncbi.nlm.nih.gov/19368334/)).
- **H4:** Cytoplasmic function under PvdS/Fur iron-starvation control, feeding pyoverdine assembly/export. **Supported** ([PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/), [PMID: 30346656](https://pubmed.ncbi.nlm.nih.gov/30346656/)).

**Refuted / distinguished:**
- PvdA is **not** a broad-specificity lysine/diamine N-hydroxylase and **not** NADH-utilizing (contrast NbtG; [PMID: 25802330](https://pubmed.ncbi.nlm.nih.gov/25802330/)) — PvdA is L-ornithine- and NADPH-specific.

---

## Limitations and Knowledge Gaps

1. **Direct biochemistry is from orthologs, not Q88GC8 itself.** The detailed kinetic and structural characterization was performed on the *P. aeruginosa* PvdA (and the fungal ortholog SidA), not on the *P. putida* KT2440 protein (Q88GC8). Function is transferred by strong homology, conserved iron-regulated expression, and shared domain architecture, but the *P. putida* enzyme's specific kinetic parameters (kcat, KM for ornithine and NADPH), coupling efficiency, and structure have not been directly measured in the reviewed literature.

2. **Substrate specificity boundaries are inferred.** PvdA is described as ornithine-specific, but the family contains examples of related N-hydroxylases with broader scope (e.g., the cadaverine/putrescine/lysine-accepting DesB, [PMID: 33784308](https://pubmed.ncbi.nlm.nih.gov/33784308/)). Whether *P. putida* PvdA has any minor activity on lysine or diamines has not been experimentally excluded for Q88GC8.

3. **Siderosome membership is a general model.** The siderosome/substrate-channeling model ([PMID: 25697961](https://pubmed.ncbi.nlm.nih.gov/25697961/)) was elaborated primarily in *P. aeruginosa*. PvdA's precise stoichiometry, protein–protein contacts, and membrane-association geometry within the *P. putida* siderosome are not directly established.

4. **Formyltransferase identity in KT2440.** The formylation step downstream of PvdA (attributed to PvdF) is well established in *P. aeruginosa*; the reviewed evidence confirms the chemistry (formyl-hydroxyornithine) but does not directly characterize the KT2440 formyltransferase acting on PvdA's product.

5. **Regulatory details are cross-species.** The PvdS/Fur regulatory logic is best documented in *P. aeruginosa*. While *P. putida* PvdA is confirmed iron-regulated, the exact promoter architecture and the KT2440-specific regulatory network (including autoinduction differences noted for the *fluorescens–putida* group) warrant KT2440-specific confirmation.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymology on Q88GC8.** Heterologously express and purify *P. putida* KT2440 PvdA; confirm FAD content, and measure steady-state and transient kinetics (kcat, KM for L-ornithine, NADPH, O₂), coupling efficiency (H₂O₂ vs. hydroxyornithine), and detection of the C4a-(hydro)peroxyflavin intermediate by stopped-flow — replicating the *P. aeruginosa* study ([PMID: 19368334](https://pubmed.ncbi.nlm.nih.gov/19368334/)) in the KT2440 enzyme.

2. **Substrate-specificity panel.** Assay purified KT2440 PvdA against L-ornithine, L-lysine, putrescine, and cadaverine (Csáky / NADPH-oxidation / O₂-consumption assays) to define whether specificity is as strict as in *P. aeruginosa* PvdA or broader, as in DesB.

3. **Genetic confirmation in KT2440.** Construct a clean *pvdA* (PP_3796) deletion in *P. putida* KT2440; verify loss of pyoverdine (fluorescence/CAS assay) under iron limitation and rescue by exogenous N⁵-hydroxy-L-ornithine and by trans-complementation, mirroring the *Burkholderia* rescue experiment ([PMID: 10456885](https://pubmed.ncbi.nlm.nih.gov/10456885/)).

4. **Structural determination.** Solve the crystal or cryo-EM structure of KT2440 PvdA (ideally with NADP⁺ and hydroxyornithine bound) to confirm the three-domain architecture and active-site geometry, and compare active-site residues to *P. aeruginosa* PvdA and SidA.

5. **Siderosome interaction mapping.** Use pulldowns / BN-PAGE, in-cell crosslinking, or fluorescence co-localization to test whether KT2440 PvdA physically associates with PvdF, the NRPS enzymes, and the inner membrane, and to probe substrate channeling of the reactive hydroxamate precursor.

6. **Regulatory dissection in KT2440.** Map the *pvdA* promoter and quantify PvdS-dependent activation and Fur-dependent repression under defined iron regimes; integrate with the observed link between arginine/ornithine precursor supply and pyoverdine output ([PMID: 31451546](https://pubmed.ncbi.nlm.nih.gov/31451546/)).

---

## Conclusion

The evidence is strong and internally consistent: **pvdA (Q88GC8 / PP_3796) encodes L-ornithine N⁵-oxygenase**, a cytoplasmic, class B FAD/NADPH/O₂-dependent N-hydroxylating flavoprotein monooxygenase that catalyzes the first committed tailoring step of pyoverdine siderophore biosynthesis — hydroxylating the ornithine side-chain amine to N⁵-hydroxy-L-ornithine, which is subsequently N-formylated into the hydroxamate iron-chelating groups of pyoverdine. Catalysis proceeds through a C4a-(hydro)peroxyflavin intermediate with substrate-triggered O₂ addition that couples NADPH oxidation to productive hydroxylation, and the gene is expressed only under iron limitation via PvdS/Fur regulation as part of high-affinity iron acquisition. The primary caveat is that the detailed biochemistry derives from close orthologs rather than the KT2440 protein itself, though homology, conserved iron-regulated expression, and shared architecture make the functional transfer secure.


## Artifacts

- [OpenScientist final report](pvdA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pvdA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8106324
2. PMID:8636031
3. PMID:10456885
4. PMID:14684153
5. PMID:21757711
6. PMID:19368334
7. PMID:25802330
8. PMID:30346656
9. PMID:36807028
10. PMID:6211451
11. PMID:25697961
12. PMID:31451546
13. PMID:33273114
14. PMID:33784308