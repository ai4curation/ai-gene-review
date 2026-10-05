---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T00:11:39.220687'
end_time: '2026-08-13T00:35:13.332492'
duration_seconds: 1414.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: soxA
  gene_symbol: soxA
  uniprot_accession: Q88R09
  protein_description: 'SubName: Full=Sarcosine oxidase subunit alpha {ECO:0000313|EMBL:AAN65956.1};
    EC=1.5.3.1 {ECO:0000313|EMBL:AAN65956.1};'
  gene_info: Name=soxA {ECO:0000313|EMBL:AAN65956.1}; OrderedLocusNames=PP_0325 {ECO:0000313|EMBL:AAN65956.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the GcvT family.
  protein_domains: 2Fe-2S-bd_N. (IPR042204); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom.
    (IPR023753); GcvT/YgfZ/DmdA. (IPR028896); GcvT/YgfZ_C. (IPR029043)
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: soxA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: soxA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88R09
- **Protein Description:** SubName: Full=Sarcosine oxidase subunit alpha {ECO:0000313|EMBL:AAN65956.1}; EC=1.5.3.1 {ECO:0000313|EMBL:AAN65956.1};
- **Gene Information:** Name=soxA {ECO:0000313|EMBL:AAN65956.1}; OrderedLocusNames=PP_0325 {ECO:0000313|EMBL:AAN65956.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the GcvT family.
- **Key Domains:** 2Fe-2S-bd_N. (IPR042204); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); GcvT/YgfZ/DmdA. (IPR028896); GcvT/YgfZ_C. (IPR029043)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "soxA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'soxA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **soxA** (gene ID: soxA, UniProt: Q88R09) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *soxA* (PP_0325 / Q88R09) — α-Subunit of Heterotetrameric Sarcosine Oxidase in *Pseudomonas putida* KT2440

## Summary

The gene **soxA** (ordered locus **PP_0325**; UniProt **Q88R09**) of *Pseudomonas putida* strain KT2440 encodes the **~1004-residue α-subunit — the largest, catalytic subunit — of heterotetrameric sarcosine oxidase (TSOX; EC 1.5.3.1)**. TSOX is a soluble, cytoplasmic, bifunctional **diflavin metalloenzyme** built from four different polypeptides (α, β, γ, δ) that assemble into an αβγδ complex. The intact enzyme catalyzes the **oxidative demethylation of sarcosine (N-methylglycine) to glycine + hydrogen peroxide**, and, when tetrahydrofolate (THF) is present, **couples the removed one-carbon unit to the formation of 5,10-methylene-tetrahydrofolate**. This links the enzyme directly to folate-dependent one-carbon metabolism.

Critically, the specific role of the **α-subunit encoded by *soxA* is not the sarcosine-oxidation step itself** — that occurs at the noncovalent FAD site housed in the β-subunit. Instead, the α-subunit binds **NAD⁺ and tetrahydrofolate** and carries out the **second half-reaction**: it is the **5,10-methylene-THF synthase module**, condensing the reactive channeled one-carbon iminium/formaldehyde intermediate onto folate and releasing glycine. This function resides in the C-terminal **GcvT / glycine-cleavage T-protein (aminomethyltransferase)-like folate-binding domain**, while an N-terminal Rossmann/glutathione-reductase-like **dinucleotide-binding domain** holds NAD⁺. The two catalytic sites of the assembled enzyme lie ~35 Å apart and are connected by a large (~10,000 Å³) internal cavity that channels the reactive intermediate from the β-subunit oxidation site to the α-subunit folate site — protecting the cell from a toxic, diffusible formaldehyde equivalent.

This assignment is supported by a convergent evidence chain: (1) the genomic context in KT2440, where PP_0325 sits within the canonical **glyA-soxBDAG-purU** folate/one-carbon operon; (2) crystallographic and biochemical studies of orthologous TSOX enzymes from *Pseudomonas maltophilia*, *Corynebacterium* sp. U-96 and P-1, and *Arthrobacter*, which localize NAD⁺ and folate to the α-subunit; and (3) quantitative full-length orthology (~47–48% identity across the entire ~1000-residue length) between Q88R09 and these structurally/biochemically characterized α-subunits, which justifies transferring their functional assignments to KT2440. The protein functions as a soluble cytoplasmic enzyme in **glycine-betaine / choline / creatine catabolism**, feeding one-carbon units into folate metabolism.

---

## Key Findings

### Finding 1 — *soxA* (PP_0325) is the α-subunit of heterotetrameric sarcosine oxidase, encoded in a conserved *glyA-soxBDAG-purU* operon

The genomic neighborhood of PP_0325 in *P. putida* KT2440 exactly recapitulates the canonical, well-characterized bacterial sarcosine-oxidase operon. Reading through the KEGG genome context: **PP_0322 = glyA** (serine hydroxymethyltransferase) → **PP_0323 = soxB (β)** → **PP_0324 = soxD (δ)** → **PP_0325 = soxA (α)** → **PP_0326 = soxG (γ)** → **PP_0327 = purU** (formyltetrahydrofolate deformylase) → **PP_0328** (formaldehyde dehydrogenase). PP_0325 spans 389,727–392,741 (3,015 bp ≈ 1,004 aa), matching the UniProt Q88R09 length of 1,004 residues exactly. This arrangement reproduces the classic **glyA-soxBDAG** gene order first described in *Corynebacterium* and *Arthrobacter*.

The original sequence analysis of the sarcosine oxidase operon established this canonical order: *"The sarcosine oxidase operon contains at least five closely packed genes encoding sarcosine oxidase subunits and serine hydroxymethyltransferase (glyA), arranged in the order glyAsoxBDAG"* ([PMID: 7543100](https://pubmed.ncbi.nlm.nih.gov/7543100/)). A later study of glycine-betaine catabolic gene clusters confirmed the subunit assignment: *"the structural genes of heterotetrameric sarcosine oxidase (soxBDAG) and dimethylglycine dehydrogenase (dmg)"* ([PMID: 11422368](https://pubmed.ncbi.nlm.nih.gov/11422368/)). Because the KT2440 locus order PP_0322–PP_0326 is identical to glyA-soxBDAG, PP_0325 is unambiguously **soxA (α)** — consistent with the UniProt gene name and its placement in the GcvT family.

### Finding 2 — The assembled enzyme oxidatively demethylates sarcosine to glycine + H₂O₂ and couples the one-carbon unit to 5,10-methylene-THF (EC 1.5.3.1)

The overall chemistry of the enzyme complex of which *soxA* is a subunit has been established biochemically and structurally in orthologs from *Pseudomonas maltophilia* and *Corynebacterium*. TSOX contains **three coenzymes (FAD, FMN, NAD⁺)** plus a tetrahydrofolate site and *"catalyzes the oxidation of sarcosine (N-methylglycine) to yield hydrogen peroxide, glycine and formaldehyde. In the presence of tetrahydrofolate, the oxidation of sarcosine is coupled to the formation of 5,10-methylenetetrahydrofolate"* ([PMID: 16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/)).

This bifunctionality — an amine-oxidation step joined to a folate one-carbon-transfer step — was described as coupling *"the oxidation of the methyl group in sarcosine (N-methylglycine) and transfer of the oxidized methyl group into the one-carbon metabolic pool"* ([PMID: 15922624](https://pubmed.ncbi.nlm.nih.gov/15922624/)). The reactive iminium/formaldehyde intermediate produced by C–H bond cleavage at the FAD site is thus not simply released as free formaldehyde in the presence of folate; instead it is captured onto THF. This is the molecular basis of EC 1.5.3.1 and directly ties the enzyme to one-carbon (folate) metabolism.

### Finding 3 — The α-subunit specifically houses NAD⁺ and the tetrahydrofolate-binding site: it is the 5,10-methylene-THF synthase half of the enzyme

Multiple crystal structures resolve the enzyme's cofactors by subunit, and they consistently place the NAD⁺ and folate sites in the **α-subunit**. In the 1.85 Å *P. maltophilia* structure, *"The NAD⁺ and putative folate binding sites are located in the alpha-subunit. The FAD binding site is in the beta-subunit. FMN is bound at the interface of the alpha and beta-subunits"* ([PMID: 16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/)). The independent *Corynebacterium* sp. U-96 structure agrees: *"The alpha subunit is composed of two domains, contains NAD(+), and binds folinic acid"* ([PMID: 15946648](https://pubmed.ncbi.nlm.nih.gov/15946648/)).

Functionally, the folate site in the α-subunit is where the second half-reaction occurs. Analysis of the channeling architecture in *Corynebacterium* U-96 states that *"The third channel goes through the α-subunit and has a folinic acid-binding site, where the iminium intermediate is converted to Gly and either formaldehyde or, 5,10-methylenetetrahydrofolate"* ([PMID: 20675294](https://pubmed.ncbi.nlm.nih.gov/20675294/)). Biochemical subunit dissection provides orthogonal confirmation: *"The alpha subunit and the alphagamma complex were each found to contain 1 mol of NAD(+) but no FAD. Since NAD(+) binds to alpha, FAD probably binds to beta"* ([PMID: 11330998](https://pubmed.ncbi.nlm.nih.gov/11330998/)). Thus, the α-subunit encoded by *soxA* is the **NAD⁺- and folate-binding, glycine-forming / methylene-THF-synthesizing module** of the enzyme — not the sarcosine dehydrogenase site.

### Finding 4 — Domain architecture and evolutionary origin: an N-terminal Rossmann NAD⁺-binding domain fused to a C-terminal GcvT/T-protein folate-binding domain

The α-subunit is a two-domain protein whose modular architecture reflects its two roles (dinucleotide binding and folate one-carbon transfer). Sequence analysis showed that the α-subunit *"contains a second ADP-binding motif within an approximately 280 residue region near the NH₂ terminus that exhibits homology with subunit A from octopine and nopaline oxidases"* ([PMID: 7543100](https://pubmed.ncbi.nlm.nih.gov/7543100/)). Structurally, this N-terminal module resembles a flavoprotein FAD-binding fold repurposed for NAD⁺: *"The N-terminal half of the alpha subunit of TSOX (alphaA) is closely similar to the FAD-binding domain of glutathione reductase but with NAD⁺ replacing FAD"* ([PMID: 16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/)).

The ~380-residue C-terminal region is homologous to the **glycine-cleavage T-protein (GcvT / aminomethyltransferase)** and to the C-terminal half of dimethylglycine dehydrogenase — the folate-binding fold that carries out one-carbon transfer. This is fully consistent with the UniProt/InterPro annotation of Q88R09, which assigns it to the **GcvT family** and lists the FAD/NAD-binding domain (IPR023753, IPR036188) together with the GcvT/YgfZ/DmdA folate-binding domain (IPR028896, IPR029043) plus a 2Fe-2S-binding N-terminal signature (IPR042204). The bioinformatic domain composition therefore independently predicts exactly the two functions (NAD⁺ binding + folate one-carbon chemistry) that structural biology localizes to this subunit.

### Finding 5 — Pathway context and localization: a soluble cytoplasmic enzyme feeding one-carbon units into folate metabolism during glycine-betaine/choline catabolism

The *soxBDAG* operon is embedded within a **folate one-carbon gene cluster**. Immediately upstream lies **glyA** (serine hydroxymethyltransferase; serine + THF ⇌ glycine + 5,10-methylene-THF), and immediately downstream lie **purU** (10-formyl-THF deformylase) and a **formaldehyde dehydrogenase** (KT2440 PP_0322–PP_0328). This gene neighborhood positions sarcosine oxidase as a supplier of one-carbon units to the folate pool. The proposed physiological pathway is **glycine betaine → dimethylglycine → sarcosine → glycine**, with the liberated methyl-derived one-carbon groups assimilated via tetrahydrofolate: *"pathways are proposed for glycine betaine catabolism in Arthrobacter species, which involve the identified folate-dependent enzymes"* ([PMID: 11422368](https://pubmed.ncbi.nlm.nih.gov/11422368/)). The original operon analysis emphasized that the cluster *"reveals homologies with key enzymes of folate one-carbon metabolism"* ([PMID: 7543100](https://pubmed.ncbi.nlm.nih.gov/7543100/)).

Regarding localization, sarcosine oxidase is a classic **soluble cytoplasmic flavoenzyme**, and UniProt Q88R09 carries no annotated signal peptide or transmembrane segments, consistent with a cytoplasmic location where THF and NAD⁺ are available.

### Finding 6 — Substrate specificity and two-site organization: *soxA*/α is the folate half-site; sarcosine (N-methylglycine) is the primary substrate

The assembled enzyme has two catalytic sites ~35 Å apart: *"The sarcosine dehydrogenase and 5,10-methylenetetrahydrofolate synthase sites are 35 A apart but connected by a large internal cavity (approximately 10,000 A³)"* ([PMID: 16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/)). Sarcosine oxidation occurs at the β-subunit FAD; the α-subunit (*soxA*) holds NAD⁺ and the folate site (the methylene-THF synthase half-reaction). It is therefore essential to state clearly that *soxA* is **not** the sarcosine-oxidation site — but the substrate consumed by the overall enzyme is the secondary amino acid **sarcosine**.

Substrate-specificity data from the related monomeric sarcosine oxidase (MSOX) define the family's selectivity: MSOX oxidizes sarcosine best, with only minor activity on other secondary amino acids, and importantly *"MSOX can oxidize other secondary amino acids (N-methyl-L-alanine, N-ethylglycine, and L-proline), but N,N-dimethylglycine, a tertiary amine, is not a substrate"* ([PMID: 10913293](https://pubmed.ncbi.nlm.nih.gov/10913293/)). This confirms that **sarcosine, not dimethylglycine, is the substrate of sarcosine oxidase** (dimethylglycine is instead handled by the separate dimethylglycine dehydrogenase, *dmg*, in the same catabolic pathway).

### Finding 7 — KT2440 *soxA* (Q88R09) is a full-length ortholog (~47–48% identity) of structurally/biochemically characterized TSOX α-subunits, justifying functional transfer

Global (Needleman–Wunsch) alignment of Q88R09 (1,004 aa) against reviewed Swiss-Prot sarcosine-oxidase α-subunits gives high, full-length identity:

| Ortholog (α-subunit) | Organism | UniProt | % Identity to Q88R09 | Notes |
|---|---|---|---|---|
| Q46337 | *Corynebacterium* sp. P-1 | Q46337 | **48.3%** (518/1072) | Source of biochemical NAD⁺/α assignment |
| Q9AGP1 | *Arthrobacter* sp. | Q9AGP1 | 47.9% (512/1068) | Glycine-betaine catabolism operon |
| Q50LF0 | *Corynebacterium* sp. U-96 | Q50LF0 | 47.5% (507/1067) | Crystal structure solved |
| O87386 | *Sinorhizobium meliloti* | O87386 | 47.1% | Additional ortholog |

The alignments span the full ~1,000-residue length, covering both the N-terminal NAD⁺-binding domain and the C-terminal GcvT/folate domain. Because the U-96 (Q50LF0) and P-1 (Q46337) enzymes are exactly those for which crystal structures and subunit-resolved cofactor assignments were determined — *"The alpha subunit is composed of two domains, contains NAD(+), and binds folinic acid"* ([PMID: 15946648](https://pubmed.ncbi.nlm.nih.gov/15946648/)) and *"The alpha subunit and the alphagamma complex were each found to contain 1 mol of NAD(+) but no FAD"* ([PMID: 11330998](https://pubmed.ncbi.nlm.nih.gov/11330998/)) — the ~47–48% full-length identity provides a quantitative, defensible basis for transferring these functional assignments to the KT2440 protein.

---

## Mechanistic Model / Interpretation

Heterotetrameric sarcosine oxidase is best understood as a **two-active-site molecular machine with substrate channeling**. The four subunits (α = *soxA*/PP_0325, β = *soxB*/PP_0323, γ = *soxG*/PP_0326, δ = *soxD*/PP_0324) assemble to co-locate three flavin/dinucleotide cofactors and a folate site.

```
                 SARCOSINE (N-methylglycine)
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │  β-subunit (soxB)                     │
        │  noncovalent FAD  ── oxidation site   │  ← C–H bond cleavage,
        │  (2-furoate = competitive inhibitor)  │    O2 → H2O2
        └───────────────┬───────────────────────┘
                        │  reactive iminium /
                        │  formaldehyde equivalent
                        │  (5-oxazolidinone intermediate)
              ~35 Å internal cavity (~10,000 Å³)
              — substrate channeling, prevents
                escape of toxic formaldehyde —
                        │
                        ▼
        ┌─────────────────────────────────────┐
        │  α-subunit (soxA / PP_0325)          │
        │  N-term: Rossmann NAD+-binding domain │
        │  C-term: GcvT/T-protein folate domain │  ← 5,10-methylene-THF
        │  binds NAD+ + tetrahydrofolate        │    synthase half-reaction
        └───────────────┬───────────────────────┘
                        │
         ┌──────────────┴───────────────┐
         ▼                              ▼
   + THF: 5,10-methylene-THF      – THF: free formaldehyde
   + GLYCINE                      + GLYCINE
```

The covalent FMN sits at the α/β interface and mediates electron transfer, functioning as an electron transferase between the two flavins; the δ (soxD) and γ (soxG) subunits complete the assembly and, in the case of the γ chain, associate with the α-subunit (the αγ complex retains NAD⁺).

**Physiologically**, the enzyme operates in the middle of a linear methylamine-catabolic funnel in *P. putida*:

```
glycine betaine ──────→ dimethylglycine ──(Dmg dehydrogenase)──→ sarcosine
                                                                     │
                                              SARCOSINE OXIDASE (soxBDAG)
                                                                     ▼
                                        GLYCINE  +  1-C unit on THF (5,10-CH2-THF)
                                                                     │
                     glyA (SHMT), purU (10-CHO-THF deformylase), FDH ┘
                                (folate one-carbon pool)
```

The **evolutionary logic** is elegant: the α-subunit is a fusion of two ancient one-carbon-metabolism modules — a dinucleotide-binding oxidoreductase fold (glutathione-reductase-like, here binding NAD⁺ instead of FAD) and a GcvT/aminomethyltransferase folate-binding fold (the same fold used by the glycine-cleavage T-protein and dimethylglycine dehydrogenase). This fusion allowed sarcosine oxidase to internalize the folate-transfer step that, in the glycine cleavage system, is performed by a standalone T-protein. The net effect is that the reactive one-carbon intermediate never leaves the enzyme, protecting the cell from free formaldehyde while efficiently loading the folate pool.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports this annotation |
|---|---|---|
| [7543100](https://pubmed.ncbi.nlm.nih.gov/7543100/) | *Sequence analysis of sarcosine oxidase and nearby genes…folate one-carbon metabolism* | Defines canonical **glyA-soxBDAG** operon order (→ identifies PP_0325 as soxA/α); describes N-terminal ADP-binding motif of α; links operon to folate one-carbon metabolism |
| [16820168](https://pubmed.ncbi.nlm.nih.gov/16820168/) | *Heterotetrameric sarcosine oxidase: structure of a diflavin metalloenzyme at 1.85 Å* | Assigns **NAD⁺ + folate to α**, FAD to β, FMN to α/β interface; overall reaction; two sites 35 Å apart, ~10,000 Å³ cavity; α N-terminal = glutathione-reductase-like NAD⁺ fold |
| [15946648](https://pubmed.ncbi.nlm.nih.gov/15946648/) | *Crystal structure of heterotetrameric sarcosine oxidase from Corynebacterium U-96* | Independent structure: **α is two-domain, binds NAD⁺ and folinic acid** (ortholog Q50LF0) |
| [11330998](https://pubmed.ncbi.nlm.nih.gov/11330998/) | *Organization of coenzymes/subunits and role of covalent flavin link* | Biochemical proof: α and αγ contain **1 mol NAD⁺, no FAD** → NAD⁺ binds α (ortholog Q46337) |
| [20675294](https://pubmed.ncbi.nlm.nih.gov/20675294/) | *Channeling and conformational changes in TSOX from Corynebacterium U-96* | Localizes glycine-forming / methylene-THF-synthase step to the **α-subunit folinic-acid site**; iminium intermediate channeled |
| [15922624](https://pubmed.ncbi.nlm.nih.gov/15922624/) | *Cloning, expression, crystallization of TSOX from P. maltophilia* | States bifunctional coupling of sarcosine methyl oxidation to the **one-carbon (folate) pool** |
| [11422368](https://pubmed.ncbi.nlm.nih.gov/11422368/) | *Genes for dimethylglycine/sarcosine degradation in Arthrobacter; glycine betaine catabolism* | Confirms **soxBDAG = four TSOX subunits**; places enzyme in glycine-betaine catabolism / folate assimilation |
| [10913293](https://pubmed.ncbi.nlm.nih.gov/10913293/) | *Monomeric sarcosine oxidase kinetics with alternate substrates* | Family substrate specificity: **sarcosine primary substrate**, minor secondary amino acids, **N,N-dimethylglycine NOT a substrate** |

Supporting/contextual literature reviewed includes mechanistic and structural studies of related enzymes: the flavin-thiolate (4a-sulfide) adduct of the TSOX FMN ([PMID: 16934831](https://pubmed.ncbi.nlm.nih.gov/16934831/)); stopped-flow kinetics and quantum-tunneling C–H cleavage in *Arthrobacter* TSOX ([PMID: 10684595](https://pubmed.ncbi.nlm.nih.gov/10684595/)); interflavin electron transfer in sarcosine oxidase ([PMID: 1657156](https://pubmed.ncbi.nlm.nih.gov/1657156/)); umbrella-sampling analysis of intermediate (5-oxazolidinone) transport through the internal tunnels ([PMID: 33576049](https://pubmed.ncbi.nlm.nih.gov/33576049/)); the structurally related FAD/FMN/ATP L-proline dehydrogenase complex whose β-subunit resembles monomeric sarcosine oxidase ([PMID: 16027125](https://pubmed.ncbi.nlm.nih.gov/16027125/)); and MSOX substrate/mechanism studies ([PMID: 16300392](https://pubmed.ncbi.nlm.nih.gov/16300392/), [PMID: 22432926](https://pubmed.ncbi.nlm.nih.gov/22432926/)). Engineering/specificity studies of sarcosine-oxidase family enzymes ([PMID: 35124004](https://pubmed.ncbi.nlm.nih.gov/35124004/), [PMID: 40932061](https://pubmed.ncbi.nlm.nih.gov/40932061/), [PMID: 37968575](https://pubmed.ncbi.nlm.nih.gov/37968575/), [PMID: 24925096](https://pubmed.ncbi.nlm.nih.gov/24925096/)) reinforce the secondary-amino-acid/N-demethylase chemistry of the family.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the KT2440 protein.** All functional assignments for Q88R09 are transferred by orthology (~47–48% full-length identity) from TSOX enzymes of *P. maltophilia*, *Corynebacterium* sp. U-96 and P-1, and *Arthrobacter*. No published enzymology, crystal structure, knockout phenotype, or localization experiment specific to *P. putida* KT2440 PP_0325 was identified. The identity level, while high and full-length, is below the ~60–70% typically considered "safe" for automatic transfer of fine catalytic detail, so residue-level active-site claims should be treated as strong predictions rather than proven facts.

2. **Folate site is "putative" in the primary structure.** In the 1.85 Å *P. maltophilia* structure the folate site is described as the *"putative folate binding site"*; it is inferred from folinic-acid soaks in the *Corynebacterium* structures and from GcvT homology, not from a co-crystal with a physiological methylene-THF product.

3. **Physiological pathway is proposed, not proven in KT2440.** The glycine-betaine → dimethylglycine → sarcosine → glycine route and the operon-based one-carbon assimilation model derive from *Arthrobacter* and sequence/operon analysis. Whether *P. putida* KT2440 actually induces this operon under glycine-betaine/choline/creatine growth, and the exact upstream demethylase(s), have not been experimentally verified here.

4. **Subunit stoichiometry and assembly in KT2440 unconfirmed.** The αβγδ composition, covalent FMN attachment chemistry, and channeling behavior are established for the model orthologs but not directly demonstrated for the KT2440 complex.

5. **The 2Fe-2S signature (IPR042204)** appears in the InterPro annotation, but classical TSOX α-subunits are not described as iron-sulfur proteins in the biochemical literature reviewed; this domain match may reflect a distant fold relationship rather than a functional [2Fe-2S] cluster and warrants caution.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and cofactor analysis.** Clone the KT2440 *soxBDAG* operon (PP_0323–PP_0326) into *E. coli*, purify the complex, and confirm the predicted cofactor set (FAD, FMN, NAD⁺) and the α-subunit's NAD⁺/folate binding by spectroscopy and denaturation-release assays — directly replicating the [PMID: 11330998](https://pubmed.ncbi.nlm.nih.gov/11330998/) subunit dissection for the *P. putida* enzyme.

2. **Steady-state and stopped-flow kinetics.** Measure sarcosine oxidation (kcat, Km, H₂O₂ production) and THF-dependent 5,10-methylene-THF formation to quantitatively confirm EC 1.5.3.1 activity and folate coupling; test whether dimethylglycine is excluded as a substrate, as predicted from family specificity ([PMID: 10913293](https://pubmed.ncbi.nlm.nih.gov/10913293/)).

3. **Gene deletion / growth phenotyping.** Construct a KT2440 ΔPP_0325 (and Δoperon) mutant and test growth on sarcosine, creatine, choline, and glycine betaine as sole carbon/nitrogen sources to establish the in vivo catabolic role and confirm operon function.

4. **Transcriptional induction analysis.** Use RT-qPCR or RNA-seq to determine whether the *glyA-soxBDAG-purU* cluster is co-induced during growth on glycine-betaine/choline/sarcosine, confirming it functions as a one-carbon catabolic operon in KT2440.

5. **Structure determination or AlphaFold-Multimer modeling.** Solve or model the KT2440 αβγδ complex to verify the two-site/channeling architecture and to map the α-subunit NAD⁺ and folate sites at residue resolution, validating the ~35 Å / ~10,000 Å³ cavity architecture predicted from orthologs.

6. **Resolve the 2Fe-2S annotation.** Test experimentally (UV-vis, EPR, iron content) whether the KT2440 complex contains any iron-sulfur center, to confirm or reject the IPR042204 domain match as functionally meaningful.

---

## Conclusion

The gene *soxA* (PP_0325, Q88R09) of *P. putida* KT2440 encodes the **α-subunit of heterotetrameric sarcosine oxidase**, the enzyme's NAD⁺- and tetrahydrofolate-binding catalytic module. It performs the **5,10-methylene-THF synthase half-reaction** — converting the channeled iminium/formaldehyde intermediate (generated at the β-subunit FAD sarcosine-oxidation site) into glycine plus a folate-bound one-carbon unit — via its C-terminal GcvT/T-protein-like domain, with an N-terminal Rossmann domain holding NAD⁺. It is a **soluble cytoplasmic** enzyme functioning in **glycine-betaine/choline/creatine catabolism**, feeding one-carbon units into folate metabolism through the conserved *glyA-soxBDAG-purU* operon. All assignments rest on strong operon-context, structural, and biochemical evidence from ~47–48%-identical, full-length orthologs, but await direct experimental confirmation in *P. putida* KT2440 itself.


## Artifacts

- [OpenScientist final report](soxA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](soxA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7543100
2. PMID:11422368
3. PMID:16820168
4. PMID:15922624
5. PMID:15946648
6. PMID:20675294
7. PMID:11330998
8. PMID:10913293
9. PMID:16934831
10. PMID:10684595
11. PMID:1657156
12. PMID:33576049
13. PMID:16027125
14. PMID:16300392
15. PMID:22432926
16. PMID:35124004
17. PMID:40932061
18. PMID:37968575
19. PMID:24925096