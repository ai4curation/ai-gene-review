# TTC19 (Q6DKK2) review notes

## Summary of verified biology
TTC19 = Tetratricopeptide repeat protein 19, mitochondrial. A nuclear-encoded,
mitochondrion-imported protein (transit peptide 1-70; mature chain 71-380) that is
embedded in the **mitochondrial inner membrane** and functions as an **assembly/maintenance
factor for respiratory Complex III (cytochrome bc1 / ubiquinol–cytochrome c reductase)**.
It is a TPR-repeat scaffold protein (5 TPR repeats, residues ~136-351) with **no catalytic
activity** — it is not an enzyme.

Core molecular role (from UniProt FUNCTION + PMID:28673544 Bottani 2017, not cached here):
TTC19 binds the mature Complex III dimer after incorporation of the Rieske Fe-S protein
UQCRFS1, and is required for **clearance/turnover of the N-terminal fragments of UQCRFS1**
that are generated during Rieske maturation. Accumulation of these fragments (when TTC19 is
lost) is detrimental to Complex III catalytic activity. Hence TTC19 preserves the structural
and functional integrity of Complex III ("husbandry" role).

## Key references
- PMID:21278747 (Ghezzi 2011, Nat Genet) — CACHED, abstract only. Discovery paper: homozygous
  nonsense mutations in TTC19 cause cIII deficiency + progressive encephalopathy; TTC19 embedded
  in inner mitochondrial membrane as part of two HMW complexes, one coinciding with cIII; physical
  interaction with cIII by co-IP; Drosophila KO recapitulates. "putative cIII assembly factor".
  Source for: GO:0005743 (IDA inner membrane), GO:0034551 (IMP cIII assembly).
- PMID:28673544 (Bottani 2017, Mol Cell) — NOT cached (no verbatim quote possible). "TTC19 plays
  a husbandry role on UQCRFS1 turnover in the biogenesis of mitochondrial respiratory complex III."
  Mechanistic basis for UQCRFS1 N-terminal fragment clearance. Cited in UniProt FUNCTION/SUBUNIT.
- PMID:20208530 (Sagona 2010, Nat Cell Biol) — CACHED, abstract only. Reported TTC19 as ZFYVE26
  (FYVE-CENT) binding partner that interacts with CHMP4B (ESCRT-III) and localizes to centrosome/
  midbody, implicated in cytokinesis abscission. **UniProt CAUTION**: midbody localization could NOT
  be confirmed by others (PMID:21278747). Source for GO:0000281 (mitotic cytokinesis, TAS),
  GO:0005813 (centrosome, TAS), GO:0030496 (midbody, TAS), and 2 protein-binding IPIs (ZFYVE26 Q68DK2,
  CHMP4B Q9H444).
- Reactome R-HSA-9865881 "Complex III assembly" (Homo sapiens) — human Complex III assembly pathway;
  TTC19 acts as an assembly factor within this.

## GOA annotation inventory (64-row TSV, collapses to distinct term+evidence+ref lines)
CC:
- GO:0005743 mitochondrial inner membrane — IBA (GO_REF:0000033), IEA (GO_REF:0000044 SubCell), IDA (PMID:21278747) → ACCEPT (core location)
- GO:0005739 mitochondrion — IDA (GO_REF:0000052 HPA), HTP (PMID:34800366) → ACCEPT non-core (less specific than inner membrane, but correct)
- GO:0005813 centrosome — TAS (PMID:20208530) → MARK_AS_OVER_ANNOTATED (disputed by UniProt CAUTION; likely off-target of the cytokinesis paper)
- GO:0030496 midbody — TAS (PMID:20208530) → MARK_AS_OVER_ANNOTATED (explicitly not reproduced by others per UniProt CAUTION)
BP:
- GO:0034551 mitochondrial respiratory chain complex III assembly — IBA, IEA (InterPro), IMP (PMID:21278747) → ACCEPT (core function)
- GO:0000281 mitotic cytokinesis — TAS (PMID:20208530) → MARK_AS_OVER_ANNOTATED (single study, disputed; not the mitochondrial core function)
MF:
- GO:0005515 protein binding — many IPI rows (PMID:16713569, 23414517, 25416956, 28514442, 31617661,
  32296183, 32814053, 33961781, 20208530) → MARK_AS_OVER_ANNOTATED (uninformative bare protein binding;
  many are high-throughput Y2H/AP-MS. Per policy, do NOT REMOVE IPI protein binding — mark over-annotated).

## core_functions decision
- No informative MF term present in GOA (only bare protein binding) and TTC19 is non-catalytic →
  OMIT molecular_function from core_functions (per instructions: do NOT invent a catalytic MF).
- directly_involved_in: GO:0034551 (mitochondrial respiratory chain complex III assembly) — verified current.
- located_in: GO:0005743 (mitochondrial inner membrane) — verified current.

## Full-text availability
Cached publications for the interactome/proteome papers are abstract-only for several
(21278747, 20208530, 16713569, 31617661, 32814053). Per curation policy, experimental IPI/IDA/IMP/TAS
annotations are NOT removed just because full text is uncached; disputed non-mitochondrial ones are
marked over-annotated with the UniProt CAUTION as justification.
