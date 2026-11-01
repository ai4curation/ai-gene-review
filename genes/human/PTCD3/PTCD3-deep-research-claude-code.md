---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:19:39.980669'
end_time: '2026-10-14T23:20:22.064850'
duration_seconds: 42.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PTCD3
  gene_symbol: PTCD3
  uniprot_accession: Q96EY7
  protein_description: 'RecName: Full=Small ribosomal subunit protein mS39 {ECO:0000303|PubMed:25838379};
    AltName: Full=28S ribosomal protein S39, mitochondrial; Short=MRP-S39; AltName:
    Full=Pentatricopeptide repeat domain-containing protein 3, mitochondrial; AltName:
    Full=Transformation-related gene 15 protein; Short=TRG-15; Flags: Precursor;'
  gene_info: Name=PTCD3; Synonyms=MRPS39; ORFNames=TRG15;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the mitochondrion-specific ribosomal protein
  protein_domains: PPR_rpt. (IPR002885); PTCD3. (IPR037387); Rib_mS39_PPR. (IPR055063);
    TPR-like_helical_dom_sf. (IPR011990); PPR_3 (PF13812)
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 6
  total_cost_usd: 0.2317435
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96EY7
- **Protein Description:** RecName: Full=Small ribosomal subunit protein mS39 {ECO:0000303|PubMed:25838379}; AltName: Full=28S ribosomal protein S39, mitochondrial; Short=MRP-S39; AltName: Full=Pentatricopeptide repeat domain-containing protein 3, mitochondrial; AltName: Full=Transformation-related gene 15 protein; Short=TRG-15; Flags: Precursor;
- **Gene Information:** Name=PTCD3; Synonyms=MRPS39; ORFNames=TRG15;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the mitochondrion-specific ribosomal protein
- **Key Domains:** PPR_rpt. (IPR002885); PTCD3. (IPR037387); Rib_mS39_PPR. (IPR055063); TPR-like_helical_dom_sf. (IPR011990); PPR_3 (PF13812)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PTCD3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PTCD3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PTCD3** (gene ID: PTCD3, UniProt: Q96EY7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PTCD3 (MRPS39, mS39; UniProt Q96EY7), human: research report

## 0. Identity check
- **Match:** The symbol, protein name and organism all agree. PTCD3 (synonyms MRPS39, TRG15) is "Small ribosomal subunit protein mS39 / 28S ribosomal protein S39, mitochondrial / Pentatricopeptide repeat domain-containing protein 3", from *Homo sapiens*, and it carries PPR repeat domains (UniProt Q96EY7 record, local file `PTCD3-uniprot.txt`).
- **Not ambiguous:** I found no competing gene with the same symbol.
- **Sources and limits:**
  - The UniProt flat file is read directly.
  - Search results are cited as retrieved. I did not retrieve full texts of the primary papers, so experimental details below are secondary-sourced unless marked otherwise.
  - Items marked ⚠ need checking against the primary paper before they go into a review.

## 1. Summary
PTCD3 is a mitochondria-specific structural protein of the small (28S) subunit of the mitochondrial ribosome, the mitoribosome. It was first characterized as a PPR-domain RNA-binding protein that regulates mitochondrial translation. Structural work places it at the mRNA entry channel, where it binds single-stranded mRNA and docks the LRPPRC–SLIRP mRNA-delivery module. Its loss causes a generalized mitochondrial translation defect with combined OXPHOS deficiency (COXPD51).

## 2. Molecular function
- **Function in UniProt:** "Mitochondrial RNA-binding protein that has a role in mitochondrial translation" (UniProt CC FUNCTION, citing PMID:19427859).
- **Founding study:** Davies et al. 2009 (PMID:19427859, the paper UniProt cites for the function line) investigated the uncharacterized PPR protein PTCD3. They showed it is a mitochondrial protein that associates with the small subunit of mitochondrial ribosomes, and they framed it against plant PPR proteins, which control stability and translation of organellar transcripts. The title is "Pentatricopeptide repeat domain protein 3 associates with the mitochondrial small ribosomal subunit and regulates translation" ([UWA repository record](https://research-repository.uwa.edu.au/en/publications/pentatricopeptide-repeat-domain-protein-3-associates-with-the-mit/)). The snippets I retrieved did not give the assay details.
- **Knockdown phenotype:** In 143B osteosarcoma cells, PTCD3 knockdown decreased mitochondrial protein synthesis, respiration, and Complex III and IV activity without changing mitochondrial mRNA levels. This points to a translational rather than RNA-processing role ([search summary of the primary data](https://affinage.wi.mit.edu/gene/PTCD3); ⚠ check against PMID:19427859).
- **Structural role:**
  - mS39 is part of the 28S subunit. UniProt describes it as a component of the mt-SSU, associated with the 12S mt-rRNA (PMID:19427859, PMID:23908630, PMID:25838379, per UniProt CC SUBUNIT).
  - The 28S subunit contains the 12S rRNA and 30 proteins.
  - mS39 forms the mRNA entry channel and binds single-stranded mRNA ([affinage.wi.mit.edu](https://affinage.wi.mit.edu/gene/MS39), a secondary summary).
- **Interaction with the LRPPRC–SLIRP module:**
  - The 2020 eLife human mitoribosome structure (["Structural basis of mitochondrial translation"](https://elifesciences.org/articles/58362/peer-reviews)) reported an extra density on mS39 that correlated with well-resolved mRNA. Mass spectrometry of the cryo-EM sample suggested the density is an LRPPRC–SLIRP heterodimer.
  - A later preprint ([bioRxiv 2022.06.20.496763](https://www.biorxiv.org/content/10.1101/2022.06.20.496763.full.pdf)) reports that LRPPRC binds mS31 and mS39 through a ring-like structure, forming a corridor that hands mRNA from SLIRP to the ribosome. It also identifies arginines involved in mRNA binding at the interface.
  - So the mS39 PPR domain probably acts as a docking and handoff surface for mRNA, particularly leaderless mt-mRNAs. This is inferred from the structures; I did not find direct biochemical proof of mRNA binding by purified mS39.
- **Catalytic activity:** None. It is a structural and RNA-binding ribosomal protein.

## 3. Localization
- **Compartment:** Mitochondrion, specifically the matrix, bound to the mitochondrial ribosome. The N-terminal 1–37 is a transit peptide, and the mature chain is residues 38–689 (UniProt FT TRANSIT/CHAIN).
- **Evidence:** Experimental localization is cited to PMID:19427859 and PMID:23908630 (UniProt CC SUBCELLULAR LOCATION). GOA includes mitochondrial matrix (IDA, FlyBase) and mitochondrial inner membrane (TAS, Reactome). The inner-membrane term reflects the mitoribosome's association with the membrane; I did not verify the evidence behind it.
- **Tissue:** Abundant in testis, skeletal muscle and heart (UniProt, PMID:19427859).

## 4. Pathway and process
- **Process:** Mitochondrial translation. The mitoribosome synthesizes the 13 mtDNA-encoded OXPHOS subunits, so PTCD3 acts upstream of Complexes I, III, IV and V.
- **Existing GOA terms** (from the UniProt record):

| GO term | Evidence | Comment |
|---|---|---|
| mitochondrial translation (GO:0032543) | IMP | Consistent with knockdown and patient-cell data. |
| mitochondrial small ribosomal subunit (GO:0005763) | NAS, ComplexPortal | Core localization. |
| rRNA binding (GO:0019843) | IDA | Consistent with association with 12S rRNA. |
| RNA binding (GO:0003723) | HDA | Consistent with the PPR/entry-channel role. |
| ribosomal small subunit binding (GO:0043024) | IDA | Probably redundant with being a subunit component. |
| mitochondrion (GO:0005739) | IDA | Parent of the more specific terms. |
| mitochondrial matrix (GO:0005759) | IDA, FlyBase | See Section 3. |
| mitochondrial inner membrane (GO:0005743) | TAS, Reactome | See Section 3. |

- **Suggested annotation reading:** The best-supported core function is structural constituent of ribosome (GO:0003735) in the mitochondrial small subunit, plus mRNA and rRNA binding. mS39 is a constituent of the mt-SSU, so "ribosomal small subunit binding" is better treated as non-core or redundant.

## 5. Disease
- **COXPD51 (MIM:619057):** Autosomal recessive. Features are intrauterine growth retardation, poor growth, progressive limb rigidity, delayed psychomotor development, hearing loss and optic atrophy, with basal ganglia and brainstem abnormalities on imaging. Patient cells show decreased Complex I and IV levels and activities and generalized mitochondrial translation defects (UniProt, PMID:30607703).
- **Likely source paper:** A database entry lists "Mitochondrial ribosomal protein PTCD3 mutations cause oxidative phosphorylation defects with Leigh syndrome", *Neurogenetics* 2019, 20:9–25 ([GlycoSmos DOID:0112137](https://glycosmos.org/diseases/DOID:0112137)). ⚠ I did not confirm that this is PMID:30607703 or its authorship. Verify before citing.
- **Mechanism:** A defect in the mitoribosome's mRNA-handling subunit gives global loss of mtDNA-encoded proteins, with Complex I and IV most affected.

## 6. Evidence quality and gaps
- **Strong:**
  - Mitoribosome association and a translation role, from knockdown and patient-cell studies and cryo-EM.
  - The disease link.
- **Inferential:** The mRNA-handoff mechanism and the specific RNA-binding residues. These come from structures, with a preprint for the LRPPRC–SLIRP details.
- **Unverified by me:**
  - Full texts of PMID:19427859, PMID:23908630, PMID:25838379 and PMID:30607703.
  - Whether the dual role in translation initiation and mRNA delivery is direct or indirect.
- **Possible experiments:**
  - In vitro RNA-binding assays with mutated entry-channel arginines.
  - Ribosome profiling in PTCD3-deficient cells to see which mRNAs depend on the mS39 docking site.

## Sources
- UniProt Q96EY7 record (local `PTCD3-uniprot.txt`)
- [Davies et al. 2009 record (UWA repository), PMID:19427859](https://research-repository.uwa.edu.au/en/publications/pentatricopeptide-repeat-domain-protein-3-associates-with-the-mit/)
- [eLife: Structural basis of mitochondrial translation (2020)](https://elifesciences.org/articles/58362/peer-reviews)
- [bioRxiv: Structural basis of LRPPRC-SLIRP-dependent translation by the mitoribosome](https://www.biorxiv.org/content/10.1101/2022.06.20.496763.full.pdf)
- [PTCD3 summary](https://affinage.wi.mit.edu/gene/PTCD3) and [mS39 summary](https://affinage.wi.mit.edu/gene/MS39) (secondary, auto-generated)
- [GlycoSmos COXPD51 entry](https://glycosmos.org/diseases/DOID:0112137)
- [GeneCards PTCD3](https://www.genecards.org/card/PTCD3)

## Citations

1. https://research-repository.uwa.edu.au/en/publications/pentatricopeptide-repeat-domain-protein-3-associates-with-the-mit/
2. https://affinage.wi.mit.edu/gene/PTCD3
3. https://affinage.wi.mit.edu/gene/MS39
4. https://elifesciences.org/articles/58362/peer-reviews
5. https://www.biorxiv.org/content/10.1101/2022.06.20.496763.full.pdf
6. https://glycosmos.org/diseases/DOID:0112137
7. https://www.genecards.org/card/PTCD3