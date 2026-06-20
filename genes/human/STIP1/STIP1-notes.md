# STIP1 (HOP / p60 / Hsp70-Hsp90 organizing protein) — research notes

UniProt: P31948 (STIP1_HUMAN). Alt names: Hop, p60, NY-REN-11.

## Core identity
TPR-domain adaptor co-chaperone that simultaneously binds HSP70 (HSPA8/HSC70) and
HSP90, physically bridging the two chaperone systems to mediate client transfer from
HSP70 to HSP90. It has NO catalytic activity; it is a scaffold/adaptor. Avoid "protein
binding" as core; use Hsp70/Hsp90 binding.

- [file:human/STIP1/STIP1-uniprot.txt "FUNCTION: Acts as a co-chaperone for HSP90AA1 (PubMed:27353360). Mediates the association of the molecular chaperones HSPA8/HSC70 and HSP90"]
- [file:human/STIP1/STIP1-uniprot.txt "SUBUNIT: Probably forms a complex composed of chaperones HSP90 and HSP70, co-chaperones STIP1/HOP, CDC37, PPP5C, PTGES3/p23, TSC1 and client protein TSC2"]
- [file:human/STIP1/STIP1-uniprot.txt "DOMAIN: The TPR 1 repeat interacts with the C-terminal of HSC70. The TPR 4, 5 and 6 repeats (also called TPR2A domain) and TPR 7, 8 and 9 repeats (also called TPR2B domain) interact with HSP90."]
- [file:human/STIP1/STIP1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm. Nucleus. Dynein axonemal particle"]

## Mechanism
Classic HOP model: TPR1 binds HSC70 C-terminal EEVD; TPR2A binds HSP90 C-terminal MEEVD.
HOP holds HSP90 in an open conformation and recruits HSP70-bound client for handoff. It
is displaced later in the cycle by p23/PTGES3 and other co-chaperones.

## GO annotation review (goa.tsv)
Partner ID map: P08238=HSP90AB1; P07900=HSP90AA1; P04626=ERBB2; P00533=EGFR;
P53041=PPP5C (TPR co-chaperone); Q8IWD4=? small interactome; others mostly HT/unrelated.

- GO:0051879 Hsp90 protein binding (IBA, IPI PMID:29127155): CORE MF. ACCEPT.
- GO:0101031 protein folding chaperone complex part_of (IDA PMID:29127155): the HSP70-HSP90
  multichaperone machine; HOP is a defining component. ACCEPT.
- GO:0005737 cytoplasm (IEA, ISS): CORE localization. ACCEPT.
- GO:0005634 nucleus (IEA, ISS, TAS PMID:16130169, PMID:1569099): HOP shuttles to nucleus;
  documented. KEEP_AS_NON_CORE / ACCEPT (UniProt lists Nucleus).
- GO:0120293 dynein axonemal particle (IEA, ISS): by similarity to other species (cilia
  context); HOP/co-chaperones implicated in axonemal dynein assembly. KEEP_AS_NON_CORE.
- GO:0005829 cytosol (TAS Reactome x7): CORE cytosolic localization. ACCEPT (one representative)
  / KEEP_AS_NON_CORE for redundant pathway-context ones.
- GO:0005794 Golgi apparatus (TAS PMID:1569099): older localization; minor. KEEP_AS_NON_CORE.
- GO:0003723 RNA binding (HDA PMID:22658674): mRNA-interactome capture; no characterized RNA
  function. MARK_AS_OVER_ANNOTATED.
- GO:0032991 protein-containing complex part_of (IDA PMID:23349634): generic; HOP in a
  methyltransferase-substrate complex context. KEEP_AS_NON_CORE.
- GO:0005515 protein binding (many IPI): HSP90 partners (P08238/P07900) -> MODIFY to Hsp90
  protein binding; PPP5C/clients (EGFR, ERBB2) -> KEEP_AS_NON_CORE (real but generic);
  unrelated HT (p53, MYC, etc., PMID:32814053; PMID:35140242) -> MARK_AS_OVER_ANNOTATED.

## Core function synthesis
1. Hsp70-Hsp90 organizing protein: TPR adaptor binding both HSC70 and HSP90 (GO:0051879
   Hsp90 protein binding + Hsp70 binding GO:0030544), bridging client transfer.
2. Component of the HSP70-HSP90 multichaperone complex (GO:0101031).
3. Cytoplasmic (also nuclear); no catalytic activity.
