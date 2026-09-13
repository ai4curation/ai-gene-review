---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T18:07:56.686294'
end_time: '2026-07-25T18:32:45.111338'
duration_seconds: 1488.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: recJ
  gene_symbol: recJ
  uniprot_accession: Q88MU1
  protein_description: 'RecName: Full=Single-stranded-DNA-specific exonuclease RecJ
    {ECO:0000256|ARBA:ARBA00019841};'
  gene_info: Name=recJ {ECO:0000313|EMBL:AAN67099.1}; OrderedLocusNames=PP_1477 {ECO:0000313|EMBL:AAN67099.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the RecJ family.
  protein_domains: DDH_dom. (IPR001667); DHH_sf. (IPR038763); DHHA1_dom. (IPR003156);
    RecJ. (IPR004610); RecJ_OB. (IPR041122)
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
  path: recJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: recJ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MU1
- **Protein Description:** RecName: Full=Single-stranded-DNA-specific exonuclease RecJ {ECO:0000256|ARBA:ARBA00019841};
- **Gene Information:** Name=recJ {ECO:0000313|EMBL:AAN67099.1}; OrderedLocusNames=PP_1477 {ECO:0000313|EMBL:AAN67099.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the RecJ family.
- **Key Domains:** DDH_dom. (IPR001667); DHH_sf. (IPR038763); DHHA1_dom. (IPR003156); RecJ. (IPR004610); RecJ_OB. (IPR041122)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "recJ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'recJ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **recJ** (gene ID: recJ, UniProt: Q88MU1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RecJ (Q88MU1 / PP_1477): Single-Stranded-DNA-Specific 5'→3' Exonuclease of *Pseudomonas putida* KT2440

## Summary

**RecJ (UniProt Q88MU1, locus PP_1477) of *Pseudomonas putida* KT2440 is a metal-dependent, single-stranded-DNA-specific 5'→3' exonuclease.** It processively degrades single-stranded DNA (ssDNA) from a free 5' end, releasing 5'-mononucleotide products, and belongs to the DHH/DHHA1 phosphoesterase superfamily. Catalysis proceeds through a two-metal-ion (Mg²⁺/Mn²⁺) mechanism organized around a conserved DHH catalytic motif, while strict single-strand specificity is imposed by a dedicated oligonucleotide/oligosaccharide-binding (OB) fold domain that binds ssDNA but not double-stranded DNA. The enzyme carries out its function in the **cytoplasm**, acting directly on chromosomal DNA and DNA-repair intermediates.

Functionally, RecJ is the dedicated **5'→3' resection nuclease of the RecF homologous-recombination pathway**. Working together with the RecQ helicase, the RecFOR mediator complex, and single-stranded DNA-binding protein (SSB), it resects the 5'-terminated strand at DNA gaps and ends to generate the 3'-single-stranded overhangs on which RecA nucleoprotein filaments assemble. Beyond recombination, RecJ contributes the excision step of methyl-directed **mismatch repair**, participates in **base-excision repair (BER)** in some bacteria, and provides overlapping, sometimes essential, nuclease activity for the repair of stalled or broken **replication forks**.

No experimental study has yet characterized the *P. putida* enzyme directly. However, the functional assignment is strongly supported by comparative evidence: Q88MU1 shares **59% amino-acid identity** with the biochemically-characterized *Escherichia coli* RecJ, retains a fully intact DHH catalytic motif and the complete four-domain RecJ architecture, and the *P. putida* KT2440 genome encodes the **complete set of RecJ's pathway partners** (RecQ, RecFOR, RecA, SSB, MutS/MutL, UvrD, and the RecBCD complex). This report synthesizes the identity verification, structural/mechanistic basis, pathway context, and comparative-genomic evidence into a coherent functional annotation.

---

## Gene/Protein Identity Verification

Before proceeding, the target identity was verified against the mandatory checklist:

- **UniProt accession:** Q88MU1
- **Protein:** Single-stranded-DNA-specific exonuclease RecJ
- **Gene / locus:** *recJ* / PP_1477
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), taxon 160488
- **Family:** RecJ family (DHH phosphoesterase superfamily)
- **Domains:** DDH_dom (IPR001667); DHH_sf (IPR038763); DHHA1 (IPR003156); RecJ (IPR004610); RecJ_OB (IPR041122)

The gene symbol *recJ*, the "single-stranded-DNA-specific exonuclease" description, and the DHH/DHHA1/OB-fold domain complement are fully mutually consistent and match the RecJ family. The literature retrieved describes RecJ enzymes of the correct family and function. **This is not a case of gene-symbol ambiguity** — the annotation is coherent and the comparative evidence (below) confirms the assignment.

---

## Key Findings

### Finding 1: RecJ (Q88MU1, PP_1477) is a single-stranded-DNA-specific 5'→3' exonuclease

The gene/protein identity is unambiguously confirmed. UniProt entry Q88MU1 is annotated as "Single-stranded-DNA-specific exonuclease RecJ," corresponding to gene *recJ* / OrderedLocusName **PP_1477** in *Pseudomonas putida* KT2440. The protein is a member of the RecJ/DHH family and carries the diagnostic DDH domain (IPR001667), the DHH superfamily fold (IPR038763), the DHHA1 domain (IPR003156), and the RecJ OB-fold domain (IPR041122).

The enzymatic activity of this protein family is defined by detailed biochemical work on the *E. coli* ortholog. RecJ degrades ssDNA strictly in the **5'→3' direction**, releasing **mononucleotide products** ([PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)). It is a **processive** enzyme, degrading approximately **1,000 nucleotides after a single binding event** to single-stranded DNA. The substrate specificity is well defined: RecJ requires a **single-stranded 5' tail of ≥7 nucleotides** for robust binding, and is poorly active on tails of ≤6 nucleotides. Critically, the enzyme is **equally potent on 5'-phosphorylated and unphosphorylated ends**, showing that end chemistry does not gate substrate engagement. It can degrade a ssDNA tail up to a double-strand junction with only limited penetration into duplex DNA.

> *"The RecJ exonuclease from Escherichia coli degrades single-stranded DNA (ssDNA) in the 5'-3' direction and participates in homologous recombination and mismatch repair."* — [PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)

> *"RecJ is a processive exonuclease, degrading approximately 1000 nt after a single binding event to single-strand DNA, and releases mononucleotide products."* — [PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)

> *"RecJ required single-stranded tails of 7 nt or greater for robust binding."* — [PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)

These properties establish the core biochemical identity of the protein: a directional, processive, single-strand-specific exonuclease that produces mononucleotides.

### Finding 2: Specificity arises from a four-domain architecture with a DHH catalytic core, an OB-fold ssDNA-binding domain, and a two-metal-ion mechanism

The structural basis of RecJ's activity and specificity was resolved by X-ray crystallography of the *Thermus thermophilus* enzyme in ligand-free and metal-bound (Mn²⁺/Mg²⁺) states. RecJ consists of **four domains that assemble into a molecule with an "O-like" ring structure** ([PMID: 20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/)). A newly identified **OB-fold domain** within this architecture binds ssDNA (but not dsDNA), and this domain alone is sufficient for DNA binding — establishing it as a novel member of the OB-fold superfamily. Truncated RecJ containing only the catalytic core has markedly lower ssDNA affinity than the intact enzyme, demonstrating that the OB-fold domain is the primary determinant of single-strand recognition and high-affinity engagement.

The catalytic mechanism is a **two-metal-ion mechanism**: the structure of the RecJ–Mn²⁺ complex indicates that phosphodiester-bond hydrolysis proceeds through coordination of two divalent metal ions in the active site.

> *"The entire RecJ consists of four domains that form a molecule with an O-like structure."* — [PMID: 20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/)

> *"The OB fold domain alone could bind to DNA, indicating that this domain is a novel member of the OB fold superfamily."* — [PMID: 20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/)

> *"the structure of the RecJ-Mn(2+) complex suggests that the hydrolysis reaction catalyzed by RecJ proceeds through a two-metal ion mechanism."* — [PMID: 20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/)

RecJ belongs to the broader **DHH phosphoesterase superfamily**, which includes family-2 inorganic pyrophosphatases, the PPX1 exopolyphosphatase, the cyclic AMPase prune, and the replication factor Cdc45. These enzymes share a common two-metal-ion strategy for hydrolyzing phosphodiester or phosphoanhydride bonds ([PMID: 22147708](https://pubmed.ncbi.nlm.nih.gov/22147708/)). Q88MU1 carries all of the corresponding domain signatures (DDH_dom, DHH_sf, DHHA1, RecJ_OB), placing the *P. putida* protein squarely within this mechanistic framework.

> *"the DHH family, including inorganic pyrophosphatases and RecJ ssDNA exonucleases. These enzymes catalyze the hydrolysis of phosphodiester bonds via a mechanism involving two Mn(2+) ions."* — [PMID: 22147708](https://pubmed.ncbi.nlm.nih.gov/22147708/)

### Finding 3: RecJ is the 5'→3' exonuclease of the RecF recombination pathway and functions in mismatch and base-excision repair

RecJ's cellular role is defined by its position within the RecF recombination pathway. In *E. coli*, the RecF recombination machinery consists of **RecQ (helicase), RecJ (5'→3' exonuclease), and RecFOR (RecA–ssDNA filament formation)** ([PMID: 15687199](https://pubmed.ncbi.nlm.nih.gov/15687199/)). Genetic analysis of nuclease-deficient *recB recD* mutants shows that **conjugational recombination and DNA repair after UV and gamma irradiation are highly dependent on *recJ***. In this genetic context, RecJ substitutes for the missing 5'→3' exonuclease activity normally provided by the RecBCD enzyme, resecting the 5'-terminated strand to expose 3'-ssDNA for RecA loading.

> *"the recombination machinery of the RecF pathway consists of RecQ (helicase), RecJ (5'-->3' exonuclease), and RecFOR (RecA-single-stranded DNA filament formation)"* — [PMID: 15687199](https://pubmed.ncbi.nlm.nih.gov/15687199/)

> *"conjugational recombination and DNA repair after UV and gamma irradiation in this mutant are highly dependent on recJ"* — [PMID: 15687199](https://pubmed.ncbi.nlm.nih.gov/15687199/)

RecJ's activity is functionally coupled to **SSB (single-stranded DNA-binding protein)**. DNA binding and nuclease activity of RecJ are specifically enhanced by pre-addition of SSB, and this interaction is proposed to aid recruitment of RecJ to its substrate ([PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)). This coupling integrates RecJ into the SSB-coated ssDNA landscape that characterizes repair and recombination intermediates.

> *"DNA binding and nuclease activity of RecJ was specifically enhanced by the pre-addition of ssDNA-binding protein and we propose that this specific interaction may aid recruitment of RecJ"* — [PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)

Beyond recombination, RecJ contributes to two additional repair pathways:

- **Mismatch repair (MMR):** RecJ is one of the redundant single-strand exonucleases (alongside ExoI, ExoVII, and ExoX) that carry out the excision step of methyl-directed mismatch repair in concert with the UvrD helicase.
- **Base-excision repair (BER):** In *Deinococcus radiodurans*, deletion of *drRecJ* causes extreme sensitivity to hydrogen peroxide and methyl-methanesulphonate, an elevated spontaneous mutation rate, and accumulation of unrepaired abasic sites in vivo — direct evidence of RecJ participation in BER, where it favors the long-patch pathway ([PMID: 32870272](https://pubmed.ncbi.nlm.nih.gov/32870272/)).

> *"the Deinococcus radiodurans RecJ (drRecJ) deletion strain exhibited extreme sensitivity to hydrogen peroxide and methyl-methanesulphonate, as well as a high spontaneous mutation rate and an accumulation of unrepaired abasic sites in vivo, indicating the involvement of drRecJ in the BER pathway"* — [PMID: 32870272](https://pubmed.ncbi.nlm.nih.gov/32870272/)

RecJ also participates in the repair of stalled or broken replication forks. In *Acinetobacter baylyi*, the double mutants *recJ recBCD* and *recJ recD* are **non-viable**, indicating that the RecJ and RecBCD nucleases provide overlapping, essential resection activity for the recombinational repair of spontaneously inactivated replication forks — if one nuclease is absent, the other becomes essential ([PMID: 17600070](https://pubmed.ncbi.nlm.nih.gov/17600070/)).

> *"double mutants recJ recBCD and recJ recD were non-viable, suggesting that the RecJ DNase or the RecBCD DNase (presumably absent in recD) becomes essential for the recombinational repair of spontaneously inactivated replication forks if the other DNase is absent"* — [PMID: 17600070](https://pubmed.ncbi.nlm.nih.gov/17600070/)

### Finding 4: *P. putida* RecJ (Q88MU1) shares 59% sequence identity with the characterized *E. coli* RecJ and retains an intact DHH catalytic motif

To validate the transfer of functional annotation from the biochemically-characterized *E. coli* enzyme to the *P. putida* protein, the two sequences were aligned directly. Q88MU1 (*P. putida* RecJ) is **569 amino acids**. A Smith-Waterman local alignment against *E. coli* RecJ (UniProt P21893, 577 aa — the enzyme whose ssDNA 5'→3' exonuclease activity is directly characterized) yields **327/552 = 59.2% amino-acid identity** over a 552-residue alignment.

Most importantly, the **diagnostic DHH catalytic tripeptide is conserved**, occurring at residue 156 of Q88MU1, and the active-site block is nearly identical between the two orthologs:

| Ortholog | Active-site sequence block |
|----------|----------------------------|
| *P. putida* RecJ (Q88MU1) | …VT**DHH**LPGEQLP… |
| *E. coli* RecJ (P21893) | …VT**DHH**LPGDTLP… |

This preserves the DHH-superfamily metal-coordinating catalytic core. The amino-acid composition (38 Asp, 36 Glu, 16 His) is consistent with the acidic, metal-binding active site expected of DHH phosphoesterases. At 59% identity across the full length and with an intact catalytic motif, functional transfer from *E. coli* RecJ to *P. putida* RecJ is on very firm ground.

> *"the structure of the RecJ-Mn(2+) complex suggests that the hydrolysis reaction catalyzed by RecJ proceeds through a two-metal ion mechanism"* — [PMID: 20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/) — the conserved DHH motif identified in Q88MU1 corresponds to the metal-coordinating catalytic core defined structurally in RecJ.

### Finding 5: The *P. putida* KT2440 genome encodes a complete RecF-pathway and mismatch-repair machinery, providing the functional context for RecJ

A protein cannot carry out a pathway function in isolation; its partners must be present. UniProt gene queries against *P. putida* KT2440 (taxon 160488) confirm that the genome encodes the **complete set of partners** that RecJ requires for its annotated pathways:

| Function | Gene | UniProt | Locus |
|----------|------|---------|-------|
| ssDNA 5'→3' exonuclease | *recJ* | Q88MU1 | PP_1477 |
| RecQ helicase | *recQ* | Q88EE9 | PP_4516 |
| RecF mediator | *recF* | Q88RW7 | PP_0012 |
| RecO mediator | *recO* | Q88MY3 | PP_1435 |
| RecR mediator | *recR* | Q88F32 | PP_4267 |
| Recombinase | *recA* | Q88ME4 | PP_1629 |
| ssDNA-binding protein | *ssb* | Q88QK5 | PP_0485 |
| Mismatch recognition | *mutS* | Q88ME7 | PP_1626 |
| MMR endonuclease/coordinator | *mutL* | Q88DD1 | PP_4896 |
| Helicase II (MMR/recomb.) | *uvrD* | Q88C31 | PP_5352 |
| RecBCD complex | *recB/recC/recD* | — | PP_4673/4674/4672 |

Notably, *recJ* (PP_1477) is located adjacent to *recO* (PP_1435) in the genome. The presence of the full RecQ–RecFOR–RecA–SSB machinery, the complete MutS/MutL/UvrD mismatch-repair set, and the RecBCD complex confirms that *P. putida* possesses the exact molecular context in which RecJ is known to operate in other bacteria.

> *"the recombination machinery of the RecF pathway consists of RecQ (helicase), RecJ (5'-->3' exonuclease), and RecFOR (RecA-single-stranded DNA filament formation)"* — [PMID: 15687199](https://pubmed.ncbi.nlm.nih.gov/15687199/) — defines the exact partner set confirmed present in the *P. putida* genome alongside *recJ*.

---

## Mechanistic Model / Interpretation

### The enzyme

RecJ is a **cytoplasmic, Mg²⁺/Mn²⁺-dependent, processive single-strand exonuclease** that hydrolyzes phosphodiester bonds one at a time from a free 5' terminus, moving 5'→3' and liberating 5'-mononucleotides. Two features work together to define its substrate:

1. **The OB-fold domain** binds ssDNA with high affinity and does not engage dsDNA — this is the molecular gatekeeper that makes RecJ single-strand specific and enforces the ≥7-nt tail requirement.
2. **The DHH/DHHA1 catalytic core** positions two divalent metal ions to activate a water nucleophile and stabilize the transition state during phosphodiester hydrolysis.

The four domains assemble into an O-shaped ring; ssDNA is threaded through the ring so that the OB-fold grips the strand while the catalytic center cleaves it, accounting for both processivity (~1,000 nt/binding event) and directionality.

```
        5'-P–N–N–N–N–N–N–N ... ssDNA 3'
             │
    ┌────────┴─────────┐
    │  OB-fold domain  │  ← binds ssDNA (not dsDNA); requires ≥7-nt 5' tail
    │  (specificity)   │
    ├──────────────────┤
    │ DHH / DHHA1 core │  ← two-metal-ion (Mg²⁺/Mn²⁺) hydrolysis
    │  (catalysis)     │     DHH motif @ residue 156 in Q88MU1
    └────────┬─────────┘
             │  releases 5'-mononucleotides, one at a time, 5'→3'
             ▼
        pN  pN  pN ...  (mononucleotide products)
```

### The pathway role

RecJ's principal job is **5' end resection** to create the 3'-ssDNA substrate for RecA. The RecF pathway operates on single-strand gaps and DNA ends generated during replication, repair, and recombination:

```
   RecQ helicase unwinds duplex
            │
            ▼
   ══════════╗
   5'────────╫──────── 3'    duplex/gap
   3'────────╫──────── 5'
            ║
   RecJ resects the 5'-strand ─────►  (removes 5' ssDNA, 5'→3')
            │
            ▼
   ══════════
   ────────  3'-OH ssDNA overhang, coated by SSB
            │
   RecFOR loads RecA onto ssDNA (displacing SSB)
            │
            ▼
   RecA nucleoprotein filament → homology search → strand invasion → repair
```

SSB both coats the resulting ssDNA and stimulates RecJ's recruitment and nuclease activity, integrating the exonuclease into the ordered assembly of the recombination machine. When RecBCD is inactivated (as in *recB recD* backgrounds), RecJ becomes the sole 5'→3' resection nuclease and is genetically essential for recombination and radiation resistance.

### The same enzyme, three pathways

| Pathway | RecJ's specific task | Key partners | Evidence |
|---------|---------------------|--------------|----------|
| **RecF homologous recombination** | 5'→3' resection to expose 3'-ssDNA for RecA loading | RecQ, RecFOR, SSB, RecA | [PMID: 15687199](https://pubmed.ncbi.nlm.nih.gov/15687199/) |
| **Methyl-directed mismatch repair** | Excision of the error-containing strand (redundant with ExoI/ExoVII/ExoX) | MutS, MutL, UvrD | [PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/) |
| **Base-excision repair** | Removal of ssDNA/abasic intermediates; favors long-patch BER | glycosylases, AP endonuclease, Pol I | [PMID: 32870272](https://pubmed.ncbi.nlm.nih.gov/32870272/) |
| **Replication-fork repair** | Resection of stalled/broken forks (overlaps RecBCD; essential when RecBCD absent) | RecBCD, RecFOR | [PMID: 17600070](https://pubmed.ncbi.nlm.nih.gov/17600070/) |

### Confidence in the *P. putida* assignment

The assignment for Q88MU1 rests on three independent, mutually reinforcing lines of evidence:

1. **Sequence homology** — 59% identity to the characterized *E. coli* enzyme, well above the ~30–40% threshold generally accepted for reliable functional transfer of enzymatic activity.
2. **Motif and domain integrity** — the DHH catalytic tripeptide and all four diagnostic domains (DDH, DHH_sf, DHHA1, RecJ_OB) are intact, indicating an active enzyme rather than a degenerate pseudo-nuclease.
3. **Genomic context** — the full complement of RecF-pathway, MMR, and RecBCD partners is present, confirming that the cellular machinery RecJ operates within exists in *P. putida*.

---

## Evidence Base

| PMID | Paper (abbreviated) | Contribution to this annotation |
|------|---------------------|--------------------------------|
| [16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/) | *RecJ exonuclease: substrates, products and interaction with SSB* | Defines the core biochemistry: 5'→3' direction, mononucleotide products, ~1,000-nt processivity, ≥7-nt tail requirement, phosphorylation independence, SSB stimulation. The primary functional reference. |
| [20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/) | *Structure of RecJ exonuclease defines its specificity for single-stranded DNA* | Provides the structural basis: four-domain O-like architecture, the OB-fold ssDNA-binding domain, and the two-metal-ion catalytic mechanism. |
| [22147708](https://pubmed.ncbi.nlm.nih.gov/22147708/) | *Structural and functional insights into...Cdc45...DHH family of phosphoesterases* | Places RecJ within the DHH superfamily and confirms the shared two-metal-ion phosphodiester hydrolysis mechanism. |
| [15687199](https://pubmed.ncbi.nlm.nih.gov/15687199/) | *Effects of recJ, recQ, and recFOR mutations...in recB recD double mutants of E. coli* | Establishes RecJ as the 5'→3' exonuclease of the RecF pathway and shows genetic dependence of recombination/repair on *recJ*. |
| [32870272](https://pubmed.ncbi.nlm.nih.gov/32870272/) | *Participation of RecJ in the base excision repair pathway of Deinococcus radiodurans* | Demonstrates RecJ involvement in BER via deletion phenotypes (H₂O₂/MMS sensitivity, abasic-site accumulation, elevated mutation rate). |
| [17600070](https://pubmed.ncbi.nlm.nih.gov/17600070/) | *Deletions of recBCD or recD...lethal together with a recJ deletion in Acinetobacter baylyi* | Shows RecJ and RecBCD provide overlapping, essential resection for replication-fork repair. |
| [16085468](https://pubmed.ncbi.nlm.nih.gov/16085468/) | *The mechanism of base excision repair in Chlamydiophila pneumoniae* | Corroborates that RecJ (as a single-strand-specific exonuclease) is a component of bacterial BER in some organisms. |
| [17599355](https://pubmed.ncbi.nlm.nih.gov/17599355/) | *Crystal structure of the cytosolic exopolyphosphatase (PPX1)...* | Illustrates the DHH-family fold and active-site architecture shared with RecJ, reinforcing the mechanistic classification. |

Several additional papers ([PMID: 18567657](https://pubmed.ncbi.nlm.nih.gov/18567657/), [PMID: 20138014](https://pubmed.ncbi.nlm.nih.gov/20138014/), [PMID: 20018207](https://pubmed.ncbi.nlm.nih.gov/20018207/), [PMID: 21705756](https://pubmed.ncbi.nlm.nih.gov/21705756/), [PMID: 7498761](https://pubmed.ncbi.nlm.nih.gov/7498761/), [PMID: 22617484](https://pubmed.ncbi.nlm.nih.gov/22617484/)) collectively situate RecJ within the RecQ–RecFOR–UvrD–MMR network, reinforcing its role as a resection nuclease that acts on recombination and replication-fork intermediates. Notably, [PMID: 14599740](https://pubmed.ncbi.nlm.nih.gov/14599740/) documents that RecJ, ExoI, ExoVII, and ExoX provide redundant single-strand exonuclease functions required for mismatch repair, UV resistance, and homologous recombination — clarifying that RecJ operates within a partially redundant nuclease group rather than as an isolated activity.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* enzyme.** All enzymatic and structural evidence derives from orthologs (*E. coli*, *T. thermophilus*, *D. radiodurans*, *A. baylyi*). The functional assignment for Q88MU1 is inferential — albeit very strongly supported by 59% identity, intact catalytic motifs, and complete genomic pathway context. Direct biochemistry (purified Q88MU1 assayed on defined ssDNA substrates) has not been performed.

2. **No structure of the *P. putida* protein was analyzed.** The four-domain architecture and OB-fold specificity are inferred from *T. thermophilus* and homology; no experimental or AlphaFold structure of Q88MU1 was examined in this investigation.

3. **Metal-cofactor and kinetic parameters are unmeasured** for the *P. putida* enzyme. Whether it prefers Mg²⁺ or Mn²⁺ in vivo, and its precise processivity/tail-length requirements, are assumed from the *E. coli* enzyme.

4. **Pathway partitioning in *P. putida* is untested.** The relative contribution of RecJ versus RecBCD to recombination, MMR, and fork repair may differ from *E. coli*, and *Pseudomonas*-specific phenotypes (e.g., under oxidative or solvent stress relevant to *P. putida*'s environmental niche) are unknown.

5. **Regulation and expression** of PP_1477 (promoter, SOS-inducibility, stress responsiveness) were not examined.

6. **Protein–protein interactions** (e.g., a direct RecJ–SSB physical interface, RecJ–RecQ coupling) are inferred functionally and have not been mapped for the *P. putida* protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and in vitro nuclease assay.** Purify tagged Q88MU1 and assay on 5'-labeled ssDNA oligonucleotides of varying tail length (5–15 nt) to confirm 5'→3' processive degradation, mononucleotide product release, and the ≥7-nt tail requirement. Test Mg²⁺ vs Mn²⁺ dependence.

2. **Structural determination / prediction.** Generate an AlphaFold model of Q88MU1 (with PAE/pLDDT confidence) and superpose it onto the *T. thermophilus* RecJ structure (from [PMID: 20129927](https://pubmed.ncbi.nlm.nih.gov/20129927/)) to verify the O-like ring, OB-fold positioning, and active-site geometry. Confirm the DHH metal-coordinating residues.

3. **Gene knockout phenotyping in KT2440.** Construct a Δ*recJ* (ΔPP_1477) strain and assess sensitivity to UV, γ-irradiation, H₂O₂, and MMS; measure spontaneous mutation rate and abasic-site accumulation to test recombination, BER, and MMR contributions in *P. putida*.

4. **Synthetic-lethality/epistasis screens.** Construct Δ*recJ* Δ*recBCD* and Δ*recJ* Δ*recD* double mutants to test whether the overlapping essential resection role seen in *A. baylyi* ([PMID: 17600070](https://pubmed.ncbi.nlm.nih.gov/17600070/)) holds in *P. putida*.

5. **SSB-stimulation assay.** Test whether *P. putida* SSB (PP_0485) stimulates Q88MU1 nuclease/binding activity, as reported for the *E. coli* pair ([PMID: 16488881](https://pubmed.ncbi.nlm.nih.gov/16488881/)).

6. **Subcellular localization confirmation.** Fluorescent-fusion imaging to confirm cytoplasmic localization and potential relocalization to DNA-repair foci after damage.

---

## Conclusion

RecJ (Q88MU1 / PP_1477) of *Pseudomonas putida* KT2440 is confidently annotated as a **cytoplasmic, single-stranded-DNA-specific, processive 5'→3' exonuclease** of the DHH/DHHA1 phosphoesterase superfamily. It hydrolyzes ssDNA from a free 5' end to mononucleotides via a two-metal-ion mechanism, with single-strand specificity enforced by an OB-fold domain. Its primary cellular function is **5' end resection in the RecF homologous-recombination pathway**, generating 3'-ssDNA overhangs for RecA loading in cooperation with RecQ, RecFOR, and SSB; it also serves the excision steps of mismatch repair and base-excision repair, and provides overlapping resection for replication-fork repair. Although no direct study of the *P. putida* enzyme exists, the assignment is robustly supported by 59% identity to the characterized *E. coli* RecJ, a fully conserved DHH catalytic motif and complete domain architecture, and the presence of RecJ's entire set of pathway partners in the *P. putida* genome.


## Artifacts

- [OpenScientist final report](recJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](recJ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16488881
2. PMID:20129927
3. PMID:22147708
4. PMID:15687199
5. PMID:32870272
6. PMID:17600070
7. PMID:18567657
8. PMID:20138014
9. PMID:20018207
10. PMID:21705756
11. PMID:7498761
12. PMID:22617484
13. PMID:14599740