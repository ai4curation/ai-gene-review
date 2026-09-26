---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T08:50:15.715379'
end_time: '2026-08-12T09:03:57.628853'
duration_seconds: 821.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: HST1
  gene_symbol: HST1
  uniprot_accession: P53685
  protein_description: 'RecName: Full=NAD-dependent protein deacetylase HST1; EC=2.3.1.286
    {ECO:0000255|PROSITE-ProRule:PRU00236}; AltName: Full=Homologous to SIR2 protein
    1; AltName: Full=Regulatory protein SIR2 homolog 1;'
  gene_info: Name=HST1; OrderedLocusNames=YOL068C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the sirtuin family. Class I subfamily.
  protein_domains: DHS-like_NAD/FAD-binding_dom. (IPR029035); NAD-dep_histone_deAcase_SIR2_N.
    (IPR007654); NAD-dep_sirtuin_deacylases. (IPR050134); Sirtuin. (IPR003000); Sirtuin_cat_small_dom_sf.
    (IPR026591)
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
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: HST1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: HST1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P53685
- **Protein Description:** RecName: Full=NAD-dependent protein deacetylase HST1; EC=2.3.1.286 {ECO:0000255|PROSITE-ProRule:PRU00236}; AltName: Full=Homologous to SIR2 protein 1; AltName: Full=Regulatory protein SIR2 homolog 1;
- **Gene Information:** Name=HST1; OrderedLocusNames=YOL068C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the sirtuin family. Class I subfamily.
- **Key Domains:** DHS-like_NAD/FAD-binding_dom. (IPR029035); NAD-dep_histone_deAcase_SIR2_N. (IPR007654); NAD-dep_sirtuin_deacylases. (IPR050134); Sirtuin. (IPR003000); Sirtuin_cat_small_dom_sf. (IPR026591)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HST1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HST1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HST1** (gene ID: HST1, UniProt: P53685) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# HST1 (YOL068C, UniProt P53685): A Nuclear NAD⁺-Dependent Sirtuin Deacetylase and Gene-Specific Repressor in *Saccharomyces cerevisiae*

## Summary

**HST1** (*Homologous to Sir Two 1*; systematic name **YOL068C**; UniProt **P53685**) encodes a **nuclear, chromatin-associated NAD⁺-dependent protein/histone lysine deacetylase** of the Sir2 (sirtuin) family, classified as EC 2.3.1.286 and belonging to the sirtuin Class I subfamily. The enzyme removes acetyl groups from acetyl-lysine residues on nucleosomal histone tails (histone H4, including H4K5 and H4K16; histone H3 at K9/K14) using an obligate, stoichiometric consumption of NAD⁺. For each lysine deacetylated, one molecule of NAD⁺ is cleaved, generating three products: the deacetylated lysine, nicotinamide, and the novel metabolite **2′-O-acetyl-ADP-ribose (OAADPr)**. This catalytic chemistry — coupling deacetylation to NAD⁺ hydrolysis — is the defining and mechanistically conserved feature of the entire sirtuin family, and it distinguishes sirtuins (Class III HDACs) from the zinc-dependent Class I/II histone deacetylases.

The **primary physiological function** of Hst1 is **gene-specific transcriptional repression**, not the regional heterochromatic silencing performed by its close paralog Sir2. Hst1 is the catalytic engine of the **Sum1–Rfm1–Hst1 complex**, in which the DNA-binding protein Sum1 recognizes **Middle Sporulation Elements (MSEs)** in target promoters, the tethering factor Rfm1 bridges Sum1 to Hst1, and Hst1 then deacetylates promoter nucleosomes to condense local chromatin and silence transcription. Through this complex, Hst1 represses **middle-sporulation/meiotic genes** (including the master meiotic activator *NDT80*, as well as *IME2* and *SMA2/mORC1*) during vegetative (mitotic) growth. This repression is gene-specific — it does not spread to neighboring genes — and it is relieved during meiosis when the activator Ndt80 outcompetes Sum1 for MSE occupancy. A second distinct regulatory role identifies Hst1 as an **NAD⁺ sensor**: because it has relatively low affinity for NAD⁺, its deacetylase activity (and hence its repression of the *de novo* NAD⁺ biosynthesis "BNA" genes) declines when cellular NAD⁺ falls, forming a feedback loop that homeostatically regulates NAD⁺ biosynthesis.

Hst1 operates in the **nucleus**, on **chromatin**, at specific gene promoters. Although Hst1 is 71% identical to Sir2 and shares a near-identical catalytic core (a large Rossmann-fold NAD⁺-binding domain plus a small zinc-binding subdomain), the two enzymes are functionally divergent: Hst1's endogenous role is gene-specific promoter repression via Sum1/Rfm1, whereas Sir2's is regional silencing via Sir3/Sir4. This divergence arises from **distinct cofactor/targeting specificities rather than differences in catalytic chemistry** — a conclusion supported by domain-swap experiments. Only when artificially targeted (e.g., in the *SUM1-1* gain-of-function background via the origin recognition complex) can Hst1 substitute for Sir2 in HMR silencing. The gene symbol is **not** ambiguous in this context: all literature reviewed corresponds precisely to the *S. cerevisiae* sirtuin HST1.

---

## Key Findings

### Finding 1: Hst1 is an NAD⁺-dependent Class III histone/protein deacetylase (sirtuin) with a defined catalytic mechanism

Hst1 (YOL068C) is one of four Sir2 homologs (Hst1–Hst4) in budding yeast and is a phylogenetically conserved NAD⁺-dependent protein deacetylase. The sirtuins are described as *"a phylogenetically conserved family of NAD(+)-dependent protein deacetylases that consume one molecule of NAD(+) for every deacetylated lysine side chain"* ([PMID: 24164855](https://pubmed.ncbi.nlm.nih.gov/24164855/)). This one-to-one stoichiometry of NAD⁺ consumption to lysine deacetylation is the biochemical signature of the family and the reason Hst1's activity is inherently coupled to the cell's metabolic state.

The reaction catalyzed produces three products. Sir2-family enzymes are *"NAD(+)-dependent histone/protein deacetylases that tightly couple the hydrolysis of NAD(+) and the deacetylation of an acetylated substrate to form nicotinamide, the deacetylated product, and the novel metabolite O-acetyl-ADP-ribose (OAADPR)"* ([PMID: 15274642](https://pubmed.ncbi.nlm.nih.gov/15274642/)). Mechanistic studies establish a sequential ternary-complex mechanism: nicotinamide is cleaved from NAD⁺ first, forming a covalent **α-1′-O-alkylamidate intermediate**, after which the acetyl group is transferred to ADP-ribose. Direct evidence for this pathway comes from work *"providing direct evidence for the formation of a covalent alpha-1'-O-alkylamidate"* ([PMID: 16388603](https://pubmed.ncbi.nlm.nih.gov/16388603/)), which also implicates a conserved catalytic histidine (His135 in the paralog Hst2) acting as a general base that activates the ribose 2′-OH. Because nicotinamide is both a reaction product and a feedback inhibitor, the mechanism itself provides a natural regulatory handle (see Finding 8).

This is the assigned enzymatic identity of Hst1: **EC 2.3.1.286**, a NAD-dependent protein deacetylase of the sirtuin Class I subfamily.

### Finding 2: Hst1's primary function is gene-specific repression of middle-sporulation genes as the catalytic subunit of the Sum1–Rfm1–Hst1 complex

The central physiological role of Hst1 is to serve as the **catalytic subunit of a promoter-targeted repressor complex**. Hst1 does not itself bind DNA; instead it is recruited to specific promoters by the sequence-specific DNA-binding protein **Sum1**, with the bridging/tethering factor **Rfm1** connecting the two. The architecture was defined by the discovery that *"Rfm1 interacts with both Sum1 and Hst1 and is required for the Sum1-Hst1 interaction"* ([PMID: 12612074](https://pubmed.ncbi.nlm.nih.gov/12612074/)). Rfm1 is required both for the physical Sum1–Hst1 interaction and for repression of the Hst1-dependent subset of middle-sporulation genes.

The functional output is described as the cooperation of *"the NAD(+)-dependent histone deacetylase Hst1 and the DNA-binding protein Sum1 for vegetative repression of many middle sporulation genes"* ([PMID: 12612074](https://pubmed.ncbi.nlm.nih.gov/12612074/)). Mechanistically, once recruited, Hst1 deacetylates promoter nucleosomes, condensing local chromatin and blocking transcription of genes needed for meiotic progression and spore formation during vegetative growth. A later study confirmed that *"Hst1 interacts with Rfm1 and Sum1 to repress the transcription of specific middle-sporulation genes"* ([PMID: 17242192](https://pubmed.ncbi.nlm.nih.gov/17242192/)).

Critically, the difference between Hst1 (gene-specific repression) and Sir2 (regional silencing) is **not** a difference in enzymatic chemistry. Domain-swap and chimera experiments showed that *"the differences in the silencing and repression functions of Sir2 and Hst1 may not be due to differences in enzymatic activities of the proteins but rather may be the result of distinct cofactor specificities"* ([PMID: 17242192](https://pubmed.ncbi.nlm.nih.gov/17242192/)). Gene-specific repression requires the Rfm1 + Sum1 cofactors, whereas Sir2's regional silencing requires Sir3 + Sir4; specificity is set by non-conserved N-terminal sequences and a small number of core residues, not by catalysis.

### Finding 3: Hst1 is an NAD⁺ sensor that represses de novo NAD⁺ biosynthesis genes

Beyond its role in meiotic-gene repression, Hst1 functions as a **metabolic sensor that closes a feedback loop on NAD⁺ biosynthesis**. Transcript-array analyses demonstrated that *"the NAD(+)-dependent deacetylase activity of Hst1p represses de novo NAD(+) biosynthesis genes in the absence of new protein synthesis, suggesting a direct effect"* ([PMID: 12972620](https://pubmed.ncbi.nlm.nih.gov/12972620/)). The salvage-pathway genes are unaffected, and Sum1 occupies the promoters of the inducible *de novo* (BNA) biosynthesis genes, tying this repression to the same Sum1-targeting logic as the meiotic genes.

This established *"a critical role of the NAD(+)-dependent deacetylase Hst1p as a sensor of NAD(+) levels and regulator of NAD(+) biosynthesis"* ([PMID: 12972620](https://pubmed.ncbi.nlm.nih.gov/12972620/)). The logic is elegant: because Hst1 has relatively low affinity for NAD⁺ compared with other sirtuins, its activity is sensitive to falling NAD⁺ concentrations. When NAD⁺ is plentiful, Hst1 is active and represses the biosynthesis genes; when NAD⁺ drops, Hst1 activity declines, de-repressing the *de novo* pathway to restore NAD⁺. Consistent with this, *"the removal of HST1-mediated repression of the NAD(+) de novo biosynthesis pathway leads to increased cellular NAD(+) levels"* ([PMID: 12972620](https://pubmed.ncbi.nlm.nih.gov/12972620/)). A subsequent study further linked Hst1 (together with the copper-sensing transcription factor Mac1 and nicotinic acid) to the regulation of NAD biosynthesis genes ([PMID: 30760525](https://pubmed.ncbi.nlm.nih.gov/30760525/)).

### Finding 4: Hst1 can substitute for Sir2 in HMR silencing when artificially targeted, and contributes to genome stability

Although Hst1 does not natively perform regional silencing, its catalytic capacity to silence chromatin can be revealed by artificial targeting. In the *SUM1-1* gain-of-function background, Sir-independent silencing at the *HMR* locus requires Hst1: *"Sum1-1 requires the Sir2 homolog, Hst1, for silencing and most probably requires the NAD(+)-dependent deacetylase activity of this protein"* ([PMID: 11313477](https://pubmed.ncbi.nlm.nih.gov/11313477/)). In this context, the mutant Sum1-1 protein binds the **origin recognition complex (ORC)** at HMR and recruits Hst1, which then *"deacetylates histones or other chromatin-associated proteins to cause chromatin condensation and transcriptional silencing"* ([PMID: 11313477](https://pubmed.ncbi.nlm.nih.gov/11313477/)).

Evolutionary analyses reinforce that Hst1 is a functionally central and retained sirtuin. In the CTG-clade *Candida* yeasts, *"HST1 has been consistently retained throughout the clade, whereas SIR2 is only present in a subset of species"* ([PMID: 27543294](https://pubmed.ncbi.nlm.nih.gov/27543294/)), and the retained HST1 paralog can regain ancestral silencing functions — underscoring that the near-identical catalytic core is readily repurposed by changing its targeting partners. Genome-wide nicotinamide sensitivity screens further found that genome-stability pathways, including sister-chromatid cohesion, are especially vulnerable to loss of sirtuin activity ([PMID: 26646153](https://pubmed.ncbi.nlm.nih.gov/26646153/)).

### Finding 5: Repression is gene-specific via MSE promoter elements and is relieved by Ndt80 competition during meiosis

The gene-specificity of Hst1/Sum1 repression is encoded in **Middle Sporulation Elements (MSEs)** in target promoters. *"SUM1 and HST1, genes previously associated with transcriptional silencing, are required for MSE-mediated repression. Sum1 binds specifically in vitro to MSEs that function as strong repressor sites in vivo. Repression by Sum1 is gene specific and does not extend to neighboring genes"* ([PMID: 10562556](https://pubmed.ncbi.nlm.nih.gov/10562556/)). This non-spreading, promoter-local character sharply distinguishes Hst1-mediated repression from Sir2-mediated heterochromatin, which spreads across kilobases.

The switch from repression to activation during meiosis is governed by direct competition between the repressor Sum1 and the activator Ndt80 for the same DNA elements: *"Sum1 and Ndt80 compete for binding to MSEs and that small changes in the sequence of an MSE can yield large differences in which protein is bound"* ([PMID: 12832469](https://pubmed.ncbi.nlm.nih.gov/12832469/)). As cells enter middle meiosis, Ndt80 accumulates and displaces the Sum1–Rfm1–Hst1 repressor, de-repressing the middle-sporulation gene program. Target genes include the master meiotic regulators *NDT80*, *IME2*, and the *SMA2/mORC1* locus ([PMID: 27362276](https://pubmed.ncbi.nlm.nih.gov/27362276/)).

### Finding 6: HST1 is 71% identical to SIR2 but, on its own, does not perform Sir2's regional silencing or rDNA functions

HST1 was originally identified as a SIR2-related gene, defining the HST (Homologous to Sir Two) family. It is *"very closely related to SIR2, showing 71% sequence identity over 84% of its length"* ([PMID: 8810037](https://pubmed.ncbi.nlm.nih.gov/8810037/)). Despite this near-identity in the catalytic core, the endogenous roles diverge: *"Disruption of HST1 has shown no phenotype with respect to mechanisms in which SIR2 has a role, namely, regional silencing of HML alpha, or in rDNA recombination"* ([PMID: 8810037](https://pubmed.ncbi.nlm.nih.gov/8810037/)). This is a key negative result: it establishes that Hst1's native function is distinct from Sir2's heterochromatin/rDNA maintenance, and that Hst1's silencing capacity is latent, revealed only when the enzyme is redirected by alternative targeting cofactors.

### Finding 7: Structural architecture and localization — a nuclear, chromatin-associated sirtuin with a Rossmann-fold NAD⁺ domain and a small Zn-binding subdomain

The structural fold of Hst1 is inferred with high confidence from its close paralog Hst2, whose full-length crystal structure was solved. That structure revealed *"a central catalytic core domain fold that is characteristic of the other Sir2 homologs, and C- and N-terminal extensions that interact with the NAD(+) and acetyl-lysine substrate-binding sites"* ([PMID: 14502267](https://pubmed.ncbi.nlm.nih.gov/14502267/)). The catalytic core is bipartite: a large **Rossmann-fold domain** that binds NAD⁺ (corresponding to InterPro IPR029035, DHS-like NAD/FAD-binding) and a smaller **zinc-binding subdomain** (IPR026591). A related sirtuin structure confirms *"the characteristic small zinc-binding domain, and the larger Rossmann-fold domain involved in NAD+-binding interactions"* ([PMID: 29543820](https://pubmed.ncbi.nlm.nih.gov/29543820/)). The acetyl-lysine substrate binds in a cleft/hydrophobic tunnel between the two domains, and the sequence-divergent N- and C-terminal extensions provide autoregulatory modulation of substrate and cofactor binding — the structural basis for the cofactor/targeting specificity that distinguishes Hst1 from Sir2.

Functionally, Hst1 acts in the **nucleus, on chromatin**. Loss or mislocalization of the Sum1–Hst1 machinery causes *"loss of the DNA-binding transcriptional regulator Sum1 and the associated histone deacetylase Hst1 from chromatin in a locus-specific manner. This is linked to increased H4K5ac at these loci"* ([PMID: 29066473](https://pubmed.ncbi.nlm.nih.gov/29066473/)). This directly demonstrates that Hst1 operates at specific chromatin loci and that its removal raises local histone acetylation — pinning down both its subcellular location (nuclear chromatin) and its substrate (nucleosomal histone tails).

### Finding 8: Hst1 activity is tuned by NAD⁺ salvage (Pnc1/nicotinamide) and it is a shared subunit of two repressive complexes

Hst1 activity is regulated post-translationally by **nicotinamide (NAM)**, the reaction product that acts as a physiological sirtuin inhibitor. The nicotinamidase **Pnc1** clears NAM, relieving inhibition: *"PNC1 overexpression suppresses the inhibitory effect of exogenously added NAM on silencing, life span, and Hst1-mediated transcriptional repression"* ([PMID: 14729974](https://pubmed.ncbi.nlm.nih.gov/14729974/)). Because *PNC1* is stress-inducible, this links Hst1-dependent repression to environmental and metabolic stress signals.

Hst1 is also a shared subunit of a second repressive assembly, the **Set3 complex (Set3C)**. *"Set3 forms a single complex, Set3C, with Snt1, YIL112w, Sif2, Cpr1, and two putative histone deacetylases, Hos2 and NAD-dependent Hst1"* ([PMID: 11711434](https://pubmed.ncbi.nlm.nih.gov/11711434/)). Set3C thereby contains both NAD-dependent (Hst1) and NAD-independent (the Class I HDAC Hos2) deacetylase activities and represses early/middle sporulation genes such as *IME2* and *NDT80*. Importantly, the same study confirms that *"Hst1 is also present in a complex with Sum1, supporting previous characterizations of Hst1 and Sum1 as repressors of middle sporulation genes during vegetative growth"* ([PMID: 11711434](https://pubmed.ncbi.nlm.nih.gov/11711434/)). Because Hst1 is largely dispensable for Set3C's meiotic repression, the **Sum1–Rfm1–Hst1 complex is regarded as the primary Hst1-dependent repressor**.

### Finding 9: Substrate specificity — nucleosomal histone lysines at target promoters

Hst1's characterized physiological substrates are the acetyl-lysines of **N-terminal histone tails** at repressed promoters. The yeast Sir2 family deacetylates specific histone lysines: *"yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3 and specifically lysine 16 of H4"* ([PMID: 10693811](https://pubmed.ncbi.nlm.nih.gov/10693811/)). Structural work captured the Hst1 paralog Hst2 *"in complex with its acetyl-lysine 16 histone H4 substrate"* ([PMID: 17289592](https://pubmed.ncbi.nlm.nih.gov/17289592/)), defining H4K16ac as a canonical family substrate.

For Hst1 specifically, in vivo evidence comes from the observation that loss of Sum1/Hst1 targeting produces *"increased H4K5ac at these loci and aberrant middle gene expression"* ([PMID: 29066473](https://pubmed.ncbi.nlm.nih.gov/29066473/)), identifying nucleosomal histone H4 tail lysines (notably H4K5) as in vivo substrates at Hst1-repressed promoters. In vitro, sirtuins including this family can also accept longer acyl-lysine substrates (propionyl-, butyryl-lysine) ([PMID: 17951578](https://pubmed.ncbi.nlm.nih.gov/17951578/)), and can deacetylate non-histone proteins — but Hst1's physiologically documented substrates are promoter nucleosomal histones. Its relatively low NAD⁺ affinity ([PMID: 12972620](https://pubmed.ncbi.nlm.nih.gov/12972620/)) tunes its output to cellular NAD⁺ levels.

---

## Mechanistic Model / Interpretation

Hst1 is best understood as a **targeted, metabolically-gated chromatin repressor**. It integrates three inputs — DNA sequence (via Sum1/MSE), cellular NAD⁺ level, and nicotinamide/stress signals — to control the timing of the meiotic gene program and NAD⁺ biosynthesis.

### The core catalytic cycle

```
   Acetyl-Lys(histone) + NAD⁺
              │
              ▼   [Hst1 catalytic core: Rossmann fold + Zn subdomain]
   Step 1: nicotinamide cleavage → α-1′-O-alkylamidate intermediate
              │
   Step 2: acetyl transfer to ADP-ribose (His as general base)
              ▼
   Deacetylated-Lys(histone) + Nicotinamide + 2′-O-acetyl-ADP-ribose (OAADPr)
```

### The Sum1–Rfm1–Hst1 targeting and repression module

```
        MSE promoter element
   ────────■────────────────────────  (target gene, e.g. NDT80, IME2, SMA2, BNA genes)
           │
         [Sum1]  ── DNA-binding, sequence-specific
           │
         [Rfm1]  ── tethering/bridging factor
           │
         [Hst1]  ── NAD⁺-dependent deacetylase (catalytic subunit)
           │
           ▼
   Deacetylation of H4K5/H4K16 (H3K9/K14) on promoter nucleosomes
           │
           ▼
   Local chromatin condensation → GENE-SPECIFIC REPRESSION (non-spreading)
```

### Developmental switch during meiosis

```
   Vegetative growth:   Sum1–Rfm1–Hst1  bound at MSE  → genes OFF
                                     │
                          Meiosis: Ndt80 accumulates
                                     │  (competes for MSE)
                                     ▼
   Middle meiosis:      Ndt80 bound at MSE            → genes ON
```

### Comparison: Hst1 vs. its paralog Sir2

| Property | **Hst1** | **Sir2** |
|---|---|---|
| Catalytic activity | NAD⁺-dependent deacetylase (EC 2.3.1.286) | NAD⁺-dependent deacetylase |
| Sequence identity | — | 71% identical to Hst1 over 84% of length |
| Targeting cofactors | Sum1 + Rfm1 (also Set3C) | Sir3 + Sir4 |
| Mode of repression | **Gene-specific**, promoter-local, non-spreading | **Regional** heterochromatin, spreads |
| Native targets | Middle-sporulation genes; *de novo* NAD⁺ (BNA) genes | HM loci, telomeres, rDNA |
| NAD⁺ affinity | Relatively **low** (metabolic sensor) | Higher |
| Basis of divergence | **Cofactor/targeting specificity**, not catalysis | Cofactor/targeting specificity |

### Metabolic feedback (NAD⁺ sensing)

```
   High NAD⁺ ──► Hst1 active ──► BNA (de novo) genes repressed ──► NAD⁺ held in check
       ▲                                                                 │
       └──────────── Low NAD⁺ ──► Hst1 inactive ──► BNA de-repressed ────┘
                     (low NAD⁺ affinity makes Hst1 the sensor)

   Nicotinamide (NAM, a product) inhibits Hst1;  Pnc1 clears NAM (stress-induced) → relieves inhibition
```

Taken together, these modules explain why Hst1 is specialized as a **precise developmental and metabolic switch** rather than a bulk chromatin silencer: its DNA targeting is delegated to Sum1/Rfm1, its catalysis is throttled by NAD⁺ availability and nicotinamide, and its low NAD⁺ affinity makes it a dedicated sensor of the very cofactor it consumes.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [24164855](https://pubmed.ncbi.nlm.nih.gov/24164855/) | *Yeast sirtuins and the regulation of aging* | Defines sirtuin family enzymatic activity; names Hst1 as a Sir2 homolog (F1) |
| [15274642](https://pubmed.ncbi.nlm.nih.gov/15274642/) | *Substrate specificity and kinetic mechanism of the Sir2 family* | Reaction products: nicotinamide + deacetylated product + OAADPr (F1) |
| [16388603](https://pubmed.ncbi.nlm.nih.gov/16388603/) | *Sir2 protein deacetylases: chemical intermediates & conserved histidine* | Direct evidence for α-1′-O-alkylamidate intermediate; catalytic His (F1) |
| [12612074](https://pubmed.ncbi.nlm.nih.gov/12612074/) | *Rfm1, a novel tethering factor…* | Establishes Sum1–Rfm1–Hst1 architecture; vegetative repression of MSGs (F2) |
| [17242192](https://pubmed.ncbi.nlm.nih.gov/17242192/) | *Swapping gene-specific and regional silencing specificities of Hst1 and Sir2* | Divergence is cofactor specificity, not catalysis (F2) |
| [12972620](https://pubmed.ncbi.nlm.nih.gov/12972620/) | *Hst1p controls biosynthesis and cellular NAD⁺ levels* | Hst1 as NAD⁺ sensor repressing de novo BNA genes (F3) |
| [30760525](https://pubmed.ncbi.nlm.nih.gov/30760525/) | *Mac1, Hst1, and nicotinic acid regulate NAD biosynthesis* | Additional regulatory link for NAD biosynthesis (F3) |
| [11313477](https://pubmed.ncbi.nlm.nih.gov/11313477/) | *A novel form of silencing by Sum1-1 requires Hst1 and ORC* | Hst1 can silence HMR when targeted via Sum1-1/ORC (F4) |
| [27543294](https://pubmed.ncbi.nlm.nih.gov/27543294/) | *Gene loss & functional divergence of sirtuins in Candida* | HST1 evolutionarily retained; can regain silencing (F4) |
| [26646153](https://pubmed.ncbi.nlm.nih.gov/26646153/) | *Genome-wide NAM screen for sirtuin-dependent pathways* | Genome-stability pathways vulnerable to sirtuin loss (F4) |
| [10562556](https://pubmed.ncbi.nlm.nih.gov/10562556/) | *Sum1 and Hst1 repress middle sporulation genes during mitosis* | Gene-specific, non-spreading MSE-based repression (F5) |
| [12832469](https://pubmed.ncbi.nlm.nih.gov/12832469/) | *Sum1 and Ndt80 compete for MSE binding* | Meiotic de-repression via Ndt80 competition (F5) |
| [27362276](https://pubmed.ncbi.nlm.nih.gov/27362276/) | *Ndt80 activates mORC1 and SMA2 via bi-directional MSE* | Target genes SMA2/mORC1; Sum1 represses in mitosis (F5) |
| [8810037](https://pubmed.ncbi.nlm.nih.gov/8810037/) | *HST1, a new member of the SIR2 family* | 71% identity to SIR2; distinct native role (no HMLα/rDNA phenotype) (F6) |
| [14502267](https://pubmed.ncbi.nlm.nih.gov/14502267/) | *Structure and autoregulation of yeast Hst2* | Structural fold applicable to Hst1 by homology; N/C autoregulation (F7) |
| [29543820](https://pubmed.ncbi.nlm.nih.gov/29543820/) | *Crystal structure of Leishmania Sir2-related protein 1* | Confirms Zn subdomain + Rossmann NAD⁺ domain fold (F7) |
| [29066473](https://pubmed.ncbi.nlm.nih.gov/29066473/) | *Repression of middle sporulation genes* | Hst1 acts on chromatin locus-specifically; H4K5ac rises on loss (F7, F9) |
| [14729974](https://pubmed.ncbi.nlm.nih.gov/14729974/) | *Nicotinamide clearance by Pnc1 regulates silencing* | Pnc1/NAM regulation of Hst1-mediated repression (F8) |
| [11711434](https://pubmed.ncbi.nlm.nih.gov/11711434/) | *SET3 complex includes Hos2 and Hst1* | Hst1 membership in Set3C; also in Sum1 complex (F8) |
| [10693811](https://pubmed.ncbi.nlm.nih.gov/10693811/) | *Sir2 is an NAD-dependent histone deacetylase* | Histone lysine substrate specificity (H3K9/K14, H4K16) (F9) |
| [17289592](https://pubmed.ncbi.nlm.nih.gov/17289592/) | *Structural basis for nicotinamide inhibition and base exchange* | Hst2 bound to acetyl-H4K16 substrate (F9) |
| [17951578](https://pubmed.ncbi.nlm.nih.gov/17951578/) | *Acetyl-lysine analog peptides as probes* | In vitro propionyl-/butyryl-lysine substrates (F9) |

**How the evidence hangs together:** The catalytic identity (F1, F9) is derived from broadly conserved sirtuin biochemistry with structural support from the near-identical paralog Hst2 (F7). The physiological function (F2, F3, F5, F8) rests on Hst1-specific genetic and transcript-profiling studies in *S. cerevisiae*. The most direct in vivo, Hst1-specific substrate evidence is the locus-specific rise in H4K5ac upon loss of Sum1/Hst1 chromatin association (F7/F9, [PMID: 29066473](https://pubmed.ncbi.nlm.nih.gov/29066473/)). The negative result that Hst1 disruption causes no HMLα/rDNA phenotype (F6) is essential for correctly bounding the claim: Hst1's native role is gene-specific promoter repression, not regional silencing.

---

## Limitations and Knowledge Gaps

1. **Structural inference by homology.** No experimentally solved structure of Hst1 (P53685) itself is cited here; its fold, active site, and autoregulatory extensions are inferred from the paralog Hst2 and other sirtuins ([PMID: 14502267](https://pubmed.ncbi.nlm.nih.gov/14502267/), [PMID: 17289592](https://pubmed.ncbi.nlm.nih.gov/17289592/)). Given 71% identity to Sir2 and close relatedness to Hst2, this inference is strong, but Hst1-specific active-site kinetic constants (Km for NAD⁺, kcat) are only qualitatively described ("relatively low NAD⁺ affinity").

2. **Direct histone-substrate mapping for Hst1 is limited.** The most-cited residue-specific in vivo readout is H4K5ac at target loci ([PMID: 29066473](https://pubmed.ncbi.nlm.nih.gov/29066473/)); the H3K9/K14/H4K16 assignments come from the Sir2 family generally ([PMID: 10693811](https://pubmed.ncbi.nlm.nih.gov/10693811/)) or from Hst2 structures ([PMID: 17289592](https://pubmed.ncbi.nlm.nih.gov/17289592/)). A comprehensive, quantitative map of Hst1's preferred histone (and possible non-histone) acetyl-lysine substrates at native promoters is not fully established.

3. **Non-histone substrates.** While the family can deacetylate non-histone proteins and longer acyl-lysines in vitro ([PMID: 17951578](https://pubmed.ncbi.nlm.nih.gov/17951578/)), Hst1's physiological non-histone substrates (if any) are not defined.

4. **Quantitative division of labor between the two Hst1 complexes.** Hst1 is in both the Sum1–Rfm1–Hst1 complex and Set3C ([PMID: 11711434](https://pubmed.ncbi.nlm.nih.gov/11711434/)). The relative contribution of each complex to specific target genes, and the extent of functional overlap with the NAD-independent HDAC Hos2 within Set3C, remain incompletely quantified.

5. **Localization detail.** The nuclear/chromatin localization is well supported functionally (recruitment to promoters, locus-specific H4K5ac), but fine-grained genome-wide occupancy (ChIP-seq) data for Hst1 across all conditions is not exhaustively catalogued here.

---

## Proposed Follow-up Experiments / Actions

1. **Determine the Hst1 structure** (ideally the Sum1–Rfm1–Hst1 complex on a nucleosome bearing acetyl-H4 tails) by crystallography or cryo-EM to directly visualize substrate engagement and the N-terminal targeting determinants that distinguish Hst1 from Sir2.

2. **Quantitative enzymology of Hst1.** Measure Km(NAD⁺), kcat, and nicotinamide Ki for purified Hst1 against defined acetyl-histone peptides/nucleosomes to rigorously establish the "low NAD⁺ affinity" that underlies its sensor function, and compare head-to-head with Sir2, Hst2–4.

3. **Genome-wide, condition-resolved Hst1 substrate mapping.** Combine Hst1 ChIP-seq with quantitative histone-PTM proteomics (H4K5ac, H4K16ac, H3K9/K14ac) in wild-type vs. *hst1Δ* across vegetative growth, NAD⁺-limited conditions, and meiotic entry, to build a residue-resolved substrate map at each target promoter.

4. **Test the NAD⁺-sensor feedback loop directly.** Titrate cellular NAD⁺ (via BNA/salvage pathway perturbation and *PNC1* modulation) and measure Hst1 occupancy, BNA-gene derepression, and NAD⁺ levels to quantify the sensor's set-point and gain.

5. **Dissect the Ndt80–Sum1–Hst1 switch kinetics** with time-resolved ChIP through meiosis to determine whether Ndt80 actively evicts the Hst1 repressor or passively wins by mass action at MSEs of key targets (*NDT80*, *IME2*, *SMA2/mORC1*).

6. **Separate Set3C vs. Sum1-complex contributions** using complex-specific separation-of-function alleles (e.g., Rfm1-binding vs. Snt1/Set3-binding mutants of Hst1) to assign each target gene to its responsible complex.

---

## Conclusion

HST1 (YOL068C; UniProt P53685) is unambiguously the **NAD⁺-dependent protein/histone deacetylase HST1** of *Saccharomyces cerevisiae* — a Class I sirtuin, EC 2.3.1.286, and a Sir2 paralog. All literature reviewed corresponds precisely to this gene and organism; the gene symbol is **not** ambiguous in this context. Its primary function is **gene-specific transcriptional repression of meiotic/middle-sporulation genes** as the catalytic subunit of the **Sum1–Rfm1–Hst1** complex at MSE promoters, executed by NAD⁺-dependent deacetylation of nucleosomal histone tails in the **nucleus**, and gated developmentally by Ndt80 competition and metabolically by its role as a **low-affinity NAD⁺ sensor** that controls *de novo* NAD⁺ biosynthesis.


## Artifacts

- [OpenScientist final report](HST1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](HST1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:24164855
2. PMID:15274642
3. PMID:16388603
4. PMID:12612074
5. PMID:17242192
6. PMID:12972620
7. PMID:30760525
8. PMID:11313477
9. PMID:27543294
10. PMID:26646153
11. PMID:10562556
12. PMID:12832469
13. PMID:27362276
14. PMID:8810037
15. PMID:14502267
16. PMID:29543820
17. PMID:29066473
18. PMID:14729974
19. PMID:11711434
20. PMID:10693811
21. PMID:17289592
22. PMID:17951578