---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T23:55:50.151786'
end_time: '2026-07-07T00:22:38.978055'
duration_seconds: 1608.83
template_file: templates/module_research.md.j2
template_variables:
  module_title: Ubiquinone biosynthesis
  module_summary: 'A taxon-neutral bacterial ubiquinone biosynthesis module covering
    formation of the benzoquinone head group and its polyprenylated membrane-associated
    intermediates from chorismate-derived 4-hydroxybenzoate. The strict pathway begins
    with UbiC production of 4-hydroxybenzoate, UbiA prenylation, UbiD decarboxylation
    supported by the UbiX-derived prenyl-FMN cofactor, and a series of hydroxylation
    and methylation steps carried out by UbiH-family monooxygenases, Coq7, UbiE, and
    UbiG. KEGG ppu00130 is broader than this strict module: it also includes other
    terpenoid-quinone or side-map entries such as generic NAD(P)H quinone oxidoreductases,
    homogentisate formation, and acyl-CoA thioesterase-like proteins that should not
    by themselves satisfy ubiquinone biosynthesis.'
  module_outline: "- Ubiquinone biosynthesis\n  - 1. 4-hydroxybenzoate precursor formation\n\
    \  - Chorismate to 4-hydroxybenzoate\n    - UbiC chorismate lyase (molecular player:\
    \ PSEPK ubiC; activity or role: chorismate lyase activity)\n  - 2. polyprenyl\
    \ side-chain attachment\n  - 4-hydroxybenzoate polyprenylation\n    - UbiA 4-hydroxybenzoate\
    \ polyprenyltransferase (molecular player: PSEPK ubiA; activity or role: 4-hydroxybenzoate\
    \ polyprenyltransferase activity)\n  - 3. prenyl-FMN cofactor supply for UbiD\n\
    \  - Prenyl-FMN cofactor synthesis\n    - UbiX flavin prenyltransferase (molecular\
    \ player: PSEPK ubiX; activity or role: flavin prenyltransferase activity)\n \
    \ - 4. polyprenyl-hydroxybenzoate decarboxylation\n  - 4-hydroxy-3-polyprenylbenzoate\
    \ decarboxylation\n    - UbiD 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular\
    \ player: PSEPK ubiD; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase\
    \ activity)\n  - 5. first aromatic hydroxylation\n  - 2-polyprenylphenol hydroxylation\n\
    \    - VisC-like 2-polyprenylphenol 6-hydroxylase (molecular player: PSEPK visC;\
    \ activity or role: 2-polyprenylphenol 6-hydroxylase activity)\n  - 6. first O-methylation\n\
    \  - Polyprenyldihydroxybenzene O-methylation\n    - UbiG 2-polyprenyl-6-hydroxyphenol\
    \ methylase (molecular player: PSEPK ubiG; activity or role: 2-polyprenyl-6-hydroxyphenol\
    \ methylase activity)\n  - 7. second aromatic hydroxylation\n  - 2-octaprenyl-6-methoxyphenol\
    \ hydroxylation\n    - UbiH 2-octaprenyl-6-methoxyphenol hydroxylase (molecular\
    \ player: PSEPK ubiH; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase\
    \ activity)\n  - 8. C-methylation of the quinol ring\n  - UbiE C-methylation\n\
    \    - UbiE 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular\
    \ player: PSEPK ubiE; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol\
    \ methyltransferase activity)\n  - 9. demethoxyubiquinol hydroxylation\n  - 3-demethoxyubiquinol\
    \ hydroxylation\n    - Coq7 3-demethoxyubiquinol hydroxylase (molecular player:\
    \ PSEPK coq7; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)\n\
    \  - 10. terminal O-methylation\n  - Demethylubiquinol O-methylation\n    - UbiG\
    \ 3-demethylubiquinol 3-O-methyltransferase (molecular player: PSEPK ubiG; activity\
    \ or role: 3-demethylubiquinol 3-O-methyltransferase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: ubiquinone_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: ubiquinone_biosynthesis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Ubiquinone biosynthesis

## Working Scope

A taxon-neutral bacterial ubiquinone biosynthesis module covering formation of the benzoquinone head group and its polyprenylated membrane-associated intermediates from chorismate-derived 4-hydroxybenzoate. The strict pathway begins with UbiC production of 4-hydroxybenzoate, UbiA prenylation, UbiD decarboxylation supported by the UbiX-derived prenyl-FMN cofactor, and a series of hydroxylation and methylation steps carried out by UbiH-family monooxygenases, Coq7, UbiE, and UbiG. KEGG ppu00130 is broader than this strict module: it also includes other terpenoid-quinone or side-map entries such as generic NAD(P)H quinone oxidoreductases, homogentisate formation, and acyl-CoA thioesterase-like proteins that should not by themselves satisfy ubiquinone biosynthesis.

## Provisional Biological Outline

- Ubiquinone biosynthesis
  - 1. 4-hydroxybenzoate precursor formation
  - Chorismate to 4-hydroxybenzoate
    - UbiC chorismate lyase (molecular player: PSEPK ubiC; activity or role: chorismate lyase activity)
  - 2. polyprenyl side-chain attachment
  - 4-hydroxybenzoate polyprenylation
    - UbiA 4-hydroxybenzoate polyprenyltransferase (molecular player: PSEPK ubiA; activity or role: 4-hydroxybenzoate polyprenyltransferase activity)
  - 3. prenyl-FMN cofactor supply for UbiD
  - Prenyl-FMN cofactor synthesis
    - UbiX flavin prenyltransferase (molecular player: PSEPK ubiX; activity or role: flavin prenyltransferase activity)
  - 4. polyprenyl-hydroxybenzoate decarboxylation
  - 4-hydroxy-3-polyprenylbenzoate decarboxylation
    - UbiD 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular player: PSEPK ubiD; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)
  - 5. first aromatic hydroxylation
  - 2-polyprenylphenol hydroxylation
    - VisC-like 2-polyprenylphenol 6-hydroxylase (molecular player: PSEPK visC; activity or role: 2-polyprenylphenol 6-hydroxylase activity)
  - 6. first O-methylation
  - Polyprenyldihydroxybenzene O-methylation
    - UbiG 2-polyprenyl-6-hydroxyphenol methylase (molecular player: PSEPK ubiG; activity or role: 2-polyprenyl-6-hydroxyphenol methylase activity)
  - 7. second aromatic hydroxylation
  - 2-octaprenyl-6-methoxyphenol hydroxylation
    - UbiH 2-octaprenyl-6-methoxyphenol hydroxylase (molecular player: PSEPK ubiH; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase activity)
  - 8. C-methylation of the quinol ring
  - UbiE C-methylation
    - UbiE 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular player: PSEPK ubiE; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)
  - 9. demethoxyubiquinol hydroxylation
  - 3-demethoxyubiquinol hydroxylation
    - Coq7 3-demethoxyubiquinol hydroxylase (molecular player: PSEPK coq7; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)
  - 10. terminal O-methylation
  - Demethylubiquinol O-methylation
    - UbiG 3-demethylubiquinol 3-O-methyltransferase (molecular player: PSEPK ubiG; activity or role: 3-demethylubiquinol 3-O-methyltransferase activity)

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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Commissioned Review Brief

## Review Topic

Ubiquinone biosynthesis

## Working Scope

A taxon-neutral bacterial ubiquinone biosynthesis module covering formation of the benzoquinone head group and its polyprenylated membrane-associated intermediates from chorismate-derived 4-hydroxybenzoate. The strict pathway begins with UbiC production of 4-hydroxybenzoate, UbiA prenylation, UbiD decarboxylation supported by the UbiX-derived prenyl-FMN cofactor, and a series of hydroxylation and methylation steps carried out by UbiH-family monooxygenases, Coq7, UbiE, and UbiG. KEGG ppu00130 is broader than this strict module: it also includes other terpenoid-quinone or side-map entries such as generic NAD(P)H quinone oxidoreductases, homogentisate formation, and acyl-CoA thioesterase-like proteins that should not by themselves satisfy ubiquinone biosynthesis.

## Provisional Biological Outline

- Ubiquinone biosynthesis
  - 1. 4-hydroxybenzoate precursor formation
  - Chorismate to 4-hydroxybenzoate
    - UbiC chorismate lyase (molecular player: PSEPK ubiC; activity or role: chorismate lyase activity)
  - 2. polyprenyl side-chain attachment
  - 4-hydroxybenzoate polyprenylation
    - UbiA 4-hydroxybenzoate polyprenyltransferase (molecular player: PSEPK ubiA; activity or role: 4-hydroxybenzoate polyprenyltransferase activity)
  - 3. prenyl-FMN cofactor supply for UbiD
  - Prenyl-FMN cofactor synthesis
    - UbiX flavin prenyltransferase (molecular player: PSEPK ubiX; activity or role: flavin prenyltransferase activity)
  - 4. polyprenyl-hydroxybenzoate decarboxylation
  - 4-hydroxy-3-polyprenylbenzoate decarboxylation
    - UbiD 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular player: PSEPK ubiD; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)
  - 5. first aromatic hydroxylation
  - 2-polyprenylphenol hydroxylation
    - VisC-like 2-polyprenylphenol 6-hydroxylase (molecular player: PSEPK visC; activity or role: 2-polyprenylphenol 6-hydroxylase activity)
  - 6. first O-methylation
  - Polyprenyldihydroxybenzene O-methylation
    - UbiG 2-polyprenyl-6-hydroxyphenol methylase (molecular player: PSEPK ubiG; activity or role: 2-polyprenyl-6-hydroxyphenol methylase activity)
  - 7. second aromatic hydroxylation
  - 2-octaprenyl-6-methoxyphenol hydroxylation
    - UbiH 2-octaprenyl-6-methoxyphenol hydroxylase (molecular player: PSEPK ubiH; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase activity)
  - 8. C-methylation of the quinol ring
  - UbiE C-methylation
    - UbiE 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular player: PSEPK ubiE; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)
  - 9. demethoxyubiquinol hydroxylation
  - 3-demethoxyubiquinol hydroxylation
    - Coq7 3-demethoxyubiquinol hydroxylase (molecular player: PSEPK coq7; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)
  - 10. terminal O-methylation
  - Demethylubiquinol O-methylation
    - UbiG 3-demethylubiquinol 3-O-methyltransferase (molecular player: PSEPK ubiG; activity or role: 3-demethylubiquinol 3-O-methyltransferase activity)

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

# Bacterial Ubiquinone Biosynthesis: A Review of the Benzoquinone Head Group Modification Pathway

## 1. Executive Summary

Ubiquinone (coenzyme Q, UQ) is an essential lipid-soluble electron carrier in aerobic respiratory chains and serves additional roles in antioxidant defense and diverse redox processes. In bacteria, its biosynthesis proceeds from the shikimate pathway intermediate chorismate through a strictly defined series of enzymatic modifications to the benzoquinone head group, which is anchored to the cytoplasmic membrane by a polyprenyl side chain. The canonical pathway, best characterized in *Escherichia coli*, requires at minimum twelve gene products (UbiA through UbiK and UbiX), which together catalyze one prenylation, one decarboxylation, three hydroxylations, and three methylations (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 3-4). Recent advances have revealed that this pathway is far more diverse than the *E. coli* model suggests: the three hydroxylation steps can be executed by at least six different flavin monooxygenase (FMO) subfamilies plus the di-iron hydroxylase Coq7, yielding nearly 20 distinct enzyme combinations across proteobacteria (kazemzadeh2023diversificationofubiquinone pages 1-2, abby2020advancesinbacterial pages 4-5). Furthermore, an O₂-independent biosynthetic route employing iron-sulfur cluster-dependent hydroxylases (UbiU, UbiV) and a dedicated accessory factor (UbiT) enables ubiquinone production under anaerobic conditions (pelosi2019ubiquinonebiosynthesisover pages 2-3, ariascartin2023roleofthe pages 1-2). The biosynthetic enzymes assemble into supramolecular complexes—the Ubi metabolon—that overcome the challenge of processing hydrophobic membrane-embedded intermediates (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 4-5). This review synthesizes current mechanistic understanding, evolutionary variation, physical constraints, and unresolved questions in bacterial ubiquinone biosynthesis.

## 2. Definition and Biological Boundaries

### 2.1 What the System Includes

Bacterial ubiquinone biosynthesis, as defined here, encompasses the conversion of chorismate-derived 4-hydroxybenzoate (4-HB) to the fully substituted benzoquinone head group of ubiquinone, together with all polyprenylated membrane-associated intermediates generated during this process. The strict module begins with UbiC-catalyzed production of 4-HB from chorismate and ends with the terminal O-methylation by UbiG to yield ubiquinone (pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 2-3). The polyprenyl diphosphate side chain—synthesized by the separate isoprenoid pathway enzymes IspA and IspB—is attached early in the pathway by UbiA, after which all subsequent intermediates are membrane-associated (abby2020advancesinbacterial pages 2-3).

### 2.2 What Should Be Treated Separately

Several neighboring pathways and processes are often conflated with ubiquinone biosynthesis but should be distinguished:

- **Menaquinone (MK) biosynthesis**: Menaquinones are naphthoquinones with a distinct evolutionary origin and head group structure, despite sharing some homologous prenyltransferases and methyltransferases with the UQ pathway. MK evolved earlier and is present across most bacterial phyla, whereas UQ is restricted to specific proteobacterial classes and eukaryotes (abby2020advancesinbacterial pages 6-7, abby2020advancesinbacterial pages 1-2).

- **Plastoquinone (PQ) biosynthesis**: While plastoquinone is also a benzoquinone, its biosynthetic pathway in cyanobacteria involves different enzymatic components and should not be equated with ubiquinone biosynthesis (abby2020advancesinbacterial pages 8-9).

- **Isoprenoid/mevalonate pathway**: The synthesis of the polyprenyl diphosphate side chain (via the MEP/DOXP pathway in most bacteria or the mevalonate pathway in some organisms) is a precursor-supply pathway, not part of the head group modification module per se (pierrel2022recentadvancesin pages 1-3).

- **Generic KEGG annotations**: The KEGG map ppu00130 (ubiquinone and other terpenoid-quinone biosynthesis) is broader than the strict UQ module. It includes NAD(P)H quinone oxidoreductases, homogentisate formation, and acyl-CoA thioesterase-like proteins that do not constitute ubiquinone biosynthesis.

Notably, the methyltransferase UbiE participates in both CoQ and menaquinone biosynthesis, which can create confusion at pathway boundaries (staiano2023biosynthesisdeficiencyand pages 4-5).

## 3. Mechanistic Overview

The following table provides a comprehensive summary of all enzymatic steps and accessory factors in the canonical bacterial UQ biosynthesis pathway:

| Step number | Enzyme name | Gene (*E. coli*) | Reaction catalyzed | Substrate→Product | Cofactor/cosubstrate | Enzyme family | Notes on variation |
|---|---|---|---|---|---|---|---|
| 1 | Chorismate lyase | **ubiC** | First committed step; cleavage of chorismate to 4-hydroxybenzoate | Chorismate → 4-hydroxybenzoate (4-HB) + pyruvate | None reported | Chorismate lyase | In many bacteria this is the canonical source of the benzenoid precursor; some species use alternative 4-HB-producing enzymes such as XanB2 rather than UbiC, so presence of UQ synthesis does not always imply **ubiC** specifically (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 1-3) |
| 2 | 4-hydroxybenzoate polyprenyltransferase | **ubiA** | Prenylation of 4-HB with the polyprenyl diphosphate side chain | 4-HB + octaprenyl diphosphate → 3-octaprenyl-4-hydroxybenzoate | Polyprenyl diphosphate donor; Mg2+ typically required for UbiA-family prenyltransferases | Membrane UbiA-family aromatic prenyltransferase | Membrane enzyme with all-α-helical fold and lateral portal for long isoprenyl substrates; chain length varies by species (CoQ6, CoQ8, CoQ10, etc.); recently validated as an antibacterial target via competitive/prodrug inhibitor DHB (abby2020advancesinbacterial pages 2-3, bargabos2024smallmoleculeproduced pages 8-11, bargabos2024smallmoleculeproduced pages 1-2) |
| 3 | Flavin prenyltransferase (cofactor supply) | **ubiX** | Synthesis of prenylated FMN (pFMN), the cofactor required by UbiD | FMN + prenyl donor → pFMN | FMN; prenyl donor | UbiX flavin prenyltransferase | Does not modify the UQ intermediate directly; supplies the unusual pFMN cofactor needed for decarboxylation. Some genomes with otherwise recognizable UQ pathways lack **ubiX/ubiD**, implying alternative decarboxylation systems in some lineages (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 5-6) |
| 4 | 4-hydroxy-3-polyprenylbenzoate decarboxylase | **ubiD** | Decarboxylation of prenyl-4-HB intermediate | 3-octaprenyl-4-hydroxybenzoate → octaprenylphenol (OPP) | pFMN supplied by UbiX | UbiD/UbiX pFMN-dependent decarboxylase system | UbiD functions with the UbiX-made cofactor and forms higher-order assemblies; this step is strongly supported in *E. coli* but is one of the major points of pathway variation because some UQ-producing bacteria apparently use another solution (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 5-6) |
| 5 | C5 hydroxylase | **ubiI** | Aromatic hydroxylation at C5 | OPP-derived ring intermediate → C5-hydroxylated intermediate | O2, FAD/FMN redox chemistry, reductant | Flavin-dependent monooxygenase (FMO) | In the canonical *E. coli* aerobic pathway UbiI is the dedicated C5 hydroxylase. In other bacteria, this role can be carried by multifunctional UbiL or UbiM, or by anaerobic UbiUV chemistry under low O2 (abby2020advancesinbacterial pages 3-4, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 11-12, abby2020advancesinbacterial pages 4-5) |
| 6 | O-methyltransferase (first O-methylation) | **ubiG** | First O-methylation of the ring | Polyprenyldihydroxybenzene intermediate → methoxy intermediate | S-adenosylmethionine (SAM) | SAM-dependent O-methyltransferase | UbiG performs both O-methylation steps in the bacterial pathway. Exact substrate sequence can vary with pathway architecture, but dual O-methyltransferase function is conserved in the classical bacterial route (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 3-4) |
| 7 | C1 hydroxylase | **ubiH** | Aromatic hydroxylation at C1 | Methoxylated polyprenylphenol intermediate → C1-hydroxylated intermediate | O2, flavin redox chemistry, reductant | Flavin-dependent monooxygenase (FMO) | In *E. coli* UbiH is the dedicated C1 hydroxylase. Other bacteria may replace this specialization with dual-activity UbiL or generalist UbiM; anaerobic bacteria can bypass the O2-dependent chemistry with UbiU/UbiV (abby2020advancesinbacterial pages 3-4, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 11-12, abby2020advancesinbacterial pages 4-5) |
| 8 | C-methyltransferase | **ubiE** | C-methylation at C2 of the quinol ring | Demethyldemethoxyubiquinone-like intermediate → demethoxyubiquinone-like intermediate | SAM | SAM-dependent C-methyltransferase | Shared ancestry/function with enzymes in menaquinone-related chemistry means annotation can be confused at pathway boundaries; nevertheless, C2 methylation by UbiE is a core obligate step in the classical route (abby2020advancesinbacterial pages 3-4, staiano2023biosynthesisdeficiencyand pages 4-5) |
| 9 | C6 hydroxylase | **ubiF** / alternative **coq7** | Terminal aromatic hydroxylation at C6 | Demethoxyubiquinone/quinol intermediate → demethylubiquinone/quinol intermediate | For UbiF: O2 and flavin chemistry; for Coq7: di-iron/O2-dependent hydroxylation | UbiF: FMO; Coq7: di-iron hydroxylase | This is the most prominent lineage-level replacement step. *E. coli* uses UbiF, but many bacteria use Coq7 instead; UbiN and UbiM can also supply C6 activity in some clades. Evolutionary analyses support repeated replacement of ancestral Coq7 by neofunctionalized FMO paralogs such as UbiF/UbiN (abby2020advancesinbacterial pages 3-4, staiano2023biosynthesisdeficiencyand pages 4-5, kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 11-12, kazemzadeh2023diversificationofubiquinone pages 6-8, abby2020advancesinbacterial pages 4-5) |
| 10 | O-methyltransferase (terminal O-methylation) | **ubiG** | Final O-methylation yielding ubiquinone | Demethylubiquinol/demethylubiquinone intermediate → ubiquinone | SAM | SAM-dependent O-methyltransferase | Same enzyme as step 6; completion of the benzoquinone head group. Because hydrophobic intermediates remain membrane-associated, efficient turnover likely depends on accessory proteins and metabolon organization rather than UbiG alone (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 4-5) |
| A1 | Atypical kinase-like ATPase accessory factor | **ubiB** | Accessory role in handling hydrophobic intermediates and/or organizing pathway flux | Not a simple substrate→product step; supports conversion of membrane-embedded intermediates by catalytic enzymes | ATP; activity stimulated by membranes/UQ intermediates | UbiB/COQ8 atypical protein kinase-like ATPase family | Near-essential for bacterial UQ production in *E. coli*; current best model is ATPase-driven extraction/handling of hydrophobic intermediates rather than classical protein phosphorylation (abby2020advancesinbacterial pages 3-4, abby2020advancesinbacterial pages 4-5) |
| A2 | Lipid-binding accessory factor | **ubiJ** | Binds hydrophobic UQ intermediates and presents them to catalytic enzymes in the aerobic Ubi complex | Intermediate trafficking/presentation rather than a discrete chemical conversion | None established; SCP2 lipid-binding domain | SCP2-domain accessory protein | Aerobic counterpart of UbiT. Required for efficient O2-dependent UQ biosynthesis; absent UbiJ abolishes or severely impairs UQ formation in *E. coli* (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 2-3) |
| A3 | Accessory assembly factor | **ubiK** | Structural/support role in the Ubi metabolon with UbiJ | No direct substrate→product step | None established | Small accessory protein associated with Ubi complex | Forms a UbiJ:UbiK heterotrimeric assembly (reported stoichiometries differ in summary descriptions) and is important, though less absolutely required than UbiJ, for efficient aerobic UQ synthesis (abby2020advancesinbacterial pages 3-4, abby2020advancesinbacterial pages 2-3) |


*Table: This table summarizes the canonical bacterial ubiquinone pathway from chorismate to ubiquinone, including the core catalytic enzymes and key accessory factors. It also highlights where the pathway is conserved versus where major bacterial variants, especially in hydroxylation and decarboxylation chemistry, are known.*

### 3.1 Precursor Formation (Step 1)

The first committed step is the UbiC-catalyzed elimination of pyruvate from chorismate to yield 4-hydroxybenzoate. This reaction is the sole source of the benzenoid ring precursor in most proteobacteria (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 1-3). In some species, such as *Xanthomonas campestris*, an alternative enzyme XanB2 produces 4-HB from chorismate (pierrel2022recentadvancesin pages 3-4). In eukaryotes, 4-HB derives from tyrosine and phenylalanine through a multi-step process that remains incompletely understood (staiano2023biosynthesisdeficiencyand pages 2-4, pierrel2022recentadvancesin pages 1-3).

### 3.2 Polyprenyl Side-Chain Attachment (Step 2)

UbiA is a membrane-integral polyprenyltransferase that attaches the polyprenyl diphosphate side chain to 4-HB, producing 3-octaprenyl-4-hydroxybenzoate in *E. coli* (abby2020advancesinbacterial pages 2-3). Structurally, UbiA adopts an all-α-helical architecture with nine transmembrane helices arranged in a U-shape, creating a large central cavity and a lateral portal that facilitates binding of the long-chain isoprenyl diphosphate substrate. The prenylated product can be released directly into the membrane lipid bilayer (abby2020advancesinbacterial pages 2-3). Key catalytic residues include Asp191 and Arg72 in *E. coli* UbiA (bargabos2024smallmoleculeproduced pages 8-11, bargabos2024smallmoleculeproduced pages 6-8). Recent work has validated UbiA as a potential antibacterial target: the compound 3,6-dihydroxy-1,2-benzisoxazole (DHB) acts as both a competitive inhibitor and a prodrug substrate of UbiA, being prenylated into a toxic chimeric product (bargabos2024smallmoleculeproduced pages 1-2, bargabos2024smallmoleculeproduced pages 11-15).

### 3.3 Prenyl-FMN Cofactor Supply and Decarboxylation (Steps 3–4)

Following prenylation, the substrate undergoes decarboxylation via the UbiD–UbiX enzyme system. UbiX is a flavin prenyltransferase that produces prenylated FMN (pFMN), an unusual modified cofactor (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 3-4). UbiD, a pFMN-dependent decarboxylase, then removes the carboxyl group from 3-octaprenyl-4-hydroxybenzoate to yield 2-octaprenylphenol (OPP) (abby2020advancesinbacterial pages 2-3, pierrel2022recentadvancesin pages 3-4). Crystal structures reveal that UbiD functions as homohexamers capable of binding pFMN (abby2020advancesinbacterial pages 2-3). Blue native-PAGE analysis shows that UbiD and UbiX co-migrate at approximately 700 kDa, suggesting they organize into larger multimeric structures (abby2020advancesinbacterial pages 2-3). Importantly, many bacterial genomes that encode an otherwise recognizable UQ pathway lack *ubiD* and *ubiX*, implying that alternative decarboxylation systems exist in some lineages. The proposed alternative gene *ubiZ* has been suggested as a candidate decarboxylase, but its short sequence (~160 amino acids) and lack of similarity to known decarboxylases raise questions about its function (abby2020advancesinbacterial pages 5-6).

### 3.4 Ring Hydroxylation, Methylation, and Completion (Steps 5–10)

After decarboxylation, the polyprenylphenol intermediate undergoes six additional modifications: three hydroxylations and three methylations. In the *E. coli* aerobic pathway, the canonical order involves:

1. **C5 hydroxylation** by UbiI (abby2020advancesinbacterial pages 3-4)
2. **First O-methylation** by UbiG using SAM (abby2020advancesinbacterial pages 3-4)
3. **C1 hydroxylation** by UbiH (abby2020advancesinbacterial pages 3-4)
4. **C-methylation at C2** by UbiE using SAM (abby2020advancesinbacterial pages 3-4)
5. **C6 hydroxylation** by UbiF (or Coq7 in other species) (abby2020advancesinbacterial pages 3-4, staiano2023biosynthesisdeficiencyand pages 4-5)
6. **Terminal O-methylation** by UbiG using SAM (abby2020advancesinbacterial pages 3-4)

The three aerobic hydroxylases UbiI, UbiH, and UbiF are all group A FAD-dependent monooxygenases that use dioxygen to activate molecular oxygen for aromatic hydroxylation (abby2020advancesinbacterial pages 3-4). UbiG is a dual-function SAM-dependent O-methyltransferase that catalyzes both the C5 and C6 O-methylation reactions (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 3-4).

## 4. Major Molecular Players and Active Assemblies

### 4.1 The Ubi Metabolon

A defining feature of bacterial UQ biosynthesis is the organization of the tail-modifying enzymes into a supramolecular complex, termed the Ubi metabolon or Ubi complex. In *E. coli*, this soluble multiprotein assembly contains five catalytic enzymes (UbiE through UbiI) that catalyze the last six reactions of the pathway, transforming polyprenylphenol into CoQ (pierrel2022recentadvancesin pages 4-5). The complex also includes critical accessory proteins:

- **UbiJ** contains a Sterol Carrier Protein 2 (SCP2) domain that binds hydrophobic UQ biosynthetic intermediates and presents their head groups to the catalytic enzymes. Deletion of *ubiJ* abolishes UQ production under aerobic conditions (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 3-4).
- **UbiK** forms a heterotrimer with UbiJ (UbiK₂:UbiJ₁ stoichiometry) and supports efficient biosynthesis, though its loss is less severe than that of UbiJ (~20% residual UQ) (abby2020advancesinbacterial pages 3-4, abby2020advancesinbacterial pages 2-3).
- **UbiB** is an atypical protein kinase-like ATPase whose activity is stimulated by membrane interaction and UQ intermediates. The current best model is that UbiB extracts hydrophobic UQ precursors from the membrane for processing by the soluble Ubi complex, rather than functioning as a classical protein kinase (abby2020advancesinbacterial pages 3-4, guerra2023coenzymeqbiochemistry pages 26-26, abby2020advancesinbacterial pages 4-5).

The structural characterization of the Ubi metabolon remains incomplete, and the precise stoichiometry of proteins within the complex is unknown (pierrel2022recentadvancesin pages 4-5).

### 4.2 Anaerobic Accessory Factors

Under anaerobic conditions, a parallel set of accessory and catalytic proteins replaces the O₂-dependent components:

- **UbiT** is the anaerobic counterpart of UbiJ, containing an SCP2 domain for lipid binding. UbiT is specifically required for O₂-independent UQ biosynthesis and cannot be replaced by UbiJ (ariascartin2023roleofthe pages 1-2, pelosi2019ubiquinonebiosynthesisover pages 12-13, ariascartin2023roleofthe pages 9-12).
- **UbiU and UbiV** form a heterodimer representing a novel class of O₂-independent hydroxylases. Each protein binds a [4Fe-4S] cluster via conserved cysteines essential for catalytic activity (pelosi2019ubiquinonebiosynthesisover pages 2-3, pelosi2019ubiquinonebiosynthesisover pages 1-2). These iron-sulfur cluster-dependent hydroxylases catalyze at least the C5 and C6 hydroxylation steps without requiring molecular oxygen as a cosubstrate (pelosi2019ubiquinonebiosynthesisover pages 12-13, abby2020advancesinbacterial pages 4-5). The clusters are matured primarily by the ISC biogenesis machinery (ariascartin2023roleofthe pages 9-12).

Expression of *ubiUV* is controlled by the anaerobic transcriptional regulator Fnr, ensuring production under low-oxygen conditions (ariascartin2023roleofthe pages 9-12). The shared enzymes UbiA, UbiB, UbiC, UbiD, UbiE, UbiG, and UbiX function in both the aerobic and anaerobic pathways (ariascartin2023roleofthe pages 1-2, pelosi2019ubiquinonebiosynthesisover pages 3-4).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Hydroxylase Diversification

The most striking feature of UQ biosynthesis variation across bacteria is the diversification of the three hydroxylation steps. Kazemzadeh et al. (2023) established a framework of six UQ-FMO subfamilies—UbiF, UbiH, UbiI, UbiL, UbiM, and UbiN—each with distinct regioselectivities, plus the structurally unrelated di-iron hydroxylase Coq7 (kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 11-12). Nearly 20 different combinations of these hydroxylases have been identified among 67 proteobacterial species (abby2020advancesinbacterial pages 4-5). The following table summarizes the major lineage-specific patterns:

| Bacterial lineage | C5 hydroxylase | C1 hydroxylase | C6 hydroxylase | Notable features |
|---|---|---|---|---|
| *Escherichia coli* (Gammaproteobacteria) | UbiI | UbiH | UbiF | Canonical three-FMO aerobic system; exemplifies the six-subfamily framework in which UbiI is C5-selective, UbiH is C1-selective, and UbiF is a neofunctionalized C6 enzyme that replaces ancestral Coq7 in many Gammaproteobacteria (pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 3-4, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 11-12) |
| Alphaproteobacteria (general) | UbiL | UbiL | Coq7 | Ancestral-like arrangement inferred for many Alphaproteobacteria: bifunctional UbiL supplies C5 and C1 activities, while iron-dependent Coq7 supplies C6 activity; supports the model that the ancestral pseudomonadotal pathway used UbiL-like + Coq7 chemistry (kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 6-8) |
| Hyphomicrobiales / Rhodobacterales | UbiL (major; UbiN may retain minor C5 activity) | UbiL | UbiN | Derived alphaproteobacterial variant in which duplication of **ubiL** generated UbiN, a neofunctionalized C6 hydroxylase that functionally replaces lost Coq7; experimental testing showed UbiN proteins typically have moderate-to-strong C6 activity with weaker C5 activity (kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 11-12, kazemzadeh2023diversificationofubiquinone pages 6-8) |
| Betaproteobacteria (e.g. *Neisseria*) | UbiI or UbiM | UbiH or UbiM | Coq7 or UbiM | Betaproteobacteria commonly use the UbiH/UbiI/Coq7 combination, but some lineages such as *Neisseria meningitidis* encode UbiM, a generalist hydroxylase able to catalyze C5, C1, and C6 steps by itself; UbiM is also notable for horizontal transfer across lineages (kazemzadeh2023diversificationofubiquinone pages 1-2, kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 11-12, abby2020advancesinbacterial pages 4-5) |
| Anaerobic pathway variant (UbiUVT-dependent) | UbiU/UbiV | UbiU/UbiV | unresolved; UbiU/UbiV implicated in at least C5 and C6, and likely substitute for aerobic hydroxylases more broadly | Oxygen-independent route found in many alpha-, beta-, and gammaproteobacteria; shares UbiA/UbiD/UbiX/UbiE/UbiG with the aerobic pathway but replaces O2-dependent FMOs with the [4Fe-4S]-containing UbiU-UbiV heterodimer plus lipid-binding accessory factor UbiT. Current evidence directly supports UbiU/UbiV roles in C5 and C6 hydroxylation, while exact step-by-step allocation remains incompletely resolved (pelosi2019ubiquinonebiosynthesisover pages 2-3, ariascartin2023roleofthe pages 1-2, pelosi2019ubiquinonebiosynthesisover pages 12-13, abby2020advancesinbacterial pages 4-5, ariascartin2023roleofthe pages 9-12) |


*Table: This table summarizes how the three hydroxylation steps in bacterial ubiquinone biosynthesis are partitioned across major proteobacterial lineages. It highlights the Kazemzadeh 2023 six-subfamily framework and contrasts canonical aerobic systems with multifunctional and anaerobic alternatives.*

### 5.2 Evolutionary History of Hydroxylases

The ancestral Pseudomonadota (formerly Proteobacteria) is inferred to have possessed a bifunctional UbiL-like FMO with C1/C5-hydroxylation activity, coupled with Coq7 for C6-hydroxylation (kazemzadeh2023diversificationofubiquinone pages 9-11). From this ancestral state:

- **UbiL duplicated** to generate UbiH, UbiI, and UbiN in different lineages through subfunctionalization (splitting dual-activity ancestral enzymes into position-specific paralogs) and neofunctionalization (acquisition of novel C6 activity, as in UbiF and UbiN) (kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 11-12).
- **Coq7 was independently lost** at least twice: once in Gammaproteobacteria (replaced by UbiF) and once in certain Alphaproteobacteria (replaced by UbiN) (kazemzadeh2023diversificationofubiquinone pages 9-11, kazemzadeh2023diversificationofubiquinone pages 11-12, kazemzadeh2023diversificationofubiquinone pages 6-8).
- **UbiM** is a generalist hydroxylase capable of all three positions (C1, C5, C6), found in ~10% of analyzed genomes, and shows evidence of horizontal gene transfer across lineages (kazemzadeh2023diversificationofubiquinone pages 2-3, kazemzadeh2023diversificationofubiquinone pages 11-12).

### 5.3 Bacteria vs. Eukaryotes

Eukaryotic CoQ biosynthesis occurs in the mitochondrial inner membrane through nuclear-encoded COQ proteins assembled in the CoQ synthome. Key differences include: eukaryotes derive 4-HB from tyrosine/phenylalanine rather than chorismate; the C1 decarboxylase/hydroxylase remains genetically uncharacterized in eukaryotes; and the accessory proteins COQ4, COQ8, COQ9, COQ10, and COQ11 have no direct bacterial orthologs for some (rizzardi2024aninvitro pages 4-9, staiano2023biosynthesisdeficiencyand pages 4-5, fernandezdelrio2021coenzymeqbiosynthesis pages 3-5, staiano2023biosynthesisdeficiencyand pages 2-4). The COQ7-COQ9 complex forms a double heterodimer that reshapes the mitochondrial membrane for substrate accessibility (staiano2023biosynthesisdeficiencyand pages 4-5). Plants employ a unique flavin-dependent monooxygenase (CoqF) not found in animals or fungi for one of the hydroxylation steps (fernandezdelrio2021coenzymeqbiosynthesis pages 3-5).

### 5.4 The O₂-Independent Pathway

The discovery of the UbiT/UbiU/UbiV-dependent anaerobic pathway (Pelosi et al. 2019) fundamentally altered the view that UQ biosynthesis was exclusively an aerobic process (pelosi2019ubiquinonebiosynthesisover pages 2-3). This pathway is distributed across alpha-, beta-, and gammaproteobacterial clades, including several human pathogens (pelosi2019ubiquinonebiosynthesisover pages 1-2). Anaerobically synthesized UQ supports nitrate respiration and uracil biosynthesis under anaerobiosis, and UbiT plays a crucial role in enabling efficient transition from anaerobic to aerobic conditions (ariascartin2023roleofthe pages 1-2, ariascartin2023roleofthe pages 9-12). The UbiU-UbiV heterodimer represents a biochemically novel class of hydroxylases, utilizing [4Fe-4S] clusters rather than flavin/O₂ chemistry (abby2020advancesinbacterial pages 4-5).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Steps and Ordering

Several steps are strictly obligatory in all known bacterial UQ pathways: prenylation by UbiA, decarboxylation (by UbiD/UbiX or an unidentified alternative), all three hydroxylations, and all three methylations. The prenylation step must precede all ring modifications, as all downstream intermediates are membrane-associated (abby2020advancesinbacterial pages 2-3). Within the ring modification phase, there is evidence for some flexibility in reaction order, though the canonical *E. coli* pathway follows the sequence: C5-hydroxylation → O-methylation → C1-hydroxylation → C-methylation → C6-hydroxylation → O-methylation (pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 3-4). The extent to which this order is strictly maintained versus permissive remains debated (staiano2023biosynthesisdeficiencyand pages 4-5, fontaine2026mitochondrialdysfunctionsin pages 6-7).

### 6.2 Membrane Association Constraint

After UbiA-catalyzed prenylation, all intermediates carry a long polyprenyl tail that anchors them in the membrane. This creates a fundamental constraint: the catalytic enzymes must either be membrane-associated or have mechanisms to extract and present the hydrophobic intermediates. The Ubi metabolon, with its UbiJ/UbiK lipid-binding accessory factors and UbiB ATPase, represents the solution to this problem (abby2020advancesinbacterial pages 3-4, pierrel2022recentadvancesin pages 3-4, abby2020advancesinbacterial pages 4-5).

### 6.3 Oxygen Dependency and Dual-Pathway Architecture

The aerobic hydroxylases (UbiI, UbiH, UbiF) require O₂ as a cosubstrate, making them non-functional under anaerobic conditions. Deletion of all three aerobic FMOs (ΔubiF ΔubiI ΔubiH) still permits wild-type levels of UQ8 production under anaerobic conditions, directly demonstrating the sufficiency of the UbiU/UbiV-dependent alternative pathway (pelosi2019ubiquinonebiosynthesisover pages 3-4). Conversely, under aerobic conditions, UbiU and UbiV are no longer produced (their expression is repressed in the presence of O₂), while UbiT remains detectable (ariascartin2023roleofthe pages 9-12). This dual-pathway architecture allows facultative anaerobes to synthesize UQ across the entire O₂ range.

### 6.4 Failure Modes

Loss of UbiA, UbiC (or its functional equivalent), or the complete hydroxylation capacity results in complete loss of UQ production. Loss of UbiJ alone abolishes aerobic UQ synthesis, while UbiK loss retains approximately 20% of wild-type levels (abby2020advancesinbacterial pages 3-4). Loss of UbiB results in near-complete loss of UQ production (abby2020advancesinbacterial pages 3-4). In engineered heterologous production strains, bottlenecks occur at the conversion of polyprenylphenol intermediates to downstream products and in prenyl chain length specificity (pierrel2022recentadvancesin pages 3-4).

## 7. Controversies and Open Questions

### 7.1 Alternative Decarboxylation Systems

While UbiD/UbiX is the well-characterized decarboxylase system in *E. coli*, many bacterial genomes with otherwise complete UQ pathways lack these genes. The proposed alternative *ubiZ* gene is of uncertain function due to its short sequence and lack of homology to known decarboxylases (abby2020advancesinbacterial pages 5-6). Whether some bacteria can scavenge decarboxylated intermediates from their environment rather than synthesizing them internally has been proposed but not definitively demonstrated (abby2020advancesinbacterial pages 5-6).

### 7.2 Eukaryotic Decarboxylation

In eukaryotes, the C1-decarboxylation step remains genetically and biochemically uncharacterized (pierrel2022recentadvancesin pages 3-4). Recent evidence suggests COQ4 may have a direct catalytic role in oxidative decarboxylation, not merely a structural function, but this remains to be fully validated (fontaine2026mitochondrialdysfunctionsin pages 6-7).

### 7.3 Reaction Order Flexibility

Whether the ring modification reactions follow a strictly defined order or can proceed through alternative sequences is debated. In COQ6-deficient eukaryotic cells, the accumulation of intermediates that have undergone C1 decarboxylation/hydroxylation before C5 modification suggests the pathway is more flexible than classical models indicated (fontaine2026mitochondrialdysfunctionsin pages 6-7). In bacteria, the existence of nearly 20 different hydroxylase combinations across species raises the question of whether each combination imposes a different preferred reaction order.

### 7.4 Metabolon Stoichiometry and Structure

The precise structure, stoichiometry, and mechanism of the bacterial Ubi metabolon remain incompletely characterized. Only limited direct protein-protein interactions have been confirmed, and whether the complex is constitutive or dynamically assembled in response to metabolic demand is unknown (pierrel2022recentadvancesin pages 4-5). Recent computational approaches using AlphaFold2 have begun to address this gap, but experimental validation is still needed.

### 7.5 UbiB Function

The exact molecular function of UbiB/COQ8 remains uncertain despite extensive study. Three models have been proposed: classical protein kinase activity, ATPase-driven substrate extraction from membranes, or small-molecule kinase activity. Current evidence favors the ATPase model, but no definitive substrate has been identified for any kinase activity (guerra2023coenzymeqbiochemistry pages 26-26).

### 7.6 Incomplete Pathways

Some bacterial genomes contain fewer than the expected complement of UQ biosynthetic genes, raising questions about whether these organisms produce UQ at all, use as-yet-unidentified enzymes, or rely on environmental scavenging of intermediates (abby2020advancesinbacterial pages 5-6).

### 7.7 Source of Hydroxyl Oxygen in Anaerobic Pathway

While the UbiU/UbiV system has been demonstrated to catalyze O₂-independent hydroxylation, the precise source of the oxygen atom incorporated into the ring under strictly anaerobic conditions—and the detailed catalytic mechanism of these [4Fe-4S]-dependent hydroxylases—remain to be elucidated (abby2020advancesinbacterial pages 4-5, ariascartin2023roleofthe pages 9-12).

## 8. Key References

1. Abby SS, Kazemzadeh K, Vragniau C, Pelosi L, Pierrel F. Advances in bacterial pathways for the biosynthesis of ubiquinone. *Biochim Biophys Acta - Bioenergetics*. 2020;1861(11):148259. doi:10.1016/j.bbabio.2020.148259

2. Pierrel F, Burgardt A, Lee JH, Pelosi L, Wendisch VF. Recent advances in the metabolic pathways and microbial production of coenzyme Q. *World J Microbiol Biotechnol*. 2022;38(4). doi:10.1007/s11274-022-03242-3

3. Kazemzadeh K, Pelosi L, Chenal C, et al. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. *Mol Biol Evol*. 2023;40(10):msad219. doi:10.1093/molbev/msad219

4. Pelosi L, Vo CDT, Abby SS, et al. Ubiquinone biosynthesis over the entire O₂ range: characterization of a conserved O₂-independent pathway. *mBio*. 2019;10(4):e01319-19. doi:10.1128/mbio.01319-19

5. Arias-Cartin R, Kazemzadeh Ferizhendi K, Séchet E, et al. Role of the *Escherichia coli* ubiquinone-synthesizing UbiUVT pathway in adaptation to changing respiratory conditions. *mBio*. 2023;14. doi:10.1128/mbio.03298-22

6. Guerra RM, Pagliarini DJ. Coenzyme Q biochemistry and biosynthesis. *Trends Biochem Sci*. 2023;48(5):463-476. doi:10.1016/j.tibs.2022.12.006

7. Bargabos R, Iinishi A, Hawkins BA, et al. Small molecule produced by *Photorhabdus* interferes with ubiquinone biosynthesis in Gram-negative bacteria. *mBio*. 2024;15(10). doi:10.1128/mbio.01167-24

8. Staiano C, García-Corzo L, Mantle D, et al. Biosynthesis, deficiency, and supplementation of coenzyme Q. *Antioxidants*. 2023;12(7):1469. doi:10.3390/antiox12071469

9. Fernández-del-Río L, Clarke CF. Coenzyme Q biosynthesis: an update on the origins of the benzenoid ring and discovery of new ring precursors. *Metabolites*. 2021;11(6):385. doi:10.3390/metabo11060385

10. Burgardt A, Pelosi L, Chehade MH, Wendisch VF, Pierrel F. Rational engineering of non-ubiquinone containing *Corynebacterium glutamicum* for enhanced coenzyme Q10 production. *Metabolites*. 2022;12(5):428. doi:10.3390/metabo12050428

References

1. (abby2020advancesinbacterial pages 2-3): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

2. (pierrel2022recentadvancesin pages 3-4): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

3. (kazemzadeh2023diversificationofubiquinone pages 1-2): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

4. (abby2020advancesinbacterial pages 4-5): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

5. (pelosi2019ubiquinonebiosynthesisover pages 2-3): Ludovic Pelosi, Chau-Duy-Tam Vo, Sophie Saphia Abby, Laurent Loiseau, Bérengère Rascalou, Mahmoud Hajj Chehade, Bruno Faivre, Mathieu Goussé, Clothilde Chenal, Nadia Touati, Laurent Binet, David Cornu, Cameron David Fyfe, Marc Fontecave, Frédéric Barras, Murielle Lombard, and Fabien Pierrel. Ubiquinone biosynthesis over the entire o <sub>2</sub> range: characterization of a conserved o <sub>2</sub> -independent pathway. Aug 2019. URL: https://doi.org/10.1128/mbio.01319-19, doi:10.1128/mbio.01319-19. This article has 54 citations and is from a domain leading peer-reviewed journal.

6. (ariascartin2023roleofthe pages 1-2): Rodrigo Arias-Cartin, Katayoun Kazemzadeh Ferizhendi, Emmanuel Séchet, Ludovic Pelosi, Corinne Loeuillet, Fabien Pierrel, Frédéric Barras, and Emmanuelle Bouveret. Role of the escherichia coli ubiquinone-synthesizing ubiuvt pathway in adaptation to changing respiratory conditions. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.03298-22, doi:10.1128/mbio.03298-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (abby2020advancesinbacterial pages 3-4): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

8. (pierrel2022recentadvancesin pages 4-5): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

9. (abby2020advancesinbacterial pages 6-7): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

10. (abby2020advancesinbacterial pages 1-2): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

11. (abby2020advancesinbacterial pages 8-9): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

12. (pierrel2022recentadvancesin pages 1-3): Fabien Pierrel, Arthur Burgardt, Jin-Ho Lee, Ludovic Pelosi, and Volker F. Wendisch. Recent advances in the metabolic pathways and microbial production of coenzyme q. World Journal of Microbiology & Biotechnology, Feb 2022. URL: https://doi.org/10.1007/s11274-022-03242-3, doi:10.1007/s11274-022-03242-3. This article has 31 citations and is from a peer-reviewed journal.

13. (staiano2023biosynthesisdeficiencyand pages 4-5): Carmine Staiano, Laura García-Corzo, David Mantle, Nadia Turton, Lauren E. Millichap, Gloria Brea-Calvo, and Iain Hargreaves. Biosynthesis, deficiency, and supplementation of coenzyme q. Antioxidants, 12:1469, Jul 2023. URL: https://doi.org/10.3390/antiox12071469, doi:10.3390/antiox12071469. This article has 25 citations.

14. (bargabos2024smallmoleculeproduced pages 8-11): Rachel Bargabos, Akira Iinishi, Bryson A. Hawkins, Thomas Privalsky, Norman Pitt, Sangkeun Son, Rachel Corsetti, Michael F. Gates, Ryan D. Miller, and Kim Lewis. Small molecule produced by <i>photorhabdus</i> interferes with ubiquinone biosynthesis in gram-negative bacteria. Oct 2024. URL: https://doi.org/10.1128/mbio.01167-24, doi:10.1128/mbio.01167-24. This article has 2 citations and is from a domain leading peer-reviewed journal.

15. (bargabos2024smallmoleculeproduced pages 1-2): Rachel Bargabos, Akira Iinishi, Bryson A. Hawkins, Thomas Privalsky, Norman Pitt, Sangkeun Son, Rachel Corsetti, Michael F. Gates, Ryan D. Miller, and Kim Lewis. Small molecule produced by <i>photorhabdus</i> interferes with ubiquinone biosynthesis in gram-negative bacteria. Oct 2024. URL: https://doi.org/10.1128/mbio.01167-24, doi:10.1128/mbio.01167-24. This article has 2 citations and is from a domain leading peer-reviewed journal.

16. (abby2020advancesinbacterial pages 5-6): Sophie Saphia Abby, Katayoun Kazemzadeh, Charles Vragniau, Ludovic Pelosi, and Fabien Pierrel. Advances in bacterial pathways for the biosynthesis of ubiquinone. Nov 2020. URL: https://doi.org/10.1016/j.bbabio.2020.148259, doi:10.1016/j.bbabio.2020.148259. This article has 91 citations and is from a peer-reviewed journal.

17. (kazemzadeh2023diversificationofubiquinone pages 2-3): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

18. (kazemzadeh2023diversificationofubiquinone pages 11-12): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

19. (kazemzadeh2023diversificationofubiquinone pages 9-11): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

20. (kazemzadeh2023diversificationofubiquinone pages 6-8): Katayoun Kazemzadeh, Ludovic Pelosi, Clothilde Chenal, Sophie-Carole Chobert, Mahmoud Hajj Chehade, Margaux Jullien, Laura Flandrin, William Schmitt, Qiqi He, Emma Bouvet, Manon Jarzynka, Nelle Varoquaux, Ivan Junier, Fabien Pierrel, and Sophie S Abby. Diversification of ubiquinone biosynthesis via gene duplications, transfers, losses, and parallel evolution. Molecular Biology and Evolution, Oct 2023. URL: https://doi.org/10.1093/molbev/msad219, doi:10.1093/molbev/msad219. This article has 12 citations and is from a highest quality peer-reviewed journal.

21. (staiano2023biosynthesisdeficiencyand pages 2-4): Carmine Staiano, Laura García-Corzo, David Mantle, Nadia Turton, Lauren E. Millichap, Gloria Brea-Calvo, and Iain Hargreaves. Biosynthesis, deficiency, and supplementation of coenzyme q. Antioxidants, 12:1469, Jul 2023. URL: https://doi.org/10.3390/antiox12071469, doi:10.3390/antiox12071469. This article has 25 citations.

22. (bargabos2024smallmoleculeproduced pages 6-8): Rachel Bargabos, Akira Iinishi, Bryson A. Hawkins, Thomas Privalsky, Norman Pitt, Sangkeun Son, Rachel Corsetti, Michael F. Gates, Ryan D. Miller, and Kim Lewis. Small molecule produced by <i>photorhabdus</i> interferes with ubiquinone biosynthesis in gram-negative bacteria. Oct 2024. URL: https://doi.org/10.1128/mbio.01167-24, doi:10.1128/mbio.01167-24. This article has 2 citations and is from a domain leading peer-reviewed journal.

23. (bargabos2024smallmoleculeproduced pages 11-15): Rachel Bargabos, Akira Iinishi, Bryson A. Hawkins, Thomas Privalsky, Norman Pitt, Sangkeun Son, Rachel Corsetti, Michael F. Gates, Ryan D. Miller, and Kim Lewis. Small molecule produced by <i>photorhabdus</i> interferes with ubiquinone biosynthesis in gram-negative bacteria. Oct 2024. URL: https://doi.org/10.1128/mbio.01167-24, doi:10.1128/mbio.01167-24. This article has 2 citations and is from a domain leading peer-reviewed journal.

24. (guerra2023coenzymeqbiochemistry pages 26-26): Rachel M. Guerra and David J. Pagliarini. Coenzyme q biochemistry and biosynthesis. Trends in Biochemical Sciences, 48:463-476, May 2023. URL: https://doi.org/10.1016/j.tibs.2022.12.006, doi:10.1016/j.tibs.2022.12.006. This article has 142 citations and is from a domain leading peer-reviewed journal.

25. (pelosi2019ubiquinonebiosynthesisover pages 12-13): Ludovic Pelosi, Chau-Duy-Tam Vo, Sophie Saphia Abby, Laurent Loiseau, Bérengère Rascalou, Mahmoud Hajj Chehade, Bruno Faivre, Mathieu Goussé, Clothilde Chenal, Nadia Touati, Laurent Binet, David Cornu, Cameron David Fyfe, Marc Fontecave, Frédéric Barras, Murielle Lombard, and Fabien Pierrel. Ubiquinone biosynthesis over the entire o <sub>2</sub> range: characterization of a conserved o <sub>2</sub> -independent pathway. Aug 2019. URL: https://doi.org/10.1128/mbio.01319-19, doi:10.1128/mbio.01319-19. This article has 54 citations and is from a domain leading peer-reviewed journal.

26. (ariascartin2023roleofthe pages 9-12): Rodrigo Arias-Cartin, Katayoun Kazemzadeh Ferizhendi, Emmanuel Séchet, Ludovic Pelosi, Corinne Loeuillet, Fabien Pierrel, Frédéric Barras, and Emmanuelle Bouveret. Role of the escherichia coli ubiquinone-synthesizing ubiuvt pathway in adaptation to changing respiratory conditions. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.03298-22, doi:10.1128/mbio.03298-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

27. (pelosi2019ubiquinonebiosynthesisover pages 1-2): Ludovic Pelosi, Chau-Duy-Tam Vo, Sophie Saphia Abby, Laurent Loiseau, Bérengère Rascalou, Mahmoud Hajj Chehade, Bruno Faivre, Mathieu Goussé, Clothilde Chenal, Nadia Touati, Laurent Binet, David Cornu, Cameron David Fyfe, Marc Fontecave, Frédéric Barras, Murielle Lombard, and Fabien Pierrel. Ubiquinone biosynthesis over the entire o <sub>2</sub> range: characterization of a conserved o <sub>2</sub> -independent pathway. Aug 2019. URL: https://doi.org/10.1128/mbio.01319-19, doi:10.1128/mbio.01319-19. This article has 54 citations and is from a domain leading peer-reviewed journal.

28. (pelosi2019ubiquinonebiosynthesisover pages 3-4): Ludovic Pelosi, Chau-Duy-Tam Vo, Sophie Saphia Abby, Laurent Loiseau, Bérengère Rascalou, Mahmoud Hajj Chehade, Bruno Faivre, Mathieu Goussé, Clothilde Chenal, Nadia Touati, Laurent Binet, David Cornu, Cameron David Fyfe, Marc Fontecave, Frédéric Barras, Murielle Lombard, and Fabien Pierrel. Ubiquinone biosynthesis over the entire o <sub>2</sub> range: characterization of a conserved o <sub>2</sub> -independent pathway. Aug 2019. URL: https://doi.org/10.1128/mbio.01319-19, doi:10.1128/mbio.01319-19. This article has 54 citations and is from a domain leading peer-reviewed journal.

29. (rizzardi2024aninvitro pages 4-9): Nicola Rizzardi. An in vitro characterization of the bioenergetic effects of a phytosome-based coenzyme q10 formulation as a potential treatment for troyer syndrome. Text, Jan 2024. URL: https://doi.org/10.48676/unibo/amsdottorato/11511, doi:10.48676/unibo/amsdottorato/11511. This article has 0 citations and is from a peer-reviewed journal.

30. (fernandezdelrio2021coenzymeqbiosynthesis pages 3-5): Lucía Fernández-del-Río and Catherine F. Clarke. Coenzyme q biosynthesis: an update on the origins of the benzenoid ring and discovery of new ring precursors. Metabolites, 11:385, Jun 2021. URL: https://doi.org/10.3390/metabo11060385, doi:10.3390/metabo11060385. This article has 56 citations.

31. (fontaine2026mitochondrialdysfunctionsin pages 6-7): Fanny Fontaine, Romain Pénicaud, and Stéphane Allouche. Mitochondrial dysfunctions in human primary coenzyme q10 deficiencies. Biomolecules, 16:302, Feb 2026. URL: https://doi.org/10.3390/biom16020302, doi:10.3390/biom16020302. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](ubiquinone_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](ubiquinone_biosynthesis-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. abby2020advancesinbacterial pages 2-3
2. abby2020advancesinbacterial pages 8-9
3. pierrel2022recentadvancesin pages 1-3
4. staiano2023biosynthesisdeficiencyand pages 4-5
5. pierrel2022recentadvancesin pages 3-4
6. abby2020advancesinbacterial pages 5-6
7. abby2020advancesinbacterial pages 3-4
8. pierrel2022recentadvancesin pages 4-5
9. ariascartin2023roleofthe pages 9-12
10. abby2020advancesinbacterial pages 4-5
11. kazemzadeh2023diversificationofubiquinone pages 9-11
12. fernandezdelrio2021coenzymeqbiosynthesis pages 3-5
13. pelosi2019ubiquinonebiosynthesisover pages 2-3
14. pelosi2019ubiquinonebiosynthesisover pages 1-2
15. pelosi2019ubiquinonebiosynthesisover pages 3-4
16. fontaine2026mitochondrialdysfunctionsin pages 6-7
17. guerra2023coenzymeqbiochemistry pages 26-26
18. kazemzadeh2023diversificationofubiquinone pages 1-2
19. ariascartin2023roleofthe pages 1-2
20. abby2020advancesinbacterial pages 6-7
21. abby2020advancesinbacterial pages 1-2
22. bargabos2024smallmoleculeproduced pages 8-11
23. bargabos2024smallmoleculeproduced pages 1-2
24. kazemzadeh2023diversificationofubiquinone pages 2-3
25. kazemzadeh2023diversificationofubiquinone pages 11-12
26. kazemzadeh2023diversificationofubiquinone pages 6-8
27. staiano2023biosynthesisdeficiencyand pages 2-4
28. bargabos2024smallmoleculeproduced pages 6-8
29. bargabos2024smallmoleculeproduced pages 11-15
30. pelosi2019ubiquinonebiosynthesisover pages 12-13
31. rizzardi2024aninvitro pages 4-9
32. 4Fe-4S
33. https://doi.org/10.1016/j.bbabio.2020.148259,
34. https://doi.org/10.1007/s11274-022-03242-3,
35. https://doi.org/10.1093/molbev/msad219,
36. https://doi.org/10.1128/mbio.01319-19,
37. https://doi.org/10.1128/mbio.03298-22,
38. https://doi.org/10.3390/antiox12071469,
39. https://doi.org/10.1128/mbio.01167-24,
40. https://doi.org/10.1016/j.tibs.2022.12.006,
41. https://doi.org/10.48676/unibo/amsdottorato/11511,
42. https://doi.org/10.3390/metabo11060385,
43. https://doi.org/10.3390/biom16020302,