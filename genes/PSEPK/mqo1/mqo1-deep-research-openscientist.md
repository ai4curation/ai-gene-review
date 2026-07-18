---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:37:16.263062'
end_time: '2026-07-11T17:51:28.469752'
duration_seconds: 852.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mqo1
  gene_symbol: mqo1
  uniprot_accession: Q88PU7
  protein_description: 'RecName: Full=Probable malate:quinone oxidoreductase 1 {ECO:0000255|HAMAP-Rule:MF_00212};
    EC=1.1.5.4 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=MQO 1 {ECO:0000255|HAMAP-Rule:MF_00212};
    AltName: Full=Malate dehydrogenase [quinone] 1 {ECO:0000255|HAMAP-Rule:MF_00212};'
  gene_info: Name=mqo1 {ECO:0000255|HAMAP-Rule:MF_00212}; Synonyms=mqo-1; OrderedLocusNames=PP_0751;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MQO family. {ECO:0000255|HAMAP-
  protein_domains: FAD/NAD-bd_sf. (IPR036188); MQO. (IPR006231); Mqo (PF06039)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mqo1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mqo1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PU7
- **Protein Description:** RecName: Full=Probable malate:quinone oxidoreductase 1 {ECO:0000255|HAMAP-Rule:MF_00212}; EC=1.1.5.4 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=MQO 1 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=Malate dehydrogenase [quinone] 1 {ECO:0000255|HAMAP-Rule:MF_00212};
- **Gene Information:** Name=mqo1 {ECO:0000255|HAMAP-Rule:MF_00212}; Synonyms=mqo-1; OrderedLocusNames=PP_0751;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MQO family. {ECO:0000255|HAMAP-
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); MQO. (IPR006231); Mqo (PF06039)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mqo1" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mqo1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mqo1** (gene ID: mqo1, UniProt: Q88PU7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *mqo1* (Q88PU7): Probable Malate:Quinone Oxidoreductase 1 of *Pseudomonas putida* KT2440

## Summary

**Mqo1** (gene *mqo1* / *mqo-1*; ordered locus **PP_0751**; UniProt **Q88PU7**) of *Pseudomonas putida* strain KT2440 encodes a **membrane-associated, FAD-dependent malate:quinone oxidoreductase (MQO; EC 1.1.5.4)**. Its primary catalytic function is the oxidation of **L-(S)-malate to oxaloacetate**, coupled to the reduction of a **respiratory quinone** rather than NAD⁺. This reaction is the penultimate step of the tricarboxylic acid (TCA) cycle and, uniquely for MQO-type enzymes, it feeds electrons **directly into the aerobic respiratory electron-transport chain**. In *Pseudomonas*, the physiological electron acceptor is **ubiquinone-9 (coenzyme Q9)**, the characteristic respiratory quinone of the genus. Mqo1 therefore functions simultaneously as a **TCA-cycle enzyme and a primary dehydrogenase of the respiratory chain**, structurally and functionally analogous to succinate dehydrogenase.

The gene identity is well supported. The UniProt accession, HAMAP rule MF_00212 annotation, Pfam domain **Mqo (PF06039)**, and the FAD/NAD(P)-binding domain (IPR036188) all converge on membership in the MQO family. Sequence analysis of the 502-residue, ~54.3 kDa protein reveals the canonical N-terminal dinucleotide-binding Rossmann fingerprint diagnostic of GR2-family FAD oxidoreductases, and an AlphaFold model of very high confidence (mean pLDDT 92.6) supports a well-folded MQO architecture. Global pairwise alignment against the experimentally validated *Escherichia coli* Mqo (P33940) gives ~52% identity — comfortably above the threshold for confident orthology — confirming that Q88PU7 is a bona fide MQO. Notably, *P. putida* KT2440 possesses **three MQO paralogs** (mqo1/PP_0751, mqo2/Q88NF9, mqo3/Q88IS4), with mqo2 and mqo3 forming a closely related duplicated pair (78% identity) and mqo1 being the more divergent isoform.

Physiologically, MQO enzymes across bacteria are most important when high TCA-cycle flux is required — during aerobic growth on organic acids, dicarboxylates, and gluconeogenic substrates. In the close relative *Pseudomonas syringae*, disruption of *mqo* slows growth on dicarboxylates and impairs in-planta fitness and virulence, directly demonstrating the enzyme's role at the malate→oxaloacetate node. Because *P. putida* KT2440 metabolizes glucose through the Entner–Doudoroff pathway and depends on a fully operational TCA cycle, glyoxylate shunt, and gluconeogenesis when growing on organic acids, Mqo1 sits at a metabolically pivotal junction supplying oxaloacetate for both cycle continuation (citrate synthase) and anaplerosis/gluconeogenesis (PEP synthesis). No direct experimental characterization of the *P. putida* KT2440 Mqo1 protein exists; this annotation rests on strong family-level biochemistry, orthology, and bioinformatic inference.

---

## Key Findings

### 1. Mqo1 is an FAD-dependent malate:quinone oxidoreductase catalyzing L-malate → oxaloacetate with a quinone as the electron acceptor

The core enzymatic identity of Mqo1 is established at the family level through direct biochemical characterization of orthologs. In the foundational study of the *Corynebacterium glutamicum* enzyme, purified MQO was shown to **oxidize L-malate to oxaloacetate and donate electrons to ubiquinone-1 and other acceptors — but not to NAD⁺** — establishing that the natural direct acceptor is a quinone ([PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/)). The same work demonstrated that **FAD is a tightly but non-covalently bound prosthetic group**, consistent with the FAD-binding domain annotation of Q88PU7. Independent work on the *Helicobacter pylori* enzyme confirmed that this **"flavin adenine dinucleotide-dependent membrane-associated enzyme donates electrons to quinones of the electron transfer chain"** ([PMID: 10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/)).

The reaction is formally:

> **(S)-malate + a quinone → a quinol + oxaloacetate**  (EC 1.1.5.4, formerly EC 1.1.99.16)

This is distinct from the classic cytoplasmic NAD-dependent malate dehydrogenase (MDH, EC 1.1.1.37): MQO is irreversible under physiological conditions and does not conserve energy as NADH, instead injecting reducing equivalents directly into the membrane quinone pool. Q88PU7 is annotated by HAMAP rule MF_00212 as belonging to the MQO family with Pfam Mqo (PF06039) and the FAD/NAD(P)-binding domain (IPR036188), placing it squarely within this characterized group.

### 2. Mqo is a peripheral inner-membrane protein bridging the TCA cycle and the respiratory chain

MQO occupies an unusual position as both a metabolic-cycle enzyme and a respiratory dehydrogenase. In *C. glutamicum*, **"Mqo is a peripheral membrane protein and can be released from the membrane by addition of chelators,"** and its activity was demonstrated in isolated membranes feeding electrons via the electron-transfer chain to oxygen ([PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/)). In *H. pylori*, the enzyme, **"similar to succinate dehydrogenase, ... is part of both the electron transfer chain and the citric acid cycle"** ([PMID: 10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/)). In the Gram-negative model *E. coli*, the **"membrane-associated malate:quinone-oxidoreductase (MQO; EC 1.1.99.16), encoded by the gene mqo"** is regulated by the ArcA-ArcB aerobic/anaerobic two-component system, with highest expression during exponential aerobic growth ([PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/)).

For Mqo1, this means the enzyme operates as a **peripheral protein on the cytoplasmic face of the inner (plasma) membrane**, where the malate substrate is accessible in the cytoplasm and the quinone acceptor resides in the membrane bilayer.

### 3. In *Pseudomonas*, mqo supports dicarboxylate/TCA-based growth and contributes to niche fitness and virulence

The most direct *Pseudomonas*-specific evidence comes from the close relative *Pseudomonas syringae* pv. tomato DC3000. A Tn5 insertion disrupting *mqo* — described as an enzyme **"of the tricarboxylic acid cycle"** — reduced growth in planta and disease symptoms; the study reported that **"mutants lacking mqo function grow more slowly in culture than wild-type bacteria when dicarboxylates are the only available carbon source,"** and linked the enzyme to apoplastic dicarboxylate utilization alongside the DctA1 transporter ([PMID: 19251849](https://pubmed.ncbi.nlm.nih.gov/19251849/)). In *Pseudomonas fluorescens* In5, a Tn5 insertion upstream of *mqo* altered the hydrogen-cyanide biocontrol phenotype ([PMID: 22417387](https://pubmed.ncbi.nlm.nih.gov/22417387/)). Consistent with a role wherever high TCA flux is needed, in *C. glutamicum* MQO/MDH/SDH activities rise coordinately on lactate, pyruvate, or acetate ([PMID: 11092846](https://pubmed.ncbi.nlm.nih.gov/11092846/)).

### 4. Sequence and bioinformatic analysis confirm a 502-aa (54.3 kDa) FAD-binding MQO

UniProtKB Q88PU7 encodes a **502-residue, 54,282 Da** protein — consistent with the ~50 kDa monomers reported for biochemically purified bacterial MQOs ([PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/); [PMID: 23143325](https://pubmed.ncbi.nlm.nih.gov/23143325/), which reported **"it consists of two subunits with a molecular mass of ~50 kDa"**). The N-terminal sequence (MAQNESVDV**VLVGAGIMS**ATL...) contains the dinucleotide-binding βαβ Rossmann fingerprint (the G-x-G motif within ...VLVGAGIMS...) diagnostic of FAD-binding GR2 oxidoreductases. Curated HAMAP annotation (MF_00212) assigns the catalytic reaction ((S)-malate + quinone = quinol + oxaloacetate), the FAD cofactor, and the TCA-cycle pathway step (oxaloacetate from (S)-malate, quinone route, step 1/1). No experimental PDB structure exists — the AlphaFold model is the only 3D structure available; the KEGG ortholog identifier is ppu:PP_0751.

### 5. *P. putida* KT2440 encodes three MQO paralogs, implying functional redundancy/specialization

A UniProt query of *P. putida* KT2440 (taxid 160488) returns **three** MQO-family proteins: **mqo1 = Q88PU7 / PP_0751 (502 aa)**, **mqo2 = Q88NF9 (527 aa)**, and **mqo3 = Q88IS4 (539 aa)**, all annotated "Probable malate:quinone oxidoreductase." Precedent for redundancy among malate-oxidizing enzymes is strong: in mycobacteria, **"both Mqo and Mdh are found in most bacterial genomes, but the level of functional redundancy between these enzymes remains unclear,"** with Mqo essential on non-fermentable carbon sources ([PMID: 35337802](https://pubmed.ncbi.nlm.nih.gov/35337802/)); and in *E. coli*, **"deletion of the mqo gene did not produce a distinguishable effect on the growth rate, nor did it affect the fitness of the organism in competition with the wild type"** because MDH compensates ([PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/)). This redundancy — three MQO paralogs plus NAD-dependent MDH — is important context for interpreting the likely phenotypic subtlety of any single *mqo1* deletion in *P. putida*.

### 6. All three paralogs are bona fide MQO orthologs; mqo2/mqo3 are a close duplicated pair and mqo1 is the divergent isoform

Global (Needleman-Wunsch) pairwise alignment of the three *P. putida* sequences against the experimentally validated *E. coli* Mqo (UniProt P33940, 548 aa; **"encoded by the gene mqo (previously called yojH)"**, [PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/)) gave the following identities:

| Paralog | UniProt | Length (aa) | % identity to *E. coli* Mqo (P33940) |
|---|---|---|---|
| **mqo1** | Q88PU7 (PP_0751) | 502 | **51.6%** |
| mqo2 | Q88NF9 | 527 | 65.8% |
| mqo3 | Q88IS4 | 539 | 63.0% |

All three are well above the ~30% threshold for confident orthology. Among the paralogs, **mqo2 vs mqo3 = 78.4% identity** (a recent duplication pair), whereas mqo1 shares only ~50% with mqo2 (49.7%) and mqo3 (52.4%), marking mqo1 as the divergent isoform. (Method: simple match/mismatch NW, which approximates but does not replace BLOSUM-based alignment; the relative pattern is robust.)

### 7. The physiological electron acceptor is ubiquinone-9 (Q9)

Because MQO enzymes reduce the membrane quinone pool rather than NAD⁺ ([PMID: 9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/); [PMID: 10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/)), the physiological acceptor is set by the organism's respiratory quinone. *Pseudomonas* species use **coenzyme Q9**: the aerobic membrane respiratory chain of *Pseudomonas aeruginosa* was shown to contain **"soluble flavin, bound flavin, coenzyme Q9, heme b, heme c, and cytochrome o"** arranged as primary dehydrogenase → b → c1 → c → o → oxygen ([PMID: 6766443](https://pubmed.ncbi.nlm.nih.gov/6766443/)). *P. putida* is an obligate aerobe of the same genus using the same ubiquinone-Q9-based chain, so **ubiquinone-9 is the physiological acceptor for Mqo1**.

### 8. Mqo1 operates at the malate→oxaloacetate node, central to growth on organic acids and gluconeogenic substrates

Q88PU7 is annotated in the TCA-cycle pathway (oxaloacetate from (S)-malate, quinone route, step 1/1). *P. putida* KT2440 uses the Entner–Doudoroff pathway for glucose and relies on a fully operational TCA cycle plus glyoxylate shunt and gluconeogenesis when growing on organic acids, coordinated by the HexR regulator — the KT2440 systems-biology study reports **"enhancing pyruvate metabolism, glyoxylate shunt, and gluconeogenesis to support growth"** on gluconeogenic substrates ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)). The oxaloacetate produced by malate oxidation is the substrate for citrate synthase (cycle continuation) and for PEP synthesis/anaplerosis. The functional importance of this node on dicarboxylates is directly demonstrated in *P. syringae* ([PMID: 19251849](https://pubmed.ncbi.nlm.nih.gov/19251849/)).

### 9. The AlphaFold model supports a well-folded MQO/GR2 FAD-oxidoreductase architecture

The AlphaFold DB model for Q88PU7 (502 residues) has **mean pLDDT 92.6 and median 96.2**; 80.3% of residues are "very high" confidence (pLDDT > 90), 95.4% are confident (pLDDT > 70), and only 2.0% are low-confidence (pLDDT < 50). The N-terminal FAD/dinucleotide-binding region (residues 1–60, containing the …VLVGAGIMS… Rossmann fingerprint) has mean pLDDT 93.7. No experimental structure exists; this is a computed model, but its high confidence supports the inferred fold.

---

## Mechanistic Model / Interpretation

Mqo1 sits at the intersection of central carbon metabolism and energy conservation. The following schematic places the enzyme in its metabolic and bioenergetic context:

```
   TCA CYCLE (cytoplasm)                    INNER (PLASMA) MEMBRANE
   ─────────────────────                    ────────────────────────

        fumarate                              cytoplasmic face
           │                                        │
        (fumarase)                                  │
           ▼                                        │
      L-(S)-malate ───────────►  [ Mqo1 · FAD ]  peripheral membrane protein
                                        │
                                        │ 2e⁻
                                        ▼
                              ubiquinone-9 (Q9) ──► reduced to quinol (Q9H2)
        oxaloacetate ◄──────────────────┘                  │
           │                                                ▼
   ┌───────┴─────────┐                          bc1 (b/c1) → cyt c → cyt o oxidase → O2
   ▼                 ▼                                    (proton-motive force → ATP)
citrate synthase   PEP / anaplerosis
(cycle continues)  (gluconeogenesis)
```

**Key mechanistic points:**

1. **Irreversible, energetically "cheap" malate oxidation.** By using quinone (E°' ≈ +0.1 V) rather than NAD⁺ (E°' ≈ −0.32 V) as the acceptor, MQO makes the otherwise thermodynamically unfavorable malate→oxaloacetate step essentially irreversible, pulling TCA-cycle flux forward. This is advantageous during rapid aerobic growth on organic acids where cycle throughput must be high.

2. **Direct coupling to respiration.** Electrons enter the Q9 pool and flow through the *bc1* complex and terminal oxidases (e.g., cytochrome *o*) to O₂, generating proton-motive force. Mqo1 thus behaves as a bona fide primary dehydrogenase of the respiratory chain, exactly parallel to succinate dehydrogenase — the analogy explicitly drawn for the *H. pylori* enzyme ([PMID: 10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/)).

3. **A redundant, multi-enzyme node.** *P. putida* KT2440 encodes three MQO paralogs plus NAD-dependent MDH. The likely division of labor — one or more MQO isoforms as the dominant workhorse, MDH providing a reversible NAD-linked route for gluconeogenic oxaloacetate reduction — mirrors the coupled MQO/MDH "malate–oxaloacetate cycling" documented in *C. glutamicum* ([PMID: 11092846](https://pubmed.ncbi.nlm.nih.gov/11092846/)). Redundancy predicts that single deletions may be phenotypically silent under nutrient-rich conditions, becoming consequential specifically on non-fermentable/organic-acid carbon sources ([PMID: 11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/); [PMID: 35337802](https://pubmed.ncbi.nlm.nih.gov/35337802/)).

**Comparison of malate-oxidizing enzymes:**

| Property | Mqo1 (MQO) | Cytoplasmic MDH |
|---|---|---|
| EC number | 1.1.5.4 | 1.1.1.37 |
| Cofactor | FAD (non-covalent) | none (NAD-dependent) |
| Electron acceptor | quinone (Q9) | NAD⁺ |
| Localization | peripheral inner-membrane | cytoplasmic |
| Reversibility | effectively irreversible | reversible (favors OAA→malate) |
| Energy conservation | via respiratory chain (PMF) | as soluble NADH |
| Primary role | forward TCA flux + respiration | gluconeogenic OAA reduction / redox balance |

---

## Evidence Base

| PMID | Organism / topic | How it supports the annotation |
|---|---|---|
| [9660197](https://pubmed.ncbi.nlm.nih.gov/9660197/) | *C. glutamicum* MQO, purified & characterized | Defines substrate (L-malate), product (oxaloacetate), quinone acceptor, non-covalent FAD, peripheral membrane localization, ~50 kDa monomer |
| [10809701](https://pubmed.ncbi.nlm.nih.gov/10809701/) | *H. pylori* MQO | Confirms FAD dependence, quinone acceptor, and the dual TCA-cycle/electron-transport-chain role (SDH analogy) |
| [11092847](https://pubmed.ncbi.nlm.nih.gov/11092847/) | *E. coli* MQO vs MDH | Membrane association, gene identity (mqo/yojH = P33940), ArcAB regulation, redundancy with MDH (silent single deletion) — the validated ortholog reference |
| [11092846](https://pubmed.ncbi.nlm.nih.gov/11092846/) | *C. glutamicum* MQO/MDH | Coordinated up-regulation on lactate/pyruvate/acetate; MQO/MDH malate–OAA cycling; MQO essential on minimal medium |
| [19251849](https://pubmed.ncbi.nlm.nih.gov/19251849/) | *P. syringae* pv. tomato *mqo* | **Closest experimental relative**: mqo is a TCA-cycle enzyme; disruption slows dicarboxylate growth and reduces in-planta virulence |
| [22417387](https://pubmed.ncbi.nlm.nih.gov/22417387/) | *P. fluorescens* In5 | Tn5 insertion upstream of *mqo* alters HCN biocontrol phenotype (Pseudomonas context) |
| [6766443](https://pubmed.ncbi.nlm.nih.gov/6766443/) | *P. aeruginosa* respiratory chain | Establishes ubiquinone-Q9 as the genus's respiratory quinone — the physiological acceptor |
| [23143325](https://pubmed.ncbi.nlm.nih.gov/23143325/) | *Bacillus* sp. PS3 MQO | Independent ~50 kDa subunit measurement matching the predicted mass of Q88PU7 |
| [35337802](https://pubmed.ncbi.nlm.nih.gov/35337802/) | Mycobacterial Mqo/Mdh | Redundancy/energetics of malate oxidation; Mqo essential on non-fermentable carbon |
| [41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/) | *P. putida* KT2440 HexR | Metabolic context: glyoxylate shunt + gluconeogenesis activation on gluconeogenic substrates |

Additional corroborating literature documents MQO as a stress/virulence-relevant TCA enzyme in diverse taxa — *M. tuberculosis* ([PMID: 37689346](https://pubmed.ncbi.nlm.nih.gov/37689346/)), *S. aureus* ([PMID: 26851155](https://pubmed.ncbi.nlm.nih.gov/26851155/)), and gluconeogenic soil mycobacteria ([PMID: 23064972](https://pubmed.ncbi.nlm.nih.gov/23064972/)) — reinforcing the enzyme's general role at the malate→oxaloacetate node during respiratory/organic-acid growth.

**No contradicting evidence** was found: every characterized MQO ortholog agrees on FAD dependence, malate→oxaloacetate chemistry, quinone acceptor, and membrane association.

---

## Limitations and Knowledge Gaps

1. **No direct experimental data on Q88PU7 itself.** The annotation is a high-confidence inference from family-level biochemistry, orthology (~52% identity to *E. coli* Mqo), curated HAMAP rules, and an AlphaFold model. The *P. putida* KT2440 Mqo1 protein has never been purified, kinetically characterized, or crystallized.

2. **Paralog division of labor is unresolved.** With three MQO paralogs (mqo1/mqo2/mqo3) plus MDH, the specific physiological contribution of *mqo1* — whether it is the dominant isoform, condition-specific, or largely redundant — is unknown. Its status as the divergent paralog (~50% identity to mqo2/mqo3) hints at possible functional specialization or altered regulation, but this is untested.

3. **Electron acceptor inferred, not measured.** Ubiquinone-9 is assigned by genus-level analogy to *P. aeruginosa*; the specific quinone kinetics of *P. putida* Mqo1 have not been measured.

4. **Localization topology.** Peripheral, cytoplasmic-face association is inferred from orthologs; the exact membrane-binding determinants and orientation in *P. putida* are not experimentally defined.

5. **Regulation.** Whether *mqo1* is under HexR, ArcAB-like, or carbon-source-responsive control in *P. putida* is not established, though such regulation is documented for orthologs.

6. **Methodological caveat.** The orthology percentages derive from a simplified Needleman-Wunsch match/mismatch scheme rather than BLOSUM-scored alignment; absolute values are approximate, though the relative ranking (mqo2/mqo3 pair vs divergent mqo1) is robust.

---

## Proposed Follow-up Experiments / Actions

1. **Single and combinatorial gene deletions.** Construct Δ*mqo1*, Δ*mqo2*, Δ*mqo3*, and multiple-knockout strains in *P. putida* KT2440; phenotype growth on glucose (ED pathway) versus malate, succinate, acetate, and other organic acids/gluconeogenic substrates to reveal condition-specific and redundant contributions.

2. **Biochemical characterization.** Heterologously express and purify Mqo1; confirm FAD content, measure kinetics (Km for L-malate, quinone analogs Q0/Q1/Q9), and verify strict L-malate (S-malate) stereospecificity and lack of NAD⁺ activity.

3. **Quinone specificity assay.** Test electron transfer to ubiquinone-9 versus shorter-chain analogs in reconstituted membrane vesicles to confirm the Q9 assignment.

4. **Localization.** Fractionate cells and use membrane/chelator-release assays (as in *C. glutamicum*) plus fluorescent fusions to confirm peripheral, cytoplasmic-face inner-membrane localization.

5. **Regulation and expression.** Perform RNA-seq/RT-qPCR of the three paralogs across carbon sources and aerobic/microaerobic conditions; test HexR and ArcAB-type regulatory dependencies.

6. **Structural validation.** Pursue an experimental structure (cryo-EM or X-ray) to validate the AlphaFold model, define the FAD- and quinone-binding sites, and enable comparison with the recently modeled *S. aureus* Mqo/Lqo active sites ([PMID: 26851155](https://pubmed.ncbi.nlm.nih.gov/26851155/)).

7. **Fitness/virulence relevance.** Given the *P. syringae* precedent, assay whether *mqo* isoforms affect *P. putida* rhizosphere colonization and fitness on plant-derived dicarboxylates.

---

## Conclusion

Mqo1 (PP_0751, Q88PU7) is, with high confidence, the canonical isoform of *P. putida* KT2440's FAD-dependent malate:quinone oxidoreductase family. It catalyzes the oxidation of L-(S)-malate to oxaloacetate in the TCA cycle while transferring electrons directly to the respiratory ubiquinone-9 pool, thereby functioning simultaneously as a metabolic enzyme and a primary respiratory dehydrogenase at the cytoplasmic face of the inner membrane. Its importance is greatest during aerobic growth on organic-acid and gluconeogenic substrates. This annotation rests on robust family-level biochemistry, strong orthology to the experimentally validated *E. coli* enzyme, curated database rules, and a very-high-confidence structural model, tempered by the absence of direct experimental study of the *P. putida* protein and the unresolved division of labor among its three MQO paralogs.


## Artifacts

- [OpenScientist final report](mqo1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mqo1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9660197
2. PMID:10809701
3. PMID:11092847
4. PMID:19251849
5. PMID:22417387
6. PMID:11092846
7. PMID:23143325
8. PMID:35337802
9. PMID:6766443
10. PMID:41260329
11. PMID:37689346
12. PMID:26851155
13. PMID:23064972