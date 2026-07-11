# UQCC2 (Q9BRT2) review notes

Gene: UQCC2 / MNF1 / M19 / C6orf125 — Ubiquinol-cytochrome c reductase complex assembly factor 2.
Human, 126 aa precursor (N-terminal transit peptide 1-13; chain 14-126). Non-enzymatic.

## Verified core biology
UQCC2 is a mitochondrial assembly factor for respiratory chain Complex III (cytochrome
bc1 / ubiquinol-cytochrome c oxidoreductase). It is the human ortholog of *S. cerevisiae*
Cbp6p; its partner UQCC1 is the ortholog of Cbp3p. UQCC1+UQCC2 form a complex that
activates translation of and stabilises the mtDNA-encoded cytochrome b (MT-CYB), delivering
it to an early Complex III assembly intermediate. UQCC2 is required for UQCC1 stability
and vice versa. Loss causes complex III deficiency.
[PMID:24385928 — full text available; definitive functional paper.]

Key verbatim anchors (PMID:24385928, full text present):
- "We established the role of UQCC2 as a complex III assembly factor that cooperates with UQCC1 (MIM 611797) to mediate cytochrome b protein expression and subsequent complex III assembly."
- "we investigated the co-expression of the genes with complex III subunit genes" ... "UQCC1 and UQCC2 are complex III assembly factors participating in cytochrome b biogenesis." (abstract)
- "UQCC2 interacts with UQCC1, the predicted ortholog of the Cbp6p binding partner, Cbp3p."
- "Subsequent SDS-PAGE and western blot analysis of the UQCC2-TAP purification revealed efficient co-isolation of UQCC1"
- "UQCC2 patient fibroblasts have specific defects in the synthesis or stability of cytochrome b."
- "in the case of COX2 and COX3, an increased amount" ... "a striking and specific defect in cytochrome b protein levels" (Fig 8A) — supports role in MT-CYB translation/stability.
- Disease: "severe intrauterine growth retardation, neonatal lactic acidosis and renal tubular dysfunction associated with complex III deficiency."
- UNIPROT: complex III subunits + ribosomal subunits "did not co-elute with UQCC2-TAP" — i.e. UQCC2 does not stably co-purify the CIII holo subunits (supports that the tight partner is UQCC1).

## Localization
- UniProt SUBCELLULAR LOCATION: Mitochondrion matrix, mitochondrion nucleoid; Mitochondrion;
  intermembrane space (ECO:0000250); matrix (ECO:0000250); inner membrane (ECO:0000250).
  "Predominantly expressed in the mitochondrial inner membrane."
- PMID:19643811 (abstract only): "Human M19 (hM19) is present in mitochondria, and
  protease-protection experiment showed it to be sublocalized in the matrix space." and
  co-localizes with mtDNA → mitochondrial nucleoid. This is the IDA source for nucleoid + matrix.
- PMID:22363741 IDA mitochondrion; "13-long amino acid sequence located at the N-terminus of
  M19 that targets the protein to mitochondria."
- IEA GO_REF:0000044 (SubCell mapping) and ISS GO_REF:0000024 (mouse ortholog Q9CQY6) supply
  inner membrane / IMS / matrix / nucleoid — consistent with UniProt SUBCELLULAR LOCATION.

## Molecular function
No catalytic activity. It is an assembly factor / chaperone-like translational activator for
MT-CYB. The only MF term in GOA is GO:0005515 protein binding (IPI). Per curation policy,
avoid using bare `protein binding` as a core function. Do NOT invent a catalytic MF.
=> core_functions will have NO molecular_function slot (only directly_involved_in + located_in).

## protein binding IPIs
- PMID:24385928 IPI with UQCC1 (Q9NVA1): the biologically meaningful, functional interaction.
  ACCEPT (bare protein binding, but genuinely the functional partner; keep as evidence).
- PMID:33961781 IPI with UQCC1 (Q9NVA1): same partner, high-throughput network. ACCEPT.
- PMID:40205054 IPI with UQCC1 (Q9NVA1): same partner. ACCEPT.
- PMID:32296183 (binary interactome, HuRI): preys CDKN2D, EXOC8, GNG13, MKRN3, MRFAP1,
  NRDE2, SNAP25, TRAPPC2, TXN2, ZNF765, UQCC1 — most are non-mitochondrial, likely Y2H
  artifacts; uninformative `protein binding`. MARK_AS_OVER_ANNOTATED (bare protein binding
  IPI, per policy do not REMOVE).

## Other BP annotations
- GO:0034551 respiratory chain complex III assembly (IBA + IDA): CORE. ACCEPT both.
- GO:0070131 positive regulation of mitochondrial translation (IDA, 24385928): supported by
  MT-CYB translational activation (COMA complex activates MT-CYB translation). ACCEPT.
- GO:0002082 regulation of oxidative phosphorylation (IMP, 22363741): supported by O2
  consumption / ATP modulation. ACCEPT (via CIII assembly, downstream OXPHOS effect).
- GO:0050796 regulation of insulin secretion (ISS from mouse Q9CQY6): downstream/indirect,
  physiological consequence of respiratory chain modulation in beta-cells (22363741). Not a
  core molecular role. KEEP_AS_NON_CORE.
- GO:2001014 regulation of skeletal muscle cell differentiation (ISS): downstream/indirect
  physiological consequence (22363741, C2C12). KEEP_AS_NON_CORE.

## CC annotations (all mitochondrial, consistent)
- GO:0005759 matrix (IBA is_active_in; IEA; ISS; IDA-supported via 19643811 protease
  protection). ACCEPT the primary ones; duplicates ACCEPT.
- GO:0005739 mitochondrion (IEA SubCell; IDA HPA GO_REF:0000052; HTP 34800366; IDA 22363741). ACCEPT.
- GO:0005743 inner membrane (IEA; ISS). UniProt: "Predominantly expressed in the mitochondrial
  inner membrane." ACCEPT.
- GO:0005758 intermembrane space (IEA; ISS, ECO:0000250). ACCEPT (by similarity; UniProt lists it).
- GO:0042645 mitochondrial nucleoid (IEA; IDA 19643811). ACCEPT.

## core_functions
- directly_involved_in GO:0034551 mitochondrial respiratory chain complex III assembly
- located_in GO:0005743 mitochondrial inner membrane (predominant)
- located_in GO:0005739 mitochondrion (general)
No molecular_function (only bare protein binding available; non-catalytic assembly factor).
Current CIII complex term = GO:0045275 (GO:0005750 obsolete) — not needed here but noted.
