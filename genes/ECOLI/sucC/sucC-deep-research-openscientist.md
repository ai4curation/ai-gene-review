---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T09:51:58.746038'
end_time: '2026-11-11T10:04:43.374080'
duration_seconds: 764.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: sucC
  gene_symbol: sucC
  uniprot_accession: P0A836
  protein_description: 'RecName: Full=Succinate--CoA ligase [ADP-forming] subunit
    beta {ECO:0000255|HAMAP-Rule:MF_00558}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_00558,
    ECO:0000269|PubMed:10353839, ECO:0000269|PubMed:7040388}; AltName: Full=Succinyl-CoA
    synthetase subunit beta {ECO:0000255|HAMAP-Rule:MF_00558}; Short=SCS-beta {ECO:0000255|HAMAP-Rule:MF_00558};'
  gene_info: Name=sucC {ECO:0000255|HAMAP-Rule:MF_00558}; OrderedLocusNames=b0728,
    JW0717;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the succinate/malate CoA ligase beta subunit
  protein_domains: ATP-grasp. (IPR011761); ATP-grasp_succ-CoA_synth-type. (IPR013650);
    ATP_grasp_subdomain_1. (IPR013815); Succ-CoA_synthase_bsu_CS. (IPR017866); SUCC_ACL_C.
    (IPR005811)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sucC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sucC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P0A836
- **Protein Description:** RecName: Full=Succinate--CoA ligase [ADP-forming] subunit beta {ECO:0000255|HAMAP-Rule:MF_00558}; EC=6.2.1.5 {ECO:0000255|HAMAP-Rule:MF_00558, ECO:0000269|PubMed:10353839, ECO:0000269|PubMed:7040388}; AltName: Full=Succinyl-CoA synthetase subunit beta {ECO:0000255|HAMAP-Rule:MF_00558}; Short=SCS-beta {ECO:0000255|HAMAP-Rule:MF_00558};
- **Gene Information:** Name=sucC {ECO:0000255|HAMAP-Rule:MF_00558}; OrderedLocusNames=b0728, JW0717;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the succinate/malate CoA ligase beta subunit
- **Key Domains:** ATP-grasp. (IPR011761); ATP-grasp_succ-CoA_synth-type. (IPR013650); ATP_grasp_subdomain_1. (IPR013815); Succ-CoA_synthase_bsu_CS. (IPR017866); SUCC_ACL_C. (IPR005811)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sucC" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sucC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sucC** (gene ID: sucC, UniProt: P0A836) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *sucC* (P0A836) — Succinyl-CoA Synthetase β-Subunit in *Escherichia coli* K-12

## Gene/Protein Identity — Verified

The gene symbol ***sucC*** unambiguously matches the target protein. UniProt **P0A836** is the **β-subunit of succinyl-CoA synthetase (SCS; succinate–CoA ligase [ADP-forming]), EC 6.2.1.5**, in *Escherichia coli* K-12 (ordered locus **b0728 / JW0717**; 388 aa, ~41.4 kDa). The literature retrieved is specifically about *E. coli* SCS and its β-subunit, and the InterPro/Pfam domain architecture (ATP-grasp + CoA-ligase) matches the UniProt annotation exactly. There is **no ambiguity**: this is one of the best-characterized enzymes in bacterial central metabolism, with multiple *E. coli* crystal structures and extensive mutagenesis. All claims below are supported by primary literature and/or cross-validated database annotation.

---

## Summary

The gene **sucC** of *Escherichia coli* K-12 encodes the **β-subunit of succinyl-CoA synthetase (SCS)**, also called succinate–CoA ligase [ADP-forming] (UniProt P0A836, EC 6.2.1.5). SCS catalyzes the **only substrate-level phosphorylation of the tricarboxylic acid (TCA) cycle**: the reversible, Mg²⁺-dependent reaction succinyl-CoA + Pᵢ + NDP ⇌ succinate + CoA + NTP, where N is adenosine (preferred in *E. coli*) or guanosine. In the oxidative direction this conserves the energy of the succinyl-CoA thioester bond as a nucleoside triphosphate (ATP in *E. coli*); in the reverse direction it regenerates succinyl-CoA for biosynthesis.

The functional enzyme is an **α₂β₂ heterotetramer** assembled from the *sucC*-encoded β-subunit and the *sucD*-encoded α-subunit. Catalysis proceeds through a **phosphohistidine intermediate** (His246α) that physically swings ~29–35 Å between two spatially separated active sites, coupled to strict **half-sites reactivity** (alternating-site cooperativity). The β-subunit (sucC) is the **substrate-specificity engine** of the enzyme: its N-terminal **ATP-grasp fold** binds the nucleotide and Mg²⁺ (and a single residue, Pro20β, sets the ADP-vs-GDP preference), while its C-terminal domain binds the dicarboxylate substrate succinate with strict selectivity over the other C4 acids of the cycle.

Physiologically, SCS is a soluble **cytoplasmic** enzyme (experimentally confirmed cytosolic localization, GO:0005829, IDA) sitting at a central metabolic branch point. It is encoded in the sdhCDAB-sucABCD operon downstream of 2-oxoglutarate dehydrogenase. In the oxidative TCA cycle it generates ATP; running in reverse, it supplies succinyl-CoA — the acyl donor for essential biosynthetic pathways including methionine biosynthesis (homoserine O-succinyltransferase) and heme/tetrapyrrole biosynthesis (5-aminolevulinate synthase). This anabolic role is particularly important during anaerobic growth, when the oxidative route from 2-oxoglutarate is repressed.

---

## Key Findings

### Primary function: the TCA cycle's unique substrate-level phosphorylation enzyme

The *sucC* gene product is one of two subunits of succinyl-CoA synthetase, the enzyme that carries out the **sole substrate-level phosphorylation reaction of the citric acid cycle**. SCS catalyzes a reversible reaction: succinyl-CoA + Pᵢ + NDP ⇌ succinate + CoA + NTP, where N denotes adenosine or guanosine. The reaction conserves the energy stored in the thioester bond of succinyl-CoA (produced by the preceding 2-oxoglutarate dehydrogenase step) by forming a nucleoside triphosphate, and it does so via a transiently phosphorylated histidine residue. The *E. coli* enzyme is structurally and kinetically well characterized, with X-ray structures to 2.3 Å resolution.

The uniqueness and reversibility of this reaction are explicitly documented: *"Succinyl-CoA synthetase (SCS) carries out the substrate-level phosphorylation of GDP or ADP in the citric acid cycle"* ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)), and *"Succinyl-CoA synthetase (SCS) catalyzes a reversible reaction that is the only substrate-level phosphorylation in the citric acid cycle"* ([PMID: 33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/)). This is the defining biochemical function of the gene product and the reason it is classified as EC 6.2.1.5 (a CoA ligase forming ADP).

### Quaternary structure: an α₂β₂ heterotetramer with shared active sites

The functional enzyme in *E. coli* is a non-dissociating **α₂β₂ heterotetramer**, assembled from the *sucD*-encoded α-subunit and the *sucC*-encoded β-subunit. *"The enzyme, as isolated from Escherichia coli, has an alpha 2 beta 2 subunit structure"* and *"the active enzyme is the nondissociating tetramer"* ([PMID: 3304349](https://pubmed.ncbi.nlm.nih.gov/3304349/)). Crystallography independently confirms this: *"E. coli SCS is an (alphabeta)2-tetramer; there are two copies of each subunit in the asymmetric unit of the crystals"* ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). Renaturation experiments show fully active enzyme can be reconstituted from separately denatured α and β subunits, with a bimolecular rate-determining assembly step, confirming that neither subunit is catalytically competent alone and that the two form an obligate partnership. Each αβ dimer contributes one active site, where the catalytic phosphohistidine and the CoA thiol are located.

### The β-subunit houses the nucleotide-binding site in an ATP-grasp fold

A central, specific role of the *sucC* product is to bind the nucleotide substrate. X-ray diffraction of phosphorylated *E. coli* SCS soaked with ADP/Mg²⁺ *"revealed an ADP-Mg(2+) complex bound in the ATP-grasp fold of the N-terminal domain of each beta-subunit"* ([PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)). This was corroborated biochemically by photoaffinity labeling: *"Two tryptic peptides from the N-terminal domain of the beta-subunit were labeled with 8-N3-ATP"* ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)), with the labeled peptides (residues 107–119β and 121–146β) lying along one side of the ATP-grasp fold. The G53βV/R54βE mutant could not be phosphorylated by ATP or GTP but could still be phosphorylated by succinyl-CoA + Pᵢ, definitively localizing the nucleotide active-site chemistry to the β-subunit N-terminal domain.

### Catalysis via a swinging phosphohistidine intermediate

The reaction mechanism requires a **phosphohistidine intermediate** and large-scale conformational movement. A histidine of the α-subunit (His246α in *E. coli*) is transiently phosphorylated, and the phosphoryl group sits at the N-termini of two "power helices," one contributed by the α-subunit C-terminal domain and one by the β-subunit C-terminal domain. Because the nucleotide binds in the β N-terminal domain while the phosphate on the histidine is generated near the succinate/CoA site, *"the catalytic histidine residue would have to move about 35 A to react with the nucleotide"* ([PMID: 9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/)). Structures that captured the phosphohistidine loop in two distinct conformations confirmed the swinging-loop model: *"The phosphoryl transfer bridges a distance of 29 Å between the binding sites for phosphohistidine in site I and site II"* ([PMID: 33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/)). Two glutamate residues — one from each subunit — are required to stabilize the histidine during phosphoryl transfer at the two sites; critically for *sucC*, *"Glu 197 beta, a residue in the nucleotide-binding domain, would provide similar stabilization of the histidine residue during the actual phosphorylation/dephosphorylation by nucleotide at site II"* ([PMID: 11781092](https://pubmed.ncbi.nlm.nih.gov/11781092/)). Thus the β-subunit contributes directly to the chemistry at the nucleotide site, not merely to binding.

### Nucleotide specificity is set by a single β-subunit residue

Unlike the GTP-preferring SCS isoforms of pig heart and *Thermus aquaticus*, *"Escherichia coli SCS … uses GDP/GTP but prefers ADP/ATP"* ([PMID: 22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/)). This preference is governed by residue 20 of the β-subunit: a *"mutant protein designed to probe nucleotide specificity (P20betaQ) had a Km(app) for GTP that was more than 5 times lower than that of wild-type SCS"* ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)), with no change to other substrate parameters. The Pro→Gln substitution shifts the enzyme toward GTP usage, pinpointing Pro20β as the molecular determinant of purine-nucleotide selectivity. This is a clear example of the β-subunit (sucC) directly encoding substrate specificity.

### The β-subunit C-terminal domain binds succinate with strict specificity

The second substrate-binding role of the β-subunit lies in its C-terminal domain, which binds the dicarboxylate substrate succinate (and participates in CoA binding). Mutations disrupting a loop of the Rossmann-type fold in this domain — I322βA and R324βN/D326βA — *"had the greatest effect on the binding of succinate and CoA"* without disrupting nucleotide phosphorylation ([PMID: 10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/)). A dedicated structural study confirmed that *"Succinate binds in the carboxy-terminal domain of the β-subunit"* and explained the enzyme's selectivity: *"The structure shows why succinyl-CoA synthetase is specific for succinate and does not react appreciably with citrate nor with the other C4-dicarboxylic acids of the citric acid cycle, fumarate and oxaloacetate, but shows some activity with L-malate"* ([PMID: 27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/)). This strict substrate specificity ensures SCS operates cleanly on succinate/succinyl-CoA within the dense pool of TCA intermediates.

### Half-sites reactivity and alternating-site cooperativity

Despite having two active sites, the *E. coli* enzyme phosphorylates only one histidine at a time. *"The enzyme shows strict half-sites reactivity with respect to the phosphorylation of a histidine residue in the alpha subunit that represents a step in catalysis"* ([PMID: 3311148](https://pubmed.ncbi.nlm.nih.gov/3311148/)). Positional ¹⁸O-isotope exchange experiments on a mono-thiophosphorylated enzyme showed no scrambling of [β,γ-¹⁸O]ATP into the non-bridge position, *"clearly indicating that the enzyme does not undergo even transient bisphosphorylation"* ([PMID: 3311148](https://pubmed.ncbi.nlm.nih.gov/3311148/)). These data support a model of cooperative, alternating active sites in which catalysis at one αβ half promotes phosphoryl transfer in the neighboring half — an elegant coupling of the two catalytic sites of the heterotetramer.

### Operon context and metabolic flux

*sucC* is encoded in the **sdhCDAB-sucABCD operon**, immediately downstream of the 2-oxoglutarate dehydrogenase genes (*sucAB*) and alongside its partner α-subunit gene *sucD*. *"the tricarboxylic acid cycle enzymes encoded by the sdhCDAB-sucABCD operon"* ([PMID: 30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/)) places *sucC* within the oxidative TCA cycle gene cluster, co-regulated with succinate dehydrogenase and 2-oxoglutarate dehydrogenase. Deletion phenotypes confirm the functional assignment: *"disruption of sucC and sucD (encoding subunits of the succinyl-CoA synthetase) increased HHP [high hydrostatic pressure] resistance"* via elevated basal RpoS activity ([PMID: 30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/)). Flux analysis shows SCS carries real, adjustable metabolic flux: deleting upstream isocitrate dehydrogenase *"diminishes flux through succinyl CoA synthetase"* ([PMID: 31504493](https://pubmed.ncbi.nlm.nih.gov/31504493/)), consistent with SCS lying downstream of 2-oxoglutarate dehydrogenase in the oxidative arm.

### Metabolic branch point feeding biosynthesis

The succinyl-CoA that SCS consumes (oxidative direction) or produces (anabolic direction) is a key acyl donor for biosynthesis. Homoserine O-succinyltransferase uses succinyl-CoA for the committed step of methionine biosynthesis: *"Homoserine acyltransferases catalyze the commitment step to methionine and other important biological precursors"* ([PMID: 17442255](https://pubmed.ncbi.nlm.nih.gov/17442255/)). In tetrapyrrole/heme biosynthesis, 5-aminolevulinate synthase *"catalyzes the condensation of glycine with succinyl-coenzyme A to yield aminolevulinate, carbon dioxide and CoA"* ([PMID: 11929042](https://pubmed.ncbi.nlm.nih.gov/11929042/)). Because SCS reversibly interconverts succinyl-CoA + Pᵢ + ADP and succinate + CoA + ATP, it both consumes succinyl-CoA (oxidative TCA, generating ATP) and regenerates it from succinate (anabolic direction). The anabolic role is *"particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed"* (UniProt P0A836 annotation).

### Cofactor requirement and cytoplasmic localization

UniProt P0A836 annotates the β-subunit as 388 amino acids (~41.4 kDa) and the enzyme as requiring Mg²⁺. Crystallographic analysis supports the Mg²⁺ requirement: *"the 'true' nucleotide substrate is probably an ADP-Mg(2+) complex"* ([PMID: 10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/)). The enzyme is a soluble, cytoplasmic protein. Experimental GO annotations assign **cytosol (GO:0005829) with evidence code IDA** (Inferred from Direct Assay) and the succinate-CoA ligase (ADP-forming) complex (GO:0009361, IDA). Molecular-function annotations include succinate-CoA ligase (ADP-forming) activity (GO:0004775, IMP), succinate-CoA ligase (GDP-forming) activity (GO:0004776, EXP), plus ATP binding and Mg²⁺ binding; process annotations include the tricarboxylic acid cycle (GO:0006099, IMP) and succinyl-CoA metabolic process (GO:0006104).

### Structural classification in the ATP-grasp superfamily

InterPro/UniProt feature mapping of P0A836 shows a two-domain architecture: an **ATP-grasp domain spanning residues 9–244** (N-terminal), carrying ATP-binding residues (46, 53–55, 99, 102, 107) and Mg²⁺-binding residues (199, 213), with substrate (succinate) binding residues in the C-terminal domain (264, 321–323). Pfam classifications are PF08442 (ATP-grasp_2) plus PF00549 (Ligase_CoA); PROSITE PS50975 (ATP_GRASP). These database-derived residues coincide precisely with the experimentally identified sites (the 8-N₃-ATP-labeled 107–119β peptide, the G53β/R54β phosphorylation-null mutant, and the C-terminal I322β/R324β/D326β succinate/CoA-binding mutants). The ATP-grasp fold is defined as *"two α+β domains that 'grasp' a molecule of ATP between them"*, and the superfamily enzymes *"catalyze the ATP-assisted reaction of a carboxylic acid with a nucleophile via the formation of an acylphosphate intermediate"* ([PMID: 21920581](https://pubmed.ncbi.nlm.nih.gov/21920581/)), consistent with the succinyl-phosphate-type intermediate chemistry of SCS.

---

## Mechanistic Model / Interpretation

### Reaction and the division of labor between subunits

```
         succinyl-CoA  +  Pi  +  ADP   ⇌   succinate  +  CoA  +  ATP      (ΔG ≈ 0; reversible)
                          |                                    |
         (oxidative TCA: energy conservation)   (anabolic: succinyl-CoA supply)
```

The enzyme is an α₂β₂ heterotetramer built from two αβ catalytic halves. The subunits divide the labor as follows:

| Feature | α-subunit (sucD) | β-subunit (**sucC**, P0A836) |
|---|---|---|
| Catalytic phosphohistidine | **His246α** (transiently phosphorylated) | — |
| Nucleotide (ADP/ATP) binding | — | **N-terminal ATP-grasp fold** (res. ~9–244) |
| Mg²⁺ binding | — | residues 199, 213 (β) |
| Nucleotide specificity switch | — | **Pro20β** (ADP vs GDP) |
| Succinate / dicarboxylate binding | (CoA, phosphate contributions) | **C-terminal domain** (res. 264, 321–323) |
| Power helix (phosphohistidine stabilization) | one power helix; Glu208α | one power helix; **Glu197β** |

### The swinging phosphohistidine couples two spatially separated half-reactions

SCS chemistry occurs in two half-reactions at two distinct sites, bridged by a mobile phosphohistidine loop:

```
  Site I (succinate/CoA end)                      Site II (nucleotide end)
  ─────────────────────────                       ──────────────────────────
  succinyl-CoA + Pi                                 His246α~P  +  NDP
        │                                                 │
        ▼  (succinyl-phosphate; CoA released)             ▼  (phosphoryl transfer to nucleotide)
   His246α  +  succinate                              His246α  +  NTP
        └──────────  phospho-His loop swings ~29–35 Å  ──────────┘
            (Glu208α stabilizes at site I; Glu197β stabilizes at site II)
```

A phosphoryl group derived from Pᵢ and succinyl-CoA (generating a succinyl-phosphate intermediate and releasing CoA) is placed onto His246α at site I. The phosphohistidine loop then swings ~29–35 Å to site II, where the phosphoryl group is transferred to the nucleotide bound in the β-subunit ATP-grasp fold, producing NTP. The two glutamates (Glu208α at site I, Glu197β at site II) stabilize the histidine for phosphorylation/dephosphorylation at each location. Strict half-sites reactivity means only one of the two catalytic halves carries the phosphoryl group at any moment, with the two sites functioning in an alternating, cooperative fashion.

### Physiological placement: a reversible node in central carbon metabolism

```
        isocitrate ──ICDH──► 2-oxoglutarate ──OGDH(sucAB)──► succinyl-CoA
                                                                  │
                                              ┌───────────────────┤
                                              │                   │
                                      (anabolic demand)      SCS (sucC/sucD)
                                              │                   │  ⇅  ATP/ADP
                                 ┌────────────┴─────────┐         ▼
                           methionine biosynthesis   heme/tetrapyrrole      succinate ──SDH──► fumarate
                           (homoserine succinyl-     (5-aminolevulinate
                            transferase)              synthase)
```

In the clockwise (oxidative) direction, SCS converts the high-energy thioester of succinyl-CoA into ATP (or GTP) — the TCA cycle's only substrate-level phosphorylation. In the reverse (anabolic) direction, it regenerates succinyl-CoA from succinate, replenishing the acyl donor needed for methionine and heme biosynthesis, which is physiologically critical when anaerobic conditions repress the oxidative 2-oxoglutarate dehydrogenase route. Its position in the sdhCDAB-sucABCD operon co-regulates it with the flanking TCA enzymes, and flux experiments confirm it carries adjustable metabolic flux downstream of 2-oxoglutarate dehydrogenase.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [9917402](https://pubmed.ncbi.nlm.nih.gov/9917402/) | *A detailed structural description of E. coli succinyl-CoA synthetase* | Defines the reaction, the α₂β₂ tetramer, and the ~35 Å histidine movement |
| [33645539](https://pubmed.ncbi.nlm.nih.gov/33645539/) | *Second distinct conformation of the phosphohistidine loop in SCS* | Confirms SCS as the unique substrate-level phosphorylation; 29 Å phosphoryl bridge |
| [10625475](https://pubmed.ncbi.nlm.nih.gov/10625475/) | *ADP-binding site of E. coli SCS revealed by x-ray crystallography* | ADP-Mg²⁺ bound in β-subunit ATP-grasp fold; Mg²⁺ requirement |
| [10353839](https://pubmed.ncbi.nlm.nih.gov/10353839/) | *Probing the nucleotide-binding site of E. coli SCS* | 8-N₃-ATP labeling, P20βQ specificity switch, C-terminal succinate/CoA mutants |
| [11781092](https://pubmed.ncbi.nlm.nih.gov/11781092/) | *Two glutamate residues… crucial for phosphorylation/dephosphorylation* | Glu197β essential at the nucleotide active site (site II) |
| [22751660](https://pubmed.ncbi.nlm.nih.gov/22751660/) | *GTP-preferring SCS from Thermus aquaticus* | Establishes E. coli ADP/ATP preference vs GTP-preferring orthologs |
| [27487822](https://pubmed.ncbi.nlm.nih.gov/27487822/) | *Structural basis for binding of succinate to SCS* | Succinate binds β C-terminal domain; explains strict specificity |
| [3304349](https://pubmed.ncbi.nlm.nih.gov/3304349/) | *Renaturation and assembly of E. coli SCS from α and β subunits* | α₂β₂ structure; non-dissociating active tetramer; obligate assembly |
| [3311148](https://pubmed.ncbi.nlm.nih.gov/3311148/) | *Positional ¹⁸O isotope exchange as a probe of E. coli SCS* | Strict half-sites reactivity; no transient bisphosphorylation |
| [30497599](https://pubmed.ncbi.nlm.nih.gov/30497599/) | *Novel genes in high hydrostatic pressure resistance of E. coli* | Operon context (sdhCDAB-sucABCD); ΔsucC/ΔsucD stress phenotype |
| [31504493](https://pubmed.ncbi.nlm.nih.gov/31504493/) | *Effects of isocitrate dehydrogenase deletion on fluxes in E. coli* | SCS carries metabolic flux, modulated by upstream ICDH |
| [17442255](https://pubmed.ncbi.nlm.nih.gov/17442255/) | *Essential functional groups in homoserine succinyltransferase* | Succinyl-CoA feeds committed step of methionine biosynthesis |
| [11929042](https://pubmed.ncbi.nlm.nih.gov/11929042/) | *Circular permutation of 5-aminolevulinate synthase* | Succinyl-CoA is substrate for first step of heme biosynthesis |
| [21920581](https://pubmed.ncbi.nlm.nih.gov/21920581/) | *The ATP-grasp enzymes* | Defines the ATP-grasp fold and its acyl-phosphate mechanism |

**Coherence of the evidence.** The structural, biochemical, genetic, and bioinformatic lines of evidence converge without contradiction. X-ray crystallography (PMIDs 9917402, 10625475, 27487822, 33645539) and photoaffinity/mutagenesis studies (PMIDs 10353839, 11781092) independently place the nucleotide site in the β N-terminal ATP-grasp fold and the succinate site in the β C-terminal domain. Kinetic isotope studies (PMID 3311148) and assembly studies (PMID 3304349) establish the α₂β₂ half-sites mechanism. Genetic/flux work (PMIDs 30497599, 31504493) confirms physiological function and operon context. Database domain mapping (ATP-grasp, Pfam PF08442/PF00549) matches the experimentally defined residues exactly. Comparative orthologous structures (pig heart GTP-specific SCS, PMID 10873456; *T. aquaticus*, PMID 22751660) confirm the conserved mechanism and highlight the species-specific nucleotide preference controlled by residue 20β.

---

## Limitations and Knowledge Gaps

- **Localization granularity.** Cytosolic localization is experimentally supported (IDA, GO:0005829), consistent with SCS being a soluble enzyme. However, formal demonstration of whether it is exclusively free in the cytoplasm versus transiently associated with other TCA enzymes in a "metabolon" in *E. coli* is not established by the reviewed literature.
- **Residue-numbering conventions.** Some catalytic residues are cited from orthologs or UniProt feature tables (e.g., Glu197β, Pro20β, succinate-binding residues 264/321–323). While cross-validated against experimental *E. coli* studies, exact numbering can differ between mature-protein and precursor schemes; specific *E. coli* numbering should be confirmed against the current UniProt entry when precision matters.
- **Quantitative kinetics.** The report establishes directionality, specificity, and mechanism qualitatively and semi-quantitatively (e.g., >5-fold Km shift for P20βQ). A consolidated table of absolute kinetic constants (kcat; Km for succinate, CoA, Pᵢ, ADP/GDP) for wild-type *E. coli* SCS was not assembled and would strengthen the metabolic-flux interpretation.
- **Regulation.** Transcriptional regulation of the sdhCDAB-sucABCD operon (e.g., by ArcA, FNR, Crp) and any post-translational modification of SCS in *E. coli* were not examined in depth; these govern when the enzyme runs oxidatively versus anabolically.
- **In vivo directionality.** The precise in vivo balance between ATP-generating (oxidative) and succinyl-CoA-supplying (anabolic) flux under defined growth conditions was inferred from annotation and flux studies rather than measured directly here.

---

## Proposed Follow-up Experiments / Actions

1. **Consolidate steady-state kinetics.** Compile or measure kcat and Km values for all substrates of wild-type *E. coli* SCS (both ADP- and GDP-forming directions) to quantify the physiological bias and parameterize flux models.
2. **Confirm *E. coli*-specific residue numbering.** Map Pro20β, Glu197β, His246α, and the succinate-binding C-terminal residues onto the current P0A836/sucD sequences and a deposited *E. coli* SCS structure (e.g., PDB entries from PMIDs 9917402/10625475/27487822) to lock in exact numbering.
3. **Directionality under defined conditions.** Use ¹³C stable-isotope-resolved metabolomics in aerobic versus anaerobic chemostat cultures to measure net SCS flux direction and quantify anabolic succinyl-CoA supply during anaerobic growth.
4. **Regulatory dissection.** Test operon regulation (ArcA/FNR/Crp) and growth-phase/RpoS effects on sucC expression, connecting the observed ΔsucC stress phenotype (PMID 30497599) to mechanism.
5. **Structural snapshots of the full cycle.** Pursue time-resolved or trapped-intermediate structures capturing the phosphohistidine loop mid-swing to further resolve the alternating-site coupling between the two αβ halves.
6. **Specificity engineering.** Use the Pro20β determinant to build nucleotide-preference variants and test their effect on cellular ATP/GTP balance, directly probing the physiological consequence of the β-subunit specificity switch.

---

*Gene identity verification: CONFIRMED. The gene symbol sucC, organism (E. coli K-12), EC 6.2.1.5, the succinate/malate-CoA ligase β-subunit family, and the ATP-grasp domain architecture (IPR011761, IPR013650, IPR013815, IPR017866, IPR005811) all match the extensive primary literature on E. coli succinyl-CoA synthetase. No gene-identity ambiguity was encountered.*


## Artifacts

- [OpenScientist final report](sucC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sucC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9917402
2. PMID:33645539
3. PMID:3304349
4. PMID:10625475
5. PMID:10353839
6. PMID:11781092
7. PMID:22751660
8. PMID:27487822
9. PMID:3311148
10. PMID:30497599
11. PMID:31504493
12. PMID:17442255
13. PMID:11929042
14. PMID:21920581