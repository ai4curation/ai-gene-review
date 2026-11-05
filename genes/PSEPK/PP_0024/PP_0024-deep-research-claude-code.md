---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:35.802266'
end_time: '2026-10-30T21:35:55.187832'
duration_seconds: 199.39
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0024
  gene_symbol: PP_0024
  uniprot_accession: Q88RV5
  protein_description: 'SubName: Full=Membrane-associated metal-dependent hydrolase
    {ECO:0000313|EMBL:AAN65658.1};'
  gene_info: OrderedLocusNames=PP_0024 {ECO:0000313|EMBL:AAN65658.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Alkaline_phosphatase_core_sf. (IPR017850); EptA-like_N. (IPR012549);
    PEA_transf_C. (IPR058130); PEA_transferase. (IPR040423); Sulfatase_N. (IPR000917)
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
  num_turns: 10
  total_cost_usd: 0.8464098
  session_id: 39c1a5a7-2f09-4fbf-a50a-4b8722cbae95
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88RV5
- **Protein Description:** SubName: Full=Membrane-associated metal-dependent hydrolase {ECO:0000313|EMBL:AAN65658.1};
- **Gene Information:** OrderedLocusNames=PP_0024 {ECO:0000313|EMBL:AAN65658.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Alkaline_phosphatase_core_sf. (IPR017850); EptA-like_N. (IPR012549); PEA_transf_C. (IPR058130); PEA_transferase. (IPR040423); Sulfatase_N. (IPR000917)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0024" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0024' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0024** (gene ID: PP_0024, UniProt: Q88RV5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I found no published experiments on PP_0024 itself, so I'm writing the report from the UniProt record, its domain and family assignments, a check of the sequence motifs, and the published work on EptA homologs.

# PP_0024 (UniProt Q88RV5), *Pseudomonas putida* KT2440: research report

## 1. Identity check and how much literature exists

| Feature | Value (source: local UniProt record `PP_0024-uniprot.txt`) |
|---|---|
| Accession | Q88RV5 (TrEMBL, unreviewed; PE 4 = predicted) |
| Locus | PP_0024 (EMBL AAN65658.1; RefSeq WP_003298414.1) |
| Organism | *P. putida* KT2440 (NCBI taxon 160488) |
| Length | 565 aa, 62.4 kDa |
| Submitted name | "Membrane-associated metal-dependent hydrolase" (taken unchanged from the genome submission, ECO:0000313) |
| Family | PANTHER PTHR30443:SF0 "PHOSPHOETHANOLAMINE TRANSFERASE EPTA"; NCBIfam NF028537 (P_eth_NH2_trans); eggNOG COG2194; CDD cd16017 "LptA" |
| Domains | Pfam PF08019 EptA_B_N (residues 75–224); Pfam PF00884 Sulfatase (252–539); InterPro IPR040423 PEA_transferase, IPR058130 PEA_transf_C, IPR017850 alkaline phosphatase core superfamily |
| Topology | 5 predicted transmembrane helices (Phobius: 27–46, 66–87, 94–116, 136–156, 168–188), then a large soluble C-terminal domain |

**Verification.** The locus tag, organism and domain composition all agree with each other. Every family classifier (PANTHER subfamily, NCBIfam, CDD, Pfam) puts PP_0024 in the **lipid A phosphoethanolamine (PEtN) transferase family, EptA/LptA/MCR**. The name "metal-dependent hydrolase" is a genome-submission label. The family is metal (Zn²⁺) dependent and works through a hydrolase-like covalent intermediate, but it is a transferase.

**Literature limitation.** I found **no primary paper that characterizes PP_0024 or Q88RV5 experimentally.** Targeted searches on *P. putida* EptA, lipid A pEtN and PP_0024 found nothing specific to this gene. Everything below is inferred from homology with characterized family members, chiefly *P. aeruginosa* EptA and *Neisseria*/*E. coli* EptA. Treat it as a prediction.

## 2. Predicted molecular function

### 2.1 Reaction
EptA-family enzymes move a phosphoethanolamine group from the membrane phospholipid **phosphatidylethanolamine (PE)** onto a phosphate of **lipid A**, the hydrophobic anchor of lipopolysaccharide (LPS). Diacylglycerol is released as the by-product:

> PE + lipid A (Kdo-lipid A / LPS) → diacylglycerol + PEtN-lipid A

Structural work on the family states this directly: "Lipid A phosphoethanolamine transferase (EptA) transfers PEA from phosphatidylethanolamine to the 1 and 4′ positions of lipid A" ([IUCrJ 2021](https://journals.iucr.org/m/issues/2021/05/00/jt5059/)).

**Which position (1 or 4′)?** This varies between species. The closest characterized relative is in the same genus: in *P. aeruginosa*, PA14_39020 (PAO1 PA1972) "is a functional pEtN transferase, named EptA_Pa, that strictly modifies the 4′ phosphate group of lipid A" (Nowicki et al. 2015, [PMC4715879](https://pmc.ncbi.nlm.nih.gov/articles/PMC4715879)). In the plant pathogen *P. syringae* pv. phaseolicola, PEtN was reported on both lipid A phosphates ([Kutschera et al. 2022, IJMS, PMC8876380](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8876380/)). The regiospecificity of PP_0024 is therefore unknown. The 4′-phosphate of lipid A is the most likely acceptor by analogy with *P. aeruginosa*.

### 2.2 Catalytic mechanism and sequence features
- In this family, the periplasmic catalytic domain has the alkaline phosphatase/sulfatase fold (PF00884, IPR017850). It binds Zn²⁺ and uses a **threonine nucleophile**, which forms a phospho-Thr (PEtN–Thr) covalent intermediate with PE before

I'll continue the report, picking up from the mechanism section.

# PP_0024 (UniProt Q88RV5), *Pseudomonas putida* KT2440 — research report

## 1. Identity verification

| Feature | Value (UniProt Q88RV5, entry v114) |
|---|---|
| Locus | PP_0024 (EMBL AAN65658.1; RefSeq WP_003298414.1) |
| Organism | *P. putida* KT2440 (taxon 160488) |
| Length / status | 565 aa; TrEMBL unreviewed; **PE 4 = Predicted** |
| Submitted name | "Membrane-associated metal-dependent hydrolase" (ECO:0000313, from the genome submission) |
| Family calls | PANTHER PTHR30443:SF0 *phosphoethanolamine transferase EptA*; NCBIfam NF028537 `P_eth_NH2_trans`; CDD cd16017 `LptA`; COG2194 |
| Domains | PF08019 `EptA_B_N` (75–224); PF00884 `Sulfatase` (252–539); IPR040423 PEA_transferase; IPR017850 alkaline-phosphatase core superfamily |
| Topology | 5 Phobius TM helices (27–46, 66–87, 94–116, 136–156, 168–188) + large soluble C-terminal domain |

The locus tag, organism and domain architecture are mutually consistent. All independent family classifiers place PP_0024 in the **lipid A phosphoethanolamine (pEtN) transferase family** (EptA / LptA / MCR). The submitted name "metal-dependent hydrolase" is a genome-annotation label: this family is Zn²⁺-dependent and has an alkaline-phosphatase-like fold, but it is a transferase, not a hydrolase.

**Literature limitation — stated plainly.** I found **no primary publication characterizing PP_0024 / Q88RV5**. Searches for *P. putida* eptA, PP_0024 lipid A, and *P. putida* pEtN lipid A returned nothing gene-specific; the two references in the UniProt entry are the KT2440 genome paper ([PMID:12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)) and its re-annotation ([PMID:26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/)), neither of which assays the protein. Everything functional below is inference from characterized homologs — chiefly *P. aeruginosa* EptA — and from the sequence itself.

## 2. Predicted molecular function

### 2.1 The reaction
EptA-family enzymes transfer a phosphoethanolamine head group from the inner-membrane phospholipid **phosphatidylethanolamine (PE)** onto a phosphate of **lipid A**, releasing diacylglycerol:

> PE + lipid A → diacylglycerol + pEtN-lipid A

A structural report on the family states it directly: "Lipid A phosphoethanolamine transferase (EptA) transfers PEA from phosphatidylethanolamine to the 1 and 4′ positions of lipid A" ([IUCrJ 2021](https://journals.iucr.org/m/issues/2021/05/00/jt5059/)).

### 2.2 Which phosphate?
Regiospecificity differs among characterized members, so this is genuinely open for PP_0024:
- The nearest characterized relative, *P. aeruginosa* EptA (PA14_39020 / PAO1 PA1972), **"strictly modifies the 4′ phosphate group of lipid A"** — a non-canonical position relative to the enterics ([Nowicki et al. 2015, PMC4715879](https://pmc.ncbi.nlm.nih.gov/articles/PMC4715879)).
- In *P. syringae* pv. phaseolicola, "the addition of P-EtN catalyzed by EptA occurs at both phosphates of lipid A" ([Kutschera et al. 2022, IJMS, PMC8876380](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8876380/)).

The 4′ position is the best single prediction for PP_0024 on genus grounds, but it should be treated as untested.

### 2.3 Mechanism and the sequence evidence for catalytic competence
Family members use the alkaline-phosphatase/sulfatase fold to bind Zn²⁺ and employ a **threonine nucleophile** that forms a covalent phospho-threonine (pEtN–Thr) intermediate with PE before transfer to lipid A — hence the "hydrolase-like" classification of the fold and the metal dependence implied by the submitted name.

I checked the 565-aa sequence for the family's diagnostic residues (`genes/PSEPK/PP_0024/PP_0024-uniprot.txt`, motif positions computed locally):

| Motif | Position in Q88RV5 | Role in the family |
|---|---|---|
| `GETARS` | 257–262 | The catalytic **Thr** of the sulfatase-like active site (Thr259 here), the pEtN acceptor nucleophile |
| `SSCGT` | 290–294 | Conserved region contributing to the Zn²⁺/substrate pocket |
| `HYKGSH` | 394–399 | His pair implicated in metal coordination |
| `SDHGE` | 467–471 | C-terminal `DHG` metal-binding motif of the alkaline-phosphatase fold |

All four signature regions are intact and correctly ordered, with ten cysteines in the periplasmic domain (positions 292, 302, 343, 347, 364, 369, 418, 426, 515, 554) consistent with the disulfide-stabilized catalytic domains seen in EptA/MCR structures. This is a **predicted-active enzyme**, not a degenerate pseudoenzyme: the residues a loss-of-function paralog typically loses are present.

### 2.4 Not a hydrolase — and not an LptA
Two naming hazards worth flagging for annotation:
- The UniProt submitted name ("membrane-associated metal-dependent hydrolase") is a fold-based guess from 2002 and should not drive a GO molecular-function assignment.
- The CDD hit `cd16017 LptA` refers to *lipid A phosphoethanolamine transferase* (the *Neisseria* name for EptA), **not** the LPS-transport protein LptA of the Lpt bridge. These are unrelated proteins that share an abbreviation; conflating them would misplace the protein into LPS export.

## 3. Localization

The predicted location is the **cytoplasmic (inner) membrane**, with the catalytic domain facing the **periplasm**:
- UniProt: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein" — though note this is an ARBA rule-based prediction (ECO:0000256|ARBA:ARBA00004429), i.e. a family-level inference, not experimental.
- Phobius predicts five TM helices confined to residues 27–188, with the ~375-residue catalytic domain (252–539) entirely C-terminal to them — the canonical EptA/MCR architecture: an N-terminal 5-TM anchor plus a periplasmic catalytic domain.

This topology matches the chemistry: the enzyme must reach PE in the inner membrane and lipid A on nascent LPS at the periplasmic face of the inner membrane, where lipid A modification occurs before Lpt-mediated export to the outer membrane. The GOA row `located_in GO:0005886 plasma membrane` (IEA from UniProtKB-SubCell) is the correct compartment at the resolution the evidence supports.

## 4. Pathway context

### 4.1 Lipid A modification, not core biosynthesis
pEtN addition is a **late covalent modification** of an otherwise complete lipid A, one of the regulated "lipid A remodeling" reactions (alongside L-Ara4N addition by ArnT, 3-O-deacylation by PagL, palmitoylation by PagP). Its biological consequence is to mask the net negative charge of the lipid A phosphates, reducing the affinity of cationic antimicrobial peptides and polymyxins and altering outer-membrane permeability and divalent-cation handling.

This matters for how PP_0024 should be annotated. The GOA row `involved_in GO:0009244 lipopolysaccharide core region biosynthetic process` (IEA:TreeGrafter) is, on homology grounds, **the wrong part of the molecule**: pEtN transferases act on lipid A, not on the core oligosaccharide region. A lipid A modification term is the better fit. Likewise the two molecular-function rows (`GO:0016772`, `GO:0016776` phosphotransferase activity, phosphate group as acceptor) are family-level placeholders far above what the family assignment supports; `GO:0016776` in particular is a poor description of a PE→lipid A head-group transfer.

### 4.2 Regulation in *Pseudomonas*: a zinc/ColRS circuit, not PmrAB
The *P. aeruginosa* work is the most informative guide to when such a gene is switched on, and it is strikingly different from the enterics:
- Extracellular **zinc** drives pEtN addition to *P. aeruginosa* lipid A, and this runs through the **ColRS** two-component system: pEtN modification is detectable in PA14 with added zinc but absent in a *colR* deletion mutant ([Nowicki et al. 2015, PMC4715879](https://pmc.ncbi.nlm.nih.gov/articles/PMC4715879)).
- In *E. coli* and *Salmonella* the orthologous gene is controlled by **PmrAB/BasRS** instead, so the *Pseudomonas* regulatory wiring is distinct ([PMC4715879](https://pmc.ncbi.nlm.nih.gov/articles/PMC4715879)).
- A 2023 analysis confirms *eptA* induction by zinc via ColRS and not by other metals, and argues that regulatory constraints limit how much *eptA* contributes to colistin resistance ([Jeannot et al., *Antibiotics* 2023, PMC9952513](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9952513/)).

This is directly relevant because **ColRS is itself a well-studied system in *P. putida***, where it governs membrane and lipid A functions: Kivistik et al. defined the ColR binding consensus from DNase I-mapped motifs and placed the **outer-membrane lipid A 3-O-deacylase PagL** and the **diacylglycerol kinase DgkA** in the ColR regulon ([Kivistik et al. 2009, *BMC Microbiol*, PMC2689224](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2689224/)). DgkA is notable here: it recycles the diacylglycerol that a pEtN transferase releases, so a ColR-controlled module comprising a pEtN transferase, PagL and DgkA would be coherent. **But I did not find PP_0024 among the predicted ColR targets in that paper**, so the link is a hypothesis, not a finding.

### 4.3 Functional consequences reported for homologs
- Overexpression of *P. aeruginosa* EptA impairs growth, and this toxicity "does not account for" — i.e. is separable from — its transferase activity, mapping instead to a C-terminal tail unique to that enzyme ([Cervoni et al. 2021, *Front Microbiol* 12:778968](https://www.frontiersin.org/articles/10.3389/fmicb.2021.778968/full)). Any phenotype from overexpressing PP_0024 would need the same control.
- On resistance, the literature is genuinely split: the 2015 study found zinc-induced pEtN modification did not shift the colistin MIC, whereas Cervoni et al. report EptA and plasmid-borne MCR-1 to have comparable pEtN transferase activity and comparable effects on colistin resistance ([Front Microbiol 2021](https://www.frontiersin.org/articles/10.3389/fmicb.2021.778968/full)). PP_0024 should not be described as a resistance determinant without direct data.

### 4.4 *P. putida* lipid A is characterized, but PP_0024's product is not
*P. putida* lipid A has been structurally analyzed by LC–high-resolution MS/MS alongside *E. coli* and *P. taiwanensis*, with acyl chains assigned to specific backbone positions and some species reported as new ([Sándor et al. 2020](https://pubmed.ncbi.nlm.nih.gov/32673427/)). The *Pseudomonas* lipid A backbone is a bis-phosphorylated β-(1→6)-linked diglucosamine ([PMC8876380](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8876380/)) — i.e. it has the 1- and 4′-phosphate acceptors this enzyme family requires. Whether pEtN-modified species are present in KT2440, and under which growth conditions, is the key missing measurement.

## 5. Summary of the functional call

**Most probable function:** a Zn²⁺-dependent, inner-membrane-anchored **lipid A phosphoethanolamine transferase (EptA ortholog)** that transfers pEtN from phosphatidylethanolamine to a lipid A phosphate (most likely 4′, by analogy with *P. aeruginosa*) at the periplasmic face of the inner membrane, as part of regulated lipid A remodeling — plausibly under zinc/ColRS control in *P. putida*.

**Confidence:** family and domain assignment, membrane topology and active-site integrity are all strong and mutually consistent (converging PANTHER subfamily, NCBIfam, CDD and dual Pfam calls, plus intact Thr nucleophile and metal-binding motifs). Everything about *this* protein's activity, regiospecificity, regulation and phenotype is **untested** (PE 4, Predicted; no primary literature).

**Annotation recommendations:**
1. Replace the molecular-function placeholders (`GO:0016772`, `GO:0016776`) with a lipid A phosphoethanolamine transferase activity term, supported by the family/domain evidence (ISS/IEA-grade, not experimental).
2. The biological-process row `GO:0009244 lipopolysaccharide core region biosynthetic process` is likely mis-targeted: pEtN transferases modify lipid A, not the core region. A lipid A modification term is the appropriate replacement.
3. Keep `GO:0005886 plasma membrane`; it is the right compartment at the resolution available. A periplasmic-face qualifier is supported by topology but is an inference you would need to author.
4. Do not carry the submitted name "metal-dependent hydrolase" into a function annotation, and do not let the `cd16017 LptA` hit route the protein into LPS transport.

**Experiments that would settle it:** MALDI-TOF/LC-MS of lipid A from wild-type vs. a PP_0024 deletion, ± added Zn²⁺, looking for a +123 Da pEtN species and its position by MS/MS; in vitro assay of the purified periplasmic domain with PE and Kdo₂-lipid A; a Thr259Ala active-site mutant as the specificity control; and a test of ColR dependence using the published *P. putida colR* mutant background.

## Sources

- [Nowicki et al. 2015 — zinc/ColRS control of pEtN addition at the lipid A 4′ phosphate in *P. aeruginosa* (PMC4715879)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4715879)
- [Cervoni et al. 2021, *Front Microbiol* 12:778968 — EptA vs MCR-1 activity; overexpression toxicity maps to the C-terminal tail](https://www.frontiersin.org/articles/10.3389/fmicb.2021.778968/full)
- [Jeannot et al. 2023, *Antibiotics* — regulatory landscape of *P. aeruginosa eptA* and colistin resistance (PMC9952513)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9952513/)
- [Kivistik et al. 2009, *BMC Microbiol* — ColR binding consensus and ColRS regulon in *P. putida* (PagL, DgkA) (PMC2689224)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2689224/)
- [Kutschera et al. 2022, *IJMS* — lipid A remodeling in *P. syringae* pv. phaseolicola; pEtN at both phosphates (PMC8876380)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8876380/)
- [IUCrJ 2021 — EptA structural work: PEA transfer from phosphatidylethanolamine to lipid A 1 and 4′ positions](https://journals.iucr.org/m/issues/2021/05/00/jt5059/)
- [Sándor et al. 2020 — LC-HRMS/MS structural characterization of lipid A from *E. coli*, *P. putida*, *P. taiwanensis*](https://pubmed.ncbi.nlm.nih.gov/32673427/)
- [pseudomonas.com — *eptA* entries for PA14_39020 and PSPA7_3323, ortholog group POG003461](https://www.pseudomonas.com/feature/show?id=1669435)
- [Nelson et al. 2002 — KT2440 genome (PMID:12534463)](https://pubmed.ncbi.nlm.nih.gov/12534463/); [Belda et al. 2016 — revisited KT2440 genome (PMID:26913973)](https://pubmed.ncbi.nlm.nih.gov/26913973/)
- Local: `genes/PSEPK/PP_0024/PP_0024-uniprot.txt`, `PP_0024-goa.tsv` (motif positions computed from the record's sequence)

## Citations

1. https://journals.iucr.org/m/issues/2021/05/00/jt5059/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC4715879
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8876380/
4. https://pubmed.ncbi.nlm.nih.gov/12534463/
5. https://pubmed.ncbi.nlm.nih.gov/26913973/
6. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9952513/
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2689224/
8. https://www.frontiersin.org/articles/10.3389/fmicb.2021.778968/full
9. https://pubmed.ncbi.nlm.nih.gov/32673427/
10. https://www.pseudomonas.com/feature/show?id=1669435