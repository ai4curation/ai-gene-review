---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-15T06:58:57.385598'
end_time: '2026-11-15T07:01:10.197304'
duration_seconds: 132.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: HAT2
  gene_symbol: HAT2
  uniprot_accession: P39984
  protein_description: 'RecName: Full=Histone acetyltransferase type B subunit 2;'
  gene_info: Name=HAT2; OrderedLocusNames=YEL056W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the WD repeat RBAP46/RBAP48/MSI1 family.
  protein_domains: Histone-bd_RBBP4-like_N. (IPR022052); WD40/YVTN_repeat-like_dom_sf.
    (IPR015943); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322); WD40_rpt.
    (IPR001680)
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
  web_search_requests: 10
  num_turns: 19
  total_cost_usd: 2.2000209000000006
  session_id: ace37217-8fc3-4955-9bc2-5ccd5a876d94
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P39984
- **Protein Description:** RecName: Full=Histone acetyltransferase type B subunit 2;
- **Gene Information:** Name=HAT2; OrderedLocusNames=YEL056W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the WD repeat RBAP46/RBAP48/MSI1 family.
- **Key Domains:** Histone-bd_RBBP4-like_N. (IPR022052); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322); WD40_rpt. (IPR001680)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HAT2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HAT2** (gene ID: HAT2, UniProt: P39984) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Pulling the cached abstracts for the key HAT2 papers to verify details before writing the report.

# HAT2 (YEL056W; UniProt P39984) in *Saccharomyces cerevisiae*: research report for functional annotation

## 1. Identity verification

The target is unambiguous. HAT2 (YEL056W, SGD:S000000782) encodes a 401-residue WD40-repeat protein of the RbAp46/RbAp48/MSI1 family. The literature retrieved concerns this yeast protein, and the family and domain assignments (WD40 propeller, RBBP4-like N-terminal histone-binding helix) match the published crystal structures (PDB 4PSW, 4PSX, 7XAY). "Hat2" also names orthologous subunits in other fungi, but all primary evidence cited here is from *S. cerevisiae* unless stated.

A note on sourcing: I read abstracts for most primary papers and the full text only for Li et al. 2014. Several claims below rest on search-result summaries rather than the papers themselves, and I flag these where they matter.

## 2. Summary

Hat2 is the non-catalytic, histone-binding regulatory subunit of the type B histone acetyltransferase complex (HAT-B: Hat1–Hat2). With the histone chaperone Hif1 it forms the nuclear NuB4 complex.

- **Primary function:** Hat2 is a WD40 β-propeller scaffold that binds histones. It gives the catalytic subunit Hat1 high-affinity binding to free histone H4, reads the unmodified H3 N-terminal tail, and bridges Hat1 to Hif1.
- **Catalysis:** Hat2 has no catalytic activity. Hat1 acetylates newly synthesised, non-nucleosomal H4 on Lys12 (and Lys5).
- **Location:** Hat2 is found in the cytoplasm and, predominantly, the nucleus.
- **Process:** It acts in the processing and deposition of newly synthesised H3–H4 (replication-independent and repair-linked chromatin assembly). Phenotypes appear in telomeric silencing and DNA double-strand-break repair, mostly when combined with H3-tail mutations.

## 3. Molecular function

### 3.1 Discovery and biochemical role

- Parthun, Widom and Gottschling (1996) purified the predominant cytoplasmic histone acetyltransferase from yeast. It acetylates Lys12 of free H4 but not H4 in chromatin, and contains two proteins, Hat1p and Hat2p.
- Hat1p is the catalytic subunit, with intrinsic specificity for lysine in a GXGKXG motif.
- Hat2p "is required for high affinity binding of the acetyltransferase to histone H4" and is highly related to RbAp48, a CAF-1 subunit that also copurifies with human HDAC1.
- The authors proposed that the Hat2p/RbAp48 family "serve as escorts of histone metabolism enzymes to facilitate their interaction with histone H4" ([PMID:8858151](https://doi.org/10.1016/s0092-8674(00)81325-2), Cell 1996).
- Extracts from either *hat1* or *hat2* mutants lack both the cytoplasmic type B activity and a nuclear free-H4-specific activity ([PMID:9575221](https://doi.org/10.1074/jbc.273.20.12599), J Biol Chem 1998).
- Poveda et al. describe Hat2 as "a protein stimulating Hat1 catalytic activity"; Hif1, by contrast, does not regulate Hat1 activity ([PMID:14761951](https://doi.org/10.1074/jbc.M314228200), J Biol Chem 2004).
- UniProt's curated function note adds that Hat2 alone cannot bind H4 and needs Hat1 for high-affinity interaction with the histone tail.

**Annotation implication:** the "histone acetyltransferase activity" rows on Hat2 (IDA/IMP from PMID:8858151 and PMID:9575221) reflect loss of holoenzyme activity in *hat2Δ* extracts. Hat2 has no acetyltransferase fold; the GNAT catalytic domain is in Hat1. Its role is best described as contributing to the activity of the complex, or as histone binding and adaptor activity.

### 3.2 Structural basis

Li et al. (2014, Genes Dev) solved Hat1p/Hat2p/CoA with an H4 peptide (4PSW, 2.1 Å) and with H4 plus H3 peptides (4PSX, 2.5 Å) ([PMID:24835250](https://doi.org/10.1101/gad.240531.114); [PMC4052767](https://pmc.ncbi.nlm.nih.gov/articles/PMC4052767)).

- **Fold:** Hat2p is a seven-bladed WD40 propeller. Its N-terminal segment forms a helix next to blade 7, and the C-terminus folds back onto that helix.
- **Hat1–Hat2 interface:** Trp197, Tyr199 and Phe205 of Hat1p pack with Leu266, Leu288 and Leu325 of Hat2p in a hydrophobic core that the authors say "appears to be critical for the complex formation". Hat2p Asp308 and Arg282 add hydrogen bonds.
- **H4 recognition:** the H4 tail contacts both subunits.
- **H3 tail reading:** an H3(1–15) peptide binds the Hat1p/Hat2p/H4 complex 1:1 with Kd ≈ 0.34 µM.
  - H3 Arg2 inserts into a small hole in the propeller and hydrogen-bonds Asn212 and Asp213.
  - H3 Lys4 hydrogen-bonds Asn162 and Glu120.
  - H3 Lys9 forms a salt bridge with Glu69.
  - Symmetric or asymmetric dimethylation of Arg2 abolishes binding; H3K4 trimethylation weakens it; H3K9 methylation has a weaker effect.
- **Interpretation:** Hat2 acts as a reader of unmodified H3 N-termini. This offers a mechanism for selecting newly synthesised H3–H4 over parental, modified histones.

Yue et al. (2022, Genes Dev) solved a 3.3 Å structure of yeast Hat1ΔC–Hat2 bound to Asf1–H3–H4 and CoA (PDB 7XAY; Asf1 from *Aspergillus fumigatus*) ([PMC9067401](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401); [Genes Dev 36:408](https://genesdev.cshlp.org/content/36/7-8/408.full)).

- The histone-fold core domains of H3 and H4 contact Hat1 and Hat2.
- The H3 N-terminal tail makes extensive contact with Hat2.
- The H4 N-terminal helix (αN) binds Hat2 in a new mode.
- The complex is equimolar, consistent with HAT-B acting on an Asf1-bound H3–H4 heterodimer.
- No structure including Hif1 turned up in my searches.

### 3.3 Adaptor role in NuB4

- Two-hybrid interactions of Hif1 with Hat1 and with H4 depend on *HAT2*. Fractionation and co-immunoprecipitation show a heterotrimeric complex "in which Hat2 bridges Hat1 and Hif1 proteins" ([PMID:14761951](https://doi.org/10.1074/jbc.M314228200)).
- Ai and Parthun (2004) isolated the nuclear Hat1p/Hat2p complex and found it copurifies with Hif1p (YLL022C), an H3/H4-selective chaperone and chromatin assembly factor.
- In vivo the nuclear complex is bound to acetylated H4 and H3, and "the association of Hif1p with acetylated H4 requires Hat1p and Hat2p" ([PMID:15099519](https://doi.org/10.1016/s1097-2765(04)00184-4), Mol Cell 2004).
- Hif1 also exists in complexes independent of Hat1 and Hat2 (Ge et al. 2011, [PMC3089522](https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522)).

## 4. Biological process

### 4.1 Processing of newly synthesised histones for chromatin assembly

- HAT-B acetylates free H4 at Lys12, and to a lesser extent Lys5; this is the conserved diacetylation mark of new H4 ([PMID:14761951](https://doi.org/10.1074/jbc.M314228200)).
- In current models, acetylation occurs on Asf1-bound H3–H4 before import. H4 tail diacetylation is proposed to weaken the Kap123–H4 NLS interaction (2017 eLife model, summarised in the review "Nuclear import of histones", [PMC7752055](https://pmc.ncbi.nlm.nih.gov/articles/PMC7752055)).
- The complex then travels with the histones into the nucleus, where Hif1 joins and the histones are handed to assembly factors ([PMID:15099519](https://doi.org/10.1016/s1097-2765(04)00184-4); [PMC9067401](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401)). Yue et al. note that the mechanism of transfer from NuB4 to Asf1 is still unknown.
- A 2023 review covers conserved Hat1 roles in H3–H4 import, replication-fork stability and replication-coupled assembly ([Genes 14:915](https://www.mdpi.com/2073-4425/14/4/915)).

### 4.2 Telomeric silencing

- Deleting *HAT1* or *HAT2* alone gives no obvious phenotype and no change in telomeric silencing.
- Combined with Lys-to-Arg mutations in the H3 tail (especially K14), *hat1Δ* or *hat2Δ* causes a significant silencing defect.
- The effect is mediated solely through H4 K12 ([PMID:10982821](https://pmc.ncbi.nlm.nih.gov/articles/PMC86239), Mol Cell Biol 2000).
- Hat1 catalytic activity and nuclear localisation are both required (Mersfelder and Parthun 2008, PMID:18753131; from a search summary).
- This is best read as an indirect consequence of defective deposition of correctly acetylated H3–H4, not a direct heterochromatin-specific role. The "subtelomeric heterochromatin formation" annotations therefore describe a downstream, redundancy-masked phenotype.

### 4.3 DNA double-strand-break repair

- *hif1Δ* and *hat1Δ* strains show similar defects in telomeric silencing and double-strand-break repair ([PMID:15099519](https://doi.org/10.1016/s1097-2765(04)00184-4)).
- Hat1p and Hif1p are recruited to a small domain around an HO-induced break (Qin and Parthun 2006, [PMC1447429](https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429)).
- NuB4 subunits contribute unequally to repair-linked chromatin reassembly, with Hif1 playing a larger role than Hat1 or Hat2 (Ge, Wang and Parthun 2011, [PMC3089522](https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522)).
- I found no direct evidence that Hat2 itself is recruited to breaks.

### 4.4 Other reported links

- **Replication origins:** a Hat1p/Hat2p sub-complex associates physically and functionally with the origin recognition complex. Deleting *HAT1* or *HAT2* worsens the growth defects of *orc-ts* mutants, and Hat1p associates dynamically with chromatin in S phase (Suter et al. 2007, [PMC2140264](https://pmc.ncbi.nlm.nih.gov/articles/PMC2140264)).
- **Lifespan:** *hat2Δ* and *hat1Δ hat2Δ*, but not *hat1Δ*, have extended lifespan, and the single-mutant transcriptomes differ. The authors suggest Hat2p may have functions beyond Hat1p's (Rosaleny et al. 2005, PMID:16023114, [FEBS Lett](https://doi.org/10.1016/j.febslet.2005.06.028)). The mechanism is undefined.
- **Expression:** UniProt records repression by farnesol (PMID:10075411).

## 5. Localisation

- Hat2 was first isolated with the cytoplasmic type B activity ([PMID:8858151](https://doi.org/10.1016/s0092-8674(00)81325-2)).
- Nuclear and cytoplasmic complexes both depend on *HAT1* and *HAT2*; the cytoplasmic complex is about 150 kDa and the nuclear one about 110 kDa ([PMID:9575221](https://doi.org/10.1074/jbc.273.20.12599)).
- Immunofluorescence of tagged Hat1, Hat2 and Hif1 shows "all three HAT-B proteins are mainly localized in the nucleus". The authors propose that type A and type B enzymes be distinguished by substrate (nucleosomal versus free histones), not by location ([PMID:14761951](https://doi.org/10.1074/jbc.M314228200)).
- The UniProt function note states that Hat2 is required for the nuclear location of Hat1. I could not confirm this from the Poveda abstract; it would need the full text.
- "Chromosome, telomeric region" is an electronic inference from the silencing process term. I found no direct evidence that Hat2 resides at telomeres.

## 6. Evolution and paralogy

Yeast has three members of the RbAp46/48 family, each in a different complex:

| Protein | Complex | Source |
|---|---|---|
| Hat2 | HAT-B / NuB4 | Papers above |
| Msi1 (Cac3) | CAF-1 | Family knowledge; not verified in this search |
| Ume1 | Rpd3L histone deacetylase | Carrozza et al. 2005, [PMID:16314178](https://www.yeastgenome.org/reference/16314178) |

- The Rpd3L subunit list from Carrozza et al. (Rpd3, Sin3, Sds3, Pho23, Dep1, Rxt2, Rxt3, Sap30, Cti6, Ash1, Ume1, Ume6) does not include Hat2.
- A 2023 cryo-EM study describes Ume1 as the histone chaperone of Rpd3L, present in two copies ([Nat Commun 2023](https://www.nature.com/articles/s41467-023-38687-z.pdf)).
- Mammalian RbAp46 (RBBP7) is the Hat2 counterpart in the HAT1 holoenzyme, while RbAp46/48 also serve in CAF-1, NuRD, Sin3 and PRC2. Yeast has split these roles among paralogs.
- **Annotation implication:** the phylogenetic (IBA) annotations placing Hat2 in the "Rpd3L complex" and "Rpd3L-Expanded complex", and probably "regulation of DNA-templated transcription", look like over-propagation from Ume1 and the multifunctional metazoan orthologs. No yeast experiment I found supports them for Hat2.

## 7. Conclusions for annotation

| Aspect | Best-supported statement | Key evidence |
|---|---|---|
| Molecular function | Histone binding (H4 tail and αN helix; unmodified H3 tail); adaptor bridging Hat1 and Hif1; contributes to, but does not catalyse, H4 K5/K12 acetylation | PMID:8858151, 14761951, 24835250; PMC9067401 |
| Complex | Hat1–Hat2 (HAT-B); Hat1–Hat2–Hif1 (NuB4) | PMID:8858151, 14761951, 15099519 |
| Process | Acetylation and handling of newly synthesised H3–H4 for chromatin assembly; indirect roles in telomeric silencing and repair-linked reassembly | PMID:10982821, 15099519; PMC3089522 |
| Location | Nucleus (predominant) and cytoplasm | PMID:9575221, 14761951 |
| Doubtful | Rpd3L membership; direct transcription regulation; intrinsic acetyltransferase activity; telomere residence | Section 6; Section 3.1 |

**Open questions:**
- How Hat2's H3-tail reading is coordinated with Asf1 and Hif1 during hand-off.
- Whether Hat2 has Hat1-independent functions, as the lifespan result suggests.
- The stoichiometry and structure of intact NuB4.

## Sources

- Parthun et al. 1996, Cell 87:85. PMID:8858151. https://doi.org/10.1016/s0092-8674(00)81325-2
- Ruiz-García et al. 1998, J Biol Chem 273:12599. PMID:9575221. https://doi.org/10.1074/jbc.273.20.12599
- Kelly et al. 2000, Mol Cell Biol 20:7051. PMID:10982821. https://pmc.ncbi.nlm.nih.gov/articles/PMC86239
- Poveda et al. 2004, J Biol Chem 279:16033. PMID:14761951. https://doi.org/10.1074/jbc.M314228200
- Ai and Parthun 2004, Mol Cell 14:195. PMID:15099519. https://doi.org/10.1016/s1097-2765(04)00184-4
- Rosaleny et al. 2005, FEBS Lett. PMID:16023114. https://doi.org/10.1016/j.febslet.2005.06.028
- Carrozza et al. 2005. PMID:16314178. https://www.yeastgenome.org/reference/16314178
- Qin and Parthun 2006. https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429
- Suter et al. 2007, BMC Biol 5:38. PMID:17880717. https://pmc.ncbi.nlm.nih.gov/articles/PMC2140264
- Ge, Wang and Parthun 2011, J Biol Chem. PMID:21454479. https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522
- Li et al. 2014, Genes Dev 28:1217. PMID:24835250. https://pmc.ncbi.nlm.nih.gov/articles/PMC4052767 ; https://genesdev.cshlp.org/content/28/11/1217.abstract ; https://rcsb.org/structure/4psx
- Yue et al. 2022, Genes Dev 36:408. https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401 ; https://genesdev.cshlp.org/content/36/7-8/408.full
- "Nuclear import of histones", Biochem Soc Trans 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7752055
- "Understanding HAT1: A Comprehensive Review of Noncanonical Roles and Connection with Disease", Genes 2023, 14:915. https://www.mdpi.com/2073-4425/14/4/915
- Rpd3L cryo-EM structure, Nat Commun 2023. https://www.nature.com/articles/s41467-023-38687-z.pdf
- UniProt P39984 and SGD HAT2. https://www.yeastgenome.org/locus/HAT2

## Citations

1. https://doi.org/10.1016/s0092-8674(00
2. https://doi.org/10.1074/jbc.273.20.12599
3. https://doi.org/10.1074/jbc.M314228200
4. https://doi.org/10.1101/gad.240531.114
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC4052767
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC9067401
7. https://genesdev.cshlp.org/content/36/7-8/408.full
8. https://doi.org/10.1016/s1097-2765(04
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3089522
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC7752055
11. https://www.mdpi.com/2073-4425/14/4/915
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC86239
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC1447429
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC2140264
15. https://doi.org/10.1016/j.febslet.2005.06.028
16. https://www.yeastgenome.org/reference/16314178
17. https://www.nature.com/articles/s41467-023-38687-z.pdf
18. https://genesdev.cshlp.org/content/28/11/1217.abstract
19. https://rcsb.org/structure/4psx
20. https://www.yeastgenome.org/locus/HAT2