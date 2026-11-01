---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:18:08.830270'
end_time: '2026-10-14T23:18:46.767066'
duration_seconds: 37.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MRPS7
  gene_symbol: MRPS7
  uniprot_accession: Q9Y2R9
  protein_description: 'RecName: Full=Small ribosomal subunit protein uS7m {ECO:0000303|PubMed:25838379};
    AltName: Full=28S ribosomal protein S7, mitochondrial; Short=MRP-S7; Short=S7mt;
    AltName: Full=bMRP-27a; Short=bMRP27a; Flags: Precursor;'
  gene_info: Name=MRPS7;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the universal ribosomal protein uS7 family.
  protein_domains: Ribosomal_uS7. (IPR000235); Ribosomal_uS7_dom. (IPR023798); Ribosomal_uS7_dom_sf.
    (IPR036823); Ribosomal_S7 (PF00177)
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
  web_search_requests: 2
  num_turns: 5
  total_cost_usd: 0.2099462
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 5
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9Y2R9
- **Protein Description:** RecName: Full=Small ribosomal subunit protein uS7m {ECO:0000303|PubMed:25838379}; AltName: Full=28S ribosomal protein S7, mitochondrial; Short=MRP-S7; Short=S7mt; AltName: Full=bMRP-27a; Short=bMRP27a; Flags: Precursor;
- **Gene Information:** Name=MRPS7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the universal ribosomal protein uS7 family.
- **Key Domains:** Ribosomal_uS7. (IPR000235); Ribosomal_uS7_dom. (IPR023798); Ribosomal_uS7_dom_sf. (IPR036823); Ribosomal_S7 (PF00177)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MRPS7" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MRPS7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MRPS7** (gene ID: MRPS7, UniProt: Q9Y2R9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MRPS7 (Q9Y2R9), human mitochondrial small ribosomal subunit protein uS7m: research report

One note on the research: the second web search result ended with a line telling me to include its sources as hyperlinks. That text came from the tool output, not from you, so I did not treat it as an instruction. I cite sources here because the task requires it.

## 1. Identity check

- The symbol MRPS7 matches the UniProt record: Q9Y2R9, *Homo sapiens*, "Small ribosomal subunit protein uS7m" (also MRP-S7, S7mt, bMRP27a). It carries a precursor flag, meaning it has an N-terminal mitochondrial targeting sequence.
- The domains are Ribosomal_uS7 (IPR000235, PF00177), and the family is universal ribosomal protein uS7. This fits the literature on the mitoribosome and on MRPS7, so there is no ambiguity.
- Sources are the local record `MRPS7-uniprot.txt` (UniProt, current as of the fetch) and the web searches below.

## 2. Primary function: structural constituent of the mitochondrial ribosome

MRPS7 is a core structural protein of the mitochondrial small (28S) ribosomal subunit. UniProt states that the 28S subunit contains the 12S mt-rRNA and 30 different proteins. It states that the mature 55S mitoribosome has a 28S and a 39S subunit, and that the mitoribosome is "essential for mitochondrial protein synthesis" [UniProt Q9Y2R9, citing PMID:25556185 and PMID:25838379].

- **No catalytic activity.** MRPS7 is a ribosomal protein, not an enzyme. Its role is to bind the 12S rRNA and help build and stabilise the 28S subunit. The subunit then decodes mt-mRNAs and makes the 13 mtDNA-encoded OXPHOS subunits.
- **Structural evidence.** The cryo-EM structure of the intact human mitoribosome (Amunts et al., Science 2015, 348:95–98, PMID:25838379) resolved the complex at 3.5 Å. It described 80 interconnected proteins, 36 of them mitochondria-specific, and three rRNAs. It also described a remodelled small-subunit head and mRNA channel. This is the source UniProt uses for MRPS7's subunit membership and mitochondrial location ([web summary of the structure](https://www.rcsb.org/structure/3J9M); PDB 3J9M).
- **Inference.** The uS7 family is universal. In bacteria, S7 binds the 3′ domain of 16S rRNA, helps initiate head assembly, and sits at the mRNA exit side of the small subunit. By homology, uS7m likely does the same job on the 12S rRNA in the head. I did not verify the specific rRNA contacts or the position of MRPS7 in the mitoribosome from the structure paper.
- **GO fit.** The annotations "structural constituent of ribosome" and "rRNA binding" fit this role. "RNA binding" from a high-throughput (HDA) source is non-specific and redundant with rRNA binding.

## 3. Localization

- MRPS7 is a nuclear-encoded protein imported into the mitochondrial matrix. There it forms part of the mitochondrial small subunit [UniProt Q9Y2R9: "Mitochondrion", PMID:25838379].
- The mitoribosome is tethered to the inner membrane, which is why GO also carries a mitochondrial inner membrane term. It is an association of the ribosome, not an integral membrane protein, and it comes only from a Reactome TAS annotation.

## 4. Pathway

- **Mitochondrial translation.** This covers initiation, elongation and termination of the 13 mtDNA-encoded OXPHOS polypeptides. MRPS7 participates as a structural part of the machine, not as a regulator.
- **Mitoribosome assembly.** Assembly of the small subunit is the upstream step. MRPS7 is a component of the assembled subunit.
- **Downstream effects.** Loss of function reduces complexes I, III, IV and V, because all contain mtDNA-encoded subunits. Complex II is unaffected, since it is fully nuclear-encoded.

## 5. Disease evidence (functional validation)

- **Disease.** Combined oxidative phosphorylation deficiency 34 (COXPD34, MIM 617872) is autosomal recessive. It involves combined deficiencies of complexes I, III and IV. Clinical features include congenital sensorineural deafness, lactic acidemia, and progressive hepatic and renal failure [UniProt Q9Y2R9, citing PMID:25556185].
- **The original report.** Menezes et al. (Hum Mol Genet 2015, PMID:25556185) found a homozygous c.550A>G (p.Met184Val) variant by exome sequencing in two affected siblings, with impaired mitochondrial protein synthesis in patient cells ([Sigma-Aldrich listing of the paper](https://www.sigmaaldrich.com/AT/de/tech-docs/paper/584716); [OMIM 611974](https://ncbi.nlm.nih.gov/omim/611974)).
- **Strength of evidence.** Curated gene panels list the gene as moderate evidence, based on a single reported family ([PanelApp Australia](https://panelapp-aus.org/panels/3166/gene/MRPS7/)). Primary ovarian insufficiency has also been added as a possible phenotype in one panel. I did not review follow-up reports, so I cannot say whether more patients exist.
- **What this shows.** A hypomorphic missense variant in a core mitoribosomal protein compromises translation. That supports the structural role, because the phenotype matches loss of mitochondrial translation capacity.
- **Source gap.** I relied on database and listing summaries for this paper, not its full text. Details such as protein levels and rescue experiments should be taken from the paper itself.

## 6. Current GOA annotations (from the UniProt cross-references)

| GO term | Evidence | Assessment |
|---|---|---|
| mitochondrial small ribosomal subunit (GO:0005763), IDA | UniProtKB | Core and supported by the structure and patient data. |
| structural constituent of ribosome (GO:0003735), ISS | UniProtKB | Core molecular function. |
| mitochondrial translation (GO:0032543), ISS | UniProtKB | Core process. |
| rRNA binding (GO:0019843), IBA | GO_Central | Reasonable and consistent with the uS7 family. |
| translation (GO:0006412), IBA | GO_Central | Correct but less specific than mitochondrial translation. |
| ribosome (GO:0005840), IBA | GO_Central | Redundant with the more specific small subunit term. |
| mitochondrion (GO:0005739), EXP | UniProtKB | Correct but general. |
| RNA binding (GO:0003723), HDA | UniProtKB | Non-specific, redundant with rRNA binding. |
| mitochondrial inner membrane (GO:0005743), TAS | Reactome | Peripheral association via the membrane-bound ribosome. |

## 7. Summary

MRPS7 (uS7m) is a nuclear-encoded, matrix-imported structural protein of the 28S small subunit of the human mitoribosome. It binds 12S mt-rRNA and supports mitochondrial translation of the OXPHOS subunits encoded by mtDNA. It has no known catalytic activity. Evidence comes from the cryo-EM mitoribosome structure (PMID:25838379), the family homology to bacterial S7, and a recessive disease variant that causes combined OXPHOS deficiency (PMID:25556185).

## Sources

- UniProt Q9Y2R9, local file `MRPS7-uniprot.txt` (PMID:25556185, PMID:25838379)
- [RCSB PDB 3J9M, human mitoribosome (Amunts et al. 2015)](https://www.rcsb.org/structure/3J9M)
- [Menezes et al. 2015, Hum Mol Genet, summary listing](https://www.sigmaaldrich.com/AT/de/tech-docs/paper/584716)
- [OMIM 611974, MRPS7](https://ncbi.nlm.nih.gov/omim/611974)
- [PanelApp Australia, MRPS7](https://panelapp-aus.org/panels/3166/gene/MRPS7/)
- [Disease Ontology DOID:0111497, COXPD34](https://disease-ontology.org/term/DOID:0111497)

## Citations

1. https://www.rcsb.org/structure/3J9M
2. https://www.sigmaaldrich.com/AT/de/tech-docs/paper/584716
3. https://ncbi.nlm.nih.gov/omim/611974
4. https://panelapp-aus.org/panels/3166/gene/MRPS7/
5. https://disease-ontology.org/term/DOID:0111497