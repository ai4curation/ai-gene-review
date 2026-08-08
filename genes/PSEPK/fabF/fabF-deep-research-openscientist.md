---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T17:38:24.410157'
end_time: '2026-07-23T17:43:30.180532'
duration_seconds: 305.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fabF
  gene_symbol: fabF
  uniprot_accession: Q88LL4
  protein_description: 'RecName: Full=3-oxoacyl-[acyl-carrier-protein] synthase 2
    {ECO:0000256|ARBA:ARBA00014657, ECO:0000256|PIRNR:PIRNR000447}; EC=2.3.1.179 {ECO:0000256|ARBA:ARBA00012356,
    ECO:0000256|PIRNR:PIRNR000447};'
  gene_info: Name=fabF {ECO:0000313|EMBL:AAN67534.1}; OrderedLocusNames=PP_1916 {ECO:0000313|EMBL:AAN67534.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
  protein_domains: 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794);
    Ketoacyl_synth_AS. (IPR018201); Ketoacyl_synth_C. (IPR014031); Ketoacyl_synth_N.
    (IPR014030)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: fabF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fabF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LL4
- **Protein Description:** RecName: Full=3-oxoacyl-[acyl-carrier-protein] synthase 2 {ECO:0000256|ARBA:ARBA00014657, ECO:0000256|PIRNR:PIRNR000447}; EC=2.3.1.179 {ECO:0000256|ARBA:ARBA00012356, ECO:0000256|PIRNR:PIRNR000447};
- **Gene Information:** Name=fabF {ECO:0000313|EMBL:AAN67534.1}; OrderedLocusNames=PP_1916 {ECO:0000313|EMBL:AAN67534.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the thiolase-like superfamily. Beta-ketoacyl-ACP
- **Key Domains:** 3-oxoacyl-ACP_synth-2. (IPR017568); Beta-ketoacyl_synthase. (IPR000794); Ketoacyl_synth_AS. (IPR018201); Ketoacyl_synth_C. (IPR014031); Ketoacyl_synth_N. (IPR014030)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fabF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fabF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fabF** (gene ID: fabF, UniProt: Q88LL4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: fabF (Q88LL4, PP_1916) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt:** Q88LL4
- **Gene:** *fabF* (ordered locus PP_1916)
- **Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / KT2440 (PSEPK)
- **Protein:** 3-oxoacyl-[acyl-carrier-protein] synthase 2 (β-ketoacyl-ACP synthase II, "KAS II")
- **EC:** 2.3.1.179
- **Family/domains:** Thiolase-like superfamily; β-ketoacyl synthase N- and C-terminal domains (IPR014030/IPR014031), 3-oxoacyl-ACP_synth-2 (IPR017568), ketoacyl-synthase active-site signature (IPR018201).

**Verification outcome — CONFIRMED, unambiguous.** The gene symbol *fabF*, the EC number 2.3.1.179, the "3-oxoacyl-ACP synthase 2 / KAS II" description, and the thiolase-fold ketosynthase domain architecture are mutually consistent and all point to the same, well-defined enzyme: the elongating condensing enzyme of bacterial type II fatty acid synthesis (FAS-II). Organism-specific genetic work in *Pseudomonas putida* (F1; PMID 34181948) directly characterizes the FabF orthologs and confirms the function assigned here. No conflicting gene of the same symbol was encountered.

---

## 1. Summary (Answer to the Research Question)

*fabF* encodes **β-ketoacyl-[acyl-carrier-protein] synthase II (KAS II; EC 2.3.1.179)**, the elongating **condensing enzyme** of the dissociated bacterial type II fatty acid synthesis (FAS-II) pathway. In each elongation cycle it catalyzes a decarboxylative **Claisen condensation** that joins a growing acyl-ACP thioester to **malonyl-ACP**, extending the fatty-acyl chain by two carbons and producing a β-ketoacyl-ACP, CO₂ and holo-ACP. It is a soluble **cytoplasmic** enzyme that acts on ACP-tethered substrates. Its physiologically distinctive role is the **elongation of palmitoleate (16:1) to cis-vaccenate (18:1)**, which makes it the key enzyme for **temperature-dependent adjustment of membrane phospholipid acyl-chain composition** (homeoviscous adaptation). In *P. putida*, the housekeeping FabF (FabF1, the PP_1916 ortholog) is required for cis-vaccenic acid synthesis.

---

## 2. Primary Function: The Reaction Catalyzed

FabF is the **elongating ketosynthase (KAS II)** of FAS-II. It catalyzes the carbon–carbon bond-forming step that lengthens the acyl chain in every round of elongation:

> **acyl-ACP (Cₙ) + malonyl-ACP → β-ketoacyl-ACP (Cₙ₊₂) + CO₂ + ACP**

"The β-ketoacyl-ACP synthase FabF catalyzes the key C-C bond formation step for fatty acid elongation in FAS-II" (Huang et al. 2024, PMID 39175097). Unlike the priming enzyme FabH/KAS III (which uses an acyl-CoA donor to start the pathway), the elongating KAS I/II enzymes use **acyl-ACP as the donor** substrate: "in the elongating KASI and KASII enzymes the donor is an acyl-ACP" (Borgaro et al. 2011, PMID 22017312). The acceptor is always **malonyl-ACP**, whose decarboxylation supplies the driving force for the condensation.

### Substrate specificity
FabF is a broad-range elongation enzyme but with characteristic chain-length preferences. In *E. coli*, "FabF efficiently catalyses the elongation of saturated C14 and unsaturated C16:1 acyl-ACP complexes" (Chen et al. 2022, PMID 36048156). Recent structural/enzymological work shows FabF has a **bimodal catalytic pattern**, preferentially acting on **C6 and C10 acyl-ACP substrates** by using two hydrophobic cavities and "front", "middle" and "back" door residues to stabilize specific chain lengths (Huang et al. 2024, PMID 39175097). The most physiologically important specialized reaction is the elongation of **palmitoleoyl-ACP (16:1) to cis-vaccenoyl-ACP (18:1)** (de Mendoza, Ulrich & Cronan 1983, PMID 6337151).

---

## 3. Catalytic Mechanism and Active-Site Chemistry

FabF adopts the **thiolase (αβαβα) fold** and operates as a homodimer, using a two-step **ping-pong mechanism** with covalent catalysis and a **Cys–His–His catalytic triad**:

1. **Acyl-enzyme formation (transacylation):** the acyl group of the donor acyl-ACP is transferred to the active-site nucleophilic **cysteine**, forming a covalent acyl-enzyme intermediate. "The nucleophilic cysteine of the active site triad was required for acyl-enzyme formation and the overall condensation activity" (Zhang et al. 2006, PMID 16618705).
2. **Decarboxylative condensation (Claisen):** malonyl-ACP binds; one histidine (His337 in *S. pneumoniae* numbering) stabilizes the malonyl thioester oxyanion/transition state, while a second histidine (His303) deprotonates a structured active-site water and promotes decarboxylation of malonate, "releasing bicarbonate"; the resulting carbanion attacks the acyl-enzyme thioester carbonyl to form the new C–C bond, yielding β-ketoacyl-ACP (PMID 16618705). Quantum-chemical analysis of FabF assigns the equivalent residues **Lys336 and His304** to "proton transfer during condensation catalysis and C-C bond formation" (Huang et al. 2024, PMID 39175097).

**Substrate delivery is gated.** Crystal structures of *E. coli* FabF and FabB in complex with substrate-mimetic acyl-ACPs show that "two active site loops undergo large conformational excursions during a dynamic gating mechanism" that "regulates acyl-ACP binding and substrate delivery to the KS active site" (Mindrebo et al. 2020, PMID 32265440). FabF recognizes ACP electrostatically, using positively charged residues on the η3-helix and loop1 near the catalytic-tunnel entrance to dock the acidic ACP (Huang et al. 2024, PMID 39175097). Mechanism-based crosslinking further captured asymmetric, cooperative substrate-binding pockets and a mobile active-site gate residue (Phe) in the related FabB (Chen et al. 2022, PMID 36048156).

**Pharmacological validation of the mechanism.** The active-site cysteine is the target of the natural product **cerulenin**, which forms a covalent adduct; the crystal structure of *B. subtilis* FabF–cerulenin shows the covalent bond forms at inhibitor carbon C3 with Cys163 (Trajtenberg et al. 2014, PMID 24641521). FabF/FabB are also the targets of **platensimycin**, which "works by inhibiting beta-ketoacyl synthases I/II (FabF/B)" (Manallack et al. 2008, PMID 18336284). These inhibitors confirm that condensation proceeds through the catalytic cysteine/malonyl-binding pocket.

---

## 4. Biological Process and Pathway Context

FabF functions within **type II (dissociated) fatty acid synthesis (FAS-II)**, the pathway that supplies the acyl chains for membrane phospholipids and lipid-derived cofactors. Each elongation cycle consists of: condensation (**FabB/FabF**) → reduction (FabG) → dehydration (FabA/FabZ) → enoyl reduction (FabI), all acting on ACP-bound intermediates. FabF performs the **committed elongation/condensation** step of this cycle. The pathway is essential for membrane biogenesis and for producing intermediates used in vitamin/cofactor biosynthesis, and it is a validated antibacterial target (Radka & Rock 2022, PMID 35650664).

### Specialized role: unsaturated fatty acids and membrane homeostasis
FabF's signature physiological contribution is control of **membrane fluidity via homeoviscous adaptation**. In *E. coli*, "strains (fabF-) lacking beta-ketoacyl-ACP synthase II are deficient in both cis-vaccenic acid synthesis and thermal regulation," and "synthase II, the product of the fabF gene, is the sole enzyme regulating the temperature-dependent composition of the membrane phospholipid acyl chains" (de Mendoza et al. 1983, PMID 6337151). FabF elongates 16:1 to 18:1 (cis-vaccenate); its activity increases at lower temperature, raising the proportion of the longer, still-unsaturated 18:1 chain to maintain membrane fluidity.

### Pathway role in *Pseudomonas putida* specifically
The soil bacterium *P. putida* has an expanded set of condensing enzymes. In *P. putida* F1, five KAS genes exist — four annotated FabF and one FabB — and genetic dissection shows a clear division of labor: "The *P. putida* ΔfabF1 deletion strain was almost entirely defective in synthesis of cis-vaccenic acid," and heterologously expressed *P. putida* fabF1 "restored *E. coli* fabF function" (Dong et al. 2021, PMID 34181948). A second paralog, **FabF2, is normally cryptic** (transcriptionally repressed) and only becomes physiologically important when its repressor (Pput_2425) is inactivated, at which point it can even substitute for FabB in unsaturated fatty acid synthesis (PMID 34181948). This establishes **FabF1 — the KT2440 PP_1916 ortholog — as the primary, housekeeping KAS II elongation enzyme**, while the paralogs provide backup or conditionally specialized activities. This is strong organism-specific support for assigning the classic KAS II function to Q88LL4.

---

## 5. Subcellular Localization

FabF is a **soluble cytoplasmic enzyme**. In FAS-II, all substrates are tethered as thioesters to the small acidic acyl carrier protein (ACP), and the pathway enzymes — including the condensing enzymes — operate in the **cytosol**, shuttling acyl chains between soluble catalytic domains on ACP. FabF has no membrane-spanning segment or signal peptide; its "localization" is defined by its function on cytoplasmic ACP-bound acyl intermediates, with the finished acyl chains subsequently transferred to the membrane-associated acyltransferases (PlsB/PlsC/PlsX-PlsY system) for phospholipid assembly. The reliance on protein–protein docking with ACP (via the η3-helix/loop1 electrostatic interface; Huang et al. 2024, PMID 39175097) is consistent with a cytoplasmic, ACP-dependent enzyme.

---

## 6. Evidence Summary

| Claim | Evidence type | Key reference |
|---|---|---|
| FabF catalyzes the C–C bond-forming elongation step of FAS-II | Structural + enzymatic (FabF–ACP complexes) | PMID 39175097 |
| Elongating KAS uses acyl-ACP donor + malonyl-ACP acceptor | Enzymology / substrate mimetics | PMID 22017312 |
| Ping-pong mechanism, catalytic Cys + two His, decarboxylative condensation | Mutagenesis / mechanism | PMID 16618705 |
| Dynamic gating of acyl-ACP substrate delivery | Crystallography + MD | PMID 32265440; PMID 36048156 |
| FabF elongates 16:1→18:1 and is the sole thermal regulator of membrane acyl chains | Genetics/physiology (*E. coli*) | PMID 6337151 |
| Housekeeping FabF1 required for cis-vaccenate in *P. putida*; multiple KAS paralogs | Gene deletion + heterologous complementation | PMID 34181948 |
| Active-site Cys is covalently modified by cerulenin; FabF is a validated drug target | Crystallography (FabF–cerulenin) | PMID 24641521; PMID 18336284 |

---

## 7. Supported and Refuted Hypotheses

**Supported**
- FabF (Q88LL4/PP_1916) is a β-ketoacyl-ACP synthase II catalyzing the elongation condensation step of FAS-II (EC 2.3.1.179).
- It operates by a ping-pong Claisen mechanism using a Cys–His–His triad and malonyl-ACP decarboxylation.
- It preferentially elongates 16:1 to 18:1 (cis-vaccenate) and contributes to temperature-dependent membrane composition.
- In *P. putida*, the housekeeping FabF (FabF1 ortholog) is genetically required for cis-vaccenic acid synthesis.

**Refuted / excluded**
- FabF is *not* a priming enzyme (that is FabH/KAS III, which uses acyl-CoA and initiates the pathway).
- FabF is *not* a membrane-integral protein; it acts on cytoplasmic ACP-bound substrates.
- The gene symbol is *not* ambiguous here — all identifiers converge on one enzyme.

---

## 8. Limitations and Future Directions

- Direct biochemical/structural characterization of the specific KT2440 protein (Q88LL4/PP_1916) was not found in the literature; functional assignment rests on (i) unambiguous sequence/domain annotation, (ii) closely related *P. putida* F1 genetics (PMID 34181948), and (iii) extensive mechanistic work on *E. coli*, *B. subtilis* and *S. pneumoniae* orthologs. Given the strong sequence and genetic conservation, this inference is robust.
- The precise in vitro chain-length profile and kinetic parameters of the KT2440 enzyme, and the exact partitioning of elongation among the multiple KAS paralogs under different conditions (temperature, solvent stress), remain to be measured directly.
- Future work: recombinant expression and steady-state kinetics of PP_1916 FabF with defined acyl-ACP substrates; crystal/cryo-EM structure of the KT2440 enzyme–ACP complex; conditional knockdown to quantify its contribution versus paralogs in KT2440 membrane lipid composition and solvent/stress tolerance.

---

### References (PMIDs)
6337151, 18336284, 22017312, 24641521, 32265440, 34181948, 35650664, 36048156, 39175097.


## Artifacts

- [OpenScientist final report](fabF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fabF-deep-research-openscientist_artifacts/final_report.pdf)