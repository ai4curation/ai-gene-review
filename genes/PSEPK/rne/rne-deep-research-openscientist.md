---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T19:33:25.602214'
end_time: '2026-08-31T20:08:10.101851'
duration_seconds: 2084.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rne
  gene_symbol: rne
  uniprot_accession: Q88LM4
  protein_description: 'RecName: Full=Ribonuclease E {ECO:0000256|HAMAP-Rule:MF_00970};
    Short=RNase E {ECO:0000256|HAMAP-Rule:MF_00970}; EC=3.1.26.12 {ECO:0000256|HAMAP-Rule:MF_00970};'
  gene_info: Name=rne {ECO:0000256|HAMAP-Rule:MF_00970, ECO:0000313|EMBL:AAN67524.1};
    OrderedLocusNames=PP_1905 {ECO:0000313|EMBL:AAN67524.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the RNase E/G family. RNase G subfamily.
  protein_domains: NA-bd_OB-fold. (IPR012340); RNA-bd_AU-1/RNase_E/G. (IPR019307);
    RNase_E. (IPR028878); RNase_E/G. (IPR004659); RNase_E_G_thioredoxin-like. (IPR048583)
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
citation_count: 30
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rne-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rne-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LM4
- **Protein Description:** RecName: Full=Ribonuclease E {ECO:0000256|HAMAP-Rule:MF_00970}; Short=RNase E {ECO:0000256|HAMAP-Rule:MF_00970}; EC=3.1.26.12 {ECO:0000256|HAMAP-Rule:MF_00970};
- **Gene Information:** Name=rne {ECO:0000256|HAMAP-Rule:MF_00970, ECO:0000313|EMBL:AAN67524.1}; OrderedLocusNames=PP_1905 {ECO:0000313|EMBL:AAN67524.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the RNase E/G family. RNase G subfamily.
- **Key Domains:** NA-bd_OB-fold. (IPR012340); RNA-bd_AU-1/RNase_E/G. (IPR019307); RNase_E. (IPR028878); RNase_E/G. (IPR004659); RNase_E_G_thioredoxin-like. (IPR048583)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rne" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rne' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rne** (gene ID: rne, UniProt: Q88LM4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Ribonuclease E (rne / PP_1905, UniProt Q88LM4) in *Pseudomonas putida* KT2440: A Functional Annotation Report

**UniProt:** Q88LM4 · **Gene:** *rne* · **Locus:** PP_1905 · **EC:** 3.1.26.12
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)

## Summary

The **rne** gene of *Pseudomonas putida* KT2440 (UniProt **Q88LM4**, ordered locus **PP_1905**) encodes **Ribonuclease E (RNase E; EC 3.1.26.12)**, a **1,091-residue (≈120.9 kDa), Mg²⁺-dependent, single-strand-specific endoribonuclease** that is the central enzyme of bacterial RNA metabolism. Its primary catalytic function is the **endonucleolytic cleavage of single-stranded RNA in A- and U-rich regions**. It performs two overarching biological tasks: (1) the **maturation of stable RNA** — the 5′ processing of 16S and 5S ribosomal RNAs and the majority of tRNAs — and (2) the **initiation of messenger RNA decay**, in which its cleavage of the monophosphorylated intermediate is typically the rate-limiting, committed step of mRNA turnover.

A critical identification issue was resolved during this investigation. Although one automated UniProt annotation tag lists the "RNase G subfamily," the protein's length and domain architecture identify it **unambiguously as full-length RNase E**, not the shorter RNase G paralog. Q88LM4 comprises an N-terminal catalytic half (S1 RNA-binding domain, Mg²⁺ active site, and a zinc-linked tetramerization region) followed by a very large **C-terminal intrinsically disordered region (~residues 506–1091)** that is entirely absent from RNase G (~489 aa). This C-terminal domain (CTD) is the **scaffold of the RNA degradosome**, a multi-enzyme machine that recruits the exoribonuclease PNPase, the DEAD-box RNA helicase RhlB, and (in *E. coli*) enolase. The organism additionally encodes a *separate* RNase G (rng), confirming that PP_1905 is the RNase E ortholog.

Functionally, the enzyme carries out its work on the **cytoplasmic face of the inner membrane**, to which it is tethered as a peripheral membrane protein via an amphipathic helix in its CTD. This localization spatially organizes RNA turnover within the cell. Substrate recognition is governed by a dedicated **5′-monophosphate sensor pocket** and a **5′→3′ linear scanning mechanism** whose progress is impeded by RNA secondary structure, bound ribosomes, and base-paired small RNAs — a mechanism that sets mRNA lifetimes. Direct experimental evidence in the exact target organism (*P. putida* KT2440) demonstrates that RNase E is a non-redundant determinant of environmental lifestyle and stress endurance, with species-specific physiological roles that diverge from *E. coli*.

---

## Key Findings

### Finding 1 — Q88LM4 is full-length RNase E, not RNase G

The single most important interpretive result of this investigation is the correct sub-family assignment. UniProt Q88LM4 is **1,091 amino acids / 120.9 kDa**. Its domain architecture consists of: an N-terminal **S1 RNA-binding motif** (residues ~39–117); a **catalytic core** with Mg²⁺ active-site binding residues (positions ~300 and 343); a **zinc-tetramerization region** (residues 401–404) annotated as "required for zinc-mediated homotetramerization and catalytic activity"; and a **very large C-terminal intrinsically disordered region** (~506–1091) containing multiple low-complexity and charged segments.

This architecture matches *E. coli* RNase E (~1,061 aa; a catalytic N-domain plus a C-terminal scaffold) and is fundamentally distinct from the short RNase G paralog (~489 aa; catalytic domain only, no C-terminal scaffold). The authoritative **HAMAP-Rule MF_00970** assigns the "RNase E subfamily"; a conflicting, lower-quality automated ARBA rule listing "RNase G subfamily" is an annotation artifact superseded by the unambiguous full-length architecture. Importantly, *P. putida* KT2440 encodes a **separate RNase G** (rng), which was studied independently (see Finding 8), removing any doubt that PP_1905 is the RNase E ortholog.

### Finding 2 — Primary function: Mg²⁺-dependent, single-strand-specific endoribonuclease cleaving A/U-rich RNA (EC 3.1.26.12)

The catalytic activity, per UniProt/HAMAP MF_00970, is: **"Endonucleolytic cleavage of single-stranded RNA in A- and U-rich regions"** (EC 3.1.26.12), with a cofactor requirement of **1 Mg²⁺ per subunit** at the active site. This is corroborated by mechanistic structural biology: Koslover et al. (2008) describe RNase E as *"an essential bacterial endoribonuclease involved in the turnover of messenger RNA and the maturation of structured RNA precursors in Escherichia coli"* and report a crystal structure revealing *"a mechanism of RNA recognition and cleavage that explains the enzyme's preference for substrates possessing a 5′-monophosphate"* ([PMID: 18682225](https://pubmed.ncbi.nlm.nih.gov/18682225/)). The dual role — mRNA turnover plus structured-RNA maturation — is the defining functional signature of RNase E.

### Finding 3 — 5′-monophosphate sensing and 5′→3′ scanning govern substrate access and cleavage-site selection

RNase E does not cleave RNA at random. It preferentially binds a **5′-monophosphorylated end** via a dedicated 5′-sensor pocket, which potentiates catalytic efficacy (Hui & Belasco 2021, [PMID: 34643703](https://pubmed.ncbi.nlm.nih.gov/34643703/); Jourdan & McDowall 2008). Richards & Belasco (2019) demonstrated that the enzyme *"searches for cleavage sites by scanning linearly from the 5′-terminal monophosphate along single-stranded regions of RNA and that its progress is impeded by structural discontinuities"* ([PMID: 30852060](https://pubmed.ncbi.nlm.nih.gov/30852060/)). These discontinuities — bound proteins, translating ribosomes, and small-RNA base-pairing — are the physical determinants that set individual mRNA lifetimes.

A second, **5′-end-independent "direct entry"** mode also exists, in which RNase E *"can cleave certain RNAs rapidly without requiring a 5′-monophosphorylated end"* by simultaneously engaging multiple single-stranded segments (Kime et al. 2010, [PMID: 19889093](https://pubmed.ncbi.nlm.nih.gov/19889093/)). The 5′-monophosphate sensing property is conserved across the RNase E/G family: for RNase G, *"the presence of a 5′ monophosphate can enhance the affinity of RNase G binding to RNA"* ([PMID: 18078441](https://pubmed.ncbi.nlm.nih.gov/18078441/)).

### Finding 4 — Quaternary structure: a zinc-linked homotetramer (dimer of dimers)

The catalytic domain assembles into a **homotetramer** whose integrity depends on a shared Zn²⁺ ion — the so-called **"Zn-link."** Callaghan et al. (2005) showed that *"two protomers share a single zinc ion"* and that *"catalytic activity does not require zinc directly but does require the quaternary structure, for which the metal is essential"* ([PMID: 15779893](https://pubmed.ncbi.nlm.nih.gov/15779893/)). Mutation of the Zn-coordinating residues causes partial zinc loss, disruption of the tetramer into dimers, and effective catalytic inactivation.

Q88LM4 preserves this architecture exactly: residues 401–404 are annotated as "required for zinc-mediated homotetramerization and catalytic activity," and UniProt records 2 Zn²⁺ per homotetramer with a "dimer of dimers" subunit state. Interestingly, a minimal ~395-residue catalytic peptide can retain scanning and cleavage even without the Zn-link (Caruthers et al. 2006, [PMID: 16854990](https://pubmed.ncbi.nlm.nih.gov/16854990/)), which delimits the essential catalytic core and shows that the tetrameric quaternary structure, while physiologically important, is not strictly required for core enzymatic activity.

### Finding 5 — Biological processes: 5′-maturation of 16S/5S rRNA and most tRNAs, plus initiation of mRNA decay

HAMAP MF_00970 assigns to Q88LM4: *"Required for the maturation of 5S and 16S rRNAs and the majority of tRNAs. Also involved in the degradation of most mRNAs."* Each arm is supported by direct experimental work in *E. coli*:

- **rRNA maturation:** RNase E and RNase G together perform two-step 5′ maturation of 16S rRNA. Li et al. (1999) showed that *"when both RNase E and CafA are inactivated, 5′ maturation of 16S rRNA is completely blocked"* ([PMID: 10329633](https://pubmed.ncbi.nlm.nih.gov/10329633/)).
- **tRNA maturation:** RNase E generates the mature 3′ termini of the proline tRNAs by a single endonucleolytic cut immediately after the CCA determinant. Mohanty et al. (2016) reported that *"RNase E is primarily responsible for the endonucleolytic removal of the entire Rho-independent transcription terminator associated with the proK, proL and proM primary transcripts by cleaving immediately downstream of the CCA determinant"* ([PMID: 27288443](https://pubmed.ncbi.nlm.nih.gov/27288443/)).
- **mRNA decay:** RNase E cleavage of the monophosphorylated intermediate is frequently the committed, rate-limiting step of turnover. Luciano et al. (2012) found that for such transcripts *"their decay rate is limited by cleavage of the monophosphorylated intermediate, making RNase E critical for their rapid turnover"* ([PMID: 22984254](https://pubmed.ncbi.nlm.nih.gov/22984254/)).

### Finding 6 — Degradosome scaffold: the C-terminal disordered domain nucleates a multi-enzyme RNA-degradation machine

The UniProt SUBUNIT annotation for Q88LM4 states that it is a *"Component of the RNA degradosome, which is a multiprotein complex involved in RNA processing and mRNA degradation."* In *E. coli*, the degradosome is *"typically composed of the endoribonuclease RNase E, which also serves as a scaffold for the other components, the exoribonuclease PNPase, the RNA helicase RhlB, and enolase"* (Regonesi et al. 2006, [PMID: 16139413](https://pubmed.ncbi.nlm.nih.gov/16139413/)).

Critically, the scaffolding role maps to the **RNase E C-terminal half**. Domínguez-Malfavón et al. (2013) found that degradosome interactions are *"absent in a mutant strain that lacks the C-terminal half, supporting the role of the carboxy-end domain as the scaffold for the degradosome"* ([PMID: 23927922](https://pubmed.ncbi.nlm.nih.gov/23927922/)). Q88LM4 carries exactly this large C-terminal intrinsically disordered region (~506–1091), providing a direct structural basis for its scaffolding role.

### Finding 7 — Localization: cytoplasmic face of the inner membrane, spatially organizing mRNA degradation

The UniProt subcellular location for Q88LM4 is **Cytoplasm and Cell inner membrane (peripheral, cytoplasmic side)**. In *E. coli*, RNase E binds the inner membrane through an amphipathic "Segment A" helix in its CTD, and this tethering shapes where decay occurs. Kim et al. (2026) reported that co-transcriptional mRNA degradation *"is rare due to membrane localization of RNase E, except for transcripts encoding inner-membrane proteins"* ([PMID: 42174289](https://pubmed.ncbi.nlm.nih.gov/42174289/)). Single-molecule imaging confirms that the membrane-binding motif and the C-terminal domain govern RNase E localization and diffusion (Troyer et al. 2025, [PMID: 40093181](https://pubmed.ncbi.nlm.nih.gov/40093181/)).

### Finding 8 — Direct *P. putida* KT2440 evidence: RNase E is a distinct, non-redundant determinant of lifestyle and stress endurance

The most directly relevant experimental evidence comes from the exact target organism. Apura et al. (2021) constructed single-RNase deletion variants of *P. putida* KT2440 (PNPase, RNase R, RNase E, RNase III, RNase G) and analyzed growth, motility, morphology, and oxidative-stress responses, concluding that *"each ribonuclease is specifically related with different traits of the environmental lifestyle that distinctively characterizes this microorganism"* ([PMID: 33089610](https://pubmed.ncbi.nlm.nih.gov/33089610/)). Critically, *"the physiological responses of P. putida to the absence of each enzyme diverged significantly from those known previously in Escherichia coli,"* revealing species-specific regulatory functions. This study confirms in vivo that RNase E (PP_1905) functions in post-transcriptional adaptation and is functionally distinguishable from its paralog RNase G (rng).

### Finding 9 — Pseudomonas degradosome assembles on the RNase E CTD via short linear motifs; autoregulation tunes enzyme level

In Pseudomonadota, the degradosome *"assembles on the C-terminal domain (CTD) of RNase E through short linear motifs (SLiMs) that determine its composition and functionality"* (Geslain et al. 2025, [PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/)). In the closely related *P. aeruginosa*, the CTD's SLiMs mediate membrane attachment, RNA binding, complex clustering, and direct binding to PNPase and RhlB; CTD mutants are impaired in cold adaptation, pH response, and virulence.

The RNase E–PNPase interaction is conserved but evolutionarily re-wired: Paris et al. (2025) found that *"a different recognition mode arose for Pseudomonas aeruginosa, illustrating the evolutionary drive to maintain physical association of the two ribonucleases"* ([PMID: 41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/)). Enzyme level is feedback-controlled: RNase E *"controls the decay of its own mRNA by cleaving it within the 5′-untranslated region (UTR), thereby autoregulating its synthesis"* (Sousa et al. 2001, [PMID: 11722748](https://pubmed.ncbi.nlm.nih.gov/11722748/)), via an evolutionarily conserved 5′UTR stem-loop sensor (Diwa et al. 2000, [PMID: 10817759](https://pubmed.ncbi.nlm.nih.gov/10817759/)). Notably, *P. aeruginosa* RhlB is a distinct "Type II" helicase that RNase E regulates by antagonizing its phase separation rather than allosterically activating it (Hausmann et al. 2026, [PMID: 42581758](https://pubmed.ncbi.nlm.nih.gov/42581758/)).

### Finding 10 — Sequence-level confirmation: N-terminus and Zn-link CxxC signature are diagnostic of RNase E

Direct analysis of the Q88LM4 sequence (1,091 aa) seals the identification. The N-terminus is **'MKRMLINATQPEELRVALVDGQRLYDL…'**, essentially identical to the diagnostic N-terminal signature of *E. coli* RNase E ('MKRMLINATQ…') and distinct from RNase G. The **Zn-link motif is intact**: cysteines occur precisely at positions **401 and 404 (a CxxC pair)**, matching the UniProt-annotated "zinc-mediated homotetramerization and catalytic activity" region (401–404). Compositional analysis confirms the two-domain architecture: the N-terminal catalytic half (res 1–510) has a globular-like charged fraction (DEKR ≈ 0.30), whereas the C-terminal half (511–1091) is strongly enriched in charged residues (DEKR ≈ 0.38) and disorder-promoting residues (P/A/Q/S/G ≈ 0.44) — the compositional hallmark of the intrinsically disordered degradosome scaffold. RNase G (~489 aa) has no such C-terminal extension.

---

## Mechanistic Model / Interpretation

The findings integrate into a coherent picture of a single, bifunctional, membrane-anchored enzyme that governs the flow of RNA through the bacterial cell.

### Domain architecture (Q88LM4, 1,091 aa)

```
 N ──────────── CATALYTIC HALF (~1–510) ──────────── │ ── C-TERMINAL DISORDERED SCAFFOLD (~506–1091) ── C
   │        │           │          │                  │
  S1 RNA   Mg2+      Zn-link     5'-sensor            SLiMs: membrane helix, RNA-binding,
  domain   active  CxxC @401/404  pocket              PNPase-, RhlB-binding, clustering
 (39–117)  site                                       (intrinsically disordered; DEKR~0.38)
          (~300,343)
   \______ homotetramer (dimer of dimers) ______/      \___ nucleates the RNA degradosome ___/
                 (2 Zn2+ per tetramer)                       tethered to inner membrane
```

### Catalytic cycle and substrate selection

```
   5'-PPP-mRNA  ──(RppH pyrophosphohydrolase)──►  5'-P-mRNA
                                                     │
                                                     ▼
                              RNase E 5'-sensor pocket binds 5'-monophosphate
                                                     │
                                     5'→3' linear scanning along ssRNA
                                                     │
              ┌──────────────────────────────────────┴─────────────────────────────┐
              ▼                                                                      ▼
   obstacle (ribosome, structure,                                A/U-rich single-stranded site reached
   sRNA duplex) → scanning impeded                                              │
   → longer mRNA lifetime                                                       ▼
                                                        Mg2+-dependent endonucleolytic cleavage
                                                                               │
                                                  ┌────────────────────────────┴──────────────┐
                                                  ▼                                            ▼
                                    downstream fragments handed to               upstream fragment recycled
                                    PNPase/RhlB in the degradosome               (new monophosphorylated 5' end)
```

An alternative **"direct entry"** pathway bypasses the 5′-sensor, engaging multiple single-stranded segments at once, allowing rapid cleavage of certain substrates independent of the 5′-phosphorylation state.

### The two jobs of RNase E

| Function | Substrate | Outcome | Key evidence |
|---|---|---|---|
| **Stable-RNA maturation** | 16S rRNA precursor | Mature 5′ end (with RNase G) | [PMID: 10329633](https://pubmed.ncbi.nlm.nih.gov/10329633/) |
| | 5S rRNA precursor | Mature 5′ end | HAMAP MF_00970 |
| | Majority of tRNA precursors; proK/proL/proM | Mature 3′ end (cut after CCA) | [PMID: 27288443](https://pubmed.ncbi.nlm.nih.gov/27288443/) |
| **mRNA decay initiation** | Most cellular mRNAs | Rate-limiting first cut → degradosome | [PMID: 22984254](https://pubmed.ncbi.nlm.nih.gov/22984254/) |
| **Autoregulation** | Own rne mRNA 5′UTR | Feedback control of enzyme level | [PMID: 11722748](https://pubmed.ncbi.nlm.nih.gov/11722748/) |

### Spatial organization

The enzyme is a **peripheral inner-membrane protein** (cytoplasmic side). Because the degradosome is membrane-tethered while transcription/translation proceed in the nucleoid/cytoplasm, most mRNA degradation is spatially segregated from transcription — except for mRNAs encoding inner-membrane proteins, whose translation brings them to the membrane where RNase E resides. This membrane localization is a genuine regulatory layer, not an incidental property.

### RNase E vs. RNase G — resolving the annotation conflict

| Feature | RNase E (Q88LM4/PP_1905) | RNase G (rng, separate gene) |
|---|---|---|
| Length | 1,091 aa (~121 kDa) | ~489 aa (~50 kDa) |
| N-terminal catalytic domain | Yes | Yes (35% identity to RNase E N-domain) |
| Zn-link CxxC (401/404) | Yes | Variable |
| C-terminal disordered scaffold | **Yes (~506–1091)** | **No** |
| Degradosome scaffold | **Yes** | No |
| Membrane tether | Yes | No |
| Essentiality | Essential | Non-essential |

The full-length architecture, the diagnostic N-terminal 'MKRMLINATQ' signature, the intact Zn-link, and the presence of a separate rng gene in the genome collectively establish that PP_1905 is **RNase E**, and that the automated "RNase G subfamily" tag is an annotation artifact.

---

## Evidence Base

| PMID | Study (abbrev.) | How it supports the findings |
|---|---|---|
| [18682225](https://pubmed.ncbi.nlm.nih.gov/18682225/) | Crystal structure of E. coli RNase E apoprotein | Enzyme class, dual role, and 5′-monophosphate preference (F2) |
| [30852060](https://pubmed.ncbi.nlm.nih.gov/30852060/) | Obstacles to scanning govern mRNA lifetimes | Defines 5′→3′ linear scanning, obstacle-limited cleavage (F3) |
| [19889093](https://pubmed.ncbi.nlm.nih.gov/19889093/) | Rapid cleavage without 5′ monophosphate | Documents the "direct entry" 5′-end-independent mode (F3) |
| [18078441](https://pubmed.ncbi.nlm.nih.gov/18078441/) | Sensing of 5′ monophosphate by RNase G | 5′-monophosphate sensing conserved in RNase E/G family (F3) |
| [15779893](https://pubmed.ncbi.nlm.nih.gov/15779893/) | "Zn-link" metal-sharing interface | Zn-linked tetramer; quaternary structure essential (F4) |
| [16854990](https://pubmed.ncbi.nlm.nih.gov/16854990/) | Minimal RNase E peptide lacking tetramer domain | Delimits minimal catalytic core (F4) |
| [10329633](https://pubmed.ncbi.nlm.nih.gov/10329633/) | RNase G + RNase E in 16S rRNA 5′ maturation | Essential role in 16S rRNA maturation (F5) |
| [27288443](https://pubmed.ncbi.nlm.nih.gov/27288443/) | RNase E generates mature 3′ termini of Pro tRNAs | Direct role in tRNA 3′-end maturation (F5) |
| [22984254](https://pubmed.ncbi.nlm.nih.gov/22984254/) | Control of 5′-end-dependent mRNA degradation | RNase E as rate-limiting step in mRNA decay (F5) |
| [16139413](https://pubmed.ncbi.nlm.nih.gov/16139413/) | Degradosome composition by proteomics | Names RNase E scaffold; lists PNPase, RhlB, enolase (F6) |
| [23927922](https://pubmed.ncbi.nlm.nih.gov/23927922/) | Assembly/distribution of E. coli degradosome | Localizes scaffolding to C-terminal domain (F6) |
| [42174289](https://pubmed.ncbi.nlm.nih.gov/42174289/) | Spatial constraints on mRNA degradation | Ties inner-membrane localization to decay pattern (F7) |
| [40093181](https://pubmed.ncbi.nlm.nih.gov/40093181/) | Single-molecule imaging of RNase E | Membrane motif + CTD govern localization/diffusion (F7) |
| [33089610](https://pubmed.ncbi.nlm.nih.gov/33089610/) | Ribonucleases control traits of P. putida | **Direct evidence in target organism** (F8) |
| [40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/) | RNase E scaffolding domain in P. aeruginosa | Pseudomonas degradosome assembles on CTD via SLiMs (F9) |
| [41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/) | Multi-dentate RNase E–PNPase interaction | Association conserved but re-wired in Pseudomonas (F9) |
| [11722748](https://pubmed.ncbi.nlm.nih.gov/11722748/) | Autoregulation of E. coli RNase E | Autoregulation via 5′UTR self-cleavage (F9) |
| [10817759](https://pubmed.ncbi.nlm.nih.gov/10817759/) | Conserved RNA stem-loop sensor for rne | Conserved 5′UTR stem-loop drives autoregulation (F9) |
| [42581758](https://pubmed.ncbi.nlm.nih.gov/42581758/) | RNase E counteracts RhlB phase separation | Pseudomonas Type II RhlB regulation via condensate control (F9) |

**Supporting context papers:** RNase G quaternary structure and dimerization ([PMID: 14622423](https://pubmed.ncbi.nlm.nih.gov/14622423/)); RNase G in 16S/23S rRNA processing ([PMID: 10362534](https://pubmed.ncbi.nlm.nih.gov/10362534/), [PMID: 21717341](https://pubmed.ncbi.nlm.nih.gov/21717341/)); functional divergence of RNase E vs. RNase G ([PMID: 20507976](https://pubmed.ncbi.nlm.nih.gov/20507976/)); *P. aeruginosa* RNase E variant, iron piracy and virulence ([PMID: 37027441](https://pubmed.ncbi.nlm.nih.gov/37027441/)); phage-encoded Dip inhibitor of the Pseudomonas degradosome ([PMID: 27447594](https://pubmed.ncbi.nlm.nih.gov/27447594/), [PMID: 27834591](https://pubmed.ncbi.nlm.nih.gov/27834591/)); RraA modulator of RNase E ([PMID: 21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/)); RhlE helicase–RNase E interactions in Pseudomonas ([PMID: 34151378](https://pubmed.ncbi.nlm.nih.gov/34151378/), [PMID: 38874491](https://pubmed.ncbi.nlm.nih.gov/38874491/)).

**Note on the RNase E/G family nuance:** Several papers ([PMID: 20507976](https://pubmed.ncbi.nlm.nih.gov/20507976/), [PMID: 14622423](https://pubmed.ncbi.nlm.nih.gov/14622423/)) emphasize that RNase G and the RNase E catalytic domain share ~35% identity but have distinct in vivo activities — RNase G cannot substitute for RNase E under normal conditions. This underscores that even though Q88LM4's catalytic domain is homologous to RNase G, its full-length architecture and scaffold domain make it the functionally distinct RNase E.

---

## Limitations and Knowledge Gaps

1. **Mechanistic evidence is largely extrapolated from *E. coli*.** The catalytic mechanism (5′-sensing, scanning, Zn-link tetramer, cleavage-site specificity) and the specific rRNA/tRNA maturation substrates are established in *E. coli*, not directly in *P. putida* KT2440. Apura et al. (2021, [PMID: 33089610](https://pubmed.ncbi.nlm.nih.gov/33089610/)) explicitly caution that *P. putida* physiological responses diverge from *E. coli*, so extrapolation carries uncertainty.

2. **No enzymatic characterization of Q88LM4 itself.** There is no purified-protein biochemistry (kcat, Km, substrate profiling) reported specifically for the *P. putida* KT2440 RNase E. All catalytic parameters are inferred from orthologs.

3. **Degradosome composition in *P. putida* is inferred, not directly mapped.** The Pseudomonas degradosome has been characterized primarily in *P. aeruginosa* ([PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/), [PMID: 41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/), [PMID: 42581758](https://pubmed.ncbi.nlm.nih.gov/42581758/)). The exact SLiM inventory, partner set (e.g., which RhlB/RhlE helicase, whether enolase associates), and CTD interaction interfaces of the KT2440 protein remain to be experimentally defined.

4. **The specific mRNA regulon of *P. putida* RNase E is unknown.** Which transcripts are direct RNase E substrates, and how this shapes KT2440's environmental adaptation and biotechnological phenotypes (e.g., solvent tolerance, aromatic-compound catabolism), has not been mapped transcriptome-wide.

5. **Subcellular localization is annotation-based.** The inner-membrane, cytoplasmic-side localization for Q88LM4 comes from UniProt/ortholog inference; direct imaging in *P. putida* has not been performed.

6. **Essentiality and autoregulation of rne in KT2440** are assumed from the family but not directly demonstrated in this organism.

---

## Proposed Follow-up Experiments / Actions

1. **Biochemical characterization of purified Q88LM4.** Express and purify the *P. putida* RNase E catalytic domain; measure Mg²⁺ dependence, 5′-monophosphate stimulation, A/U-site specificity, and Zn-link tetramerization to confirm mechanism directly in this organism.

2. **Transcriptome-wide substrate mapping.** Apply RNA-seq/degradome-seq or TIER-seq to an rne conditional depletion strain of KT2440 to catalog direct cleavage sites and define the RNase E regulon, distinguishing it from the RNase G (rng) regulon.

3. **Degradosome pull-down / interactomics.** Co-immunoprecipitation or proximity labeling of tagged RNase E in KT2440 to establish the native degradosome composition (PNPase, RhlB/RhlE helicase, enolase or alternatives) and validate the SLiM-based CTD assembly inferred from *P. aeruginosa*.

4. **CTD truncation genetics.** Construct CTD-deletion and membrane-motif mutants to test their effects on growth, cold/oxidative-stress adaptation, motility, and degradosome assembly — paralleling the *P. aeruginosa* CTD-mutant phenotypes.

5. **Localization imaging.** Fluorescent-fusion single-molecule imaging in live *P. putida* to confirm inner-membrane localization and quantify how the membrane motif and CTD govern diffusion and clustering.

6. **Autoregulation test.** Assay whether the rne 5′UTR forms the conserved stem-loop sensor and mediates feedback control of RNase E levels in KT2440, as in *E. coli*.

---

## Conclusion

The gene **rne / PP_1905 (Q88LM4)** of *Pseudomonas putida* KT2440 encodes the **full-length Ribonuclease E**, the master endoribonuclease of bacterial RNA metabolism. It is a Mg²⁺-dependent, single-strand-specific endonuclease (EC 3.1.26.12) that cleaves A/U-rich RNA, preferentially at 5′-monophosphorylated substrates via a 5′→3′ scanning mechanism. It matures 16S/5S rRNA and most tRNAs and initiates (usually rate-limits) the decay of most mRNAs. Its zinc-linked catalytic domain forms a homotetramer, while its large C-terminal intrinsically disordered domain scaffolds the RNA degradosome and tethers the machine to the cytoplasmic face of the inner membrane. Direct evidence in the target organism confirms non-redundant, species-specific physiological roles, distinct from its separately encoded paralog RNase G. The UniProt "RNase G subfamily" tag is an automated-annotation artifact superseded by the protein's unambiguous full-length RNase E architecture.


## Artifacts

- [OpenScientist final report](rne-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rne-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:18682225
2. PMID:34643703
3. PMID:30852060
4. PMID:19889093
5. PMID:18078441
6. PMID:15779893
7. PMID:16854990
8. PMID:10329633
9. PMID:27288443
10. PMID:22984254
11. PMID:16139413
12. PMID:23927922
13. PMID:42174289
14. PMID:40093181
15. PMID:33089610
16. PMID:40096066
17. PMID:41036625
18. PMID:11722748
19. PMID:10817759
20. PMID:42581758
21. PMID:14622423
22. PMID:10362534
23. PMID:21717341
24. PMID:20507976
25. PMID:37027441
26. PMID:27447594
27. PMID:27834591
28. PMID:21063756
29. PMID:34151378
30. PMID:38874491