# SLC7A4 (CAT-4) curation notes

UniProt: O43246 (CTR4_HUMAN). HGNC:11062. Gene on 22q11.2 (VCFS region).
Member of SLC7 family; SLC7A1-A4 are the "cationic amino acid transporters"
(CATs); A5-A13 are the heteromeric transporters (HATs). SLC7A4 is a CAT-type
(single polypeptide), **not** a HAT — it has no 4F2hc/rBAT heavy chain.

## Key question going in: is SLC7A4 actually a transporter?

The family name "cationic amino acid transporter 4 / CAT-4" is a homology label,
not a demonstrated function. For two decades its transport function was uncertain:

- 1998 (PMID:9598310, Sperandeo et al., Genomics): cloned SLC7A4 by EST screening,
  mapped it to the VCFS-deleted region 22q11.2, named it a CAA transporter by
  homology. Reported a preliminary oocyte result — [PMID:9598310 "Microinjection
  of SLC7A4 mRNA into Xenopus laevis oocytes demonstrates a significant stimulation
  of CAA transport."] and [PMID:9598310 "SLC7A4 displays high homology with SLC7A1
  and SLC7A2, two previously known CAA transporters."]. Abstract-only in cache;
  this oocyte CAA-transport claim was **not reproduced** by later work.
- 2002 (PMID:12049641, Wolf et al., Biochem J — NOT cached; title in UniProt):
  "Expression of solute carrier 7A4 (SLC7A4) in the plasma membrane is not
  sufficient to mediate amino acid transport activity." Established PM localization
  but found no cationic-AA transport. UniProt CC:FUNCTION records: [file:human/SLC7A4/SLC7A4-uniprot.txt
  "Does not transport the cationic amino acids arginine or lysine"].

## Resolved in 2026 — SLC7A4 is a pH-gated L-leucine transporter

PMID:41904136 (Kolokouris et al., Nat Commun 2026; cryo-EM of the plant homologue
CAT4 + transport assays/MD on human SLC7A4). This is the definitive functional
characterization and supersedes the "uncertain / cationic" picture:

- [PMID:41904136 "we show that the plasma membrane amino acid transporter SLC7A4 is
  regulated by low extracellular pH and functions as a leucine transporter in human
  cells"] — establishes the MF (L-leucine transporter), the location (plasma
  membrane), and pH regulation.
- Does NOT transport cationic amino acids: [PMID:41904136 "studies utilising Xenopus
  oocytes demonstrated that human SLC7A4 does not transport the cationic amino acids
  arginine or lysine"]. So GO:0015174 basic amino acid transmembrane transporter
  activity (and the IEA-inferred GO:1990822 basic amino acid transmembrane transport)
  are **contradicted**, not merely over-general.
- Activity is acid-activated: [PMID:41904136 "we observed a substantial increase in
  L-Leu uptake at pH 6.5 and 5.5 compared to pH 7.5 in HCT-116 cells, indicating that
  SLC7A4 is activated at acidic pH"]. UniProt: pH optimum 6.5/5.5; Glu125 (TM3) is the
  pH sensor (MUTAGEN E125Q/E125S abolish acidic activation).
- Selectivity is tunable: a triple mutant V332S/L336S/L394M switches affinity toward
  L-Arg, showing the WT pocket is leucine-selective by design (UniProt MUTAGEN).
- Tissue context consistent with a pH-responsive role: [PMID:41904136 "SLC7A4
  enrichment in the choroid plexus (blood-brain barrier) and testis, with secondary
  expression reported in placental trophoblasts"].

## Localization

Plasma membrane confirmed directly (GO:0005886 IDA, PMID:41904136; also Wolf 2002).
14 predicted TM helices (ECO:0000255), LeuT/APC fold. Multi-pass membrane protein.
GO:0016020 "membrane" rows are correct but less specific than the supported PM term →
MODIFY to GO:0005886. (GO:0016020 is a generic membrane term, not a root-organelle
term, so the refine-to-specific rule applies.)

## Not heteromeric

CAT subfamily member; single polypeptide; no heavy chain. Do not model in_complex
4F2hc/SLC3A2 and do not add GO:1990184 (amino-acid transport complex).

## Annotation decisions (summary)

- Plasma membrane (IBA is_active_in; IDA located_in): ACCEPT, core location.
- GO:0015190 L-leucine transmembrane transporter activity (IDA): ACCEPT, core MF.
- GO:1903801 L-leucine import across plasma membrane (IDA): ACCEPT, core BP.
- GO:0006865 amino acid transport (IBA) / GO:0055085 transmembrane transport (IEA):
  correct but general → MODIFY to GO:1903801.
- GO:0015171 amino acid transmembrane transporter activity (IBA) / GO:0022857
  transmembrane transporter activity (IEA): correct but general → MODIFY to GO:0015190.
- GO:0016020 membrane (IEA; TAS): MODIFY to GO:0005886 plasma membrane.
- GO:0015174 basic amino acid transmembrane transporter activity (TAS 1998) and
  GO:1990822 basic amino acid transmembrane transport (IEA, from GO:0015174):
  REMOVE — directly contradicted (no Arg/Lys transport). The family-name-based
  1998 oocyte CAA claim was not reproduced and is superseded by PMID:41904136.

No bare GO:0005515 protein binding row present in GOA.

## IBA phylogeny note

The IBA WITH/FROM lists (CAT1 P30825, CAT2 P52569, CAT3 Q8WY07, fly/mouse/rat/
Arabidopsis CATs) seed the amino-acid-transporter node; SLC7A4's own accession is
absent (it had no experimental annotation at PAINT time). The family-level
"amino acid transmembrane transporter / amino acid transport" inference is sound for
SLC7A4 (it is a bona fide amino acid transporter); it just needs refinement to the
leucine specificity now shown experimentally. The *cationic* specificity the family
name implies does not hold for A4.
