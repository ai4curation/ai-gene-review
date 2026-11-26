---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-10T01:50:13.869995'
end_time: '2026-11-10T01:51:59.511179'
duration_seconds: 105.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: G6PC2
  gene_symbol: G6PC2
  uniprot_accession: Q9NQR9
  protein_description: 'RecName: Full=Glucose-6-phosphatase 2; Short=G-6-Pase 2; Short=G6Pase
    2; EC=3.1.3.9; AltName: Full=Islet-specific glucose-6-phosphatase catalytic subunit-related
    protein;'
  gene_info: Name=G6PC2; Synonyms=IGRP;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the glucose-6-phosphatase family. .
  protein_domains: Glucose-6-phosphatase. (IPR016275); PAP2/HPO. (IPR000326); PAP2/HPO_sf.
    (IPR036938); PAP2 (PF01569)
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
  web_search_requests: 7
  num_turns: 12
  total_cost_usd: 1.8462392
  session_id: 6a3c7605-68d5-489a-8548-01f1dcb8129c
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 20
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9NQR9
- **Protein Description:** RecName: Full=Glucose-6-phosphatase 2; Short=G-6-Pase 2; Short=G6Pase 2; EC=3.1.3.9; AltName: Full=Islet-specific glucose-6-phosphatase catalytic subunit-related protein;
- **Gene Information:** Name=G6PC2; Synonyms=IGRP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the glucose-6-phosphatase family. .
- **Key Domains:** Glucose-6-phosphatase. (IPR016275); PAP2/HPO. (IPR000326); PAP2/HPO_sf. (IPR036938); PAP2 (PF01569)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "G6PC2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'G6PC2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **G6PC2** (gene ID: G6PC2, UniProt: Q9NQR9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# G6PC2 (Glucose-6-phosphatase catalytic subunit 2; IGRP) — Research Report for Functional Annotation

**Target:** human G6PC2, UniProt Q9NQR9 (synonym IGRP), 355 aa, glucose-6-phosphatase family, PAP2 fold.

## Identity verification

The symbol, organism and family all match the literature retrieved. G6PC2 is the islet-specific paralog of the hepatic/renal glucose-6-phosphatase G6PC1 and the ubiquitous G6PC3. No ambiguity with a different gene was found.

**Sourcing note.** Claims below are tied to the sources I retrieved in this session (search-result abstracts and excerpts, plus the local UniProt record and GOA file). I did not read full texts. Items marked *(from memory, unverified)* were not retrieved in this session and should be checked before being quoted in a review.

## 1. Summary

G6PC2 is a multi-pass endoplasmic reticulum (ER) membrane glucose-6-phosphatase expressed almost exclusively in pancreatic islets. It hydrolyses glucose-6-phosphate (G6P) to glucose and inorganic phosphate (EC 3.1.3.9), with its active site predicted to face the ER lumen.

Its physiological role is not hepatic-style glucose production. In beta cells it opposes glucokinase, creating a glucose/G6P futile cycle that reduces glycolytic flux and raises the glucose threshold for insulin secretion. A 2025 study shows the same mechanism sets the glucose threshold for glucagon suppression in alpha cells.

Human genetics agrees with this: G6PC2 is a major locus for fasting glucose, and loss-of-function coding alleles lower it. The protein is also a major CD8 T-cell autoantigen in the NOD mouse model of type 1 diabetes, which is immunologically important but not a function of the protein.

## 2. Molecular function

### 2.1 Reaction and kinetics

- **Reaction:** D-glucose 6-phosphate + H2O → D-glucose + phosphate (Rhea:16689). UniProt ties this to Petrolonis et al. 2004 (PMID:14722102).
- **Kinetics:** Petrolonis et al. reported Km 0.45 mM and Vmax 32 nmol/mg/min by malachite green assay, and Km 0.29 mM and Vmax 77 nmol/mg/min by a glucose oxidase/peroxidase coupled assay. They concluded IGRP is the major islet glucose-6-phosphatase ([J Biol Chem 2004, PMID:14722102](https://glycosmos.org/pubannotations/14722102)).
- **Low specific activity:** activity is far below that of G6PC1, and it was hard to demonstrate at first.

### 2.2 The early activity controversy

- Martin et al. 2001 (PMID:11297555), who cloned the human and rat genes, could not define a catalytic activity.
- Shieh et al. 2005 reported that IGRP "possesses almost no hydrolase activity", unlike G6Pase-α and G6Pase-β ([Diabetologia 2005](https://link.springer.com/content/pdf/10.1007/s00125-005-1848-6.pdf)).
- A Chou-lab review notes Petrolonis et al. detected a low rate of hydrolysis under somewhat different conditions, and that the methodological source of the discrepancy is unclear ([PMC2785553](https://pmc.ncbi.nlm.nih.gov/articles/PMC2785553)).
- The dispute is now settled by genetics: glucose-6-phosphatase activity and glucose cycling are abolished in G6pc2 knockout islets ([Bosma et al. 2020, PMID:32213654](https://pmc.ncbi.nlm.nih.gov/articles/PMC7331801)).

### 2.3 Catalytic mechanism and structure

No experimental structure was found. Mechanistic understanding comes from the PAP2 family, G6PC1, and an AlphaFold2 model tested by mutagenesis.

- **UniProt features (by similarity or prediction):** His174 as nucleophile, His115 as proton donor, Arg79 and Arg168 as substrate-binding residues, and nine predicted transmembrane helices.
- **AlphaFold2-guided mutagenesis** ([Biosci Rep 2024, PMC10776900](https://pmc.ncbi.nlm.nih.gov/articles/PMC10776900/)):
  - residues forming a predicted intramolecular disulfide bond are essential for protein expression;
  - PAP2-motif residues are critical for enzyme activity;
  - residues lining a predicted substrate cavity modulate activity and substrate specificity;
  - a putative cholesterol-recognition (CRAC) motif influences expression or activity.
- **Conserved residues:** Arg79Gln, Gly114Arg and Ser324Pro reduce activity without affecting expression when tested in mouse G6pc1 as a surrogate ([Boortz et al. 2016, PLoS ONE, PMC5017610](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5017610/)).

### 2.4 Substrate specificity

G6P is the established physiological substrate. The 2024 structure-function paper reports that substrate-cavity residues alter substrate specificity, but I did not retrieve which alternative substrates were tested. Treat anything beyond G6P as unverified.

## 3. Localization and topology

- **ER membrane:** Shieh et al. 2004 showed IGRP is a glycoprotein embedded in the ER membrane (PMID:15044018; title and UniProt annotation only).
- **N-glycosylation:** Asn92 is glycosylated, and the non-glycosylated form is unstable and degraded by the proteasome (UniProt, citing PMID:15044018).
- **Topology:** nine transmembrane helices, with a lumenal N-terminus and cytoplasmic C-terminus, are predicted. The C-terminal residues 352–355 form a predicted ER-retention motif.
- **Functional consequence:** a lumenal active site means G6P must be imported from the cytosol. By analogy with G6PC1, this is expected to be via the G6P translocase SLC37A4. I did not retrieve direct evidence for this coupling in islets.
- **Cell-type expression:**
  - Pancreas-specific, with lower expression in testis; protein is detected in most islet cells (UniProt, citing PMID:11297555).
  - Expression is about 5-fold higher in beta than alpha cells in humans, versus about 20-fold in mice ([PMC10776900](https://pmc.ncbi.nlm.nih.gov/articles/PMC10776900/)).
  - Promoter and enhancer differences likely explain the higher alpha-cell expression in humans ([PMC11439184, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11439184/)).
- **Isoforms:** two truncated splice isoforms (Q9NQR9-2 and -3) lack most of the catalytic domain. Alternative splicing gives differential expression in human thymus and spleen versus pancreas (PMID:16520917), which is relevant to immune tolerance rather than enzymology.

## 4. Biological process: glucose/G6P futile cycling

### 4.1 Beta cells

- **Model:** G6PC2 opposes glucokinase, forming a futile cycle that sets glycolytic flux and therefore the glucose sensitivity of insulin secretion ([O'Brien 2013, Curr Diab Rep, PMC4041587](https://pmc.ncbi.nlm.nih.gov/articles/PMC4041587); [Bosma et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7331801)).
- **Germline knockout mice:** fasting blood glucose falls while fasting insulin is unchanged. In isolated islets, glucose cycling is abolished, glycolysis is elevated, and insulin secretion is enhanced at submaximal but not high glucose ([Bosma et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7331801)).
- **Beta-cell-specific deletion** in adult mice is sufficient to lower fasting glucose without changing fasting insulin ([Bosma et al. 2020, PMID:32213654](https://www.pubmed.gov/32213654/)).
- **Cycling rates:** early radiotracer estimates were very low. A stable-isotope method found much higher rates, abolished in knockout islets (Wall et al. 2015, [PDF](https://www.vanderbilt.edu/younglab/pdf/wall15.pdf); [VUMC summary](https://news.vumc.org/?p=210349)).
- **Metabolic flux:** G6PC2 negatively regulates glucose oxidation and insulin secretion in beta cells ([J Biol Chem 2022, PMC8941207](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8941207/)).

### 4.2 Alpha cells

Alpha-cell-specific deletion in mice shifts the glucose set point for glucagon suppression leftward, with more than half-maximal suppression at 1 mM glucose. Insulin output, islet hormone content and islet structure were unchanged. The effect was confirmed in primary human alpha cells ([Sci Transl Med, January 2025](https://www.science.org/doi/10.1126/scitranslmed.adi6148); [PMC12212188](https://pmc.ncbi.nlm.nih.gov/articles/PMC12212188/)).

### 4.3 What G6PC2 does not do

- UniProt's function text ("may be responsible for glucose production through glycogenolysis and gluconeogenesis") is by-similarity to G6PC1.
- The gluconeogenesis annotations (IBA, IEA, Reactome TAS) follow the same logic. Islet cells are not gluconeogenic glucose exporters, and the knockout phenotype is altered glucose sensing, not impaired glucose production.
- The evolutionary benefit of G6PC2 remains unclear and is unlikely to be its effect on fasting glucose ([O'Brien 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC4041587)).

## 5. Human genetics

- **Fasting glucose locus:** a G6PC2 polymorphism is associated with fasting plasma glucose (Bouatia-Naji et al. 2008, Science, PMID:18451265). UniProt designates the locus FGQTL1 (MIM:612108).
- **Coding variants define the effector gene:** Val219Leu, His177Tyr and Tyr207Ser independently influence fasting glucose. The associated alleles reduce protein abundance through proteasomal degradation, establishing G6PC2 as the effector transcript at the G6PC2–ABCB11 locus ([Mahajan et al. 2015, PLoS Genet, PMC4307976](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4307976/)).
  - Val219Leu is common (minor allele frequency 48.1%), and His177Tyr is low-frequency.
  - Single-variant associations matched the functional data only once haplotype phase was considered.
- **Systematic variant testing:** of 22 nonsynonymous variants, 16 reduced protein expression by more than 50% in 832/13 cells. Four of the remaining six reduced enzyme activity instead ([J Biol Chem 2022, PMC8800118](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8800118/)).
- **Direction of effect:** loss of function lowers fasting glucose in both humans and mice, consistent with the cycling model.
- **GOA experimental rows:** the IMP annotations to glucose homeostasis and regulation of insulin secretion cite PMID:20668700, which I did not retrieve.

## 6. Autoantigen role (not a molecular function)

- IGRP206–214 is an immunodominant CD8 T-cell epitope in NOD mice. T cells recognising it can make up 40–50% of the islet CD8 infiltrate ([PMC3664523](https://pmc.ncbi.nlm.nih.gov/articles/PMC3664523); [JCI 29602](https://www.jci.org/articles/view/29602/files/pdf)).
- IGRP is dispensable for disease: NOD mice lacking G6pc2 develop diabetes with unchanged onset, incidence and sex bias ([PMC3198073](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198073)).
- IGRP-specific T cells do not develop in proinsulin-tolerant NOD mice, so the response appears secondary to proinsulin autoimmunity ([JCI 29602](https://www.jci.org/articles/view/29602/files/pdf)).
- Human epitopes hIGRP228–236 and hIGRP265–273 are recognised in HLA-A*0201-transgenic NOD mice, and T-cell responses to G6PC2 peptides are reported in human type 1 diabetes ([PMC3198073](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198073)).
- The original identification of IGRP as the antigen of the 8.3 T-cell clone is Lieberman et al. 2003, PNAS *(from memory, unverified)*.

## 7. Implications for the existing GO annotations

| Annotation | Evidence in GOA | Assessment |
|---|---|---|
| GO:0004346 glucose-6-phosphatase activity | EXP (PMID:14722102), IBA, IEA | Core molecular function; supported by direct assay and by loss of activity in knockout islets. |
| GO:0005789 ER membrane | TAS (Reactome), IEA | Supported by Shieh et al. 2004 (PMID:15044018); this is where the activity acts. |
| GO:0005783 ER, GO:0016020 membrane | IBA, IEA | Correct; membrane is less specific than ER membrane. |
| GO:0006094 gluconeogenesis | IBA, IEA, Reactome TAS | Family-level inference from G6PC1. Not supported for an islet-restricted enzyme whose demonstrated role is glucose cycling. Likely over-annotation. |
| GO:0042593 glucose homeostasis | IMP (PMID:20668700) | Consistent with knockout and human genetic data. |
| GO:0050796 regulation of insulin secretion | IMP (PMID:20668700) | Consistent; the direction is negative regulation at sub-maximal glucose. |

Possible additions worth evaluating against GO term definitions are a negative-regulation-of-insulin-secretion term and a glucagon-secretion regulation term (from the 2025 alpha-cell study). I did not look up term IDs.

## 8. Open questions

- No experimental structure exists; topology and active-site assignments rest on prediction, homology and mutagenesis.
- Why the specific activity is so low relative to G6PC1, and whether an islet-specific cofactor or the lipid environment (the CRAC motif) modulates it.
- Whether SLC37A4 supplies G6P to G6PC2 in islets.
- The selective advantage of the futile cycle.
- The relative contributions of beta-cell and alpha-cell G6PC2 to human fasting glucose, given the higher alpha-cell expression in humans.

## Sources

- [Petrolonis et al. 2004, J Biol Chem — enzymatic characterization of IGRP (PMID:14722102)](https://glycosmos.org/pubannotations/14722102)
- [Shieh et al. 2005, Diabetologia](https://link.springer.com/content/pdf/10.1007/s00125-005-1848-6.pdf)
- [Chou-lab review (PMC2785553)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2785553)
- [O'Brien 2013, Curr Diab Rep, "Moving on from GWAS" (PMC4041587)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4041587)
- [Wall et al. 2015 — stable isotope glucose cycling](https://www.vanderbilt.edu/younglab/pdf/wall15.pdf) and [VUMC news summary, January 2015](https://news.vumc.org/?p=210349)
- [Mahajan et al. 2015, PLoS Genet (PMC4307976)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4307976/)
- [Boortz et al. 2016, PLoS ONE (PMC5017610)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5017610/)
- [Bosma et al. 2020, J Mol Endocrinol (PMID:32213654)](https://www.pubmed.gov/32213654/); [PMC7331801](https://pmc.ncbi.nlm.nih.gov/articles/PMC7331801)
- [Nonsynonymous SNPs in G6PC2, J Biol Chem 2022 (PMC8800118)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8800118/)
- [G6PC2 negatively regulates glucose oxidation and insulin secretion, J Biol Chem 2022 (PMC8941207)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8941207/)
- [Structural motifs critical for human G6PC2 function, Biosci Rep 2024 (PMC10776900)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10776900/)
- [Promoter and enhancer differences in human versus mouse alpha cells, 2024 (PMC11439184)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11439184/)
- [G6PC2 controls glucagon secretion, Sci Transl Med 2025](https://www.science.org/doi/10.1126/scitranslmed.adi6148); [PMC12212188](https://pmc.ncbi.nlm.nih.gov/articles/PMC12212188/)
- [IGRP epitopes in NOD mice (PMC3664523)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3664523)
- [G6pc2 deletion in NOD mice and human epitopes (PMC3198073)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198073)
- [Proinsulin-tolerant NOD mice, JCI 29602](https://www.jci.org/articles/view/29602/files/pdf)
- [Dos Santos et al. 2006, Diabetologia — alternative splicing (PMID:16520917)](https://link.springer.com/doi/10.1007/s00125-006-0185-8)
- Local files: `genes/human/G6PC2/G6PC2-uniprot.txt` (UniProt Q9NQR9) and `genes/human/G6PC2/G6PC2-goa.tsv`

## Citations

1. https://glycosmos.org/pubannotations/14722102
2. https://link.springer.com/content/pdf/10.1007/s00125-005-1848-6.pdf
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC2785553
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC7331801
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC10776900/
6. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5017610/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC11439184/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC4041587
9. https://www.pubmed.gov/32213654/
10. https://www.vanderbilt.edu/younglab/pdf/wall15.pdf
11. https://news.vumc.org/?p=210349
12. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8941207/
13. https://www.science.org/doi/10.1126/scitranslmed.adi6148
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC12212188/
15. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4307976/
16. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8800118/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC3664523
18. https://www.jci.org/articles/view/29602/files/pdf
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC3198073
20. https://link.springer.com/doi/10.1007/s00125-006-0185-8