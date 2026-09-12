# FraE research notes (Cylindrospermum stagnale PCC 7417)

Gene: **fraE** ortholog, ordered locus **Cylst_1328**, *Cylindrospermum stagnale* PCC 7417.
UniProt: **K9WTV4** (K9WTV4_9NOST, unreviewed/TrEMBL), 259 aa, PE=4 (Predicted).
Taxon: NCBITaxon:56107. RefSeq WP_015206874.1; EMBL AFZ23618.1. eggNOG COG1277.
UniProt SubName (EMBL-derived, non-experimental): "ABC-type transport system involved in
multi-copper enzyme maturation, permease component".

## Summary

K9WTV4 is the **FraE ortholog** in *Cylindrospermum stagnale* PCC 7417 of the well-studied
*Nostoc* (Anabaena) sp. PCC 7120 FraE (alr2394; UniProt A0ACD7RSN5). FraE is the third and
least-characterized gene of the **fraC-fraD-fraE** operon in filamentous, heterocyst-forming
cyanobacteria. In PCC 7120 the operon is constitutively expressed, and single mutants of its
genes fragment under nitrogen deprivation and fail to grow diazotrophically despite forming
heterocysts [PMID:20487302 "was constitutively expressed as an operon together with two downstream
genes, \nalr2393 (fraD) and alr2394 (fraE)"; PMID:20487302 "Single mutants of these genes showed
filament fragmentation under \nnitrogen deprivation and did not grow diazotrophically, although
they formed \nheterocysts"]. The operon partners FraC and FraD localize to the intercellular septa
and act as structural components of the septal junction that connects adjacent cells in the
filament [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also \nlocated at the
intercellular septa"]. FraE itself has little direct functional characterization; its molecular
classification is essentially domain-based, and no transported substrate is known. The UniProt
SubName "multi-copper enzyme maturation" is an unreviewed EMBL annotation and is not an
experimentally supported substrate assignment; do not over-claim it.

## Orthology evidence

The FraE ortholog assignment for K9WTV4 rests on reciprocal-best-hit homology plus conserved
operon synteny (module genome scan; modules/septal_junction/):

- **Homology (RBH)**: K9WTV4 is the reciprocal best hit of PCC 7120 FraE (A0ACD7RSN5); forward
  E = 7.2e-109, 70.3% identity — the reciprocal best-scoring FraE match in *C. stagnale*.
- **Protein family (broad, non-diagnostic on its own)**: InterPro **IPR032688** "ABC-2 type
  transporter permease protein NosY-like" (ABC2_NosY-like); Pfam **PF12679** "ABC-2 family
  transporter protein" (ABC2_membrane_2); PANTHER **PTHR43471** "ABC Transporter Permease". This
  ABC-2 permease family is broad and present across cyanobacteria, so family membership alone does
  not discriminate the true FraE ortholog.
- **Conserved operon synteny (the decisive evidence)**: the FraC/FraD/FraE best hits carry
  consecutive accessions in *C. stagnale* — **Cylst_1330 (fraC) – Cylst_1329 (fraD) – Cylst_1328
  (fraE)** — reproducing the intact, syntenic fraC-fraD-fraE operon. Because the ABC-2 family is
  non-diagnostic, this conserved operon context is the key evidence that K9WTV4 is the true FraE
  ortholog rather than an unrelated ABC-2 permease paralog.

Provenance sentence (quotable): K9WTV4 is the FraE ortholog of Nostoc sp. PCC 7120 FraE
(A0ACD7RSN5) by reciprocal-best-hit phmmer homology (forward E = 7.2e-109, 70.3% identity) and by
conserved operon synteny of the fraC-fraD-fraE operon (Cylst_1330-Cylst_1329-Cylst_1328 in
C. stagnale).

## Protein family / domain architecture

K9WTV4 is an integral-membrane **ABC-2-type transporter permease-family** protein (NosY-like),
i.e. the membrane permease component, NOT the ATP-hydrolyzing (nucleotide-binding) ATPase subunit.
UniProt/Phobius predicts six transmembrane helices (residues 21-40, 52-76, 103-124, 130-146,
153-177, 230-254), consistent with a polytopic integral membrane permease. A permease component
of an ABC transporter provides the transmembrane translocation pathway but does not itself
hydrolyze ATP; full "ABC-type transporter activity" (ATP-coupled primary active transport) is a
property of the complete transporter (permease + nucleotide-binding domain), not of the permease
subunit alone.

Provenance for the family assignment used in this review:
K9WTV4 (FraE ortholog, Cylst_1328) is classified by InterPro as IPR032688 "ABC-2 type transporter
permease protein NosY-like" (Pfam PF12679; PANTHER PTHR43471), i.e. an integral-membrane
ABC-2-type transporter permease-family protein that is the permease (not ATPase) component.

## Caveats / knowledge gaps

- K9WTV4 is the *C. stagnale* ortholog of the least-characterized member of the fraC-fraD-fraE
  operon. Its ABC-2 permease classification is domain-based (IEA from IPR032688), and there is no
  direct experimental data specifically on this protein; the functional picture is inferred by
  orthology (ISS) to PCC 7120 FraE.
- No specific transported substrate is known. The UniProt SubName "multi-copper enzyme maturation"
  is an unreviewed EMBL string, not experimental evidence; do not over-claim a substrate.
- Because its operon partners FraC and FraD are structural septal-junction proteins rather than
  canonical substrate transporters, it remains possible that FraE also acts primarily in filament
  integrity / septal-junction context (a purely structural role) rather than as a classical
  substrate-transporting permease. The two GOA IEA annotations (transmembrane transport; ABC-type
  transporter activity) reflect the fold, not a demonstrated transport reaction.

## Existing GOA annotations (IEA, GO_REF:0000002, from InterPro IPR032688)

- GO:0055085 transmembrane transport (BP, involved_in) — general BP consistent with an
  integral-membrane permease fold; domain-based. ACCEPT.
- GO:0140359 ABC-type transporter activity (MF, enables) — the "enables" qualifier over-claims for
  a permease-only subunit, which contributes to but does not independently enable ATP-coupled
  transporter activity. Better represented as contributes_to the complex-level activity, with a
  subunit-level transmembrane transporter activity (GO:0022857). MARK_AS_OVER_ANNOTATED.

## Proposed additions (ISS, orthology/domain-based)

- GO:0022857 transmembrane transporter activity (MF) — subunit-level MF for the permease component.
- GO:0005886 plasma membrane (CC) — polytopic integral cytoplasmic-membrane protein by prediction
  and operon context.

## Key references

- PMID:20487302 — Merino-Puerto et al. 2010, Mol Microbiol. Establishes the fraC-fraD-fraE operon
  in PCC 7120, its constitutive expression, and mutant phenotypes (fragmentation, no diazotrophic
  growth), plus septal localization of FraC and FraD. PRIMARY for the 7120 ortholog whose function
  is transferred here. Abstract only in cache.
- file:CYLST/FraE/FraE-notes.md — these notes (orthology evidence, family assignment, provenance).
