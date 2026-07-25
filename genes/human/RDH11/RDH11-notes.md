# RDH11 (Retinol dehydrogenase 11) — review notes

UniProt: Q8TC12 (RDH11_HUMAN). Synonyms: ARSDR1, PSDR1, SDR7C1; RalR1; PSDR1;
"HCV core-binding protein HCBP12"; "Short chain dehydrogenase/reductase family 7C member 1".
HGNC:17964. 318 aa. Chromosome 14.

## Core biology (grounded in the local UniProt record)

RDH11 is a microsomal, membrane-bound **NADPH-dependent retinaldehyde reductase /
retinol dehydrogenase** of the short-chain dehydrogenase/reductase (SDR) family
(subfamily SDR7C, alongside its paralog RDH12).

- Enzyme classification EC=1.1.1.300; catalyzes all-trans-retinol + NADP(+) =
  all-trans-retinal + NADPH + H(+) (Rhea:RHEA:25033), plus the 11-cis (RHEA:54912),
  9-cis (RHEA:54916) and 13-cis (RHEA:54920) reactions
  [file:human/RDH11/RDH11-uniprot.txt "EC=1.1.1.300"].
- Function: "Retinol dehydrogenase with a clear preference for NADP. Displays high
  activity towards 9-cis, 11-cis and all-trans-retinol, and to a lesser extent on
  13-cis-retinol" [file:human/RDH11/RDH11-uniprot.txt "Retinol dehydrogenase with a
  clear preference for NADP."].
- The physiologically dominant direction is **reduction** of retinaldehyde to retinol:
  the enzyme is "approximately 50-fold more efficient for the reduction of
  all-trans-retinal than for the oxidation of all-trans-retinol"
  [PMID:12036956 "The enzyme is approximately 50-fold more efficient for the reduction of all-trans-retinal than for the oxidation of all-trans-retinol."]. Kinetics favor NADP(H): "with at
  least an 800-fold lower apparent K(m) values for NADP+ and NADPH versus NAD+ and NADH
  as cofactors" [PMID:12036956 "with at least an 800-fold lower apparent K(m) values for NADP+ and NADPH versus NAD+ and NADH"].
- No steroid dehydrogenase activity: "Has no dehydrogenase activity towards steroid"
  [file:human/RDH11/RDH11-uniprot.txt "Has no dehydrogenase"].
- NADP binding site: BINDING 48..54 /ligand="NADP(+)"; catalytic proton acceptor
  ACT_SITE 202 [file:human/RDH11/RDH11-uniprot.txt].

## Substrate specificity / dual specificity

RDH11 belongs to a novel subfamily of four retinol dehydrogenases (RDH11-14) that
"display dual-substrate specificity, uniquely metabolizing all-trans- and cis-retinols
with C(15) pro-R specificity" [PMID:12226107 "display \ndual-substrate specificity, uniquely metabolizing all-trans- and cis-retinols \nwith C(15) pro-R specificity."]. The paper positions RDH11 in the RPE:
"RDH11-14 fill the \ngap in our understanding of 11-cis-retinal and all-trans-retinal transformations \nin photoreceptor (RDH12) and retinal pigment epithelial cells (RDH11)"
[PMID:12226107].

## Aldehyde detoxification / mouse ortholog (SCALD)

PMID:12807874 characterizes the **mouse** ortholog SCALD (short-chain aldehyde
reductase): "SCALD appears to be the mouse ortholog of the human protein that has been
designated variously as prostate short-chain dehydrogenase/reductase 1, retinal
reductase 1, and retinol dehydrogenase 11" [PMID:12807874 "SCALD appears to be the mouse ortholog of the human protein that has been \ndesignated variously as prostate short-chain \ndehydrogenase/reductase 1, retinal reductase 1, and retinol dehydrogenase 11."]. Mouse SCALD reduces
short-chain aldehydes "including nonanal and 4-hydroxy-2-nonenal" and also retinaldehydes
[PMID:12807874 "The enzyme specifically uses NADPH to reduce a variety of short-chain aldehydes, \nincluding nonanal and 4-hydroxy-2-nonenal."]. IMPORTANT species caveat: **human** RDH11
is much weaker on these toxic aldehydes than mouse — UniProt CAUTION: "In contrast to
mouse, human RDH11 exhibits little or no activity towards toxic lipid peroxidation
products, such as nonanal or 4-hydroxy-nonenal"
[file:human/RDH11/RDH11-uniprot.txt "In contrast to"]. So the "cellular detoxification of
aldehyde" (GO:0110095) and generic "aldehyde dehydrogenase (NADP+)" annotations
originate from the mouse ortholog and are, at best, weakly supported for the human gene.
Note that GO:0033721 aldehyde dehydrogenase (NADP+) activity is defined as aldehyde ->
acid (oxidation to carboxylic acid), which is NOT the reductase (aldehyde -> alcohol)
chemistry RDH11 performs — this IEA (Ensembl transfer from mouse Q9QYF1) is a
wrong-reaction over-annotation.

## Localization

Endoplasmic reticulum membrane; single-pass type II membrane protein (N-terminal
signal-anchor TM 1..21, cytoplasmic catalytic domain 22..318)
[file:human/RDH11/RDH11-uniprot.txt "Endoplasmic reticulum membrane"]. Localization to
the ER shown experimentally [PMID:12036956 "localizes to the endoplasmic reticulum."].
IEA (Ensembl) also assigns photoreceptor inner segment (GO:0001917) — from the mouse
ortholog; consistent with retinal expression but not experimentally shown for the human
protein in the cached literature.

## SELENOF interaction (regulation)

Selenoprotein F (SELENOF, Sep15) physically interacts with RDH11 (Y2H, FRET, co-IP,
pull-down) and inhibits its retinaldehyde-reductase activity:
"SELENOF interacts with RDH11 and blocks its enzyme activity to \nreduce all-trans-retinaldehyde"
[PMID:29410696 "SELENOF interacts with RDH11 and blocks its enzyme activity to \nreduce all-trans-retinaldehyde."]. The paper restates RDH11 function:
"RDH11 is an enzyme for the reduction of all-trans-retinaldehyde to \nall-trans-retinol (vitamin A)"
[PMID:29410696 "RDH11 is an enzyme for the reduction of all-trans-retinaldehyde to \nall-trans-retinol (vitamin A)."]. GOA records two IPI "protein binding" annotations from
this paper axis (SELENOF O60613) and the BioPlex AP-MS studies (UBAC1 Q9BSL1).

## Disease

Biallelic RDH11 nonsense mutations cause "Retinal dystrophy, juvenile cataracts, and
short stature syndrome (RDJCSS)" [MIM:616108]
[file:human/RDH11/RDH11-uniprot.txt "Retinal dystrophy, juvenile cataracts, and"];
originally reported by PMID:24916380 (a new syndrome with retinitis pigmentosa caused by
nonsense mutations in RDH11).

## Interaction papers (bare "protein binding" IPI)

- PMID:28514442 (BioPlex 2.0) and PMID:33961781 (BioPlex 3.0): proteome-scale AP-MS
  interactome studies; RDH11 is one bait/prey among thousands. WITH/FROM UniProtKB:Q9BSL1
  (UBAC1). These are generic high-throughput "protein binding" (GO:0005515) IPI — keep as
  non-core / over-annotated, not removable (IPI).
- PMID:29410696: targeted SELENOF interaction (WITH/FROM O60613). Biologically meaningful
  (regulatory), but the GO annotation itself is bare GO:0005515.

## Paralog note (ISS provenance)

The ISS annotations (GO_REF:0000024) carry WITH/FROM UniProtKB:Q96NR8 = **human RDH12**,
the closest SDR7C paralog. The NAD+ term (GO:0004745) transferred this way is dubious for
RDH11, which strongly prefers NADP (see 800-fold Km difference above). NADP-dependent
terms are the well-supported ones.

## Provenance status of cited pubs

- PMID:12036956, PMID:12226107, PMID:12807874: abstract-only in cache
  (full_text_available: false) but authoritative experimental papers; UniProt cites them
  for CATALYTIC ACTIVITY / FUNCTION / SUBCELLULAR LOCATION.
- PMID:28514442, PMID:29410696, PMID:33961781: full text available.
