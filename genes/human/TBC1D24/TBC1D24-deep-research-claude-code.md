---
provider: claude_code
cached: false
start_time: '2026-11-13T15:49:27.699040'
end_time: '2026-11-13T15:51:31.821795'
duration_seconds: 124.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TBC1D24
  gene_symbol: TBC1D24
  uniprot_accession: Q9ULP9
  protein_description: 'RecName: Full=TBC1 domain family member 24;'
  gene_info: Name=TBC1D24; Synonyms=KIAA1171;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: Rab-GAP-TBC_dom. (IPR000195); Rab-GAP_TBC_sf. (IPR035969); TLDc_dom.
    (IPR006571); RabGAP-TBC (PF00566); TLD (PF07534)
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
  web_search_requests: 12
  num_turns: 19
  total_cost_usd: 2.1943497999999995
  session_id: 7cfb9a62-7989-4b1e-b19e-342893070fbd
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9ULP9
- **Protein Description:** RecName: Full=TBC1 domain family member 24;
- **Gene Information:** Name=TBC1D24; Synonyms=KIAA1171;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Rab-GAP-TBC_dom. (IPR000195); Rab-GAP_TBC_sf. (IPR035969); TLDc_dom. (IPR006571); RabGAP-TBC (PF00566); TLD (PF07534)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TBC1D24" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TBC1D24' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TBC1D24** (gene ID: TBC1D24, UniProt: Q9ULP9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TBC1D24 (human, UniProt Q9ULP9): function, pathways and localization

**Identity check.** The symbol, organism and domain architecture all match the literature: human TBC1D24 (KIAA1171) is consistently described as an N-terminal TBC (Rab-GAP-like) domain fused to a C-terminal TLDc domain. No ambiguity with another gene was found.

**Verification limits.** Most claims below rest on abstracts, the UniProt record and search summaries, not full texts. Two PubMed fetches were blocked, so the 2024 *Structure* and 2025 *iScience* findings are taken from UniProt's curated summary and repository abstracts. Items marked "(from memory)" were not retrieved in this session and should be checked before citing.

## 1. Summary

TBC1D24 is a brain-enriched, peripheral membrane regulator of vesicle trafficking, not a demonstrated enzyme. Evidence points to three mechanisms:

- **ARF6 suppression:** it binds ARF6 and prevents its activation, which underlies its roles in neuronal migration, neurite and axon growth, and dendritic spine maintenance.
- **Phosphoinositide-dependent membrane recruitment:** the TBC domain binds PI(4,5)P2-type lipids, which is needed for synaptic vesicle trafficking.
- **V-ATPase regulation:** the TLDc domain binds V1 subunits of the vacuolar ATPase, affecting organelle and synaptic vesicle acidification.

Rab-GAP activity for the human protein remains unproven ("May act as a GAP" in UniProt).

## 2. Molecular function

### TBC domain: atypical, lipid-binding, GAP activity unproven
- TBC1D24 is an unconventional TBC protein that lacks the catalytic "arginine finger", so any GTP-hydrolysis stimulation would need an alternative mechanism (review statement in [Finelli et al. 2019, PMC6360273](https://pmc.ncbi.nlm.nih.gov/articles/PMC6360273)).
- The Drosophila ortholog Skywalker was reported to act as a GAP for Rab35: dominant-negative Rab35 rescued *sky* mutants and constitutively active Rab35 mimicked them (Uytterhoeven et al. 2011, *Cell*, citation from memory; summarized at [InteractiveFly](https://www.sdbonline.org/sites/FLY/genebrief/skywalker.htm)).
- Crystal structures of the Skywalker TBC domain (PDB 5HJN apo, 2.5 Å; 5HJQ with IP3, 2.3 Å) revealed a conserved cationic pocket that binds phosphoinositides phosphorylated at the 4 and 5 positions. The most prevalent patient mutations map to this pocket and reduce lipid binding. In flies they impair synaptic vesicle trafficking and cause seizures, and raising synaptic PI(4,5)P2 reverses the defects ([Fischer et al. 2016, *Nat Struct Mol Biol*, PMID 27669036](https://pubmed.ncbi.nlm.nih.gov/27669036/); [RCSB 5HJQ](https://www.rcsb.org/structure/5hjq)).

### ARF6 binding and suppression
- TBC1D24 co-immunoprecipitates with ARF6. Overexpression increases neurite length and arborization, and the epilepsy mutations D147H and A509V revert this (Falace et al. 2010, *Am J Hum Genet*, PMID 20727515; abstract in the local cache).
- In utero knockdown in rat neocortex delays the multipolar-to-bipolar transition and radial migration. Inactive ARF6 rescues the phenotype and active ARF6 phenocopies it, indicating that TBC1D24 prevents ARF6 activation ([Falace et al. 2014, *PNAS*, PMID 24469796](https://pmc.ncbi.nlm.nih.gov/articles/PMC3926028)).
- The biochemical mechanism is unresolved: no direct ARF-GAP catalysis has been shown.

### TLDc domain: V-ATPase interaction, with conflicting direction
- The TLDc domain defines a class of V-ATPase-interacting proteins. In an early study, purified TLDc domains of Ncoa7, Oxr1 and Tldc2 pulled down V-ATPase, but that of Tbc1d24 did not ([Eaton et al. 2021, *Sci Rep*, PMC8608904](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8608904/)).
- Oot & Wilkens 2024 (*Structure* 32:989, PMID 38593795, "Human V-ATPase function is positively and negatively regulated by TLDc proteins") is cited by UniProt for TBC1D24 inhibiting V-ATPase by inducing disassembly of the complex.
- Pepe, Aprile et al. 2025 (*iScience*, PMID 39758816) report that TBC1D24 binds ATP6V1A and ATP6V1B2 in brain. Knockout neurons show cytosolic mislocalization of V1, raised endo-lysosomal pH, impaired autophagy and defective synaptic vesicle endocytosis and reacidification. They conclude it is a positive regulator in neurons ([DOAJ record](https://doaj.org/article/3595403cd28a40d0a2aeb0dc5f4a6f82)).
- The in vitro (inhibitory) and neuronal (positive) results are not reconciled; UniProt records both.
- A crystal structure of the Drosophila Skywalker TLDc domain exists (PDB 6R82; [RCSB](https://www.rcsb.org/annotations/6R82)). TLDc mutations (R360H, G501R) cause activity-induced locomotion and vesicle trafficking defects in flies that are rescued by antioxidants (Lüthy et al. 2019, *Brain*, PMID 31257402).

### RAB22A and recycling endosomes
In HeLa cells, TBC1D24 overexpression increases tubular recycling endosomes carrying clathrin-independent endocytosis cargo, and its deletion impairs their formation. TBC1D24 binds RAB22A, through which it regulates this recycling ([Nguyen et al. 2020, *BBRC*, PMID 32475639](https://www.pubmed.gov/32475639/)). This is a binding and effector-like relationship, not demonstrated GAP activity.

## 3. Biological processes

| Process | Evidence | Source |
|---|---|---|
| Synaptic vesicle endocytosis and recycling | Tbc1d24 disruption in mouse impairs presynaptic endocytosis; disease mutations cause partial loss of function | [Finelli et al. 2019, *Hum Mol Genet*, PMID 30335140](https://pmc.ncbi.nlm.nih.gov/articles/PMC6360273) |
| Endosomal sorting of synaptic vesicle proteins | Skywalker restricts Rab35-driven sorting to the endolysosomal route (fly) | [Fischer et al. 2016](https://pubmed.ncbi.nlm.nih.gov/27669036/) |
| Axon specification and growth-cone trafficking | Silencing in rat cortical neurons impairs axon specification, initial-segment maturation and growth-cone endocytosis, with altered ARF6 activation; also examined in patient iPSC neurons | [Aprile et al. 2019, *Cell Death Differ*, PMC6889177](https://pmc.ncbi.nlm.nih.gov/articles/PMC6889177) |
| Cortical radial migration and neuronal maturation | In utero knockdown, ARF6 rescue | [Falace et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3926028) |
| Dendritic spine maintenance | Postsynaptic TBC1D24 suppresses ARF6; F251L destabilizes the protein; adult hippocampal knockdown causes spine loss and fear-memory deficits | [Lin et al. 2020, *PLoS Genet*, PMID 32004315](https://doaj.org/article/490b041e33c249168770dfdd26320f44) |
| Organelle acidification and neuronal autophagy | V-ATPase V1 localization and lysosomal pH depend on TBC1D24 in neurons | [Pepe et al. 2025](https://doaj.org/article/3595403cd28a40d0a2aeb0dc5f4a6f82) |
| Hair-cell ribbon synapse vesicle recycling | S178L knock-in mice show endosome-like vacuoles, fewer ribbon-associated vesicles and reduced sustained exocytosis | [2024 *Clin Genet* study, PMID 39400345](https://searchworks.jioinstitute.edu.in/articles/cmedm__39400345) |
| Oxidative stress resistance | Disease mutations alter sensitivity to oxidative stress in Neuro2a cells; likely secondary to the TLDc/trafficking role | [Finelli et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6360273) |

The oxidative-stress and developmental phenotypes are best read as downstream of the trafficking and acidification roles, not as separate core functions.

## 4. Localization

- **Cytoplasm with partial plasma-membrane association**, as a peripheral membrane protein (Falace et al. 2010; UniProt Q9ULP9).
- **Presynapse**, on synaptic vesicle and endosomal membranes, recruited by phosphoinositides (Lüthy et al. 2019; [Fischer et al. 2016](https://pubmed.ncbi.nlm.nih.gov/27669036/)).
- **Postsynapse and dendrites**, at excitatory synapses ([Lin et al. 2020](https://doaj.org/article/490b041e33c249168770dfdd26320f44)).
- **Growth cone, soma and neurites** ([Aprile et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6889177); Pepe et al. 2025 via UniProt).
- **Tubular recycling endosomes** in non-neuronal cells ([Nguyen et al. 2020](https://www.pubmed.gov/32475639/)).
- **Inner ear:** stereocilia of hair cells and spiral ganglion neurons in developing mouse cochlea; one study reported expression in human but not mouse hair cells ([OMIM 613577 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/613577)).
- Clathrin-coated vesicle association is recorded in UniProt by similarity to mouse only.
- Expression is highest in brain, mainly cortex and hippocampus (Falace et al. 2010).

## 5. Disease relevance (as functional evidence)

Biallelic or dominant variants cause a spectrum recorded in UniProt: familial infantile myoclonic epilepsy, developmental and epileptic encephalopathy 16, DOORS syndrome, recessive deafness DFNB86, dominant deafness DFNA65, and rolandic epilepsy with exercise-induced dystonia. Over 50 missense and loss-of-function variants are spread across both domains (Lüthy et al. 2019). Haploinsufficiency is clinically significant ([Finelli et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6360273)).

## 6. Open questions and caveats for annotation

- **Rab-GAP activity is not established for the human protein.** The Rab35 evidence is from Drosophila, and the domain lacks the arginine finger.
- **The ARF6 mechanism is undefined:** "prevents ARF6 activation" is a genetic and cell-biological inference, not ARF-GAP catalysis.
- **V-ATPase direction is contested** (inhibitor in vitro versus positive regulator in neurons).
- **Mouse S178L hearing phenotype is inconsistent:** an earlier study found no hearing loss, while the 2024 knock-in found mild loss.
- **G501R versus G511R numbering** for the TLDc variant differs between passages of Lüthy et al. 2019; check which sequence each refers to.

## Sources

- [Fischer et al. 2016, PMID 27669036](https://pubmed.ncbi.nlm.nih.gov/27669036/)
- [RCSB 5HJQ](https://www.rcsb.org/structure/5hjq) and [RCSB 5HJN](https://www.rcsb.org/structure/5HJN)
- [RCSB 6R82 (Skywalker TLDc)](https://www.rcsb.org/annotations/6R82)
- [Falace et al. 2014, PMC3926028](https://pmc.ncbi.nlm.nih.gov/articles/PMC3926028)
- [Finelli et al. 2019, PMC6360273](https://pmc.ncbi.nlm.nih.gov/articles/PMC6360273)
- [Aprile et al. 2019, PMC6889177](https://pmc.ncbi.nlm.nih.gov/articles/PMC6889177)
- [Lin et al. 2020, PLoS Genet](https://doaj.org/article/490b041e33c249168770dfdd26320f44)
- [Nguyen et al. 2020, PMID 32475639](https://www.pubmed.gov/32475639/)
- [Pepe et al. 2025, iScience (DOAJ)](https://doaj.org/article/3595403cd28a40d0a2aeb0dc5f4a6f82)
- [Eaton et al. 2021, PMC8608904](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8608904/)
- [Addgene record for PMID 38593795 (Oot & Wilkens 2024)](https://addgene.org/browse/pubmed/38593795)
- [S178L knock-in mouse study, PMID 39400345](https://searchworks.jioinstitute.edu.in/articles/cmedm__39400345)
- [OMIM 613577 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/613577)
- [InteractiveFly: skywalker](https://www.sdbonline.org/sites/FLY/genebrief/skywalker.htm)
- Local files: `genes/human/TBC1D24/TBC1D24-uniprot.txt`, `publications/PMID_20727515.md`, `publications/PMID_30335140.md`, `publications/PMID_31257402.md`

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6360273
2. https://www.sdbonline.org/sites/FLY/genebrief/skywalker.htm
3. https://pubmed.ncbi.nlm.nih.gov/27669036/
4. https://www.rcsb.org/structure/5hjq
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3926028
6. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8608904/
7. https://doaj.org/article/3595403cd28a40d0a2aeb0dc5f4a6f82
8. https://www.rcsb.org/annotations/6R82
9. https://www.pubmed.gov/32475639/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC6889177
11. https://doaj.org/article/490b041e33c249168770dfdd26320f44
12. https://searchworks.jioinstitute.edu.in/articles/cmedm__39400345
13. https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/613577
14. https://www.rcsb.org/structure/5HJN
15. https://addgene.org/browse/pubmed/38593795