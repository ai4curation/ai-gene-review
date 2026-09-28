---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:05:13.275322'
end_time: '2026-09-01T16:28:51.688499'
duration_seconds: 1418.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ku
  gene_symbol: ku
  uniprot_accession: Q88HU8
  protein_description: 'RecName: Full=Non-homologous end joining protein Ku {ECO:0000256|HAMAP-Rule:MF_01875};'
  gene_info: Name=ku {ECO:0000256|HAMAP-Rule:MF_01875}; OrderedLocusNames=PP_3255
    {ECO:0000313|EMBL:AAN68862.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the prokaryotic Ku family. {ECO:0000256|HAMAP-
  protein_domains: DNA_bd_Ku70/Ku80. (IPR006164); Prok_Ku. (IPR009187); SPOC-like_C_dom_sf.
    (IPR016194); Ku (PF02735)
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ku-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ku-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HU8
- **Protein Description:** RecName: Full=Non-homologous end joining protein Ku {ECO:0000256|HAMAP-Rule:MF_01875};
- **Gene Information:** Name=ku {ECO:0000256|HAMAP-Rule:MF_01875}; OrderedLocusNames=PP_3255 {ECO:0000313|EMBL:AAN68862.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the prokaryotic Ku family. {ECO:0000256|HAMAP-
- **Key Domains:** DNA_bd_Ku70/Ku80. (IPR006164); Prok_Ku. (IPR009187); SPOC-like_C_dom_sf. (IPR016194); Ku (PF02735)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ku" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ku' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ku** (gene ID: ku, UniProt: Q88HU8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Non-Homologous End Joining Protein Ku (gene *ku*, PP_3255, UniProt Q88HU8) in *Pseudomonas putida* KT2440

## Summary

The gene **ku** (locus **PP_3255**; UniProt **Q88HU8**) of *Pseudomonas putida* KT2440 encodes the **Non-Homologous End Joining (NHEJ) protein Ku**, the DNA-double-strand-break (DSB) end-binding component of the bacterial NHEJ DNA-repair pathway. Ku is **not an enzyme**; it is a sequence-independent DNA-end-recognition and end-bridging protein. Its identity is unambiguous: the UniProt record assigns it to the prokaryotic Ku family (Pfam **PF02735** "Ku"; InterPro **IPR009187** "Prok_Ku"; **IPR006164** Ku70/Ku80 DNA-binding core; **IPR016194** SPOC-like C-terminal domain), and *P. putida* KT2440 is one of the minority of bacteria that encodes both Ku and its obligate catalytic partner **DNA ligase D (LigD)** — the two proteins that constitute the complete, self-sufficient bacterial NHEJ machine. This report therefore concerns the correct target: the bacterial (prokaryotic) Ku, which functions as a **homodimer**, in contrast to the eukaryotic Ku70/Ku80 heterodimer.

Mechanistically, Ku performs the first three of the five canonical NHEJ phases — **end sensing, end protection, and end tethering**. It recognizes and clamps blunt or near-blunt broken dsDNA ends without regard to sequence, shields those ends from nucleolytic (exonuclease) degradation, threads inward along the DNA duplex, and oligomerizes into higher-order arrays that bridge and synapse the two broken ends. Through a defined C-terminal subregion, Ku then recruits and stimulates LigD, handing off the held ends to the catalytic machine (LigD supplies polymerase, 3′-phosphoesterase, and ATP-dependent ligase activities) that processes and reseals the break. Ku is the **rate-limiting factor** of the pathway and the structural anchor on which the entire end-joining apparatus is built.

Biologically, Ku-dependent NHEJ provides *P. putida* with a **template-independent, RecA-independent, intrinsically mutagenic** route to repair chromosomal DSBs. This pathway is most important when a homologous sister template is unavailable — for example in stationary phase or dormancy — and it operates in the cytoplasm/nucleoid directly at break sites on chromosomal DNA. In *P. putida* KT2440 specifically, the presence of Ku+LigD makes the strain a valuable genome-engineering chassis, because Ku-dependent NHEJ shapes the mutational outcomes of programmable DSBs introduced by CRISPR-Cas9 and I-SceI editing tools.

---

## Key Findings

### Finding 1 — Ku (PP_3255, Q88HU8) is the DNA-end-binding component of prokaryotic NHEJ in *P. putida*, acting with LigD

The identity of the target is verified at the sequence and family level. UniProt **Q88HU8** corresponds to gene *ku* / locus **PP_3255** and is assigned to the prokaryotic Ku family through Pfam **PF02735** ("Ku"), InterPro **IPR009187** ("Prok_Ku"), and the Ku70/Ku80 DNA-binding core domain **IPR006164**. Crucially, *P. putida* KT2440 is documented to encode **both** Ku and LigD — the two-component minimal NHEJ system — a feature that distinguishes it from most bacteria. This pathway repairs Cas9-generated double-strand breaks in vivo in *P. putida* ([PMID: 36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/)): *"Unlike most bacteria, P. putida KT2440 encodes the Ku and LigD proteins involved in Non-Homologous End Joining (NHEJ)."*

A defining structural feature separating the bacterial protein from its eukaryotic namesake is quaternary organization: **bacterial Ku functions as a homodimer**, whereas the eukaryotic version is a Ku70/Ku80 heterodimer ([PMID: 41118517](https://pubmed.ncbi.nlm.nih.gov/41118517/)): *"bacterial NHEJ operates with a simpler toolkit comprising a Ku homodimer and the multifunctional LigD."* This homodimeric architecture and the reduced "toolkit" define the mechanistic context in which the *P. putida* protein operates.

### Finding 2 — Ku binds DNA ends, bridges/synapses the two broken ends, threads inward, and recruits LigD via its C-terminus

Structural and biochemical studies of bacterial Ku homologs converge on a consistent mechanistic picture. Ku is a **ring/clamp-structured protein** that binds DNA ends and then recruits downstream factors that access the ends by **threading of Ku inward** along the DNA ([PMID: 26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/)): *"The ring structured eukaryotic Ku binds DNA ends and recruits other factors which can access DNA ends through the threading of Ku inward the DNA."* The same study dissects the C-terminus and assigns discrete mechanistic roles to its subregions: *"the minimal C-terminus is required for the Ku-LigD interaction, whereas the basic extension controls the threading and DNA bridging abilities of Ku."* Thus the **minimal C-terminal region mediates LigD recruitment**, while the **basic C-terminal extension governs threading and DNA bridging**.

Two recent cryo-EM studies provide direct structural confirmation of the synapsis function. Cryo-EM of *Mycobacterium tuberculosis* Ku shows it forms an **extended proteo-filament** upon DNA binding, with the C-terminus regulating DNA loading and facilitating LigD recruitment ([PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/)): *"the C-terminus of Ku regulates DNA binding and loading and facilitates subsequent recruitment of LigD."* Independently, a 2.74 Å cryo-EM structure of *Bacillus subtilis* Ku captured **two blunt DNA ends bridged by Ku alone**, supporting a model in which oligomeric arrays of Ku homodimers physically synapse the break ([PMID: 41118517](https://pubmed.ncbi.nlm.nih.gov/41118517/)): *"oligomeric arrays of Ku homodimers bridge and stabilize two DNA ends, facilitating efficient DSB repair."* Together these findings establish that Ku itself synapses the two broken ends prior to ligation and controls the hand-off to the catalytic step.

### Finding 3 — Ku-dependent NHEJ repairs DSBs in *P. putida* and shapes error-prone (mutagenic) end-joining outcomes

In *P. putida* KT2440, genetic manipulation of the NHEJ machinery has direct, measurable consequences on DSB repair. Removing or overproducing Ku/LigD alters the spectrum of mutations generated upon repair of Cas9-mediated DSBs, and the pathway carries intrinsic mutagenic potential ([PMID: 36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/)): *"This pathway of repair of double-strand breaks (DSBs) in DNA has an intrinsic mutagenic potential."* This establishes a bona fide, non-templated DSB-repair activity operating in the living cell and demonstrates that Ku status is causally connected to repair outcomes.

The central importance of Ku is reinforced by cross-pathway genetics in the related pseudomonad *P. aeruginosa*, where deletion analysis found **RecA and Ku (but not LigD) conditionally essential**, revealing that *Pseudomonas* can perform even **LigD-independent NHEJ** ([PMID: 42306942](https://pubmed.ncbi.nlm.nih.gov/42306942/)): *"RecA and Ku (but not LigD) are conditionally essential, which suggests that P. aeruginosa can conduct LigD-independent NHEJ."* This positions Ku as the central, most essential NHEJ factor in *Pseudomonas* — it remains functionally important even under conditions where the canonical ligase is dispensable, underscoring that Ku's end-recognition/bridging role is the indispensable core of the pathway.

### Finding 4 — Ku + LigD constitute a complete, self-sufficient two-component NHEJ machine; Ku provides end recognition/bridging while LigD provides all processing/ligation chemistry

The foundational reconstitution of bacterial NHEJ established that just two proteins suffice. Della et al. (2004, *Science*) demonstrated that prokaryotic Ku and ligase *"form a bona fide NHEJ system that encodes all the recognition, processing, and ligation activities required for DSB repair"* ([PMID: 15499016](https://pubmed.ncbi.nlm.nih.gov/15499016/)). Within this division of labor, **Ku contributes end recognition and bridging**, whereas **LigD supplies all catalytic chemistry**. LigD is a modular enzyme comprising an N-terminal polymerase (POL) domain, a central 3′-phosphoesterase (PE) domain, and a C-terminal ATP-dependent ligase (LIG) domain ([PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/)): *"LigD, a modular enzyme composed of a C-terminal ATP-dependent ligase domain (LIG), a central 3'-phosphoesterase domain (PE), and an N-terminal polymerase domain (POL)."*

The mutagenicity of NHEJ is mechanistically traceable to the LigD polymerase acting on Ku-held ends. LigD POL *"is proficient at adding templated and nontemplated deoxynucleotides and ribonucleotides to DNA ends in vitro and is the catalyst in vivo of unfaithful NHEJ events involving nontemplated single-nucleotide additions to blunt DSB ends"* ([PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/)). Because Ku holds and synapses the ends while LigD performs these often-inaccurate additions and the final seal, the pathway is intrinsically error-prone — yet capable of joining even incompatible ends that other pathways cannot. This clarifies precisely which activities belong to Ku (non-catalytic end recognition, protection, bridging, LigD recruitment) versus its partner (all nucleotidyl-transfer and ligation chemistry).

### Finding 5 — Ku is the rate-limiting DNA-end sensor that protects broken ends from nucleolytic degradation and oligomerizes on DNA to drive synapsis

Detailed in vitro/in silico characterization of mycobacterial Ku demonstrates the physical properties underlying its end-protection and synapsis functions. Ku binds linear dsDNA with **positive cooperativity for substrates ≥40 bp**, can **slide along DNA**, and forms **DNA-dependent higher-order oligomers** implicated in synapsis; importantly, Ku binding both stabilizes the nucleoprotein complex and **shields DNA ends from exonuclease degradation** ([PMID: 39122073](https://pubmed.ncbi.nlm.nih.gov/39122073/)): *"mKu's DNA binding stabilizes both the protein and DNA, while also shielding DNA ends from exonuclease degradation,"* and *"showing positive cooperativity for DNA substrates of 40 base pairs or longer, and its ability to slide along DNA strands."* The cooperative loading and sliding behavior provides the physical basis for the inward-threading and oligomerization steps described above.

Cryo-EM has now defined the Ku–Ku dimerization, DNA-binding, and synapsis interfaces and confirmed that **Ku is the rate-limiting factor** of two-component NHEJ, with NHEJ being the sole DSB-repair pathway available during mycobacterial dormancy ([PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)): *"relying on mycobacterial Ku (mKu) and ligase D, with mKu as the rate-limiting factor."* The broader pathway context is that NHEJ is one of several DSB-repair options — operating alongside homologous recombination (HR) and single-strand annealing (SSA) — and becomes especially important when a sister template is absent ([PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/)). By analogy and by shared machinery, the *P. putida* Ku occupies the same rate-limiting, end-protecting position in its NHEJ system.

### Finding 6 — Ku's defining role is the "end-sensing / end-protection / end-tethering" anchor of NHEJ; in *P. putida* this underpins its use as a genome-engineering chassis

Contemporary mechanistic reviews frame NHEJ as five sequential phases — **end sensing, end protection, end tethering, end processing, and end ligation** — and emphasize that the pathway relies on protein assemblies rather than sequence complementarity ([PMID: 41871908](https://pubmed.ncbi.nlm.nih.gov/41871908/)): *"relying instead on protein assemblies to bridge and stabilize the two DNA ends."* Critically, the end-tethering machineries are *"all anchored on Ku"* — placing Ku, the earliest-acting non-catalytic factor, at the organizing center of the first three phases. In the streamlined prokaryotic Ku+LigD system, Ku alone therefore carries out end sensing, end protection, and end tethering, before LigD performs processing and ligation.

In *P. putida* KT2440 specifically, the (atypical) presence of Ku+LigD makes NHEJ a practical lever in genome engineering. NHEJ is exploited alongside CRISPR-Cas9 and I-SceI double-strand-break tools; NHEJ status modulates the mutational outcomes of programmable DSBs and is an active consideration in the strain's editing toolbox ([PMID: 36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/); [PMID: 39031514](https://pubmed.ncbi.nlm.nih.gov/39031514/)). The I-SceI-based editing system for *P. putida* KT2440 uses a *"double-strand break introducing gene I-sceI and sacB counterselection marker"* ([PMID: 39031514](https://pubmed.ncbi.nlm.nih.gov/39031514/)) — the applied context in which Ku-dependent end joining competes with (or is suppressed in favor of) homology-directed repair to achieve precise edits.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent, well-supported model of Ku as the **non-catalytic scaffold** that initiates and organizes bacterial NHEJ in *P. putida*. The two-component machine can be summarized as a sequential hand-off:

```
   Double-strand break in chromosomal DNA (cytoplasm / nucleoid)
                          |
                          v
  [1] END SENSING    Ku homodimer recognizes blunt/near-blunt dsDNA
                     ends (sequence-independent), loads as ring/clamp
                          |
                          v
  [2] END PROTECTION Ku shields ends from exonuclease degradation;
                     stabilizes the nucleoprotein complex
                          |
                          v
  [3] END TETHERING  Ku threads inward (basic C-terminal extension),
                     binds cooperatively (>=40 bp), slides, and
                     oligomerizes into arrays that BRIDGE / SYNAPSE
                     the two broken ends
                          |
                          v
  [4] LigD RECRUIT   Minimal C-terminal subregion of Ku recruits
                     and stimulates LigD
                          |
                          v
  [5] PROCESS+LIGATE LigD POL (fill-in, +/- nontemplated nt ->
                     mutagenic), LigD PE (3'-P processing),
                     LigD LIG (ATP-dependent seal)
                          |
                          v
        Repaired DNA (often with small insertions/deletions)
```

**Division of labor.** The table below summarizes which activities are supplied by Ku versus LigD, clarifying that Ku is entirely non-catalytic and LigD supplies all chemistry.

| NHEJ phase | Protein responsible | Activity | Key evidence |
|---|---|---|---|
| End sensing | **Ku** (homodimer) | Sequence-independent dsDNA end binding | [PMID: 26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/) |
| End protection | **Ku** | Shields ends from exonucleases; stabilizes complex | [PMID: 39122073](https://pubmed.ncbi.nlm.nih.gov/39122073/) |
| End tethering / synapsis | **Ku** | Threading, cooperative binding, oligomer arrays bridge two ends | [PMID: 41118517](https://pubmed.ncbi.nlm.nih.gov/41118517/); [PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/) |
| Ligase recruitment | **Ku** (minimal C-terminus) | Recruits/stimulates LigD | [PMID: 26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/); [PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/) |
| End processing | **LigD** (POL, PE) | Fill-in synthesis (± nontemplated nt), 3′-phosphoesterase | [PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/) |
| End ligation | **LigD** (LIG) | ATP-dependent nick sealing | [PMID: 15499016](https://pubmed.ncbi.nlm.nih.gov/15499016/) |

**Localization.** Ku carries out its function **inside the cell, in the cytoplasm/nucleoid, directly at DSB sites on chromosomal DNA**. There is no signal peptide or transmembrane character implied by the family; the protein's substrate is the physical DNA end, so its site of action is defined by wherever a break occurs on the genome.

**Pathway logic.** Ku-dependent NHEJ is a **template-independent** and (in *Pseudomonas*) at least partly **RecA-independent** DSB-repair route. Because it does not require a homologous donor, it is the pathway of choice when a sister chromosome is unavailable — notably in **stationary phase / dormancy** — but this convenience comes at the cost of fidelity: LigD's ability to add nontemplated nucleotides to Ku-held ends makes the outcome intrinsically **mutagenic**. Ku is the **rate-limiting** component and the physical **anchor** for the whole assembly, which is why its loss cripples NHEJ even where LigD can be bypassed.

**Applied significance in *P. putida*.** Because KT2440 unusually possesses this machine, Ku-dependent NHEJ is a real force in the strain's genome-editing behavior: it competes with homology-directed repair at CRISPR-Cas9 and I-SceI breaks and biases outcomes toward small indels. Editing strategies for *P. putida* therefore either exploit NHEJ (for random small mutations) or suppress it (to favor precise, homology-directed edits).

---

## Evidence Base

| PMID | Organism / system | Contribution to this report | Type |
|---|---|---|---|
| [36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/) | *P. putida* KT2440 | **Direct**: KT2440 encodes Ku+LigD; NHEJ repairs Cas9 DSBs; intrinsically mutagenic | Primary (in vivo, target organism) |
| [42306942](https://pubmed.ncbi.nlm.nih.gov/42306942/) | *P. aeruginosa* | Ku (not LigD) conditionally essential; LigD-independent NHEJ; Ku is central | Primary (genetics, close relative) |
| [26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/) | Bacterial Ku | C-terminus dissection: LigD interaction vs. threading/bridging roles | Primary (biochemistry) |
| [41118517](https://pubmed.ncbi.nlm.nih.gov/41118517/) | *B. subtilis* | Cryo-EM (2.74 Å): Ku homodimer arrays bridge two blunt DNA ends | Primary (structure) |
| [41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/) | *M. tuberculosis* | Cryo-EM: Ku proteo-filament; C-terminus controls loading + LigD recruitment | Primary (structure) |
| [39122073](https://pubmed.ncbi.nlm.nih.gov/39122073/) | Mycobacterial Ku | Cooperative binding (≥40 bp), sliding, oligomerization, exonuclease shielding | Primary (in vitro/in silico) |
| [41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/) | Mycobacterial Ku | Cryo-EM of Ku–DNA synaptic complex; Ku is rate-limiting; NHEJ in dormancy | Primary (structure) |
| [15499016](https://pubmed.ncbi.nlm.nih.gov/15499016/) | Prokaryotic Ku+LigD | Foundational: Ku+LigD = complete two-component NHEJ machine | Primary (reconstitution) |
| [23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/) | *M. smegmatis* | LigD domain architecture (POL/PE/LIG); POL is catalyst of mutagenic additions | Primary (biochemistry) |
| [21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/) | *M. smegmatis* | NHEJ is one of three DSB pathways (HR, NHEJ, SSA); error-prone | Primary (genetics) |
| [41871908](https://pubmed.ncbi.nlm.nih.gov/41871908/) | Review | Five-phase NHEJ framework; end-tethering "all anchored on Ku" | Review |
| [39031514](https://pubmed.ncbi.nlm.nih.gov/39031514/) | *P. putida* KT2440 | I-SceI DSB-based genome editing — applied context for NHEJ | Primary (methods) |

**How the evidence supports the annotation.** The target-organism paper ([PMID: 36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/)) directly establishes that *P. putida* KT2440 possesses and uses Ku for NHEJ, and that the pathway is mutagenic in vivo. The reconstitution paper ([PMID: 15499016](https://pubmed.ncbi.nlm.nih.gov/15499016/)) demonstrates that Ku+LigD alone suffice for the entire pathway, defining the minimal machine. Structural studies in *B. subtilis*, *M. tuberculosis*, and *Mycobacterium* ([PMID: 41118517](https://pubmed.ncbi.nlm.nih.gov/41118517/); [PMID: 41298423](https://pubmed.ncbi.nlm.nih.gov/41298423/); [PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/)) provide the physical basis for end bridging, synapsis, and rate-limiting behavior. Biochemical dissection ([PMID: 26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/); [PMID: 39122073](https://pubmed.ncbi.nlm.nih.gov/39122073/)) assigns specific functions to Ku subregions and confirms end protection. The LigD papers ([PMID: 23198659](https://pubmed.ncbi.nlm.nih.gov/23198659/); [PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/)) delineate the boundary between Ku's non-catalytic role and LigD's chemistry.

**Note on cross-organism inference.** Because there is currently no published high-resolution structure or detailed biochemistry of the *P. putida* KT2440 Ku protein itself, several mechanistic details (threading, oligomerization, synapsis interfaces, exonuclease protection) are inferred from well-characterized bacterial orthologs (*B. subtilis*, *M. tuberculosis/smegmatis*). This inference is strongly justified by the high conservation of the prokaryotic Ku family (shared Pfam/InterPro domains) and by the direct in vivo demonstration that KT2440 Ku participates in NHEJ. The applied *P. putida* observations ([PMID: 36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/); [PMID: 39031514](https://pubmed.ncbi.nlm.nih.gov/39031514/)) anchor the general model to the target organism.

---

## Limitations and Knowledge Gaps

1. **No target-specific structure or biochemistry.** The detailed mechanistic attributes (DNA sliding, cooperative loading ≥40 bp, oligomer-array synapsis, exonuclease shielding, precise C-terminal subregion functions) are established for mycobacterial and *B. subtilis* Ku, not for *P. putida* PP_3255. While family conservation makes transfer of these properties well-founded, the KT2440 protein has not been crystallized, cryo-EM-solved, or biochemically reconstituted in isolation.

2. **LigD-independent NHEJ is incompletely defined.** The *P. aeruginosa* finding that Ku (but not LigD) is conditionally essential implies an alternative ligase or LigD-independent route ([PMID: 42306942](https://pubmed.ncbi.nlm.nih.gov/42306942/)), but the identity of the substitute ligase and whether the same holds in *P. putida* remains unresolved.

3. **Physiological trigger conditions in *P. putida* are inferred, not measured.** The claim that NHEJ dominates in stationary phase/dormancy derives largely from mycobacterial work ([PMID: 41521670](https://pubmed.ncbi.nlm.nih.gov/41521670/); [PMID: 21219454](https://pubmed.ncbi.nlm.nih.gov/21219454/)). The specific growth-phase and stress dependence of *ku* expression and NHEJ activity in KT2440 has not been directly quantified here.

4. **Quantitative parameters absent for the target.** DNA-binding affinities (Kd), stoichiometry, and end-joining efficiencies are available for orthologs but not for Q88HU8 specifically. Effect sizes for how *ku* deletion/overexpression shifts edit outcomes in KT2440 are described qualitatively in the literature rather than tabulated here.

5. **Regulation and interactome unexplored.** Whether *P. putida* Ku is regulated (transcriptionally, post-translationally) or interacts with additional accessory factors beyond LigD (as eukaryotic Ku does with XLF, XRCC4, etc.) is not established for this organism.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination of *P. putida* Ku.** Solve the cryo-EM/crystal structure of PP_3255 alone and in complex with DNA (and with LigD), to confirm the homodimer clamp, threading, and synapsis interfaces directly in the target protein rather than by homology.

2. **In vitro reconstitution with KT2440 proteins.** Purify PP_3255 Ku and *P. putida* LigD and reconstitute NHEJ on defined blunt and non-complementary end substrates; measure DNA-binding affinity, cooperativity (test the ≥40 bp threshold), exonuclease-protection, and end-joining fidelity/efficiency. Compare to mycobacterial benchmarks.

3. **Targeted C-terminal mutagenesis.** Recreate the minimal-C-terminus vs. basic-extension dissection ([PMID: 26961308](https://pubmed.ncbi.nlm.nih.gov/26961308/)) in the KT2440 protein to test whether LigD-recruitment and threading/bridging map to the same subregions.

4. **Growth-phase and stress profiling.** Quantify *ku* (PP_3255) and *ligD* expression across exponential, stationary, and stress (ionizing radiation, desiccation, oxidative, antibiotic) conditions in KT2440, and correlate with NHEJ-mediated repair efficiency using an inducible DSB reporter.

5. **Editing-outcome quantification.** Systematically measure how Δ*ku*, WT, and *ku*-overexpression backgrounds change the indel spectrum and precise-edit efficiency at CRISPR-Cas9 and I-SceI breaks in KT2440, to establish quantitative rules for exploiting or suppressing NHEJ during genome engineering ([PMID: 36475478](https://pubmed.ncbi.nlm.nih.gov/36475478/); [PMID: 39031514](https://pubmed.ncbi.nlm.nih.gov/39031514/)).

6. **Test for LigD-independent NHEJ in *P. putida*.** Replicate the *P. aeruginosa* conditional-essentiality experiment ([PMID: 42306942](https://pubmed.ncbi.nlm.nih.gov/42306942/)) in KT2440 and identify any alternative ligase that can act with Ku.

---

## Conclusion

The gene *ku* (PP_3255, UniProt Q88HU8) of *Pseudomonas putida* KT2440 encodes the **prokaryotic Non-Homologous End Joining protein Ku**, a non-catalytic, homodimeric DNA-double-strand-break end-binding scaffold. Its primary function is to **sense, protect, and tether** broken chromosomal DNA ends in a sequence-independent manner, then recruit the catalytic ligase LigD to complete repair. Ku is the rate-limiting anchor of the minimal two-component (Ku+LigD) bacterial NHEJ machine, acts in the cytoplasm/nucleoid at DSB sites, and provides a template-independent, intrinsically mutagenic repair route that is biologically most relevant when no homologous template is available — and that is a practical determinant of genome-editing outcomes in this biotechnologically important strain. The gene symbol and family assignment are unambiguous and fully consistent with the UniProt annotation.


## Artifacts

- [OpenScientist final report](ku-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ku-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36475478
2. PMID:41118517
3. PMID:26961308
4. PMID:41298423
5. PMID:42306942
6. PMID:15499016
7. PMID:23198659
8. PMID:39122073
9. PMID:41521670
10. PMID:21219454
11. PMID:41871908
12. PMID:39031514