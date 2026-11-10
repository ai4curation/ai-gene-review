# LOC542632 (maize GSTU6 / "ZmGST27", A0A804QUX9) - manual literature research

No deep-research API was available; this file records manual literature work
(PubMed MCP searches, cached publications in `publications/`, UniProt and NCBI Gene
records) carried out for this review.

## Identity

- UniProt A0A804QUX9 (TrEMBL, 237 aa), B73 v5 gene model Zm00001eb356600, chromosome 8.
  NCBI GeneID 542632, RefSeq NP_001105627.1.
- NCBI Gene 542632 is named "glutathione transferase27" with other designations
  "Probable glutathione S-transferase GSTU6", "glutathione S-transferase GST 27",
  "glutathione S-transferase GSTU6"; aliases GRMZM2G077206 / Zm00001d011154 (v4).
- The older TrEMBL entry Q9FQB2 (same 237-aa product, same GeneID 542632, RefSeq
  NP_001105627.1) carries the mRNA AF244692 deposited by McGonigle et al. 2000
  [PMID:11080288 "we have identified 25 soybean (Glycine max) and 42 maize (Zea mays)
  clones and obtained accurate full-length GST sequences"]. The "GST 27" name comes from
  the numbering of that EST survey.
- Sequence family: tau class GST. UniProt: "Belongs to the GST superfamily. Tau family"
  (ARBA-only; treated as unvetted), but independent signatures agree: InterPro
  IPR045074 GST_C_Tau, CDD cd03058 GST_N_Tau and cd03185 GST_C_Tau, PANTHER
  PTHR11260:SF776, SFLD Main.3 Omega- and Tau-like. Thioredoxin-fold GST N-terminal
  domain (9..88) and all-alpha GST C-terminal domain (95..222).
- Own inspection of the sequence: the N-terminal region reads
  `LKLLGAWPSPFVNRVRMALH`, the canonical tau-class G-site motif, with the putative
  catalytic serine (Ser19 in A0A804QUX9 numbering) in the position of the active-site
  serine conserved in plant tau GSTs (McGonigle et al. abstract: "only the active site
  serine, as well as another serine and arginine in or near the 'G-site' are conserved
  throughout").

## Naming trap: two different maize "GST-27" genes

- The classic safener-inducible maize "GST-27" is the 27-kDa phi-class subunit of
  GST II (29/27 heterodimer) and GST IV (27/27 homodimer) [PMID:7858222 "GST IV a
  homodimer of 27 kDa subunits"]. That protein is Swiss-Prot P46420 (GST4, GST class-phi
  member 4, GST-27, GST-IV; GeneID 542311; cDNA X79515), a different gene from
  LOC542632.
- Biochemical work on GST-27/GST IV (alachlor/metolachlor conjugation, transgenic
  herbicide tolerance, tetrapyrrole binding [PMID:15948579], alachlor sensitivity of
  inbreds [PMID:12226466], purification of GST II [PMID:7599527]) concerns P46420 and must
  not be transferred to LOC542632.
- Pang et al. 2012 call their gene "ZmGST27" but designed primers from AF244692
  [PMID:22792398 "were designed from the ORF region of ZmGST27 (accession number
  AF244692)"], i.e. from the LOC542632 (tau) transcript. Their discussion nevertheless
  says dichlormid "has been reported to increase the levels of ZmGST27 and ZmMRP1
  transcripts [28], [29]", which probably refers to the phi GST-27 literature
  (reference list not in cache; not verified). The expression data in the Pang papers
  are therefore attributed to LOC542632, while their literature context partly
  conflates the two genes.
- Cancado et al. 2005 (PMID:32689200, abstract only from PubMed) describe an
  Al-inducible "GST27.2" homologous to "the maize gene GST27, which is known to be
  induced by xenobiotics", and classify it as "theta-type" (old name for phi); this
  relates to the phi gene, not LOC542632.

## Experimental evidence on LOC542632 itself

1. Pang et al. 2012 PLoS One (PMID:22792398, full text): semi-quantitative RT-PCR in
   maize leaves; "the expression of ZmGST27 was induced by all five test compounds"
   (atrazine, 2,4-D, primisulfuron, metolachlor, dichlormid), detectable at 4 h and
   maintained to 96 h; induction was the earliest of the three genes studied
   ("For all chemicals, the inducing effect was first detected on ZmGST27"). The authors
   themselves interpret induction by 2,4-D and primisulfuron as "a general response of
   this gene to chemical stress".
2. Pang et al. 2012 PLoS One (PMID:23144728, full text): rac- and S-metolachlor induce
   ZmGST27 comparably ("the inducing effect of rac- and S-metolachlor on the expression
   of ZmGST27 and ZmGT1 is comparable"); "The non-selective up-regulation of ZmGST27
   expression by rac- and S-metolachlor is likely to be a general response of this gene
   to chemical stress."
3. Torabi & Rahmani 2025 (PMID:39970567, abstract): GST27 upregulated by
   24-epibrassinolide under arsenic stress; gene identity (phi vs tau) not stated in the
   abstract; not used.
4. McGonigle et al. 2000 (PMID:11080288): source of the AF244692 sequence; the abstract
   reports microarray induction of type III (tau) GSTs by inducers and recombinant
   activity for "a subset of GSTs"; whether GST 27 was in the assayed subset could not be
   checked (full text not retrievable: PMC59210 returned no body text).

No study has measured the enzymatic activity, substrate range, subcellular location,
or loss-of-function phenotype of the LOC542632 protein.

## Inference

- Molecular function: tau-class GSTs with an intact catalytic serine are
  glutathione transferases (EC 2.5.1.18) with CDNB and herbicide (chloroacetanilide,
  diphenyl ether) conjugating activity in most cases; the UniRule RU369102 assignment
  of EC 2.5.1.18 and the conserved G-site support glutathione transferase activity, but
  no assay exists for this protein.
- Location: plant tau GSTs without targeting peptides are cytosolic; A0A804QUX9 has no
  predicted signal peptide or transit peptide in the record; UniRule assigns cytosol.
- Process: the xenobiotic-inducible expression is consistent with a phase II
  herbicide-detoxification role, but induction is not participation; no process term is
  proposed beyond the existing glutathione metabolic process row.
