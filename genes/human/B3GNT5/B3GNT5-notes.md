# B3GNT5 (Q9BYG0) review notes

## Summary of gene function

B3GNT5 encodes **Lactosylceramide 1,3-N-acetyl-beta-D-glucosaminyltransferase**
(EC 2.4.1.206), also called **lactotriaosylceramide synthase / Lc3 synthase /
beta-1,3-N-acetylglucosaminyltransferase 5 (beta3Gn-T5)**. It is the enzyme that
**initiates the (neo)lacto-series glycosphingolipid branch**: it transfers GlcNAc
from UDP-GlcNAc onto **lactosylceramide (LacCer)** to make **lactotriaosylceramide
(Lc3Cer, GlcNAcbeta1-3Galbeta1-4Glc-ceramide)**, the committed precursor of the
lacto/neolacto-series glycosphingolipids that carry Lewis and HNK-1 antigens.

Key facts grounded in the authoritative UniProt record
[file:human/B3GNT5/B3GNT5-uniprot.txt]:

- RecName "Lactosylceramide 1,3-N-acetyl-beta-D-glucosaminyltransferase";
  AltName "Lactotriaosylceramide synthase / Lc(3)Cer synthase / Lc3 synthase";
  EC=2.4.1.206 [file:human/B3GNT5/B3GNT5-uniprot.txt].
- FUNCTION: "Beta-1,3-N-acetylglucosaminyltransferase that plays a key role in
  the synthesis of lacto- or neolacto-series carbohydrate chains on glycolipids,
  notably by participating in biosynthesis of HNK-1 and Lewis X carbohydrate
  structures. Has strong activity toward lactosylceramide (LacCer) and
  neolactotetraosylceramide (nLc(4)Cer; paragloboside), resulting in the synthesis
  of Lc(3)Cer and neolactopentaosylceramide (nLc(5)Cer), respectively."
  [file:human/B3GNT5/B3GNT5-uniprot.txt].
- CATALYTIC ACTIVITY 1 (core): LacCer + UDP-GlcNAc -> Lc3Cer + UDP + H+
  (RHEA:13905, EC 2.4.1.206), evidence PubMed:11283017 and PubMed:11384981
  [file:human/B3GNT5/B3GNT5-uniprot.txt]. This is exactly GO:0047256.
- CATALYTIC ACTIVITY 2 (extension): nLc4Cer + UDP-GlcNAc ->
  IV(3)-beta-GlcNAc-nLc4Cer (RHEA:23004), evidence PubMed:11283017
  [file:human/B3GNT5/B3GNT5-uniprot.txt]. This maps well to GO:0008532
  (N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransferase activity).
- SUBCELLULAR LOCATION: "Golgi apparatus membrane; Single-pass type II membrane
  protein" (ECO:0000250, i.e. by similarity)
  [file:human/B3GNT5/B3GNT5-uniprot.txt]. Topology: cytoplasmic 1-14,
  TM 15-35 (signal-anchor for type II membrane protein), lumenal 36-378.
- SIMILARITY: glycosyltransferase 31 family (CAZy GT31); Pfam PF01762
  Galactosyl_T; InterPro IPR002659 Glyco_trans_31; PANTHER PTHR11214:SF21
  [file:human/B3GNT5/B3GNT5-uniprot.txt].
- INTERACTION: "Q9BYG0; Q9UHG0: DCDC2" NbExp=3
  [file:human/B3GNT5/B3GNT5-uniprot.txt] — corresponds to the IntAct/HuRI
  binary interaction annotated as GO:0005515 protein binding (PMID:32296183).

## Primary literature (both abstract-only in cache)

- PMID:11283017 (Togayachi et al. 2001, J Biol Chem) — cloning/characterization
  of human & rat beta3Gn-T5; establishes Lc3Cer synthase activity. UniProt cites
  this as EC 2.4.1.206 evidence. Cache `full_text_available: false`; abstract:
  "beta3Gn-T5 exhibited strong activity to transfer GlcNAc to glycolipid
  substrates, such as lactosylceramide (LacCer) and neolactotetraosylceramide
  (nLc(4)Cer; paragloboside), resulting in the synthesis of Lc(3)Cer and
  neolactopentaosylceramide (nLc(5)Cer), respectively"
  [PMID:11283017]. Also documents retinoic-acid up-regulation / TPA
  down-regulation and rat brain developmental expression changes.
- PMID:11384981 (Henion et al. 2001, J Biol Chem) — cloning of the mouse Lc3
  synthase gene; the human/mouse GOA experimental annotations (GO:0047256 IDA;
  GO:0007417 CNS development IDA; GO:0009247 & GO:0009101 TAS) trace to this
  paper. Cache `full_text_available: false`. Abstract:
  "The entry point for lacto-series glycolipids is catalyzed by the beta1,3
  N-acetylglucosaminyltransferase GlcNAc(beta1,3)Gal(beta1,4)Glc-ceramide (Lc3)
  synthase enzyme" and "In situ hybridization analysis revealed that that the
  Lc3 synthase was expressed in most tissues at embryonic day 11 with elevated
  expression in the developing central nervous system"
  [PMID:11384981]. Note: this is a mouse paper; the human GOA IDA annotations
  are propagated by curators who read the full text. Per policy, experimental
  annotations are not removed on the basis of the abstract-only cache.
- PMID:32296183 (Luck et al. 2020, Nature) — HuRI human binary interactome map;
  source of the IntAct B3GNT5–DCDC2 interaction (GO:0005515 IPI). Full text
  available but is a systematic dataset paper; the specific pair is in the
  supplementary interaction data, not discussed in prose. Kept as
  MARK_AS_OVER_ANNOTATED per bare-protein-binding policy.

## Reactome

- R-HSA-9846501 "B3GNT5 transfers GlcNAc to LacCer" — the reaction event; source
  of GO:0047256 TAS and GO:0000139 TAS. Summary matches UniProt exactly.
- R-HSA-9840309 "Glycosphingolipid biosynthesis" — pathway; source of GO:0006688
  TAS.

## Verified GO term ids (OLS, 2026-07)

- GO:0047256 lactosylceramide 1,3-N-acetyl-beta-D-glucosaminyltransferase
  activity — def matches RHEA:13905 exactly (LacCer + UDP-GlcNAc -> Lc3Cer).
  **CORE MF.**
- GO:0008532 N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransferase
  activity — matches the nLc4Cer extension (second catalytic activity). Not
  currently in GOA; noted as an additional/secondary activity, not made core.
- GO:0006688 glycosphingolipid biosynthetic process — CORE BP (there is no
  more specific "lacto-series glycosphingolipid biosynthetic process" term in GO;
  GO:0001572 is lactosylceramide biosynthesis, i.e. the substrate not product).
- GO:0000139 Golgi membrane — CORE location; consistent with UniProt "Golgi
  apparatus membrane; Single-pass type II membrane protein".

## Annotation review reasoning (high level)

- Core enzymatic identity (GO:0047256), Golgi-membrane localization (GO:0000139),
  and glycosphingolipid biosynthesis (GO:0006688) are all well supported and
  ACCEPTED.
- Generic IEA MF/BP terms (glycosyltransferase activity GO:0016757,
  hexosyltransferase activity GO:0016758) are correct-but-general; MODIFY to the
  specific GO:0047256, or KEEP_AS_NON_CORE as accurate parents.
- GO:0009101 glycoprotein biosynthetic process is a mis-grouping: B3GNT5
  glycosylates a **glycolipid** (ceramide), not a protein. The InterPro IEA and
  the UniProt PATHWAY line ("protein glycosylation") reflect a family-level
  default for GT31; for this enzyme the product is a glycosphingolipid, not a
  glycoprotein. MARK_AS_OVER_ANNOTATED (IEA) / MARK_AS_OVER_ANNOTATED (TAS from
  the mouse paper, which is about glycolipids). GO:0009247 glycolipid
  biosynthetic process is the correct-but-general form and is KEEP_AS_NON_CORE.
- GO:0007417 central nervous system development (IDA, PMID:11384981): the mouse
  Lc3 synthase is developmentally expressed and enriched in developing CNS
  (in situ hybridization). This is an expression/developmental-context
  annotation, not a demonstrated developmental function; KEEP_AS_NON_CORE
  (pleiotropic/developmental context, not the core molecular role).
- GO:0016020 membrane (IEA, InterPro) is an uninformative parent of Golgi
  membrane; MODIFY to GO:0000139.
- GO:0005515 protein binding (IPI, DCDC2) — bare protein binding; per policy
  MARK_AS_OVER_ANNOTATED (not removed).
</content>
</invoke>
