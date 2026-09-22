# SLCO5A1 / OATP5A1 (Q9H2Y9) — curation journal

## Starting position

SLCO5A1 is the most divergent member of the SLCO/OATP (SLC21) family and had no
characterised substrate. GOA before this review held only family-level inference
(`GO:0015291` secondary active transmembrane transporter activity IBA, `GO:0043252`
sodium-independent organic anion transport IBA, `GO:0016323` basolateral plasma membrane
IBA) plus InterPro IEAs, and plasma-membrane CC from three independent IDA sources.

A 2026 paper (PMID:42231149, Cell Mol Biol Lett) reports a substrate set. Everything below
is about how much weight that single study can carry.

## 1. What PMID:42231149 actually did

Stably transfected HEK293 cells overexpressing human OATP5A1 (HEK-OATP5A1) vs vector
control (HEK-VC), characterised by qRT-PCR, immunoblot and immunofluorescence; candidate
substrates from other OATPs screened by uptake; untargeted metabolomics after incubation
with human plasma; then follow-up kinetics.

[PMID:42231149 "uptake assays and untargeted metabolomics analysis identified the hormone
conjugate estrone-3-sulfate, the amino acids glutamine, glycine and tyrosine, the vitamins
pantothenic acid (vitamin B5) and thiamine (vitamin B1) and the nucleotide thymine as
potential OATP5A1 substrates."]

[PMID:42231149 "While estrone-3-sulfate, tyrosine and thiamine were further characterised as
uptake substrates, glutamine and glycine were exported by OATP5A1."]

[PMID:42231149 "For estrone-3-sulfate, tyrosine and thiamine, kinetic transport parameters
(Km values) of 102.2 µM, 169.9 µM and 15.6 µM were calculated, respectively."]

Controls that raise my confidence above "overexpression artefact":

- 4 °C counter-controls for both uptake and efflux:
  [PMID:42231149 "In line with these data, efflux experiments after preloading the cells
  (Fig. 6C and D) demonstrated a highly significant OATP5A1-mediated efflux which is
  significantly reduced in HEK-OATP5A1 cells by performing the same experiments at 4 °C"].
- Pharmacology consistent with the family:
  [PMID:42231149 "Furthermore, OATP5A1-mediated tyrosine uptake could be significantly
  inhibited by BSP, benzbromarone and to a lower extend by rifampicin"].
- Saturable Michaelis–Menten kinetics with six biological replicates, and for thiamine a
  background-depletion design ([PMID:42231149 "Because of the high intracellular background
  of thiamine, cells were cultured in thiamine-free medium before uptake experiments."]).

Reasons for caution, all of which I hold against it:

1. **One lab, one heterologous system.** HEK293 overexpression only; no oocytes, no
   proteoliposomes, no knockdown/knockout in a cell that expresses OATP5A1 endogenously, no
   tissue-level validation.
2. **Direct contradiction with prior work on the flagship substrate.**
   [PMID:42231149 "The hormone conjugate estrone-3-sulfate has been investigated as
   substrate of OATP5A1 before. However, no significantly increased uptake was detected in
   these studies [16, 17]."] The authors' own explanation is system-dependent:
   [PMID:42231149 "The discrepancy to our findings may be owing to the differences in
   experimental conditions, including variations in the investigated concentrations of
   estrone-3-sulfate, as well as the utilisation of different cell systems, such as X.
   laevis oocytes instead of HEK293 cells."] So the very first substrate is already a
   two-against-one disagreement, resolved here in favour of the newer study by the newer
   study.
3. **Affinities are low relative to physiological concentrations.**
   [PMID:42231149 "The Km value for OATP5A1-mediated estrone-3-sulfate transport (102.2 µM)
   is higher than the Km value for estrone-3-sulfate transport by other OATP family members
   (e.g., 0.46 µM for OATP1B1) [32]. This suggests that OATP5A1 is a low-affinity-high-capacity
   transporter of estrone-3-sulfate."] Thiamine's Km (15.6 µM) sits far above plasma thiamine
   (40–120 nM); the authors argue relevance only in the intestinal lumen.
4. **Bidirectionality is unusual for an OATP** but not incoherent. OATPs are widely modelled
   as electroneutral **exchangers**; an obligate antiporter naturally produces net uptake of
   one substrate and net efflux of another in the same cell, and the family-level IBA term
   already on this gene, `GO:0015291` secondary active transmembrane transporter activity, is
   exactly the term that accommodates this. I read the uptake/efflux pattern as *supporting*
   rather than undermining the IBA — but the exchange stoichiometry and counter-ion were not
   determined, so this remains a model, not a result.
5. Several "substrates" are inferred from inhibition only:
   pantothenic acid and thymine inhibited tyrosine uptake but showed no direct uptake because
   of unremovable background. I do **not** annotate those.

## 2. Localisation

Three independent IDA sources for `GO:0005886`, which is unusually good for an orphan:

- This paper, in HEK cells: [PMID:42231149 "Localisation of the OATP5A1 protein was analysed
  by immunofluorescence analysis showing a localisation of the recombinantly expressed
  protein in the plasma membrane of HEK-OATP5A1 cells"] with a Na+/K+-ATPase marker overlay
  ([PMID:42231149 "Membrane localisation of OATP5A1 was confirmed by the yellow colour in the
  overlay."]).
- Endogenous protein in human tissue: [PMID:21278488 "Furthermore, we localized OATP3A1 and
  OATP5A1 to the plasma membrane of epithelial cells of the lactiferous ducts in normal breast
  tissue."] — note the same group (König/Fromm), so not fully independent, but a different
  system and endogenous protein. Also [PMID:21278488 "In breast cancer, both OATPs are highly
  expressed in the plasma membrane and in the cytoplasm."], i.e. a partly intracellular pool.
- HPA immunofluorescence (GO_REF:0000052).

`GO:0016323` **basolateral** plasma membrane is a different matter. Its IBA donors are
SLCO2B1 (O94956), SLCO1B3 (Q9NPD5), SLCO1C1 (Q9NYB5), SLCO3A1 (Q9UIG8), SLCO1B1 (Q9Y6L6),
plus rat and *Drosophila* Oatps — i.e. OATPs characterised in **polarised** epithelia
(sinusoidal/basolateral hepatocyte membrane above all). Nothing in the SLCO5A1-specific
record establishes polarity: HEK293 cells are not polarised, and the breast-tissue study
says "plasma membrane", not "basolateral". This is a granularity/context problem with the
propagated term rather than a wrong node, so MODIFY → `GO:0005886` with a
`propagation_review` of root_cause `TERM_SCOPING_PROBLEM`, not REMOVE.

## 3. How I annotated

Position taken: **the transporter identity is credible; the specific substrate list is
provisional.** Concretely that means keeping the generic MF (`GO:0022857`, `GO:0015291`) as
the annotations that carry the weight, accepting the two curator-made IDA BP terms
(`GO:0006865` amino acid transport, `GO:0015888` thiamine transport) that GOA has already
drawn from this paper, and adding the specific MF terms only as **`NEW` reviewer proposals**
whose `reason` states the single-lab/heterologous limitation explicitly.

| Term | Evidence | Action |
|---|---|---|
| GO:0015291 secondary active transmembrane transporter activity | IBA | ACCEPT (core) |
| GO:0043252 sodium-independent organic anion transport | IBA | ACCEPT |
| GO:0016323 basolateral plasma membrane | IBA | MODIFY → GO:0005886 (+ propagation_review) |
| GO:0005886 plasma membrane | IDA ×3, IEA | ACCEPT |
| GO:0016020 membrane / GO:0022857 / GO:0055085 | IEA | ACCEPT |
| GO:0006865 amino acid transport | IDA | ACCEPT |
| GO:0015888 thiamine transport | IDA | ACCEPT |
| GO:0005302 L-tyrosine transmembrane transporter activity | — | NEW (proposed) |
| GO:0015234 thiamine transmembrane transporter activity | — | NEW (proposed) |
| GO:0015186 L-glutamine transmembrane transporter activity | — | NEW (proposed) |
| GO:0015187 glycine transmembrane transporter activity | — | NEW (proposed) |
| GO:0032973 amino acid export across plasma membrane | — | NEW (proposed) |

Estrone-3-sulfate has no matching MF term in GO (`GO:0015347` sodium-independent organic
anion transmembrane transporter activity and `GO:0008514` organic anion transmembrane
transporter activity are both **obsolete**; curators annotate OATP E3S transport to the
bare `GO:0022857`). Recorded in `proposed_new_terms` instead of forcing a wrong term.

## 4. Open questions carried forward

- Does OATP5A1 transport E3S at all? Two prior oocyte studies say no; one HEK study says yes
  at 102 µM Km. Needs a third system.
- What is the counter-substrate? If OATP5A1 is an exchanger, the Gln/Gly efflux and the
  Tyr/thiamine influx may be two halves of one antiport cycle, which would make several of
  the "substrates" mechanistically interdependent rather than independent.
- Is any of this true at endogenous expression? Brain expression in neurons and astrocytes
  makes the glutamine claim interesting ([PMID:42231149 "Because OATP5A1 is also expressed in
  the human brain, including neuronal cells and astrocytes [18, 19], this efflux could have
  important physiological functions."]) but no endogenous-loss-of-function experiment exists.
