---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:38:31.309351'
end_time: '2026-07-18T17:31:20.569266'
duration_seconds: 3169.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ispG
  gene_symbol: ispG
  uniprot_accession: Q88PJ7
  protein_description: 'RecName: Full=4-hydroxy-3-methylbut-2-en-1-yl diphosphate
    synthase (flavodoxin) {ECO:0000255|HAMAP-Rule:MF_00159}; EC=1.17.7.3 {ECO:0000255|HAMAP-Rule:MF_00159};
    AltName: Full=1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase {ECO:0000255|HAMAP-Rule:MF_00159};'
  gene_info: Name=ispG {ECO:0000255|HAMAP-Rule:MF_00159}; OrderedLocusNames=PP_0853;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the IspG family. {ECO:0000255|HAMAP-
  protein_domains: Dihydropteroate_synth-like_sf. (IPR011005); IspG_bac. (IPR016425);
    IspG_bac-typ. (IPR004588); IspG_C. (IPR058579); IspG_TIM. (IPR058578)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ispG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ispG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PJ7
- **Protein Description:** RecName: Full=4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin) {ECO:0000255|HAMAP-Rule:MF_00159}; EC=1.17.7.3 {ECO:0000255|HAMAP-Rule:MF_00159}; AltName: Full=1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate synthase {ECO:0000255|HAMAP-Rule:MF_00159};
- **Gene Information:** Name=ispG {ECO:0000255|HAMAP-Rule:MF_00159}; OrderedLocusNames=PP_0853;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the IspG family. {ECO:0000255|HAMAP-
- **Key Domains:** Dihydropteroate_synth-like_sf. (IPR011005); IspG_bac. (IPR016425); IspG_bac-typ. (IPR004588); IspG_C. (IPR058579); IspG_TIM. (IPR058578)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ispG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ispG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ispG** (gene ID: ispG, UniProt: Q88PJ7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *ispG* (Q88PJ7, PP_0853) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt:** Q88PJ7 — *ispG* / OrderedLocusName **PP_0853**
- **Protein:** 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin); a.k.a. **(E)-1-hydroxy-2-methyl-but-2-enyl 4-diphosphate synthase**, **HMBPP synthase**, historically **GcpE**
- **EC:** 1.17.7.3
- **Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125), a Gram‑negative soil bacterium
- **Family / domains:** IspG family; TIM-barrel (dihydropteroate-synthase-like superfamily, IPR011005), IspG_TIM (IPR058578), IspG_C (IPR058579), bacterial IspG signatures (IPR004588, IPR016425)

**Verification outcome — CONFIRMED (unambiguous).** The gene symbol *ispG* (synonym *gcpE*), the EC number, the annotated reaction, the [4Fe-4S] IspG protein family, and the TIM-barrel domain architecture are mutually consistent and match the primary experimental and structural literature. *ispG* is a highly conserved, universally single-copy enzyme of the bacterial/plastidial MEP pathway; there is no competing gene bearing this symbol. Mechanistic and structural studies were performed in orthologs (*E. coli*, *Thermus thermophilus*, *Aquifex aeolicus*); given the enzyme's near-invariant catalytic core, these findings transfer directly to the *P. putida* protein.

---

## 1. Summary (Answer to the Research Question)

*ispG* encodes **(E)-4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (HMBPP synthase / GcpE)**, an oxygen-sensitive **[4Fe-4S] cluster metalloenzyme** that catalyzes the **penultimate step of the methylerythritol phosphate (MEP / non-mevalonate) pathway** of isoprenoid precursor biosynthesis. It performs the **reductive dehydroxylation (ring-opening) of the cyclic substrate 2‑C‑methyl‑D‑erythritol‑2,4‑cyclodiphosphate (MEcPP) to the linear allylic product (E)‑4‑hydroxy‑3‑methylbut‑2‑enyl diphosphate (HMBPP)**, consuming two electrons supplied by a physiological electron-donor system (flavodoxin/flavodoxin reductase; ferredoxin in some organisms). The enzyme functions in the **cytoplasm** and is essential for supplying IPP and DMAPP, the universal five-carbon isoprenoid building blocks.

---

## 2. Primary Function: the Catalyzed Reaction and Substrate Specificity

**Reaction (EC 1.17.7.3):**

> 2‑C‑methyl‑D‑erythritol‑2,4‑cyclodiphosphate (MEcPP) + 2 e⁻ + 2 H⁺ → (E)‑4‑hydroxy‑3‑methylbut‑2‑enyl diphosphate (HMBPP) + H₂O

This was established biochemically by Kollas et al. (2002): recombinant GcpE "was enzymatically active in converting 2‑C‑methyl‑D‑erythritol‑2,4‑cyclodiphosphate (MEcPP) into (E)‑4‑hydroxy‑3‑methyl‑but‑2‑enyl diphosphate (HMBPP) in the presence of dithionite as reductant," with a **k_cat ≈ 0.4 s⁻¹** and specific activity 0.6 µmol·min⁻¹·mg⁻¹ (PMID 12482607). The transformation is formally a **2‑electron reductive dehydroxylation**: the substrate's five-membered 2,4-cyclodiphosphate ring is opened and the C3 hydroxyl is eliminated, generating the (E)-configured allylic double bond of HMBPP (Witjaksono et al. 2025, PMID 41122037).

**Substrate specificity.** IspG is highly specific for MEcPP, the product of the upstream enzyme IspF (MEcPP synthase). Substrate analogues such as monofluoromethyl-erythritol cyclodiphosphate have been synthesized specifically to probe/inhibit the active site, underscoring the tight steric/electronic requirements of the funnel-shaped pocket (Witjaksono et al. 2025, PMID 41122037).

---

## 3. Catalytic Mechanism and the Iron-Sulfur Cluster

IspG is a **[4Fe-4S] metalloenzyme** (Witjaksono et al. 2025, PMID 41122037). Anaerobically purified enzyme "contains solely [4Fe-4S] clusters," and, upon addition of MEcPP plus a reductant, EPR spectroscopy reveals a transient iron-sulfur signal whose similarity to that of ferredoxin:thioredoxin reductase indicates that "an intermediate is directly bound to the active-site cluster" (Adedeji et al. 2007, PMID 17214985). Thus catalysis proceeds through **inner-sphere coordination of the substrate to the unique ("apical") fourth iron** of the cluster, which lacks a cysteine ligand and is instead available to bind the substrate oxygen. Two electrons, delivered one at a time by the electron-donor system, drive C–O bond cleavage, likely via organometallic/radical intermediates (a ferraoxetane/allyl-anion or Fe-bound radical intermediate has been proposed).

The reaction's obligatory reductant is a **redox protein system**. Mössbauer and reconstitution studies established that the **bacterial enzyme utilizes NADPH/flavodoxin/flavodoxin reductase as a reducing shuttle system**, reducing MEcPP to HMBPP **via two consecutive one-electron transfers** (Seemann et al. 2005, PMID 15650872). This is the origin of the UniProt name "…(flavodoxin)": in *P. putida*, electrons flow NADPH → flavodoxin reductase → **flavodoxin** → IspG [4Fe-4S] cluster. (Notably, the *Arabidopsis* plastidial ortholog cannot use this bacterial shuttle and required 5-deazaflavin semiquinone in vitro, indicating organism-specific redox partners — PMID 15650872.) The enzyme's **oxygen sensitivity** (PMID 41122037) reflects the lability of the reduced [4Fe-4S] cluster and confines function to the reducing intracellular environment.

**Organometallic intermediates.** Detailed EPR/ENDOR/HYSCORE spectroscopy with ²H, ¹³C and ¹⁷O labeling shows the mechanism is genuinely organometallic: reduction of MEcPP generates an **Fe–C–H-containing intermediate, most likely a ferraoxetane**, which is reduced to a **ferracyclopropane in which HMBPP forms an η²-alkenyl π-complex with the 4th (apical) iron** of the [4Fe-4S] cluster; alkyne (propargyl) diphosphate analogues exploit this by forming a comparable metallacycle and inhibit potently (Kᵢ ≈ 300 nM) (Wang et al. 2010, PMID 20534554). This explains the mechanistic necessity of the non-cysteinyl 4th iron identified structurally.

---

## 4. Three-Dimensional Structure

The crystal structure of the GcpE(IspG)–MEcPP complex from *Thermus thermophilus* (1.55 Å; Rekittke et al. 2012, PMID 22967895) reveals a **two-domain architecture**:

- an N-terminal **(β/α)₈ TIM-barrel** that forms a funnel binding MEcPP (matching InterPro IPR058578/IPR011005 for Q88PJ7), and
- a C-terminal **[4Fe-4S]-cluster domain** (IPR058579).

"MEcPP binding inside the TIM-barrel funnel induces a **60° rotation of the [4Fe-4S] cluster-containing domain onto the TIM-barrel entrance**," closing a clamshell over the substrate; "the **apical iron of the [4Fe-4S] cluster ligates with the C3 oxygen atom of MEcPP**" (PMID 22967895). This directly visualizes how the metallocenter is positioned to abstract the C3 hydroxyl. In physiological assemblies the enzyme is typically dimeric, and in some organisms the two domains are contributed in *trans*.

---

## 5. Localization

IspG is a **soluble cytoplasmic enzyme**. Multiple lines of evidence support this: (i) it lacks signal peptides or transmembrane segments; (ii) its oxygen-labile reduced [4Fe-4S] cluster requires the reducing cytosolic milieu; (iii) its substrate (MEcPP) and product (HMBPP) are polar, doubly-phosphorylated small molecules generated and consumed by other cytosolic MEP-pathway enzymes; and (iv) its electron donors (flavodoxin/ferredoxin) are cytoplasmic. In plants/algae the ortholog is plastid-localized, consistent with the cyanobacterial/endosymbiotic origin of the pathway; in the free-living bacterium *P. putida* the reaction occurs in the cytoplasm.

**Target-specific sequence support (this study).** Kyte–Doolittle hydropathy analysis of Q88PJ7 (window 19) finds **no transmembrane-like segment** (maximum window hydropathy 1.51, below the ~1.6 TM threshold; 0 windows exceed it) and an overall **GRAVY of −0.03** (hydrophilic, i.e., soluble/globular). The **N-terminus (MHGESPIKRRESRKIW…) is highly charged** (8 charged residues in the first 30) and lacks the hydrophobic core of a cleavable signal peptide. These features are fully consistent with a soluble cytoplasmic enzyme.

---

## 6. Pathway Context and Biological Role

*ispG* operates in the **MEP (2‑C‑methyl‑D‑erythritol‑4‑phosphate) / DOXP / non-mevalonate pathway**, the route *Pseudomonas putida* uses to synthesize isoprenoid precursors. This is confirmed for the target organism: "In *P. putida* and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway," and KT2440 has been engineered via MEP-pathway genes (dxs, dxr, idi) for isoprenoid (lycopene) production (Hernandez-Arranz et al. 2019, PMID 31500633). More broadly, many Gram-negative bacteria including *Pseudomonas* rely exclusively on the MEP pathway rather than the mevalonate pathway (Qabar et al. 2026, PMID 41700894).

Pathway order and IspG's position (penultimate step):

1. DXS: pyruvate + G3P → DXP
2. DXR (IspC): DXP → MEP
3. IspD: MEP → CDP-ME
4. IspE: CDP-ME → CDP-MEP
5. IspF: CDP-MEP → **MEcPP**
6. **IspG (this gene): MEcPP → HMBPP**  ← penultimate step
7. IspH (LytB): HMBPP → IPP + DMAPP (final step)

The product **HMBPP is the direct substrate of IspH**, which yields **isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP)** — the universal C5 building blocks for all downstream isoprenoids (ubiquinone/quinones for respiration, bactoprenol/undecaprenyl phosphate for cell-wall/LPS assembly, carotenoids, and prenylated products). IspG is therefore **essential** for viability in *P. putida* (Kollas et al. 2002 describe GcpE as "an essential enzyme of the non-mevalonate pathway"; PMID 12482607).

**Downstream significance of the product.** HMBPP is the **most potent known microbial phosphoantigen**, sensed by human Vγ9Vδ2 T cells through intracellular binding to butyrophilin BTN3A1/BTN2A1 (Yang et al. 2019, PMID 30902636; Zhang et al. 2025, PMID 40505658). Thus IspG activity in bacteria couples directly to host immune surveillance. Because humans use the mevalonate pathway and lack IspG, the enzyme is a **validated, selective antimicrobial drug target** (Witjaksono et al. 2025, PMID 41122037).

---

## 6b. Target-Specific Bioinformatic Evidence (this study)

To ensure the mechanistic/structural conclusions (derived from orthologs) apply to the actual *P. putida* protein, I retrieved the Q88PJ7 sequence (369 aa) and aligned it to the biochemically characterized *E. coli* IspG (P62620, 372 aa):

- **73.8% amino-acid identity** (267/362 aligned positions) — very high conservation across the whole enzyme.
- The protein contains only **4 cysteines** (positions 104, 270, 273, 305). The three cysteines that ligate the catalytic **[4Fe-4S] cluster in *E. coli* IspG (Cys270, Cys273, Cys305) are all conserved** in the target, in the C-terminal motif **C270-P-S-C273…C305 (CPSC…C)**.
- Only three cysteines coordinate the cluster; the **fourth ("apical") iron is left unligated**, consistent with the structural finding that it binds the substrate C3 oxygen (see §4).

This target-specific evolutionary/structural inference confirms an intact, canonical IspG active site in Q88PJ7 and justifies transferring the enzymology and mechanism established in *E. coli* and *T. thermophilus* to the *P. putida* enzyme.

## 7. Evidence Summary

| Claim | Evidence type | Source |
|---|---|---|
| Catalyzes MEcPP → HMBPP | Direct in vitro enzymology, kinetics (k_cat 0.4 s⁻¹) | Kollas 2002 (PMID 12482607) |
| Essential MEP-pathway enzyme | Functional/genetic characterization | Kollas 2002 (PMID 12482607) |
| [4Fe-4S] enzyme; 2-e⁻ reductive dehydroxylation; O₂-sensitive | Biochemistry + mechanistic review | Witjaksono 2025 (PMID 41122037) |
| Substrate binds apical Fe of the cluster | EPR spectroscopy of intermediate | Adedeji 2007 (PMID 17214985) |
| TIM-barrel + mobile Fe-S domain; Fe–C3-O ligation | 1.55 Å X-ray structure | Rekittke 2012 (PMID 22967895) |
| Pseudomonas uses MEP (not mevalonate) pathway | Comparative genomics review | Qabar 2026 (PMID 41700894) |
| Product HMBPP is a phosphoantigen; validated drug target | Structural immunology; med-chem | Yang 2019 (PMID 30902636); Witjaksono 2025 (PMID 41122037) |
| Domain/family assignment | Bioinformatics (InterPro/UniProt) | UniProt Q88PJ7; InterPro |
| Target conserves [4Fe-4S] cysteines; 73.8% id to E. coli IspG | Sequence alignment (this study) | Q88PJ7 vs P62620 |
| Electron donor = NADPH/flavodoxin/flavodoxin reductase; two 1-e⁻ transfers | Mössbauer + reconstitution | Seemann 2005 (PMID 15650872) |
| Organometallic ferraoxetane/ferracyclopropane intermediates on 4th Fe | EPR/ENDOR/HYSCORE | Wang/Oldfield 2010 (PMID 20534554) |
| *P. putida* KT2440 uses the MEP pathway for isoprenoid precursors | Metabolic engineering | Hernandez-Arranz 2019 (PMID 31500633) |
| Target has no TM helix/signal peptide; soluble (GRAVY −0.03) → cytoplasmic | Hydropathy analysis (this study) | Q88PJ7 |

---

## 8. Supported vs. Refuted Hypotheses

- **Supported:** IspG is HMBPP synthase (EC 1.17.7.3) catalyzing MEcPP → HMBPP; a cytoplasmic [4Fe-4S] enzyme; penultimate MEP-pathway step; essential; product feeds IspH to make IPP/DMAPP.
- **Refuted / excluded:** IspG is *not* a transporter, structural protein, or signaling receptor; it is not a mevalonate-pathway enzyme; the "flavodoxin" in its name denotes the electron-donor requirement, not a separate activity.

## 9. Limitations and Future Directions

- Enzymatic, structural, and mechanistic data derive from orthologs (*T. thermophilus*, *A. aeolicus*, *E. coli*), not from the *P. putida* protein itself; however, catalytic residues, the cluster-binding motif, and domain architecture are conserved, so functional transfer is well justified.
- The organometallic intermediates (ferraoxetane/ferracyclopropane) and the NADPH/flavodoxin/flavodoxin-reductase donor system are now established for bacterial IspG generally (PMIDs 20534554, 15650872); the specific *P. putida* KT2440 flavodoxin/reductase isoforms that partner IspG have not yet been individually mapped.
- No *P. putida*-specific crystal structure or in vivo knockout kinetic study was located; these would refine strain-specific parameters.

---

### Key References
- Kollas et al. (2002) *FEBS Lett.* — Functional characterization of GcpE, an essential MEP-pathway enzyme. **PMID 12482607**
- Adedeji et al. (2007) *FEBS Lett.* — Active-site [4Fe-4S] cluster involvement (EPR). **PMID 17214985**
- Rekittke et al. (2012) *FEBS Lett.* — GcpE(IspG)–MEcPP crystal structure, 1.55 Å. **PMID 22967895**
- Witjaksono et al. (2025) — IspG mechanism / mechanism-based inhibitors; antimicrobial target. **PMID 41122037**
- Qabar et al. (2026) — Bacterial MEP vs. mevalonate pathway distribution. **PMID 41700894**
- Yang et al. (2019) *Immunity* — HMBPP phosphoantigen sensing by butyrophilin/Vγ9Vδ2 T cells. **PMID 30902636**
- Seemann et al. (2005) *FEBS Lett.* — GcpE is a [4Fe-4S] protein; NADPH/flavodoxin/flavodoxin-reductase shuttle; two consecutive 1-e⁻ transfers. **PMID 15650872**
- Wang et al. (Oldfield lab, 2010) *J. Am. Chem. Soc.* — Organometallic (ferraoxetane/ferracyclopropane) mechanism and inhibition of GcpE/IspG. **PMID 20534554**
- Hernandez-Arranz et al. (2019) — *P. putida* KT2440 uses the MEP pathway; isoprenoid engineering. **PMID 31500633**


## Artifacts

- [OpenScientist final report](ispG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ispG-deep-research-openscientist_artifacts/final_report.pdf)