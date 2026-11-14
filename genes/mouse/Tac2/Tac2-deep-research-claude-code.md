---
provider: claude_code
cached: false
start_time: '2026-11-13T23:38:20.659614'
end_time: '2026-11-13T23:39:25.163864'
duration_seconds: 64.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Tac2
  gene_symbol: Tac3
  uniprot_accession: P55099
  protein_description: 'RecName: Full=Tachykinin-3; AltName: Full=Neurokinin B-like
    protein Zneurok1; AltName: Full=Preprotachykinin-B; Short=PPT-B; Contains: RecName:
    Full=Neurokinin-B; Short=NKB; AltName: Full=Neuromedin-K; Flags: Precursor;'
  gene_info: Name=Tac3; Synonyms=Nknb, Tac2;
  organism_full: Mus musculus (Mouse).
  protein_family: Belongs to the tachykinin family. .
  protein_domains: Neurokinin-B/TAC3. (IPR003635); Tachy_Neuro_lke_CS. (IPR013055);
    Neurokinin_B (PF03823)
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
  web_search_requests: 3
  num_turns: 6
  total_cost_usd: 0.5108113999999999
  session_id: 429c94bb-30e0-4272-9363-bece4f101d1e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P55099
- **Protein Description:** RecName: Full=Tachykinin-3; AltName: Full=Neurokinin B-like protein Zneurok1; AltName: Full=Preprotachykinin-B; Short=PPT-B; Contains: RecName: Full=Neurokinin-B; Short=NKB; AltName: Full=Neuromedin-K; Flags: Precursor;
- **Gene Information:** Name=Tac3; Synonyms=Nknb, Tac2;
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Belongs to the tachykinin family. .
- **Key Domains:** Neurokinin-B/TAC3. (IPR003635); Tachy_Neuro_lke_CS. (IPR013055); Neurokinin_B (PF03823)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Tac3" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Tac3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Tac3** (gene ID: Tac2, UniProt: P55099) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Research report: mouse Tac3 (Tac2) / neurokinin B (UniProt P55099)

I researched this from a small set of web searches. There were no local gene files to draw on. Most claims below come from search excerpts and secondary summaries, not full texts I read. Treat the citations as pointers to check before you use them as GO evidence.

## 1. Identity check

- **Gene:** In mouse the gene is named *Tac2* (synonyms *Tac3*, *Nknb*). It is the ortholog of human *TAC3*. The mouse name differs from the human one only for historical reasons; it is not a different gene.
- **Organism:** The literature found is on *Mus musculus* (mouse), plus comparative work in human, rat, sheep and monkey. That matches the UniProt record.
- **Family and domains:** The protein is a tachykinin precursor (Neurokinin-B/TAC3 IPR003635; PF03823; tachykinin consensus motif IPR013055). This fits the literature, which describes a preprotachykinin-B that is processed into neurokinin B (NKB). No conflicting gene with the same symbol turned up.

## 2. Primary function: precursor of a secreted neuropeptide hormone

- **Not an enzyme or transporter.** Tac2 encodes preprotachykinin-B, a secretory prohormone. It is a signaling ligand precursor.
- **Processing:** A review states that the gene's exons encode a precursor that is cleaved first to proneurokinin B and then to NKB. Exon 5 encodes the active NKB peptide ([PMC3858905](https://pmc.ncbi.nlm.nih.gov/articles/PMC3858905); [PMC2992576](https://pmc.ncbi.nlm.nih.gov/articles/PMC2992576)).
- **The active peptide:** NKB is a C-terminally amidated decapeptide ending in the tachykinin motif FxGLM-NH2. This is general knowledge about the family and the UniProt record, not a source found in this search.
- **Receptor:** NKB is the preferred endogenous agonist of the NK3 receptor (NK3R, encoded by *Tacr3*). NK3R is a G-protein-coupled receptor. NKB has lower affinity for NK1R and NK2R.
- **Suggested GO molecular function:** neurokinin receptor binding, or hormone/neuropeptide hormone activity.

## 3. Where it acts

- **Inside the cell:** The precursor enters the secretory pathway. Like other neuropeptides it is thought to be stored in large dense-core vesicles. These can release their contents outside the synaptic cleft, at sites with no specialised structure ([PMC2992576](https://pmc.ncbi.nlm.nih.gov/articles/PMC2992576)). This is a general neuropeptide statement; the search found no mouse Tac2-specific data on vesicle sorting or on which prohormone convertase cleaves it.
- **Where it functions:** in the extracellular space, as a secreted peptide.
- **Main cells that make it:** kisspeptin/NKB/dynorphin ("KNDy") neurons in the hypothalamic arcuate nucleus. *Tac2* and *Tacr3* are co-expressed in arcuate cells, a nodal point for controlling GnRH secretion ([PMC3198996](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198996); [PMC4399316](https://pmc.ncbi.nlm.nih.gov/articles/PMC4399316)).
- **Other brain regions:** It is also expressed elsewhere in the brain, including the central amygdala, and is induced across the brain by chronic stress (see section 5).

## 4. Pathway role: the KNDy / GnRH pulse generator

- **Autocrine and paracrine action:** NKB released from KNDy neurons acts on NK3R on the same population of neurons.
- **Effect on firing:** The NK3R agonist senktide increases KNDy neuron firing. This fits a model where NKB drives synchronized bursts, dynorphin terminates them, and kisspeptin carries the output to GnRH neurons ([PMC4399316](https://pmc.ncbi.nlm.nih.gov/articles/PMC4399316); [PMC3198996](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198996)).
- **Effect on LH:** In rodents, sheep and monkeys, NK3R agonists stimulate LH secretion, probably through a pathway that depends on Kiss1 and GnRH ([PMC3858905](https://pmc.ncbi.nlm.nih.gov/articles/PMC3858905)).
- **Puberty:** In mouse, *Tac2* and *Tacr3* mRNA rise across puberty. *Tac2* appears less sensitive than *Kiss1* to sex-steroid negative feedback ([PMC3858905](https://pmc.ncbi.nlm.nih.gov/articles/PMC3858905)).

## 5. Genetic evidence in mouse

| Model | Phenotype | Source |
|---|---|---|
| *Tac2*−/− male | Normal puberty timing; fertile | [PMC7722126](https://pmc.ncbi.nlm.nih.gov/articles/PMC7722126), [Torres 2021](https://orbi.uliege.be/bitstream/2268/260389/1/Torres%202021.pdf) |
| *Tac2*−/− female | Delayed puberty; fertile as adults | same |
| *Tacr3*−/− | Fertile, but with central reproductive defects (lower FSH, smaller testes) | [PMC3320245](https://pmc.ncbi.nlm.nih.gov/articles/PMC3320245), [Endocrinology 153:1578](https://dbpia.nl.go.kr/endo/article/153/4/1578/2423671) |

- **Mouse vs. human:** People with *TAC3* or *TACR3* loss-of-function mutations have hypogonadotropic hypogonadism. The much milder mouse phenotype is commonly explained by compensation from other tachykinins, such as NKA acting through NK2R and substance P acting through NK1R ([LJMU NKA study](https://researchonline.ljmu.ac.uk/11578/3/Characterization%20of%20the%20role%20of%20NKA%20in%20the%20control%20of%20puberty%20onset%20and%20gonadotropin%20release%20in%20the%20female%20mouse..pdf); [PMC3281542](https://pmc.ncbi.nlm.nih.gov/articles/PMC3281542)).
- **What this means for annotation:** The process annotation should be regulation of gonadotropin/GnRH secretion and of puberty onset. It should not be an essential fertility role.

## 6. Roles in the brain outside reproduction

- **Fear memory:** Andero et al. 2014 (*Neuron*) reported that Tac2/NKB/NK3R signaling in the central amygdala takes part in fear-memory consolidation; blocking it impairs consolidation in males. A follow-up study found that the same blockade enhances consolidation in females ([OUCI record](https://ouci.dntb.gov.ua/works/42z1GeK4); [Zelikowsky lab review](https://www.zelikowskylab.com/s/MarvaretalJNReview.pdf)).
- **Social isolation:** Zelikowsky et al. 2018 (*Cell*) found that two weeks of social isolation, but not 24 hours, raises Tac2/NKB across the brain. Region-specific Tac2 signaling drives the resulting aggression, persistent fear and hypersensitivity. NK3R antagonism reverses these effects ([PMC5967263](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967263); [Caltech preprint](https://authors.library.caltech.edu/records/xgk8s-ec475/preview/nihms964019.pdf)).
- **Annotation status:** These are neuromodulatory roles of the same ligand–NK3R signal. They are real, but are best annotated as non-core.

## 7. Summary for annotation

- **Core molecular function:** a neuropeptide hormone/ligand that activates NK3R (tachykinin receptor binding).
- **Location:** extracellular space, as a secreted peptide; in the cell, the precursor is handled in secretory/dense-core vesicles.
- **Core process:** the tachykinin receptor signaling pathway, which leads to regulation of GnRH/LH secretion through the arcuate KNDy network. Puberty timing in females is part of this.
- **Non-core:** fear-memory consolidation and stress-induced behavior.
- **Gaps:** I found no mouse-specific data on which prohormone convertase or amidating enzyme processes the precursor, or on how the peptide is packaged into vesicles. Human disease data and mouse knockout data disagree on how essential the gene is.

I did not verify PMIDs; resolve them before citing these papers in GO annotations.

Sources:
- [PMC3198996](https://pmc.ncbi.nlm.nih.gov/articles/PMC3198996)
- [PMC4399316](https://pmc.ncbi.nlm.nih.gov/articles/PMC4399316)
- [PMC3858905](https://pmc.ncbi.nlm.nih.gov/articles/PMC3858905)
- [PMC2992576](https://pmc.ncbi.nlm.nih.gov/articles/PMC2992576)
- [PMC7722126](https://pmc.ncbi.nlm.nih.gov/articles/PMC7722126)
- [PMC3320245](https://pmc.ncbi.nlm.nih.gov/articles/PMC3320245)
- [PMC3281542](https://pmc.ncbi.nlm.nih.gov/articles/PMC3281542)
- [PMC5967263](https://pmc.ncbi.nlm.nih.gov/articles/PMC5967263)
- [Torres 2021 (ULiège)](https://orbi.uliege.be/bitstream/2268/260389/1/Torres%202021.pdf)
- [Endocrinology 153(4):1578](https://dbpia.nl.go.kr/endo/article/153/4/1578/2423671)
- [LJMU NKA puberty study](https://researchonline.ljmu.ac.uk/11578/3/Characterization%20of%20the%20role%20of%20NKA%20in%20the%20control%20of%20puberty%20onset%20and%20gonadotropin%20release%20in%20the%20female%20mouse..pdf)
- [Zelikowsky et al. 2018 (Caltech)](https://authors.library.caltech.edu/records/xgk8s-ec475/preview/nihms964019.pdf)
- [Tac2 fear-learning study (OUCI)](https://ouci.dntb.gov.ua/works/42z1GeK4)
- [Zelikowsky lab review](https://www.zelikowskylab.com/s/MarvaretalJNReview.pdf)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3858905
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC2992576
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3198996
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC4399316
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC7722126
6. https://orbi.uliege.be/bitstream/2268/260389/1/Torres%202021.pdf
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC3320245
8. https://dbpia.nl.go.kr/endo/article/153/4/1578/2423671
9. https://researchonline.ljmu.ac.uk/11578/3/Characterization%20of%20the%20role%20of%20NKA%20in%20the%20control%20of%20puberty%20onset%20and%20gonadotropin%20release%20in%20the%20female%20mouse..pdf
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3281542
11. https://ouci.dntb.gov.ua/works/42z1GeK4
12. https://www.zelikowskylab.com/s/MarvaretalJNReview.pdf
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC5967263
14. https://authors.library.caltech.edu/records/xgk8s-ec475/preview/nihms964019.pdf