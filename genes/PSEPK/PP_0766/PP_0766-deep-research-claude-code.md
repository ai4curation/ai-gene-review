---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:12:16.034434'
end_time: '2026-10-30T21:17:10.006715'
duration_seconds: 293.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0766
  gene_symbol: PP_0766
  uniprot_accession: Q88PT2
  protein_description: 'RecName: Full=DUF1329 domain-containing protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_0766 {ECO:0000313|EMBL:AAN66391.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DUF1329. (IPR010752); DUF1329 (PF07044)
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 17
  total_cost_usd: 1.10703283
  session_id: 4507e4df-991f-4f15-ac8c-2db38ce89dfc
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 11
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88PT2
- **Protein Description:** RecName: Full=DUF1329 domain-containing protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_0766 {ECO:0000313|EMBL:AAN66391.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF1329. (IPR010752); DUF1329 (PF07044)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0766" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0766' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0766** (gene ID: PP_0766, UniProt: Q88PT2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking the gene neighbourhood and fitness data, then searching for any studies of the DUF1329/DUF1302 pair.

Fetching the full text of the two key papers (the RB-TnSeq study and the Foldy structural analysis).

# PP_0766 (Q88PT2) in *Pseudomonas putida* KT2440: research report

## Summary

PP_0766 is a 454-residue protein with an N-terminal signal peptide and a DUF1329 (PF07044, IPR010752) domain. It has not been characterised biochemically. Three lines of evidence point the same way:

- **Mutant fitness.** Transposon mutants of PP_0766, and of its partner gene PP_0765 (a DUF1302 protein), grow poorly specifically when the carbon source is a fatty-acid ester (Tween 20 or butyl stearate). The free fatty acids give no such defect (Thompson et al., 2020).
- **Protein features.** PP_0766 has a predicted cleavable signal peptide and is classified in a LolA-like fold.
- **Structure prediction.** AlphaFold co-folding predicts that it contacts PP_0765, a predicted outer-membrane β-barrel, and PP_2019, an RND/MMPL-family inner-membrane transporter (Roberts et al., 2024).

The best current model is that PP_0766 is a **periplasmic LolA-like carrier in a three-part system that moves a fatty-acyl or hydrophobic substrate across the cell envelope**. That system would be PP_2019 in the inner membrane, PP_0766 in the periplasm and PP_0765 in the outer membrane. An older hypothesis, that the DUF1302/DUF1329 pair is itself an esterase, has not been tested. Neither the substrate nor the direction of transport is known.

## 1. Identity check

| Feature | Value | Source |
|---|---|---|
| Accession / locus | Q88PT2 / PP_0766 (EMBL AAN66391.1; RefSeq WP_010952007.1) | UniProt Q88PT2 (unreviewed, PE 4: Predicted) |
| Length | 454 aa, about 50.6 kDa | UniProt |
| Signal peptide | Residues 1–24; mature chain 25–454 | UniProt FT SIGNAL (SignalP, ECO:0000256) |
| Domain | DUF1329 (PF07044; IPR010752) | InterPro / Pfam |
| Fold | CDD cd16329 "LolA_like"; Gene3D 2.50.20.10 "Lipoprotein localisation LolA/LolB/LppX" | UniProt cross-references |
| Name | "DUF1329 domain-containing protein" is a machine-generated name (ProtNLM, ECO:0008006), not curated | UniProt DE line |
| GenBank product | "conserved exported protein of unknown function" | KEGG ppu:PP_0766 |

The identity is unambiguous. The locus tag, the organism (KT2440) and the domain all agree with the literature described below, which refers to PP_0766 by locus tag. There are no GO annotations for this protein in the local GOA file (`genes/PSEPK/PP_0766/PP_0766-goa.tsv` contains only a header row).

## 2. Domain and family

- **Pfam/InterPro DUF1329 (PF07044 / IPR010752).** The entry says only: "This family consists of several hypothetical bacterial proteins of around 475 residues in length. The majority of family members are from Pseudomonas species but the family also contains sequences from Shewanella oneidensis and Thauera aromatica." InterPro lists about 4,140 member proteins from about 2,070 taxa, and none has an experimental structure ([InterPro IPR010752](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR010752/), accessed 2026-10).
- **The partner family DUF1302 (PF06980) gives the most informative description:** "This entry represents a family of predicted outer membrane beta barrel proteins... These proteins are likely part of an exporter system that includes an MMPL exporter, a DUF1329 protein [pfam:PF07044] family protein that likely acts as a LolA-like chaperone." ([Pfam PF06980 via NCBI CDD](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980); InterPro API)
- **LolA-like fold.** The CDD (cd16329) and Gene3D (2.50.20.10) classifications place PP_0766 in the same structural class as LolA, LolB and the mycobacterial LppX/LprG proteins. All of these bind acyl chains in a hydrophobic cavity and shuttle lipidated or hydrophobic cargo across the periplasm or cell envelope. This suggests that PP_0766 binds a hydrophobic ligand. It does **not** mean that PP_0766 carries lipoproteins as LolA does.

## 3. Genomic context

From KEGG coordinates on the KT2440 chromosome (NC_002947), all genes on the + strand:

| Gene (KEGG) | Coordinates | Annotation |
|---|---|---|
| PP_0763 | 878472..880154 | Medium-chain fatty-acid CoA ligase |
| DUF1302 gene (UniProt PP_0765, Q88PT3; 628 aa, signal peptide 1–29) | 880486..882372 | Predicted outer-membrane β-barrel ("Adhesin", a ProtNLM name) |
| **PP_0766** | **882398..883762** | **DUF1329, exported** |
| LuxR/MalT-family regulator | 884090..886807 | Transcriptional regulator |
| PP_0767 / PP_0769 | 886967… | Response regulator/TPR protein; sensor histidine kinase |

Locus-tag numbering for the neighbours differs between KEGG and UniProt. The gene order, however, is consistent.

The DUF1302 and DUF1329 genes are separated by only 25 bp, so they are very likely co-transcribed. Thompson et al. (2020) concluded that "they are likely coexpressed in an operon positively regulated by the LuxR-type regulator PP_0767". The authors also note that "colocalization of PP_0765/PP_0766 near fatty acid catabolic genes in P. putida KT2440 and many other pseudomonads" is conserved (their Fig. S3). This matches the adjacent medium-chain acyl-CoA ligase. No MMPL/RND gene lies in this locus. The predicted inner-membrane partner, PP_2019, is encoded elsewhere, in the PP_2018–PP_2021 operon.

In *P. aeruginosa*, the ECLIPSE dark-proteome analysis found that DUF1302 genes frequently co-occur with DUF1329, LuxR-type and AraC-type regulator genes. It also reported an AlphaFold-Multimer model of the DUF1302–DUF1329 complex with a high interface score (ipTM about 0.84). The authors state that no experimental work on this family exists in *P. aeruginosa* (ECLIPSE, *Bioinformatics* 2026, PMID:42605071; [PMC13499233](https://pmc.ncbi.nlm.nih.gov/articles/PMC13499233/)).

## 4. Experimental evidence: RB-TnSeq fitness

**Thompson MG, Incha MR, Pearson AN, et al. Fatty acid and alcohol metabolism in *Pseudomonas putida*: functional analysis using random barcode transposon sequencing. *Appl Environ Microbiol* 2020;86(21):e01665-20. PMID:32826213; PMC7580535; DOI 10.1128/AEM.01665-20.**

These are the key findings, quoted verbatim from the PMC text:

- "Comparing the mutant fitness scores between Tween 20 and laurate (C12) carbon source experiments revealed six genes (PP_0765, PP_0766, PP_0767, PP_0914, PP_2018, and PP_2019) that had significant and severe fitness defects specific to Tween 20 (fitness score, less than −2; t-statistic > |4|) in both biological replicates."
- "The same comparison between butyl stearate and myristate (C14) revealed four genes specific to the fatty ester (PP_0765, PP_0766, PP_2018, and PP_4058)…"
- "As PP_0765-6 and PP_2018 appear to have specific importance under both of the ester conditions tested, it is possible that they contribute to the hydrolysis of the fatty ester bonds. However, it is also possible that the esterase is secreted or associated with the outer membrane, in which case, its enzymatic activity would be shared among the library, and it would not have the associated fitness defect expected."
- "Previous work in multiple other Pseudomonas species has shown cofitness of DUF1302/DUF1329 family genes with BNR domain and RND family efflux genes when grown on Tween 20. The authors proposed that the genes may work together in order to export a component of the cell wall. However, an alternative hypothesis could be that PP_0765 and PP_0766 contribute to catalyzing the hydrolysis of fatty esters… Further work will need to be done to biochemically characterize the potential enzymatic activity of these proteins."

How to read this:

- The phenotype is **conditional and specific**. PP_0766 is needed to use fatty-acid *esters*, but not the matching free fatty acids (laurate, myristate).
- The defect therefore lies upstream of β-oxidation: at ester hydrolysis, at uptake or handling of the ester or its products, or at some envelope function needed when growing on these amphiphiles.
- The esterase idea was offered as a hypothesis only. The authors themselves raise a strong objection to it: a secreted or surface esterase is a "public good" shared across the mutant pool, so losing it should *not* cause a fitness defect in a pooled assay. A mutant that is cell-autonomously defective fits better with loss of a transport or envelope-assembly component.
- Precision: this is a genome-wide pooled screen with two replicates. Individual deletion mutants were not tested and no complementation is reported.

## 5. Structural and interaction prediction

**Roberts JB, Nava AA, Pearson AN, Incha MR, et al. Foldy: an open-source web application for interactive protein structure analysis. *PLoS Comput Biol* 2024;20(2):e1011171. PMID:38306398; PMC10866462.**

This paper used PP_0765 and PP_0766 as a case study. Verbatim:

- "Prior RB-TnSeq experiments show the function of PP_0765 and PP_0766 correlates with two other genes which are essential for growth on Tween20: a periplasmic protein (PP_2018) and a multidrug efflux transporter (PP_2019)."
- "PP_0766 is predicted to interact with both PP_2019 and PP_0765, which, along with PP_0765's distinctive transmembrane beta barrel structure, suggest that PP_0766 may be localized to the periplasm, and PP_0765 may be localized to the outer membrane."
- "Altogether this suggests that PP_0765 and PP_0766, which were previously suspected of being involved in hydrolase activity, may actually be components of a novel transport system."

Caveats:

- The paper reports the predicted contacts as weak: "PP_0766 and PP_2019 weakly interact, PP_0766 and PP_0765 weakly interact, and PP_2019 and PP_2018 strongly interact."
- Peer reviewers asked for more detail on how the membrane proteins were modelled, and pointed out mislabelled panels in Fig. 4c.
- This is AlphaFold-based inference with no binding or localisation experiments.

**What the partners are.** KEGG annotates PP_2019 as "putative multidrug efflux transporter, RND family" (KO K07003, the MMPL-like RND class) and PP_2018 as a "BNR domain protein". This matches the Pfam DUF1302 description of a system made of an MMPL exporter, a DUF1329 LolA-like chaperone and a DUF1302 β-barrel.

**An analogous system in another organism, not shown to be homologous.** In *Castellaniella defragrans*, the HAE3-family RND transporter AmeD is co-expressed with an outer-membrane protein (AmeA) and two periplasmic proteins (AmeB and AmeC). Together they form a proposed four-part exporter of apolar monoterpenes (PMID:30334144, *Biodegradation* 2019). The architecture is similar: an RND pump of the HAE3/MMPL type, periplasmic carriers and an outer-membrane channel. I did not verify whether AmeA, AmeB or AmeC carry DUF1302 or DUF1329 domains, so this is offered only as an architectural parallel.

## 6. Synthesis

### Molecular function
- **Most likely:** a periplasmic carrier that binds a hydrophobic or acyl-containing ligand, with a LolA-like fold (CDD cd16329, Gene3D 2.50.20.10). It probably accepts substrate from the RND/MMPL inner-membrane transporter PP_2019 and passes it to the DUF1302 outer-membrane β-barrel (Pfam PF06980 description; Roberts et al. 2024).
- **No evidence** for catalytic activity. There are no known catalytic motifs and no enzyme assay. The esterase proposal (Thompson et al. 2020) has not been tested.
- **No evidence** that it carries lipoproteins. The LolA resemblance is a fold classification, not a functional assignment.

### Cellular location
- **Periplasm** is the best-supported location. Two independent lines agree: a predicted Sec signal peptide (residues 1–24, SignalP) with no predicted transmembrane helices in the mature chain, and a LolA-like soluble periplasmic fold, together with predicted contacts with an outer-membrane β-barrel and an inner-membrane RND protein.
- There is no experimental localisation; the protein exists at UniProt level PE 4 (predicted).

### Biological process
- **Supported phenotype:** it is required for growth on long-chain fatty-acid esters (Tween 20, butyl stearate) as the sole carbon source, but not on the matching free fatty acids (RB-TnSeq; PMID:32826213).
- **Possible mechanisms:**
  1. Export, across the envelope, of a hydrophobic molecule needed to use the esters. This could be an envelope or cell-surface component, as proposed in earlier multi-*Pseudomonas* cofitness work cited by Thompson et al.
  2. Uptake, or periplasmic shuttling, of the ester or of its fatty-acyl products.
  3. Direct involvement in ester hydrolysis. This is the least favoured, given the public-good argument.
- The transport direction and the substrate are both unknown.

### Regulation
- Probably co-transcribed with the DUF1302 gene and positively regulated by the adjacent LuxR/MalT-type regulator, which also had fitness defects on Tween 20 and on some short-chain fatty acids (Thompson et al., 2020).

## 7. Implications for GO annotation

These are suggestions for curation. PP_0766 currently has no GOA annotations.

- **Cellular component:** `periplasmic space` (GO:0042597) is defensible as an IC/ISS inference: a signal peptide, a LolA-like soluble fold, and predicted placement between the inner- and outer-membrane partners. Flag it as predicted, not demonstrated.
- **Molecular function:** no experimentally supported term. A lipid-binding or transporter-related term would rest only on fold similarity, so a conservative curator would leave molecular function unannotated or flag it as a knowledge gap. Do **not** annotate esterase/hydrolase activity, and do not annotate lipoprotein transporter activity by analogy to LolA.
- **Biological process:** the fitness phenotype, combined with the predicted partners, could support a cautious process term about transport across the cell envelope. The underlying evidence, however, is a pooled-fitness phenotype plus structure prediction. Neither the substrate nor the direction of transport is established, so process annotation should be avoided or stay very general.

## 8. Open questions and suggested experiments

1. **Localisation:** periplasmic fractionation (osmotic shock), or a PhoA/mCherry fusion, to confirm that PP_0766 is in the periplasm.
2. **Complex formation:** co-purification or crosslinking with PP_0765 and PP_2019, and bacterial two-hybrid assays, to test the predicted three-part system.
3. **Ligand binding:** purify mature PP_0766 (residues 25–454). Then screen binding of fatty acids, acyl esters, Tween 20 fragments and lipids, using intrinsic fluorescence, thermal-shift or native mass spectrometry, and attempt a crystal structure.
4. **Esterase test:** assay purified PP_0766 alone, and together with PP_0765, against p-nitrophenyl esters, Tween 20 and butyl stearate.
5. **Phenotype from clean deletions:** single deletions of PP_0765, PP_0766 and PP_2019 with complementation, grown alone in monoculture on Tween 20 and butyl stearate. Monoculture removes the public-good confound. Also compare the extracellular and cell-associated lipid profiles of the mutants to look for an exported molecule.

## Sources

**Primary literature**
- Thompson MG et al. (2020) *Appl Environ Microbiol* 86:e01665-20. PMID:32826213. [PMC7580535](https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/); preprint [bioRxiv 2020.07.04.188060](https://www.biorxiv.org/content/10.1101/2020.07.04.188060v1.full.pdf)
- Roberts JB et al. (2024) Foldy. *PLoS Comput Biol* 20:e1011171. PMID:38306398. [PMC10866462](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011171)
- ECLIPSE: exploring the dark proteome of ESKAPE pathogens (2026) *Bioinformatics*. PMID:42605071. [PMC13499233](https://pmc.ncbi.nlm.nih.gov/articles/PMC13499233/)
- AmeABCD RND transporter in *Castellaniella defragrans* (2019) *Biodegradation*. PMID:30334144 (architectural analogy only)
- Nelson KE et al. (2002) *Environ Microbiol* 4:799–808 (PMID:12534463); Belda E et al. (2016) *Environ Microbiol* 18:3403–3424 (PMID:26913973). These are the KT2440 genome papers.

**Databases**
- UniProt [Q88PT2](https://www.uniprot.org/uniprotkb/Q88PT2) and [Q88PT3](https://www.uniprot.org/uniprotkb/Q88PT3), local copies:
  ```
  /home/cmungall/ai-gene-review/genes/PSEPK/PP_0766/PP_0766-uniprot.txt
  /home/cmungall/ai-gene-review/genes/PSEPK/PP_0765/PP_0765-uniprot.txt
  ```
- InterPro [IPR010752](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR010752/); Pfam PF07044 and [PF06980 (NCBI CDD)](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980)
- KEGG entries ppu:PP_0763 to PP_0769, PP_2018 and PP_2019 ([KEGG](https://www.kegg.jp/entry/ppu:PP_0766))
- *Pseudomonas* Genome DB pages surfaced by search, e.g. [pseudomonas.com](https://www.pseudomonas.com/feature/show?id=1840607); [GO wiki PSEAE:LOLA](https://gowiki.tamu.edu/wiki/index.php/PSEAE:LOLA) for LolA background

**Not used**
- The Fitness Browser page for PP_0766 (fit.genomics.lbl.gov) was behind a Cloudflare challenge and could not be retrieved, so no per-gene fitness values are given here.
- The paper Thompson et al. cite for earlier multi-*Pseudomonas* DUF1302/DUF1329 cofitness on Tween 20 could not be identified from the reference list I retrieved, so that claim is reported only as Thompson et al. state it.

## Citations

1. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR010752/
2. https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC13499233/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/
5. https://www.biorxiv.org/content/10.1101/2020.07.04.188060v1.full.pdf
6. https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011171
7. https://www.uniprot.org/uniprotkb/Q88PT2
8. https://www.uniprot.org/uniprotkb/Q88PT3
9. https://www.kegg.jp/entry/ppu:PP_0766
10. https://www.pseudomonas.com/feature/show?id=1840607
11. https://gowiki.tamu.edu/wiki/index.php/PSEAE:LOLA