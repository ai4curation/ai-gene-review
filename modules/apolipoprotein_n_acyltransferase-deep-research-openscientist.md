---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:36:37.450061'
end_time: '2026-07-11T14:45:48.680125'
duration_seconds: 551.23
template_file: templates/module_research.md.j2
template_variables:
  module_title: Apolipoprotein N-acyltransferase
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00666 module for the final
    phospholipid-dependent N-acylation step of bacterial lipoprotein maturation. The
    module is centered on Lnt (PP_4790, UniProtKB:Q88DN4), which transfers an acyl
    chain from a glycerophospholipid to the amino group of the N-terminal cysteine
    of a diacylglyceryl lipoprotein.
  module_outline: "- Apolipoprotein N-acyltransferase\n  - 1. Final N-acylation of\
    \ mature bacterial lipoprotein\n  - Lnt apolipoprotein N-acyltransferase step\n\
    \    - lnt: apolipoprotein N-acyltransferase (molecular player: PSEPK lnt; activity\
    \ or role: N-acyltransferase activity)"
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
  path: apolipoprotein_n_acyltransferase-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: apolipoprotein_n_acyltransferase-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Apolipoprotein N-acyltransferase

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00666 module for the final phospholipid-dependent N-acylation step of bacterial lipoprotein maturation. The module is centered on Lnt (PP_4790, UniProtKB:Q88DN4), which transfers an acyl chain from a glycerophospholipid to the amino group of the N-terminal cysteine of a diacylglyceryl lipoprotein.

## Provisional Biological Outline

- Apolipoprotein N-acyltransferase
  - 1. Final N-acylation of mature bacterial lipoprotein
  - Lnt apolipoprotein N-acyltransferase step
    - lnt: apolipoprotein N-acyltransferase (molecular player: PSEPK lnt; activity or role: N-acyltransferase activity)

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

# Apolipoprotein *N*-acyltransferase (Lnt): the phospholipid-dependent final step of bacterial lipoprotein maturation

*A review-style synthesis anchored on the* Pseudomonas putida *KT2440 UniPathway UPA00666 module (Lnt = PP_4790, UniProtKB:Q88DN4)*

---

## 1. Executive summary

Bacterial lipoproteins are anchored in the cell envelope through a lipid-modified N‑terminal cysteine and serve in envelope assembly, transport, enzymatic catalysis, signalling and virulence. Their maturation is a strictly ordered, three-enzyme, membrane-embedded post-translational pathway: **Lgt → LspA → Lnt**. **Apolipoprotein *N*-acyltransferase (Lnt)** catalyses the *final* step — transfer of a single acyl chain from a membrane glycerophospholipid to the free α‑amino group of the already diacylated N‑terminal cysteine — converting a *diacyl* apolipoprotein into the mature *triacyl* lipoprotein (PMID 28698362, 25670733). In diderm (Gram‑negative/proteobacterial) cells this is a chemically and topologically well-defined reaction: Lnt is an integral inner-membrane enzyme of the **carbon-nitrogen (CN) hydrolase / nitrilase superfamily** that operates by a **ping-pong mechanism** through a covalent **thioester acyl-enzyme intermediate** on a catalytic cysteine, using an **E267‑K335‑C387 catalytic triad** (numbering from *E. coli*) (PMID 21676878, 17416655). Crystal structures of Lnt from *Pseudomonas aeruginosa* and *Escherichia coli* are near-identical — a multi-TM membrane domain supporting a periplasmic catalytic domain with an active site at the membrane–periplasm interface — and provide the best available structural proxy for the *P. putida* KT2440 enzyme (PMID 28675161, 28698362).

The system's boundaries are important. Lnt maturation is **upstream of, and mechanistically distinct from, the Lol trafficking pathway** (LolCDE–LolA–LolB) that sorts mature lipoproteins to the outer membrane; N‑acylation is a *prerequisite* for efficient Lol recognition but is not itself a sorting step (PMID 15513925). Across evolution, Lnt is conserved in proteobacteria and in high‑GC Gram‑positives (Actinobacteria/Mycobacteria) but is **absent from low‑GC Firmicutes**, which nonetheless N‑acylate their lipoproteins using non-orthologous, convergent enzymes and produce a wider range of acylation states (PMID 24093492, 32723923). Lnt is **essential in proteobacteria** and is an antibiotic-target candidate, though a more challenging one than LspA (PMID 15513925, 32979868, 31036406). *P. putida* KT2440, a γ‑proteobacterium, is expected to use the canonical, essential Lnt route.

---

## 2. Definition and biological boundaries

### 2.1 What the system *is*
The UPA00666 module is narrowly the **N‑acylation reaction that completes lipoprotein maturation**:

- **Substrate (acceptor):** *S*-diacylglyceryl-cysteine apolipoprotein — a lipoprotein whose N‑terminal cysteine already bears a thioether-linked diacylglyceryl group (installed by Lgt) and whose signal peptide has been removed (by LspA), leaving a free α‑amino group.
- **Co-substrate (acyl donor):** a membrane **glycerophospholipid**, predominantly phosphatidylethanolamine (PE) in enterobacteria (PMID 21676878).
- **Enzyme:** **Lnt** (PP_4790 / Q88DN4 in *P. putida* KT2440), an integral inner-membrane protein.
- **Product:** the **mature triacylated lipoprotein**, carrying two ester-linked acyl chains (diacylglyceryl) plus one **amide (N)-linked** acyl chain on the cysteine α‑amino group, and a by-product **lyso-phospholipid**.

The module therefore *begins* with the LspA product and *ends* with the triacyl lipoprotein. It is defined by a single covalent chemistry — amide bond formation on an N‑terminal cysteine — carried out by one enzyme.

### 2.2 Neighbouring processes that should be treated separately
Several adjacent processes are frequently discussed together with Lnt but are mechanistically distinct and should not be conflated:

1. **Upstream maturation steps.** *Lgt* (phosphatidylglycerol:prolipoprotein diacylglyceryl transferase) recognises the **lipobox** and adds the diacylglyceryl group; *LspA* (signal peptidase II) removes the signal peptide (PMID 28698362, 25670733). These generate Lnt's substrate but are separate enzymes/reactions.
2. **Lol trafficking.** The **LolCDE** ABC transporter extracts OM-destined lipoproteins from the inner membrane, hands them to the periplasmic chaperone **LolA**, which delivers them to the OM receptor **LolB** (PMID 15513925). This is a *transport* system, not a modification step; it acts on Lnt's product. Notably, LolB is restricted to γ‑proteobacteria and absent from some diderms (e.g., spirochetes), underscoring that trafficking machinery varies independently of the acylation chemistry (PMID 39149330).
3. **Sorting rules (the "+2 rule").** Whether a mature lipoprotein stays in the inner membrane or is exported depends on the residue immediately following the acylated cysteine (classically Asp at +2 acts as a Lol-avoidance/IM-retention signal in *E. coli*) (PMID 15513925). This is a sequence-encoded sorting determinant, orthogonal to the acylation reaction.
4. **Innate-immune recognition.** Triacylated versus diacylated lipopeptides are differentially sensed by **TLR2/TLR1** vs **TLR2/TLR6**. This is a host-side consequence of the acylation state, not part of the bacterial enzymatic module (PMID 32723923).

### 2.3 Competing definitions
There is broad agreement on the biochemistry in proteobacteria. The main definitional tension concerns **"apolipoprotein N‑acyltransferase" as a function versus Lnt as a specific protein family**: low‑GC Firmicutes perform N‑acylation without an Lnt ortholog, so "apolipoprotein N‑acyltransferase activity" is polyphyletic even though the *lnt* gene family is not universal (PMID 24093492, 32723923). For UPA00666 in *P. putida*, the narrow, protein-specific definition (Lnt = CN-hydrolase-family enzyme) applies.

---

## 3. Mechanistic overview

### 3.1 The best current model: a two-step ping-pong transacylation
Lnt runs a **bi‑bi ping‑pong** reaction in two half-reactions (PMID 21676878):

1. **Acyl-enzyme formation (donor half-reaction).** The catalytic cysteine (C387 in *E. coli*) attacks the *sn*-1 ester carbonyl of a glycerophospholipid, forming a **covalent thioester acyl-enzyme intermediate** and releasing a **lyso-phospholipid**. This half-reaction is comparatively *slow* and rate-influencing.
2. **N‑acyl transfer (acceptor half-reaction).** The α‑amino group of the diacylglyceryl-cysteine apolipoprotein attacks the thioester, resolving the intermediate and installing the **amide-linked** acyl chain. This step is *fast* in vitro.

The **E267‑K335‑C387** triad is the catalytic core: Cys is the nucleophile, and the Glu/Lys pair supports thioester formation and aminolysis, consistent with nitrilase/CN‑hydrolase chemistry (PMID 17416655). Structural snapshots subsequently visualised intermediate states along this pathway, reinforcing the interfacial, two-step model (PMID 37390210, 28675161).

### 3.2 Which steps are obligatory, conditional, or accessory
- **Obligatory:** (i) prior diacylglyceryl modification and signal-peptide cleavage (Lnt cannot act on an uncleaved prolipoprotein or a non-diacylated cysteine); (ii) acyl-enzyme formation *before* N‑acyl transfer (enforced by the ping-pong mechanism); (iii) an intact catalytic triad and the additional essential residues Y388/E389 (active-site pocket) and W237/E343 (mobile arms) (PMID 17416655).
- **Conditional / substrate-dependent:** the *identity* of the transferred acyl chain, which reflects the cellular phospholipid pool and headgroup/acyl-chain composition rather than a fixed intrinsic selectivity (PMID 21676878).
- **Accessory / downstream:** Lol-mediated sorting and the +2 retention rule — required for correct localisation of the product but not for the acylation chemistry itself (PMID 15513925).

### 3.3 Topology and compartmentalisation
Lnt is a polytopic inner-membrane protein; *E. coli* topology mapping indicates **six transmembrane segments** with the catalytic domain facing the **periplasm** (PMID 15513925). Structures show the periplasmic globular (CN-hydrolase) domain sitting atop the membrane domain, with the active site at the interface — ideally placed to accept a membrane-embedded phospholipid donor and a membrane-anchored lipoprotein acceptor while performing chemistry in the aqueous periplasmic environment (PMID 28675161, 28698362).

---

## 4. Major molecular players and active assemblies

| Step | Enzyme / assembly | Reaction | Notes |
|---|---|---|---|
| 1 | **Lgt** | Diacylglyceryl transfer to lipobox Cys (from PG) | Recognises lipobox; generates thioether-linked diacylglyceryl-cysteine (PMID 28698362) |
| 2 | **LspA** (signal peptidase II) | Signal-peptide cleavage | Yields free N‑terminal S‑diacylglyceryl-Cys; top antibiotic target (globomycin, myxovirescin) (PMID 31036406) |
| 3 | **Lnt** (this module; PP_4790/Q88DN4) | *N*-acylation of Cys α‑amino group from a phospholipid | CN-hydrolase family; E267‑K335‑C387; thioester intermediate; ping-pong (PMID 21676878, 17416655) |
| Downstream | **LolCDE / LolA / LolB** | IM→OM sorting of mature lipoprotein | Separate transport module; depends on Lnt product; LolB γ‑proteobacteria-restricted (PMID 15513925, 39149330) |

**Structural anchor for *P. putida*:** The *P. aeruginosa* and *E. coli* Lnt crystal structures are "remarkably similar" (PMID 28675161). Because *P. putida* KT2440 Lnt is a close γ‑proteobacterial relative of *P. aeruginosa* Lnt, and proteobacterial Lnt orthologs cross-complement in vivo (PMID 17416655), the *P. aeruginosa* structure is the best representative for understanding PP_4790's architecture and active site. No experimental *P. putida* Lnt structure is required to infer the mechanism, though this remains an inference rather than a direct measurement.

**Acyl donor:** glycerophospholipids, with PE the efficient donor in enterobacteria and activity strongly modulated by headgroup and acyl-chain composition (PMID 21676878). *P. putida* membranes are PE/PG-rich, so PE is the plausible physiological donor, but this has not been directly demonstrated in *P. putida* and is extrapolated from *E. coli*.

---

## 5. Evolutionary and cell-biological variation

### 5.1 Deep origin and family membership
Lnt belongs to the **nitrilase / carbon-nitrogen hydrolase superfamily**, an ancient and widespread group of Cys‑Glu‑Lys catalytic-triad enzymes (PMID 17416655, 29859843). The lipoprotein-processing pathway as a whole is a conserved feature of the bacterial envelope, and the diacyl→triacyl chemistry appears deeply rooted in diderm lineages. Within the superfamily, the **soluble nitrilases are the best out-group for understanding the ancestral catalytic core**, while the membrane domain and mobile "arms" are Lnt-specific elaborations that adapt the enzyme to interfacial, lipid substrates (PMID 29859843, 17416655).

### 5.2 Lineage variation and alternative routes
- **Proteobacteria (incl. *P. putida*):** canonical, essential Lnt; triacylated lipoproteins; product feeds the Lol pathway (PMID 15513925, 28675161).
- **High-GC Gram-positives (Actinobacteria/Mycobacteria):** possess functional Lnt (e.g., *M. bovis* BCG_2070c); knockout abolishes N‑acylation; lipoproteins are triacylated, sometimes with tuberculostearic/palmitoyl chains (PMID 24093492). These Lnt do **not** cross-complement *E. coli*, indicating divergent substrate/partner surfaces (PMID 17416655).
- **Low-GC Gram-positives (Firmicutes):** **no Lnt ortholog**, yet N‑acylation occurs via **non-orthologous, convergent** enzymes, and the N‑terminal acylation state is **structurally heterogeneous** (di-, tri-, N‑acetyl, lyso forms) — a genuinely alternative molecular route to a similar chemical outcome (PMID 24093492, 32723923). In some species N‑acylation depends on membrane lipid state/physiology (e.g., pH/lipid composition), a regulatory dimension largely absent from the essential proteobacterial route (PMID 22467782).

### 5.3 Physiological/compartmental variation
Because Lnt acts at the inner-membrane/periplasm interface, its activity is embedded in envelope lipid homeostasis: the acyl chains it transfers mirror the phospholipid pool (PMID 21676878, 25670733). Variation is therefore expected across growth conditions that reshape membrane lipids, but for the essential proteobacterial enzyme the reaction chemistry itself is invariant.

---

## 6. Constraints, dependencies, and failure modes

- **Strict pathway order.** Lnt requires the *product of LspA* (a cleaved, diacylated cysteine with a free α‑amino group); it cannot act on a prolipoprotein or an unmodified cysteine. The three enzymes act sequentially and non-interchangeably (PMID 28698362, 25670733).
- **Internal reaction order.** The ping-pong mechanism mandates acyl-enzyme formation *before* aminolysis; the two half-reactions cannot be reversed (PMID 21676878).
- **Compartmental constraint.** Catalysis occurs at the periplasm-facing membrane interface via a six-TM enzyme; both substrates are membrane-associated while the chemistry is periplasmic (PMID 15513925, 28675161).
- **Downstream dependency.** N‑acylation is required for efficient **Lol recognition**; loss of Lnt causes apo-lipoproteins (e.g., apoLpp) to accumulate in the inner membrane and is **lethal** in *E. coli* — evidence that ruling-out an "unacylated export" path is well supported (PMID 15513925).
- **Failure modes.** Depletion/inactivation of Lnt → accumulation of diacyl apolipoproteins, mislocalisation, envelope stress, and death in proteobacteria (PMID 15513925). This essentiality is the basis for antibiotic interest, tempered by the difficulty of achieving selectivity at Lnt's active site (PMID 32979868, 31036406).

---

## 7. Controversies and open questions

1. **Phospholipid donor selectivity.** Early work suggested minimal headgroup preference; later defined in vitro assays found strong headgroup/acyl-chain dependence (PE efficient) (PMID 21676878). The physiological donor(s) in *P. putida* specifically have not been measured and are inferred from enterobacterial data.
2. **Direct evidence in *P. putida*.** The KT2440 Lnt (PP_4790) is assigned by orthology/UniPathway; mechanism, structure, essentiality, and donor identity are extrapolated from *E. coli* and *P. aeruginosa*. Direct biochemical/genetic validation in KT2440 is lacking. This is a clear over-extrapolation risk the field should acknowledge.
3. **Structural interpretation of intermediates.** Multiple 2017 structures and later "snapshot" work support the interfacial ping-pong model, but details of substrate entry/exit routes and arm dynamics (W237/E343) remain partly modelled rather than fully resolved (PMID 28675161, 28698362, 37390210, 17416655).
4. **Cross-lineage comparability.** Data are mixed across *E. coli*, *P. aeruginosa*, mycobacteria, and Firmicutes. Because actinomycete Lnt does not complement *E. coli* and Firmicutes lack Lnt entirely, mechanistic claims should not be generalised uncritically across all bacteria (PMID 17416655, 24093492, 32723923).
5. **Druggability.** Whether Lnt (as opposed to LspA) can yield a selective, non-toxic antibacterial remains open; its buried, membrane-interfacial active site is a practical obstacle (PMID 32979868, 31036406).
6. **Regulation.** Whether Lnt activity is regulated (versus constitutively essential) — as hinted by lipid/physiology-dependent N‑acylation in some Gram-positives — is unresolved for proteobacteria (PMID 22467782).

---

## 8. Key references

- Robichon C, Vidal-Ingigliardi D, Pugsley AP. *Depletion of apolipoprotein N-acyltransferase causes mislocalization of outer membrane lipoproteins in E. coli.* J Biol Chem. 2005. **PMID 15513925** — Lnt essentiality, 6-TM topology, Lnt→Lol dependency.
- Vidal-Ingigliardi D, Lewenza S, Buddelmeijer N. *Identification of essential residues in apolipoprotein N-acyl transferase, a member of the CN hydrolase family.* J Bacteriol. 2007. **PMID 17416655** — E267-K335-C387 triad; proteobacterial cross-complementation.
- Hillmann F, Argentini M, Buddelmeijer N. *Kinetics and phospholipid specificity of apolipoprotein N-acyltransferase.* J Biol Chem. 2011. **PMID 21676878** — thioester intermediate; ping-pong kinetics; PE donor.
- Brülle JK, Tschumi A, Sander P. *Lipoproteins of slow-growing Mycobacteria... N-acylated by Lnt BCG_2070c.* 2013. **PMID 24093492** — Lnt distribution; high-GC Gram-positive Lnt.
- Buddelmeijer N. *The molecular mechanism of bacterial lipoprotein modification—how, when and why?* FEMS Microbiol Rev. 2015. **PMID 25670733** — authoritative pathway review.
- Wiktor M, ... Caffrey M, et al. *Structural insights into the membrane integral N-acyltransferase step...* 2017. **PMID 28675161** — *P. aeruginosa* + *E. coli* Lnt structures.
- Noland CL, ... Murray BW, et al. *Structural insights into lipoprotein N-acylation by...* 2017. **PMID 28698362** — Lnt structure; pathway description.
- Cheng L, Doyle A, El Arnaout T. *The N-acyltransferase Lnt: structure-function insights.* 2018. **PMID 29859843** — comparison with soluble nitrilases.
- El Arnaout T, Soulimane T. *Targeting Lipoprotein Biogenesis: Considerations towards Antimicrobials.* 2019. **PMID 31036406** — druggability triage (LspA vs Lnt).
- Gardiner JH, ... Meredith TC, et al. *Lipoprotein N-acylation (structural heterogeneity in Firmicutes).* 2020. **PMID 32723923** — Lnt-independent N-acylation; TLR2.
- Legood S, Boneca IG, Buddelmeijer N. *Mode of action of lipoprotein modification enzymes—novel antibacterial targets.* 2021. **PMID 32979868** — essentiality; HTS assays.
- Smithers L, ... Caffrey M, et al. *Structure snapshots reveal the mechanism of a bacterial membrane lipoprotein N-acyltransferase.* 2023. **PMID 37390210** — mechanistic intermediates.
- McClain MS, Voss BJ, Cover TL. *Lipoprotein Processing and Sorting in Helicobacter pylori.* 2020. **PMID 32430470** — diderm processing/sorting context.
- Buddelmeijer N. *N-acylation of lipoproteins: not when sour.* 2012. **PMID 22467782** — physiological modulation of N-acylation.
- (Lol pathway context) LolB γ‑proteobacteria restriction. **PMID 39149330**.

---

*Scope note:* This review treats the **proteobacterial, Lnt-dependent** N‑acylation module (UPA00666) as the core system, with *P. putida* KT2440 Lnt (PP_4790/Q88DN4) as the focal ortholog. Claims specific to KT2440 are, at present, inferences from close relatives (*P. aeruginosa*, *E. coli*) rather than direct measurements, and are flagged as such throughout.


## Artifacts

- [OpenScientist final report](apolipoprotein_n_acyltransferase-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](apolipoprotein_n_acyltransferase-deep-research-openscientist_artifacts/final_report.pdf)