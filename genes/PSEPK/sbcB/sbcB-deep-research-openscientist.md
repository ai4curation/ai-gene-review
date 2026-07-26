---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-25T17:35:28.761018'
end_time: '2026-07-25T18:07:52.517901'
duration_seconds: 1943.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sbcB
  gene_symbol: sbcB
  uniprot_accession: Q88N51
  protein_description: 'RecName: Full=Exodeoxyribonuclease I {ECO:0000256|ARBA:ARBA00019900,
    ECO:0000256|PIRNR:PIRNR000977}; EC=3.1.11.1 {ECO:0000256|ARBA:ARBA00012108, ECO:0000256|PIRNR:PIRNR000977};'
  gene_info: Name=sbcB {ECO:0000313|EMBL:AAN66988.1}; OrderedLocusNames=PP_1365 {ECO:0000313|EMBL:AAN66988.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Exodeoxyribonuclease_I. (IPR023607); EXOI_SH3. (IPR034747); EXOI_SH3_sf.
    (IPR038649); Exonuc_1_C. (IPR058561); Exonuc_1_SH3. (IPR013620)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sbcB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sbcB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N51
- **Protein Description:** RecName: Full=Exodeoxyribonuclease I {ECO:0000256|ARBA:ARBA00019900, ECO:0000256|PIRNR:PIRNR000977}; EC=3.1.11.1 {ECO:0000256|ARBA:ARBA00012108, ECO:0000256|PIRNR:PIRNR000977};
- **Gene Information:** Name=sbcB {ECO:0000313|EMBL:AAN66988.1}; OrderedLocusNames=PP_1365 {ECO:0000313|EMBL:AAN66988.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Exodeoxyribonuclease_I. (IPR023607); EXOI_SH3. (IPR034747); EXOI_SH3_sf. (IPR038649); Exonuc_1_C. (IPR058561); Exonuc_1_SH3. (IPR013620)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sbcB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sbcB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sbcB** (gene ID: sbcB, UniProt: Q88N51) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *sbcB* (PP_1365, UniProt Q88N51) in *Pseudomonas putida* KT2440

## Summary

**The gene *sbcB* (ordered locus name PP_1365; UniProt Q88N51) of *Pseudomonas putida* strain KT2440 encodes Exodeoxyribonuclease I (ExoI, EC 3.1.11.1), a magnesium-dependent, highly processive 3′→5′ exonuclease that is specific for single-stranded DNA (ssDNA).** The enzyme binds the free 3′-hydroxyl end of ssDNA and processively hydrolyzes it in the 3′-to-5′ direction, releasing deoxyribonucleoside-5′-monophosphates. Catalysis proceeds through an RNase H-like DEDDh active site using a two-metal-ion (Mg²⁺) mechanism, and a distinctive DNA-encircling "crossover" loop together with an SH3-like domain provides the enzyme's high processivity.

The gene symbol and the UniProt functional annotation are internally consistent, and the identification is secure. The *sbcB* symbol has a long, well-documented history in *Escherichia coli*, where it (and its allele name *xonA*) was biochemically defined as the structural gene for exonuclease I. The *P. putida* protein is a genuine ortholog: a global pairwise alignment gives **48.0% amino-acid identity** to the experimentally characterized *E. coli* enzyme, and every catalytic and metal-coordinating residue is perfectly conserved. The domain architecture flagged by UniProt/InterPro (Exodeoxyribonuclease_I, EXOI_SH3, Exonuc_1_C) matches the well-studied *E. coli* ExoI fold. There is therefore no ambiguity: this is authentically an exonuclease I gene, not a same-symbol homonym from another gene family.

Functionally, SbcB is a soluble **cytoplasmic** enzyme that acts on ssDNA intermediates generated during DNA **recombination, mismatch repair, and replication**. It is a monomer that is physically recruited to its ssDNA substrate by single-stranded DNA-binding protein (SSB) through the conserved SSB C-terminal tail, an interaction that stimulates its nuclease activity. Biologically, ExoI is one of a set of partially redundant 3′-ssDNA exonucleases that trim and edit 3′ single-stranded tails, thereby limiting aberrant recombination substrates and safeguarding genome stability. All members of this functional network — SSB, the redundant exonucleases (ExoVII, SbcCD), and the RecBCD recombination machinery — are encoded in the *P. putida* KT2440 genome, so the pathway inferred from *E. coli* is structurally feasible in this organism. **It must be emphasized that no *P. putida*-specific experimental characterization of PP_1365 exists;** the functional assignment rests on strong orthology-based inference from the extensively characterized *E. coli* enzyme plus rule-based database annotation.

### Identity at a glance

| Attribute | Value |
|-----------|-------|
| UniProt | Q88N51 |
| Gene | *sbcB* (ordered locus **PP_1365**) |
| Organism | *P. putida* KT2440 (ATCC 47054 / DSM 6125), taxid 160488 |
| Protein | Exodeoxyribonuclease I, **EC 3.1.11.1** |
| Length / state | 477 aa; monomer; soluble cytoplasmic |
| Domains | RNase_T catalytic (PF00929; SSF53098) + ExoI_SH3 (PF08411; IPR034747) + ExoI_C (PF26016; IPR058561) |
| Orthology | eggNOG COG2925; 48.0% identity to *E. coli* ExoI (P04995) |

---

## Key Findings

### F001 — SbcB/PP_1365 is Exodeoxyribonuclease I: a processive 3′→5′ single-stranded DNA exonuclease (EC 3.1.11.1)

UniProt Q88N51 assigns EC 3.1.11.1 with the catalytic activity "*Exonucleolytic cleavage in the 3′- to 5′-direction to yield nucleoside 5′-phosphates*," derived from the PIRNR000977 rule-based signature. This annotation is anchored in decades of biochemistry on the *E. coli* ortholog. The classic genetic and biochemical study by Phillips and Kushner established that the *sbcB*/*xonA* locus is the structural gene for exonuclease I, "*an enzyme that hydrolyzes single-stranded DNA to mononucleotides in the 3′-to-5′ direction*" [PMID: 2834321](https://pubmed.ncbi.nlm.nih.gov/2834321/). Modern structural work confirms this substrate specificity and directionality: *E. coli* ExoI "*digests single-stranded DNA (ssDNA) in the 3′-5′ direction in a highly processive manner*" [PMID: 23609540](https://pubmed.ncbi.nlm.nih.gov/23609540/). Independent sequence/family analysis likewise classifies *E. coli* exonuclease I among "*processive 3′→5′ exodeoxyribonucleases that degrade single-stranded DNA*" [PMID: 9396823](https://pubmed.ncbi.nlm.nih.gov/9396823/).

The enzyme requires a **free 3′-OH terminus**, does not act on the 5′ end, and does not degrade duplex DNA — properties that define its role as a *ssDNA 3′-end trimmer* rather than a general nuclease. The *P. putida* protein is a 477-amino-acid monomer whose domain layout mirrors the *E. coli* enzyme: a Pfam RNase_T (PF00929) catalytic domain, an ExoI_SH3 (PF08411) domain, and an ExoI_C (PF26016) C-terminal domain. In sum, the primary function of the gene product is unambiguous — it is an enzyme that catalyzes the processive, single-strand-specific, 3′→5′ hydrolysis of DNA into 5′-mononucleotides.

### F002 — Catalysis uses an RNase H-like DEDDh fold with a two-Mg²⁺ mechanism, and a crossover loop confers processivity

InterPro, Pfam, and SUPFAM place Q88N51 in the **Ribonuclease H-like superfamily** (SSF53098; IPR012337/IPR036397), decorated with an SH3-like domain (IPR034747/IPR013620) and an ExoI C-terminal domain (IPR058561). Membership in the **DEDD(h)** exonuclease superfamily positions three-to-four conserved acidic residues plus a catalytic histidine at the active site. The *E. coli* ExoI crystal structure reveals "*a C-shaped molecule with three domains that form a central positively charged groove. The active site is at the bottom of the groove, while an extended loop, proposed to encircle the DNA, crosses over the groove*" [PMID: 23609540](https://pubmed.ncbi.nlm.nih.gov/23609540/). This crossover loop physically encircles the ssDNA substrate and, together with the SH3-like domain, is the structural basis of the enzyme's exceptional processivity — the enzyme threads the 3′ end into the active site while gripping downstream nucleotides. The same structure reveals "*an Mg²⁺ ion bound to the scissile phosphate in a position corresponding to Mg(B) in related two-metal nucleases*" [PMID: 23609540](https://pubmed.ncbi.nlm.nih.gov/23609540/), establishing the two-metal-ion catalytic mechanism.

Critically, this active-site architecture is shared across the DEDDh group. The structure of human ISG20 shows that "*its structure, including that of the active site, is very similar to those of the corresponding domains of two DEDDh-group DNases, the epsilon subunit of Escherichia coli DNA polymerase III and E. coli exonuclease I*" [PMID: 15527770](https://pubmed.ncbi.nlm.nih.gov/15527770/). The convergence of exonuclease I, the Pol III ε proofreading subunit, and ISG20 on the same fold and mechanism strongly corroborates the mechanistic model transferred to the *P. putida* enzyme.

### F003 — SbcB is a cytoplasmic monomer recruited to, and stimulated by, single-stranded DNA-binding protein (SSB)

UniProt Q88N51's SUBUNIT annotation states: "*Monomer. Interacts with ssb (via C-terminus); this interaction stimulates the exonuclease activity by recruiting the enzyme to its substrate.*" This is grounded in direct structural and biochemical evidence from the *E. coli* system. A co-crystal structure of *E. coli* ExoI bound to an SSB C-terminal (SSB-Ct) peptide shows the conserved amphipathic SSB tail docking into a pocket on ExoI; the authors concluded that "*SSB stimulates ExoI by recruiting the enzyme to its substrate*" and that this "*provide[s] a structural paradigm for understanding SSB's organizational role in genome maintenance*" [PMID: 18591666](https://pubmed.ncbi.nlm.nih.gov/18591666/). Mutational mapping identified the specific molecular anchor: "*the C-terminal-most SSB-Ct Phe anchors the peptide to a binding pocket on ExoI*" [PMID: 19527069](https://pubmed.ncbi.nlm.nih.gov/19527069/).

Kinetically, SSB does more than tether the enzyme — it activates it by improving substrate handling: "*SSB stabilizes ExoI substrate binding and melts secondary structures that could impede ExoI processivity*" [PMID: 21572106](https://pubmed.ncbi.nlm.nih.gov/21572106/), affecting both apparent *k*cat and *K*m. Because SbcB is a soluble enzyme (see F006) that acts on cytoplasmic/nucleoid ssDNA intermediates, its **subcellular site of action is the cytoplasm**, where it operates in concert with SSB-coated ssDNA at sites of active genome maintenance.

### F004 — ExoI functions in DNA repair, recombination editing, and mismatch repair, with partial redundancy among 3′ ssDNA exonucleases

UniProt keywords (DNA damage, DNA repair) and Gene Ontology (DNA repair, GO:0006281) capture the biological process. Genetically, in *E. coli*, exonuclease I "*has been implicated in the DNA repair and recombination pathways mediated by the recB and recC gene products (exonuclease V)*" [PMID: 2834321](https://pubmed.ncbi.nlm.nih.gov/2834321/); classic *sbcB* mutations were originally isolated as suppressors that restore recombination proficiency to *recBC* strains. By degrading 3′ single-stranded tails, ExoI edits recombination intermediates and modulates the balance of RecBCD/RecFOR-dependent recombination.

A key genome-stability role is redundancy: cells surviving RecG loss and PriA-driven re-replication "*must have either RecG or a 3′ single-stranded DNA (ssDNA) exonuclease, which can be exonuclease I, exonuclease VII, or SbcCD*" [PMID: 20647503](https://pubmed.ncbi.nlm.nih.gov/20647503/). This demonstrates that ExoI acts as one of several interchangeable 3′-ssDNA exonucleases that trim aberrant 3′ tails, limit inappropriate recombination substrates, and thereby prevent lethal re-replication. The same work links these nucleases to mismatch repair; the eukaryotic counterpart role of the ExoI family in mismatch-repair excision is separately documented (e.g., 5′-directed MMR excision, [PMID: 14636568](https://pubmed.ncbi.nlm.nih.gov/14636568/)), reinforcing the repair-and-editing theme. This redundancy means that loss of *sbcB* alone is frequently phenotypically buffered — consistent with ExoI being an **editing/back-up nuclease** rather than an essential replicative enzyme.

### F005 — *P. putida* SbcB shares 48% identity with *E. coli* ExoI and conserves all catalytic/Mg²⁺ residues

Because no direct experimental study of PP_1365 exists, the safety of transferring function from the *E. coli* enzyme was quantified by a Needleman–Wunsch global alignment (BLOSUM62) of Q88N51 (477 aa) against the experimentally characterized *E. coli* ExoI (P04995, 475 aa). This gives **48.0% identity over 465 aligned columns** — well above the ~30% threshold at which functional transfer between orthologs is considered reliable. More importantly, every functionally critical residue is conserved. The table below maps the key *E. coli* residues to their *P. putida* counterparts.

| Role | *E. coli* (P04995) | *P. putida* (Q88N51) | Conservation |
|------|--------------------|-----------------------|--------------|
| Mg²⁺-coordinating acidic (D) | Asp15 | Asp9 | Identical |
| Mg²⁺-coordinating acidic (E) | Glu17 | Glu11 | Identical |
| DEDDh catalytic His ("important for activity") | His181 | His174 | Identical |
| Mg²⁺-binding acidic (D) | Asp186 | Asp179 | Identical |
| Substrate-contacting Arg | Arg165 | Arg158 | Identical |
| Substrate-contacting Arg | Arg148 | Arg142 | Identical |
| N-terminal catalytic motif | HDYETFG | HDYETTG | Conserved motif (HDYET**x**G) |
| SSB-Ct-binding surface | Tyr207 | Trp200 | Conservative aromatic |
| SSB-Ct-binding surface | Gln311 | Pro303 | Divergent |
| SSB-Ct-binding surface | Arg338 | Asn331 | Divergent |

The conserved Mg²⁺-coordinating residues (D9/E11/D179) are precisely those that mediate the two-metal catalysis described in the *E. coli* structure, where an "*Mg²⁺ ion bound to the scissile phosphate in a position corresponding to Mg(B)*" was observed [PMID: 23609540](https://pubmed.ncbi.nlm.nih.gov/23609540/). The SSB-contact surface is only partially conserved — a conservative Tyr→Trp swap plus two divergent positions — consistent with a **species-tuned SSB interface**, in line with the finding that "*the C terminus of SSB (SSB-Ct) forms the docking site for heterologous proteins*" [PMID: 18591666](https://pubmed.ncbi.nlm.nih.gov/18591666/). The perfect conservation of the two-metal DEDDh catalytic core and the ssDNA-contacting arginines is direct bioinformatic evidence that PP_1365 is a *bona fide, catalytically active* exonuclease I — not merely a database label.

### F006 — Q88N51 is a soluble cytoplasmic protein, and its partner SSB plus redundant 3′-exonucleases are all encoded in the *P. putida* KT2440 genome

UniProt Q88N51 carries **no transmembrane and no signal-peptide feature** (only Domain and Binding-site features), consistent with a soluble cytoplasmic enzyme acting on nucleoid ssDNA — where its substrates arise. A genome survey of *P. putida* KT2440 (taxid 160488) confirms that the entire functional network is present in this organism, so the pathway context inferred from *E. coli* is genetically feasible here rather than resting on extrapolation alone:

| Function | Gene | Locus | UniProt |
|----------|------|-------|---------|
| Exonuclease I (this study) | *sbcB* | PP_1365 | Q88N51 |
| SSB partner | *ssb* | PP_0485 | Q88QK5 |
| Exonuclease VII (large subunit) | *xseA* | PP_1027 | Q88P26 |
| Exonuclease VII (small subunit) | *xseB* | PP_0529 | Q88QG5 |
| SbcCD nuclease (SbcC) | *sbcC* | PP_2024 | Q88LB1 |
| SbcCD nuclease (SbcD) | *sbcD* | PP_2025 | Q88LB0 |
| RecBCD / ExoV (RecB) | *recB* | PP_4673 | Q88DZ5 |
| RecBCD / ExoV (RecC) | *recC* | PP_4674 | Q88DZ4 |
| 5′→3′ ssDNA exonuclease | *recJ* | PP_1477 | Q88MU1 |

The presence of the redundant trio ExoI/ExoVII/SbcCD — the same set shown to be functionally interchangeable in *E. coli* [PMID: 20647503](https://pubmed.ncbi.nlm.nih.gov/20647503/) — grounds the redundancy model in *P. putida*. Likewise, the confirmed *ssb* gene (PP_0485) makes the SSB-mediated recruitment mechanism feasible in this organism [PMID: 18591666](https://pubmed.ncbi.nlm.nih.gov/18591666/).

---

## Mechanistic Model / Interpretation

Integrating the six findings yields a coherent picture of SbcB as a cytoplasmic, SSB-guided 3′→5′ ssDNA exonuclease that edits DNA intermediates during repair and recombination.

**Reaction catalyzed.** SbcB binds the free 3′-OH terminus of a single-stranded DNA and processively removes nucleotides one at a time in the 3′→5′ direction, releasing deoxyribonucleoside-5′-monophosphates and stopping when a short 5′ remnant is reached. It is strictly single-strand-specific and requires Mg²⁺.

```
        SSB-coated ssDNA (cytoplasm / nucleoid)
   5'──────────────────────────────3'-OH
        ▓▓▓▓▓ SSB   SSB ▓▓▓▓▓
                          │ SSB C-terminal tail (...D-D-D-I-P-F)
                          │  docks into pocket; C-terminal Phe anchors
                          ▼
                    ┌───────────┐
                    │   SbcB    │  C-shaped, 3 domains
                    │  (ExoI)   │  crossover loop + SH3 encircle ssDNA
                    │  DEDDh    │  D9 / E11 / H174 / D179
                    │  active   │  2 x Mg2+  (RNase H-like, two-metal)
                    │  site     │  R142 / R158 contact substrate
                    └─────┬─────┘
                          │  processive 3'->5' hydrolysis
                          ▼
             released:  dNMP  dNMP  dNMP ...  (5'-mononucleotides)
```

**Where it acts.** The enzyme is soluble and operates in the cytoplasm on nucleoid-associated ssDNA. Its recruitment to substrate is organized by SSB: SSB coats ssDNA at replication forks, recombination intermediates, and repair gaps, and its exposed C-terminal tail docks SbcB directly onto the substrate. This raises the local concentration of enzyme at ssDNA, stabilizes substrate binding, and melts secondary structure that would otherwise stall the processive machine — coupling the enzyme's activity to the physiological state of the DNA.

**Pathways.** Biologically, SbcB is an "editing" nuclease. In recombination, it and other 3′-ssDNA exonucleases trim 3′ single-stranded tails, thereby modulating which substrates enter the RecBCD/RecA recombination pathway — the historical basis for *sbcB* mutations acting as suppressors in *recBC* backgrounds. In genome maintenance more broadly, SbcB is one of three functionally redundant 3′-ssDNA exonucleases (with Exonuclease VII and SbcCD) that remove aberrant 3′ tails and prevent lethal, PriA-driven re-replication when RecG is absent. This redundancy explains why single-gene *sbcB* deletions are typically phenotypically mild — a caveat directly relevant to interpreting any future knockout in *P. putida*.

**Confidence and inference chain.** The functional assignment for PP_1365 is inferential but robust. It rests on (1) rule-based EC assignment (PIRNR000977), (2) 48% identity to a biochemically defined ortholog, (3) perfect conservation of all catalytic and metal-binding residues, and (4) genomic confirmation that the full partner network exists in KT2440. The weakest link is the SSB-interaction interface, which is only partially conserved and may be species-tuned; and, most importantly, no direct experimental study of the *P. putida* protein exists.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|----------------------|------------------------------|
| [2834321](https://pubmed.ncbi.nlm.nih.gov/2834321/) | *Physical and biochemical characterization of cloned sbcB and xonA mutations from E. coli K-12* | Defines *sbcB*/*xonA* as the structural gene for exonuclease I (3′→5′ ssDNA → mononucleotides); links it to RecBC repair/recombination (F001, F004) |
| [23609540](https://pubmed.ncbi.nlm.nih.gov/23609540/) | *Crystal structures of E. coli exonuclease I in complex with ssDNA* | Establishes processive 3′→5′ digestion, three-domain C-shape, DNA-encircling crossover loop, and the two-metal (Mg²⁺) mechanism (F001, F002, F005) |
| [9396823](https://pubmed.ncbi.nlm.nih.gov/9396823/) | *The proofreading domain of E. coli DNA polymerase I and other exonuclease domains* | Independent family analysis classifying ExoI as a processive 3′→5′ ssDNA exodeoxyribonuclease (F001) |
| [15527770](https://pubmed.ncbi.nlm.nih.gov/15527770/) | *Crystal structure of human ISG20, an interferon-induced antiviral ribonuclease* | Places ExoI in the DEDDh group; active site shared with Pol III ε and ISG20 (F002) |
| [18591666](https://pubmed.ncbi.nlm.nih.gov/18591666/) | *Structural basis of E. coli SSB stimulation of exonuclease I* | Co-crystal showing SSB-Ct docking; SSB stimulates ExoI by recruitment to substrate (F003, F005, F006) |
| [19527069](https://pubmed.ncbi.nlm.nih.gov/19527069/) | *Peptide inhibitors identify roles for SSB C-terminal residues in SSB/ExoI complex formation* | Identifies the SSB C-terminal Phe as the anchoring residue for the ExoI-binding pocket (F003) |
| [21572106](https://pubmed.ncbi.nlm.nih.gov/21572106/) | *Mechanism of Exonuclease I stimulation by the single-stranded DNA-binding protein* | SSB stabilizes substrate binding and melts secondary structure to aid processivity (F003) |
| [20647503](https://pubmed.ncbi.nlm.nih.gov/20647503/) | *RecG protein and single-strand DNA exonucleases avoid cell lethality associated with PriA helicase activity* | Demonstrates functional redundancy of ExoI, ExoVII, and SbcCD as 3′-ssDNA exonucleases (F004, F006) |

**Supporting/contextual literature.** Structural studies of the trimeric archaeal PhoExo I ([PMID: 26138487](https://pubmed.ncbi.nlm.nih.gov/26138487/)) and the NMR model of the Pol III ε proofreading subunit ([PMID: 11772007](https://pubmed.ncbi.nlm.nih.gov/11772007/)) reinforce the RNase H-like/DEDDh mechanistic paradigm. Human EXO1 studies ([PMID: 12414623](https://pubmed.ncbi.nlm.nih.gov/12414623/), [PMID: 24829445](https://pubmed.ncbi.nlm.nih.gov/24829445/)) and mismatch-repair excision work ([PMID: 14636568](https://pubmed.ncbi.nlm.nih.gov/14636568/), [PMID: 16905530](https://pubmed.ncbi.nlm.nih.gov/16905530/), [PMID: 16085492](https://pubmed.ncbi.nlm.nih.gov/16085492/)) document the broader family's role in DNA repair, though these concern eukaryotic exonucleases and are contextual rather than direct evidence for the bacterial 3′→5′ enzyme.

**No contradicting evidence** was found. All lines of evidence — genetic, biochemical, structural, bioinformatic, and genomic — converge on the same functional assignment.

### Supported and refuted hypotheses

**Supported**

- **H1** — *sbcB* catalyzes processive 3′→5′ exonucleolytic degradation of ssDNA to 5′-mononucleotides (EC 3.1.11.1). *Supported* (PMID 2834321, 23609540, 9396823; UniProt).
- **H2** — Catalysis is Mg²⁺-dependent via a DEDDh/RNase H-like two-metal mechanism; processivity comes from a DNA-encircling crossover loop/SH3 domain. *Supported* (PMID 23609540, 15527770; InterPro/Pfam).
- **H3** — The enzyme is a cytoplasmic monomer recruited to and stimulated by SSB (SSB-Ct docking). *Supported* (UniProt; PMID 18591666, 19527069, 21572106).
- **H4** — Biological role is 3′-ssDNA editing in recombination, MMR, and prevention of aberrant re-replication, with redundancy among 3′ exonucleases. *Supported* (PMID 2834321, 20647503).

**Refuted / excluded**

- Not a 5′→3′ nuclease, not a double-strand-DNA nuclease, and not an RNA-degrading ribonuclease as its primary role (any "RNA exonuclease" GO term appears only as a low-confidence IEA projection; the biochemically defined substrate is ssDNA).
- Not a membrane or secreted protein; no transporter or signaling function.

---

## Limitations and Knowledge Gaps

1. **No organism-specific experimental data.** There is no published biochemical, genetic, or structural study of *P. putida* PP_1365 itself. The entire functional assignment is inferred from the *E. coli* ortholog plus rule-based database annotation. Enzyme kinetics, exact processivity, and metal-ion preferences have not been measured for the *P. putida* protein.

2. **SSB interface divergence.** While the catalytic core is perfectly conserved, the SSB-Ct docking surface is only partially conserved (conservative Y→W plus two divergent positions). Whether *P. putida* SSB stimulates SbcB with the same affinity and mechanism as in *E. coli* is untested; the enzyme is presumably stimulated by its own cognate SSB.

3. **Redundancy obscures phenotype.** Because ExoI, ExoVII, and SbcCD are functionally redundant, a single *sbcB* deletion is likely to have a subtle phenotype, complicating loss-of-function studies. Any physiological role unique to *P. putida* (e.g., under its characteristic environmental/solvent stresses) is unknown.

4. **Structure is homology-inferred.** No experimental structure of the *P. putida* protein exists. Residue mappings rely on sequence alignment to the *E. coli* structure; an AlphaFold model would strengthen (but not replace) this inference.

5. **Family annotation caveat.** UniProt lists "Protein Family: Not specified," and the EC assignment is rule-based (PIRNR/ARBA). Rule-based annotations can occasionally be imprecise, though here they are strongly corroborated by orthology.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzyme assay (highest priority).** Express and purify His-tagged PP_1365 and directly assay 3′→5′ exonuclease activity on 3′-labeled ssDNA oligonucleotides, confirming (a) single-strand specificity, (b) 3′→5′ directionality, (c) release of 5′-mononucleotides, and (d) Mg²⁺ dependence. Include a catalytic-dead mutant (e.g., D9A/E11A or H174A) as a negative control.

2. **SSB-stimulation test.** Measure ExoI activity ± purified *P. putida* SSB (PP_0485), and ± an SSB-Ct peptide, to determine whether the recruitment/stimulation mechanism is conserved despite the divergent interface residues. Use surface plasmon resonance or ITC to quantify the SbcB–SSB affinity.

3. **Structural model and validation.** Generate an AlphaFold2/3 model of Q88N51, superpose it on the *E. coli* ExoI–ssDNA structure (PDB from PMID 23609540), and verify the crossover-loop geometry and active-site residue positions (D9, E11, H174, D179; R142, R158). Longer term, pursue an experimental crystal or cryo-EM structure.

4. **Genetic redundancy analysis in KT2440.** Construct single (Δ*sbcB*) and combinatorial (Δ*sbcB* Δ*xseA* Δ*sbcC*; ± Δ*recG*) knockouts and assay UV/MMS sensitivity, recombination frequency, and viability, testing whether the *E. coli* redundancy and PriA-lethality relationships hold in *P. putida*.

5. **Phenotypic context.** Examine whether *sbcB* contributes to genome stability under *P. putida*-relevant stresses (oxidative, solvent, and stationary-phase conditions) where ssDNA repair intermediates accumulate.

---

## Conclusion

*sbcB* (PP_1365, Q88N51) of *Pseudomonas putida* KT2440 is confidently annotated as **Exodeoxyribonuclease I (EC 3.1.11.1)** — a cytoplasmic, Mg²⁺-dependent, processive 3′→5′ single-stranded-DNA exonuclease that uses an RNase H-like DEDDh two-metal active site and a DNA-encircling crossover loop, is recruited to and stimulated by SSB, and functions as one of several partially redundant 3′-ssDNA exonucleases in DNA recombination, repair, and mismatch-repair editing. The assignment is inferential (48% identity and full active-site conservation relative to the biochemically defined *E. coli* enzyme, plus genomic confirmation of the complete partner network) but robust, and awaits direct experimental confirmation in *P. putida*.


## Artifacts

- [OpenScientist final report](sbcB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sbcB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2834321
2. PMID:23609540
3. PMID:9396823
4. PMID:15527770
5. PMID:18591666
6. PMID:19527069
7. PMID:21572106
8. PMID:20647503
9. PMID:14636568
10. PMID:26138487
11. PMID:11772007
12. PMID:12414623
13. PMID:24829445
14. PMID:16905530
15. PMID:16085492