# Pde4 (dunce, dnc) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Identity of the benchmark accession
- Q9W4S9 is a Swiss-Prot entry for dnc isoforms N and G (983 aa). The dnc locus (FBgn0000479, CG32498) is split across several Swiss-Prot entries: P12252 (isoform II displayed, 1070 aa; carries the EXP annotation for GO:0004115 from PMID:1660926), Q9W4T4 (isoform I, 1209 aa; the PANTHER-classified member, PTHR11347:SF219), Q8IRU4 (isoform F) and Q9W4S9.
- Q9W4S9 is an alternative N-terminal product of the same gene, not a fragment and not a broken gene model. compare_dnc_entries.py (Pde4-bioinformatics/RESULTS.md) shows a 614-residue identical C-terminal block with P12252, the PDEase domain at 569-898, and every P12252 active-site, cAMP-binding and metal-binding residue conserved (e.g. proton donor P12252 H732 = Q9W4S9 645). PDEase domain is ~71% identical to human PDE4D.
- FlyBase copies gene-level annotations to every dnc UniProt accession, so the Q9W4S9 GOA set equals P12252's minus the EXP row.

### Evolutionary grounding
- PANTHER: fly dnc (Q9W4T4) and C. elegans pde-4 share PTHR11347:SF219; human PDE4A/B/C/D are in separate subfamilies (SF74, SF108, SF135, SF91). Yeast PDE2 (ISS donor SGD:S000005887) is in SF198.
- PAINT: node PTN001682918 carries IBD GO:0004115 with FB:FBgn0000479 among its seeds together with mammalian PDE4s and yeast PDE2, so cAMP PDE activity is ancestral to the clade and the ISS transfer is consistent with the tree.
- PAINT IBA GO:0141162 negative regulation of cAMP/PKA signal transduction is on all human PDE4s (QuickGO); used to replace the generic signal transduction row.
- Q9W4T4 also carries an IBA for GO:0047555 (cGMP PDE activity); not on Q9W4S9, but this conflicts with cAMP specificity; raised as a question.
- PANTHER family review interpro/panther/PTHR11347/PTHR11347-review.yaml: uses Q9W4S9 as reference protein, describes the PDE4/Dunce cAMP branch; no subfamily disagreement (it does not assert a subfamily for Q9W4S9, and SF219 holds the dnc gene via Q9W4T4).

### Primary literature read (abstracts unless noted)
- PMID:1660926 Qiu 1991: dnc cDNA in yeast gives cAMP PDE activity identical to the fly enzyme.
- PMID:3030881 Bellen & Kiger 1987: null females remate every 22-24 h; mutations abolish PDE activity, elevate cAMP.
- PMID:3934032 Gailey 1985: naive dnc males court normally; conditioning defect only.
- PMID:7946340 Levine 1994: shortened circadian period, augmented phase delays, higher cAMP peaks.
- PMID:1848082 Nighorn 1991: dnc PDE concentrated in mushroom body neuropil.
- PMID:6808513 Duerr & Quinn 1982: reduced habituation and short sensitization.
- Full text: PMID:16135747, 19158309, 23197709, 12040051.

### Changes from the previous review
- signal transduction: KEEP_AS_NON_CORE -> MODIFY to GO:0141162.
- chemical synaptic transmission (3 rows): ACCEPT -> MODIFY to GO:0050804 modulation of chemical synaptic transmission (enzyme regulates, does not execute transmission).
- learning -> MODIFY to olfactory learning; memory -> MODIFY to short-term memory (more specific terms already carried, matching the paradigms in the cited studies).
- mating behavior, courtship behavior, circadian rhythm, nonassociative learning: UNDECIDED -> KEEP_AS_NON_CORE, supported by primary papers (the TAS reviews are not cached).
- synapse: ACCEPT -> KEEP_AS_NON_CORE (inferred from process annotation; only neuropil localization shown).
- Core function: added GO:0141162; removed chemical synaptic transmission and synapse from core.
- Added EXP-basis reference PMID:1660926 and five primary papers; review-only TAS references flagged LOW/UNVERIFIED and kept.

### Relative to review next
- Rule: benchmark accession is an alternative-isoform entry of dnc; the canonical entry P12252 (isoform II, carries the EXP) has no review in the repo -> relative is P12252, same_gene_canonical, folder genes/DROME/Pde4__P12252.
- Modules: none in modules/ include dnc.
