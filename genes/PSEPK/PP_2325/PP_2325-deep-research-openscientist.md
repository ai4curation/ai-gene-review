---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:47:00.329868'
end_time: '2026-07-18T14:54:36.620233'
duration_seconds: 4056.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2325
  gene_symbol: PP_2325
  uniprot_accession: Q88KG5
  protein_description: 'RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465,
    ECO:0000256|RuleBase:RU362068}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014, ECO:0000256|RuleBase:RU362068};
    AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024, ECO:0000256|RuleBase:RU362068};'
  gene_info: OrderedLocusNames=PP_2325 {ECO:0000313|EMBL:AAN67938.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ketopantoate reductase family.
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328);
    ApbA. (IPR003710); KPA_reductase. (IPR013752); KPR-Related. (IPR051402)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: PP_2325-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2325-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KG5
- **Protein Description:** RecName: Full=2-dehydropantoate 2-reductase {ECO:0000256|ARBA:ARBA00019465, ECO:0000256|RuleBase:RU362068}; EC=1.1.1.169 {ECO:0000256|ARBA:ARBA00013014, ECO:0000256|RuleBase:RU362068}; AltName: Full=Ketopantoate reductase {ECO:0000256|ARBA:ARBA00032024, ECO:0000256|RuleBase:RU362068};
- **Gene Information:** OrderedLocusNames=PP_2325 {ECO:0000313|EMBL:AAN67938.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ketopantoate reductase family.
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); ApbA. (IPR003710); KPA_reductase. (IPR013752); KPR-Related. (IPR051402)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2325" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2325' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2325** (gene ID: PP_2325, UniProt: Q88KG5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2325 (Q88KG5) — Ketopantoate Reductase of *Pseudomonas putida* KT2440

## Summary

**PP_2325 (UniProt Q88KG5) of *Pseudomonas putida* KT2440 encodes ketopantoate reductase (KPR), also known as 2-dehydropantoate 2-reductase (PanE/ApbA; EC 1.1.1.169; KEGG orthology K00077).** This soluble, cytoplasmic oxidoreductase catalyzes the NADPH-dependent, stereospecific reduction of 2-dehydropantoate (ketopantoate) to (R)-pantoate. This reaction is the committed reductive step in the pantoate branch of pantothenate (vitamin B5) biosynthesis, which in turn feeds the biosynthesis of coenzyme A (CoA) and acyl carrier protein (ACP) — cofactors central to all fatty-acid, polyketide, and central-carbon metabolism. The substrate is specifically ketopantoate and the obligate hydride donor is NADPH.

The identity of PP_2325 as a ketopantoate reductase is strongly supported by convergent lines of evidence. UniProt and KEGG independently annotate the 315-residue protein as 2-dehydropantoate 2-reductase (EC 1.1.1.169, K00077), placing it in pathway ppu00770 (Pantothenate and CoA biosynthesis). The protein carries the diagnostic InterPro/Pfam signatures of the family — ApbA (PF02558; the N-terminal NAD(P)-binding Rossmann domain) and ApbA_C (PF08546; the C-terminal catalytic domain) — and directly retains the N-terminal Rossmann glycine-rich dinucleotide-binding motif (GSGAIG at residues 12–17). Function is transferred with high confidence from biochemically and structurally characterized bacterial orthologs (chiefly *Escherichia coli* PanE), for which the reaction, cofactor specificity, kinetic mechanism, stereochemistry, and catalytic residues have all been experimentally established.

Because the ketopantoate reductase family is intrinsically divergent at the sequence level (~20–29% pairwise identity between validated homologs), residue-level catalytic conservation in PP_2325 is best inferred through profile-HMM/InterPro methods rather than naive pairwise alignment. PP_2325 shows ~27% identity to *E. coli* PanE, which is entirely within the normal range for this family. The pantothenate pathway is otherwise complete in *P. putida* (panBC at PP_4699/PP_4700), and an IlvC ortholog (PP_4678) plus two additional KPR-family paralogs (PP_1351, PP_2998) may provide partial functional redundancy. Among these, PP_2325 is the canonically curated PanE/ApbA ketopantoate reductase.

---

## Key Findings

### Finding 1 — PP_2325 is ketopantoate reductase (EC 1.1.1.169), catalyzing the NADPH-dependent reduction of 2-dehydropantoate to (R)-pantoate

UniProt Q88KG5 annotates PP_2325 as 2-dehydropantoate 2-reductase (EC 1.1.1.169) with the catalytic activity:

> **(R)-pantoate + NADP⁺ ⇌ 2-dehydropantoate + NADPH + H⁺**

The 315-amino-acid protein belongs to the ketopantoate reductase (ApbA/PanE) family, carrying InterPro signatures IPR003710 (ApbA) and IPR013752 (KPA_reductase). Direct sequence inspection confirms an N-terminal Rossmann-fold dinucleotide-binding glycine-rich motif (GSGAIG at residues 12–17), which matches the canonical G-x-G-x-x-[GA] fingerprint for NADP(H) binding.

This assignment is anchored in primary biochemical literature on the enzyme family. As stated in the structural characterization of *E. coli* KPR, *"The NADPH-dependent reduction of ketopantoate to pantoate, catalyzed by ketopantoate reductase (KPR; EC 1.1.1.169), is essential for the biosynthesis of pantothenate (vitamin B5)"* [PMID: 15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/). This is independently reaffirmed in the ternary-complex study: *"Ketopantoate reductase (KPR, EC 1.1.1.169) catalyzes the NADPH-dependent reduction of ketopantoate to pantoate, an essential step for the biosynthesis of pantothenate (vitamin B5)"* [PMID: 17229734](https://pubmed.ncbi.nlm.nih.gov/17229734/). Both establish the reaction, the cofactor (NADPH), the EC number, and the pathway role that match the UniProt annotation of PP_2325.

### Finding 2 — KPR is a two-domain Rossmann-fold enzyme using conserved Lys, Asn, and Glu residues with a substrate-induced conformational change

Crystallographic and kinetic work on *E. coli* KPR — a monomeric homolog — reveals a two-domain architecture: NADP(H) is bound in a cleft between an N-terminal Rossmann-fold domain and a C-terminal α-helical domain. As reported, *"The cofactor is bound in the active site cleft between the N-terminal Rossmann-fold domain and the C-terminal alpha-helical domain"* [PMID: 15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/).

Site-directed mutagenesis coupled with steady-state kinetics has dissected the catalytic machinery: *"The steady-state kinetics of active site mutants R31A, K72A, N98A, K176A, S244A, and E256A implicate Asn98 as well as Lys176 and Glu256 in the catalytic mechanism"* [PMID: 17229734](https://pubmed.ncbi.nlm.nih.gov/17229734/). In this scheme, Asn98, Lys176, and Glu256 form the catalytic core; Arg31 and Lys72 bind the cofactor; and Ser244 contacts the substrate. Catalysis involves a hinge-bending domain closure that repositions the essential Lys176 to hydrogen-bond the C2 hydroxyl of the pantoate product. PP_2325 conserves the corresponding N-terminal Rossmann motif (GSGAIG) and is assigned to the same family, so it is expected to employ the same two-domain catalytic strategy.

### Finding 3 — KPR is a monomeric ~34 kDa enzyme with an ordered sequential mechanism and stereospecific pro-S hydride transfer to C2

Detailed kinetic and NMR analysis of the *E. coli* panE-encoded enzyme established the reaction mechanism. The enzyme is a monomeric ~34 kDa protein with KM(NADPH) ≈ 20 µM, KM(ketopantoate) ≈ 60 µM, and kcat ≈ 40 s⁻¹. Steady-state and product-inhibition patterns fit an ordered sequential mechanism: *"The steady-state initial velocity and product inhibition patterns are consistent with an ordered sequential kinetic mechanism in which NADPH binding is followed by ketopantoate binding, and pantoate release precedes NADP(+) release"* [PMID: 10736170](https://pubmed.ncbi.nlm.nih.gov/10736170/).

The chemistry is stereospecific: *"The stereospecific transfer of the pro-S hydrogen atom of NADPH to the C-2 position of ketopantoate was demonstrated by (1)H NMR spectroscopy"* [PMID: 10736170](https://pubmed.ncbi.nlm.nih.gov/10736170/), which yields D-(–)-(R)-pantoate. A single general acid/base (pK ≈ 7.8–8.4) operates during turnover, and hydride transfer is not fully rate-limiting. The monomeric two-domain fold is corroborated by the 1.7 Å crystal structure: *"The enzyme is monomeric and has two domains separated by a cleft. The N-terminal domain has an alphabeta-fold of the Rossmann type"* [PMID: 11724562](https://pubmed.ncbi.nlm.nih.gov/11724562/). PP_2325 (315 aa, ~34 kDa) is the *P. putida* ortholog of this enzyme and is expected to share these properties.

### Finding 4 — PP_2325 performs the final step of the pantoate branch of pantothenate/CoA biosynthesis in the cytoplasm; it belongs to the 6-PGDH C-terminal-domain-like superfamily

The bacterial pantothenate biosynthetic pathway comprises four enzymes. As summarized: *"the pantothenate biosynthetic pathway is well-established in bacteria, comprising four enzymic reactions catalysed by ketopantoate hydroxymethyltransferase (KPHMT), L-aspartate-alpha-decarboxylase (ADC), pantothenate synthetase (PS) and ketopantoate reductase (KPR) encoded by panB, panD, panC and panE genes, respectively"* [PMID: 18726075](https://pubmed.ncbi.nlm.nih.gov/18726075/).

UniProt places PP_2325 at *"(R)-pantothenate biosynthesis; (R)-pantoate from 3-methyl-2-oxobutanoate: step 2/2"*. In sequence, PanB (KPHMT) converts 3-methyl-2-oxobutanoate (ketoisovalerate) into ketopantoate; KPR (PP_2325) then reduces ketopantoate to (R)-pantoate; PanC (pantothenate synthetase) condenses (R)-pantoate with β-alanine to form pantothenate, the direct precursor of CoA and ACP.

Structurally, KPR belongs to a larger superfamily: *"KPR is shown to be a member of the 6-phosphogluconate dehydrogenase C-terminal domain-like superfamily"* [PMID: 11724562](https://pubmed.ncbi.nlm.nih.gov/11724562/), which matches PP_2325's InterPro assignments IPR008927 and IPR013328. The gene has a documented dual identity: in *Salmonella*, *"apbA and panE are allelic and map to 10 min on both the S. typhimurium and E. coli chromosomes"* [PMID: 9721324](https://pubmed.ncbi.nlm.nih.gov/9721324/), confirming that the ApbA and PanE names denote the same ketopantoate reductase gene product. In *E. coli*, a second, moonlighting KPR activity is provided by ilvC (ketol-acid reductoisomerase).

### Finding 5 — PP_2325 is a divergent but bona fide KPR ortholog; pantothenate biosynthesis is conditionally essential in *P. putida* KT2440 on minimal medium

Global pairwise alignment (BLOSUM62) of PP_2325 (315 aa) against the experimentally characterized *E. coli* PanE (303 aa) yields 27.0% identity over 293 aligned positions. This is squarely within the documented low-similarity range for the KPR family. As directly stated: *"The sequence similarity among putative KPRs is limited and KPR itself belongs to a large superfamily of 6-phosphogluconate dehydrogenases"* [PMID: 20876192](https://pubmed.ncbi.nlm.nih.gov/20876192/). Despite this divergence, PP_2325 retains the diagnostic N-terminal Rossmann NADP-binding motif and the KPR-specific InterPro signatures (ApbA IPR003710, KPA_reductase IPR013752).

Physiologically, a genome-wide mini-Tn5 mutant screen of *P. putida* KT2440 on glucose minimal medium recovered vitamin/amino-acid biosynthesis auxotrophs: *"Among the set of identified conditionally essential genes were a number of genes involved in the biosynthesis of certain amino acids and vitamins"* [PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/). Because de novo pantothenate/CoA production requires KPR activity, the enzyme is expected to be required for growth unless pantothenate is supplied. As in *E. coli*, a secondary KPR activity from ketol-acid reductoisomerase (IlvC) may partly mask the phenotype of a single panE knockout.

### Finding 6 — Per-residue catalytic-site conservation cannot be verified by naive pairwise alignment; HMM/InterPro annotation is the appropriate method for this divergent family

Attempts to map the experimentally defined *E. coli* PanE catalytic/binding residues (Arg31, Lys72, Asn98, Lys176, Ser244, Glu256, plus substrate-contacting Asn180/194/241) directly onto PP_2325 by hand-rolled global alignment were inconclusive. A linear-gap Needleman–Wunsch alignment gave 27% identity, whereas an affine-gap (Gotoh) alignment gave only 19% identity with the catalytic columns clearly misregistered (e.g., *E. coli* K72 aligning to a non-equivalent PP position 37). This instability reflects the intrinsically low sequence similarity of the family rather than the absence of the catalytic residues — the same limitation noted in the family: *"The sequence similarity among putative KPRs is limited and KPR itself belongs to a large superfamily of 6-phosphogluconate dehydrogenases"* [PMID: 20876192](https://pubmed.ncbi.nlm.nih.gov/20876192/).

Reliable residue-level equivalence therefore requires profile-HMM or structure-based alignment. PP_2325 is positively assigned KPR-specific InterPro/Pfam signatures (ApbA IPR003710, KPA_reductase IPR013752) that are built from curated multiple alignments encoding the conserved catalytic positions, and it directly retains the N-terminal Rossmann NADP-binding motif (GSGAIG, residues 12–17) confirmed by sequence inspection. This finding is methodologically important: it explains why the annotation rests on HMM/domain evidence rather than a simple pairwise residue match.

### Finding 7 — KEGG independently assigns PP_2325 to K00077 (EC 1.1.1.169); Pfam ApbA + ApbA_C confirm both functional domains; the gene is not in a pan operon

KEGG (entry `ppu:PP_2325`) independently annotates the gene as 2-dehydropantoate 2-reductase, KEGG Orthology K00077, EC 1.1.1.169, mapped to pathways ppu00770 (Pantothenate and CoA biosynthesis) and ppu01240 (Biosynthesis of cofactors), and classified as an oxidoreductase acting on CH-OH groups with NAD(P)⁺ as acceptor. KEGG lists Pfam motifs ApbA (PF02558; N-terminal NAD(P)-binding/Rossmann domain) and ApbA_C (PF08546; C-terminal catalytic domain), directly confirming that PP_2325 possesses both the cofactor-binding and the catalytic domains characteristic of KPR.

The gene occupies genome coordinates 2,652,614–2,653,561 (948 bp, forward strand). Genomic-neighborhood analysis shows that PP_2325 is **not** part of a pantothenate operon: the upstream gene PP_2324 (K01626, DAHP synthase, aromatic amino-acid biosynthesis) is divergently transcribed on the opposite strand, and the downstream same-strand gene PP_2326 is an unrelated universal stress protein. The panB/panC/panD genes are located elsewhere in the genome. This gene arrangement is consistent with independent transcriptional regulation of ketopantoate reductase rather than co-regulation within a biosynthetic gene cluster.

### Finding 8 — *P. putida* encodes a complete pantothenate pathway with a panBC cluster, an IlvC backup, and three KPR-family paralogs; PP_2325 is the canonical curated PanE/ApbA

KEGG KO-to-gene mapping for *P. putida* KT2440 (ppu) resolves the pathway components: panB = K00606 → PP_4699 and panC = K01918 → PP_4700 (adjacent loci forming a panBC cluster, located far from PP_2325); ilvC = K00053 → PP_4678 (present, providing the documented secondary/moonlighting ketopantoate reductase activity). Notably, three genes are assigned to K00077 (2-dehydropantoate 2-reductase): **PP_1351, PP_2325, and PP_2998** — indicating multiple KPR-family paralogs in this genome, consistent with the "KPR-Related" InterPro superfamily IPR051402. PP_2325 is the paralog carrying the canonical ApbA/PanE UniProt curation (Q88KG5) and both ApbA + ApbA_C Pfam domains.

KEGG returned no gene under panD (K01579, aspartate 1-decarboxylase), suggesting that the β-alanine supply for pantothenate in *P. putida* may proceed via an alternative or divergent route. The existence of an IlvC ortholog plus two additional K00077 paralogs implies that a single PP_2325 knockout might be phenotypically buffered, mirroring the *E. coli* situation where an ilvC panE double mutant is required to fully abolish KPR activity.

---

## Mechanistic Model and Interpretation

### The reaction and its place in metabolism

PP_2325 catalyzes the second (committed, reductive) step of the pantoate branch of pantothenate biosynthesis:

```
   3-methyl-2-oxobutanoate (ketoisovalerate)
              │
              │   PanB (KPHMT, PP_4699)  + 5,10-CH2-THF
              ▼
        2-dehydropantoate  (ketopantoate)
              │
              │   ★ PP_2325 (KPR / PanE / ApbA, Q88KG5)  + NADPH → NADP+
              │      pro-S hydride to C2, ordered sequential mechanism
              ▼
          (R)-pantoate
              │
              │   PanC (pantothenate synthetase, PP_4700)  + β-alanine + ATP
              ▼
          (R)-pantothenate  (vitamin B5)
              │
              │   PanK → ... → Coenzyme A  &  Acyl Carrier Protein (ACP)
              ▼
     central & lipid metabolism (fatty acids, TCA, PHA synthesis, etc.)
```

The enzyme is the sole dedicated reductase of this branch and produces the chiral (R)-pantoate needed downstream. Because CoA and ACP are indispensable for fatty-acid metabolism, the TCA cycle, and — importantly for *P. putida* — medium-chain-length polyhydroxyalkanoate (PHA) synthesis and diverse aromatic/terpenoid catabolism, KPR sits upstream of a large fraction of the organism's carbon flux.

### Enzyme architecture and catalytic cycle

The structural and kinetic model, transferred from characterized bacterial orthologs, is:

| Feature | Property (from *E. coli* PanE) | Basis for transfer to PP_2325 |
|---|---|---|
| Oligomeric state | Monomer, ~34 kDa | PP_2325 = 315 aa, ~34 kDa |
| Fold | Two domains: N-terminal Rossmann + C-terminal α-helical | ApbA (PF02558) + ApbA_C (PF08546) present |
| Cofactor | NADPH (binds first) | GSGAIG Rossmann motif, res 12–17 |
| Substrate | Ketopantoate (binds second) | Family / KO assignment K00077 |
| Kinetic mechanism | Ordered sequential; pantoate released before NADP⁺ | Family-conserved |
| Chemistry | Stereospecific pro-S hydride transfer to C2 → (R)-pantoate | Family-conserved |
| Catalytic residues | Asn98, Lys176, Glu256 (catalysis); Arg31, Lys72 (cofactor); Ser244 (substrate) | Encoded in InterPro HMM; not verifiable by naive alignment |
| Conformational change | Hinge-bending domain closure repositions Lys176 | Family-conserved |

An important nuance emerges from comparative studies: while *E. coli* KPR is monomeric and follows a strictly ordered mechanism, the *Staphylococcus aureus* enzyme is a stable dimer showing kinetic cooperativity for NADPH (Hill coefficient ~2.5) that arises from a random-addition mechanism kinetically biased toward NADPH-first binding [PMID: 25946571](https://pubmed.ncbi.nlm.nih.gov/25946571/). The oligomeric state and exact kinetic behavior of PP_2325 therefore cannot be assumed a priori and would require direct biochemical study.

### Localization

Ketopantoate reductase is a soluble cytoplasmic enzyme. It has no signal peptide, no transmembrane segments, and its substrates/products (ketopantoate, pantoate, NADPH/NADP⁺) are cytosolic metabolites. Its role is carried out entirely within the cytoplasm, where it participates in soluble intermediary metabolism.

### Redundancy and regulation

The *P. putida* genome presents a more complex picture than a single dedicated KPR. Three genes map to K00077 (PP_1351, PP_2325, PP_2998), and an IlvC ortholog (PP_4678) can supply moonlighting KPR activity — a phenomenon experimentally demonstrated in other systems, where *"functional replacement of a pantothenate biosynthesis enzyme, 2-dehydropantoate 2-reductase (E.C. 1.1.1.169), by an endosymbiont gene, ilvC, encoding a substrate ambiguous enzyme"* was shown [PMID: 25527092](https://pubmed.ncbi.nlm.nih.gov/25527092/). PP_2325 is nonetheless the canonically curated PanE/ApbA reductase, distinguished by its UniProt curation and complete ApbA + ApbA_C domain complement. Its non-operonic genomic context (isolated from panBC/panD) implies independent regulation.

In archaea, KPR is a feedback regulatory node for CoA biosynthesis (CoA competitively inhibits at the NAD(P)H site) [PMID: 23941541](https://pubmed.ncbi.nlm.nih.gov/23941541/); [PMID: 26757028](https://pubmed.ncbi.nlm.nih.gov/26757028/). Whether the *P. putida* enzyme is similarly feedback-regulated is unknown, as bacterial CoA feedback regulation classically targets pantothenate kinase rather than KPR.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [15966718](https://pubmed.ncbi.nlm.nih.gov/15966718/) | *Crystal structure of E. coli KPR with NADP+ bound* | Establishes reaction, NADPH cofactor, EC 1.1.1.169, pathway role, and two-domain cofactor binding |
| [17229734](https://pubmed.ncbi.nlm.nih.gov/17229734/) | *E. coli KPR ternary complex with NADP+ and pantoate* | Identifies catalytic residues (Asn98, Lys176, Glu256), substrate recognition, conformational change |
| [10736170](https://pubmed.ncbi.nlm.nih.gov/10736170/) | *Kinetic/mechanistic analysis of E. coli panE KPR* | Ordered sequential mechanism; stereospecific pro-S hydride transfer to C2 |
| [11724562](https://pubmed.ncbi.nlm.nih.gov/11724562/) | *E. coli KPR crystal structure at 1.7 Å* | Monomeric two-domain Rossmann architecture; 6-PGDH C-terminal superfamily assignment |
| [18726075](https://pubmed.ncbi.nlm.nih.gov/18726075/) | *Engineering pantothenate levels in plants* | Defines the four-enzyme bacterial pathway (panB/panD/panC/panE) placing KPR as the reductase |
| [9721324](https://pubmed.ncbi.nlm.nih.gov/9721324/) | *panE maps at 10 min, allelic to apbA in S. typhimurium* | Establishes ApbA = PanE identity |
| [9488683](https://pubmed.ncbi.nlm.nih.gov/9488683/) | *ApbA of S. typhimurium required for thiamine via APB pathway* | Confirms ApbA is ketopantoate reductase; monomer, NADPH-preferring |
| [20876192](https://pubmed.ncbi.nlm.nih.gov/20876192/) | *Detecting subtle functional differences in KPR* | Documents limited KPR sequence similarity; justifies HMM-based annotation |
| [20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | *Conditionally essential genes of P. putida KT2440* | Organism-specific evidence that vitamin biosynthesis genes are conditionally essential on minimal medium |
| [25946571](https://pubmed.ncbi.nlm.nih.gov/25946571/) | *Kinetic cooperativity in dimeric S. aureus KPR* | Shows oligomeric state/kinetics vary across KPR family — cautions against over-transfer |
| [25527092](https://pubmed.ncbi.nlm.nih.gov/25527092/) | *Substrate-ambiguous enzyme in symbiont genome reduction* | Demonstrates IlvC can functionally replace KPR (EC 1.1.1.169), supporting redundancy model |
| [23941541](https://pubmed.ncbi.nlm.nih.gov/23941541/) | *Archaeal KPR and CoA biosynthesis regulation* | KPR as a feedback regulatory node in archaea; NADH-preferring variant exists |
| [26757028](https://pubmed.ncbi.nlm.nih.gov/26757028/) | *Archaeal KPR complexed with CoA and 2-oxopantoate* | Structural basis for CoA feedback inhibition at the NAD(P)H site |
| [23243306](https://pubmed.ncbi.nlm.nih.gov/23243306/) | *PanG, a new ketopantoate reductase* | Shows multiple non-orthologous KPRs exist; convertibility of KPRs to pantoate |
| [10553653](https://pubmed.ncbi.nlm.nih.gov/10553653/) | *Pantothenate production via panE overexpression* | panE encodes 303-aa, 33.8 kDa KPR; overexpression boosts pantothenate excretion |

The **consistency across UniProt, KEGG, InterPro/Pfam, and the primary structural/kinetic literature** is the strongest aspect of this annotation: four independent annotation systems and multiple experimentally characterized orthologs converge on the same assignment. The primary **challenge** is the absence of direct experimental characterization of the *P. putida* PP_2325 protein itself — all mechanistic detail is transferred from orthologs — combined with the family's low sequence identity and evidence that oligomeric state/kinetics vary between homologs.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of PP_2325.** There is no published enzymology, crystal structure, or knockout phenotype for the *P. putida* KT2440 protein specifically. All mechanistic claims (kinetics, stereochemistry, catalytic residues, oligomeric state) are inferred from orthologs, principally *E. coli* PanE.

2. **Low sequence identity limits residue-level inference.** At ~27% identity to *E. coli* PanE, naive pairwise alignment cannot register the catalytic residues reliably (Finding 6). Residue equivalence rests on profile-HMM assignment. A structure-based alignment (e.g., against an AlphaFold model) was not performed and would strengthen residue-level claims.

3. **Family-level variability in mechanism.** KPRs range from monomeric/ordered (*E. coli*) to dimeric/cooperative (*S. aureus*), and some prefer NADH over NADPH (archaeal Tk-KPR). The oligomeric state, cofactor preference, and kinetic mechanism of PP_2325 are therefore not settled by homology alone.

4. **Genetic redundancy complicates loss-of-function interpretation.** With three K00077 paralogs (PP_1351, PP_2325, PP_2998) plus a potentially moonlighting IlvC (PP_4678), a single PP_2325 deletion may not produce a pantothenate auxotrophy, obscuring in vivo confirmation of its role.

5. **Missing/divergent panD.** No canonical aspartate 1-decarboxylase (K01579) was mapped, leaving the β-alanine supply route for pantothenate synthesis in *P. putida* unresolved. This is a pathway-level gap, not specific to PP_2325.

6. **Regulation unknown.** Whether PP_2325 is feedback-inhibited by CoA (as in archaea) or transcriptionally regulated (its non-operonic context suggests independent control) has not been investigated.

---

## Proposed Follow-up Experiments and Actions

1. **Recombinant expression and enzyme assay.** Clone PP_2325, purify the protein, and measure NADPH-dependent reduction of chemically synthesized ketopantoate spectrophotometrically (NADPH oxidation at 340 nm). Determine KM(NADPH), KM(ketopantoate), and kcat, and test NADH vs NADPH preference to place PP_2325 relative to bacterial vs archaeal KPR types.

2. **Determine oligomeric state.** Use size-exclusion chromatography and/or analytical ultracentrifugation to distinguish a monomeric (*E. coli*-like) from a dimeric (*S. aureus*-like) assembly, and test for kinetic cooperativity via NADPH saturation curves (Hill coefficient).

3. **Structural validation.** Generate an AlphaFold model of Q88KG5 and perform a structure-based superposition against *E. coli* KPR (structures from PMID 11724562 / 17229734) to confirm spatial conservation of the Asn98/Lys176/Glu256-equivalent residues; ideally solve an experimental structure with NADP⁺ and pantoate bound.

4. **Genetic dissection of redundancy.** Construct single (ΔPP_2325) and combinatorial (ΔPP_2325 ΔPP_1351 ΔPP_2998 ΔilvC) deletion mutants and score for pantothenate auxotrophy on minimal medium ± pantothenate/pantoate to establish which paralog(s) carry the physiological KPR activity in vivo.

5. **Complementation test.** Confirm functional identity by complementing an *E. coli* ilvC panE double mutant (which lacks all KPR activity) with PP_2325, as was done successfully for panG and EF1861 [PMID: 23243306](https://pubmed.ncbi.nlm.nih.gov/23243306/).

6. **Feedback-regulation test.** Assay PP_2325 activity in the presence of CoA to determine whether this bacterial enzyme, like its archaeal counterparts, is subject to CoA feedback inhibition at the nucleotide-binding site.

7. **Resolve the β-alanine route.** Search the *P. putida* genome/transcriptome for a divergent aspartate decarboxylase or an alternative β-alanine source (e.g., from spermine/uracil degradation) to complete the pathway annotation.

---

## Conclusion

PP_2325 (Q88KG5) is the ketopantoate reductase (2-dehydropantoate 2-reductase; PanE/ApbA; EC 1.1.1.169; K00077) of *Pseudomonas putida* KT2440 — a soluble cytoplasmic, NADPH-dependent oxidoreductase that stereospecifically reduces ketopantoate to (R)-pantoate in the committed reductive step of pantothenate (vitamin B5) biosynthesis, upstream of coenzyme A and acyl carrier protein. This assignment is supported by convergent UniProt, KEGG, and InterPro/Pfam annotations, by the diagnostic Rossmann NADP-binding motif and dual ApbA/ApbA_C domains, and by extensive biochemical and structural characterization of bacterial orthologs, with the caveats that the family is highly divergent, that *P. putida* harbors partially redundant KPR-family paralogs and a moonlighting IlvC, and that no direct experimental characterization of the PP_2325 protein itself yet exists.


## Artifacts

- [OpenScientist final report](PP_2325-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2325-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15966718
2. PMID:17229734
3. PMID:10736170
4. PMID:11724562
5. PMID:18726075
6. PMID:9721324
7. PMID:20876192
8. PMID:20158506
9. PMID:25946571
10. PMID:25527092
11. PMID:23941541
12. PMID:26757028
13. PMID:23243306