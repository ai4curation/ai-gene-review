---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T15:56:44.166864'
end_time: '2026-07-25T16:18:56.456515'
duration_seconds: 1332.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: cysI
  gene_symbol: cysI
  uniprot_accession: Q88KB9
  protein_description: 'SubName: Full=Sulphite reductase hemoprotein, beta subunit
    {ECO:0000313|EMBL:AAN67984.1};'
  gene_info: Name=cysI {ECO:0000313|EMBL:AAN67984.1}; OrderedLocusNames=PP_2371 {ECO:0000313|EMBL:AAN67984.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: NIR_SIR_4Fe-4S. (IPR051329); NiRdtase/SiRdtase_haem-b_fer. (IPR005117);
    Nit/Sulf_reduc_fer-like_dom_sf. (IPR036136); NO2/SO3_Rdtase_4Fe4S_dom. (IPR006067);
    NO2/SO3_Rdtase_4Fe4S_sf. (IPR045854)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: cysI-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: cysI-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KB9
- **Protein Description:** SubName: Full=Sulphite reductase hemoprotein, beta subunit {ECO:0000313|EMBL:AAN67984.1};
- **Gene Information:** Name=cysI {ECO:0000313|EMBL:AAN67984.1}; OrderedLocusNames=PP_2371 {ECO:0000313|EMBL:AAN67984.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** NIR_SIR_4Fe-4S. (IPR051329); NiRdtase/SiRdtase_haem-b_fer. (IPR005117); Nit/Sulf_reduc_fer-like_dom_sf. (IPR036136); NO2/SO3_Rdtase_4Fe4S_dom. (IPR006067); NO2/SO3_Rdtase_4Fe4S_sf. (IPR045854)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cysI" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cysI' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cysI** (gene ID: cysI, UniProt: Q88KB9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *cysI* (PP_2371, UniProt Q88KB9) in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

*cysI* (locus **PP_2371**; UniProt **Q88KB9**) encodes the **sulfite reductase hemoprotein (SiRHP), the β subunit of assimilatory NADPH‑dependent sulfite reductase (EC 1.8.1.2)**. Its primary catalytic function is the **six‑electron reduction of sulfite (SO₃²⁻) to sulfide (S²⁻/H₂S)** at a unique **siroheme–[4Fe‑4S] coupled cofactor**. This is the **terminal reductive step of the assimilatory sulfate‑reduction pathway**, generating the reduced sulfur (sulfide) that is subsequently incorporated into L‑cysteine (and thence methionine, coenzymes, and other sulfur metabolites). The enzyme is a **soluble cytoplasmic** protein that acts as the catalytic partner of the CysJ diflavin flavoprotein, which delivers electrons from NADPH. The functional assignment is supported by conserved domain architecture and sequence homology, and by decades of experimental biochemistry, crystallography, and genetics in the closely related enterobacterial and *Pseudomonas*/actinobacterial systems.

**Identity verification:** The gene symbol *cysI*, the UniProt description ("Sulphite reductase hemoprotein, beta subunit"), the InterPro/Pfam domains (PF01077 nitrite/sulfite reductase 4Fe‑4S; PF03460 ferredoxin‑like half‑domain), and the cofactor keywords (4Fe‑4S, Heme, Iron, Iron‑sulfur, Oxidoreductase) are **fully mutually consistent** and match the canonical CysI hemoprotein of assimilatory sulfite reductase. No ambiguity was found. Where direct *P. putida* KT2440 biochemical studies of PP_2371 are lacking, function is inferred from strong orthology to experimentally characterized CysI proteins.

---

## 2. Molecular Identity and Domain Architecture

| Property | Value (UniProt Q88KB9) |
|---|---|
| Gene / locus | *cysI* / PP_2371 |
| Length / mass | 550 aa / 62.2 kDa |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) |
| Keywords | 4Fe‑4S, Heme, Iron, Iron‑sulfur, Metal‑binding, Oxidoreductase |
| GO (function) | GO:0016491 oxidoreductase; GO:0020037 heme binding; GO:0051539 [4Fe‑4S] binding; GO:0046872 metal‑ion binding |
| Domains | 2× "Nitrite/Sulfite reductase 4Fe‑4S" (Pfam PF01077) + 2× "ferredoxin‑like" (Pfam PF03460) |
| Cross‑refs | KEGG ppu:PP_2371; BioCyc PPUT160488:G1G01‑2534‑MONOMER; AlphaFoldDB Q88KB9 |

The protein has the characteristic **internally duplicated two‑domain repeat** of the nitrite/sulfite‑reductase (NIR/SIR) superfamily, and its C‑terminus contains the canonical cysteine‑rich cofactor‑ligating motif (…G**C**MNA**C**GHHH…**C**…) that supplies the four cysteine ligands to the [4Fe‑4S] cluster, one of which is the **bridging thiolate shared with the siroheme iron**. There is no signal peptide or transmembrane segment, consistent with a soluble cytoplasmic localization.

---

## 3. Primary Function: Catalysis and Substrate Specificity

The CysI hemoprotein is the **catalytic subunit** that binds substrate and carries out its reduction. The reaction is:

> **SO₃²⁻ + 6 e⁻ + 6–8 H⁺ → S²⁻ (H₂S) + 3 H₂O**

Key features:

- **Six‑electron chemistry with no released intermediates.** The active site of the *E. coli* hemoprotein "is exquisitely designed to catalyze the six‑electron reductions of sulfite to sulfide and nitrite to ammonia" (Crane, Siegel & Getzoff, 1997, PMID 9315848). The enzyme therefore has a **secondary nitrite‑reductase activity** (nitrite → ammonia), reflecting shared active‑site chemistry across the NIR/SIR family, but its **physiological substrate is sulfite** in the cysteine‑biosynthetic (assimilatory) context.
- **Push–pull mechanism.** "The substrate evolves through a push‑pull mechanism, where electron transfer is coupled to three dehydration steps" (Askenasy & Stroupe, 2020, PMID 32851831). An extensive network of positively charged residues, ordered waters, and siroheme carboxylates binds, polarizes, and protonates the anionic substrate at the siroheme sixth axial position (Crane et al., 1997, PMID 9315848).
- **Assimilatory holoenzyme.** In *E. coli*, "the flavoprotein and hemoprotein components of … NADPH‑sulfite reductase are encoded by *cysJ* and *cysI*, respectively" (Wu, Siegel & Kredich, 1991, PMID 1987123). Electrons flow **NADPH → FAD → FMN (CysJ diflavin flavoprotein) → siroheme/[4Fe‑4S] (CysI) → sulfite**. Recent cryo‑EM confirms the two‑subunit organization: "SiR has two subunits: an NADPH, FMN, and FAD‑binding diflavin flavoprotein and a siroheme/Fe[4S4]‑containing hemoprotein" (Ghazi Esfahani et al., 2025, PMID 40140349). The classical holoenzyme stoichiometry is α₈β₄ (CysJ₈CysI₄).

---

## 4. Cofactors: The Siroheme–[4Fe‑4S] Coupled Center

The defining feature of CysI is its bimetallic active site:

- **Siroheme covalently coupled to a [4Fe‑4S] cluster via a shared cysteine.** "The hallmark of sulfite reductase is its catalytic center made of an iron‑containing porphyrinoid called siroheme that is covalently coupled to a [4Fe‑4S] cluster through a shared cysteine ligand" (Askenasy & Stroupe, 2020, PMID 32851831). Crystallography across oxidation states shows "a bridging cysteine thiolate supplied by the protein always covalently links the siroheme (iron isobacteriochlorin) to the Fe4S4 cluster, facilitating their ability to transfer electrons to substrate" (Crane, Siegel & Getzoff, 1997, PMID 9315848). Sulfite binds directly to the siroheme iron; the [4Fe‑4S] cluster tunes the redox potential and relays electrons.
- **Cofactor dependency on siroheme biosynthesis (CysG).** Siroheme is made from uroporphyrinogen III by methylation, oxidation, and iron insertion. "*cysG* mutants cannot reduce sulfite to sulfide and require a source of sulfide or cysteine for growth" (Kolko et al., 2001, PMID 11114933), and *cysG* "encodes a uroporphyrinogen III methyltransferase required for the synthesis of siroheme, a cofactor for the hemoprotein" (Wu et al., 1991, PMID 1987123). Without siroheme, CysI accumulates as inactive apo‑protein. (*P. putida* KT2440 encodes the siroheme synthase machinery required to activate CysI.)

---

## 5. Biological Process and Pathway Context

CysI catalyzes the **last dedicated reductive step of assimilatory sulfate reduction**, the pathway supplying reduced sulfur for biosynthesis:

> sulfate (SO₄²⁻) → **APS** (ATP sulfurylase, CysN/CysD) → **PAPS/sulfite** (APS/PAPS reductase, CysH; in *Pseudomonas* an APS reductase route) → **sulfide** (**sulfite reductase, CysJI**) → **L‑cysteine** (O‑acetylserine sulfhydrylase / cysteine synthase, CysK/CysM)

Genetic evidence directly ties *cysI* to sulfide production:
- In *Zymomonas mobilis*, inactivation of the sulfite‑reductase genes *cysIJ* rendered mutants "unable to produce detectable H₂S," and sulfite could not restore it (Tan et al., 2013, PMID 23086550).
- In *Corynebacterium glutamicum*, mutational analysis showed *cysI* (among the *cys* cluster) "were demonstrated to be involved in the reduction of inorganic sulphur compounds" (Rückert et al., 2005, PMID 16159395).

The sulfide produced is condensed with O‑acetyl‑L‑serine to form L‑cysteine, the entry point for all sulfur‑containing biomolecules (cysteine, methionine, glutathione, Fe‑S clusters, thiamine, biotin, coenzyme A). In enteric bacteria the *cys* regulon (including *cysJIH*) is controlled by the LysR‑type activator **CysB** with N‑acetylserine as inducer and sulfide/cysteine as anti‑inducers (Borum & Monty, 1976, PMID 1107320); an analogous sulfur‑responsive regulatory logic operates in *Pseudomonas*.

### 5.1 KT2440‑specific genomic and pathway organization (this study)

Database mapping of the *P. putida* KT2440 genome (KEGG) provides direct, organism‑specific confirmation and refines the pathway picture:

- **Exact assignment:** KEGG annotates **ppu:PP_2371 = K00381, "sulfite reductase (NADPH) hemoprotein beta‑component" [EC 1.8.1.2]**, in pathway **ppu00920 (Sulfur metabolism)** and modules **M00176 (Assimilatory sulfate reduction, sulfate ⇒ H₂S)** and **M00616 (Sulfate–sulfur assimilation)**. Chromosomal position: complement(2,707,556–2,709,208), 1,653 bp (550 aa).
- **Not an operon with *cysJ*:** The genes immediately flanking PP_2371 (PP_2370, unknown; PP_2372, putative sugar‑binding protein) are unrelated. Thus, unlike the *E. coli cysJIH* operon, KT2440 *cysI* is **genomically dispersed** from its flavoprotein partner. The CysJ diflavin flavoprotein (KO K00380) maps to **PP_0860 / PP_1703** elsewhere on the chromosome.
- **PAPS‑independent (APS‑reductase) route:** KT2440 encodes an **APS reductase (CysH, K00390 = PP_2328)** and ATP‑sulfurylase component **CysD (K00957 = PP_1303)**, but **no APS kinase (cysC, K00860) and no PAPS reductase** were found. This indicates that *P. putida* reduces activated sulfate as **APS directly to sulfite (bypassing PAPS)** — consistent with the [4Fe‑4S] APS reductase characterized in the related *P. aeruginosa* (Kim et al., 2004, PMID 15491155). CysI (PP_2371) then performs the final **sulfite → sulfide** step, and the sulfide is delivered to **cysteine synthase / O‑acetylserine sulfhydrylase (CysK, K01738 = PP_4571)** to form L‑cysteine.

Pathway in KT2440: SO₄²⁻ → (ATP sulfurylase, CysDN) → **APS** → (**APS reductase CysH/PP_2328**) → **sulfite** → (**sulfite reductase CysI/PP_2371 + CysJ flavoprotein PP_0860/PP_1703**) → **sulfide** → (**CysK/PP_4571 + O‑acetylserine**) → **L‑cysteine**.

*Note on pathway specialization:* Assimilatory sulfite reductase (CysI/SiRHP) is mechanistically and evolutionarily distinct from **dissimilatory** sulfite reductase (DsrAB), which uses sulfite as a terminal respiratory electron acceptor (Colman et al., 2022, PMID 35122336); both, however, share the siroheme–[4Fe‑4S] catalytic strategy (Askenasy & Stroupe, 2020, PMID 32851831). PP_2371 belongs to the **assimilatory** class, consistent with *P. putida*'s aerobic biosynthetic sulfur metabolism.

---

## 6. Subcellular Localization

CysI is a **soluble cytoplasmic** enzyme. It carries no signal peptide or transmembrane helix (UniProt Q88KB9), and the assimilatory NADPH‑sulfite reductase holoenzyme is a soluble cytoplasmic complex composed of the CysJ flavoprotein and CysI hemoprotein (Ghazi Esfahani et al., 2025, PMID 40140349; Wu et al., 1991, PMID 1987123). It therefore performs its reaction in the cytoplasm, drawing reducing equivalents from cytoplasmic NADPH — in contrast to membrane‑bound/periplasmic respiratory nitrite/sulfite reductases (e.g., cytochrome *c* nitrite reductase NrfA).

---

## 7. Supported and Refuted Hypotheses

**Supported**
- H1: PP_2371/*cysI* encodes sulfite reductase hemoprotein (β subunit). **Supported** (domain architecture, cofactor keywords, orthology; PMIDs 9315848, 1987123, 40140349).
- H2: The enzyme catalyzes the six‑electron reduction of sulfite to sulfide. **Supported** (PMIDs 9315848, 40140349, 32851831).
- H3: Catalysis occurs at a siroheme–[4Fe‑4S] coupled center via a bridging cysteine, using a push‑pull mechanism. **Supported** (PMIDs 32851831, 9315848).
- H4: The gene product functions in the assimilatory sulfate‑reduction/cysteine‑biosynthesis pathway; loss abolishes H₂S. **Supported** (PMIDs 23086550, 16159395).
- H5: The product is a soluble cytoplasmic hemoprotein partnering the CysJ diflavin flavoprotein. **Supported** (PMIDs 40140349, 1987123; UniProt features).

**Refuted / excluded**
- That PP_2371 is a **dissimilatory** (respiratory) sulfite reductase — excluded by family/domain type and aerobic assimilatory context.
- That the physiological substrate is nitrite — nitrite reduction is a documented *in vitro* side activity but the biological role is sulfite reduction for cysteine biosynthesis.

---

## 8. Limitations and Future Directions

- **No direct biochemical/structural study of PP_2371 itself** was found; the functional assignment rests on strong orthology to experimentally characterized CysI/SiRHP proteins (primarily *E. coli*) and on genetic evidence from other bacteria. Direct enzymatic assay, cofactor quantitation, and structure determination of the *P. putida* protein would confirm the inference.
- **Operon structure and regulation in KT2440** (e.g., *cysJIH* organization, CysB‑type control, sulfur‑starvation induction) were not experimentally verified here and warrant genomic/transcriptomic confirmation.
- **Electron‑donor partner in *Pseudomonas*.** While *E. coli* uses the NADPH diflavin flavoprotein CysJ, some organisms use ferredoxin/flavodoxin donors; the exact physiological reductant for PP_2371 should be confirmed.

---

## 9. Key References
- Crane BR, Siegel LM, Getzoff ED. Structures of the siroheme- and Fe4S4-containing active center of sulfite reductase… *Biochemistry* 1997. PMID **9315848**.
- Askenasy I, Stroupe ME. The Siroheme‑[4Fe‑4S] Coupled Center. 2020. PMID **32851831**.
- Ghazi Esfahani et al. Structure of dimerized assimilatory NADPH‑dependent sulfite reductase… 2025. PMID **40140349** (also PMID 38915618).
- Wu JY, Siegel LM, Kredich NM. High‑level expression of *E. coli* NADPH‑sulfite reductase (cysJ/cysI; cysG/siroheme). 1991. PMID **1987123**.
- Tan et al. H₂S formation by *cysIJ*‑inactivated *Zymomonas mobilis*. 2013. PMID **23086550**.
- Rückert et al. *C. glutamicum* assimilatory sulphate‑reduction *cys* cluster. 2005. PMID **16159395**.
- Kolko et al. Alternative siroheme synthesis; *cysG* required for sulfite reduction. 2001. PMID **11114933**.
- Colman et al. Structural evolution of dissimilatory sulfite reductase (contrast). 2022. PMID **35122336**.
- Borum & Monty. CysB regulation of cysteine biosynthetic enzymes. 1976. PMID **1107320**.


## Artifacts

- [OpenScientist final report](cysI-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](cysI-deep-research-openscientist_artifacts/final_report.pdf)