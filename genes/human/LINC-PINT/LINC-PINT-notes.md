# LINC-PINT (PINT87aa, UniProt A0A455ZAR2) – review notes

## Scope

This folder is the UniProt entry A0A455ZAR2 (PNT87_HUMAN, "Transcriptional regulator
PINT87aa"), an 87-aa peptide. UniProt files it under the HGNC symbol of its host locus,
`LINC-PINT` (HGNC:26885), a long intergenic non-protein-coding RNA. There is no separate
HGNC symbol for the peptide, and the host is itself non-coding, so there is no competing
canonical protein for this symbol; the folder name is the plain host symbol.

Separate peptide-level from RNA-level evidence. Almost all LINC-PINT literature (miRNA
sponging, PRC2 recruitment, p53-induced transcript; dozens of cancer/inflammation papers)
concerns the RNA and is **not** evidence about PINT87aa. A PubMed search on 2026-10-03 for
`PINT87aa`, `circPINT`, `PINT 87aa` and `LINC-PINT AND (circular OR circRNA)` returned
only two primary papers on the peptide (PMID:30367041, PMID:33754036), plus reviews.
Both come from overlapping authors (Zhang N, Zhao K, Sun Yat-sen University); there is
no independent replication.

## Origin: translated from a circular RNA

- Peptide is encoded by circPINTexon2 (circBase hsa_circ_0082389), a back-spliced circle of
  LINC-PINT exon 2. [PMID:30367041 "The long exon 2 of LINC-PINT, which contains the 3′ AG receptor and 5′ GT donor sequences required for back-splicing, was identified as a circRNA"]
- Translation is cap-independent from an IRES within the circle. [PMID:30367041 "the natural IRES in circPINTexon2 induced ribosome entry and initiated translation"]
- The circle and the linear lncRNA are in different compartments: [PMID:30367041 "linear LINC-PINT largely localized to the nucleus, whereas circPINTexon2 was mostly cytoplasmic"]
- Endogenous peptide detected with a custom antibody and IP–MS. [PMID:30367041 "Endogenous immunoprecipitation using this antibody followed by LC-MS/MS in 293T cells further confirmed that the 10-kDa peptide sequences matched the predicted 87-aa sORF"]
  UniProt PE1 (protein sequence 1-7 and 37-56 by MS).
- Sequence is unusual: Arg-rich, with a run of seven Cys (CCCCCCC); no known domain other
  than Pfam PF21971 (LINC-PINT family, which is just this peptide). No PANTHER / PAN-GO.

## Glioblastoma paper (PMID:30367041) – PAF1 complex

- Binds PAF1 (pull-down/IP–MS, co-IP, purified-protein binding to PAF1 aa 150–300).
  [PMID:30367041 "A direct binding assay using purified proteins further indicated that PINT87aa interacts with the 150–300-aa domain of PAF1"]
- Nuclear (RFP/GFP fusions; co-localises with PAF1).
  [PMID:30367041 "Using RFP fusion protein labeling, we found that this peptide was concentrated in nucleus"]
  [PMID:30367041 "Furthermore, GFP-PINT87aa and PAF1 co-localized in the nucleus"]
  Note the tension: the coding circle is cytoplasmic (translation site) but the product is
  nuclear. Fine – small peptide, synthesised in cytoplasm.
- Reduces mRNA of PAF1 targets (CPEB1, SOX2, MYC) in brain tumour-initiating cells.
  [PMID:30367041 "The mRNA of PAF1 downstream genes, including CPEB1, SOX-2, c-Myc, etc., was inhibited transcriptionally"]
- ChIP: co-occupies CPEB1 promoter with PAF1; overexpression/knockdown raise/lower PAF1 promoter occupancy.
  [PMID:30367041 "PINT87aa overexpression or knocking down enhanced or decreased PAF1/CPEB1 promoter affinity, respectively"]
- Model (explicitly an assumption): [PMID:30367041 "We assumed that PINT87aa may work as an anchor and keep PAF1 complex on target genes’ promoter, which sequentially pauses Pol II-induced mRNA elongation"]
- No DNA binding: [PMID:30367041 "Although no evidence showed that PINT87aa directly binds to DNA and act as a transcription factor"]
- Important control separating RNA vs peptide: ASO knockdown of linear LINC-PINT did not
  change PAF1 targets. [PMID:30367041 "LINC-PINT knockdown in SW1783 and Hs683 cells using specific ASOs increased cell viability but did not alter PAF1 downstream gene mRNA or protein levels"]
- Elongation per se was not measured (no Pol II pausing index / nascent RNA); GO:0034244
  (negative regulation of transcription elongation by RNA Pol II) would over-reach the data.
  GO:0000122 is the safer level.

## HCC paper (PMID:33754036) – FOXM1

- Binds FOXM1 DNA-binding domain (docking + co-IP, GFP-only control negative; deletion of
  aa 30–36 abolishes binding). [PMID:33754036 "PINT87aa could bind to the DNA-binding domain of FOXM1, which was confirmed by co-IP results, indicating that PINT87aa-GFP and FOXM1 interacted with each other"]
  [PMID:33754036 "The co-IP results showed no interaction between the truncated PINT87aa-GFP and FOXM1"]
- Does not change FOXM1 levels but lowers its targets incl. PHB2. [PMID:33754036 "We confirmed that FOXM1 could promote the transcription of PHB2 and a negative regulatory effect of PINT87aa on PHB2 expression"]
- Downstream phenotypes from overexpression in HCC lines: senescence, G1 arrest, reduced
  PHB2-dependent mitophagy. [PMID:33754036 "These results indicated that PINT87aa could decrease PHB2 mediated mitophagy"]
  These are overexpression phenotypes in tumour lines; indirect, so not proposed as NEW.

## Decisions

- GO:0000122 IMP – ACCEPT (core). Both papers point to repression of RNA Pol II target genes.
- protein binding (PAF1) – REMOVE: uninformative; PAF1 is an elongation-complex subunit,
  not a DNA-binding TF, so GO:0140297 does not fit; no "PAF1 complex binding" MF exists.
  Mechanism captured by the BP plus description.
- protein binding (FOXM1) – MODIFY to GO:0140297 DNA-binding transcription factor binding
  (FOXM1 is a forkhead DNA-binding TF; binding maps to its DBD).
- nucleus IDA and IEA – ACCEPT.
- Not proposing GO:0003714 transcription corepressor activity: plausible for the FOXM1
  arm but only overexpression data from one group; raised as a question instead.
- No NEW BP terms for senescence / mitophagy (indirect, overexpression).
