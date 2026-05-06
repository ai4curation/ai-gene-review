# GO Issue: NTR for SNIPE defense system + gap in anti-phage defense hierarchy

## Summary

A newly characterized anti-phage defense system, SNIPE (Surface-associated Nuclease Inhibiting Phage Entry; [PMID:41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/)), does not fit under the existing [GO:0099046](https://amigo.geneontology.org/amigo/term/GO:0099046) `clearance of foreign intracellular nucleic acids` branch because it destroys phage DNA *during* membrane injection — the DNA is never intracellular.

This new term request also highlights a broader gap: none of the bacterial anti-phage nucleic acid defense systems (CRISPR-Cas, R-M) are currently classified under [GO:0051607](https://amigo.geneontology.org/amigo/term/GO:0051607) `defense response to virus`, despite anti-phage defense being their primary evolved biological role. We propose (a) a new `SNIPE defense system` term under `defense response to virus`, and (b) adding `defense response to virus` as a second parent for the existing CRISPR-Cas and R-M system terms. Existing phage entry/ejection BP terms (e.g. [GO:0039678](https://amigo.geneontology.org/amigo/term/GO:0039678), [GO:0099001](https://amigo.geneontology.org/amigo/term/GO:0099001)) can capture injection mechanics, but not the host-side SNIPE defense process term requested here.

## Current hierarchy

```
defense response (GO:0006952)
  ├─ defense response to virus (GO:0051607)          ← CRISPR, R-M, SNIPE NOT here
  │
  └─ defense response to other organism (GO:0098542)
      └─ defense response to symbiont (GO:0140546)
          └─ clearance of foreign intracellular nucleic acids (GO:0099046)
              ├─ CRISPR-cas system (GO:0099048)
              ├─ clearance of foreign intracellular RNA (GO:0099047)
              └─ clearance of foreign intracellular DNA (GO:0044355)
                  └─ DNA restriction-modification system (GO:0009307)
```

## Problems

### 1. CRISPR-Cas and R-M are not under "defense response to virus"

CRISPR-Cas and restriction-modification systems are anti-viral defense systems. Their primary biological role is to protect bacteria and archaea from bacteriophage infection. Yet they are only reachable through `defense response to symbiont`, not through `defense response to virus` ([GO:0051607](https://amigo.geneontology.org/amigo/term/GO:0051607)).

This was partially noted in issue #10994 by Jim Hu, who wrote:

> "An umbrella term for the overall process of CRISPR-mediated adaptive immunity could be over all of these, the closest appropriate parent would be GO:0044355 clearance of foreign intracellular DNA, but this should have a parent term that includes both RNA and DNA. Otherwise, it would be a child of GO:0006952 defense response."

The CRISPR-cas system term was subsequently created under `clearance of foreign intracellular nucleic acids`, but the connection to virus defense was never made.

### 2. "Clearance of foreign intracellular nucleic acids" is too narrow for SNIPE

SNIPE ([PMID:41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/); Saxton et al. 2026, Nature) is a membrane-anchored GIY-YIG nuclease that cleaves phage DNA *during* genome injection — before the DNA enters the cytoplasm. It associates with the ManYZ inner membrane complex at genome injection sites and binds phage tape measure proteins to position its nuclease domain for cleavage of the incoming DNA. SNIPE was originally identified as PD-λ-1 in a functional screen of the *E. coli* pangenome ([PMID:36123438](https://pubmed.ncbi.nlm.nih.gov/36123438/); Vassallo et al. 2022).

The term "clearance of foreign intracellular nucleic acids" does not fit SNIPE because:
- **"Clearance"** implies something is present and then removed; SNIPE *prevents* entry
- **"Intracellular"** implies the nucleic acid is already inside the cell; SNIPE acts at the membrane during translocation

Yet SNIPE is clearly in the same functional class as CRISPR-Cas and R-M — it is a nucleic acid-targeting anti-phage defense system. SNIPE homologues (InterPro [IPR025280](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR025280/), Pfam [PF13250](https://www.ebi.ac.uk/interpro/entry/pfam/PF13250/)) are found in ~33% of well-sequenced bacterial clades, with 1,612 protein members across 2,466 taxa ([PMID:41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/)).

### 3. "Defense response to symbiont" is an awkward parent for anti-phage systems

While GO's use of "symbiont" encompasses parasitism, the phrasing is unintuitive for phage defense systems. More importantly, `defense response to virus` ([GO:0051607](https://amigo.geneontology.org/amigo/term/GO:0051607)) exists and is precisely the right concept.

## Proposed changes

### A. Consider adding `defense response to virus` as a parent of CRISPR-Cas and R-M

CRISPR-Cas and R-M systems evolved under selective pressure from phage predation — CRISPR spacers in natural populations are overwhelmingly phage-derived ([PMID:37460672](https://pubmed.ncbi.nlm.nih.gov/37460672/)), and R-M systems are primarily maintained as anti-phage defenses. These systems *can* incidentally target non-viral foreign DNA (e.g. conjugative plasmids), but anti-viral defense is their primary biological role.

We propose that [GO:0099048](https://amigo.geneontology.org/amigo/term/GO:0099048) `CRISPR-cas system` and [GO:0009307](https://amigo.geneontology.org/amigo/term/GO:0009307) `DNA restriction-modification system` should individually gain [GO:0051607](https://amigo.geneontology.org/amigo/term/GO:0051607) `defense response to virus` as a second is_a parent. The umbrella term [GO:0099046](https://amigo.geneontology.org/amigo/term/GO:0099046) `clearance of foreign intracellular nucleic acids` should NOT gain this parent, since the concept of clearing foreign nucleic acids is mechanism-descriptive and source-agnostic — it is not inherently anti-viral.

### B. New term: SNIPE defense system

```
Term name: SNIPE defense system
Namespace: biological_process
Definition: A defense response to a virus in which a membrane-anchored
  nuclease of the SNIPE family cleaves viral DNA during genome injection
  across the cell membrane. SNIPE proteins associate with inner membrane
  components at phage genome injection sites, bind phage tape measure
  proteins via their DUF4041 domain, and use a GIY-YIG nuclease domain
  to degrade incoming phage DNA before it enters the cytoplasm. Unlike
  restriction-modification or CRISPR-Cas systems, self/non-self
  discrimination is achieved through subcellular localization at the
  membrane rather than recognition of specific DNA sequences or
  modifications.
References: PMID:41741653 (Saxton et al. 2026),
  PMID:36123438 (Vassallo et al. 2022)
```

**Parentage**: The SNIPE term should be `is_a` [GO:0051607](https://amigo.geneontology.org/amigo/term/GO:0051607) `defense response to virus`. It should NOT be under `clearance of foreign intracellular nucleic acids` ([GO:0099046](https://amigo.geneontology.org/amigo/term/GO:0099046)) because the DNA is not intracellular when cleaved.

### C. Proposed hierarchy after changes

```
defense response to virus (GO:0051607)
  ├─ CRISPR-cas system (GO:0099048)                    [add second parent]
  ├─ DNA restriction-modification system (GO:0009307)  [add second parent]
  └─ SNIPE defense system [NEW]

defense response to symbiont (GO:0140546)
  └─ clearance of foreign intracellular nucleic acids (GO:0099046)  [unchanged]
      ├─ CRISPR-cas system (GO:0099048)
      ├─ clearance of foreign intracellular RNA (GO:0099047)
      └─ clearance of foreign intracellular DNA (GO:0044355)
          └─ DNA restriction-modification system (GO:0009307)
```

CRISPR-Cas and R-M gain `defense response to virus` as a second parent, reflecting their primary evolved function while retaining their placement under `clearance of foreign intracellular nucleic acids`. SNIPE goes exclusively under `defense response to virus` since (a) it functions specifically as an anti-phage system targeting phage tape measure proteins, and (b) it does not clear intracellular nucleic acids — it destroys DNA at the membrane during injection.

### D. Optional: intermediate grouping term

If the GO editors want a grouping term for all nucleic acid-targeting anti-viral systems (CRISPR, R-M, SNIPE, and potentially BREX, DISARM, Zorya, etc.; reviewed in [PMID:37460672](https://pubmed.ncbi.nlm.nih.gov/37460672/)), a term like:

```
Term name: antiviral defense by targeting viral nucleic acid
Definition: A defense response to a virus in which the host targets
  viral nucleic acid for degradation or modification, preventing
  viral replication. Includes systems that act on nucleic acid after
  cell entry (e.g. CRISPR-Cas, restriction-modification) and systems
  that act during genome injection (e.g. SNIPE).
is_a: defense response to virus (GO:0051607)
```

This is optional but would provide a clean home for the growing number of characterized bacterial anti-phage nucleic acid defense systems.

## InterPro2GO strategy for SNIPE

Separately, [IPR025280](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR025280/) / [PF13250](https://www.ebi.ac.uk/interpro/entry/pfam/PF13250/) (SNIPE associated domain, formerly DUF4041) currently has **no GO term mappings**. Because this is a domain entry (not a full-length protein family), direct mapping to catalytic activity or membrane location is likely too broad. A safer approach is:

```
Do NOT map IPR025280 alone to GO:0004520 (DNA endonuclease activity)
Do NOT map IPR025280 alone to GO:0005886 (plasma membrane)
Prefer architecture-aware rules (e.g. IPR025280 + GIY-YIG nuclease + membrane targeting features)
Then map the full architecture to GO:NNNNNNN ; SNIPE defense system [new BP term]
```

This reduces false-positive propagation across the 1,612 proteins in the SNIPE-associated domain family (2,466 taxa) that may not all share the same full mechanism.

### Bioinformatics note

Detailed architecture analysis has been moved to a sibling note:
`go-issue-antiviral-nucleic-acid-defense-bioinformatics.md`.

High-level takeaway: if InterPro2GO mapping is pursued, use an architecture-aware strategy combining `IPR025280` with catalytic and membrane-targeting evidence, rather than mapping `IPR025280` alone.

## GO-CAM plan for SNIPE defense in *E. coli*

A GO-CAM model for the SNIPE defense system against phage λ would capture the causal chain of molecular activities during genome injection. Based on the experimental evidence in [PMID:41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/):

### Activities and gene products

**Host activities:**

| Activity (MF) | Enabled by | Evidence | Key figures |
|---------------|-----------|----------|-------------|
| [GO:0004520](https://amigo.geneontology.org/amigo/term/GO:0004520) DNA endonuclease activity | SNIPE (A0A8T9CRB7) | IDA — E414A mutation abolishes cleavage; ³²P-labelled DNA degradation assay | Fig. 1d, 2d |
| [GO:0003690](https://amigo.geneontology.org/amigo/term/GO:0003690) double-stranded DNA binding | SNIPE (A0A8T9CRB7) | IDA — DUF4041 domain; positively charged surface; ΔDUF4041 loses cytoplasmic DNA localization | Fig. 1g, ExtData 2f |
| [GO:0015578](https://amigo.geneontology.org/amigo/term/GO:0015578) mannose transmembrane transporter activity | ManY (P69801) | background/context — provides the injection site that SNIPE monitors | Fig. 3a,b |
| [GO:0015578](https://amigo.geneontology.org/amigo/term/GO:0015578) mannose transmembrane transporter activity | ManZ (P69805) | background/context — part of injection complex | Fig. 3a,b |
| [GO:0015288](https://amigo.geneontology.org/amigo/term/GO:0015288) porin activity | LamB (P02943) | background/context — outer membrane receptor for phage λ | Fig. 3a |

**Phage activities:**

| Activity (MF) | Enabled by | Evidence | Key figures |
|---------------|-----------|----------|-------------|
| [GO:0051035](https://amigo.geneontology.org/amigo/term/GO:0051035) DNA transmembrane transporter activity (candidate MF for gpH) | gpH / TMP (P03736) | IDA-compatible mechanistic evidence: TMP facilitates λ genome injection across inner membrane; escape mutants map to TMP; TMP interacts with SNIPE | Fig. 3a, 4d, 4e |
| [GO:0046812](https://amigo.geneontology.org/amigo/term/GO:0046812) host cell surface binding | gpJ (P03749) | background — tail tip protein, host specificity/receptor binding | Fig. 3a |

Note: existing BP terms already capture phage genome injection/ejection, including [GO:0039678](https://amigo.geneontology.org/amigo/term/GO:0039678) and [GO:0099001](https://amigo.geneontology.org/amigo/term/GO:0099001). For MF, [GO:0051035](https://amigo.geneontology.org/amigo/term/GO:0051035) may be sufficient for gpH. If GO editors consider this too generic, then a more specific child MF could be discussed. Also note [GO:0046718](https://amigo.geneontology.org/amigo/term/GO:0046718) is currently labeled `symbiont entry into host cell` (with viral-entry synonyms).

### Causal relations

```
PHAGE SIDE:
  gpJ:host cell surface binding
    └─ directly positively regulates →
        gpH:DNA transmembrane transporter activity
          ├─ part_of → GO:0099001 symbiont genome ejection through host cell envelope, long flexible tail mechanism
          ├─ occurs_in → GO:0005886 plasma membrane
          ├─ has input → phage λ genomic DNA
          └─ directly positively regulates →
              SNIPE:DNA binding (DUF4041 binds TMP gpH)
              [phage injection triggers SNIPE engagement]

HOST SIDE (constitutive pre-positioning):
  ManYZ:mannose transmembrane transporter activity
    └─ causally upstream of, positive effect →
        SNIPE:DNA binding
        [SNIPE pre-associates with ManYZ before infection]

DEFENSE:
  SNIPE:DNA binding (DUF4041 binds phage TMP gpH + phage DNA)
    ├─ has input → gpH (P03736)
    ├─ occurs_in → GO:0005886 plasma membrane
    └─ directly positively regulates →
        SNIPE:DNA endonuclease activity (GIY-YIG cleaves phage DNA)
          ├─ has input → phage λ genomic DNA
          ├─ part_of → SNIPE defense system [NEW BP]
          └─ directly negatively regulates →
              gpH:DNA transmembrane transporter activity
              [phage DNA destroyed, infection blocked]
```

The model captures the interplay between phage and host: the phage's own genome injection activity (gpH) is what triggers SNIPE engagement, and SNIPE's nuclease activity in turn negatively regulates that same injection process by destroying the DNA being translocated.

### Key causal logic

1. **ManYZ** provides the genome injection channel in the inner membrane. SNIPE pre-associates with ManYZ *before* infection (TurboID proximity labelling, Fig. 3c; ExtData 4f,g).
2. **Phage λ injects** its genome through ManYZ. The tape measure protein (gpH, P03736) accompanies the DNA.
3. **SNIPE DUF4041 domain** binds the TMP during injection — this positions the nuclease. Evidence: escape mutants all map to TMP (Fig. 4d); SNIPE mutants with enhanced DUF4041 binding show 6-7 log enhanced defense (Fig. 4b); UV crosslinking confirms direct SNIPE-TMP interaction (Fig. 4e).
4. **SNIPE GIY-YIG nuclease** cleaves the incoming phage DNA. Evidence: E414A catalytic mutant loses all defense (Fig. 1d); ³²P-DNA is degraded to <100bp fragments only in SNIPE+ cells (Fig. 2d); CFP-ParB foci (marking phage genome) are reduced ~30-fold (Fig. 2b,c).
5. The infected cell **survives** (direct defense, not abortive infection). Evidence: growth curves show no lysis (Fig. 1b); phage production per cell is unchanged (Fig. 2f).

### ManYZ-independent defense (siphoviruses)

A second, simpler GO-CAM could model SNIPE defense against siphoviruses in ΔmanYZ background, where SNIPE provides weaker defense through direct weak binding to diverse TMPs without ManYZ pre-positioning (Fig. 4a; BASEL collection screen).

### Entities and identifiers for GO-CAM

| Entity | ID | Type | Organism |
|--------|-----|------|----------|
| SNIPE | UniProt:A0A8T9CRB7 | gene product | *E. coli* (wild) |
| ManY | UniProt:P69801 | gene product | *E. coli* K-12 |
| ManZ | UniProt:P69805 | gene product | *E. coli* K-12 |
| LamB | UniProt:P02943 | gene product | *E. coli* K-12 |
| gpH (TMP) | UniProt:P03736 | gene product | phage λ |
| gpJ (tail tip) | UniProt:P03749 | gene product | phage λ |
| phage λ DNA | — | substrate/input | phage λ |
| plasma membrane | GO:0005886 | cellular component | — |
| SNIPE defense system | GO:NNNNNNN [new] | biological process | — |

### Potential additional term needs

- **Optional MF refinement for tape measure proteins**: use [GO:0051035](https://amigo.geneontology.org/amigo/term/GO:0051035) `DNA transmembrane transporter activity` for gpH unless GO editors request a more specific child term for phage tape measure protein-mediated genome translocation.

### Notes on modeling

- The SNIPE-ManYZ interaction is **pre-infection** — it's constitutive positioning, not a response to infection. This is unusual for defense system GO-CAMs and should be modeled as a constitutive `causally upstream of` relation rather than a stimulus-response.
- The phage TMP (gpH) is both a **binding partner** of SNIPE and an **input** to the defense process — it's the specificity determinant that SNIPE recognizes.
- For siphovirus defense without ManYZ, the model is simpler: just SNIPE activities without the ManYZ positioning step.

## Related issues

- [#10994](https://github.com/geneontology/go-ontology/issues/10994) — OTR+NTR: CRISPR biology (Jim Hu's original request, partially addressed)
- [#18727](https://github.com/geneontology/go-ontology/issues/18727) — clearance of foreign intracellular nucleic acids parentage
- [#8796](https://github.com/geneontology/go-ontology/issues/8796) — foreign DNA clearance (original term request by UniProt)

## Key references

- [PMID:41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/) — Saxton DS, DeWeirdt PC, Doering CR, Roney IJ & Laub MT (2026) A membrane-bound nuclease directly cleaves phage DNA during genome injection. *Nature*. doi:10.1038/s41586-026-10207-1
- [PMID:36123438](https://pubmed.ncbi.nlm.nih.gov/36123438/) — Vassallo CN, Doering CR, Littlehale ML, Teodoro GIC & Laub MT (2022) A functional selection reveals previously undetected anti-phage defence systems in the *E. coli* pangenome. *Nat Microbiol* 7:1568-1579.
- [PMID:37460672](https://pubmed.ncbi.nlm.nih.gov/37460672/) — Georjon H & Bernheim A (2023) The highly diverse antiphage defence systems of bacteria. *Nat Rev Microbiol* 21:686-700.
- [PMID:31857715](https://pubmed.ncbi.nlm.nih.gov/31857715/) — Makarova KS et al. (2020) Evolutionary classification of CRISPR-Cas systems: a burst of class 2 and derived variants. *Nat Rev Microbiol* 18:67-83.
