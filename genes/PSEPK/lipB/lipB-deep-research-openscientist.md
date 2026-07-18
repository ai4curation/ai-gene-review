---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T15:28:39.943106'
end_time: '2026-07-18T16:10:48.023246'
duration_seconds: 2528.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lipB
  gene_symbol: lipB
  uniprot_accession: Q88DM4
  protein_description: 'RecName: Full=Octanoyltransferase {ECO:0000255|HAMAP-Rule:MF_00013};
    EC=2.3.1.181 {ECO:0000255|HAMAP-Rule:MF_00013}; AltName: Full=Lipoate-protein
    ligase B {ECO:0000255|HAMAP-Rule:MF_00013}; AltName: Full=Lipoyl/octanoyl transferase
    {ECO:0000255|HAMAP-Rule:MF_00013}; AltName: Full=Octanoyl-[acyl-carrier-protein]-protein
    N-octanoyltransferase {ECO:0000255|HAMAP-Rule:MF_00013};'
  gene_info: Name=lipB {ECO:0000255|HAMAP-Rule:MF_00013}; OrderedLocusNames=PP_4801;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the LipB family. {ECO:0000255|HAMAP-
  protein_domains: aa-tRNA-synth_II/BPL/LPL. (IPR045864); BPL_LPL_catalytic. (IPR004143);
    Octanoyltransferase. (IPR000544); Octanoyltransferase_CS. (IPR020605); LplA-B_cat
    (PF21948)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lipB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lipB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DM4
- **Protein Description:** RecName: Full=Octanoyltransferase {ECO:0000255|HAMAP-Rule:MF_00013}; EC=2.3.1.181 {ECO:0000255|HAMAP-Rule:MF_00013}; AltName: Full=Lipoate-protein ligase B {ECO:0000255|HAMAP-Rule:MF_00013}; AltName: Full=Lipoyl/octanoyl transferase {ECO:0000255|HAMAP-Rule:MF_00013}; AltName: Full=Octanoyl-[acyl-carrier-protein]-protein N-octanoyltransferase {ECO:0000255|HAMAP-Rule:MF_00013};
- **Gene Information:** Name=lipB {ECO:0000255|HAMAP-Rule:MF_00013}; OrderedLocusNames=PP_4801;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the LipB family. {ECO:0000255|HAMAP-
- **Key Domains:** aa-tRNA-synth_II/BPL/LPL. (IPR045864); BPL_LPL_catalytic. (IPR004143); Octanoyltransferase. (IPR000544); Octanoyltransferase_CS. (IPR020605); LplA-B_cat (PF21948)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lipB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lipB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lipB** (gene ID: lipB, UniProt: Q88DM4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LipB (Q88DM4 / PP_4801) in *Pseudomonas putida* KT2440: Octanoyltransferase Initiating De Novo Lipoic-Acid Cofactor Assembly

**Target:** UniProt **Q88DM4** (LIPB_PSEPK) · Gene **lipB** · OrderedLocusName **PP_4801** · EC **2.3.1.181**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / **KT2440**)
**Report date:** 2026-07-18

---

## Summary

**LipB (UniProt Q88DM4; ordered locus PP_4801) is the octanoyltransferase (EC 2.3.1.181) that catalyzes the first committed step of de novo lipoic-acid cofactor biosynthesis in *Pseudomonas putida* KT2440.** It transfers the eight-carbon octanoyl chain from octanoyl-acyl-carrier-protein (octanoyl-ACP), an intermediate diverted from the fatty-acid biosynthetic pool, onto the ε-amino group of a specific, conserved lysine residue in the lipoyl domains of its cognate acceptor proteins. The reaction is `octanoyl-[ACP] + L-lysyl-[protein] → N6-octanoyl-L-lysyl-[protein] + holo-[ACP] + H+` (Rhea:17665), and it corresponds to step 1 of 2 in the UniPathway route "protein N6-(lipoyl)lysine from octanoyl-[ACP]" (UPA00538/UER00592). Its immediate product is the substrate of the adjacent lipoyl synthase LipA (PP_4800), which inserts two sulfur atoms to complete the mature lipoyl cofactor.

The enzyme operates in the **cytoplasm** and acts on the lipoyl domains of the E2 subunits of the 2-oxoacid dehydrogenase complexes (pyruvate dehydrogenase, 2-oxoglutarate dehydrogenase, and the branched-chain 2-oxoacid/2-oxoisovalerate dehydrogenase) and on the glycine cleavage system H protein (GcvH). These are the central and branched-chain metabolic hubs whose activity requires a covalently bound lipoyl arm. LipB thus sits at the origin of protein lipoylation and is essential for endogenous activation of all of these complexes; loss-of-function of the orthologous gene renders bacteria auxotrophic for lipoate or octanoate.

Mechanistically, LipB is a member of the LipB/BPL/LPL catalytic superfamily and uses a **Cys–Lys catalytic dyad** with a covalent thioester acyl-enzyme intermediate. In Q88DM4, Cys169 is the nucleophile that forms the octanoyl-cysteine thioester, and residue Lys135 lowers the Cys thiol pKa to activate it. The AlphaFold model of Q88DM4 (mean pLDDT 95.2) places the Lys135 Nζ atom 3.10 Å from the Cys169 sulfur — a hydrogen-bond/ion-pair distance — structurally validating this dyad. Because the *P. putida* enzyme itself has not been characterized biochemically, its functional assignment rests on strong orthology to the experimentally defined *Escherichia coli* LipB (54.8% identity, identical catalytic-Cys sequence motif `RINPCGYAG`), conserved domain architecture, and pathway/genomic context (lipB–lipA adjacency). Confidence in the annotation is very high.

---

## Key Findings

### F001 — LipB catalyzes the first committed step of de novo lipoic-acid biosynthesis

UniProt Q88DM4, governed by HAMAP rule MF_00013, annotates LipB as an octanoyltransferase (EC 2.3.1.181) catalyzing the reaction octanoyl-[ACP] + L-lysyl-[protein] → N6-octanoyl-L-lysyl-[protein] + holo-[ACP] + H+ (Rhea:17665). This is the first of the two committed reactions that build the lipoyl cofactor directly on target proteins, and it corresponds to UniPathway UPA00538/UER00592 (step 1/2).

The role is anchored by experimental work on the orthologous *E. coli* enzyme. As stated by Cronan and colleagues, *"LipB is responsible for octanoylation of the E2 components of 2-oxoacid dehydrogenases to provide the substrates of LipA, an S-adenosyl-L-methionine radical enzyme that inserts two sulfur atoms into the octanoyl moiety to give the active lipoylated dehydrogenase complexes"* ([PMID: 21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/)). The two-step logic of the pathway is likewise explicit in the lipoyl-synthase literature: *"The lipoyl cofactor is synthesized de novo in two committed steps, involving the LipB-catalyzed transfer of an octanoyl chain derived from fatty acid biosynthesis to a lipoyl carrier protein and the LipA-catalyzed insertion of sulfur atoms at C6 and C8 of the octanoyl chain"* ([PMID: 26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/)). LipB therefore performs the acyl-transfer step, and LipA performs the subsequent sulfur-insertion step.

### F002 — Substrate: octanoyl-ACP, with documented selectivity for the C8 acyl chain

The physiological acyl donor is octanoyl-ACP. UniProt notes that "octanoyl-ACP is likely to be the physiological substrate," although lipoyl-ACP can also serve. The enzyme's preference for the eight-carbon chain is not incidental: LipB has a *"well-documented substrate selectivity, indicating a mechanism of octanoic acid recognition"* ([PMID: 34704050](https://pubmed.ncbi.nlm.nih.gov/34704050/)). Bartholow et al. (2021) established that this selectivity is mediated by specific protein–protein interactions between LipB and ACP that position and recognize the octanoate chain: *"In bacteria, octanoic acid is transferred from the acyl carrier protein (ACP) to the lipoylated target protein by the octanoyltransferase LipB."* Complementary NMR/biochemical work reinforces that LipB primarily recognizes the C8 chain length ([PMID: 35764173](https://pubmed.ncbi.nlm.nih.gov/35764173/)). This chain-length specificity is what commits precisely an eight-carbon precursor — the correct length for later sulfur insertion at C6 and C8 — to the lipoylation pathway.

### F003 — Cys–Lys catalytic dyad and a thioester acyl-enzyme intermediate

LipB is a two-step (ping-pong) acyltransferase that proceeds through a covalent octanoyl-cysteine thioester intermediate. UniProt Q88DM4 annotates the active site as ACT_SITE 169 ("Acyl-thioester intermediate") and SITE 135 ("Lowers pKa of active site Cys"), with substrate-binding residues at positions 71–78, 138–140, and 151–153, all within the BPL/LPL catalytic domain (residues 32–207) that adopts the Class-II aminoacyl-tRNA-synthetase/biotin-synthetase-like fold (SSF55681). The Cronan group established that the LipB/LipL family uses a catalytic cysteine and forms a thioester-linked acyl-enzyme: structural comparison showed that *"although the active site cysteine residues of LipL and LipB are located in different positions within the polypeptide chains, alignment of their structures show these residues occupy similar positions"* ([PMID: 21338421](https://pubmed.ncbi.nlm.nih.gov/21338421/)). This confirms that the *P. putida* ACT_SITE Cys169 is the acyl-transfer nucleophile.

### F004 — Cytoplasmic localization; acceptors are E2 lipoyl domains and GcvH

UniProt assigns LipB to the cytoplasm (GO:0005737), consistent with its soluble substrates and the intracellular fatty-acid synthesis pathway that supplies octanoyl-ACP. Its physiological acyl acceptors are the lipoyl domains of the 2-oxoacid dehydrogenase E2 subunits and the glycine cleavage H protein. In *E. coli*, LipB co-purifies with intact 2-oxoacid dehydrogenase complexes: *"We report that the intact pyruvate and 2-oxoglutarate dehydrogenase complexes specifically copurify with both LipB and LipA"* ([PMID: 21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/)), and the binding surface spans both the lipoyl domain and the E2 subunit itself. In organisms with a dedicated octanoyltransferase, the glycine cleavage H protein is a defined target — *"We report that LipM specifically modifies the glycine cleavage system protein, GcvH"* ([PMID: 21338421](https://pubmed.ncbi.nlm.nih.gov/21338421/)) — a route that is also physiologically relevant to glycine oxidation in *Pseudomonas*.

### F005 — Essentiality: lipB nulls are lipoate/octanoate auxotrophs

LipB is required for endogenous lipoylation. Hermes and Cronan showed that *"strains containing null mutations in lipB are auxotrophic for either lipoic acid or octanoic acid"* ([PMID: 19684135](https://pubmed.ncbi.nlm.nih.gov/19684135/)), and that suppression required salvage-ligase (LplA) variants with a reduced Km for free octanoate — i.e., only an alternate route into the pathway can bypass the loss of LipB. This defines LipB as the sole entry point for de novo (biosynthetic) lipoylation; in its absence, cells depend entirely on scavenging lipoate/octanoate from the environment.

### F006 — P. putida LipB is a bona fide ortholog of experimentally characterized E. coli LipB

A global Needleman–Wunsch alignment of Q88DM4 (216 aa) against *E. coli* LipB (P60720, 213 aa) yields **54.8% identity** (119/217 aligned positions). Critically, the active-site cysteine sequence context is strictly conserved and identical between the two proteins: **`RINPCGYAG`** (Cys169 in both). Both proteins are assigned to COG0321 and are governed by HAMAP rule MF_00013. This level of identity, combined with an identical catalytic motif and shared domain architecture, licenses transfer of the well-established *E. coli* function to the *P. putida* enzyme with high confidence.

### F007 — Lipoate is uniquely assembled directly on its cognate enzymes

Unlike most cofactors — which are synthesized and then attached — lipoic acid is built in place on the very enzymes that require it. Authoritative reviews make this explicit: *"the cofactor is assembled on its cognate proteins rather than being assembled and subsequently attached as in the typical pathway, like that of biotin attachment. The first lipoate biosynthetic pathway determined was that of Escherichia coli, which utilizes two enzymes to form the active lipoylated protein from a fatty acid biosynthetic intermediate"* ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)). LipB catalyzes the first of these two on-protein steps, transferring octanoate from the fatty-acid intermediate octanoyl-ACP onto the acceptor lysine ([PMID: 30236800](https://pubmed.ncbi.nlm.nih.gov/30236800/)).

### F008 — AlphaFold structurally validates the Cys169–Lys135 dyad in Q88DM4

The AlphaFold model AF-Q88DM4-F1 is of very high quality (mean pLDDT 95.2; pLDDT 98.1 at Lys135, 83.4 at Cys169). In the folded model, the ε-amino nitrogen (Nζ) of Lys135 lies **3.10 Å** from the sulfur (Sγ) of Cys169 — a hydrogen-bond/ion-pair distance — and no other basic residue is within 8 Å of the Cys thiol. This geometry independently confirms UniProt's functional annotation: Cys169 is the thioester-forming nucleophile and Lys135 is positioned precisely to lower its pKa and activate it for catalysis.

### F009 — LipB supplies the lipoyl cofactor to multiple lipoate-dependent complexes in P. putida

*P. putida* runs several lipoyl-dependent multienzyme systems, all of which depend on LipB-initiated lipoylation: pyruvate dehydrogenase, 2-oxoglutarate dehydrogenase, the branched-chain 2-oxoacid dehydrogenase, and the glycine cleavage system. The branched-chain complex is particularly well documented in this organism — its E1 component was crystallized from *P. putida*: *"The crystal structure of a heterotetrameric (alpha2beta2) E1, 2-oxoisovalerate dehydrogenase from Pseudomonas putida, reveals a tightly packed arrangement of the four subunits"* ([PMID: 10426958](https://pubmed.ncbi.nlm.nih.gov/10426958/)). Uniquely, *P. putida* expresses two distinct lipoamide dehydrogenases (E3): *"Pseudomonas putida produces two lipoamide dehydrogenases with molecular weights of 49,000 and 56,000 designated LPD-val and LPD-glc"* ([PMID: 6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/)), with LPD-val serving branched-chain 2-oxoacid oxidation and LPD-glc serving glucose/glycine oxidation. Every one of these lipoyl-arm-bearing systems lies downstream of LipB.

### F010 — Genomic organization: lipB (PP_4801) adjacent to lipA (PP_4800)

In *P. putida* KT2440, lipB (PP_4801) is immediately adjacent to lipA (PP_4800, Q88DM5; lipoyl synthase, EC 2.8.1.8). This gene pairing mirrors the lipBA operon organization documented in other γ-proteobacteria — for example the *Shewanella* lipBA operon, which is regulated by cAMP-CRP ([PMID: 25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/)). The physical adjacency of the two committed de novo lipoylation genes reflects their sequential, obligately coupled roles: LipB makes the octanoyl-protein that LipA then converts to lipoyl-protein.

---

## Mechanistic Model / Interpretation

### The de novo lipoylation pathway and LipB's place in it

```
  Fatty-acid synthesis (FAS II)
            │
            ▼
      octanoyl-ACP  ──────────┐  (C8 acyl donor; selectively recognized)
                              │
                    ┌─────────▼───────────┐
                    │   LipB (PP_4801)     │   STEP 1  EC 2.3.1.181
                    │  octanoyltransferase │   Cys169–Lys135 dyad
                    │  thioester intermed. │   octanoyl-S-Cys169 acyl-enzyme
                    └─────────┬───────────┘
                              │  transfers octanoyl → ε-NH2 of acceptor Lys
                              ▼
        N6-octanoyl-[lysyl-protein]  (octanoyl-E2 / octanoyl-GcvH)
                              │
                    ┌─────────▼───────────┐
                    │   LipA (PP_4800)     │   STEP 2  EC 2.8.1.8
                    │   lipoyl synthase    │   radical-SAM; +2 S at C6,C8
                    └─────────┬───────────┘
                              ▼
        N6-(lipoyl)-[lysyl-protein]  = MATURE, ACTIVE cofactor
                              │
      ┌───────────────┬───────┴────────┬──────────────────┐
      ▼               ▼                ▼                  ▼
  Pyruvate DH     2-oxoglutarate   Branched-chain      Glycine
  (E2)            DH (E2)          2-oxoacid DH (E2)   cleavage (GcvH)
```

### Reaction chemistry

LipB is a ping-pong (double-displacement) acyltransferase. The catalytic cysteine (Cys169), activated by the adjacent lysine (Lys135) that lowers its thiol pKa, attacks the thioester of octanoyl-ACP to form a covalent **octanoyl-S-Cys169 acyl-enzyme intermediate**, releasing holo-ACP. In the second half-reaction, the ε-amino group of the acceptor lysine (in an E2 lipoyl domain or GcvH) attacks the acyl-enzyme, transferring octanoate to form the amide-linked N6-octanoyl-lysyl product and regenerating free enzyme. The 3.1 Å Cys169–Lys135 geometry seen in the AlphaFold model is exactly what this chemistry requires.

### Why "on-protein" assembly matters

Lipoate is not synthesized as a free molecule and later attached. Instead, LipB installs the eight-carbon precursor directly on the target lysine, and LipA then completes the cofactor in situ. This unusual strategy explains why LipB substrate selectivity for the C8 chain is essential: only an eight-carbon chain places carbons 6 and 8 where LipA's radical-SAM chemistry can insert the two sulfur atoms that create the functional dithiolane ring.

### Comparison of the P. putida and E. coli enzymes

| Property | *P. putida* LipB (Q88DM4) | *E. coli* LipB (P60720) |
|---|---|---|
| Length | 216 aa | 213 aa |
| Sequence identity | — | 54.8% (vs Q88DM4) |
| Catalytic Cys motif | `RINPCGYAG` (Cys169) | `RINPCGYAG` (Cys169) |
| Catalytic dyad | Cys169 / Lys135 | Cys / Lys |
| EC number | 2.3.1.181 | 2.3.1.181 |
| Orthology group | COG0321 / HAMAP MF_00013 | COG0321 / HAMAP MF_00013 |
| Genomic context | lipB (PP_4801)–lipA (PP_4800) | lipB–lipA |
| Biochemical characterization | Inferred (not yet assayed) | Experimentally established |

### Downstream metabolic dependence in P. putida

| Lipoyl-dependent system | Lipoyl-bearing component | Metabolic role | E3 partner in *P. putida* |
|---|---|---|---|
| Pyruvate dehydrogenase | E2 (AceF-type) lipoyl domain | Pyruvate → acetyl-CoA | LPD-glc |
| 2-Oxoglutarate dehydrogenase | E2 (SucB-type) lipoyl domain | TCA cycle | LPD-glc |
| Branched-chain 2-oxoacid DH | E2 lipoyl domain | Val/Leu/Ile catabolism | LPD-val |
| Glycine cleavage system | GcvH H protein | Glycine/one-carbon metabolism | LPD-glc |

Because all four systems require a lipoyl arm, and because LipB is the sole entry into de novo lipoylation, LipB activity is a single upstream determinant of central carbon metabolism (PDH, OGDH), branched-chain amino-acid catabolism (BCKDH), and one-carbon/glycine metabolism (GCS) in *P. putida*.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [21209092](https://pubmed.ncbi.nlm.nih.gov/21209092/) | *Protein–protein interactions in assembly of lipoic acid on the 2-oxoacid dehydrogenases* | Defines LipB's catalytic role (octanoylation of E2 to feed LipA) and shows LipB co-purifies with intact PDH/OGDH complexes (F001, F004). |
| [26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/) | *Characterization of Lipoyl Synthase from Mycobacterium tuberculosis* | States the two-step de novo pathway: LipB octanoyl transfer, then LipA sulfur insertion at C6/C8 (F001). |
| [34704050](https://pubmed.ncbi.nlm.nih.gov/34704050/) | *Protein–protein interaction based substrate control in octanoyltransfer* | Documents LipB substrate selectivity and octanoic-acid recognition via ACP interactions (F002). |
| [35764173](https://pubmed.ncbi.nlm.nih.gov/35764173/) | *Lipoate protein ligase B primarily recognizes the C8 chain* | Reinforces C8 chain-length recognition by LipB (F002). |
| [21338421](https://pubmed.ncbi.nlm.nih.gov/21338421/) | *A novel amidotransferase required for lipoic acid cofactor assembly in B. subtilis* | Establishes the LipB/LipL family catalytic cysteine and identifies GcvH as a target of the octanoyltransfer step (F003, F004). |
| [19684135](https://pubmed.ncbi.nlm.nih.gov/19684135/) | *Scavenging of cytosolic octanoic acid by mutant LplA ... lacking LipB* | Shows lipB nulls are lipoate/octanoate auxotrophs; defines essentiality (F005). |
| [27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/) | *Assembly of Lipoic Acid on Its Cognate Enzymes* | Authoritative review: lipoate is built on cognate proteins via LipB+LipA from a fatty-acid intermediate (F007). |
| [30236800](https://pubmed.ncbi.nlm.nih.gov/30236800/) | *Advances in synthesis of biotin and assembly of lipoic acid* | Review context for on-protein lipoate assembly (F007). |
| [10426958](https://pubmed.ncbi.nlm.nih.gov/10426958/) | *Crystal structure of 2-oxoisovalerate dehydrogenase (P. putida)* | Confirms P. putida possesses a branched-chain 2-oxoacid DH requiring lipoylation (F009). |
| [6546487](https://pubmed.ncbi.nlm.nih.gov/6546487/) | *Oxidation of glycine by Pseudomonas putida requires a specific lipoamide dehydrogenase* | Establishes P. putida's two lipoamide dehydrogenases (LPD-val, LPD-glc) and its multiple lipoate-dependent systems (F009). |
| [25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/) | *A new regulatory mechanism for bacterial lipoic acid synthesis* | Documents lipBA operon organization and cAMP-CRP regulation in γ-proteobacteria (F010). |

Supporting/contextual literature also reviewed: LipM/LipL two-gene octanoyltransfer in *B. subtilis* ([PMID: 21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/)); archaeal LplA-N/LplA-C lipoylation ([PMID: 23116157](https://pubmed.ncbi.nlm.nih.gov/23116157/)); yeast Lip3 ([PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/)); GcvH NMR assignments ([PMID: 29335837](https://pubmed.ncbi.nlm.nih.gov/29335837/)); metabolic engineering of free lipoic acid ([PMID: 36639019](https://pubmed.ncbi.nlm.nih.gov/36639019/)); review of lipoic acid attachment ([PMID: 38624243](https://pubmed.ncbi.nlm.nih.gov/38624243/)); human E3 structure ([PMID: 15946682](https://pubmed.ncbi.nlm.nih.gov/15946682/)); *P. aeruginosa* branched-chain oxo-acid DH ([PMID: 3085653](https://pubmed.ncbi.nlm.nih.gov/3085653/)).

**Gene-identity note.** No literature was found for a *different* gene sharing the symbol "lipB" that would create an identification conflict. All evidence is consistent with Q88DM4 being the octanoyltransferase LipB of the de novo lipoate pathway. The gene identity is confirmed, not ambiguous.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the P. putida enzyme.** The functional assignment for Q88DM4 rests on strong orthology (54.8% identity, identical catalytic-Cys motif) to the experimentally defined *E. coli* LipB, plus HAMAP/COG family membership, structural inference (AlphaFold dyad geometry), and pathway context — not on direct enzyme assays of the *P. putida* protein. No published kinetic parameters (kcat, Km for octanoyl-ACP or acceptor domains) exist for Q88DM4 specifically.

2. **No experimental structure.** The Cys169–Lys135 dyad is validated by an AlphaFold model (very high confidence, mean pLDDT 95.2), not by an experimental crystal or cryo-EM structure of the *P. putida* enzyme.

3. **Acceptor specificity in P. putida is inferred.** The identification of PDH-E2, OGDH-E2, BCKDH-E2, and GcvH as LipB acceptors in *P. putida* is drawn from the general bacterial paradigm and from the known presence of these complexes in *P. putida*, not from direct demonstration of LipB modifying each one in this organism.

4. **Regulation is not directly established.** The lipBA operon and cAMP-CRP regulation are documented in *Shewanella* and other γ-proteobacteria; whether PP_4801/PP_4800 are co-transcribed and identically regulated in *P. putida* KT2440 has not been experimentally confirmed here.

5. **Salvage-pathway interplay.** Whether *P. putida* possesses a functional LplA-type salvage ligase capable of bypassing LipB (as in *E. coli*), and the relative flux through de novo vs. salvage routes under different growth conditions, was not assessed.

---

## Proposed Follow-up Experiments / Actions

1. **In vitro enzymatic assay of recombinant Q88DM4.** Express and purify *P. putida* LipB and measure octanoyltransferase activity using octanoyl-ACP donor and a purified lipoyl domain (or GcvH) acceptor. Determine kcat and Km, and confirm the C8 chain-length preference against C6/C10 acyl-ACPs.

2. **Active-site mutagenesis.** Generate C169A and K135A/K135Q variants and confirm loss of activity, directly testing the predicted Cys–Lys dyad and thioester mechanism. Trap and detect the octanoyl-Cys169 acyl-enzyme intermediate by mass spectrometry.

3. **Genetic complementation / essentiality.** Construct a PP_4801 deletion in *P. putida* KT2440 and test for lipoate/octanoate auxotrophy; complement with *E. coli* lipB and with the native gene to confirm functional equivalence.

4. **Acceptor mapping in P. putida.** Use anti-lipoyl Western blotting and MS on the lipB deletion vs. wild type to confirm which endogenous proteins (PDH-E2, OGDH-E2, BCKDH-E2, GcvH) lose lipoylation, directly establishing acceptor specificity in this organism.

5. **Operon and regulation analysis.** Perform RT-PCR/RNA-seq and promoter mapping to test whether PP_4801–PP_4800 form a lipBA operon and whether cAMP-CRP or catabolite status modulates their expression, as seen in *Shewanella*.

6. **Experimental structure determination.** Solve a crystal or cryo-EM structure of *P. putida* LipB, ideally with an octanoyl/acyl-ACP or lipoyl-domain complex, to validate the AlphaFold-predicted dyad geometry and the ACP-recognition surface underlying substrate selectivity.

---

*Report generated from a 5-iteration autonomous investigation. Gene identity (lipB / Q88DM4 / PP_4801, Pseudomonas putida KT2440) was verified against UniProt, orthology, structural, and pathway evidence; no gene-symbol ambiguity was found.*


## Artifacts

- [OpenScientist final report](lipB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lipB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21209092
2. PMID:26841001
3. PMID:34704050
4. PMID:35764173
5. PMID:21338421
6. PMID:19684135
7. PMID:27074917
8. PMID:30236800
9. PMID:10426958
10. PMID:6546487
11. PMID:25611823
12. PMID:21338420
13. PMID:23116157
14. PMID:23960015
15. PMID:29335837
16. PMID:36639019
17. PMID:38624243
18. PMID:15946682
19. PMID:3085653