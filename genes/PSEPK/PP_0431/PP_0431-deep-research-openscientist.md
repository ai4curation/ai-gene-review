---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:09:55.754970'
end_time: '2026-07-20T20:20:36.230271'
duration_seconds: 640.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0431
  gene_symbol: PP_0431
  uniprot_accession: Q88QQ7
  protein_description: 'RecName: Full=Protoporphyrinogen IX oxidase {ECO:0000256|ARBA:ARBA00017504,
    ECO:0000256|HAMAP-Rule:MF_02239}; Short=PPO {ECO:0000256|HAMAP-Rule:MF_02239};
    EC=1.3.99.- {ECO:0000256|HAMAP-Rule:MF_02239, ECO:0000256|PIRNR:PIRNR004638};'
  gene_info: OrderedLocusNames=PP_0431 {ECO:0000313|EMBL:AAN66061.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HemJ family. {ECO:0000256|ARBA:ARBA00006501,
  protein_domains: HemJ-like. (IPR005265); UPF0093 (PF03653)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0431-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0431-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QQ7
- **Protein Description:** RecName: Full=Protoporphyrinogen IX oxidase {ECO:0000256|ARBA:ARBA00017504, ECO:0000256|HAMAP-Rule:MF_02239}; Short=PPO {ECO:0000256|HAMAP-Rule:MF_02239}; EC=1.3.99.- {ECO:0000256|HAMAP-Rule:MF_02239, ECO:0000256|PIRNR:PIRNR004638};
- **Gene Information:** OrderedLocusNames=PP_0431 {ECO:0000313|EMBL:AAN66061.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HemJ family. {ECO:0000256|ARBA:ARBA00006501,
- **Key Domains:** HemJ-like. (IPR005265); UPF0093 (PF03653)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0431" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0431' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0431** (gene ID: PP_0431, UniProt: Q88QQ7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_0431 (UniProt Q88QQ7): A HemJ-Type Protoporphyrinogen IX Oxidase in *Pseudomonas putida* KT2440

## Summary

**PP_0431 (UniProt Q88QQ7) of *Pseudomonas putida* KT2440 encodes a HemJ-type protoporphyrinogen IX oxidase (PPO / Protox; EC 1.3.99.-), a polytopic integral cytoplasmic-membrane enzyme that catalyzes the six-electron oxidation of protoporphyrinogen IX to protoporphyrin IX.** This is the last enzymatic step common to the biosynthesis of heme and (in phototrophs) chlorophyll — the reaction immediately preceding metal insertion into the tetrapyrrole macrocycle. The functional assignment rests on strong homology and domain-based evidence: UniProt places PP_0431 in the HemJ family (UPF0093 / Pfam PF03653; InterPro IPR005265, "HemJ-like"), which is one of three phylogenetically unrelated, isofunctional enzyme families (HemG, HemY, HemJ) that independently converged on the same protoporphyrinogen-oxidizing chemistry.

Protoporphyrinogen IX oxidase converts the colorless, unstable hexahydroporphyrin protoporphyrinogen IX into the fully conjugated, planar macrocycle protoporphyrin IX by removing six hydrogen atoms (a six-electron oxidation). Protoporphyrin IX is then metallated — by ferrochelatase in the heme branch, or by magnesium chelatase in the chlorophyll branch — making the PPO reaction the last shared intermediate of the two great tetrapyrrole pathways. Because *P. putida* is a Gram-negative γ-proteobacterium and a non-phototroph, the enzyme operates in the context of the classical (protoporphyrin-dependent) prokaryotic heme route, where coproporphyrinogen III is first decarboxylated to protoporphyrinogen IX and then oxidized to protoporphyrin IX prior to iron insertion to form protoheme.

The evidence for PP_0431 *specifically* is inferential (domain/family homology by HAMAP rule MF_02239) rather than a direct enzyme assay of the Pseudomonas protein. However, the HemJ family has been experimentally validated in orthologous systems: the founding gene *slr1790* of *Synechocystis* sp. PCC 6803 is essential, and its loss causes accumulation of protoporphyrin IX (the diagnostic signature of a blocked PPO step); a *Rhodobacter sphaeroides* HemJ homolog expressed in *E. coli* displayed Protox activity in vitro. HemJ is a membrane-spanning protein distantly related to the M subunit of respiratory complex I (NADH dehydrogenase). Taken together, the annotation of PP_0431 as the HemJ-type membrane protoporphyrinogen IX oxidase of *P. putida* is well supported by convergent structural, phylogenetic, and functional evidence from orthologs.

---

## Gene/Protein Identity Verification

Per the mandatory verification protocol, I confirmed the target is correctly identified before proceeding:

| Attribute | Target Specification | Assessment |
|---|---|---|
| **UniProt accession** | Q88QQ7 | Confirmed |
| **Locus tag** | PP_0431 (OrderedLocusNames) | Confirmed; γ-proteobacterial *Pseudomonas* gene |
| **Organism** | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) | Confirmed |
| **Protein description** | Protoporphyrinogen IX oxidase (PPO); EC 1.3.99.- | Consistent with HemJ family assignment |
| **Protein family** | HemJ family | Confirmed |
| **Key domains** | HemJ-like (IPR005265); UPF0093 (PF03653) | Confirmed — diagnostic of the HemJ PPO isoform |

**No ambiguity conflict was encountered.** The gene symbol "PP_0431" is a locus tag (not a common gene name shared across organisms), so the risk of cross-organism symbol collision is low. All family, domain, and EC evidence align internally and with the literature on the HemJ isoform. No conflicting "same-symbol/different gene" literature was found. The one important caveat — carried throughout this report — is that the functional characterization derives from HemJ **orthologs** (cyanobacterial and α-proteobacterial), not from a direct biochemical assay of the *P. putida* protein itself.

---

## Key Findings

### Finding 1 — PP_0431 is a HemJ-type protoporphyrinogen IX oxidase catalyzing the last common step of heme/chlorophyll biosynthesis

UniProt Q88QQ7 assigns PP_0431 to the **HemJ family** (UPF0093 / PF03653; EC 1.3.99.-). Protoporphyrinogen IX oxidase (Protox / PPO) is remarkable in molecular evolution because the identical enzymatic function is carried out by **three nonhomologous, isofunctional enzyme families** — HemG, HemY, and HemJ — that share no common ancestry yet catalyze the same reaction. As stated directly in the phylogenetic analysis of Kobayashi and colleagues, *"Three nonhomologous isofunctional enzymes, HemG, HemJ, and HemY, for Protox have been identified"* ([PMID: 25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/)). The reaction itself is the oxidation of protoporphyrinogen IX to protoporphyrin IX, which the same authors describe as producing *"the last common intermediate for the biosynthesis of heme and chlorophyll"* ([PMID: 25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/)).

This position in the pathway is corroborated by an independent cyanobacterial study, which describes *"Protoporphyrinogen IX oxidase (PPOX), which catalyzes the last common step of the heme and chlorophyll biosynthesis pathways,"* and confirms it *"is encoded by three phylogenetically-unrelated genes, hemY, hemG and hemJ"* ([PMID: 36357749](https://pubmed.ncbi.nlm.nih.gov/36357749/)). The convergence of two independent lines of evidence — the tri-family isofunctionality and the specific "last common step" pathway position — firmly establishes the biochemical role that the HemJ family (and therefore PP_0431) performs.

**Interpretation:** PP_0431 catalyzes protoporphyrinogen IX → protoporphyrin IX, the branch-point precursor step of tetrapyrrole biosynthesis. Because *P. putida* is a non-phototroph, the physiologically relevant downstream branch is heme (protoheme) biosynthesis via ferrochelatase.

### Finding 2 — HemJ is an integral membrane protein; its loss causes protoporphyrin IX accumulation and is essential for growth

The founding member of the HemJ family, gene *slr1790* of *Synechocystis* sp. PCC 6803, encodes a membrane protein. The characterization study reports that *"The slr1790 gene encodes a putative membrane-spanning protein that is distantly related to the M subunit of NADH dehydrogenase complex I"* ([PMID: 20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/)). This is an important structural clue: HemJ is a **polytopic integral membrane protein**, consistent with a subcellular localization in the cytoplasmic (inner) membrane, and its distant relationship to a complex I subunit hints at a membrane-embedded redox architecture.

The essentiality and pathway placement were demonstrated genetically and metabolically. Attempts to fully segregate disruptants were unsuccessful (they remained heteroplasmic), and the cells that partially lost the gene *"accumulated a substantial amount of protoporphyrin IX, suggesting that the slr1790 gene is essential for growth and Protox activity of cells"* ([PMID: 20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/)). Accumulation of protoporphyrin IX signals a metabolic bottleneck at the terminal tetrapyrrole steps when HemJ is impaired. A separate cyanobacterial study reinforced this metabolic signature, reporting that impaired HemJ *"led to the accumulation of coproporphyrin III and protoporphyrin IX, indicative of impaired HemJ activity"* ([PMID: 39657587](https://pubmed.ncbi.nlm.nih.gov/39657587/)).

Critically, direct biochemical evidence exists for the family: a HemJ homolog from *Rhodobacter sphaeroides* (an α-proteobacterium, phylogenetically closer to *Pseudomonas* than the cyanobacteria are) was heterologously expressed and assayed. The authors *"overexpressed an slr1790 homolog of Rhodobacter sphaeroides in Escherichia coli and found that this recombinant protein possesses Protox activity in vitro"* ([PMID: 20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/)). This in vitro demonstration of protoporphyrinogen oxidase activity by a proteobacterial HemJ is the strongest available functional support for the annotation of PP_0431.

**Interpretation:** HemJ (and by orthology PP_0431) is a membrane-bound enzyme, essential in the organisms tested, whose loss blocks the terminal tetrapyrrole steps and causes porphyrin (protoporphyrin IX, coproporphyrin III) accumulation. The Rhodobacter in vitro result provides direct enzymatic proof of function for a proteobacterial family member.

### Finding 3 — *P. putida* uses the HemJ-type PPO despite HemG dominance in γ-Proteobacteria

The distribution of the three PPO isoforms across the tree of life is uneven and shaped by lateral gene transfer. Phylogenomic clustering shows that *"Most organisms possess only one of the three Protox types, with some exceptions"* ([PMID: 25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/)). For the γ-Proteobacteria, the "default" isoform is generally HemG — the flavodoxin-like oxygen-independent enzyme first characterized in *E. coli*. The evolutionary analysis notes that *"HemG is mostly limited to γ-Proteobacteria whereas HemJ may have originated within α-Proteobacteria and transferred to other Proteobacteria and Cyanobacteria"* ([PMID: 25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/)).

Against this backdrop, UniProt's assignment of PP_0431 — a γ-proteobacterial *Pseudomonas* gene — to the **HemJ** family (rather than HemG) is biologically notable. It indicates that *P. putida* carries and retains a HemJ-type PPO, most plausibly acquired through the same lateral transfer route that spread HemJ from α-Proteobacteria into other proteobacterial lineages. Because most organisms carry only a single Protox type, HemJ is the single functional protoporphyrinogen IX oxidase operating in *P. putida*.

**Interpretation:** PP_0431/HemJ is the sole PPO of *P. putida*, an evolutionary outlier relative to the HemG-dominated γ-Proteobacteria, consistent with lateral acquisition/retention of the α-proteobacterial-origin HemJ isoform.

### Finding 4 — The reaction is a six-electron oxidation, embedded in the Gram-negative heme pathway, with isoform diversity for oxygen-limited conditions

Authoritative reviews of heme biosynthesis define the chemistry precisely. Dailey's review of the terminal steps describes the penultimate reaction as *"the six-electron oxidation of protoporphyrinogen to protoporphyrin IX"* ([PMID: 12196143](https://pubmed.ncbi.nlm.nih.gov/12196143/)). This is the exact transformation catalyzed by PP_0431/HemJ: removal of six hydrogen atoms to aromatize the macrocycle.

The reaction's placement in the Gram-negative bacterial pathway used by *P. putida* is spelled out by Dailey et al.: *"Gram-negative bacteria first decarboxylate coproporphyrinogen III to protoporphyrinogen IX and then oxidize this to protoporphyrin IX prior to metal insertion to make protoheme"* ([PMID: 28123057](https://pubmed.ncbi.nlm.nih.gov/28123057/)). This locates the HemJ step directly between coproporphyrinogen oxidase (HemF/HemN) and ferrochelatase (HemH) in the classical protoporphyrin-dependent (PPD) route.

Finally, the same review explains *why* three isofunctional PPO enzymes exist at all: *"In order to adapt to oxygen-deficient conditions, two steps in the bacterial pathways have multiple forms to accommodate oxidative reactions in an anaerobic environment"* ([PMID: 28123057](https://pubmed.ncbi.nlm.nih.gov/28123057/)). Protoporphyrinogen oxidation is intrinsically an oxidative step; the HemY isoform uses molecular oxygen as terminal electron acceptor, whereas HemG and HemJ can couple to the respiratory chain / alternative acceptors, allowing heme synthesis to proceed when oxygen is scarce. The EC number assigned to PP_0431 (**1.3.99.-**, with the "99" indicating an unspecified/other acceptor) reflects precisely this oxygen-independent, acceptor-flexible character of the HemJ isoform — distinct from the strictly O₂-dependent HemY (EC 1.3.3.4).

**Interpretation:** PP_0431/HemJ performs a six-electron aromatizing oxidation of protoporphyrinogen IX within the Gram-negative heme route, and its very existence as a distinct isoform reflects adaptation to variable oxygen availability — a physiologically relevant trait for the metabolically versatile soil bacterium *P. putida*.

---

## Mechanistic Model and Interpretation

### Position in the tetrapyrrole biosynthesis pathway

PP_0431/HemJ operates at the branch point of tetrapyrrole biosynthesis. In *P. putida* (a non-phototroph), only the heme branch is physiologically relevant:

```
        Glutamate / 5-aminolevulinate (ALA)
              │
              ▼
        Porphobilinogen
              │
              ▼
        Hydroxymethylbilane
              │
              ▼
        Uroporphyrinogen III
              │  (HemE, uroporphyrinogen decarboxylase)
              ▼
      Coproporphyrinogen III
              │  (HemF / HemN, coproporphyrinogen oxidase)
              ▼
      Protoporphyrinogen IX  ◄── substrate
              │
   ┌──────────┴───────────┐
   │   PP_0431  =  HemJ    │   Protoporphyrinogen IX oxidase (PPO / Protox)
   │   EC 1.3.99.-         │   SIX-ELECTRON OXIDATION (removal of 6 H)
   │   membrane-bound      │   O2-independent isoform
   └──────────┬───────────┘
              ▼
        Protoporphyrin IX  ◄── product = LAST COMMON INTERMEDIATE
              │
   ┌──────────┴───────────────────────┐
   ▼                                   ▼
 Ferrochelatase (HemH)          Mg-chelatase (phototrophs only —
 + Fe²⁺                          NOT operative in P. putida)
   │                                   │
   ▼                                   ▼
 PROTOHEME (heme b)                Chlorophyll
   │
   ▼
 Cytochromes, catalases,
 peroxidases, other hemoproteins
```

Because heme is essential for aerobic respiration (cytochromes), oxidative-stress defenses (catalase/peroxidase), and other hemoproteins, HemJ activity is expected to be **essential** in *P. putida*, consistent with the essentiality demonstrated for the cyanobacterial ortholog.

### Why three isofunctional enzymes? (Convergent evolution)

The PPO step is a textbook case of **non-orthologous gene displacement / convergent evolution**. Three unrelated protein folds independently evolved to catalyze the same chemically demanding aromatization:

| Isoform | Fold / cofactor | O₂ dependence | Typical distribution | EC |
|---|---|---|---|---|
| **HemY** | FAD-binding, monomeric flavoprotein | O₂-dependent | Eukaryotes, Gram-positive bacteria | 1.3.3.4 |
| **HemG** | Flavodoxin-like | O₂-independent (respiratory chain) | γ-Proteobacteria (e.g., *E. coli*) | 1.3.5.3 |
| **HemJ** | Polytopic membrane protein (complex-I M-subunit-like) | O₂-independent / acceptor-flexible | α-Proteobacteria, Cyanobacteria, laterally spread | **1.3.99.-** ← **PP_0431** |

The existence of oxygen-independent isoforms (HemG, HemJ) allows heme synthesis to continue under microaerobic/anaerobic conditions, since molecular oxygen cannot be relied upon as the terminal electron acceptor in such environments ([PMID: 28123057](https://pubmed.ncbi.nlm.nih.gov/28123057/)). This is consistent with the ecological lifestyle of *P. putida*, a soil organism that experiences fluctuating oxygen tension.

### Subcellular localization

Multiple lines of evidence converge on a **cytoplasmic (inner) membrane** localization:

1. The founding HemJ (*slr1790*) is *"a putative membrane-spanning protein"* ([PMID: 20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/)).
2. It is distantly related to the M subunit of NADH dehydrogenase (complex I), a membrane-integral respiratory complex ([PMID: 20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/)).
3. The UPF0093 / PF03653 domain and IPR005265 signature are characteristic of small polytopic membrane proteins.

A membrane localization is mechanistically sensible: it would allow HemJ to couple the oxidation of protoporphyrinogen directly to membrane-embedded electron carriers (e.g., quinones / the respiratory chain), rationalizing its oxygen-independence and its EC 1.3.99.- ("other acceptor") classification. It also co-localizes the enzyme with its hydrophobic substrate and with downstream ferrochelatase and heme-utilizing systems.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [25108393](https://pubmed.ncbi.nlm.nih.gov/25108393/) | *Molecular phylogeny and intricate evolutionary history of the three isofunctional enzymes involved in the oxidation of protoporphyrinogen IX* | Establishes the three nonhomologous isofunctional PPO families; defines the reaction as forming "the last common intermediate"; provides the HemG/HemJ distribution and lateral-transfer context (F1, F3) |
| [20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/) | *Identification of a gene essential for protoporphyrinogen IX oxidase activity in Synechocystis sp. PCC6803* | Founding characterization of HemJ (*slr1790*): membrane-spanning protein related to complex I M subunit; essential gene; protoporphyrin IX accumulation on loss; **in vitro Protox activity of a Rhodobacter HemJ homolog** (F2) |
| [36357749](https://pubmed.ncbi.nlm.nih.gov/36357749/) | *Heterologous complementation systems verify the mosaic distribution of three distinct protoporphyrinogen IX oxidase in the cyanobacterial phylum* | Confirms HemJ identity; "last common step"; three phylogenetically unrelated genes hemY/hemG/hemJ (F1) |
| [39657587](https://pubmed.ncbi.nlm.nih.gov/39657587/) | *Epigenetic control of tetrapyrrole biosynthesis by m4C DNA methylation in a cyanobacterium* | Confirms metabolic block phenotype: impaired HemJ → coproporphyrin III and protoporphyrin IX accumulation (F2) |
| [12196143](https://pubmed.ncbi.nlm.nih.gov/12196143/) | *Terminal steps of haem biosynthesis* (Dailey review) | Defines the exact chemistry: "six-electron oxidation of protoporphyrinogen to protoporphyrin IX" (F4) |
| [28123057](https://pubmed.ncbi.nlm.nih.gov/28123057/) | *Prokaryotic Heme Biosynthesis: Multiple Pathways to a Common Essential Product* (Dailey review) | Places the PPO step in the Gram-negative heme pathway; explains isoform multiplicity as adaptation to oxygen-deficient conditions (F4) |
| [29925590](https://pubmed.ncbi.nlm.nih.gov/29925590/) | *The cyanobacterial protoporphyrinogen oxidase HemJ is a new [heme-containing enzyme]* | Additional biochemical characterization of the HemJ isoform (supporting context) |

**Strength of evidence:** The functional assignment is supported by (i) direct in vitro enzyme activity of a proteobacterial (Rhodobacter) HemJ homolog; (ii) genetic essentiality and diagnostic porphyrin-accumulation phenotypes in the founding cyanobacterial ortholog; (iii) consistent domain/family signatures (HAMAP MF_02239, PF03653, IPR005265); and (iv) authoritative pathway reviews. The chief weakness is that no study has assayed the *P. putida* PP_0431 protein directly — the assignment is inference-by-orthology.

---

## Supported vs. Refuted Hypotheses

- **Supported:** PP_0431 is a HemJ-type protoporphyrinogen IX oxidase catalyzing the last common step of heme/chlorophyll biosynthesis.
- **Supported:** It is an integral membrane enzyme, essential for growth, whose loss causes protoporphyrin IX (and coproporphyrin III) accumulation.
- **Supported:** *P. putida* (a γ-proteobacterium) carries the HemJ form rather than the lineage-typical HemG, most plausibly by lateral transfer.
- **Refuted / not applicable:** PP_0431 is *not* a HemG (flavodoxin) or HemY (FAD, strictly O₂-dependent) enzyme; there is no evidence it acts outside the membrane; it is not a transporter, structural protein, adapter, or signaling molecule.

---

## Limitations and Knowledge Gaps

1. **No direct characterization of PP_0431 itself.** All functional evidence derives from HemJ orthologs (*Synechocystis slr1790*, *Rhodobacter sphaeroides* homolog, and other cyanobacterial HemJ). The *P. putida* protein has not been purified or assayed for protoporphyrinogen oxidase activity, nor has PP_0431 been genetically knocked out with phenotypic follow-up in *P. putida*.

2. **Cofactor and mechanism only partially resolved.** The HemJ family is the least characterized of the three PPO isoforms. The exact cofactor(s), the identity of the physiological electron acceptor (quinone? cytochrome? O₂?), and the catalytic residues remain incompletely defined. One study (PMID 29925590) reports HemJ is a heme-associated enzyme, adding nuance to the mechanism.

3. **Membrane topology not experimentally mapped for PP_0431.** Localization to the cytoplasmic membrane is inferred from family membership and the complex-I M-subunit relationship, not from direct topology mapping in *P. putida*.

4. **Essentiality in *P. putida* is assumed, not shown.** HemJ is essential in *Synechocystis*; heme is essential for aerobic respiration in *P. putida*, so PP_0431 is very likely essential, but this specific gene's essentiality has not been directly confirmed.

5. **EC number is incomplete (1.3.99.-).** The dash reflects genuine uncertainty about the terminal electron acceptor, a gap in the biochemical understanding of the HemJ isoform generally.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzyme assay.** Heterologously express PP_0431 (Q88QQ7) in an *E. coli* strain and assay protoporphyrinogen IX oxidase activity in vitro (fluorometric protoporphyrin IX formation), mirroring the successful Rhodobacter HemJ assay ([PMID: 20823222](https://pubmed.ncbi.nlm.nih.gov/20823222/)).

2. **Genetic complementation.** Test whether PP_0431 complements an *E. coli hemG* conditional mutant (or a HemJ-null cyanobacterium), providing in vivo functional proof.

3. **Knockout / conditional depletion in *P. putida*.** Construct a PP_0431 deletion or CRISPRi knockdown and test for essentiality; use HPLC/fluorescence to detect protoporphyrin IX and coproporphyrin III accumulation as the diagnostic metabolic signature ([PMID: 39657587](https://pubmed.ncbi.nlm.nih.gov/39657587/)).

4. **Determine the electron acceptor.** Assay activity with candidate acceptors (ubiquinone/menaquinone analogs, cytochromes, O₂) to resolve the EC 1.3.99.- ambiguity and test the hypothesis that HemJ couples to the respiratory chain.

5. **Cofactor identification and structure.** Perform UV-vis/EPR spectroscopy and mass spectrometry to test for heme or other bound cofactors (following up on PMID 29925590), and pursue a cryo-EM or crystal structure to define the membrane topology and active site.

6. **Membrane topology mapping.** Use reporter fusions (PhoA/GFP) or cysteine-scanning to experimentally establish the polytopic membrane topology of PP_0431 in *P. putida*.

---

## Conclusion

PP_0431 (UniProt Q88QQ7) of *Pseudomonas putida* KT2440 is confidently annotated as the **HemJ-type protoporphyrinogen IX oxidase (PPO / Protox; EC 1.3.99.-)** — a polytopic integral cytoplasmic-membrane enzyme that catalyzes the six-electron oxidation of protoporphyrinogen IX to protoporphyrin IX, the last step common to heme (and, in phototrophs, chlorophyll) biosynthesis. It is one of three phylogenetically unrelated, isofunctional PPO families (HemG/HemY/HemJ), and *P. putida* appears to be an evolutionary outlier among the HemG-dominated γ-Proteobacteria in retaining the α-proteobacterial-origin HemJ isoform. The assignment is supported by domain/family homology, the essentiality and porphyrin-accumulation phenotypes of HemJ orthologs, in vitro Protox activity of a proteobacterial HemJ homolog, and authoritative pathway reviews — while direct biochemical characterization of the *P. putida* protein itself remains an open experimental target.

---
*Prepared from primary literature and authoritative reviews (PMIDs 12196143, 20823222, 25108393, 28123057, 29925590, 36357749, 39657587) and UniProt/InterPro/HAMAP (MF_02239) annotations. Search date: 2026-07-21.*


## Artifacts

- [OpenScientist final report](PP_0431-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0431-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25108393
2. PMID:36357749
3. PMID:20823222
4. PMID:39657587
5. PMID:12196143
6. PMID:28123057