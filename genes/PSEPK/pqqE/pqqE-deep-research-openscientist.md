---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T14:01:02.208713'
end_time: '2026-07-20T14:24:31.635928'
duration_seconds: 1409.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pqqE
  gene_symbol: pqqE
  uniprot_accession: Q88QV8
  protein_description: 'RecName: Full=PqqA peptide cyclase {ECO:0000255|HAMAP-Rule:MF_00660};
    EC=1.21.98.4 {ECO:0000255|HAMAP-Rule:MF_00660}; AltName: Full=Coenzyme PQQ synthesis
    protein E {ECO:0000255|HAMAP-Rule:MF_00660}; AltName: Full=Pyrroloquinoline quinone
    biosynthesis protein E {ECO:0000255|HAMAP-Rule:MF_00660};'
  gene_info: Name=pqqE {ECO:0000255|HAMAP-Rule:MF_00660}; OrderedLocusNames=PP_0376;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the radical SAM superfamily. PqqE family.
  protein_domains: 4Fe4S-binding_SPASM_dom. (IPR023885); Aldolase_TIM. (IPR013785);
    Elp3/MiaA/NifB-like_rSAM. (IPR006638); MoaA_NifB_PqqE_Fe-S-bd_CS. (IPR000385);
    PQQ_synth_PqqE_bac. (IPR011843)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pqqE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pqqE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QV8
- **Protein Description:** RecName: Full=PqqA peptide cyclase {ECO:0000255|HAMAP-Rule:MF_00660}; EC=1.21.98.4 {ECO:0000255|HAMAP-Rule:MF_00660}; AltName: Full=Coenzyme PQQ synthesis protein E {ECO:0000255|HAMAP-Rule:MF_00660}; AltName: Full=Pyrroloquinoline quinone biosynthesis protein E {ECO:0000255|HAMAP-Rule:MF_00660};
- **Gene Information:** Name=pqqE {ECO:0000255|HAMAP-Rule:MF_00660}; OrderedLocusNames=PP_0376;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the radical SAM superfamily. PqqE family.
- **Key Domains:** 4Fe4S-binding_SPASM_dom. (IPR023885); Aldolase_TIM. (IPR013785); Elp3/MiaA/NifB-like_rSAM. (IPR006638); MoaA_NifB_PqqE_Fe-S-bd_CS. (IPR000385); PQQ_synth_PqqE_bac. (IPR011843)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pqqE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pqqE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pqqE** (gene ID: pqqE, UniProt: Q88QV8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PqqE (Q88QV8), PqqA Peptide Cyclase from *Pseudomonas putida* KT2440

## Summary

**PqqE (UniProt Q88QV8; locus PP_0376) is the entry-point radical *S*-adenosyl-L-methionine (radical SAM) enzyme of pyrroloquinoline quinone (PQQ) cofactor biosynthesis.** Its defining, experimentally established function is to catalyze the first committed tailoring step of PQQ assembly: a radical-mediated, intramolecular carbon–carbon cross-link between a specific glutamate and a specific tyrosine side chain within the short, ribosomally synthesized precursor peptide PqqA. This reaction (EC 1.21.98.4; Rhea RHEA:56836) converts PqqA and *S*-adenosyl-L-methionine (SAM) into an E–Y cross-linked PqqA, 5′-deoxyadenosine, L-methionine, and a proton. Because PQQ is a ribosomally synthesized and post-translationally modified peptide (RiPP)-derived cofactor, PqqE founds the entire pathway — everything downstream (proteolytic excision, hydroxylation by PqqB, and the eight-electron oxidative ring closure by PqqC) operates on the cross-linked product that PqqE creates.

Mechanistically, PqqE belongs to the SPASM-domain subclass of the radical SAM superfamily. It carries an N-terminal catalytic [4Fe-4S] cluster (ligated by the canonical CxxxCxxC motif at Cys21/Cys25/Cys28 in the *P. putida* protein) that reductively cleaves SAM to generate a highly reactive 5′-deoxyadenosyl radical, plus two C-terminal auxiliary Fe-S clusters (AuxI and AuxII) housed in the SPASM domain that shuttle electrons during catalysis. Full activity in vitro depends on the RiPP-recognition-element (RRE) chaperone PqqD, which binds the otherwise unstructured PqqA peptide and presents it to PqqE, and on a physiological flavodoxin/flavodoxin-reductase reducing system. The enzyme has no signal peptide or transmembrane segment and functions in the cytoplasm.

In the physiological context of *P. putida* KT2440, the PQQ produced through this pathway serves as the redox coenzyme of the periplasmic glucose dehydrogenase (GDH/Gcd), enabling direct oxidation of glucose to gluconic acid in the periplasm. This activity underlies the bacterium's capacity for mineral-phosphate solubilization in the rhizosphere, a trait of agronomic significance. Thus PqqE, a cytoplasmic biosynthetic enzyme, ultimately provisions a periplasmic oxidative metabolic pathway. The gene lies within the *pqqFABCDEG* operon (PP_0376 = *pqqE*).

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check was completed and **confirmed positive** on every axis:

| Verification axis | UniProt target | What the literature/databases describe | Match? |
|---|---|---|---|
| Gene symbol | *pqqE* | *pqqE* — PQQ biosynthesis radical SAM gene | ✅ |
| Protein name | PqqA peptide cyclase; Coenzyme PQQ synthesis protein E | PqqE, catalyzes Glu–Tyr cross-link in PqqA | ✅ |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) | *P. putida* KT2440 *pqq* operon characterized (PMID 27287323) | ✅ |
| Family | Radical SAM superfamily, PqqE family | Radical SAM / SPASM-domain enzyme (PMID 29405700) | ✅ |
| Domains | SPASM 4Fe4S-binding; rSAM; TIM-barrel; MoaA/NifB/PqqE Fe-S | SPASM domain + N-terminal rSAM [4Fe-4S] confirmed | ✅ |
| EC number | 1.21.98.4 | EC 1.21.98.4 (Rhea RHEA:56836) | ✅ |

The gene symbol is **unambiguous** for this protein. The extensive primary literature on PqqE (much of it from orthologs in *Methylobacterium/Methylorubrum extorquens*, plus direct annotation of the *P. putida* KT2440 protein) aligns precisely with the UniProt identity. This report proceeds on solid identity grounds.

---

## Key Findings

### Finding 1 — PqqE catalyzes the first committed step of PQQ biosynthesis: a C–C cross-link between Glu and Tyr in the precursor peptide PqqA

The defining function of PqqE is the installation of a new carbon–carbon bond between two amino-acid side chains within the short ribosomal peptide PqqA. This was established by in vitro reconstitution by Barr and colleagues, who demonstrated that PqqE, in conjunction with the accessory protein PqqD, "carries out the first step in PQQ biosynthesis: a radical-mediated formation of a new carbon-carbon bond between two amino acid side chains on PqqA" ([PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/)). Subsequent EPR and mechanistic work by Tao et al. specified the chemistry precisely: "A key step in PQQ biosynthesis is a carbon-carbon cross-link reaction between glutamate and tyrosine side chains within the ribosomally synthesized peptide substrate PqqA. This reaction is catalyzed by the radical SAM enzyme PqqE" ([PMID: 31769977](https://pubmed.ncbi.nlm.nih.gov/31769977/)).

This is the enzyme's **primary catalytic function** and the direct answer to "what reaction is catalyzed": a radical-mediated intramolecular Glu–Tyr cross-linking of PqqA. The reaction is classified as EC 1.21.98.4, within the oxidoreductase class acting on X–H and Y–H to form an X–Y bond. Because PQQ is peptide-derived, this cross-link seeds all downstream chemistry — the modified glutamate and tyrosine are the atomic precursors of the fused tricyclic PQQ ring system.

### Finding 2 — PqqE is a SPASM-domain radical SAM enzyme with a catalytic [4Fe-4S] cluster plus two auxiliary Fe-S clusters

PqqE's catalytic architecture places it firmly in the SPASM/Twitch subgroup of the radical SAM superfamily. X-ray crystallography together with Mössbauer and EPR spectroscopy (Barr et al. 2018) revealed that, beyond the N-terminal radical-SAM [4Fe-4S] cluster, the enzyme carries two C-terminal auxiliary clusters: "The auxiliary cluster nearest the RS site (AuxI) is in the form of a 2Fe-2S cluster ligated by four cysteines, an Fe-S center not seen previously in other SPASM domain proteins; this assignment is further supported by Mössbauer and EPR spectroscopies. The second, more remote cluster (AuxII) is a 4Fe-4S center that is ligated by three cysteine residues and one aspartate residue" ([PMID: 29405700](https://pubmed.ncbi.nlm.nih.gov/29405700/)). The unusual Cys4-ligated [2Fe-2S] AuxI cluster distinguishes PqqE from most other SPASM enzymes, which typically house [4Fe-4S] auxiliary clusters.

The catalytic mechanism is the canonical radical SAM strategy: "PqqE is a radical *S*-adenosyl-l-methionine (SAM) (RS) enzyme, a family of enzymes that use the reductive cleavage of a [4Fe-4S] cluster-bound SAM molecule to generate a 5′-deoxyadenosyl radical" ([PMID: 30097100](https://pubmed.ncbi.nlm.nih.gov/30097100/)). The 5′-deoxyadenosyl radical abstracts a hydrogen atom to initiate the cross-linking chemistry on PqqA. The auxiliary clusters are thought to mediate the electron-transfer events required to complete the reaction (analogous to auxiliary clusters in other SPASM/Twitch enzymes such as the sactisynthases). EPR mapping of the individual clusters was extended by Tao et al. ([PMID: 31769977](https://pubmed.ncbi.nlm.nih.gov/31769977/)).

The three metal-binding cysteines of the catalytic cluster in the *P. putida* protein are annotated at positions 21, 25, and 28 — the canonical CxxxCxxC radical SAM motif — consistent with the sequence analysis in Finding 5.

### Finding 3 — PqqE activity requires the RiPP-chaperone PqqD and a flavodoxin/flavodoxin-reductase reducing system

PqqE does not act efficiently on free PqqA; it requires a dedicated peptide chaperone. Barr et al. reported that "PqqE activity is dependent on the accessory protein PqqD, which was recently shown to bind PqqA tightly. In addition, PqqE activity in vitro requires the presence of a flavodoxin- and flavodoxin reductase-based reduction system, with other reductants leading to an uncoupled cleavage of the co-substrate SAM" ([PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/)). This dual dependency is mechanistically important: the flavodoxin system supplies the low-potential electron needed for productive, coupled SAM cleavage, whereas non-physiological reductants (e.g., dithionite) drive futile, uncoupled SAM cleavage not linked to substrate modification.

The role of PqqD as a substrate-presentation chaperone was clarified by NMR studies: "The substrate is the peptide PqqA, which is presented to the radical SAM enzyme PqqE by the small protein PqqD. PqqA is unstructured in solution, and only binds to PqqE when in complex with PqqD" ([PMID: 27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/)). PqqD is a member of the RiPP-recognition-element (RRE) family — a conserved motif that mediates leader-peptide recognition across many RiPP biosynthetic pathways. Thus PqqE functions as part of a two-protein catalytic unit (PqqE–PqqD) rather than as a standalone enzyme.

### Finding 4 — In *P. putida* KT2440, the *pqqFABCDEG* operon supplies PQQ for periplasmic glucose dehydrogenase, driving gluconic-acid production and phosphate solubilization

The physiological purpose of PqqE in the target organism is to help manufacture PQQ for periplasmic redox metabolism. An & Moe mapped the *P. putida* KT2440 *pqq* gene cluster and connected it to phosphate solubilization: "Soil-dwelling microbes solubilize mineral phosphates by secreting gluconic acid, which is produced from glucose by a periplasmic glucose dehydrogenase (GDH) that requires pyrroloquinoline quinone (PQQ) as a redox coenzyme" ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). They further documented the operon organization: "The pqq gene cluster (pqqFABCDEG) encodes at least two independent transcripts."

This establishes the pathway-level context and the spatial division of labor: PqqE builds the cofactor in the cytoplasm, mature PQQ is delivered for use in the periplasm, and there it activates GDH (Gcd) to oxidize glucose to gluconic acid. The study also reported that PQQ and GDH activity are highest with glucose as the sole carbon source and under low soluble phosphate, and that PQQ level limits the rate of phosphate solubilization — connecting *pqqE* function to an ecologically and agronomically important rhizosphere trait. *pqqE* (PP_0376) is the radical-SAM gene embedded in this operon.

### Finding 5 — Sequence analysis pinpoints the Glu15/Tyr19 (E-x-x-x-Y) cross-link pair in PqqA and the CxxxCxxC + SPASM cysteines in PqqE

Direct analysis of the *P. putida* KT2440 sequences localizes the reactive residues. The PqqA precursor (UniProt Q88QV4) is a 23-residue peptide, `MWTKPAYTDLRIGFEVTMYFANR`, containing a single glutamate (Glu15) and the conserved reactive tyrosine (Tyr19) arranged as the canonical **E-x-x-x-Y motif** (segment E15–V–T–M–Y19). Because the peptide has only one glutamate, the substrate specificity of PqqE is effectively hard-wired by the sequence of PqqA itself.

The PqqE protein (Q88QV8, 376 aa) carries the radical-SAM CxxxCxxC motif at Cys21/Cys25/Cys28 (C21-PLQ-C25-PY-C28), which ligates the catalytic [4Fe-4S] cluster, and a cysteine-rich C-terminal SPASM region (cysteines at approximately positions 264/305/308/318/320/336) supplying ligands for the auxiliary Fe-S clusters. This sequence-level assignment is fully consistent with the structural/spectroscopic work in Finding 2 and the UniProt feature annotations in Finding 6.

### Finding 6 — Authoritative reaction (Rhea RHEA:56836)

The curated catalytic activity for Q88QV8 (via HAMAP-Rule MF_00660) is:

> **[PQQ precursor protein] + S-adenosyl-L-methionine = E-Y cross-linked-[PQQ precursor protein] + 5′-deoxyadenosine + L-methionine + H⁺**
> (Rhea RHEA:56836; EC 1.21.98.4)

The cofactor annotation specifies binding of one [4Fe-4S] cluster coordinated by three cysteines and an exchangeable SAM, with the three metal-binding cysteines at positions 21, 25, and 28 — exactly the CxxxCxxC motif identified by sequence analysis. The pathway is annotated as "cofactor biosynthesis; pyrroloquinoline quinone biosynthesis." Critically for localization, **no signal peptide and no transmembrane feature is annotated**, consistent with a cytoplasmic enzyme.

### Finding 7 — The PqqA E-x-x-x-Y cross-link motif is universally conserved across diverse PQQ-producing bacteria

An alignment of 25 reviewed PqqA orthologs from taxonomically diverse PQQ producers (*Pseudomonas* spp., *Acinetobacter*, *Klebsiella/Kluyvera*, *Stutzerimonas*, *Bradyrhizobium*, *Ruegeria*, *Gluconobacter*, *Methylococcus*, *Methylobacillus*, *Variovorax*, *Colwellia*, *Dinoroseobacter*) shows an **invariant Glu-x-x-x-Tyr motif in every sequence** — the reactive glutamate and tyrosine are always exactly three residues apart. Observed variants of the pentapeptide window include EVTMY, EVTLY, EINMY, EINSY, EITMY, and EKPSY, but the E and Y positions never vary. The *P. putida* KT2440 PqqA (EVTMY) is identical to many *Pseudomonas*/*Acinetobacter* orthologs.

This deep evolutionary conservation is strong bioinformatic evidence that the Glu–Tyr geometry is the essential recognition/reaction determinant for PqqE across the bacterial kingdom, reinforcing the mechanistic assignment. PqqE cross-references confirm identity: KEGG ppu:PP_0376; Pfam PF04055 (radical SAM) + PF13186 (SPASM auxiliary [4Fe-4S]); InterPro IPR011843/IPR017200/IPR050377 (PqqE). No experimental PDB structure exists for the *P. putida* protein specifically, though structures have been solved for orthologs.

---

## Mechanistic Model / Interpretation

PqqE operates at the head of a four-enzyme RiPP maturation pathway that converts a ribosomal peptide into the free small-molecule cofactor PQQ. The following model synthesizes the findings.

### The PQQ biosynthetic pathway (RiPP logic)

```
   Ribosome
      │  translates
      ▼
   PqqA (23-aa precursor peptide, unstructured)
   ...G-F-E15-V-T-M-Y19-F-A-N-R
            │            │
            └── Glu ─────┘ Tyr   (E-x-x-x-Y motif; 3 residues apart)
      │
      │  PqqD (RRE chaperone) binds unstructured PqqA,
      │  presents it to PqqE
      ▼
 ┌───────────────────────────────────────────────┐
 │  PqqE  (radical SAM, SPASM domain)  ◀── THIS PROTEIN
 │   • [4Fe-4S] cat. cluster (Cys21/25/28) + SAM  │
 │   • AuxI [2Fe-2S] (Cys4) + AuxII [4Fe-4S]      │
 │   • flavodoxin/Fld-reductase supplies e⁻       │
 │                                                 │
 │   SAM ─(reductive cleavage)→ 5′-dAdo• radical   │
 │   5′-dAdo• abstracts H → C–C bond Glu15–Tyr19   │
 └───────────────────────────────────────────────┘
      │  product: E–Y cross-linked PqqA
      │           + 5′-deoxyadenosine + L-Met + H⁺
      ▼
   Protease/peptidase (excision of cross-linked di-amino-acid unit)
      ▼
   PqqB  (dual hydroxylase)
      ▼
   PqqC  (8-electron, 8-proton oxidase; ring closure)
      ▼
   PQQ  (mature tricyclic o-quinone cofactor)
      │  delivered / assembled for periplasmic use
      ▼
   Periplasmic glucose dehydrogenase (Gcd/GDH) holoenzyme
      │  glucose ──► gluconic acid
      ▼
   Mineral-phosphate solubilization (rhizosphere)
```

### Reaction catalyzed (the core answer)

| Attribute | Value |
|---|---|
| Enzyme | PqqE / PqqA peptide cyclase |
| EC number | 1.21.98.4 |
| Rhea | RHEA:56836 |
| Substrate | PqqA precursor peptide (specifically Glu15 + Tyr19 side chains) |
| Co-substrate | S-adenosyl-L-methionine (SAM) |
| Products | E–Y cross-linked PqqA + 5′-deoxyadenosine + L-methionine + H⁺ |
| Chemistry | Radical-mediated intramolecular C–C cross-link |
| Cofactors | Catalytic [4Fe-4S] + SAM; AuxI [2Fe-2S]; AuxII [4Fe-4S] |
| Required partners | PqqD (RRE chaperone); flavodoxin/flavodoxin-reductase reductant |
| Localization | Cytoplasm (no signal peptide, no TM segment) |
| Pathway | PQQ cofactor biosynthesis (first committed step) |

### Substrate specificity

Substrate specificity is dictated by two layers: (1) the **PqqD chaperone** recognizes the PqqA leader region via an RRE and delivers the peptide, providing selectivity at the level of protein–peptide recognition; and (2) the **E-x-x-x-Y motif** in the PqqA core positions exactly one glutamate and one tyrosine at a fixed 3-residue spacing, so the enzyme's chemistry has a single, geometrically defined pair of reactive side chains to act on. The universal conservation of this motif across phylogenetically distant PQQ producers (Finding 7) shows that PqqE's substrate is essentially invariant in its reactive core, even where flanking residues drift.

### Localization

PqqE itself is a **cytoplasmic** enzyme — consistent with the strict anaerobic sensitivity of most radical SAM chemistry (the *M. extorquens* ortholog is a notable, unusually oxygen-tolerant exception; [PMID: 26188050](https://pubmed.ncbi.nlm.nih.gov/26188050/)) and with the absence of any secretion or membrane-anchoring signal in Q88QV8. The **product** of the pathway (PQQ), however, exerts its metabolic function in the **periplasm**, as the redox coenzyme of glucose dehydrogenase. This cytoplasm→periplasm hand-off is the key spatial feature of PqqE's biological role.

---

## Evidence Base

| PMID | Study (paraphrased) | How it supports the findings |
|---|---|---|
| [26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/) | Barr et al. — In vitro demonstration that PqqE catalyzes de novo C–C cross-linking within PqqA in the presence of PqqD | **Primary evidence** for Findings 1 & 3: establishes the first-step C–C cross-link, PqqD dependence, flavodoxin reductant requirement |
| [31769977](https://pubmed.ncbi.nlm.nih.gov/31769977/) | Tao et al. — EPR identification of Fe-S clusters in PqqE | Supports Findings 1 & 2: specifies Glu–Tyr cross-link chemistry; maps the individual Fe-S clusters |
| [29405700](https://pubmed.ncbi.nlm.nih.gov/29405700/) | Barr et al. — X-ray + EPR of auxiliary Fe-S clusters | **Primary evidence** for Finding 2: defines AuxI ([2Fe-2S], Cys4) and AuxII ([4Fe-4S], 3 Cys + 1 Asp) |
| [30097100](https://pubmed.ncbi.nlm.nih.gov/30097100/) | Zhu et al. — Expression/purification/characterization methods for PqqE | Supports Finding 2: reductive SAM cleavage generating the 5′-deoxyadenosyl radical |
| [27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/) | Evans et al. — NMR assignments of PqqD and PqqD–PqqA complex | **Primary evidence** for Finding 3: PqqA is unstructured and presented to PqqE only via PqqD |
| [27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/) | An & Moe — Regulation of PQQ-dependent GDH in *P. putida* KT2440 | **Organism-specific evidence** for Finding 4: *pqqFABCDEG* operon; periplasmic GDH; gluconic acid; phosphate solubilization |
| [32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/) | Review — Biogenesis of PQQ | Context for the whole pathway (PqqE, PqqF/G, PqqB mechanisms) |
| [31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/) | Two-component protease in PQQ biosynthesis | Context: identifies the peptidase excising the cross-linked di-amino-acid precursor, downstream of PqqE |
| [26188050](https://pubmed.ncbi.nlm.nih.gov/26188050/) | *M. extorquens* PqqE — oxygen-tolerant radical SAM enzyme | Supports Finding 2: multiple Fe-S clusters; reductive SAM cleavage at N-terminal [4Fe-4S]; notes unusual O₂ tolerance |

Additional structural literature on related SPASM/Twitch radical SAM RiPP enzymes — SkfB ([PMID: 30217813](https://pubmed.ncbi.nlm.nih.gov/30217813/)), CteB ([PMID: 28704043](https://pubmed.ncbi.nlm.nih.gov/28704043/)), SuiB ([PMID: 28893989](https://pubmed.ncbi.nlm.nih.gov/28893989/)), RumC ([PMID: 32972973](https://pubmed.ncbi.nlm.nih.gov/32972973/)), and the methodological guidelines paper ([PMID: 30097102](https://pubmed.ncbi.nlm.nih.gov/30097102/)) — provides the mechanistic framework for interpreting PqqE's auxiliary-cluster-assisted radical cross-linking chemistry, even though these enzymes act on different peptide substrates.

**Note on peripheral literature.** Much of the recent PQQ literature in the corpus concerns PQQ's *downstream* nutraceutical/pharmacological effects in eukaryotes (anti-aging, osteoarthritis, oocyte quality, SLE, cancer scaffolds; e.g., PMIDs 41763140, 41812718, 41564475, 42068909). These describe the **product** PQQ's bioactivity, not PqqE's enzymology, and are peripheral to the annotation of the enzyme.

---

## Limitations and Knowledge Gaps

1. **No experimental structure of the *P. putida* protein.** All structural/spectroscopic characterization of PqqE has been performed on orthologs (notably *Methylobacterium/Methylorubrum extorquens*). The functional assignment for Q88QV8 relies on very high sequence conservation, curated HAMAP rules, and the universal E-x-x-x-Y motif — strong but ultimately homology-based inference for this specific protein. No PDB entry exists for the KT2440 enzyme.

2. **Direct enzymatic assays are ortholog-based.** The in vitro reconstitution demonstrating C–C cross-linking (PMID 26961875) and the Fe-S cluster characterizations were performed on non-*P. putida* PqqE. The KT2440 protein has not, to our knowledge, been individually reconstituted and assayed, though there is no reason to expect divergent chemistry given identical active-site motifs.

3. **Precise regiochemistry/atom connectivity of the cross-link.** The literature establishes a Glu–Tyr C–C bond, but complete atomic-resolution definition of the new bond in the peptide-bound state — and how AuxI/AuxII orchestrate the required electron transfers — remains an active area; the exact order of H-atom abstraction and electron flow is still being refined.

4. **PQQ trafficking to the periplasm is not fully resolved.** How mature PQQ (assembled from a cytoplasmically initiated pathway) reaches the periplasmic GDH, and whether any final maturation occurs outside the cytoplasm, is not fully worked out in *P. putida*.

5. **Regulatory coupling.** While An & Moe (PMID 27287323) tie PQQ/GDH output to carbon source and phosphate availability, the specific transcriptional/post-transcriptional control of *pqqE* within the two-transcript *pqqFABCDEG* operon is only partially defined.

---

## Proposed Follow-up Experiments / Actions

1. **Reconstitute *P. putida* KT2440 PqqE directly.** Express Q88QV8 anaerobically, reconstitute Fe-S clusters, and assay Glu15–Tyr19 cross-linking on the cognate PqqA (Q88QV4) ± PqqD by LC-MS/MS to confirm the reaction in the target organism and quantify kinetics (k_cat/K_M).

2. **Solve the KT2440 PqqE structure (or a high-confidence model).** Even an AlphaFold model validated against the *M. extorquens* structures would confirm cluster ligand geometry (Cys21/25/28; SPASM cysteines) and support the AuxI [2Fe-2S] assignment in this organism.

3. **Mutagenesis of the E-x-x-x-Y motif.** Substitute PqqA Glu15 or Tyr19 (and vary the 3-residue spacer) to test whether the fixed E–Y geometry is strictly required, directly probing the substrate-specificity model from Findings 5 and 7.

4. **Trap and characterize the AuxI/AuxII redox states during turnover.** Time-resolved EPR/Mössbauer on the KT2440 enzyme to define the electron-transfer roles of the auxiliary clusters during cross-link formation.

5. **In vivo genetics in KT2440.** Construct a clean *pqqE* deletion and complementation; confirm loss of PQQ, periplasmic GDH activity, gluconic-acid secretion, and mineral-phosphate solubilization — closing the loop from enzyme to ecological phenotype.

6. **Trace PQQ trafficking.** Use isotopically labeled precursor and subcellular fractionation to follow PQQ from cytoplasmic synthesis to periplasmic GDH incorporation.

---

## Conclusion

PqqE (Q88QV8, PP_0376) in *Pseudomonas putida* KT2440 is the **radical SAM (SPASM-domain) enzyme that initiates pyrroloquinoline quinone biosynthesis** by catalyzing a radical-mediated intramolecular carbon–carbon cross-link between the glutamate (Glu15) and tyrosine (Tyr19) side chains of the ribosomal precursor peptide PqqA (EC 1.21.98.4; RHEA:56836), consuming SAM to yield 5′-deoxyadenosine and L-methionine. It requires the RRE chaperone PqqD to present the unstructured PqqA and a flavodoxin-based reductant for coupled catalysis, and it uses a catalytic [4Fe-4S] cluster plus two auxiliary Fe-S clusters. The enzyme works in the cytoplasm; the PQQ it helps produce functions in the periplasm as the redox coenzyme of glucose dehydrogenase, driving glucose-to-gluconate oxidation and mineral-phosphate solubilization in the rhizosphere.


## Artifacts

- [OpenScientist final report](pqqE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pqqE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26961875
2. PMID:31769977
3. PMID:29405700
4. PMID:30097100
5. PMID:27638737
6. PMID:27287323
7. PMID:26188050
8. PMID:30217813
9. PMID:28704043
10. PMID:28893989
11. PMID:32972973
12. PMID:30097102