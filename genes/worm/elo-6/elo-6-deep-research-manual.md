# elo-6 (C. elegans, Q20303, F41H10.8) - manual literature review

Deep-research APIs were not available for this session; this file records a manual
literature search (PubMed via MCP, cached publications) performed by the reviewer.

## Search
- PubMed `elo-6 elegans branched-chain fatty acid`: 1 hit (PMID:15340492).
- PubMed `(elo-5 OR elo-6) AND (mmBCFA OR "monomethyl branched-chain") AND elegans`: 4 hits
  (PMID:15340492, PMID:34826420, PMID:37245562, PMID:38704027). The three later papers study
  elo-5, not elo-6; PMID:38704027 was cached because it states the precursor of the worm
  sphingoid base.

## Key findings

1. **Identity and family.** ELO-6 is one of eight C. elegans homologues of the yeast
   long-chain fatty-acid elongation enzymes [PMID:15340492 "we identified eight sequences
   homologous to the yeast long-chain FA elongation enzymes"]. UniProt places it in the ELO
   family (Pfam PF01151, PROSITE PS01188, PANTHER PTHR11157:SF27) with seven predicted
   transmembrane helices.

2. **Role in mmBCFA synthesis (RNAi + GC).** RNAi of elo-5 (F41H10.7) and elo-6 (F41H10.8)
   altered branched-chain FA levels [PMID:15340492 "the RNAi treatment of the two remaining
   genes, elo-5 (F41H10.7) and elo-6 (F41H10.8), affected the levels of branched-chain FA"].
   elo-6 RNAi lowered only C17ISO [PMID:15340492 "The RNAi of elo-6 significantly reduced the
   amount of only C17ISO"], leading the authors to suggest that ELO-6 elongates C15ISO to C17ISO
   [PMID:15340492 "ELO-6 may function in elongating C15ISO to C17ISO"].

3. **No direct biochemical assay.** The paper contains no heterologous expression or in vitro
   elongase assay for ELO-6; the C15ISO->C17ISO reaction assigned in UniProt (RHEA:35335, with
   ECO:0000269 to PMID:15340492) is an inference from the RNAi fatty-acid profile plus family
   membership.

4. **Phenotype.** elo-6 RNAi caused no obvious growth or morphological defects, unlike elo-5
   [PMID:15340492 "the suppression of elo-6 activity by feeding double-stranded RNA (dsRNA) to
   wild-type animals did not cause obvious morphological or growth defects"].

5. **Expression.** elo-6 promoter::GFP is expressed in the gut, neurons, pharynx and vulval
   muscles [PMID:15340492 "elo-6 was expressed in neurons, pharynx, and vulva muscles"].

6. **Regulation.** elo-6 promoter activity is lowered by lpd-1 (SREBP homologue) RNAi
   [PMID:15340492 "elo-5 and elo-6 transcription is downregulated in the absence of lpd-1"].

7. **Sphingolipids.** The worm sphingoid base derives from C15ISO (the ELO-5 product), not
   from C17ISO [PMID:38704027 "Serine palmitoyltransferase (SPT) catalyzes the condensation of a
   monomethyl branched chain fatty acid C15ISO and serine to form the precursor of the
   iso-branched d17:1 (id17:1) sphingoid base"]. No study links ELO-6 to sphingolipid synthesis.

## Gaps
- No enzymology, substrate range or subcellular localisation study of ELO-6 itself.
- No deletion-allele phenotype analysis beyond RNAi in the literature found.
