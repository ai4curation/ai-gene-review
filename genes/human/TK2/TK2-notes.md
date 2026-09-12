# TK2 (Thymidine kinase 2, mitochondrial) — review notes

UniProtKB: O00142 (KITM_HUMAN). HGNC:11831. Chr 16q21. EC 2.7.1.21 (thymidine kinase),
EC 2.7.1.74 (deoxycytidine kinase), EC 2.7.1.- (deoxyuridine kinase).

Deep research: falcon was OUT OF CREDITS (HTTP 402) at review time, so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record,
the seeded GOA, and cached `publications/PMID_*.md` (all 6 GOA-cited PMIDs are cached).

## Core biology

TK2 is the **mitochondrial thymidine kinase 2**, a multisubstrate deoxyribonucleoside
kinase of the DCK/DGK (deoxyribonucleoside kinase) family. It phosphorylates the
pyrimidine deoxyribonucleosides **thymidine, deoxycytidine and deoxyuridine** to their
respective dNMPs (dTMP, dCMP, dUMP) using ATP, within the mitochondrial matrix.

- [PMID:9079672 "Human thymidine kinase 2 (TK2) is a deoxyribonucleoside kinase that phosphorylates thymidine, deoxycytidine, and deoxyuridine."]
- UniProt FUNCTION [file:human/TK2/TK2-uniprot.txt "Phosphorylates thymidine, deoxycytidine, and deoxyuridine in the mitochondrial matrix"]
- Kinetics: KM 16 uM thymidine, 36 uM 2'-deoxycytidine (UniProt / PMID:9989599).

TK2 is the **pyrimidine arm of the mitochondrial deoxyribonucleoside salvage pathway**.
The mitochondrial dNTP pool is separated from the cytosolic pool (inner membrane
impermeable to charged molecules); it is maintained by import of cytosolic dNTPs or by
salvage of deoxynucleosides inside mitochondria. De novo dNTP synthesis enzymes are
absent from mitochondria. In non-replicating/quiescent cells, where cytosolic dNTP
synthesis is down-regulated, mtDNA synthesis depends solely on the mitochondrial salvage
kinases TK2 and DGUOK (dGK).

- [PMID:11687801 "In non-replicating cells, where cytosolic dNTP synthesis is down-regulated, mtDNA synthesis depends solely on the mitochondrial salvage pathway enzymes, the deoxyribonucleosides kinases."]
- [PMID:11687801 "Two of the four human deoxyribonucleoside kinases, deoxyguanosine kinase (dGK) and thymidine kinase-2 (TK2), are expressed in mitochondria."]
- [PMID:11687801 "TK2 phosphorylates deoxythymidine, deoxycytidine and deoxyuridine."]
- UniProt [file:human/TK2/TK2-uniprot.txt "mtDNA synthesis depends solely on TK2 and DGUOK"]

DGUOK (deoxyguanosine kinase) handles the **purine** arm (deoxyguanosine, deoxyadenosine);
TK2 handles the **pyrimidine** arm. Together they supply all four mitochondrial dNTPs via
salvage in post-mitotic tissue.

## Localization

Mitochondrion / mitochondrial matrix. N-terminal mitochondrial transit peptide (residues
1-33), cleaved; mature chain 34-265.

- UniProt SUBCELLULAR LOCATION: Mitochondrion (PubMed:9989599, IDA).
- UniProt FUNCTION locates activity to "the mitochondrial matrix".
- Reactome R-HSA-109759 places TK2 activity in mitochondrial matrix (TAS).
- High-throughput mitochondrial proteome (PMID:34800366, MitoCoP) includes TK2 (HTP).

## Disease

- **MTDPS2** (mitochondrial DNA depletion syndrome 2, myopathic form; MIM:609560):
  autosomal recessive; childhood-onset muscle weakness with mtDNA depletion in skeletal
  muscle. Loss-of-function TK2 variants reduce muscle mitochondrial TK2 activity to
  14-45% of control (PMID:11687801). Wide clinical variability; can be rapidly progressive
  with early death.
- **PEOB3** (progressive external ophthalmoplegia with multiple mtDNA deletions,
  autosomal recessive 3; MIM:617069) — PMID:21937588.
- Deoxynucleoside (dCMP/dTMP prodrug, e.g. doxecitine/doxribtimine) substrate-bypass
  therapy is in clinical use for TK2 deficiency (rationale: replenish the salvage products
  downstream of the missing kinase step).

## GOA annotation assessment summary

Core MF (accept): GO:0004797 thymidine kinase activity (IDA PMID:11687801, PMID:9989599;
TAS PMID:9079672; IBA; IEA). GO:0004137 deoxycytidine kinase activity (IDA x2; IBA; IEA).
GO:0005524 ATP binding (IEA InterPro) — accept, substrate/cofactor is ATP.
GO:0019136 deoxynucleoside kinase activity (IEA) — accept as parent MF (deoxyuridine
kinase arm; the RHEA:28206 deoxyuridine reaction maps here).
GO:0019206 nucleoside kinase activity (TAS Reactome) — grandparent MF; MARK_AS_OVER_ANNOTATED
(too general; the three specific pyrimidine dNK activities are the informative terms).

Over-annotated / wrong-branch MF:
- GO:0004136 deoxyadenosine kinase activity (IBA) — this is the DGUOK/purine arm, NOT TK2.
  TK2 phosphorylates pyrimidines. IBA propagation from the shared dNK PANTHER family is a
  paralog over-annotation. MARK_AS_OVER_ANNOTATED (borderline REMOVE; TK2 has negligible
  dA activity). The linked BP GO:0006170 dAMP biosynthetic process (IEA, inferred from
  GO:0004136) is likewise a purine-arm over-annotation.
- GO:0005515 protein binding (IPI x2, GSTK1/Q9Y2Q3 from high-throughput AP-MS) —
  uninformative; MARK_AS_OVER_ANNOTATED per curation policy (do not REMOVE experimental
  IPIs; bare protein binding is not informative).

CC:
- GO:0005739 mitochondrion (IBA is_active_in; IEA; IDA PMID:9989599; HTP PMID:34800366) —
  accept. GO:0005759 mitochondrial matrix (TAS Reactome) — accept (more specific).
- GO:0005737 cytoplasm (IBA is_active_in) — MARK_AS_OVER_ANNOTATED: TK2 is a
  matrix-localized mitochondrial protein with a cleaved transit peptide; the cytoplasm
  term is an over-broad IBA (family members include cytosolic dCK; TK2 itself is
  mitochondrial).

BP (mostly accept as different granularities of pyrimidine dNMP salvage / mtDNA precursor
supply):
- GO:0046104 thymidine metabolic process (IEA) — accept.
- GO:0046092 deoxycytidine metabolic process (IEA) — accept.
- GO:0009157 deoxyribonucleoside monophosphate biosynthetic process (IEA) — accept
  (direct product class).
- GO:0043097 pyrimidine nucleoside salvage (TAS Reactome) — accept (core pathway role).
- GO:0009165 nucleotide biosynthetic process (IEA, inferred from GO:0019206) —
  MARK_AS_OVER_ANNOTATED (too general).
- GO:0006139 nucleobase-containing compound metabolic process (TAS PMID:9079672) —
  MARK_AS_OVER_ANNOTATED (very general parent).
- GO:0006170 dAMP biosynthetic process (IEA from GO:0004136) — see purine-arm note;
  MARK_AS_OVER_ANNOTATED.
