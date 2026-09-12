---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:26:52.992728'
end_time: '2026-07-11T14:35:34.166397'
duration_seconds: 521.17
template_file: templates/module_research.md.j2
template_variables:
  module_title: prolipoprotein diacylglyceryl transfer
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00664 module for the first
    bacterial lipoprotein-maturation step, in which Lgt transfers a diacylglyceryl
    group from phosphatidylglycerol to the conserved N-terminal cysteine of a prolipoprotein.
    The local UniPathway bucket contains lgt/PP_5142/Q88CN8, a reviewed UniProtKB
    phosphatidylglycerol--prolipoprotein diacylglyceryl transferase entry with EC
    2.5.1.145 and Rhea:RHEA:56712. This module records the Lgt transfer reaction rather
    than the downstream signal-peptide cleavage and N-acylation steps catalyzed by
    LspA and Lnt.
  module_outline: "- prolipoprotein diacylglyceryl transfer\n  - 1. Lgt diacylglyceryl\
    \ transfer to prolipoprotein cysteine\n  - Lgt prolipoprotein diacylglyceryl transfer\n\
    \    - lgt: prolipoprotein diacylglyceryl transferase (molecular player: PSEPK\
    \ lgt; activity or role: phosphatidylglycerol-prolipoprotein diacylglyceryl transferase\
    \ activity)"
  module_connections: No explicit connections.
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: prolipoprotein_diacylglyceryl_transfer-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: prolipoprotein_diacylglyceryl_transfer-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

prolipoprotein diacylglyceryl transfer

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00664 module for the first bacterial lipoprotein-maturation step, in which Lgt transfers a diacylglyceryl group from phosphatidylglycerol to the conserved N-terminal cysteine of a prolipoprotein. The local UniPathway bucket contains lgt/PP_5142/Q88CN8, a reviewed UniProtKB phosphatidylglycerol--prolipoprotein diacylglyceryl transferase entry with EC 2.5.1.145 and Rhea:RHEA:56712. This module records the Lgt transfer reaction rather than the downstream signal-peptide cleavage and N-acylation steps catalyzed by LspA and Lnt.

## Provisional Biological Outline

- prolipoprotein diacylglyceryl transfer
  - 1. Lgt diacylglyceryl transfer to prolipoprotein cysteine
  - Lgt prolipoprotein diacylglyceryl transfer
    - lgt: prolipoprotein diacylglyceryl transferase (molecular player: PSEPK lgt; activity or role: phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity)

## Known Relationships Among Steps

No explicit connections.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

# Prolipoprotein Diacylglyceryl Transfer by Lgt: A Review-Style Synthesis

*Scope module: Pseudomonas putida KT2440 UniPathway UPA00664 — Lgt (PP_5142 / UniProtKB Q88CN8; EC 2.5.1.145; Rhea:RHEA:56712). Search date: 2026-07-11 (PubMed).*

---

## 1. Executive summary

Bacterial lipoproteins are membrane-anchored proteins whose defining feature is a lipid-modified N-terminal cysteine. The **first and committed step** in building that anchor is catalyzed by **prolipoprotein diacylglyceryl transferase (Lgt)**, an integral inner-membrane enzyme that transfers a **diacylglyceryl group from the membrane phospholipid phosphatidylglycerol (PG)** onto the thiol of the invariant cysteine of a "lipobox," producing a thioether-linked **S-diacylglyceryl-prolipoprotein** (EC 2.5.1.145; RHEA:56712) (PMID 28698362; PMID 26729647). This review treats the **Lgt reaction itself** as the biological system of interest — a single, mechanistically discrete, membrane-embedded acyl/glyceryl-transfer event — and deliberately separates it from the downstream signal-peptide cleavage (LspA) and N-acylation (Lnt) steps, and from the still-later Lol sorting machinery, which are frequently conflated with it.

The key conclusions are: (i) Lgt performs the committed, gatekeeping reaction of the entire lipoprotein-maturation pathway and imposes a hard ordering constraint on everything downstream (PMID 24780125; PMID 42126242); (ii) it is **universally present in bacteria and absent from archaea**, marking it as a bacterial-specific innovation tied to bacterial phospholipid chemistry (PMID 42126242; PMID 39372745); (iii) its **essentiality is lineage-dependent** — lethal in Proteobacteria, dispensable in several monoderms (PMID 35938851; PMID 32490790; PMID 31226163); and (iv) crystal structures rationalize a **membrane-lateral, two-site catalytic mechanism** with essential active-site arginines (PMID 26729647; PMID 31340643). Because it is essential in Gram-negatives, surface-accessible, and mechanistically distinct from human enzymes, Lgt is an actively pursued antibiotic target (PMID 33875545; PMID 31036406).

---

## 2. Definition and biological boundaries

### 2.1 What is included

The system is the **single enzymatic reaction**:

> phosphatidylglycerol + [prolipoprotein]-L-cysteine → [prolipoprotein]-S-1,2-diacyl-sn-glyceryl-L-cysteine + sn-glycerol-1-phosphate

catalyzed by Lgt. Its scope comprises: (1) recognition of an unmodified prolipoprotein bearing a **lipobox** — the consensus [LVI]-[ASTVI]-[GAS]-**C** motif at the signal-peptide/mature-protein junction — as it emerges laterally from the translocon; (2) binding and activation of the PG donor; and (3) transfer of the diacylglyceryl moiety to the cysteine sulfhydryl to form a **thioether bond** (PMID 28698362; PMID 26729647). The P. putida representative Q88CN8/PP_5142 is a canonical member of this reviewed family.

### 2.2 What should be treated separately (common confusions)

- **LspA (signal peptidase II)** cleaves the signal peptide *after* Lgt acts, unmasking the α-amino group of the now N-terminal S-diacylglyceryl-cysteine. This is a peptidase reaction, mechanistically and structurally unrelated to Lgt (PMID 28506828; PMID 31036406).
- **N-acylation (Lnt or non-orthologous equivalents)** adds the **third** acyl chain to the α-amino group, generating **triacylated** lipoproteins. Gram-negatives use **Lnt**; several Gram-positives that lack an E. coli-type Lnt achieve tri-acylation by other enzymes (e.g., Actinobacterial **Ppm2**), so di- versus tri-acylation and the identity of the acyltransferase are all **downstream of, and separable from, Lgt** (PMID 28698362; PMID 24780125; PMID 21205202; PMID 23029442).
- **The Lol pathway (LolCDE/LolA/LolB)** and the **"+2 rule"** govern *trafficking/sorting* of already-mature lipoproteins to the outer membrane; these are localization events, not modification chemistry, and act well downstream of Lgt (PMID 24780125).
- **TLR2 immune recognition** of di-/tri-acylated lipopeptides is a *host* consequence of the modification, not part of the enzymatic system (PMID 32849426; PMID 31226163).
- **Archaeal "lipoprotein" lipidation** is a convergent but molecularly distinct process with no Lgt homolog (PMID 39372745).

### 2.3 Competing definitions

There is little dispute over the reaction chemistry. Two definitional tensions exist: (a) whether Lgt is a true **polytopic seven-transmembrane** protein or a **seven-helix bundle peripherally embedded in the inner leaflet** — a point raised by solubilization/behavioral evidence (PMID 31256204) that qualifies the "integral membrane" label of the crystallographic model (PMID 26729647); and (b) the loose colloquial use of "lipoprotein maturation" to mean the whole Lgt→LspA→Lnt cascade, versus the strict UniPathway UPA00664 module, which records only the Lgt transfer step.

---

## 3. Mechanistic overview

**Best current model (ordered, membrane-embedded catalysis):**

1. **Substrate presentation.** A preprolipoprotein is exported through the cytoplasmic membrane, predominantly via **Sec** (occasionally **Tat**). As it exits the translocon, its hydrophobic signal peptide with the C-terminal lipobox remains membrane-associated and is recognized by Lgt (PMID 32490790; PMID 24780125).

2. **Donor loading.** Lgt binds **phosphatidylglycerol** in a dedicated site. Structures of E. coli Lgt captured PG and, separately, the inhibitor **palmitic acid**, defining **two binding sites** (a PG/donor site and a lipid/acyl site) (PMID 26729647). A companion mechanistic study describes how the **PG headgroup is activated** for transfer (PMID 31340643).

3. **Diacylglyceryl transfer.** The **thiol of the invariant lipobox cysteine** attacks the sn-1/sn-2 diacylglyceryl unit of PG, forming a **thioether-linked S-diacylglyceryl-cysteine** and releasing sn-glycerol-1-phosphate. **Arg143 and Arg239 are essential** for this transfer (likely stabilizing the phosphate/transition state and orienting substrates) (PMID 26729647).

4. **Product release.** The lipid-modified lipobox peptide **exits laterally** into the bilayer, consistent with a laterally open active site rather than an aqueous channel (PMID 26729647). The S-diacylglyceryl-prolipoprotein is then handed to LspA.

**Obligatory vs conditional vs accessory steps.**
- *Obligatory:* PG binding, cysteine thioether formation. Without Lgt action, LspA cannot cleave — establishing a **strict upstream dependency** (PMID 24780125).
- *Conditional/lineage-specific:* subsequent **N-acylation by Lnt** (present in diderms and some monoderms, historically thought absent in many Firmicutes but now known to occur via alternative enzymes in some Gram-positives).
- *Accessory:* Sec vs Tat choice for export; downstream Lol sorting and the +2 / +3,+4 retention rules (PMID 17350956).

---

## 4. Major molecular players and active assemblies

| Player | Role in the Lgt step | Evidence |
|---|---|---|
| **Lgt** (PP_5142/Q88CN8 in P. putida) | Catalyzes diacylglyceryl transfer; ~7-helix inner-membrane enzyme; conserved catalytic core plus variable "arm" and "head" domains | PMID 26729647; PMID 42126242 |
| **Phosphatidylglycerol (PG)** | Diacylglyceryl **donor**; anionic membrane phospholipid | PMID 26729647; PMID 31340643 |
| **Prolipoprotein + lipobox Cys** | Acceptor substrate; [LVI][ASTVI][GAS]**C** motif | PMID 28698362; PMID 28506828 |
| **Arg143, Arg239** (E. coli numbering) | Essential catalytic/positioning residues | PMID 26729647 |
| **Sec (and Tat) translocon** | Delivers preprolipoprotein to the membrane for Lgt | PMID 32490790; PMID 24780125 |

Lgt is generally described as a **monomeric** enzyme; chromatographic behavior as an active monomer has been reported, alongside the debate on the strength of its membrane association (PMID 31256204). No stable multi-subunit "maturation complex" is required for the Lgt step itself; the three enzymes act **sequentially** rather than as a fixed holoenzyme (PMID 28698362).

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across lineages
- **Universality and origin.** Lgt is found in **all bacteria** and **absent from archaea** (PMID 42126242; PMID 39372745). The catalytic core is deeply conserved; the peripheral **"arm" and "head" domains vary** and appear to underlie functional diversity among pathogens (PMID 42126242) — these variable modules are the plausible "later elaborations," while the PG-binding catalytic core represents the **ancestral, best-representative** unit.
- **Diderms vs monoderms and alternative N-acylation routes.** Both use Lgt then LspA. **Lnt-mediated tri-acylation** is characteristic of diderms, but the downstream N-acylation machinery is strikingly **non-orthologous** across lineages while the Lgt step stays invariant: low-GC Firmicutes such as *S. aureus* **lack an E. coli-type Lnt yet still make triacylated lipoproteins** (e.g., α-N-acylated SitC), implying a distinct acyltransferase (PMID 21205202); and Actinobacteria (*Corynebacterium/Mycobacterium*) N-acylate via **Ppm2** in the *ppm* operon (PMID 23029442). This is a clear case of the same outcome reached by different molecular means — and underscores that only the **Lgt diacylglyceryl transfer** is universal and mechanistically fixed (PMID 24780125; PMID 19805005).
- **Sorting downstream diverges.** E. coli uses the **"+2 rule"** (Asp at +2 → inner-membrane retention), whereas **P. aeruginosa follows a "+3,+4 rule"** (PMID 17350956), and **Borrelia** lipoproteins default to surface display (PMID 16468989). These are downstream of Lgt but illustrate lineage plasticity of the broader system.

### 5.2 Physiological states and consequences
- In **Proteobacteria**, Lgt is required for outer-membrane integrity; its loss permeabilizes the OM and sensitizes to serum/antibiotics (PMID 33875545; PMID 35938851).
- In **Gram-positive pathogens**, Lgt output (lipoproteins) shapes **host innate immunity via TLR2**, with double-edged effects on virulence and inflammation (PMID 31226163; PMID 19805005; PMID 32849426).
- **Archaea** solve the analogous problem with a **distinct, non-Lgt machinery** dictated by isoprenoid ether lipids (PMID 39372745).

---

## 6. Constraints, dependencies, and failure modes

- **Ordering constraint (hard).** Lgt must act **before** LspA; LspA needs the S-diacylglyceryl substrate. Thus Lgt is a rate/route-defining gate (PMID 24780125).
- **Compartment constraint.** Reaction occurs at the **cytoplasmic (inner) membrane**, using membrane PG and a membrane-tethered substrate; substrate/product enter and leave **laterally** (PMID 26729647).
- **Substrate specificity.** An **invariant cysteine** in a recognizable lipobox is required; the sulfhydryl is the sole nucleophile — no cysteine, no thioether, no downstream maturation (PMID 28698362; PMID 28506828).
- **Failure modes.** Loss/inhibition of Lgt → accumulation of unmodified prolipoproteins, OM permeabilization, morphological defects and death in Proteobacteria (independent of Lpp) (PMID 35938851); attenuated virulence and altered TLR2 signaling in Gram-positives (PMID 31226163).
- **What is ruled out.** LspA-first or Lnt-first routes are excluded by the substrate requirements of those enzymes; a purely cytoplasmic/aqueous reaction is excluded by the membrane-lateral structural model and PG dependence (PMID 26729647; PMID 24780125).

---

## 7. Controversies and open questions

1. **Membrane topology.** Is Lgt a genuine 7-TM integral protein (crystallographic view, PMID 26729647) or a 7-helix bundle **peripherally embedded** in the inner leaflet (solubilization/behavioral and MODA evidence, PMID 31256204)? This bears directly on inhibitor design.
2. **Precise chemistry of PG activation** and the exact catalytic roles of Arg143/Arg239 (electrostatic transition-state stabilization vs substrate positioning) remain to be fully resolved at transition-state resolution (PMID 31340643; PMID 26729647).
3. **Essentiality determinants.** Why is Lgt essential in Proteobacteria but dispensable in several monoderms (PMID 32490790; PMID 31226163)? Is essentiality strictly tied to OM lipoprotein cargo (e.g., Lol substrates), or to specific critical lipoproteins?
4. **Cross-organism extrapolation.** Much mechanistic detail comes from **E. coli**; functional divergence via the variable arm/head domains cautions against assuming identical behavior in, e.g., P. putida, mycobacteria, or Firmicutes (PMID 42126242).
5. **Druggability & selectivity.** Tool inhibitors exist (e.g., G2824, palmitic acid as a co-crystallized ligand), and Lgt inhibition is insensitive to Lpp-deletion resistance (PMID 33875545), but selective, whole-cell-active leads and their resistance liabilities are still open (PMID 31036406).

---

## 8. Key references

- Legood, Oliveira Paiva, Taib, et al. *Arm and head domain in highly conserved lipoprotein modification enzyme Lgt determine functional diversity among bacterial pathogens.* 2026. **PMID 42126242** — Lgt universal in bacteria, absent in archaea; conserved core + variable domains.
- Mao, Zhao, Kang, et al. *Crystal structure of E. coli lipoprotein diacylglyceryl transferase.* Nat Commun 2016. **PMID 26729647** — structures with PG and palmitic acid; Arg143/Arg239; lateral access.
- Singh, Bilal, McClory, et al. *Mechanism of Phosphatidylglycerol Activation Catalyzed by Prolipoprotein Diacylglyceryl Transferase.* 2019. **PMID 31340643** — PG activation mechanism.
- Noland, Kattke, Diao, et al. *Structural insights into lipoprotein N-acylation by Lnt.* PNAS 2017. **PMID 28698362** — pathway ordering; lipobox recognition; Lgt→LspA→Lnt.
- Zückert. *Secretion of bacterial lipoproteins…* 2014. **PMID 24780125** — pathway ordering, monoderm vs diderm, Lol/+2 rule.
- Legood, Seng, Boneca, Buddelmeijer. *A Defect in Lipoprotein Modification by Lgt Leads to… Cell Death in E. coli… Independent of Lpp.* 2022. **PMID 35938851** — essentiality/failure mode in Proteobacteria.
- Dautin, Argentini, Mohiman, et al. *Role of the unique, non-essential Lgt in Corynebacterium.* 2020. **PMID 32490790** — non-essentiality in a monoderm.
- Diao, Komura, Sano, et al. *Inhibition of E. coli Lgt Is Insensitive to Resistance Caused by Deletion of Braun's Lipoprotein.* 2021. **PMID 33875545** — first Lgt inhibitor (G2824); OM permeabilization.
- Sangith, Kumar, Sankaran. *Evidence to Suggest Lgt is a Weakly Associated Inner Membrane Protein.* 2019. **PMID 31256204** — topology controversy.
- El Arnaout & Soulimane. *Targeting Lipoprotein Biogenesis: Considerations towards Antimicrobials.* 2019. **PMID 31036406** — druggability of Lgt/LspA/Lnt.
- Hong, Makarova, Xu, et al. *…first biogenesis machinery of archaeal lipoproteins.* 2024. **PMID 39372745** — archaeal absence of Lgt; distinct route.
- Narita & Tokuda. *Amino acids at positions 3 and 4 determine membrane specificity of P. aeruginosa lipoproteins.* 2007. **PMID 17350956** — "+3,+4 rule."
- Mohammad, Nguyen, et al. *YIN and YANG of lipoproteins… S. aureus.* 2019. **PMID 31226163**; Schmaler et al. 2010. **PMID 19805005** — Gram-positive lgt dispensability, TLR2 biology.
- Asanuma, Kurokawa, et al. *Structural evidence of α-aminoacylated lipoproteins of Staphylococcus aureus.* 2011. **PMID 21205202** — Lnt-independent tri-acylation in a Firmicute.
- Mohiman, Argentini, et al. *The ppm operon is essential for acylation and glycosylation of lipoproteins in Corynebacterium glutamicum.* 2012. **PMID 23029442** — Ppm2 as an alternative N-acyltransferase in Actinobacteria.
- Sangith & Sankaran. *Stringency of LspA in recognition of signal peptides.* 2017. **PMID 28506828** — lipobox definition, LspA boundary.

---

*Uncertainty note:* Most atomic-resolution mechanism derives from E. coli Lgt; extrapolation to P. putida (Q88CN8) and to Gram-positive/actinobacterial homologs is inferred from strong sequence/structure conservation of the catalytic core but is qualified by documented divergence in peripheral domains and in downstream steps (di- vs tri-acylation; sorting rules). Direct experimental characterization of *P. putida* KT2440 Lgt (PP_5142) is sparse in the primary literature; as a diderm Gammaproteobacterium closely related to *P. aeruginosa* and *E. coli*, it is expected to require Lgt for outer-membrane lipoprotein biogenesis and to follow the "+3,+4" *Pseudomonas* sorting logic downstream (PMID 17350956), but this remains an inference rather than a direct measurement.


## Artifacts

- [OpenScientist final report](prolipoprotein_diacylglyceryl_transfer-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](prolipoprotein_diacylglyceryl_transfer-deep-research-openscientist_artifacts/final_report.pdf)