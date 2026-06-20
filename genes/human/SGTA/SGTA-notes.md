# SGTA (small glutamine-rich TPR-containing protein alpha / SGT / alphaSGT) — notes

UniProt: O43765 (SGTA_HUMAN). SGT family. Homodimer.

## Core identity
Cytosolic TPR-domain co-chaperone central to tail-anchored (TA) membrane protein
biogenesis and cytosolic quality control of hydrophobic/mislocalized substrates. It
binds HSC70/HSP70 and HSP90 via its TPR repeats and regulates their ATPase activity;
it acts upstream of / together with the BAG6 complex and the ASNA1/TRC40 (GET) pathway
to deliver TA proteins to the ER, and it antagonizes BAG6-mediated ubiquitination/triage
to the proteasome (a maturation-vs-degradation rheostat).

- [file:human/SGTA/SGTA-uniprot.txt "FUNCTION: Co-chaperone that binds misfolded and hydrophobic patches-containing client proteins in the cytosol. Mediates their targeting to the endoplasmic reticulum but also regulates their sorting to the proteasome when targeting fails"]
- [file:human/SGTA/SGTA-uniprot.txt "Functions upstream of the BAG6 complex and ASNA1, binding more rapidly the transmembrane domain of newly synthesized proteins"]
- [file:human/SGTA/SGTA-uniprot.txt "collaborates with the BAG6 complex to maintain hydrophobic substrates in non-ubiquitinated states"]
- [file:human/SGTA/SGTA-uniprot.txt "Competes with RNF126 for interaction with BAG6, preventing the ubiquitination of client proteins associated with the BAG6 complex"]
- [file:human/SGTA/SGTA-uniprot.txt "Binds directly to HSC70 and HSP70 and regulates their ATPase activity"]
- [file:human/SGTA/SGTA-uniprot.txt "SUBUNIT: Homodimer. ... Interacts (via TPR repeats) with HSP90AA1. ... Interacts (via TPR repeats) with HSPA8/Hsc70; the interaction is direct. Interacts with BAG6 (via ubiquitin-like domain)"]
- [file:human/SGTA/SGTA-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm. Nucleus."]
- [file:human/SGTA/SGTA-uniprot.txt "SIMILARITY: Belongs to the SGT family."]

## BAG6 antagonism (PMID:23129660, Leznicki & High 2012)
- [PMID:23129660 "SGTA actively promotes the deubiquitination of mislocalized proteins that are already covalently modified, thus reversing the actions of BAG6 and inhibiting its capacity to promote substrate-specific degradation."]

## GO annotation review (goa.tsv)
Partner map: P07900=HSP90AA1; P08238=HSP90AB1; O95816=BAG6; P46379=BAG6; P11441=UBL4A
(BAG6/GET-pathway component); O43765=SGTA self (homodimer); rest HT/unrelated.

- GO:0060090 molecular adaptor activity (IBA): CORE MF. SGTA is an adaptor delivering
  clients. ACCEPT.
- GO:0006620 post-translational protein targeting to ER membrane (IBA): CORE process. ACCEPT.
- GO:0071816 tail-anchored membrane protein insertion into ER membrane (IDA PMID:25535373):
  precise CORE process. ACCEPT.
- GO:0072380 TRC complex part_of (IBA): SGTA associates with the TRC/GET targeting module
  (ASNA1/BAG6). ACCEPT / KEEP_AS_NON_CORE (it acts with but is sometimes drawn as separate
  from the core TRC40 complex). ACCEPT.
- GO:1904288 BAT3/BAG6 complex binding (IPI PMID:23246001): CORE MF interaction. ACCEPT.
- ERAD-related: GO:0036503 ERAD pathway (IDA), GO:1904293 neg reg ERAD (IDA), GO:1904294
  pos reg ERAD (IMP), GO:2000059 neg reg ub-dependent catabolism (IDA), GO:2000060 pos reg
  ub-dependent catabolism (IMP): SGTA modulates triage of mislocalized/ERAD substrates;
  both pos and neg regulation reported (context-dependent rheostat). ACCEPT/KEEP_AS_NON_CORE.
- GO:0016020 membrane (IBA/IEA/IDA): SGTA is cytosolic but transiently membrane-associated
  during TA delivery. KEEP_AS_NON_CORE.
- GO:0005737 cytoplasm / GO:0005829 cytosol (IEA/IDA/TAS): CORE localization. ACCEPT.
- GO:0005634 nucleus (IEA/IDA PMID:16580629) / GO:0005654 nucleoplasm (IDA): nuclear
  accumulation during apoptosis; documented but secondary. KEEP_AS_NON_CORE.
- GO:0042802 identical protein binding (IEA, IPI x2): SGTA homodimer. ACCEPT (real, specific).
- GO:0005515 protein binding (many IPI): HSP90 (P07900/P08238) -> MODIFY to Hsp90 protein
  binding; BAG6 (O95816/P46379)/UBL4A(P11441) -> meaningful but bare term; KEEP_AS_NON_CORE
  (BAG6 binding has its own term GO:1904288 already annotated); HT-unrelated -> KEEP_AS_NON_CORE.

## Core function synthesis
1. Molecular adaptor / co-chaperone (GO:0060090) binding HSC70/HSP70/HSP90 (TPR) and
   hydrophobic clients; regulates HSP70 ATPase.
2. TA membrane protein targeting to ER (GO:0006620 / GO:0071816) via BAG6/TRC(GET) pathway.
3. Quality-control rheostat antagonizing BAG6-mediated ubiquitination/proteasomal triage
   (GO:1904288 BAG6 complex binding; ERAD regulation terms).
4. Homodimer (GO:0042802); cytosolic (also nuclear).
