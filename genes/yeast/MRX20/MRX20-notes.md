# MRX20 (YFR045W / P43617) — curation notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* MRX20.
Provenance is recorded inline as [SOURCE "verbatim supporting text"] where possible.

## Identity (resolved carefully — there is a genuine name/function tension)

- SGD **standard name = MRX20**; systematic name **YFR045W**; UniProt **P43617**
  (entry name YFL5_YEAST). SGD confirms MRX20 is the standard name and expands it
  as "Mitochondrial oRganization of gene eXpression"
  [https://www.yeastgenome.org/locus/YFR045W].
- **Important**: UniProt P43617 itself does NOT carry the MRX20 gene name; it lists
  only `OrderedLocusNames=YFR045W` and describes the protein as
  "Uncharacterized mitochondrial carrier YFR045W" (RecName)
  [genes/yeast/MRX20/MRX20-uniprot.txt line 6-7].
- The **"Mrx" name series (Mrx1–Mrx21)** was coined by the MIOREX study
  (Kehrein et al. 2015, Cell Reports, PMID:25683707): previously uncharacterized
  proteins that co-purified by quantitative mass spectrometry with native
  mitochondrial-ribosome ("MIOREX") complexes were given Mrx numbers. SGD's
  "name description" reference for MRX20 is this paper. **Being pulled down with
  MIOREX complexes is a proteomic association, not a demonstrated molecular
  function.** The abstract describes MIOREX as ribosome interactomes
  [PMID:25683707 "These interactions result in large expressosome-like assemblies
  that we termed mitochondrial organization of gene expression (MIOREX) complexes."].
  I could NOT obtain the full text (not open access; PubMed MCP unauthenticated),
  so I do not have a verbatim, MRX20-specific quote from this paper and treat its
  MRX20-specific content as an association only.

### The core tension
The name "MRX20" suggests a role in mitochondrial gene expression, but every
structural/sequence line of evidence says this is a **mitochondrial carrier
(SLC25 / MCF; TC 2.A.29) family** inner-membrane transporter. These two facts are
not contradictory — an integral inner-membrane carrier could plausibly be found in
the vicinity of membrane-tethered translation machinery — but they mean the gene's
**actual molecular function (what it transports, if anything) is unknown**.

## Domain / sequence analysis (done inline from the UniProt record)

Source: genes/yeast/MRX20/MRX20-uniprot.txt

- 309 aa, ~34.4 kDa. PE=3 (inferred from homology). No experimental structure; AlphaFold model exists.
- **Mitochondrial carrier family (MCF/SLC25)**: `SIMILARITY ... Belongs to the
  mitochondrial carrier (TC 2.A.29) family` (line 73). Pfam PF00153 Mito_carr ×3;
  PROSITE PS50920 SOLCAR ×3; PRINTS MITOCARRIER; InterPro IPR002067 (MCP),
  IPR023395 (MCP_dom_sf), IPR018108 (MCP_transmembrane), IPR049563 (TXTP-like);
  Gene3D 1.50.40.10 mitochondrial carrier domain; SUPFAM SSF103506 (lines 116–126).
- **Six TM helices** (12–32, 47–67, 100–120, 184–204, 222–242, 285–305) and
  **three tandem Solcar repeats** (6–83, 97–211, 216–302) (lines 133–156) — the
  canonical MCF three-repeat / six-TM architecture (pseudo-3-fold symmetry).
- **Subcellular location**: `Mitochondrion inner membrane {ECO:0000305};
  Multi-pass membrane protein {ECO:0000305}` (lines 71–72). KW Mitochondrion,
  Mitochondrion inner membrane, Transmembrane, Transport (lines 128–129).
- PANTHER: family **PTHR45788** "SUCCINATE/FUMARATE MITOCHONDRIAL
  TRANSPORTER-RELATED"; **subfamily PTHR45788:SF5 "AFR253WP"** (lines 121–122).

### Subfamily context is decisive for judging the IBA "citrate" annotations
From interpro/panther/PTHR45788/PTHR45788-entries.csv (reviewed members):
- The **broad family PTHR45788** contains the characterized tricarboxylate/citrate
  carriers CTP1 (P38152, *S. cerevisiae*), SLC25A1 (human P53007, bovine P79110,
  rat P32089, mouse), SFC1 succinate/fumarate carrier (P33303, *S. cerevisiae*),
  plant SFC1 (Q9M038), Aspergillus ctpA/B/C, etc.
- **But MRX20's own subfamily PTHR45788:SF5 ("AFR253WP")** contains ONLY
  *Saccharomyces*-lineage **uncharacterized** carriers: P43617 (YFR045W itself),
  A7A285 (SCY_1795), B3LUQ6 (SCRG_05595), B5VI70 (AWRI1631_61110) — all annotated
  "Uncharacterized mitochondrial carrier". No SF5 member has a demonstrated
  substrate.
- => The GOA IBA annotations for **citrate secondary active transmembrane
  transporter activity** (GO:0071913) and **mitochondrial citrate transmembrane
  transport** (GO:0006843) are propagated from the **family level** (driven by the
  CTP1/SLC25A1 clade), NOT from MRX20's own uncharacterized subfamily. This is a
  classic over-specific IBA propagation: MRX20 is very likely a carrier, but the
  *citrate* substrate assignment is not supported for it specifically.

## Literature (sparse — this is a dark gene)

1. **Belenkiy et al. 2000, Biochim Biophys Acta, PMID:10930523** (abstract only).
   - Systematic survey/resequencing of the 35 yeast mitochondrial transport
     proteins (MTPs); YFR045W is one of them.
     [PMID:10930523 "Mitochondrial transport proteins (MTP) typically are
     homodimeric with a 30-kDa subunit with six transmembrane helices."]
   - The five MTP consensus residues (present in MTPs with identified transport
     function) were confirmed present in YFR045W after resequencing
     [PMID:10930523 "We do now find these five consensus residues also in the new
     sequences of YNL083W and YFR045W."].
   - Expression of YFR045W is stress-inducible
     [PMID:10930523 "the expressions of YFR045W, YPR021C, and YDR470C are induced
     by various stress situations."].
   - This is the **ISS source** SGD used for the "mitochondrial inner membrane"
     and "mitochondrial transport" annotations (GOA original_reference_id
     PMID:10930523; note SGD's with/from points to paralogs SGD:S000003838 and
     SGD:S000005027).
   - NOTE: abstract reports YFR045W resequenced to 285 aa; current UniProt sequence
     is 309 aa (SEQUENCE CAUTION notes an earlier erroneous gene model / frameshift,
     lines 75–78) — the annotation predates the corrected model but the MCF family
     assignment is unaffected.

2. **Kehrein et al. 2015, Cell Reports, PMID:25683707** (abstract only).
   - Source of the MRX20 name; MIOREX (mitochondrial ribosome) co-purification by
     quantitative MS. Provides only an *association*, no molecular function for
     MRX20. (See "Identity" above.)

3. **SGD large-scale phenotype data** (https://www.yeastgenome.org/locus/YFR045W):
   null mutant is **viable**; "decreased levels of chitin and normal resistance to
   calcofluor white"; high-throughput screens additionally report decreased chitin
   deposition, decreased competitive fitness, increased chronological lifespan, and
   abnormal vacuolar morphology. All non-specific/pleiotropic; none pins a molecular
   function. Protein abundance ~710 molecules/cell (low). Not recorded as a
   dedicated citable PMID here; treated as background, not used for a specific GO
   claim.

## Assessment summary (what is KNOWN vs NOT known)

KNOWN (well supported):
- Integral **mitochondrial inner-membrane** protein, multi-pass (6 TM). [homology/ISS/subcell]
- Member of the **mitochondrial carrier (SLC25/MCF) family** with canonical
  three-repeat architecture. [Pfam/PROSITE/PANTHER/InterPro]
- Almost certainly functions in **transmembrane transport** (family-level). [InterPro IEA + family]
- Stress-inducible expression; non-essential; low abundance. [PMID:10930523; SGD HTP]

NOT known (genuine knowledge gaps):
- **Transported substrate / specific molecular function** — SF5 subfamily is
  entirely uncharacterized; citrate assignment is a family-level IBA over-propagation.
- Whether MRX20 has any **direct role in mitochondrial gene expression** (the "MRX"
  name reflects only MIOREX proteomic co-purification, not a demonstrated function).
- **Physiological process / pathway** it serves; loss-of-function phenotypes are
  weak and pleiotropic.
- Whether it is a genuine transporter or a pseudo-transporter (no substrate assay exists).

## Curation decisions (rationale)

- C: mitochondrial inner membrane (ISS, PMID:10930523) → ACCEPT (core; strong homology + MCF membrane protein).
- C: mitochondrial inner membrane (IEA, GO_REF:0000044 SubCell) → ACCEPT (consistent, redundant with ISS).
- C: mitochondrion (IBA) → ACCEPT as non-core (correct but less specific than inner membrane).
- P: transmembrane transport (IEA InterPro) → ACCEPT (family-level; correct general process).
- P: mitochondrial transport (ISS, PMID:10930523) → ACCEPT/KEEP (general, defensible).
- F: citrate secondary active transmembrane transporter activity (IBA) → MARK_AS_OVER_ANNOTATED
  (family-level propagation; MRX20's SF5 subfamily has no citrate-transport member; substrate unknown).
- P: mitochondrial citrate transmembrane transport (IBA) → MARK_AS_OVER_ANNOTATED (same reason).
- F: molecular_function (ND) → ACCEPT (honestly records that MF is unknown; do not invent one).

core_functions: only the defensible general MF ("transmembrane transporter activity",
GO:0022857) with location mitochondrial inner membrane (GO:0005743). No specific
substrate claimed.
