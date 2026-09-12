---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T19:10:28.293824'
end_time: '2026-07-11T19:27:43.116250'
duration_seconds: 1034.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lpdV
  gene_symbol: lpdV
  uniprot_accession: Q88EP9
  protein_description: 'RecName: Full=Dihydrolipoyl dehydrogenase {ECO:0000256|ARBA:ARBA00016961,
    ECO:0000256|RuleBase:RU003692}; EC=1.8.1.4 {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692};'
  gene_info: Name=lpdV {ECO:0000313|EMBL:AAN69982.1}; OrderedLocusNames=PP_4404 {ECO:0000313|EMBL:AAN69982.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-I pyridine nucleotide-disulfide
  protein_domains: Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188);
    FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156);
    Lipoamide_DH. (IPR006258)
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lpdV-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lpdV-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EP9
- **Protein Description:** RecName: Full=Dihydrolipoyl dehydrogenase {ECO:0000256|ARBA:ARBA00016961, ECO:0000256|RuleBase:RU003692}; EC=1.8.1.4 {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692};
- **Gene Information:** Name=lpdV {ECO:0000313|EMBL:AAN69982.1}; OrderedLocusNames=PP_4404 {ECO:0000313|EMBL:AAN69982.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-I pyridine nucleotide-disulfide
- **Key Domains:** Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156); Lipoamide_DH. (IPR006258)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lpdV" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lpdV' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lpdV** (gene ID: lpdV, UniProt: Q88EP9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lpdV* (Q88EP9, PP_4404) — LPD-val, the Branched-Chain Keto Acid Dehydrogenase-Specific E3 of *Pseudomonas putida* KT2440

**UniProt:** Q88EP9 · **Gene:** *lpdV* · **Locus:** PP_4404 · **EC 1.8.1.4** · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)

---

## Summary

The gene **lpdV** of *Pseudomonas putida* KT2440 (UniProt **Q88EP9**; ordered locus **PP_4404**) encodes **LPD-val**, a **dihydrolipoyl dehydrogenase** (also called dihydrolipoamide dehydrogenase or lipoamide dehydrogenase; **EC 1.8.1.4**). LPD-val is the **E3 component** of the **branched-chain keto acid dehydrogenase (BCKAD) multienzyme complex**. It is a homodimeric FAD-containing flavoprotein belonging to the **class-I pyridine nucleotide-disulfide oxidoreductase family**, and it carries out the terminal, electron-recycling step of the complex: it re-oxidizes the reduced dihydrolipoyl group covalently tethered to the E2 core and passes the electrons to NAD⁺, regenerating the oxidized lipoyl cofactor and producing NADH. The net half-reaction is **dihydrolipoamide + NAD⁺ → lipoamide + NADH + H⁺**. This function has been established by decades of direct biochemical, genetic, and sequence work in *P. putida*, and is corroborated here by direct analysis of the Q88EP9 sequence, the KT2440 genome annotation, and the AlphaFold structural model.

The distinguishing feature of LPD-val is its **substrate/complex specificity**. *P. putida* produces three separate lipoamide dehydrogenases: **LPD-glc** (the housekeeping E3 shared by the pyruvate and 2-oxoglutarate dehydrogenase complexes and the glycine-cleavage system), **LPD-3** (function unknown), and **LPD-val** (dedicated to BCKAD). Reconstitution experiments showed that a lipoamide-dehydrogenase-deficient BCKAD preparation was stimulated **10-fold specifically by LPD-val, but not by LPD-glc**; the reciprocal specificity holds for 2-oxoglutarate dehydrogenase, which is served by LPD-glc and not LPD-val. LPD-val therefore represents a case of paralogous functional specialization: a deeply divergent E3 (~39 % amino-acid identity to LPD-glc) evolved to serve one particular oxo-acid dehydrogenase complex.

Functionally, LPD-val operates **in the cytoplasm** as part of the branched-chain amino acid (valine, leucine, isoleucine) catabolic pathway. It is the terminal gene of the **bkd operon** (*bkdAA–bkdAB–bkdB–lpdV*), which is transcribed as a single ~6.2 kb message, activated by the Lrp-family regulator **BkdR** in the presence of L-branched-chain amino acid inducers, and subject to **Crc-mediated catabolite repression**. The BCKAD complex it serves catalyzes the oxidative decarboxylation of the branched-chain 2-oxo acids (2-ketoisovalerate, 2-ketoisocaproate, 2-keto-3-methylvalerate) derived from Val/Leu/Ile, feeding branched-chain acyl-CoA products into downstream catabolism. This report presents the full evidence base for these conclusions.

---

## Key Findings

### Finding 1 — *lpdV* encodes the dedicated E3 (dihydrolipoamide dehydrogenase) of the *P. putida* BCKAD complex

The structural gene *lpdV* consists of **459 codons plus a stop codon** (66.3 % G+C) and encodes a protein of predicted mass **Mr ≈ 48,164** (≈ 48,949 with bound FAD), consistent with the ~49 kDa LPD-val band observed on SDS-PAGE. The gene lies at the **3′ end of the bkd operon**, its open reading frame beginning just **two bases after the stop codon of the E2 (bkdB) gene** ([PMID: 2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/)). This tight genetic coupling to the E2 gene is the first indication that its product is the E3 of the same complex.

The functional assignment rests on a decisive **reconstitution experiment**: a purified branched-chain keto acid dehydrogenase preparation that had lost its lipoamide-dehydrogenase activity was **stimulated 10-fold by LPD-val but not by LPD-glc (LPD-glu)**, whereas 2-ketoglutarate dehydrogenase was stimulated by LPD-glc and not by LPD-val ([PMID: 6895373](https://pubmed.ncbi.nlm.nih.gov/6895373/)). This demonstrates that the *P. putida* BCKAD complex has a **specific requirement for LPD-val**, and that LPD-val is not interchangeable with the housekeeping E3. Together these results define *lpdV* as the LPD-val structural gene and identify its product as the complex-specific E3.

> "The nucleotide sequence of the structural gene for LPD-val, lpdV, was determined and consists of 459 codons plus the stop codon. The open reading frame begins two bases after the stop codon for the E2 subunit" — [PMID: 2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/)

> "A purified preparation of branched-chain keto acid dehydrogenase, which was deficient in lipoamide dehydrogenase, was stimulated 10-fold by LPD-val but not by LPD-glu, which suggested that the branched-chain keto acid dehydrogenase of P. putida has a specific requirement for LPD-val." — [PMID: 6895373](https://pubmed.ncbi.nlm.nih.gov/6895373/)

### Finding 2 — LPD-val is an FAD-containing, redox-active-disulfide flavoprotein of the class-I pyridine nucleotide-disulfide oxidoreductase family (EC 1.8.1.4)

LPD-val's deduced sequence groups it with other lipoamide dehydrogenases — a subclass of **redox-active disulfide flavoproteins**. A diagnostic C-terminal CNBr peptide with the sequence **TIHAHPTL** is shared by LPD-val of *P. putida*, the analogous enzyme of *P. aeruginosa*, and *E. coli* lipoamide dehydrogenase — a signature **not found in any other flavoprotein** in the Dayhoff database, which the authors proposed as characteristic of lipoamide dehydrogenase ([PMID: 3085653](https://pubmed.ncbi.nlm.nih.gov/3085653/); [PMID: 2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/)).

The catalytic machinery of this family is well established from mechanistic studies of homologous E3 enzymes. Each subunit carries a **non-covalently bound FAD** and a **redox-active cystine disulfide**, with a **His–Glu active-site diad** (His450–Glu455 in *Azotobacter vinelandii*) acting as the catalytic base. The enzyme runs a **ping-pong kinetic mechanism**, with NADH formation being rate-limiting in the physiological direction ([PMID: 1633804](https://pubmed.ncbi.nlm.nih.gov/1633804/)). Crystallographic work on the human orthologue shows that during the reductive half-reaction the **nicotinamide ring of NAD(H) stacks directly on the isoalloxazine ring of FAD**, enabling hydride transfer ([PMID: 15946682](https://pubmed.ncbi.nlm.nih.gov/15946682/)). These conserved features define the reaction chemistry LPD-val performs.

> "All three peptides had a common segment of eight amino acids, with the sequence TIHAHPTL. This homology was not evident in any other flavoproteins in the Dayhoff data base which suggests that this sequence might be characteristic of lipoamide dehydrogenase." — [PMID: 3085653](https://pubmed.ncbi.nlm.nih.gov/3085653/)

> "The wild-type enzyme functions according to a ping-pong mechanism in the physiological reaction in which the formation of NADH is rate-limiting." — [PMID: 1633804](https://pubmed.ncbi.nlm.nih.gov/1633804/)

> "When NADH is present, however, the nicotinamide base stacks directly on the isoalloxazine ring system of the FAD." — [PMID: 15946682](https://pubmed.ncbi.nlm.nih.gov/15946682/)

### Finding 3 — LPD-val functions in branched-chain amino acid catabolism as part of the bkd-encoded BCKAD complex, under BkdR activation and catabolite repression

The **bkd operon** encodes the four proteins of the BCKAD multienzyme complex: **E1α (bkdA1/bkdAA)**, **E1β (bkdA2/bkdAB)**, **E2 dihydrolipoyl transacylase (bkdB)**, and **E3 dihydrolipoyl dehydrogenase (lpdV)**. A single **~6.2 kb transcript** spans all structural genes ([PMID: 2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/); [PMID: 10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/)).

The complex's **substrate specificity** was defined directly: the purified enzyme is active with **2-ketoisovalerate, 2-ketoisocaproate, and 2-keto-3-methylvalerate** in a ratio of **1.0 : 0.8 : 0.7**, but shows **no activity with pyruvate or 2-ketoglutarate**. It converts 2-keto-[1-¹⁴C]isovalerate to CO₂, isobutyryl-CoA and NADH in equimolar amounts ([PMID: 7298579](https://pubmed.ncbi.nlm.nih.gov/7298579/)). These three substrates are the 2-oxo acids derived from valine, leucine and isoleucine, respectively, so LPD-val serves the committed oxidative-decarboxylation step of branched-chain amino acid catabolism.

Consistent with this role, the BCKAD complex is **induced by growth on valine, leucine, or isoleucine** ([PMID: 5030618](https://pubmed.ncbi.nlm.nih.gov/5030618/)). Transcription of the operon requires the **Lrp-family activator BkdR** together with an **L-branched-chain amino acid (or D-leucine) inducer**, with half-maximal transcription at ~2.8 mM L-valine ([PMID: 10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/)). Superimposed on this is **carbon catabolite repression mediated by Crc**, documented in both *P. putida* and *P. aeruginosa* ([PMID: 10648542](https://pubmed.ncbi.nlm.nih.gov/10648542/)). Thus LPD-val's expression is tightly coupled to the availability of its pathway's substrates and to the cell's carbon status.

> "The purified enzyme was active with 2-ketoisovalerate, 2-ketoisocaproate, and 2-keto-3-methylvalerate in a ratio of 1.0:0.8:0.7 but showed no activity with either pyruvate or 2-ketoglutarate." — [PMID: 7298579](https://pubmed.ncbi.nlm.nih.gov/7298579/)

> "BkdR is the transcriptional activator of the bkd operon, which encodes the four proteins of the branched-chain keto acid dehydrogenase multienzyme complex of Pseudomonas putida." — [PMID: 10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/)

> "The bkd operons of P. putida and P. aeruginosa encode the inducible multienzyme complex branched-chain keto acid dehydrogenase, which is regulated in both species by catabolite repression. We report here that this effect is mediated in both species by Crc." — [PMID: 10648542](https://pubmed.ncbi.nlm.nih.gov/10648542/)

### Finding 4 — Direct sequence analysis of Q88EP9 confirms the two-Rossmann-fold architecture, redox-active disulfide, and catalytic motifs of dihydrolipoyl dehydrogenase

Direct analysis of the 459-residue Q88EP9 sequence identifies all the diagnostic features of the family:

| Motif / feature | Residues | Sequence | Role |
|---|---|---|---|
| N-terminal FAD-binding Rossmann fingerprint | 13–18 | GGGPGG (GxGxxG) | FAD dinucleotide binding |
| Redox-active disulfide (Lipoamide_DH signature) | 44 / 49 | GGTC**44**LNIGC**49** (Cys-x₄-Cys) | Catalytic cystine — electron relay from lipoyl to FAD |
| NAD-binding Rossmann fingerprint | 176–181 | VVVGGGYIG | NAD⁺/NADH binding |
| FAD-associated motif | ~302 | WAIGD | FAD environment |
| Lipoamide-DH signature (catalytic His) | 434–441 | TIHAHPTL (His436/His438) | Active-site base (His–Glu diad) |

These features exactly match the **class-I pyridine nucleotide-disulfide oxidoreductase / Lipoamide_DH (IPR006258)** architecture assigned in UniProt, and correspond one-to-one to the catalytic elements established mechanistically for the homologous enzymes in Finding 2. The presence of **two separate Rossmann folds** (one for FAD, one for NAD) and the **Cys-x₄-Cys redox disulfide** places Q88EP9 unambiguously in the dihydrolipoyl dehydrogenase subfamily.

### Finding 5 — In the KT2440 genome, PP_4404/lpdV is the fourth, contiguous gene of the bkd operon, confirming strain-specific identity

Genome coordinates for *P. putida* KT2440 place four co-oriented, tightly abutting genes:

| Locus | Gene | Component | KEGG / EC | Coordinates |
|---|---|---|---|---|
| PP_4401 | bkdAA | E1α | K00166, EC 1.2.4.4 | 4,992,044–4,993,276 |
| PP_4402 | bkdAB | E1β | K00167, EC 1.2.4.4 | 4,993,317–4,994,336 |
| PP_4403 | bkdB | E2 (dihydrolipoyl transacylase) | K09699, EC 2.3.1.168 | 4,994,337–4,995,608 |
| **PP_4404** | **lpdV** | **E3 (dihydrolipoyl dehydrogenase)** | **K00382, EC 1.8.1.4** | **4,995,611–4,996,990** |

*lpdV* begins only **3 bp after the bkdB stop codon** (4,995,608 → 4,995,611), exactly matching the "two bases after the E2 stop codon" junction reported for the cloned operon ([PMID: 2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/)). The adjacent PP_4405 (a sensory-box protein) is on the opposite strand and outside the operon. KEGG annotates PP_4404 as "dihydrolipoyl dehydrogenase component of branched-chain alpha-keto acid dehydrogenase complex" (K00382), UniProt Q88EP9, NCBI AAN69982. This anchors the target protein to the correct strain-specific locus and operon context, satisfying the gene-identity verification required for this annotation.

### Finding 6 — The AlphaFold model of Q88EP9 shows a formed redox-active disulfide and a cross-subunit active site typical of homodimeric E3 enzymes

The AlphaFold DB model **AF-Q88EP9-F1 (v6)** is of very high confidence: mean per-residue **pLDDT = 97.4**, with 97.8 % of residues above 90 and all catalytic residues above 97 (Gly13 98.8, Cys44 97.2, Cys49 97.1, Gly180 97.6, Trp302 98.9, His436 98.8, His438 98.3). The two active-site cysteines identified by sequence analysis are modeled as a **bona fide disulfide bond: Cys44 Sγ–Cys49 Sγ = 2.05 Å**, the canonical S–S distance, i.e. the resting **oxidized redox-active center**.

Within a single subunit, the catalytic His of the TIHAHPTL motif (His438–Pro439) lies **~27 Å from that subunit's own disulfide**, while His436 pairs with a nearby Glu carboxylate (Glu443, ~8 Å), consistent with the **His–Glu catalytic diad**. The large His-to-own-disulfide distance indicates that, as in all characterized E3 enzymes, **the active site is completed in *trans* by the partner monomer** — confirming that LPD-val must function as a homodimer, with each active site built from residues of both subunits.

### Finding 7 — LPD-val is a deeply divergent E3 paralog reflecting ancient duplication and functional specialization for BCKAD

*P. putida* KT2440 carries exactly **three K00382 dihydrolipoyl-dehydrogenase paralogs**: **PP_4404/lpdV (LPD-val)**, **PP_4187/lpdG (LPD-glc)**, and **PP_5366/lpd (LPD-3)** — matching the three lipoamide dehydrogenases described biochemically by Palmer et al. ([PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/)). Global (Needleman–Wunsch, BLOSUM62) alignment shows LPD-val is markedly divergent from its paralogs and orthologues:

| Pair | % identity |
|---|---|
| LPD-val vs LPD-glc (housekeeping) | 38.9 % |
| LPD-val vs LPD-3 | 42.4 % |
| LPD-val vs *E. coli* Lpd | 37.1 % |
| LPD-val vs human DLD | 35.4 % |
| LPD-glc vs LPD-3 | 48.4 % |
| LPD-glc vs *E. coli* Lpd | 40.8 % |

The **LPD-glc/LPD-3 pair are more similar to each other (48.4 %) than either is to LPD-val**, and the housekeeping LPD-glc is even closer to *E. coli* Lpd (40.8 %) than LPD-val is (37.1 %). This pattern indicates that LPD-val diverged **anciently** and specialized for the BCKAD role, while retaining the essential catalytic Cys-x₄-Cys disulfide and His–Glu diad. The three-paralog architecture explains how *P. putida* dedicates a distinct E3 to branched-chain amino acid catabolism.

> "Pseudomonas putida is able to produce three lipoamide dehydrogenases: (i) LPD-glc, which is the E3 component of the pyruvate and 2-ketoglutarate dehydrogenase complexes and the L-factor for the glycine oxidation system; (ii) LPD-val, which is the specific E3 component of the branched-chain keto acid dehydrogenase complex and is induced by growth on leucine, isoleucine, or valine; and (iii) LPD-3, which was discovered in a lpdG mutant and whose role is unknown." — [PMID: 1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/)

---

## Mechanistic Model / Interpretation

### The BCKAD complex and LPD-val's place in it

The branched-chain keto acid dehydrogenase complex is a large, multi-copy assembly built on an E2 core, decorated with E1 and E3 components. It performs the irreversible oxidative decarboxylation of branched-chain 2-oxo acids in three coupled steps:

```
                Branched-chain 2-oxo acid (e.g. 2-ketoisovalerate)
                                │
                                ▼
   ┌─────────── E1 (bkdAA/bkdAB, α2β2, ThDP) ───────────┐
   │   Decarboxylation; hydroxyacyl-ThDP intermediate    │
   │   → reductive acylation of E2's lipoyl-lysine arm   │
   └─────────────────────────────────────────────────────┘
                                │ CO2 released
                                ▼
   ┌─────────── E2 (bkdB, dihydrolipoyl transacylase) ───┐
   │   Acyl group transferred to CoA → branched acyl-CoA │
   │   Lipoyl arm left REDUCED (dihydrolipoamide)        │
   └─────────────────────────────────────────────────────┘
                                │ isobutyryl-CoA out
                                ▼
   ┌─────────── E3 = LPD-val (lpdV, FAD) ── HOMODIMER ────┐
   │   Reoxidizes dihydrolipoamide on E2's swinging arm  │
   │   Electrons: dihydrolipoyl → Cys44–Cys49 → FAD → NAD+│
   │   dihydrolipoamide + NAD+ → lipoamide + NADH + H+    │
   └─────────────────────────────────────────────────────┘
                                │
                                ▼
                        NADH (to respiratory chain)
                 + regenerated oxidized lipoyl arm (next cycle)
```

LPD-val performs the **third, electron-recycling step**. Without it, the lipoyl arms of E2 would remain reduced and the complex would stall after one turnover. LPD-val's job is to **reset the lipoyl cofactor and export the reducing equivalents as NADH**.

### The catalytic cycle of LPD-val

The enzyme cycles between oxidized (EQ) and two-electron-reduced (EH₂) states via a ping-pong mechanism ([PMID: 1633804](https://pubmed.ncbi.nlm.nih.gov/1633804/)):

1. **Reductive (lipoyl) half-reaction.** The dihydrolipoyl group on E2's swinging lysine arm reduces the enzyme's **redox-active disulfide (Cys44–Cys49)**, forming a transient charge-transfer complex. The His436/His438–Glu443 diad acts as a general base, deprotonating the incoming dithiol. Electrons pass from the nascent enzyme dithiol to the **FAD**.
2. **Oxidative (NAD⁺) half-reaction.** Reduced FADH⁻ transfers a hydride to **NAD⁺**, whose nicotinamide ring stacks on the isoalloxazine ring ([PMID: 15946682](https://pubmed.ncbi.nlm.nih.gov/15946682/)), producing **NADH** and regenerating oxidized FAD and the Cys44–Cys49 disulfide.

The AlphaFold model captures the **resting oxidized state**: Cys44–Cys49 is a closed 2.05 Å disulfide (Finding 6). Because the catalytic His of one subunit sits ~27 Å from its own disulfide, each functional active site is assembled **across the dimer interface** — a hallmark of E3 enzymes and the reason LPD-val is obligately homodimeric.

### Why a dedicated E3?

*P. putida* keeps three E3 paralogs (Finding 7) and partitions them by complex. The reconstitution data (Finding 1) show this partitioning is **functionally strict**: LPD-val serves BCKAD, LPD-glc serves pyruvate/2-oxoglutarate dehydrogenase and glycine cleavage. The ~39 % identity between LPD-val and LPD-glc, and the fact that LPD-glc clusters with *E. coli* Lpd rather than with LPD-val, indicate that LPD-val is an **anciently duplicated, specialized isoform** rather than a recent redundant copy. Embedding *lpdV* as the terminal gene of the bkd operon (Findings 1, 5) ensures the specialized E3 is **co-expressed stoichiometrically with its E1 and E2 partners** whenever branched-chain amino acids are available — regulation achieved through BkdR activation and Crc catabolite repression (Finding 3).

### Localization

All evidence places LPD-val in the **bacterial cytoplasm**, where it is assembled into the soluble BCKAD complex. There is no signal peptide or membrane-anchoring feature; the NADH it produces is delivered to the cytoplasmic/membrane respiratory machinery. Its "location of function" is therefore the cytoplasmic BCKAD assembly, physically tethered to the E2 core via its interaction with the swinging lipoyl-lysine arms.

---

## Evidence Base

| PMID | Title (abbreviated) | Contribution |
|---|---|---|
| [2917566](https://pubmed.ncbi.nlm.nih.gov/2917566/) | *Sequence analysis of the lpdV gene…* | Defines lpdV (459 codons), places it 2 bp after E2 stop; operon organization |
| [6895373](https://pubmed.ncbi.nlm.nih.gov/6895373/) | *Isolation of a specific lipoamide dehydrogenase…* | Reconstitution: BCKAD stimulated 10× by LPD-val, not LPD-glc — proves complex specificity |
| [7298579](https://pubmed.ncbi.nlm.nih.gov/7298579/) | *Purification of a branched-chain keto acid dehydrogenase…* | Substrate specificity (three branched 2-oxo acids; no pyruvate/2-KG); products |
| [3085653](https://pubmed.ncbi.nlm.nih.gov/3085653/) | *Resolution of branched-chain oxo acid dehydrogenase of P. aeruginosa* | TIHAHPTL lipoamide-DH signature motif |
| [1633804](https://pubmed.ncbi.nlm.nih.gov/1633804/) | *Lipoamide dehydrogenase from A. vinelandii: His450-Glu455 diad* | Catalytic diad and ping-pong mechanism |
| [15946682](https://pubmed.ncbi.nlm.nih.gov/15946682/) | *Crystal structure of human dihydrolipoamide dehydrogenase* | NAD(H)–FAD stacking; structural basis of hydride transfer |
| [10217783](https://pubmed.ncbi.nlm.nih.gov/10217783/) | *In vitro transcriptional studies of the bkd operon…* | Operon = four proteins incl. lpdV; BkdR + L-BCAA/D-Leu inducers |
| [5030618](https://pubmed.ncbi.nlm.nih.gov/5030618/) | *Regulation of valine catabolism in P. putida* | BCKAD induced by Val/Leu/Ile |
| [10648542](https://pubmed.ncbi.nlm.nih.gov/10648542/) | *Crc is involved in catabolite repression…* | Crc-mediated catabolite repression of the bkd operon |
| [1902462](https://pubmed.ncbi.nlm.nih.gov/1902462/) | *Cloning and sequence analysis of the LPD-glc gene…* | Three-paralog architecture; roles of LPD-glc, LPD-val, LPD-3 |

Supporting regulatory literature (BkdR mechanism) includes the demonstration of BkdR binding stoichiometry (three tetramers per DNA molecule; [PMID: 8670279](https://pubmed.ncbi.nlm.nih.gov/8670279/)), the BkdR–DNA bend and cooperative binding model ([PMID: 9068646](https://pubmed.ncbi.nlm.nih.gov/9068646/)), and BkdR–DNA footprinting ([PMID: 7836297](https://pubmed.ncbi.nlm.nih.gov/7836297/)). Cross-family structural comparison confirms the conserved FAD/NAD(P)H fold across DLD, GSR, TrxR and AIF ([PMID: 40451368](https://pubmed.ncbi.nlm.nih.gov/40451368/)) and the mechanistic logic of pyridine nucleotide-disulfide oxidoreductases ([PMID: 7557016](https://pubmed.ncbi.nlm.nih.gov/7557016/)). The broader branched-chain catabolic context (leucine and isoleucine pathways) is documented in [PMID: 4150714](https://pubmed.ncbi.nlm.nih.gov/4150714/) and [PMID: 4150713](https://pubmed.ncbi.nlm.nih.gov/4150713/).

**Concordance of evidence.** All independent lines — biochemical reconstitution, substrate profiling, gene sequencing, genome annotation, direct sequence-motif analysis, and structural modeling — converge on the same conclusion: LPD-val is the BCKAD-specific E3 dihydrolipoyl dehydrogenase. No line of evidence challenges this assignment. The gene symbol *lpdV* correctly matches the protein description, the organism is correct (*P. putida* KT2440), and the domain/family features (class-I pyridine nucleotide-disulfide oxidoreductase; Lipoamide_DH IPR006258) align precisely with the literature.

---

## Limitations and Knowledge Gaps

1. **No experimental 3-D structure of LPD-val exists.** The structural conclusions (disulfide geometry, dimer interface, cross-subunit active site) rest on a very high-confidence AlphaFold model and on homology to crystallized orthologues (human DLD, *A. vinelandii* Lpd), not on a solved LPD-val structure. Kinetic constants (kcat, Km for dihydrolipoamide and NAD⁺) specific to LPD-val have not been reported in the modern literature reviewed here.

2. **Steady-state kinetic parameters and cofactor stoichiometry** of LPD-val itself (as opposed to the whole BCKAD complex) are not quantified in the retrieved literature. The mechanistic parameters cited come from homologues.

3. **The role of LPD-3 (PP_5366) remains unknown**, and whether it can partially substitute for LPD-val or LPD-glc under any condition has not been resolved. This leaves open a small possibility of functional overlap not captured by the classic reconstitution assays.

4. **Direct evidence for the *trans* (cross-subunit) active-site completion in LPD-val specifically** is inferential (from the AlphaFold model plus homology). No mutagenesis of LPD-val's own catalytic residues (Cys44, Cys49, His436/His438, Glu443) has been reported.

5. **Post-translational and assembly details** — the exact copy number of E3 per BCKAD complex in *P. putida*, and the affinity of LPD-val for the E2 core versus LPD-glc — are not established.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics.** Overexpress and purify His-tagged LPD-val, then measure kcat and Km for dihydrolipoamide (or the DTNB/lipoamide surrogate assay) and NAD⁺, plus the reverse (diaphorase) reaction, to obtain LPD-val-specific parameters and directly confirm EC 1.8.1.4 activity.

2. **Site-directed mutagenesis of the catalytic center.** Individually mutate Cys44, Cys49, His436/His438, and Glu443 and assay activity and complex reconstitution, to validate the redox disulfide and His–Glu diad predicted from sequence and the AlphaFold model.

3. **Reconstitution specificity, quantified.** Repeat the classic LPD-val vs LPD-glc reconstitution ([PMID: 6895373](https://pubmed.ncbi.nlm.nih.gov/6895373/)) with purified recombinant E1/E2/E3 to derive quantitative affinities and turnover, and test whether LPD-3 can substitute at all.

4. **Structural determination.** Solve the LPD-val crystal or cryo-EM structure (ideally in complex with the E2 lipoyl domain) to confirm the homodimeric, cross-subunit active-site architecture and the resting disulfide geometry.

5. **Genetics.** Construct a clean *lpdV* deletion in KT2440 and test growth on Val/Leu/Ile as sole carbon/nitrogen source; complement with *lpdV*, *lpdG*, and *lpd* to define in vivo specificity and any redundancy.

6. **Regulation.** Use transcriptional reporters to quantify BkdR-dependent induction and Crc repression of *lpdV* across carbon sources, confirming that E3 expression tracks the rest of the operon stoichiometrically.

---

## Conclusion

*lpdV* (Q88EP9, PP_4404) encodes **LPD-val**, the **branched-chain keto acid dehydrogenase-specific E3 (dihydrolipoyl dehydrogenase, EC 1.8.1.4)** of *Pseudomonas putida* KT2440. It is a cytoplasmic, homodimeric, FAD- and redox-active-disulfide flavoprotein of the class-I pyridine nucleotide-disulfide oxidoreductase family that re-oxidizes the dihydrolipoyl group on the E2 core of the BCKAD complex and transfers the electrons to NAD⁺ (dihydrolipoamide + NAD⁺ → lipoamide + NADH + H⁺). It is the terminal gene of the BkdR-activated, Crc-repressed *bkd* operon (*bkdAA–bkdAB–bkdB–lpdV*), sustaining oxidative decarboxylation of the branched-chain 2-oxo acids from valine, leucine and isoleucine, and it is functionally distinct from the housekeeping E3 LPD-glc. Every independent line of evidence — biochemical, genetic, genomic, sequence-analytical, and structural — converges on this assignment.


## Artifacts

- [OpenScientist final report](lpdV-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lpdV-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2917566
2. PMID:6895373
3. PMID:3085653
4. PMID:1633804
5. PMID:15946682
6. PMID:10217783
7. PMID:7298579
8. PMID:5030618
9. PMID:10648542
10. PMID:1902462
11. PMID:8670279
12. PMID:9068646
13. PMID:7836297
14. PMID:40451368
15. PMID:7557016
16. PMID:4150714
17. PMID:4150713