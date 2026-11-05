---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:10:53.735389'
end_time: '2026-10-30T21:15:02.320900'
duration_seconds: 248.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2389
  gene_symbol: PP_2389
  uniprot_accession: Q88KA1
  protein_description: 'RecName: Full=YqcI/YcgG family protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_2389 {ECO:0000313|EMBL:AAN68002.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Uncharacterised_YqcI/YcgG. (IPR014988); YqcI_YcgG (PF08892)
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 15
  total_cost_usd: 1.144254385
  session_id: 23e54804-7eb8-4bbf-8e53-842509d374bd
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88KA1
- **Protein Description:** RecName: Full=YqcI/YcgG family protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_2389 {ECO:0000313|EMBL:AAN68002.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Uncharacterised_YqcI/YcgG. (IPR014988); YqcI_YcgG (PF08892)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2389" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2389' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2389** (gene ID: PP_2389, UniProt: Q88KA1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Still working: the main paper (Sun et al. 2026) is read. Next I'm checking the PP_2389 sequence against AglA for the heme-binding cysteine, and looking at its genomic context.

# PP_2389 (UniProt Q88KA1) in *Pseudomonas putida* KT2440: research report

## Summary

PP_2389 is a 262-residue protein with no experimental characterisation. No paper studies it directly, it has no GO annotations (the GOA file has only a header row), and UniProt rates it PE 4 (predicted). Its name, "YqcI/YcgG family protein", was assigned by the ProtNLM machine-learning model.

Two lines of evidence do point to a likely function:

- **Family membership.** It belongs to Pfam PF08892, InterPro IPR014988 and PANTHER PTHR40045:SF1. Work from 2012 to 2026 shows that this family is a new structural class of thiolate-ligated heme enzymes that hydroxylate the N–H bonds of guanidine groups, usually in arginine.
- **Conserved catalytic residues.** My own alignment shows that PP_2389 keeps the proximal heme-ligand cysteine motif (F-P-C) and the main catalytic core motifs of the family.

The best-supported hypothesis is that PP_2389 is a cytoplasmic, heme-dependent guanidine (arginine-type) N-hydroxylase whose physiological substrate is unknown. I am confident about the family assignment and the heme/cysteine prediction. I am not confident about the exact substrate or the pathway.

## 1. Identity check

| Feature | Value | Source |
|---|---|---|
| Accession | Q88KA1 (unreviewed TrEMBL), 262 aa, 29.6 kDa | UniProt flat file (local `PP_2389-uniprot.txt`) |
| Locus | PP_2389, complement(2727324..2728112), KT2440 chromosome | KEGG ppu:PP_2389 |
| GenBank product | "conserved protein of unknown function" | KEGG / Nelson et al. 2002 (PMID:12534463); Belda et al. 2016 (PMID:26913973) |
| Orthology | COG3403; KEGG K09190 "uncharacterized protein" | UniProt DR lines; KEGG |
| Domains | Pfam PF08892 YqcI_YcgG; InterPro IPR014988; PANTHER PTHR40045 / SF1 "YQCI_YCGG FAMILY PROTEIN" | UniProt DR lines |
| Existing GO annotations | None | local GOA file |

The symbol "PP_2389" is a KT2440 ordered locus tag and is not ambiguous. Searching the web for "PP_2389" found no publication about this gene. Everything below is inferred from the protein family and from sequence analysis.

## 2. The YqcI/YcgG family is a class of heme-dependent guanidine N-hydroxylases

### 2.1 Historical status
The family is named after two *Bacillus subtilis* 168 proteins of unknown function, YqcI (P45944) and YcgG (P94382). For many years it was a "domain of unknown function"-type family. PANTHER PTHR40045 holds about 2,200 proteins from about 2,000 proteomes (local `interpro/panther/PTHR40045/PTHR40045-metadata.yaml`). Sun et al. (2026) state that YqcI/YcgG enzymes "are ubiquitous across all domains of life, yet only six bacterial members have been functionally characterized."

### 2.2 DcsA: the first member shown to be a heme protein
In *Streptomyces lavendulae*, the D-cycloserine biosynthesis gene *dcsA* encodes a family member (UniProt D2Z024, "Putative N(ω)-hydroxy-L-arginine synthase").
- Kumagai et al. (2012, *Antimicrob. Agents Chemother.*, PMID:22547619) found by spectroscopy that recombinant DcsA "is a heme protein, supporting an idea that DcsA is an enzyme catalyzing hydroxylation".
- A ΔdcsA mutant made no D-cycloserine, and adding N(ω)-hydroxy-L-arginine (NHA) to the culture restored production. The authors concluded that DcsA is "essential to generate NHA as a precursor in the DCS biosynthetic pathway."
- DcsB, an arginase homolog, then hydrolyses NHA to L-ornithine and hydroxyurea (KEGG EC 3.5.3.25). KEGG assigns DcsA to KO K19741, N(ω)-hydroxy-L-arginine synthase.
- Sources: [PMC3393407-related record via Rhea/KEGG](https://www.kegg.jp/entry/K19741), [PMC3716191](https://pmc.ncbi.nlm.nih.gov/articles/PMC3716191/), [PMC2825969](https://pmc.ncbi.nlm.nih.gov/articles/PMC2825969) (2010 cloning of the 10-gene *dcsA–dcsJ* cluster).

### 2.3 Other characterised members in natural-product pathways
Sun et al. (2026) list the members with known roles. I took these citations from the paper's reference list through a summarising fetch and have not checked them one by one against PubMed.
- **AglA** (*Streptomyces monomycini*) carries out internal Nε-hydroxylation of aminomethylphosphonate-linked arginine (AMPn-Arg) in argolaphos biosynthesis (Zhang et al. 2022, *JACS*, PMID:35616638).
- **DcsA**: N(ω)-hydroxy-L-arginine formation in D-cycloserine biosynthesis (Kumagai et al. 2012, PMID:22547619).
- **GntA**, from the guanitoxin pathway in cyanobacteria (Lima et al. 2022, *JACS*, PMID:35583956), and **ChmN**, cited with guanitoxin / LC-MS methods (Crooke et al. 2024, *JACS*, PMID:38810110). The ChmN name also appears in a chalkophomycin N-hydroxypyrrole preprint ([bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.01.24.577118v2.full)).
- Pathways for miharamycins (Romo et al. 2019, *JACS*, PMID:31150226) and ambocidins (Lai et al. 2024, *Angew. Chem.*, PMID:39175099). These are the likely sources of the AlphaFold-modelled homologs Mhr24 and AmbT.

The shared chemistry is **hydroxylation of a guanidino N–H**: an N-hydroxy-guanidine precursor feeds later steps that build N–N or N–O-containing groups, such as hydroxyurea in D-cycloserine biosynthesis, the N-hydroxyarginine in argolaphos, and the cyclic guanidine phosphate ester of guanitoxin.

### 2.4 Structure and mechanism (Sun et al. 2026)
Sun Y. et al., "A Dynamic Gate Enables Regioselective Hydroxylation of Free Arginine by a Non-Canonical Heme Enzyme", *Adv. Sci.* 2026; 13(6):e13032; doi:10.1002/advs.202513032; PMID:41221789. Sources: [PMC12866846](https://pmc.ncbi.nlm.nih.gov/articles/PMC12866846/), [Wiley](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202513032), [PubMed](https://pubmed.ncbi.nlm.nih.gov/41221789/). PDB entries: 9UB3 (apo, 2.06 Å), 9UB5 (AglA–Arg, 1.83 Å; [NCBI](https://www.ncbi.nlm.nih.gov/Structure/pdb/9UB5)), 9UBA, 9UBB (AglA K225E–Arg, the PANTHER representative structure), 9UBS and 9UBT ([PDBj](https://pdbj.org/mine/summary/9ubb)).

- **Fold.** "AglA adopts a sandwich-like architecture, featuring a central four-stranded β-sheet (β1–β4) flanked by three helices (α1, α2, α5) on one side and two helices (α3, α4) on the opposite side." DALI finds no significant similarity to known heme enzymes (Z ≤ 5.4), so the family is "a new structural class" of "thiolate-ligated heme enzymes beyond canonical P450s". It lacks both the P450 α-helical core and the P450 PROSITE motif.
- **Heme ligation.** "The heme iron is axially coordinated by the thiol group of Cys44." The heme propionates make salt bridges with Arg166, Lys196 and Arg200. The C44A mutation abolishes activity.
- **Substrate pocket and regioselectivity gate.** Substrate binds on the distal side of the heme. Phe152, Arg179 and Phe182 sandwich the arginine side chain, and Gln177 positions a bridging water. Loop L2 (from α5 to the C-terminus) changes shape when substrate binds. Together these act as a "regiochemical gate" that allows only internal Nε-hydroxylation of AMPn-Arg. Wild-type AglA is "essentially inactive for free arginine". Single mutations change that: K196R, K225E and K196R/K225E give Nδ-hydroxyarginine from free L-Arg, and K196H, K196M and T220R give Nω-hydroxyarginine.
- **Electron supply.** Activity in vitro needed NAD(P)H plus a ferredoxin/ferredoxin-reductase p

I'll continue the report from where it was cut, keeping to the scientific content.

## 2.4 (continued) Electron supply

In vitro activity required NAD(P)H together with a ferredoxin/ferredoxin-reductase partner. For a self-sufficient fusion construct, the host offered two candidate reductases — a 2Fe-2S protein and a PDR/VanB-type oxidoreductase — and "only the PDR/VanB reductase supported AglA-catalyzed Nε-hydroxylation." The authors "speculate that AglA catalyzes AMPn-Arg via a similar electron transfer pathway" to P450s, with an Fe(IV)=O intermediate inferred from MD rather than observed. So the family appears to need an external reductase, which the enzyme itself does not encode.

## 3. Sequence analysis of PP_2389

I aligned Q88KA1 against three family members using Biopython's global aligner with BLOSUM62 (gap open −10, extend −0.5):

| Comparison | Identity over aligned positions |
|---|---|
| DcsA (D2Z024, *S. lavendulae*) | 97/235 = 41.3% |
| YcgG (P94382, *B. subtilis*) | 82/237 = 34.6% |
| YqcI (P45944, *B. subtilis*) | 74/238 = 31.1% |

Observations:

- **41% identity to DcsA** is high for a bacterial family spanning all domains of life, and well above the threshold at which fold and active-site architecture are reliably conserved. PP_2389 is a bona fide family member, not a remote relative.
- **The proximal cysteine is conserved.** PP_2389 has cysteines at positions 8, 46, 58, 146 and 244. Cys46 sits in the motif `FPCLFGR` (residues 44–50), which aligns to DcsA `FPCVFSR` and to *B. subtilis* `FPCIPGR`. In AglA the heme ligand Cys44 sits in the equivalent position of this same strictly conserved F-P-C block. PP_2389's Cys46 is therefore the predicted heme thiolate ligand.
- **Other family-diagnostic blocks are intact**, including `WSFCYAGMPLFINM` (aligning to DcsA `WSMCFHGMPLFINM`), the `RSRNLGQH` block and `VINPRE` — the region that in AglA contributes the β3/β4 catalytic cavity and the Phe/Arg/Phe substrate clamp. The C-terminal `CPFHAH` corresponds to DcsA `CPFTF` and *B. subtilis* `CPFS`, part of the conserved loop-L2 region that in AglA forms the regioselectivity gate.
- Residues equivalent to AglA's Lys196/Lys225/Thr220 (the positions whose mutation re-routes regioselectivity) are not identical in PP_2389, which is consistent with a different substrate or a different hydroxylation position, but I cannot predict either from the alignment alone.

Caveat on the analysis: these are pairwise global alignments, not a curated family MSA or a structure superposition, and the residue-number mapping to AglA's Cys44 rests on motif correspondence rather than on a solved or modelled PP_2389 structure. An AlphaFold model of Q88KA1 exists (UniProt cross-references AlphaFoldDB) and would be the natural way to confirm that Cys46 points into a heme pocket.

## 4. Genomic context gives no pathway assignment

KEGG places PP_2389 at complement(2727324..2728112), with these neighbours:

| Locus | Annotation | Strand/position |
|---|---|---|
| PP_2386 | conserved protein of unknown function | complement(2724739..2725569) |
| PP_2387 | conserved protein of unknown function | complement(2725573..2726655) |
| PP_2388 | transporter, LysE family | complement(2726695..2727321) |
| **PP_2389** | **conserved protein of unknown function** | **complement(2727324..2728112)** |
| PP_2390 | transcriptional regulator, LysR family | 2728273..2729193 |
| PP_2392 | putative major facilitator family transporter | 2729554..2730597 |

Two points are worth noting, but neither is strong evidence:

- PP_2388 lies immediately upstream on the same strand, with only a 3-bp gap to PP_2389, so the two are plausibly co-transcribed. **LysE-family transporters export basic amino acids** — the founding member, *Corynebacterium glutamicum* LysE, is a lysine/arginine exporter. A LysE exporter adjacent to a predicted arginine-modifying heme enzyme is suggestive of arginine-related metabolism, and a divergently transcribed LysR/LTTR-family regulator (PP_2390) is the kind of regulator that controls amino-acid catabolic operons. This is an operon-context inference only; I found no transcriptomic or mutant-fitness data to support it.
- There is **no secondary-metabolite gene cluster** here — no NRPS, PKS, arginase homolog or phosphonate genes of the sort that accompany DcsA, AglA or GntA. So PP_2389 is probably not part of a natural-product pathway, which distinguishes it from all six characterised family members and makes the "housekeeping-like" YqcI/YcgG subset (to which the *B. subtilis* proteins also belong) the better comparison.

I attempted to retrieve mutant-fitness data for PP_2389 from the LBL Fitness Browser (which has a *P. putida* KT2440 RB-TnSeq dataset), but the server returned a Cloudflare challenge page rather than data. That resource should be checked manually at https://fit.genomics.lbl.gov/ — a phenotype under a specific nitrogen or amino-acid condition would be the single most informative piece of missing evidence.

## 5. What can and cannot be said about function

**Reasonably supported:**

1. **Molecular function: heme binding**, via a cysteine thiolate. Supported by the spectroscopic demonstration that DcsA (41% identical) is a heme protein (PMID:22547619), by the AglA crystal structures showing Cys44-ligated heme as the family architecture (PMID:41221789), and by conservation of the F-P-C motif at PP_2389 Cys46.
2. **Molecular function: oxidoreductase, acting on a guanidino N–H to form an N-hydroxy product.** This is the unifying chemistry of every characterised family member. For PP_2389 it is a family-level inference, not a measured activity.
3. **Localization: cytoplasm.** PP_2389 has no signal peptide, no transmembrane segment and no lipoprotein motif in UniProt's feature set; the characterised members are soluble proteins purified from *E. coli* cytoplasm and assayed in vitro with soluble redox partners. No localisation claim is made experimentally for any family member, so this rests on the absence of targeting signals plus the soluble behaviour of homologs.
4. **Requires an external electron donor** — NAD(P)H via a ferredoxin/ferredoxin reductase or a PDR/VanB-class reductase (PMID:41427725-adjacent work; Sun et al. 2026). PP_2389 itself has no reductase domain, so a partner protein must supply electrons. Identifying that partner in *P. putida* is an open question.

**Not supported / unknown:**

- **The substrate.** Free L-arginine, a modified arginine, or another guanidine-containing metabolite (agmatine, guanidinobutyrate, creatine-like compounds) are all possible. Note that wild-type AglA is "essentially inactive for free arginine", so one cannot assume free arginine is the default substrate for an uncharacterised member.
- **The regiochemistry** (Nω vs Nδ vs Nε), which in AglA is set by residues that differ in PP_2389.
- **The pathway.** *P. putida* KT2440 has rich arginine catabolism (arginine succinyltransferase, arginine decarboxylase/agmatine, arginine deiminase routes), but I found no evidence linking PP_2389 to any of them.
- Any **phenotype** of a PP_2389 mutant.

## 6. Suggested annotation and next steps

A defensible annotation set, all by sequence/ortholog inference (ISS/ISM-type evidence, not experimental):

- `GO:0020037` heme binding — confident
- `GO:0046872` metal ion binding / `GO:0005506` iron ion binding — confident
- `GO:0016705` oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen — plausible at this level of generality
- `GO:0005737` cytoplasm — plausible, from absence of targeting signals

I would *not* propose a specific activity term such as N(ω)-hydroxy-L-arginine synthase for PP_2389. That term fits DcsA, where knockout plus chemical complementation establishes the product, but for PP_2389 the substrate is unknown and the family demonstrably varies its regiochemistry and substrate between members.

The experiments that would settle this:

1. **Heterologous expression and UV-visible spectroscopy** — a Soret band near 420 nm with a thiolate-type ferrous-CO shift would confirm the cysteine-ligated heme directly, exactly as was done for DcsA.
2. **Activity screen against a guanidine panel** (L-Arg, agmatine, homoarginine, guanidinobutyrate, arginine-containing peptides) with NADPH plus ferredoxin/ferredoxin reductase, reading products by LC-HRMS/MS for the +16 Da N-hydroxy species.
3. **Check RB-TnSeq fitness data** for PP_2389 across the *P. putida* condition set, especially nitrogen and amino-acid sources.
4. **Confirm the PP_2388–PP_2389 operon** by RT-PCR and test whether PP_2390 (LysR-family) regulates it; a shared inducer would name the metabolic context.
5. **AlphaFold model superposition onto 9UB5** to verify Cys46 heme coordination and to read off the substrate-clamp residues that correspond to AglA Phe152/Arg179/Phe182.

## Sources

- [Sun et al., A Dynamic Gate Enables Regioselective Hydroxylation of Free Arginine by a Non-Canonical Heme Enzyme, Adv Sci 2026 (PMC12866846)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12866846/) · [Wiley](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202513032) · [PubMed 41221789](https://pubmed.ncbi.nlm.nih.gov/41221789/) · [DOAJ record](https://doaj.org/article/0542e2ac7cbc4ac59eec38dadeee8173)
- PDB: [9UB5 AglA–Arg](https://www.ncbi.nlm.nih.gov/Structure/pdb/9UB5) · [9UB3 apo](https://rcsb.org/structure/9ub3) · [9UBB](https://pdbj.org/mine/summary/9ubb) · [9UBT](https://rcsb.org/structure/9ubt) · [9UBS](https://pdbj.org/mine/summary/9ubs) · [9UBA](https://pdbj.org/mine/summary/9uba)
- D-cycloserine / DcsA: [KEGG K19741](https://www.kegg.jp/entry/K19741) · [KEGG EC 3.5.3.25](https://www.kegg.jp/entry/3.5.3.25) · [KEGG ag:BAI70376](https://www.kegg.jp/entry/ag:BAI70376) · [PMC2825969](https://pmc.ncbi.nlm.nih.gov/articles/PMC2825969) · [PMC3716191](https://pmc.ncbi.nlm.nih.gov/articles/PMC3716191/) · [Rhea 36791](https://rhea-db.org/rhea/36791) · [Rhea 36263](https://rhea-db.org/rhea/36263)
- Chalkophomycin N-hydroxypyrrole-forming enzymes: [bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.01.24.577118v2.full)
- Guanidine natural products: [Gramibactin graminine, ACS Chem Biol](https://pubs.acs.org/doi/10.1021/acschembio.2c00593)
- KT2440 genome: [Nelson et al. 2002](https://umiacswww-vip.umiacs.umd.edu/node/19075) (PMID:12534463); Belda et al. 2016 (PMID:26913973)
- Local data: `genes/PSEPK/PP_2389/PP_2389-uniprot.txt`, `PP_2389-goa.tsv`, `interpro/panther/PTHR40045/`; UniProt REST (Q88KA1, D2Z024, P94382, P45944); KEGG REST (ppu:PP_2386–PP_2392)

**One honest limitation to flag:** the reference list entries for GntA, ChmN, AmbT, Mhr24, the miharamycin and ambocidin papers came through a summarising fetch of the Sun et al. page rather than from the verbatim reference list, so those author/PMID pairings should be verified against PubMed before being written into a review file. The claims I have quoted verbatim (the family description, Cys44 ligation, the fold, the gate residues, the mutant regiochemistry) are from the article text itself.

## Citations

1. https://www.kegg.jp/entry/K19741
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3716191/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC2825969
4. https://www.biorxiv.org/content/10.1101/2024.01.24.577118v2.full
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC12866846/
6. https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202513032
7. https://pubmed.ncbi.nlm.nih.gov/41221789/
8. https://www.ncbi.nlm.nih.gov/Structure/pdb/9UB5
9. https://pdbj.org/mine/summary/9ubb
10. https://fit.genomics.lbl.gov/
11. https://doaj.org/article/0542e2ac7cbc4ac59eec38dadeee8173
12. https://rcsb.org/structure/9ub3
13. https://rcsb.org/structure/9ubt
14. https://pdbj.org/mine/summary/9ubs
15. https://pdbj.org/mine/summary/9uba
16. https://www.kegg.jp/entry/3.5.3.25
17. https://www.kegg.jp/entry/ag:BAI70376
18. https://rhea-db.org/rhea/36791
19. https://rhea-db.org/rhea/36263
20. https://pubs.acs.org/doi/10.1021/acschembio.2c00593
21. https://umiacswww-vip.umiacs.umd.edu/node/19075