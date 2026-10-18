---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T02:02:07.697773'
end_time: '2026-10-04T02:15:27.387618'
duration_seconds: 799.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: pli1
  gene_symbol: pli1
  uniprot_accession: O94451
  protein_description: 'RecName: Full=E3 SUMO-protein ligase pli1; EC=2.3.2.-; AltName:
    Full=E3 SUMO-protein transferase plil {ECO:0000305};'
  gene_info: Name=pli1; ORFNames=SPAC1687.05;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the PIAS family. .
  protein_domains: PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034);
    SAP_dom_sf. (IPR036361); SIZ1/2_SP-RING. (IPR031141)
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
citation_count: 24
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pli1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pli1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** O94451
- **Protein Description:** RecName: Full=E3 SUMO-protein ligase pli1; EC=2.3.2.-; AltName: Full=E3 SUMO-protein transferase plil {ECO:0000305};
- **Gene Information:** Name=pli1; ORFNames=SPAC1687.05;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the PIAS family. .
- **Key Domains:** PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); SIZ1/2_SP-RING. (IPR031141)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pli1" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pli1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pli1** (gene ID: pli1, UniProt: O94451) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Pli1 (SPAC1687.05 / UniProt O94451): The Principal Nuclear SUMO E3 Ligase of Fission Yeast

**Gene:** *pli1* (systematic ORF name SPAC1687.05)
**Protein:** E3 SUMO-protein ligase Pli1 (EC 2.3.2.-)
**UniProt:** O94451
**Organism:** *Schizosaccharomyces pombe* (strain 972 / ATCC 24843), fission yeast
**Family:** Siz/PIAS (SP-RING) family; human ortholog PIAS1

## Summary

**Pli1 is the principal SUMO (Pmt3) E3 ligase of the fission yeast *Schizosaccharomyces pombe* — the organism's sole member of the Siz/PIAS (SP-RING) family and the ortholog of human PIAS1.** Its primary molecular function is to catalyze the ATP-independent, isopeptide-bond ligation of the small ubiquitin-related modifier SUMO (in *S. pombe*, the protein Pmt3) onto lysine residues of substrate proteins (EC 2.3.2.-). As an E3 ligase, Pli1 does not form the SUMO thioester itself; rather it accelerates and directs transfer of SUMO from the charged E2 conjugating enzyme Hus5 (Ubc9) — which is loaded by the E1 activating complex Fub2/Uba2–Rad31 — onto specific substrate lysines, and it is uniquely responsible for building poly-SUMO chains in this organism. This identification is unambiguous: the UniProt accession (O94451), gene name (pli1 / SPAC1687.05), organism (*S. pombe* 972/ATCC 24843), PIAS protein family, and the diagnostic SAP + PINIT + SP-RING domain architecture all match the primary literature precisely. There is no gene-symbol ambiguity.

Mechanistically, Pli1 is a modular enzyme of 727 amino acids. Its catalytic activity resides in an SP-RING (Siz/PIAS-RING) zinc finger (residues ~290–371), which activates the E2~SUMO thioester; point mutations in this RING finger abolish sumoylation activity and reproduce *pli1*-deletion phenotypes. An N-terminal SAP domain (residues ~18–52) mediates chromatin/DNA association and nuclear targeting, and a PINIT domain (residues ~108–261) contributes to substrate selection and to redirecting SUMO onto non-consensus substrate lysines, exactly as established for the orthologous Siz/PIAS enzymes. The C-terminal half of the protein is largely disordered/low-complexity.

Biologically, Pli1 operates in the nucleus as a genome-maintenance enzyme. It safeguards centromeric heterochromatin and chromosome segregation, restrains telomere length by modulating telomerase, controls homologous recombination at repeats and arrested replication forks, participates in meiotic recombination and a dedicated interstrand-crosslink repair branch, and feeds its (poly-)SUMOylated products into the SUMO-targeted ubiquitin ligase (STUbL; Slx8-Rfp/RNF4)–Cdc48-Ufd1-Npl4 degradation axis. It acts at defined nuclear locations — centromeres, telomeres, arrested forks, and the nuclear periphery/nuclear pore — and its own activity is homeostatically tuned by SUMOylation that is antagonized by the nuclear-pore SUMO protease Ulp1 (SENP1/2). Known direct or pathway substrates include Topoisomerase I (Top1), the shelterin subunit Tpz1 (TPP1 homolog) at lysine 242, and the meiotic linear-element protein Rec10.

---

## Key Findings

### Finding 1 — Pli1 is the principal SUMO E3 ligase of fission yeast, the sole SP-RING/PIAS-family member

Pli1 was demonstrated biochemically and genetically to be a SUMO E3 ligase both *in vivo* and *in vitro*, and it is the unique *S. pombe* member of the SP-RING (Siz/PIAS) family. The founding study states directly that "Pli1p, the unique fission yeast member of the SP-RING family, is a SUMO E3 ligase in vivo and in vitro" ([PMID: 15359282](https://pubmed.ncbi.nlm.nih.gov/15359282/)). A subsequent study distinguished Pli1 from the other, specialized *S. pombe* SP-RING ligase Nse2 (associated with the Smc5/6 complex), establishing that "Pli1p, but not the related Nse2p, is the principal SUMO E3 ligase enzyme involved" in bulk/global sumoylation ([PMID: 17209013](https://pubmed.ncbi.nlm.nih.gov/17209013/)). Importantly, *pli1* mutants are strongly impaired for global sumoylation yet remain viable, which both confirms Pli1 as the bulk ligase and shows that it is not individually essential — a hallmark of E3 ligases, which raise the efficiency and specificity of a reaction that can proceed at low level without them. A comparative review of the two *S. pombe* SUMO ligases reinforced that "SUMO ligases facilitate the SUMOylation of specific subsets of proteins," with Pli1 and Nse2 each having distinct roles in genome stability ([PMID: 18031226](https://pubmed.ncbi.nlm.nih.gov/18031226/)).

### Finding 2 — Catalytic activity depends on the SP-RING finger; domain architecture mirrors Siz1/PIAS

Pli1's catalytic activity maps to its SP-RING zinc finger. Structure-function analysis showed that "point mutations within the RING finger of Pli1p totally or partially reproduce the pli1 deletion phenotypes, thus correlating with their sumoylation activity" ([PMID: 15359282](https://pubmed.ncbi.nlm.nih.gov/15359282/)) — a direct genetic link between the RING and catalysis. The mechanistic logic is well understood from the orthologous Siz/PIAS enzymes. In budding-yeast/mammalian Siz1, "the SP-RING and SP-CTD are required for activation of the E2 ~ SUMO thioester, while the PINIT domain is essential for redirecting SUMO conjugation to the proliferating cell nuclear antigen (PCNA) at lysine 164" ([PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/)). In the PIAS-type enzyme Ull1/Siz1, "a novel conserved N-terminal domain, called PINIT, as well as the RING-like domain (SP-RING) were required for the SUMO ligase activity" ([PMID: 16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/)). In the Arabidopsis ortholog SIZ1, the "SP-RING is required for SUMO conjugation activity and nuclear localization," while PINIT mutations impair in-vivo SUMOylation ([PMID: 19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/)), and domain-dissection studies confirm that the diverse properties of SIZ1 are separable and associated with specific domains ([PMID: 20404572](https://pubmed.ncbi.nlm.nih.gov/20404572/)). More broadly, SP-RING/RING-like E3 domains "bind and activate the E2-Ubl thioester by stabilizing a conformation that is optimal for nucleophilic attack by the side chain residue (typically lysine) on the substrate" ([PMID: 30242710](https://pubmed.ncbi.nlm.nih.gov/30242710/)). These results, taken together, define Pli1's catalytic mechanism by homology and by direct mutation.

### Finding 3 — Pli1-dependent sumoylation maintains centromeric heterochromatin, silencing, and chromosome segregation

*pli1Δ* cells are sensitive to the microtubule-destabilizing drug thiabendazole (TBZ) and exhibit enhanced minichromosome loss, indicating compromised centromere function. This is linked to defective heterochromatin: "The weakened centromeric function of pli1Delta cells may be related to the defective heterochromatin structure at the central core, as shown by the reduced silencing of an ura4 variegation reporter gene inserted at cnt and imr" ([PMID: 15359282](https://pubmed.ncbi.nlm.nih.gov/15359282/)). A recent study extended this to nuclear organization, showing that Pli1-driven poly-SUMOylation recruits the STUbL Slx8 to cluster centromeres at the spindle-pole body and promote silencing: "The formation of this single Slx8 focus requires the E3 SUMO ligase Pli1, poly-SUMOylation and the histone methyl transferase Clr4" ([PMID: 39786922](https://pubmed.ncbi.nlm.nih.gov/39786922/)). Thus Pli1 acts upstream of heterochromatin integrity and of the spatial clustering of centromeres at the nuclear periphery, with the H3K9 methyltransferase Clr4 as a required partner.

### Finding 4 — Pli1/SUMO restrains telomere length by modulating telomerase, and regulates recombination at repeats

Loss of Pli1 elongates telomeres: "*pli1Delta* cells exhibit consistent telomere length increase" ([PMID: 15359282](https://pubmed.ncbi.nlm.nih.gov/15359282/)). Follow-up work determined the mechanism is not telomere–telomere recombination but telomerase regulation: "sumoylation increases telomerase activity, therefore suggesting that this modification controls the activity of a positive or negative regulator of telomerase" ([PMID: 17209013](https://pubmed.ncbi.nlm.nih.gov/17209013/)). In parallel, *pli1Δ* cells show deregulated homologous recombination and enhanced loss of reporters at heterochromatic repeats by gene conversion, placing Pli1 at the interface of SUMO signaling and recombination control at repetitive loci.

### Finding 5 — Pli1 (PIAS1 ortholog) feeds the STUbL/Ufd1-Cdc48 pathway in the DNA-damage response

Pli1 is the fission-yeast ortholog of human PIAS1, and its SUMO products are the substrates of the downstream STUbL/segregase degradation machinery. "Ufd1 interacts physically and functionally with the Sumo-targeted ubiquitin ligase (STUbL) Rfp1, homologous to human RNF4, and with the Sumo E3 ligase Pli1, homologous to human PIAS1" ([PMID: 24265825](https://pubmed.ncbi.nlm.nih.gov/24265825/)). Disrupting the Ufd1 C-terminus causes accumulation of high-molecular-weight SUMO conjugates and severe genomic instability requiring homologous recombination for repair — directly connecting Pli1-generated SUMO conjugates to the Cdc48–Ufd1–Npl4 segregase and ubiquitin-dependent turnover. The founding STUbL study underscored the specificity of this relationship: genomic-instability phenotypes of *slx8*/STUbL mutants "are suppressed by deletion of the major SUMO ligase Pli1, demonstrating the specificity of STUbLs as regulators of sumoylated proteins" ([PMID: 17762865](https://pubmed.ncbi.nlm.nih.gov/17762865/)). A proteome-wide map of >1,000 SUMO sites in 468 proteins further showed that STUbL/Ufd1-regulated conjugates are often "dynamically associated with centromeres or telomeres" ([PMID: 26537787](https://pubmed.ncbi.nlm.nih.gov/26537787/)), matching Pli1's sites of action.

### Finding 6 — Pli1 sumoylates specific genome-stability substrates: Topoisomerase I (Top1) and the shelterin subunit Tpz1

Beyond bulk sumoylation, Pli1 modifies defined substrates. For Topoisomerase I: "Slx8 removes Pli1-dependent Top1-SUMO conjugates and in doing so helps to constrain recombination at RTS1" ([PMID: 23936535](https://pubmed.ncbi.nlm.nih.gov/23936535/)) — identifying Top1 as a direct Pli1 substrate whose SUMOylation limits spontaneous recombination and is subsequently cleared by STUbL. At telomeres, the shelterin subunit Tpz1 (the TPP1 homolog) is the key telomeric SUMO substrate: "SUMOylation of the shelterin subunit TPP1 homolog in Schizosaccharomyces pombe (Tpz1) on lysine 242 is important for telomere length homeostasis. Furthermore... Tpz1 SUMOylation prevents telomerase accumulation at telomeres by promoting recruitment of Stn1-Ten1 to telomeres" ([PMID: 24711392](https://pubmed.ncbi.nlm.nih.gov/24711392/)). Because Pli1 is the principal ligase controlling telomere length via telomerase ([PMID: 17209013](https://pubmed.ncbi.nlm.nih.gov/17209013/)), Tpz1-K242 is the molecular link between Pli1 activity and the telomere-length phenotype. These two examples illustrate Pli1's substrate specificity: site-specific modification (e.g., Tpz1 K242) with defined downstream consequences (Stn1-Ten1 recruitment, telomerase restraint, recombination control).

### Finding 7 — Pli1 builds poly-SUMO chains at arrested forks and routes lesions to nuclear pores

Pli1 is uniquely responsible for SUMO-chain (poly-SUMO) formation in fission yeast, and this activity has a defined role at stalled replication forks. "The E3 SUMO ligase Pli1 acts at arrested forks to safeguard integrity of nascent strands and generates poly-SUMOylation which promote relocation to NPCs but impede the resumption of DNA synthesis by homologous recombination (HR)" ([PMID: 33159083](https://pubmed.ncbi.nlm.nih.gov/33159083/)). Biochemically, the choice between substrate monosumoylation and chain-building is governed by distinct Ubc9 complexes: "Ubc9:SUMO instead promotes global sumoylation and chain formation, via the Pli1 E3 SUMO ligase" ([PMID: 21444718](https://pubmed.ncbi.nlm.nih.gov/21444718/)). Poly-SUMO chains are the preferred recognition signal for STUbLs, so Pli1's chain-building activity is the molecular trigger that routes damaged/arrested loci into the STUbL–segregase pathway and to the nuclear-pore complex for processing.

### Finding 8 — Pli1 is itself a nuclear SUMO substrate, protected by the nuclear-pore SUMO protease Ulp1

Pli1 activity is homeostatically regulated through its own SUMOylation. When the nucleoporin Nup132 is absent, the SUMO protease Ulp1 is delocalized from the nuclear periphery and "can no longer antagonize sumoylation of the PIAS family SUMO E3 ligase, Pli1. Consequently, SUMO chain-modified Pli1 is targeted for proteasomal degradation by the concerted action of a SUMO-targeted ubiquitin ligase (STUbL) and Cdc48-Ufd1-Npl4" ([PMID: 26221037](https://pubmed.ncbi.nlm.nih.gov/26221037/)). The resulting Pli1 loss produces profound SUMO-pathway defects and centromere dysfunction. This establishes a feedback architecture: Pli1 makes SUMO chains; SUMO chains on Pli1 itself (if not removed by Ulp1 at the pore) mark it for STUbL-mediated destruction — making the nuclear-pore-localized Ulp1 a guardian of the ligase.

### Finding 9 — Pli1 functions in meiotic recombination and in an interstrand-crosslink repair pathway

Pli1 contributes to meiotic recombination through SUMOylation of linear-element (LinE) proteins. Pmt3/SUMO localizes transiently along meiotic linear elements, and "mutation of the SUMO ligase Pli1 caused aberrant LinE formation and reduced genetic recombination indicating a role for SUMOylation of LinEs for the regulation of meiotic recombination" ([PMID: 19756689](https://pubmed.ncbi.nlm.nih.gov/19756689/)); Pli1 is required for a post-translational modification of the major LinE component Rec10 (the Red1 homolog). Independently, a synthetic-genetic-array analysis of DNA interstrand-crosslink (ICL) repair revealed that, in addition to the Pso2 and Fan1 routes, "we also demonstrate the existence of a third pathway of ICL repair, dependent on the SUMO E3 ligase Pli1" ([PMID: 24192486](https://pubmed.ncbi.nlm.nih.gov/24192486/)). A further link to repair-pathway choice comes from checkpoint signaling: Rad3-dependent phosphorylation of Rad9 can redirect repair "through a Pli1-mediated sumoylation pathway into the error-free branch of the Rhp6 repair pathway" ([PMID: 17515930](https://pubmed.ncbi.nlm.nih.gov/17515930/)).

### Finding 10 — Residue-level domain architecture (727 aa)

UniProt curation of O94451 defines Pli1 as a 727-amino-acid protein with an N-terminal **SAP domain (residues ~18–52)**, a **PINIT domain (~108–261)**, and a catalytic **SP-RING-type zinc finger (~290–371)** bearing four annotated metal-coordinating residues, followed by a long disordered/low-complexity C-terminal region (~408–558 and 706–727). The corresponding Pfam/InterPro signatures are PF02037/SAP (IPR003034), PF14324/PINIT (IPR023321), and PF02891 zf-MIZ / SIZ1/2 SP-RING (IPR031141), plus the SAP and PINIT superfamily folds (IPR036361, IPR038654). This architecture is the defining signature of the Siz/PIAS family and confirms protein identity.

### Finding 11 — Capstone synthesis

Integrating 24 primary and review papers with UniProt structural curation, Pli1 (727 aa; SPAC1687.05; PIAS1 ortholog) is the principal nuclear SUMO E3 ligase of *S. pombe*. Its catalyzed reaction is the ATP-independent isopeptide ligation of SUMO (Pmt3), relayed from the E1 (Fub2/Uba2–Rad31) via the E2 Hus5 (Ubc9), onto substrate lysines, with the SP-RING as the catalytic module, PINIT directing substrate choice, and SAP targeting chromatin. Its substrate repertoire spans bulk nuclear proteins plus specific targets (Top1, Tpz1-K242, Rec10/LinE proteins), and it uniquely builds poly-SUMO chains. It operates at centromeres, telomeres, arrested forks, and the nuclear periphery/NPC, feeding the STUbL(Slx8-Rfp/RNF4)–Cdc48-Ufd1-Npl4 degradation axis.

---

## Mechanistic Model / Interpretation

Pli1 sits at the center of the fission-yeast SUMO conjugation cascade and channels its output toward genome maintenance. The enzymatic logic and its downstream connections can be summarized as follows:

```
   ATP                SUMO (Pmt3)
    │                     │
    ▼                     ▼
 ┌────────────────────────────┐
 │  E1: Fub2/Uba2 – Rad31     │  activates SUMO (forms E1~SUMO thioester)
 └────────────┬───────────────┘
              │ trans-thioesterification
              ▼
 ┌────────────────────────────┐
 │  E2: Hus5 (Ubc9) ~ SUMO    │  charged conjugating enzyme
 └────────────┬───────────────┘
              │  <-- PLI1 acts here -->
              ▼
 ┌──────────────────────────────────────────────┐
 │  E3: PLI1  (SP-RING activates E2~SUMO;        │
 │            PINIT directs substrate;           │
 │            SAP targets chromatin/nucleus)     │
 └───────┬───────────────────────────┬──────────┘
         │ mono-SUMO                  │ poly-SUMO chains
         ▼                            ▼
  Substrate-Lys–SUMO           Substrate-(SUMO)n
  (Top1, Tpz1-K242,                 │
   Rec10/LinEs, bulk)               ▼
         │                   ┌──────────────────────┐
         │                   │ STUbL: Slx8-Rfp/RNF4 │  recognizes SUMO chains
         ▼                   └──────────┬───────────┘
   functional outcome                   ▼  poly-ubiquitin
   (silencing, telomere        ┌──────────────────────┐
    restraint, HR control)     │ Cdc48–Ufd1–Npl4      │  segregase → proteasome
                               └──────────────────────┘

  Homeostasis: Ulp1 (SENP1/2) at the NPC removes SUMO from substrates and
  from Pli1 itself, protecting Pli1 from STUbL-mediated degradation.
```

The central concept is **spatial and substrate-directed SUMOylation coupled to downstream ubiquitin-dependent turnover.** Pli1 does not merely bulk-conjugate SUMO; it tunes outcomes at specific chromatin loci:

| Nuclear location | Pli1 action | Key substrate / partner | Functional outcome |
|---|---|---|---|
| Centromeres | Poly-SUMO; Slx8 recruitment | Clr4 (H3K9me) dependent | Heterochromatin silencing, centromere clustering, faithful segregation ([15359282](https://pubmed.ncbi.nlm.nih.gov/15359282/), [39786922](https://pubmed.ncbi.nlm.nih.gov/39786922/)) |
| Telomeres | Site-specific SUMO | Tpz1-K242 (shelterin) | Stn1-Ten1 recruitment; telomerase restraint; length homeostasis ([24711392](https://pubmed.ncbi.nlm.nih.gov/24711392/), [17209013](https://pubmed.ncbi.nlm.nih.gov/17209013/)) |
| Arrested forks | Poly-SUMO | nascent-strand factors | NPC relocation; delayed HR restart ([33159083](https://pubmed.ncbi.nlm.nih.gov/33159083/)) |
| Repeats (RTS1) | Mono-SUMO | Topoisomerase I | Constrained recombination; cleared by Slx8 ([23936535](https://pubmed.ncbi.nlm.nih.gov/23936535/)) |
| Meiotic chromosomes | SUMO on LinEs | Rec10 (Red1 homolog) | Linear-element assembly; recombination ([19756689](https://pubmed.ncbi.nlm.nih.gov/19756689/)) |
| Nuclear periphery/NPC | Auto-SUMO chains | Ulp1 / STUbL / Cdc48 | Pli1 self-regulation / turnover ([26221037](https://pubmed.ncbi.nlm.nih.gov/26221037/)) |

The **poly-SUMO-chain activity** is the pivotal feature distinguishing Pli1 from the other *S. pombe* SP-RING ligase Nse2. Chains are the preferred ligand of STUbLs, so Pli1's chain-building converts a reversible post-translational mark into a commitment signal for ubiquitin-dependent extraction/degradation via Slx8-Rfp and the Cdc48–Ufd1–Npl4 segregase. This explains the striking genetic epistasis in which deleting *pli1* suppresses the genome-instability phenotypes of STUbL mutants ([PMID: 17762865](https://pubmed.ncbi.nlm.nih.gov/17762865/)): without Pli1-made chains, there is nothing toxic for the STUbL to process. The system is kept in balance by Ulp1 at the nuclear pore, which de-conjugates SUMO — including from Pli1 itself — thereby protecting the ligase from self-destruction and preventing runaway chain accumulation.

In short, Pli1's **primary function** is enzymatic: it is a SUMO E3 ligase (EC 2.3.2.-) that catalyzes isopeptide transfer of Pmt3/SUMO onto substrate lysines in the nucleus. Its **biological role** is genome guardianship — silencing, segregation, telomere and fork homeostasis, and recombination control — achieved by directing SUMO (and SUMO chains) onto the right substrates at the right chromatin addresses and handing the products to the STUbL/segregase pathway.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [15359282](https://pubmed.ncbi.nlm.nih.gov/15359282/) | *Pli1p in centromere and telomere maintenance* | Founding identification of Pli1 as the sole SP-RING SUMO E3 ligase; RING-point mutants lose activity; centromere/telomere phenotypes |
| [17209013](https://pubmed.ncbi.nlm.nih.gov/17209013/) | *SUMO in telomere maintenance* | Pli1 is the principal (not Nse2) bulk ligase; telomere control via telomerase activity, not recombination |
| [24265825](https://pubmed.ncbi.nlm.nih.gov/24265825/) | *Ufd1 and STUbLs in DDR* | Pli1 = PIAS1 ortholog; physical/functional link to Rfp1/RNF4 STUbL and Cdc48-Ufd1-Npl4 |
| [39786922](https://pubmed.ncbi.nlm.nih.gov/39786922/) | *Slx8 at clustered centromeres* | Pli1 + poly-SUMO + Clr4 drive Slx8 focus formation and peripheral silencing |
| [19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/) | *Structure of Siz1 SUMO E3 ligase* | Mechanistic roles of SP-RING (E2~SUMO activation) and PINIT (substrate redirection to PCNA K164) |
| [16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/) | *Ull1/Siz1 ligase + regulatory domains* | PINIT and SP-RING both required for ligase activity |
| [19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/) | *SIZ1 domain structures* | SP-RING required for SUMO conjugation + nuclear localization; PINIT for in-vivo SUMOylation |
| [20404572](https://pubmed.ncbi.nlm.nih.gov/20404572/) | *Structural/functional SIZ1* | Domains make separable contributions in a PIAS/Siz ortholog |
| [30242710](https://pubmed.ncbi.nlm.nih.gov/30242710/) | *Trapping E3-substrate intermediates* | General mechanism: SP-RING/RING-like domains activate E2-Ubl thioester for lysine attack |
| [23936535](https://pubmed.ncbi.nlm.nih.gov/23936535/) | *Slx8 removes Pli1-dependent Top1-SUMO* | Top1 is a direct Pli1 substrate; SUMO constrains recombination at RTS1 |
| [24711392](https://pubmed.ncbi.nlm.nih.gov/24711392/) | *SUMOylation of Tpz1* | Tpz1-K242 SUMOylation → Stn1-Ten1 recruitment, telomerase restraint |
| [33159083](https://pubmed.ncbi.nlm.nih.gov/33159083/) | *Nuclear pore primes RDR at arrested forks* | Pli1 at arrested forks; poly-SUMO → NPC relocation, delayed HR restart |
| [21444718](https://pubmed.ncbi.nlm.nih.gov/21444718/) | *Distinct Ubc9 noncovalent complexes* | Ubc9:SUMO + Pli1 drive global sumoylation and chain formation |
| [19756689](https://pubmed.ncbi.nlm.nih.gov/19756689/) | *SUMOylation in linear elements/meiosis* | Pli1 required for LinE/Rec10 modification and meiotic recombination |
| [24192486](https://pubmed.ncbi.nlm.nih.gov/24192486/) | *Fan1 and Pli1 in ICL repair* | Pli1 defines a third, Pso2/Fan1-independent ICL repair pathway |
| [17762865](https://pubmed.ncbi.nlm.nih.gov/17762865/) | *STUbLs in genome stability* | *pli1Δ* suppresses STUbL-mutant instability → Pli1 chains are the STUbL substrate |
| [26221037](https://pubmed.ncbi.nlm.nih.gov/26221037/) | *Pli1 protected by Ulp1 at the pore* | Pli1 is itself a SUMO substrate; Ulp1 protects it from STUbL/Cdc48 degradation |
| [26537787](https://pubmed.ncbi.nlm.nih.gov/26537787/) | *Proteome-wide SUMO sites* | >1,000 SUMO sites; STUbL/Ufd1 substrates enriched at centromeres/telomeres |
| [18031226](https://pubmed.ncbi.nlm.nih.gov/18031226/) | *S. pombe SUMO ligases review* | Comparative Pli1 vs Nse2 roles in genome stability |
| [17515930](https://pubmed.ncbi.nlm.nih.gov/17515930/) | *Rad9 phosphorylation & repair choice* | Checkpoint signaling can route repair into a Pli1-sumoylation branch |

Supporting/contextual references on SUMO-like domains and substrate scope include [PMID: 19363481](https://pubmed.ncbi.nlm.nih.gov/19363481/) (Rad60 SLD1 binds the Pli1/Siz E3 specificity enzyme) and [PMID: 40254064](https://pubmed.ncbi.nlm.nih.gov/40254064/) (global UBL-substrate analysis, including a non-protein substrate — spermidine — of fission-yeast SUMO Pmt3). Arabidopsis SIZ1/MMS21 comparative work ([PMID: 23056518](https://pubmed.ncbi.nlm.nih.gov/23056518/), [PMID: 18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/)) reinforces the conserved Siz/PIAS domain logic used to interpret Pli1.

**Convergence of evidence.** The identification of Pli1 as a SUMO E3 ligase rests on direct biochemistry (*in vitro* ligase activity), genetics (RING-point mutants phenocopy deletion in proportion to activity loss), orthology (PIAS1/Siz1), and structural/domain conservation (SAP-PINIT-SP-RING). Substrate assignments (Top1, Tpz1-K242, Rec10) come from targeted studies rather than high-throughput inference alone, satisfying the preference for precise over high-throughput evidence.

---

## Limitations and Knowledge Gaps

1. **Few direct, structurally defined Pli1 substrates.** Only a handful of substrate lysines are precisely mapped (notably Tpz1-K242). The exact sites on Top1 and most bulk substrates, and the structural basis of Pli1 substrate choice (how PINIT and SAP cooperate for each target), remain uncharacterized for the fission-yeast enzyme specifically.

2. **Mechanism of telomerase regulation is indirect.** Pli1 restrains telomere length by modulating telomerase activity via a regulator, with Tpz1-K242 as the leading link, but the complete chain from Pli1 → Tpz1-SUMO → Stn1-Ten1 → telomerase has not been fully reconstituted biochemically.

3. **No experimental 3D structure of Pli1 itself.** Mechanistic inferences about the SP-RING, PINIT, and SAP domains derive largely from orthologs (Siz1, SIZ1) and from UniProt/InterPro domain annotation; a fission-yeast Pli1 structure (or validated AlphaFold model with catalytic-site analysis) would refine the model.

4. **Quantitative E2/chain-switch regulation.** How the Ubc9:SUMO noncovalent complex and Pli1 are regulated *in vivo* to toggle between mono-SUMOylation and poly-chain building at specific loci is not resolved.

5. **Dependence on database annotation for some structural detail.** Finding 10's residue boundaries come from UniProt curation; while consistent with the family, exact domain limits for Pli1 are computational.

6. **Pleiotropy vs. direct role.** Some phenotypes (global recombination deregulation) could be indirect consequences of bulk-sumoylation loss rather than a dedicated Pli1 substrate pathway; distinguishing direct from downstream effects remains incomplete.

---

## Proposed Follow-up Experiments / Actions

1. **Map Pli1 substrate lysines at scale with site resolution.** Apply SUMO-site proteomics (e.g., pLink-UBL, [PMID: 40254064](https://pubmed.ncbi.nlm.nih.gov/40254064/)) in WT vs *pli1Δ* vs *pli1* RING-dead strains to define the *Pli1-dependent* sub-SUMOylome and distinguish direct from indirect targets.

2. **Reconstitute the Tpz1 telomere axis in vitro.** Use purified Pli1, Hus5/Ubc9, Pmt3 E1, and Tpz1 to confirm K242 as a direct Pli1 site and test whether Tpz1-SUMO directly enhances Stn1-Ten1 binding — closing the mechanistic gap in telomere-length control.

3. **Solve or model the Pli1 structure.** Obtain a cryo-EM/crystal structure or a validated AlphaFold model of Pli1 (full length and SP-RING–PINIT module), and use it with mutagenesis to test substrate-redirection by PINIT and chromatin engagement by SAP.

4. **Dissect the mono- vs. poly-SUMO switch.** Engineer Pli1 variants or Ubc9-complex mutants that selectively abolish chain-building while retaining mono-SUMOylation, and assay effects on STUbL recruitment, fork-to-NPC relocation ([PMID: 33159083](https://pubmed.ncbi.nlm.nih.gov/33159083/)), and centromere clustering ([PMID: 39786922](https://pubmed.ncbi.nlm.nih.gov/39786922/)).

5. **Separation-of-function alleles.** Build domain-specific *pli1* alleles (SAP-dead, PINIT-dead, SP-RING-dead) and systematically assign centromere, telomere, meiotic, and ICL-repair phenotypes to individual domains — mirroring the SIZ1 domain-dissection strategy ([PMID: 19837819](https://pubmed.ncbi.nlm.nih.gov/19837819/), [PMID: 20404572](https://pubmed.ncbi.nlm.nih.gov/20404572/)).

6. **Quantify the Ulp1–Pli1 homeostatic loop.** Use the *nup132Δ* delocalization system ([PMID: 26221037](https://pubmed.ncbi.nlm.nih.gov/26221037/)) with live-cell imaging to measure Pli1 stability, auto-SUMOylation, and STUbL/Cdc48-dependent turnover kinetics.

7. **Test human-ortholog complementation.** Determine whether human PIAS1 can rescue defined *pli1Δ* phenotypes, as was shown for RNF4↔Slx8 ([PMID: 17762865](https://pubmed.ncbi.nlm.nih.gov/17762865/)), to formally establish functional orthology.

---

## Conclusion

Pli1 (SPAC1687.05 / UniProt O94451) is unambiguously identified as the **principal nuclear SUMO E3 ligase of *S. pombe***, the sole Siz/PIAS SP-RING family member and the human PIAS1 ortholog. Its primary, catalyzed function is the ATP-independent isopeptide ligation of SUMO (Pmt3) onto substrate lysines — relayed from the E1 (Fub2/Uba2–Rad31) and E2 (Hus5/Ubc9) — with its SP-RING domain providing catalysis, its PINIT domain directing substrate selection, and its SAP domain targeting chromatin. It uniquely builds poly-SUMO chains. Acting in the nucleus at centromeres, telomeres, arrested replication forks, meiotic chromosomes, and the nuclear periphery, Pli1 maintains heterochromatic silencing and chromosome segregation, restrains telomerase/telomere length (via Tpz1-K242), controls homologous recombination (via Top1 and others), supports meiotic recombination and interstrand-crosslink repair, and feeds its (poly-)SUMOylated products into the STUbL (Slx8-Rfp/RNF4)–Cdc48-Ufd1-Npl4 degradation axis — all under homeostatic control by the nuclear-pore SUMO protease Ulp1.


## Artifacts

- [OpenScientist final report](pli1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pli1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15359282
2. PMID:17209013
3. PMID:18031226
4. PMID:19748360
5. PMID:16109721
6. PMID:19837819
7. PMID:20404572
8. PMID:30242710
9. PMID:39786922
10. PMID:24265825
11. PMID:17762865
12. PMID:26537787
13. PMID:23936535
14. PMID:24711392
15. PMID:33159083
16. PMID:21444718
17. PMID:26221037
18. PMID:19756689
19. PMID:24192486
20. PMID:17515930
21. PMID:19363481
22. PMID:40254064
23. PMID:23056518
24. PMID:18583943