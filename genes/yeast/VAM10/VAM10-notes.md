# VAM10 (YOR068C) — curation notes

Organism: *Saccharomyces cerevisiae* S288C (yeast)
UniProt: Q08474 (VAM10_YEAST); SGD: S000005594; systematic name YOR068C
Protein: 114 aa, ~11.8 kDa; PE=4 (Predicted). Standard name VAM10 = "VAcuole Morphology 10" / "altered vacuole morphology".

## Journal

### 2026-07-05 — setup
- `just fetch-gene yeast VAM10` succeeded on bare symbol; resolved to Q08474. Files: uniprot.txt, goa.tsv, ai-review.yaml stub (4 annotations).
- `just fetch-gene-pmids` — only one PMID cited across GOA: PMID:12748377 (Kato & Wickner 2003). Cached, but **abstract-only** (`full_text_available: false`, PMC access restricted).
- Deep research (falcon) launched in background.

## Domain / sequence analysis (inline, from UniProt record)

Sequence (114 aa):
```
MLFEVFGEVL ASYIVSSKTK GELAFPVNNA PPDSLVAINC VVLFLRSAIG SCSGAKELIR
SSALELSCSS SCGLPATDKP GSFHSGALSK SILSANEAVV SKSSLSFLSS FVDI
```

- **No annotated domain / motif / signal.** UniProt lists a single CHAIN feature (1..114) and no PFAM/InterPro/PROSITE hits; the record has no `DR Pfam`/`DR InterPro` lines. PANTHER family: none found by the fetch pipeline ("No PANTHER family found in UniProt data").
- **No transmembrane segment declared.** UniProt annotates SUBCELLULAR LOCATION as "Vacuole membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}" — i.e. inferred (ECO:0000305), membrane-associated but **peripheral**, not integral. Keyword `Membrane` is present but there is no `TRANSMEM` feature.
- **Composition:** N-terminal ~1–20 is hydrophobic/amphipathic (MLFEVFGEVLASYIVSSKTK); the C-terminal two-thirds is Ser-rich (many S/A/L). No Cys cluster of note (a few scattered C). No coiled-coil is annotated. This is consistent with a small, largely disordered/low-complexity peripheral membrane protein with no catalytic fold — i.e. **no basis to assign an enzymatic molecular function from sequence**.
- **Orthology:** UniProt cross-refs HOGENOM CLU_2122470_0_0_1 (singleton-like cluster), InParanoid Q08474, OrthoDB 10325102at2759. VAM10 is poorly conserved and effectively *Saccharomyces*-restricted / fungal-lineage-narrow; no metazoan ortholog is established. This limits transfer of molecular-function inference from orthologs.
- **Genomic note (from the primary paper):** YOR068C/VAM10 lies **within the VPS5 gene on the opposite DNA strand** [PMID:12748377 abstract, "YOR068c, termed VAM10 (altered vacuole morphology), lies within the VPS5 gene on the opposite DNA strand."]. This nested arrangement is why the gene was historically overlooked and is a caution against confusing VAM10 with VPS5 phenotypes.

**Domain-analysis conclusion:** VAM10 is a small (114 aa) peripheral vacuolar-membrane protein with **no recognizable catalytic or binding domain** and no strong orthology signal. Its molecular activity therefore cannot be inferred from structure and must rest on the single functional study.

## Literature synthesis

Only one functional paper exists (VAM10 is genuinely understudied).

### PMID:12748377 — Kato M, Wickner W. "Vam10p defines a Sec18p-independent step of priming that allows yeast vacuole tethering." PNAS 2003. (abstract-only in cache)

Verbatim abstract statements (from cached `publications/PMID_12748377.md`):
- "YOR068c, termed VAM10 (altered vacuole morphology), lies within the VPS5 gene on the opposite DNA strand."
- "VAM10 deletion causes vacuole fragmentation in vivo." → in-vivo loss-of-function phenotype (basis of IMP GO:0042144).
- "The in vitro fusion of purified yeast vacuoles is stimulated by recombinant Vam10p and blocked by antibody to Vam10p." → Vam10p is a positive-acting factor for homotypic vacuole fusion in a defined in-vitro assay.
- "Vam10p acts early in the priming stage of fusion, independent of Sec18p." → places Vam10p in the priming (pre-docking) stage, but distinct from the canonical Sec18p (NSF)/Sec17p (α-SNAP) SNARE-disassembly priming.
- "After priming, recombinant Vam10p will not stimulate fusion and anti-Vam10p antibodies will not inhibit; Vam10p provides a functional marker for this Sec18p-independent priming step."
- "Pure Vam10p restores normal, Ypt7p-dependent tethering to vacuoles from a vam10Delta strain." → Vam10p is required to establish Ypt7p (Rab GTPase)-dependent tethering; vacuoles lacking it are tethering-deficient.

**Interpretation.** The homotypic vacuole fusion cascade in yeast proceeds priming → tethering → docking (trans-SNARE pairing) → fusion. Canonical priming is Sec18p(NSF)/Sec17p(α-SNAP)-driven SNARE-complex disassembly. Kato & Wickner define a **second, Sec18p-independent priming activity** provided by Vam10p that is a prerequisite for the subsequent Ypt7p-dependent tethering step (tethering is executed by the HOPS complex with the Rab Ypt7p). Vam10p is thus a positive regulator/facilitator that acts upstream of, and enables, HOPS/Ypt7p-mediated tethering.

### KNOWN vs NOT-known

KNOWN (evidence-supported):
- **BP:** required for homotypic (non-autophagic) vacuole fusion; deletion fragments vacuoles in vivo (IMP, PMID:12748377). This is the core biological role.
- **BP/mechanistic placement:** acts at an early, Sec18p-**independent** priming step that is a prerequisite for Ypt7p-dependent tethering (in-vitro reconstitution, PMID:12748377).
- **CC:** vacuolar (fungal-type vacuole) membrane; peripheral membrane protein (IC from SGD, PMID:12748377; UniProt SubCell IEA). Consistent with acting on the vacuole surface during fusion.

NOT-known (genuine gaps — primary deliverable):
- **Molecular function is dark.** No biochemical activity is defined. It is unknown whether Vam10p is an enzyme, a lipid/membrane binder, a protein adaptor/tether, or a regulator of another priming factor. There is no MF beyond the ND root in GOA, and sequence gives no fold-level clue.
- **Direct binding partner(s) unknown.** Vam10p enables Ypt7p-dependent tethering but it is not established whether it binds Ypt7p, the HOPS complex, a SNARE, a lipid, or acts indirectly. The molecular target of the "Sec18p-independent priming" is undefined.
- **Mechanism of the Sec18p-independent priming step is unknown.** What conformational/compositional change on the vacuole membrane Vam10p produces to license tethering is undetermined.
- **Structure unknown** (PE=4 predicted; AlphaFoldDB model exists but no experimental structure, and the protein is largely low-complexity).
- **Conservation/orthology of function** across fungi and beyond is uncharacterized.

## Annotation-by-annotation plan

1. `GO:0005774 vacuolar membrane` / located_in / IEA / GO_REF:0000044 (UniProt SubCell) — ACCEPT (non-core supporting CC; consistent with IC vacuole-membrane call). Same location as the more specific SGD term below.
2. `GO:0000329 fungal-type vacuole membrane` / located_in / IC / PMID:12748377 — ACCEPT. Species-appropriate (fungal-type vacuole) refinement of the CC; IC from the functional study. This is the informative CC and can back the core-function location.
3. `GO:0003674 molecular_function` (root) / enables / ND / GO_REF:0000015 — this is the explicit "no known MF" placeholder. Keep but not core; represents the real MF_DARK gap. Action: ACCEPT (honest ND root; do NOT invent an MF).
4. `GO:0042144 vacuole fusion, non-autophagic` / involved_in / IMP / PMID:12748377 — ACCEPT as the CORE biological process (deletion → vacuole fragmentation; recombinant protein stimulates in-vitro fusion). Well supported.

Avoid `protein binding` (not present here anyway). Do not assign a specific tether/priming MF term — none fits the undefined activity; record it as a knowledge gap instead.

Core function: single BP-centered core (vacuole fusion / early Sec18p-independent priming enabling Ypt7p-dependent tethering) at the fungal-type vacuole membrane, with molecular_function left at the root (MF_DARK) and the mechanism captured under knowledge_gaps.

### 2026-07-05 — falcon deep research completed (corroboration)

Falcon (Edison Scientific) deep research completed after ~27 min (`VAM10-deep-research-falcon.md`, 21 citations). It corroborates the review and adds context (citations in falcon's `keyname pages N-N` style, which the reference validator skips, so NONE are quoted into the YAML; all YAML supporting_text remains verbatim from the cached PMID:12748377 abstract):
- VAM10/YOR068C identified in the Seeley et al. (2002) genome-wide FM4-64 vacuole-morphology screen; vam10Δ shows a class B fragmentation phenotype in ~90% of cells (Seeley, Kato, Wickner, Eitzen 2002).
- **VAM10 is NOT a HOPS subunit.** The six original VAM genes that are HOPS subunits are VAM1/VPS11, VAM2/VPS41, VAM5/VPS33, VAM6/VPS39, VAM8/VPS18, VAM9/VPS16; VAM3/VAM7 are SNAREs; VAM4 = the Rab Ypt7p. Vam10p is instead an "additional fusion factor" acting in a Sec18p-independent priming step upstream of HOPS/Ypt7p-mediated tethering. (This is why the review frames VAM10 as acting upstream of, and enabling, HOPS/Ypt7p tethering — not as a HOPS component.)
- Molecular mechanism still unknown: enzyme vs scaffold vs regulator undetermined; no crystal/cryo-EM structure; interaction partners not comprehensively mapped — matches the MF_DARK and partner knowledge gaps recorded.
- vam10Δ does not show a strong VPS/CPY-secretion sorting phenotype, consistent with a role specific to homotypic vacuole fusion rather than biosynthetic trafficking; the VPS5-proximity caveat is noted but in-vitro biochemistry supports a direct Vam10p role.

No annotation actions changed as a result; falcon strengthens the ACCEPT calls and the honesty of the knowledge-gaps section.
