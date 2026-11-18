---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:24:34.626340'
end_time: '2026-11-18T15:26:18.716690'
duration_seconds: 104.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SAS4
  gene_symbol: SAS4
  uniprot_accession: Q04003
  protein_description: 'RecName: Full=Something about silencing protein 4;'
  gene_info: Name=SAS4; OrderedLocusNames=YDR181C; ORFNames=YD9395.15C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Not specified in UniProt
  protein_domains: Cullin_homology. (IPR016158); Sas4. (IPR038988); Sas4_dom. (IPR029184);
    SAS4 (PF15460)
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
  web_search_requests: 6
  num_turns: 14
  total_cost_usd: 1.4411296
  session_id: 70470438-f0e0-4f27-a865-9d6e8f2d8780
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q04003
- **Protein Description:** RecName: Full=Something about silencing protein 4;
- **Gene Information:** Name=SAS4; OrderedLocusNames=YDR181C; ORFNames=YD9395.15C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cullin_homology. (IPR016158); Sas4. (IPR038988); Sas4_dom. (IPR029184); SAS4 (PF15460)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SAS4" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SAS4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SAS4** (gene ID: SAS4, UniProt: Q04003) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SAS4 (YDR181C, UniProt Q04003) in *Saccharomyces cerevisiae*: research report for functional annotation

## 1. Identity verification

The target is unambiguous. "SAS4" in budding yeast is *Something About Silencing 4* (YDR181C, SGD:S000002589), and the literature matches the UniProt description, organism and domains (Pfam PF15460 SAS4; InterPro IPR029184, IPR038988, IPR016158 cullin homology).

One homonym must be excluded: metazoan **SAS-4/CPAP/CENPJ** ("spindle assembly abnormal 4") is an unrelated centriole protein. Web searches for "Sas4/Sas5" return *C. elegans* centriole papers (SAS-4, SAS-5, SAS-6), and none of that literature applies to Q04003.

**Sourcing.** I read the UniProt record, the SGD description and the cached PubMed abstracts in this repository; several primary papers were available only as abstracts. Statements marked † rest on my recollection of papers I could not retrieve this session and should be checked before being quoted in a review.

## 2. Summary

Sas4 is a non-catalytic, essential-for-activity subunit of the SAS (SAS-I) histone acetyltransferase complex. The complex consists of the MYST-family catalytic subunit Sas2, Sas4, and Sas5. Sas4 is the central architectural subunit: it bridges Sas2 and Sas5, and recombinant Sas2 has no detectable HAT activity without it. The complex acetylates histone H4 lysine 16 (H4K16) and supplies roughly 60% of cellular H4K16ac. Its best-defined biological role is to oppose Sir2-dependent deacetylation, which limits the spread of SIR heterochromatin at telomeres and silent mating-type loci. Sas4 is nuclear and chromatin-associated.

## 3. Molecular function

### 3.1 Sas4 is an obligate activating subunit, not the catalyst

- **Catalysis resides in Sas2.** Sas2 is a MYST-family acetyltransferase with a conserved acetyl-CoA binding motif. Mutations in that motif abolish Sas2-dependent silencing at HML and telomeres (Osada et al. 2001, PMID:11731479).
- **Sas4 is required for activity.** With recombinant proteins, "recombinant Sas2 has HAT activity that absolutely requires Sas4 and is stimulated by Sas5" (Sutton et al. 2003, PMID:12626510).
- **Sas4 is the bridging subunit.** Schaper et al. found "that Sas4p was the central subunit of the SAS-I complex, bridging Sas2p and Sas5p" (2005, PMID:15788653).
- **Loss of Sas4 phenocopies loss of Sas2.** Auxin-induced degradation of Sas4 reduced bulk H4K16ac to a similar degree as *sas2Δ* (Reiter et al. 2021, PMID:34014972).

No catalytic motif has been described in Sas4. Its "histone acetyltransferase activity" and "acetyltransferase activity" annotations (IDA from PMID:12626510 and PMID:11731479) therefore reflect assays of the complex. In GO terms, Sas4 *contributes to* H4K16 acetyltransferase activity rather than *enabling* it; its own function is closer to a scaffold or enzyme-activator role.

### 3.2 Substrate specificity

- **Sites.** The recombinant and native complexes acetylate H4K16 and H3K14 in vitro (PMID:12626510). A later study of the native complex reported exclusive H4K16 acetylation in vitro and a requirement for the bulk of H4K16ac in vivo ([Shia et al. 2005, JBC](https://www.jbc.org/article/S0021-9258(20)80910-7/fulltext)).
- **In vivo target.** An H4K16R mutant shows the same silencing phenotypes as *sas2Δ*, which points to H4K16 as the relevant target (Meijsing & Ehrenhofer-Murray 2001, PMID:11731480).
- **Free versus nucleosomal histones (sources conflict).** Sutton et al. found that neither recombinant nor native complex acetylated nucleosomal histones under conditions optimal for free histones (PMID:12626510). Shia et al. describe nucleosomal activity as very weak compared with NuA4. The SGD description says the complex "acetylates free histones and nucleosomes". The UniProt statement that it cannot acetylate nucleosomes follows Sutton et al.
- **Asf1-bound histones are not substrates.** Association of H3 and H4 with Asf1 blocks their acetylation by the complex, despite the physical and genetic SAS–Asf1 interaction (PMID:12626510).

### 3.3 Complex composition and stoichiometry

- Sas2, Sas4 and Sas5 co-purify as a nuclear complex (PMID:11731479; PMID:11731480).
- Osada et al. estimated its size at ~450 kDa. Shia et al. later characterised it as a ~125 kDa trimer with one copy of each subunit and no other components. The trimer is the better-characterised model.
- Sas5 is a YEATS-domain protein (described in the 2001 papers as a TAF(II)30 homolog or TFIIF-related).
- Sas4 is described as a "cullin domain protein" (PMID:34014972), consistent with the InterPro cullin-homology signature.
- I found no experimental structure of Sas4 or the SAS complex, and no domain-level map of the Sas4–Sas2 or Sas4–Sas5 contacts. The mechanism by which Sas4 activates Sas2 is unknown.

### 3.4 Interaction partners

| Partner | Evidence | Meaning |
|---|---|---|
| Sas2, Sas5 | Co-purification, recombinant reconstitution (PMID:11731479, 11731480, 12626510, 15788653) | Stable complex partners |
| Asf1 | Complex interacts with Asf1; *asf1* mutants show similar silencing defects (PMID:11731479) | Link to histone deposition |
| Cac1/Rlf2 (CAF-I) | Sas2 interacts with Cac1 (PMID:11731480) | Link to replication-coupled assembly |
| Various | High-throughput interactomes (PMID:21179020, PMID:37968396) | Supporting only |

UniProt cites PMID:11404324 for the Asf1 interaction and complex composition. That paper's abstract concerns Asf1/Hir1 and histone gene repression and does not mention SAS proteins. The citation may be mis-keyed, or the data may be in the full text, which I could not check.

## 4. Biological process

### 4.1 Heterochromatin boundaries

- **Discovery.** *SAS4* and *SAS5* were identified genetically as silencing regulators alongside *SAS2* (Xu et al. 1999, PMID:10471696, PMID:10471697). They are locus-specific: mutants lose silencing at HML and telomeres but improve silencing at a silencer-defective HMR†.
- **Mechanism.** Sas2 and Sir2 have opposing effects on H4K16 acetylation, and this balance sets the telomeric heterochromatin boundary. In *sas2Δ* or H4K16R cells, Sir3 spreads from about 3 kb to about 15 kb from the telomere, repressing adjacent genes (Suka et al. 2002, PMID:12379856; also Kimura et al. 2002, Nat Genet, cited via a review).
- **HMR boundary.** UniProt records heterochromatin spreading downstream of HMR as the *sas4* disruption phenotype (PMID:16079223).
- **rDNA.** The complex also contributes to rDNA silencing (PMID:11731480).

The apparent "silencing defect" at telomeres in *sas* mutants is therefore best read as an indirect effect: without H4K16ac, SIR proteins spread and are redistributed. The direct role of the complex is anti-silencing boundary formation. The existing "subtelomeric heterochromatin formation" annotation should be read in that light; a boundary or negative-regulation-of-spreading reading fits the mechanism better.

### 4.2 Replication-coupled and genome-wide H4K16 acetylation

- **Recruitment model.** The complex is proposed to be recruited to newly replicated DNA through chromatin assembly factors to acetylate H4K16 (PMID:11731480). The alternative is acetylation of free histones before deposition (PMID:12626510). The two models are not fully reconciled.
- **Timing.** H4K16ac appears in chromatin immediately at replication, and this increase depends entirely on SAS-I. Deposition is delayed at strongly transcribed genes (PMID:34014972, using the Sas4 degron).
- **Distribution.** Loss of Sas2 reduces H4K16ac mainly within open reading frames. The mark is deposited independently of transcription and histone exchange and may impede RNA polymerase II passage through gene bodies ([Heise et al., NAR](https://thebiogrid.org/123548/publication/genome-wide-h4-k16-acetylation-by-sas-i-is-deposited-independently-of-transcription-and-histone-exchange.html)).

## 5. Localization

- **Nucleus.** SAS-I is a nuclear complex (PMID:11731480).
- **Chromatin.** Annotated by IDA from PMID:11731479.
- **Telomeric region.** This annotation is electronic, inferred from the process annotation. Function at subtelomeric boundaries is well supported, but I found no direct evidence that Sas4 is enriched at telomeres.
- **Nuclear import.** Sas2 and Sas5 are imported by the karyopherins Kap123 and Pse1. Sas4 is not a substrate of either, and deleting its putative NLS did not affect its nuclear localization, so the subunits appear to be imported independently and Sas4's route is unknown (PMID:15788653).
- **Abundance.** About 800 molecules per cell in log phase (PMID:14562106, via UniProt).

## 6. Evolution and bioinformatic inference

- Sas4 has two predicted coiled-coil regions (residues 90–120 and 139–160), a predicted disordered region (319–338), and the C-terminal Sas4 domain (PF15460).
- The cullin-homology assignment suggests a scaffold-like fold, consistent with its bridging role. There is no evidence for ubiquitin-ligase function.
- The Sas4 family appears to be fungal-restricted†. The H4K16 acetyltransferase function is conserved in metazoa (MOF/KAT8) but with different accessory subunits†.

## 7. Annotation implications

| Aspect | Best-supported statement | Confidence |
|---|---|---|
| MF | Non-catalytic subunit required for Sas2 H4K16 acetyltransferase activity; bridges Sas2 and Sas5 | High |
| CC | SAS acetyltransferase complex; nucleus; chromatin | High |
| BP | H4K16 acetylation limiting SIR heterochromatin spreading at telomeres, HML and HMR | High |
| BP | Replication-coupled H4K16 acetylation | Moderate to high |
| BP | rDNA silencing | Moderate (single study) |
| Bare "protein binding" rows | Uninformative; the partners indicate complex scaffolding and histone-chaperone association | — |

## 8. Open questions

1. How does Sas4 activate Sas2 (allosteric activation, stabilisation, or substrate presentation)? No structure exists.
2. Is the physiological substrate free H3–H4 before deposition, or newly assembled nucleosomes?
3. How do Asf1 and CAF-I recruit the complex when Asf1-bound histones are refractory to acetylation?
4. How is Sas4 imported into the nucleus?
5. Is H3K14 acetylation by the complex relevant in vivo?

## Sources

- UniProt Q04003: https://www.uniprot.org/uniprotkb/Q04003/entry
- SGD SAS4: https://www.yeastgenome.org/locus/SAS4
- Xu EY et al. (1999) Genetics 153:13–23, PMID:10471696; Genetics 153:25–33, PMID:10471697 (cited via UniProt; not read)
- Osada S et al. (2001) Genes Dev 15:3155–68, PMID:11731479, https://doi.org/10.1101/gad.907201
- Meijsing SH, Ehrenhofer-Murray AE (2001) Genes Dev 15:3169–82, PMID:11731480, https://pubmed.ncbi.nlm.nih.gov/11731480
- Suka N et al. (2002) Nat Genet 32:378–83, PMID:12379856, https://www.yeastgenome.org/reference/12379856
- Sutton A et al. (2003) J Biol Chem 278:16887–92, PMID:12626510, https://www.jbc.org/article/S0021-9258(19)58409-5/fulltext
- Shia WJ et al. (2005) J Biol Chem, "Characterization of the yeast trimeric-SAS acetyltransferase complex", https://www.jbc.org/article/S0021-9258(20)80910-7/fulltext
- Schaper S et al. (2005) J Cell Sci 118:1473–84, PMID:15788653, https://doi.org/10.1242/jcs.01739
- Heise F et al., Nucleic Acids Res, "Genome-wide H4 K16 acetylation by SAS-I is deposited independently of transcription and histone exchange" (author and year from my recollection; title from the BioGRID record), https://thebiogrid.org/123548/publication/genome-wide-h4-k16-acetylation-by-sas-i-is-deposited-independently-of-transcription-and-histone-exchange.html
- Reiter C et al. (2021) PLoS One, PMID:34014972, https://pmc.ncbi.nlm.nih.gov/articles/PMC8136709
- Jambunathan N et al. (2005) Genetics, PMID:16079223 (HMR boundary; cited via UniProt; not read)
- Lambert JP et al. (2010) PMID:21179020; Michaelis AC et al. (2023) Nature, PMID:37968396 (interactomes)
- Pfam PF15460: https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam15460

## Citations

1. https://www.jbc.org/article/S0021-9258(20
2. https://thebiogrid.org/123548/publication/genome-wide-h4-k16-acetylation-by-sas-i-is-deposited-independently-of-transcription-and-histone-exchange.html
3. https://www.uniprot.org/uniprotkb/Q04003/entry
4. https://www.yeastgenome.org/locus/SAS4
5. https://doi.org/10.1101/gad.907201
6. https://pubmed.ncbi.nlm.nih.gov/11731480
7. https://www.yeastgenome.org/reference/12379856
8. https://www.jbc.org/article/S0021-9258(19
9. https://doi.org/10.1242/jcs.01739
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC8136709
11. https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam15460