# Acadvl (CG7461, dACADVL) — Drosophila melanogaster — Review Notes

UniProt: A1ZBJ2 (TrEMBL, unreviewed). FlyBase: FBgn0034432. Gene: Acadvl / CG7461.
NCBI TaxID 7227. Ortholog of human ACADVL (P49748, VLCAD).

## Summary of identity / function

Acadvl is the single Drosophila ortholog of the human very-long-chain acyl-CoA
dehydrogenase (VLCAD). It is a member of the acyl-CoA dehydrogenase (ACAD) family,
an FAD-dependent flavoenzyme that catalyzes the first, committed step of each cycle
of mitochondrial fatty acid beta-oxidation for long- and very-long-chain acyl-CoA
thioesters.

From the local UniProt record (A1ZBJ2):
- FUNCTION: "Very long-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA
  dehydrogenases that catalyze the first step of mitochondrial fatty acid beta-oxidation
  (FAO), breaking down fatty acids into acetyl-CoA and allowing the production of energy
  from fats." ... "very long-chain specific acyl-CoA dehydrogenase acts specifically on
  fatty acyl-CoAs with saturated 12 to 24 carbons long primary chains."
  [ECO:0000256|ARBA:ARBA00094192 — electronic/ARBA, transferred by rule]
- EC assignments: EC=1.3.8.8 (long-chain acyl-CoA dehydrogenase) and EC=1.3.8.9
  (very-long-chain acyl-CoA dehydrogenase); catalytic-activity blocks give the RHEA
  reactions with electron-transfer flavoprotein (ETF) as electron acceptor.
- COFACTOR: FAD [ChEBI:CHEBI:57692].
- PATHWAY: "Lipid metabolism; mitochondrial fatty acid beta-oxidation."
- SUBUNIT: "Homodimer. Homodimerizes after import into the mitochondrion."
- SUBCELLULAR LOCATION: "Mitochondrion inner membrane; Peripheral membrane protein."
- SIMILARITY: "Belongs to the acyl-CoA dehydrogenase family."
- Domain architecture (Pfam): Acyl-CoA_dh_N (PF02771), Acyl-CoA_dh_M (PF02770),
  Acyl-CoA_dh_1 (PF00441), ACAD9-ACADV_C (PF21343). CDD cd01161 = VLCAD.
- PANTHER subfamily PTHR43884:SF11 "VERY LONG-CHAIN SPECIFIC ACYL-COA DEHYDROGENASE,
  MITOCHONDRIAL" — supports the VLCAD-specific (not generic ACAD) assignment.
- PE 1: Evidence at protein level (PeptideAtlas A1ZBJ2 peptides); Reactome R-DME-77305
  "Beta oxidation of palmitoyl-CoA to myristoyl-CoA" (fly reaction).

Note on the C-terminal domain (PF21343 / IPR049448 "ACAD9/ACADV-like C"): both VLCAD
and ACAD9 carry this extra C-terminal extension. In human, ACADVL and ACAD9 are close
paralogs; in Drosophila, CG7461/Acadvl is reported as the single ortholog covering the
VLCAD/ACAD9 clade. The PANTHER subfamily call (SF11, VLCAD) and CDD VLCAD hit favor the
VLCAD assignment, and the fly gene is named Acadvl by FlyBase.

## Evidence status of GOA annotations

The GOA (Acadvl-goa.tsv) contains NO experimental (IDA/IMP/IPI/IGI/IEP) annotations —
this is a TrEMBL entry. All 13 annotations are electronic or homology-based:
- IBA (GO_REF:0000033, PANTHER PTN000856877 including human P49748, rat RGD:2014):
  GO:0017099 VLCAD activity; GO:0000062 fatty-acyl-CoA binding.
- IEA/InterPro (GO_REF:0000002): GO:0003995 ACAD activity; GO:0016627 oxidoreductase
  CH-CH; GO:0050660 FAD binding.
- IEA/EC (GO_REF:0000003): GO:0004466 (from EC 1.3.8.8); GO:0017099 (from EC 1.3.8.9).
- IEA/SubCell (GO_REF:0000044): GO:0005743 mitochondrial inner membrane.
- IEA/ARBA (GO_REF:0000117): GO:0006631 fatty acid metabolic process.
- ISS/FlyBase from human UniProtKB:P49748 (GO_REF:0000024): GO:0005739 mitochondrion;
  GO:0004466 LCAD activity; GO:0017099 VLCAD activity; GO:0033539 FAO using ACAD.

Because the ISS annotations are transferred by curator judgment from the well-characterized
human VLCAD (P49748), and the IBA/IEA/EC/InterPro calls all converge on the same ACAD-family
FAD-dependent beta-oxidation function, the electronic annotations are collectively well
grounded for this gene. There is no cross-paralog mistransfer problem here (the human source
P49748 IS ACADVL, unlike the human-review case where mouse P50544=LCAD was mistransferred).

## Fly-specific literature (context only; not in publications/ cache)

Web literature (not cached, so NOT used as verbatim supporting_text; recorded here as
provenance for the biological framing):

- Lee et al. 2012, Oxid Med Cell Longev "Overexpression of Fatty-Acid-beta-Oxidation-Related
  Genes Extends the Lifespan of Drosophila melanogaster" — reports dVLCAD (CG7461) among
  beta-oxidation genes; flies homozygous for a null allele die prematurely, and overexpression
  of FAO genes extends lifespan. Supports a conserved role of Acadvl in FAO/energy homeostasis
  in the fly. (web-sourced; abstract only accessible.)
- G3 (Bethesda) 2025 "Characterizing fatty acid oxidation genes in Drosophila"
  (academic.oup.com/g3journal/article/15/8/jkaf139) — systematic characterization of fly FAO
  genes including CG7461; notes ACADVL and ACAD9 are both predicted orthologs of fly CG7461.
  (web-sourced.)
- FlyBase FBgn0034432 gene report: protein targeted to inner mitochondrial membrane, catalyzes
  first step of mitochondrial FAO, specific for long-/very-long-chain fatty acids. (web-sourced.)

These corroborate the electronic annotations but cannot be used as `supporting_text` (not in
the cached publications/ folder). Verbatim `supporting_text` in the review is drawn from the
local UniProt record (file:DROME/Acadvl/Acadvl-uniprot.txt), which is an allowed local source.

## Review decisions (rationale)

- GO:0017099 VLCAD activity (IBA + IEA-EC + ISS, ×3): core MF. ACCEPT the IBA (best-grounded
  phylogenetic call), KEEP the redundant IEA/ISS copies as non-core. This is the defining
  function; PANTHER SF11 and CDD VLCAD support the specific level.
- GO:0004466 LCAD activity (IEA-EC + ISS): VLCAD also has long-chain activity (EC 1.3.8.8,
  RHEA:17721; classic palmitoyl-CoA C16 substrate). ACCEPT one, KEEP non-core the duplicate.
- GO:0000062 fatty-acyl-CoA binding (IBA): correct but ancillary substrate binding →
  KEEP_AS_NON_CORE (mirrors human review).
- GO:0003995 acyl-CoA dehydrogenase activity (IEA/InterPro): correct general parent, subsumed
  by specific VLCAD/LCAD terms → KEEP_AS_NON_CORE.
- GO:0016627 oxidoreductase, CH-CH (IEA/InterPro): correct intermediate parent → KEEP_AS_NON_CORE.
- GO:0050660 FAD binding (IEA/InterPro): FAD is the obligate cofactor (UniProt COFACTOR: FAD) →
  ACCEPT (core cofactor feature).
- GO:0005743 mitochondrial inner membrane (IEA/SubCell): UniProt "Mitochondrion inner membrane;
  Peripheral membrane protein" → ACCEPT (core location).
- GO:0005739 mitochondrion (ISS): correct but less specific than inner membrane →
  KEEP_AS_NON_CORE.
- GO:0006631 fatty acid metabolic process (IEA/ARBA): correct but broad parent of beta-oxidation
  → KEEP_AS_NON_CORE.
- GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase (ISS): the exact process
  VLCAD performs → ACCEPT (core BP).

No REMOVE actions: unlike the human entry, there are no cross-paralog mistransfers here; every
electronic call is consistent with the conserved ACAD/VLCAD function and with the human ortholog
P49748 source.

## Core functions chosen
1. Very-long-chain (and long-chain) acyl-CoA dehydrogenase activity (GO:0017099) in
   mitochondrial fatty acid beta-oxidation (GO:0033539), located at mitochondrial inner
   membrane (GO:0005743).
2. FAD binding (GO:0050660) — obligate redox cofactor.
</content>
</invoke>
