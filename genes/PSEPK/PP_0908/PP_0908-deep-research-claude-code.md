---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:11:34.676065'
end_time: '2026-10-30T21:15:46.821277'
duration_seconds: 252.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0908
  gene_symbol: PP_0908
  uniprot_accession: Q88PE2
  protein_description: 'RecName: Full=DUF1513 domain-containing protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_0908 {ECO:0000313|EMBL:AAN66533.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Quino_amine_DH_bsu. (IPR011044); UCP028101. (IPR008311); WD40/YVTN_repeat-like_dom_sf.
    (IPR015943); DUF1513 (PF07433)
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
  web_search_requests: 7
  num_turns: 16
  total_cost_usd: 1.0348967999999998
  session_id: a19241e0-7ff7-496f-84b7-09f7ef34c79a
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88PE2
- **Protein Description:** RecName: Full=DUF1513 domain-containing protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_0908 {ECO:0000313|EMBL:AAN66533.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Quino_amine_DH_bsu. (IPR011044); UCP028101. (IPR008311); WD40/YVTN_repeat-like_dom_sf. (IPR015943); DUF1513 (PF07433)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0908" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0908' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0908** (gene ID: PP_0908, UniProt: Q88PE2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Checking the Pfam literature on the EfeUOB association and the gene neighbourhood.

Wrapping up the operon context; one last literature check on DUF1513 in other bacteria.

# PP_0908 (Q88PE2), *Pseudomonas putida* KT2440: research report on the DUF1513 / COG3490 protein

## Summary

**PP_0908 has never been studied experimentally**, and its biochemical function is unknown. Searches of the web and the literature found no publication that names PP_0908 or reports an experiment on any DUF1513 protein. Everything below is inference from the protein's sequence and domains, from the genes around it, and from database classifications.

- **Protein:** a 365-residue protein with a cleavable N-terminal signal peptide (an export signal). Almost all of it is a single DUF1513 domain, which is predicted to fold into a ring-shaped "β-propeller" structure.
- **Function:** Pfam's curators classify DUF1513 proteins as part of an EfeUOB-like iron uptake system. PP_0908 sits in a tight cluster of genes, PP_0910–PP_0909–PP_0908, whose neighbours encode an EfeO/imelysin-like protein and a protein with cytochrome c and peroxidase-like domains. Together these support a hypothesis that PP_0908 is an accessory part of a system in the periplasm (the space between the two membranes) for taking up or processing ferrous iron.
- **What remains unknown:** the reaction it catalyses (if any), what it binds, and whether it binds a cofactor.

## 1. Identity check

| Feature | Value | Source |
|---|---|---|
| Accession | Q88PE2 (Q88PE2_PSEPK), unreviewed TrEMBL entry, 365 aa, 39,944 Da | UniProt flat file (local `PP_0908-uniprot.txt`) |
| Locus | PP_0908; EMBL AAN66533.1; RefSeq WP_010952112.1 | UniProt |
| Organism | *P. putida* KT2440 (NCBI taxon 160488) | UniProt |
| Name | "DUF1513 domain-containing protein". This name was generated by the ProtNLM machine-learning model (ECO:0008006), so it is not evidence of function. | UniProt |
| GenBank product | "conserved exported protein of unknown function" | KEGG ppu:PP_0908 |
| Protein existence | PE 4, "Predicted" | UniProt |
| Existing GO annotations | None (the GOA file contains only a header row) | local `PP_0908-goa.tsv` |

The locus tag, organism and domain content all agree with each other, so there is no doubt about which protein this is. The difficulty is not ambiguity but that no literature exists for it or its close homologues.

Genome sources: Nelson et al. 2002, *Environ Microbiol* 4:799 (PMID:12534463), and the re-annotation by Belda et al. 2016, *Environ Microbiol* 18:3403 (PMID:26913973). Neither paper characterises PP_0908.

## 2. Domain architecture and predicted structure

| Signature | Database description | Interpretation |
|---|---|---|
| **Pfam PF07433, DUF1513** | "Protein of unknown function." The curated InterPro/Pfam text reads: *"This entry represents bacterial proteins that are predicted to be the outer membrane component of an efeUOB-like ferrous iron, uptake system."* It cites Miethke et al. 2013 (PMID:23764491) and Price et al. 2018 (PMID:29769716). | Covers almost the whole mature protein. About 2,083 proteins in about 2,050 proteomes, all bacterial ([InterPro API](https://www.ebi.ac.uk/interpro/api/entry/pfam/PF07433)). |
| **PIRSF028101 / IPR008311, UCP028101** | *"There are currently no experimental data for members of this group or their homologues, nor do they exhibit features indicative of any function."* | Confirms that the family is uncharacterised. |
| **IPR011044 / SSF50969 / Gene3D 2.130.10.10** | "Quinoprotein amine dehydrogenase β-chain-like"; YVTN repeat-like β-propeller | Predicts a 7-bladed β-propeller fold. This fold is shared with the β-chain of quinohemoprotein amine dehydrogenase, the H chain of methylamine dehydrogenase, and archaeal S-layer YVTN domains ([InterPro IPR011044](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR011044/)). |
| **IPR015943** | WD40/YVTN repeat-like domain superfamily | Same β-propeller fold. |
| COG3490 / KEGG K09947 | "Uncharacterized conserved protein, DUF1513 domain"; function unknown | [NCBI CDD COG3490](https://www.ncbi.nlm.nih.gov/Structure/cdd/COG3490) |

**Interpreting the fold.** A β-propeller fold does not by itself imply an enzyme. The same fold serves as a binding scaffold (WD40 proteins), a lactonase or gluconolactonase, or the substrate-binding subunit of a quinoprotein. KEGG's weaker motif hits ("Lactonase", "choice_anch_I") are consistent with a generic propeller and do not establish an activity. The match to the quinoprotein amine dehydrogenase β-chain is structural only. The quinone cofactor in those enzymes sits on a different subunit, so the match does not imply that PP_0908 is a dehydrogenase.

**N-terminus.** The protein begins `MLRRQALKLGSVLLSALTLGGW…`. This is a hydrophobic signal peptide, and `RRQALKL` loosely resembles the twin-arginine (Tat) consensus (S/T)-R-R-x-F-L-K. This is my own reading of the sequence; no prediction tool was run. Together with GenBank's "exported" annotation, it suggests export across the inner membrane, possibly by the Tat pathway, which exports already-folded proteins that often carry cofactors. A Tat route is plausible but unconfirmed. SignalP 6 or TatP should be run to test it.

**Localisation caveat.** Pfam calls DUF1513 proteins the "outer membrane component". However, PP_0908 shows no feature of an outer-membrane β-barrel, such as alternating amphipathic β-strands or a C-terminal aromatic signature. Its fold is a soluble propeller. The most defensible prediction is a **soluble periplasmic protein**, or at most one loosely attached to a membrane. Its outer-membrane location should be treated as unverified.

## 3. Genomic context: an operon with putative iron-handling genes

Gene coordinates (KEGG, reverse strand, transcribed from PP_0910 toward PP_0908):

| Locus | Coordinates | Product / domains | KO |
|---|---|---|---|
| PP_0906 | c(1045333..1048377) | RND multidrug efflux transporter | K18138 |
| PP_0907 | c(1048379..1049599) | RND membrane fusion protein | K03585 |
| **PP_0908** | **c(1049755..1050852)** | **DUF1513, exported** | **K09947** |
| PP_0909 | c(1050855..1051919) | **Peptidase_M75** (imelysin / EfeO-like), exported | K07338 |
| PP_0910 | c(1051939..1053366) | **DHOR + Cytochrome_C / CBB3** (di-haem, cytochrome c peroxidase-like), exported | – |
| PP_0911, PP_0912 | c(1053476..1054463) | conserved hypothetical | – |
| PP_0913 | c(1054500..1055831) | Peptidase_M75; "putative iron-regulated protein" | K07231 |
| PP_0915 | c(1058291..1058887) | Fe-superoxide dismutase | K04564 |

Data from the [KEGG REST API](https://rest.kegg.jp/get/ppu:PP_0908) (KEGG gene entries for ppu:PP_0906–PP_0915).

**PP_0910, PP_0909 and PP_0908 form a tightly packed cluster.** The genes are separated by only about 3–20 bp, and the start codon of PP_0910 overlaps PP_0909. This layout is typical of a co-transcribed operon. STRING links PP_0908 to its neighbours with high confidence ([STRING API](https://string-db.org)):

| Partner | Combined score | Neighbourhood | Phylogenetic co-occurrence | Co-expression |
|---|---|---|---|---|
| PP_0909 (M75) | 0.991 | 0.869 | 0.775 | 0.401 |
| PP_0910 (di-haem cyt c) | 0.990 | 0.844 | 0.775 | 0.436 |
| PP_0913 (M75, "iron-regulated") | 0.928 | 0.686 | 0.775 | – |

The strong phylogenetic co-occurrence score (0.775) means that PP_0908, PP_0909 and PP_0910 orthologues tend to be present or absent together across genomes. That pattern is a hallmark of a functional module, not just neighbouring genes.

**Why this points to iron.**
- **The M75 partner.** Peptidase M75 (imelysin) domains define EfeO. EfeO is the periplasmic, cupredoxin-associated component of the EfeUOB ferrous iron transporter, which in *B. subtilis* is essential for high-affinity uptake of ferrous and ferric iron (Miethke et al. 2013, *BBA* 1833:2267, PMID:23764491; this is one of the two references Pfam cites for DUF1513). The same family includes P19/FtrA, the copper-binding protein that oxidises iron in the bacterial Ftr system.
- **The Ftr model in *Rubrivivax gelatinosus*.** Steunou et al. 2022 propose that the copper protein FtrA (P19-like) oxidises Fe²⁺ while reducing its bound copper. The ferric iron then passes via FtrB to the permease FtrC, and the electrons are recycled by FtrD, which acts as an electron sink ([Steunou et al. 2022, *FEBS J* 289:6286, doi:10.1111/febs.16476](https://hal-udl.archives-ouvertes.fr/CEA-UPSAY/hal-03795534v1); structures [PDB 7R4Z](https://rcsb.org/structure/7R4Z), [7R5P](https://rcsb.org/structure/7R5P)). The equivalent *Bordetella* system, FtrABCD (Brickman & Armstrong 2012, *Mol Microbiol*; [PubMed 23647104](https://pubmed.ncbi.nlm.nih.gov/23647104)), is iron- and pH-responsive and required for ferrous iron use under acidic conditions ([ECU theses on the Brucella/Bordetella Ftr system](https://thescholarship.ecu.edu/items/4223bc10-4aea-4eab-92b3-4299b859b15b)).
- **The di-haem cytochrome c partner.** PP_0910's domains suggest a periplasmic redox protein. In this kind of module it could plausibly carry electrons released by iron oxidation, similar to the electron-sink role proposed for FtrD.

**Important differences from the classic systems.** KT2440 has no annotated EfeO (K07224) or EfeB/DyP peroxidase (K16301). Its only FTR1/EfeU-family permease, PP_0180 (K07243), is encoded far from this cluster. So the PP_0908–PP_0910 cluster is at most an *EfeUOB-like* or *Ftr-like* periplasmic module with a non-canonical makeup. No paper has linked PP_0908 to any of the defined components (EfeO, EfeB, FtrA, FtrB, FtrD) one-to-one.

## 4. High-throughput and functional-genomics evidence

- Pfam cites **Price et al. 2018** (*Nature* 557:503, PMID:29769716), the large RB-TnSeq fitness study, as support for its iron-uptake description of DUF1513. This suggests that DUF1513 genes in at least some bacteria showed fitness phenotypes, or co-fitness with iron-uptake genes, under specific conditions. I could not open the Fitness Browser entry for KT2440 PP_0908 or PaperBLAST, because both were blocked by a Cloudflare challenge. **So I cannot confirm whether PP_0908 itself has any fitness phenotype in KT2440.** This is the most useful check to do next.
- I found no transcriptomic or proteomic study that specifically reports PP_0908. I also did not verify whether it responds to iron levels or Fur, the iron-responsive regulator.

## 5. Synthesis: function, location and pathway

| Aspect | Best current inference | Confidence |
|---|---|---|
| Molecular function | Unknown. The β-propeller suggests a binding scaffold, possibly for a partner protein or a metal or redox ligand. No catalytic residues or cofactor motif are recognisable. | Low |
| Biological process | Possibly an accessory role in periplasmic ferrous-iron acquisition or processing (EfeUOB/Ftr-like), together with the M75 protein PP_0909 and the di-haem cytochrome PP_0910 | Low to moderate. Rests on Pfam's family-level classification, operon structure, and co-occurrence across genomes. |
| Location | Exported by a signal peptide, possibly Tat-dependent. Most likely periplasmic and soluble. The Pfam "outer membrane" label is not supported by the sequence. | Moderate for "exported/periplasmic"; low for "outer membrane" |
| Pathway | No defined pathway. Candidate module: PP_0910–PP_0909–PP_0908 (plus PP_0913), with EfeU/FTR1-family permease PP_0180 as a possible inner-membrane partner elsewhere in the genome | Speculative |

### Implications for GO annotation
- No experimental GO terms are justified.
- If annotating at all, use the cellular-component term **periplasmic space (GO:0042597)**, and only after a signal-peptide prediction tool confirms export. A process term such as *iron ion transport* would rest only on family-level inference plus operon context. It should be treated as a hypothesis, not proposed as a new annotation, unless fitness data in KT2440 (Fitness Browser) support it.
- Do not transfer quinoprotein dehydrogenase, lactonase or peptidase activities from the structural superfamily matches. Peptidase_M75 is a domain of the neighbouring PP_0909 protein, not of PP_0908.

## 6. Suggested experiments and open questions
1. **Fitness data:** look up PP_0908, PP_0909, PP_0910 and PP_0180 in the Fitness Browser (organism "Putida"). Check for co-fitness and for phenotypes under iron limitation, chelators such as 2,2′-dipyridyl, low pH, or copper stress.
2. **Gene deletions:** measure growth of ΔPP_0908 and Δ(PP_0908–0910) strains with Fe²⁺ (plus ascorbate) as the sole iron source at acidic pH, with and without a *pvd* (pyoverdine) background. Pyoverdine is *P. putida*'s main siderophore and would otherwise mask a defect in ferrous uptake.
3. **Localisation:** fractionate PhoA/GFP fusions or use cell-fractionation with immunoblotting. Test Tat dependence in a Δ*tatC* strain.
4. **Biochemistry:** purify the mature protein and test whether it binds metals (Fe, Cu) and whether it interacts with PP_0909 and PP_0910, for example by pull-down or crosslinking.
5. **Regulation:** test whether the PP_0910–0908 operon is induced by iron limitation through Fur.

## References
- Nelson KE et al. (2002) Complete genome sequence and comparative analysis of the metabolically versatile *Pseudomonas putida* KT2440. *Environ Microbiol* 4:799–808. PMID:12534463.
- Belda E et al. (2016) The revisited genome of *Pseudomonas putida* KT2440 enlightens its value as a robust metabolic chassis. *Environ Microbiol* 18:3403–3424. PMID:26913973.
- Miethke M, Monteferrante CG, Marahiel MA, van Dijl JM (2013) The *Bacillus subtilis* EfeUOB transporter is essential for high-affinity acquisition of ferrous and ferric iron. *Biochim Biophys Acta* 1833:2267–2278. PMID:23764491.
- Price MN et al. (2018) Mutant phenotypes for thousands of bacterial genes of unknown function. *Nature* 557:503–509. PMID:29769716.
- Steunou AS et al. (2022) New insights into the mechanism of iron transport through the bacterial Ftr system present in pathogens. *FEBS J* 289:6286–6307. https://hal-udl.archives-ouvertes.fr/CEA-UPSAY/hal-03795534v1
- Brickman TJ, Armstrong SK (2012) Iron and pH-responsive FtrABCD ferrous iron utilization system of *Bordetella* species. *Mol Microbiol*. https://pubmed.ncbi.nlm.nih.gov/23647104
- Kumar S, Davis RM, Ruiz N (2024) YdbH and YnbE form an intermembrane bridge… *PNAS* 121:e2321512121. PMID:38748582. Listed by InterPro under IPR008311; no relevance to PP_0908's function was established.
- InterPro/Pfam entries PF07433, IPR008311, IPR011044 (InterPro API, accessed 2026-10-30): https://www.ebi.ac.uk/interpro/api/entry/pfam/PF07433
- NCBI CDD COG3490: https://www.ncbi.nlm.nih.gov/Structure/cdd/COG3490
- KEGG gene entries ppu:PP_0906–PP_0915 and KO K09947, K07338, K07231, K07243: https://rest.kegg.jp/get/ppu:PP_0908
- STRING v12 interaction partners for PP_0908 (taxon 160488): https://string-db.org
- Thesis material on the Brucella/Bordetella Ftr system, East Carolina University: https://thescholarship.ecu.edu/items/4223bc10-4aea-4eab-92b3-4299b859b15b

## Citations

1. https://www.ebi.ac.uk/interpro/api/entry/pfam/PF07433
2. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR011044/
3. https://www.ncbi.nlm.nih.gov/Structure/cdd/COG3490
4. https://rest.kegg.jp/get/ppu:PP_0908
5. https://string-db.org
6. https://hal-udl.archives-ouvertes.fr/CEA-UPSAY/hal-03795534v1
7. https://rcsb.org/structure/7R4Z
8. https://rcsb.org/structure/7R5P
9. https://pubmed.ncbi.nlm.nih.gov/23647104
10. https://thescholarship.ecu.edu/items/4223bc10-4aea-4eab-92b3-4299b859b15b