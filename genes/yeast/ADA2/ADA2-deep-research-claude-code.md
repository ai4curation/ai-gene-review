---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:19:53.946740'
end_time: '2026-11-18T15:21:39.961107'
duration_seconds: 106.01
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: ADA2
  gene_symbol: ADA2
  uniprot_accession: Q02336
  protein_description: 'RecName: Full=SAGA complex subunit ADA2; AltName: Full=Transcriptional
    adapter 2;'
  gene_info: Name=ADA2; OrderedLocusNames=YDR448W; ORFNames=D9461.33;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Not specified in UniProt
  protein_domains: ADA2-like_ZZ. (IPR041983); Ada2/TADA2. (IPR016827); Homeodomain-like_sf.
    (IPR009057); SANT/Myb. (IPR001005); SANT_dom. (IPR017884)
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
  num_turns: 16
  total_cost_usd: 2.0024301
  session_id: 1b4afd02-cb7e-485b-bb5b-7e3bfee56082
  stop_reason: end_turn
  permission_denials: 1
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
- **UniProt Accession:** Q02336
- **Protein Description:** RecName: Full=SAGA complex subunit ADA2; AltName: Full=Transcriptional adapter 2;
- **Gene Information:** Name=ADA2; OrderedLocusNames=YDR448W; ORFNames=D9461.33;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ADA2-like_ZZ. (IPR041983); Ada2/TADA2. (IPR016827); Homeodomain-like_sf. (IPR009057); SANT/Myb. (IPR001005); SANT_dom. (IPR017884)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ADA2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ADA2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ADA2** (gene ID: ADA2, UniProt: Q02336) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ADA2 (YDR448W; UniProt Q02336) in *Saccharomyces cerevisiae*: research report

## Identity check and sourcing

The target is unambiguous: yeast ADA2 ("Transcriptional adapter 2", SAGA complex subunit ADA2), a 434-residue protein with an N-terminal ZZ zinc finger (residues 2–58), a SANT domain (60–112) and a C-terminal SWIRM domain (349–434), matching the InterPro domains given. It is not the human *ADA2* gene (adenosine deaminase 2, formerly CECR1), which is unrelated; the human orthologs of yeast Ada2 are TADA2A and TADA2B.

Findings below come from the UniProt record and from abstracts or search summaries of the cited papers; I did not read full texts. Items I am recalling without a retrieved source are marked "(from memory)".

## 1. Primary function: non-catalytic activator of the Gcn5 acetyltransferase

Ada2 is not an enzyme. It is the obligate partner of the histone acetyltransferase Gcn5 within the HAT module (Gcn5, Ada2, Ada3/Ngg1, Sgf29), which is shared by the SAGA, SLIK/SALSA and ADA complexes.

- **Discovery as an "adaptor".** ADA2 was isolated genetically as a gene required for the function of certain acidic activation domains: mutants resist the toxicity of overexpressed GAL4-VP16 (Berger et al. 1992, Cell, PMID:1638630).
- **Physical link to Gcn5 and Ada3.** Ada2 binds Gcn5 (Marcus et al. 1994, PMID:7957049) and forms a trimeric complex with Ada3 and Gcn5 (Horiuchi et al. 1995, PMID:7862114).
- **Domain mapping.** The N-terminal and middle regions of Ada2 are both essential in vivo, and the middle region is needed for Ada3 binding (Candau & Berger 1996, PMID:8617808; [abstract](https://www.scilit.net/publications/ca60e5a83bf817d43379ced732bf5db5)).
- **Catalytic core.** Ada2, Ada3 and Gcn5 are sufficient in vitro for nucleosomal acetyltransferase activity and lysine specificity. Ada2 increases Gcn5 catalytic activity, while Ada3 promotes nucleosomal acetylation and broadens lysine specificity (Balasubramanian et al. 2002, J Biol Chem 277:7989; [SGD record](https://www.yeastgenome.org/reference/11773077)). Gcn5 alone acetylates free histones and peptides but not nucleosomes.
- **SANT domain requirement.** The SANT domain is required in vivo and for HAT activity of native Gcn5 complexes ([Boyer et al. 2002, Mol Cell 10:935](https://pure.psu.edu/en/publications/essential-role-for-the-sant-domain-in-the-functioning-of-multiple/); [Sterner et al. 2002, J Biol Chem 277:8178](https://www.yeastgenome.org/reference/S000074947)). These papers interpreted it as a substrate-recognition element.
- **Structural mechanism (revises the above).** Crystal structures of an Ada2/Gcn5 complex (PDB 6CW2, 6CW3; ~2.0 Å) show the SANT domain sits away from the Gcn5 peptide-binding pocket. It does not act as a histone-tail binder; instead it raises Gcn5's affinity for acetyl-CoA, the first substrate in Gcn5's ordered Bi-Bi mechanism ([Sun et al. 2018, PNAS, PMID:30224453](https://pmc.ncbi.nlm.nih.gov/articles/PMC6176591)).
- **Central region.** A clustered mutation in the conserved central region (ada2-RLR: R211S, L212A, R215A) cuts PHO5 activation about threefold and reduces Gcn5-mediated acetylation in vitro to about 40% of wild type ([Hoke et al. 2008, J Mol Biol, PMID:18950642](https://www.pubmed.gov/18950642/)). The same region binds phospholipids in vitro, the basis of the GO "phosphatidylserine binding" annotation; the authors only suggest a physiological role.

**Substrate specificity of the activity Ada2 supports:** SAGA preferentially acetylates histone H3 (K9, K14, K18, K23) and H2B; the ADA complex acetylates nucleosomal H3 (K14, K18) and H2B (Grant et al. 1997, PMID:9224714; Grant et al. 1999, PMID:10026213; per UniProt).

## 2. Structural role: tethering the HAT module to SAGA

- **SWIRM domain as tether.** The SWIRM domain is required for the HAT module to join SAGA, but not for assembly of the ADA complex. Deleting it leaves Ada2 bound to the other HAT subunits but nearly eliminates association with core SAGA proteins ([Haile et al. 2023, BBA Gene Regul Mech](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10226619/)).
- **Effect on activity.** In the isolated Gcn5/Ada2/Ada3 module, SWIRM deletion modestly increases HAT activity and has negligible effect on nucleosome binding. Loss of the HAT module from SAGA reduces SAGA's H2B deubiquitinating activity (same study).
- **Cryo-EM.** Yeast SAGA structures resolve the core and Tra1 modules at about 3.3 Å, but the HAT module is flexible (about 9 Å) and could not be modelled ([Wang et al. 2020, Nature 577:717](https://pmc.ncbi.nlm.nih.gov/articles/PMC6994259); Papai et al. 2020, Nature (from memory)). SAGA adopts a range of conformations with the HAT module in different orientations ([Vasyliuk et al. 2022, Sci Rep](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9296673/)).
- **First resolved HAT module.** A 2025 structure of *Chaetomium thermophilum* SAGA resolves three of four HAT subunits at 3.7 Å: Gcn5 is nested between Ada2 and Ada3, and the Ada2 SWIRM domain contacts Ada3 and the N-terminal region of Ada1 ([Molecular Cell 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/)). This is an ortholog, not the yeast protein.
- **DNA binding by SWIRM.** The human ADA2α SWIRM domain binds double-stranded and nucleosomal DNA (Qian et al. 2005, Nat Struct Mol Biol; [PDB 2AQE](https://proteopedia.org/w/2aqe)). This is ortholog evidence; for yeast, the Haile data argue the SWIRM is not needed for nucleosome binding by the module.

## 3. Complexes

| Complex | Size | Composition relevant to Ada2 | Source |
|---|---|---|---|
| SAGA | 1.8 MDa, 19 subunits | HAT module plus DUB, core/TAF and Tra1/SPT modules | PMID:9224714, 9674426, 9885573, 25216679 |
| SLIK/SALSA | SAGA variant | Truncated Spt7, no Spt8; structurally and biochemically equivalent to SAGA | PMID:12446794, 12186975, 33864814 |
| ADA | 0.8 MDa | Ada2, Ada3, Gcn5, Sgf29, Ahc1, Ahc2; distinct from SAGA | PMID:10490601, 21734642 |

IntAct lists high-count interactions with Gcn5, Ngg1/Ada3, Hfi1/Ada1 and Tra1 (UniProt).

## 4. Biological process and pathway role

- **RNA polymerase II transcription coactivation.** SAGA is recruited by activators to upstream activating sequences, acetylates promoter nucleosomes, and supports pre-initiation complex assembly. It acts as a general cofactor for essentially all Pol II transcription (Baptista et al. 2017, PMID:28918903; Lee et al. 2000, PMID:10864329). Ada2's contribution is the HAT arm.
- **Direct activator contact (older model).** The Ada2 N-terminus binds the VP16 activation domain (Silverman et al. 1994, PMID:7972120), and Ada2 was reported to associate with the VP16 and Gcn4 activation domains and with TBP ([Barlev et al. 1995, PMID:7642611](https://www.yeastgenome.org/reference/7642611)). Current models place activator binding mainly on Tra1 and TBP delivery on Spt3/Spt8, so these in vitro contacts are probably not Ada2's main mechanism (this weighting is my assessment).
- **Silencing.** Ada2 promotes silencing at telomeres and rDNA. It binds telomeric chromatin and Sir2 in vivo; loss of ADA2 causes Sir2/Sir3 spreading into subtelomeric regions and decreased H4K16 acetylation ([Jacobson & Pillus 2009, PMID:19737915](https://pmc.ncbi.nlm.nih.gov/articles/PMC2702157)). This is a secondary role resting on a single study.
- **DNA damage.** GO carries IMP annotations for DNA damage response (PMID:15340070) and sister-chromatid double-strand break repair (PMID:23357952). These are likely indirect consequences of losing Gcn5-dependent acetylation. Note that PMID:15340070 is titled as a *Drosophila* Ada2b paper, so the yeast phenotype attribution deserves a full-text check.

## 5. Localization

Ada2 is nuclear and acts on chromatin, at promoters/UAS regions as part of SAGA and at subtelomeric chromatin (ChIP; PMID:19737915). The nuclear GO annotations are NAS/IBA/IEA rather than direct imaging. Abundance is about 1,720 molecules per cell in log phase (Ghaemmaghami et al. 2003, PMID:14562106).

## 6. Summary for annotation

- **Core molecular function:** activator of Gcn5 histone acetyltransferase activity (enhancing acetyl-CoA binding) and structural adaptor anchoring the HAT module in SAGA. "Transcription coactivator activity" is the fitting existing term; an enzyme-activator term would capture the mechanism more precisely.
- **Core process:** histone H3 acetylation-dependent regulation of Pol II transcription.
- **Core location:** nucleus/chromatin, in the SAGA, SLIK and ADA complexes.
- **Peripheral or weakly supported:** phosphatidylserine binding (in vitro), telomeric and rDNA silencing, DNA damage and repair roles, zinc binding (structural, ZZ finger).

## Open questions

- No high-resolution structure exists of the yeast HAT module on a nucleosome.
- The function of the ZZ finger beyond Gcn5 binding is undefined.
- The in vivo relevance of phospholipid binding is untested.
- Whether the silencing role is independent of Gcn5 needs confirmation.

## Sources

- [Sun et al. 2018, PNAS (PMC6176591)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6176591)
- [PDB 6CW3 (Proteopedia)](https://proteopedia.org/wiki/index.php/6cw3)
- [Haile et al. 2023 (PMC10226619)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10226619/)
- [Wang et al. 2020, Nature (PMC6994259)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6994259)
- [Vasyliuk et al. 2022, Sci Rep (PMC9296673)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9296673/)
- [SAGA structure including HAT module, Mol Cell 2025 (PMC12768303)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/)
- [Hoke et al. 2008 (PubMed 18950642)](https://www.pubmed.gov/18950642/)
- [Jacobson & Pillus 2009 (PMC2702157)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2702157)
- [Balasubramanian et al. 2002 (SGD)](https://www.yeastgenome.org/reference/11773077)
- [Balasubramanian et al. 2002 (Penn State record)](https://pure.psu.edu/en/publications/role-of-the-ada2-and-ada3-transcriptional-coactivators-in-histone/)
- [Sterner et al. 2002 (SGD)](https://www.yeastgenome.org/reference/S000074947)
- [Boyer et al. 2002 (Penn State record)](https://pure.psu.edu/en/publications/essential-role-for-the-sant-domain-in-the-functioning-of-multiple/)
- [Candau & Berger 1996 (abstract)](https://www.scilit.net/publications/ca60e5a83bf817d43379ced732bf5db5)
- [Barlev et al. 1995 (SGD)](https://www.yeastgenome.org/reference/7642611)
- [PDB 2AQE, human ADA2α SWIRM (Proteopedia)](https://proteopedia.org/w/2aqe)
- UniProt Q02336 and the SGD gene description (local copies in `genes/yeast/ADA2/`)

## Citations

1. https://www.scilit.net/publications/ca60e5a83bf817d43379ced732bf5db5
2. https://www.yeastgenome.org/reference/11773077
3. https://pure.psu.edu/en/publications/essential-role-for-the-sant-domain-in-the-functioning-of-multiple/
4. https://www.yeastgenome.org/reference/S000074947
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6176591
6. https://www.pubmed.gov/18950642/
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10226619/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC6994259
9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9296673/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC12768303/
11. https://proteopedia.org/w/2aqe
12. https://www.yeastgenome.org/reference/7642611
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC2702157
14. https://proteopedia.org/wiki/index.php/6cw3
15. https://pure.psu.edu/en/publications/role-of-the-ada2-and-ada3-transcriptional-coactivators-in-histone/