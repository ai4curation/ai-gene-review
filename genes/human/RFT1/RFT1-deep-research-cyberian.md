---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T20:09:04.121189'
end_time: '2026-01-23T20:22:34.869934'
duration_seconds: 810.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RFT1
  gene_symbol: RFT1
  uniprot_accession: Q96AA3
  protein_description: 'RecName: Full=Man(5)GlcNAc(2)-PP-dolichol translocation protein
    RFT1 {ECO:0000305|PubMed:18313027}; AltName: Full=Protein RFT1 homolog {ECO:0000312|HGNC:HGNC:30220};'
  gene_info: Name=RFT1 {ECO:0000312|HGNC:HGNC:30220};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the RFT1 family. .
  protein_domains: RFT1. (IPR007594); Rft-1 (PF04506)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96AA3
- **Protein Description:** RecName: Full=Man(5)GlcNAc(2)-PP-dolichol translocation protein RFT1 {ECO:0000305|PubMed:18313027}; AltName: Full=Protein RFT1 homolog {ECO:0000312|HGNC:HGNC:30220};
- **Gene Information:** Name=RFT1 {ECO:0000312|HGNC:HGNC:30220};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RFT1 family. .
- **Key Domains:** RFT1. (IPR007594); Rft-1 (PF04506)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RFT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RFT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RFT1** (gene ID: RFT1, UniProt: Q96AA3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RFT1: The Man5GlcNAc2-PP-Dolichol Flippase Essential for N-Linked Glycosylation

## Introduction

RFT1 (UniProt: Q96AA3) encodes a 541-amino acid integral membrane protein that functions as a lipid-linked oligosaccharide (LLO) flippase in the endoplasmic reticulum (ER). The protein catalyzes the translocation of Man5GlcNAc2-PP-dolichol (M5GN2-PP-Dol) from the cytoplasmic face to the luminal face of the ER membrane, a critical step in the biosynthesis of the oligosaccharide substrate used for N-linked protein glycosylation [helenius-2002-rft1-nature-abstract]. This translocation event represents an essential checkpoint in the dolichol pathway, as the final assembly steps of the 14-sugar N-glycan precursor can only occur within the ER lumen where the mannose and glucose donors (Dol-P-Man and Dol-P-Glc) are available.

The identification of RFT1's function has had a complex scientific history. Initial genetic studies in yeast in 2002 demonstrated that RFT1 is essential for viability and that its depletion results in accumulation of the M5GN2-PP-Dol intermediate on the cytoplasmic face of the ER [helenius-2002-rft1-nature-abstract]. However, subsequent biochemical studies using reconstituted systems challenged whether RFT1 directly catalyzes the flipping reaction or plays an indirect role [frank-2008-rft1-flip-abstract]. This controversy persisted for over two decades until 2024, when a fully reconstituted in vitro assay definitively demonstrated that purified RFT1 directly catalyzes M5GN2-PP-Dol translocation across lipid bilayers [chen-2024-rft1-flippase-abstract].

RFT1 belongs to the MOP (multidrug/oligosaccharidyl-lipid/polysaccharide) exporter superfamily of transporters, which includes the bacterial MurJ flippases that export lipid II for peptidoglycan biosynthesis. Defects in human RFT1 cause RFT1-CDG (formerly CDG-In), a rare congenital disorder of glycosylation characterized by developmental delay, seizures, and sensorineural deafness [haeuptle-2008-rft1-cdg-abstract].

## Molecular Function: The LLO Flippase Activity

The primary function of RFT1 is to catalyze the ATP-independent translocation of Man5GlcNAc2-PP-dolichol across the ER membrane. This flippase activity is essential because N-glycan biosynthesis is topologically divided between the two leaflets of the ER membrane. The initial steps of oligosaccharide assembly—adding two GlcNAc residues and five mannose residues to dolichol pyrophosphate—occur on the cytoplasmic face using nucleotide-activated sugar donors (UDP-GlcNAc and GDP-mannose). The subsequent steps—adding four more mannoses and three glucoses—occur in the ER lumen using dolichol-phosphate-linked sugar donors [chen-2024-rft1-flippase-abstract].

The 2024 study by Chen et al. definitively resolved the mechanism question by developing a completely reconstituted in vitro assay. Using proteoliposomes containing purified RFT1 and synthetic M5GN2-PP-Dol substrate, the researchers demonstrated that RFT1 is both necessary and sufficient for translocation [chen-2024-rft1-flippase-abstract]. Key characteristics of the flippase activity include:

1. **ATP independence**: Translocation occurs without ATP hydrolysis, suggesting a facilitated diffusion or alternating access mechanism rather than active transport.

2. **Substrate selectivity**: RFT1 demonstrates strong preference for M5GN2-PP-Dol over M3GN2-PP-Dol (the three-mannose intermediate), ensuring that translocation occurs only after the complete heptasaccharide is assembled on the cytoplasmic face.

3. **Lipid carrier tolerance**: The flippase activity occurs with similar kinetics for both natural dolichol and synthetic phytanol lipid carriers.

4. **Functional conservation**: The archaeal homolog Agl23 from halophilic archaea can functionally substitute for RFT1 in yeast, demonstrating evolutionary conservation of this essential function [chen-2024-rft1-flippase-abstract].

## The Scientific Controversy and Its Resolution

The question of whether RFT1 directly catalyzes LLO flipping was controversial for over twenty years. The initial genetic evidence from Helenius et al. (2002) strongly supported a direct role: yeast cells lacking RFT1 accumulated M5GN2-PP-Dol on the cytoplasmic face and failed to complete N-glycan biosynthesis [helenius-2002-rft1-nature-abstract]. However, subsequent biochemical studies produced contradictory results.

Frank et al. (2008) reported that LLO flipping activity could be detected in reconstituted proteoliposomes that lacked RFT1, leading them to conclude that "a specific ER protein(s), but not Rft1, is required to flip Man5GlcNAc2-PP-Dol in reconstituted vesicles" [frank-2008-rft1-flip-abstract]. Similarly, Rush et al. (2009) found that sealed microsomes prepared from RFT1-depleted yeast cells retained normal M5-DLO flippase activity in vitro, even though the same cells accumulated 37-fold more M5GN2-PP-Dol than wild-type cells in vivo [rush-2009-rft1-microsomes-abstract].

These paradoxical findings suggested that cellular organization might be critical for RFT1 function—that the protein's role might depend on membrane organization, protein complexes, or other factors that are disrupted during cell lysis and microsome preparation. Alternative explanations included the possibility that RFT1 functions indirectly, perhaps by organizing or chaperoning the substrate rather than directly catalyzing translocation.

The controversy was resolved by the 2024 study, which identified several technical factors that had confounded earlier in vitro studies [chen-2024-rft1-flippase-abstract]. The key advance was developing a fully reconstituted system with defined components, including purified RFT1 protein and synthetic M5GN2-PP-Dol substrate, rather than relying on crude microsomal preparations that contained numerous contaminating activities. This approach definitively demonstrated that purified RFT1 catalyzes M5GN2-PP-Dol translocation, confirming its identity as the authentic ER flippase.

## Protein Structure and Membrane Topology

Human RFT1 is a polytopic membrane protein with a complex transmembrane architecture. Recent structural predictions using AlphaFold2 reveal that the protein contains 14 transmembrane (TM) spans arranged as two lobes, each containing seven transmembrane helices [pei-2024-rft1-molecular-abstract]. This is in contrast to earlier predictions of 11 transmembrane domains based on hydropathy analysis.

Key structural features include:

1. **Nin-Cin topology**: Both the N-terminus and C-terminus are oriented toward the cytoplasm, consistent with an even number of transmembrane spans.

2. **Central hydrophilic cavity**: A cavity approximately 23 Å wide at the membrane-water interface extends into the membrane, presumably providing a translocation pathway for the bulky glycan headgroup.

3. **Inward-open conformation**: The AlphaFold model resembles the inward-open state of alternating access transporters, suggesting that the protein likely cycles between inward-open (cytoplasm-facing) and outward-open (lumen-facing) conformations during the translocation cycle.

4. **Structural similarity to MurJ**: The overall architecture resembles bacterial MurJ flippases, which transport lipid II (the peptidoglycan precursor) across the cytoplasmic membrane. Both proteins belong to the MOP transporter superfamily and share the challenge of translocating large, amphipathic lipid-linked substrates [pei-2024-rft1-molecular-abstract].

5. **Lack of N-glycosylation**: Although human RFT1 contains a potential N-glycosylation sequon in intracellular loop 3, the protein is not N-glycosylated, consistent with this region being oriented toward the cytoplasm rather than the ER lumen.

The human RFT1 protein shares only 22% sequence identity with its yeast ortholog, yet the human protein can functionally complement yeast cells lacking RFT1, demonstrating that the core structural and functional features are evolutionarily conserved [haeuptle-2008-rft1-cdg-abstract].

## Subcellular Localization and Tissue Expression

RFT1 localizes to the endoplasmic reticulum membrane, consistent with its function in the ER-localized N-glycosylation pathway [pei-2024-rft1-molecular-abstract]. Fluorescence microscopy studies in yeast using ER marker proteins demonstrate that RFT1 distributes throughout the ER network rather than being restricted to specific ER subdomains. This distribution pattern is consistent with the protein's role in the general N-glycosylation pathway, which operates throughout the ER to modify newly synthesized secretory and membrane proteins.

The ER localization is essential for RFT1 function because the substrate (M5GN2-PP-Dol) is synthesized on the cytoplasmic face of the ER, and the product of translocation is immediately utilized by luminal mannosyltransferases and glucosyltransferases to complete N-glycan biosynthesis.

Interestingly, studies in Trypanosoma brucei have revealed that the RFT1 ortholog (TbRFT1) localizes to both the ER and the Golgi apparatus [gottier-2017-rft1-gpi-abstract]. This dual localization suggests that RFT1 may have additional roles beyond ER-localized LLO flipping, at least in some organisms. However, whether human RFT1 similarly localizes to the Golgi remains to be determined.

With respect to tissue distribution, data from the Human Protein Atlas demonstrates that RFT1 exhibits low tissue specificity, being expressed in all examined human tissues [human-protein-atlas]. The mRNA expression shows relatively uniform distribution (Tau score of 0.23), with highest expression observed in pancreas (21.1 nTPM), lymph nodes (15.7 nTPM), and endocrine tissues such as parathyroid and thyroid glands (13.7-14.6 nTPM). Skeletal muscle shows the lowest expression (4.6 nTPM), while brain regions display moderate levels (4.4-7.6 nTPM). This ubiquitous expression pattern is consistent with RFT1's essential role in N-linked glycosylation, a fundamental process required for the maturation of secretory and membrane proteins in all cell types.

## Position in the N-Glycosylation Pathway

N-linked glycosylation is the most common covalent modification of proteins in eukaryotic cells, with profound implications for protein folding, quality control, trafficking, and function [helenius-2004-nglycans-review-abstract]. The glycans serve multiple roles in the ER: they promote proper folding by stabilizing polypeptide structures, act as recognition tags for lectins and chaperones, and signal whether proteins have achieved their native conformation or should be targeted for degradation via ER-associated degradation (ERAD). The transfer of the pre-assembled oligosaccharide from its dolichol carrier to nascent proteins is mediated by the oligosaccharyltransferase (OST) complex at the ER translocon, ensuring that glycosylation occurs co-translationally.

RFT1 occupies a central position in the dolichol pathway of N-linked glycosylation, acting at the boundary between cytoplasmic and luminal biosynthetic steps:

**Upstream enzymes (cytoplasmic face):**
- DPAGT1: Transfers GlcNAc-1-P to dolichol-P
- ALG13/ALG14: Adds second GlcNAc
- ALG1: Adds first mannose (α1,4)
- ALG2: Adds mannoses 2 and 3 (α1,3 and α1,6)
- ALG11: Adds mannoses 4 and 5 (α1,2)

**The RFT1 translocation step:**
M5GN2-PP-Dol is flipped from the cytoplasmic to the luminal face of the ER membrane.

**Downstream enzymes (luminal face):**
- ALG3: Adds mannose 6 (α1,3)
- ALG9: Adds mannose 7 (α1,2)
- ALG12: Adds mannose 8 (α1,6)
- ALG9: Adds mannose 9 (α1,2)
- ALG6, ALG8, ALG10: Add three glucose residues

**Final transfer:**
The oligosaccharyltransferase (OST) complex transfers the completed Glc3Man9GlcNAc2 oligosaccharide from dolichol to asparagine residues in nascent polypeptides within the consensus sequence Asn-X-Ser/Thr.

The strict substrate selectivity of RFT1 for the M5 intermediate (rather than shorter intermediates) ensures that translocation occurs only after the cytoplasmic biosynthetic steps are complete. This checkpoint function prevents premature translocation that would result in truncated, non-functional glycan structures [chen-2024-rft1-flippase-abstract].

## Broader Roles in Glycosylation

While the primary function of RFT1 is in the N-glycosylation pathway, recent evidence suggests that RFT1 may influence other glycosylation processes. A study in Trypanosoma brucei, where RFT1 is non-essential and can be completely deleted (unlike in yeast and mammals), revealed that TbRFT1 deficiency affects not only N-glycosylation but also glycosylphosphatidylinositol (GPI) anchor side-chain modification [gottier-2017-rft1-gpi-abstract].

Analysis of GPI-anchored proteins in TbRFT1-null parasites demonstrated truncated GPI anchor side chains compared to wild-type cells. Importantly, this GPI underglycosylation was not due to defective formation of GPI precursor lipids or impaired galactosylation in the ER. Rather, the defect appeared to occur at modifications expected to take place in the Golgi apparatus. Consistent with this, TbRFT1 was found to localize to both the ER and Golgi by immunofluorescence microscopy [gottier-2017-rft1-gpi-abstract]. These findings implicate RFT1 in a broader range of glycosylation processes than previously appreciated, though whether this expanded role applies to human RFT1 remains to be determined.

The connection between N-glycosylation and GPI anchor biosynthesis is not entirely surprising, as both pathways share the use of dolichol-linked sugar donors and involve similar topological challenges of transporting glycolipid intermediates across membranes. The observation that RFT1 affects GPI glycosylation in T. brucei raises the possibility that some aspects of the clinical phenotype in RFT1-CDG patients may relate to GPI anchor defects in addition to N-glycosylation abnormalities.

## Evolutionary Conservation

RFT1 is highly conserved across eukaryotes and has functional orthologs in archaea, reflecting the ancient origin of N-linked glycosylation. Key observations regarding conservation include:

1. **Eukaryotic conservation**: RFT1 orthologs are found in all examined eukaryotes, from yeast to humans. Despite only 22% sequence identity between human and yeast RFT1, the proteins are functionally interchangeable—human RFT1 complements yeast rft1Δ mutants [haeuptle-2008-rft1-cdg-abstract].

2. **Archaeal orthologs**: Archaea also assemble N-glycans on dolichol-linked carriers and possess RFT1 homologs. The archaeal protein Agl23 from Haloferax halobium can suppress rft1Δ lethality in yeast and exhibits M5GN2-PP-Dol flipping activity, demonstrating functional conservation across domains of life [chen-2024-rft1-flippase-abstract].

3. **MOP superfamily membership**: RFT1 belongs to the oligosaccharidyl-lipid flippase (OLF) family within the broader MOP transporter superfamily. This superfamily includes the bacterial MurJ lipid II flippases, suggesting that lipid-linked oligosaccharide translocation mechanisms evolved from a common ancestor.

## Clinical Significance: RFT1-CDG

Defects in human RFT1 cause RFT1-CDG (OMIM 612015), a rare autosomal recessive disorder formerly known as CDG-In. This condition was first described in 2008 when Haeuptle et al. identified a patient with a homozygous c.199C>T mutation (p.R67C) in RFT1 [haeuptle-2008-rft1-cdg-abstract].

**Clinical features** of RFT1-CDG typically include:
- Developmental delay and intellectual disability
- Hypotonia
- Seizures, often presenting as early-onset epileptic encephalopathy [aeby-2016-rft1-epilepsy-abstract]
- Sensorineural deafness (a distinctive feature that helps distinguish RFT1-CDG from other CDG subtypes) [vleugels-2009-rft1-novel-cdg-abstract]
- Hepatomegaly and coagulopathy
- Dysmorphic features

**Cellular pathology**: At the cellular level, RFT1 deficiency causes accumulation of DolPP-GlcNAc2Man5 on the cytoplasmic face of the ER and a corresponding reduction in the complete DolPP-GlcNAc2Man9Glc3 oligosaccharide in the lumen. This results in hypoglycosylation of many secretory and membrane proteins, as the oligosaccharyltransferase cannot efficiently transfer incomplete glycan structures [haeuptle-2008-rft1-cdg-abstract].

**Known mutations**: To date, multiple pathogenic RFT1 mutations have been identified, including:
- p.R67C (in a hydrophilic loop)
- p.R25W, p.C70R (N-terminal region)
- p.K152E (luminal loop)
- p.G276D, p.E298K (luminal loops)
- p.M408V, p.R442Q (transmembrane domains) [pei-2024-rft1-molecular-abstract]

Analysis of disease mutations reveals that most map to highly conserved regions of the protein, particularly the central hydrophilic cavity that likely forms the substrate translocation pathway. Mutations in the transmembrane domains appear to be associated with milder phenotypes compared to mutations in the luminal loops [pei-2024-rft1-molecular-abstract].

**Diagnosis and treatment**: RFT1-CDG is diagnosed through a combination of transferrin isoelectric focusing (which shows a type I CDG pattern), cellular LLO analysis (showing M5GN2-PP-Dol accumulation), and confirmatory genetic testing. Currently, no specific treatment exists for RFT1-CDG; management is symptomatic and supportive, focusing on seizure control, developmental support, and management of other complications.

## Open Questions

Despite significant advances in understanding RFT1 function, several important questions remain:

1. **Detailed translocation mechanism**: While it is now established that RFT1 catalyzes M5GN2-PP-Dol translocation, the precise molecular mechanism remains unclear. Does RFT1 function as a true flippase with an alternating access mechanism, or does it create a channel or groove that allows the lipid-linked oligosaccharide to traverse the membrane? High-resolution structural studies of RFT1 in different conformational states are needed.

2. **Energetics of translocation**: How does RFT1 catalyze the thermodynamically unfavorable movement of a large, hydrophilic glycan headgroup across the hydrophobic membrane core without ATP hydrolysis? Understanding whether translocation is driven by substrate concentration gradients, membrane potential, or other factors remains an open question.

3. **In vivo regulation**: Little is known about how RFT1 activity is regulated in cells. Is the protein subject to post-translational modification? Does it form functional complexes with other glycosylation machinery components? Does RFT1 expression or activity change in response to ER stress or glycosylation demands?

4. **Genotype-phenotype correlations**: With relatively few RFT1-CDG patients identified to date, the relationship between specific mutations and clinical severity remains incompletely defined. Why do some mutations (e.g., transmembrane domain mutations) appear to cause milder disease than others?

5. **Therapeutic opportunities**: Could RFT1-CDG be treated by approaches that enhance residual RFT1 activity, bypass the translocation step, or supplement glycosylation through alternative pathways? Understanding the degree of residual function in different mutations could inform therapeutic strategies.

6. **Resolution of the in vitro paradox**: Although the 2024 study definitively showed that purified RFT1 catalyzes translocation, the question of why earlier microsomal studies failed to detect RFT1-dependent activity remains incompletely understood. Identifying the confounding factors in those experiments could provide insights into the cellular organization of the N-glycosylation machinery.

7. **Role in GPI anchor glycosylation**: Studies in T. brucei suggest that RFT1 may influence GPI anchor side-chain modification in addition to N-glycosylation. Whether this broader role is conserved in humans, and whether GPI anchor defects contribute to RFT1-CDG pathology, remains to be investigated.

8. **Dual localization significance**: The observation that TbRFT1 localizes to both ER and Golgi raises questions about whether human RFT1 has similar dual localization and whether this reflects additional functions beyond LLO flipping in the ER.

## References

1. **[helenius-2002-rft1-nature-abstract]** Helenius J, Ng DT, Marolda CL, Walter P, Valvano MA, Aebi M. Translocation of lipid-linked oligosaccharides across the ER membrane requires Rft1 protein. Nature. 2002 Jan 24;415(6870):447-50. PMID: 11807558. DOI: 10.1038/415447a. https://pubmed.ncbi.nlm.nih.gov/11807558/

2. **[chen-2024-rft1-flippase-abstract]** Chen S, Pei CX, Xu S, Li H, Liu YS, Wang Y, Jin C, Dean N, Gao XD. Rft1 catalyzes lipid-linked oligosaccharide translocation across the ER membrane. Nat Commun. 2024 Jun 17;15(1):5186. PMID: 38886340. PMCID: PMC11182771. DOI: 10.1038/s41467-024-48999-3. https://pubmed.ncbi.nlm.nih.gov/38886340/

3. **[haeuptle-2008-rft1-cdg-abstract]** Haeuptle MA, Pujol FM, Neupert C, Winchester B, Kastaniotis AJ, Aebi M, Hennet T. Human RFT1 deficiency leads to a disorder of N-linked glycosylation. Am J Hum Genet. 2008 Mar;82(3):600-6. PMID: 18313027. PMCID: PMC2427296. DOI: 10.1016/j.ajhg.2007.12.021. https://pubmed.ncbi.nlm.nih.gov/18313027/

4. **[frank-2008-rft1-flip-abstract]** Frank CG, Sanyal S, Rush JS, Waechter CJ, Menon AK. Does Rft1 flip an N-glycan lipid precursor? Nature. 2008 Aug 7;454(7205):732. PMID: 18668045. DOI: 10.1038/nature07165. https://pubmed.ncbi.nlm.nih.gov/18668045/

5. **[rush-2009-rft1-microsomes-abstract]** Rush JS, Gao N, Lehrman MA, Matveev S, Waechter CJ. Suppression of Rft1 expression does not impair the transbilayer movement of Man5GlcNAc2-P-P-dolichol in sealed microsomes from yeast. J Biol Chem. 2009 Jul 17;284(29):19835-42. PMID: 19494107. PMCID: PMC2740409. DOI: 10.1074/jbc.M109.000893. https://pubmed.ncbi.nlm.nih.gov/19494107/

6. **[vleugels-2009-rft1-novel-cdg-abstract]** Vleugels W, Haeuptle MA, Ng BG, Michalski JC, Battini R, Dionisi-Vici C, Ludman MD, Jaeken J, Foulquier F, Freeze HH, Matthijs G, Hennet T. RFT1 deficiency in three novel CDG patients. Hum Mutat. 2009 Oct;30(10):1428-34. PMID: 19701946. DOI: 10.1002/humu.21085. https://pubmed.ncbi.nlm.nih.gov/19701946/

7. **[aeby-2016-rft1-epilepsy-abstract]** Aeby A, Prigogine C, Vilain C, Malfilatre G, Jaeken J, Lederer D, Van Bogaert P. RFT1-congenital disorder of glycosylation (CDG) syndrome: a cause of early-onset severe epilepsy. Epileptic Disord. 2016 Mar;18(1):92-6. PMID: 26892341. DOI: 10.1684/epd.2016.0802. https://pubmed.ncbi.nlm.nih.gov/26892341/

8. **[pei-2024-rft1-molecular-abstract]** Pei CX, Bhattacharjee S, Bhattacharjee S, Dean N. Molecular characterization of Rft1, an ER membrane protein associated with congenital disorder of glycosylation RFT1-CDG. J Biol Chem. 2024 Aug;300(8):107583. PMID: 39025454. PMCID: PMC11014557. DOI: 10.1016/j.jbc.2024.107583. https://pubmed.ncbi.nlm.nih.gov/39025454/

9. **[gottier-2017-rft1-gpi-abstract]** Gottier P, Suter DM, Combes L, Zufferey M, Gönczy P, Bütikofer P. RFT1 Protein Affects Glycosylphosphatidylinositol (GPI) Anchor Glycosylation. J Biol Chem. 2017 Jan 20;292(3):853-864. PMID: 27927990. PMCID: PMC5247644. DOI: 10.1074/jbc.M116.758367. https://pubmed.ncbi.nlm.nih.gov/27927990/

10. **[helenius-2004-nglycans-review-abstract]** Helenius A, Aebi M. Roles of N-linked glycans in the endoplasmic reticulum. Annu Rev Biochem. 2004;73:1019-49. PMID: 15189166. DOI: 10.1146/annurev.biochem.73.011303.073752. https://pubmed.ncbi.nlm.nih.gov/15189166/

11. **[human-protein-atlas]** Human Protein Atlas. RFT1 Tissue Expression. https://www.proteinatlas.org/ENSG00000163933-RFT1/tissue

12. **[omim-611908]** OMIM Entry *611908 - RFT1 HOMOLOG; RFT1. https://omim.org/entry/611908

13. **[sgd-rft1]** Saccharomyces Genome Database. RFT1 / YBL020W. https://www.yeastgenome.org/locus/S000000116


## Citations

1. aeby-2016-rft1-epilepsy-abstract.md
2. chen-2024-rft1-flippase-abstract.md
3. frank-2008-rft1-flip-abstract.md
4. gottier-2017-rft1-gpi-abstract.md
5. haeuptle-2008-rft1-cdg-abstract.md
6. helenius-2002-rft1-nature-abstract.md
7. helenius-2004-nglycans-review-abstract.md
8. pei-2024-rft1-molecular-abstract.md
9. rush-2009-rft1-microsomes-abstract.md
10. vleugels-2009-rft1-novel-cdg-abstract.md