# ERR1 (YOR393W) curation notes

Gene: **ERR1** — Enolase-related protein 1
UniProt: **P0CX10** (ERR1_YEAST); SGD: S000005920; systematic name YOR393W.
Organism: *Saccharomyces cerevisiae* S288C (NCBITaxon:559292).
Protein existence level: **PE 3 — Inferred from homology** (no direct experimental
characterization of the protein itself).

This is an understudied ("dark") gene. The primary curation goal is an honest
`knowledge_gaps` section plus carefully-reasoned `core_functions`/`description`
grounded in domain architecture, orthology, and the (sparse) literature — never
invented function.

---

## 1. Paralog landscape — critical for evidence attribution

*S. cerevisiae* has three "Enolase-Related Region" (ERR) genes plus the two true
glycolytic enolases:

| Gene | UniProt | Systematic name | SGD | Length |
|------|---------|-----------------|-----|--------|
| ERR1 | P0CX10  | YOR393W         | S000005920 | 437 aa |
| ERR2 | P0CX11  | YPL281C         | S000006202 | 437 aa |
| ERR3 | P42222  | YMR323W         | S000004942 | 437 aa |
| ENO1 | P00924  | YGR254W         | S000003486 | 437 aa |
| ENO2 | P00925  | YHR174W         | S000001217 | 437 aa |

**Sequence identities I computed inline (ungapped, all sequences are exactly 437 aa
with no indels — enolase is a highly conserved rigid TIM-barrel fold):**

- ERR1 vs **ERR2 = 100.0%** identical (the two proteins are the *same* sequence; this
  is why UniProt merged YOR393W and YPL281C into a single accession P0CX10 carrying
  two OrderedLocusNames and two EnsemblFungi/KEGG mRNA cross-references).
- ERR1 vs **ERR3 = 99.5%** identical (only 2 residue differences over 437).
- ERR1 vs **ENO1 = 68.0%** identical.
- ERR1 vs **ENO2 = 67.3%** identical.

**Consequence:** the three ERR proteins are functionally indistinguishable at the
protein level. No protein-level, sequence-based, or most biochemical assays could
attribute a phenotype specifically to *ERR1* rather than *ERR2/ERR3*. Only
locus-specific genetics (deletion of the specific ORF, allele-specific expression)
could do so, and I have found no such ERR1-specific functional study. Any functional
claim from the literature (or from IBA/ISA propagation) is really a claim about the
ERR family, not ERR1 uniquely.

Foundational reference: Pryde, Huckle & Louis 1995 [PMID:7785338, "The first of
these shows 61%\nand 60% DNA sequence identity to Enolases 1 and 2 respectively. The
Enolase-like\nsequence appears to be species specific, with three copies being found
in all\nstrains of S. cerevisiae studied. The location of the three copies is the same\nfor
all strains."]. Note: this reference is **abstract-only** in our cache
(`full_text_available: false`) and reports DNA (not protein) identity and genomic
location — it does NOT assay enzymatic activity.

---

## 2. Domain architecture and catalytic-residue analysis (inline, from UniProt)

UniProt P0CX10 annotates a complete two-domain enolase architecture:
- Enolase N-terminal domain (Pfam PF03952 Enolase_N; IPR029017)
- Enolase C-terminal TIM-barrel domain (Pfam PF00113 Enolase_C; IPR020810)
- PANTHER PTHR11902 (ENOLASE), CDD cd03313 enolase, PROSITE PS00164 ENOLASE,
  HAMAP MF_00318 Enolase, SFLD enolase.
- KW: Glycolysis, Lyase, Magnesium, Metal-binding.

UniProt catalytic/binding features (all `ECO:0000250`, i.e. by-similarity, not
experimental):
- ACT_SITE 212 "Proton donor" (Glu)
- ACT_SITE 346 "Proton acceptor" (Lys)
- BINDING 160, 169 substrate
- BINDING 247 Mg(2+)
- BINDING 296 Mg(2+)/substrate
- BINDING 321 Mg(2+)/substrate
- BINDING 373–376 substrate; 397 substrate

**Catalytic-residue conservation check I ran inline (ERR1 vs ENO2, position-matched
because both are 437 aa, no indels):**

| Pos | ERR1 | ENO2 | Role |
|-----|------|------|------|
| 212 | E | E | proton donor (ACT_SITE) |
| 346 | K | K | proton acceptor (ACT_SITE) |
| 160 | H | H | substrate binding |
| 169 | E | E | substrate binding |
| 247 | D | D | Mg2+ binding |
| 296 | E | E | Mg2+/substrate binding |
| 321 | D | D | Mg2+/substrate binding |
| 397 | K | K | substrate binding |

**All 8 annotated catalytic / Mg-binding / substrate-binding residues are identical
between ERR1 and ENO2.** The canonical enolase catalytic machinery (Glu proton donor,
Lys proton acceptor, the D/E/D Mg2+ triad) is fully intact. ERR1 is therefore **NOT a
degenerate pseudoenzyme** — it retains every residue required for phosphopyruvate
hydratase (enolase) catalysis. This makes the *molecular-function* annotations
(phosphopyruvate hydratase activity GO:0004634; magnesium ion binding GO:0000287)
**domain-defensible** as a prediction.

**But** conserved catalytic residues establish *capacity*, not *in-vivo activity or
role*. The gap is physiological, not structural (see §4).

---

## 3. What is KNOWN vs NOT KNOWN

### KNOWN (well supported)
- ERR1 is a member of the enolase family with a complete, catalytically-intact enolase
  fold (domain analysis + residue conservation above).
- There are three near-identical ERR paralogs at conserved sub-telomeric loci, present
  in all S. cerevisiae strains examined; the family is *S. cerevisiae*-specific
  (Pryde et al. 1995, PMID:7785338).
- By homology to ENO1/ENO2, the predicted activity is 2-phospho-D-glycerate
  hydro-lyase (EC 4.2.1.11): (2R)-2-phosphoglycerate = phosphoenolpyruvate + H2O,
  Mg2+-dependent.

### NOT KNOWN (genuine gaps)
- **Whether ERR1 is catalytically active as an enolase in vivo.** No purified-protein
  enzyme assay attributable specifically to ERR1 exists. PE level is 3 (homology).
- **The in-vivo biological role.** Deleting ENO1+ENO2 is what impairs glycolysis;
  the ERR genes are not part of the characterized core glycolytic machinery. Whether
  ERR1 contributes measurably to glycolytic flux under any standard condition is
  undetermined.
- **The expression condition.** If ERR1 is expressed at all, under what
  condition/stage? (The ERR family has been discussed in the context of sporulation
  in the broader literature, but I have not verified an ERR1-specific expression
  dataset in our cache; do not assert this without provenance.)
- **Redundancy / non-redundancy vs ERR2, ERR3, and vs ENO1/ENO2.** Because ERR1 =
  ERR2 (100%) and ~ERR3 (99.5%), any function is almost certainly shared across the
  ERR trio; whether the trio does anything the true enolases do not is unknown.
- **Subcellular localization** is undetermined (GOA carries an ND cellular_component
  annotation). Cytosol is the default expectation for a glycolytic-type enzyme (no
  signal peptide/TM in the sequence), but this is not experimentally established for
  ERR1.

---

## 4. Annotation-by-annotation reasoning (GOA has 10 lines)

All ten GOA lines derive from **homology/electronic/phylogenetic** inference or are
ND placeholders — there is **no experimental (IDA/IMP/IPI/IGI) annotation** for ERR1.

1. `GO:0004634 phosphopyruvate hydratase activity` / IBA (GO_REF:0000033) — enables.
   Phylogenetic propagation from the enolase PANTHER family (PTN000224401), with
   ENO1/ENO2 among the source genes. Domain-defensible (residues intact). **ACCEPT**
   as the core predicted MF; but note it is inference, not measured for ERR1.
2. `GO:0006096 glycolytic process` / IBA (GO_REF:0000033) — involved_in. Propagated
   BP. The MF is defensible; the *process* (that ERR1 actually participates in
   glycolysis in vivo) is exactly the unproven physiological claim. **KEEP_AS_NON_CORE**
   — retain the family-level expectation but flag it is not established that ERR1
   contributes to glycolytic flux (it is not one of the two characterized glycolytic
   enolases). This is the honest treatment for a dark paralog.
3. `GO:0000015 phosphopyruvate hydratase complex` / IBA (GO_REF:0000033) — part_of.
   Enolase functions as a homodimer/oligomer = the phosphopyruvate hydratase complex.
   For a catalytically-competent enolase this CC is reasonable **but** whether ERR1
   forms/joins such a complex in vivo is unverified. **KEEP_AS_NON_CORE**.
4. `GO:0000015 phosphopyruvate hydratase complex` / IEA (GO_REF:0000002, InterPro) —
   part_of. Same term via InterPro IPR000941. Redundant electronic support for #3.
   **KEEP_AS_NON_CORE**.
5. `GO:0000287 magnesium ion binding` / IEA (GO_REF:0000002, InterPro) — enables.
   Mg2+ is the enolase cofactor; the three Mg-binding residues are conserved in ERR1
   (D247/E296/D321). Domain-defensible. **ACCEPT**.
6. `GO:0004634 phosphopyruvate hydratase activity` / IEA (GO_REF:0000120) — enables.
   Combined automated (ARBA/EC/RHEA/InterPro). Redundant with #1/#8. **ACCEPT** (same
   MF, electronic).
7. `GO:0006096 glycolytic process` / IEA (GO_REF:0000120) — involved_in. Redundant
   with #2, electronic. **KEEP_AS_NON_CORE** (same reasoning as #2).
8. `GO:0004634 phosphopyruvate hydratase activity` / ISA (PMID:7785338;
   with SGD:S000001217 ENO1, SGD:S000003486 ENO2) — enables. Sequence-similarity
   annotation from SGD based on the Pryde 1995 identity to ENO1/ENO2. The reference
   supports *sequence similarity*, and the MF is domain-defensible. **ACCEPT**, but
   note the supporting paper reports DNA identity + genomic location only (abstract
   states "61% and 60% DNA sequence identity to Enolases 1 and 2"), not enzyme assay.
   Per curation rules: do NOT REMOVE an ISA annotation on paralog grounds; the MF
   inference is sound.
9. `GO:0005575 cellular_component` / ND (GO_REF:0000015) — is_active_in. Root-term ND
   placeholder = "no data". Standard practice is to keep as-is. **ACCEPT** (it
   correctly records the absence of CC data).
10. `GO:0008150 biological_process` / ND (GO_REF:0000015) — involved_in. Root-term ND
    placeholder. **ACCEPT** (records absence of BP data).

No `protein binding` terms present (good). No experimental annotations to protect from
over-ruling. No negated/isoform annotations.

---

## 5. Provenance discipline

- Sequence identities and catalytic-residue table in §1–2 are computed inline in this
  session from UniProt sequences (P0CX10 ERR1, P00925 ENO2, P00924 ENO1, P0CX11 ERR2,
  P42222 ERR3). These are recorded as a `file:` bioinformatics-style provenance
  anchored to the UniProt record; the core numeric claims (100% ERR1=ERR2, all
  catalytic residues conserved) are reproducible from the sequences in the UniProt
  files.
- The only literature reference in GOA is PMID:7785338 (abstract-only). Quotes used in
  the review are verbatim substrings of the cached abstract.
- Falcon deep research was requested; if/when it returns it is kept as
  `ERR1-deep-research-falcon.md`. It must NOT be used to fabricate ERR1-specific
  experimental claims — the paralog-indistinguishability point above stands regardless.

## 6. Deep research status (falcon unavailable)

Falcon deep research (`just deep-research-falcon yeast ERR1 --fallback perplexity-lite`)
was launched at the start of the session and ran for ~24 minutes with **zero output**
before the wrapper gave up; a single bounded retry (8-min hard timeout) was then
attempted per protocol and also returned nothing (SIGTERM/exit 143). No
`ERR1-deep-research-*.md` file was produced. The Edison/falcon endpoint was effectively
hanging today. Per project rules I did NOT fabricate a `-deep-research-{provider}.md`
file. This review is therefore grounded entirely in:
  - the UniProt record P0CX10 (domain architecture, catalytic residues, PE level),
  - the QuickGO GOA export (the 10 existing annotations),
  - the one cached primary reference PMID:7785338 (abstract-only), and
  - inline sequence/catalytic-residue analysis run in this session (ERR1 vs
    ENO1/ENO2/ERR2/ERR3).
The paralog-indistinguishability and dark-gene conclusions do not depend on deep
research; the honest `knowledge_gaps` section captures exactly what remains unknown.
