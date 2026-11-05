# GALNS (human) — review notes

UniProtKB:P34059 · HGNC:4122 · N-acetylgalactosamine-6-sulfatase (galactose-6-sulfate sulfatase; GalN6S) · EC 3.1.6.4

Deep research: falcon provider was out of credits (HTTP 402) at the time of this review, so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record
(`GALNS-uniprot.txt`), the seeded GOA (`GALNS-goa.tsv`), cached publications, and cached Reactome entries.

## Core biology (verified)

- **Molecular function.** GALNS is a lysosomal sulfatase that hydrolytically removes the 6-O-sulfate
  group from two terminal sugars: N-acetyl-D-galactosamine-6-sulfate (in chondroitin-6-sulfate) and
  D-galactose-6-sulfate (in keratan sulfate). EC 3.1.6.4.
  [PMID:22940367 "removes sulfate groups from a terminal N-acetylgalactosamine-6-sulfate (or galactose-6-sulfate) in mucopolysaccharides such as keratan sulfate and chondroitin-6-sulfate"]
  UniProt CATALYTIC ACTIVITY: "Hydrolysis of the 6-sulfate groups of the N-acetyl-D-galactosamine 6-sulfate
  units of chondroitin sulfate and of the D-galactose 6-sulfate units of keratan sulfate."
  The GO term GO:0043890 "N-acetylgalactosamine-6-sulfatase activity" has a definition that matches
  this exactly and is the correct core MF term (present in GOA as IEA, TAS, EXP, and IDA).

- **Formylglycine dependence.** Like all sulfatases, GALNS requires post-translational conversion of an
  active-site cysteine (Cys79, in a CXPXR motif) to Cα-formylglycine (3-oxoalanine), catalysed by the
  formylglycine-generating enzyme SUMF1/FGE; this modified residue is the catalytic nucleophile.
  [PMID:22940367 "FGE recognizes this motif and converts Cys 79 into a formylglycine aldehyde"]
  SUMF1 is the master regulator of all 17 human sulfatases; loss of SUMF1 causes multiple sulfatase
  deficiency. SUMF2 modulates (dampens) SUMF1 enhancement of sulfatase activity [PMID:15962010].

- **Cofactor / structure.** Homodimeric glycoprotein; each monomer binds one Ca2+ ion coordinating the
  formylglycine nucleophile [PMID:22940367]. Two N-glycosylation sites (Asn204, Asn423); three disulfide bonds.

- **Localisation.** Lysosome / lysosomal lumen. Immunostaining in cultured lung fibroblasts confirms
  lysosomal localisation [PMID:30760748 "GALNS indeed showed a lysosomal localization in both ever smokers and COPD patients"].
  As a secreted lysosomal hydrolase it is also detected extracellularly (extracellular exosome HDA
  PMID:23533145; extracellular region / azurophil granule lumen via neutrophil degranulation Reactome).

- **Biological process.** Catabolism of the glycosaminoglycans keratan sulfate and chondroitin-6-sulfate.
  GOA carries GO:0030207 chondroitin sulfate proteoglycan catabolic process (IDA, PMID:18285341 — modulating
  GALNS/ASB expression changes cellular chondroitin sulfate content). The keratan-sulfate side of the core
  BP is not yet in GOA; GO:0042340 (current label "keratan sulfate proteoglycan catabolic process") is the
  correct term and is added as a NEW annotation.

- **Disease.** Deficiency causes mucopolysaccharidosis type IVA (MPS IVA / Morquio A syndrome; MIM 253000),
  an autosomal recessive lysosomal storage disease with intracellular accumulation of keratan sulfate and
  chondroitin-6-sulfate; short stature, skeletal dysplasia, corneal clouding, normal intelligence.
  Extensive allelic heterogeneity; most missense mutations destabilise the fold rather than hit the active
  site [PMID:22940367].

## Annotation-by-annotation decisions (summary)

- GO:0004065 arylsulfatase activity (IBA) — ACCEPT. Family-level MF, correct but broad; PAN-GO/IBA term
  for the sulfatase family. Not the most specific term but not wrong.
- GO:0005764 lysosome (IEA, GO_REF:0000120) — ACCEPT. Consistent with IDA + UniProt SUBCELL.
- GO:0043890 N-acetylgalactosamine-6-sulfatase activity (IEA) — ACCEPT. This is the correct core MF.
- GO:0043890 (TAS, Reactome:R-HSA-2263490) — ACCEPT. Same correct MF, Reactome-sourced.
- GO:0005764 lysosome (IDA, PMID:30760748) — ACCEPT. Direct immunolocalisation.
- GO:0043890 (EXP, PMID:22940367) — ACCEPT. Structure/enzymology paper; correct core MF.
- GO:0030207 chondroitin sulfate proteoglycan catabolic process (IDA, PMID:18285341) — ACCEPT (non-core
  vs KS but a genuine core catabolic role). Core BP.
- GO:0043890 (IDA, PMID:18285341) — ACCEPT. Correct core MF, IDA.
- GO:0005576 extracellular region (TAS, Reactome R-HSA-6798751 neutrophil degranulation) — KEEP_AS_NON_CORE.
  Secreted-fraction / degranulation localisation, not the primary site of action.
- GO:0035578 azurophil granule lumen (TAS, Reactome) — KEEP_AS_NON_CORE. Neutrophil degranulation context.
- GO:0043202 lysosomal lumen (TAS, Reactome R-HSA-2263490) — ACCEPT. Precise site of action.
- GO:0070062 extracellular exosome (HDA, PMID:23533145) — KEEP_AS_NON_CORE. High-throughput proteomics of
  prostatic-secretion exosomes; localisation byproduct, not core.
- GO:0043202 lysosomal lumen (TAS, Reactome R-HSA-1630304) — ACCEPT. Precise site of action.
- GO:0008484 sulfuric ester hydrolase activity (IDA, PMID:15962010) — MARK_AS_OVER_ANNOTATED. Parent MF
  (sulfuric ester hydrolase); GALNS's specific activity GO:0043890 is the informative child. The SUMF1/SUMF2
  paper measured GALNS activity as one of several sulfatases; the general term is subsumed by the specific one.
- GO:0003943 N-acetylgalactosamine-4-sulfatase activity (TAS, PMID:8325655) — MODIFY → GO:0043890. This is
  the wrong specificity: GALNS is a 6-sulfatase; the 4-sulfatase is ARSB. The cited paper (PMID:8325655) is a
  chromosome-mapping abstract that does not assay 4-sulfatase activity. TAS (not experimental), so replacing
  the mistaken 4-sulfatase term with the correct 6-sulfatase term is appropriate.

## NEW
- GO:0042340 keratan sulfate proteoglycan catabolic process — the KS-degradation half of the core BP,
  supported by UniProt FUNCTION and the structure paper; Reactome models "Keratan sulfate degradation"
  (R-HSA-2022857) with GALNS.


## 2026-11-02 — catalytic specificity and source reassessment

The single GALNS 6-sulfatase activity covers both chondroitin GalNAc6S and keratan Gal6S. Direct human enzyme experiments distinguish synthetic substrate promiscuity from physiological glycan specificity: purified GALNS hydrolyzes 4-MU-sulfate with kcat 4.2/min and the coupled 4-MU-Gal6S substrate with kcat 228/min. The aryl reaction is real chemistry but is kept outside the defining physiological core. The product-soaked GalNAc crystal pose is nonproductive. Formylglycine maturation and calcium support the catalytic mechanism; they are not separate molecular functions (PMID:22940367).

The original human kidney study measures chondroitin-6-sulfate oligosaccharide desulfation in crude extracts and corrects a 2.4% arylsulfatase B contribution from contaminating 4-sulfated substrate. It does not demonstrate GALNS 4-desulfation (PMID:820716). The selected original MCF-7 study reports changes in GALNS activity and total chondroitin sulfate after GALNS manipulation, but unchanged C4S and ASB activity; its explicit 4-MU-sulfate recipe belongs to ASB, with the GALNS protocol referred to prior work (PMID:18285341). GALNS is actually present among the cDNA activity assays in the SUMF study, although its detailed supplementary substrate recipe remains inaccessible (PMID:15962010).

The earlier judgment on PMID:8325655 overstated what its abstract established. The abstract names a human 6-sulfatase and a fibroblast enzyme assay, but the full assay substrate was not recovered. The specific incoming 4-sulfatase assertion is now unresolved, without a wrong-gene claim. The old MISCITED finding remains historical. The broad sulfuric ester hydrolase annotation is refined to the directly supported 6-sulfatase child.

Human GALNS/LAMP1 colocalization supports the lysosome annotations, and the normal Reactome R-HSA-1630304 reaction supplies the lysosomal keratan pathway context (PMID:30760748). The inherited keratan-catabolic proposal is retained because GALNS itself performs desulfation, supported by same-role comparator annotations and nonredundant typed ancestry. Its evidence/reference is explicitly revised from EXP/PMID:22940367 to TAS/Reactome:R-HSA-1630304: the former paper directly assays synthetic substrates. Defective-mutant event R-HSA-2263490 is kept distinct from the normal catalytic reaction.

The urinary-vesicle occurrence is supported by the actual P34059 row in Supplemental Table 2 of PMID:23533145: sheet SI Table 2, row 319, 7/7/10/9 unique peptides. This supports non-core fraction association without inferring topology or biogenesis. It explicitly revisits the October 10 over-annotation decision; both that old review row and the preceding non-core journal wording remain historical. The neutrophil Reactome input/output sets likewise support contextual cargo locations, not GALNS-driven exocytosis.

One canonical 522-residue sequence is declared. Signal removal and mature-chain processing are not alternative splice products. The exact target sequence and arylsulfatase IBD node were checked in the actual family tree, retaining the incoming/later donor difference as dated provenance. The source archive preserves all original contexts and historical quotation locators without duplicating the current judgments. The private proposal was subsequently reconciled with the genuine native acquisition documented below.

## 2026-11-02: genuine native reconciliation

The actual UniProt snapshot and 15-row, 16-column GOA export match the independently inspected inputs. A private genuine native seed resolves all 15 current source joins without overwriting the inherited review. The canonical sequence is 522 residues; signal processing does not create an alternative product. The original part_of atom is restored on native row 11. The retained keratan process remains a separate TAS/Reactome NEW.

All 36 normal sources are present: 18 main files were reused unchanged and 18 previously missing files were acquired through native paths. All four active excerpts are exact native-cache substrings, preserving the two active inherited associations and all 29 historical associations through immutable locators. Source access notes continue to describe the actual reading scope, independently of cache availability. Scoped validation and rendering outcomes are pending.

## 2026-11-02: scoped validation outcomes

Default schema, ontology, reference and best-practice validation passed with zero advisories. Strict GOA reconciliation confirms all 15 source annotations, with the separate retained NEW preserved. The status audit computed COMPLETE while retaining the specific 4-sulfatase UNDECIDED judgment; the initial DRAFT mismatch remains in the execution record. Native EDIT history, final status and the private 16-row/one-core/13-reference render passed. All 36 scientific sources and the GO term cache remain unchanged by authored curation.


## 2026-11-04 — Substrate specificity and the evidence for glycan degradation

GALNS uses formylglycine derived from Cys79 and a calcium-containing active site to remove 6-sulfate groups from chondroitin and keratan substrates. Human kidney oligosaccharide assays and recombinant-enzyme kinetics support that defining chemistry. The same purified recombinant protein also turns over synthetic 4-MU-sulfate, so its arylsulfatase annotation retains non-core measured chemistry without assigning a physiological aryl substrate ([PMID:820716](https://pubmed.ncbi.nlm.nih.gov/820716/), [PMID:22940367](https://pubmed.ncbi.nlm.nih.gov/22940367/)).

The 4-sulfatase TAS claim remains unresolved. Correcting a small separate ARSB contribution in a crude preparation is not a direct comparison that rules out all GALNS 4S activity. The additional mutation/transfection abstract and diagnostic-assay Methods do not provide that comparison either ([PMID:1522213](https://pubmed.ncbi.nlm.nih.gov/1522213/), [PMID:24726177](https://pubmed.ncbi.nlm.nih.gov/24726177/)). The 6-sulfatase term describes a different positional reaction, rather than a more specific descendant of the 4-sulfatase term. No wrong-gene or negative-assay claim is inferred from inaccessible Methods.

The normal [GALNS keratan reaction](https://reactome.org/content/detail/R-HSA-1630304) identifies the enzyme performing the sulfate-hydrolysis step, and the [keratan degradation pathway](https://reactome.org/content/detail/R-HSA-2022857) establishes proteoglycan-level process context. The retained NEW remains TAS, separate from the 15 current source rows. Its former EXP attribution to a synthetic-substrate paper remains preserved historically. The repository module agrees with this mechanism but cites the gene review, so it does not supply independent evidence.

The proteomic target row securely identifies GALNS in the urinary preparation, but does not separate exosome association from surface binding or co-isolation of soluble enzyme ([PMID:23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/), Supplemental Table 2, sheet SI Table 2 row 319). The specific exosome annotation is therefore again MARK_AS_OVER_ANNOTATED, as on October 10; the positive detection and exact peptide counts remain recorded. More peptides cannot by themselves settle vesicle association, and this judgment does not assert absence from vesicles.

Eight inherited reference-finding statements are restored with individual assessments. The chromosome-mapping statement's categorical claim that no 4S assay was performed is disputed because the original assay has not been inspected, without declaring the biological claim experimentally refuted. The revised 18285341 anchor explicitly retains the joint ASB/GALNS subject; its selected Results show GALNS-specific total-CS effects while C4S remains unchanged. Eight concise current snippets are source-exact, remain below 25 words per source and are not repeated in this appended section.

This bounded proposal preserves the 15 original machine contexts, literal extension, canonical product, one core and all 36 source files. Default validation passed with zero advisories. Strict GOA matched all 15 originals, preserving the separate TAS NEW. Native EDIT history, COMPLETE status audit, private 16-row/one-core/17-reference render, public links and whitespace checks passed. The 4-sulfatase judgment remains UNDECIDED; all 36 source files remain unchanged.

## 2026-11-04 — Positional specificity and primary-result reconciliation

The current review separates three observations in the purified human enzyme study: its stated normal 6-sulfated-galactoside specificity, direct synthetic 4-MU-Gal6S turnover, and measurable synthetic aryl-sulfate turnover interpreted by the authors as substrate promiscuity ([PMID:22940367](https://pubmed.ncbi.nlm.nih.gov/22940367/)). Short exact anchors now support each claim once. Positive 6S evidence does not by itself test every possible 4S substrate. A lateral term correction could be appropriate if the original mapping error were established; the unavailable substrate details underlying PMID:8325655 leave that particular assertion uncertain. No annotation action changes.

The [author-uploaded original of PMID:18285341](https://www.researchgate.net/publication/5567525_Distinct_Effects_of_N-Acetylgalactosamine-4-sulfatase_and_Galactose-6-sulfatase_Expression_on_Chondroitin_Sulfates), Results/Table 2/Figure 2 caption, distinguishes the GALNS-specific CS and C4S outcomes that the collective abstract compresses with ASB results. GALNS manipulation changes total CS without the C4S increase after silencing or change after overexpression reported in the collective framing. Table 1 separately concerns enzyme activity. The reference assessment now states this apparent abstract-versus-Results discrepancy explicitly and uses the narrower per-gene Results for interpretation. These cellular results are not a purified comparative substrate assay and cannot establish universal absence of GALNS 4S side activity. The normal cache remains abstract-only; selected original text and caption were read externally, but figure images and the earlier referenced GALNS assay recipe were not inspected.

The UniProt finding now has a source-derived record-section locator. Its statement and excerpt remain exact, as do all eight inherited finding statements, all original contexts, the separate TAS keratan proposal, the canonical sequence and the prior journal. Current excerpts are kept only in the review and recorded by byte offsets in the evidence archive.

Target validation passed with zero advisories; strict GOA matched all 15 originals, with the separate TAS NEW preserved. Native codex EDIT history, COMPLETE status audit, private 16-row/one-core/17-reference rendering and whitespace checks passed. One source-specific UNDECIDED judgment remains; all 36 scientific sources are unchanged.
