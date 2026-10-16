---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:21:44.623534'
end_time: '2026-08-31T12:35:49.655411'
duration_seconds: 845.03
template_file: templates/module_research.md.j2
template_variables:
  module_title: UDP-glucose and UDP-galactose biosynthesis
  module_summary: Species-neutral bacterial module for production of UDP-glucose from
    glucose 6-phosphate and its reversible interconversion with UDP-galactose. The
    module contains phosphoglucomutase, UTP--glucose-1-phosphate uridylyltransferase,
    and UDP-glucose 4-epimerase reactions. It supplies activated hexoses to multiple
    downstream glycoconjugate and storage-polymer pathways; those consuming pathways
    are outside this module.
  module_outline: "- UDP-glucose and UDP-galactose biosynthesis\n  - 1. glucose 1-phosphate\
    \ formation\n  - Phosphoglucomutase reaction\n    - Pgm: phosphoglucomutase (molecular\
    \ player: bacterial phosphoglucomutase family; activity or role: phosphoglucomutase\
    \ activity)\n    - AlgC: phosphoglucomutase (molecular player: bifunctional phosphomannomutase/phosphoglucomutase\
    \ family; activity or role: phosphoglucomutase activity)\n  - 2. UDP-glucose formation\n\
    \  - UTP--glucose-1-phosphate uridylyltransferase reaction\n    - GalU: UTP--glucose-1-phosphate\
    \ uridylyltransferase (molecular player: bacterial UTP--glucose-1-phosphate uridylyltransferase\
    \ family; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)\n\
    \  - 3. UDP-galactose formation and interconversion\n  - UDP-glucose 4-epimerase\
    \ reaction\n    - GalE: UDP-glucose 4-epimerase (molecular player: UDP-glucose\
    \ 4-epimerase family; activity or role: UDP-glucose 4-epimerase activity)"
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
  path: udp_glucose_and_udp_galactose_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: udp_glucose_and_udp_galactose_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

UDP-glucose and UDP-galactose biosynthesis

## Working Scope

Species-neutral bacterial module for production of UDP-glucose from glucose 6-phosphate and its reversible interconversion with UDP-galactose. The module contains phosphoglucomutase, UTP--glucose-1-phosphate uridylyltransferase, and UDP-glucose 4-epimerase reactions. It supplies activated hexoses to multiple downstream glycoconjugate and storage-polymer pathways; those consuming pathways are outside this module.

## Provisional Biological Outline

- UDP-glucose and UDP-galactose biosynthesis
  - 1. glucose 1-phosphate formation
  - Phosphoglucomutase reaction
    - Pgm: phosphoglucomutase (molecular player: bacterial phosphoglucomutase family; activity or role: phosphoglucomutase activity)
    - AlgC: phosphoglucomutase (molecular player: bifunctional phosphomannomutase/phosphoglucomutase family; activity or role: phosphoglucomutase activity)
  - 2. UDP-glucose formation
  - UTP--glucose-1-phosphate uridylyltransferase reaction
    - GalU: UTP--glucose-1-phosphate uridylyltransferase (molecular player: bacterial UTP--glucose-1-phosphate uridylyltransferase family; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
  - 3. UDP-galactose formation and interconversion
  - UDP-glucose 4-epimerase reaction
    - GalE: UDP-glucose 4-epimerase (molecular player: UDP-glucose 4-epimerase family; activity or role: UDP-glucose 4-epimerase activity)

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

# UDP-Glucose and UDP-Galactose Biosynthesis: A Three-Enzyme Bacterial Supply Module

*A concise review-style synthesis. Citations are given as PubMed IDs (PMID). Claims are qualified where the evidence is indirect or organism-specific.*

---

## 1. Executive summary

In bacteria, the nucleotide sugars UDP-glucose (UDP-Glc) and UDP-galactose (UDP-Gal) are produced by a compact, near-universal module of three enzymatic activities acting in series:

1. **Phosphoglucomutase** (Pgm, or the bifunctional AlgC/PMM-PGM class) interconverts glucose-6-phosphate (G6P) and glucose-1-phosphate (G1P).
2. **UTP–glucose-1-phosphate uridylyltransferase** (GalU / UDP-glucose pyrophosphorylase, UGP; EC 2.7.7.9) condenses G1P with UTP to give UDP-Glc + pyrophosphate (PPi).
3. **UDP-glucose 4-epimerase** (GalE; EC 5.1.3.2) reversibly epimerizes UDP-Glc at C4 to UDP-Gal.

The module is best understood as a **metabolic supply hub**: its single committed product, UDP-Glc, is the branch point from which UDP-Gal and a large set of downstream glycoconjugate and storage pathways draw activated hexose. The first two reactions are obligatory and sequential for *de novo* synthesis; the GalE reaction is a **reversible, accessory branch** that both generates UDP-Gal and connects to catabolic galactose salvage (the Leloir pathway).

Mechanistically the three steps are unusually well characterized. The mutase uses a phosphoserine "ping-pong" relay and a dramatic re-orientation of a bisphosphate intermediate (PMID 15238632, 23517223); GalU is an oligomerization-dependent nucleotidyltransferase, typically tetrameric in bacteria (PMID 39704542); and GalE is a short-chain dehydrogenase/reductase (SDR) that uses a tightly bound NAD⁺ to transiently oxidize, rotate, and re-reduce a 4-ketopyranose intermediate (PMID 26162744, 9708982). The major boundary confusions—bacterial glycogen (ADP-glucose/GlgC, **not** UDP-Glc) and the catabolic Leloir enzymes GalK/GalT—are cleared up in §2.

---

## 2. Definition and biological boundaries

### 2.1 What is inside the module
The module is defined by **product**, not by pathway membership: it comprises exactly the reactions that convert G6P → G1P → UDP-Glc ⇌ UDP-Gal. Concretely:

| Step | Activity | EC | Representative players |
|------|----------|----|------------------------|
| 1 | Phosphoglucomutase | 5.4.2.2 | Pgm (dedicated); AlgC/SpgM/PgmG (bifunctional PMM/PGM) |
| 2 | UTP:G1P uridylyltransferase | 2.7.7.9 | GalU / UGP |
| 3 | UDP-glucose 4-epimerase | 5.1.3.2 | GalE |

The **committed, module-defining** reaction is step 2 (GalU): phosphoglucomutase also serves glycolysis/gluconeogenesis and other nucleotide-sugar routes, so only when its G1P is drawn into GalU does the flux "belong" to this module.

### 2.2 Neighboring systems frequently confused with it (and why they are separate)

- **Bacterial glycogen synthesis is NOT part of this module.** In most bacteria and cyanobacteria the glucosyl donor for glycogen is **ADP-glucose**, made by glucose-1-phosphate *adenylyl*transferase **GlgC** (EC 2.7.7.27), an allosterically regulated enzyme (activated by 3-PGA/FBP, inhibited by Pi) that shares G1P with GalU but diverges to a different nucleotide sugar (PMID 39639537, 41631621, 24112771). Thus GalU and GlgC represent a **branch point at G1P**, not a shared pathway. (Plants/animals use UDP-Glc for storage glucans; bacteria generally do not—an important cross-kingdom caveat.)
- **The catabolic Leloir pathway (GalK → GalT → GalE) is a separate, neighboring system.** Galactokinase (GalK, a GHMP kinase; PMID 15590630) and galactose-1-phosphate uridylyltransferase (GalT/GALT) salvage exogenous galactose. GalT runs a **double-displacement** mechanism through a covalent UMP–histidine intermediate, swapping UMP between Gal-1-P and UDP-Glc (PMID 21793161)—a chemistry unrelated to GalU's single-displacement nucleotidyl transfer. **GalE is the only enzyme genuinely shared** between the biosynthetic module and catabolic salvage. Equating "the Leloir pathway" with "UDP-Glc/UDP-Gal biosynthesis" is a common definitional error.
- **Downstream consuming pathways are outside the module.** UDP-Glc/UDP-Gal feed lipopolysaccharide (LPS) core/O-antigen, capsular polysaccharide (CPS), exopolysaccharide/biofilm matrix, wall teichoic acid (WTA) glycosylation, trehalose (OtsA uses UDP-Glc), osmoregulated periplasmic glucans, and glycolipids. These are *sinks*, not part of the supply module (see §6).

### 2.3 Competing definitions
Two definitional axes create most of the literature ambiguity: (i) **"Leloir pathway"** is often used loosely to include or exclude GalE and phosphoglucomutase; here we treat GalK/GalT as catabolic and outside scope. (ii) **"UGP"** is used for both the bacterial GalU family and the structurally distinct eukaryotic UDP-glucose pyrophosphorylases; the two are analogous, not orthologous (see §4.2, §5).

---

## 3. Mechanistic overview

### 3.1 Best current model of the sequence of events
```
 G6P ⇌(Pgm/AlgC)⇌ G1P ──(GalU, +UTP, −PPi)──▶ UDP-Glc ⇌(GalE)⇌ UDP-Gal
                                                  │
                                                  ▼ (downstream sinks: LPS, CPS, EPS, WTA-Gal, trehalose…)
```
- **Step 1 (mutase):** reversible; freely equilibrates G6P/G1P. Direction is pulled toward G1P when downstream steps consume it.
- **Step 2 (GalU):** the **committed, quasi-irreversible in vivo** step. Although chemically reversible, cytoplasmic **pyrophosphatase hydrolysis of PPi** pulls the reaction toward UDP-Glc, making this the physiological commitment point and the flux-controlling node.
- **Step 3 (GalE):** freely **reversible**; sets the UDP-Glc:UDP-Gal ratio according to demand. Because de novo cells make little free galactose, UDP-Gal is normally produced *from* UDP-Glc by GalE rather than by salvage.

### 3.2 Obligatory vs conditional vs accessory
- **Obligatory** for any UDP-Glc output: steps 1 and 2 (unless UDP-Glc is imported/salvaged, which bacteria generally cannot do at scale).
- **Accessory/branch:** step 3 (GalE) is required only when UDP-Gal is needed; it is dispensable for pure UDP-Glc supply.
- **Conditional players:** the phosphoglucomutase activity can be delivered by a dedicated Pgm **or** a bifunctional AlgC-type enzyme that also makes mannose-1-phosphate for GDP-mannose/alginate; which one is present is lineage- and niche-dependent (§4.1).

### 3.3 Chemistry of each step
- **Phosphoglucomutase (α-D-phosphohexomutase superfamily).** A conserved **catalytic phosphoserine** phosphorylates the substrate to a **glucose-1,6-bisphosphate** intermediate; the intermediate then **reorients ~180°** in the active site so the other phosphate can be transferred back to the enzyme, yielding product with the phosphate moved from C1 to C6 (or vice versa). A conserved **His (His329 in P. aeruginosa PMM/PGM), or an analogous Lys in the PGM subgroup**, acts as the general acid/base (PMID 23517223). The phosphorylation state of the catalytic Ser strongly modulates enzyme flexibility and the required domain motions (PMID 24403075, 30149860).
- **GalU (nucleotidyltransferase).** UTP attacks G1P; the α-phosphate of UTP is transferred to the phosphate of G1P forming the UDP-Glc pyrophosphate linkage with release of PPi. Single in-line displacement at phosphorus; Mg²⁺-assisted. Broad 1-phosphosugar tolerance in vitro (e.g., E. amylovora GalU also uridylylates GlcNAc-1-P, xylose-1-P, mannose-1-P; PMID 28844747).
- **GalE (SDR epimerase).** The tightly (essentially irreversibly) bound **NAD⁺** abstracts a hydride from C4 of the glucosyl/galactosyl moiety, generating a **4-ketopyranose** and NADH; the neutral intermediate **rotates within the active site** so that hydride is returned to the opposite face, inverting C4 stereochemistry with **no net redox change** (PMID 26162744, 9708982). Ser124/Tyr149 (E. coli numbering) form the catalytic couple.

---

## 4. Major molecular players and active assemblies

### 4.1 Phosphoglucomutase: two protein solutions to one activity
- **Dedicated Pgm** enzymes provide phosphoglucomutase activity as their primary role.
- **Bifunctional PMM/PGM (AlgC class).** AlgC (*P. aeruginosa*), SpgM (*Stenotrophomonas maltophilia*), and PgmG (*Sphingomonas paucimobilis*) carry **both** phosphoglucomutase and phosphomannomutase activities in one four-domain polypeptide (PMID 12761084, 10788412). PgmG shows ~50-fold higher catalytic efficiency for G1P than M1P, i.e., it is "primarily" a PGM that can moonlight as a PMM (PMID 10788412). These enzymes are the paradigm for the α-D-phosphohexomutase mechanism and are structurally the best-studied (P. aeruginosa PMM/PGM; PMID 23517223, 24403075, 23893395). Their **catalytic cycle demands large domain motions**, and loss of the bifunctional PGM reduces LPS and abolishes virulence in *S. maltophilia* (PMID 12761084)—illustrating how one enzyme feeds several nucleotide-sugar modules.

### 4.2 GalU / UGP: oligomerization-dependent nucleotidyltransferase
Bacterial GalU adopts a Rossmann-like nucleotidyltransferase (dinucleotide-binding) fold; **activity is tied to oligomeric state, and most bacterial homologs are tetramers** (PMID 39704542). Crystal structures from *Yersinia pestis* (PMID 31475928) and *Erwinia amylovora* (PMID 28844747) reveal a conserved active site and support GalU as an **antibacterial/antivirulence drug target**—e.g., in silico–predicted GalU inhibitors block WTA galactosylation and attenuate *Listeria* virulence (PMID 29517123). Note the important caveat that the **bacterial GalU family and the eukaryotic UGP family differ in oligomeric organization and are generally treated as distinct protein lineages performing the same reaction**. Bacterial GalU is typically tetrameric (PMID 39704542), whereas the active eukaryotic enzyme is a **homo-octamer in human and yeast but essentially monomeric in most plants** (PMID 29494650)—so even within eukaryotes the quaternary structure varies, and it differs again from bacteria. This is best read as convergence on a common chemistry rather than assumed strict orthology.

### 4.3 GalE: single-domain SDR homodimer with buried NAD⁺
GalE is a member of the **SDR superfamily** (Rossmann NAD-binding fold), usually a homodimer, with the cofactor bound so tightly it copurifies and is not exchanged during turnover (PMID 26162744). Structures of *E. coli* GalE with UDP-Glc/UDP-Gal (PMID 9708982) and, more recently, cyanobacterial GalE (*Nostoc* all4713) in complex with UDP-Glc and NAD (PMID 42250718) define the substrate pocket and the geometry that permits ketopyranose rotation. **Substrate breadth differs by lineage:** single-domain bacterial GalE typically prefers UDP-hexoses, whereas some eukaryotic GALEs (human, *Drosophila*) additionally interconvert **UDP-GlcNAc/UDP-GalNAc** (PMID 22654673).

---

## 5. Evolutionary and cell-biological variation

- **Deep, modular ancestry from ancient folds.** Each step is built on an old scaffold: the α-D-phosphohexomutase superfamily (phosphoserine-relay mutases; PMID 15238632), the nucleotidyltransferase/Rossmann fold (GalU), and the NAD-dependent SDR/Rossmann fold (GalE). The **reaction logic is conserved from bacteria to humans**, but the specific proteins performing GalU differ in quaternary structure between prokaryotes and eukaryotes (bacterial tetramer vs eukaryotic octamer/monomer; PMID 39704542, 29494650), consistent with **convergent recruitment to the same chemistry** rather than assumed strict orthology.
- **Best representatives of the ancestral role.** For the mutase, the *P. aeruginosa* PMM/PGM is the mechanistic archetype, but the **dedicated Pgm** (mono-functional) likely reflects the ancestral "just PGM" role, with **bifunctional PMM/PGM an elaboration** that co-opted the same active site for mannose. For GalE, the **single-domain, UDP-hexose-specific bacterial enzyme** is the best model of the ancestral epimerase; the dual UDP-hexose/UDP-HexNAc activity of metazoan GALE is a later broadening.
- **Lineage-specific wiring.** Which phosphoglucomutase is used (Pgm vs AlgC-type) tracks with a lineage's glycan repertoire—alginate/gellan/EPS producers favor the bifunctional enzyme because it simultaneously supplies M1P. GalE presence/absence and specificity track with whether an organism builds galactose- or GalNAc-containing surface glycans.
- **Physiological-state variation.** Expression of galU/galE is frequently up-regulated under biofilm, stress, or host-colonization conditions; e.g., galU carbon flux is partitioned between exopolysaccharide synthesis and the pentose phosphate pathway under changing oxygen tension in *Komagataeibacter* (PMID 32270472). This is regulatory tuning of a shared hub rather than a change in the core chemistry.
- **Cross-kingdom caveat (do not overgeneralize).** Storage-glucan chemistry differs sharply: **bacteria = ADP-glucose/GlgC; plants/animals = UDP-glucose**. Galactose toxicity phenotypes and UPR involvement described in yeast and mammals (PMID 35301088, 29580862, 21793161) reflect eukaryotic salvage physiology and should not be transposed onto the bacterial biosynthetic module.

---

## 6. Constraints, dependencies, and failure modes

- **Order is fixed for de novo synthesis:** G6P must become G1P before GalU can act, and UDP-Glc must exist before GalE can make UDP-Gal. There is no bacterial route that makes UDP-Gal from UDP-Glc without GalE, nor UDP-Glc from G1P without a nucleotidyltransferase.
- **Thermodynamic pull:** GalU is chemically reversible but rendered effectively forward in vivo by **PPi hydrolysis**; without pyrophosphatase activity the commitment step would stall. This is the key "directional" constraint.
- **Cofactor dependency:** GalE is inert without its bound NAD⁺; the cofactor is regenerated intramolecularly each cycle, so net turnover consumes no NAD(H)—but apo-enzyme or reduced/adducted NAD states are inactive.
- **Substrate-specific branching at G1P:** G1P is contested by GalU (→UDP-Glc) and GlgC (→ADP-Glc); these are **mutually exclusive fates** for a given G1P molecule and are separately regulated (allosteric control of GlgC; PMID 24112771, 39639537). Mannose branches away earlier (M1P via PMM/AlgC).
- **Failure modes (loss-of-function phenotypes, all in downstream sinks):** galU loss → truncated LPS core, colonization and biofilm defects, heightened sensitivity to bile/complement/antimicrobials (*Vibrio cholerae*, PMID 11119535; *Xanthomonas*, PMID 25033927). galE loss → inability to make UDP-Gal-containing surface glycans and loss of galactose catabolism, but often near-normal LPS if galactose is not a core sugar (PMID 11119535). These phenotypes belong to consuming pathways, confirming the module's role as **supplier, not effector**.

---

## 7. Controversies and open questions

1. **In vivo directionality and flux control.** The commitment step is generally assigned to GalU (PPi-pulled), but quantitative flux control coefficients across the mutase/GalU/GalE trio are rarely measured; the relative control under biofilm vs planktonic states is largely inferred, not directly demonstrated.
2. **Oligomeric state and regulation of GalU.** The tetramer is the consensus (PMID 39704542), but whether oligomerization is a *regulatory* switch (allostery, UTP/UDP-Glc feedback) or merely a stability requirement is unsettled and likely species-specific.
3. **"Which PGM?" ambiguity.** Many genomes encode multiple phosphohexomutases (dedicated Pgm, AlgC-type, phosphoglucosamine mutase GlmM/related; note substrate-assisted catalysis in that subfamily, PMID 29967067). Assigning the physiologically dominant supplier of G1P to a specific gene is often done by homology rather than by flux measurement.
4. **GalE substrate scope generalizations.** The UDP-HexNAc epimerase activity is prominent in metazoan GALE (PMID 22654673) and some bacteria but absent in others; reviews sometimes overstate promiscuity by pooling data across distant organisms (PMID 26162744). Substrate range should be asserted per-enzyme, not per-family.
5. **Evolutionary origin of the bacterial vs eukaryotic UGP split.** The bacterial and eukaryotic enzymes differ in quaternary structure (tetramer vs octamer/monomer; PMID 39704542, 29494650); whether this reflects deep divergence within one fold family or independent recruitment is not fully resolved and merits explicit phylogenetic caution.
6. **Cross-organism transfer of mechanism.** Much galactosemia/UPR mechanism is eukaryotic (PMID 35301088, 21793161); its relevance to bacterial physiology is limited and should not be assumed.

---

## 8. Key references

- Beerens, Soetaert & Desmet. UDP-hexose 4-epimerases: structure, mechanism and substrate specificity. *Biotechnol. Adv.*/review, 2015. **PMID 26162744**.
- Thoden & Holden. Binding of UDP-galactose and UDP-glucose to *E. coli* UDP-galactose 4-epimerase (4′-ketopyranose rotation). 1998. **PMID 9708982**.
- Huo et al. GalE all4713 from *Nostoc* sp. PCC 7120; crystal structure with UDP-Glc and NAD. 2026. **PMID 42250718**.
- Shackelford, Regni & Beamer. Evolutionary trace analysis of the α-D-phosphohexomutase superfamily. 2004. **PMID 15238632**.
- Lee, Mehra-Chaudhary, Furdui & Beamer. Essential active-site His329 in the α-D-phosphohexomutase superfamily (P. aeruginosa PMM/PGM). 2013. **PMID 23517223**.
- Lee et al. Dephosphorylation-promoted flexibility coupled to phosphohexomutase catalysis. 2014. **PMID 24403075**.
- Videira et al. Bifunctional PgmG (PGM/PMM) of *Sphingomonas paucimobilis*; G1P preference. 2000. **PMID 10788412**.
- McKay et al. Bifunctional SpgM (PGM/PMM) of *Stenotrophomonas maltophilia*; LPS/virulence. 2003. **PMID 12761084**.
- Führing et al. Functional tetrameric bacterial UDP-glucose pyrophosphorylase; drug-target rationale. 2025. **PMID 39704542**.
- Gibbs et al. Crystal structure of *Yersinia pestis* UGP. 2019. **PMID 31475928**.
- Cotrim et al. Crystal structure and oligomeric state of sugarcane UGPase; contrasts plant-monomer vs human/yeast-octamer (eukaryotic vs bacterial comparison). 2018. **PMID 29494650**.
- Benini et al. *Erwinia amylovora* GalU: activity, structure, substrate specificity; couples to GalE→UDP-Gal for amylovoran. 2017. **PMID 28844747**.
- Kuenemann et al. GalU inhibitors block *Listeria* WTA galactosylation/virulence. 2018. **PMID 29517123**.
- Nesper et al. *Vibrio cholerae* galU/galE: LPS, colonization, biofilm. 2001. **PMID 11119535**.
- Liao et al. *Xanthomonas campestris* galU: polysaccharide, motility, virulence, stress. 2014. **PMID 25033927**.
- Lee et al. Cyanobacterial GlgC and ADP-glucose glycogen synthesis (boundary). 2026. **PMID 41631621**; 2025 **PMID 39639537**; *S. mutans* ADP-Glc PPase **PMID 24112771**.
- McCorvie & Timson. Type I galactosemia enzymology: GALT double-displacement (boundary/Leloir). 2011. **PMID 21793161**.
- Daenzer et al. *Drosophila* GALE dual UDP-Gal/UDP-GalNAc activities (lineage variation). 2012. **PMID 22654673**.
- Thoden et al. Human galactokinase structure (GHMP kinase; catabolic Leloir boundary). 2005. **PMID 15590630**.
- Huang et al. galU controls carbon flux between EPS and PP pathway in *Komagataeibacter*. 2020. **PMID 32270472**.

---

### Explicit uncertainty statement
This synthesis draws on structural and enzymological work concentrated in a handful of model organisms (*P. aeruginosa* PMM/PGM; *E. coli*/*Nostoc* GalE; *Y. pestis*/*E. amylovora* GalU). Mechanistic chemistry (phosphoserine relay, PPi-pulled nucleotidyl transfer, NAD⁺-mediated C4 epimerization) is strongly supported and broadly transferable. In contrast, regulation, oligomeric-state control, quantitative flux control, and per-species substrate breadth are less uniformly established and should not be generalized across all bacteria without direct evidence.


## Artifacts

- [OpenScientist final report](udp_glucose_and_udp_galactose_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](udp_glucose_and_udp_galactose_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)