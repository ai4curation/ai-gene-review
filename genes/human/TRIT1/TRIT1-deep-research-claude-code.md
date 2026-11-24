---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:20:26.703066'
end_time: '2026-10-14T23:21:09.142045'
duration_seconds: 42.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TRIT1
  gene_symbol: TRIT1
  uniprot_accession: Q9H3H1
  protein_description: 'RecName: Full=tRNA dimethylallyltransferase; EC=2.5.1.75 {ECO:0000269|PubMed:24901367};
    AltName: Full=Isopentenyl-diphosphate:tRNA isopentenyltransferase; Short=IPP transferase;
    Short=IPPT; AltName: Full=hGRO1; AltName: Full=tRNA isopentenyltransferase 1;
    Short=IPTase; Flags: Precursor;'
  gene_info: Name=TRIT1; Synonyms=IPT, MOD5;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the IPP transferase family. .
  protein_domains: Dimethylallyltransferase. (IPR039657); IPP_transferase_euk. (IPR030666);
    IPT. (IPR018022); Matrin/U1-like-C_Znf_C2H2. (IPR003604); P-loop_NTPase. (IPR027417)
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
  num_turns: 4
  total_cost_usd: 0.20692320000000003
  session_id: d59b2dca-3995-59ba-98f7-69e97fb62d6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 4
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9H3H1
- **Protein Description:** RecName: Full=tRNA dimethylallyltransferase; EC=2.5.1.75 {ECO:0000269|PubMed:24901367}; AltName: Full=Isopentenyl-diphosphate:tRNA isopentenyltransferase; Short=IPP transferase; Short=IPPT; AltName: Full=hGRO1; AltName: Full=tRNA isopentenyltransferase 1; Short=IPTase; Flags: Precursor;
- **Gene Information:** Name=TRIT1; Synonyms=IPT, MOD5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the IPP transferase family. .
- **Key Domains:** Dimethylallyltransferase. (IPR039657); IPP_transferase_euk. (IPR030666); IPT. (IPR018022); Matrin/U1-like-C_Znf_C2H2. (IPR003604); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TRIT1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TRIT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TRIT1** (gene ID: TRIT1, UniProt: Q9H3H1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TRIT1 (human tRNA dimethylallyltransferase, Q9H3H1): research report

## 0. Identity check

The gene symbol, protein name, family and domains all match.
- UniProt Q9H3H1 is TRIT1 (synonyms IPT, MOD5), *Homo sapiens*, EC 2.5.1.75, "tRNA dimethylallyltransferase". It is in the IPP transferase family, with an IPT domain, a P-loop NTPase fold and a C-terminal C2H2 zinc finger.
- Alternative names are isopentenyl-diphosphate:tRNA isopentenyltransferase (IPPT) and hGRO1. "hGRO1" comes from the UniProt record. It is the original cloned name of the human homolog of yeast *MOD5* and *E. coli* MiaA.
- The literature found is on the correct gene. This report rests on a limited search. The PLoS Genetics 2020 paper and the Yarham 2014 paper were retrieved only as search snippets, so I did not read their full text. Other citations below are from memory and are flagged "not re-verified here".

## 1. Primary molecular function

TRIT1 is a tRNA modification enzyme. It transfers a dimethylallyl (Δ2-isopentenyl, C5) group from dimethylallyl diphosphate (DMAPP) onto the exocyclic N6 amine of adenosine 37 in the anticodon loop. The product is N6-isopentenyladenosine (i6A37).
- Reaction (EC 2.5.1.75): adenine37 in tRNA + dimethylallyl diphosphate → N6-dimethylallyl-adenine37 in tRNA + diphosphate. UniProt cites PMID:24901367 for this activity.
- The target is A37 in the sequence A36-A37-A38 of the anticodon loop, immediately 3′ to the anticodon. Only a subset of tRNAs carry the modification. In humans these are tRNAs that read codons beginning with U, plus a few others.
- This pattern is conserved from bacterial MiaA through yeast Mod5 to human TRIT1. Bacterial and yeast i6A37 is often further modified to ms2i6A by MiaB-type enzymes. In human mitochondria this step is done by CDK5RAP1 (not re-verified here).

### Key experimental evidence
- **Yarham et al. 2014, PLoS Genet** ([PMC4046958](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4046958/); PMID:24901367).
  - A patient with a combined mitochondrial respiratory chain defect carried a homozygous TRIT1 p.Arg323Gln missense variant.
  - Patient fibroblasts were deficient in i6A37 on both cytosolic and mitochondrial tRNAs.
  - Transduction with wild-type TRIT1 fully complemented the deficiency in both tRNA classes.
  - A pathogenic mt-tRNA-Ser(UCN) mutation in the A36-A37-A38 loop (m.7480A>G) also abolished i6A37.
  - This is the primary experimental basis for the UniProt catalytic annotation.
- **Khalique et al. 2020, PLoS Genet** ([PMC7200024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7200024/); PMID:32324744). This work was in yeast and human systems.
  - Substrate recognition is driven largely by the A36-A37-A38 sequence.
  - Some tRNAs are restricted despite carrying that sequence. The cytosolic tRNA-Trp(CCA) is poorly modified.
  - TRIT1 has an N-terminal mitochondrial targeting sequence (MTS). Point mutations that reduce import lower modification of mitochondrial tRNAs but not cytosolic tRNAs.
- **Fradejas et al. 2013** (Biochem J; not re-verified here). Mammalian Trit1 modifies tRNA[Ser]Sec, the selenocysteine tRNA, at A37. This is needed for full selenoprotein expression. It makes Sec-tRNA a specialised substrate.
- **Golovko et al. 2000** (Gene; not re-verified here). The original cloning of hGRO1 on chromosome 1p34. Spinola and colleagues later proposed TRIT1 as a lung-cancer tumour suppressor candidate (not re-verified here).
- **Structure and evolution.** The structure of yeast Mod5 bound to tRNA (Zhou and Huang 2008, not re-verified here) shows how the IPT domain and zinc finger engage the anticodon stem-loop. Human TRIT1 is inferred to use the same mechanism through its InterPro domains (IPR039657, IPR030666, IPR018022, IPR003604, IPR027417).

## 2. Subcellular location

TRIT1 acts on tRNA in two compartments, not in the secreted or extracellular space.
- **Cytosol or nucleus:** modification of nuclear-encoded cytosolic tRNAs. The enzyme is expected to act on tRNA after transcription. The nuclear versus cytosolic split was not established in the sources I read.
- **Mitochondrial matrix:** modification of mt-tRNAs such as tRNA-Ser(UCN). Import depends on the N-terminal MTS (Khalique 2020). UniProt flags the entry "Precursor", consistent with a cleavable presequence.
- Dual targeting is the key feature. It explains why TRIT1 variants affect both cytosolic and mitochondrial translation.

## 3. Pathways and biological processes

- **tRNA modification and processing**, specifically tRNA N6-isopentenylation at position 37. The modification stabilises codon-anticodon pairing at the first codon position (A36-U) and supports translational accuracy and efficiency. This is the precise role. Downstream effects are consequences of this function.
- **Mitochondrial translation.** Lack of i6A37 on mt-tRNAs impairs synthesis of respiratory chain subunits. Patient fibroblasts showed combined respiratory chain deficiency (Yarham 2014).
- **Selenoprotein synthesis**, through modification of Sec-tRNA (Fradejas 2013, not re-verified).
- **Broader cellular phenotypes.** The tumour suppressor, redox and ferroptosis phenotypes reported in cancer studies are likely indirect effects of translational changes. I did not review these and treat them as lower-priority context.

## 4. Disease relevance

- Biallelic TRIT1 variants cause a mitochondrial disease. The first case was p.Arg323Gln, with combined respiratory chain deficiency and a severe neurological phenotype (Yarham 2014).
- Additional reports of biallelic TRIT1 variants describe neurodevelopmental disease, including Kernohan et al. 2017, Hum Mutat (not re-verified here). The clinical details above are from memory and should be checked against OMIM or ClinVar.
- Mutations in the substrate, such as mt-tRNA-Ser(UCN) m.7480A>G, abolish i6A37 and converge on the same biochemical defect.

## 5. Suggested GO-style summary

| Aspect | Suggested annotation |
|---|---|
| MF | tRNA dimethylallyltransferase activity (GO:0052381) |
| MF (supporting) | tRNA binding; zinc ion binding (zinc finger) |
| BP | tRNA modification, specifically tRNA N6-isopentenylation at A37; mitochondrial tRNA modification |
| CC | mitochondrion (matrix); cytosol |

I did not verify these GO term IDs against the ontology. Check them with the OLS MCP before use.
- Avoid a generic "protein binding" annotation.
- The selenoprotein and respiratory-chain phenotypes are consequences of the modification. They should be kept non-core or omitted.

## 6. Open questions

- The nuclear versus cytosolic distribution of the enzyme.
- Whether TRIT1 is regulated, for example by DMAPP supply from the mevalonate pathway or by competition between mitochondrial import and cytosolic retention.
- Why some A36-A37-A38-containing tRNAs are poorly modified, such as tRNA-Trp(CCA), and whether this is a deliberate restriction.
- Whether any non-tRNA substrates exist. None were found in this search.

## Sources
- [Yarham et al. 2014, PLoS Genet, PMC4046958](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4046958/)
- [Khalique et al. 2020, PLoS Genet, PMC7200024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7200024/)
- [bioRxiv preprint of Khalique 2020](https://www.biorxiv.org/content/10.1101/714972)
- [SGD reference page for PMID:24901367](https://www.yeastgenome.org/reference/24901367)

## Citations

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4046958/
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7200024/
3. https://www.biorxiv.org/content/10.1101/714972
4. https://www.yeastgenome.org/reference/24901367