---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T23:13:11.429879'
end_time: '2026-10-14T23:13:47.597911'
duration_seconds: 36.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: FBXL4
  gene_symbol: FBXL4
  uniprot_accession: Q9UKA2
  protein_description: 'RecName: Full=F-box/LRR-repeat protein 4; AltName: Full=F-box
    and leucine-rich repeat protein 4; AltName: Full=F-box protein FBL4/FBL5;'
  gene_info: Name=FBXL4; Synonyms=FBL4, FBL5;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: F-box-like_dom_sf. (IPR036047); F-box_dom. (IPR001810); FBXL15_LRR.
    (IPR057207); Leu-rich_rpt_Cys-con_subtyp. (IPR006553); LRR_dom_sf. (IPR032675)
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
  total_cost_usd: 0.20494840000000003
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
- **UniProt Accession:** Q9UKA2
- **Protein Description:** RecName: Full=F-box/LRR-repeat protein 4; AltName: Full=F-box and leucine-rich repeat protein 4; AltName: Full=F-box protein FBL4/FBL5;
- **Gene Information:** Name=FBXL4; Synonyms=FBL4, FBL5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** F-box-like_dom_sf. (IPR036047); F-box_dom. (IPR001810); FBXL15_LRR. (IPR057207); Leu-rich_rpt_Cys-con_subtyp. (IPR006553); LRR_dom_sf. (IPR032675)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FBXL4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FBXL4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FBXL4** (gene ID: FBXL4, UniProt: Q9UKA2) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FBXL4 (Q9UKA2), human: research report

**Identity check.** The UniProt record is F-box/LRR-repeat protein 4, gene FBXL4 (synonyms FBL4, FBL5), in *Homo sapiens*. Its domains are an F-box and a leucine-rich repeat (LRR) region. The literature below is on this same gene. No ambiguity with another gene was found.

**Method and limits.** This report rests on two web searches, which returned the 2023 EMBO J paper and its preprints. The remaining points come from my background knowledge and have no verified URLs. These are the Cao and Alsina papers, the Gai 2013 mitochondrial-localisation paper, the Bonnen 2013 and Gai 2013 disease papers, the mouse knockout, the structural work and the Sabouny 2024 hypoxia point. I could not check them against their sources here, so check them before citing. Claims backed by a search result carry a link.

## Summary

FBXL4 is the substrate-recognition subunit of a Cullin1-based SCF (Skp1–Cul1–F-box) E3 ubiquitin ligase. The ligase sits on the **mitochondrial outer membrane**. There it ubiquitylates the mitophagy receptors **BNIP3 and NIX (BNIP3L)** and sends them to proteasomal degradation. This keeps basal mitophagy low. Loss-of-function variants cause **mitochondrial DNA depletion syndrome 13 (MTDPS13)**, an encephalomyopathic disease. The mechanism is excess BNIP3/NIX and over-active mitophagy.

## Molecular function

- **Activity.** FBXL4 is a substrate adaptor for an SCF-type cullin-RING ubiquitin ligase. The F-box binds Skp1 and Cul1. The LRR region is the predicted substrate-binding module. The ligase catalyses ubiquitin transfer to BNIP3 and NIX, which targets them for degradation.
- **Primary evidence.** [Nguyen-Dien et al., EMBO J 2023;42(13):e112767](https://link.springer.com/10.15252/embj.2022112767) ([PMC10308361](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10308361/); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2022.10.12.511867.full.pdf)) reports that SCF-FBXL4 "localises to the mitochondrial outer membrane in unstressed cells and mediates the constitutive ubiquitylation and degradation of the mitophagy receptors NIX and BNIP3".
- **Independent work (not verified here).** A separate study (Cao et al., 2023, which I believe appeared in EMBO J and/or *Nature Cell Biology*) describes a mitochondrial SCF-FBXL4 ligase that degrades BNIP3 and NIX, and I believe Alsina et al. (2023) reached the same conclusion. This convergence is reported in a [discussion thread](https://s4me.info/threads/a-mitochondrial-scf%E2%80%90fbxl4-ubiquitin-e3-ligase-complex-degrades-bnip3-and-nix-to-restrain-mitophagy-and-prevent-mitochondrial-disease-2023-cao.45548) and in the search summaries.
- **Substrate specificity.** The substrates are the outer-membrane BH3-only-like mitophagy receptors BNIP3 and NIX. The search summaries do not address other substrates, so none are claimed.

## Localisation

FBXL4 is on the **mitochondrial outer membrane**, facing the cytosol. This fits the ubiquitylation of other outer-membrane proteins. Earlier work (Gai et al. 2013, unverified) reported mitochondrial targeting through an N-terminal sequence. The search results also place the ligase at the outer membrane under basal, non-stressed conditions.

## Pathway and biological role

- **Negative regulation of receptor-mediated mitophagy.** BNIP3 and NIX are induced by HIF1α under hypoxia or iron chelation, and CRL2-VHL controls HIF1α. FBXL4 acts as a separate checkpoint on the receptors themselves. It sets the basal level of receptor-mediated mitophagy.
- **Mouse model.** Per the search summary, *Fbxl4*-knockout mice have raised BNIP3 and NIX and die perinatally. Knocking out either *Bnip3* or *Nix* rescues their metabolic derangements and viability. This shows that the receptor accumulation is causal.
- **Mitochondrial homeostasis.** Excess mitophagy in FBXL4-deficient cells is associated with lower mitochondrial mass, mtDNA depletion and respiratory-chain deficiency. Earlier reports (Bonnen 2013 and Gai 2013, unverified) linked FBXL4 to mtDNA maintenance and mitochondrial dynamics, but the mitophagy mechanism is the best-supported primary role.

## Disease

Biallelic loss-of-function or missense variants in FBXL4 cause **MTDPS13**, an early-onset encephalomyopathy with lactic acidosis, hypotonia and developmental delay. In the EMBO J paper, the pathogenic variants "do not efficiently interact with the core SCF ubiquitin ligase machinery or mediate the degradation of NIX and BNIP3". This leads to excess basal mitophagy. These are the search-summary wordings, not full-text checks.

## Evidence summary

| Claim | Evidence type | Source |
|---|---|---|
| SCF-FBXL4 degrades BNIP3 and NIX | Experimental: cell biology, ubiquitylation, degradation | [EMBO J 2023](https://link.springer.com/10.15252/embj.2022112767) |
| Outer-membrane localisation | Experimental | [PMC10308361](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10308361/) |
| Disease variants impair SCF assembly | Experimental | Same paper |
| *Bnip3* or *Nix* loss rescues *Fbxl4*-null mice | Mouse genetics | Search summary of the independent study, not verified |
| F-box and LRR architecture | Domain inference | UniProt/InterPro: IPR001810, IPR006553, IPR032675 |

## Suggestions for GO annotation

- **Molecular function.** Use the substrate-specific adaptor role for a cullin-RING ligase. A reasonable choice is a ubiquitin-protein ligase substrate-recognition term (for example, ubiquitin-ligase-substrate adaptor activity), not a bare "protein binding" term. Check the term in the OLS MCP.
- **Process.** Use negative regulation of mitophagy, and protein ubiquitination or proteasomal degradation of BNIP3/NIX.
- **Component.** Use mitochondrial outer membrane and the SCF ubiquitin ligase complex.
- **Caution.** MTDPS13 and mtDNA maintenance effects are downstream. They are best treated as non-core.

## Open questions

- How FBXL4 recognises its substrates, and the role of the LRR domain. Structural work may exist (unverified), and the search did not cover it.
- How FBXL4 activity is regulated under hypoxia or iron chelation, when BNIP3/NIX must be stabilised.
- Whether other outer-membrane substrates exist.
- Why the disease is so tissue-selective despite ubiquitous expression.

## Sources

- [Nguyen-Dien et al., EMBO J 2023, FBXL4 suppresses mitophagy by restricting the accumulation of NIX and BNIP3 mitophagy receptors](https://link.springer.com/10.15252/embj.2022112767)
- [PMC10308361 (full text)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10308361/)
- [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2022.10.12.511867.full.pdf)
- [Monash record](https://research.monash.edu/en/publications/fbxl4-suppresses-mitophagy-by-restricting-the-accumulation-of-nix/)
- [S4ME thread on Cao et al. 2023](https://s4me.info/threads/a-mitochondrial-scf%E2%80%90fbxl4-ubiquitin-e3-ligase-complex-degrades-bnip3-and-nix-to-restrain-mitophagy-and-prevent-mitochondrial-disease-2023-cao.45548)

## Citations

1. https://link.springer.com/10.15252/embj.2022112767
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10308361/
3. https://www.biorxiv.org/content/10.1101/2022.10.12.511867.full.pdf
4. https://s4me.info/threads/a-mitochondrial-scf%E2%80%90fbxl4-ubiquitin-e3-ligase-complex-degrades-bnip3-and-nix-to-restrain-mitophagy-and-prevent-mitochondrial-disease-2023-cao.45548
5. https://research.monash.edu/en/publications/fbxl4-suppresses-mitophagy-by-restricting-the-accumulation-of-nix/