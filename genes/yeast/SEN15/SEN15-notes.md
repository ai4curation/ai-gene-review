# SEN15 (Q04675, YMR059W) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files and prediction-evidence folders were not opened or used. This is a
de novo review; no earlier SEN15 notes or review existed in this folder.

### Deep research

`just deep-research-falcon yeast SEN15 --fallback perplexity-lite` failed: falcon
(Edison) raised "Failed to authenticate", and the perplexity-lite fallback returned
HTTP 401 "You exceeded your current quota". No deep-research file was produced. The
review is built from primary literature cached in `publications/` (listed below) and
the UniProt record.

### Identity

- Q04675 SEN15_YEAST, 128 aa, Swiss-Prot reviewed, PE 1. Gene SEN15, ORF YMR059W,
  SGD:S000004663. Single product; the EMBL CAA89769.1 translation has an erroneous
  initiation (UniProt sequence caution), not an alternative isoform.
- Domains: Pfam PF09631 (Sen15), IPR018593 (tRNA-endonuc_su_Sen15), IPR042777
  (Sen15_fungi), plus the superfamily-level IPR011856/IPR036167 matches to the
  archaeal endonuclease fold.

### Evolutionary placement

- PANTHER PTHR28518 / PTHR28518:SF1 (TRNA-SPLICING ENDONUCLEASE SUBUNIT SEN15),
  the same subfamily as S. pombe sen15 (Q7LKV3). The SEN15 IBA rows come from PAINT node
  PTN002003396 and list SGD:S000004663 itself as a source: that is the expected marker
  that this gene's own IDA/IPI data seeded the node, not circularity.
- PAINT propagated only GO:0000214 (complex) and GO:0000379 (splice-site recognition and
  cleavage) from PTN002003396. SGD's IDA contributes_to GO:0000213 tRNA-intron lyase
  activity was not propagated. For SEN15 itself this does not matter (the IDA is direct),
  but the omission is treated as a deliberate PAINT choice when the yeast data are used as
  a transfer reference.
- Human TSEN15 (Q8WW01) is in a different PANTHER family (PTHR28582), sharing only the
  Pfam Sen15 domain. Human structural results are used here only at the level of complex
  architecture and are not transferred as SEN15-specific functions. Song & Markley give
  20% identity between human and S. cerevisiae Sen15 [PMID:17166513 "it shows only 23% and
  20% sequence identities, respectively, to two yeast orthologs, Sp Sen15 from
  Schizosaccharomyces pombe and Sc Sen15 from Saccharomyces cerevisiae."], and S. cerevisiae
  Sen15 lacks the archaeal N-terminal domain [PMID:17166513 "the N-terminal domain of
  MJ_endo ( β 1 , β 2 , α 1 , β 3 and β 4 ) has been deleted in Sc Sen15 and ST_endo2"].

### What is experimentally established in S. cerevisiae

1. Subunit of the tRNA-splicing endonuclease, and essential [PMID:9200603 "We have cloned
   the genes encoding all four protein subunits of endonuclease. Each gene is essential."]
   (abstract only in cache; UniProt records N-terminal protein sequencing of Sen15 from the
   purified enzyme: "CHARACTERIZATION, PROTEIN SEQUENCE OF 1-11, AND SUBUNIT").
2. Not a catalytic subunit: the 5' and 3' active sites are Sen2 and Sen34 [PMID:9200603 "the
   eucaryal tRNA splicing endonuclease contains two functionally independent active sites for
   cleavage of the 5' and 3' splice sites, encoded by SEN2 and SEN34, respectively."]. The 5'
   site is a composite active site that also uses Sen34 residues [PMID:16710424 "catalysis at
   the 5' splice site requires the conserved cation-pi sandwich derived from the Sen34 subunit
   in addition to the catalytic triad of Sen2"]; Sen15 has no reported catalytic residues.
3. Direct partner of Sen34 (two-hybrid; UniProt SUBUNIT "Interacts directly with SEN34",
   ECO:0000269 PMID:9200603; summarized in PMID:17166513 "Yeast two-hybrid analysis further
   showed strong interactions between Sen2 and Sen54 and between Sen34 and Sen15"). Large-scale
   affinity-purification MS (PMID:37968396) is the second GO:0005515 IPI source, also with SEN34.
4. Localization: the endonuclease (assayed via Sen2p, Sen54p and enzyme activity, not Sen15p
   directly) is peripherally associated with the cytosolic face of the mitochondrial outer
   membrane [PMID:12925762 "The endonuclease is peripherally associated with the cytosolic
   surface of the outer mitochondrial membrane."], with "only a small amount, if any, of the
   enzyme" in the nucleus. Fractionation separated the enzyme from ER (Sec63p) and nuclear
   markers. UniProt's "Endomembrane system" and "Nucleus" lines for Sen15 cite this same
   paper; neither is well supported for Sen15 specifically.

### Complex-level findings not transferred to Sen15 as process annotations

- Dhungel & Hopper 2012 (PMID:22391451, abstract only): a nuclear-restricted SEN complex
  splices pre-tRNA but does not rescue growth, revealing an essential cytoplasmic function
  that "requires all four SEN complex subunits and the catalytic core"; a subset of pre-rRNAs
  accumulates, suggesting moonlighting in rRNA processing.
- Tsuboi et al. 2015 (PMID:25971974, full text): the Sen complex cleaves the mitochondria-
  localized CBP1 mRNA; cleavage depends on Sen2 catalytic H297 and on mitochondrial
  localization (sen54-Δ(200–232)). Sen15 was not assayed individually.
- These are necessity/complex-level data. The cleaving entities are Sen2/Sen34; Sen15's
  contribution, if any, is structural. No NEW process term was proposed; the issue is raised
  as a suggested question.

### Decisions

- GO:0000213 contributes_to (IDA): ACCEPT — correct use of contributes_to for a noncatalytic
  subunit of the enzyme.
- GO:0000214 (IBA, IDA, IEA, IPI): ACCEPT all.
- GO:0000379 (IBA, IDA, IEA): ACCEPT all.
- GO:0006388 (IEA): MODIFY → GO:0000379; Sen15 has no role in the ligation step.
- GO:0003676 (IEA superfamily mapping): MARK_AS_OVER_ANNOTATED.
- GO:0005515 ×2 (IPI with SEN34): REMOVE per protein-binding policy; the interaction is real
  and is captured by complex membership.
- GO:0005741 (IEA, NAS): ACCEPT; the NAS cites the 1997 paper, which predates the
  mitochondrial localization finding (PMID:12925762) — the claim is right, the reference
  attribution looks off, but the 1997 full text was not read so no source defect is asserted.
- GO:0005634 (IEA): KEEP_AS_NON_CORE — at most a minor pool.
- GO:0012505 endomembrane system (IEA): MARK_AS_OVER_ANNOTATED — GO's endomembrane system
  excludes mitochondria, and the cited fractionation separated the enzyme from ER/nuclear
  envelope markers.
