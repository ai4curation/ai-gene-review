# nspC (VC_1623, Q9KRL4) curation notes

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

Fetched with `just fetch-gene VIBCH Q9KRL4 --alias nspC`.

Deep research: no gene-level provider deep-research file was generated in this
session. The module-level OpenScientist report was used for retrieval only;
claims were checked against cached papers (PMID:19196710 full text; the others
abstract-only).

Key evidence:

- Genetics in V. cholerae: [PMID:19196710 "Deletion of VC1623 resulted in the
  disappearance of norspermidine and the novel accumulation of
  carboxynorspermidine"]; both sym-norspermidine and spermidine are lost.
- Substrate specificity of the orthologue (V. vulnificus CANSDC, assayed in the
  same paper): carboxynorspermidine preferred 20-fold over carboxyspermidine,
  with [PMID:19196710 "no activity with l -arginine, l -lysine, and meso
  -diaminopimelate"]. This contradicts the IBA diaminopimelate decarboxylase
  activity transferred from PTN000159906.
- Orthologue genetics outside Vibrio: C. jejuni [PMID:22025614] and
  B. thetaiotaomicron [PMID:27118128] show the CASDC orthologue makes spermidine.
- Structure of the C. jejuni/V. cholerae CANSDC: group IV PLP decarboxylase fold,
  obligate dimer with active sites at the subunit interface [PMID:20534592].

Decisions:

- GO:0008836 IBA and GO:0009085 IBA: REMOVE. Over-propagation from the
  family-root PAINT node PTN000159906 into the NspC subfamily PTHR43727:SF1; the
  PTHR43727 family review records the node as NEEDS_PRUNING for SF1.
- GO:0003824 IEA: TOO_GENERAL (entailed by the accepted carboxy-lyase activity);
  the KT2440 NspC review uses the same action.
- GO:0016831 (IEA, ISS): ACCEPT; the most specific existing GO MF. A specific
  EC 4.1.1.96 term is proposed, as in the KT2440 review.
- GO:0045312 nor-spermidine biosynthesis (IEA, ISS): ACCEPT as core, because
  norspermidine is the major V. cholerae product. In KT2440 the same term is
  KEEP_AS_NON_CORE because no diaminopropane supply is established there; the
  biology differs between organisms, not the reading of the term.
- GO:0008295 ISS: ACCEPT (core).
- GO:0030170 ISS: ACCEPT (PLP cofactor; Lys51 Schiff base by similarity).
- GO:0042803 ISS: KEEP_AS_NON_CORE (structural dimer, not the function).
- GO:0044010 IDA: KEEP_AS_NON_CORE. The biofilm defect is downstream of
  norspermidine signalling and is rescued by exogenous norspermidine; the enzyme
  performs no biofilm step itself.


## 2026-11-05 complete gene-level comparative audit

Re-read every existing annotation, core function, raw UniProt record, relevant
provider report and primary literature. Original annotation payloads and raw
UniProt/GOA snapshots were preserved; no new annotation rows were added. Five
authored NEW rows across the four-gene baseline remain inherited proposals, not
new proposals from this audit. Default Falcon research was attempted with
`just deep-research ORGANISM GENE --provider falcon`; it failed with HTTP 403
authentication. No provider report was fabricated or overwritten. Manual findings
are recorded here; the command logs are in the ignored module-audit cache.

QuickGO on 2026-11-05 confirmed active GO:0102143 includes both carboxynorspermidine
and carboxyspermidine dehydrogenase reactions, and GO:0102144 is obsolete as the
same activity. Searches for carboxyspermidine/carboxynorspermidine decarboxylase
and carboxypolyamine returned no specific decarboxylase term. The existing NTR
name was retained; no GO or PTN identifier was invented. PANTHER official names
were checked in panther.obo, and exact protein/subfamily assignments against the
unchanged UniProt records (PTHR43796:SF2 for the dehydrogenases; PTHR43727:SF1 for
the decarboxylases).

The comparative literature requires a substrate-specific reading. The B. fragilis
and C. leptum enzymes have measured putrescine/DAP kinetics, but these are not
measurements of this target [PMID:37437886, "These data suggest that both enzymes
can use putrescine or DAP and thus produce carboxyspermidine or
carboxynorspermidine."]. Agmatine was not tested in those comparisons. The 2025
reconstruction shows that related pairs can make tetramines or use agmatine;
those functions are not transferred here [PMID:40074085, "The ASA-dependent
pathway consisting of CASDH/CASDC homologs has diversified during evolution
to produce norspermidine (29), N1-aminopropylagmatine (37), and as we have shown
here, spermidine and Spm/Tspm."]. Physiological product identity, reconstructed
pathway activity and isolated-enzyme turnover are distinct evidence.

The 2009 deletions/complementations used C6709, not the N16961 reference strain.
These are same-species locus assignments, not claims of an N16961 experiment
[PMID:19196710, "Wild-type V. cholerae strain C6709 cells grown in M9 minimal
medium"]. Purified CANSDC specificity, including lack of meso-diaminopimelate
activity and 20-fold substrate preference, was measured in the V. vulnificus
ortholog; it is not a direct Q9KRL4 assay. No blanket absence of experimental
support is inferred from these strain distinctions.

Refined GO:0003824 and all GO:0016831 rows to MODIFY with the already-supported
NTR carboxyspermidine/carboxynorspermidine decarboxylase activity; the core uses
proposed_molecular_function with the matching proposal. This changes specificity,
not the claimed chemistry. Existing lysine/diaminopimelate removals remain
consistent with the family review.

`just paint-losses VIBCH nspC` found no IRD or IKR on this lineage. The existing
PTN000159906 over-propagation rationale remains supported by the family review;
the V. vulnificus substrate assay is identified precisely. PLP binding and
homodimerization are inferred from C. jejuni A8FNH9, not directly measured on
Q9KRL4. The earlier notes' "C. jejuni/V. cholerae CANSDC" structural wording was
imprecise: PDB 3N29 is C. jejuni [PMID:39887002]. The existing experimentally
grounded biofilm annotation remains KEEP_AS_NON_CORE as a downstream phenotype.


## PR #6089 requested revisions — 2026-11-06

Replaced generic pasted reasons with annotation-specific evidence and action rationales. Distinguished the two LysA-propagation defects, inferred PLP/assembly/location, the catalytic refinements, native C6709 process evidence transferred to N16961, and the downstream biofilm phenotype. No annotation actions changed. Machine annotation payloads, inherited NEW assertions and raw UniProt/GOA files were preserved; no new annotation rows were added. Existing research/provider records were not refreshed.
