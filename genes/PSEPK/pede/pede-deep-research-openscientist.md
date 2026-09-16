---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T06:14:28.881459'
end_time: '2026-08-31T07:13:16.967657'
duration_seconds: 3528.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pede
  gene_symbol: pedE
  uniprot_accession: Q88JH5
  protein_description: 'RecName: Full=Quinoprotein alcohol dehydrogenase PedE {ECO:0000303|PubMed:28655819};
    EC=1.1.2.8 {ECO:0000305|PubMed:28655819}; AltName: Full=Ca(2+)-dependent pyrroloquinoline
    quinone-dependent alcohol dehydrogenase {ECO:0000303|PubMed:28655819}; Short=Ca(2+)-dependent
    PQQ-ADH {ECO:0000303|PubMed:28655819}; Flags: Precursor;'
  gene_info: Name=pedE {ECO:0000303|PubMed:28655819}; Synonyms=qedH-I {ECO:0000312|EMBL:AAN68282.1};
    OrderedLocusNames=PP_2674 {ECO:0000312|EMBL:AAN68282.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial PQQ dehydrogenase family.
  protein_domains: ADHI. (IPR034119); PQQ_b-propeller_rpt. (IPR018391); PQQ_MeOH/EtOH_DH.
    (IPR017512); PQQ_rpt_dom. (IPR002372); Quinoprotein_ADH-like_sf. (IPR011047)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pede-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pede-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JH5
- **Protein Description:** RecName: Full=Quinoprotein alcohol dehydrogenase PedE {ECO:0000303|PubMed:28655819}; EC=1.1.2.8 {ECO:0000305|PubMed:28655819}; AltName: Full=Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydrogenase {ECO:0000303|PubMed:28655819}; Short=Ca(2+)-dependent PQQ-ADH {ECO:0000303|PubMed:28655819}; Flags: Precursor;
- **Gene Information:** Name=pedE {ECO:0000303|PubMed:28655819}; Synonyms=qedH-I {ECO:0000312|EMBL:AAN68282.1}; OrderedLocusNames=PP_2674 {ECO:0000312|EMBL:AAN68282.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial PQQ dehydrogenase family.
- **Key Domains:** ADHI. (IPR034119); PQQ_b-propeller_rpt. (IPR018391); PQQ_MeOH/EtOH_DH. (IPR017512); PQQ_rpt_dom. (IPR002372); Quinoprotein_ADH-like_sf. (IPR011047)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pedE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pedE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pedE** (gene ID: pede, UniProt: Q88JH5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *pedE* (PP_2674, UniProt Q88JH5)
## Quinoprotein Alcohol Dehydrogenase PedE in *Pseudomonas putida* KT2440

---

## Summary

**PedE (gene *pedE*, synonym *qedH-I*, ordered locus PP_2674; UniProt Q88JH5) is a soluble, periplasmic, Ca²⁺- and pyrroloquinoline-quinone (PQQ)-dependent quinoprotein alcohol dehydrogenase (EC 1.1.2.8) from *Pseudomonas putida* KT2440.** Its primary function is to catalyze the initial oxidation of a broad range of volatile and aromatic alcohols (and their aldehydes) in the bacterial periplasm, transferring the abstracted electrons through its PQQ cofactor to a dedicated periplasmic cytochrome *c*. The enzyme is the calcium-utilizing, "lanthanide-free" partner in a functionally redundant pair with the lanthanide-dependent enzyme PedH (PP_2679), and the two are inversely regulated by rare-earth-element (REE) availability — a regulatory phenomenon known as the "REE switch."

The reaction catalyzed is: **primary alcohol + 2 Fe(III)-[cytochrome *c*] → aldehyde + 2 Fe(II)-[cytochrome *c*] + 2 H⁺**. PedE has notably broad substrate specificity: it oxidizes linear primary alcohols across a C2–C8 range (ethanol, butanol, hexanol, octanol), secondary alcohols (e.g., butan-2-ol), aromatic alcohols (2-phenylethanol, cinnamyl alcohol), the isoprenoid alcohol farnesol, and aldehydes (converting them to carboxylic acids). More recent work has extended its documented substrate range to include several diols of biotechnological interest — (2S,3S)-2,3-butanediol, (R)-1,3-butanediol, and 1,4-butanediol. Structurally, PedE is a 631-amino-acid precursor bearing an N-terminal signal peptide (residues 1–33) that is cleaved during periplasmic export; the mature enzyme folds into the characteristic eight-bladed β-propeller quinoprotein-dehydrogenase architecture, binds one PQQ molecule and two Ca²⁺ ions per subunit, uses His358 as the catalytic proton acceptor, and functions as a homodimer.

Biologically, PedE performs the committed first step of several periplasmic catabolic routes. It initiates the **Ped pathway** that converts 2-phenylethanol to phenylacetic acid (feeding into the phenylacetyl-CoA catabolon), a **glycerol-utilization route** (glycerol → glyceraldehyde → glycerate), and **butanediol degradation** pathways. Transcription of *pedE* is controlled by the PedS2/PedR2 two-component system together with the response regulator PedR1, and its activity is favored under lanthanide-scarce conditions. Together, these features define PedE as a versatile periplasmic redox biocatalyst positioned at the entry point of volatile-alcohol and diol metabolism in *P. putida*.

---

## Gene/Protein Identity Verification

Before presenting the findings, the target identity was verified against the UniProt reference. All literature discussed below refers to the correct gene and organism:

| Attribute | Reference (UniProt Q88JH5) | Literature confirmation |
|-----------|---------------------------|-------------------------|
| Gene symbol | *pedE* (syn. *qedH-I*) | Confirmed in Wehrmann et al. 2017 ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)) |
| Locus tag | PP_2674 | Explicitly cited as "PedE (PP_2674)" |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125) | Matches all primary studies |
| EC number | 1.1.2.8 (alcohol dehydrogenase, cytochrome *c* acceptor) | Consistent with reaction |
| Family | Bacterial PQQ dehydrogenase family | Confirmed as PQQ-ADH |
| Domains | PQQ β-propeller repeats, Quinoprotein ADH-like SF | Confirmed by biochemistry |

**Verification outcome:** The gene symbol *pedE*, the locus tag PP_2674, the organism, the enzyme family, and the domain architecture are all mutually consistent between the UniProt entry and the primary literature. There is no ambiguity — this is a well-characterized enzyme with dedicated biochemical studies. Research proceeded with high confidence.

---

## Key Findings

### Finding 1: PedE is a Ca²⁺-dependent PQQ alcohol dehydrogenase with broad substrate specificity

The most direct and authoritative characterization of PedE comes from the biochemical study by Wehrmann and colleagues (2017, *mBio*), who purified both PedE and its paralog PedH and assayed their enzymatic activities. They established that **PedE (PP_2674) is the Ca²⁺-dependent counterpart of the lanthanide-dependent PedH**, and that it is active on "a range of substrates... including linear and aromatic primary and secondary alcohols, as well as aldehydes" ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)). This places PedE firmly in EC class 1.1.2.8 (alcohol dehydrogenase using cytochrome *c* as the electron acceptor) and within the bacterial PQQ dehydrogenase family.

The breadth of substrate acceptance is a defining feature. Rather than being specialized for a single alcohol, PedE tolerates:
- **Linear primary alcohols** spanning at least C2 to C8 (ethanol, butan-1-ol, hexan-1-ol, octan-1-ol);
- **Secondary alcohols** (e.g., butan-2-ol);
- **Aromatic alcohols** (2-phenylethanol, cinnamyl alcohol);
- **Isoprenoid/terpenoid alcohols** (farnesol);
- **Aldehydes**, which are further oxidized to the corresponding carboxylic acids (e.g., acetaldehyde → acetate).

This broad-spectrum activity makes PedE a generalist "first responder" enzyme for the entry of diverse alcoholic compounds into central metabolism. The catalytic requirement for calcium (as opposed to a lanthanide) is what distinguishes PedE from PedH and gives it its physiological identity as the constitutively-competent, lanthanide-independent enzyme.

### Finding 2: PedE functions in the periplasm and feeds electrons to cytochrome *c*

PedE operates in the **periplasmic space**, not the cytoplasm. Two lines of evidence support this localization. First, the UniProt entry (Q88JH5) annotates the protein as a **precursor** carrying an N-terminal signal peptide (residues 1–33), the classic hallmark of Sec-dependent export to the periplasm. Second, Wehrmann et al. (2017) describe this entire enzyme class in periplasmic terms, noting that "many Gram-negative bacteria have evolved periplasmic oxidation systems based on pyrroloquinoline quinone-dependent alcohol dehydrogenases (PQQ-ADHs) that are often functionally redundant" ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)).

The mechanistic logic of periplasmic localization is that PedE uses the non-covalently bound cofactor **PQQ** as its redox prosthetic group to abstract a hydride/electrons from the alcohol substrate, and then re-oxidizes PQQ by passing electrons to an independent cytochrome *c*. This electron-transfer paradigm was established genetically by Arias et al. (2008), who described PQQ as "a prosthetic group of certain alcohol dehydrogenases that transfers electrons to an independent cytochrome *c*" ([PMID: 18177365](https://pubmed.ncbi.nlm.nih.gov/18177365/)). The periplasmic location is functionally sensible: it allows the cell to oxidize substrates at the periplasm–membrane interface and dump the electrons directly into the respiratory chain via cytochrome *c*, coupling alcohol oxidation to energy conservation without importing potentially toxic substrates into the cytoplasm. The supporting accessory machinery — PQQ biosynthesis (encoded by *pqqABCDEF*) and cytochrome *c* maturation (Ccm system) — is required for a functional holoenzyme.

### Finding 3: PedE initiates the Ped pathway (2-phenylethanol → phenylacetic acid) and volatile-alcohol/glycerol catabolism

The physiological pathway context of PedE was defined by Arias et al. (2008, *Environmental Microbiology*), who genetically dissected the **Ped catabolic route** (*PedS1R1ABCS2R2DEFGHI*) in *Pseudomonas putida*. They showed this route is "needed for the uptake of 2-phenylethanol and for its oxidation to phenylacetic acid via phenylacetaldehyde" ([PMID: 18177365](https://pubmed.ncbi.nlm.nih.gov/18177365/)). Critically, they concluded that the pathway requires "two quinoprotein alcohol dehydrogenases" — these being PedE and PedH — operating alongside "two different two-component signal-transducing systems."

In this pathway, PedE catalyzes the first oxidation: **2-phenylethanol → phenylacetaldehyde**. A downstream aldehyde dehydrogenase then converts phenylacetaldehyde to phenylacetic acid, which enters the phenylacetyl-CoA catabolon for ring degradation. This makes PedE the committed entry enzyme for aromatic-alcohol catabolism.

Beyond aromatic alcohols, PedE's role extends to other volatile substrates. Wehrmann et al. (2020, *mBio*) demonstrated that PedE and/or PedH initiate a **novel glycerol-utilization route** in which glycerol is oxidized to glyceraldehyde and then to glycerate — a lanthanum-responsive, substrate-specific metabolic capability that broadens the physiological importance of these quinoproteins beyond classic alcohol catabolism ([PMID: 32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/)).

### Finding 4: PedE (Ca²⁺) and PedH (Ln³⁺) are functionally redundant and inversely regulated by lanthanides — the "REE switch"

One of the most biologically interesting aspects of PedE is that it does not act alone: it is one of two functionally interchangeable enzymes whose deployment depends on metal availability. Wehrmann et al. (2017) established the **functional redundancy** of PedE and PedH and showed that their expression is inversely regulated in response to lanthanide availability, with sensitivity in the physiologically remarkable 1–10 nM La³⁺ range ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)). PedE is used when lanthanides are scarce (relying on the ubiquitous Ca²⁺), whereas PedH is used when lanthanides are available (using a lanthanide ion in its active site).

The molecular basis of this switch was elucidated by Wehrmann et al. (2018, *mSphere*), who demonstrated that the **PedS2/PedR2 two-component system** (PP_2671/PP_2672) governs the REE switch ([PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/)). In the absence of lanthanides, the sensor histidine kinase PedS2 phosphorylates the response regulator PedR2, which then **activates transcription of *pedE* and represses *pedH***. When lanthanides become available, PedS2's kinase activity is lowered, reversing the regulatory output and switching the cell from PedE to PedH. This elegant regulatory architecture allows *P. putida* to exploit whichever cofactor — calcium or lanthanide — is available in its environment while maintaining the same overall catalytic capability.

```
        LANTHANIDES SCARCE                    LANTHANIDES AVAILABLE
        ─────────────────                     ─────────────────────
        PedS2 kinase ON                       PedS2 kinase LOW
              │                                     │
              ▼                                     ▼
        PedR2 ~P (active)                     PedR2 (less active)
              │                                     │
       ┌──────┴──────┐                       ┌──────┴──────┐
       ▼             ▼                        ▼             ▼
   pedE ON       pedH OFF                 pedE OFF      pedH ON
   (Ca²⁺-ADH)                                          (Ln³⁺-ADH)
       │                                                   │
       └───────────► ALCOHOL OXIDATION ◄──────────────────┘
                     (functionally redundant)
```

### Finding 5: PedE substrate range extends to industrially relevant diols

Recent enzyme-assay and gene-deletion studies have significantly expanded the known substrate scope of PedE to include **diols**, which are of considerable biotechnological interest. Three independent lines of evidence contribute here:

- **2,3-Butanediol:** Liu et al. (2021, *Frontiers in Bioengineering and Biotechnology*) confirmed by enzyme assays that "two quinoprotein alcohol dehydrogenases, PedE (PP2674) and PedH (PP2679), were confirmed to be responsible for (2S,3S)-2,3-BDO dehydrogenation" to acetoin ([PMID: 34513815](https://pubmed.ncbi.nlm.nih.gov/34513815/)).
- **1,3-Butanediol:** Arumugam et al. (2026, *Applied and Environmental Microbiology*) showed the *ped* cluster oxidizes (R)-1,3-butanediol to (R)-3-hydroxybutyrate, and that "gene deletion and enzyme assays identified *pedE* and PP_2049 as essential for (R)-1,3-BDO catabolism" ([PMID: 42328986](https://pubmed.ncbi.nlm.nih.gov/42328986/)).
- **1,4-Butanediol:** Op de Hipt et al. (2025) noted that PedE catalyzes the initial oxidation of 1,4-butanediol in *P. putida* (a capability absent in the related *P. taiwanensis*).

The ability to oxidize diols positions PedE as a valuable biocatalyst for the conversion of these C4 platform chemicals into higher-value oxidized products (acetoin, 3-hydroxybutyrate), and demonstrates that the enzyme's broad specificity is not limited to mono-alcohols.

### Finding 6: PedE is a soluble quinoprotein capable of direct electron transfer to electrodes — an engineerable biocatalyst

Wehrmann and Klebensberger (2018, *Microbial Biotechnology*) characterized PedE (PP_2674) specifically as a **soluble** quinoprotein (distinguishing it from membrane-bound quinoproteins) and highlighted the biotechnological appeal of the PQQ-ADH class. They noted that "due to their ability for direct electron transfer to electrodes, the utilization of rare earth metals as cofactor, and their periplasmic localization, pyrroloquinoline quinone-dependent alcohol dehydrogenases (PQQ-ADHs) represent an interesting class of biocatalysts" ([PMID: 29239114](https://pubmed.ncbi.nlm.nih.gov/29239114/)).

To improve PedE's utility as an industrial biocatalyst, this study engineered a **thermostable and solvent-tolerant triple mutant (R91D/E408P/N410K)** using a heterologous whole-cell screening approach in *E. coli*. The engineered variant exhibited a melting-temperature increase of ~7 °C and roughly double the DMSO tolerance of the wild-type enzyme. This work confirms both the soluble periplasmic nature of PedE and its tractability for protein engineering, underscoring its promise for biosensor and bioelectrocatalysis applications.

### Finding 7: *pedE* transcription requires PedR1 and the PedS2/PedR2 two-component system; REE uptake requires the PedA1A2BC transporter

The regulatory network controlling *pedE* is layered. Arumugam et al. (2026) used promoter–GFP fusions to show that **full activation of the *pedE* promoter requires both PedR1 and the PedS2–PedR2 two-component system**, and — challenging a previously held "indirect-only" model — demonstrated that PedR1 acts as a **direct activator** of catabolic genes ([PMID: 42328986](https://pubmed.ncbi.nlm.nih.gov/42328986/)).

On the metal-supply side, Wehrmann et al. (2019, *Frontiers in Microbiology*) showed that REE-dependent (i.e., PedH-favoring) growth on 2-phenylethanol requires the **ABC transporter PedA1A2BC** for cytoplasmic lanthanide uptake, and that iron availability modulates the REE switch, likely through mismetallation of the sensor kinase PedS2. This reveals that the PedE/PedH switch is embedded in a broader metal-homeostasis network, integrating signals from lanthanide, calcium, and iron availability.

### Finding 8: Structural and mechanistic details of PedE

Integrating the UniProt annotation (Q88JH5) with comparative structural inference from the closely related quinoprotein ethanol dehydrogenase QEDH/ExaA (*P. aeruginosa*, UniProt Q9Z4J7) yields a detailed structural picture:

| Feature | Detail |
|---------|--------|
| Precursor length | 631 amino acids |
| Signal peptide | Residues 1–33 (cleaved) |
| Mature chain | Residues 34–631 |
| Fold | Eight-bladed β-propeller (quinoprotein ADH-like superfamily) |
| Cofactors | 1 PQQ (non-covalent) + 2 Ca²⁺ per subunit |
| Ca²⁺ sites | One active-site Ca²⁺ (adjacent to PQQ, aids catalysis); one N-terminal structural Ca²⁺ |
| Catalytic residue | His358 (proton acceptor) |
| Oligomeric state | Homodimer |
| Electron acceptor | Inducible cytochrome *c*550 (encoded by an adjacent gene) |
| Localization | Periplasm |
| Reaction | primary alcohol + 2 Fe(III)-[cyt *c*] → aldehyde + 2 Fe(II)-[cyt *c*] + 2 H⁺ (EC 1.1.2.8) |

Documented substrates include ethanol, butan-1-ol, butan-2-ol, hexan-1-ol, octan-1-ol, 2-phenylethanol, cinnamyl alcohol, and farnesol (each oxidized to the corresponding aldehyde), plus aldehyde→carboxylate reactions (e.g., acetaldehyde → acetate). The mechanistic assignment as a PQQ-dependent periplasmic quinoprotein is anchored by Wehrmann et al. (2017), who describe these as "periplasmic oxidation systems based on pyrroloquinoline quinone-dependent alcohol dehydrogenases" ([PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/)). Note that the structural details (His358, the two Ca²⁺ sites, the homodimeric state) are inferred by strong homology to characterized quinoprotein ADHs rather than from an experimental PedE crystal structure, which has not yet been reported.

---

## Mechanistic Model / Interpretation

The findings cohere into a single, well-supported mechanistic model of PedE as the **calcium-utilizing entry enzyme for periplasmic alcohol/diol oxidation** in *P. putida* KT2440.

**Catalytic cycle:**

```
   Periplasm
   ─────────────────────────────────────────────────────────
   R-CH₂OH  (alcohol substrate: ethanol, butanol, hexanol,
      │      octanol, 2-phenylethanol, farnesol, diols...)
      │
      ▼
   ┌──────────────────────────────────┐
   │   PedE homodimer                  │
   │   β-propeller fold                │
   │   PQQ + Ca²⁺(active) + Ca²⁺(struct)│    His358 = proton acceptor
   │                                   │
   │   R-CH₂OH ──► R-CHO + 2H⁺ + 2e⁻   │
   │        (PQQ → PQQH₂ → PQQ)        │
   └──────────────┬───────────────────┘
                  │ 2 e⁻
                  ▼
        cytochrome c550 (Fe³⁺ → Fe²⁺)
                  │
                  ▼
        respiratory electron transport chain
        (energy conservation)
```

**Pathway integration:** PedE sits at the head of multiple convergent catabolic routes. Its broad substrate specificity means it acts as a metabolic funnel, taking chemically diverse alcohols and channeling their oxidation products into central metabolism:

| Substrate | PedE product | Downstream fate |
|-----------|--------------|-----------------|
| 2-Phenylethanol | Phenylacetaldehyde | → Phenylacetic acid → phenylacetyl-CoA catabolon (Ped pathway) |
| Glycerol | Glyceraldehyde | → Glycerate → central metabolism |
| (2S,3S)-2,3-Butanediol | Acetoin | → C4 metabolism |
| (R)-1,3-Butanediol | (R)-3-Hydroxybutyrate | → β-oxidation-linked catabolism |
| 1,4-Butanediol | 4-Hydroxybutyraldehyde | → succinate route |
| Ethanol / short-chain alcohols | Acetaldehyde etc. | → Acetate → acetyl-CoA |

**Regulatory integration:** PedE is the "default" enzyme deployed under lanthanide-scarce conditions. The PedS2/PedR2 two-component system senses lanthanide status and reciprocally regulates *pedE* (ON without REE) and *pedH* (ON with REE), while PedR1 provides direct activation of the promoter and the PedA1A2BC ABC transporter supplies lanthanides for the alternative PedH branch. The net effect is a robust, environment-responsive system that guarantees alcohol-oxidizing capacity regardless of whether calcium or lanthanides dominate the local environment. PedE and PedH are thus not redundant "spares" in a trivial sense but a metal-adaptive pair, of which PedE is the phylogenetically ancient, universally-available (Ca²⁺-based) member.

---

## Evidence Base

| Study | PMID | Contribution | Support/Challenge |
|-------|------|--------------|-------------------|
| Wehrmann et al. 2017, *mBio* — *Functional Role of Lanthanides in Enzymatic Activity and Transcriptional Regulation of PQQ-ADHs* | [28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) | Direct biochemical characterization of purified PedE and PedH; establishes Ca²⁺-dependence, broad substrate range, periplasmic PQQ-ADH class, functional redundancy, and lanthanide-responsive regulation | **Primary support** for Findings 1, 2, 4, 8 |
| Arias et al. 2008, *Environ Microbiol* — *Genetic analyses...conversion of 2-phenylethylamine and 2-phenylethanol into phenylacetic acid* | [18177365](https://pubmed.ncbi.nlm.nih.gov/18177365/) | Genetically defines the Ped pathway (*PedS1R1ABCS2R2DEFGHI*); establishes PQQ→cytochrome *c* electron transfer and role of two quinoprotein ADHs | **Primary support** for Findings 2, 3 |
| Wehrmann et al. 2018, *mSphere* — *The PedS2/PedR2 Two-Component System Is Crucial for the REE Switch* | [30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/) | Demonstrates PedS2/PedR2 control of the REE switch; PedR2~P activates *pedE*, represses *pedH* | **Primary support** for Finding 4 |
| Wehrmann & Klebensberger 2018, *Microb Biotechnol* — *Engineering thermal stability and solvent tolerance of the soluble quinoprotein PedE* | [29239114](https://pubmed.ncbi.nlm.nih.gov/29239114/) | Characterizes PedE as soluble, periplasmic, electrode-active; engineers thermostable/solvent-tolerant triple mutant | **Primary support** for Findings 6, 7 |
| Liu et al. 2021, *Front Bioeng Biotechnol* — *Dehydrogenation Mechanism of Three Stereoisomers of Butane-2,3-Diol* | [34513815](https://pubmed.ncbi.nlm.nih.gov/34513815/) | Enzyme assays confirm PedE oxidizes (2S,3S)-2,3-butanediol | **Support** for Finding 5 |
| Arumugam et al. 2026, *Appl Environ Microbiol* — *(R)-1,3-butanediol catabolism* | [42328986](https://pubmed.ncbi.nlm.nih.gov/42328986/) | Gene-deletion/enzyme assays show *pedE* essential for (R)-1,3-BDO catabolism; PedR1 is a direct promoter activator | **Support** for Findings 5, 7 |
| Wehrmann et al. 2020, *mBio* — *The Cellular Response to Lanthanum...Novel Route for Glycerol Metabolism* | [32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/) | Shows PedE/PedH initiate a glycerol-utilization route | **Support** for Finding 3 |

The evidence base is unusually strong for a bacterial enzyme from a non-model-organism context: PedE has been directly purified and biochemically assayed, its regulation has been dissected genetically, and its substrate range has been repeatedly extended through targeted experiments. The experimental evidence (purified-enzyme assays, gene deletions, promoter fusions) is prioritized here over purely bioinformatic inference, though the fine structural details rest on homology modeling.

---

## Limitations and Knowledge Gaps

1. **No experimental crystal structure of PedE.** The detailed active-site geometry — including the assignment of His358 as the catalytic proton acceptor and the two Ca²⁺ coordination sites — is inferred by homology to the well-characterized quinoprotein ethanol dehydrogenase QEDH/ExaA of *P. aeruginosa* (UniProt Q9Z4J7). A direct PedE structure would confirm these assignments and clarify the structural determinants of its broad substrate specificity.

2. **Quantitative kinetics are incompletely catalogued.** While the qualitative substrate range is well established, comprehensive kinetic parameters (kcat, Km, catalytic efficiencies) across the full substrate panel — particularly comparing PedE with PedH under matched conditions — are not fully reported in the reviewed literature. This limits our ability to rank substrate preferences precisely.

3. **The identity of the physiological cytochrome *c* acceptor** ("cytochrome *c*550, encoded by an adjacent gene") is annotated by similarity; direct demonstration of the specific electron-acceptor partner for PedE in vivo would strengthen the electron-transfer model.

4. **The molecular basis of iron modulation of the REE switch** (proposed mismetallation of PedS2) remains a hypothesis rather than a demonstrated mechanism.

5. **1,3- and 1,4-butanediol findings derive from very recent (2025–2026) studies** whose abstracts were available but whose full experimental details were not deeply reviewed here; these should be considered emerging rather than fully consolidated.

---

## Proposed Follow-up Experiments / Actions

1. **Determine the PedE crystal structure** (or a high-quality cryo-EM/AlphaFold3 model with holoenzyme cofactors) to experimentally confirm the His358 catalytic residue, the two Ca²⁺ sites, and the PQQ-binding pocket, and to rationalize the broad substrate specificity.

2. **Comprehensive steady-state kinetics** of purified PedE across its full substrate panel (C2–C8 alcohols, secondary alcohols, aromatic alcohols, farnesol, and the three butanediols), reporting kcat/Km, to build a quantitative substrate-preference profile and compare directly with PedH.

3. **Identify and validate the cognate cytochrome *c* acceptor** via in vitro reconstitution and gene-deletion of the adjacent cytochrome *c*550 gene, confirming the electron-transfer partner.

4. **Structure-guided engineering** building on the R91D/E408P/N410K thermostable variant, to further tune PedE for diol oxidation (2,3-/1,3-/1,4-butanediol) toward biotechnological production of acetoin and 3-hydroxybutyrate.

5. **Mechanistic test of the iron–PedS2 mismetallation hypothesis** using purified PedS2 kinase assays under varying metal conditions to determine whether iron directly alters kinase activity and thereby the REE switch.

6. **In vivo flux measurements** (e.g., ¹³C metabolic flux analysis) of *pedE* single-deletion vs. *pedE/pedH* double-deletion strains grown on each substrate class, to quantify PedE's specific contribution to periplasmic alcohol/diol catabolism under lanthanide-scarce conditions.

---

## Conclusion

PedE (PP_2674, Q88JH5) is a soluble, periplasmic, calcium- and PQQ-dependent quinoprotein alcohol dehydrogenase (EC 1.1.2.8) that catalyzes the initial oxidation of a broad range of primary, secondary, aromatic, and isoprenoid alcohols — as well as diols and aldehydes — passing electrons via its PQQ cofactor to a periplasmic cytochrome *c*. It performs the committed entry step of multiple catabolic routes (the Ped pathway to phenylacetic acid, a glycerol-utilization route, and butanediol degradation) and is the lanthanide-free member of a functionally redundant, REE-switch-regulated enzyme pair with PedH, predominating when lanthanides are scarce.


## Artifacts

- [OpenScientist final report](pede-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pede-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28655819
2. PMID:18177365
3. PMID:32345644
4. PMID:30158283
5. PMID:34513815
6. PMID:42328986
7. PMID:29239114