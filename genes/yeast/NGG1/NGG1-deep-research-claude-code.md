---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:21:41.102306'
end_time: '2026-11-18T15:24:32.277692'
duration_seconds: 171.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: NGG1
  gene_symbol: NGG1
  uniprot_accession: P32494
  protein_description: 'RecName: Full=SAGA complex subunit NGG1; AltName: Full=Chromatin-remodeling
    complexes subunit NGG1; AltName: Full=Transcriptional adapter 3;'
  gene_info: Name=NGG1; Synonyms=ADA3, SWI7; OrderedLocusNames=YDR176W; ORFNames=YD9395.09;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the NGG1 family. .
  protein_domains: Histone_AcTrfase_su3. (IPR019340); Ada3 (PF10198)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-fable-5-2
  - claude-haiku-5-5
  web_search_requests: 11
  num_turns: 23
  total_cost_usd: 2.045591325
  session_id: 4d082601-fd04-43ee-baf4-8860842f7de7
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P32494
- **Protein Description:** RecName: Full=SAGA complex subunit NGG1; AltName: Full=Chromatin-remodeling complexes subunit NGG1; AltName: Full=Transcriptional adapter 3;
- **Gene Information:** Name=NGG1; Synonyms=ADA3, SWI7; OrderedLocusNames=YDR176W; ORFNames=YD9395.09;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the NGG1 family. .
- **Key Domains:** Histone_AcTrfase_su3. (IPR019340); Ada3 (PF10198)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NGG1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NGG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NGG1** (gene ID: NGG1, UniProt: P32494) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still gathering primary-source details: checking the repository's cached publications for the key NGG1/ADA3 papers before writing the report.

# NGG1 (ADA3 / SWI7; YDR176W; UniProt P32494) in *Saccharomyces cerevisiae*: research report

## Identity check

The target is unambiguous. NGG1, ADA3 and SWI7 are names for the same yeast gene (YDR176W), and the literature matches the UniProt description: a 702-residue SAGA subunit in the NGG1 family with the Ada3 / histone acetyltransferase subunit 3 domain (PF10198, IPR019340). The human ortholog is TADA3. No conflicting gene with this symbol was found.

**Sourcing limits.** Most primary papers were read as abstracts only (PubMed and PMC blocked automated access). Statements taken from search summaries or reviews rather than the paper itself are marked "secondary". I did not find any 2023–2024 primary study focused on yeast Ada3 itself; the most recent directly relevant work is a 2023 HAT-module study and a 2025 structure.

## 1. Summary

Ngg1/Ada3 is a non-catalytic, obligate structural and regulatory subunit of the Gcn5 histone acetyltransferase (HAT) module. It has no enzymatic activity of its own. Its primary function is to enable Gcn5, together with Ada2, to acetylate nucleosomal histone H3 (and H2B) with the lysine specificity of the native complexes. The same module sits in three nuclear complexes: SAGA, the SAGA-like SLIK/SALSA form, and the smaller ADA complex. Through SAGA it contributes to coactivation of RNA polymerase II transcription.

## 2. Discovery and nomenclature

- **NGG1.** Brandl et al. (EMBO J 1993, PMID:8262068) isolated the gene in a screen for relief of glucose repression of Gal4-regulated transcription. An *ngg1* null in a *gal80* background gave about 300-fold relief versus about 20-fold for *gal80* alone, and the effect depended on Gal4. The authors concluded Ngg1 inhibits Gal4 function in glucose (secondary: abstract summary via [SGD](https://yeastgenome.org/locus/NGG1)).
- **ADA3.** Piña et al. (Mol Cell Biol 1993, PMID:8413201) isolated the gene by resistance to toxic GAL4-VP16 overexpression, the "alteration/deficiency in activation" screen that also yielded ADA2 and GCN5 (title from the UniProt record; paper not read).
- **Dual regulator.** The two screens gave Ngg1 a reputation as both coactivator and repressor. Later work places both phenotypes within its role in Gcn5 complexes rather than as a separate repressor activity.

## 3. Molecular function: an adaptor that licenses Gcn5 for nucleosomes

**The Ada2–Ada3–Gcn5 trimer.** Horiuchi et al. 1995 (PMID:7862114) showed that the three proteins "form a heterotrimeric complex in vitro, with ADA2 as the linchpin holding ADA3 and GCN5 together." Ada3 splits into two non-overlapping domains that complement a *Δada3* strain only when supplied together. The C-terminal domain "alone suffices for heterotrimeric complex formation in vitro," and the authors proposed that the N-terminal domain mediates contact with activation domains.

**Enabling nucleosomal acetylation.** Balasubramanian et al. 2002 (J Biol Chem 277:7989–7995, PMID:11773077) is the key biochemical paper:

- Ada2, Ada3 and Gcn5 "form a catalytic core of the ADA and Spt-Ada-Gcn5-acetyltransferase HAT complexes, which is necessary and sufficient in vitro for nucleosomal HAT activity and lysine specificity of the intact HAT complexes."
- "Ada3 is necessary for Gcn5-dependent nucleosomal HAT activity in yeast extracts."
- "Ada2 potentiates the Gcn5 catalytic activity and … Ada3 facilitates nucleosomal acetylation and an expanded lysine specificity."

This is the paper behind the GO "histone acetyltransferase activity" IDA on NGG1. The activity belongs to Gcn5; Ada3 contributes to it as part of the complex, so the annotation is best read as "contributes to" rather than as intrinsic catalysis.

**Substrate specificity of the complexes.** Per the UniProt summary of Grant et al. 1999 (PMID:10026213), SAGA preferentially acetylates H3 (K9, K14, K18, K23) and H2B, and ADA acetylates nucleosomal H3 (K14, K18) and H2B. Free Gcn5 acetylates H3 tail peptides but is active on nucleosomes only with both Ada2 and Ada3 ([Mattoo et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/), introduction). A later study reports that Ada2 and Ada3 are also needed for robust acetylation of non-histone substrates (secondary; search summary).

**Activator contacts.** Two 1996 J Biol Chem papers from the Brandl lab ([SGD 8663102](https://www.yeastgenome.org/reference/8663102), [SGD 8621592](https://www.yeastgenome.org/reference/8621592)) map functions to the N-terminal 373 residues (all secondary, from abstract summaries):

- Residues 274–373, narrowed to a Phe-rich predicted amphipathic helix, are essential for glucose repression.
- An activation domain lies in the N-terminus.
- Residues 274–307 are required for a two-hybrid interaction with the C-terminal activation domain of Pdr1. The authors suggested this may be indirect, mediated by the ADA complex.

Current models assign most activator binding in SAGA to Tra1, so direct Ada3–activator contact remains unproven.

## 4. Complexes and architecture

| Complex | Size | Ngg1/Ada3 context | Key evidence |
|---|---|---|---|
| SAGA | 1.8 MDa, 19 subunits | HAT module (Gcn5, Ada2, Ngg1/Ada3, Sgf29) | Grant et al. 1998 (PMID:9674426); Lee et al. 2011 (PMID:21734642) |
| SLIK/SALSA | SAGA variant with truncated Spt7, no Spt8 | Same HAT module | PMID:12446794, PMID:12186975; structurally and biochemically equivalent to SAGA (PMID:33864814) |
| ADA | 0.8 MDa | HAT module plus Ahc1 and Ahc2 | Eberharter et al. 1999 (PMID:10490601); Lee et al. 2011 |

- **ADA is a distinct complex.** Eberharter et al. 1999 purified it over 10 chromatographic steps and showed Ada2, Ada3 and Gcn5 "are indeed integral components of ADA." Deleting AHC1 disrupted ADA but not SAGA.
- **Modular network.** Lee et al. 2011 defined a HAT module that "includes all three previous described components (Gcn5, Ada3 and Ada2), together with Sgf29" and is shared between SAGA and ADA. In *ada2Δ*, "all and only the components of the HAT module were lost." The composition of *ada3Δ* complexes was not in the portion I could read.
- **Tra1.** Saleh et al. 1998 (PMID:9756893) identified Tra1 "through tandem mass spectrometry analysis of proteins that associate with Ngg1p/Ada3p."
- **Cryo-EM of yeast SAGA.** Wang et al. 2020 (Nature, PMID:31969703) resolved the core at 3.3 Å; the HAT module was too mobile to model (secondary: [PomBase](https://www.pombase.org/reference/PMID:31969703) and [RCSB 6T9I](https://www.rcsb.org/structure/6t9i) summaries).
- **Tethering of the HAT module.** A 2023 study ([BBA Gene Regul Mech](https://pmc.ncbi.nlm.nih.gov/articles/PMC10226619/)) found the Ada2 SWIRM domain is required for HAT-module incorporation into SAGA but not ADA. Its AlphaFold-Multimer model predicts Ada3 as helical segments joined by disordered linkers that contact all module subunits, with the Ada3 C-terminus positioned near the tethering site (secondary: search summary).

**First resolved structure of Ada3 in SAGA.** [Mattoo et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/) (Mol Cell 85:4333–4346, doi:10.1016/j.molcel.2025.10.025) solved *Chaetomium thermophilum* SAGA at 2.7 Å overall, with the minimal HAT module at 3.7 Å. Residue numbers below are for the *C. thermophilum* proteins, not yeast Ngg1.

- "Gcn5 is nested between Ada2 and Ada3."
- "Ada3 contains an elongated coiled coil region (aa 573–634) that interacts with most of the of C-terminal region of Ada2 (aa 233–326) and the SWIRM domain of Ada2."
- "Together, Ada1-SID (residues 61–129), the SWIRM domain of Ada2 (residues 453–514), and Ada3 (residues 394–530) form a multi-helical bundle."
- "Two Spt7 helices (Helix 1 and Helix2) extend from the core and clamp Ada3."
- Yeast mutants of the Ada1 and Spt7 elements lost Gcn5 from SAGA. Ada3 itself was not mutated, and Sgf29 was not modelled.

Ada3 is therefore both an intra-module scaffold and the surface through which the core (Spt7, Ada1) holds the HAT module.

## 5. Biological process

- **Transcription coactivation.** SAGA is a general cofactor for RNA polymerase II transcription (PMID:28918903, PMID:10864329, per UniProt). Ngg1's contribution is promoter-proximal histone acetylation by the HAT module. *ada3* mutants show slow growth and weakened activation by a subset of acidic activators (Horiuchi 1995).
- **Glucose repression of GAL genes.** This founding phenotype is real but best treated as a downstream consequence of losing Gcn5-complex function at Gal4-regulated promoters.
- **Cross-talk with deubiquitination.** Loss of the HAT module from SAGA lowers its H2B deubiquitinating activity (2023 study; secondary).
- **DNA damage response: weakly supported.** The GO IMP annotation and UniProt's "may be involved in response to DNA damage" cite PMID:15340070, a *Drosophila* Ada2b paper. Its abstract says only that "a yeast ada2 mutant is also sensitive to a genotoxic agent"; neither ADA3 nor NGG1 appears in the abstract. I could not read the full text, so whether an *ada3/ngg1* mutant was assayed is unverified.

## 6. Localization

Ngg1 acts in the nucleus, on chromatin at promoters and upstream activating sequences as part of SAGA, SLIK and ADA. Support is by complex membership and function; the nucleus rows in GOA are NAS and IEA rather than direct imaging. UniProt predicts a nuclear localization signal at residues 606–618 (sequence-based, not tested). Abundance is about 2,470 molecules per cell in log phase (PMID:14562106).

## 7. Sequence features and conservation

- 702 aa, 79.3 kDa; predicted disordered regions at 1–29, 90–224, 611–636 and 672–702 (MobiDB-lite).
- Phosphorylation at Ser134, Ser407 and Thr464 (Thr464 from a Cdk1 substrate screen, PMID:19779198); no functional role established.
- The conserved Ada3 domain lies in the C-terminal half, matching the Ada2/Gcn5-binding C-terminal domain of Horiuchi 1995. The N-terminal half is more divergent.
- Orthologs exist across eukaryotes. Human TADA3 is in both SAGA and ATAC (secondary).

## 8. Open questions

- No nucleosome-bound structure of the HAT module shows how Ada3 "expands lysine specificity".
- The N-terminal domain is essential in vivo but has no defined molecular partner in current structures.
- Whether Ngg1 has any direct, HAT-independent role in DNA damage responses is unresolved.

## Sources

- [UniProt P32494](https://www.uniprot.org/uniprotkb/P32494) and [SGD NGG1](https://yeastgenome.org/locus/NGG1)
- Horiuchi et al. 1995, Mol Cell Biol 15:1203–9, PMID:7862114, [doi](https://doi.org/10.1128/MCB.15.3.1203)
- Balasubramanian et al. 2002, J Biol Chem 277:7989–95, PMID:11773077, [doi](https://doi.org/10.1074/jbc.M110849200)
- Eberharter et al. 1999, Mol Cell Biol 19:6621–31, PMID:10490601, [doi](https://doi.org/10.1128/MCB.19.10.6621)
- Saleh et al. 1998, J Biol Chem 273:26559–65, PMID:9756893, [doi](https://doi.org/10.1074/jbc.273.41.26559)
- Lee et al. 2011, Mol Syst Biol 7:503, PMID:21734642, [PMC3159981](https://pmc.ncbi.nlm.nih.gov/articles/PMC3159981/)
- Wang et al. 2020, Nature, PMID:31969703, [PomBase record](https://www.pombase.org/reference/PMID:31969703)
- "The SAGA HAT module is tethered by its SWIRM domain and modulates activity of the SAGA DUB module", 2023, [PMC10226619](https://pmc.ncbi.nlm.nih.gov/articles/PMC10226619/)
- Mattoo et al. 2025, Mol Cell 85:4333–4346, PMID:41260211, [PMC12768303](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/)
- "The Ada2/Ada3/Gcn5/Sgf29 histone acetyltransferase module" (review), [PMC8351874](https://pmc.ncbi.nlm.nih.gov/articles/PMC8351874)
- Qi et al. 2004, Mol Cell Biol 24:8080–9, PMID:15340070, [doi](https://doi.org/10.1128/MCB.24.18.8080-8089.2004)
- Brandl lab 1996 papers: [SGD 8663102](https://www.yeastgenome.org/reference/8663102), [SGD 8621592](https://www.yeastgenome.org/reference/8621592)

## Citations

1. https://yeastgenome.org/locus/NGG1
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/
3. https://www.yeastgenome.org/reference/8663102
4. https://www.yeastgenome.org/reference/8621592
5. https://www.pombase.org/reference/PMID:31969703
6. https://www.rcsb.org/structure/6t9i
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC10226619/
8. https://www.uniprot.org/uniprotkb/P32494
9. https://doi.org/10.1128/MCB.15.3.1203
10. https://doi.org/10.1074/jbc.M110849200
11. https://doi.org/10.1128/MCB.19.10.6621
12. https://doi.org/10.1074/jbc.273.41.26559
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3159981/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC8351874
15. https://doi.org/10.1128/MCB.24.18.8080-8089.2004