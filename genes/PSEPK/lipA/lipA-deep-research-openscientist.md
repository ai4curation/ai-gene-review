---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T15:28:36.252928'
end_time: '2026-07-18T16:22:28.223500'
duration_seconds: 3231.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lipA
  gene_symbol: lipA
  uniprot_accession: Q88DM5
  protein_description: 'RecName: Full=Lipoyl synthase {ECO:0000255|HAMAP-Rule:MF_00206};
    EC=2.8.1.8 {ECO:0000255|HAMAP-Rule:MF_00206}; AltName: Full=Lip-syn {ECO:0000255|HAMAP-Rule:MF_00206};
    Short=LS {ECO:0000255|HAMAP-Rule:MF_00206}; AltName: Full=Lipoate synthase {ECO:0000255|HAMAP-Rule:MF_00206};
    AltName: Full=Lipoic acid synthase {ECO:0000255|HAMAP-Rule:MF_00206}; AltName:
    Full=Sulfur insertion protein LipA {ECO:0000255|HAMAP-Rule:MF_00206};'
  gene_info: Name=lipA {ECO:0000255|HAMAP-Rule:MF_00206}; OrderedLocusNames=PP_4800;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the radical SAM superfamily. Lipoyl synthase
  protein_domains: Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638);
    LIAS_N. (IPR031691); Lipoyl_synth. (IPR003698); rSAM. (IPR007197)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lipA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lipA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DM5
- **Protein Description:** RecName: Full=Lipoyl synthase {ECO:0000255|HAMAP-Rule:MF_00206}; EC=2.8.1.8 {ECO:0000255|HAMAP-Rule:MF_00206}; AltName: Full=Lip-syn {ECO:0000255|HAMAP-Rule:MF_00206}; Short=LS {ECO:0000255|HAMAP-Rule:MF_00206}; AltName: Full=Lipoate synthase {ECO:0000255|HAMAP-Rule:MF_00206}; AltName: Full=Lipoic acid synthase {ECO:0000255|HAMAP-Rule:MF_00206}; AltName: Full=Sulfur insertion protein LipA {ECO:0000255|HAMAP-Rule:MF_00206};
- **Gene Information:** Name=lipA {ECO:0000255|HAMAP-Rule:MF_00206}; OrderedLocusNames=PP_4800;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the radical SAM superfamily. Lipoyl synthase
- **Key Domains:** Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638); LIAS_N. (IPR031691); Lipoyl_synth. (IPR003698); rSAM. (IPR007197)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lipA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lipA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lipA** (gene ID: lipA, UniProt: Q88DM5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lipA* (PP_4800, UniProt Q88DM5) — Lipoyl Synthase of *Pseudomonas putida* KT2440

## Summary

The gene **lipA** (ordered locus **PP_4800**; UniProt **Q88DM5**) of *Pseudomonas putida* KT2440 encodes **lipoyl synthase (LipA; EC 2.8.1.8)**, the enzyme that catalyzes the final, committed step of *de novo* lipoic-acid (lipoyl-cofactor) biosynthesis. LipA is a **radical S-adenosyl-L-methionine (radical-SAM) enzyme** that inserts two sulfur atoms at the chemically unactivated **C6 and C8 carbons of a protein-bound octanoyl chain** — an octanoyl group amide-linked to a specific lysine residue of a lipoyl carrier protein — converting it into the mature dithiolane lipoyl cofactor. This is the only known biological route to forming the C–S bonds of lipoic acid, and it is the sulfur-insertion reaction that gives the protein its alternate name "sulfur insertion protein LipA."

Mechanistically, LipA carries **two distinct [4Fe-4S] clusters** per polypeptide. The N-terminal **radical-SAM cluster**, ligated by the canonical CX₃CX₂C motif, reductively cleaves two molecules of SAM to generate two 5′-deoxyadenosyl radicals that sequentially abstract hydrogen atoms from C6 and C8 of the octanoyl substrate. The second, **auxiliary [4Fe-4S] cluster**, ligated by a CX₄CX₅C motif unique to lipoyl synthases plus a conserved serine, is **sacrificed as the sulfur donor** during each catalytic turnover — one of its sulfides becomes covalently attached to the substrate — and must be regenerated in vivo by iron-sulfur cluster carrier proteins (NfuA/IscU). The enzyme acts in the **cytoplasm**, downstream of type II fatty-acid synthesis and the octanoyltransferase LipB, and its physiological products are the lipoylated E2 subunits of the pyruvate, 2-oxoglutarate, and branched-chain 2-oxoacid dehydrogenase complexes and the glycine cleavage system H-protein.

No *P. putida*-specific biochemical study of Q88DM5 exists; the functional assignment rests on **strong orthology and conservation**. Q88DM5 shares **65% amino-acid identity with the biochemically characterized *Escherichia coli* LipA**, conserves **both Fe-S cluster cysteine motifs** and the **catalytically essential C-terminal RSSY motif** (including the auxiliary-cluster serine ligand), and is genomically **co-located with its cognate octanoyltransferase gene *lipB* (PP_4801)** in a *lipBA* tandem arrangement typical of γ-proteobacteria. Together these lines of evidence make the annotation of Q88DM5 as a bona fide lipoyl synthase secure to a high degree of confidence.

---

## Key Findings

### Finding 1 — Q88DM5 is a bona fide lipoyl synthase catalyzing sulfur insertion at C6/C8 of protein-bound octanoyl (EC 2.8.1.8)

The primary function of the *lipA* gene product is to catalyze the **insertion of two sulfur atoms at the unactivated C6 and C8 positions of a protein-bound octanoyl chain**, producing the lipoyl cofactor. This reaction is the terminal, sulfur-inserting step of *de novo* lipoic-acid biosynthesis and is chemically remarkable because it functionalizes saturated, unactivated carbon centers.

The assignment is anchored in the UniProt annotation (HAMAP-Rule MF_00206), which classifies Q88DM5 as lipoyl synthase, EC 2.8.1.8, in the radical-SAM superfamily. This was independently corroborated by bioinformatic analysis of the retrieved 338-residue sequence, which confirmed both diagnostic iron-sulfur cluster motifs: the **radical-SAM CX₃CX₂C motif** (sequence CTRRCPFC beginning at residue 110) and the **lipoyl-synthase auxiliary-cluster CX₄CX₅C motif** (CEEASCPNLGEC beginning at residue 84). The chemistry of the LipA-catalyzed reaction was defined by mechanistic studies on characterized orthologs, which established that lipoyl synthase "catalyzes the insertion of two sulfur atoms at the unactivated C6 and C8 positions of a protein-bound octanoyl chain to produce the lipoyl cofactor" ([PMID: 27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/)) and that this constitutes "the LipA-catalyzed insertion of sulfur atoms at C6 and C8 of the octanoyl chain" ([PMID: 26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/)).

The reaction can be summarized:

```
  (N6-octanoyl)-lysyl-[carrier protein]  +  2 SAM  +  2 e-  +  [S from auxiliary cluster]
                              │
                    LipA (radical SAM, 2× [4Fe-4S])
                              ▼
  (N6-lipoyl)-lysyl-[carrier protein]  +  2 L-methionine  +  2 5'-deoxyadenosine
```

### Finding 2 — LipA is a radical-SAM enzyme with two [4Fe-4S] clusters; the auxiliary cluster is sacrificed as the sulfur source each turnover

LipA is a two-cluster radical-SAM enzyme. Characterization of the *E. coli* ortholog established that the enzyme "can accommodate two [4Fe-4S] clusters per polypeptide and that this form of the enzyme is relevant to turnover" ([PMID: 15362861](https://pubmed.ncbi.nlm.nih.gov/15362861/)), with roughly 6.9 Fe and 6.4 S per polypeptide. One cluster is ligated by the CX₃CX₂C radical-SAM motif and initiates radical chemistry; the second, auxiliary cluster is ligated by the CX₄CX₅C motif conserved only in lipoyl synthases.

The catalytic cycle consumes **two equivalents of SAM**, each reductively cleaved to a 5′-deoxyadenosyl radical that abstracts a hydrogen atom from C6 and then C8 of the octanoyl chain in sequence. The inserted sulfur atoms are supplied not by a freely diffusing donor but by **destruction of the auxiliary cluster itself**. Crystallographic snapshots of *Mycobacterium tuberculosis* LipA captured this directly: during turnover "the serine ligand dissociates from the cluster, the iron ion is lost, and a sulfur atom that is still part of the cluster becomes covalently attached to C6 of the octanoyl substrate" ([PMID: 27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/)). Because the sulfur donor is consumed, the auxiliary cluster is a single-turnover reagent that must be rebuilt: "the second cluster is the sulfur source, necessitating its destruction during turnover. In Escherichia coli, this auxiliary cluster can be restored after each turnover by NfuA or IscU" ([PMID: 34292556](https://pubmed.ncbi.nlm.nih.gov/34292556/)). A catalytically and kinetically competent enzyme–substrate cross-linked intermediate, linked through the auxiliary cluster, was demonstrated biochemically, providing strong support for this sacrificial mechanism ([PMID: 24901788](https://pubmed.ncbi.nlm.nih.gov/24901788/)).

### Finding 3 — LipA works in the cytoplasmic de novo lipoic-acid pathway (LipB→LipA), acting on lipoyl carrier proteins

LipA operates as the **second of two committed steps** in the *de novo* lipoyl-cofactor biosynthesis pathway. The lipoyl cofactor "is synthesized de novo in two committed steps, involving the LipB-catalyzed transfer of an octanoyl chain derived from fatty acid biosynthesis to a lipoyl carrier protein and the LipA-catalyzed insertion of sulfur atoms at C6 and C8 of the octanoyl chain" ([PMID: 26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/)). The octanoyl precursor is drawn from **type II fatty-acid biosynthesis (octanoyl-ACP)**, transferred by the octanoyltransferase LipB onto a lysine of a lipoyl carrier protein, and then sulfur-inserted by LipA.

Critically, LipA does not act on free octanoic acid but on the **protein-bound octanoyl substrate**. Studies of the *M. tuberculosis* ortholog showed that LipA "forms a complex with the H protein of the glycine cleavage system and that the strength of association is dependent on the presence of S-adenosyl-L-methionine" ([PMID: 26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/)), demonstrating a direct, SAM-dependent physical engagement of the lipoyl carrier protein substrate. The pathway is cytoplasmic and ultimately lipoylates the E2 subunits of pyruvate dehydrogenase, 2-oxoglutarate dehydrogenase, and branched-chain 2-oxoacid dehydrogenase, as well as the glycine cleavage H-protein — all soluble cytoplasmic multienzyme components. In γ-proteobacteria such as *Shewanella*, the *lipB* and *lipA* genes are "organized into an operon lipBA" and are regulated by cAMP-CRP ([PMID: 25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/)), providing the genomic and regulatory context for the pathway.

### Finding 4 — Q88DM5 shares 65% identity with the biochemically characterized E. coli LipA

Because no direct biochemistry has been performed on the *P. putida* enzyme, the strength of the functional transfer rests on sequence orthology. A global (Needleman-Wunsch) alignment of the 338-residue Q88DM5 against characterized orthologs gave **65.3% identity to *E. coli* LipA** (P60716; 321 aa; 207/317 aligned positions) and 29.9% identity to *M. tuberculosis* LipA. The high identity to *E. coli* LipA spans the catalytic core, and both catalytic Fe-S motifs (radical-SAM CX₃CX₂C and auxiliary CX₄CX₅C) are present in Q88DM5. This level of identity to a rigorously characterized ortholog places the functional assignment on firm footing — well above the ~30–40% identity threshold generally considered sufficient for confident transfer of enzymatic function within a conserved family.

| Ortholog | Organism | Length (aa) | % identity to Q88DM5 | Characterization status |
|---|---|---|---|---|
| P60716 (LipA) | *E. coli* | 321 | 65.3% | Extensively biochemically characterized |
| LipA | *M. tuberculosis* | 429 | 29.9% | Crystallographically characterized |
| **Q88DM5 (LipA)** | ***P. putida* KT2440** | **338** | **—** | **Annotated by orthology (this report)** |

### Finding 5 — In P. putida KT2440, lipA (PP_4800) is contiguous with lipB octanoyltransferase (PP_4801), forming a lipBA arrangement

Organism-specific genomic context reinforces the functional assignment. KEGG genome annotation places **PP_4801 = octanoyltransferase LipB** (K03801, EC 2.3.1.181) at complement(5464467..5465117) and **PP_4800 = lipoyl synthase LipA** (K03644, EC 2.8.1.8) at complement(5463448..5464464) — on the **same strand** and adjacent, overlapping by 3 bp (lipB ends at 5464467, lipA starts at 5464464). Thus *lipB* directly precedes *lipA* in the direction of transcription. Both genes are assigned to KEGG pathway ppu00785 "Lipoic acid metabolism." The other flanking gene, PP_4799, is an unrelated muramoyltetrapeptide carboxypeptidase.

This tandem *lipBA* organization exactly parallels the conserved *lipBA* operon documented in other γ-proteobacteria, where "the two genes (lipB and lipA) encoding lipoic acid synthesis pathway were proved to be organized into an operon lipBA in Shewanella" ([PMID: 25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/)). The physical pairing of the enzyme catalyzing octanoyl transfer with the enzyme catalyzing subsequent sulfur insertion is strong contextual evidence that PP_4800 functions in *de novo* lipoylation together with its neighbor.

### Finding 6 — Q88DM5 conserves the catalytically essential RSSY motif, including the auxiliary-cluster serine ligand

Beyond the two cysteine-rich cluster motifs, LipA requires a **conserved C-terminal RSSY motif** for catalysis. Pairwise alignment of Q88DM5 to *E. coli* LipA shows this region is essentially identical: *P. putida* "...GPLV**RSSY**HADQQAH..." versus *E. coli* "...GPFV**RSSY**HADLQAK...". The motif aligns exactly, mapping *E. coli* R306-S307-S308-Y309 to *P. putida* **R322-S323-S324-Y325**.

The functional importance of this motif is well established. In *E. coli* and *M. tuberculosis* LipA, the arginine and the second serine of the motif are absolutely required for lipoyl-cofactor formation, with the serine serving as the **fourth (serine) ligand of the sacrificial auxiliary [4Fe-4S] cluster** — the same serine seen to dissociate during sulfur transfer in the crystallographic studies. As shown for the motif: "one serine residue (Ser308 in Escherichia coli) in a highly conserved R306,S,S308,Y motif in the C-terminal region of the protein... Arg306 and Ser308 are absolutely required for LipCo formation" ([PMID: 42244760](https://pubmed.ncbi.nlm.nih.gov/42244760/)). The complete conservation of this motif in Q88DM5 — including S324, the auxiliary-cluster serine ligand equivalent to *E. coli* Ser308 — confirms that the *P. putida* enzyme possesses the full catalytic machinery for the sacrificial-cluster sulfur-insertion mechanism.

---

## Mechanistic Model / Interpretation

Integrating the six findings yields a coherent, high-confidence mechanistic model for Q88DM5 in *P. putida* KT2440:

**Pathway position.** LipA is the terminal enzyme of the two-step *de novo* lipoic-acid biosynthesis pathway, which draws its precursor from fatty-acid synthesis:

```
Type II fatty-acid synthesis
        │  (octanoyl-ACP)
        ▼
   LipB (PP_4801, octanoyltransferase, EC 2.3.1.181)
        │  transfers octanoyl onto Lys of lipoyl carrier protein
        ▼
   (N6-octanoyl)-lysyl-[carrier protein]        ← LipA substrate
        │
        ▼
   LipA (PP_4800, lipoyl synthase, EC 2.8.1.8)  ← THIS GENE
        │  inserts S at C6 and C8 (2× SAM, aux-cluster S donor)
        ▼
   (N6-lipoyl)-lysyl-[carrier protein]          ← mature lipoyl cofactor
        │
        ▼
   Functional E2 (PDH, OGDH, BCKDH) + GcvH H-protein
```

**Catalytic mechanism (per turnover of one sulfur).** The radical-SAM [4Fe-4S] cluster (ligated by C110/C114/C117 of the CTRRCPFC motif) binds SAM and, upon reduction, cleaves it to L-methionine plus a 5′-deoxyadenosyl radical. This radical abstracts a hydrogen from C6 (then, in a second SAM-consuming cycle, from C8) of the octanoyl chain. The resulting substrate carbon radical attacks a bridging sulfide of the auxiliary [4Fe-4S] cluster (ligated by C84/C89/C95 and the serine S324). Sulfur–carbon bond formation proceeds with loss of the serine-ligated iron and partial disassembly of the auxiliary cluster to a [3Fe-4S] species — consistent with the cross-linked intermediate detected by Mössbauer spectroscopy. After both C6 and C8 sulfurs are installed and the dithiolane ring closes, the spent auxiliary cluster is regenerated by iron-sulfur carrier proteins (NfuA/IscU homologs), returning LipA to a catalytically competent two-cluster state.

**Substrate specificity.** LipA does not act on free fatty acids. Its substrate is the octanoyl group amide-linked to a specific lysine of a lipoyl carrier protein (in *P. putida*, the E2 domains of 2-oxoacid dehydrogenases and the glycine cleavage H-protein). Substrate engagement is SAM-dependent, and the enzyme forms a transient covalent cross-link to the carrier protein through the auxiliary cluster during turnover.

**Localization.** The entire pathway — fatty-acid synthesis, LipB octanoyl transfer, LipA sulfur insertion, and the lipoylated target complexes — is **cytoplasmic**. There is no signal peptide, transmembrane domain, or evidence for secretion; LipA carries out its function as a soluble cytoplasmic enzyme.

**Biological role.** By producing the lipoyl cofactor, LipA is essential for the function of the central-metabolism 2-oxoacid dehydrogenase complexes (pyruvate → acetyl-CoA; 2-oxoglutarate → succinyl-CoA; branched-chain amino-acid catabolism) and the glycine cleavage system. In *P. putida*, an organism with a strongly oxidative, TCA-cycle-centered metabolism well suited to its role as a soil bacterium and biotechnological chassis, lipoylation is expected to be important for aerobic respiratory metabolism — consistent with the broad correlation between OADHC lipoylation capacity and aerobiosis observed across microbial genomes ([PMID: 24489835](https://pubmed.ncbi.nlm.nih.gov/24489835/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this annotation |
|---|---|---|
| [27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/) | *Crystallographic snapshots of sulfur insertion by lipoyl synthase* | Defines the reaction (C6/C8 sulfur insertion on protein-bound octanoyl); direct structural proof that the auxiliary cluster serine dissociates and a cluster sulfur becomes covalently bonded to substrate C6 |
| [26841001](https://pubmed.ncbi.nlm.nih.gov/26841001/) | *Characterization of Lipoyl Synthase from M. tuberculosis* | Establishes the two-step LipB→LipA de novo pathway; shows SAM-dependent LipA–GcvH (H-protein) complex formation |
| [15362861](https://pubmed.ncbi.nlm.nih.gov/15362861/) | *E. coli lipoyl synthase binds two distinct [4Fe-4S] clusters* | Establishes the turnover-relevant two-cluster architecture shared by the family |
| [34292556](https://pubmed.ncbi.nlm.nih.gov/34292556/) | *Biochemical Approaches to Probe the Auxiliary Fe-S Cluster (M. tuberculosis)* | Explains auxiliary cluster as sacrificial sulfur source and in vivo regeneration by NfuA/IscU |
| [24901788](https://pubmed.ncbi.nlm.nih.gov/24901788/) | *Catalytically and kinetically competent enzyme-substrate cross-linked intermediate* | Provides biochemical evidence for the covalent cross-linked intermediate through the auxiliary cluster |
| [42244760](https://pubmed.ncbi.nlm.nih.gov/42244760/) | *Amino Acids in the RSSY Motif Control Substrate Binding and Reactivity* | Establishes essentiality of the RSSY motif (Arg306, Ser308) and the auxiliary-cluster serine ligand, conserved as R322/S324 in Q88DM5 |
| [25611823](https://pubmed.ncbi.nlm.nih.gov/25611823/) | *A new regulatory mechanism for bacterial lipoic acid synthesis* | Documents the conserved lipBA operon organization and cAMP-CRP regulation in γ-proteobacteria, paralleling PP_4801-PP_4800 |
| [24489835](https://pubmed.ncbi.nlm.nih.gov/24489835/) | *Comparative genomic analysis of OADHC lipoylation and aerobiosis* | Contextualizes lipoylation as central to aerobic 2-oxoacid dehydrogenase metabolism |
| [21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/) | *Novel two-gene requirement for octanoyltransfer in B. subtilis* | Illustrates pathway variation (LipM/LipL) in Gram-positives; underscores that the E. coli/γ-proteobacterial LipB→LipA model applies to P. putida |

**Consistency of the evidence base.** All primary mechanistic studies (from *E. coli*, *M. tuberculosis*, and human systems) converge on the same reaction, cofactor requirements, and mechanism. No study contradicts the assignment. The primary limitation is that all direct experimental data derive from **orthologs**, not from the *P. putida* enzyme itself; the transfer of function is justified by the high sequence identity (Finding 4), full conservation of catalytic motifs (Findings 1 and 6), and organism-specific genomic context (Finding 5).

---

## Limitations and Knowledge Gaps

1. **No direct P. putida biochemistry.** There is no purified-enzyme kinetic, spectroscopic, or structural characterization of Q88DM5 specifically. The functional annotation is inferred — albeit with high confidence — from orthology and conserved motifs rather than measured in the native protein.

2. **Lipoyl carrier protein partners not experimentally mapped in P. putida.** While the substrate is certainly a lipoyl carrier protein, the specific *P. putida* E2 subunits and the GcvH H-protein that LipA lipoylates have not been individually confirmed by experiment in this organism.

3. **Auxiliary-cluster regeneration machinery not confirmed in P. putida.** The identity of the Fe-S carrier protein(s) (NfuA/IscU homologs) that restore the sacrificed auxiliary cluster in *P. putida* has not been established experimentally.

4. **Operon structure and regulation inferred, not measured.** The *lipBA* tandem arrangement is documented from genome coordinates; transcriptional co-expression and any cAMP-CRP-type regulation in *P. putida* remain to be verified experimentally. It also remains formally untested whether *P. putida* additionally uses an alternative LipM/LipL-type octanoyl-transfer route (as in *B. subtilis*).

5. **Essentiality and salvage not assessed.** Whether *P. putida* can bypass *de novo* synthesis via a lipoate salvage pathway (LplA-type ligase) under lipoate-supplemented conditions, and thus whether *lipA* is conditionally essential, has not been examined here.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic essentiality test.** Construct a *P. putida* KT2440 Δ*lipA* (ΔPP_4800) mutant and test for growth on unsupplemented minimal medium versus medium supplemented with free lipoic acid, to confirm the *de novo* biosynthetic role and probe for salvage capacity.

2. **Complementation assay.** Test whether *P. putida lipA* complements an *E. coli* Δ*lipA* mutant (restoring growth without lipoate supplementation), providing a direct functional demonstration of the orthologous activity.

3. **In vitro reconstitution.** Heterologously express and purify Q88DM5, reconstitute its two [4Fe-4S] clusters anaerobically, and assay sulfur insertion on an (N6-octanoyl)-lysyl carrier-protein or peptide substrate with SAM, measuring lipoyl-cofactor formation and 5′-deoxyadenosine production.

4. **Cluster and motif verification.** Use Mössbauer/EPR spectroscopy and site-directed mutagenesis of the predicted cluster ligands (C84/C89/C95 auxiliary; C110/C114/C117 radical-SAM) and the RSSY serine (S324) to confirm cluster assignments and catalytic essentiality in the *P. putida* enzyme.

5. **Operon and regulation analysis.** Perform RT-PCR/RNA-seq to confirm co-transcription of PP_4801-PP_4800 and map the promoter and any CRP-binding regulatory elements.

6. **Substrate-partner identification.** Use co-purification or cross-linking (exploiting the SAM-dependent covalent intermediate) to identify the specific *P. putida* lipoyl carrier proteins (E2 subunits, GcvH) that serve as LipA substrates in vivo.

---

## Conclusion

The gene *lipA* (PP_4800; UniProt Q88DM5) of *Pseudomonas putida* KT2440 encodes **lipoyl synthase (EC 2.8.1.8)**, a cytoplasmic radical-SAM enzyme that performs the final, committed step of *de novo* lipoic-acid biosynthesis: inserting two sulfur atoms at C6 and C8 of a protein-bound octanoyl chain to form the mature lipoyl cofactor. It uses two [4Fe-4S] clusters — a radical-SAM cluster that generates deoxyadenosyl radicals from SAM, and an auxiliary cluster that is sacrificed as the sulfur donor and regenerated in vivo. Although the assignment rests on orthology rather than direct *P. putida* biochemistry, it is strongly supported by 65% identity to the characterized *E. coli* enzyme, complete conservation of all catalytic elements (both Fe-S cluster motifs and the essential RSSY motif with auxiliary-cluster serine S324), and organism-specific genomic co-localization with its cognate octanoyltransferase gene *lipB* (PP_4801).


## Artifacts

- [OpenScientist final report](lipA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lipA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27506792
2. PMID:26841001
3. PMID:15362861
4. PMID:34292556
5. PMID:24901788
6. PMID:25611823
7. PMID:42244760
8. PMID:24489835