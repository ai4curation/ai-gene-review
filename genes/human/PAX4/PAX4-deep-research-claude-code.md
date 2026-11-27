---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-10T01:50:13.837731'
end_time: '2026-11-10T01:52:08.537326'
duration_seconds: 114.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PAX4
  gene_symbol: PAX4
  uniprot_accession: O43316
  protein_description: 'RecName: Full=Paired box protein Pax-4 {ECO:0000305};'
  gene_info: Name=PAX4 {ECO:0000303|PubMed:9439631, ECO:0000312|HGNC:HGNC:8618};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the paired homeobox family. .
  protein_domains: HD. (IPR001356); Homeobox_CS. (IPR017970); Homeodomain-like_sf.
    (IPR009057); PAIRED_DNA-bd_site. (IPR043182); Paired_dom. (IPR001523)
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
  web_search_requests: 14
  num_turns: 17
  total_cost_usd: 2.0764321999999997
  session_id: 9bc5441f-587a-4734-9be3-27787edc62e8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O43316
- **Protein Description:** RecName: Full=Paired box protein Pax-4 {ECO:0000305};
- **Gene Information:** Name=PAX4 {ECO:0000303|PubMed:9439631, ECO:0000312|HGNC:HGNC:8618};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the paired homeobox family. .
- **Key Domains:** HD. (IPR001356); Homeobox_CS. (IPR017970); Homeodomain-like_sf. (IPR009057); PAIRED_DNA-bd_site. (IPR043182); Paired_dom. (IPR001523)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PAX4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PAX4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PAX4** (gene ID: PAX4, UniProt: O43316) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PAX4 (human, UniProt O43316): Research Report for Functional Annotation

## 1. Identity verification

The target is unambiguous. "PAX4" is the HGNC symbol for the human paired box 4 gene on chromosome 7q32, encoding Paired box protein Pax-4 (O43316), a member of the paired homeobox family. Its N-terminal paired domain (UniProt DNA_BIND 5–131) and paired-type homeodomain (170–229) match the literature, which is entirely about this protein and its rodent, zebrafish and pig orthologs. No conflicting use of the symbol was found.

A note on evidence: much of the mechanism comes from mouse/rat Pax4 (P32115). Direct human evidence exists for intestinal organoids, hiPSC-derived islets, EndoC-βH1 cells, human islets and disease variants, and is flagged as such below.

## 2. Summary

PAX4 is a nuclear, sequence-specific DNA-binding transcription factor that acts mainly as a transcriptional repressor. It functions transiently in endocrine progenitors of the pancreas and gut as a lineage-allocation switch:

- **Pancreas:** it promotes the β-cell fate (and δ-cell fate in mouse) and suppresses the α-cell programme, largely through mutual repression with the homeobox factor ARX.
- **Intestine:** it drives enterochromaffin (serotonin) cell differentiation and suppresses ARX-dependent enteroendocrine subtypes.
- **Adult β cells:** a secondary, lower-level role in proliferation and survival under stress.

Loss-of-function or hypomorphic human variants cause or predispose to diabetes (MODY9, ketosis-prone diabetes, East Asian type 2 diabetes).

## 3. Molecular function

### 3.1 DNA binding

- PAX4 binds a bipartite element: a homeodomain site and a paired-domain site separated by about 15 nucleotides. These elements overlap PAX6 sites in islet hormone genes (Smith et al. 1999, Mol Cell Biol; [PMC84911](https://pmc.ncbi.nlm.nih.gov/articles/PMC84911)).
- It binds a common element in the glucagon, insulin and somatostatin promoters, and competes with the activator PAX6 for it (UniProt O43316 function text, by similarity to mouse P32115).
- GOA carries an IDA for sequence-specific double-stranded DNA binding (GO:1990837, ARUK-UCL) on the human protein.

### 3.2 Active transcriptional repression

- In an α-cell line, PAX4 repressed the glucagon and insulin promoters. A GAL4–PAX4 fusion also repressed, so the effect is active repression and not only competition with PAX6. Repression mapped to more than one region, with the homeodomain and C-terminal portion strongest (Smith et al. 1999; [PMC84911](https://pmc.ncbi.nlm.nih.gov/articles/PMC84911)).
- A companion paper identified a portable repression domain and an E1A-responsive activation domain in Pax4 (Mol Cell Biol 1999, 19:8281–8291; I recall this as Fujitani et al., but the search did not confirm the authors).
- Stable PAX4 expression in a rat glucagon-producing line completely silenced the endogenous glucagon gene, and PAX4 repressed the insulin promoter independently of PAX6 (Petersen et al. 2000; [abstract](https://researchprofiles.ku.dk/en/publications/pax4-represses-pancreatic-glucagon-gene-expression/)).
- For the human protein, GOA has an IDA for DNA-binding transcription repressor activity, RNA polymerase II-specific (GO:0001227), from the ZNF800 study (PMID:37883554).

### 3.3 Context-dependent activation

Pax4 transactivated the Bcl-xL and c-myc promoters in reporter assays, and the diabetes-linked R121W mutant was less efficient (Brun et al. 2004, J Cell Biol 167:1123; PMID:15596543; [article](https://rupress.org/jcb/article/167/6/1123/51557/The-diabetes-linked-transcription-factor-PAX4)). Whether Bcl-xL is a direct binding target is unresolved, so "repressor" is the well-supported primary activity and activation is secondary.

### 3.4 Target genes

| Target | Effect | Evidence | Directness |
|---|---|---|---|
| ARX | Repression | Mouse genetics; binding to a cis-element about 14.2 kb downstream of the Arx stop codon ([PMC3083195](https://pmc.ncbi.nlm.nih.gov/articles/PMC3083195)); human organoids | Direct in mouse pancreas; possibly indirect in human gut (see 4.2) |
| Glucagon (GCG) | Repression | Reporter assays, stable expression | Promoter binding shown |
| Insulin (INS) | Repression in reporter assays | Reporter assays | Promoter binding shown; physiological meaning unclear |
| Ghrelin | Repression | ChIP and mutated-reporter assays in zebrafish; repressed target in mouse | Direct in zebrafish only |
| MafA | Repression | Mouse | Direct or indirect not established |
| Bcl-xL, c-myc, Id2 | Activation | Adenoviral overexpression in rat and human islets | Uncertain |

### 3.5 Isoforms

Isoform 2 (PAX4v, lacking exon 7) was found in human insulinoma. It reversed wild-type PAX4-mediated repression of the insulin promoter in co-transfection, consistent with a dominant-negative form (Miyamoto et al. 2001; PMID:11263967; [record](https://ouci.dntb.gov.ua/works/40OG3G37)).

## 4. Biological processes

### 4.1 Pancreatic endocrine cell fate (primary role)

**Mouse loss of function.** Pax4-null mice lack mature insulin-producing β cells and somatostatin-producing δ cells, and have greatly increased numbers of glucagon-producing α cells. Pax4 is expressed early in a subset of endocrine progenitors and later restricted to β cells (Sosa-Pineda et al. 1997, Nature 386:399; I recall PMID:9121556 — one search summary gave a different PMID, so verify before citing).

**Cross-repression with ARX.** Arx and Pax4 each repress the other's expression, and this allocates endocrine fates. Double mutants lose mature α and β cells and produce almost exclusively somatostatin cells (Collombat et al. 2005, Development; PMID:15930104). This shows Pax4 is not strictly required for δ-cell genesis, revising the 1997 interpretation.

**Gain of function.** Ectopic Pax4 forces endocrine precursors and mature α cells to adopt a β-cell identity. The resulting glucagon deficiency triggers continuous α-cell neogenesis, which can restore β-cell mass in chemically diabetic mice (Collombat et al. 2009, Cell; [abstract](https://hdl.handle.net/11858/00-001M-0000-0015-8811-C)). A later study from the same group found Pax4 dispensable for α-to-β-like conversion triggered by Arx loss, making Arx the main trigger ([PLoS Genetics 2013](https://doaj.org/article/4e3a977952b4450ba86d5e7735490859)).

**Human evidence.** Lau et al. 2023 (Nat Commun 14:6119; [article](https://www.nature.com/articles/s41467-023-41860-z)):

- PAX4 knockout in hiPSC-derived islets did not ablate β cells. It produced compromised β cells with more polyhormonal cells, less insulin, derepressed α-cell genes and reduced maturation genes.
- Lines carrying risk alleles showed the same phenotype, reversed by gene correction.
- PAX4 knockdown in EndoC-βH1 cells impaired insulin secretion and reduced insulin content.
- The authors conclude PAX4 is not essential for in vitro differentiation to stem-cell islets, but haploinsufficiency and loss-of-function alleles raise diabetes risk by biasing precursors toward an α-cell fate.

A 2026 Nature Communications paper using an ARX/PAX4 dual-reporter iPSC line reports the same direction of effect ([article](https://www.nature.com/articles/s41467-026-75255-7)). Constitutive PAX4 expression in human ESCs increases their propensity to form β-like cells ([PMC2262135](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2262135/)).

**Other species.** In zebrafish, pax4 knockdown increases α cells through arx derepression without affecting β or δ cells ([PMC3563606](https://pmc.ncbi.nlm.nih.gov/articles/PMC3563606)). A 2026 study reports that PAX4-knockout piglets develop severe hyperglycaemia within 24 hours and die by day 3 ([summary](https://www.citedrive.com/en/discovery/functional-inactivation-of-pax4-results-in-disrupted-endocrine-pancreas-development-and-neonatal-diabetes-in-pigs/)).

The requirement for β-cell genesis is therefore strict in mouse and pig, weaker in human in vitro models, and absent in zebrafish. The conserved core is repression of ARX and the α-cell programme.

### 4.2 Intestinal enteroendocrine differentiation (direct human evidence)

- A CRISPR screen of all transcription factors in adult human small-intestine organoids identified ZNF800 as a repressor of enteroendocrine commitment that acts through a PAX4-centred network (Lin et al. 2023, Science 382:451–458; PMID:37883554; [record](https://pure.prinsesmaximacentrum.nl/en/publications/unbiased-transcription-factor-crispr-screen-identifies-znf800-as-/)).
- ZNF800 knockout raised enteroendocrine cells from about 1% to about 15%, mostly enterochromaffin cells. PAX4 is a direct ZNF800 target, and PAX4 knockout reversed the effect, shifting cells from enterochromaffin to other subtypes including L cells ([2024 commentary by the authors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10819080/)).
- PAX4 inhibits ARX unilaterally in this system. ARX is needed for L, G, I and N cells. ChIP-qPCR reportedly found no direct PAX4–ARX interaction in enteroendocrine cells, so repression there may be indirect. I only saw this through the commentary, not the primary paper.
- Mouse data agree: Pax4 mutants have impaired serotonin, somatostatin, GIP and gastrin cell differentiation, with more GLP-1 L cells and Arx upregulation (Beucher et al. 2012, PLoS One; PMID:22570716; [PMC3343025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3343025/)).

### 4.3 Adult β-cell proliferation and survival (secondary)

- Adenoviral Pax4 overexpression increased β-cell proliferation about 3.5-fold in rat and human islets and raised Bcl-xL, c-myc and Id2 mRNA (Brun et al. 2004; PMID:15596543).
- Activin A and betacellulin induced Pax4 transcription and β-cell proliferation in rat islets; PI3-kinase inhibition nearly abolished betacellulin-induced Pax4 expression.
- Bcl-xL induction altered mitochondrial calcium and ATP production and impaired glucose-induced insulin secretion, so overexpression has a functional cost.
- In adults, Pax4 expression is limited to a subset of β cells able to proliferate under increased metabolic demand (Ko, Fonseca & Wu 2023, Int J Mol Sci; [PMC10179455](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10179455/)).

These are largely overexpression data and should be treated as non-core relative to the developmental fate-switch role.

### 4.4 Retina and pineal gland (expression only)

In rat, Pax4 mRNA is strongly expressed in the pineal gland and in retinal photoreceptors, with a diurnal rhythm peaking in the light period. The nocturnal fall in pineal expression depends on sympathetic input and cAMP (Rath et al. 2009, Endocrinology; [PMC2646524](https://pmc.ncbi.nlm.nih.gov/articles/PMC2646524)). I found no loss-of-function evidence for a PAX4 role in retina or brain development. The existing IBA annotations to brain, forebrain, retina and sensory organ development probably reflect PAX6-clade biology and deserve scrutiny for PAX4.

## 5. Localization

- PAX4 acts in the nucleus on chromatin, consistent with its DNA-binding function. UniProt lists nucleus and chromosome by similarity to mouse; Reactome gives nucleoplasm (TAS).
- I did not find a dedicated localization experiment on endogenous human PAX4 in these searches; the nuclear assignment rests on function, orthology and reporter and ChIP assays.
- Cell-type context: transient expression in NEUROG3-lineage endocrine progenitors of fetal pancreas and intestinal epithelium, low expression in a subset of adult β cells, and high expression in insulinomas.

## 6. Pathway context

- **Upstream:** PAX4 is induced in late NEUROG3-positive endocrine progenitors. In human gut it is directly repressed by ZNF800 (PMID:37883554). In adult islets it is induced by activin A and betacellulin through PI3-kinase.
- **Core circuit:** a PAX4–ARX mutual-repression toggle. PAX4 dominance gives β cells (pancreas) or enterochromaffin cells (gut). ARX dominance gives α cells or L, G, I and N cells.
- **Downstream:** repression of glucagon, ghrelin and ARX; indirect support of the β-cell programme.

## 7. Human disease genetics

| Variant | Phenotype | Functional evidence | Source |
|---|---|---|---|
| R121W (paired domain) | Type 2 diabetes in Japanese, homozygous carriers | Reduced transactivation of Bcl-xL and c-myc promoters | Shimajiri et al. 2001, PMID:11723072; Brun 2004 |
| R133W | Ketosis-prone diabetes, West African ancestry; homozygotes in 4% of cases, none in 355 controls | — | Mauvais-Jarvis et al. 2004, PMID:15509590 ([paper](https://zendy.io/pdf-viewer/10.1093/hmg/ddh341)) |
| R164W, IVS7-1G>A | MODY9 in Thai families | R164W segregates and impairs repression of insulin and glucagon promoters | Plengvidhya et al. 2007, PMID:17426099 ([record](https://repository.li.mahidol.ac.th/handle/123456789/24289)) |
| R192H (rs2233580, homeodomain) | East Asian type 2 diabetes, odds ratio about 1.75; lower β-cell function in non-diabetic carriers | hiPSC islets show more polyhormonal cells and less insulin | Lau et al. 2023 |
| Y186X | Early-onset diabetes, Singapore family | Protein-truncating | Lau et al. 2023 |

All the functionally tested variants reduce PAX4 activity, supporting a loss-of-function or haploinsufficiency mechanism. The R192H association is robust; the MODY9 designation rests on few families.

## 8. Implications for annotation

- **Core molecular function:** DNA-binding transcription repressor activity, RNA polymerase II-specific (GO:0001227), with cis-regulatory sequence-specific DNA binding. This has direct human IDA support.
- **Core processes:** type B pancreatic cell differentiation (mouse genetics, human hiPSC support); intestinal enterochromaffin cell differentiation and negative regulation of other enteroendocrine fates (human IDA); negative regulation of α-cell differentiation through ARX repression.
- **Location:** nucleus/chromatin.
- **Likely over-annotations:** brain, forebrain, retina and sensory organ development (IBA), and the vague "animal organ morphogenesis" (TAS).
- **Open questions:** the genome-wide direct targets of human PAX4; whether ARX repression is direct in human cells; the co-repressors recruited by the homeodomain/C-terminal repression domain; and why human β-cell genesis tolerates PAX4 loss better than mouse.

## Sources

- [Smith et al. 1999, Mol Cell Biol — PAX4 as transcriptional repressor (PMC84911)](https://pmc.ncbi.nlm.nih.gov/articles/PMC84911)
- [Petersen et al. 2000 — Pax4 represses pancreatic glucagon gene expression](https://researchprofiles.ku.dk/en/publications/pax4-represses-pancreatic-glucagon-gene-expression/)
- [Brun et al. 2004, J Cell Biol — PAX4 promotes β-cell proliferation and survival](https://rupress.org/jcb/article/167/6/1123/51557/The-diabetes-linked-transcription-factor-PAX4)
- [Collombat et al. 2009, Cell — ectopic Pax4 converts progenitors and α cells to β cells](https://hdl.handle.net/11858/00-001M-0000-0015-8811-C)
- [Collombat et al. 2005, Development — Arx/Pax4 double mutants (PMID:15930104)](https://searchworks.jioinstitute.edu.in/articles/cmedm__15930104)
- [PLoS Genetics 2013 — Pax4 dispensable for Arx-loss-driven conversion](https://doaj.org/article/4e3a977952b4450ba86d5e7735490859)
- [Arx regulatory element bound by Pax4 (PMC3083195)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3083195)
- [Djiotsa et al. 2012 — zebrafish pax4 and arx (PMC3563606)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3563606)
- [Lau et al. 2023, Nat Commun — PAX4 loss of function and human endocrine development](https://www.nature.com/articles/s41467-023-41860-z)
- [bioRxiv preprint of Lau et al.](https://www.biorxiv.org/content/10.1101/2022.05.15.491987v1.full)
- [Nat Commun 2026 — human α versus β fate allocation](https://www.nature.com/articles/s41467-026-75255-7)
- [PAX4 enhances β-cell differentiation of human ESCs (PMC2262135)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2262135/)
- [Lin et al. 2023, Science — ZNF800 screen (institutional record)](https://pure.prinsesmaximacentrum.nl/en/publications/unbiased-transcription-factor-crispr-screen-identifies-znf800-as-/)
- [Lin et al. 2024, Clin Transl Med commentary (PMC10819080)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10819080/)
- [Beucher et al. 2012, PLoS One — Arx and Pax4 in enteroendocrine specification (PMC3343025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3343025/)
- [Ko, Fonseca & Wu 2023 — Pax4 in Health and Diabetes (PMC10179455)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10179455/)
- [Brun & Gauthier 2008 review — Pax4 in mature β-cell expansion and survival](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_70252963)
- [Miyamoto et al. 2001 — dominant-negative PAX4 in human insulinoma](https://ouci.dntb.gov.ua/works/40OG3G37)
- [Mauvais-Jarvis et al. 2004, Hum Mol Genet — PAX4 and ketosis-prone diabetes](https://zendy.io/pdf-viewer/10.1093/hmg/ddh341)
- [Plengvidhya et al. 2007 — PAX4 mutations in Thai MODY](https://repository.li.mahidol.ac.th/handle/123456789/24289)
- [Rath et al. 2009, Endocrinology — Pax4 in rat pineal and retina (PMC2646524)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2646524)
- [Pig PAX4 knockout, 2026](https://www.citedrive.com/en/discovery/functional-inactivation-of-pax4-results-in-disrupted-endocrine-pancreas-development-and-neonatal-diabetes-in-pigs/)
- UniProt O43316 record and GOA annotations (local files `genes/human/PAX4/PAX4-uniprot.txt`, `PAX4-goa.tsv`)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC84911
2. https://researchprofiles.ku.dk/en/publications/pax4-represses-pancreatic-glucagon-gene-expression/
3. https://rupress.org/jcb/article/167/6/1123/51557/The-diabetes-linked-transcription-factor-PAX4
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC3083195
5. https://ouci.dntb.gov.ua/works/40OG3G37
6. https://hdl.handle.net/11858/00-001M-0000-0015-8811-C
7. https://doaj.org/article/4e3a977952b4450ba86d5e7735490859
8. https://www.nature.com/articles/s41467-023-41860-z
9. https://www.nature.com/articles/s41467-026-75255-7
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2262135/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3563606
12. https://www.citedrive.com/en/discovery/functional-inactivation-of-pax4-results-in-disrupted-endocrine-pancreas-development-and-neonatal-diabetes-in-pigs/
13. https://pure.prinsesmaximacentrum.nl/en/publications/unbiased-transcription-factor-crispr-screen-identifies-znf800-as-/
14. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10819080/
15. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3343025/
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10179455/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC2646524
18. https://zendy.io/pdf-viewer/10.1093/hmg/ddh341
19. https://repository.li.mahidol.ac.th/handle/123456789/24289
20. https://searchworks.jioinstitute.edu.in/articles/cmedm__15930104
21. https://www.biorxiv.org/content/10.1101/2022.05.15.491987v1.full
22. https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_70252963