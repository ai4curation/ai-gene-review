---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T17:22:54.511423'
end_time: '2026-07-17T18:25:50.717105'
duration_seconds: 3776.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argE
  gene_symbol: argE
  uniprot_accession: Q88CJ5
  protein_description: 'SubName: Full=Acetylornithine deacetylase {ECO:0000313|EMBL:AAN70751.1};
    EC=3.5.1.16 {ECO:0000313|EMBL:AAN70751.1};'
  gene_info: Name=argE {ECO:0000313|EMBL:AAN70751.1}; OrderedLocusNames=PP_5186 {ECO:0000313|EMBL:AAN70751.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase M20A family. ArgE subfamily.
  protein_domains: AcOrn-deacetyl. (IPR010169); ArgE/DapE_CS. (IPR001261); Bact_exopeptidase_dim_dom.
    (IPR036264); Peptidase_M20. (IPR002933); Peptidase_M20_dimer. (IPR011650)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: argE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CJ5
- **Protein Description:** SubName: Full=Acetylornithine deacetylase {ECO:0000313|EMBL:AAN70751.1}; EC=3.5.1.16 {ECO:0000313|EMBL:AAN70751.1};
- **Gene Information:** Name=argE {ECO:0000313|EMBL:AAN70751.1}; OrderedLocusNames=PP_5186 {ECO:0000313|EMBL:AAN70751.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase M20A family. ArgE subfamily.
- **Key Domains:** AcOrn-deacetyl. (IPR010169); ArgE/DapE_CS. (IPR001261); Bact_exopeptidase_dim_dom. (IPR036264); Peptidase_M20. (IPR002933); Peptidase_M20_dimer. (IPR011650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argE** (gene ID: argE, UniProt: Q88CJ5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *argE* / PP_5186 (UniProt Q88CJ5) in *Pseudomonas putida* KT2440

## Summary

The gene **argE** (ordered locus **PP_5186**; UniProt **Q88CJ5**) of *Pseudomonas putida* strain KT2440 encodes a **cytoplasmic, zinc/cobalt-dependent dinuclear metallohydrolase** belonging to the **peptidase M20A family, ArgE subfamily**. Its primary predicted function is that of an **acetylornithine deacetylase (N-acetyl-L-ornithine deacetylase, EC 3.5.1.16)**, which catalyzes the hydrolysis of **N-acetyl-L-ornithine + H₂O → L-ornithine + acetate**. This is the fifth step of the classical **linear ("acetylase") branch of de novo L-arginine biosynthesis**, the step that liberates free L-ornithine so that it can be carbamoylated to citrulline and, ultimately, converted to arginine. All bioinformatic, evolutionary, and network evidence converge on this assignment; there is, at present, no direct wet-lab biochemical characterization of the PP_5186 protein itself, so the functional call rests on strong homology-based inference anchored to biochemically validated orthologs.

The identity of the target was rigorously verified. PP_5186 shares **50.3 % amino-acid identity** with the experimentally characterized *Escherichia coli* ArgE, and **all seven functionally annotated catalytic and metal-binding residues** of *E. coli* ArgE are strictly conserved. Multiple curated, ArgE-specific signatures (HAMAP MF_01108, NCBIfam TIGR01892, InterPro IPR010169) match the protein, and it maps to the KEGG ortholog **K01438 (argE)**. Genomically, PP_5186 is immediately downstream of **PP_5185**, the N-acetylglutamate synthase (ArgA) that catalyzes the first committed step of the same pathway, and its STRING functional-interaction network is dominated by arginine-biosynthesis and arginine-metabolism enzymes. The subcellular location is **cytoplasmic**, consistent with a soluble biosynthetic metalloenzyme and with immunolocalization of a plant ArgE homolog to the cytosol.

An important nuance is that *P. putida* KT2440 does **not** rely primarily on the ArgE route. Like most bacteria, it encodes the **cyclic ArgJ ornithine acetyltransferase (PP_1346)**, which recycles the acetyl group and is the dominant ornithine-generating enzyme. *P. putida* also carries a **second, more divergent argE paralog (PP_3571)**. In a closely analogous organism, *Sinorhizobium meliloti*, which likewise encodes both ArgJ and ArgE, single and even double *argE/argJ* mutants remain arginine prototrophs. PP_5186 is therefore best described as a **catalytically competent but genetically redundant / accessory** deacetylase route to ornithine, rather than the essential committed enzyme it is in *Enterobacteriaceae*.

---

## Key Findings

### Finding 1 — Primary function: N-acetyl-L-ornithine deacetylase (EC 3.5.1.16)

PP_5186 (Q88CJ5, *argE*) is a **predicted N-acetyl-L-ornithine deacetylase (EC 3.5.1.16)** that catalyzes the reaction:

> **N-acetyl-L-ornithine + H₂O → L-ornithine + acetate**

This is the fifth (final deacylation) step of the **linear/acetylase branch of L-arginine biosynthesis**, in which the acetyl group that had been added to glutamate at the start of the pathway is finally removed to release free ornithine. The assignment rests on a coherent stack of curated evidence: UniProt Q88CJ5 describes a **380-residue, 41.4-kDa** protein assigned to the **peptidase M20A family / ArgE subfamily**, carrying EC 3.5.1.16. Critically, the protein matches ArgE-*specific* bioinformatic signatures rather than generic M20 signatures — **HAMAP MF_01108 (ArgE)**, **NCBIfam TIGR01892 (AcOrn-deacetyl)**, and **InterPro IPR010169 (AcOrn-deacetyl)** — and is annotated with **GO:0008777 (acetylornithine deacetylase activity)** and **GO:0006526 (L-arginine biosynthetic process)**. It maps to the KEGG ortholog **K01438 (argE)**.

The reaction itself is not in doubt for the ArgE family: homologous enzymes have been biochemically confirmed to catalyze exactly this hydrolysis. Work on *Sinorhizobium meliloti* describes that "*N-acetylornithine (NAO) deacetylase (ArgE) hydrolyses NAO to acetate and ornithine*" ([PMID: 26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/)), and the arginine-pathway evolution literature states that ornithine "*is produced from N-alpha-acetylornithine by a deacylase, acetylornithinase (AOase) (argE encoded)*" ([PMID: 10692366](https://pubmed.ncbi.nlm.nih.gov/10692366/)). Both statements define precisely the EC 3.5.1.16 function assigned to Q88CJ5.

### Finding 2 — A cytoplasmic dinuclear Zn(II)/Co(II) M20A metallohydrolase with broad α-N-acyl specificity

ArgE is a **dinuclear (two-metal) zinc/cobalt-dependent metallohydrolase**. UniProt Q88CJ5 lists a Zn²⁺ cofactor, both Cobalt and Zinc keywords, explicit metal-binding sites, and a **cytoplasmic** subcellular location. Its domain architecture is the canonical M20 pairing of a catalytic **Peptidase M20 domain (PF01546)** with an **M20 dimerization domain (PF07687, residues 174–278)** — the latter being responsible for the physiological homodimer typical of this family.

The metal chemistry and substrate scope are established by biochemical work on the *E. coli* ArgE ortholog. Javid-Majd and Blanchard reported that "*the purified enzyme contains a single atom of zinc per monomer. The activity of this enzyme can be increased greater than 2-fold by the addition of zinc, or 8-fold by the addition of cobalt. This suggests that the enzyme can accommodate two metal ions at the active site*" ([PMID: 10684608](https://pubmed.ncbi.nlm.nih.gov/10684608/)). The same study established that the specificity is **broad** rather than narrowly restricted to acetylornithine: "*The substrate specificity of the enzyme is relatively broad, with a number of alpha-N-acyl-L-amino acids exhibiting activity, including both alpha-N-acetyl- and alpha-N-formylmethionine that exhibit higher activity than alpha-N-acetyl-L-ornithine*" ([PMID: 10684608](https://pubmed.ncbi.nlm.nih.gov/10684608/)). The mechanism proceeds through a metal-activated water molecule that attacks the acetyl carbonyl, aided by a general-acid/general-base pair, with a single partially rate-limiting proton transfer.

Direct structural confirmation of the two-metal architecture comes from EXAFS spectroscopy of *E. coli* ArgE loaded with Zn(II), Co(II), and Mn(II), which reveals a metal–metal vector of ~3.3–3.4 Å "*suggesting the formation of a dinuclear site*" ([PMID: 22459917](https://pubmed.ncbi.nlm.nih.gov/22459917/)). The cytoplasmic localization is further corroborated by immunogold electron microscopy of the plant ArgE homolog DRIP-1, which is "*confined exclusively to the cytosol*" ([PMID: 12102508](https://pubmed.ncbi.nlm.nih.gov/12102508/)).

### Finding 3 — Pathway context: a redundant deacetylase alongside the dominant cyclic ArgJ route

*P. putida* KT2440 possesses **both** routes to ornithine. The **cyclic** route uses **ArgJ ornithine acetyltransferase (KEGG K00620, gene PP_1346)**, which transfers the acetyl group from N-acetylornithine directly onto glutamate, thereby regenerating N-acetylglutamate and recycling the acetyl moiety. The **linear** route instead uses ArgE to hydrolyze off the acetyl group and discard it as acetate. Strikingly, KEGG maps **two** acetylornithine deacetylase genes to K01438 in KT2440: the target **PP_5186** and a paralog **PP_3571**. Other pathway components are present as expected — argB/NAG kinase (PP_5289), argC (PP_0432/PP_3633).

Because ArgJ is present and dominant in most bacteria — "*the formation of ornithine is catalyzed by an enzyme transferring the acetyl group of N-alpha-acetylornithine to glutamate (ornithine acetyltransferase [OATase]) (argJ encoded)*" ([PMID: 10692366](https://pubmed.ncbi.nlm.nih.gov/10692366/)) — the ArgE deacetylase is dispensable in organisms that carry both. This is demonstrated directly in *S. meliloti*, where "*argE and argJ single mutants, and an argEJ double mutant, are arginine prototrophs*" ([PMID: 26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/)). By analogy, PP_5186 is expected to be a **redundant / accessory** contributor to ornithine formation in *P. putida*, backing up the cyclic ArgJ route.

### Finding 4 — Sequence identity and strict conservation of the catalytic machinery

Global pairwise alignment identifies PP_5186 as the **true ArgE ortholog**. It shares **50.3 % amino-acid identity** with the experimentally characterized *E. coli* ArgE (P23908, 383 aa) but only **36.8 %** with its own *P. putida* paralog PP_3571 (Q88GZ4), meaning PP_5186 is substantially closer to bona fide ArgE than to its divergent in-genome paralog.

All **seven** functionally annotated *E. coli* ArgE residues are strictly conserved in PP_5186:

| Role | *E. coli* ArgE | PP_5186 (Q88CJ5) |
|------|----------------|------------------|
| Metal ligand (His) | His80 | His76 |
| Metal ligand (Asp) | Asp112 | Asp108 |
| Metal ligand (Glu) | Glu145 | Glu141 |
| Metal ligand (Glu) | Glu169 | Glu165 |
| Metal ligand (His) | His355 | His352 |
| Catalytic general base (Asp) | Asp82 | Asp78 |
| Catalytic general acid (Glu) | Glu144 | Glu140 |

This reproduces the canonical peptidase-M20 dinuclear metallohydrolase active-site constellation — two histidines, bridging Glu/Asp carboxylates, and a general acid/base pair. The functional relevance of the general acid/base dyad is established biochemically: the pH-dependence of *E. coli* ArgE "*revealed the presence of two enzymic groups, one functioning as a general base and one functioning as a general acid*" ([PMID: 10684608](https://pubmed.ncbi.nlm.nih.gov/10684608/)). The complete conservation of these catalytic residues in PP_5186 is strong structural evidence that the enzyme is catalytically competent.

### Finding 5 — Genomic synteny with argA (N-acetylglutamate synthase) and a Lrp-family regulator

The genomic neighborhood of PP_5186 reinforces its arginine-biosynthesis role. Immediately upstream lies **PP_5185**, an amino-acid acetyltransferase (P0A0Z9) annotated as **N-acetylglutamate synthase / ArgA (EC 2.3.1.1)** — the **first, committed step** of arginine biosynthesis (glutamate + acetyl-CoA → N-acetyl-L-glutamate). Thus the **first (ArgA)** and **fifth (ArgE)** steps of the acetylated-ornithine branch are physically clustered. Nearby genes include **PP_5188**, an **AsnC/Lrp-family transcriptional regulator** — a family that commonly senses amino acids and controls amino-acid biosynthetic operons — plus glutamate/glutamylpolyamine-synthetase-family genes (PP_5183/PP_5184).

This arrangement mirrors the operonic organization of *argE* genes in other bacteria. In *Lactococcus lactis*, "*The gltS-argE operon ... encodes a putative glutamate or arginine transport protein and acetylornithine deacetylase, which catalyzes an important step in the arginine biosynthesis pathway*" ([PMID: 14762010](https://pubmed.ncbi.nlm.nih.gov/14762010/)), demonstrating that *argE* genes are routinely embedded in arginine-biosynthesis gene clusters under dedicated regulation — exactly the context observed around PP_5186.

### Finding 6 — STRING network embeds PP_5186 in the arginine biosynthesis/metabolism module

The STRING v12 functional-interaction network for PP_5186 (*P. putida* KT2440, taxid 160488) is dominated by arginine-pathway enzymes, with high confidence scores:

| Partner | Function | STRING score |
|---------|----------|--------------|
| argG | argininosuccinate synthase | 0.964 |
| argF | ornithine carbamoyltransferase | 0.929 |
| arcB | (arginine catabolism) | 0.926 |
| PP_3571 | argE paralog | 0.922 |
| argJ | ornithine acetyltransferase | 0.919 |
| aruC | acetylornithine/succinylornithine aminotransferase | 0.916 |
| arcA | arginine deiminase | 0.908 |
| argA | N-acetylglutamate synthase | 0.893 |
| argB | NAG kinase | 0.624 |
| astC | succinylornithine aminotransferase | 0.586 |

Critically, the network directly links PP_5186 to the enzyme that **generates its substrate** (aruC/ArgD → N-acetylornithine) and to the enzyme that **consumes its product** (argF → uses L-ornithine + carbamoyl-phosphate to make citrulline), as well as to the downstream argininosuccinate-forming steps (argG/argH). This "substrate-upstream, product-downstream" flanking is the signature of a metabolic-pathway member and places PP_5186 squarely at the ornithine node.

---

## Mechanistic Model / Interpretation

The evidence assembles into a coherent mechanistic picture of PP_5186 as the ornithine-releasing deacetylase of the **linear (acetylase) branch** of arginine biosynthesis, operating in parallel with the dominant **cyclic (ArgJ) branch**.

```
                  De novo L-arginine biosynthesis in P. putida KT2440
                  ===================================================

     L-glutamate
        |
        |  ArgA / N-acetylglutamate synthase   (PP_5185)  <-- syntenic neighbor
        v            [EC 2.3.1.1]
   N-acetyl-L-glutamate
        |
        |  ArgB / NAG kinase (PP_5289)
        v
   N-acetylglutamyl-phosphate
        |
        |  ArgC (PP_0432 / PP_3633)
        v
   N-acetylglutamate-5-semialdehyde
        |
        |  ArgD / AruC  aminotransferase  (STRING 0.916)
        v
   N-acetyl-L-ornithine  <==== SUBSTRATE
        |                                \
        |  ArgE  (PP_5186, TARGET)        \  ArgJ ornithine acetyltransferase
        |  EC 3.5.1.16                     \ (PP_1346)  -- DOMINANT cyclic route
        |  + H2O  -> acetate (discarded)    \  transfers acetyl back to glutamate
        v                                     v
   L-ORNITHINE  <==== PRODUCT  <----------------
        |
        |  ArgF / ornithine carbamoyltransferase (STRING 0.929)
        v
   L-citrulline
        |
        |  ArgG argininosuccinate synthase (STRING 0.964) --> ArgH
        v
   L-ARGININE
```

**Active-site chemistry.** PP_5186 is a homodimeric M20A metalloenzyme. Each monomer harbors a **dinuclear metal center** (typically 1–2 Zn²⁺, with Co²⁺ strongly activating) bridged by carboxylate ligands (Asp108, Glu141, Glu165) and coordinated by two histidines (His76, His352). A metal-bound water/hydroxide is the nucleophile that attacks the acetyl carbonyl of N-acetyl-L-ornithine; **Asp78** acts as the general base to deprotonate/orient the water and **Glu140** as the general acid to protonate the leaving amine, resolving the tetrahedral intermediate to release L-ornithine and acetate. The strict conservation of every one of these residues (Finding 4) means the catalytic apparatus is intact and the enzyme is very likely active.

**Physiological role and redundancy.** Because *P. putida* carries the cyclic **ArgJ** route (PP_1346) as its principal ornithine source, PP_5186 functions as a **parallel / backup deacetylase** rather than an indispensable committed enzyme. The precedent from *S. meliloti* — where deleting *argE*, *argJ*, or both still yields arginine prototrophs — indicates that in dual-route organisms neither enzyme is strictly essential, and additional aminoacylase-type deacetylases can further buffer the pathway. The broad α-N-acyl-amino-acid specificity of ArgE orthologs (Finding 2) further suggests PP_5186 may contribute to **secondary deacylation activities** (e.g., turnover of other N-acetyl/N-formyl amino acids), though this is unconfirmed for the *P. putida* protein.

**Localization.** All evidence points to a **cytoplasmic** site of action: a soluble metalloenzyme with no signal peptide, UniProt cytoplasm annotation, and cytosolic immunolocalization of a plant homolog. This is where free ornithine is generated and immediately handed off to ArgF for carbamoylation — consistent with the tight metabolic channeling implied by the STRING network.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|--------------------------------|
| [10684608](https://pubmed.ncbi.nlm.nih.gov/10684608/) | *Mechanistic analysis of the argE-encoded N-acetylornithine deacetylase* | Primary biochemistry of *E. coli* ArgE: Zn/Co dinuclear site, broad α-N-acyl specificity, general acid/base dyad. Defines the residues conserved in PP_5186. |
| [22459917](https://pubmed.ncbi.nlm.nih.gov/22459917/) | *Structural characterization of Zn/Co/Mn-loaded ArgE from E. coli* | EXAFS evidence for a dinuclear metal center (M–M ~3.3–3.4 Å), confirming the two-metal architecture. |
| [26271664](https://pubmed.ncbi.nlm.nih.gov/26271664/) | *Arginine biosynthesis in Sinorhizobium meliloti 1021* | Defines the ArgE reaction (NAO → acetate + ornithine); shows *argE*, *argJ*, and *argEJ* mutants are prototrophs — the basis for the redundancy interpretation. |
| [10692366](https://pubmed.ncbi.nlm.nih.gov/10692366/) | *Evolution of arginine biosynthesis; N-α-acetyl ornithinase* | Establishes that *argE* encodes the ornithine-producing deacylase and that ArgJ is the dominant route in most prokaryotes. |
| [14762010](https://pubmed.ncbi.nlm.nih.gov/14762010/) | *ArgR and AhrC regulation in Lactococcus lactis* | Shows *argE* genes are embedded in arginine-biosynthesis operons under dedicated regulation, paralleling PP_5186's syntenic/regulated context. |
| [12102508](https://pubmed.ncbi.nlm.nih.gov/12102508/) | *Citrulline and DRIP-1 (ArgE homologue) in wild watermelon* | Immunogold EM localizes an ArgE homolog exclusively to the cytosol, supporting cytoplasmic localization. |
| [9829957](https://pubmed.ncbi.nlm.nih.gov/9829957/) | *argE gene of Myxococcus xanthus* | Genetic demonstration that *argE* disruption causes arginine auxotrophy in an organism relying on the linear route — validates the ArgE→arginine functional link. |
| [11852094](https://pubmed.ncbi.nlm.nih.gov/11852094/) | *lysK as an argE homolog in Thermus thermophilus* | Illustrates the broad specificity/promiscuity of the ArgE family (deacetylates both N-acetylornithine and N-acetyllysine). |

**Supporting vs. challenging.** All the ArgE-family papers (10684608, 22459917, 26271664, 10692366, 14762010, 12102508, 9829957) *support* the annotation of PP_5186. The *challenge* is one of directness rather than contradiction: none of these characterize the *P. putida* PP_5186 protein itself, and the *S. meliloti* and dual-route data actively temper the physiological importance of ArgE where ArgJ is present. Several other *Pseudomonas*-related papers surfaced during literature search (e.g., PADI/citrullination in sepsis, c-di-GMP signaling, glyoxal responses, polyamine synthases) are **not relevant** to this gene and were correctly excluded — they concern unrelated arginine-derivative biology or share only superficial keyword overlap.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of PP_5186.** The functional assignment is entirely homology- and network-based. There is no purified-enzyme assay, no measured kcat/Km for N-acetyl-L-ornithine or alternative substrates, and no crystal structure for the *P. putida* protein. Confidence in the reaction is high (strong ortholog + full active-site conservation), but the quantitative kinetics and true substrate preference are unmeasured.

2. **Redundancy and physiological role are inferred, not tested.** No *P. putida argE* (PP_5186) knockout phenotype has been reported. The prediction that PP_5186 is dispensable (because ArgJ/PP_1346 dominates) rests on analogy to *S. meliloti*. A *P. putida*-specific mutant analysis is needed to confirm redundancy and to distinguish the roles of PP_5186 versus the paralog PP_3571.

3. **Two paralogs mapping to K01438.** The functional division of labor between PP_5186 and PP_3571 is unknown. They may be differentially expressed, differentially regulated, or specialized for distinct N-acyl substrates. Only sequence-distance data (50.3 % vs 36.8 % identity to *E. coli* ArgE) currently distinguish them.

4. **Substrate specificity is extrapolated.** The "broad α-N-acyl-amino-acid" behavior is documented for *E. coli* ArgE and *T. thermophilus* LysK, not for PP_5186. Whether PP_5186 has meaningful moonlighting deacylase activity (e.g., on N-acetylmethionine or N-acetyllysine) is untested.

5. **Regulation is unconfirmed.** The adjacent AsnC/Lrp-family regulator (PP_5188) and the general ArgR paradigm suggest arginine-responsive control, but promoter mapping, operon structure, and ArgR-binding for the PP_5185–PP_5186 region in *P. putida* have not been experimentally established.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Clone, express, and purify PP_5186; measure steady-state kinetics (kcat, Km) for N-acetyl-L-ornithine and a panel of α-N-acyl amino acids (N-acetylmethionine, N-formylmethionine, N-acetyllysine). Determine metal dependence (apo vs Zn²⁺ vs Co²⁺ reconstitution) to confirm the dinuclear Zn/Co behavior predicted from the *E. coli* ortholog.

2. **Genetic dissection of redundancy.** Construct single (ΔPP_5186, ΔPP_3571, ΔargJ/PP_1346) and combinatorial deletion strains in *P. putida* KT2440 and test arginine prototrophy on minimal medium ± arginine. This directly tests the redundancy hypothesis and clarifies the relative contributions of the linear vs cyclic routes.

3. **Paralog specialization.** Compare expression (RT-qPCR / RNA-seq) of PP_5186 vs PP_3571 across growth conditions (arginine excess/limitation, different carbon/nitrogen sources) to determine whether the paralogs are condition-specific.

4. **Structural validation.** Solve the crystal or cryo-EM structure of PP_5186 (or generate a high-confidence AlphaFold model with metal placement) to confirm the dinuclear active-site geometry and the positioning of His76/Asp78/Asp108/Glu140/Glu141/Glu165/His352.

5. **Regulatory mapping.** Test whether the PP_5188 Lrp/AsnC regulator and/or ArgR controls the PP_5185–PP_5186 locus via promoter–reporter fusions and electrophoretic mobility-shift assays with arginine as effector.

6. **Metabolic flux tracing.** Use ¹³C/¹⁵N-labeled precursors to quantify how much ornithine flux proceeds through the ArgE (acetate-releasing) branch versus the ArgJ (acetyl-recycling) branch under standard and arginine-limited growth.

---

## Conclusion

The gene **argE / PP_5186 (Q88CJ5)** in *Pseudomonas putida* KT2440 encodes a **cytoplasmic, zinc/cobalt-dependent dinuclear M20A metallohydrolase** that functions as an **acetylornithine deacetylase (EC 3.5.1.16)**, hydrolyzing **N-acetyl-L-ornithine to L-ornithine + acetate** in the linear branch of de novo L-arginine biosynthesis. The assignment is exceptionally well supported at the sequence, structural-homology, syntenic, and network levels — 50.3 % identity to biochemically validated *E. coli* ArgE with complete conservation of all catalytic and metal-binding residues — even though the *P. putida* protein has not itself been characterized in vitro. Because *P. putida* also carries the dominant cyclic ArgJ ornithine acetyltransferase (PP_1346) plus a second *argE* paralog (PP_3571), PP_5186 is most parsimoniously interpreted as a **catalytically competent but genetically redundant / accessory** route to ornithine.


## Artifacts

- [OpenScientist final report](argE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26271664
2. PMID:10692366
3. PMID:10684608
4. PMID:22459917
5. PMID:12102508
6. PMID:14762010