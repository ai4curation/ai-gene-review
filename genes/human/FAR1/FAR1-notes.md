# FAR1 (human) review notes

UniProt: Q8WVX9 (FACR1_HUMAN). Gene FAR1 / MLSTD2 (Male sterility domain-containing protein 2).
HGNC:26222. 515 aa. EC 1.2.1.84.

## Core biology

FAR1 = fatty acyl-CoA reductase 1, a peroxisomal-membrane, NADPH-dependent reductase
that reduces long-chain (C16/C18) fatty acyl-CoA to the corresponding primary fatty
alcohol, releasing CoA. The reaction proceeds via a fatty aldehyde intermediate (two
NADPH-consuming reduction steps), and the overall reaction is:

> a long-chain fatty acyl-CoA + 2 NADPH + 2 H(+) = a long-chain primary fatty alcohol
> + 2 NADP(+) + CoA (EC 1.2.1.84, RHEA:52716)
[file:human/FAR1/FAR1-uniprot.txt "Reaction=a long-chain fatty acyl-CoA + 2 NADPH + 2 H(+) = a long-chain"]

Substrate preference: saturated/unsaturated C16 or C18 fatty acyl-CoA. From UniProt
FUNCTION: "Catalyzes the reduction of saturated and unsaturated C16 or C18 fatty
acyl-CoA to fatty alcohols" [file:human/FAR1/FAR1-uniprot.txt "Catalyzes the reduction of saturated and unsaturated C16 or"].
Confirmed enzymatically for palmitoyl-CoA (C16:0), stearoyl-CoA (C18:0), oleoyl-CoA
(C18:1), plus (in the mouse ortholog / PubMed:35238077) C20, iso-branched C18/C20, and
linoleoyl-CoA.

The abstract of PMID:15220348 (Cheng & Russell 2004): "Fatty acyl-CoA esters were the
substrate of FAR1, and the enzyme required NADPH as a cofactor. FAR1 preferred saturated
and unsaturated fatty acids of 16 or 18 carbons as substrates"
[PMID:15220348 "Fatty acyl-CoA esters were the substrate \nof FAR1, and the enzyme required NADPH as a cofactor. FAR1 preferred saturated \nand unsaturated fatty acids of 16 or 18 carbons as substrates"] and
"Confocal light microscopy \nindicated that FAR1 and FAR2 were localized in the peroxisome"
[PMID:15220348 "FAR1 and FAR2 were localized in the peroxisome"].

## Molecular function GO term choice

- GO:0102965 "alcohol-forming long-chain fatty acyl-CoA reductase activity": long-chain =
  aliphatic tail of 13-22 carbons (OLS). This exactly matches FAR1's C16/C18 (and up to
  C20) preference. This is the IDA-supported term in UniProtKB/GOA (PMID:15220348,
  20071337, 24108123). **This is the correct core MF.**
- GO:0080019 "alcohol-forming VERY long-chain fatty acyl-CoA reductase activity": very
  long-chain = >22 carbons. FAR1 prefers C16/C18, NOT VLCFA — so this IBA/IEA
  family-level term is a chain-length over-annotation (it reflects the wider FAR family,
  including plant FARs that act on VLCFA). Right reaction class, wrong chain-length
  specialization → MARK_AS_OVER_ANNOTATED (not removed; the essence — alcohol-forming
  acyl-CoA reductase — is correct).

## Biological process / pathway

FAR1 supplies the fatty alcohols consumed by AGPS (alkyl-DHAP synthase) to form the
ether bond in ether glycerophospholipids/plasmalogens; it is the rate-limiting enzyme.
- PMID:20071337 (Honsho 2010) abstract: "the enzyme fatty acyl-CoA reductase 1 (Far1)
  supplies the fatty alcohols used in the formation of ether-linked alkyl bonds"
  [PMID:20071337 "supplies the fatty alcohols used in the \nformation of ether-linked alkyl bonds"];
  feedback: "Far1 activity is elevated in \nplasmalogen-deficient cells" and
  "ether lipid biosynthesis in mammalian cells is regulated by a \nnegative feedback
  mechanism that senses cellular plasmalogen levels" [PMID:20071337 "negative feedback \nmechanism that senses cellular plasmalogen levels"].
- PMID:24108123 (Honsho 2013) abstract: "Expression of Far1 increased plasmalogen
  synthesis in wild-type \nChinese hamster ovary cells, strongly suggesting that Far1 is a
  rate-limiting \nenzyme for plasmalogen synthesis" [PMID:24108123 "Far1 is a rate-limiting \nenzyme for plasmalogen synthesis"].
- FAR1 product also feeds wax monoester synthesis (fatty alcohol + acyl-CoA -> wax ester,
  via AWAT1/2 in cytosol). UniProt: "In parallel, it is\nalso required for wax monoesters
  production" [file:human/FAR1/FAR1-uniprot.txt "also required for wax monoesters"].
  Reactome R-HSA-9640463 "Wax biosynthesis" and R-HSA-390425 "FAR1 reduces PalmCoA to
  HXOL" support this. Note: wax biosynthesis (GO:0010025) is largely inferred by
  similarity/ortholog transfer in human; sebaceous/preputial-gland wax role is the
  physiological context.

Process terms:
- GO:0008611 ether lipid biosynthetic process — IDA (24108123) + IMP (20071337). Core BP.
- GO:0046474 glycerophospholipid biosynthetic process — IDA (20071337). Ether
  glycerophospholipids (plasmalogens) are glycerophospholipids; correct but more general
  than 0008611; keep as non-core / accept as valid parent-level annotation.
- GO:0035336 long-chain fatty-acyl-CoA metabolic process — IDA (15220348) + IBA. FAR1
  consumes long-chain fatty acyl-CoA; correct, somewhat generic. Keep.
- GO:0010025 wax biosynthetic process — ISS/IEA/TAS. Correct by orthology + Reactome; wax
  is a real downstream use of the fatty-alcohol product; keep as non-core.
- GO:0008610 lipid biosynthetic process (IEA/ARBA) and GO:1901568 fatty acid derivative
  metabolic process (IEA/ARBA) — high-level generic parents; redundant with the specific
  terms. Over-annotated (generic).

## Cellular component

Peroxisome / peroxisomal membrane. FAR1 is a C-terminally tail-anchored, single-pass
peroxisomal membrane protein; PEX19 mediates targeting.
- UniProt SUBCELLULAR LOCATION: "Peroxisome membrane ...; Single-pass membrane protein"
  [file:human/FAR1/FAR1-uniprot.txt "Single-pass membrane protein"].
- PMID:24108123 abstract: "Far1 is shown to be \na peroxisomal tail-anchored protein"
  [PMID:24108123 "Far1 is shown to be \na peroxisomal tail-anchored protein"] and
  "The hydrophobic C terminus of Far1 binds to \nPex19p" [PMID:24108123 "The hydrophobic C terminus of Far1 binds to"].
- GO:0005778 peroxisomal membrane (IDA 24108123, HDA 21525035, IBA, IEA, TAS) and
  GO:0005777 peroxisome (IDA 20071337, HPA 0000052, IEA) — all correct, core CC.
- Note PMID:21525035 (HDA, peroxisomal membrane) is a proteomic co-purification of
  peroxisomal membrane protein complexes (PEX14 pulldown); FAR1 detected as a bona fide
  peroxisomal membrane protein. Consistent; accept.

## Protein binding (GO:0005515, IPI, PMID:32814053)

PMID:32814053 is a large-scale neurodegenerative-disease Y2H interactome
(Haenig 2020). GOA records three IPI interactions from IntAct (with KLF11/O14901,
BAG6-isoform/P46379-2, COL26A1-isoform/Q96A83-2). UniProt lists these same three
interactions (BAG6, COL26A1, KLF11; NbExp=3) [file:human/FAR1/FAR1-uniprot.txt
"Q8WVX9; O14901: KLF11; NbExp=3"]. These are high-throughput Y2H hits with no established
biological role for FAR1; bare "protein binding" is uninformative. Per policy: do not
REMOVE an IPI protein-binding annotation — MARK_AS_OVER_ANNOTATED.

The functionally meaningful interaction (PEX19, targeting receptor) is a distinct,
literature-curated interaction (PMID:24108123) and is captured in UniProt SUBUNIT, not in
this GO:0005515 IPI row.

## Disease

- PFCRD (peroxisomal fatty acyl-CoA reductase 1 disorder; MIM:616154) — autosomal
  recessive; biallelic LOF; severe ID, epilepsy, microcephaly, cataracts (PMID:25439727).
- CSPSD (cataracts, spastic paraparesis, speech delay; MIM:619338) — autosomal dominant;
  R480C/H/L gain-of-function variants escape plasmalogen feedback -> increased ether-lipid
  synthesis (PMID:33239752).

## Action summary rationale

- Core MF: GO:0102965 (long-chain, IDA) — ACCEPT.
- GO:0080019 (very-long-chain, IBA + 2x IEA) — MARK_AS_OVER_ANNOTATED (chain-length).
- Core CC: peroxisome / peroxisomal membrane — ACCEPT all (IDA/HDA/IBA + redundant IEA/TAS
  of the gene's own correct location are ACCEPTed per policy, not marked over-annotated).
- Core BP: GO:0008611 ether lipid biosynthetic process — ACCEPT (IDA + IMP).
- GO:0016620 (generic oxidoreductase MF, IEA) — the reaction is not aldehyde/oxo-donor
  driven at the physiological (acyl-CoA -> alcohol) level; it's a plausible parent but
  generic and slightly off; MARK_AS_OVER_ANNOTATED.
- GO:0016491 oxidoreductase activity (TAS Reactome) — correct but very generic parent;
  KEEP_AS_NON_CORE.
- Generic BP parents (GO:0008610, GO:1901568) — MARK_AS_OVER_ANNOTATED (uninformative).
- GO:0005515 protein binding (IPI) — MARK_AS_OVER_ANNOTATED (HT Y2H, uninformative).
