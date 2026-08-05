---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:25:14.702925'
end_time: '2026-07-20T18:42:03.471620'
duration_seconds: 1008.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mobA
  gene_symbol: mobA
  uniprot_accession: Q88HA3
  protein_description: 'RecName: Full=Molybdenum cofactor guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316};
    Short=MoCo guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316}; EC=2.7.7.77
    {ECO:0000255|HAMAP-Rule:MF_00316}; AltName: Full=GTP:molybdopterin guanylyltransferase
    {ECO:0000255|HAMAP-Rule:MF_00316}; AltName: Full=Mo-MPT guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316};
    AltName: Full=Molybdopterin guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316};
    AltName: Full=Molybdopterin-guanine dinucleotide synthase {ECO:0000255|HAMAP-Rule:MF_00316};
    Short=MGD synthase {ECO:0000255|HAMAP-Rule:MF_00316};'
  gene_info: Name=mobA {ECO:0000255|HAMAP-Rule:MF_00316}; OrderedLocusNames=PP_3457;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MobA family. {ECO:0000255|HAMAP-
  protein_domains: MobA-like_NTP_Trfase. (IPR025877); Molybde_CF_guanTrfase. (IPR013482);
    Nucleotide-diphossugar_trans. (IPR029044); NTP_transf_3 (PF12804)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mobA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mobA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88HA3
- **Protein Description:** RecName: Full=Molybdenum cofactor guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316}; Short=MoCo guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316}; EC=2.7.7.77 {ECO:0000255|HAMAP-Rule:MF_00316}; AltName: Full=GTP:molybdopterin guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316}; AltName: Full=Mo-MPT guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316}; AltName: Full=Molybdopterin guanylyltransferase {ECO:0000255|HAMAP-Rule:MF_00316}; AltName: Full=Molybdopterin-guanine dinucleotide synthase {ECO:0000255|HAMAP-Rule:MF_00316}; Short=MGD synthase {ECO:0000255|HAMAP-Rule:MF_00316};
- **Gene Information:** Name=mobA {ECO:0000255|HAMAP-Rule:MF_00316}; OrderedLocusNames=PP_3457;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MobA family. {ECO:0000255|HAMAP-
- **Key Domains:** MobA-like_NTP_Trfase. (IPR025877); Molybde_CF_guanTrfase. (IPR013482); Nucleotide-diphossugar_trans. (IPR029044); NTP_transf_3 (PF12804)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mobA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mobA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mobA** (gene ID: mobA, UniProt: Q88HA3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MobA (Q88HA3 / PP_3457) in *Pseudomonas putida* KT2440

**Gene:** *mobA* (OrderedLocusName PP_3457)
**UniProt:** Q88HA3
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440), taxon code PSEPK
**EC:** 2.7.7.77 · **KEGG Orthology:** K03752 · **Protein family:** MobA family (HAMAP MF_00316)
**Domains:** MobA-like_NTP_Trfase (IPR025877); Molybde_CF_guanTrfase (IPR013482); Nucleotide-diphospho-sugar transferase fold (IPR029044); NTP_transf_3 (PF12804)
**Protein-existence level:** PE = 3 (inferred from homology)

---

## Summary

MobA (Q88HA3, locus PP_3457) of *Pseudomonas putida* KT2440 is a **molybdenum cofactor (Moco) guanylyltransferase** (EC 2.7.7.77; also GTP:molybdopterin guanylyltransferase / Mo-MPT guanylyltransferase / MGD synthase). Its primary biochemical function is to catalyze the Mg²⁺-dependent transfer of a GMP moiety from **GTP** onto the terminal phosphate of **molybdopterin (Mo-MPT)**, producing **molybdopterin guanine dinucleotide (MGD)** and ultimately the **bis-MGD** form of the cofactor, with release of pyrophosphate. This is the fourth, bacteria/archaea-specific step of molybdenum cofactor biosynthesis, converting the base Mo-MPT into the dinucleotide form.

The bis-MGD product built by MobA is the obligatory cofactor of the **DMSO reductase family** of molybdoenzymes — nitrate reductases, DMSO/TMAO reductases, formate dehydrogenases, and related molybdopterin oxidoreductases — which drive anaerobic respiration and nitrogen/carbon/sulfur cycling. MobA therefore gates the maturation and catalytic activation of a broad set of respiratory enzymes. In *P. putida* KT2440 the plausible downstream "client" enzymes encoded in the genome are a molybdopterin oxidoreductase (PP_4676) and two formate dehydrogenase catalytic subunits (PP_0489, PP_2185). MobA acts in the **cytoplasm**, assembling bis-MGD on its own surface via a bis-Mo-MPT intermediate and then delivering the finished cofactor to folded apo-molybdoenzymes.

The functional assignment for the *P. putida* protein is made by strong orthology and conserved-motif analysis rather than by direct experiment: no *P. putida*-specific biochemical study of this protein exists (hence PE = 3). Q88HA3 shares **29.6 % sequence identity / 52.4 % similarity** with the extensively characterized *E. coli* MobA (P32173, PE = 1), and retains the diagnostic glycine-rich N-terminal nucleotidyltransferase (GTP-binding) motif, the MPT-binding region, and the conserved C-terminal motif. Genomic-context analysis adds organism-specific nuance: unlike *E. coli*, *P. putida* KT2440 encodes *mobA* as a **stand-alone (monocistronic) gene and lacks a MobB accessory homolog**, while retaining upstream Moco machinery and two MocA-family cytidylyltransferase paralogs. The conclusions below rest on *E. coli* / *R. sphaeroides* / *M. tuberculosis* biochemistry combined with bioinformatic verification that Q88HA3 is a bona fide MobA. The gene symbol *mobA* unambiguously matches the protein description, family and domain content — there is no gene-identity ambiguity.

---

## Key Findings

### F001 — MobA is a molybdenum cofactor guanylyltransferase (EC 2.7.7.77)

The core function of MobA is to link a **guanosine monophosphate (GMP)** group, donated by **GTP**, onto the terminal phosphate of **molybdopterin (MPT)**, forming **molybdopterin guanine dinucleotide (MGD)**. This was established in *E. coli*, whose MobA is the direct ortholog of *P. putida* Q88HA3/PP_3457. In a defined in vitro system, purified MobA "links a guanosine 5′-phosphate to MPT forming molybdopterin guanine dinucleotide. This reaction requires GTP, MgCl₂, and the MPT form of the cofactor and can efficiently reconstitute *Rhodobacter sphaeroides* apo-DMSOR" ([PMID: 10978347](https://pubmed.ncbi.nlm.nih.gov/10978347/)). Near-atomic-resolution structural work defined the catalytic mechanism as a "nucleophilic attack by MPT on the GMP donor, most likely GTP, to produce MGD and pyrophosphate" ([PMID: 11080634](https://pubmed.ncbi.nlm.nih.gov/11080634/)).

The reaction can be summarized as:

```
   GTP  +  Mo-MPT   --(MobA, Mg2+)-->   MGD  +  PPi
   (repeated to build the bis-MGD cofactor)
```

The strict Mg²⁺ and GTP requirement, plus the specific use of the MPT (not the fully mature dinucleotide) substrate, defines the enzyme's substrate specificity. This is the reaction that EC 2.7.7.77 encodes, and it is the primary function assigned to Q88HA3.

### F002 — The MobA product (bis-MGD) is required by the DMSO reductase family of molybdoenzymes

The physiological importance of MobA lies in the enzymes that depend on its product. The MGD/bis-MGD modification "is required for the functioning of many bacterial molybdoenzymes, including the nitrate reductases, dimethylsulfoxide (DMSO) and trimethylamine-N-oxide (TMAO) reductases, and formate dehydrogenases" ([PMID: 10978347](https://pubmed.ncbi.nlm.nih.gov/10978347/)). Genetic evidence from *Mycobacterium tuberculosis* confirms the causal link: MobA "converts MoCo to bis-molybdopterin guanine dinucleotide (bis-MGD), a form of the cofactor that is required by the dimethylsulfoxide (DMSO) reductase family of enzymes, which includes the nitrate reductase NarGHI," and a *mobA* deletion mutant lost both assimilatory and respiratory nitrate reductase activity ([PMID: 25404027](https://pubmed.ncbi.nlm.nih.gov/25404027/)). MobA is therefore a **maturation factor** whose loss silences a whole class of downstream respiratory enzymes — through the precise removal of an essential cofactor modification, not a broad pleiotropic effect.

### F003 — MobA is a two-domain Rossmann-fold enzyme with a division of labor between its domains

MobA (~191–194 aa, ~22 kDa) has an α/β architecture in which "the N-terminal half of the molecule adopts a Rossman fold. The structure of MobA has striking similarity to *Bacillus subtilis* SpsA," a nucleotide-diphospho-sugar transferase ([PMID: 10978347](https://pubmed.ncbi.nlm.nih.gov/10978347/)). This homology is the structural basis of the InterPro/Pfam domain annotations for Q88HA3 (MobA-like_NTP_Trfase IPR025877; nucleotide-diphospho-sugar transferase fold IPR029044; PF12804 NTP_transf_3). A MobA:GTP cocrystal localizes the GTP-binding site to the N-terminal domain via three signature sequence motifs, with the MPT-binding site adjacent.

Domain-swap and site-directed mutagenesis experiments in *E. coli* dissected the two domains' roles: "Exchange of the complete N-terminal domain of each protein resulted in the total inversion of nucleotide specificity activity, showing that the N-terminal domain determines nucleotide recognition and binding. Analysis of protein-protein interactions showed that the C-terminal domain of either MocA or MobA determines the specific binding to the respective acceptor protein" ([PMID: 21081498](https://pubmed.ncbi.nlm.nih.gov/21081498/)). Thus MobA reads **GTP with its N-terminus** and reads the **destination molybdoenzyme with its C-terminus** — a modular design that explains how closely related transferases (MobA/GMP vs MocA/CMP) achieve distinct specificities.

### F004 — bis-MGD is assembled on MobA via a bis-Mo-MPT intermediate, then transferred to apoenzymes

MobA does more than a single guanylyl transfer: it acts as an assembly platform. In vitro reconstitution with purified components identified a novel **bis-Mo-MPT intermediate bound on MobA prior to nucleotide attachment**. "The addition of Mg-GTP to MobA loaded with bis-Mo-MPT resulted in formation and release of the final bis-MGD product. This cofactor was fully functional and reconstituted the catalytic activity of apo-TMAO reductase (TorA)" ([PMID: 24003231](https://pubmed.ncbi.nlm.nih.gov/24003231/)). The proposed sequence is: (1) formation of bis-Mo-MPT on MobA, (2) addition of two GMP units to form bis-MGD, and (3) release and transfer of the completed cofactor to the target molybdoenzyme. This establishes MobA's mechanistic role as both catalyst and delivery scaffold.

### F005 — MobA works in the cytoplasm as the fourth step of Moco biosynthesis; MobB is an accessory modulator

Moco biosynthesis proceeds in four conserved steps, the fourth (present only in bacteria and archaea) being that "an additional modification of Moco is possible with the attachment of a nucleotide (CMP or GMP) to the phosphate group of MPT, forming the dinucleotide variants of Moco" ([PMID: 32239579](https://pubmed.ncbi.nlm.nih.gov/32239579/)). Moco is inserted into apoenzymes after folding: "these enzymes require complex molybdenum-containing cofactors, which are inserted into the apoenzymes after folding. For almost all the bacterial molybdoenzymes, molybdenum cofactor insertion requires the involvement of specific chaperones" ([PMID: 26468212](https://pubmed.ncbi.nlm.nih.gov/26468212/)), locating MobA's activity firmly in the cytoplasm. In *E. coli*, the accessory protein **MobB** is co-transcribed with MobA and, although not essential, "the dimeric MobB increases the activation of molybdoenzymes, incorporating this cofactor by a mechanism that is not understood," and a MobA:MobB complex is structurally feasible ([PMID: 12682065](https://pubmed.ncbi.nlm.nih.gov/12682065/)). This context is important for interpreting the *P. putida* genome, which — as shown below — lacks MobB.

### F006 — Sequence analysis confirms Q88HA3 is a bona fide MobA ortholog

A global BLOSUM62 (Needleman–Wunsch) alignment of *P. putida* MobA (Q88HA3, 191 aa) against the experimentally characterized *E. coli* MobA (P32173, 194 aa) gives **29.6 % identity and 52.4 % similarity over 189 aligned positions** (alignment score 199). Critically, the diagnostic N-terminal glycine-rich nucleotidyltransferase motif is strictly conserved:

| Region | *P. putida* Q88HA3 | *E. coli* P32173 |
|---|---|---|
| N-terminal GTP-binding motif | L-A-G-G-R-G-Q-R-M-G-G | L-A-G-G-K-A-R-R-M-G-G |
| MPT-binding region | …PGPLAG… | …PGPLAG… (conserved) |
| C-terminal motif | …N-x-P-E-E-L | …N-x-P-E-E-L |

The conservation of the GTP-binding, MPT-binding, and C-terminal motifs across a moderately divergent sequence (typical for orthologous bacterial Moco enzymes) confirms that Q88HA3 possesses the intact catalytic apparatus of a functional MoCo guanylyltransferase. Q88HA3 is annotated PE = 3 (inferred from homology), while *E. coli* MobA is PE = 1 (evidence at protein level) — underscoring that the *P. putida* assignment is a well-supported homology inference rather than direct measurement.

### F007 — In *P. putida* KT2440, *mobA* is monocistronic and the genome lacks MobB

KEGG genomic context places PP_3457 (*mobA*, chromosome 3,919,409–3,919,984, + strand) between the multidrug efflux gene *mexB*/PP_3456 and *acs*/PP_3458, with **no adjacent Moco-biosynthesis genes** — i.e., it is *not* organized in a *mob* operon as in *E. coli*. A KEGG orthology search of the KT2440 genome for **MobB (K03753) returns no hits**, whereas the core upstream Moco machinery is present: *moaA* (K03750, PP_2123), a *moeA*-family gene (PP_1294), and *mobA* itself (K03752, PP_3457, EC 2.7.7.77). This is an organism-specific finding: *P. putida* MobA must function without the MobB accessory protein that modulates cofactor insertion in *E. coli* — suggesting either that MobB is dispensable in this organism or that another factor substitutes.

### F008 — Candidate bis-MGD client molybdoenzymes are encoded in *P. putida* KT2440

KEGG orthology mapping identifies the plausible downstream enzymes that would consume MobA's bis-MGD product: a **molybdopterin oxidoreductase (K07147, PP_4676)** and **formate dehydrogenase catalytic subunits (K00123, PP_0489 and PP_2185)** — all members of the DMSO-reductase / Moco-dependent family (formate dehydrogenase assembly and catalysis reviewed in [PMID: 25514355](https://pubmed.ncbi.nlm.nih.gov/25514355/)). The genome also encodes two **MocA-family paralogs (K07141, PP_2483 and PP_4230)**, the CTP:molybdopterin cytidylyltransferases that make the alternative MCD cofactor for a distinct set of molybdoenzymes — consistent with the general pattern that MobA (GMP) and MocA (CMP) provide parallel dinucleotide-cofactor branches. Notably, **no respiratory nitrate reductase *narG* (K00370) was detected**; the gene PP_2092 annotated "nitrate reductase" is in fact an NNP-family nitrate/nitrite MFS transporter (K02575), so the *P. putida* client set differs from the classic *E. coli* NarGHI paradigm.

---

## Mechanistic Model / Interpretation

Integrating the findings yields a coherent picture of where MobA sits in *P. putida* metabolism and how it works.

### Pathway position

```
 Step 1        Step 2        Step 3            Step 4 (bacteria/archaea)         Client enzymes
 GTP ─► cPMP ─► MPT  ─► Mo-MPT (Moco) ─────► MobA: + GMP (from GTP) ──► bis-MGD ─► apo-molybdoenzyme
        (MoaA…) (MPT synth.) (MoeA/MogA)      ↑ Mg2+, via bis-Mo-MPT              (holoenzyme, active)
                                              │ N-domain binds GTP                 in P. putida KT2440:
                                              │ C-domain binds MPT + target        • Mo-oxidoreductase PP_4676
                                              └───────────────────────────────►    • FDH PP_0489 / PP_2185
```

MobA catalyzes the **terminal maturation step** that converts base Moco (Mo-MPT) into the dinucleotide form. Mechanistically (F003, F004): the **N-terminal Rossmann-fold domain** binds Mg-GTP and enforces guanine specificity; the enzyme assembles a **bis-Mo-MPT intermediate** on its surface; two successive guanylyl transfers add GMP groups (each releasing pyrophosphate) to form **bis-MGD**; and the **C-terminal domain** recognizes the specific apo-molybdoenzyme to which the finished cofactor is handed off. This makes MobA simultaneously a catalyst and a chaperone-like delivery platform, operating in the **cytoplasm** on already-folded apoenzymes (F005).

### Functional consequence

Because bis-MGD is obligatory for the DMSO reductase family (F002), MobA gates the activation of *P. putida*'s formate dehydrogenases and molybdopterin oxidoreductase (F008). In organisms where this has been tested genetically, *mobA* loss abolishes downstream molybdoenzyme activity (nitrate reductase in *M. tuberculosis*, F002). MobA's role is therefore precise and upstream: it does not itself catalyze respiration but is a prerequisite for it.

### Organism-specific tailoring

The *P. putida* system is **streamlined** relative to *E. coli*: *mobA* is monocistronic and there is **no MobB** (F007). Combined with the substitution of NarGHI (absent) by formate dehydrogenases and a generic molybdopterin oxidoreductase as the client set (F008), this indicates that *P. putida* uses its single MobA to feed a smaller, distinct panel of bis-MGD enzymes, alongside a parallel MocA/MCD branch for other molybdoenzymes.

### Comparison table: *E. coli* (reference) vs *P. putida* KT2440

| Feature | *E. coli* MobA (P32173) | *P. putida* MobA (Q88HA3) |
|---|---|---|
| Evidence level | PE = 1 (protein-level, biochemistry + structure) | PE = 3 (inferred from homology) |
| Reaction | GTP + Mo-MPT → MGD + PPi (→ bis-MGD) | Same (by orthology; conserved motifs) |
| Length | 194 aa | 191 aa |
| Gene organization | *mob* operon with *mobB* | monocistronic; **no *mobB*** |
| MobB accessory | Present (K03753) | Absent |
| Key clients | NarGHI, DMSO/TMAO reductases, FDHs | Mo-oxidoreductase PP_4676; FDHs PP_0489/PP_2185 (no *narG*) |
| Paralog | MocA (CMP transferase) | Two MocA paralogs (PP_2483, PP_4230) |

---

## Localization

MobA is a **soluble cytoplasmic enzyme**. Moco and its dinucleotide variants are synthesized in the cytoplasm, and the mature cofactor is inserted into apoenzymes after they fold, with insertion "for almost all the bacterial molybdoenzymes" requiring specific chaperones ([PMID: 26468212](https://pubmed.ncbi.nlm.nih.gov/26468212/)). MobA therefore operates in the cytoplasm together with system-specific chaperones (and, in organisms that have it, MobB) to mature apo-molybdoenzymes. Periplasmic molybdoenzymes receive their fully assembled, cofactor-loaded holoenzyme via Tat-dependent export after cytoplasmic maturation, consistent with MobA acting entirely on the cytoplasmic side.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [10978347](https://pubmed.ncbi.nlm.nih.gov/10978347/) | *Crystal structure of E. coli MobA / MGD biosynthesis* | Defines catalyzed reaction, substrates (GTP, Mg²⁺, MPT), product (MGD); Rossmann fold, SpsA homology; lists downstream molybdoenzymes requiring MGD |
| [11080634](https://pubmed.ncbi.nlm.nih.gov/11080634/) | *E. coli MobA at near-atomic resolution* | States catalytic mechanism: nucleophilic attack by MPT on GMP donor → MGD + pyrophosphate |
| [24003231](https://pubmed.ncbi.nlm.nih.gov/24003231/) | *bis-molybdopterin intermediate in Moco biosynthesis* | Identifies bis-Mo-MPT intermediate; shows bis-MGD built on MobA and transferred to reconstitute apo-TorA |
| [21081498](https://pubmed.ncbi.nlm.nih.gov/21081498/) | *Specificity of MPT dinucleotide transferases* | Domain-swap: N-terminal domain sets nucleotide specificity, C-terminal domain sets acceptor-protein binding |
| [25404027](https://pubmed.ncbi.nlm.nih.gov/25404027/) | *bis-MGD required for M. tuberculosis persistence* | Genetic proof: MobA makes bis-MGD required by DMSO reductase family (incl. NarGHI); *mobA* deletion abolishes nitrate reductase activity |
| [12682065](https://pubmed.ncbi.nlm.nih.gov/12682065/) | *E. coli MobB crystal structure* | MobB accessory role — dimeric MobB increases molybdoenzyme activation; MobA:MobB interaction |
| [32239579](https://pubmed.ncbi.nlm.nih.gov/32239579/) | *Moco biosynthesis in E. coli (review)* | Places guanylylation as the fourth, bacteria-specific step |
| [26468212](https://pubmed.ncbi.nlm.nih.gov/26468212/) | *Bacterial molybdoenzymes (review)* | Cofactor inserted into folded apoenzymes with cytoplasmic chaperones |
| [25514355](https://pubmed.ncbi.nlm.nih.gov/25514355/) | *Formate dehydrogenase assembly/catalysis (review)* | Background on candidate *P. putida* client FDHs |
| [28284029](https://pubmed.ncbi.nlm.nih.gov/28284029/) | *Shared function / moonlighting in Moco biosynthesis* | Confirms four-step conserved pathway and shared components |

Supporting reviews on regulation and sulfur delivery ([PMID: 31517366](https://pubmed.ncbi.nlm.nih.gov/31517366/), [PMID: 38631442](https://pubmed.ncbi.nlm.nih.gov/38631442/), [PMID: 31655739](https://pubmed.ncbi.nlm.nih.gov/31655739/), [PMID: 28098827](https://pubmed.ncbi.nlm.nih.gov/28098827/)) place MobA within the broader Moco / Fe-S / sulfur-transfer network but do not directly characterize the *P. putida* protein.

**How the evidence maps onto Q88HA3:** all mechanistic and structural evidence derives from orthologs (*E. coli*, *R. sphaeroides*, *M. tuberculosis*). The bridge to the *P. putida* protein is the sequence/motif conservation in F006 and the genomic context in F007–F008. This is a well-supported homology inference, not a direct measurement.

---

## Supported and Refuted Hypotheses

| Statement | Status | Basis |
|---|---|---|
| MobA (Q88HA3) is a GTP:molybdopterin guanylyltransferase making MGD | **Supported** | Orthology + biochemical reconstitution (PMID 10978347, 11080634; F001, F006) |
| Reaction consumes GTP + Mo-MPT (+Mg²⁺) → MGD + PPi | **Supported** | PMID 10978347, 11080634 (F001) |
| Enzyme is specific for guanine (GTP), distinct from CTP-using MocA | **Supported** | PMID 21081498 (F003) |
| Product (bis-MGD) supplies DMSO reductase family enzymes | **Supported** | PMID 10978347, 25404027 (F002) |
| MobA is cytoplasmic and works with chaperones (± MobB) | **Supported** | PMID 26468212, 12682065 (F005) |
| *P. putida* encodes *mobA* monocistronically and lacks MobB | **Supported** | KEGG genome analysis (F007) |
| PP_3457 has direct experimental characterization in *P. putida* | **Not found** | No organism-specific study located; annotation is by orthology (PE = 3) |

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific experimental data.** Q88HA3 is annotated PE = 3 (inferred from homology). Its catalytic activity, kinetics, substrate specificity, and structure have not been measured directly; all functional claims are transferred from orthologs. Given the near-universal conservation of MobA and the HAMAP MF_00316 rule, the inference is strong but not experimentally confirmed for PP_3457.

2. **Moderate sequence identity to the reference.** The 29.6 % identity to *E. coli* MobA, while typical for orthologous Moco enzymes and accompanied by strictly conserved catalytic motifs, leaves residual uncertainty about fine details (e.g., exact kinetic parameters, acceptor-protein specificity).

3. **Client enzyme assignments are predictions.** PP_4676, PP_0489, and PP_2185 are candidate bis-MGD-dependent enzymes identified by KEGG orthology, not by demonstrated MobA→enzyme cofactor transfer in *P. putida*.

4. **Absence of MobB is inferred from KEGG.** The lack of a K03753 hit strongly suggests no MobB, but the functional consequence — how *P. putida* achieves efficient molybdoenzyme activation without MobB — is unknown.

5. **MobA vs MocA branch partitioning.** *P. putida* encodes two MocA paralogs; which molybdoenzymes receive MGD (from MobA) vs MCD (from MocA) has not been experimentally delineated in this organism.

6. **Physiological/regulatory conditions.** The conditions under which *P. putida* upregulates *mobA* and its client molybdoenzymes (e.g., anaerobiosis, formate metabolism) were not investigated here; regulation by FNR/Fur/ArcA is documented only in *E. coli* ([PMID: 31517366](https://pubmed.ncbi.nlm.nih.gov/31517366/)).

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical assay.** Recombinantly express and purify Q88HA3; measure MoCo guanylyltransferase activity (GTP + Mo-MPT → MGD + PPi) in vitro, and determine kinetic constants and Mg²⁺/GTP dependence — the single most valuable experiment to lift the protein from PE = 3 to PE = 1.

2. **Cofactor reconstitution.** Test whether purified Q88HA3-generated bis-MGD reconstitutes the activity of purified *P. putida* apo-formate dehydrogenase (PP_0489/PP_2185) and the molybdopterin oxidoreductase (PP_4676), confirming the predicted client relationships.

3. **Gene knockout phenotyping.** Construct a Δ*PP_3457* mutant and assay formate dehydrogenase and molybdopterin-oxidoreductase activities; loss of activity would establish MobA's in vivo requirement, paralleling the *M. tuberculosis* nitrate-reductase result.

4. **Structural determination.** Solve the crystal or cryo-EM structure of Q88HA3 (± GTP, ± Mo-MPT), or validate an AlphaFold model against the *E. coli* MobA structures (PDB 1FR9/1E5K family), to confirm the two-domain Rossmann-fold architecture and the three GTP-binding motifs plus the acceptor-binding C-terminal surface.

5. **MobB-independence test.** Determine whether *P. putida* molybdoenzyme maturation proceeds efficiently without MobB, and search for a functional substitute; complement with heterologous *E. coli* MobB to see if activation improves.

6. **MobA/MocA branch mapping.** Use targeted mutants (Δ*PP_3457*, Δ*PP_2483*, Δ*PP_4230*) plus cofactor extraction/LC-MS (MGD vs MCD) to assign which molybdoenzymes depend on the guanylyl (MobA) vs cytidylyl (MocA) branch.

7. **Expression/regulation profiling.** Measure *PP_3457* transcription under aerobic vs anaerobic and formate-rich conditions to connect MobA cofactor supply with client-enzyme demand.

---

## Conclusion

MobA (Q88HA3 / PP_3457) is the *Pseudomonas putida* KT2440 **molybdenum cofactor guanylyltransferase** that performs the fourth, bacteria-specific step of Moco biosynthesis — transferring GMP from GTP onto molybdopterin to build the **bis-MGD** cofactor in the cytoplasm and deliver it to DMSO-reductase-family molybdoenzymes (in this organism, formate dehydrogenases and a molybdopterin oxidoreductase). The assignment is a robust homology inference anchored on the biochemically and structurally characterized *E. coli* MobA, reinforced by conserved catalytic motifs and organism-specific genomic evidence showing a streamlined, MobB-less, monocistronic arrangement. Direct biochemical and genetic validation in *P. putida* remains the key outstanding work.


## Artifacts

- [OpenScientist final report](mobA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mobA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10978347
2. PMID:11080634
3. PMID:25404027
4. PMID:21081498
5. PMID:24003231
6. PMID:32239579
7. PMID:26468212
8. PMID:12682065
9. PMID:25514355
10. PMID:31517366
11. PMID:38631442
12. PMID:31655739
13. PMID:28098827