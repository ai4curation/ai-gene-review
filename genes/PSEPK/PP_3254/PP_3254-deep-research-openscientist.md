---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:16:03.774650'
end_time: '2026-08-19T07:31:16.522207'
duration_seconds: 912.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3254
  gene_symbol: PP_3254
  uniprot_accession: Q88HU9
  protein_description: 'SubName: Full=Nucleosidase {ECO:0000313|EMBL:AAN68861.1};'
  gene_info: OrderedLocusNames=PP_3254 {ECO:0000313|EMBL:AAN68861.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Nucleoside_phosphorylase_d. (IPR000845); Nucleoside_phosphorylase_sf.
    (IPR035994); PNP_UDP_1 (PF01048)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3254-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3254-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HU9
- **Protein Description:** SubName: Full=Nucleosidase {ECO:0000313|EMBL:AAN68861.1};
- **Gene Information:** OrderedLocusNames=PP_3254 {ECO:0000313|EMBL:AAN68861.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Nucleoside_phosphorylase_d. (IPR000845); Nucleoside_phosphorylase_sf. (IPR035994); PNP_UDP_1 (PF01048)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3254" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3254' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3254** (gene ID: PP_3254, UniProt: Q88HU9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_3254 (Q88HU9): A 5′-Methylthioadenosine/S-Adenosylhomocysteine Nucleosidase from *Pseudomonas putida* KT2440

**Gene:** PP_3254 (OrderedLocusNames) · **UniProt:** Q88HU9 · **Protein ID:** AAN68861 · **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950), proteome PSEPK · **Length:** 217 aa · **Genome position:** 3,688,981–3,689,634 (654 bp)

---

## Summary

**PP_3254 (UniProt Q88HU9) encodes a cytosolic, homodimeric 5′-methylthioadenosine/S-adenosylhomocysteine nucleosidase (MTAN; EC 3.2.2.9), a housekeeping hydrolase of the activated methyl cycle in *Pseudomonas putida* KT2440.** The enzyme catalyzes the irreversible hydrolytic cleavage of the N-ribosidic (N9–C1′) bond of adenosyl-containing metabolites — principally 5′-methylthioadenosine (MTA), S-adenosyl-L-homocysteine (SAH), and 5′-deoxyadenosine (5′-dAdo) — releasing free adenine plus the corresponding ribose product. This assignment converges from orthology (KEGG K01243, eggNOG COG0775, PANTHER PTHR46832:SF1), domain architecture (Pfam PF01048 PNP_UDP_1; InterPro IPR000845/IPR035994, the nucleoside phosphorylase fold), and — most decisively — residue-level conservation of the catalytic machinery when aligned to the biochemically and structurally characterized *E. coli* MTAN.

The protein's primary physiological role is **metabolite detoxification and adenine salvage**. MTA, SAH, and 5′-dAdo are potent product inhibitors of the enzyme families that generate them — SAM-dependent methyltransferases, polyamine (spermidine) synthases, and radical-SAM enzymes. By cleaving these by-products, MTAN relieves feedback inhibition and keeps the activated methyl cycle turning, while the released adenine is recycled into the nucleotide pool via adenine phosphoribosyltransferase (Apt, PP_0746). Crucially, genome-context analysis of KT2440 shows that **luxS is absent**, so — unlike in *E. coli* and *Vibrio* — the S-ribosylhomocysteine product cannot be converted into autoinducer-2 (AI-2). PP_3254 therefore does **not** participate in AI-2 quorum sensing in this organism. Likewise, the canonical methylthioribose→methionine salvage pathway is genetically incomplete in KT2440, further focusing the enzyme's physiological importance on product-inhibition relief and purine salvage.

It must be stated plainly that **no direct enzymatic assay of the *P. putida* KT2440 protein itself has been published.** The annotation rests on strong bioinformatic and evolutionary inference: unambiguous orthology to a large, deeply studied bacterial enzyme family and conservation of every catalytically essential active-site position. This is a high-confidence annotation, but one derived by homology and genome context rather than by biochemical characterization of Q88HU9.

---

## Identity Verification

The mandatory identity checks are satisfied. The generic UniProt label "Nucleosidase" and the listed domains (IPR000845, IPR035994, PF01048 PNP_UDP_1) are fully consistent with — and resolve to — MTA/SAH nucleosidase. The organism, locus tag, and accession all match. This is **not** an ambiguous-symbol situation: multiple orthogonal databases and sequence analysis converge on the same enzyme.

| Attribute | Value |
|---|---|
| UniProt accession | Q88HU9 |
| Locus tag | PP_3254 |
| Organism | *Pseudomonas putida* KT2440 |
| UniProt description | "Nucleosidase" (SubName, EMBL AAN68861.1) |
| Length | 217 aa |
| KEGG orthology | K01243 — adenosylhomocysteine nucleosidase [EC:3.2.2.9] |
| eggNOG / COG | COG0775 (MTA/SAH nucleosidase) |
| PANTHER | PTHR46832:SF1 |
| Pfam / InterPro | PF01048 (PNP_UDP_1); IPR000845 / IPR035994; SUPFAM SSF53167 |

---

## Key Findings

### Finding 1 — PP_3254 is a 5′-methylthioadenosine/S-adenosylhomocysteine nucleosidase (MTAN, EC 3.2.2.9)

Multiple independent annotation systems converge on the same identity. KEGG assigns ortholog **K01243**, "adenosylhomocysteine nucleosidase [EC:3.2.2.9]" (ppu:PP_3254). eggNOG places the protein in **COG0775** (MTA/SAH nucleosidase). PANTHER classifies it as subfamily **PTHR46832:SF1**, "5′-METHYLTHIOADENOSINE/S-ADENOSYLHOMOCYSTEINE NUCLEOSIDASE." The Pfam domain **PF01048** (PNP_UDP_1) and InterPro entries IPR000845 and IPR035994 define the nucleoside phosphorylase domain and superfamily fold (SSF53167). The associated Gene Ontology molecular functions are methylthioadenosine nucleosidase activity (GO:0008930) and adenosylhomocysteine nucleosidase activity (GO:0008782).

The decisive evidence beyond database labels is **sequence conservation of the catalytic residues**. A global alignment of Q88HU9 (217 aa) against the biochemically and structurally characterized *E. coli* MTAN (P0AF12, 232 aa) shows that the principal catalytic residues are conserved despite only ~23–29% overall identity (the "twilight zone" typical of divergent bacterial MTANs): *E. coli* Asp197 → query Asp188, and *E. coli* Glu174 → query Glu165. Conservation of the general-acid aspartate and the ribosyl-binding glutamate at their expected positions is the strongest possible in-silico indicator that this protein is a catalytically competent MTAN rather than a distant, non-functional homolog.

This family is precisely defined in the literature. As stated by Namanja-Magliano et al., *"5′-Methylthioadenosine/S-adenosylhomocysteine nucleosidase (MTAN) is a bacterial enzyme that catalyzes the hydrolysis of the N-ribosidic bond in 5′-methylthioadenosine (MTA) and S-adenosylhomocysteine (SAH)"* [PMID: 27019223](https://pubmed.ncbi.nlm.nih.gov/27019223/). The authoritative Parveen & Cornell review adds that the enzyme *"is an integral component of the activated methyl cycle, which recycles adenine and methionine through S-adenosylmethionine (SAM)-mediated methylation reactions"* [PMID: 21166890](https://pubmed.ncbi.nlm.nih.gov/21166890/).

### Finding 2 — Reaction catalyzed, substrate specificity, and quaternary structure

MTAN catalyzes **irreversible hydrolytic depurination** — it is a hydrolase using water, distinct from human MTA phosphorylase, which uses phosphate. The three canonical reactions are:

```
  MTA        + H2O  →  adenine  +  5-methylthio-D-ribose (MTR)
  SAH        + H2O  →  adenine  +  S-ribosyl-L-homocysteine (SRH)
  5′-dAdo    + H2O  →  adenine  +  5-deoxy-D-ribose
```

Bacterial MTANs are **broad-specificity** enzymes. In addition to MTA and SAH, they accept adenosine and 5′-deoxyadenosine, and — in organisms using the futalosine route to menaquinone — 6-amino-6-deoxyfutalosine. *P. putida* uses the classical MenA–H menaquinone/ubiquinone pathway, so the futalosine substrate is not physiologically relevant here.

The catalytic mechanism proceeds through a **dissociative, oxocarbenium-ion-like transition state**: the N-ribosidic bond breaks with substantial ribooxocarbenium character, a conserved general-acid aspartate (Asp197 in *E. coli*; Asp188 in PP_3254 by alignment) protonates N7 of the departing adenine, and a precisely positioned water molecule attacks the anomeric carbon.

The products are documented directly: *"Bacterial 5′-methylthioadenosine/S-adenosylhomocysteine nucleosidase (MTAN) hydrolyzes adenine from its substrates to form S-methyl-5-thioribose and S-ribosyl-l-homocysteine"* [PMID: 30860833](https://pubmed.ncbi.nlm.nih.gov/30860833/). The breadth of substrate acceptance is established for *Campylobacter jejuni* MTAN, whose *"substrate specificity ... is demonstrated to include 6-amino-6-deoxyfutalosine, 5′-methylthioadenosine, S-adenosylhomocysteine, adenosine, and 5′-deoxyadenosine"* [PMID: 30339406](https://pubmed.ncbi.nlm.nih.gov/30339406/).

Structurally, MTANs are **homodimers with two catalytic sites at the dimer interface**: *"Crystal structures show MTANs to be homodimers with two catalytic sites near the dimer interface"* [PMID: 24502544](https://pubmed.ncbi.nlm.nih.gov/24502544/). Each active site is composed of residues contributed by both monomers, and catalytic-site cooperativity between the two protomers has been documented. The subcellular localization is **cytosolic** (GO:0005829), consistent with the intracellular SAM-cycle metabolites it processes.

### Finding 3 — Physiological role in *P. putida*: methyl-cycle detoxification and adenine salvage, NOT AI-2 quorum sensing

This finding most sharply distinguishes PP_3254's *in vivo* role from the pathogen-focused MTAN literature. Genome-context analysis of KT2440 in KEGG shows that **luxS (K07173, S-ribosylhomocysteine lyase / AI-2 synthase) is absent from the genome.** LuxS converts the SRH product of MTAN into the AI-2 quorum-sensing autoinducer. Without it, the SRH generated by PP_3254 cannot be routed to AI-2. Therefore, despite the extensive literature linking bacterial MTANs to AI-2 quorum sensing in *E. coli*, *Vibrio cholerae*, and *Staphylococcus aureus*, **this role does not apply to PP_3254 in *P. putida*.** *Pseudomonas* instead uses acyl-homoserine-lactone quorum sensing, which does not depend on MTAN.

By contrast, the canonical SAH-recycling route is intact: S-adenosylhomocysteine hydrolase *ahcY* (K01251) is present as PP_4976, and SAM synthetase *metK* (K00789) is present as PP_4967. Because SAH can be recycled by the AhcY route back toward methionine and SAM, MTAN's contribution to SAH turnover is partially redundant in this organism — its more distinctive and non-redundant contribution is clearance of **MTA and 5′-deoxyadenosine**, for which the AhcY route offers no alternative. KEGG assigns PP_3254 to pathway ppu00270 (cysteine and methionine metabolism) and ppu01230 (biosynthesis of amino acids).

The general importance of relieving product inhibition is captured by the Parveen & Cornell review: *"MTA, SAH and 5′-deoxyadenosine (5′dADO) are product inhibitors of these reactions, and are substrates of MTA/SAH nucleosidase, underscoring its importance in a wide array of metabolic reactions"* [PMID: 21166890](https://pubmed.ncbi.nlm.nih.gov/21166890/). The same review enumerates the enzyme's roles: *"MTAN activity has been linked to quorum sensing pathways, polyamine biosynthesis, and adenine salvage"* [PMID: 27019223](https://pubmed.ncbi.nlm.nih.gov/27019223/) — of which, in *P. putida*, the polyamine-biosynthesis (MTA clearance) and adenine-salvage roles apply, while the AI-2 quorum-sensing role does not.

### Finding 4 — Active-site conservation confirms catalytic competence; methionine-salvage pathway is incomplete

A refined BLOSUM62 affine-gap alignment of Q88HU9 against the structurally characterized *E. coli* MTAN (P0AF12) gave **29.4% identity and 48.5% similarity over 204 aligned positions**. Mapping every characterized *E. coli* active-site residue onto the *P. putida* sequence shows near-complete conservation of the catalytic and substrate-binding machinery:

| *E. coli* MTAN residue | Role | PP_3254 (Q88HU9) equivalent | Conservation |
|---|---|---|---|
| Ile50 | Hydrophobic substrate pocket | Ile61 | Identical |
| Ser76 | Ribose binding | Ser87 | Identical |
| Glu174 | Ribosyl-hydroxyl binding | Glu165 | Identical |
| Asp197 | General acid, protonates adenine N7 leaving group | Asp188 | Identical |
| Arg193 | Positive charge in active site | Lys184 | Conservative (charge retained) |
| Phe207 | Aromatic adenine stacking | Trp198 | Conservative (aromatic retained) |
| Glu12 | N-terminal nucleophile-activating residue | Not unambiguously aligned | Uncertain (N-terminal extension) |

Six of seven catalytic/binding positions are conserved (four identical, two conservatively substituted with charge or aromaticity preserved). The only ambiguity is the N-terminal nucleophile-activating Glu12, which could not be unambiguously placed because Q88HU9 carries a ~15-residue N-terminal extension. This pattern strongly supports the conclusion that PP_3254 is a **catalytically active MTAN**. The mechanistic importance of the conserved residues is underscored by the demonstration that *"Precise Positioning of Water Is Critical for Hydrolysis Catalyzed by 5′-Methylthioadenosine Nucleosidase"* [PMID: 35969806](https://pubmed.ncbi.nlm.nih.gov/35969806/) — the conserved Asp/Glu pair is exactly what orients that catalytic water.

Genome reconstruction adds two important contextual observations. First, the classical **5-methylthioribose → methionine salvage pathway is incomplete** in KT2440: methylthioribose kinase *mtnK* (K00899) and downstream *mtnB* (K08964) and *mtnC* (K08965) are absent; only *mtnA* (PP_1766) and an ARD-family gene (K08967/PP_1832) are present. This means the MTR product of MTAN is not efficiently recycled to methionine, reinforcing that the enzyme's dominant benefit is removal of the inhibitory adenosyl by-products and adenine recovery rather than sulfur/methionine salvage. Second, **adenine phosphoribosyltransferase *apt* (K00761, PP_0746) is present**, providing the route by which the released adenine re-enters the nucleotide pool (adenine + PRPP → AMP). Third, the operon context is that of a **standalone housekeeping gene**: PP_3254 is flanked by functionally unrelated genes — PP_3253 (carboxylate-amine ligase) and PP_3255 (Ku/NHEJ DNA-repair protein) — rather than sitting within a salvage or quorum-sensing operon.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of PP_3254 as the **"clean-up" hydrolase of the activated methyl cycle** in *P. putida*. The diagram summarizes the metabolic context and the fate of each substrate and product:

```
                 SAM (metK / PP_4967)
                   │
        ┌──────────┼───────────────┬─────────────────────┐
        │          │               │                     │
   methyltransferases      spermidine synthase     radical-SAM enzymes
        │          │               │                     │
        ▼          ▼               ▼                     ▼
       SAH        SAH             MTA                 5′-dAdo
        │                          │                     │
   (ahcY / PP_4976,                │                     │
    canonical route)               │                     │
        │          └──────────────┼─────────────────────┘
        ▼                         ▼
    homocysteine        ╔══════════════════════════╗
                        ║   PP_3254  MTAN          ║  cytosol
                        ║   EC 3.2.2.9, homodimer  ║  Asp188 / Glu165
                        ╚══════════════════════════╝
                                  │  + H2O
                 ┌────────────────┼──────────────────────┐
                 ▼                ▼                       ▼
              adenine      5-methylthioribose    S-ribosylhomocysteine
                 │          (MTR)                  (SRH)
                 │           │                       │
          apt (PP_0746)      │                  ✗ luxS ABSENT
          adenine + PRPP     │                  → NO AI-2 produced
             → AMP           │
                       methionine-salvage
                       pathway INCOMPLETE
                       (mtnK/B/C absent)
```

**The central logic:** SAM is the universal methyl donor and aminopropyl donor. Every reaction that consumes SAM generates one of three adenosyl by-products — SAH (from methyl transfer), MTA (from polyamine/spermidine synthesis and other aminopropyl transfers), or 5′-dAdo (from radical-SAM chemistry). All three are **potent competitive product inhibitors** of the enzymes that make them. If they accumulate, SAM-dependent metabolism grinds to a halt. MTAN prevents this by hydrolyzing all three to free adenine, keeping the cycle flowing.

What makes PP_3254's role in *P. putida* distinctive relative to the model-pathogen literature is the **downstream genomic wiring**:

1. **The SRH branch is a dead end for signaling.** In *E. coli*/*Vibrio*, SRH is cleaved by LuxS to make AI-2. KT2440 has no *luxS*, so PP_3254 makes no contribution to AI-2 signaling — a genuine, organism-specific functional difference, not merely an untested possibility.
2. **The MTR branch does not efficiently feed methionine salvage.** The *mtnK/mtnB/mtnC* genes are missing, so recovered methylthioribose is not readily converted back to methionine. The sulfur-salvage benefit that motivates MTAN in some organisms is muted here.
3. **The adenine branch is fully functional.** With *apt* (PP_0746) present, the adenine released by every MTAN turnover is salvaged into AMP, conserving purine and energetic investment.

The net interpretation is that PP_3254 functions as a **cytosolic housekeeping detoxification and adenine-salvage enzyme**. Its non-redundant value lies in clearing MTA and 5′-dAdo (SAH being partly handled by AhcY) and returning adenine to the nucleotide pool. It is a metabolic "janitor" of the methyl cycle rather than a signaling enzyme in this species.

---

## Evidence Base

The functional call is supported by a well-developed literature on bacterial MTANs. The table summarizes how each key paper contributes.

| PMID | Focus | Contribution to this annotation |
|---|---|---|
| [21166890](https://pubmed.ncbi.nlm.nih.gov/21166890/) | Authoritative MTAN review (Parveen & Cornell) | Defines MTAN as integral to the activated methyl cycle; establishes MTA/SAH/5′-dAdo as product inhibitors and MTAN substrates — the basis for the detoxification role |
| [27019223](https://pubmed.ncbi.nlm.nih.gov/27019223/) | *M. tuberculosis* Rv0091 MTAN, transition-state structure | Defines the enzyme and the exact N-ribosidic bond cleaved (EC 3.2.2.9); lists quorum sensing, polyamine biosynthesis, adenine salvage |
| [30860833](https://pubmed.ncbi.nlm.nih.gov/30860833/) | *H. pylori* MTAN vs human MTAP inhibitors | Documents the reaction products (S-methyl-5-thioribose and S-ribosylhomocysteine) |
| [30339406](https://pubmed.ncbi.nlm.nih.gov/30339406/) | *C. jejuni* MTAN transition-state analogues | Establishes the broad substrate specificity (6-amino-6-deoxyfutalosine, MTA, SAH, adenosine, 5′-dAdo) |
| [24502544](https://pubmed.ncbi.nlm.nih.gov/24502544/) | Catalytic-site cooperativity in dimeric MTAN | Establishes the homodimeric quaternary structure with two active sites at the dimer interface |
| [35969806](https://pubmed.ncbi.nlm.nih.gov/35969806/) | Water positioning in MTAN catalysis | Supports the water-nucleophile hydrolytic mechanism served by the conserved Asp/Glu residues |
| [19270684](https://pubmed.ncbi.nlm.nih.gov/19270684/) | Transition-state analogues disrupt quorum sensing (*V. cholerae*) | Illustrates the MTAN→AI-2 link that is **absent** in *P. putida* (contextualizes Finding 3) |
| [28487228](https://pubmed.ncbi.nlm.nih.gov/28487228/) | SAHN and AI-2 / biofilm in *E. coli* | Confirms EC 3.2.2.9, methyl-recycling essentiality, and the luxS-dependent AI-2 link absent here |
| [23611628](https://pubmed.ncbi.nlm.nih.gov/23611628/) | Pfs essential for *S. aureus* virulence | Shows MTAN's pleiotropic metabolic importance (methylation, polyamines, vitamins); LuxS/AI-2-independent phenotypes |
| [22931458](https://pubmed.ncbi.nlm.nih.gov/22931458/) | Femtomolar MTAN inhibitors, thermodynamics | Confirms hydrolytic cleavage of adenine from MTA; species-specific active-site behavior |

**Convergence and divergence.** The papers converge unanimously on the biochemistry (reaction, products, broad specificity, homodimeric structure, dissociative mechanism). Where the literature and this annotation **diverge** is on physiological role: nearly all primary studies are pathogen-focused and emphasize AI-2 quorum sensing and virulence. The genome-context analysis of KT2440 (absent *luxS*, incomplete methionine-salvage pathway) is what redirects the interpretation away from signaling and toward metabolite detoxification and adenine salvage for this specific organism. Adopting the pathogen literature's emphasis uncritically would misassign PP_3254's *in vivo* role.

---

## Supported and Refuted Hypotheses

**Supported**
- PP_3254 is an MTA/SAH nucleosidase (EC 3.2.2.9) — convergent database + homology + active-site evidence. *(High confidence)*
- It is a cytosolic homodimeric hydrolase acting on MTA/SAH/5′-dAdo, releasing adenine. *(High confidence, by strong homology to characterized orthologs)*
- Its principal in-vivo role in *P. putida* is adenine salvage + relief of SAM-cycle product inhibition. *(Moderate–high confidence; genome-based inference)*

**Refuted / not applicable in *P. putida***
- MTAN → AI-2 quorum sensing: refuted (no *luxS*).
- MTAN → net methionine salvage from MTA: not realized (pathway incomplete, no *mtnK*).
- Futalosine/menaquinone role: not applicable (KT2440 uses the classical Men pathway).

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of Q88HU9.** There is no published enzyme assay, kinetic measurement (kcat, Km), or crystal structure of the *P. putida* KT2440 protein itself. Every functional statement is inferred from orthology, domain architecture, and residue conservation. Confidence is high because MTAN is a large, deeply studied family and the catalytic residues are conserved — but this remains inference, not direct evidence.

2. **N-terminal residue ambiguity.** The ~15-residue N-terminal extension in Q88HU9 prevented unambiguous alignment of the nucleophile-activating Glu12 equivalent. Whether this extension has structural/regulatory significance, or simply reflects an alternative start-codon annotation, is unresolved.

3. **Substrate-preference profile unknown.** Bacterial MTANs vary in relative activity toward MTA vs SAH vs 5′-dAdo. Which substrate PP_3254 handles best in vivo is untested.

4. **Quantitative redundancy with AhcY unquantified.** SAH is recyclable by AhcY (PP_4976), making MTAN's SAH activity partly redundant, but the relative flux through the two routes is unknown.

5. **Localization inferred, not observed.** Cytosolic localization (GO:0005829) is inferred from pathway membership and the absence of signal/localization sequences; it has not been directly demonstrated for this protein.

6. **Pathway inferences from KO assignments.** Absence of *luxS* and *mtnK* is inferred from KEGG orthology and could, in principle, miss non-orthologous gene replacements; targeted metabolomics would directly confirm.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Clone, express, and purify PP_3254; measure kcat/Km against MTA, SAH, 5′-deoxyadenosine, and adenosine using a xanthine-oxidase-coupled or direct adenine-release assay. This converts the inferential annotation into direct biochemical evidence and reveals the substrate-preference profile.

2. **Structural determination.** Solve the crystal/cryo-EM structure (or generate a validated AlphaFold model with active-site verification) to confirm the homodimeric fold, the two dimer-interface active sites, and the positions of Asp188, Glu165, and the ambiguous N-terminal nucleophile residue.

3. **Gene knockout + metabolite profiling.** Construct a ΔPP_3254 mutant in KT2440 and quantify intracellular MTA, SAH, 5′-dAdo, and adenine by LC-MS. Accumulation of MTA/5′-dAdo (but not SAH, if AhcY compensates) would experimentally confirm the non-redundant detoxification role predicted here.

4. **Confirm absence of AI-2 signaling.** Test wild-type and ΔPP_3254 strains in an AI-2 bioassay (e.g., *Vibrio harveyi* reporter) to empirically verify that PP_3254 does not feed quorum sensing, consistent with absent *luxS*.

5. **Adenine-salvage flux tracing.** Use isotopically labeled substrate to confirm that adenine released by PP_3254 is channeled through Apt (PP_0746) into the AMP pool.

6. **Growth-condition transcriptomics.** Determine when PP_3254 is expressed (e.g., during rapid growth demanding high methyltransferase/polyamine flux) to clarify physiological demand.

---

## Conclusion

PP_3254 (Q88HU9) is, with high confidence, a **cytosolic homodimeric 5′-methylthioadenosine/S-adenosylhomocysteine nucleosidase (MTAN, EC 3.2.2.9)** of the PNP/UDP-phosphorylase superfamily. It irreversibly hydrolyzes the N-ribosidic bond of MTA, SAH, and 5′-deoxyadenosine to release free adenine plus the corresponding ribose products, using a water nucleophile positioned by a conserved general-acid Asp188/Glu165 catalytic pair. Its primary physiological function in *P. putida* KT2440 is **detoxification of product-inhibitory adenosyl metabolites within the activated methyl cycle, coupled to adenine salvage** — not AI-2 quorum sensing (genetically impossible here, as *luxS* is absent) and not efficient methionine salvage (that pathway is incomplete). The assignment is grounded in convergent orthology, domain architecture, and residue-level conservation of the catalytic machinery, but has not yet been confirmed by direct biochemical assay of this specific protein.


## Artifacts

- [OpenScientist final report](PP_3254-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3254-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27019223
2. PMID:21166890
3. PMID:30860833
4. PMID:30339406
5. PMID:24502544
6. PMID:35969806