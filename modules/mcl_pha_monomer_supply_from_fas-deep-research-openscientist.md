---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T12:10:26.322691'
end_time: '2026-07-11T12:22:09.354052'
duration_seconds: 703.03
template_file: templates/module_research.md.j2
template_variables:
  module_title: mcl-PHA monomer supply from de novo fatty-acid synthesis
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00212 module for the PhaG
    bridge from de novo fatty-acid synthesis to medium-chain-length polyhydroxyalkanoate
    (mcl-PHA) biosynthesis. PhaG supplies (R)-3-hydroxyacyl-CoA monomers from ACP-bound
    fatty-acid-synthesis intermediates for downstream PHA synthases. This module records
    the monomer supply connection rather than the PhaC polymerization step or the
    alternative beta-oxidation/PhaJ monomer-supply routes.
  module_outline: "- mcl-PHA monomer supply from de novo fatty-acid synthesis\n  -\
    \ 1. PhaG bridge from FAS intermediates to mcl-PHA monomers\n  - PhaG FAS-to-mcl-PHA\
    \ monomer supply\n    - phaG: 3-hydroxyacyl-ACP:CoA transacylase (molecular player:\
    \ PSEPK phaG; activity or role: acyltransferase activity)"
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mcl_pha_monomer_supply_from_fas-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mcl_pha_monomer_supply_from_fas-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

mcl-PHA monomer supply from de novo fatty-acid synthesis

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00212 module for the PhaG bridge from de novo fatty-acid synthesis to medium-chain-length polyhydroxyalkanoate (mcl-PHA) biosynthesis. PhaG supplies (R)-3-hydroxyacyl-CoA monomers from ACP-bound fatty-acid-synthesis intermediates for downstream PHA synthases. This module records the monomer supply connection rather than the PhaC polymerization step or the alternative beta-oxidation/PhaJ monomer-supply routes.

## Provisional Biological Outline

- mcl-PHA monomer supply from de novo fatty-acid synthesis
  - 1. PhaG bridge from FAS intermediates to mcl-PHA monomers
  - PhaG FAS-to-mcl-PHA monomer supply
    - phaG: 3-hydroxyacyl-ACP:CoA transacylase (molecular player: PSEPK phaG; activity or role: acyltransferase activity)

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

# The PhaG Bridge: mcl-PHA Monomer Supply from De Novo Fatty-Acid Synthesis

*A commissioned review-style synthesis of the PhaG-mediated connection between de novo fatty-acid synthesis (FAS) and medium-chain-length polyhydroxyalkanoate (mcl-PHA) biosynthesis in* Pseudomonas putida *KT2440 and related pseudomonads. UniPathway UPA00212 module; molecular player PSEPK PhaG.*

---

## Summary

Medium-chain-length polyhydroxyalkanoates (mcl-PHAs; C6–C14 3-hydroxy-fatty-acid polyesters) are carbon and redox storage polymers accumulated by fluorescent pseudomonads and prized as biodegradable thermoplastics. Their (R)-3-hydroxyacyl-CoA monomers can be drawn from two metabolically distinct sources: **β-oxidation of exogenous fatty acids** (via (R)-enoyl-CoA hydratases, PhaJ) and **de novo fatty-acid synthesis** from unrelated carbon sources such as sugars or gluconate. This review concerns the second route and its keystone enzyme, **PhaG** — the device that "taps" FAS by removing (R)-3-hydroxyacyl chains from acyl carrier protein (ACP) and routing them, as coenzyme-A (CoA) thioesters, to the CoA-specific PHA synthases PhaC1/PhaC2. PhaG thereby makes polymer composition independent of the feedstock's chain length, enabling mcl-PHA production from cheap, structurally unrelated substrates.

Three conclusions anchor the current state of knowledge. **First**, PhaG's physiological role as the dedicated FAS-to-PHA bridge is well established and conserved: a loss-of-function *phaG* mutant specifically collapses PHA synthesis from de novo carbon (but not from fatty acids), and heterologous co-expression of *phaC1* plus *phaG* reconstitutes the whole route in bacteria that otherwise cannot make PHA from sugars. **Second**, PhaG's enzymatic mechanism is genuinely contested: originally described as a single acyl-ACP:CoA *transacylase* generating (R)-3-hydroxyacyl-CoA directly, it was later reassigned as a *thioesterase* that releases free (R)-3-hydroxy fatty acid, which a separate (R)-3-hydroxyacyl-CoA ligase (e.g., PP0763) must then activate to the CoA thioester. Both interpretations remain in active use. **Third**, in *P. putida* KT2440 PhaG is the principal but *non-obligatory* de novo supplier: parallel routes (β-oxidation via PhaJ enzymes, and quinoprotein dehydrogenases PedE/PedH) leave residual PHA when *phaG* is deleted, and PhaG competes with RhlA for the same FASII (R)-3-hydroxyacyl-ACP intermediate pool.

The module is best read as an evolutionarily *late, conditional acyl-transfer node* grafted onto two ancient and near-universal chemistries — fatty-acid synthesis and CoA thioester metabolism. It is strongly regulated by nutritional status (maximal under nitrogen limitation; gated post-transcriptionally by the Crc regulator at the *phaC1* step), taxonomically restricted to certain pseudomonads and related Proteobacteria, and frequently carried on mobile genetic elements. This review lays out the evidence, the competing definitions, and the most important open questions.

---

## Key Findings

### Finding 1 — PhaG bridges de novo FAS to mcl-PHA by diverting (R)-3-hydroxyacyl intermediates from ACP

PhaG was first identified in *P. putida* as an (R)-3-hydroxydecanoyl-ACP:CoA transacylase (Rehm, Krüger, Steinbüchel, 1998, *J. Biol. Chem.* 273:24044). The genetics are decisive about its physiological role. A loss-of-function *phaG* mutant (PhaG(N)-21) loses PHA accumulation from unrelated, non-fatty-acid carbon sources, and complementation restores it. In *P. aeruginosa*, a *phaG* knockout reduced PHA from gluconate to roughly 40% of wild-type while PHA production from fatty acids was unaffected — showing that PhaG serves specifically the de novo FAS route and not the β-oxidation route ([PMID: 10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/)). The abstract states plainly that "PhaG from P. aeruginosa exhibits 3-hydroxyacyl-ACP:CoA transacylase activity and strongly enhances the metabolic flux from fatty acid de novo synthesis towards PHA(MCL) synthesis." Sufficiency was demonstrated by reconstitution: functional expression of *phaC1* and *phaG* established a new pathway for mcl-PHA biosynthesis from nonrelated carbon sources in *P. fragi* (~14% CDW from gluconate, 60 mol% 3-hydroxydecanoate), a bacterium that does not natively do this ([PMID: 10788390](https://pubmed.ncbi.nlm.nih.gov/10788390/)). Together, the knockout (necessity, and de-novo-specificity) and the heterologous reconstitution (sufficiency) establish PhaG as the bridge from FAS intermediates to mcl-PHA monomers.

### Finding 2 — The enzymatic mechanism is disputed: transacylase vs. thioesterase-plus-CoA-ligase

The original model (1998–2005) held that PhaG is a single acyl-ACP:CoA transacylase making (R)-3-hydroxyacyl-CoA directly. A revised model (Wang et al., 2012, *Appl. Environ. Microbiol.* 78:519–527) proposed that PhaG functions instead as an (R)-3-hydroxyacyl-ACP **thioesterase**, releasing free (R)-3-hydroxy fatty acid, which is then activated to its CoA thioester by a *separate* (R)-3-hydroxyacyl-CoA ligase (*P. putida* PP0763; *P. aeruginosa* PA3924). This two-enzyme reading is supported by heterologous reconstitution: PHA production in *E. coli* requires co-expression of PhaG *plus* a 3HA-CoA ligase — PhaG alone is insufficient. As one report states, "PhaG, which is first known as a (R)-3-hydroxyacyl-acyl carrier protein (ACP)-CoA transferase, actually functions as a 3-hydroxyacyl-ACP thioesterase, and the product of PP0763 gene from Pseudomonas putida KT2440 has a (R)-3-hydroxyacyl (3HA)-CoA ligase activity" ([PMID: 25732207](https://pubmed.ncbi.nlm.nih.gov/25732207/); see also [PMID: 30799088](https://pubmed.ncbi.nlm.nih.gov/30799088/)). Yet the transacylase interpretation persists and is used productively in metabolic engineering, where PhaG is deployed explicitly as an enzyme "that transfers 3-hydroxy acyl-chains between acyl-carrier protein and coenzyme A thioester forms" to build acyl-CoA pools ([PMID: 35338129](https://pubmed.ncbi.nlm.nih.gov/35338129/)). The disagreement is not merely semantic: under the thioesterase model, the genuinely PHA-committed step may be the downstream ligase rather than PhaG itself.

### Finding 3 — PhaG is one of several redundant, condition-dependent monomer-supply routes in KT2440

In *P. putida* KT2440, monomers arrive from at least two systems: (i) de novo FAS via PhaG (dominant on sugars/gluconate under nitrogen limitation) and (ii) β-oxidation via the (R)-specific enoyl-CoA hydratases PhaJ1/PhaJ4/MaoC (dominant on fatty acids; PhaJ4 is the main supplier for C8/C10). Their redundancy was quantified by a systematic deletion study: removing all three *phaJ* genes still left ~10.7% CDW PHA, and additionally deleting *phaG* caused only a further **1.8-fold decrease** without abolishing accumulation — with quinoprotein alcohol dehydrogenases PedE/PedH implicated as further suppliers. As the study reports, "the deletion of (R)-3-hydroxydecanoyl-ACP:CoA transacylase (PhaG), which connects de novo FA and PHA synthesis pathways, while causing a further 1.8-fold decrease in PHA content, did not abolish PHA accumulation" ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)). The route is also strongly condition-gated: "maximal phaG expression was observed only under nitrogen limitation, with concomitant PHA accumulation" ([PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/)), and at the downstream end the Crc global regulator post-transcriptionally represses *phaC1* translation under balanced C/N ratios ([PMID: 24118893](https://pubmed.ncbi.nlm.nih.gov/24118893/)). PhaG is therefore principal without being obligatory.

### Finding 4 — PhaG and RhlA are parallel (R)-3-hydroxyacyl-ACP-draining enzymes competing for the same pool

In *P. aeruginosa* grown on non-fatty-acid carbon, both PHA (via PhaG) and rhamnolipid (via RhlA) precursors derive from the same de novo FASII intermediate, (R)-3-hydroxyacyl-ACP. PhaG converts this to (R)-3-hydroxyacyl-CoA — the obligatory substrate for the CoA-specific synthases — while RhlA dimerizes two (R)-3-hydroxyacyl-ACP-derived 3-hydroxyalkanoic acids into the rhamnolipid precursor HAA. The primary study states: "The PHA synthases (PhaC1 and PhaC2) are only able to use CoA-linked 3-hydroxy acids and the PhaG enzyme catalyzes the conversion of (R)-3-hydroxyacyl-ACP to (R)-3-hydroxyacyl-CoA, the substrate of PhaC1 and PhaC2" ([PMID: 30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/)). The same work reports that RhlA can generate both rhamnolipid and PHA precursors, and — importantly — that blocking β-oxidation does not decrease this flux, reinforcing that de novo FAS (not β-oxidation) feeds both enzymes on unrelated carbon. RhlA thus defines a competing drain on PhaG's substrate pool and sharpens the module's boundary: the shared node is the ACP-bound intermediate, and the CoA-charging requirement is what makes PhaG (or PhaG + ligase) obligatory for the PHA destination.

### Finding 5 — Synthesis: PhaG is an evolutionarily late, conditional ACP→CoA acyl-transfer node on ancient FAS/CoA chemistry

Convergent evidence across organisms supports a single integrated picture. **Role:** knockouts specifically reduce de-novo-fed PHA (*P. aeruginosa* gluconate PHA to ~40% WT; [PMID: 10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/)) and heterologous *phaC1*+*phaG* reconstitutes the route in non-producers (*P. fragi*; [PMID: 10788390](https://pubmed.ncbi.nlm.nih.gov/10788390/)). **Redundancy:** *phaG* deletion in KT2440 lowers PHA only ~1.8-fold, with PhaJ and PedE/PedH backups ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)). **Regulation:** the route is nitrogen-limitation-induced ([PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/)) and Crc-gated on *phaC1* ([PMID: 24118893](https://pubmed.ncbi.nlm.nih.gov/24118893/)). **Shared substrate:** PhaG and RhlA both draw from the FASII (R)-3-hydroxyacyl-ACP pool ([PMID: 30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/)). **Origin:** *pha* clusters reside on mobile genomic islands with signatures of horizontal transfer, sitting atop the universal FAS + CoA chassis ([PMID: 17629557](https://pubmed.ncbi.nlm.nih.gov/17629557/)). The one unresolved core issue is the chemistry itself — one-step transacylase versus two-step thioesterase + ligase ([PMID: 25732207](https://pubmed.ncbi.nlm.nih.gov/25732207/) vs [PMID: 35338129](https://pubmed.ncbi.nlm.nih.gov/35338129/)).

---

## Definition and Biological Boundaries

### What is inside the module

The UPA00212 "PhaG bridge" module comprises the **single committed hand-off** by which FAS-derived (R)-3-hydroxyacyl intermediates become mcl-PHA precursors:

> (R)-3-hydroxyacyl-**ACP** (an obligate FAS intermediate) → (R)-3-hydroxyacyl-**CoA** (the PHA-synthase substrate), mediated by **PhaG** (a soluble ~34 kDa protein of the α/β-hydrolase superfamily in *P. putida* KT2440).

The output is the **charged monomer pool** feeding PhaC. The module records the *supply connection*, not the downstream polymerization chemistry.

### What lies just outside (and is often conflated)

- **Fatty-acid synthesis proper** (FabB/F/G/A/Z, ACP). PhaG draws on FAS intermediates but is not part of the elongation cycle. FabG (β-ketoacyl-ACP reductase) generates the (R)-3-hydroxyacyl-ACP that PhaG intercepts.
- **The PhaC polymerization step.** PhaC1/PhaC2 (class II PHA synthases) polymerize the CoA-charged monomers. This is the consumer of the module's product, not the module.
- **The β-oxidation / PhaJ route.** When fatty acids are the feedstock, monomers are supplied by (R)-specific enoyl-CoA hydratases (PhaJ1, PhaJ4, MaoC), entirely bypassing PhaG. This is the *alternative* monomer-supply system and must be treated separately.
- **PHA depolymerase / granule proteins** (PhaZ, phasins PhaF/PhaI). Part of the granule cycle, not monomer supply.
- **Rhamnolipid biosynthesis (RhlA).** RhlA diverts the same (R)-3-hydroxyacyl-ACP intermediates to a different product (HAA), a *competing* drain — a neighbor to be treated separately, not part of the PhaG module ([PMID: 30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/)).

### Competing definitions

The chief definitional disagreement is **whether "PhaG" denotes a transacylase (one enzyme, one step) or a thioesterase (requiring a downstream CoA ligase to complete the bridge).** Under the thioesterase model the "module" is really two enzymes (PhaG + a 3HA-CoA ligase such as PP0763). Annotation conventions still commonly list PhaG as "3-hydroxyacyl-ACP:CoA transacylase," which the primary biochemistry now questions.

---

## Mechanistic Model / Interpretation

### The best current model of the sequence of events

```
   Sugar / gluconate / "unrelated" carbon source
                │
                ▼   (central metabolism → acetyl-CoA → malonyl-ACP)
        ┌───────────────────────────────┐
        │   FASII elongation cycle       │
        │   (FabB/F, FabG, FabA/Z, FabI) │
        └───────────────┬───────────────┘
                        │  FabG produces:
             (R)-3-hydroxyacyl-ACP   ◄─── shared intermediate pool
                        │
          ┌─────────────┴──────────────┐
          │                            │
      PhaG node                    RhlA (P. aeruginosa)
   (contested chemistry)               │
          │                            ▼
   ┌──────┴───────┐              HAA → rhamnolipid
   │              │
 MODEL A        MODEL B
 one-step       thioesterase → free (R)-3-OH acid
 transacylase        │
   │            3HA-CoA ligase (PP0763 / PA3924)
   │                 │
   └──────┬──────────┘
          ▼
   (R)-3-hydroxyacyl-CoA   ◄─── OBLIGATORY PhaC substrate
          │
     PhaC1 / PhaC2 (CoA-specific mcl-PHA synthases)
          │
          ▼
       mcl-PHA polymer (C6–C14 3-hydroxyacyl units) → cytoplasmic granules
```

The defining constraint is the **ACP → CoA carrier switch**. FAS chemistry runs on ACP; PHA polymerization runs on CoA. The module exists precisely to reconcile these two incompatible acyl-carrier currencies. Whether that reconciliation is achieved by direct transacylation (Model A) or by hydrolysis-then-re-ligation (Model B) is the crux of the mechanistic debate.

**Obligatory / conditional / accessory steps:**

| Category | Element | Why |
|---|---|---|
| **Obligatory** | Presentation to PhaC as a CoA thioester | PhaC1/PhaC2 are strictly CoA-specific; a CoA-charged, (R)-configured monomer is non-negotiable |
| **Conditional** | The de novo route itself | Engaged chiefly on "unrelated" carbon (sugars/gluconate) and under nitrogen limitation with carbon excess |
| **Accessory (in KT2440)** | PhaG specifically | β-oxidation/PhaJ and PedE/PedH can also supply monomers, so the strict obligation is on "some monomer supply," not on PhaG |

### Major molecular players and active assemblies

| Player | Role in the module | Notes / evidence |
|---|---|---|
| **PhaG** (~34 kDa, α/β-hydrolase superfamily) | Removes (R)-3-hydroxyacyl chain from ACP; yields CoA thioester (Model A) or free acid (Model B) | First identified in *P. putida* (Rehm et al., 1998); [PMID: 10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/) |
| **ACP** (FAS acyl carrier protein) | Substrate carrier delivering (R)-3-hydroxyacyl chains | Shared with FAS and RhlA — a competed-for pool |
| **FabG** (β-ketoacyl-ACP reductase) | Generates (R)-3-hydroxyacyl-ACP upstream | Immediate source of PhaG's substrate |
| **(R)-3-hydroxyacyl-CoA ligase** (PP0763; PA3924) | Activates free 3-OH acid to CoA thioester (Model B only) | Required for PHA in recombinant *E. coli* alongside PhaG ([PMID: 25732207](https://pubmed.ncbi.nlm.nih.gov/25732207/), [PMID: 30799088](https://pubmed.ncbi.nlm.nih.gov/30799088/)) |
| **PhaC1 / PhaC2** (class II synthases) | Polymerize (R)-3-hydroxyacyl-CoA → mcl-PHA | Consumer of module output; strictly CoA-specific ([PMID: 30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/)) |
| **PhaJ1 / PhaJ4 / MaoC** | *Alternative* supply from β-oxidation | PhaJ4 dominant for C8/C10 on fatty acids ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)) |
| **PedE / PedH** | Accessory/backup monomer suppliers | Implicated when main routes removed ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)) |
| **Crc** | Post-transcriptional repressor of *phaC1* | Gates polymerization under balanced C/N ([PMID: 24118893](https://pubmed.ncbi.nlm.nih.gov/24118893/)) |

No stable multi-enzyme complex has been demonstrated; the module is best understood as a **soluble, diffusible metabolite hand-off** via ACP-bound and/or free/CoA-bound intermediates, not a channelled assembly.

### Evolutionary and cell-biological variation

- **Phylogenetic distribution.** *phaG* homologues are widespread among *Pseudomonas* (putida, aeruginosa, oleovorans, stutzeri, nitroreducens, fragi) and extend to non-pseudomonads such as *Burkholderia* ([PMID: 15859323](https://pubmed.ncbi.nlm.nih.gov/15859323/)), indicating the de novo route is broadly disseminated among mcl-PHA producers.
- **"Cryptic" homologues.** In *P. oleovorans*, *phaG* exists (~95% identity to the *P. putida* enzyme) but is transcriptionally silent under inducing conditions, so the strain does not make mcl-PHA from unrelated carbon unless the gene is placed under a heterologous promoter ([PMID: 11131392](https://pubmed.ncbi.nlm.nih.gov/11131392/)). Sequence conservation therefore does not guarantee an active route — regulation matters as much as gene presence.
- **Physiological-state dependence.** PhaG-dependent flux is gated by nutrient status (maximal under nitrogen limitation; [PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/)) and by global regulators (Crc represses *phaC1*; [PMID: 24118893](https://pubmed.ncbi.nlm.nih.gov/24118893/)).
- **Alternative molecular means to the same end.** The de novo route (PhaG) and the β-oxidation route (PhaJ) converge on the identical product — (R)-3-hydroxyacyl-CoA — by unrelated chemistry, feedstock-dependently.
- **Deepest plausible origin.** The two components the module *depends on* — type II FAS (ACP, FabG-type reductases) and CoA thioester metabolism — are evolutionarily deep and near-universal, predating the bacterial radiation. PhaG itself, an α/β-hydrolase-superfamily enzyme, is best read as a **lineage-restricted recruitment** that grafts an ACP-tapping activity onto this ancient chassis. The mobility of *pha* clusters on genomic islands, with mosaic G+C content and horizontal-transfer signatures for *phaB/phaC* ([PMID: 17629557](https://pubmed.ncbi.nlm.nih.gov/17629557/)), helps explain the patchy, sometimes cryptic distribution of an otherwise conserved capability. RhlA represents a **parallel recruitment** of the same substrate to a different product, useful for polarizing what is PhaG-specific versus generic ACP-tapping chemistry.

### Constraints, dependencies, and failure modes

- **Order constraint.** FAS must generate (R)-3-hydroxyacyl-ACP before PhaG can act; PhaC cannot act until a CoA thioester exists. Thus FAS → PhaG → (ligase, if Model B) → PhaC is a fixed order.
- **Carrier constraint (mutually exclusive currencies).** PhaC will not accept ACP-bound or free-acid substrate; a CoA thioester is mandatory. This rules out any path in which a free 3-hydroxy acid is polymerized directly, and is the strongest argument that a ligase step must exist wherever PhaG behaves as a thioesterase.
- **Stereochemical constraint.** PHA synthases are (R)-specific, which is why the FASII (R)-3-hydroxyacyl-ACP intermediate is the natural de novo donor and why (R)-specific PhaJ hydratases are needed on the β-oxidation route.
- **Feedstock specificity.** The PhaG route is engaged on "unrelated" carbon; on fatty acids, β-oxidation/PhaJ dominates and PhaG becomes largely dispensable — a knockout reduces PHA from gluconate but not from fatty acids ([PMID: 10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/)).
- **Failure modes / evidence ruling out alternatives.** *phaG* deletion in KT2440 causes only a ~1.8-fold further drop (on top of triple-*phaJ* deletion) and does not abolish PHA, with PedE/PedH implicated as additional suppliers ([PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)). Blocking β-oxidation does not decrease the de-novo-fed flux to PHA/rhamnolipid precursors, confirming FASII — not β-oxidation — as the source on unrelated carbon ([PMID: 30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/)).

---

## Evidence Base

| PMID | Short title | How it supports/challenges the review |
|---|---|---|
| [10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/) | PhaG in mcl-PHA from non-related carbon (*P. aeruginosa*) | **Supports F1:** direct evidence PhaG couples de novo FAS to mcl-PHA; gluconate-specific knockout defect (~40% WT), fatty-acid-fed PHA unaffected |
| [10788390](https://pubmed.ncbi.nlm.nih.gov/10788390/) | PhaG-mediated PHA in recombinant *P. fragi* | **Supports F1:** reconstitution with *phaC1*+*phaG* shows the bridge is sufficient in a non-native host |
| [25732207](https://pubmed.ncbi.nlm.nih.gov/25732207/) | PHBHHx in recombinant *E. coli* | **Supports F2 (Model B):** states PhaG is a thioesterase and PP0763 is the 3HA-CoA ligase |
| [35338129](https://pubmed.ncbi.nlm.nih.gov/35338129/) | Medium-chain oleochemicals via acyl-ACP:CoA transacylase | **Supports F2 (Model A):** persisting one-step transacylase interpretation in engineering |
| [30799088](https://pubmed.ncbi.nlm.nih.gov/30799088/) | LA-based polymers in recombinant *E. coli* | **Supports F2 (Model B):** PHA needs PhaG *plus* a 3HA-CoA ligase |
| [36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/) | β-oxidation–PHA relationship in KT2440 revisited | **Supports F3:** quantifies PhaG contribution (1.8-fold), shows redundancy with PhaJ and PedE/PedH |
| [16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/) | PHA from styrene in *P. putida* CA-3 | **Supports F3:** maximal *phaG* expression under nitrogen limitation |
| [24118893](https://pubmed.ncbi.nlm.nih.gov/24118893/) | Crc inhibits PHA production in *P. putida* | **Supports F3/F5:** post-transcriptional gating of *phaC1* under balanced C/N |
| [30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/) | β-oxidation and de novo FAS for RL and PHA (*P. aeruginosa*) | **Supports F4:** CoA-charging constraint; PhaG vs RhlA competition; β-oxidation not the FASII-fed source |
| [11131392](https://pubmed.ncbi.nlm.nih.gov/11131392/) | Cryptic *phaG* in *P. oleovorans* | **Supports F5:** gene presence ≠ activity; regulation gates the bridge |
| [15859323](https://pubmed.ncbi.nlm.nih.gov/15859323/) | PCR identification of *phaG* in *Pseudomonas*/*Burkholderia* | **Supports F5:** broad taxonomic distribution of *phaG* |
| [17629557](https://pubmed.ncbi.nlm.nih.gov/17629557/) | PHA genes in an Antarctic *Pseudomonas* genomic island | **Supports F5:** horizontal transfer / mobile *pha* clusters on a universal FAS+CoA chassis |
| [21046374](https://pubmed.ncbi.nlm.nih.gov/21046374/) | PHA homopolymers by *P. putida* | Context: *phaG* deletion used to build homopolymer-producing chassis |
| [16215853](https://pubmed.ncbi.nlm.nih.gov/16215853/) | PHBHHx from gluconate/glucose (engineered strains) | Context: engineered de-novo-fed routes using PhaG or thioesterase strategies |
| [33085217](https://pubmed.ncbi.nlm.nih.gov/33085217/) | Engineering PHA pathways in *P. putida* (review) | Reviews metabolic/regulatory circuits of PHA in KT2440 |
| [28497290](https://pubmed.ncbi.nlm.nih.gov/28497290/) | KT2440 relA/spoT mutant PHA production | Stringent response modulates but is not strictly required for accumulation |

**Strongly supported claims:** PhaG links de novo FAS to mcl-PHA; its loss specifically impairs PHA from unrelated carbon but not from fatty acids; the route is nitrogen-limitation-induced and Crc-gated; the pathway is transferable to heterologous hosts; the same FASII pool feeds both PhaG and RhlA.

**Weaker / indirect claims:** the precise one-step vs two-step chemistry; the exhaustive inventory and flux share of alternative suppliers; PhaG's intrinsic chain-length preference.

---

## Limitations and Knowledge Gaps

- **Mechanistic ambiguity is unresolved** and is the dominant limitation. No single experiment in this evidence base decisively adjudicates transacylase (Model A) vs thioesterase + ligase (Model B) in the native organism. If Model B holds, the truly PHA-committed step may be the 3HA-CoA ligase (PP0763), not PhaG.
- **Organism mixing.** Conclusions blend data from *P. putida*, *P. aeruginosa*, *P. fragi*, *P. oleovorans*, *Pseudomonas* sp. 61-3, and recombinant *E. coli*. RhlA competition is *P. aeruginosa*-specific (rhamnolipid producer) and should not be assumed in all pseudomonads; homologues differ (e.g., cryptic *P. oleovorans phaG*; distinct ligases).
- **Incomplete flux apportionment.** The quantitative partitioning of monomer supply among PhaG, PhaJ1/PhaJ4/MaoC, and PedE/PedH under defined conditions is not fully resolved.
- **No structural data** on PhaG with a bound (R)-3-hydroxyacyl-ACP are represented here; the catalytic residues that would discriminate transacylation from hydrolysis remain to be pinned down experimentally.
- **Chain-length selectivity.** PhaG's intrinsic selectivity across C6–C14 substrates, and how it shapes monomer composition relative to PhaC's own selectivity, is incompletely mapped.
- **Regulatory detail** beyond nitrogen limitation and Crc (e.g., the stringent response) is only partially characterized.

---

## Proposed Follow-up Experiments / Actions

1. **Resolve the mechanism directly.** Purify PhaG and assay, with a defined (R)-3-hydroxyacyl-ACP substrate, whether the immediate product is a CoA thioester (transacylase) or a free acid (thioesterase), with and without added PP0763 ligase, CoA, and ATP — in a single controlled system.
2. **Native-context epistasis.** Construct clean *phaG*, PP0763, and *phaG*+PP0763 deletions in KT2440 and quantify de-novo-fed PHA to determine which step is rate-limiting/obligatory in vivo.
3. **Full redundancy accounting.** In a *phaJ1/phaJ4/maoC* + *phaG* multiple-deletion background, additionally delete *pedE/pedH* to test whether the residual PHA is fully explained, closing the monomer-supply budget.
4. **Flux partitioning at the shared node.** Use ¹³C tracing in *P. aeruginosa* to quantify how (R)-3-hydroxyacyl-ACP is split between PhaG (→PHA) and RhlA (→rhamnolipid) under varying C/N ratios.
5. **Structural biology.** Determine a PhaG structure (or high-quality model) with substrate to define ACP vs CoA recognition and rationalize the transacylase-vs-thioesterase mechanism.
6. **Cross-organism validation.** Test whether the ligase-dependent requirement seen in *E. coli* reflects a genuine native two-enzyme relay in pseudomonads or is a heterologous-host artifact.

---

## Key References

- Rehm BHA, Krüger N, Steinbüchel A. *J Biol Chem* 273:24044–24051 (1998). Original identification of PhaG as (R)-3-hydroxydecanoyl-ACP:CoA transacylase linking FAS and PHA synthesis in *P. putida* (foundational).
- *The Pseudomonas aeruginosa phaG gene product...from non-related carbon sources.* [PMID: 10713430](https://pubmed.ncbi.nlm.nih.gov/10713430/)
- *PhaG-mediated synthesis of PHA...in recombinant Pseudomonas fragi.* [PMID: 10788390](https://pubmed.ncbi.nlm.nih.gov/10788390/)
- *Homologous functional expression of cryptic phaG from Pseudomonas oleovorans.* [PMID: 11131392](https://pubmed.ncbi.nlm.nih.gov/11131392/)
- *Specific identification of (R)-3-hydroxyacyl-ACP:CoA transacylase gene...by PCR.* [PMID: 15859323](https://pubmed.ncbi.nlm.nih.gov/15859323/)
- *Genetic characterization of accumulation of PHA from styrene in P. putida CA-3.* [PMID: 16085828](https://pubmed.ncbi.nlm.nih.gov/16085828/)
- *Biosynthesis of poly(3-hydroxybutyrate-co-3-hydroxyalkanoates) by recombinant E. coli.* [PMID: 25732207](https://pubmed.ncbi.nlm.nih.gov/25732207/)
- *Novel lactate-based polymers containing mcl-3HA in recombinant E. coli.* [PMID: 30799088](https://pubmed.ncbi.nlm.nih.gov/30799088/)
- *Metabolic engineering to produce medium-chain oleochemicals via acyl-ACP:CoA transacylase.* [PMID: 35338129](https://pubmed.ncbi.nlm.nih.gov/35338129/)
- *β-oxidation–PHA synthesis relationship in P. putida KT2440 revisited.* [PMID: 36763117](https://pubmed.ncbi.nlm.nih.gov/36763117/)
- *The Crc protein inhibits PHA production in P. putida under balanced C/N.* [PMID: 24118893](https://pubmed.ncbi.nlm.nih.gov/24118893/)
- *Role of β-oxidation and de novo FAS in RL and PHA production by P. aeruginosa.* [PMID: 30919102](https://pubmed.ncbi.nlm.nih.gov/30919102/)
- *PHA genes of a stress-resistant Antarctic Pseudomonas within a genomic island.* [PMID: 17629557](https://pubmed.ncbi.nlm.nih.gov/17629557/)
- *Engineering Native and Synthetic Pathways in P. putida for Tailored PHAs.* [PMID: 33085217](https://pubmed.ncbi.nlm.nih.gov/33085217/)
- *Biosynthesis of PHA homopolymers by Pseudomonas putida.* [PMID: 21046374](https://pubmed.ncbi.nlm.nih.gov/21046374/)

---

*Prepared as a commissioned synthesis over three investigation iterations (5 findings, 21 papers reviewed). Uncertainty is flagged explicitly; mechanistic claims are attributed to their source organisms and should not be over-generalized across all bacteria.*


## Artifacts

- [OpenScientist final report](mcl_pha_monomer_supply_from_fas-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mcl_pha_monomer_supply_from_fas-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10713430
2. PMID:10788390
3. PMID:25732207
4. PMID:30799088
5. PMID:35338129
6. PMID:36763117
7. PMID:16085828
8. PMID:24118893
9. PMID:30919102
10. PMID:17629557
11. PMID:15859323
12. PMID:11131392
13. PMID:33085217
14. PMID:21046374