# rsfS (P0AAT6, YbeB/RsfA) - manual literature synthesis

No deep-research API was available in this session; this summary was assembled
manually from cached publications (`publications/PMID_*.md`) and PubMed searches
(query: `(RsfS OR YbeB OR "ribosomal silencing factor") AND (Escherichia coli OR bacteria OR ribosome)`, 43 hits, screened by title/abstract).

## Identity
- E. coli K-12 rsfS (b0637; synonyms ybeB, rsfA, slm3), 105 aa, Iojap/RsfS family
  (Pfam PF02410, TIGR00090, HAMAP MF_01477, PANTHER PTHR21043). Orthologs: human
  mitochondrial MALSU1 (C7orf30), yeast Atp25 N-terminus, maize chloroplast Iojap.

## Key findings
1. Association with 50S subunits. iTRAQ proteomics of sucrose-gradient fractions:
   "we identified several uncharacterized proteins that comigrated with the 50S, including YhbY, YbeB, YibL, and YjgA."
   [PMID:16980477]
2. Ribosomal silencing (Hauser et al. 2012, full text read) [PMID:22829778]:
   - binds uL14 (Y2H, pull-down; L14 mutations abolish binding):
     "Thus, we conclude that L14 is the primary and specific binding target of RsfA on the LRS"
   - in vitro: "Purified RsfA suppressed the translational activity dramatically down to about 20%, when RsfA was added to the 50S subunits before the oligo(Phe) synthesis"
     and "We conclude that RsfA blocks association of the ribosomal subunits to functional 70S ribosomes."
     No inhibition of pre-formed programmed 70S (elongation unaffected).
   - in vivo: "These results demonstrate that RsfA acts as a negative modulator of protein translation in vivo in the stationary phase."
   - deletion: stationary-phase viability loss, >10 h lag on rich->poor shift, rescued by casamino acids.
   - no assembly defect reported: "Our results do not indicate any assembly defects as deletion strains of rsfA appear to have perfectly assembled ribosomes"
   - human C7orf30 inhibits mitochondrial poly(U) translation (orthologous function conserved).
3. Pre-50S biogenesis network (Nikolay et al. 2021, abstract only) [PMID:33639093]:
   native ObgE-tagged pre-50S particles carry "a network of interacting biogenesis factors consisting of YjgA, RluD, RsfS, and ObgE on the immature pre-50S subunit".
   UniProt (curated from the full text) adds that RsfS contacts ObgE and enhances its GTPase activity.
4. Growth-arrest recovery (2026, full text) [PMID:41965359]: in a delta-rimM strain RsfS
   accumulates on pre-50S and mature 50S; "Upregulated RsfS levels safeguard the 50S subunits until 30S assembly is complete."
   In wild type "Only a small fraction of these particles was bound by RsfS."
5. Reviews: [PMID:35790407] "Is RsfS a Hibernation Factor or a Ribosome Biogenesis Factor?" (abstract only)
   frames the open question; [PMID:42530354] (2026 MMBR review, abstract only) groups RsfS with
   factors that "prevent the association of the 30S ribosomal subunit with the 50S subunit".

## Interpretation
RsfS is a small cytosolic 50S-binding protein that docks on uL14 at the subunit interface
(near bridge B8), sterically preventing 30S joining. This silences translation in stationary
phase/nutrient downshift and acts as a checkpoint keeping immature (pre-50S) subunits out of
translation; it is part of a late 50S biogenesis factor network with ObgE, RluD and DarP.
