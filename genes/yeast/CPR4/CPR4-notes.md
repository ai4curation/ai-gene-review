# CPR4 (S. cerevisiae, YCR069W, P25334) — curation notes

Journal of research for the AI GO-annotation review. Inline provenance uses
`[PMID:xxxx "verbatim supporting text"]`.

## Identity (verified)

- UniProt: **P25334** `CYPR_YEAST`, "Peptidyl-prolyl cis-trans isomerase CPR4",
  EC 5.2.1.8, AltName Rotamase, **Flags: Precursor** (has signal peptide).
- Gene: **CPR4**; Synonyms **CYP4, SCC3**; systematic name **YCR069W** (chromosome III).
- SGD: S000000665. PANTHER family PTHR11071 (Cyclophilin-type PPIase),
  subfamily **PTHR11071:SF568 "PEPTIDYL-PROLYL CIS-TRANS ISOMERASE CPR4-RELATED"**.
- Length 318 aa, MW 35.8 kDa.
- PE level: `PE 3: Inferred from homology` — UniProt has **no direct experimental
  evidence** for CPR4 protein existence/function; identity/function is homology-based.
- Originally cloned/sequenced as **SCC3** ("S. cerevisiae cyclophilin 3"), the third
  cyclophilin-homologous gene found in budding yeast [PMID:1803821, Franco et al. 1991].

CPR4 is one of eight cyclophilins in S. cerevisiae (CPR1–CPR8). Its closest paralog is
**CPR8** (P53728, CYP8); both are the yeast "cyclophilin C (CypC)"-type / vacuolar cyclophilins
and share PANTHER subfamily SF568 (verified in
`interpro/panther/PTHR11071/PTHR11071-entries.csv`: both P25334/CPR4 and P53728/CPR8 map to
SF568 "CPR4-RELATED"). [PMID:15998457 "Cpr4 and Cpr8 contain a single CLD domain plus a long
amino-terminal signal peptide and are located in vacuoles"]. Dolinski et al. describe Cpr8 as
"a homolog of the secretory pathway cyclophilin Cpr4" [PMID:9371805].

## Domain architecture (verified from UniProt FT + inline sequence analysis)

- **SIGNAL 1..20** (ECO:0000255) — N-terminal cleavable signal peptide → ER / secretory targeting.
- **CHAIN 21..318** mature protein.
- **DOMAIN 55..225** "PPIase cyclophilin-type" (PROSITE PRU00156).
- **TRANSMEM 286..303** "Helical" (ECO:0000255) — a single C-terminal transmembrane helix.
- **CARBOHYD 166** N-linked glycosylation site (ECO:0000255) → consistent with lumenal topology.
- Keywords: Glycoprotein; Isomerase; Membrane; Rotamase; Signal; Transmembrane; Transmembrane helix.

Franco et al. 1991 described exactly this dual topology from sequence:
[PMID:1803821 "contains two hydrophobic cores, one at the amino terminal, 20 amino acids long,
which could serve as a signal peptide, and the other one at the carboxyl end with a structure
similar to a transmembrane helix"] and concluded [PMID:1803821 "Scc3 could be a secretory or,
more likely, a transmembrane protein"]. UniProt SUBCELLULAR LOCATION: "Membrane; Single-pass
membrane protein" (ECO:0000305, an inference, not experimental).

## Catalytic-residue / CsA-pocket analysis (inline, this review)

I compared the CPR4 cyclophilin domain to human cyclophilin A (PPIA, P62937), whose
catalytic/CsA-contact residues are well established.

**Catalytic core motifs are PRESENT and correctly positioned within the 55–225 domain:**
`NNFAML` (pos 82), `HTYSYR` (104), `GPFTVYGP` (132), `FGPD` (161), `GQITSG` (190), `RFLYFV` (219).
These correspond to conserved cyclophilin catalytic/substrate-binding elements → PPIase
catalytic machinery is intact → **PPIase (GO:0003755) is domain-defensible**.

**NOTABLE DIVERGENCE — the conserved CsA-binding tryptophan is ABSENT.**
Human CypA has a single Trp, W121, in `FICTAKTE`**W**`LDGKHVV`; W121 lines the cyclosporin-A
pocket and is a key CsA contact. The homologous region in CPR4 is `IITTKAD`**GNE**`ELDGK` —
no Trp in the entire cyclophilin domain (the protein's only Trp is W2, in the signal peptide).
Whole-domain Trp count = 0. This is **independently corroborated** by Franco et al. as reported
in the deep-research synthesis: the W121-equivalent is replaced by glutamate in Scc3/CPR4
(a W121E-type substitution) [file:yeast/CPR4/CPR4-deep-research-falcon.md, citing Franco 1991].
Interpretation: CPR4 likely has **reduced/altered cyclosporin-A binding** relative to canonical
cyclophilins, even though the PPIase catalytic residues are conserved. In human CypA, W121→F/A
lowers CsA affinity 75–200-fold but PPIase activity only 2–13-fold, showing the two are
structurally separable. (This is a sequence-based prediction; CPR4 CsA binding is untested.)

## NinaA structural parallel (functional hypothesis, not established for CPR4)

The only cyclophilin sharing CPR4's dual topology (N-terminal signal peptide + C-terminal TM +
central CLD) is *Drosophila* **NinaA**, a membrane-anchored, secretory-pathway cyclophilin
required for correct folding and ER→Golgi transport of rhodopsin. Franco 1991
[PMID:1803821 "The only cyclophilin with similar structure to that of Scc3 is ninaA from
Drosophila melanogaster, a transmembrane protein which seems to be implicated in the correct
folding and/or intercalation of rhodopsin in the endoplasmic reticulum of the fly
photoreceptors"] and [PMID:1803821 "the amino and the carboxy regions of Scc3 and ninaA share
a significant level of homology, which suggests that they have a similar function, albeit for
different target proteins"]. NinaA is a CypC ortholog [PMID:15998457 "A retina-specific
cyclophilin of the fruit fly Drosophila melanogaster, NinaA (an ortholog of mammal CypC), is
crucial for the folding of rhodopsin isoforms"]. This motivates a hypothesis that CPR4 is a
membrane-anchored, substrate-specific foldase for secretory/membrane clients — but yeast has no
rhodopsins and CPR4's substrates are unknown.

## What is KNOWN vs NOT known about CPR4 specifically

### KNOWN (or well-supported)
1. CPR4 is a cyclophilin-family PPIase by sequence/homology (UniProt, PANTHER, InterPro,
   Pfam PF00160, CDD cd00317). Catalytic residues intact (this review). EC 5.2.1.8.
2. Signal peptide + C-terminal TM helix → a **secretory-pathway / ER, membrane** cyclophilin
   [PMID:1803821; PMID:15998457]. Dolinski et al. call it "the secretory pathway cyclophilin
   Cpr4" [PMID:9371805].
3. CPR4 is **non-essential**. None of the eight yeast cyclophilins (nor an octuple mutant) is
   essential; little/no functional redundancy [PMID:15998457 "none of the eight individual
   cyclophilins was found to be essential in S. cerevisiae"; "an octuplet mutant lacking all
   eight cyclophilins was viable and that there was little or no evidence for functional
   redundancy"]; corroborated for all 12 immunophilins in [PMID:9371805 "None of the eight
   cyclophilins or four FKBPs were essential"; "yeast mutants lacking all 12 immunophilins were
   viable"].
4. **Localization**: Wang & Heitman 2005 place Cpr4 (and Cpr8) in **vacuoles** [PMID:15998457
   "Cpr4 and Cpr8 ... are located in vacuoles"]. SGD HDA (systematic microscopy) also assigns
   the fungal-type vacuole (GO:0000324) [PMID:26928762 source dataset]. Family-level IBA instead
   assigns ER (GO:0005783)/cytoplasm. So localization data are partly discordant (vacuole vs ER);
   both are within the secretory/endomembrane system and not mutually exclusive for a protein
   that transits the ER en route to the vacuole. PMID:26928762 is a genome-wide library/methods
   paper and does not discuss CPR4 individually.

### NOT known (genuine gaps)
- **No physiological in-vivo substrate/client of CPR4 is known.** Dolinski et al. conclude
  immunophilin physiological functions are "largely unknown" and that each "regulates a
  restricted number of unique partner proteins that remain to be identified"
  [PMID:9371805 "the physiological functions of these proteins are largely unknown";
  "regulates a restricted number of unique partner proteins that remain to be identified"].
- **Whether CPR4's PPIase activity is measured / required in vivo** — no direct biochemical
  measurement of CPR4 PPIase kinetics or substrate specificity has been reported (deep research).
- **Redundancy with CPR8** (its SF568 paralog) or with other ER/secretory folding factors —
  untested; viability data show little redundancy but substrate-level redundancy is unexplored.
- **CsA binding of CPR4 specifically** — untested; predicted atypical (missing W121-equivalent).
- **The NinaA-analogous foldase hypothesis** — plausible from topology/homology but never
  experimentally validated in yeast.
- No specific biological process is experimentally assigned; GOA carries an explicit ND
  "biological_process" root annotation (GO_REF:0000015).

## Annotation-by-annotation plan (8 GOA rows)

1. GO:0003755 PPIase, IBA (GO_REF:0000033), enables → **ACCEPT** (core MF; catalytic residues intact).
2. GO:0005783 endoplasmic reticulum, IBA, is_active_in → **KEEP_AS_NON_CORE**: architecture
   (signal peptide + TM) supports secretory/ER; note vacuole is the more specific experimental call.
3. GO:0006457 protein folding, IBA, involved_in → **ACCEPT** as general family-level BP; no
   CPR4-specific in-vivo process known → keep general.
4. GO:0003755 PPIase, IEA (GO_REF:0000120 InterPro/EC), enables → **ACCEPT** (redundant MF confirmation).
5. GO:0016020 membrane, IEA (GO_REF:0000044 SubCell), located_in → **KEEP_AS_NON_CORE**:
   C-terminal TM helix supports membrane; general term.
6. GO:0000324 fungal-type vacuole, HDA (PMID:26928762), located_in → **KEEP_AS_NON_CORE**
   (experimental localization; concordant with Wang&Heitman vacuole; do not remove).
7. GO:0003755 PPIase, ISS (PMID:9371805), enables → **ACCEPT** (ISS from a cyclophilin homolog; MF consistent).
8. GO:0008150 biological_process (root), ND (GO_REF:0000015) → **ACCEPT** (honest "no specific BP known" placeholder).

## References
- PMID:1803821 — Franco et al. (1991) Yeast. Original SCC3/CPR4 cloning+sequence; dual topology;
  NinaA parallel. Abstract-only in cache. HIGH relevance (primary source for identity/topology).
- PMID:9371805 — Dolinski, Muir, Cardenas, Heitman (1997) PNAS. Immunophilin knockouts;
  non-essentiality; "unknown physiological function / unique partners." Abstract-only. HIGH.
- PMID:15998457 — Wang & Heitman (2005) Genome Biology "The cyclophilins." Full text. Cpr4/Cpr8
  vacuolar localization; octuple-mutant viability; NinaA=CypC. HIGH (review, direct CPR4 statements).
- PMID:15353296 — Arévalo-Rodríguez et al. (2004) Front Biosci "Prolyl isomerases in yeast."
  Abstract-only. MEDIUM (review context).
- PMID:26928762 — Yofe et al. (2016) Nat Methods, SWAT. Source of HDA vacuole datapoint; does not
  discuss CPR4 individually. MEDIUM (localization datapoint).
- file:yeast/CPR4/CPR4-deep-research-falcon.md — Falcon deep research synthesis. Used for the
  W121E-equivalent corroboration and general synthesis; independently consistent with my
  UniProt/sequence analysis.
</content>
