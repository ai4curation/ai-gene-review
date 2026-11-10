---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T04:27:52.776619'
end_time: '2026-10-24T04:28:31.826707'
duration_seconds: 39.05
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MTIF2
  gene_symbol: MTIF2
  uniprot_accession: P46199
  protein_description: 'RecName: Full=Translation initiation factor IF-2, mitochondrial;
    Short=IF-2(Mt); Short=IF-2Mt; Short=IF2(mt); Flags: Precursor;'
  gene_info: Name=MTIF2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TRAFAC class translation factor GTPase
  protein_domains: EF-G-like_DII. (IPR053905); IF2_II. (IPR044145); P-loop_NTPase.
    (IPR027417); Small_GTP-bd. (IPR005225); T_Tr_GTP-bd_dom. (IPR000795)
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
  num_turns: 5
  total_cost_usd: 0.3239872
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P46199
- **Protein Description:** RecName: Full=Translation initiation factor IF-2, mitochondrial; Short=IF-2(Mt); Short=IF-2Mt; Short=IF2(mt); Flags: Precursor;
- **Gene Information:** Name=MTIF2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TRAFAC class translation factor GTPase
- **Key Domains:** EF-G-like_DII. (IPR053905); IF2_II. (IPR044145); P-loop_NTPase. (IPR027417); Small_GTP-bd. (IPR005225); T_Tr_GTP-bd_dom. (IPR000795)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MTIF2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MTIF2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MTIF2** (gene ID: MTIF2, UniProt: P46199) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MTIF2 (UniProt P46199), human mitochondrial translation initiation factor 2 (IF-2mt)

## Identity check
- The symbol, protein name and organism match. MTIF2 encodes "Translation initiation factor IF-2, mitochondrial" (IF-2mt, mtIF2) in *Homo sapiens*. The gene is on chromosome 2p16.1.
- The UniProt domains (P-loop NTPase, small GTP-binding domain, IF2 domain II) and the "TRAFAC class translation factor GTPase" family fit the bacterial IF-2 lineage. No ambiguity with a different gene was found.
- Evidence level: the first-pass searches returned abstracts, PDB records and secondary summaries, not full texts. Quoted details are limited to what those sources show. Anything I could not confirm is marked.

## Primary function
- MTIF2 is a GTPase that acts as the main initiation factor of the mitochondrial ribosome (mitoribosome).
- It binds the formylated initiator tRNA (fMet-tRNA^Met) and positions it in the P-site of the small (28S) subunit on the start codon. It then promotes joining of the large (39S) subunit to form the 55S initiation complex.
- GTP hydrolysis by mtIF2 follows subunit joining. This is the standard bacterial IF-2 mechanism, which I am describing from the family homology and not from a source checked here.
- It is not an enzyme in the metabolic sense. The only reaction is GTP → GDP + Pi, which gates the release of the factor from the ribosome.
- Substrate specificity: the 2018 cryo-EM paper reports "unique features of mtIF2 that are required for specific recognition of fMet–tRNAMet and regulation of its GTPase activity" ([Kummer et al. 2018, PMID:30089917](https://pubmed.ncbi.nlm.nih.gov/30089917/)).

### Why mitochondria need this factor in a special form
- Mammalian mitochondrial translation initiation lacks IF-1, which is essential in all other translation systems from bacteria to mammals.
- Only one type of tRNA^Met serves both initiation and elongation. mtIF2 therefore has to discriminate the formylated initiator from the same tRNA used in elongation.
- The cryo-EM work identified an extra domain insertion in mtIF2. It closes the decoding centre, "stabilizes the binding of leaderless mRNAs and induces conformational changes in the rRNA nucleotides involved in decoding."
- A secondary preprint describes the insertion as about 37 residues, an α-helix between domains II and III, first noted in bovine mtIF2. It may play a role similar to bacterial IF-1. This is less authoritative than the primary paper.
- Most mitochondrial mRNAs have no 5′ leader, so this mtIF2 feature matters for how they are recognised.
- Same paper, side finding: the N-terminal portion of mL45 blocks the ribosomal tunnel during initiation. This may help target mitoribosomes to the inner membrane.

## Gene and protein
- Ma & Spremulli cloned the human cDNA ([PMID:7829522, J Biol Chem 270:1859–1865, 1995](https://purl.uniprot.org/citations/7829522)).
- Per the search summary of that paper, the cDNAs came from liver, heart and fetal brain libraries and encode a 727-residue protein with a 29-residue presequence.
- Identity with prokaryotic IF-2 is about 30–40%. The G-domain is the most conserved region.
- Human IF-2mt is no more similar to the yeast mitochondrial factor than to bacterial IF-2s.
- I did not retrieve the full text, so these details come from search summaries. The "2181 residues" figure in the abstract is probably a nucleotide count, not a residue count.

## Localization
- MTIF2 is encoded in the nucleus and imported into mitochondria. The "Precursor" flag and the N-terminal presequence indicate import and cleavage in the matrix.
- It acts in the mitochondrial matrix, associated with the 28S small subunit and the 55S monosome.
- The 2018 complex structure (PDB [6GAW](https://rcsb.org/structure/6GAW), 55S; [6GAZ](https://rcsb.org/structure/6gaz), 28S with IF-2; [6GB2](https://www.rcsb.org/structure/6gb2), 39S) places mtIF2 on the initiating mitoribosome. DOI: 10.1038/s41586-018-0373-y.

## Pathway context
- The pathway is mitochondrial translation initiation (GO: mitochondrial translational initiation), which feeds synthesis of the 13 mtDNA-encoded OXPHOS subunits.
- A later structural study (PDB [9OJM](https://www.rcsb.org/structure/9OJM), bioRxiv preprint, [Choreography of human mitochondrial leaderless mRNA translation initiation](https://www.biorxiv.org/content/10.1101/2025.07.10.662049.full.pdf)) reports two parallel pathways for leaderless mRNA:
  - In one, mRNA loads onto the 28S subunit before the 39S subunit joins.
  - In the other, a preassembled 55S monosome loads directly.
  - The preprint reports that mtIF3 suppresses the monosome-loading route.
  - This is a preprint and was seen only through its search summary.
- Related work: [Distinct pre-initiation steps in human mitochondrial translation (PMC7287080)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7287080/) and [Translation initiation of leaderless and polycistronic transcripts in mammalian mitochondria (PMC9881170)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9881170/). I did not read these.
- The partner factor in initiation is mtIF3 (MTIF3). The 2018 structure shows mtIF3 on the 28S subunit, but I did not confirm its exact role in that paper.

## Suggested GO annotation implications
- **Molecular function:** translation initiation factor activity (GO:0003743) and GTPase activity (GO:0003924). Also GTP binding and fMet-tRNA binding. Use specific terms and avoid generic "protein binding".
- **Process:** mitochondrial translational initiation.
- **Location:** mitochondrial matrix, with association to the mitochondrial small ribosomal subunit and the monosome.
- **Evidence grade:** experimental support comes from the cDNA cloning work and the cryo-EM structure. The existing GO annotations should be checked against these two papers before any are changed.
- **Not established:** I found nothing here that supports a process role beyond translation initiation, such as a direct role in disease. Disease associations were not researched.

## Gaps and caveats
- I did not find or read a primary biochemical paper showing GTP-dependent fMet-tRNA binding by human mtIF2 in vitro. The Spremulli lab has published on this, but I did not verify any citation, so none is given.
- Not checked: disease variants, expression regulation and post-translational modification.
- Statements about IF-2 mechanism beyond the cited sources rest on bacterial homology.

## Sources
- [Kummer et al., Nature 2018, PMID:30089917](https://pubmed.ncbi.nlm.nih.gov/30089917/)
- [Ma & Spremulli, J Biol Chem 1995, PMID:7829522 (UniProt citation record)](https://purl.uniprot.org/citations/7829522)
- PDB entries [6GAW](https://rcsb.org/structure/6GAW), [6GAZ](https://rcsb.org/structure/6gaz), [6GB2](https://www.rcsb.org/structure/6gb2) and [9OJM](https://www.rcsb.org/structure/9OJM)
- [bioRxiv: Choreography of human mitochondrial leaderless mRNA translation initiation](https://www.biorxiv.org/content/10.1101/2025.07.10.662049.full.pdf)
- [PMC7287080](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7287080/) and [PMC9881170](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9881170/)

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/30089917/
2. https://purl.uniprot.org/citations/7829522
3. https://rcsb.org/structure/6GAW
4. https://rcsb.org/structure/6gaz
5. https://www.rcsb.org/structure/6gb2
6. https://www.rcsb.org/structure/9OJM
7. https://www.biorxiv.org/content/10.1101/2025.07.10.662049.full.pdf
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7287080/
9. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9881170/