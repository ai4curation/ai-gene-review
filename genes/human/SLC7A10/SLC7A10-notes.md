# SLC7A10 (Asc-1 / asc-type amino acid transporter 1) — curation notes

UniProt: Q9NS82 (AAA1_HUMAN). HGNC:11058. Chromosome 19q13. 523 aa, APC
(amino acid-polyamine-organocation) superfamily; PANTHER PTHR11785:SF73.
Batch 8 of the canonical-surfaceome backfill. This gene is a **heteromeric amino
acid transporter (HAT) light chain**, like the batch-7 SLC7A5–A9 light chains —
NOT a CAT-type single-chain transporter.

## Core biology (synthesized)

asc-1 is the catalytic **light chain** of a disulfide-linked heterodimer with the
heavy chain **SLC3A2 / 4F2hc (CD98hc)**, which is required for its functional
surface expression. It is a **Na+- and Cl--independent antiporter
(exchanger)** — operating preferentially though not exclusively in exchange mode —
of **small neutral amino acids** — glycine, L-alanine, L-serine,
L-threonine, L-cysteine and alpha-aminoisobutyrate — and, distinctively,
**D-isomers**, most notably **D-serine** (and D-alanine), transporting D-serine
with high affinity (Km ≈ 22.8 µM, close to its physiological brain concentration).
System asc. It operates preferentially but not exclusively in exchange mode.

Physiologically, asc-1 controls synaptic/extracellular levels of **D-serine** (an
NMDA-receptor co-agonist) and **glycine** in the CNS, modulating glycinergic
inhibitory neurotransmission (spinal cord/brainstem) and NMDA-dependent excitatory
transmission (hippocampal Schaffer collateral–CA1). It is also an adipose-tissue
marker implicated (by similarity, mouse) in white vs beige/brown adipocyte lineage
commitment via D-serine release.

## Key evidence

- Mouse Asc-1 identification / 4F2hc heterodimer / substrate selectivity / exchange
  mode: [PMID:10734121 "Asc-1 required 4F2hc for its functional"; "confirming that
  Asc-1 and 4F2hc are linked via a disulfide bond."; "Asc-1-mediated transport was
  not dependent on the presence of Na(+) or Cl(-)."; "Asc-1 preferred small neutral
  amino acids such as Gly, L-Ala, L-Ser, L-Thr"; "Asc-1 operated preferentially,
  although not exclusively, in an exchange mode."]. This paper is on MOUSE Asc-1
  (cloned from mouse brain); GOA nonetheless applies it as TAS to human SLC7A10, and
  human hAsc-1 is 91% identical with conserved properties (below).
- Human hAsc-1 cloning / 4F2hc dependence / high-affinity D-serine / brain:
  [PMID:10863037 "4F2 heavy chain for its functional expression in Xenopus oocytes.";
  "small neutral amino acids in a Na(+)-independent manner."; "D-serine at high
  affinity with a K(m) value of 22.8 microM."; "hAsc-1 is proposed to play
  significant roles in the"]. 91% identity to mouse Asc-1.
- UniProt Q9NS82 curated (ECO:0000250 by similarity from mouse P63115 / rat P63116):
  SUBUNIT "Disulfide-linked heterodimer with the amino acid transport protein
  SLC3A2/4F2hc"; FUNCTION describes exchange transport of small neutral L- and
  D-amino acids, glycinergic neurotransmission regulation, Schaffer collateral D-serine
  release modulating NMDA receptors, and the adipocyte-lineage role. CATALYTIC ACTIVITY
  lists Rhea exchange reactions (all X(out)/L-alanine(in) antiport): glycine
  (CHEBI:57305), L-serine (CHEBI:33384), L-threonine, L-cysteine (CHEBI:35235),
  D-serine (CHEBI:35247), D-alanine, L-alanine (CHEBI:57972), etc. — confirming the
  antiporter (exchange) mechanism and substrate set.
- Structure: cryo-EM PDBs 8QEY, 8WNS/T/Y (asc-1–4F2hc complex), 9 TM helices modeled.
- ComplexPortal CPX-8189 "ASC1-4F2 heteromeric amino acid transporter complex".

## Ontology / mechanism findings (OLS getAncestors, verified this session)

- GO:1990184 (amino acid transport complex) is a descendant of GO:0032991
  protein-containing complex (via GO:0098796 membrane protein complex / GO:0098797
  plasma membrane protein complex). GO:1902495 (transmembrane transporter complex) is
  also a child of GO:0032991. The two are **siblings under GO:0032991**, so
  MODIFY GO:1902495 → GO:1990184 is a **lateral move to the structurally accurate
  complex class, NOT an is_a refinement** — same justification used for SLC7A5–A9.
- GO:0015804 (neutral amino acid transport) is an is_a descendant of GO:0006865
  (amino acid transport) — so the generic GO:0006865 row is TOO_GENERAL given the
  accepted specific GO:0015804.

## Curation decisions (summary)

- MF substrate terms kept: GO:0015175 (neutral L-amino acid transporter, IDA core),
  GO:0015194 (L-serine transporter). GO:0015179 (L-amino acid transporter) is
  TOO_GENERAL (parent of accepted GO:0015175). GO:0022857 (transmembrane transporter)
  TOO_GENERAL (root).
- Mechanism: asc-1 is an antiporter operating preferentially in exchange mode; captured as core MF GO:0015297
  (antiporter activity) + proposed combined term. None of the existing MF rows are
  explicitly uniporter/symporter-flavored, so no lateral MODIFY of existing substrate
  MFs is required — substrate-specific transporter terms are kept as accurate.
- BP transport terms (neutral amino acid transport, glycine transport, L-serine
  transport, D-serine/D-alanine transmembrane transport) are ACCEPTed: asc-1 performs
  the transport step (participation test satisfied).
- GO:0060094 (positive regulation of glycinergic synaptic transmission): KEEP_AS_NON_CORE
  — a downstream regulatory consequence of glycine transport, not a step asc-1 executes.
- GO:1903444 (negative regulation of brown fat cell differentiation): KEEP_AS_NON_CORE
  — genuine (mouse, by-similarity) regulatory role via D-serine release; peripheral to
  the CNS transport core and asc-1 does not execute a differentiation step.
- GO:0005515 protein binding (IPI, with APPBP2 Q92624 from HuRI): REMOVE per
  protein-binding policy (uninformative). NB the WITH/FROM here is APPBP2, NOT SLC3A2;
  the functional SLC3A2 heterodimer is modeled via the GO:1990184 complex row +
  in_complex, not bare binding.
- GO:0016020 membrane → MODIFY to GO:0005886 plasma membrane (specific location known).
- Plasma membrane rows (IBA/IEA/ISS/NAS/TAS ×several): ACCEPT (core location).
