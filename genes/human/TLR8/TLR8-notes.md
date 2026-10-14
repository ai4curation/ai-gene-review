# TLR8 (human, Q9NR97) — curation notes

Batch 1 of the INNATE_IMMUNITY project (Toll/TLR axis). Reviewed immediately after
TLR7 (Q9NYK1), with which TLR8 shares its PAINT node, most of its electronic
annotations, and several references.

**Deep research:** `TLR8-deep-research-falcon.md` (Edison/Falcon) was produced and
read. Its citation keys are internal document handles rather than PMIDs, so it is
used here only for orientation; every claim below is anchored to a cached
publication in `publications/`.

## What TLR8 is

Endosomal single-pass type I membrane pattern-recognition receptor of the same
subfamily as TLR7 and TLR9: LRR ectodomain, one transmembrane helix, cytoplasmic
TIR domain. It is the most highly expressed nucleic-acid-sensing TLR in the human
myeloid compartment.

- [PMID:31778653 "TLR8 is among the highest-expressed pattern-recognition
  receptors in the human myeloid compartment"]

**Ligands: uridine plus a short oligonucleotide, at two sites.**
- [PMID:25599397 "TLR8 recognized two degradation products of ssRNA—uridine and a
  short oligonucleotide—at two distinct sites: uridine bound the site on the
  dimerization interface where small chemical ligands are recognized, whereas short
  oligonucleotides bound a newly identified site on the concave surface of the TLR8
  horseshoe structure."]
- [PMID:25599397 "Site-directed mutagenesis revealed that both binding sites were
  essential for activation of TLR8 by ssRNA."]
- [PMID:25599397 "These results demonstrate that TLR8 is a sensor for both uridine
  and a short oligonucleotide derived from RNA."]

Both ligands are generated in situ by RNase T2:
- [PMID:31778653 "This is due to RNase T2's preferential cleavage of
  single-stranded RNA molecules between purine and uridine residues, which
  critically contributes to the supply of catabolic uridine and the generation of
  purine-2',3'-cyclophosphate-terminated oligoribonucleotides."]
- [PMID:31778653 "Thus-generated molecules constitute agonistic ligands for the
  first and second binding pocket of TLR8."]

Note the contrast with TLR7, which matters for the ligand-specific pathway terms:
TLR7's site 1 takes **guanosine**, TLR8's takes **uridine**, and TLR7 has a second
site absent from TLR8 [PMID:27742543]. The two receptors nonetheless share
synthetic agonists (R-848) [PMID:12032557].

**Viral ssRNA.**
- [PMID:14976262 "By using Toll-like receptor (TLR)-deficient mice and genetic
  complementation, we show that murine TLR7 and human TLR8 mediate species-specific
  recognition of GU-rich ssRNA."]
- [PMID:33718825 "Here, we show that GU-rich single-stranded RNA (GU-rich RNA)
  derived from SARS-CoV-2, SARS-CoV-1, and HIV-1 trigger a TLR8-dependent
  pro-inflammatory cytokine response from human macrophages in the absence of
  pyroptosis"]

**Activation mechanism: Z-loop cleavage then ligand-induced dimer reorganisation.**
- [PMID:26929371 "TLR8 with the uncleaved Z-loop is unable to form a dimer, which
  is essential for activation, irrespective of the presence of agonistic ligands."]
- [PMID:23520111 "Upon ligand stimulation, the TLR8 dimer was reorganized such
  that the two C termini were brought into proximity."]
- [PMID:25297876 "Both furin-like proprotein convertase and cathepsins contribute
  to TLR8 cleavage in the early/late endosomes."]

**Localisation: early endosome and ER — explicitly not late endosome, lysosome or
Golgi.** This is the sharpest difference from TLR7/TLR9 and the main reason several
location rows were demoted.
- [PMID:22164301 "we demonstrate that TLR8 localized to the early endosome and the
  ER but not to the late endosome or lysosome in human monocytes and HeLa
  transfectants"]
- [PMID:22164301 "Late endosome (MPR), lysosome (LAMP-1), and Golgi (p115) markers
  did not colocalize with TLR8"]
- [PMID:22164301 "Thus, the localization site of TLR8 differed from TLR7 and TLR9,
  both of which reside in the endolysosome and the ER."]
- [PMID:22164301 "UNC93B1 physically associated with human TLR8, similar to TLRs 3,
  7, and 9, and played a critical role in TLR8-mediated signaling."]

**Disease.** X-linked gain-of-function variants cause IMD98 (neutropenia,
lymphoproliferation, autoinflammation, bone-marrow failure), mostly as somatic
mosaicism.
- [PMID:33512449 "All variants conferred gain of function to TLR8 protein, and
  immune phenotyping demonstrated a proinflammatory phenotype with activated T
  cells and elevated serum cytokines associated with impaired B-cell maturation."]

## Annotation-level findings

1. **Localisation rows contradicted by PMID:22164301.** The two `GO:0000139 Golgi
   membrane` Reactome TAS rows and the two `GO:0036020 endolysosome membrane` rows
   (ARBA IEA + Reactome TAS) assert compartments in which endogenous TLR8 was
   explicitly *not* found in human monocytes. They are marked
   MARK_AS_OVER_ANNOTATED, with `GO:0031901 early endosome membrane` proposed for
   the endolysosome rows. `GO:0010008 endosome membrane` (EXP, IEA, two Reactome
   rows) and the ER membrane Reactome rows are accepted.

2. **`GO:0009897 external side of plasma membrane` (IDA, PMID:24942581) is
   contradicted by the paper it cites.** The cached record is abstract-only, so I
   retrieved the open PMC full text (PMC4136363). TLR8 *is* assayed there — 26
   mentions — which is exactly why the row cannot be dismissed as a wrong
   identifier. But the measurement is explicitly intracellular: "Intracellular TLR8
   staining was performed using the Cytofix/Cytoperm Fixation/Permeabilization
   Solution Kit", and the discussion speaks of "the increase in expression of
   pattern recognition receptors such as intracellular TLR8". The same paper's two
   other TLR8 rows (`GO:0034158`, `GO:0003727`) are supported by its ssRNA40
   stimulation experiments and are accepted; the surface-location row is REMOVEd.

3. **`GO:0003725 double-stranded RNA binding`, two IDA rows.** PMID:33718825 used
   GU-rich *single-stranded* RNA throughout (its abstract says so), and PMID:16111635
   is the nucleoside-modification study of RNA sensing. TLR8's structurally defined
   sites bind uridine and a short oligonucleotide [PMID:25599397]. Both rows MODIFY
   to `GO:0003727 single-stranded RNA binding`, which TLR8 already carries.

4. **`GO:0003677 DNA binding` (IDA, PMID:16123302).** The Treg-reversal paper used
   "synthetic and natural ligands for human TLR8"; DNA sensing is TLR9's function,
   and the TLR8 ligand-binding sites are defined for uridine and short RNA
   oligonucleotides. Cached record is abstract-only, so the row is not removed on
   an unverifiable mis-attribution claim; it is marked MARK_AS_OVER_ANNOTATED.
   `GO:0003723 RNA binding` (TAS, same paper) MODIFYs to the informative
   `GO:0003727`.

5. **`GO:0016064 immunoglobulin mediated immune response` (TAS, PMID:16123302).**
   The cited paper concerns reversal of CD4+ regulatory T cell suppression; nothing
   in it bears on immunoglobulin-mediated immunity, and TAS is not experimental
   evidence to defer to. REMOVE.

6. **Type II interferon.** As for TLR7, the `IDA PMID:16286015` row rests on a paper
   measuring IFN-alpha/beta and IFN-lambda only, so it MODIFYs to `GO:0034346
   positive regulation of type III interferon production` (the decision already
   taken in the TLR9 review). Unlike TLR7 — where PMID:32706371 shows IFN-gamma
   loss in TLR7-deficient patients — there is no TLR8-specific IFN-gamma evidence
   in the reviewed literature, so the ARBA `IEA` row is MARK_AS_OVER_ANNOTATED,
   matching TLR9.

7. **`GO:0071260 cellular response to mechanical stimulus` (IEP, PMID:19593445).**
   Same wrong-reference problem as TLR7 and TLR3: the identifier resolves to
   "Expression of the Bcl-2 protein BAD promotes prostate cancer growth", whose
   cached full text has no occurrence of "TLR" or "toll". UNDECIDED, with
   `reference_review.correctness: WRONG_IDENTIFIER`.

8. **`GO:0005515 protein binding`, two IPI rows (UNC93B1).** Uninformative. TLR8 is
   the client of UNC93B1 and the biology is trafficking; the BioPlex row
   (PMID:33961781) is a proteome-scale interactome screen with no functional
   assignment. REMOVE both, mirroring the TLR3/TLR7 handling. Removal does not
   dispute either interaction — PMID:22164301 establishes the UNC93B1 association
   directly.

9. **Plasma membrane IBA.** The `is_active_in GO:0005886` row sits at the TLR7/8/9
   node. For TLR8 the endosomal restriction is not merely where it signals but a
   prerequisite: the Z-loop must be cleaved by endosomal proteases before the
   receptor can dimerise at all [PMID:26929371, PMID:25297876]. KEEP_AS_NON_CORE,
   with the node-level question raised.

10. **`GO:0038023 signaling receptor activity` and `GO:0045087` (NAS,
    PMID:12032557).** Author-statement rows from the R-848 correspondence. Both are
    true but generic; the receptor-activity row MODIFYs to `GO:0038187 pattern
    recognition receptor activity`, which TLR8 already carries by IBA and which is
    what the structures establish.

## Deep-research cross-check (2026-09-30)

The Falcon report had already been read for orientation when the review was
written; this pass re-compared it against each decision.

- **Agrees:** dual-site ligand recognition with uridine at site 1 (PMID:25599397);
  preformed inactive dimer reorganised by agonist (PMID:23520111); Z-loop insertion;
  UNC93B1-dependent trafficking and colocalisation with Rab5 early endosomes and ER
  but not Golgi or LAMP1 lysosomes (matches PMID:22164301 and the demotion of the Golgi
  and endolysosome membrane rows); myeloid expression; strong NF-kappaB/inflammatory
  output with weaker type I IFN than TLR7; IMD98 gain-of-function.
- **Adds (not used for decisions):** TIRAP-dependent TLR8-IRF5 signalling; mouse data
  that TLR8 restrains TLR7; NK ADCC enhancement by TLR8 agonists. None verified in a
  cached primary paper; none is an activity TLR8 itself performs that GO lacks.
- **Minor conflict:** the report says the second site "preferentially binds
  guanosine-rich ssRNA"; the review follows the primary structure paper
  (PMID:25599397: a short oligonucleotide at the concave-surface site). Left as is.
- **Changes:** no annotation decisions changed. Added the report to `references`
  and cited it as corroborating context on the `GO:0038187` IBA row.

