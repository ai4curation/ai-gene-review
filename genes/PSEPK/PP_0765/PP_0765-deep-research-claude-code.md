---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:12:16.061896'
end_time: '2026-10-30T21:16:22.387139'
duration_seconds: 246.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0765
  gene_symbol: PP_0765
  uniprot_accession: Q88PT3
  protein_description: 'RecName: Full=Adhesin {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_0765 {ECO:0000313|EMBL:AAN66390.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DUF1302. (IPR010727); DUF1302 (PF06980)
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
  web_search_requests: 5
  num_turns: 19
  total_cost_usd: 1.05840978
  session_id: b1de343e-dc08-4b39-9279-5b687f4089f1
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 6
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88PT3
- **Protein Description:** RecName: Full=Adhesin {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_0765 {ECO:0000313|EMBL:AAN66390.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF1302. (IPR010727); DUF1302 (PF06980)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0765" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0765' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0765** (gene ID: PP_0765, UniProt: Q88PT3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Neighbourhood check done: PP_0765 sits between a fatty acid–CoA ligase gene and the DUF1329 gene, all on the same strand. Next I'm searching for experimental data on these DUF families.

The key source is Thompson et al. (2020), an RB-TnSeq study of *P. putida* fatty acid metabolism. I'm reading its full text for the PP_0765/PP_0766 data.

The publisher pages refused automated fetches, so I'm getting the open-access full text from Europe PMC.

The local copy has the abstract only, so I'm trying the eScholarship PDF for the full results.

The bioRxiv fetch was blocked as a bot-check workaround, so I'm not retrying it. I'll rely on search-result excerpts and the cached abstract.

# PP_0765 (UniProt Q88PT3), a DUF1302 protein in *Pseudomonas putida* KT2440: research report

## Summary

This is the right protein: KEGG ppu:PP_0765 links to UniProt Q88PT3, and the 628-amino-acid sequence is identical in both records. PP_0765 is a secreted protein of about 68 kDa from *P. putida* KT2440. It has a single DUF1302 domain (Pfam PF06980; InterPro IPR010727). No biochemical, structural or localisation experiments have been done on PP_0765 itself, and it has **no GO annotations** (the local GOA file is empty).

The strongest functional evidence comes from one transposon-sequencing study (Thompson et al., 2020). It found that PP_0765, and its neighbouring gene PP_0766 (a DUF1329 protein), are needed specifically for growth on **fatty acid esters**: Tween 20 and butyl stearate. They are not needed for growth on the free fatty acids. Two competing roles have been proposed:

- **Esterase:** the 2020 study's hypothesis.
- **Outer-membrane β-barrel that moves substrate across the envelope with PP_0766:** supported by the Pfam family description, the sequence and a later structure-prediction study.

The sequence evidence favours an outer-membrane location. Neither role has been tested biochemically.

The UniProt name "Adhesin" was generated by a machine-learning model (`ECO:0008006|Google:ProtNLM`). No evidence supports it.

---

## 1. Identity and basic features

| Feature | Value | Source |
|---|---|---|
| Accession / locus | Q88PT3 / PP_0765 (EMBL AAN66390.1; RefSeq WP_010952006.1) | UniProt Q88PT3 (local file `genes/PSEPK/PP_0765/PP_0765-uniprot.txt`) |
| Length | 628 aa, about 67.9 kDa | UniProt |
| Signal peptide | Residues 1–29 (SignalP); mature chain 30–628 | UniProt FT SIGNAL `ECO:0000256|SAM:SignalP` |
| Domain | DUF1302 (PF06980 / IPR010727) | UniProt DR lines |
| Orthologous group | eggNOG COG3203 | UniProt DR line |
| Evidence level | PE 4 (Predicted); unreviewed TrEMBL entry | UniProt |
| GenBank product name | "conserved exported protein of unknown function" | [KEGG ppu:PP_0765](https://www.genome.jp/entry/ppu:PP_0765) |
| Genome position | 880486..882372, + strand | KEGG |

COG3203 is, as far as I know, the porin (OmpC-like) outer-membrane protein group. I did not check its exact description, so treat this point as supporting only.

**The C-terminus fits an outer-membrane β-barrel.** The protein ends in "…SFGVNF" with a terminal phenylalanine. This matches the C-terminal aromatic "β-signal" that the BAM machinery recognises in Gram-negative outer-membrane β-barrel proteins. This is my own reading of the sequence, not a published result.

## 2. The DUF1302 family

Pfam/CDD describes PF06980 as follows ([NCBI CDD pfam06980](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980)):

- It is a family of "predicted outer membrane beta barrel proteins" of about 600 residues, which "remain uncharacterised".
- Its members are "likely part of an exporter system that includes an MMPL exporter" and a DUF1329 (PF07044) protein "that likely acts as a LolA-like chaperone".

PP_0765 fits this description: it is 628 residues long, has a cleavable signal peptide and ends in the β-signal motif. Its DUF1329 partner sits next to it in the genome:

- PP_0766 (Q88PT2, 454 aa) has its own signal peptide.
- It carries a DUF1329 domain and matches CDD cd16329 "LolA_like" and Gene3D 2.50.20.10 "Lipoprotein localisation LolA/LolB/LppX" (UniProt Q88PT2, local file).

The LolA/LolB fold binds and carries hydrophobic acyl chains across the periplasm. That suggests PP_0766 shuttles a hydrophobic molecule between the inner and outer membranes, with PP_0765 as the outer-membrane end of the route.

## 3. Genomic context (KEGG ppu)

| Locus | Strand / position | Annotation |
|---|---|---|
| PP_0762 | − | Glycerate dehydrogenase |
| **PP_0763** | + 878472..880154 | **Medium-chain fatty acid–CoA ligase** (AMP-binding domain) |
| **PP_0765** | + 880486..882372 | DUF1302, predicted outer-membrane β-barrel |
| **PP_0766** | + 882398..883762 | DUF1329, LolA-like periplasmic protein |
| PP_0767 | + 884090.. | LuxR/MalT-family transcriptional regulator |
| PP_0768 / PP_0769 | + | Response regulator with TPR domain / sensor histidine kinase |

PP_0765 and PP_0766 are on the same strand, only 25 bp apart, and very likely form one operon. A fatty acid–CoA ligase sits just upstream, which links the pair to fatty acid metabolism. No MMPL exporter was found in this stretch of the genome, so the "MMPL-associated exporter" arrangement in the Pfam description may not apply here.

## 4. Experimental evidence: RB-TnSeq fitness (Thompson et al., 2020)

**Reference:** Thompson MG, Incha MR, Pearson AN, … Mukhopadhyay A, Deutschbauer AM. "Fatty Acid and Alcohol Metabolism in *Pseudomonas putida*: Functional Analysis Using Random Barcode Transposon Sequencing." *Appl Environ Microbiol* 86(21):e01665-20 (2020). PMID:32826213; PMC7580535; [doi:10.1128/AEM.01665-20](https://journals.asm.org/doi/10.1128/aem.01665-20). Preprint: [bioRxiv 2020.07.04.188060](https://www.biorxiv.org/content/10.1101/2020.07.04.188060v1.full).

- **Design:** pooled barcoded transposon mutants were grown on 13 fatty acids and 10 alcohols. The abstract (cached locally) says "Fitness data from mutant pools grown on fatty acids of varying chain lengths indicated specific enzyme substrate preferences and enabled us to hypothesize that DUF1302/DUF1329 family proteins potentially function as esterases."
- **Main result:** the study compared Tween 20 with laurate, and butyl stearate with myristate. Both comparisons found that PP_0765 and PP_0766 mutants had severe fitness defects specific to the ester substrates ([PMC7580535](https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/)). In each pair, the free fatty acid is the product the ester releases (lauric acid from Tween 20, stearic acid from butyl stearate), so the mutants grow on the free acid but not on the ester. The gene products are therefore needed to get at or break down the ester, not to oxidise the fatty acid.
- **Support from other species:** the paper cites earlier fitness data in other *Pseudomonas* species where DUF1302/DUF1329 genes were co-fit on Tween 20 with BNR-domain genes and RND-family efflux genes. The authors raised the possibility that these genes work together, possibly to export a cell-wall component.
- **The authors' own caveat:** they say biochemistry and mutational analysis are needed to find out whether these proteins really are esterases or do something else.

**Caveats on this evidence:**

- I could read only the abstract and search-engine excerpts. The cached file `publications/PMID_32826213.md` is abstract-only. Europe PMC's full-text service returned an error and the publisher returned HTTP 403. A direct fetch of the bioRxiv full text was refused by this session's permission classifier as bot-check circumvention, and I did not retry it.
- So the exact fitness values, the co-fitness partners and the Tween 20 export statement were not read in the paper itself. They come from search-tool summaries of the PMC and bioRxiv pages.
- These are fitness data from pooled mutants. They show the genes are **necessary** for using esters. They do not show which molecule PP_0765 acts on, or whether it catalyses anything.

## 5. Weighing the proposed functions

**Hypothesis A: esterase (Thompson et al., 2020).**
- For: the ester-specific fitness defect.
- Against: DUF1302 has no recognised hydrolase motif (no α/β-hydrolase fold, no GxSxG). The family is predicted to be a β-barrel, not an enzyme.

**Hypothesis B: outer-membrane β-barrel that moves fatty acid esters or related molecules, working with the periplasmic LolA-like PP_0766.**
- For: the Pfam description of the family, the signal peptide, the C-terminal Phe β-signal, and the LolA/LolB fold of the partner.
- For: a later structure-prediction study (Foldy, a web application for protein structure analysis from the Joint BioEnergy Institute (JBEI)) reportedly modelled PP_0765 as a membrane β-barrel in complex with PP_0766 and suggested a role in substrate transport ([ResearchGate entry](https://www.researchgate.net/publication/370784102_Foldy_a_web_application_for_interactive_protein_structure_analysis)). I could not open that paper, so this claim is reported second-hand.

**What best fits all the evidence.** PP_0765 is probably an outer-membrane β-barrel. With PP_0766 it likely carries large, hydrophobic fatty acid esters (such as Tween 20 or butyl stearate), or the fatty acids released from them, across the cell envelope. Any hydrolysis is probably done by another enzyme. This would explain:

- the ester-specific phenotype, because free fatty acids can enter by other routes such as FadL-type channels;
- the operon link to the PP_0763 fatty acid–CoA ligase;
- the co-fitness with efflux and envelope genes in other pseudomonads.

The direction of transport (import or export) is not known.

## 6. Localisation

| Compartment | Confidence | Basis |
|---|---|---|
| Outer membrane (integral β-barrel) | Moderate, predicted | SignalP signal peptide, C-terminal Phe β-signal, Pfam family description, structure prediction (Foldy) |
| Periplasm / cell envelope (with PP_0766) | Predicted | Partner has a signal peptide and a LolA-like fold |

No experiment has localised PP_0765, whether by fractionation or by proteomics.

## 7. GO annotation implications

- **Current annotations:** none in GOA.
- **Defensible now:** the cellular component "cell outer membrane" (GO:0009279) could be justified as a predicted location, by curator inference (IC) from the signal peptide, the β-signal and the family description.
- **Biological process:** a process term about using fatty acid esters as a carbon source rests only on necessity (fitness) data, and the mechanism is unknown. Per the project's rule on proposing new terms, hold it back or treat it as tentative.
- **Molecular function:** do not assign a hydrolase/esterase function (carboxylic ester hydrolase activity) or a transporter function yet. Neither has been shown biochemically, and the domain evidence argues against an esterase.
- **Name:** the ProtNLM name "Adhesin" has no support from domain, context or experiment. A better name would be "DUF1302 family outer membrane protein" or "putative outer membrane β-barrel protein involved in fatty acid ester utilisation".

## 8. Open questions and suggested experiments

1. Grow clean ΔPP_0765 and ΔPP_0766 deletion mutants, and complemented strains, on Tween 20, butyl stearate and their free acids, to confirm the RB-TnSeq phenotype.
2. Assay the purified protein for esterase activity (e.g. p-nitrophenyl esters, Tween hydrolysis), and test supernatant and whole cells of wild-type and mutant strains. This tests hypothesis A.
3. Fractionate membranes (sucrose gradient or sarkosyl extraction) and check heat-modifiability, a mobility shift typical of β-barrels, to test outer-membrane localisation.
4. Pull-down or crosslinking of PP_0765 with PP_0766, and testing whether PP_0766 binds fatty acyl chains, as LolA does lipoprotein acyl chains.
5. Measure uptake of labelled fatty acid esters in mutant and wild-type cells to tell import apart from export.

---

## Sources
- UniProt Q88PT3 and Q88PT2 flat files (local: `genes/PSEPK/PP_0765/PP_0765-uniprot.txt`, `genes/PSEPK/PP_0766/PP_0766-uniprot.txt`); release entry version 81, 28 January 2026.
- KEGG entries ppu:PP_0760–PP_0770, fetched 30 October 2026: https://www.genome.jp/entry/ppu:PP_0765
- [NCBI CDD / Pfam PF06980 (DUF1302)](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980)
- [Thompson et al. 2020, *Appl Environ Microbiol* 86:e01665-20, PMID:32826213 (PMC7580535)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/); [ASM version](https://journals.asm.org/doi/10.1128/aem.01665-20); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2020.07.04.188060v1.full); [ResearchGate copy](https://www.researchgate.net/publication/343794609_Functional_analysis_of_the_fatty_acid_and_alcohol_metabolism_of_Pseudomonas_putida_using_RB-TnSeq)
- [Foldy: a web application for interactive protein structure analysis (ResearchGate)](https://www.researchgate.net/publication/370784102_Foldy_a_web_application_for_interactive_protein_structure_analysis), not read directly
- [PaperBLAST family search, PF07044 (DUF1329)](https://papers.genomics.lbl.gov/cgi-bin/hmmSearch.cgi?hmmId=PF07044)
- [bioRxiv 2026 preprint on hydrocarbon metabolism and PET degradation](https://www.biorxiv.org/content/10.64898/2026.03.18.709718v1.full.pdf), which mentions DUF1302/DUF1329 only in passing
- Background only, on other *Pseudomonas* outer-membrane channels for hydrophobic molecules: [OprG structure (PMC2993939)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2993939/)

## Citations

1. https://www.genome.jp/entry/ppu:PP_0765
2. https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980
3. https://journals.asm.org/doi/10.1128/aem.01665-20
4. https://www.biorxiv.org/content/10.1101/2020.07.04.188060v1.full
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/
6. https://www.researchgate.net/publication/370784102_Foldy_a_web_application_for_interactive_protein_structure_analysis
7. https://www.researchgate.net/publication/343794609_Functional_analysis_of_the_fatty_acid_and_alcohol_metabolism_of_Pseudomonas_putida_using_RB-TnSeq
8. https://papers.genomics.lbl.gov/cgi-bin/hmmSearch.cgi?hmmId=PF07044
9. https://www.biorxiv.org/content/10.64898/2026.03.18.709718v1.full.pdf
10. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2993939/