---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T06:47:14.888729'
end_time: '2026-08-11T07:07:29.861642'
duration_seconds: 1214.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SSB1
  gene_symbol: SSB1
  uniprot_accession: P11484
  protein_description: 'RecName: Full=Ribosome-associated molecular chaperone SSB1
    {ECO:0000303|PubMed:11739779}; EC=3.6.4.10 {ECO:0000269|PubMed:9860955}; AltName:
    Full=Cold-inducible protein YG101 {ECO:0000303|PubMed:6761581}; AltName: Full=Heat
    shock protein SSB1 {ECO:0000303|PubMed:3302682}; AltName: Full=Hsp70 chaperone
    Ssb {ECO:0000303|PubMed:8994035};'
  gene_info: Name=SSB1 {ECO:0000303|PubMed:3302682}; Synonyms=YG101 {ECO:0000303|PubMed:6761581};
    OrderedLocusNames=YDL229W {ECO:0000312|SGD:S000002388};
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the heat shock protein 70 family. Ssb-type Hsp70
  protein_domains: ATPase_NBD. (IPR043129); Heat_shock_70_CS. (IPR018181); HSP70_C_sf.
    (IPR029048); HSP70_peptide-bd_sf. (IPR029047); Hsp_70_fam. (IPR013126)
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SSB1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SSB1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P11484
- **Protein Description:** RecName: Full=Ribosome-associated molecular chaperone SSB1 {ECO:0000303|PubMed:11739779}; EC=3.6.4.10 {ECO:0000269|PubMed:9860955}; AltName: Full=Cold-inducible protein YG101 {ECO:0000303|PubMed:6761581}; AltName: Full=Heat shock protein SSB1 {ECO:0000303|PubMed:3302682}; AltName: Full=Hsp70 chaperone Ssb {ECO:0000303|PubMed:8994035};
- **Gene Information:** Name=SSB1 {ECO:0000303|PubMed:3302682}; Synonyms=YG101 {ECO:0000303|PubMed:6761581}; OrderedLocusNames=YDL229W {ECO:0000312|SGD:S000002388};
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the heat shock protein 70 family. Ssb-type Hsp70
- **Key Domains:** ATPase_NBD. (IPR043129); Heat_shock_70_CS. (IPR018181); HSP70_C_sf. (IPR029048); HSP70_peptide-bd_sf. (IPR029047); Hsp_70_fam. (IPR013126)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SSB1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SSB1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SSB1** (gene ID: SSB1, UniProt: P11484) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Yeast SSB1 (P11484 / YDL229W)

**UniProt:** P11484 · **Gene:** SSB1 (synonym YG101; ORF YDL229W) · **Organism:** *Saccharomyces cerevisiae* (S288c)
**Family:** Heat-shock protein 70 (Hsp70), Ssb-type · **EC:** 3.6.4.10 (ATP-driven chaperone)

## Summary

**SSB1** (systematic name *YDL229W*, UniProt **P11484**) of *Saccharomyces cerevisiae* (strain S288c) encodes **Ssb1**, a cytosolic, ATP-dependent molecular chaperone of the **heat shock protein 70 (Hsp70) family**, belonging specifically to the **Ssb-type** subfamily. Its primary, defining function is **co-translational protein folding**: Ssb1 is physically tethered to the large (60S) ribosomal subunit near the polypeptide exit tunnel, where it captures emerging nascent polypeptide chains and, through cycles of ATP-driven binding and release, prevents their premature misfolding and aggregation until they can attain a folding-competent or native state. Its catalytic activity is that of an ATPase — **EC 3.6.4.10**, ATP + H₂O → ADP + phosphate + H⁺ — and this ATPase cycle is the engine that powers substrate binding and release. Importantly, this yeast Hsp70 chaperone is **entirely unrelated** to the identically-named human single-stranded-DNA-binding proteins (SSB/SSB1); the gene symbol here refers unambiguously to a ribosome-associated Hsp70 in baker's yeast, and the protein family, domains (ATPase_NBD, Hsp70 peptide-binding domain), and organism all align with this identity.

Ssb1 does not act alone. Its ATPase activity is stimulated by the **ribosome-associated complex (RAC)**, a stable heterodimer of the J-domain co-chaperone **Zuo1** and the atypical Hsp70 **Ssz1**, which functions as the specialized J-protein cochaperone that activates Ssb on the ribosome. The nucleotide-exchange step of the cycle — the release of ADP to reset the chaperone for another round — is supplied by the **Hsp110 protein Sse1**. Together this forms a complete, mechanistically-defined Hsp70 reaction cycle operating directly at the ribosomal exit site. Ssb1 selectively engages short, degenerate sequence motifs enriched in **positively charged and aromatic residues**, and for a defined class of clients — notably **WD40 β-propeller proteins** — it acts as the upstream relay that hands substrates to the chaperonin **TRiC/CCT**.

Beyond folding of the nascent proteome, Ssb1 contributes to **translational fidelity, translation termination, and ribosome biogenesis**; it suppresses **de novo [PSI⁺] prion formation** by correctly folding nascent Sup35; and it carries out a distinct **extra-ribosomal signaling role**, bridging the SNF1/AMPK–Glc7 phosphatase axis together with the 14-3-3 protein Bmh1 to regulate glucose repression. Ssb1 has a nearly identical paralog, **Ssb2** (P40150), with which it shares **99.3% sequence identity** (differing at only 4 of 613 residues), explaining their broad functional redundancy — the two are usually treated together as "Ssb1/2."

---

## Key Findings

### 1. Ssb1 is a ribosome-associated Hsp70 that binds nascent chains to assist co-translational folding

The central function of Ssb1 is to bind newly synthesized polypeptides as they emerge from the translating ribosome and to keep them folding-competent. In vivo **selective ribosome profiling** has mapped Ssb–nascent-chain interactions at near-residue resolution and revealed the principle of substrate recognition: Ssb "engages most substrates by multiple binding-release cycles to a degenerate sequence enriched in positively charged and aromatic amino acids" ([PMID: 28708998](https://pubmed.ncbi.nlm.nih.gov/28708998/)). This defines the **substrate specificity** of Ssb — it is not sequence-specific in a strict sense but recognizes a physicochemical signature (basic and aromatic residues) that is common in unfolded regions of nascent chains.

The functional consequence of this activity is demonstrated by loss-of-function studies: deletion of *SSB* "leads to widespread aggregation of newly synthesized polypeptides" ([PMID: 23332755](https://pubmed.ncbi.nlm.nih.gov/23332755/)). This establishes that Ssb is essential for maintaining the solubility and folding competence of the nascent proteome — without it, freshly translated proteins misfold and aggregate on a genome-wide scale. Ssb is therefore best described as a **general co-translational holdase/foldase** operating at the front line of protein biogenesis.

### 2. Ssb ATPase activity is stimulated by the ribosome-associated complex (RAC = Zuo1 + Ssz1)

Like all Hsp70 chaperones, Ssb requires a **J-domain (Hsp40-type) co-chaperone** to stimulate its otherwise weak intrinsic ATPase activity and thereby drive high-affinity substrate capture. For Ssb, this role is played by the **RAC** heterodimer — a complex of the J-protein **Zuo1** and the non-canonical Hsp70 **Ssz1**. RAC "stimulates the ATPase activity of the ribosome-bound Hsp70 homolog Ssb, which interacts with nascent polypeptide chains to facilitate de novo protein folding" ([PMID: 28771464](https://pubmed.ncbi.nlm.nih.gov/28771464/)).

Crosslinking experiments confirm that this stimulation is functionally required for substrate engagement: "an efficient crosslink of the nascent chain to Ssb1/2p depends on the presence of functional RAC," including a functional Zuo1 J-domain ([PMID: 11929994](https://pubmed.ncbi.nlm.nih.gov/11929994/)). This establishes RAC as the obligate activating co-chaperone that couples Ssb's ATPase cycle to productive nascent-chain binding, forming what has been described as a **"functional chaperone triad"** (Ssb + Zuo1 + Ssz1) on the yeast ribosome.

### 3. Ssb binds the ribosomal tunnel exit via uL23/Rpl25, positioning its substrate-binding domain to receive nascent chains

The spatial organization of Ssb on the ribosome has been resolved structurally. **Cryo-EM structures** of ribosome-bound yeast Ssb identify **Rpl25/uL23** as the ribosomal binding site and reveal the chaperone's interaction with a model nascent chain ([PMID: 41545346](https://pubmed.ncbi.nlm.nih.gov/41545346/)). uL23 is the universal docking hub at the exit tunnel used by many ribosome-associated factors, and its identification pinpoints exactly where Ssb sits.

Critically, the structures show that RAC "positions the substrate binding domain of Ssb-ATP close to the tunnel exit to receive nascent chains" ([PMID: 41545346](https://pubmed.ncbi.nlm.nih.gov/41545346/)). This provides a mechanistic picture: RAC not only chemically activates Ssb's ATPase but also geometrically orients the ATP-bound (open, low-affinity) form of Ssb's substrate-binding domain (SBD) directly over the tunnel exit, so that emerging chains are captured the moment they appear. Upon ATP hydrolysis, Ssb undergoes conformational changes to the closed (high-affinity) state while remaining anchored by the bound nascent chain — completing the capture step of the cycle at the correct location.

### 4. RAC/Ssb maintains translational fidelity, termination, and ribosome biogenesis

The RAC/Ssb system's influence extends to the accuracy of translation itself. Loss of RAC or Ssb1/2p **impairs translational fidelity** — producing defects in termination and amino-acid misincorporation — and confers hypersensitivity to the aminoglycoside **paromomycin**: "Translational fidelity was impaired in the absence of functional RAC or Ssb1/2p, and the effect was further enhanced by paromomycin" ([PMID: 15456889](https://pubmed.ncbi.nlm.nih.gov/15456889/)).

A mechanistic basis for this was later established: RAC/Ssb is required for the **assembly of fully functional ribosomes**. In its absence, "ribosome biogenesis is hampered such that core ribosomal particles are structurally altered at the decoding and peptidyl transferase centers" ([PMID: 31114879](https://pubmed.ncbi.nlm.nih.gov/31114879/)). These altered ribosomes bind paromomycin with high affinity (KD = 76.6 nM), impairing stop/sense codon discrimination. Thus the fidelity defects seen upon Ssb loss are, at least in part, an indirect consequence of Ssb's role in producing correctly assembled ribosomes — linking co-translational chaperoning to the integrity of the translation apparatus itself.

### 5. Ssb has an extra-ribosomal signaling role bridging SNF1/AMPK–Glc7 with 14-3-3 Bmh1

A distinct, non-folding function of Ssb operates away from the ribosome in **glucose signaling**. Ssb bridges the **SNF1** (yeast AMPK) and **Glc7** (PP1 phosphatase) complexes, acting together with the 14-3-3 protein **Bmh1** to promote Glc7-mediated dephosphorylation and inactivation of SNF1. "The defect in glucose-repression in the absence of Ssb is due to the ability of the chaperone to bridge between the SNF1 and Glc7 complexes" ([PMID: 27001512](https://pubmed.ncbi.nlm.nih.gov/27001512/)).

This post-translational function requires a specific partnership: "Ssb performs this post-translational function in concert with the 14-3-3 protein Bmh, to which Ssb binds via its very C-terminus" ([PMID: 27001512](https://pubmed.ncbi.nlm.nih.gov/27001512/)). Raising the levels of either Ssb or Bmh allowed Glc7 to dephosphorylate SNF1 even in the absence of the regulatory subunit Reg1, and suppressed transcriptional deregulation in *Δreg1* cells. This identifies Ssb as a **scaffolding/signaling factor** in the glucose-repression pathway, with the extreme C-terminus serving as the Bmh1-binding determinant — a role mechanistically separable from its ribosome-associated folding activity.

### 6. Ssb inhibits de novo formation of the [PSI⁺] prion by properly folding nascent Sup35

Because Ssb folds nascent chains, it directly affects the fate of aggregation-prone proteins such as the translation-termination factor **Sup35**, whose amyloid conversion produces the **[PSI⁺]** prion. Ssb1/2p and RAC "were previously found to inhibit [PSI⁺] prion generation" ([PMID: 33020283](https://pubmed.ncbi.nlm.nih.gov/33020283/)), and restoring normal Ssb levels cured most [PSI⁺] variants that had arisen in its absence. Conversely, "the loss of Ssb or disruption of RAC results in the increased formation of [PSI⁺]" ([PMID: 26968706](https://pubmed.ncbi.nlm.nih.gov/26968706/)).

This bidirectional relationship — loss increases prion formation, restoration cures it — is strong evidence that Ssb's protective effect stems from its ability to correctly fold nascent Sup35 before it can nucleate amyloid. Ssb thus functions as a **guardian against protein-based heritable conformational disorders**, a role of considerable interest as a tractable model for human amyloid disease.

### 7. Ssb1/2p acts upstream of the chaperonin TRiC/CCT to fold WD40 β-propeller proteins

Ssb is not merely a general holdase — it feeds a defined subset of clients into the downstream chaperonin pathway. A specific class of **WD40 β-propeller proteins** interacts transiently with TRiC/CCT upon synthesis and requires it to fold, and "TRiC cooperates in the folding of these proteins with the ribosome-associated heat shock protein (Hsp)70 chaperones Ssb1/2p" ([PMID: 14517260](https://pubmed.ncbi.nlm.nih.gov/14517260/)).

The selectivity of this relay is highlighted by a striking contrast: "newly synthesized actin and tubulins, the major known client proteins of TRiC, are independent of Ssb1/2p and instead use the co-chaperone GimC/prefoldin" ([PMID: 14517260](https://pubmed.ncbi.nlm.nih.gov/14517260/)). Thus TRiC receives different substrate classes from different upstream chaperones — WD40 proteins via Ssb, cytoskeletal proteins via prefoldin/GimC. GimC can partially substitute for Ssb on WD40 substrates such as Cdc55p, but the combined deletion of *SSB* and *GIM* genes is lethal, indicating these upstream feeder systems provide overlapping but jointly essential functions. This finding defines a specific **substrate handoff pathway** and refines Ssb's substrate selectivity beyond a simple bulk role.

### 8. Domain architecture, catalyzed reaction, and the Sse1 nucleotide-exchange factor

UniProt P11484 defines Ssb1 as a **613-amino-acid, 66.6 kDa** protein with the canonical Hsp70 two-domain architecture:

| Region | Residues | Function |
|---|---|---|
| Nucleotide-binding domain (NBD) | 2–391 | ATP binding and hydrolysis (the ATPase engine) |
| Inter-domain linker | 392–402 | Allosteric coupling of NBD and SBD |
| Substrate-binding domain (SBD) | 403–613 | Captures nascent-chain segments |
| α-helical lid | 516–612 | Closes over bound substrate |
| Ribosome-binding motif | 428–430 & 601–613 | Anchors Ssb near the tunnel exit |
| Nuclear export signal | 574–582 | Cytoplasmic localization control |

The catalyzed reaction is **ATP + H₂O = ADP + phosphate + H⁺ (EC 3.6.4.10)**. Ssb binds close to the ribosomal tunnel exit, contacting ribosomal proteins RPL35, RPL39, RPL19 and rRNA (PubMed 27882919), and its ATP cycle is regulated by the Hsp110 nucleotide-exchange factor **Sse1** (PubMed 16219770). Post-translational modifications include N-terminal acetylation (Ala2) and phosphorylation at Thr47 and Thr431. This architecture is the structural basis for the allosteric ATPase cycle in which the nucleotide state of the NBD controls the affinity of the SBD for substrate.

### 9. Ssb1 and Ssb2 are 99.3% identical paralogs, explaining functional redundancy

A direct pairwise comparison of the UniProt sequences of Ssb1 (P11484) and Ssb2 (P40150) — both exactly 613 residues — shows **609 of 613 positions identical (99.3% identity)**. Only four residues differ: **E49Q, M413I, C435V, and A436S**. Notably, three of the four substitutions (413, 435, 436) cluster in or near the substrate-binding domain. This near-perfect identity explains the extensive functional redundancy of the two paralogs and the practice throughout the literature of referring to them jointly as "Ssb1/2." Whether the small cluster of SBD-proximal differences confers any subtle substrate-preference distinction between the two paralogs remains an open question.

### 10. Sse1 (Hsp110) is the biogenesis-relevant nucleotide-exchange factor; Fes1 serves Ssa, not Ssb

Completing the ATPase cycle requires a **nucleotide-exchange factor (NEF)** to catalyze release of ADP. Yeast has three cytosolic Hsp70 NEF families (Sse1/Sse2–Hsp110, Fes1–HspBP1, and Snl1–Bag1), and the evidence points to **Sse1** as Ssb's relevant NEF. Sse1 "participates in most Hsp70-mediated processes and is of particular importance in protein biogenesis and degradation" ([PMID: 24671421](https://pubmed.ncbi.nlm.nih.gov/24671421/)) — consistent with its role in the co-translational, biogenesis-associated Ssb cycle. Crucially, the alternative NEF Fes1 is excluded: "Fes1 was found to interact in vivo preferentially with the Ssa family of cytosolic Hsp70 and not the co-translational Ssb homolog" ([PMID: 24671421](https://pubmed.ncbi.nlm.nih.gov/24671421/)). This NEF specificity — Fes1 for Ssa, Sse1 for the biogenesis pathway including Ssb — assigns Sse1/Hsp110 as the nucleotide-exchange factor that resets Ssb for successive rounds of nascent-chain binding.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, mechanistically complete picture of Ssb1 as a **ribosome-tethered Hsp70 that folds the nascent proteome co-translationally**, driven by a full ATPase cycle whose every step is now assigned to a specific factor.

### The co-translational Hsp70 cycle at the ribosomal exit tunnel

```
                          Ribosome (60S subunit)
                   ┌───────────────────────────────────┐
                   │        exit tunnel                 │
                   │            │                        │
                   │            ▼  nascent chain         │
   uL23/Rpl25 ─────┤        ~~~~~~~~~~~                  │
   (docking site)  │       /           \                │
                   │      │  RAC        │  ← Zuo1 (J-domain) + Ssz1
                   │      │ positions & │     stimulate Ssb ATPase &
                   │      │ activates   │     position SBD at tunnel
                   └──────┼─────────────┼──────────────┘
                          │             │
                          ▼             │
                    ┌───────────┐       │
                    │   Ssb1    │       │
                    │ NBD + SBD │       │
                    └───────────┘       │
                          │             │
         ATP-bound (open, low affinity) │  ← receives nascent chain
                          │             │
             RAC-stimulated hydrolysis  │  (EC 3.6.4.10)
                          ▼             │
         ADP-bound (closed, high affinity) — grips substrate
                          │
              Sse1 (Hsp110 NEF) exchanges ADP → ATP
                          │
                          ▼
                  release; chain folds or
                  is relayed to TRiC/CCT
                  (WD40 β-propeller clients)
```

**Step by step:** (1) Ssb1 docks at the ribosomal exit tunnel via uL23/Rpl25 and neighboring ribosomal proteins/rRNA (F003, F008). (2) RAC — the Zuo1–Ssz1 heterodimer — both stimulates Ssb's ATPase and positions the ATP-bound (open, low-affinity) SBD directly over the emerging chain (F002, F003). (3) A nascent-chain segment enriched in positively charged and aromatic residues enters the SBD (F001). (4) RAC-stimulated ATP hydrolysis (EC 3.6.4.10) closes the SBD lid, converting Ssb to the high-affinity ADP state that grips the substrate (F008). (5) The Hsp110 NEF Sse1 catalyzes ADP→ATP exchange, reopening the SBD and releasing the segment (F010). (6) Through multiple such bind-release cycles the chain is kept folding-competent; general clients fold locally, while specific WD40 β-propeller clients are relayed to the downstream chaperonin TRiC/CCT (F007).

This cycle is now **fully populated** with molecular actors: substrate specificity (degenerate basic/aromatic motif), the J-protein activator (RAC/Zuo1–Ssz1), the ribosomal docking site (uL23/Rpl25), the catalyzed reaction (ATP hydrolysis, EC 3.6.4.10), and the nucleotide-exchange factor (Sse1/Hsp110).

### Two functional pools: ribosomal and extra-ribosomal

Ssb1 operates in two spatially and functionally distinct modes:

| Feature | Ribosome-associated pool | Extra-ribosomal pool |
|---|---|---|
| Location | 60S exit tunnel (uL23/Rpl25) | Cytosol, off-ribosome |
| Primary role | Co-translational folding of nascent chains | Glucose-repression signaling |
| Key partners | RAC (Zuo1–Ssz1), Sse1, TRiC/CCT | Bmh1 (14-3-3), SNF1, Glc7 |
| Binding determinant | SBD + ribosome-binding motifs | Extreme C-terminus (Bmh1) |
| Outcome | Prevents aggregation; feeds TRiC; suppresses [PSI⁺] | Promotes Glc7 dephosphorylation of SNF1 |

The ribosomal pool (F001–F004, F006, F007) accounts for the protein's canonical annotation as a co-translational chaperone, its role in translational fidelity/ribosome biogenesis, its suppression of the [PSI⁺] prion (by folding nascent Sup35), and its substrate handoff to TRiC. The extra-ribosomal pool (F005) reflects a genuinely distinct moonlighting function in metabolic signaling, mediated by a different part of the protein (the C-terminus) and a different set of partners.

### Redundancy and evolutionary interpretation

The 99.3% identity between Ssb1 and Ssb2 (F009) indicates a recent gene duplication with essentially no functional divergence, so that the two are effectively interchangeable and studied as "Ssb1/2." This redundancy buffers the cell against loss of either single gene, and it means most published phenotypes reflect the loss of both paralogs.

---

## Evidence Base

The report rests on a mixture of high-resolution structural, biochemical, ribosome-profiling, genetic, and bioinformatic evidence. The strongest, most precise studies are prioritized below.

| PMID | Title (abbreviated) | Contribution | Type of evidence |
|---|---|---|---|
| [28708998](https://pubmed.ncbi.nlm.nih.gov/28708998/) | *Profiling Ssb-Nascent Chain Interactions* | Defines substrate specificity (degenerate basic/aromatic motif; multiple bind-release cycles) | Selective ribosome profiling, near-residue resolution |
| [23332755](https://pubmed.ncbi.nlm.nih.gov/23332755/) | *Cotranslational function of ribosome-associated Hsp70* | Δ*SSB* causes genome-wide aggregation of nascent proteins | Loss-of-function, proteomics |
| [28771464](https://pubmed.ncbi.nlm.nih.gov/28771464/) | *Two chaperones locked in an embrace: RAC* | RAC stimulates Ssb ATPase to drive folding | Structural/biochemical review |
| [11929994](https://pubmed.ncbi.nlm.nih.gov/11929994/) | *A functional chaperone triad on the yeast ribosome* | Nascent-chain crosslink to Ssb requires functional RAC/Zuo1 J-domain | Crosslinking, genetics |
| [41545346](https://pubmed.ncbi.nlm.nih.gov/41545346/) | *The cotranslational cycle of ribosome-bound Ssb* | uL23/Rpl25 docking site; RAC positions SBD-ATP at tunnel exit | Cryo-EM structures |
| [15456889](https://pubmed.ncbi.nlm.nih.gov/15456889/) | *RAC and Ssb1/2p required for accurate translation* | RAC/Ssb loss impairs fidelity; paromomycin hypersensitivity | Genetics, reporter assays |
| [31114879](https://pubmed.ncbi.nlm.nih.gov/31114879/) | *Dual role of RAC/Ssb in termination fidelity* | Ssb required for ribosome assembly; altered decoding/PTC centers (KD 76.6 nM paromomycin) | Biochemistry, structural |
| [27001512](https://pubmed.ncbi.nlm.nih.gov/27001512/) | *Ssb and Bmh1 regulate glucose-repressed genes* | Ssb bridges SNF1–Glc7 with Bmh1 via its C-terminus | Genetics, biochemistry |
| [33020283](https://pubmed.ncbi.nlm.nih.gov/33020283/) | *Normal Ssb levels cure [PSI⁺] variants* | Restoring Ssb cures prions; Ssb inhibits [PSI⁺] generation | Genetics, prion assays |
| [26968706](https://pubmed.ncbi.nlm.nih.gov/26968706/) | *Dual role of RAC in prion formation* | Loss of Ssb/RAC increases [PSI⁺] formation | Genetics |
| [14517260](https://pubmed.ncbi.nlm.nih.gov/14517260/) | *TRiC/CCT cooperates with different upstream chaperones* | Ssb feeds WD40 β-propellers to TRiC; actin/tubulins independent (use GimC) | Biochemistry, genetics |
| [24671421](https://pubmed.ncbi.nlm.nih.gov/24671421/) | *Hierarchical specificity of Hsp70 NEFs in yeast* | Sse1 is the biogenesis NEF; Fes1 serves Ssa not Ssb | In vivo interaction, genetics |

Supporting/contextual literature reviewed includes studies on RAC/Ssb in translational repression of polylysine-stalled ribosomes ([PMID: 23007158](https://pubmed.ncbi.nlm.nih.gov/23007158/), [PMID: 25154418](https://pubmed.ncbi.nlm.nih.gov/25154418/)), the sequential recruitment of Hsp70/Ssb before TRiC governed by nascent-chain topology and elongation rate ([PMID: 31400849](https://pubmed.ncbi.nlm.nih.gov/31400849/)), cotranslational assembly of protein complexes ([PMID: 30158700](https://pubmed.ncbi.nlm.nih.gov/30158700/)), cooperation of Ssb/RAC with the RQC ubiquitin ligase Ltn1 ([PMID: 32957466](https://pubmed.ncbi.nlm.nih.gov/32957466/)), and multiple studies on Ssb's modulation of prions and heritable elements ([PMID: 37240005](https://pubmed.ncbi.nlm.nih.gov/37240005/), [PMID: 27828954](https://pubmed.ncbi.nlm.nih.gov/27828954/), [PMID: 30995727](https://pubmed.ncbi.nlm.nih.gov/30995727/)). The kinetic advantage of tethering a chaperone at the exit tunnel — raising its effective local concentration by 4–5 orders of magnitude — is documented in [PMID: 19519521](https://pubmed.ncbi.nlm.nih.gov/19519521/).

**Convergence of evidence types:** The core folding function is supported by orthogonal methods — ribosome profiling (specificity), deletion proteomics (aggregation), cryo-EM (structure/positioning), crosslinking (RAC dependence), and genetics (fidelity, prions). This multi-modal convergence gives high confidence in the mechanistic model. The most recent cryo-EM work (PMID 41545346) is especially valuable because it visualizes the entire cotranslational cycle directly.

---

## Limitations and Knowledge Gaps

1. **Ssb1 vs. Ssb2 individually.** Because the two paralogs are 99.3% identical and are routinely deleted together, almost all functional data pertain to "Ssb1/2" jointly. Whether Ssb1 specifically has any unique substrate preference, expression pattern, or regulation distinct from Ssb2 — potentially conferred by the four differing residues clustered near the SBD (E49Q, M413I, C435V, A436S) — has not been resolved. The gene identity of P11484 as *SSB1* is secure, but paralog-specific biology is largely unaddressed.

2. **NEF assignment is inferential.** The assignment of Sse1/Hsp110 as Ssb's nucleotide-exchange factor rests on Sse1's general importance in protein biogenesis and the exclusion of Fes1 (which prefers Ssa). A direct, quantitative demonstration of Sse1-catalyzed nucleotide exchange specifically on ribosome-bound Ssb, with kinetics, would strengthen this conclusion.

3. **Substrate scope beyond WD40 proteins.** While WD40 β-propellers are a well-defined TRiC-relayed client class, the full repertoire of Ssb's obligate clients (versus proteins that merely transit Ssb en route to folding) is not comprehensively catalogued. The rules governing which nascent chains fold with Ssb alone versus which require downstream handoff remain incompletely defined.

4. **Mechanism of the signaling role.** The extra-ribosomal SNF1–Glc7–Bmh1 bridging function is genetically well-supported, but the structural basis of the Ssb–Bmh1 C-terminal interaction and how the same protein partitions between ribosomal and signaling pools are not established.

5. **Ribosome biogenesis vs. direct fidelity effects.** Ssb's contributions to translational fidelity appear partly indirect (via defective ribosome assembly). Disentangling the direct co-translational folding contribution from the ribosome-biogenesis contribution to fidelity phenotypes remains difficult.

6. **Quantitative aggregation phenotype.** The statement that Δ*SSB* causes "widespread aggregation" is qualitative in this summary; the precise fraction of the proteome affected and the client-level determinants of aggregation vulnerability warrant quantitative follow-up.

---

## Proposed Follow-up Experiments / Actions

1. **Paralog-resolved functional analysis.** Construct strains expressing only Ssb1 or only Ssb2 (single-paralog complementation of a *Δssb1 Δssb2* background) and perform selective ribosome profiling and aggregation proteomics to test whether the four SBD-proximal residue differences produce any measurable substrate-preference divergence.

2. **Direct NEF kinetics.** Reconstitute purified ribosome–Ssb complexes and measure ADP-release kinetics with and without Sse1 (and Sse2) in vitro, directly confirming Sse1/Hsp110 as the nucleotide-exchange factor for Ssb and quantifying its catalytic efficiency versus Fes1 and Snl1.

3. **Comprehensive client mapping.** Combine Ssb selective ribosome profiling with TRiC profiling in matched conditions to define, genome-wide, which nascent chains are Ssb-only, TRiC-only, or sequentially Ssb→TRiC, refining the substrate-handoff rules (building on PMID 31400849).

4. **Structural basis of Ssb–Bmh1 signaling.** Determine the structure (cryo-EM or crystallography) of the Ssb C-terminus in complex with Bmh1, and use point mutants of the extreme C-terminus to selectively ablate the signaling function while preserving folding, cleanly separating the two pools.

5. **Time-resolved cryo-EM of the cycle.** Extend the recent cryo-EM work (PMID 41545346) with substrate- and nucleotide-trapped states to capture the ATP→ADP→ATP transitions of ribosome-bound Ssb, visualizing the conformational trajectory of the SBD lid during a single bind-release cycle.

6. **Prion-folding causality.** Directly test whether Ssb's [PSI⁺]-suppressing effect requires co-translational engagement of nascent Sup35 specifically (versus post-translational action) using Sup35 variants that alter the Ssb-binding motif, tying the anti-prion function precisely to the co-translational folding mechanism.

---

## Conclusion

Yeast **Ssb1** (P11484, YDL229W) is a cytosolic, ribosome-tethered **Hsp70 molecular chaperone** whose primary function is **ATP-driven co-translational folding of the nascent proteome**. Catalyzing ATP hydrolysis (EC 3.6.4.10), it docks at the 60S ribosomal exit tunnel via uL23/Rpl25, is activated and positioned by the RAC co-chaperone (Zuo1–Ssz1), captures emerging chains at degenerate basic/aromatic motifs, is reset by the Hsp110 NEF Sse1, and relays select clients (WD40 β-propellers) to TRiC/CCT. It further safeguards translational fidelity and ribosome biogenesis, suppresses the [PSI⁺] prion by folding nascent Sup35, and moonlights off-ribosome to regulate glucose repression via the SNF1–Glc7–Bmh1 axis. It is functionally redundant with its 99.3%-identical paralog Ssb2. This yeast Hsp70 is unrelated to the human single-stranded-DNA-binding proteins of the same name.


## Artifacts

- [OpenScientist final report](SSB1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SSB1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28708998
2. PMID:23332755
3. PMID:28771464
4. PMID:11929994
5. PMID:41545346
6. PMID:15456889
7. PMID:31114879
8. PMID:27001512
9. PMID:33020283
10. PMID:26968706
11. PMID:14517260
12. PMID:24671421
13. PMID:23007158
14. PMID:25154418
15. PMID:31400849
16. PMID:30158700
17. PMID:32957466
18. PMID:37240005
19. PMID:27828954
20. PMID:30995727
21. PMID:19519521