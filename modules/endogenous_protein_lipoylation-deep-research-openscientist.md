---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:50:37.348275'
end_time: '2026-09-01T11:11:14.080092'
duration_seconds: 1236.73
template_file: templates/module_research.md.j2
template_variables:
  module_title: Endogenous protein lipoylation
  module_summary: 'Endogenous protein lipoylation builds a lipoyl cofactor directly
    on conserved lysine residues in lipoyl domains. All characterized routes transfer
    an octanoyl group from octanoyl-acyl carrier protein to a protein carrier and
    use a radical-SAM lipoate synthase to insert sulfur atoms at C6 and C8. The topology
    varies by lineage: some organisms modify client lipoyl domains directly, whereas
    others use GcvH as an obligatory relay carrier and an amidotransferase to deliver
    the modified acyl group to client proteins. This module models the direct bacterial
    route, the characterized Bacillus relay, and the characterized human mitochondrial
    relay as alternatives. Exogenous lipoate salvage by ATP-dependent lipoate-protein
    ligases and the downstream lipoate-dependent enzyme complexes are outside the
    boundary.'
  module_outline: "- Endogenous protein lipoylation\n  - Alternative versions by route\
    \ topology and lineage: Endogenous protein-lipoylation topologies\n    - Direct\
    \ LipB-LipA route\n      - 1. direct octanoyl transfer from acyl carrier protein\
    \ to a client lipoyl domain\n      - Direct octanoylation of a client lipoyl domain\n\
    \        - LipB-family octanoyltransferase (molecular player: LipB family octanoyltransferases;\
    \ activity or role: lipoyl(octanoyl) transferase activity)\n      - 2. sulfur\
    \ insertion into the directly octanoylated client lipoyl domain\n      - Sulfur\
    \ insertion on the client lipoyl domain\n        - LipA-family lipoate synthase\
    \ (molecular player: LipA family lipoate synthases; activity or role: lipoate\
    \ synthase activity)\n    - Bacillus GcvH octanoyl-relay route\n      - 1. octanoyl\
    \ transfer from acyl carrier protein to GcvH\n      - LipM-dependent GcvH octanoylation\n\
    \        - LipM octanoyltransferase (molecular player: Octanoyltransferase LipM\
    \ family; activity or role: GcvH-directed lipoyl(octanoyl) transferase activity)\n\
    \      - 2. transfer of octanoyl from GcvH to client E2 lipoyl domains\n     \
    \ - LipL-dependent octanoyl relay to E2\n        - LipL octanoyl-GcvH amidotransferase\
    \ (molecular player: Octanoyltransferase LipL family; activity or role: octanoyl-GcvH:protein\
    \ amidotransferase activity)\n      - 3. sulfur insertion into octanoylated client\
    \ E2 lipoyl domains\n      - LipA sulfur insertion on client E2\n        - Bacillus\
    \ LipA lipoate synthase (molecular player: LipA family lipoate synthases; activity\
    \ or role: lipoate synthase activity)\n    - Human mitochondrial GCSH lipoyl-relay\
    \ route\n      - 1. octanoyl transfer from mitochondrial acyl carrier protein\
    \ to GCSH\n      - LIPT2-dependent GCSH octanoylation\n        - LIPT2 octanoyltransferase\
    \ (molecular player: LipB family octanoyltransferases; activity or role: GCSH-directed\
    \ lipoyl(octanoyl) transferase activity)\n      - 2. sulfur insertion into GCSH-bound\
    \ octanoyl\n      - LIAS sulfur insertion on GCSH\n        - LIAS lipoate synthase\
    \ (molecular player: LipA family lipoate synthases; activity or role: lipoate\
    \ synthase activity)\n      - 3. transfer of mature lipoyl from GCSH to client\
    \ E2 lipoyl domains\n      - LIPT1-dependent lipoyl relay to E2\n        - LIPT1\
    \ lipoyl-GCSH amidotransferase (molecular player: Lipoate-protein ligase family;\
    \ activity or role: lipoyl-GCSH:protein amidotransferase activity)"
  module_connections: '- Direct octanoylation of a client lipoyl domain feeds into
    Sulfur insertion on the client lipoyl domain: Direct LipB octanoylation precedes
    LipA sulfur insertion.

    - LipM-dependent GcvH octanoylation feeds into LipL-dependent octanoyl relay to
    E2: GcvH carries octanoyl from LipM to LipL.

    - LipL-dependent octanoyl relay to E2 feeds into LipA sulfur insertion on client
    E2: LipL transfer to E2 precedes LipA sulfur insertion.

    - LIPT2-dependent GCSH octanoylation feeds into LIAS sulfur insertion on GCSH:
    GCSH-bound octanoyl is sulfurated before transfer to E2.

    - LIAS sulfur insertion on GCSH feeds into LIPT1-dependent lipoyl relay to E2:
    Mature lipoyl is relayed from GCSH to client E2 proteins.'
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
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Endogenous protein lipoylation

## Working Scope

Endogenous protein lipoylation builds a lipoyl cofactor directly on conserved lysine residues in lipoyl domains. All characterized routes transfer an octanoyl group from octanoyl-acyl carrier protein to a protein carrier and use a radical-SAM lipoate synthase to insert sulfur atoms at C6 and C8. The topology varies by lineage: some organisms modify client lipoyl domains directly, whereas others use GcvH as an obligatory relay carrier and an amidotransferase to deliver the modified acyl group to client proteins. This module models the direct bacterial route, the characterized Bacillus relay, and the characterized human mitochondrial relay as alternatives. Exogenous lipoate salvage by ATP-dependent lipoate-protein ligases and the downstream lipoate-dependent enzyme complexes are outside the boundary.

## Provisional Biological Outline

- Endogenous protein lipoylation
  - Alternative versions by route topology and lineage: Endogenous protein-lipoylation topologies
    - Direct LipB-LipA route
      - 1. direct octanoyl transfer from acyl carrier protein to a client lipoyl domain
      - Direct octanoylation of a client lipoyl domain
        - LipB-family octanoyltransferase (molecular player: LipB family octanoyltransferases; activity or role: lipoyl(octanoyl) transferase activity)
      - 2. sulfur insertion into the directly octanoylated client lipoyl domain
      - Sulfur insertion on the client lipoyl domain
        - LipA-family lipoate synthase (molecular player: LipA family lipoate synthases; activity or role: lipoate synthase activity)
    - Bacillus GcvH octanoyl-relay route
      - 1. octanoyl transfer from acyl carrier protein to GcvH
      - LipM-dependent GcvH octanoylation
        - LipM octanoyltransferase (molecular player: Octanoyltransferase LipM family; activity or role: GcvH-directed lipoyl(octanoyl) transferase activity)
      - 2. transfer of octanoyl from GcvH to client E2 lipoyl domains
      - LipL-dependent octanoyl relay to E2
        - LipL octanoyl-GcvH amidotransferase (molecular player: Octanoyltransferase LipL family; activity or role: octanoyl-GcvH:protein amidotransferase activity)
      - 3. sulfur insertion into octanoylated client E2 lipoyl domains
      - LipA sulfur insertion on client E2
        - Bacillus LipA lipoate synthase (molecular player: LipA family lipoate synthases; activity or role: lipoate synthase activity)
    - Human mitochondrial GCSH lipoyl-relay route
      - 1. octanoyl transfer from mitochondrial acyl carrier protein to GCSH
      - LIPT2-dependent GCSH octanoylation
        - LIPT2 octanoyltransferase (molecular player: LipB family octanoyltransferases; activity or role: GCSH-directed lipoyl(octanoyl) transferase activity)
      - 2. sulfur insertion into GCSH-bound octanoyl
      - LIAS sulfur insertion on GCSH
        - LIAS lipoate synthase (molecular player: LipA family lipoate synthases; activity or role: lipoate synthase activity)
      - 3. transfer of mature lipoyl from GCSH to client E2 lipoyl domains
      - LIPT1-dependent lipoyl relay to E2
        - LIPT1 lipoyl-GCSH amidotransferase (molecular player: Lipoate-protein ligase family; activity or role: lipoyl-GCSH:protein amidotransferase activity)

## Known Relationships Among Steps

- Direct octanoylation of a client lipoyl domain feeds into Sulfur insertion on the client lipoyl domain: Direct LipB octanoylation precedes LipA sulfur insertion.
- LipM-dependent GcvH octanoylation feeds into LipL-dependent octanoyl relay to E2: GcvH carries octanoyl from LipM to LipL.
- LipL-dependent octanoyl relay to E2 feeds into LipA sulfur insertion on client E2: LipL transfer to E2 precedes LipA sulfur insertion.
- LIPT2-dependent GCSH octanoylation feeds into LIAS sulfur insertion on GCSH: GCSH-bound octanoyl is sulfurated before transfer to E2.
- LIAS sulfur insertion on GCSH feeds into LIPT1-dependent lipoyl relay to E2: Mature lipoyl is relayed from GCSH to client E2 proteins.

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

# Endogenous Protein Lipoylation: How Cells Build a Sulfur-Containing Cofactor Directly on Their Enzymes

*A review-style synthesis. Citations are given as PubMed IDs (PMID), linked to PubMed.*

---

## 1. Executive Summary

Lipoic acid (6,8-dithiooctanoic acid) is an essential redox cofactor for a small set of central-metabolism multienzyme complexes: the 2-oxoacid dehydrogenases (pyruvate dehydrogenase, PDH; 2-oxoglutarate/α-ketoglutarate dehydrogenase, OGDH/α-KGDH; branched-chain ketoacid dehydrogenase, BCKDH; 2-oxoadipate dehydrogenase) and the glycine cleavage system (GCS). Unlike almost every other cofactor, lipoate is **not synthesized as a free molecule and then attached**; instead it is **assembled in place, atom by atom, on a specific lysine of its cognate protein** ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)). This defines the biological system reviewed here — *endogenous protein lipoylation* — and separates it cleanly from exogenous lipoate salvage by ATP-dependent lipoate-protein ligases (LplA-type), which is a distinct, parallel system explicitly excluded from this scope.

Two chemical operations are universal and obligatory: (i) transfer of an **octanoyl group from octanoyl–acyl carrier protein (octanoyl-ACP)**, diverted from type-II/mitochondrial fatty acid synthesis, onto a protein acceptor; and (ii) **radical-SAM sulfur insertion at C6 and C8** by lipoyl synthase (LipA/LIAS), which sacrifices one of its own iron–sulfur clusters as the sulfur source ([PMID: 27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/); [PMID: 25100160](https://pubmed.ncbi.nlm.nih.gov/25100160/)). What varies across life is the **topology** of step (i): some lineages octanoylate the client lipoyl domain directly (the *E. coli* LipB→LipA route), whereas others octanoylate the glycine-cleavage H-protein (GcvH/GCSH) first and use an amidotransferase to relay the modified group to client E2 domains (the *Bacillus subtilis* LipM/LipL and human LIPT2/LIAS/LIPT1 relays). The relay routes differ in a crucial detail: in *Bacillus* the **octanoyl** group is relayed to E2 and sulfur is inserted last, whereas in humans sulfur is inserted on **GCSH** first and the **mature lipoyl** group is relayed ([PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/); [PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/)).

The system is ancient, essential, and modular. Its parts have been reshuffled by extensive horizontal gene transfer, gene fusion, and loss, producing unexpected combinations — including a recently characterized bacterial route that splits sulfur insertion across two radical-SAM proteins (LipS1/LipS2) ([PMID: 37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/)). Failures of the human pathway cause severe, often lethal neonatal mitochondrial encephalopathies ([PMID: 24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/); [PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/)), and lipoylated proteins are the direct targets of copper-induced cell death (cuproptosis), linking this biosynthetic module to contemporary disease biology.

---

## 2. Definition and Biological Boundaries

**What is included.** Endogenous protein lipoylation comprises the enzymatic steps that build the lipoyl cofactor *de novo* on an apo lipoyl domain, starting from octanoyl-ACP:

1. **Octanoyl transfer** from octanoyl-ACP to a protein acceptor (a client E2/H lipoyl domain directly, or GcvH/GCSH as a relay carrier).
2. **Amidotransfer/relay** of the (octanoyl or lipoyl) group from the carrier to client lipoyl domains, in relay topologies only.
3. **Sulfur insertion** at C6 and C8 by a radical-SAM lipoyl synthase.

The product is a lipoyllysine amide on a conserved lysine within a ~80-residue lipoyl domain that acts as a swinging arm during catalysis.

**What lies just outside the boundary (and is frequently conflated).**

- **Exogenous lipoate/octanoate salvage.** ATP-dependent lipoate-protein ligases (*E. coli* LplA; *B. subtilis* LplJ; human LIPT1 acting in a salvage-like transfer; *Plasmodium* LplA1/LplA2) attach *pre-formed* lipoate scavenged from the environment or from other proteins. This is mechanistically distinct (adenylation chemistry, no sulfur insertion) and is a common source of confusion because several enzymes are annotated as "lipoate ligases" yet actually catalyze octanoyltransfer in biosynthesis (e.g., *B. subtilis* LipM) ([PMID: 20882995](https://pubmed.ncbi.nlm.nih.gov/20882995/)). Salvage can mask biosynthetic phenotypes (e.g., *Plasmodium* LipB is dispensable in blood stages because a salvage ligase compensates) ([PMID: 18069893](https://pubmed.ncbi.nlm.nih.gov/18069893/)).
- **Upstream fatty-acid synthesis.** FAS II / mitochondrial FAS (mtFAS) produces the octanoyl-ACP feedstock. It is the dedicated, non-substitutable supplier but is not part of the lipoylation module proper ([PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/); [PMID: 31473256](https://pubmed.ncbi.nlm.nih.gov/31473256/)).
- **Iron–sulfur cluster biogenesis.** LipA/LIAS consumes and must regenerate an auxiliary [4Fe-4S] cluster; the ISC machinery and carriers (NfuA, IscU) are enabling partners, not lipoylation enzymes ([PMID: 30097094](https://pubmed.ncbi.nlm.nih.gov/30097094/)).
- **Downstream lipoate-dependent enzymology and its consequences.** The catalytic use of lipoate by PDH/OGDH/BCKDH/GCS, the reoxidation of dihydrolipoate by dihydrolipoyl dehydrogenase (DLD/E3), and copper-dependent cell death (cuproptosis) targeting lipoylated proteins are outcomes of lipoylation, not steps within it.

**Competing definitions.** Some literature uses "lipoic acid metabolism" as an umbrella covering biosynthesis *and* salvage; others reserve "lipoate biosynthesis" for the two-enzyme *E. coli* paradigm and treat the relay as an "assembly" pathway. Because the enzymes are annotated inconsistently — the PF03099 cofactor-transferase family contains octanoyltransferases, amidotransferases, and ligases that are hard to tell apart by sequence ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)) — functional assignment must rest on biochemistry, not annotation.

---

## 3. Mechanistic Overview

### 3.1 The two invariant chemical operations (Finding F001)

**Octanoyl transfer.** LipB-family and LplA-like (LipM) octanoyltransferases use a **thioester-linked acyl-enzyme intermediate**: the octanoyl group is transferred from octanoyl-ACP onto an active-site cysteine (e.g., LipM Cys150) and then onto the ε-amino group of the target lysine, forming an amide. The primary literature states this directly: *"LipB transfers the octanoyl moiety from octanoyl-acyl carrier protein to the lipoyl domains of the 2-oxoacid dehydrogenases via a thioester-linked octanoyl-LipB intermediate. The octanoylated dehydrogenase is then converted to the enzymatically active lipoylated species by insertion of two sulfur atoms into the octanoyl moiety by the S-adenosyl-L-methionine radical enzyme, LipA"* ([PMID: 20882995](https://pubmed.ncbi.nlm.nih.gov/20882995/)). This is a group-transfer reaction with no net redox change and no ATP requirement (contrast salvage ligases, which adenylate lipoate). The defining conceptual feature of the whole system is that *"the cofactor is assembled on its cognate proteins rather than being assembled and subsequently attached as in the typical pathway, like that of biotin attachment"* ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)).

**Sulfur insertion (Finding F002).** Lipoyl synthase (LipA in bacteria; LIAS in humans) is a radical S-adenosylmethionine (SAM) enzyme with **two [4Fe-4S] clusters**: a canonical radical-SAM cluster that reductively cleaves SAM to generate 5′-deoxyadenosyl radicals (which abstract hydrogen atoms from the unactivated C6 and C8 of the octanoyl chain), and an **auxiliary cluster**, *"bound by a CX4CX5C motif unique to lipoyl synthase. The fourth ligand to the auxiliary cluster is an extremely unusual serine residue,"* and site-directed mutants show *"this conserved serine ligand is essential for the sulfur insertion steps"* ([PMID: 25100160](https://pubmed.ncbi.nlm.nih.gov/25100160/)). Crystallographic snapshots of a turnover intermediate from *M. tuberculosis* LipA directly visualize the auxiliary cluster being dismantled: *"the serine ligand dissociates from the cluster, the iron ion is lost, and a sulfur atom that is still part of the cluster becomes covalently attached to C6 of the octanoyl substrate. This intermediate structure provides a clear picture of iron-sulfur cluster destruction in action, supporting the role of the auxiliary cluster as the sulfur source"* ([PMID: 27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/)). Because the cluster is consumed, sustained turnover requires cluster regeneration — *"Escherichia coli proteins NfuA or IscU can confer catalytic properties to E. coli LipA in vitro"* ([PMID: 30097094](https://pubmed.ncbi.nlm.nih.gov/30097094/)).

### 3.2 The three modeled topologies (Finding F003)

**(A) Direct LipB→LipA route (E. coli, plants, plastids).** LipB octanoylates the client lipoyl domain directly; LipA then sulfurates it. Only two enzymes are required — the minimal pathway ([PMID: 20882995](https://pubmed.ncbi.nlm.nih.gov/20882995/); [PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)).

**(B) Bacillus GcvH octanoyl-relay (Gram-positive bacteria).** Four proteins:
1. **LipM** octanoylates **GcvH** (not the client); notably, *"B. subtilis encodes an octanoyltransferase that has virtually no sequence resemblance to E. coli LipB but instead has a sequence that resembles that of the E. coli lipoate ligase, LplA"* ([PMID: 20882995](https://pubmed.ncbi.nlm.nih.gov/20882995/));
2. **LipL** amidotransfers the **octanoyl** group from octanoyl-GcvH to client E2 lipoyl domains — *"LipL, transfers octanoate from octanoyl-GCV to other LDs in an amido-transfer reaction"* ([PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/));
3. **LipA** inserts sulfur on the E2-bound octanoyl chain.

Deletion of either gene abolishes lipoate synthesis despite an intact LipA: *"B. subtilis ΔlipL strains are unable to synthesize lipoic acid despite the presence of LipM and the sulphur insertion enzyme, LipA, which should suffice for lipoic acid biosynthesis based on the E. coli model"* ([PMID: 21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/)).

**(C) Human mitochondrial GCSH lipoyl-relay.** Three lipoate-specific enzymes: *"Mitochondrial lipoate synthesis involves three enzymatic steps catalyzed sequentially by lipoyl(octanoyl) transferase 2 (LIPT2), lipoic acid synthetase (LIAS), and lipoyltransferase 1 (LIPT1)"* ([PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/)):
1. **LIPT2** octanoylates **GCSH** (the human GcvH);
2. **LIAS** inserts sulfur on GCSH-bound octanoyl, producing **mature lipoyl-GCSH**;
3. **LIPT1** transfers the **mature lipoyl** group from GCSH to client E2 domains.

**Key ordering distinction.** In route (B) the relay moves an *octanoyl* group and sulfur insertion is the last step (on E2); in route (C) sulfur insertion precedes the relay, which moves a *fully mature lipoyl* group. This is a genuine mechanistic difference, not a notational one, supported by the enzymology (LipL transfers octanoate) and by human genetics (LIPT1 loss spares the GCS; see §6).

### 3.3 Obligatory vs. conditional vs. accessory steps

- **Obligatory (all routes):** octanoyl transfer from octanoyl-ACP; radical-SAM sulfur insertion. No route bypasses either.
- **Conditional (relay lineages only):** GcvH/GCSH octanoylation and the LipL/LIPT1 amidotransfer. These are dispensable in direct-route organisms but strictly required where the client-directed octanoyltransferase is absent.
- **Accessory/enabling:** octanoyl-ACP supply (FAS II/mtFAS); auxiliary-cluster regeneration (NfuA/IscU); DLD/E3 recycling of dihydrolipoate (downstream).

---

## 4. Major Molecular Players and Active Assemblies

| Player | Family / fold | Reaction in endogenous lipoylation | Notes |
|---|---|---|---|
| **LipB** | Cofactor transferase PF03099 (LipB subtype) | Octanoyl-ACP → client lipoyl-domain Lys | Minimal direct route; Cys-thioester intermediate [20882995] |
| **LipM** | PF03099, **LplA-like** | Octanoyl-ACP → **GcvH** | Annotated as "ligase" but is an octanoyltransferase; Cys150 nucleophile [20882995] |
| **LipL** | PF03099 (amidotransferase) | Octanoyl-**GcvH** → client E2 (amidotransfer) | Obligatory relay; also required in scavenging [21338420, 23960015, 31066113] |
| **LIPT2** | LipB-family | Octanoyl-(mt)ACP → **GCSH** | Human GcvH-directed octanoyltransferase [28757203] |
| **LIPT1** | Lipoate-protein ligase family | Lipoyl-**GCSH** → client E2 | Relays *mature* lipoyl; also salvage-competent [24777537, 33487163] |
| **LipA / LIAS** | Radical-SAM, two [4Fe-4S] | Sulfur insertion at C6, C8 | Auxiliary cluster = sacrificial S donor; unique Ser ligand [25100160, 27506792] |
| **LipS1 + LipS2** | Two radical-SAM proteins | Split sulfur insertion (LipA-independent lineages) | Newly characterized bipartite synthase [37368881] |
| **GcvH / GCSH** | Glycine-cleavage H-protein (lipoyl-domain fold) | Obligatory acyl/lipoyl **relay carrier** | Central hub; moonlights beyond its GCS role [31066113] |
| **octanoyl-ACP** | ACP + 4′-phosphopantetheine | Committed acyl donor | From FAS II / mtFAS [20226757, 31473256] |
| **NfuA / IscU** | Fe–S carriers | Regenerate LipA auxiliary cluster | Enabling, not core [30097094] |

**Active assemblies.** The functional "reaction unit" is an enzyme paired with a **lipoyl-domain-fold substrate** (client E2/BCKDH/OGDH domains, or GcvH/GCSH). Substrate recognition is domain-based and specific: relay carriers and clients present near-identical folds, which is precisely why an amidotransferase (LipL/LIPT1) can move a group between them, and why salvage ligases with strict subunit specificity cannot substitute for the relay (Finding F007). As shown in *B. subtilis*, *"a ∆lipL mutant, in which the endogenous lipoylation pathway of E2 subunits is blocked, showed growth defects in minimal media even when supplemented with lipoate and despite the presence of a functional LplJ,"* because *"the crucial role of LipL during lipoate utilization relies on the strict substrate specificity of LplJ, determined by charge complementarity between the ligase and the lipoylable subunits"* ([PMID: 31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/)).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Across lineages (Finding F004)

- **Direct route:** *E. coli* and most Gram-negative bacteria; **plants** use the *E. coli*-type LipB/LipA logic in plastids and mitochondria ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/); [PMID: 32111914](https://pubmed.ncbi.nlm.nih.gov/32111914/)).
- **Relay route:** *Bacillus subtilis*, *Staphylococcus aureus* and other Gram-positives (LipM/LipL/GcvH) ([PMID: 21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/); [PMID: 31451544](https://pubmed.ncbi.nlm.nih.gov/31451544/)); **fungi and mammals** use a *B. subtilis*-type relay through the H-protein (GCSH/Gcv3) ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/); [PMID: 33487163](https://pubmed.ncbi.nlm.nih.gov/33487163/)).
- **Bipartite-synthase route:** some bacteria/archaea use *"a novel lipoate assembly pathway in bacteria based on a sLpl(AB) lipoate:protein ligase, which attaches octanoate or lipoate to apo-proteins, and 2 radical SAM proteins, LipS1 and LipS2, which work together as lipoyl synthase and insert 2 sulfur atoms"* ([PMID: 37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/)) — showing even the "invariant" sulfur-insertion chemistry can be partitioned.

The transferases (all except sulfur-insertion enzymes) belong to *"PFAM family PF03099 (the cofactor transferase family). Although these enzymes share some sequence similarity, they catalyze three markedly distinct enzyme reactions"* ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)). Their phylogenetic distribution *"in the 2 prokaryotic domains was shaped by a complex network of horizontal gene transfers, acquisition of additional genes, fusions, and losses"* ([PMID: 37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/)), making the pathway a mix-and-match assembly of interchangeable modules.

### 5.2 Across compartments and life stages (Finding F006)

Apicomplexan parasites are the clearest example of *compartment-determined* topology. *Plasmodium* runs de novo biosynthesis exclusively in the apicoplast: *"LA biosynthesis, comprising octanoyl-acyl carrier protein (ACP): protein N-octanoyltransferase (LipB) and lipoate synthase (LipA), is exclusively found in the apicoplast of Plasmodium where it generates LA de novo from octanoyl-ACP, provided by the type II fatty acid biosynthesis (FAS II) pathway"* ([PMID: 22607141](https://pubmed.ncbi.nlm.nih.gov/22607141/)), while running salvage in the mitochondrion (LplA1; dual-targeted LplA2) — spatially and functionally separate systems.

Their essentiality is **stage-specific**. Apicoplast LipB is dispensable in blood stages: *"disruption of the LipB gene did not negatively affect parasite growth despite a drastic loss of LA (>90%). Surprisingly, the sole, apicoplast-located pyruvate dehydrogenase still showed lipoylation, suggesting that an alternative lipoylation pathway exists"* ([PMID: 18069893](https://pubmed.ncbi.nlm.nih.gov/18069893/)). Yet de novo synthesis is critical for liver-stage maturation: *"sporozoites lacking the apicoplast lipoic acid protein ligase LipB are markedly attenuated in their infectivity for mice, and in vitro studies document a very late liver stage arrest"* ([PMID: 23490300](https://pubmed.ncbi.nlm.nih.gov/23490300/)).

### 5.3 Across physiological states (Finding F008)

Because octanoyl-ACP is the committed feedstock, lipoylation is coupled to fatty-acid/acetyl-CoA flux and to respiratory state. In yeast, *"defects in mitochondrial FAS... result in... loss of cellular lipoic acid"* that cannot be rescued by exogenous fatty acids ([PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/)). Moreover, *"octanoyl-ACP provides the C8 backbone for endogenous lipoic acid synthesis. Accumulating evidence suggests that mtFAS-generated acyl-ACPs act as signaling molecules in an intramitochondrial metabolic state sensing circuit, coordinating mitochondrial acetyl-CoA levels with mitochondrial respiration, Fe-S cluster biogenesis and protein lipoylation"* ([PMID: 31473256](https://pubmed.ncbi.nlm.nih.gov/31473256/)). Downstream, lipoylation status governs susceptibility to **cuproptosis**, a copper-dependent regulated cell death in which *"copper binds lipoylated mitochondrial proteins, promotes aggregation of tricarboxylic acid cycle components, destabilizes iron-sulfur cluster proteins, and elicits FDX1- and protein lipoylation-dependent proteotoxic stress"* ([PMID: 42653078](https://pubmed.ncbi.nlm.nih.gov/42653078/)) — a physiologically and therapeutically important consequence of the pathway's output.

---

## 6. Constraints, Dependencies, and Failure Modes

**Mandatory ordering.**
- Octanoylation **must precede** sulfur insertion everywhere — LipA/LIAS act only on an octanoyl chain already amide-linked to a lysine, never on free octanoate.
- In relay routes, GcvH/GCSH octanoylation **precedes** the amidotransfer to E2.
- The **relative order of sulfur insertion and relay differs by lineage** (Bacillus: relay octanoyl → sulfurate on E2 [PMID: 23960015]; human: sulfurate on GCSH → relay mature lipoyl [PMID: 28757203]).

**Substrate/compartment constraints.**
- The acyl donor must be **octanoyl-ACP**; free octanoate or dietary lipoate cannot feed the de novo route (mtFAS loss abolishes cellular lipoate and is not rescued by exogenous fatty acids) ([PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/)).
- In relay lineages, the client E2 subunits can **only** be modified via the GcvH/GCSH relay; the salvage ligase's strict subunit specificity rules out a direct ligase-to-E2 shortcut (*B. subtilis* ΔlipL fails even with lipoate + functional LplJ) ([PMID: 31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/)).
- LipA/LIAS depends on Fe–S cluster supply/repair; iron or ISC deficiency phenocopies lipoylation failure ([PMID: 30097094](https://pubmed.ncbi.nlm.nih.gov/30097094/)).

**Human failure modes — which independently validate pathway order (Finding F005).**

| Gene | Step | Biochemical signature | GCS status |
|---|---|---|---|
| **LIPT2** | GCSH octanoylation | ↓ PDHc, ↓ α-KGDHc, ↓ protein lipoylation, mild ↑ glycine; rescued by WT LIPT2 | affected |
| **LIAS** | Sulfur insertion on GCSH | NKH-like early convulsions + mitochondrial energy defect | affected |
| **LIPT1** | Lipoyl relay to E2 | Combined 2-oxoacid dehydrogenase deficiency, Leigh-like | **spared** |

For LIPT2, *"affected individuals' fibroblasts showed reduced oxygen consumption rates, PDHc, α-KGDHc activities, leucine catabolic flux, and decreased protein lipoylation. A normalization of lipoylation was observed after expression of wild-type LIPT2"* ([PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/)). The decisive genetic evidence for step order is that *"LIPT1 deficiency spares the GCS, and resulted in a combined 2-oxoacid dehydrogenase deficiency"* ([PMID: 24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/)). Because GCSH is lipoylated *upstream* of LIPT1, loss of LIPT1 leaves a functional H-protein (intact GCS) while starving E2 clients — exactly the pattern predicted by the "sulfur-first, relay-last" human topology, and not by any alternative ordering.

---

## 7. Mechanistic Model / Interpretation

The system is best understood as a **conserved two-reaction core** wrapped in a **variable delivery topology**. The core chemistry is fixed because both operations are hard problems evolution solved once: capturing a thioester-activated C8 chain onto a specific lysine, and functionalizing two inert C–H bonds with sulfur using a consumable Fe–S cluster. Everything else — whether a relay carrier is used, whether sulfur is inserted before or after relay, whether the pathway runs in an apicoplast or a mitochondrion — is a modular arrangement of interchangeable PF03099 transferases plus a radical-SAM synthase.

```
                 ┌─────────────────── CONSERVED CORE ───────────────────┐
 octanoyl-ACP ──▶│ octanoyltransfer (thioester acyl-enzyme intermediate) │──▶ radical-SAM ──▶ lipoyl-protein
 (from FAS II /  │                                                        │   sulfur insertion
  mtFAS)         └──────────────────────────────────────────────────────┘   (sacrificial aux [4Fe-4S])

   VARIABLE TOPOLOGY:
   • Direct:   transfer & sulfur both on E2 client            (E. coli, plants)        [2 enzymes]
   • Relay-A:  transfer→GcvH, relay octanoyl→E2, sulfur on E2  (Bacillus: LipM/LipL/LipA) [4 proteins]
   • Relay-B:  transfer→GCSH, sulfur on GCSH, relay lipoyl→E2  (human: LIPT2/LIAS/LIPT1)  [3 enzymes]
   • Split-S:  sLplAB ligase + LipS1 + LipS2 for sulfur       (novel bacterial route)
```

This modular view explains the pathway's patchy, HGT-driven phylogenetic distribution and its clinical logic in one framework: perturbing the core (LIAS, mtFAS) is globally catastrophic, whereas perturbing a topology-specific relay component (LIPT1, LipL) produces a more selective, **position-diagnostic** phenotype (the GCS-sparing signature of LIPT1 deficiency being the clearest example). For understanding the ancestral role of the expanded transferase family, LipB best represents the primitive acyltransfer chemistry, while the LplA-like members (LipM, LipL) represent later relay/ligase specializations; the H-protein-centered relay may be the more ancient "primordial moonlighting" configuration, with the two-enzyme direct route a streamlined derivative.

---

## 8. Evidence Base

| PMID | How it supports / challenges the model |
|---|---|
| [27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/) | Authoritative synthesis: in-situ assembly (vs. biotin); PF03099 shared ancestry with three distinct reactions; lineage distribution. **Supports** F001, F004. |
| [20882995](https://pubmed.ncbi.nlm.nih.gov/20882995/) | E. coli LipB thioester mechanism; LipM is LplA-like, not LipB-like. **Supports** F001, F003. |
| [25100160](https://pubmed.ncbi.nlm.nih.gov/25100160/) | LipA two-cluster architecture; unique CX4CX5C serine ligand essential for sulfur insertion. **Supports** F002. |
| [27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/) | Crystallographic snapshots of auxiliary-cluster destruction and sulfur transfer to C6. **Supports** F002 (settles sacrificial-cluster debate). |
| [26390103](https://pubmed.ncbi.nlm.nih.gov/26390103/) | EPR trapping places substrate radical within bonding distance of cluster iron. **Supports** F002. |
| [30097094](https://pubmed.ncbi.nlm.nih.gov/30097094/) | NfuA/IscU regenerate LipA cluster, enabling turnover. **Supports** F002 (turnover constraint). |
| [21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/) | Bacillus four-protein requirement; ΔlipL cannot synthesize lipoate despite LipA. **Supports** F003, F007. |
| [23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/) | LipL transfers octanoate (amidotransfer), fixing Bacillus step order. **Supports** F008 step-order. |
| [28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/) | Human LIPT2/LIAS/LIPT1 three-step relay; LIPT2 disease rescued by WT. **Supports** F003, F005. |
| [24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/) | LIPT1 deficiency spares GCS → downstream position. **Supports** F005 (relay order). |
| [37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/) | Novel sLplAB–LipS1/LipS2 route; HGT-shaped distribution. **Supports** F004 (modularity). |
| [22607141](https://pubmed.ncbi.nlm.nih.gov/22607141/) | Plasmodium apicoplast-confined de novo route from FAS II octanoyl-ACP. **Supports** F006. |
| [18069893](https://pubmed.ncbi.nlm.nih.gov/18069893/) | LipB dispensable in blood stages (salvage redundancy). **Supports** F006 (partitioning). |
| [23490300](https://pubmed.ncbi.nlm.nih.gov/23490300/) | De novo route essential in liver stage. **Supports** F006 (stage specificity). |
| [31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/) | LipL/GcvH bottleneck required even during salvage; LplJ charge-complementarity constraint. **Supports** F007. |
| [31451544](https://pubmed.ncbi.nlm.nih.gov/31451544/) | Dynamic GcvH relay in S. aureus. **Supports** F007 (generality). |
| [20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/) | mtFAS is non-bypassable source of octanoyl-ACP. **Supports** F008. |
| [31473256](https://pubmed.ncbi.nlm.nih.gov/31473256/) | Octanoyl-ACP feedstock; acyl-ACP metabolic-state sensing. **Supports** F008. |
| [33487163](https://pubmed.ncbi.nlm.nih.gov/33487163/) | Yeast lipoylation genetics; substrate flexibility; engineered bypass with activating enzymes. **Nuances** F008 constraint. |
| [42653078](https://pubmed.ncbi.nlm.nih.gov/42653078/) | Cuproptosis targets lipoylated proteins (downstream relevance). **Contextualizes** output. |

---

## 9. Controversies and Open Questions

1. **The sacrificial-cluster model — largely settled, historically contested.** The idea that LipA destroys its auxiliary cluster each turnover was initially controversial (an enzyme that consumes part of itself). Crystallographic and spectroscopic evidence now strongly support it ([PMID: 27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/); [PMID: 26390103](https://pubmed.ncbi.nlm.nih.gov/26390103/); [PMID: 25100160](https://pubmed.ncbi.nlm.nih.gov/25100160/)), but the *in vivo* stoichiometry and the exact identity/kinetics of the physiological cluster-regeneration system across organisms remain incompletely defined ([PMID: 30097094](https://pubmed.ncbi.nlm.nih.gov/30097094/)).

2. **Exact acyl species and order in relay routes.** The Bacillus de novo route relays **octanoate** with sulfur inserted last ([PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/)), whereas the human route sulfurates GCSH first and relays **lipoate** ([PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/)). Whether some organisms are flexible (LipA able to act on either GcvH-bound or E2-bound octanoyl) is not fully resolved, and abstracts sometimes describe steps loosely, which can mislead cross-organism comparison.

3. **Annotation vs. function.** Many PF03099 members are misannotated as "lipoate ligases" when they are octanoyltransferases or amidotransferases; conversely LIPT1 is a genuine ligase-family member that acts as a relay amidotransferase. Functional inference from sequence alone is unreliable ([PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/)).

4. **Depth of origin and the ancestral state.** The transferases share the PF03099 fold and were distributed by extensive HGT, fusion, and loss ([PMID: 37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/)), making a simple linear evolutionary narrative untenable. The bipartite LipS1/LipS2 synthase shows the sulfur-insertion step is also evolutionarily labile.

5. **Regulation.** How lipoylation flux is regulated beyond substrate supply (mtFAS/mtACP sensing [PMID: 31473256]) — demand-driven control, turnover of lipoylated proteins, and tissue/developmental differences in mammals — is largely unmapped.

6. **Extrapolation risk.** Much mechanism is drawn from *E. coli*, *B. subtilis*, *M. tuberculosis* LipA structures, and yeast genetics; direct structural/biochemical data on the *human* LIPT2/LIAS/LIPT1 enzymes are comparatively thin, and inferences about human ordering rest substantially on patient biochemistry and heterologous complementation ([PMID: 33487163](https://pubmed.ncbi.nlm.nih.gov/33487163/)). Claims should not be generalized across these systems without care.

---

## 10. Limitations and Knowledge Gaps

- **No primary experimental data were generated** in this investigation; the synthesis is literature-based, drawing on 35 papers and 8 confirmed findings. Conclusions inherit the limitations of the underlying studies.
- **Uneven organism coverage.** Mechanistic depth is greatest for *E. coli*, *B. subtilis*, yeast, and human; archaeal and many bacterial lineages are represented mainly by phylogenomics ([PMID: 37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/)) rather than biochemistry.
- **Structural coverage is partial.** LipA has excellent structural data; the human relay transferases (LIPT2, LIPT1) and the amidotransfer transition states are less well resolved.
- **In vivo regulation** of the acyl-ACP metabolic-sensing circuit is still largely a model ([PMID: 31473256](https://pubmed.ncbi.nlm.nih.gov/31473256/)).

---

## 11. Proposed Follow-up Experiments / Actions

1. **Direct kinetic reconstitution of the human relay** with purified LIPT2, LIAS (+ Fe–S regeneration), LIPT1, GCSH, and E2 lipoyl domains to confirm the sulfur-first order and measure step commitment, rather than inferring it from disease genetics.
2. **Define the sLplAB–LipS1/LipS2 mechanism**: determine which radical-SAM protein donates which sulfur (C6 vs C8), whether they act processively, and reconstruct ancestral vs derived status by ancestral-sequence reconstruction.
3. **Test therapeutic bypass** of human mtFAS/lipoylation disorders using mitochondrially targeted octanoate/lipoate-activating enzymes, extending the yeast proof-of-concept ([PMID: 33487163](https://pubmed.ncbi.nlm.nih.gov/33487163/)) to patient-derived fibroblasts.
4. **Map lipoylation–cuproptosis coupling** by titrating LIPT2/LIAS/LIPT1 activity and quantifying DLAT lipoylation vs copper-induced death, to test whether endogenous lipoylation flux is a cuproptosis vulnerability biomarker.
5. **Systematic Fe–S regeneration dependency**: measure lipoylation flux as a function of NfuA/IscU (and mammalian NFU1/ISCU) availability to quantify the turnover constraint in vivo.
6. **Structural biology of the amidotransfer step**: solve LipL–GcvH and LIPT1–GCSH complex structures to understand how relay carrier and client E2 are discriminated.

---

## 12. Key References

- Cronan JE. *Assembly of Lipoic Acid on Its Cognate Enzymes: an Extraordinary and Essential Biosynthetic Pathway.* Microbiol Mol Biol Rev, 2016. **[PMID: 27074917](https://pubmed.ncbi.nlm.nih.gov/27074917/).**
- Christensen QH, Cronan JE. *A new family of octanoyltransferases generally annotated as lipoate protein ligases* (LipM). 2010. **[PMID: 20882995](https://pubmed.ncbi.nlm.nih.gov/20882995/).**
- Martin N, et al. *A novel two-gene requirement for the octanoyltransfer reaction of B. subtilis lipoic acid biosynthesis* (LipL). 2011. **[PMID: 21338420](https://pubmed.ncbi.nlm.nih.gov/21338420/).**
- Hermes FA, Cronan JE. *The S. cerevisiae lipoate protein ligase homologue Lip3.* 2013. **[PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/).**
- Rasetto NB, et al. *Unravelling the lipoyl-relay of exogenous lipoate utilization in B. subtilis.* 2019. **[PMID: 31066113](https://pubmed.ncbi.nlm.nih.gov/31066113/).**
- Teoh WP, et al. *Dynamic Relay of Protein-Bound Lipoic Acid in Staphylococcus aureus.* 2019. **[PMID: 31451544](https://pubmed.ncbi.nlm.nih.gov/31451544/).**
- Harmer JE, et al. *Structures of lipoyl synthase reveal a compact active site for controlling sequential sulfur insertion reactions.* 2014. **[PMID: 25100160](https://pubmed.ncbi.nlm.nih.gov/25100160/).**
- McLaughlin MI, et al. *Crystallographic snapshots of sulfur insertion by lipoyl synthase.* PNAS, 2016. **[PMID: 27506792](https://pubmed.ncbi.nlm.nih.gov/27506792/).**
- Lanz ND, et al. *Characterization of a Radical Intermediate in Lipoyl Cofactor Biosynthesis.* 2015. **[PMID: 26390103](https://pubmed.ncbi.nlm.nih.gov/26390103/).**
- McCarthy EL, Booker SJ. *Iron-Sulfur Cluster Regeneration in E. coli Lipoyl Synthase.* 2018. **[PMID: 30097094](https://pubmed.ncbi.nlm.nih.gov/30097094/).**
- Habarou F, et al. *Biallelic Mutations in LIPT2 Cause a Mitochondrial Lipoylation Defect Associated with Severe Neonatal Encephalopathy.* Am J Hum Genet, 2017. **[PMID: 28757203](https://pubmed.ncbi.nlm.nih.gov/28757203/).**
- Mayr JA, et al. *Lipoic acid biosynthesis defects.* 2014. **[PMID: 24777537](https://pubmed.ncbi.nlm.nih.gov/24777537/).**
- Pietikäinen LP, et al. *Genetic dissection of the mitochondrial lipoylation pathway in yeast.* 2021. **[PMID: 33487163](https://pubmed.ncbi.nlm.nih.gov/33487163/).**
- Tanabe TS, et al. *Identification of a novel lipoic acid biosynthesis pathway reveals the complex evolution of lipoate assembly in prokaryotes* (sLplAB–LipS1/LipS2). 2023. **[PMID: 37368881](https://pubmed.ncbi.nlm.nih.gov/37368881/).**
- Hiltunen JK, et al. *Mitochondrial fatty acid synthesis and respiration.* 2010. **[PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/).**
- Masud AJ, et al. *Mitochondrial ACP at the interface of metabolic state sensing and mitochondrial function.* 2019. **[PMID: 31473256](https://pubmed.ncbi.nlm.nih.gov/31473256/).**
- Storm J, Müller S. *Lipoic acid metabolism of Plasmodium — a suitable drug target.* 2012. **[PMID: 22607141](https://pubmed.ncbi.nlm.nih.gov/22607141/).**
- Günther S, et al. *Apicoplast lipoic acid protein ligase B is not essential for P. falciparum.* 2007. **[PMID: 18069893](https://pubmed.ncbi.nlm.nih.gov/18069893/).**
- Falkard B, et al. *A key role for lipoic acid synthesis during Plasmodium liver stage development.* 2013. **[PMID: 23490300](https://pubmed.ncbi.nlm.nih.gov/23490300/).**
- Deschermeier C, et al. *Knockout studies reveal an important role of Plasmodium LplA1 for asexual blood stage parasite survival.* 2012. **[PMID: 19434237](https://pubmed.ncbi.nlm.nih.gov/19434237/).**

---

*Prepared as an autonomous literature synthesis of endogenous protein lipoylation. Scope excludes ATP-dependent salvage ligation of free lipoate and the downstream lipoate-dependent enzyme complexes, per the review brief. Uncertainty is flagged in §9–§10; mechanistic ordering claims for the human route rest partly on patient biochemistry and heterologous complementation rather than direct enzymology, and should be interpreted accordingly.*


## Artifacts

- [OpenScientist final report](endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](endogenous_protein_lipoylation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27074917
2. PMID:27506792
3. PMID:25100160
4. PMID:23960015
5. PMID:28757203
6. PMID:37368881
7. PMID:24777537
8. PMID:20882995
9. PMID:18069893
10. PMID:20226757
11. PMID:31473256
12. PMID:30097094
13. PMID:21338420
14. PMID:31066113
15. PMID:32111914
16. PMID:31451544
17. PMID:33487163
18. PMID:22607141
19. PMID:23490300
20. PMID:42653078
21. PMID:26390103
22. PMID:19434237