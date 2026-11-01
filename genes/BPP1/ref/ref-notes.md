# Curation Notes: ref (P35926) — Bacteriophage P1

## Identity & Genomic Context
- **Gene symbol**: `ref` ("recombination enhancement function")
- **UniProtKB**: `P35926` (`REF_BPP1`, 186 aa, 21.3 kDa)
- **Organism**: Punavirus P1 (`NCBITaxon:2886926`, *Escherichia phage P1*)
- **Locus**: Early C1-repressible gene located near the right end of the P1 linear virion map (head-to-head with `bof`, immediately downstream of two C1 operator sites) [PMID:2542224, PMID:21193392].

## Molecular Function & Mechanism
1. **RecA-Dependent HNH-Family Endonuclease (NOT an Enzyme Activator)**:
   - Early genetic studies showed that `ref` expression stimulates *recA*-dependent homologous and microhomologous recombination (such as precise excision of `IS1` elements between 9-bp direct repeats in `galT::IS1`) in *E. coli* [PMID:2542224].
   - For decades, it was hypothesized that Ref might act as a direct regulator or activator of RecA protein (`GO:0008047` `enzyme activator activity`).
   - However, **Gruenig et al. (2011)** (`PMID:21193392`) purified and biochemically/structurally characterized Ref, explicitly **refuting** the RecA-regulator hypothesis:
     - *"In this work we have purified and characterized the Ref protein, finding no evidence that it functions as a RecA regulator. Instead, Ref protein is a new kind of enzyme; that is, a RecA-dependent nuclease."* [PMID:21193392]
     - *"Ref binds to ss- and dsDNA but does not cleave any DNA substrate until RecA protein and ATP are added to form RecA nucleoprotein filaments. Ref cleaves only where RecA protein is bound."* [PMID:21193392]
     - *"The overall structure of Ref, including several putative active site histidine residues, defines a new subclass of HNH-family nucleases. We propose that enhancement of recombination by Ref reflects the introduction of directed, recombinogenic double-strand breaks."* [PMID:21193392]
   - Structurally, Ref comprises an intrinsically disordered highly basic N-terminal DNA-binding domain (76 aa, required for DNA tethering and two-step D-loop cleavage) and a globular C-terminal HNH-family nuclease domain (110 aa) that coordinates two Zn2+ ions [PMID:21193392].
   - Ref cleaves single-stranded DNA (`GO:0000014` `single-stranded DNA endonuclease activity`) bound by active RecA nucleoprotein filaments (ATPase-dependent) and cleaves both the displaced strand and paired strand at RecA-generated D-loops to produce targeted double-strand breaks (`GO:0004519` `endonuclease activity`) [PMID:21193392].

## Review of Existing GOA Annotations
- `GO:0008047` (`enzyme activator activity`, EXP `PMID:21193392`): **MODIFY** -> `GO:0004519` (`endonuclease activity`) and `GO:0000014` (`single-stranded DNA endonuclease activity`). `PMID:21193392` explicitly refuted the idea that Ref is a RecA activator; rather, RecA filaments activate the HNH endonuclease activity of Ref.
- `GO:0006310` (`DNA recombination`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0233`): **ACCEPT**. Ref generates targeted recombinogenic double-strand breaks at RecA-bound sites to stimulate homologous and microhomologous recombination [PMID:2542224, PMID:21193392].
- `GO:0006281` (`DNA repair`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0228`): **REMOVE**. Automated keyword mapping artifact from UniProt keyword `KW-0228` (`DNA excision`), which was assigned because Ref stimulated precise excision of `IS1` elements via microhomologous recombination (`PMID:2542224`), not nucleotide excision DNA repair; Ref introduces double-strand breaks rather than repairing damaged DNA.
