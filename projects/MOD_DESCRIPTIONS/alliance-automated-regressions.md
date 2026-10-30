---
title: "Alliance automated description regressions"
species: [worm]
autolink_exclude: [DPM1]
---

# Alliance automated descriptions that lost content

For these worm genes the current Alliance automated gene description (fetched 2026-10-29) is missing
function content that the RefSeq copy of an earlier Alliance release still carries. Texts are
quoted verbatim from `genes/worm/<gene>/<gene>-descriptions.yaml`. Found during the description
review in [MOD_DESCRIPTIONS](../MOD_DESCRIPTIONS.md). The RefSeq bracketed provenance line gives the release.

Check each case before filing it. The automated text is generated from GO annotations, so a
loss can follow an annotation that was deliberately withdrawn. For example, daf-15's
"regulation of autophagosome assembly" is no longer in GOA. A real regression is one where the
annotations are still present but the sentences are gone (ced-5, che-2: the current text has
expression and orthology only).

## ced-5 (WB:WBGene00000419)

- **Current Alliance automated:** Is expressed in body wall muscle cell; hermaphrodite somatic gonadal cell; and intestinal cell. Human ortholog(s) of this gene implicated in attention deficit hyperactivity disorder; immunodeficiency 40; and intellectual disability. Orthologous to several human genes including DOCK2 (dedicator of cytokinesis 2) and DOCK5 (dedicator of cytokinesis 5).
- **RefSeq (GeneID:177942):** Enables SH3 domain binding activity and enzyme binding activity. Involved in several processes, including engulfment of apoptotic cell; left/right axis specification; and positive regulation of distal tip cell migration. Part of guanyl-nucleotide exchange factor complex. Is active in presynapse. Is expressed in body wall muscle cell; hermaphrodite somatic gonadal cell; and intestinal cell. Human ortholog(s) of this gene implicated in attention deficit hyperactivity disorder and immunodeficiency 40. Orthologous to several human genes including DOCK2 (dedicator of cytokinesis 2) and DOCK5 (dedicator of cytokinesis 5). [provided by Alliance of Genome Resources, Jun 2026]

## che-2 (WB:WBGene00000484)

- **Current Alliance automated:** Is expressed in neurons. Human ortholog(s) of this gene implicated in asphyxiating thoracic dystrophy 2. Orthologous to human IFT80 (intraflagellar transport 80).
- **RefSeq (GeneID:180401):** Involved in several processes, including dauer larval development; negative regulation of transforming growth factor beta receptor signaling pathway; and positive regulation of locomotion involved in locomotory behavior. Located in ciliary basal body and non-motile cilium. Is expressed in neurons. Human ortholog(s) of this gene implicated in asphyxiating thoracic dystrophy 2. Orthologous to human IFT80 (intraflagellar transport 80). [provided by Alliance of Genome Resources, Jul 2025]

## daf-15 (WB:WBGene00000911)

- **Current Alliance automated:** Is expressed in several structures, including body wall musculature; excretory cell; hermaphrodite distal tip cell; intestine; and pharyngeal muscle cell. Human ortholog(s) of this gene implicated in nicotine dependence. Orthologous to human RPTOR (regulatory associated protein of MTOR complex 1).
- **RefSeq (GeneID:177770):** Predicted to enable protein kinase activator activity and protein-macromolecule adaptor activity. Involved in nematode larval development and regulation of autophagosome assembly. Part of TORC1 complex. Is expressed in several structures, including body wall musculature; excretory cell; hermaphrodite distal tip cell; intestine; and pharyngeal muscle cell. Human ortholog(s) of this gene implicated in nicotine dependence. Orthologous to human RPTOR (regulatory associated protein of MTOR complex 1). [provided by Alliance of Genome Resources, Jun 2026]

## dpm-1 (WB:WBGene00022044)

- **Current Alliance automated:** Predicted to enable dolichyl-phosphate beta-D-mannosyltransferase activity. Predicted to be involved in dolichol-linked oligosaccharide biosynthetic process. Predicted to be located in endoplasmic reticulum. Predicted to be active in endoplasmic reticulum membrane. Human ortholog(s) of this gene implicated in congenital disorder of glycosylation Ie. Orthologous to human DPM1 (dolichyl-phosphate mannosyltransferase subunit 1, catalytic).
- **RefSeq (GeneID:176874):** Predicted to enable dolichyl-phosphate beta-D-mannosyltransferase activity. Predicted to be involved in GPI anchor biosynthetic process; dolichol-linked oligosaccharide biosynthetic process; and protein O-linked glycosylation via mannose. Predicted to be located in endoplasmic reticulum. Predicted to be active in endoplasmic reticulum membrane. Human ortholog(s) of this gene implicated in congenital disorder of glycosylation Ie. Orthologous to human DPM1 (dolichyl-phosphate mannosyltransferase subunit 1, catalytic). [provided by Alliance of Genome Resources, Jun 2026]

## J7SF87 (WB:WBGene00021183)

- **Current Alliance automated:** Predicted to enable FAD binding activity and sulfide:quinone oxidoreductase activity. Predicted to be active in mitochondrion. Human ortholog(s) of this gene implicated in inherited metabolic disorder. Orthologous to human SQOR (sulfide quinone oxidoreductase).
- **RefSeq (GeneID:189421):** Predicted to enable FAD binding activity and sulfide:quinone oxidoreductase activity. Predicted to be involved in sulfide oxidation, using sulfide:quinone oxidoreductase. Predicted to be active in mitochondrion. Orthologous to human SQOR (sulfide quinone oxidoreductase). [provided by Alliance of Genome Resources, Jul 2025]

## nsy-1 (WB:WBGene00003822)

- **Current Alliance automated:** Enables mitogen-activated protein kinase kinase binding activity and protein kinase activity. Involved in several processes, including defense response to bacterium; determination of adult lifespan; and regulation of gene expression. Located in axon cytoplasm; perikaryon; and postsynaptic density. Is active in cytoplasm. Is expressed in several structures, including AWC; hypodermis; intestine; rectal gland cell; and tail. Used to study alcohol use disorder and amphetamine abuse. Human ortholog(s) of this gene implicated in Huntington's disease and arthritis. Orthologous to several human genes including MAP3K15 (mitogen-activated protein kinase kinase kinase 15) and MAP3K5 (mitogen-activated protein kinase kinase kinase 5).
- **RefSeq (GeneID:24104671):** Enables MAP kinase kinase kinase activity; mitogen-activated protein kinase kinase binding activity; and protein serine/threonine/tyrosine kinase activity. Involved in several processes, including defense response to bacterium; determination of adult lifespan; and regulation of gene expression. Located in axon cytoplasm; neuronal cell body; and postsynaptic density. Is active in cytoplasm. Is expressed in several structures, including AWC; hypodermis; intestine; rectal gland cell; and tail. Used to study alcohol use disorder and amphetamine abuse. Human ortholog(s) of this gene implicated in Huntington's disease. Orthologous to several human genes including MAP3K15 (mitogen-activated protein kinase kinase kinase 15) and MAP3K5 (mitogen-activated protein kinase kinase kinase 5). [provided by Alliance of Genome Resources, Jun 2026]

## nud-1 (WB:WBGene00003829)

- **Current Alliance automated:** Is expressed in gonad; hypodermis; intestine; and neurons. Used to study epilepsy and lissencephaly. Orthologous to human NUDC (nuclear distribution C, dynein complex regulator).
- **RefSeq (GeneID:176754):** Enables protein folding chaperone and unfolded protein binding activity. Involved in several processes, including GABAergic synaptic transmission; pronuclear migration; and vulval development. Predicted to be located in synapse. Predicted to be active in cytoplasm. Is expressed in gonad; hypodermis; intestine; and neurons. Used to study epilepsy and lissencephaly. Orthologous to human NUDC (nuclear distribution C, dynein complex regulator). [provided by Alliance of Genome Resources, Jun 2026]

## ppgn-1 (WB:WBGene00021425)

- **Current Alliance automated:** Human ortholog(s) of this gene implicated in hereditary spastic paraplegia 7. Orthologous to human SPG7 (SPG7 matrix AAA peptidase subunit, paraplegin).
- **RefSeq (GeneID:177021):** Predicted to enable metalloendopeptidase activity. Predicted to be involved in mitochondrial protein processing. Predicted to be located in membrane and mitochondrion. Predicted to be part of m-AAA complex. Human ortholog(s) of this gene implicated in hereditary spastic paraplegia 7. Orthologous to human SPG7 (SPG7 matrix AAA peptidase subunit, paraplegin). [provided by Alliance of Genome Resources, Jun 2026]

## wago-1 (WB:WBGene00011061)

- **Current Alliance automated:** Predicted to enable RNA endonuclease activity; miRNA binding activity; and single-stranded RNA binding activity. Predicted to be involved in regulatory ncRNA-mediated post-transcriptional gene silencing. Located in P granule. Is expressed in germ line and in male.
- **RefSeq (GeneID:172463):** Enables DEAD/H-box RNA helicase binding activity. Predicted to be involved in regulatory ncRNA-mediated post-transcriptional gene silencing. Located in P granule. Is expressed in germ line and in male. [provided by Alliance of Genome Resources, Jul 2025]
