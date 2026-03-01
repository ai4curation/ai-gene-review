# SNIPE Exploration: Membrane-Bound Phage Defense Nuclease

## Overview

SNIPE (Surface-associated Nuclease Inhibiting Phage Entry) is a bacterial antiphage defense system published in *Nature* (February 2026) that cleaves phage DNA during genome injection. This document records an exploration of existing candidates in the ai-gene-review repository relevant to SNIPE biology.

**Reference**: [A membrane-bound nuclease directly cleaves phage DNA during genome injection | Nature](https://www.nature.com/articles/s41586-026-10207-1)

## SNIPE Key Features

- **GIY-YIG nuclease domain** cleaves incoming phage DNA
- **DUF4041 domain** binds phage tape measure protein (TMP) and incoming DNA
- **N-terminal region** associates with **ManYZ complex** (mannose phosphotransferase system) used by phages as DNA entry receptor
- Self/non-self discrimination via **spatial context** (only targets DNA passing through phage injection machinery)
- 500+ homologues across bacterial phyla
- Some variants use **DivIVA-like domains** or **type III secretion system ATPase-like** features for membrane anchoring

## Exploration Results (2026-03-01)

### Direct SNIPE Content: None

No gene reviews, deep research, or publications directly related to SNIPE exist in this repository. No genes with DUF4041 domains are under review. The GIY-YIG nuclease domain appears only in InterPro-to-GO mapping data, not in any gene review.

### Relevant Existing Gene: DivIVA (BACSU)

**`genes/BACSU/divIVA/divIVA-ai-review.yaml`** (P71021)

~34% of SNIPE homologues lacking transmembrane domains use DivIVA-like domains for membrane anchoring. The repository has a complete review of DivIVA in *B. subtilis* as a membrane curvature-sensing scaffold protein. Key properties shared with SNIPE DivIVA-domain variants:
- Senses negative membrane curvature at cell poles/septa
- N-terminal membrane-binding domain inserts hydrophobic residues into curved membranes
- Forms oligomeric structures for higher-order assembly

This provides domain-level context for understanding how a subset of SNIPE variants localize to membranes without classical TM domains.

### Phage-Bacteria Arms Race Genes (Phage Side)

| Gene | Organism | File | Relevance to SNIPE |
|------|----------|------|-------------------|
| darB | Phage P1 (9CAUD) | `genes/9CAUD/darB/darB-ai-review.yaml` | Antirestriction protein ejected into host to protect phage DNA from Type I R-M. SNIPE is conceptually the host-side counterpart |
| DAM | Phage T4 (BPT4) | `genes/BPT4/DAM/DAM-ai-review.yaml` | DNA adenine methyltransferase that protects phage DNA from host restriction. Same evolutionary arms race SNIPE participates in |
| AcrF8 | Phage ZF40 (BPZF4) | `genes/BPZF4/AcrF8/AcrF8-ai-review.yaml` | Anti-CRISPR protein inhibiting Type I-F CRISPR-Cas. Another phage counter-defense strategy |
| AimP | Phage phi3T (BPPHT) | `genes/BPPHT/AimP/AimP-falcon-research.md` | Phage quorum sensing peptide governing lysis-lysogeny. Phage decision-making about infection strategy |

### Related Projects

| Project | File | Connection |
|---------|------|------------|
| Anti-CRISPR | `projects/ANTI_CRISPR.md` | CRISPR-Cas and SNIPE are both bacterial defense systems; anti-CRISPRs and SNIPE-evading phage mutations are parallel arms race strategies |
| SPKW-BPT4 | `projects/SPKW-BPT4.md` | Addresses annotation challenges for phage-bacteria interactions; relevant to how SNIPE annotations should be handled |
| cGAS-STING | `projects/CGAS_STING_PATHWAY.md` | Eukaryotic cytosolic DNA sensing pathway; conceptual parallel (cGAS senses foreign DNA in cytoplasm; SNIPE intercepts it at the membrane) |
| Surveillance Immunity | `projects/CAEEL_SURVEILLANCE_IMMUNITY.md` | Both represent innate immunity via spatial/contextual detection rather than sequence recognition |

### UniRule Entries for Phage Structural Biology

Two UniRule entries touch on tape measure proteins (the phage components SNIPE targets):
- **UR001207021** — Lambdavirus tape measure protein family (HAMAP MF_04138)
- **UR001158635** — Caudoviricetes lambda-like tail assembly scaffold (HAMAP MF_04134)

These rules annotate the phage-side proteins that SNIPE interacts with.

## Annotation Concern: GIY-YIG Domain Misannotation Risk

The InterPro-to-GO mapping (`rules/arba/_interpro2go.txt`) contains:

```
InterPro:IPR047296 UvrC/Cho-like, GIY-YIG domain → GO:0006289 (nucleotide-excision repair)
```

SNIPE uses a GIY-YIG nuclease domain for **phage DNA cleavage during injection** — a defense function unrelated to nucleotide-excision repair. Automated annotation of SNIPE homologues through this InterPro entry would produce **incorrect GO annotations** for 500+ proteins. This mapping assumes GIY-YIG = DNA repair (as in UvrC), but SNIPE demonstrates this domain has been repurposed for antiphage defense.

## What Would Be Needed to Add SNIPE

1. **Identify the SNIPE UniProt entry** — Once the protein is in UniProt, fetch it with `just fetch-gene ECOLI <gene>`
2. **ManYZ receptor genes** — E. coli ManY and ManZ (mannose PTS components) are not currently reviewed
3. **New GO terms needed**:
   - Phage DNA cleavage activity during genome injection (molecular function)
   - Defense response to bacteriophage via membrane-bound nuclease (biological process)
   - Spatial self/non-self discrimination (as distinct from sequence-based recognition like R-M systems)
4. **InterPro-to-GO mapping update** — Flag that GIY-YIG domain (IPR047296) should not universally map to nucleotide-excision repair; SNIPE-type proteins need a distinct mapping
5. **Broader phage defense project** — A project file covering SNIPE alongside Zorya and Kiwa as membrane-localized injection-targeting defense systems (none of these are currently in the repo)

## E. coli Genes Currently in Repo

The 20 ECOLI genes are predominantly chaperones and protein quality control (DnaJ, DnaK, GroEL, HdeA/B, Skp, SlyD, Spy, CpxP, CnoX, SecB, surA, RidA), cell division (ftsI, mrdA), and metabolic enzymes (glgX, lpd, sucA/B, rbsD). None are defense-related.

## Status

- [x] Initial exploration complete (2026-03-01)
- [ ] Identify SNIPE UniProt entry when available
- [ ] Consider creating phage injection defense project
- [ ] Flag GIY-YIG InterPro-to-GO misannotation concern

Last updated: 2026-03-01
