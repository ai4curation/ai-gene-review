# PP_0423 curation notes

## 2026-07-18: selection and first-pass assessment

- PP_0423 was selected after the PSEPK module/pathway/taxon OpenScientist report
  identified it outside the KEGG `ppu00785` bucket as a possible GcvH-relay
  component [`file:projects/P_PUTIDA/deep-research/PSEPK__endogenous_protein_lipoylation__ppu00785-deep-research-openscientist.md`].
- UniProt Q88QR5 is an unreviewed 234-aa protein named only as a BPL/LPL
  catalytic-domain-containing protein. It carries InterPro `IPR050664`
  (LipM/LipL octanoyltransferase family) and PANTHER `PTHR43679:SF2`
  [`file:PSEPK/PP_0423/PP_0423-uniprot.txt`, "DR   InterPro; IPR050664; Octanoyltrans_LipM/LipL."].
- The local PANTHER member table assigns both characterized *Bacillus subtilis*
  LipM (P54511) and LipL (P39648) to `PTHR43679:SF2`. The family/subfamily call
  therefore does not distinguish octanoyl-ACP:GcvH transfer from
  octanoyl-GcvH:E2 amidotransfer [`file:interpro/panther/PTHR43679/PTHR43679-entries.csv`].
- The fetched QuickGO table contains no GO annotations. No molecular function
  is proposed in the first pass because substrate direction and physiological
  role remain unresolved.
- Current module decision: retain PP_0423 as a high-priority uncertain relay
  or salvage candidate. Do not count it as satisfying a relay variant, do not
  assign a salvage reaction, and do not alter the covered LipB/LipA
  direct-route call.

## OpenScientist assessment

The gene-level report favors an ATP-dependent LplA-type salvage-ligase
hypothesis based on sequence similarity, a predicted interaction network, and
single-domain LplA precedents
[`file:PSEPK/PP_0423/PP_0423-deep-research-openscientist.md`]. Those are useful
hypothesis-generating observations, but they do not discriminate the reaction
experimentally. The report explicitly retains ligase-versus-transferase
ambiguity, consistent with the family-level evidence above. The first-pass
review therefore records no specific GO molecular function.

## Discriminating experiments

1. Test purified PP_0423 with octanoyl-ACP plus apo-GcvH and, separately, with
   octanoyl-GcvH plus apo E2 lipoyl domains; identify modified lysines by mass
   spectrometry.
2. Compare lipoylation of GcvH and E2 clients in wild type, `PP_0423` deletion,
   `lipB` deletion, and double-mutant strains to determine whether PP_0423 is a
   redundant transferase, a relay enzyme, or unrelated to lipoylation.
