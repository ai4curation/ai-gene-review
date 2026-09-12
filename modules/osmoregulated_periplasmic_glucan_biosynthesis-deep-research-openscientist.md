---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T15:21:31.878228'
end_time: '2026-07-11T15:32:11.845659'
duration_seconds: 639.97
template_file: templates/module_research.md.j2
template_variables:
  module_title: Osmoregulated periplasmic glucan biosynthesis
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00637 module for biosynthesis
    of osmoregulated periplasmic glucans by the OpgH inner-membrane glucosyltransferase
    and the OpgG periplasmic glucan biosynthesis protein.
  module_outline: "- Osmoregulated periplasmic glucan biosynthesis\n  - 1. Inner-membrane\
    \ OPG glucosyltransferase\n  - OpgH glucosyltransferase step\n    - opgH: OPG\
    \ glucosyltransferase (molecular player: PSEPK opgH; activity or role: glucosyltransferase\
    \ activity)\n  - 2. Periplasmic OPG biosynthesis protein\n  - OpgG periplasmic\
    \ glucan biosynthesis step\n    - opgG: periplasmic OPG biosynthesis factor (molecular\
    \ player: PSEPK opgG; activity or role: carbohydrate binding)"
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
  path: osmoregulated_periplasmic_glucan_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: osmoregulated_periplasmic_glucan_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Osmoregulated periplasmic glucan biosynthesis

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00637 module for biosynthesis of osmoregulated periplasmic glucans by the OpgH inner-membrane glucosyltransferase and the OpgG periplasmic glucan biosynthesis protein.

## Provisional Biological Outline

- Osmoregulated periplasmic glucan biosynthesis
  - 1. Inner-membrane OPG glucosyltransferase
  - OpgH glucosyltransferase step
    - opgH: OPG glucosyltransferase (molecular player: PSEPK opgH; activity or role: glucosyltransferase activity)
  - 2. Periplasmic OPG biosynthesis protein
  - OpgG periplasmic glucan biosynthesis step
    - opgG: periplasmic OPG biosynthesis factor (molecular player: PSEPK opgG; activity or role: carbohydrate binding)

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

# Osmoregulated Periplasmic Glucan Biosynthesis (UPA00637): OpgH and OpgG

*A review-style synthesis anchored on the* Pseudomonas putida *KT2440 OpgH/OpgG module, set in its broader proteobacterial context.*

---

## 1. Executive summary

Osmoregulated periplasmic glucans (OPGs; historically "membrane-derived oligosaccharides," MDOs, in *Escherichia coli*) are a family of β-glucose polymers that accumulate to high concentration in the periplasm of Gram-negative bacteria when the surrounding medium is dilute (low osmolarity). The UniPathway module **UPA00637** captures the conserved, minimal core of their biosynthesis: an inner-membrane glucosyltransferase, **OpgH**, that polymerizes a β-glucan backbone from UDP-glucose on the cytoplasmic face of the inner membrane, and a periplasmic partner protein, **OpgG**, that is strictly required for producing mature backbone. In *P. putida* KT2440 these are encoded by *opgH* (PSEPK OpgH) and *opgG* (PSEPK OpgG), the orthologues of the *E. coli mdoGH*/*opgGH* bicistronic operon.

The system is best understood as a **two-protein glucan factory** that is gated by osmolarity and fed by central carbon metabolism. Its output is not a fixed molecule but a tunable one: the backbone is β-1,2-linked with β-1,6 branches (in *E. coli* and pseudomonads), and it is decorated post-synthetically by accessory enzymes (succinyl, phosphoglycerol, O-acetyl groups) that are **not** part of UPA00637 proper. OpgH additionally "moonlights" as a nutrient-dependent inhibitor of cell division by sequestering FtsZ — a role mechanistically separate from glucan synthesis and unique to OpgH within this module. Loss of OPGs produces a strikingly pleiotropic envelope phenotype (motility loss, exopolysaccharide overproduction, biofilm and virulence defects), much of it transduced through the Rcs envelope-stress phosphorelay.

The strongest, best-replicated claims are: (i) *opgG* and *opgH* are individually essential for backbone synthesis; (ii) the donor is UDP-glucose and the process is osmoregulated; and (iii) OpgH sequesters FtsZ. The most important open questions concern the precise biochemical division of labor between OpgH and OpgG, whether *P. putida* makes linear or cyclic glucans, and how much of the phenotypic pleiotropy is a direct glucan effect versus an indirect signaling consequence.

---

## 2. Definition and biological boundaries

### 2.1 What is included

UPA00637 as scoped here comprises exactly two obligatory steps:

1. **Inner-membrane OPG glucosyltransferase step — OpgH.** A large polytopic cytoplasmic-membrane protein (~97 kDa in *E. coli* MdoH) carrying glucosyltransferase activity; it transfers glucosyl units from UDP-glucose to build the β-glucan backbone.
2. **Periplasmic OPG biosynthesis step — OpgG.** A ~56 kDa periplasmic protein (carbohydrate-binding role) that is obligatorily required for backbone production, presumably acting on the nascent/translocated glucan on the periplasmic side.

Together they generate the **unsubstituted glucose backbone** of OPGs. This is the appropriate boundary of the "biosynthesis of OPG backbone" pathway.

### 2.2 What is adjacent and should be treated separately

- **Backbone modification enzymes (OpgB, OpgC, OpgD).** These add or edit substituents or influence chain length but are not backbone-synthesizing: *opgB* (sn-1-phosphoglycerol transferase), *opgC* (succinyl/O-acyl transferase), and *opgD* (an OpgG paralog affecting chain length). In *Shigella flexneri* the *opg* family is *opgGH* (bicistronic) plus *opgB*, *opgC*, and *opgD* [PMID 20062978]; in *Rhodobacter sphaeroides* the operon is *opgGIH* with a downstream *opgC* controlling succinylation [PMID 12027885]. These modifications determine anionic charge and are physiologically important but mechanistically downstream of UPA00637.
- **Alternative, non-homologous OPG routes (Ndv/Chv and Cgs systems).** The Rhizobiaceae synthesize **cyclic β-(1,2)-glucans** via a single very large (~319 kDa) inner-membrane protein (NdvB/ChvB) that forms a protein-linked oligosaccharide intermediate [PMID 8830704]. In *Brucella*, the equivalent cyclic-β-1,2-glucan is made by a dedicated inner-membrane **synthase/transporter/modifier complex (Cgs/Cgt/Cgm)** that physically assembles (homo- and heterotypic interactions, polar localization) to couple synthesis, periplasmic transport, and succinylation [PMID 25733613]. Both achieve a similar biological outcome (periplasmic osmoprotectant/virulence glucan) by a completely different molecular means and are **not** homologous to OpgGH. They should not be conflated with the Opg pathway.
- **"Orphan" cyclic-β-glucan synthases in pseudomonads.** A recently described BcsA-like GT2/GH17 fusion protein present in *P. aeruginosa*, *P. fluorescens*, *P. putida* KT2440, and *P. syringae* is predicted to make **cyclic β-(1,3)-glucan**, a distinct polysaccharide from OpgGH-dependent OPGs [PMID 37267309]. Its existence means "periplasmic glucan" in *P. putida* is not synonymous with the OpgGH product; care is needed to avoid attributing cyclic-β-glucan chemistry to the OpgGH module.
- **NdvB-mediated biofilm antibiotic resistance.** In *P. aeruginosa*, *ndvB* (PA1163) contributes to biofilm antibiotic tolerance but is explicitly **not** responsible for the OpgGH-dependent OPG described at the *opgGH* locus [PMID 17906125]. A frequent source of confusion.
- **Downstream regulatory consequences.** Colanic-acid capsule synthesis, Rcs phosphorelay activation, and motility are affected *by* OPG status but are separate systems [PMID 9352941].

### 2.3 Competing definitions

"OPG," "MDO," "periplasmic glucan," and "cyclic glucan" are used loosely in the older literature. Bohin's classification organizes OPGs into **four families based on backbone linkage/branching** [PMID 10779706]; the OpgGH-dependent family (β-1,2 backbone with β-1,6 branches) is Family I / the enterobacterial-pseudomonad type. Terminological drift — especially calling all periplasmic glucans "MDO" or lumping Ndv/Chv cyclic glucans with OpgGH glucans — remains a real hazard.

---

## 3. Mechanistic overview

### 3.1 Best current model of the sequence of events

1. **Substrate supply (accessory/upstream).** UDP-glucose is generated by central metabolism (e.g., *galU*/*galF*). It is the glucosyl donor for OPG synthesis [PMID 26150539].
2. **Backbone polymerization at the inner membrane (obligatory — OpgH).** OpgH, a polytopic inner-membrane glucosyltransferase, uses UDP-glucose to build the β-glucan backbone. Genetic and biochemical evidence in *E. coli* shows OpgH/MdoH is required for glucosyltransferase activity [PMID 7934824], and the reaction uses **acyl carrier protein (ACP) as a cofactor** [PMID 26150539]. Polymerization is thought to occur on the cytoplasmic face with concomitant/subsequent translocation of the growing glucan to the periplasm.
3. **Periplasmic maturation (obligatory — OpgG).** OpgG, a periplasmic β-sandwich/carbohydrate-binding protein, is strictly required for producing the mature backbone; loss of OpgG abolishes glucan even when OpgH is intact [PMID 11325942]. Its precise catalytic/chaperone role (chain-length control, branching, or scaffolding of OpgH) is not fully resolved.
4. **Substitution/editing (conditional/accessory).** OpgB (phosphoglycerol), OpgC (succinyl/O-acetyl), and OpgD (chain length) act on the periplasmic backbone, tuning charge and size [PMID 20062978; PMID 12027885]. These are species-dependent and dispensable for making glucose backbone.

### 3.2 Obligatory vs conditional vs accessory

- **Obligatory:** OpgH (backbone glucosyltransferase) and OpgG (periplasmic maturation). Either knockout abolishes OPGs [PMID 11325942; PMID 19118363; PMID 20062978].
- **Conditional:** osmoregulatory input (transcriptional repression at high osmolarity plus enzyme-level control) [PMID 17906125; PMID 10779706] — synthesis is strongly favored at low osmolarity but the genes are present regardless.
- **Accessory:** substitution enzymes (OpgB/C), chain-length modulator (OpgD), UDP-glucose supply, and the **OpgH–FtsZ moonlighting activity** (affects cell size, not glucan chemistry) [PMID 23935518].

### 3.3 Regulatory logic

Osmoregulation is dual-level: high osmolarity represses *opgGH* transcription and also dampens enzyme activity; low osmolarity derepresses and activates, matching glucan output to periplasmic osmotic demand, with feedback control preventing overaccumulation [PMID 10779706]. Periplasmic OPG levels are, in turn, read out by the **Rcs (RcsC/RcsB/RcsA) phosphorelay**, which controls colanic-acid capsule and other envelope genes [PMID 9352941].

---

## 4. Major molecular players and active assemblies

| Player | Location | Role | Status in UPA00637 | Key evidence |
|---|---|---|---|---|
| **OpgH** (MdoH; HrpM in *P. syringae*) | Inner membrane, polytopic (~97 kDa) | Glucosyltransferase; builds β-glucan backbone from UDP-glucose; moonlights as FtsZ-sequestering cell-size regulator | **Core, obligatory** | PMID 7934824; 26150539; 23935518 |
| **OpgG** (MdoG) | Periplasm (~56 kDa) | Carbohydrate-binding; required for mature backbone (chain length/branching/scaffolding) | **Core, obligatory** | PMID 7934824; 11325942 |
| OpgI | (in some α-proteobacteria, e.g. *R. sphaeroides* *opgGIH*) | Additional backbone-synthesis factor | Accessory/lineage-specific | PMID 12027885 |
| OpgD | Periplasm, OpgG paralog | Chain-length control | Accessory | PMID 20062978 |
| OpgB | Membrane | sn-1-phosphoglycerol transferase (substitution) | Accessory | PMID 20062978 |
| OpgC | Membrane | Succinyl/O-acyl transferase (anionic substitution) | Accessory | PMID 12027885; 20062978 |
| UDP-glucose (GalU/GalF) | Cytoplasm | Glucosyl donor | Substrate (upstream) | PMID 26150539 |
| ACP | Cytoplasm | Cofactor for the glucosyltransferase reaction | Cofactor | PMID 26150539 |

**Active assembly.** The functional unit is an OpgH–OpgG couple spanning the inner membrane and periplasm: OpgH polymerizes and (likely) translocates, OpgG completes maturation in the periplasm. There is no strong evidence that they form an obligate stable heterocomplex vs. a functional/kinetic coupling; this remains an open structural question. Note that OpgH's cell-division role involves a *distinct* interaction with **FtsZ** at the septum [PMID 23935518], a second "assembly" entirely separate from the glucan machinery.

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across lineages

- **OPGs (or functional equivalents) are near-universal in Proteobacteria.** OPGs occur in almost all **α-, β- and γ-Proteobacteria**, and where classical OPGs are absent (**ε-Proteobacteria**) OPG-like oligosaccharides take their place [PMID 26265506] — underscoring a pervasive, conserved requirement for a periplasmic glucan in the Gram-negative envelope.
- **OpgGH is the deepest, most widely distributed OPG-synthesis solution in Proteobacteria** — the *opgG*/*opgH* pair is the most broadly conserved OPG-biosynthetic gene set in proteobacterial genomes [PMID 17906125]. The best representatives for understanding the ancestral OpgGH role are the well-characterized enterobacterial (E. coli MdoGH) and pseudomonad (*P. aeruginosa* OpgGH; *P. syringae* HrpM) systems, which retain the minimal bicistronic architecture. *P. putida* KT2440 OpgH/OpgG belong to this conserved core.
- **Structural backbone families vary** [PMID 10779706]: enterobacteria/pseudomonads make β-1,2 backbones with β-1,6 branches; *P. aeruginosa* OPGs are **linear** β-1,2 glucans with a few β-1,6 branches and succinyl substituents [PMID 17906125]; *R. sphaeroides* makes **cyclic anionic** OPGs [PMID 12027885]. Thus even within the OpgGH family, linear vs cyclic and neutral vs anionic outcomes differ by lineage.
- **Convergent, non-homologous alternatives exist:** Rhizobiaceae use NdvB/ChvB (~319 kDa, protein-linked intermediate) to make cyclic β-1,2-glucans [PMID 8830704]; *Brucella* uses a Cgs/Cgt/Cgm inner-membrane complex for the same class of molecule [PMID 25733613]; and some pseudomonads additionally carry an orphan GT2/GH17 synthase predicted to make cyclic β-1,3-glucan [PMID 37267309]. These are alternative routes to a periplasmic osmoprotectant glucan.

### 5.2 Physiological-state and cell-cycle variation

- **Osmotic state** is the dominant variable: OPGs accumulate at low osmolarity and are downregulated at high osmolarity [PMID 17906125; PMID 10779706].
- **Nutrient/growth-rate state** is coupled to OpgH's cell-size function: under nutrient-rich, fast growth, OpgH (sensing UDP-glucose) localizes to the septum and delays division, yielding larger cells [PMID 23935518].
- **Lineage-specific loss.** *Yersinia pestis* lost the *opgGH* operon during its emergence from *Y. pseudotuberculosis*; the loss correlates with reduced cell size, and restoring *opgGH* restores the larger size — a natural experiment showing the operon is dispensable in an obligate mammal/flea lifestyle [PMID 26150539]. Intriguingly, *Y. pseudotuberculosis* retains the operon but does **not** detectably make OPGs under tested conditions, showing that gene presence ≠ glucan production.

### 5.3 A note on the convergent cell-size module

OpgH is functionally analogous to *Bacillus subtilis* **UgtP**, a glucosyltransferase that also inhibits FtsZ in a growth-rate–dependent manner — yet OpgH and UgtP share **no homology and different enzymatic activities**, a textbook case of convergent evolution using UDP-glucose as a shared nutrient proxy [PMID 23935518]. This cell-size role is a **later elaboration** layered onto the ancestral glucan-synthesis function of OpgH and is absent from OpgG.

---

## 6. Constraints, dependencies, and failure modes

- **Compartment/order constraints.** Backbone polymerization must precede periplasmic maturation and any substitution; substitutions (OpgB/C) act on periplasmic glucan and therefore cannot occur before OpgH-dependent synthesis and translocation. UDP-glucose must be available in the cytoplasm before OpgH can act [PMID 26150539].
- **Non-redundancy.** OpgG and OpgH cannot substitute for one another: both are required, ruling out models in which OpgH alone suffices to make mature glucan [PMID 11325942; PMID 20062978].
- **Osmotic gating.** High osmolarity is a physiological "off" state; OPG synthesis at high osmolarity is minimized by combined transcriptional and enzymatic repression [PMID 10779706].
- **Failure modes (opg-null phenotype).** Loss of OPGs causes a highly pleiotropic envelope disturbance: EPS overproduction, reduced motility, bile-salt hypersensitivity, reduced secreted enzymes, and virulence loss in phytopathogens [PMID 11325942]; low-osmolarity growth/motility defects and ~100-fold virulence attenuation in *Salmonella* [PMID 19118363]; altered biofilm architecture in *P. aeruginosa* [PMID 17906125]. Much of this is transduced by Rcs, which senses periplasmic glucan status [PMID 9352941]. Importantly, the *specific* role differs by species: OPGs act as periplasmic signaling molecules that indirectly regulate virulence genes, but when secreted they can directly sequester antibiotics or engage host cells during invasion [PMID 26265506] — so "the OPG phenotype" is context-dependent rather than a single universal function.
- **Evidence ruling out alternatives.** The *opgGH* locus, not *ndvB*, is responsible for OpgGH-type OPGs in *P. aeruginosa* [PMID 17906125]; and OpgH's FtsZ role is separable from glucan output (Yersinia data), so the two OpgH functions must be considered independently [PMID 26150539; PMID 23935518].

---

## 7. Controversies and open questions

1. **Division of labor between OpgH and OpgG.** OpgH clearly carries glucosyltransferase activity, but OpgG's exact biochemical role — chain-length determination, branching, scaffolding/chaperoning of OpgH, or a hydrolase/transglycosylase activity — remains unresolved. It is "required," but the mechanism of that requirement is inferred, not proven [PMID 7934824; PMID 11325942].
2. **Linear vs cyclic product in *P. putida*.** *P. aeruginosa* OpgGH makes linear glucans [PMID 17906125], but pseudomonads also harbor an orphan synthase predicted to make cyclic β-1,3-glucan [PMID 37267309]. The exact structure of the *P. putida* KT2440 OpgGH product and how it partitions from any orphan-synthase product has not, to our knowledge, been directly determined — a genuine gap for the scoped organism.
3. **How direct is the pleiotropy?** Because Rcs reads periplasmic glucan status [PMID 9352941], many opg-null phenotypes may be indirect signaling consequences rather than direct structural effects of missing glucan. Disentangling direct vs signaling effects is unresolved.
4. **Gene presence vs glucan production.** *Y. pseudotuberculosis* keeps *opgGH* but makes no detectable OPGs under tested conditions [PMID 26150539], implying additional, uncharacterized activation requirements (substrate flux, cofactor, or unknown regulator). This warns against inferring glucan production from genome annotation alone — directly relevant to a genome-annotation-driven module like *P. putida* UPA00637.
5. **Cross-organism extrapolation.** Much mechanistic detail comes from *E. coli*, with structural/product detail from *P. aeruginosa*, *R. sphaeroides*, and enteric pathogens. Extending these to *P. putida* is reasonable given OpgGH conservation but should be flagged as inference, not measurement, for KT2440 specifically.

---

## 8. Key references

- Bohin JP. **Osmoregulated periplasmic glucans in Proteobacteria.** *FEMS Microbiol Lett* 2000. PMID **10779706**. — Foundational review; OPG families, osmoregulation, feedback, pleiotropy.
- Loubens I, et al. **Homology between mdoA (E. coli periplasmic glucan) and hrpM (P. syringae pathogenicity).** *Mol Microbiol* 1993. PMID **7934824**. — mdoGH operon; MdoG (56 kDa periplasmic) and MdoH (97 kDa membrane glucosyltransferase); pseudomonad link.
- Lequette Y, et al. **Linear OPGs encoded by opgGH of Pseudomonas aeruginosa.** *J Bacteriol* 2007. PMID **17906125**. — Pseudomonad OpgGH product structure, osmoregulation, biofilm; ndvB distinction.
- Hill NS, et al. **A moonlighting enzyme links E. coli cell size with central metabolism.** *Curr Biol* 2013. PMID **23935518**. — OpgH sequesters FtsZ; UDP-glucose nutrient proxy; convergence with UgtP.
- Quintard K, et al. **Role of the opgGH operon in Yersinia pseudotuberculosis and its deletion in Y. pestis.** *J Bacteriol* 2015. PMID **26150539**. — UDP-glucose/ACP cofactor; FtsZ/cell-size; lineage-specific loss; gene-presence ≠ product.
- Page F, et al. **OPG synthesis required for Erwinia chrysanthemi pathogenicity.** *J Bacteriol* 2001. PMID **11325942**. — opgGH essentiality; pleiotropic mutant phenotype; virulence loss.
- Bhagwat AA, et al. **OPGs of Salmonella Typhimurium required for optimal virulence in mice.** *Microbiology* 2009. PMID **19118363**. — Bicistronic opgGH; low-osmolarity growth/motility; virulence attenuation.
- Liu J, et al. **OPG synthesis gene family of Shigella flexneri.** *Arch Microbiol* 2010. PMID **20062978**. — opgGH + opgB/opgC/opgD family organization; backbone structure.
- Cogez V, et al. **opgGIH and opgC of Rhodobacter sphaeroides.** *J Bacteriol* 2002. PMID **12027885**. — Operon variation (opgGIH), succinylation, cyclic anionic OPGs.
- Ebel W, et al. **Inactivation of mdoH increases colanic acid via Rcs.** *J Bacteriol* 1997. PMID **9352941**. — Periplasmic glucan status signals through RcsC.
- Bontemps-Gallo S, Lacroix JM. **New insights into the biological role of the osmoregulated periplasmic glucans in pathogenic and symbiotic bacteria.** *Environ Microbiol Rep* 2015. PMID **26265506**. — Authoritative review; distribution across α/β/γ-Proteobacteria, OPG-like glucans in ε-Proteobacteria, four species-specific biological roles.
- Castro OA, et al. **Cyclic β-(1,2)-glucan synthesis in Rhizobiaceae: 319-kDa intermediate.** *J Bacteriol* 1996. PMID **8830704**. — Non-homologous NdvB/ChvB alternative route.
- Guidolin LS, et al. **Interaction network and localization of Brucella abortus membrane proteins for cyclic β-1,2-glucan synthesis, transport, and succinylation.** *J Bacteriol* 2015. PMID **25733613**. — Cgs/Cgt/Cgm inner-membrane complex; alternative periplasmic-glucan machine distinct from OpgGH.
- Spiers AJ, et al. **BcsA-like orphan proteins: a novel pseudomonad cyclic-β-glucan synthase family.** *BMC Microbiol/BMC* 2023. PMID **37267309**. — Predicted cyclic β-1,3-glucan synthase in P. putida KT2440 and other pseudomonads.

---

### Uncertainty statement

Claims about OpgH backbone glucosyltransferase activity, UDP-glucose donor usage, osmoregulation, the opg-null pleiotropic phenotype, and OpgH–FtsZ sequestration are **strongly supported** by multiple organisms and direct experiments. The precise catalytic role of **OpgG**, the exact **structure of the *P. putida* KT2440 OpgGH product** (linear vs cyclic; substitution pattern), and the extent to which the *P. putida* module behaves as its *E. coli*/*P. aeruginosa* orthologues do are **inferences** from homology and neighboring-organism data, and should be treated as provisional for KT2440 specifically.


## Artifacts

- [OpenScientist final report](osmoregulated_periplasmic_glucan_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](osmoregulated_periplasmic_glucan_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)