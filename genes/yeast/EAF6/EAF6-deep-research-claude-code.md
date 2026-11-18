---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:19:53.944872'
end_time: '2026-11-18T15:22:29.385108'
duration_seconds: 155.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: EAF6
  gene_symbol: EAF6
  uniprot_accession: P47128
  protein_description: 'RecName: Full=Chromatin modification-related protein EAF6;
    AltName: Full=ESA1-associated factor 6;'
  gene_info: Name=EAF6; OrderedLocusNames=YJR082C; ORFNames=J1854;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the EAF6 family. .
  protein_domains: Eaf6. (IPR015418); NuA4 (PF09340)
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
  web_search_requests: 13
  num_turns: 24
  total_cost_usd: 2.304149755
  session_id: dff1e700-3ff1-482b-b2fc-89478c9e4948
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P47128
- **Protein Description:** RecName: Full=Chromatin modification-related protein EAF6; AltName: Full=ESA1-associated factor 6;
- **Gene Information:** Name=EAF6; OrderedLocusNames=YJR082C; ORFNames=J1854;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the EAF6 family. .
- **Key Domains:** Eaf6. (IPR015418); NuA4 (PF09340)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EAF6" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EAF6' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EAF6** (gene ID: EAF6, UniProt: P47128) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Direct page fetches are blocked, so I'm filling the remaining gaps with a few targeted searches and the local UniProt record, then writing the report.

# EAF6 (YJR082C; UniProt P47128) in *Saccharomyces cerevisiae*: research report

## Scope and limits of this report

- **Identity check passed.** The symbol EAF6 ("ESA1-associated factor 6"), the organism (*S. cerevisiae* S288c), the EAF6 family, and the Eaf6/NuA4 domain (IPR015418, PF09340) all match the literature found. The human orthologue is named MEAF6 (hEaf6), so there is no symbol collision.
- **Source access was limited.** Direct fetches of PMC, PubMed, Europe PMC and SGD pages were all blocked. The report rests on the local UniProt record, the abstract-only cached papers in the repository, and web-search result summaries of the primary papers.
- **Nothing here is a checked verbatim quote.** Statements should be re-verified against full text before being used as `supporting_text`.
- **Little is known about Eaf6 on its own.** Almost everything is inferred from the complexes it sits in. No dedicated study of yeast Eaf6 was found.

## 1. Summary

Eaf6 is a small (113 aa), nuclear, non-catalytic subunit shared by two MYST-family histone acetyltransferase (HAT) complexes:

- **NuA4**, whose catalytic subunit is Esa1 and which acetylates nucleosomal H4 and H2A.
- **NuA3**, whose catalytic subunit is Sas3 and which acetylates H3K14 (and, per recent work, H3K23).

Within NuA4, Eaf6 belongs to the four-subunit catalytic HAT module, "piccolo NuA4" (Esa1, Epl1, Yng2, Eaf6). Its long N-terminal helix packs into a four-helix bundle with Epl1 and Yng2. Eaf6 has no known enzymatic activity and is not essential for viability. The best-supported description is a structural subunit of the scaffold–ING–Eaf6 assembly that is conserved across MYST acetyltransferase complexes.

## 2. Protein features

| Feature | Detail | Source |
|---|---|---|
| Length | 113 aa | UniProt P47128 |
| Family / domain | EAF6 family; Eaf6 (IPR015418), NuA4 (PF09340); PANTHER PTHR13476 (MEAF6) | UniProt P47128 |
| Predicted coiled coil | residues 1–43 | UniProt P47128 |
| Experimental helices | 2–6 and a long helix 8–43 (PDB 5J9T), plus short C-terminal helices | UniProt P47128 |
| Disordered region | 36–64 (MobiDB-lite prediction) | UniProt P47128 |
| Abundance | about 504 molecules per cell in log phase | Ghaemmaghami et al. 2003, PMID:14562106 |
| Catalytic motifs or histone-reader domains | none annotated | UniProt P47128 |

Structures containing full-length Eaf6 include the crystal structures 5J9Q/5J9T/5J9U/5J9W, the cryo-EM entries 7VVU/7VVZ, and later cryo-EM entries 8X2X–8X32, 9UUO, 9UUS and 9VKW (UniProt cross-references; I could not confirm which paper the 8X and 9U/9V entries belong to).

## 3. Role in the NuA4 complex

### Complex membership
- Eaf6 is one of 13 NuA4 subunits: Act1, Arp4, Yaf9, Eaf1 (Vid21), Swc4, Eaf3, Eaf5, Eaf6, Eaf7, Epl1, Esa1, Tra1 and Yng2 (UniProt, citing PMID:15485911, PMID:15353583, PMID:27594449, PMID:36198799).
- It was identified as a NuA4 component by affinity purification and mass spectrometry in 2004 (Zhang et al., PMID:15485911; Krogan et al., PMID:15353583). Both are abstract-only in the local cache, so the Eaf6-specific data were not read.
- The human Tip60 complex contains the homologue FLJ11730, named hEaf6 for its homology to yeast Eaf6 ([Doyon et al. 2004, Mol Cell Biol 24:1884](https://pubmed.ncbi.nlm.nih.gov/14966270/)).

### Position in the HAT (piccolo) module
- Piccolo NuA4 comprises Esa1, Epl1, Yng2 and Eaf6 and carries the nucleosomal H4/H2A acetyltransferase activity ([Wang et al. 2018, Nat Commun](https://www.nature.com/articles/s41467-018-03504-5); [Zukin et al. 2022, eLife](https://elifesciences.org/articles/81400)).
- The crystal structure of the NuA4 core contained the Esa1 HAT domain (141–445), the Epl1 EPcA domain (50–400), the Yng2 N-terminal region (1–120) and full-length Eaf6 ([Xu et al. 2016, Mol Cell 63:965](https://www.cell.com/molecular-cell/fulltext/S1097-2765(16)30377-X)).
- That structure has two parts:
  - a catalytic core of Esa1 plus Epl1 EPcA-I;
  - a four-helix bundle formed by Epl1 EPcA-II, Yng2 and the major helix of Eaf6.
- Esa1 is activated through its contacts with Epl1, and the complex recognises the nucleosomal H4 tail by a "double recognition" mechanism (Xu et al. 2016). Neither property is attributed to Eaf6.
- A secondary source, citing Mitchell et al. 2008, says Eaf6 joins piccolo through Yng2. I could not check this in the primary paper.

### Position in the holo-complex
- Epl1 tethers the HAT module to the Eaf1-scaffolded core, and the module is flexible relative to the Tra1 hub ([Zukin et al. 2022](https://elifesciences.org/articles/81400)).
- A separate cryo-EM study located Esa1, Yng2 and Eaf6 within full NuA4 ([Ji et al. 2022, PNAS](https://pubmed.ncbi.nlm.nih.gov/36417436/)).
- In the nucleosome-bound structure, the nucleosome is held mainly by the HAT module ([Qu et al. 2022, Nature 610:569](https://www.nature.com/articles/s41586-022-05303-x)).
- The 2022 studies disagree on HAT-module placement and on whether the complete complex binds nucleosomes as piccolo does.
- A 2025 study reports cryo-EM structures of piccolo NuA4 through the acetylation process ([PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2414490122)).

### What Eaf6 contributes
No source found shows that Eaf6 is required for piccolo assembly or for HAT activity. The mapped determinants lie elsewhere: Epl1 subdomains I and II bridge Esa1 and Yng2, the Epl1 N-terminal subdomain binds the nucleosome, and Yng2's N-terminus is needed for nucleosome acetylation ([Chittuluru et al. 2011, NSMB](https://pubmed.ncbi.nlm.nih.gov/21984211/) and related work).

## 4. Role in the NuA3 complex

- NuA3 has five core subunits: Sas3, Nto1, Eaf6, Yng1 and Taf14 ([Nguyen et al. 2024, Nat Commun](https://www.nature.com/articles/s41467-024-49730-y)).
- Eaf6 was placed in NuA3 by Taverna et al. 2006 (PMID:17157260), the source of the GO NuA3 annotations.
- NuA3 exists in two forms (UniProt, citing PMID:17157260 and PMID:25104842):
  - **NuA3a** binds H3K4me3 through the Yng1 PHD finger and acetylates H3K14 at promoters of active genes.
  - **NuA3b** additionally contains Pdp3, binds H3K36me3 through its PWWP domain, and acts in coding regions during elongation.
- Eaf6 is annotated to both forms ([SGD GO:1990467](https://www.yeastgenome.org/go/GO:1990467)).
- The 2024 structural work addresses Taf14–Yng1–Sas3 contacts; Eaf6 was not analysed.
- By analogy, Nto1 is the Epl1/BRPF-like scaffold and Yng1 the ING protein, so Eaf6 probably occupies the equivalent bundle position in NuA3. This is inference from homologous complexes, not a direct yeast result.

## 5. Conservation

The scaffold–ING–Eaf6 arrangement recurs across MYST complexes, which argues that the Eaf6 role is ancient:

- **Human MOZ/MORF (KAT6A/B):** tetrameric complexes with BRPF1/2/3, ING5 and MEAF6, with BRPF1 as the scaffold that binds ING5 and EAF6 directly (reviewed in [PMC4936061](https://pmc.ncbi.nlm.nih.gov/articles/PMC4936061)).
- **Human HBO1 (KAT7):** co-purifies with ING4/5 and EAF6.
- **Drosophila Enok:** a quartet with Br140, Ing5 and Eaf6.
- **Mouse Meaf6 knockout:** loss stopped cell proliferation with little change in histone acetylation, and the authors concluded Meaf6 is not essential for HAT activity but modulates Kat7 complex assembly ([PMID:32918898](https://pubmed.ncbi.nlm.nih.gov/32918898)).

The mouse result is the closest available functional test of an Eaf6-family protein. It is orthologue evidence and does not establish the yeast phenotype.

## 6. Localization

- Nuclear, from the genome-wide GFP localization study (Huh et al. 2003, PMID:14562095).
- Consistent with its stable membership in chromatin-bound NuA4 and NuA3. No sub-nuclear or cytoplasmic pool specific to Eaf6 was found.

## 7. Processes and phenotypes

### Processes (complex-level)
- **Transcription:** NuA4 is recruited by activators through Tra1 and acetylates promoter nucleosomes; NuA3 acts at promoters (NuA3a) and coding regions (NuA3b).
- **DNA repair:** NuA4 is recruited to double-strand breaks and acetylates H4 there. The GO "DNA repair" annotation for Eaf6 cites Utley et al. 2005 (PMID:16135807), a paper on regulation of NuA4 activity by H4 phosphorylation. It is abstract-only in the cache, so whether Eaf6 itself was assayed is unverified.
- These are roles of the complexes. Eaf6 takes part as a structural subunit and does not catalyse acetylation.

### Deletion phenotypes
- *EAF6* is non-essential; the essential NuA4 subunits do not include it ([Searle et al. 2017 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328)).
- Most non-essential NuA4 subunits have little effect on complex integrity and show 12–42 genetic interactions each, whereas *eaf1Δ* collapses the complex ([Mitchell et al. 2008, Mol Cell Biol 28:2244](https://www.yeastgenome.org/reference/S000125272)).
- *eaf6Δ* cells show no or only a modest increase in chromosome loss, unlike *eaf1Δ* and *yaf9Δ* (Mitchell et al. 2008, as reported in search summaries).
- *eaf6Δ* was one of the query strains in a synthetic dosage lethality screen of NuA4 mutants ([Mitchell et al. 2011](https://www.yeastgenome.org/reference/S000147077)).
- I found no direct measurement of bulk H4 or H3 acetylation in *eaf6Δ*.

## 8. Assessment of existing database annotations

| Annotation | Assessment |
|---|---|
| NuA4 complex; NuA3, NuA3a, NuA3b complexes | Well supported by purification and structures |
| Nucleus | Supported |
| Histone acetyltransferase activity (GOA; evidence ECO:0000305, curator inference; PMID:17157260) | Eaf6 has no catalytic domain; the activity belongs to Esa1 and Sas3. At most a "contributes to" relationship |
| DNA repair, DNA-templated transcription, chromatin remodeling | Complex-level roles; no Eaf6-specific evidence found |

## 9. Open questions

- Is Eaf6 required in yeast for assembly or stability of the Epl1–Yng2 (NuA4) and Nto1–Yng1 (NuA3) bundles, or for normal H4/H3 acetylation levels?
- Does the modest *eaf6Δ* phenotype reflect loss of NuA4 function, NuA3 function, or both? No separation-of-function analysis was found.
- What does the C-terminal half (roughly residues 44–113, partly disordered) do?
- Does Eaf6 occupy the same structural position in NuA3 as in piccolo NuA4? No NuA3 structure containing Eaf6 was found.

## Sources

- UniProt P47128 (local copy `genes/yeast/EAF6/EAF6-uniprot.txt`)
- [Xu et al. 2016, Mol Cell — NuA4 core complex, double recognition mechanism](https://www.cell.com/molecular-cell/fulltext/S1097-2765(16)30377-X) ([PDB 5J9Q](https://www.rcsb.org/structure/5J9Q), [5J9T](https://rcsb.org/structure/5J9T))
- [Wang et al. 2018, Nat Commun — Architecture of the NuA4/TIP60 complex](https://www.nature.com/articles/s41467-018-03504-5)
- [Zukin et al. 2022, eLife — Structure and flexibility of yeast NuA4](https://elifesciences.org/articles/81400)
- [Ji et al. 2022, PNAS — Structure of the NuA4 histone acetyltransferase complex](https://pubmed.ncbi.nlm.nih.gov/36417436/)
- [Qu et al. 2022, Nature — NuA4 bound to the nucleosome](https://www.nature.com/articles/s41586-022-05303-x)
- [PNAS 2025 — Cryo-EM structures reveal the acetylation process of piccolo NuA4](https://www.pnas.org/doi/10.1073/pnas.2414490122)
- [Chittuluru et al. 2011, NSMB — NuA4 and piccolo NuA4 nucleosome interaction](https://pubmed.ncbi.nlm.nih.gov/21984211/)
- [Doyon et al. 2004, Mol Cell Biol — NuA4 conservation from yeast to humans](https://pubmed.ncbi.nlm.nih.gov/14966270/)
- [Mitchell et al. 2008, Mol Cell Biol — Functional dissection of NuA4](https://www.yeastgenome.org/reference/S000125272)
- [Mitchell et al. 2011 — NuA4 synthetic dosage lethality screen](https://www.yeastgenome.org/reference/S000147077)
- [Searle et al. 2017 — NuA4 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328)
- [Nguyen et al. 2024, Nat Commun — Taf14, Yng1 and Sas3 in NuA3](https://www.nature.com/articles/s41467-024-49730-y)
- [SGD GO:1990467 NuA3a complex](https://www.yeastgenome.org/go/GO:1990467)
- [Review of MOZ/MORF–BRPF–ING5–EAF6 complexes](https://pmc.ncbi.nlm.nih.gov/articles/PMC4936061)
- [MEAF6 is essential for cell proliferation and KAT7 complex assembly](https://pubmed.ncbi.nlm.nih.gov/32918898)
- [Alliance / SGD gene page for EAF6](https://alliancegenome.org/gene/SGD:S000003842)
- Cached abstract-only papers: PMID:15485911, PMID:15353583, PMID:17157260, PMID:25104842, PMID:16135807, PMID:24843044, PMID:14562095, PMID:14562106

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/14966270/
2. https://www.nature.com/articles/s41467-018-03504-5
3. https://elifesciences.org/articles/81400
4. https://www.cell.com/molecular-cell/fulltext/S1097-2765(16
5. https://pubmed.ncbi.nlm.nih.gov/36417436/
6. https://www.nature.com/articles/s41586-022-05303-x
7. https://www.pnas.org/doi/10.1073/pnas.2414490122
8. https://pubmed.ncbi.nlm.nih.gov/21984211/
9. https://www.nature.com/articles/s41467-024-49730-y
10. https://www.yeastgenome.org/go/GO:1990467
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC4936061
12. https://pubmed.ncbi.nlm.nih.gov/32918898
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC5340328
14. https://www.yeastgenome.org/reference/S000125272
15. https://www.yeastgenome.org/reference/S000147077
16. https://www.rcsb.org/structure/5J9Q
17. https://rcsb.org/structure/5J9T
18. https://alliancegenome.org/gene/SGD:S000003842