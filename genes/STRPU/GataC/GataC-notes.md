# GataC (SpGATAc / Sp-GataC / gatac; UniProt O77156) - curation notes

## Identity of the UniProt entry

- O77156 (`O77156_STRPU`, unreviewed/TrEMBL, 431 aa) is the S. purpuratus "GATA
  transcription factor" cDNA AF077674 (EMBL AAC62960.1) deposited by the Davidson
  lab from a coelomocyte cDNA screen. Its single RX line is Pancer, Rast & Davidson
  1999 (PMID:10398804), which reports the gene as "a GATA-2/3 homologue (SpGATAc)"
  [PMID:10398804 "Three coelomocyte genes reported here encode transcription
  factors. These are an NFKB homologue (SpNFKB); a GATA-2/3 homologue (SpGATAc);
  and a runt domain factor (SpRunt-1)."]. The NCBI Gene record linked from the
  entry (KEGG spu:373316, NCBI Gene 373316) is named `GATAc` / "GATA
  transcription factor".
- Class assignment: the InterPro hits are IPR016374 "TF_GATA-2/3" and the FunFams
  are GATA-2 / GATA-3, i.e. the GATA1/2/3 (class I) family, and Poustka et al.
  2007 explicitly list "SpGataE and SpGataC (orthologs of Gata4/Gata5/Gata6 and
  Gata1/Gata2/Gata3, respectively)" [PMID:17506889]. Solek et al. 2013 call it
  "SpGatac, an ortholog of vertebrate Gata-1/2/3" [PMID:23792116]. The other sea
  urchin GATA gene, gatae (Q64HK6, GATA4/5/6 class, endomesoderm GRN), is a
  separate accession reviewed in `genes/STRPU/GataE/`.
- Confidence that O77156 is the GRN gene gatac: HIGH. The accession is the
  originally cloned SpGATAc cDNA, the NCBI gene name is GATAc, the domain/family
  assignments are GATA1/2/3-class, and the GRN literature (Materna & Davidson
  2012; Materna et al. 2013; Solek et al. 2013) uses gataC/SpGatac for the
  GATA1/2/3 ortholog. No second GATA1/2/3-class gene is described in the genome.
- Domain architecture (UniProt FT): two GATA-type zinc fingers (221-245 and
  274-298; PROSITE PS50114 domains 215-269 and 268-321), disordered regions at
  43-84 and 199-218. Two-finger architecture typical of vertebrate GATA1/2/3.
- PANTHER PTHR10071 "TRANSCRIPTION FACTOR GATA FAMILY MEMBER", subfamily
  PTHR10071:SF281 "BOX A-BINDING FACTOR-RELATED" (labels copied from
  `interpro/panther/panther.obo`, not from memory; the subfamily name is
  dominated by a different member and is not a description of GataC). O77156 is
  not in `interpro/panther/panther-members.tsv`.

## Embryonic expression: oral non-skeletogenic mesoderm (NSM)

- gataC is one of the first two transcription factor genes specific to the oral
  NSM, switched on at 17-18 hpf: [PMID:23261933 "The first transcription factor
  genes specific to the oral NSM, prox1 and gataC, are transcriptionally
  activated in this region between 17 and 18 hpf (Fig. 1B,T), which is
  significantly later than the onset of Nodal transcription at about 8-9 hpf"]
  and [PMID:23261933 "gataC, as seen in Fig. 1B, only begins to be transcribed
  significantly at about 17 hpf similar to prox1; both genes have almost
  identical activation kinetics between 18 and 24 hpf (Fig. 1B)."].
- Oral-mesoderm specificity was first noted in genome-wide expression surveys:
  [PMID:22306924 "The prox1, gataC, and ese genes are of particular interest
  because they are specifically expressed in the oral mesoderm (Fig. 6) (Poustka
  et al., 2007; Rizzo et al., 2006)."]
- The oral NSM is the blastocoelar cell (larval immunocyte) lineage:
  [PMID:23261933 "About one-third of the NSM cells, located in a V-shaped sector
  directly beneath the oral ectoderm, give rise upon gastrulation to a particular
  mesenchymal cell type known as blastocoelar cells (Ruffins and Ettensohn,
  1996)."] and [PMID:23261933 "However, the blastocoelar cell regulatory state
  originates prior to gastrulation when oral NSM cells commence to express
  exclusively specific transcription factors."]

## Inputs into gataC (upstream circuitry)

- Delta/Notch: in the regulome-wide D/N perturbation, gataC is among the NSM
  genes lost by 18 hpf: [PMID:22306924 "These genes encode the transcription
  factors Prox1, GataC, and Ese and are activated at around 16 hpf (Materna et
  al., 2010)."]; [PMID:22306924 "By the time the expression of Delta in the
  skeletogenic cell lineage terminates, only gcm, gataE, prox1, ese, and gataC
  have been activated in the NSM (Fig. 9)."]. Whether the D/N input is direct
  is not known: [PMID:22306924 "One or more of prox1, ese, and gataC could
  potentially be directly activated by D/N signaling as well."]
- Aboral repression by Gcm/GataE: [PMID:23261933 "If gcm or gataE expression are
  blocked by treatment with MASOs we see an expansion of ese, prox1, gataC, and
  erg expression (the same is seen for shr2 expression; not shown)."]. Solek et
  al. 2013 took this to cis-regulatory resolution: [PMID:23792116 "Regulatory
  analysis of SpGatac indicates that oral NSM identity is directly suppressed in
  presumptive pigment cells by the transcription factor SpGcm."] (abstract only
  cached; the reporter constructs and Gcm-site details are in the full text,
  which is not available here).

## Outputs: what GataC itself does

- Pre-gastrular GRN: GataC has no measurable output on the regulatory genes of
  the pre-gastrular NSM: [PMID:23261933 "GataC MASO treatment does not affect any
  regulatory genes pre-gastrulation (Supp. Fig. 4; Solek and Rast, personal
  communication)"]. So in the pre-gastrular GRN gataC is a marker/output node of
  the oral NSM regulatory state rather than a driver of it.
- Blastocoelar cell (immunocyte) development: the functional paper is Solek et
  al. 2013 (abstract only cached): [PMID:23792116 "Perturbation of SpGatac
  affects blastocoelar cell migration at gastrulation and later expression of
  immune effector genes, whereas interference with SpScl function disrupts
  segregation of pigment and blastocoelar cell precursors."]. The abstract does
  not give the direction of the effector-gene changes or the gene identities.
- Co-expressed hematopoietic-type cofactors: [PMID:23792116 "Homologs of several
  transcription regulators that interact with Gata-1/2/3 and Scl factors in
  vertebrate hematopoiesis are also co-expressed in the oral NSM, including
  SpE-protein, the sea urchin homolog of vertebrate E2A/HEB/E2-2 and SpLmo2, an
  ortholog of a dedicated cofactor of the Scl-GATA transcription complex."].
  The Davidson lab makes the same comparison: [PMID:23261933 "Thus for example
  gataC, scl, and lmo2 form a complex that regulates hematopoietic genes
  (Lecuyer and Hoang, 2004; Matthews and Visvader, 2003)"].

## Adult expression: coelomocytes

- [PMID:10398804 "The immune effector cells of sea urchins are the coelomocytes,
  whose primary function is protection against invasive marine pathogens; here
  we identify six genes expressed in coelomocytes, homologues of which are also
  expressed in cells of the mammalian immune system."]
- Response to bacterial challenge (down, not up): [PMID:10398804 "All three of
  these coelomocyte genes respond sharply to bacterial challenge: SpNFKB and
  SpRunt-1 genes are rapidly up-regulated, while transcripts of SpGATAc factor
  disappear within hours of injection of bacteria."] and [PMID:10398804 "Sham
  injection also activates SpNFKB and SpRunt, though with slower kinetics, but
  does not affect SpGATAc levels."]

## GO curation decisions

- No direct DNA-binding assay (EMSA/ChIP) or reporter assay of a GataC-dependent
  target module is cached for this gene, so the MF is kept at the electronic
  GO:0000981 level (ACCEPT) with the literature merged into the row; no
  activator/repressor child and no cis-regulatory-region binding term proposed.
- Only one NEW BP: GO:0002520 immune system development (IMP, PMID:23792116),
  because SpGatac knockdown alters blastocoelar cell (larval immunocyte)
  migration and immune effector gene expression, and the gene is expressed in
  adult coelomocytes. Comparator check (QuickGO): human GATA3 (P23771) carries
  GO:0002520 (IBA) and GATA1 (P15976) carries hemopoiesis descendants
  (erythrocyte/megakaryocyte differentiation, IMP), so lineage-development terms
  are the convention for this class.
- Not proposed: mesodermal cell fate specification (GataC does not affect any
  regulatory gene pre-gastrulation, so it does not perform the specification
  step; the specification is done by Delta/Notch, Gcm/GataE, Nodal-downstream
  inputs), regulation of cell migration (a transcription factor is not the
  migration machinery; the migration defect is a downstream consequence),
  positive/negative regulation of transcription (sign not given in the cached
  abstract).
