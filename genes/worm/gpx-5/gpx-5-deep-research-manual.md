# gpx-5 (C11E4.1, UniProt Q93204) - manual literature review

No deep-research API was available; this summary was assembled by hand from the
cached publication, PubMed searches and the UniProt record.

## Identity and sequence features

- gpx-5 / C11E4.1 (WormBase WBGene00007516; GeneID 181178), chromosome X, 223 aa,
  unreviewed TrEMBL entry Q93204 (sequence version 3) [file:worm/gpx-5/gpx-5-uniprot.txt].
- Member of the glutathione peroxidase family (Pfam PF00255 GSHPx, PIRSF000303,
  PROSITE PS00460/PS00763/PS51355, PANTHER PTHR11592:SF88 "GLUTATHIONE
  PEROXIDASE-RELATED") [file:worm/gpx-5/gpx-5-uniprot.txt].
- Predicted N-terminal signal peptide 1-17 (SignalP); no transmembrane segment and no
  C-terminal ER-retention motif (ends ...EQLLAEPAN).
- The peroxidatic position is a cysteine (Cys72, in the motif NVATFCAYT), which aligns with
  the selenocysteine of human GPX1 (Sec49, motif NVASLUGTT). gpx-5 is therefore a
  Cys-type (non-selenium) GPx, like mammalian epididymal GPX5 (P21765, mouse), which
  is also a secreted Cys-GPx. The other tetrad positions appear conserved: Gln102 in the
  FPCNQF signature and Trp182 in the WNFEKF motif (positions computed from the
  UniProt sequence in this session).
- Cys-GPx enzymes outside vertebrates are frequently thioredoxin-dependent rather
  than glutathione-dependent peroxidases; the reducing substrate of GPX-5 has not been
  measured. This is general family knowledge, not a gpx-5 result.

## Experimental literature

PubMed search "gpx-5 AND elegans" (Oct 2026) returned only two recent papers, neither of
which characterises GPX-5 specifically. The key experimental paper is the GSH-metabolism
RNAi screen of Lüersen et al. 2013:

- [PMID:23593298 "knockdown of an alpha-class related GST (gst-32), an omega-class GST
  (gst-44) and an extracellular glutathione peroxidase (C11E4.1) less profoundly affected
  the survival rate under arsenite stress"]. In the screen table, C11E4.1/gpx-5 RNAi gave
  80.0+/-14.5 % survival under juglone (no significant effect) and 13.3+/-9.4 % (***)
  under arsenite.
- The authors interpret the arsenite result through GSH-dependent peroxide reduction
  [PMID:23593298 "Both, the alpha-class related gst-32 and the GPX are implicated in the
  oxidative stress response by way of their GSH-dependent reduction of inorganic and
  organic peroxides or by their ability to eliminate secondary products of lipid
  peroxidation."] - an inference from the family, not a measurement on GPX-5.
- PMID:42822957 (Wan et al. 2026, abstract only): expression of gpx-1 to gpx-6 decreased on
  6-PPD quinone exposure and RNAi of the gpx genes exacerbated 6-PPDQ neurotoxicity. Not
  gene-specific mechanistic evidence.

No biochemical activity assay, localisation study or structure exists for GPX-5.
