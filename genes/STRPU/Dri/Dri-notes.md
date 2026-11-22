# Dri (Strongylocentrotus purpuratus, UniProt Q8MQH7) - curation notes

## Identity

- UniProt Q8MQH7 (`DRI_STRPU`, Swiss-Prot reviewed, 490 aa, EMBL AY130972 /
  AAM81746) is Spdeadringer (Spdri), deposited by the Davidson lab; its single RX
  line is PMID:12941621 (Amore et al. 2003), the paper that cloned and named the
  gene. The community symbol in the GRN literature is `dri` / `Spdri`; here the
  folder alias is `Dri`.
- Domain architecture (UniProt FT): ARID DNA-binding domain at 202-294 (PROSITE
  PS51011) and a C-terminal REKLES domain at 389-479 (PS51486), the two-domain
  architecture diagnostic of the ARID3 / Dead ringer / Bright subfamily (InterPro
  IPR045147 "ARI3A/B/C"). PANTHER PTHR15348:SF0 (label not written from memory).
  No identity doubt: the accession, the RX paper and the GRN gene are the same
  entity.

## What the gene is

- [PMID:12941621 "The Spdeadringer (Spdri) gene encodes an ARID-class
  transcription factor not previously known in sea urchin embryos."]
- [PMID:12941621 "We show that Spdri is a key player in two separate
  developmental gene regulatory networks (GRNs)."]

## Expression (biphasic)

- [PMID:12941621 "Spdri is expressed in a biphasic manner, first, after 12 h and
  until ingression in the skeletogenic descendants of the large micromeres;
  second, after about 20 h in the oral ectoderm, where its transcripts remain
  present at 30-50 mRNA molecules/cell far into development."]
- Timing matters for the choice of GO terms: [PMID:12941621 "In both
  territories, the periods of Spdri expression follow prior territorial
  specification events."] Dri is therefore not a specification gene in either
  territory; it is deployed after the skeletogenic and oral-ectoderm regulatory
  states are already installed, and acts to drive differentiation-gene
  batteries (PMCs) or to maintain/elaborate the oral regulatory state.
- UniProt DEVELOPMENTAL STAGE (from the same paper): later expression in apical
  plate and ciliary band of the post-gastrular embryo.

## Place in the skeletogenic (PMC) GRN

- Inputs: dri is downstream of the double-negative-gate regulators. In the
  Oliveri/Tu/Davidson 2008 synthesis: [PMID:18413610 "The tbr and alx1 genes
  also provide inputs into the additional skeletogenic differentiation genes
  dri and foxb."] Cis-regulatory dissection of the spdri locus confirms the
  inputs: [PMID:18718463 "the reporter responded to known spdri's
  transcriptional regulators (Ets1, Alx1, Gsc and Dri)."]
- Outputs: Dri, with Ets1, is a driver of the terminal skeletogenic
  differentiation gene battery. [PMID:12941621 "Spdri is shown to act in the
  micromere descendants in the pathways that result in the expression of
  batteries of terminal skeletogenic genes."] [PMID:18413610 "these
  differentiation genes require as drivers products of all of the now familiar
  components of the skeletogenic regulatory state ( alx1 , ets1 , tbr , tel ,
  erg , hex , foxb , dri )"]
- Direct, positive cis-regulatory input (the key MF evidence): on the Sp-cyp1
  (cyclophilin) 218-bp module, [PMID:16574094 "elimination of either Ets1 or Dri
  inputs severely depresses the activity of expression constructs containing
  this DNA fragment; and that Ets1 and Dri target sites within the 218 bp
  fragment are required for normal expression. This indicates that the
  predicted inputs are direct."] The authors generalise: [PMID:16574094 "these
  genes probably constitute a skeletogenic gene battery, defined by its Ets
  plus Dri regulatory inputs."]
- Loss of function: [PMID:12941621 "morphological consequences of alphaSpdri
  MASO treatment include failure of spiculogenesis and of correct primary
  mesenchyme cell (pmc) patterning in the postgastrular embryo, and also
  failure of gastrulation."] Micromere-transplant chimeras separate the
  autonomous from the non-autonomous requirement: [PMID:12941621 "while Spdri
  expression is required autonomously for expression of skeletogenic genes
  prior to ingression, complete skeletogenesis also requires the expression of
  oral ectoderm patterning information."]

## Place in the oral ectoderm GRN

- [PMID:12941621 "But, in the oral ectoderm, the same gene participates in the
  central GRN controlling oral ectoderm identity."]
- Knockdown converts the whole ectoderm to aboral character: [PMID:12941621
  "If its expression is blocked by treatment with alphaSpdri MASO,
  oral-specific features disappear and expression of the aboral ectoderm marker
  spec1 encompasses the whole of the ectoderm."] Su et al. 2009 cite this as one
  of the perturbations showing the oral GRN controls the aboral repressor:
  [PMID:19268450 "treatments which interfere with the operation of the GRN,
  such as knock-down of dri (Amore et al., 2003), of hnf6 (Otim et al., 2004),
  or of gsc (Angerer et al., 2001), all cause expression of spec1 to spread
  around the whole ectoderm."]
- Position in the Su 2009 oral ectoderm GRN: dri belongs to the set released by
  the Gsc "repressor A" gate (the oral-ectoderm analogue of the HesC gate):
  [PMID:19268450 "The definitive set of early regulatory genes in the oral
  ectoderm, including dri, bra,, and hes all are under repressor A control, as
  evinced by their sharp decrease in expression when gsc mRNA translation is
  prevented by MASO treatment."] Its later domain is the oral "face":
  [PMID:19268450 "There remains the main cuboidal epithelium of the oral
  ectoderm “face” which continues to express the gsc, dri, and hes genes."]
- Cis-regulation (Mahmud & Amore 2008): a 4.7 kb fragment (-3456;+389) with a
  GFP reporter reproduces both expression phases, and [PMID:18718463 "Both in
  the PMCs' and Oral Ectoderm's expression phases, activation of spdri is
  obtained through the integration of three kinds of inputs: positive and
  globally distributed ones; negative ones (that prevent ectopic expression);
  positive and tissue-specific ones."] The reporter responds to Dri itself,
  implying autoregulation.

## Pleiotropic / indirect effects (not annotated)

- Gastrulation failure after dri MASO is indirect: [PMID:12941621 "Failure of
  gastrulation is not due to indirect interference with endomesodermal
  specification per se, since all endomesodermal genes tested function normally
  in alphaSpdri MASO embryos."] It is attributed partly to a late micromere
  signalling function needed to clear SoxB1 from the prospective endoderm and
  partly to a non-autonomous oral ectoderm effect. Not a Dri participation in
  gastrulation; no BP term proposed.

## GOA audit (all electronic)

- Six rows, three IBA (PAINT, PTN000394188) and three IEA (InterPro ARID
  domain; ARBA/UniProt subcellular). DNA binding, nucleus and regulation of
  transcription by RNA polymerase II are all correct for an ARID-class TF; DNA
  binding is under-specific and the literature supports the RNA polymerase II
  cis-regulatory-region sequence-specific child. No GO-CAM contains Q8MQH7
  (gocams/index.tsv).

## Decisions

- NEW GO:0001228 (IDA, PMID:16574094): direct positive cis-regulatory input on
  Sp-cyp1 is shown by site mutation and reporter loss.
- NEW GO:0045944 (IMP, PMID:12941621; IDA, PMID:16574094).
- NEW GO:0070169 positive regulation of biomineral tissue development (IMP,
  PMID:12941621): autonomous requirement for skeletogenic gene expression and
  failure of spiculogenesis; matches the convention used for Alx1 and Ets1.
- NEW GO:0001715 ectodermal cell fate specification (IMP, PMID:12941621) for
  the oral-ectoderm role: Dri is part of the GRN that establishes/maintains
  oral (vs aboral) ectodermal identity; the project convention (Otx, Eve,
  SoxB1) uses this term for sub-ectodermal regional fates. GO:0060834
  oral/aboral axis specification exists but carries no annotations in QuickGO,
  so it is raised as a question rather than asserted.
- Not proposed: mesodermal cell fate specification (Dri follows specification),
  gastrulation (indirect), EMT (dri is needed until ingression but no ingression
  defect is described as Dri-autonomous).
