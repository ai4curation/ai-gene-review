---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:47:17.802531'
end_time: '2026-09-01T03:07:37.155772'
duration_seconds: 1219.35
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial Mla intermembrane phospholipid transport
  module_summary: A species-neutral diderm-bacterial module for phospholipid exchange
    across the cell envelope through an outer-membrane MlaA/VacJ interface, a soluble
    periplasmic MlaC carrier, and an ATP-coupled inner-membrane MlaFEDB complex. The
    module represents the conserved transport architecture without forcing a universal
    retrograde or anterograde net direction.
  module_outline: "- Bacterial Mla intermembrane phospholipid transport\n  - 1. Outer-membrane\
    \ phospholipid handling\n  - MlaA/VacJ outer-membrane interface\n    - MlaA/VacJ\
    \ outer-membrane phospholipid interface (molecular player: MlaA/VacJ family; activity\
    \ or role: outer-membrane phospholipid handling activity)\n  - 2. Periplasmic\
    \ phospholipid shuttling\n  - MlaC periplasmic phospholipid shuttle\n    - MlaC-family\
    \ periplasmic phospholipid carrier (molecular player: MlaC phospholipid-carrier\
    \ family; activity or role: phospholipid binding)\n  - 3. ATP-coupled inner-membrane\
    \ phospholipid handling\n  - MlaFEDB inner-membrane complex\n    - MlaFEDB phospholipid\
    \ transport complex (molecular player: MlaFEDB ABC phospholipid transport complex;\
    \ activity or role: phospholipid transfer activity)"
  module_connections: No explicit connections.
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
citation_count: 25
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_mla_intermembrane_phospholipid_transport-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_mla_intermembrane_phospholipid_transport-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial Mla intermembrane phospholipid transport

## Working Scope

A species-neutral diderm-bacterial module for phospholipid exchange across the cell envelope through an outer-membrane MlaA/VacJ interface, a soluble periplasmic MlaC carrier, and an ATP-coupled inner-membrane MlaFEDB complex. The module represents the conserved transport architecture without forcing a universal retrograde or anterograde net direction.

## Provisional Biological Outline

- Bacterial Mla intermembrane phospholipid transport
  - 1. Outer-membrane phospholipid handling
  - MlaA/VacJ outer-membrane interface
    - MlaA/VacJ outer-membrane phospholipid interface (molecular player: MlaA/VacJ family; activity or role: outer-membrane phospholipid handling activity)
  - 2. Periplasmic phospholipid shuttling
  - MlaC periplasmic phospholipid shuttle
    - MlaC-family periplasmic phospholipid carrier (molecular player: MlaC phospholipid-carrier family; activity or role: phospholipid binding)
  - 3. ATP-coupled inner-membrane phospholipid handling
  - MlaFEDB inner-membrane complex
    - MlaFEDB phospholipid transport complex (molecular player: MlaFEDB ABC phospholipid transport complex; activity or role: phospholipid transfer activity)

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

# Bacterial Mla Intermembrane Phospholipid Transport: A Mechanistic Review

*A commissioned review-style synthesis. Citations are given as PubMed IDs (PMID).*

---

## 1. Executive Summary

The **Mla system** (Maintenance of Lipid Asymmetry) is a conserved, trans-envelope protein module found across diderm (Gram-negative-type) bacteria that moves glycerophospholipids (PLs) between the outer membrane (OM) and inner membrane (IM) across the aqueous periplasm. It is built from three physically separate assemblies that together bridge the entire cell envelope: an OM lipoprotein interface (**MlaA/VacJ**, docked onto the trimeric porins OmpC/OmpF), a small soluble periplasmic carrier (**MlaC**), and an ATP-powered IM ABC transporter (**MlaFEDB**). The system's canonical, best-supported physiological role is to preserve OM lipid asymmetry—keeping lipopolysaccharide (LPS) in the outer leaflet and PLs in the inner leaflet—by clearing PLs that mislocalize to the OM outer leaflet. This asymmetry is central to the OM's function as a permeability barrier, and hence to intrinsic antibiotic resistance and virulence.

A decade and a half of genetics, biochemistry, and (more recently) cryo-EM has converged on a coherent tripartite architecture and a plausible "point-to-point" lipid relay: MlaA extracts/receives a PL from the OM outer leaflet, hands it to MlaC, MlaC diffuses across the periplasm, and MlaFEDB captures the lipid at the IM (or vice versa). The two flanking complexes never touch; MlaC is the obligate ferry. The central mechanistic controversy is **directionality**: whether the net physiological flux is retrograde (OM→IM, an "import"/repair pathway) or anterograde (IM→OM, a biosynthetic "export" pathway). Genetic origins and recent reconstituted biochemistry favor ATP-driven retrograde transport, but the machine is architecturally direction-neutral and may run either way depending on physiological context.

This review defines the boundaries of the Mla module, lays out the current mechanistic model and the molecular players executing each step, situates Mla within the broader **MCE (Mammalian Cell Entry) superfamily** and its eukaryotic organellar relatives, and delineates what is strongly supported versus contested. We emphasize uncertainty: much mechanistic detail derives from *Escherichia coli* and a handful of pathogens, structures are largely of the IM complex, and the directionality question remains genuinely open.

---

## 2. Definition and Biological Boundaries

### What is included

The Mla system, in its species-neutral core, is exactly three functional assemblies spanning the three envelope compartments ([PMID: 39080293](https://pubmed.ncbi.nlm.nih.gov/39080293/); [PMID: 28388411](https://pubmed.ncbi.nlm.nih.gov/28388411/)):

| Compartment | Assembly | Core components | Role |
|---|---|---|---|
| Outer membrane | MlaA–OmpC/F | MlaA (VacJ) lipoprotein + trimeric porin | Handling of PLs at the OM outer leaflet |
| Periplasm | MlaC | Soluble monomeric carrier | Binds/shuttles one PL across the periplasm |
| Inner membrane | MlaFEDB | ABC transporter (MlaF₂E₂D₆B₂) | ATP-coupled PL capture/release at the IM |

The founding definition (Malinverni & Silhavy, 2009) framed Mla as an ABC transport system of "at least 6 proteins" with "at least one component in each cellular compartment," conserved widely, that "prevents PL accumulation in the outer leaflet of the OM" ([PMID: 19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/)). The canonical gene set is *mlaFEDCB* plus *mlaA*; MlaB is a small STAS-domain regulatory subunit, MlaF/MlaE/MlaD constitute the IM ABC transporter, and MlaD supplies the hexameric MCE ring. Multiple independent structural and biochemical studies converge on this three-assembly architecture: MlaD forms a ring associated with the IM ABC transporter, and MlaC ferries lipids between MlaD and the OM complex ([PMID: 28388411](https://pubmed.ncbi.nlm.nih.gov/28388411/)); a 2024 study restates the "three proteinaceous assemblies: the MlaA-OmpC complex, situated within the outer membrane; the periplasmic phospholipid shuttle protein, MlaC; and the inner membrane ABC transporter complex, MlaFEDB" ([PMID: 39080293](https://pubmed.ncbi.nlm.nih.gov/39080293/)).

### What is *not* included (frequently conflated neighbors)

Several envelope processes are adjacent to or confused with Mla but should be treated separately:

- **Enzymatic OM-asymmetry repair (PldA, PagP, periplasmic phospholipase).** These enzymes *destroy or modify* surface-mislocalized PLs in place rather than *transporting* them. A periplasmic phospholipase maintains OM lipid asymmetry in parallel with Mla ([PMID: 37463202](https://pubmed.ncbi.nlm.nih.gov/37463202/)). This is a redundant, alternative route to the same physiological outcome, not part of the transporter, and it helps explain why *mla* loss is typically sub-lethal.
- **LPS transport (Lpt pathway).** Lpt moves LPS, not PLs, from IM to OM; it is a distinct machine with a distinct substrate.
- **Other MCE paralogs (Pqi/YebT).** In *E. coli*, PqiABC and YebT (LetB) are paralogous MCE systems with completely different architectures (stacked rings / syringe channels spanning the periplasm) and are not the Mla system ([PMID: 28388411](https://pubmed.ncbi.nlm.nih.gov/28388411/)).
- **General PL biosynthesis and IM flippases.** Mla is an intermembrane trafficking module, not a *de novo* biosynthetic or IM-flipping activity.

### Competing definitions

The principal definitional tension is directional framing. The original "Mla = import/repair" formulation ([PMID: 19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/)) treats the system as retrograde. An alternative body of work reframes Mla as an anterograde **exporter** supplying PLs to the OM ([PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/)). The scope adopted here deliberately treats the module as *directionally neutral* architecture, because the conserved parts are the same regardless of net flux.

---

## 3. Mechanistic Overview

### Best current model: a three-stop lipid relay

The consensus model is a **point-to-point, non-vesicular relay** in which a single PL is passed hand-to-hand across the envelope, with the periplasmic carrier MlaC as the obligatory intermediate that keeps the OM and IM complexes from contacting each other directly:

```
   OUTER MEMBRANE
   ┌───────────────────────────────────────────┐
   │  outer leaflet: LPS  |  (mislocalized PL)  │
   │                        ▲                    │
   │        MlaA (VacJ) ────┘  docked on OmpC/F  │  ── Step 1: PL handling at OM
   └────────────┬──────────────────────────────┘
                │  PL hand-off (membrane thinning directs lipid)
                ▼
   PERIPLASM   MlaC  ◄───── carries ONE PL ─────►   ── Step 2: shuttle (mutually
                │  (single-partner binding)            exclusive MlaA vs MlaD binding)
                ▼
   ┌────────────┴──────────────────────────────┐
   │  MlaD hexameric MCE ring (periplasmic)     │
   │  ─────────── continuous channel ────────── │  ── Step 3: ATP-coupled capture/
   │  MlaE (TM permease) + MlaF (ATPase) + MlaB │      release at IM (MlaFEDB)
   INNER MEMBRANE
   └───────────────────────────────────────────┘
```

Step ordering is dictated by compartment topology: the OM step and the IM step are physically separated by the periplasm and can only be connected through MlaC. Because MlaC's MlaA-binding and MlaD-binding surfaces overlap, MlaC can engage only one partner at a time, enforcing an alternating pick-up/drop-off cycle ([PMID: 37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/)).

### Obligatory, conditional, and accessory steps

- **Obligatory:** MlaC-mediated transfer between the two membrane complexes (there is no other way to cross the periplasm within this module); the MlaD ring as the periplasmic conduit to/from MlaE.
- **Conditional/energized:** ATP hydrolysis by MlaFEDB, which disrupts a lipid-binding equilibrium to drive vectorial (retrograde) transport ([PMID: 34873038](https://pubmed.ncbi.nlm.nih.gov/34873038/)). Notably, *some* transfer steps (e.g., MlaC receiving lipid from MlaFEDB) have been reported to occur without ATP ([PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/)), indicating that not every hand-off requires the ATPase.
- **Accessory:** MlaB (STAS-domain regulatory subunit stabilizing/regulating the ABC complex); the specific porin partner (OmpC vs OmpF) at the OM.

### Molecular events per step

1. **OM handling (MlaA/VacJ).** MlaA is a donut-shaped OM lipoprotein forming a channel in association with trimeric porins; the crystal structure of MlaA–OmpF established this architecture ([PMID: 29038444](https://pubmed.ncbi.nlm.nih.gov/29038444/)). Cryo-EM of the OmpC–MlaA–MlaC assembly shows that "the OmpC-MlaA complex transfers PLs to the periplasmic chaperone MlaC," with local membrane thinning helping direct lipids into the pathway ([PMID: 38092770](https://pubmed.ncbi.nlm.nih.gov/38092770/)).
2. **Periplasmic shuttle (MlaC).** MlaC binds a single PL in a two-domain NTF2-like/PBP fold; a "pivoting β-sheet mechanism that functions to open and close the phospholipid-binding pocket" gates the lipid site ([PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/); [PMID: 36084896](https://pubmed.ncbi.nlm.nih.gov/36084896/)). MlaD spontaneously transfers PL to MlaC, implying MlaC has higher intrinsic PL affinity ([PMID: 30284446](https://pubmed.ncbi.nlm.nih.gov/30284446/)).
3. **IM handling (MlaFEDB).** The 12-subunit MlaF₂E₂D₆B₂ complex binds multiple PLs and undergoes large ATP-driven conformational changes; "a continuous transport pathway extends from the MlaE substrate-binding site, through the channel of MlaD, and into the periplasm" ([PMID: 33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/); [PMID: 32884137](https://pubmed.ncbi.nlm.nih.gov/32884137/)).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 MlaA / VacJ — the outer-membrane interface

MlaA was originally identified as **VacJ**, a virulence factor: it "was initially identified – and called VacJ – based on its role in the intracellular spreading of *Shigella flexneri*" ([PMID: 38802775](https://pubmed.ncbi.nlm.nih.gov/38802775/)), long before its lipid-transport role was appreciated. Structurally it is a donut-shaped OM lipoprotein that forms a channel in complex with trimeric porins OmpC/OmpF ([PMID: 29038444](https://pubmed.ncbi.nlm.nih.gov/29038444/)). Functionally, the OmpC–MlaA complex extracts PLs from the OM outer leaflet and transfers them to MlaC, with membrane thinning steering the lipid into the carrier ([PMID: 38092770](https://pubmed.ncbi.nlm.nih.gov/38092770/)). Importantly, MlaA is not architecturally uniform: a survey demonstrated "the existence of two MlaA classes among 21 bacterial species, characterized by the presence or lack of a lipoprotein signal peptide" ([PMID: 30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/)), the first clear evidence of lineage variation in the OM component.

### 4.2 MlaC — the periplasmic carrier

MlaC is a small, soluble, monomeric PL-binding protein and the obligate periplasmic ferry. It belongs to a **non-canonical class of substrate-binding proteins**: crystal structures reveal a two-domain organization (NTF2-like plus PL-binding-protein domains) derived from a cystatin-like fold, with a segmented mechanism of opening its binding site and capacity to accommodate PLs of varied acyl composition ([PMID: 36084896](https://pubmed.ncbi.nlm.nih.gov/36084896/)). A pivoting β-sheet gates the pocket open and closed ([PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/)). Interaction mapping by computational structure prediction and deep mutational scanning shows the MlaD- and MlaA-binding surfaces "overlap to a large extent, leading to a model in which MlaC can only bind one of these proteins at a time"—the structural basis of the alternating shuttle ([PMID: 37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/)). Directional affinity is built in: "MlaD spontaneously transfers PLs to MlaC, suggesting that the latter has a higher affinity for PLs" ([PMID: 30284446](https://pubmed.ncbi.nlm.nih.gov/30284446/)). The MlaC–MlaD complex has been solved directly, providing the molecular basis of the periplasmic-to-IM hand-off ([PMID: 39080293](https://pubmed.ncbi.nlm.nih.gov/39080293/)).

### 4.3 MlaFEDB — the inner-membrane ABC engine

MlaFEDB is a **structurally distinct ABC transporter** and has been described as the founding member of a new transporter superfamily. Its 3.05 Å cryo-EM structure with bound substrate revealed only "distant relationships to the LPS and MacAB transporters, as well as the eukaryotic ABCA/ABCG families," and "a continuous transport pathway extends from the MlaE substrate-binding site, through the channel of MlaD, and into the periplasm" ([PMID: 33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/)). Multiple independent structures established a 12-subunit stoichiometry, **MlaF₂E₂D₆B₂**, with "six well-resolved phospholipids in three distinct cavities, and large-scale conformational changes upon ATP binding" ([PMID: 32884137](https://pubmed.ncbi.nlm.nih.gov/32884137/); [PMID: 33199922](https://pubmed.ncbi.nlm.nih.gov/33199922/); [PMID: 33845086](https://pubmed.ncbi.nlm.nih.gov/33845086/)). Subunit roles: **MlaE** is the transmembrane permease; **MlaF** the nucleotide-binding ATPase; **MlaD** the hexameric MCE-domain ring that both caps the transporter and forms the periplasmic conduit; **MlaB** a STAS-domain accessory that stabilizes and regulates the complex. A synthesis of all available structures proposes an ABC-type lipid-translocation model with parallels to human ABCA/ABCG ([PMID: 35981415](https://pubmed.ncbi.nlm.nih.gov/35981415/)).

| Subunit | Fold/class | Function |
|---|---|---|
| MlaA | OM lipoprotein (donut) | PL handling at OM outer leaflet; docks on OmpC/F |
| MlaC | NTF2-like/PBP, cystatin-derived | Single-PL periplasmic shuttle; one partner at a time |
| MlaD | MCE domain (hexameric ring) | Periplasmic conduit; PL relay to/from MlaC |
| MlaE | Transmembrane permease | Substrate-binding site; PL translocation across IM |
| MlaF | ABC ATPase (NBD) | ATP binding/hydrolysis powering the cycle |
| MlaB | STAS domain | Regulatory/stabilizing accessory |

---

## 5. Evolutionary and Cell-Biological Variation

### The MCE superfamily context

MlaD is a **Mammalian Cell Entry (MCE)** domain protein, and the MCE superfamily is deeply conserved and architecturally diverse. In *E. coli* alone, three paralogous MCE systems have radically different shapes: MlaD forms a single hexameric ring, whereas "YebT forms an elongated tube consisting of seven stacked MCE rings, and PqiB adopts a syringe-like architecture. Both YebT and PqiB create channels of sufficient length to span the periplasmic space" ([PMID: 28388411](https://pubmed.ncbi.nlm.nih.gov/28388411/)). This contrast is mechanistically important: Mla solves the periplasm-crossing problem with a *diffusible carrier* (MlaC), while its paralogs solve it with a *fixed channel*. MCE domains are also present in eukaryotic organelles (chloroplasts and mitochondria), pointing to an ancient lipid-handling role predating the bacteria/organelle divergence.

### Lineage-specific elaborations

- **Chimeric Mla–Pqi systems.** In *Brucella abortus* and across the order Hyphomicrobiales, "a complex named Mpc, which exhibits homology to both Mla and Pqi components," effectively fuses the two module types; it bridges both membranes and is required for survival in macrophages ([PMID: 40804184](https://pubmed.ncbi.nlm.nih.gov/40804184/)). This is a clear case of lineage-specific architectural remodeling.
- **Two MlaA classes.** The OM component varies in whether it carries a lipoprotein signal peptide, defining at least two structural classes across bacterial species ([PMID: 30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/)).
- **Species-specific porin partners and physiology.** The identity of the associated porin (OmpC vs OmpF) and the downstream physiological consequences of Mla loss vary by organism (see §6).

### Ancestral representatives

For understanding the ancestral MCE role, the **single-ring MlaD** is the most parsimonious representative of the minimal functional unit, while the stacked-ring YebT and syringe-like PqiB architectures and the chimeric Mpc are best interpreted as later elaborations or fusions. The eukaryotic organellar MCE homologs suggest the core lipid-binding ring is ancient; the soluble MlaC carrier and the specific MlaFEDB ABC pairing may be more derived features of the diderm periplasmic solution.

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering and mutual-exclusivity constraints

- **Compartmentalization enforces order.** The OM and IM steps cannot occur simultaneously on the same lipid because they are separated by the periplasm; MlaC is the only bridge. This makes MlaC hand-off an obligatory intermediate in either direction.
- **Single-partner binding.** MlaC's overlapping MlaA/MlaD interfaces make OM-binding and IM-binding mutually exclusive, forcing a strict pick-up-then-deliver alternation ([PMID: 37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/)).
- **Energy coupling is directional.** ATP hydrolysis by MlaFEDB disrupts a lipid-binding equilibrium to impose net retrograde flux, meaning the direction of the energized step is a property of the ATP cycle, not free diffusion ([PMID: 34873038](https://pubmed.ncbi.nlm.nih.gov/34873038/)).

### Physiological consequences of failure

Loss of Mla components compromises OM barrier function with pleiotropic, organism-specific outcomes:

| Organism | Perturbation | Phenotype | Reference |
|---|---|---|---|
| *Neisseria gonorrhoeae* | *mlaA* loss | Altered virulence, increased membrane vesicle production, higher cell counts in host-mimicking conditions | [PMID: 30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/) |
| *Haemophilus influenzae* | *vacJ/mlaA* inactivation | Increased FA/PL content, greater susceptibility to hydrophobic antimicrobials, reduced epithelial infection, faster pulmonary clearance | [PMID: 29720703](https://pubmed.ncbi.nlm.nih.gov/29720703/) |
| *Pseudomonas aeruginosa* | *mlaA* deletion | Increased fluoroquinolone susceptibility, reduced rhamnolipid secretion, altered motility/biofilm, heightened innate immune response | [PMID: 37660742](https://pubmed.ncbi.nlm.nih.gov/37660742/) |
| *Acinetobacter baumannii* | *mlaC* modulation | PG remodeling; *mlaC* deletion abolishes C4-mediated colistin potentiation | [PMID: 42318744](https://pubmed.ncbi.nlm.nih.gov/42318744/) |
| *A. baumannii* | Disrupted PL transport + degradation | Permissive state enabling LOS-deficient, colistin-resistant variants | [PMID: 42384486](https://pubmed.ncbi.nlm.nih.gov/42384486/) |

The *P. aeruginosa* data are illustrative: "mlaA deletion in P. aeruginosa ATCC27853 results in phenotypic changes including, an increase in fluoroquinolones susceptibility" ([PMID: 37660742](https://pubmed.ncbi.nlm.nih.gov/37660742/)). In *A. baumannii*, a stress that "upregulates mlaC expression, a key determinant of phospholipid retrograde transport" links the carrier to lipid remodeling: "Deletion of mlaC reduces C4-induced PG enrichment and abolishes C4-mediated potentiation of colistin" ([PMID: 42318744](https://pubmed.ncbi.nlm.nih.gov/42318744/)). And loss of the OM lipoprotein has direct fitness consequences: "Lack of MlaA resulted in higher cell counts during conditions mimicking different host niches" in *N. gonorrhoeae* ([PMID: 30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/)).

Two general lessons emerge. First, Mla loss is usually **sub-lethal** because enzymatic repair provides a parallel route: mislocalized "glycerophospholipids that mislocalize to the outer leaflet are removed by the Mla pathway, which consists of the outer membrane channel MlaA, the periplasmic lipid carrier MlaC, and the inner membrane transporter MlaBDEF," working alongside a periplasmic phospholipase ([PMID: 37463202](https://pubmed.ncbi.nlm.nih.gov/37463202/)). Second, Mla sits at a druggable but double-edged nexus: disrupting PL transport can sensitize cells to existing antibiotics or, paradoxically, open adaptive routes to resistance (e.g., LOS-deficient colistin resistance; [PMID: 42384486](https://pubmed.ncbi.nlm.nih.gov/42384486/)).

---

## 7. Mechanistic Model / Interpretation (Synthesis)

Putting the confirmed findings together yields the following integrated picture. The Mla module is best understood as a **modular, three-stop relay** whose conserved core is (i) an OM PL-handling interface (MlaA on a porin), (ii) a diffusible single-PL carrier (MlaC), and (iii) an ATP-coupled IM ABC engine (MlaFEDB) capped by an MCE ring (MlaD). The invariant logic is topological: because the two membranes are separated by a wide aqueous periplasm, a soluble carrier is mechanistically required, and because MlaC's two docking surfaces overlap, transport must proceed by strict alternation—load at one membrane, cross, unload at the other. This is the structural reason there is no "direct" OM–IM contact within Mla.

Directionality is imposed on this neutral scaffold by energy coupling. The MlaFEDB ATP cycle disrupts a lipid-binding equilibrium to bias flux; genetic and reconstitution data indicate the dominant, asymmetry-preserving mode is retrograde clearance of mislocalized OM PLs. However, individual hand-off steps can proceed without ATP, and export-consistent observations exist, so the system is better described as *biased-bidirectional* than as a committed pump in one direction.

Evolutionarily, the MCE ring at the heart of MlaD is the ancient, conserved element—shared with paralogous bacterial systems (Pqi/YebT) and with eukaryotic organellar lipid transporters—while the soluble MlaC solution, the specific MlaFEDB ABC pairing, the two MlaA classes, and chimeric Mpc-type fusions are lineage-specific elaborations. The system's biology is ultimately about OM asymmetry and barrier integrity, which is why *mla* perturbations reverberate into vesiculation, virulence, and antibiotic susceptibility across pathogens, and why enzymatic repair pathways provide parallel redundancy that keeps Mla loss sub-lethal.

---

## 8. Controversies and Open Questions

### 8.1 Directionality — the central debate

Whether the net physiological flux is **retrograde (OM→IM)** or **anterograde (IM→OM)** remains the field's defining controversy.

- **For retrograde.** The founding genetic definition described "an ABC transport system in *Escherichia coli* with predicted import function that serves to prevent PL accumulation in the outer leaflet of the OM… composed of at least 6 proteins and contains at least 1 component in each cellular compartment" ([PMID: 19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/)). Reconstituted transfer assays show ATP disrupts a lipid-binding equilibrium to drive retrograde transport critical for OM asymmetry ([PMID: 34873038](https://pubmed.ncbi.nlm.nih.gov/34873038/)). A dedicated review notes that although "several groups have advocated that transport could happen in an anterograde fashion (from IM to OM)… recent biochemical studies strongly support retrograde transport" ([PMID: 36459067](https://pubmed.ncbi.nlm.nih.gov/36459067/)).
- **For anterograde.** Evidence that the Mla ABC transporter can export PLs from the IM has been cited to argue "that the Mla pathway may have a role in anterograde phospholipid transport" ([PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/)).

The most defensible current position is that the **architecture is direction-neutral**; the balance of ATP-coupled biochemistry favors retrograde as the dominant asymmetry-maintaining mode, but the system may operate bidirectionally depending on lipid gradients and physiological state. Much of the disagreement reflects differences in assay systems (in vivo genetics vs reconstituted vesicles vs isolated-protein transfer) and organisms, which are not always directly comparable.

### 8.2 Other open questions

- **Substrate scope and selectivity.** MlaC is polyspecific for PL acyl chains ([PMID: 36084896](https://pubmed.ncbi.nlm.nih.gov/36084896/)), but how (or whether) the system discriminates among PL species, and how this relates to lipid-remodeling phenotypes ([PMID: 42318744](https://pubmed.ncbi.nlm.nih.gov/42318744/)), is unresolved.
- **Whole-span structure in action.** Structures exist for MlaFEDB, MlaA–OmpF, MlaC, MlaC–MlaD, and OmpC–MlaA–MlaC individually, but no single structure captures the complete OM-to-IM span mid-transfer; the choreography of MlaC docking/undocking is inferred rather than directly observed.
- **Non-canonical ABC features.** Computational analyses argue that Mla proteins have distinctive properties differentiating them from classical ABC components—e.g., a dynamic MlaA C-terminal extension protruding into the periplasm, an EQ loop in MlaE, and poorly understood MlaB–MlaF interfaces—prompting alternative transport models such as "bait-capture-pull" ([PMID: 41047745](https://pubmed.ncbi.nlm.nih.gov/41047745/)). These predictions await experimental testing.
- **Organism generalizability.** The bulk of mechanistic detail is from *E. coli* with pathogen-specific phenotypes layered on; extrapolating a single directional or mechanistic model to all diderm bacteria risks overgeneralization.

---

## 9. Evidence Base

| Paper (PMID) | Contribution | Supports / Challenges |
|---|---|---|
| Malinverni & Silhavy 2009 ([19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/)) | Founding definition: 6 proteins, one per compartment, "import" function | Supports tripartite module + retrograde framing |
| Ekiert et al. 2017 ([28388411](https://pubmed.ncbi.nlm.nih.gov/28388411/)) | MlaD ring + MlaC ferry; MCE architectural diversity (YebT/PqiB) | Supports architecture and MCE context |
| Coudray et al. 2020 ([33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/)) | 3.05 Å MlaFEDB; ABCA/ABCG kinship; continuous pathway | Supports IM engine as distinct superfamily |
| Chi et al. 2020 ([32884137](https://pubmed.ncbi.nlm.nih.gov/32884137/)) | Six bound PLs; ATP-driven conformational change | Supports ATP-coupled cycling |
| Tang et al. 2021 ([33199922](https://pubmed.ncbi.nlm.nih.gov/33199922/)); Zhou et al. 2021 ([33845086](https://pubmed.ncbi.nlm.nih.gov/33845086/)) | MlaF₂E₂D₆B₂ stoichiometry; nucleotide states | Supports 12-subunit assembly |
| Hughes et al. 2019 ([31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/)) | Pivoting β-sheet in MlaC; export evidence | Supports carrier mechanism; challenges retrograde-only view |
| Dutta & Kanaujia 2022 ([36084896](https://pubmed.ncbi.nlm.nih.gov/36084896/)) | MlaC cystatin-derived fold; polyspecific PL binding | Supports non-canonical carrier |
| MacRae et al. 2023 ([37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/)) | Overlapping MlaA/MlaD surfaces on MlaC | Supports single-partner shuttle |
| Ercan et al. 2019 ([30284446](https://pubmed.ncbi.nlm.nih.gov/30284446/)) | MlaD→MlaC spontaneous transfer | Supports directional affinity |
| Abellón-Ruiz et al. 2017 ([29038444](https://pubmed.ncbi.nlm.nih.gov/29038444/)) | MlaA–OmpF donut/channel structure | Supports OM interface |
| Yeow et al. 2023 ([38092770](https://pubmed.ncbi.nlm.nih.gov/38092770/)) | OmpC–MlaA–MlaC; membrane thinning; PL→MlaC | Supports OM step |
| Low et al. 2021 ([34873038](https://pubmed.ncbi.nlm.nih.gov/34873038/)) | ATP-driven retrograde in reconstitution | Supports retrograde directionality |
| Abellón-Ruiz 2023 ([36459067](https://pubmed.ncbi.nlm.nih.gov/36459067/)) | Directionality review | Frames the controversy |
| Kaur & Mingeot-Leclercq 2024 ([38802775](https://pubmed.ncbi.nlm.nih.gov/38802775/)) | VacJ/MlaA identity and biology | Supports OM component history |
| Baarda et al. 2019 ([30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/)) | Two MlaA classes; virulence/vesiculation | Supports lineage variation |
| Lannoy et al. 2025 ([40804184](https://pubmed.ncbi.nlm.nih.gov/40804184/)) | Brucella Mpc Mla–Pqi chimera | Supports evolutionary variation |
| Guest et al. 2023 ([37463202](https://pubmed.ncbi.nlm.nih.gov/37463202/)) | Parallel periplasmic phospholipase | Defines module boundary vs enzymatic repair |
| Kamischke/Ekiert review 2022 ([35981415](https://pubmed.ncbi.nlm.nih.gov/35981415/)) | Structural synthesis; ABCA/ABCG parallels | Supports translocation model |
| Physiology set: [29720703](https://pubmed.ncbi.nlm.nih.gov/29720703/), [37660742](https://pubmed.ncbi.nlm.nih.gov/37660742/), [42318744](https://pubmed.ncbi.nlm.nih.gov/42318744/), [42384486](https://pubmed.ncbi.nlm.nih.gov/42384486/) | Barrier/virulence/antibiotic phenotypes | Supports physiological relevance |
| Dutta & Kanaujia 2025 ([41047745](https://pubmed.ncbi.nlm.nih.gov/41047745/)) | Distinctive Mla features; "bait-capture-pull" | Proposes new, untested model |

---

## 10. Limitations and Knowledge Gaps

- **Structural gap at the whole-envelope scale.** No structure captures the complete, actively transferring OM→periplasm→IM span; the working cycle is reconstructed from separate snapshots.
- **Assay heterogeneity drives the directionality debate.** In vivo genetics, reconstituted proteoliposomes, and isolated-protein transfer assays give partly discordant directional readouts and are not always directly comparable.
- **Organism bias.** Mechanism is anchored in *E. coli*; phenotypes are drawn from a handful of pathogens (*Neisseria, Haemophilus, Pseudomonas, Acinetobacter, Brucella, Shigella*). Generalization to all diderms is provisional.
- **Substrate discrimination poorly defined.** How PL species selectivity (or its absence) integrates with observed lipid-remodeling phenotypes is not established.
- **Regulation understudied.** The physiological signals that switch Mla activity/direction, and MlaB's precise regulatory contribution, remain unclear.
- **Novel computational predictions untested.** Models such as "bait-capture-pull" and the roles of the MlaA C-terminal extension and MlaE EQ loop ([PMID: 41047745](https://pubmed.ncbi.nlm.nih.gov/41047745/)) are hypotheses awaiting experimental validation.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Directionality resolution in a unified system.** Build a fully reconstituted, dual-membrane vesicle system with fluorescently labeled PLs and directly measure net flux (and its ATP dependence) under defined lipid gradients, in a single preparation, to reconcile retrograde vs anterograde claims.
2. **Whole-span structure in action.** Pursue cryo-EM/cryo-ET (or nanodisc-tethered) structures of the MlaA–OmpC / MlaC / MlaFEDB assembly with trapped transfer intermediates to visualize MlaC docking and hand-off.
3. **MlaC single-partner cycling.** Use single-molecule FRET to test the predicted mutually exclusive MlaA/MlaD binding and measure the alternation kinetics directly ([PMID: 37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/)).
4. **Substrate-selectivity mapping.** Systematically test MlaC/MlaFEDB transfer across defined PL species (head group and acyl chain) to define selectivity and link it to remodeling phenotypes ([PMID: 42318744](https://pubmed.ncbi.nlm.nih.gov/42318744/)).
5. **Cross-lineage comparison.** Characterize the two MlaA classes ([PMID: 30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/)) and the chimeric Mpc system ([PMID: 40804184](https://pubmed.ncbi.nlm.nih.gov/40804184/)) functionally to test which architectural features are essential vs elaborations.
6. **Test computational predictions.** Experimentally probe the MlaA C-terminal extension dynamics, the MlaE EQ loop, and the "bait-capture-pull" model via targeted mutagenesis and transport assays ([PMID: 41047745](https://pubmed.ncbi.nlm.nih.gov/41047745/)).
7. **Therapeutic dissection.** Given the double-edged link to antibiotic susceptibility/resistance, define conditions under which Mla inhibition sensitizes vs enables adaptive resistance ([PMID: 37660742](https://pubmed.ncbi.nlm.nih.gov/37660742/); [PMID: 42384486](https://pubmed.ncbi.nlm.nih.gov/42384486/)).

---

## 12. Key References

- Malinverni JC, Silhavy TJ. *An ABC transport system that maintains lipid asymmetry in the gram-negative outer membrane.* [PMID: 19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/)
- Ekiert DC et al. *Architectures of Lipid Transport Systems for the Bacterial Outer Membrane.* [PMID: 28388411](https://pubmed.ncbi.nlm.nih.gov/28388411/)
- Wotherspoon P et al. *Structure of the MlaC-MlaD complex...* [PMID: 39080293](https://pubmed.ncbi.nlm.nih.gov/39080293/)
- Coudray N et al. *Structure of bacterial phospholipid transporter MlaFEDB with substrate bound.* [PMID: 33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/)
- Chi X et al. *Structural mechanism of phospholipids translocation by MlaFEDB complex.* [PMID: 32884137](https://pubmed.ncbi.nlm.nih.gov/32884137/)
- Tang X et al. *Structural insights into outer membrane asymmetry maintenance... by MlaFEDB.* [PMID: 33199922](https://pubmed.ncbi.nlm.nih.gov/33199922/)
- Zhou C et al. *Structural Insight into Phospholipid Transport by the MlaFEBD Complex from P. aeruginosa.* [PMID: 33845086](https://pubmed.ncbi.nlm.nih.gov/33845086/)
- Hughes GW et al. *Evidence for phospholipid export from the bacterial inner membrane by the Mla ABC transport system.* [PMID: 31235958](https://pubmed.ncbi.nlm.nih.gov/31235958/)
- Dutta S, Kanaujia SP. *MlaC belongs to a unique class of non-canonical substrate-binding proteins...* [PMID: 36084896](https://pubmed.ncbi.nlm.nih.gov/36084896/)
- MacRae MR et al. *Protein-protein interactions in the Mla lipid transport system...* [PMID: 37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/)
- Ercan B et al. *Characterization of Interactions and Phospholipid Transfer between Substrate Binding Proteins of the OmpC-Mla System.* [PMID: 30284446](https://pubmed.ncbi.nlm.nih.gov/30284446/)
- Abellón-Ruiz J et al. *Structural basis for maintenance of bacterial outer membrane lipid asymmetry.* [PMID: 29038444](https://pubmed.ncbi.nlm.nih.gov/29038444/)
- Yeow J et al. *Molecular mechanism of phospholipid transport at the bacterial outer membrane interface.* [PMID: 38092770](https://pubmed.ncbi.nlm.nih.gov/38092770/)
- Low WY et al. *ATP disrupts lipid-binding equilibrium to drive retrograde transport...* [PMID: 34873038](https://pubmed.ncbi.nlm.nih.gov/34873038/)
- Abellón-Ruiz J. *Forward or backward, that is the question: phospholipid trafficking by the Mla system.* [PMID: 36459067](https://pubmed.ncbi.nlm.nih.gov/36459067/)
- Kaur H, Mingeot-Leclercq M-P. *Maintenance of bacterial outer membrane lipid asymmetry: insight into MlaA.* [PMID: 38802775](https://pubmed.ncbi.nlm.nih.gov/38802775/)
- Baarda BI et al. *Neisseria gonorrhoeae MlaA influences gonococcal virulence and membrane vesicle production.* [PMID: 30845186](https://pubmed.ncbi.nlm.nih.gov/30845186/)
- Lannoy A et al. *A chimeric Mla-Pqi lipid transport system is required for Brucella abortus survival in macrophages.* [PMID: 40804184](https://pubmed.ncbi.nlm.nih.gov/40804184/)
- Guest RL et al. *A periplasmic phospholipase that maintains outer membrane lipid asymmetry.* [PMID: 37463202](https://pubmed.ncbi.nlm.nih.gov/37463202/)
- Ekiert/Kamischke review. *Structure and mechanism of the bacterial lipid ABC transporter, MlaFEDB.* [PMID: 35981415](https://pubmed.ncbi.nlm.nih.gov/35981415/)
- *Modulation of Haemophilus influenzae interaction with hydrophobic molecules by VacJ/MlaA.* [PMID: 29720703](https://pubmed.ncbi.nlm.nih.gov/29720703/)
- *P. aeruginosa MlaA/VacJ deficiency: motility, biofilm, fluoroquinolone susceptibility.* [PMID: 37660742](https://pubmed.ncbi.nlm.nih.gov/37660742/)
- *Targeting LPS transport... sensitizes Acinetobacter baumannii to colistin.* [PMID: 42318744](https://pubmed.ncbi.nlm.nih.gov/42318744/)
- *Outer membrane remodeling... lipooligosaccharide-deficient colistin resistance.* [PMID: 42384486](https://pubmed.ncbi.nlm.nih.gov/42384486/)
- *Distinctive Properties of Mla Proteins Differentiate Them From Classical ABC Transporter Components.* [PMID: 41047745](https://pubmed.ncbi.nlm.nih.gov/41047745/)

---

*Prepared as a species-neutral synthesis. Mechanistic detail is anchored predominantly in* E. coli *with pathogen-specific physiology layered in; directional and selectivity claims should not be uncritically generalized across all diderm lineages.*


## Artifacts

- [OpenScientist final report](bacterial_mla_intermembrane_phospholipid_transport-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_mla_intermembrane_phospholipid_transport-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:39080293
2. PMID:28388411
3. PMID:19383799
4. PMID:37463202
5. PMID:31235958
6. PMID:37100290
7. PMID:34873038
8. PMID:29038444
9. PMID:38092770
10. PMID:36084896
11. PMID:30284446
12. PMID:33236984
13. PMID:32884137
14. PMID:38802775
15. PMID:30845186
16. PMID:33199922
17. PMID:33845086
18. PMID:35981415
19. PMID:40804184
20. PMID:29720703
21. PMID:37660742
22. PMID:42318744
23. PMID:42384486
24. PMID:36459067
25. PMID:41047745