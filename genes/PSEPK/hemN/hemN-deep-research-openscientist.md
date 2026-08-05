---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:45:18.369297'
end_time: '2026-07-20T21:06:09.998576'
duration_seconds: 1251.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemN
  gene_symbol: hemN
  uniprot_accession: Q88F35
  protein_description: 'RecName: Full=Coproporphyrinogen-III oxidase {ECO:0000256|PIRNR:PIRNR000167};
    EC=1.3.98.3 {ECO:0000256|PIRNR:PIRNR000167};'
  gene_info: Name=hemN {ECO:0000313|EMBL:AAN69844.1}; OrderedLocusNames=PP_4264 {ECO:0000313|EMBL:AAN69844.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the anaerobic coproporphyrinogen-III oxidase
  protein_domains: Coprogen_oxidase_HemN. (IPR004558); Coproporphyrinogen-III_oxidase.
    (IPR034505); Elp3/MiaA/NifB-like_rSAM. (IPR006638); HemN_C. (IPR010723); rSAM.
    (IPR007197)
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
  path: hemN-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemN-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F35
- **Protein Description:** RecName: Full=Coproporphyrinogen-III oxidase {ECO:0000256|PIRNR:PIRNR000167}; EC=1.3.98.3 {ECO:0000256|PIRNR:PIRNR000167};
- **Gene Information:** Name=hemN {ECO:0000313|EMBL:AAN69844.1}; OrderedLocusNames=PP_4264 {ECO:0000313|EMBL:AAN69844.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the anaerobic coproporphyrinogen-III oxidase
- **Key Domains:** Coprogen_oxidase_HemN. (IPR004558); Coproporphyrinogen-III_oxidase. (IPR034505); Elp3/MiaA/NifB-like_rSAM. (IPR006638); HemN_C. (IPR010723); rSAM. (IPR007197)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemN" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemN** (gene ID: hemN, UniProt: Q88F35) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *hemN* (PP_4264, UniProt Q88F35) in *Pseudomonas putida* KT2440

## Summary

The gene **hemN** (ordered locus **PP_4264**; UniProt accession **Q88F35**) of *Pseudomonas putida* KT2440 encodes the **oxygen-independent (anaerobic) coproporphyrinogen-III oxidase** (EC 1.3.98.3), a soluble cytoplasmic enzyme of the **heme (tetrapyrrole) biosynthetic pathway**. Its primary and defining function is to catalyze the **oxidative decarboxylation of the two ring-A/ring-B propionate side chains of coproporphyrinogen III to the corresponding vinyl groups of protoporphyrinogen IX**, executing the antepenultimate step of protoporphyrin-IX biosynthesis without requiring molecular oxygen. This assignment is supported by direct biochemical and structural characterization of the *Escherichia coli* ortholog, by phenotypic/regulatory studies of orthologs in closely related *Pseudomonas* and *Alcaligenes* species, and by sequence-level confirmation that the *P. putida* protein carries every diagnostic catalytic motif at conserved positions.

Mechanistically, HemN is the **founding structurally-characterized member of the radical S-adenosyl-L-methionine (radical SAM) superfamily**. It harbors a **[4Fe-4S] cluster** ligated by three cysteines of a conserved CX₃CX₂C motif (the **CANICYYC** sequence at residues 63–70 in Q88F35) and binds **two molecules of SAM** in adjacent sites. Reductive cleavage of one SAM generates a highly reactive **5′-deoxyadenosyl radical** that abstracts a hydrogen from a substrate propionate; the second SAM acts as a hydrogen relay. The two propionate decarboxylations proceed **sequentially through a mono-decarboxylated intermediate, harderoporphyrinogen**, consuming two SAM and releasing two CO₂, two 5′-deoxyadenosine, and two L-methionine per turnover (Rhea:15425).

Biologically, HemN provides the **O₂-independent route** to protoporphyrinogen IX, complementing the oxygen-dependent enzyme **HemF** (PP_0073) and enabling heme synthesis under anaerobic/microaerobic conditions. In *Pseudomonas*, hemN transcription is controlled by the **Fnr-type redox regulators Anr and Dnr**, and loss of HemN function causes accumulation and excretion of **coproporphyrin III**, the oxidized form of the blocked substrate. The *P. putida* genome additionally encodes a **second HemN-family paralog (PP_3781)**, giving a redundant, redox-responsive coproporphyrinogen-III oxidase system that parallels the HemF/HemN/HemZ arrangement documented in *P. aeruginosa* and *Bacillus subtilis*. The enzyme carries out its function in the **cytoplasm** as a soluble monomer.

### Identity verification

The gene symbol "hemN" corresponds precisely to the UniProt protein description, the organism is correct, and the protein family/domains align with the characterized literature. No gene-symbol ambiguity was encountered — "hemN" is used uniformly across bacteria for this radical-SAM enzyme.

| Attribute | UniProt reference (Q88F35) | Confirmed by investigation |
|---|---|---|
| Gene symbol | hemN | ✔ Matches characterized HemN family |
| Protein | Coproporphyrinogen-III oxidase, EC 1.3.98.3 | ✔ O₂-independent copro-III oxidase |
| Organism | *P. putida* KT2440 (taxid 160488) | ✔ PP_4264 confirmed in genome |
| Length / mass | 460 aa / 52.6 kDa | ✔ Consistent with ~52 kDa orthologs |
| Family | Anaerobic coproporphyrinogen-III oxidase | ✔ InterPro IPR004558 |
| Domains | rSAM (IPR007197), HemN_C (IPR010723), Elp3/MiaA/NifB-like rSAM (IPR006638) | ✔ Radical-SAM architecture confirmed |

---

## Key Findings

### Finding 1 — HemN is the oxygen-independent coproporphyrinogen-III oxidase of heme biosynthesis

The core function of HemN is the **O₂-independent conversion of coproporphyrinogen III to protoporphyrinogen IX** (EC 1.3.98.3): the oxidative decarboxylation of the two propionate side chains on pyrrole rings A and B of coproporphyrinogen III to vinyl groups. In vitro anaerobic enzyme assays of recombinant *E. coli* HemN directly demonstrated coproporphyrinogen-III oxidase activity ([PMID: 12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/)), described explicitly as: *"In bacteria the oxygen-independent coproporphyrinogen-III oxidase catalyzes the oxygen-independent conversion of coproporphyrinogen-III to protoporphyrinogen-IX."* The structural study reinforced the physiological essentiality: *"HemN catalyzes the essential conversion of coproporphyrinogen III to protoporphyrinogen IX during heme biosynthesis"* ([PMID: 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/)).

The physiological substrate is coproporphyrinogen III specifically (the type-III isomer). HemN acts on the two propionates of rings A and B, retaining the other two propionates (rings C and D) in protoporphyrinogen IX — the same regiochemical outcome as the unrelated O₂-dependent HemF but achieved by radical chemistry. The *P. putida* HemN (hemN/PP_4264) is orthologous to the characterized enzymes and belongs to the anaerobic coproporphyrinogen-III oxidase family (InterPro IPR004558), so the reaction assignment transfers with high confidence given the conserved sequence signatures (Finding 5).

### Finding 2 — HemN is a radical SAM enzyme with a [4Fe-4S] cluster and two bound SAM molecules

HemN was the **first radical SAM enzyme to have its crystal structure solved** (2.07 Å, *E. coli*), defining the structural template for the entire superfamily. The structure shows a **[4Fe-4S] cluster ligated by three cysteines** of the conserved CXXXCXXC motif, with a SAM molecule coordinating the fourth, unique iron: *"HemN binds a 4Fe-4S cluster through three cysteine residues conserved in all Radical SAM enzymes. A juxtaposed SAM coordinates the fourth Fe ion through its amide nitrogen and carboxylate oxygen"* ([PMID: 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/)). The SAM sulfonium sits ~3.5 Å from the cluster, positioned for single-electron transfer and reductive cleavage to a 5′-deoxyadenosyl radical.

A striking, functionally important feature is that HemN binds a **second SAM immediately adjacent to the first**: *"HemN, strikingly, binds a second SAM immediately adjacent to the first. It may thus successively catalyze two propionate decarboxylations"* ([PMID: 14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/)). This provides the structural basis for the two sequential decarboxylation events.

Biochemical work confirmed the cluster's identity and the essentiality of its ligands: the enzyme contains an **O₂-sensitive Fe-S cluster**, and *"Cysteine residues Cys(62), Cys(66), and Cys(69), which are part of the conserved CXXXCXXC motif found in all HemN proteins, are essential for iron-sulfur cluster formation and enzyme function"* ([PMID: 12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/)). The oxygen sensitivity of this cluster is the molecular basis for HemN serving as the *anaerobic* branch of coproporphyrinogen oxidation.

### Finding 3 — Sequential radical decarboxylation via a harderoporphyrinogen intermediate, requiring SAM and NAD(P)H

The catalytic cycle proceeds by **radical chemistry** and requires **SAM, NAD(P)H, and additional cytoplasmic components** ([PMID: 12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/)): *"The enzyme requires S-adenosyl-l-methionine (SAM), NAD(P)H, and additional cytoplasmatic components for catalysis."* Mechanistic re-investigation established that the two propionate groups are decarboxylated **one at a time**, passing through the **mono-decarboxylated intermediate harderoporphyrinogen** ([PMID: 30884058](https://pubmed.ncbi.nlm.nih.gov/30884058/)). The revised mechanism assigns distinct roles to the two SAM molecules: *"a SAM serves as a hydrogen relay which mediates a radical-based hydrogen transfer from the propionate to the 5'-deoxyadenosyl (dAdo) radical generated from another SAM in the active site."* One SAM is the source of the initiating 5′-deoxyadenosyl radical, while the second SAM mediates hydrogen transfer during radical-based decarboxylation.

### Finding 4 — Cytoplasmic soluble monomer; Anr/Dnr redox regulation; loss-of-function causes coproporphyrin III accumulation

Anaerobically purified HemN is a **monomeric, soluble cytoplasmic protein** of native mass ~52 kDa ([PMID: 12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/)): *"Anaerobically purified HemN is a monomeric protein with a native M(r) = 52,000 +/- 5,000."* This establishes both the oligomeric state (monomer) and subcellular localization (cytoplasm). HemN has no signal peptide or membrane-spanning region, and tetrapyrrole biosynthesis occurs in the bacterial cytoplasm.

In *P. aeruginosa*, hemN is strongly induced under anaerobic conditions through two Fnr-type redox regulators: *"An approximately 10-fold anaerobic induction of hemN gene expression was mediated by the dual action of Anr and a second Fnr-type regulator, Dnr"* ([PMID: 9767567](https://pubmed.ncbi.nlm.nih.gov/9767567/)). The physiological importance is shown by the loss-of-function phenotype: *"An anr mutant did not contain detectable amounts of hemN mRNA and accumulated coproporphyrin III both aerobically and anaerobically, indicating the importance of HemN for aerobic and anaerobic haem formation"* ([PMID: 9767567](https://pubmed.ncbi.nlm.nih.gov/9767567/)). Accumulation of **coproporphyrin III** (the oxidized, aromatized form of unprocessed coproporphyrinogen III) is the diagnostic metabolic signature of a blocked coproporphyrinogen-III oxidase step.

The orthologous *Alcaligenes eutrophus* hemN shows the same logic: Fnr-regulated, O₂-repressed, required for anaerobic growth on nitrate/nitrite, with coproporphyrin III excretion upon inactivation ([PMID: 9396835](https://pubmed.ncbi.nlm.nih.gov/9396835/)). Because *P. putida* KT2440 encodes the Anr regulator and hemN (PP_4264), the same redox-responsive control is expected in the target organism (inferred by orthology).

### Finding 5 — Sequence-level confirmation of catalytic motifs in Q88F35

Direct inspection of the 460-aa, 52.6 kDa *P. putida* KT2440 HemN sequence (Q88F35) confirms the two essential functional motifs at conserved positions:

- The radical-SAM [4Fe-4S]-binding motif **CANICYYC** (a CxxxCxxC motif) at **residues 63–70**, positionally equivalent to the essential Cys62/Cys66/Cys69 of *E. coli* HemN. Their essentiality was established experimentally: *"Cysteine residues Cys(62), Cys(66), and Cys(69) ... are essential for iron-sulfur cluster formation and enzyme function"* ([PMID: 12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/)).
- The **SAM-binding GGGTP motif** at **residues 113–117**, matching the *E. coli* Gly111/Gly113 whose mutation abolished activity: *"Mutation of Gly(111) and Gly(113), which are part of the potential GGGTP S-adenosyl-l-methionine binding motif, completely abolished enzymatic function"* ([PMID: 12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/)).

UniProt (rule-based, PIRNR000167) assigns the exact catalytic reaction (Rhea:15425): **coproporphyrinogen III + 2 SAM → protoporphyrinogen IX + 2 5′-deoxyadenosine + 2 L-methionine + 2 CO₂** (EC 1.3.98.3); cofactor: one [4Fe-4S] cluster coordinated by 3 cysteines plus an exchangeable SAM; pathway: protoporphyrin-IX biosynthesis (protoporphyrinogen-IX from coproporphyrinogen-III, AdoMet route, step 1/1); subcellular location: cytoplasm.

### Finding 6 — A redundant coproporphyrinogen-III oxidase system in *P. putida* KT2440

*P. putida* KT2440 encodes **three coproporphyrinogen-III oxidase-related genes**, giving redundancy across oxygen regimes:

| Gene | Locus | UniProt | Length | EC | Oxygen requirement | Role |
|---|---|---|---|---|---|---|
| **hemF** | PP_0073 | Q88RQ6 | 303 aa | 1.3.3.3 | O₂-**dependent** | Aerobic copro-III oxidase |
| **hemN** (target) | PP_4264 | Q88F35 | 460 aa | 1.3.98.3 | O₂-**independent** | Radical-SAM anaerobic copro-III oxidase |
| HemN-family paralog | PP_3781 | Q88GE3 | 471 aa | (1.3.98.3-type) | O₂-independent (predicted) | Second HemN/HemZ/HemW-type enzyme |

This mirrors the HemF + HemN (+ HemZ) arrangement documented in *P. aeruginosa* ([PMID: 9767567](https://pubmed.ncbi.nlm.nih.gov/9767567/)) and *B. subtilis* ([PMID: 10498703](https://pubmed.ncbi.nlm.nih.gov/10498703/)). In *P. aeruginosa*, *"Mutation of hemN and hemF did not abolish aerobic or anaerobic growth, indicating the existence of an additional HemN-type enzyme, which was termed HemZ"* ([PMID: 9767567](https://pubmed.ncbi.nlm.nih.gov/9767567/)) — paralleling the three *P. putida* genes. **Caveat:** some HemN-family proteins (HemW-type) are radical-SAM heme chaperones rather than coproporphyrinogen oxidases, so PP_3781's exact activity should not be assumed from family membership alone. This redundancy explains why heme synthesis is robust across the aerobic–anaerobic spectrum that *P. putida* encounters in soil and rhizosphere niches, and why loss of a single enzyme is typically non-lethal yet causes coproporphyrin III accumulation when the alternate route cannot compensate.

---

## Mechanistic Model / Interpretation

### Position in the heme biosynthetic pathway

```
  ...  →  Coproporphyrinogen III
                     │
                     │  [Oxidative decarboxylation of 2 propionate → 2 vinyl groups]
                     │
        ┌────────────┴─────────────┐
        │                          │
   O2-DEPENDENT               O2-INDEPENDENT
   HemF (PP_0073)             HemN (PP_4264)  ← TARGET
   EC 1.3.3.3                 EC 1.3.98.3      (+ paralog PP_3781)
   uses O2                    radical-SAM; no O2 required
        │                          │
        └────────────┬─────────────┘
                     ▼
           Protoporphyrinogen IX
                     │
                     ▼  (HemG/HemY protoporphyrinogen oxidase)
             Protoporphyrin IX
                     │
                     ▼  (HemH ferrochelatase)
                   Heme b
```

### Catalytic cycle of HemN (radical-SAM chemistry)

```
   [4Fe-4S]1+  +  SAM(1)  ──►  [4Fe-4S]2+  +  L-Met  +  5'-deoxyadenosyl radical (dAdo•)
                                                              │
                                                              ▼
                        dAdo•  abstracts H from propionate β-carbon of substrate
                                                              │
                                                              ▼
              Substrate radical  →  decarboxylation (–CO2)  →  vinyl group formed
                                                              │
                        SAM(2) acts as H-relay in radical-based H transfer
                                                              │
                                                              ▼
                        Repeat on 2nd propionate (via harderoporphyrinogen intermediate)
                                                              │
                                                              ▼
   Net: Coproporphyrinogen III + 2 SAM  →  Protoporphyrinogen IX
                              + 2 CO2 + 2 5'-deoxyadenosine + 2 L-Met     (Rhea:15425)
```

The coherent picture is of a **cytoplasmic, soluble, monomeric radical-SAM metalloenzyme** that uses an oxygen-sensitive [4Fe-4S] cluster and two SAM cofactors to perform demanding C–C bond chemistry (decarboxylation of unactivated propionate side chains) without molecular oxygen. This capability is precisely why the enzyme exists as a distinct paralog to the oxygen-dependent HemF: it allows the cell to complete heme biosynthesis when oxygen is scarce or absent. In *Pseudomonas*, this need arises under low-oxygen/denitrifying conditions, when the Anr/Dnr regulators induce hemN. The metabolic redundancy — HemF for aerobic conditions, HemN and PP_3781 for anaerobic/microaerobic conditions — insulates the essential supply of heme (for cytochromes, catalases, and other hemoproteins) from the oxygen fluctuations that an environmentally versatile soil/rhizosphere organism like *P. putida* KT2440 routinely experiences.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [12114526](https://pubmed.ncbi.nlm.nih.gov/12114526/) | *Oxygen-independent coproporphyrinogen-III oxidase HemN from E. coli* | Primary biochemistry: reaction, O₂-sensitive Fe-S cluster, essential Cys62/66/69 and GGGTP motif, SAM/NAD(P)H requirement, monomeric cytoplasmic ~52 kDa protein |
| [14633981](https://pubmed.ncbi.nlm.nih.gov/14633981/) | *Crystal structure of coproporphyrinogen III oxidase reveals cofactor geometry of Radical SAM enzymes* | First radical-SAM crystal structure; [4Fe-4S]/SAM coordination; two-SAM binding rationalizing two sequential decarboxylations; confirms essential role in heme biosynthesis |
| [30884058](https://pubmed.ncbi.nlm.nih.gov/30884058/) | *Revisiting the Mechanism of the Anaerobic Coproporphyrinogen III Oxidase HemN* | Sequential decarboxylation via harderoporphyrinogen intermediate; two-SAM hydrogen-relay mechanism |
| [9767567](https://pubmed.ncbi.nlm.nih.gov/9767567/) | *Regulation of P. aeruginosa hemF and hemN by Anr and Dnr* | Anr/Dnr redox regulation (~10-fold anaerobic induction); coproporphyrin III accumulation in anr mutant; evidence for a third HemZ-type enzyme |
| [9396835](https://pubmed.ncbi.nlm.nih.gov/9396835/) | *A. eutrophus hemN required for heme biosynthesis during anaerobic growth* | Ortholog: Fnr-regulated, O₂-repressed, required for anaerobic growth; coproporphyrin III excretion on loss; cross-complements *S. typhimurium* hemF/hemN mutant |
| [10498703](https://pubmed.ncbi.nlm.nih.gov/10498703/) | *Transcriptional control of B. subtilis hemN and hemZ* | Confirms the multi-enzyme redundant copro-III oxidase system and redox-cascade regulation in another bacterium |
| [16218869](https://pubmed.ncbi.nlm.nih.gov/16218869/) | *Structural and functional comparison of HemN to other radical SAM enzymes* | Review placing HemN within the radical-SAM superfamily; notes extreme O₂ sensitivity of the family |
| [15450488](https://pubmed.ncbi.nlm.nih.gov/15450488/) | *Structure and function of radical SAM enzymes* | Review of HemN cofactor geometry and the radical-SAM paradigm |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *Revisited genome of P. putida KT2440* | Genomic/annotation context for the KT2440 metabolic chassis |

All directly cited snippets were verified against the source abstracts. The primary biochemical/structural/mechanistic evidence (PMIDs 12114526, 14633981, 30884058) derives from *E. coli* HemN, and the primary regulatory/phenotypic evidence (PMIDs 9767567, 9396835) from *P. aeruginosa* and *A. eutrophus* orthologs; the transfer to *P. putida* PP_4264 rests on orthology plus direct sequence-motif conservation (Finding 5).

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Evidence |
|---|---|---|
| hemN encodes O₂-independent coproporphyrinogen-III oxidase (copro III → protoporphyrinogen IX) | **Supported** | PMID 12114526, 14633981 |
| HemN is a radical SAM enzyme with a [4Fe-4S] cluster and generates a dAdo radical | **Supported** | PMID 14633981, 12114526 |
| HemN uses two SAM for sequential decarboxylation via harderoporphyrinogen | **Supported** | PMID 14633981, 30884058 |
| HemN acts in the cytoplasm as a soluble monomer | **Supported** | PMID 12114526 |
| hemN is redox-regulated (Anr/Dnr) and functionally important for heme formation in *Pseudomonas* | **Supported** | PMID 9767567, 9396835 |
| P. putida encodes a redundant HemF/HemN/HemN-paralog system | **Supported** | UniProt enumeration; PMID 9767567, 10498703 |
| "hemN" is an ambiguous symbol / wrong-gene risk | **Refuted** | Symbol uniform across bacteria; UniProt domains match |

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 protein.** All enzymatic, structural, and mechanistic data come from orthologs (chiefly *E. coli* HemN). The functional assignment to Q88F35 is by orthology and conserved catalytic motifs, not by direct assay of the *P. putida* enzyme. Confidence is nonetheless high given the family-defining conserved motifs (CXXXCXXC, GGGTP) and unambiguous domain architecture.

2. **Regulation in *P. putida* is inferred, not measured.** Anr/Dnr control of hemN is demonstrated in *P. aeruginosa* and Fnr control in *A. eutrophus*; the presence of Anr and hemN in KT2440 makes the same control likely, but the specific promoter architecture (Anr-box position) and induction magnitude in KT2440 have not been experimentally confirmed. Note also that, unlike *P. aeruginosa*, *P. putida* KT2440 cannot grow by denitrification, so the HemN role likely relates to microaerobic rather than fully anaerobic physiology.

3. **Functional status of the paralog PP_3781 is unverified.** It is annotated as an oxygen-independent coproporphyrinogen-III oxidase family protein, but whether it is catalytically active, whether it is a true HemN/HemZ or a HemW-type radical-SAM heme chaperone, and its physiological contribution in KT2440 are unknown.

4. **Substrate-specificity fine detail.** While the reaction and the ring-A/B propionate targets are established for the family, the precise regiochemical order of the two decarboxylations and any *P. putida*-specific kinetic parameters (K_m, k_cat, redox-partner identity) are undefined.

5. **Physiological reductant in vivo.** In vitro assays used NAD(P)H plus additional cytoplasmic components; the actual in vivo electron donor that reduces the [4Fe-4S] cluster in *P. putida* is not established.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and anaerobic enzyme assay** of recombinant *P. putida* HemN (Q88F35) to directly confirm coproporphyrinogen-III oxidase activity, measure kinetic parameters, and verify harderoporphyrinogen-intermediate formation, closing the orthology-inference gap.

2. **Targeted gene deletion of PP_4264** (and combinatorial deletions with PP_0073/hemF and PP_3781) in KT2440, followed by growth phenotyping across aerobic, microaerobic, and anaerobic conditions, with HPLC/fluorescence monitoring for **coproporphyrin III accumulation** as the diagnostic readout.

3. **Test the redundancy hypothesis directly**: determine whether a hemN single mutant is heme-prototrophic under microaerobiosis (predicting compensation by PP_3781/HemF), and whether a hemN/PP_3781 double mutant becomes conditionally heme-auxotrophic.

4. **Map and validate the Anr/Dnr regulation**: identify Anr/Dnr binding site(s) upstream of PP_4264 and quantify anaerobic/microaerobic induction by RT-qPCR or reporter fusion in wild-type vs. an *anr* mutant of KT2440.

5. **Biochemically characterize PP_3781** to determine whether it is an active anaerobic copro-III oxidase (HemN/HemZ-type) or a HemW-type protein with a different in vivo role.

6. **EPR/Mössbauer or structural analysis** (or a high-confidence AlphaFold model plus cofactor docking) of *P. putida* HemN to confirm the [4Fe-4S] cluster geometry and the two-SAM arrangement predicted from the *E. coli* structure.

---

## Conclusion

*hemN* (PP_4264; UniProt Q88F35) encodes the **oxygen-independent, cytoplasmic, radical-SAM coproporphyrinogen-III oxidase** of *Pseudomonas putida* KT2440. It catalyzes the oxidative decarboxylation of the two ring-A/B propionate side chains of coproporphyrinogen III to yield protoporphyrinogen IX in heme biosynthesis, using a [4Fe-4S] cluster and two SAM molecules to drive sequential radical decarboxylations through a harderoporphyrinogen intermediate. It is the anaerobic counterpart of the oxygen-dependent HemF within a redundant, redox-regulated (Anr/Dnr) system, ensuring heme supply irrespective of oxygen availability. The identity is unambiguous and all diagnostic catalytic motifs are conserved in the target sequence.


## Artifacts

- [OpenScientist final report](hemN-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemN-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12114526
2. PMID:14633981
3. PMID:30884058
4. PMID:9767567
5. PMID:9396835
6. PMID:10498703