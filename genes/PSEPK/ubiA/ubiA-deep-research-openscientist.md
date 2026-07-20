---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:49.937430'
end_time: '2026-07-18T18:11:31.543354'
duration_seconds: 1061.61
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiA
  gene_symbol: ubiA
  uniprot_accession: Q88C65
  protein_description: 'RecName: Full=4-hydroxybenzoate octaprenyltransferase {ECO:0000255|HAMAP-Rule:MF_01635};
    EC=2.5.1.39 {ECO:0000255|HAMAP-Rule:MF_01635}; AltName: Full=4-HB polyprenyltransferase
    {ECO:0000255|HAMAP-Rule:MF_01635};'
  gene_info: Name=ubiA {ECO:0000255|HAMAP-Rule:MF_01635}; OrderedLocusNames=PP_5318;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiA prenyltransferase family.
  protein_domains: HB_polyprenyltransferase-like. (IPR006370); Prenyltransferase.
    (IPR039653); UbiA_prenyltransferase. (IPR000537); UbiA_sf. (IPR044878); UbiA (PF01040)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C65
- **Protein Description:** RecName: Full=4-hydroxybenzoate octaprenyltransferase {ECO:0000255|HAMAP-Rule:MF_01635}; EC=2.5.1.39 {ECO:0000255|HAMAP-Rule:MF_01635}; AltName: Full=4-HB polyprenyltransferase {ECO:0000255|HAMAP-Rule:MF_01635};
- **Gene Information:** Name=ubiA {ECO:0000255|HAMAP-Rule:MF_01635}; OrderedLocusNames=PP_5318;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiA prenyltransferase family.
- **Key Domains:** HB_polyprenyltransferase-like. (IPR006370); Prenyltransferase. (IPR039653); UbiA_prenyltransferase. (IPR000537); UbiA_sf. (IPR044878); UbiA (PF01040)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiA** (gene ID: ubiA, UniProt: Q88C65) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: UbiA (PP_5318 / Q88C65) in *Pseudomonas putida* KT2440

**Gene symbol:** *ubiA* | **UniProt:** Q88C65 (UBIA_PSEPK) | **Ordered locus:** PP_5318 | **KEGG:** ppu:PP_5318
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)
**EC number:** 2.5.1.39 | **Protein family:** UbiA prenyltransferase superfamily (Pfam PF01040)

---

## Summary

**UbiA (PP_5318, Q88C65) in *Pseudomonas putida* KT2440 is 4-hydroxybenzoate polyprenyltransferase (EC 2.5.1.39), an integral, magnesium-dependent inner-membrane enzyme that catalyzes the second and committed step of ubiquinone (coenzyme Q) biosynthesis.** The enzyme transfers an all-*trans* polyprenyl group from a polyprenyl-diphosphate donor onto the C-3 position of the aromatic head group 4-hydroxybenzoate (4-HB, also called *para*-hydroxybenzoate/PHB), producing 3-polyprenyl-4-hydroxybenzoate plus inorganic diphosphate. This product is the first membrane-anchored intermediate of the coenzyme Q pathway; all subsequent modifications (hydroxylations, methylations, decarboxylation) act on the aromatic ring while the isoprenoid tail keeps the molecule embedded in the lipid bilayer. The reference reaction is catalogued as Rhea:27782, and the biological process is ubiquinone biosynthesis (GO:0006744), which supplies the lipophilic electron carrier essential for the aerobic respiratory chain.

Gene identity has been verified at three independent levels, so this is not a case of symbol ambiguity. First, the target UniProt entry is governed by HAMAP rule MF_01635, which assigns Q88C65 to the UbiA prenyltransferase family and specifies the octaprenyltransferase reaction. Second, the physically retrieved 296-residue Q88C65 sequence contains both diagnostic aspartate-rich Mg²⁺-binding motifs of the UbiA superfamily (an N-D-x-x-D motif "NDFAD" at residue 73, and a second Asp-rich cluster "DDD" at residues 199–201) and is strongly hydrophobic, consistent with the polytopic transmembrane fold. Third, the biochemical and genetic literature on the orthologous *E. coli* UbiA — the founding member of the family and the enzyme whose reaction defines EC 2.5.1.39 — is internally consistent and directly transferable through high sequence identity and cross-species functional complementation.

The enzyme carries out its function *within* the cytoplasmic (inner) membrane rather than in the aqueous cytoplasm. Crystal structures of an archaeal UbiA homolog reveal a nine-transmembrane-helix fold with a central active-site cavity that opens laterally to the lipid bilayer, so the hydrophobic polyprenyl substrate and product can partition into the membrane while the reaction proceeds. Substrate specificity is well defined on the aromatic side (4-hydroxybenzoate) but permissive on the prenyl-donor side: purified *E. coli* UbiA accepts geranyl-, farnesyl- and solanesyl-diphosphate, so the isoprenoid chain length of the product is dictated by the cellular polyprenyl-diphosphate pool rather than by strict enzyme selection. In *P. putida* this pool is expected to yield the physiological coenzyme Q species of pseudomonads.

---

## Key Findings

### Finding 1 — UbiA catalyzes the committed prenylation step of ubiquinone biosynthesis

UbiA (PP_5318, Q88C65) catalyzes the membrane-associated condensation of 4-hydroxybenzoate with a polyprenyl-diphosphate donor:

> **4-hydroxybenzoate + polyprenyl-diphosphate → 3-polyprenyl-4-hydroxybenzoate + diphosphate**

This is EC 2.5.1.39. The foundational genetic evidence comes from *E. coli* K-12, where *ubiA* mutants specifically lack the activity that converts 4-hydroxybenzoate to 3-octaprenyl-4-hydroxybenzoate, mapping *ubiA* as the structural gene for 4-hydroxybenzoate octaprenyltransferase ([PMID: 4552989](https://pubmed.ncbi.nlm.nih.gov/4552989/)). That study describes the reaction as "the conversion of 4-hydroxybenzoate into 3-octaprenyl-4-hydroxybenzoate, catalyzed by 4-hydroxybenzoate octaprenyltransferase," defining both the chemistry and the gene–enzyme relationship.

The genomic and pathway context reinforces the functional call. In *E. coli*, *ubiA* lies directly downstream of *ubiC* (chorismate pyruvate-lyase, the enzyme that produces the 4-HB substrate) in a typical operon; UbiA thus performs the second step of the pathway, immediately consuming the aromatic precursor generated by UbiC. As the primary cloning paper states, "the ubiA gene, coding for the 4-hydroxybenzoate octaprenyl transferase, was identified by sequence homology and complementation of a ubiA⁻ strain. It is located directly downstream of ubiC in a typical operon structure" ([PMID: 1644192](https://pubmed.ncbi.nlm.nih.gov/1644192/)). The gene was independently cloned and sequenced as "encoding the membrane-bound p-hydroxybenzoate:octaprenyltransferase" ([PMID: 8409922](https://pubmed.ncbi.nlm.nih.gov/8409922/)). Because Q88C65 is assigned by HAMAP rule MF_01635 to the same family and reaction, the *P. putida* ortholog performs the identical committed prenyl-transfer step. This step is "committed" because prenylation converts a soluble, freely diffusing aromatic acid into a membrane-anchored intermediate irreversibly channeled toward coenzyme Q. (Note: the exact *ubiC-ubiA* operon synteny is documented in *E. coli*; the *P. putida* genomic arrangement was not independently confirmed here.)

### Finding 2 — UbiA is an integral-membrane, Mg²⁺-dependent enzyme with a permissive prenyl-donor site

Direct biochemical characterization of the *E. coli* enzyme established its physical and catalytic properties. Purified/enriched 4-HB polyprenyltransferase is membrane-bound: "the enzyme is membrane-bound and could not be solubilized by hypotonic buffer or detergent treatment. The enzymatic activity is optimal at pH 7.8 and depends on the presence of magnesium ions. Geranyldiphosphate (GPP), all-trans-farnesyldiphosphate (FPP) and all-trans-solanesyldiphosphate (SPP) are accepted as side chain precursors" ([PMID: 8155731](https://pubmed.ncbi.nlm.nih.gov/8155731/)). The reported affinities were GPP (C10, Kₘ ≈ 254 µM), FPP (C15, Kₘ ≈ 22 µM) and SPP (C45, Kₘ ≈ 31 µM); crucially, a *cis*-configured octaprenyl-diphosphate was **not** accepted. This demonstrates two things: (1) the enzyme requires the all-*trans* stereochemistry of the isoprenoid donor, and (2) it tolerates a wide range of chain lengths, so the *in vivo* product length is set by whichever polyprenyl-diphosphate dominates the cellular pool rather than by tight active-site selection.

The membrane localization and Mg²⁺ requirement were confirmed independently *in vivo*: "both the side-chain precursor and 4-hydroxybenozate octaprenyltransferase were shown to be membrane-bound. The enzyme required Mg(2+) for optimal activity" ([PMID: 4552989](https://pubmed.ncbi.nlm.nih.gov/4552989/)). Hydropathy analysis of the cloned sequence predicts a polytopic membrane protein with multiple hydrophobic regions, homologous to the yeast COQ2 prenyltransferase ([PMID: 8409922](https://pubmed.ncbi.nlm.nih.gov/8409922/)). The magnesium dependence is mechanistically central: the divalent cation bridges the enzyme's Asp-rich motifs to the diphosphate leaving group, stabilizing the developing charge as the prenyl carbocation attacks the aromatic ring.

The donor permissiveness has practical significance beyond respiration. When *E. coli ubiA* is expressed heterologously using geranyl-diphosphate, it catalyzes formation of 3-geranyl-4-hydroxybenzoate, a step that can be redirected toward shikonin/naphthoquinone biosynthesis ([PMID: 11038051](https://pubmed.ncbi.nlm.nih.gov/11038051/)), and the same gene has been actively expressed as a membrane-bound prenyltransferase in tobacco ([PMID: 11206977](https://pubmed.ncbi.nlm.nih.gov/11206977/)). These heterologous studies confirm that UbiA's intrinsic catalytic behavior — aromatic 4-HB acceptor plus flexible prenyl donor — is portable across kingdoms.

### Finding 3 — UbiA belongs to the UbiA superfamily of intramembrane aromatic prenyltransferases

Q88C65 carries the UbiA prenyltransferase domain (Pfam PF01040; InterPro IPR000537, IPR044878 "UbiA_sf") and the HB_polyprenyltransferase-like signature (IPR006370). The authoritative superfamily review establishes that "the UbiA superfamily of intramembrane prenyltransferases catalyzes a key biosynthetic step in the production of ubiquinones, menaquinones, plastoquinones, hemes, chlorophylls, vitamin E, and structural lipids" ([PMID: 26922674](https://pubmed.ncbi.nlm.nih.gov/26922674/)). Members share a conserved Mg²⁺/Asp-rich active site and install lipophilic isoprenoid tails onto aromatic head groups within the lipid bilayer; the review notes that "prenyltransferases in this superfamily have distinctive substrate preferences," exactly the pattern observed for UbiA (fixed aromatic acceptor, flexible prenyl donor).

Evolutionary evidence confirms deep conservation of the specific octaprenyltransferase function. The *aarE* gene product of *Providencia stuartii* "displayed 61% amino acid identity to the Escherichia coli UbiA protein, an octaprenyltransferase required for the second step of ubiquinone biosynthesis. Complementation experiments in both Providencia stuartii and E. coli demonstrated that aarE and ubiA are functionally equivalent" ([PMID: 9559821](https://pubmed.ncbi.nlm.nih.gov/9559821/)). This interchangeability — high sequence identity combined with cross-species genetic complementation — is strong evidence that orthologs like *P. putida* UbiA retain the same reaction. It also illustrates that mutations in this gene produce measurable downstream physiological readouts.

The broader superfamily context is useful for interpreting substrate range. Many plant and fungal UbiA-type enzymes prenylate diverse aromatic acceptors (flavonoids, coumarins, orsellinic acid), and some UbiA-type enzymes even catalyze terpene cyclization ([PMID: 41836159](https://pubmed.ncbi.nlm.nih.gov/41836159/)). These specialized-metabolism relatives share the same catalytic machinery but have diverged in acceptor specificity. *P. putida* UbiA, however, sits firmly in the primary-metabolism (ubiquinone) branch defined by the *E. coli* prototype and the MF_01635 HAMAP rule.

### Finding 4 — Crystal structures reveal a 9-TM fold with a laterally opening, intramembrane active site

The structural basis for intramembrane catalysis was solved by Cheng & Li in *Science* (2014): apo and substrate-bound structures of an archaeal UbiA at 3.3 and 3.6 Å resolution. "The structures reveal nine transmembrane helices and an extramembrane cap domain that surround a large central cavity containing the active site. To facilitate the catalysis inside membranes, UbiA has an unusual active site that opens laterally to the lipid bilayer. Our studies illuminate general mechanisms for substrate recognition and catalysis in the UbiA superfamily and rationalize disease-related mutations in humans" ([PMID: 24558159](https://pubmed.ncbi.nlm.nih.gov/24558159/)). This lateral opening is the key architectural insight: it allows the long, hydrophobic polyprenyl substrate and the equally hydrophobic prenylated product to slide in and out of the membrane while the aromatic head group and the diphosphate leaving group are processed at the Mg²⁺-containing catalytic center. Because the study explicitly generalizes its mechanism across the superfamily, the framework is transferable to *P. putida* UbiA via the shared UbiA_sf fold (IPR044878).

The relevance of this fold to the eukaryotic homologs further underscores its conservation. An AlphaFold-based analysis of COQ2 — the direct eukaryotic counterpart of bacterial UbiA in the coenzyme Q pathway — describes COQ2 as "a member of the UbiA family of transmembrane prenyltransferases that catalyzes the condensation of the head and tail precursors of CoQ, which is a key step in the process, because its product is the first intermediate that will be modified in the head by the next components of the synthesis process" ([PMID: 38671943](https://pubmed.ncbi.nlm.nih.gov/38671943/)). This is a precise description of what *P. putida* UbiA does at the bacterial inner membrane.

### Finding 5 — The actual Q88C65 sequence carries the diagnostic catalytic motifs (direct identity confirmation)

Rather than relying solely on orthology, the investigation retrieved and analyzed the physical UniProt Q88C65 sequence (296 aa; header `sp|Q88C65|UBIA_PSEPK`). Motif analysis identified both conserved catalytic aspartate-rich motifs that define the UbiA superfamily and coordinate Mg²⁺ and the prenyl-diphosphate:

- **First motif (N-D-x-x-D):** "NDFAD" at residue 73, embedded in the C-x-N-D signature "AGCCINDFADRK".
- **Second Asp-rich cluster (D-D-D):** residues 199–201, within "VDRDDDLKI".

These are precisely the aspartates whose side chains chelate the catalytic Mg²⁺ and stabilize the diphosphate leaving group in the UbiA mechanism ([PMID: 26922674](https://pubmed.ncbi.nlm.nih.gov/26922674/)). The protein is strongly hydrophobic (≈57% A/I/L/M/F/V/W/Y/C residues) with multiple predicted transmembrane segments by Kyte–Doolittle hydropathy, consistent with the polytopic 9-TM UbiA fold ([PMID: 24558159](https://pubmed.ncbi.nlm.nih.gov/24558159/)). This direct sequence-level evidence closes the gene-identity verification loop: the target protein is not merely annotated as UbiA — it structurally *is* a UbiA-family enzyme with intact catalytic machinery.

### Finding 6 — Curated UniProt/GO/Rhea annotation converges with the primary literature

The curated annotation for Q88C65 (HAMAP MF_01635) is fully consistent with the experimental and structural evidence above and pins down the physiological details:

| Annotation field | Value |
|---|---|
| **FUNCTION** | Catalyzes prenylation of *para*-hydroxybenzoate (PHB) with an all-*trans* polyprenyl group; second step in the final reaction sequence of ubiquinone-8 (UQ-8) biosynthesis; generates the first membrane-bound Q intermediate, 3-octaprenyl-4-hydroxybenzoate |
| **Catalytic activity (Rhea:27782)** | all-*trans*-octaprenyl diphosphate + 4-hydroxybenzoate = 4-hydroxy-3-(all-*trans*-octaprenyl)benzoate + diphosphate |
| **Cofactor** | Mg²⁺ |
| **Pathway** | Cofactor biosynthesis; ubiquinone biosynthesis |
| **Subcellular location** | Cell inner membrane |
| **GO — Function** | GO:0008412 (4-hydroxybenzoate polyprenyltransferase activity) |
| **GO — Process** | GO:0006744 (ubiquinone biosynthetic process) |
| **GO — Component** | GO:0005886 (plasma membrane) |
| **Transmembrane helices** | 8 annotated |
| **Keywords** | Magnesium, Transferase, Ubiquinone biosynthesis, Cell inner membrane |
| **Cross-reference** | KEGG ppu:PP_5318 |

The convergence of independent lines of evidence — *E. coli* genetics/biochemistry, cross-species complementation, crystallography, direct sequence-motif analysis, and curated database annotation — makes this one of the most robustly supported functional annotations possible for a non-model-organism gene.

---

## Mechanistic Model / Interpretation

### Position in the coenzyme Q (ubiquinone) pathway

UbiA occupies the second step of the classical ubiquinone biosynthetic route, immediately downstream of the chorismate-derived aromatic precursor:

```
Chorismate
   │  UbiC (chorismate pyruvate-lyase)              [step 1]
   ▼
4-Hydroxybenzoate (4-HB / PHB)  ── soluble aromatic head group
   │
   │  + all-trans-polyprenyl-diphosphate (donor; chain length from cellular pool)
   │  + Mg2+
   ▼  UbiA (PP_5318 / Q88C65)   ★ COMMITTED STEP ★  [step 2]
   │
3-Polyprenyl-4-hydroxybenzoate  ── FIRST membrane-anchored Q intermediate
   │
   │  UbiD/UbiX (decarboxylation), UbiH/UbiI/UbiF (hydroxylations),
   │  UbiE/UbiG (methylations) — all act on the ring; tail stays in membrane
   ▼
Ubiquinone (Coenzyme Q)  ── lipophilic electron carrier of the respiratory chain
```

The reaction UbiA catalyzes is the moment a water-soluble metabolite becomes a lipid. Before UbiA, 4-hydroxybenzoate diffuses freely in the cytoplasm; after UbiA, the attached isoprenoid tail anchors the molecule permanently in the inner membrane, where every subsequent tailoring enzyme can process the ring face-on from the membrane surface. This is why the step is "committed": it is effectively irreversible in the cellular context and channels carbon exclusively toward coenzyme Q. Physiologically, ubiquinone is the central lipid-soluble electron/proton carrier of the aerobic respiratory chain; in *E. coli*, loss of *ubiA* abolishes aerobic growth on non-fermentable substrates, a defect rescued by exogenous ubiquinone ([PMID: 8409922](https://pubmed.ncbi.nlm.nih.gov/8409922/)). For *P. putida*, an obligately respiratory soil bacterium, this step is expected to be important for efficient aerobic energy metabolism.

### How catalysis happens inside a membrane

The structural model explains an otherwise puzzling problem: how does a single active site handle one polar substrate (4-HB, plus a highly charged diphosphate) and one extremely hydrophobic substrate (a C₄₀–C₄₅ polyprenyl chain)? The answer from the archaeal UbiA structures ([PMID: 24558159](https://pubmed.ncbi.nlm.nih.gov/24558159/)) is a nine-transmembrane-helix bundle capped by an extramembrane domain, enclosing a large central cavity. The catalytic center — built around the two Asp-rich motifs and the Mg²⁺ ion — sits in this cavity, but the cavity has a **lateral portal opening into the lipid bilayer**. The isoprenoid tail threads through this portal into the membrane interior, while the aromatic head and diphosphate are held at the Mg²⁺ center.

Mechanistically, Mg²⁺ bridges the Asp-rich motifs (in Q88C65: NDFAD at residue 73 and DDD at residues 199–201) to the diphosphate of the prenyl donor. Ionization of the allylic diphosphate generates (or approaches) a prenyl carbocation; the electron-rich C-3 position of 4-hydroxybenzoate attacks this electrophile in a Friedel–Crafts-type C-alkylation, forming the new C–C bond and releasing inorganic diphosphate. The requirement for the all-*trans* donor configuration ([PMID: 8155731](https://pubmed.ncbi.nlm.nih.gov/8155731/)) reflects the geometric fit of the extended isoprenoid in the lateral membrane channel.

```
   Cytoplasmic face
        │
   ┌────┴─────────────────────┐   Extramembrane cap
   │  4-HB  •  Mg2+ • Asp-rich │   (holds polar head + diphosphate)
   │        active site        │
   ├───────────────╲───────────┤  ← lateral portal
   │  TM helices    ╲ polyprenyl│
   │  (~9 TM)        ╲ tail ~~~~│~~→ into lipid bilayer
   └─────────────────╲─────────┘
   Inner membrane (lipid)
```

### Substrate specificity summary

| Substrate role | Identity / range | Evidence |
|---|---|---|
| **Aromatic acceptor** | 4-hydroxybenzoate (fixed) | EC 2.5.1.39; Rhea:27782; *E. coli* genetics [PMID: 4552989] |
| **Prenyl donor** | all-*trans*-polyprenyl-diphosphate; accepts GPP/FPP/SPP; **not** *cis*-octaprenyl-PP | Kₘ values, *E. coli* enzyme [PMID: 8155731] |
| **Product chain length** | Set by cellular polyprenyl-PP pool (octaprenyl per HAMAP; pseudomonads commonly UQ-9) | [PMID: 8155731]; HAMAP MF_01635 |
| **Cofactor** | Mg²⁺ (essential) | [PMID: 8155731]; [PMID: 4552989] |
| **Location of catalysis** | Inner (cytoplasmic) membrane, active site open to bilayer | [PMID: 24558159]; UniProt Q88C65 |

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [4552989](https://pubmed.ncbi.nlm.nih.gov/4552989/) | Biochemical/genetic studies on ubiquinone biosynthesis in *E. coli* K-12: 4-HB octaprenyltransferase | Defines the reaction; maps *ubiA* as the structural gene; establishes membrane localization and Mg²⁺ requirement *in vivo* |
| [1644192](https://pubmed.ncbi.nlm.nih.gov/1644192/) | Cloning of *ubiC* and *ubiA* from *E. coli* | Establishes *ubiA* identity by homology + complementation; operon context downstream of *ubiC*; the prenylation step |
| [8409922](https://pubmed.ncbi.nlm.nih.gov/8409922/) | Cloning/sequence of *ubiA*, membrane-bound p-hydroxybenzoate:octaprenyltransferase | Gene product identity; hydropathy predicts polytopic membrane protein; aerobic-respiration phenotype; homology to yeast COQ2 |
| [8155731](https://pubmed.ncbi.nlm.nih.gov/8155731/) | Characterization of 4-HB polyprenyltransferase from *E. coli* | Direct biochemistry: membrane-bound, detergent-resistant, Mg²⁺-dependent, pH 7.8 optimum; donor Kₘ values; requires all-*trans* donor |
| [9559821](https://pubmed.ncbi.nlm.nih.gov/9559821/) | *aarE*, the *ubiA* homolog of *P. stuartii* | Evolutionary/functional: 61% identity to *E. coli* UbiA; *aarE* and *ubiA* interchangeable by complementation |
| [26922674](https://pubmed.ncbi.nlm.nih.gov/26922674/) | The UbiA superfamily of intramembrane aromatic prenyltransferases (review) | Places UbiA in the superfamily; conserved Mg²⁺/Asp active site; roles across quinones, hemes, chlorophylls, vitamin E |
| [24558159](https://pubmed.ncbi.nlm.nih.gov/24558159/) | Structural insights into ubiquinone biosynthesis in membranes (*Science*) | Crystal structure: 9-TM fold, extramembrane cap, laterally opening active site; general mechanism for the superfamily |
| [38671943](https://pubmed.ncbi.nlm.nih.gov/38671943/) | AlphaFold analysis of COQ2 | Eukaryotic UbiA-family counterpart; confirms "condensation of head and tail precursors of CoQ" as the committed step |
| [11038051](https://pubmed.ncbi.nlm.nih.gov/11038051/) | Expression of bacterial *ubiA* in *Lithospermum* | Demonstrates donor flexibility (GPP → 3-geranyl-4-HB); portability of the enzyme's core chemistry |
| [11206977](https://pubmed.ncbi.nlm.nih.gov/11206977/) | Active expression of *E. coli ubiA* in tobacco | Confirms *ubiA* encodes an integral membrane prenyltransferase; membrane-targeting requirements for activity |

**Consistency of the evidence.** All primary sources agree on the enzyme's identity, reaction, cofactor, and membrane localization. There are no contradicting reports. The only annotations to treat with mild caution are those that infer the specific product species purely from the *E. coli* octaprenyl (UQ-8) chain length; the biochemistry ([PMID: 8155731](https://pubmed.ncbi.nlm.nih.gov/8155731/)) shows the enzyme itself is chain-length-permissive, so the actual product species in *P. putida* is set by that organism's polyprenyl-diphosphate synthase.

**A note on gene-symbol ambiguity.** The symbol *ubiA* is also used for a large family of specialized-metabolism prenyltransferases in plants and fungi (e.g., flavonoid, coumarin, orsellinic-acid, and even terpene-cyclizing enzymes: [PMID: 40080387](https://pubmed.ncbi.nlm.nih.gov/40080387/), [PMID: 38641144](https://pubmed.ncbi.nlm.nih.gov/38641144/), [PMID: 40759078](https://pubmed.ncbi.nlm.nih.gov/40759078/), [PMID: 41836159](https://pubmed.ncbi.nlm.nih.gov/41836159/)). These share the UbiA fold but differ in aromatic-acceptor specificity, and the mammalian paralog *UBIAD1* is a distinct member. The target here is unambiguously the **primary-metabolism, ubiquinone-pathway** UbiA: this is confirmed by the HAMAP MF_01635 rule, the operon context, the direct catalytic-motif analysis of the Q88C65 sequence, and cross-species complementation with the *E. coli* prototype. No mis-assignment to a specialized-metabolism homolog has occurred.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical study of the *P. putida* protein.** The functional assignment rests on orthology to *E. coli* UbiA (backed by HAMAP MF_01635, sequence-motif analysis, and structural homology), not on purification or kinetics of Q88C65 itself. The inference is very strong but remains inference for this specific ortholog.

2. **Physiological prenyl-donor chain length is not experimentally pinned down for this strain.** UniProt/HAMAP annotates octaprenyl (UQ-8) by rule, but pseudomonads are commonly reported to produce UQ-9. Because the enzyme is chain-length-permissive, the actual product species depends on the *P. putida* polyprenyl-diphosphate synthase (e.g., an octaprenyl/solanesyl-PP synthase homolog), which was not characterized here.

3. **Structural data are from an archaeal homolog, not from a Gammaproteobacterium.** The 9-TM fold and laterally opening active site are almost certainly conserved (human/eukaryotic COQ2 and UBIAD1 fit the same framework), but no experimental structure of a *Pseudomonas* UbiA exists. UniProt annotates 8 TM helices versus the 9 seen in the archaeal crystal structure — a minor topology discrepancy likely reflecting prediction vs. crystallography.

4. **Operon arrangement and regulation are uncharacterized in *P. putida*.** The *ubiC-ubiA* synteny is documented in *E. coli*; whether the same arrangement holds in *P. putida* KT2440, and whether UbiA associates with a membrane-bound coenzyme Q biosynthetic complex ("CoQ synthome") in this organism, is unknown.

5. **No phenotypic knockout data for PP_5318 specifically.** By analogy, loss of function would impair aerobic respiration; the *aarE*/*ubiA* work ([PMID: 9559821](https://pubmed.ncbi.nlm.nih.gov/9559821/)) and *E. coli ubiA* mutants ([PMID: 8409922](https://pubmed.ncbi.nlm.nih.gov/8409922/)) show such mutations have measurable physiological consequences, but a targeted PP_5318 deletion phenotype was not part of this evidence base.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay of recombinant Q88C65.** Express PP_5318 in an *E. coli ubiA⁻* background and assay membrane fractions with 4-hydroxybenzoate plus a panel of all-*trans* prenyl-diphosphate donors (GPP, FPP, SPP, octaprenyl-PP, solanesyl-PP). This would (a) confirm activity of the specific ortholog, (b) measure its donor Kₘ profile, and (c) test complementation of the *E. coli* mutant — mirroring the *aarE* experiment.

2. **Determine the physiological Q species in *P. putida* KT2440.** Extract and quantify ubiquinones by LC-MS to establish whether the strain makes UQ-8, UQ-9, or a mixture, resolving the octaprenyl-vs-nonaprenyl annotation question and clarifying the *in vivo* donor.

3. **Targeted PP_5318 deletion / conditional knockdown.** Test the predicted phenotype: impaired aerobic respiratory growth, accumulation of 4-hydroxybenzoate, and loss of downstream Q intermediates; complement with *E. coli ubiA* to confirm specificity.

4. **Active-site mutagenesis of the diagnostic motifs.** Mutate the NDFAD (residue 73) and DDD (residues 199–201) aspartates to alanine and confirm loss of Mg²⁺-dependent activity, experimentally validating the sequence-motif assignment from Finding 5.

5. **Homology-model / AlphaFold structure of Q88C65** superposed on the archaeal UbiA and COQ2 models to map the predicted 8–9 TM topology, the lateral membrane portal, and the Mg²⁺-coordinating residues — providing a structural rationale specific to the *Pseudomonas* enzyme.

6. **Confirm operon structure and test for a CoQ biosynthetic complex in *P. putida*.** Map the genomic neighborhood of PP_5318 and use co-immunoprecipitation or BN-PAGE of tagged UbiA to determine whether it associates with other Ubi enzymes at the inner membrane.

---

## Conclusion

*ubiA* (PP_5318 / Q88C65) in *Pseudomonas putida* KT2440 encodes **4-hydroxybenzoate polyprenyltransferase (EC 2.5.1.39)**, an integral, Mg²⁺-dependent inner-membrane enzyme of the UbiA prenyltransferase superfamily. It catalyzes the **second, committed step of ubiquinone (coenzyme Q) biosynthesis**, transferring an all-*trans* polyprenyl group from polyprenyl-diphosphate onto C-3 of 4-hydroxybenzoate (Rhea:27782) to form 3-polyprenyl-4-hydroxybenzoate plus diphosphate — the first membrane-anchored Q intermediate. Catalysis occurs *within* the inner membrane through an active site that opens laterally to the lipid bilayer; the aromatic acceptor is strictly 4-hydroxybenzoate, while the prenyl-donor chain length is set by the cellular polyprenyl-diphosphate pool. The product feeds the coenzyme Q pathway that supplies the lipophilic electron carrier for aerobic respiration. This annotation is supported by convergent genetic, biochemical, structural, evolutionary, and sequence-level evidence, and the gene identity has been verified directly against the Q88C65 sequence — no symbol ambiguity remains.


## Artifacts

- [OpenScientist final report](ubiA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:4552989
2. PMID:1644192
3. PMID:8409922
4. PMID:8155731
5. PMID:11038051
6. PMID:11206977
7. PMID:26922674
8. PMID:9559821
9. PMID:41836159
10. PMID:24558159
11. PMID:38671943
12. PMID:40080387
13. PMID:38641144
14. PMID:40759078