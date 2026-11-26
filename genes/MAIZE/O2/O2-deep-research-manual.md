# O2 (Opaque-2), Zea mays: manual literature research

No deep-research provider API was available in this session, so this file was
compiled by hand from cached publications (publications/PMID_*.md) and PubMed
searches. Quotations are verbatim from the cached abstracts or full text.

## Identity

- Reviewed entry: UniProtKB P12959 (OP2_MAIZE, "Regulatory protein opaque-2",
  453 aa, Swiss-Prot). MaizeGDB 24976.
- The batch task named the unreviewed TrEMBL entry B4FHZ3 (441 aa, "Opaque-2
  protein", B73 full-length cDNA BT036731), which carries GeneID 542375 and
  Gramene Zm00001eb301570. NCBI Gene 542375 ("opaque endosperm 2", aliases
  GRMZM2G015534, Zm00001d018971, o2) lists both P12959 (UniProtKB/Swiss-Prot) and
  B4FHZ3 as protein products, so the two accessions are the same gene. Length
  differences reflect allelic/cDNA variation (UniProt records conflicts
  E26 -> EPEPEPE and K231 -> KR between the genomic and cDNA clones of P12959).
- `just fetch-gene MAIZE O2` resolved P12959, and the GOA file is keyed to
  P12959 (7 rows). B4FHZ3 has its own GOA set of 10 rows, which includes three
  EnsemblPlants projections not on P12959: GO:0043565 sequence-specific DNA
  binding, GO:0045893 positive regulation of DNA-templated transcription and
  GO:0010581 regulation of starch biosynthetic process.

## Domain architecture

- bZIP domain 225-288 (PROSITE PS50217), basic motif 228-251, leucine zipper
  253-274; Pfam PF00170 bZIP_1 and PF12498 bZIP_C; CDD cd14702 bZIP_plant_GBF1;
  PANTHER PTHR46408:SF7 (REGULATORY PROTEIN OPAQUE-2), a group C plant bZIP
  family that also contains Arabidopsis bZIP9/10/25/63 and rice RISBZ1-like
  proteins.
- Hartings et al. 1989 [PMID:2479535 "The opaque 2 protein contains a domain
  similar to the leucine zipper motif identified in DNA binding proteins"].
- Two nuclear localization signals, one SV40-like (101-135) and one bipartite
  NLS inside the basic DNA-binding region (223-254) [PMID:1332794 "The second
  NLS was located in the basic, DNA binding domain (between residues 223 and
  254) and had a bipartite structure."].
- An N-terminal acidic activation domain is drawn in Zhang et al. 2012
  [PMID:22937104 "AD: acidic activation domain; bZIP: basic leucine zipper
  domain; NLS: nuclear localisation signals."].

## Molecular function: sequence-specific DNA-binding transcription activator

- Binding site in 22-kD zein promoters by DNase I footprinting, ACGT core;
  transactivation of an O2-site multimer in yeast [PMID:1392590 "we have
  identified the binding site for the O2 protein (O2) in the promoter of 22-kD
  zein genes"; "in yeast cells the O2 protein can activate expression of a lacZ
  gene containing a multimer of the O2 target sequence as part of its promoter,
  thus confirming its role as a transcriptional activator"]. Endosperm nuclear
  O2 recognises the site in gel shift assays with O2 antibodies.
- b-32 (albumin) promoter activated in vivo, five O2 sites; O2 binds and
  activates its own promoter [PMID:2001677 "the promoter of the b-32 gene is
  activated in vivo in the presence of the O2 gene product"; "The O2 protein is
  also shown to be capable of binding in vitro and activating in vivo, its own
  promoter."].
- An R->K substitution in the basic region (o2-676) abolishes specific binding
  and reduces zein, linking DNA binding to function in vivo [PMID:1899843 "the
  o2-676 mutant protein does not show specific recognition of zein promoter
  fragments"].
- Binds 22-kD zein promoters as a homodimer and heterodimerises with OHP1
  [PMID:8453304 "the O2 protein binds 22-kD zein gene promoters as a homodimer
  in vitro"; OHP1 "can bind the O2 target site both as a homodimer and in a
  heterodimeric complex with O2"].
- Genome-wide: ChIP-seq found 1686 binding sites over 1143 genes; TGACGTGG is
  the strongest motif; O2 directly regulates all zeins except 16- and 18-kD
  [PMID:25691733 "ChIP-Seq analysis detected 1686 O2 DNA binding sites
  distributed over 1143 genes."; "We confirmed that, except for the 16- and
  18-kD zeins, O2 directly regulates expression of all other zeins."].
- Transactivation of the 22-kD zein z1C promoter in onion epidermal cells, 3-4
  fold, repressed by ZmTaxilin [PMID:22937104 "YFP-O2 is able to induce
  transcription of the z1C promoter by 3–4 fold relative to the negative
  controls"].

## Interactors and regulation of O2 activity

- PBF (Dof zinc finger, P-box binding) interacts with O2 in vitro
  [PMID:9207153 "PBF interacts in vitro with the basic leucine zipper protein
  Opaque2"]. O2 and PBF additively transactivate starch-pathway promoters
  (PPDK1, PPDK2, SSIII) through adjacent P-box and O2 box [PMID:27621432 "we
  found a prolamine box and an O2 box that can be additively transactivated by
  PBF and O2"].
- OHP1 bZIP heterodimer partner [PMID:8453304].
- GCN5/ADA2 co-activators, diurnal phosphorylation control of DNA binding
  (cited in the PMID:22937104 introduction; primary papers not cached).
- ZmTaxilin interacts with O2 (Y2H, GST pull-down from 15 DAP kernels),
  retains YFP-O2 outside the nucleus and reduces its activity on the z1C
  promoter by 47% [PMID:22937104 "YFP-O2 was completely repressed to be
  transported into nucleus when YFP-O2 and CFP-Taxilin were co-expressed";
  "the transcriptional activity on z1C promoter was reduced by 47% when
  compared to YFP-O2 alone"].
- Upstream regulators: ZmABI19 binds and activates the O2 promoter
  [PMID:33751093]; ZmEREB167 represses O2 [PMID:39870138].

## Localization

- Nucleus in maize and tobacco cells; NLS-GUS fusions [PMID:1332794 "The maize
  regulatory protein Opaque-2 (O2) localizes to the nucleus in both maize and
  tobacco cells."].
- YFP-O2 alone in onion epidermis: "localised predominantly to the nucleus and
  the cytoplasm" [PMID:22937104].

## Biological roles

- Endosperm-specific; controls 22-kD zein accumulation (reduced to about 10%
  in o2) and also 27-kD zein, b-32 albumin, lysine-ketoglutarate
  reductase/saccharopine dehydrogenase, Ask1 and cyPPDK1 [PMID:22937104
  introduction].
- Starch: o2 reduces starch by about 11%, and O2 directly transactivates PPDK1,
  PPDK2 and SSIII promoters [PMID:27621432 "The starch content in the PbfRNAi
  and o2 mutants was reduced by ∼5% and 11%, respectively"].
- The o2 mutation raises lysine content of the kernel (quality protein maize);
  this is the basis of its agronomic importance but is a downstream effect of
  reduced zein (lysine-poor) synthesis.

## Gaps

- Primary papers on GCN5/ADA2 and on phosphorylation-dependent DNA binding were
  not cached; full texts of PMID:25691733 and PMID:27621432 were not available
  (abstract only).
