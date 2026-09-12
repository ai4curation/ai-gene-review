# FraE research notes (Nostoc punctiforme PCC 73102)

Gene: **fraE** ortholog, ordered locus **Npun_R1225**, *Nostoc punctiforme* (strain ATCC 29133 / PCC 73102).
UniProt: **B2IXC7** (B2IXC7_NOSP7, unreviewed/TrEMBL), 259 aa, PE=4 (Predicted).
Taxon: NCBITaxon:63737. RefSeq WP_012407970.1; EMBL ACC79949.1.

## Summary

B2IXC7 is the **FraE ortholog** in *Nostoc punctiforme* PCC 73102 of the well-studied *Nostoc*
(Anabaena) sp. PCC 7120 FraE (alr2394; UniProt A0ACD7RSN5). FraE is the third and
least-characterized gene of the **fraC-fraD-fraE** operon in filamentous, heterocyst-forming
cyanobacteria. In PCC 7120 the operon is constitutively expressed, and single mutants of its
genes fragment under nitrogen deprivation and fail to grow diazotrophically despite forming
heterocysts [PMID:20487302 "constitutively expressed as an operon together with two downstream
genes, alr2393 (fraD) and alr2394 (fraE)"; PMID:20487302 "Single mutants of these genes showed
filament fragmentation under nitrogen deprivation and did not grow diazotrophically, although
they formed heterocysts"]. The operon partners FraC and FraD localize to the intercellular septa
and act as structural components of the septal junction that connects adjacent cells in the
filament [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the
intercellular septa"]. FraE itself has little direct functional characterization; its molecular
classification is essentially domain-based, and no transported substrate is known.

## Orthology evidence

The FraE ortholog assignment for B2IXC7 rests on exemplar homology plus conserved operon synteny
(a module genome scan; modules/septal_junction/RESULTS.md):

- **Homology**: phmmer of B2IXC7 against PCC 7120 FraE (A0ACD7RSN5) gives a highly significant hit,
  E = 6e-119 (5.9e-119), 74.5% (~75%) identity — B2IXC7 is the reciprocal best-scoring FraE match
  in *N. punctiforme*.
- **Protein family (broad, non-diagnostic on its own)**: InterPro **IPR032688** "ABC-2 type
  transporter permease protein NosY-like"; Pfam **PF12679** "ABC-2 family transporter protein"
  (ABC2_membrane_2); PANTHER **PTHR43471** "ABC Transporter Permease". This ABC-2 permease family
  is broad and present across cyanobacteria, so family membership alone does not discriminate the
  true FraE ortholog.
- **Conserved operon synteny (the decisive evidence)**: the FraC/FraD/FraE best hits carry
  consecutive accessions in *N. punctiforme* — **B2IXC9 (FraC) – B2IXC8 (FraD) – B2IXC7 (FraE)** —
  reproducing the intact, syntenic fraC-fraD-fraE operon. Because the ABC-2 family is
  non-diagnostic, this conserved operon context is the key evidence that B2IXC7 is the true FraE
  ortholog rather than an unrelated ABC-2 permease paralog.

Provenance sentence (quotable): B2IXC7 is the FraE ortholog of Nostoc sp. PCC 7120 FraE
(A0ACD7RSN5) by phmmer homology (E = 6e-119, ~75% identity) and by conserved operon synteny of
the fraC-fraD-fraE operon (B2IXC9-B2IXC8-B2IXC7 in N. punctiforme).

## Protein family / domain architecture

B2IXC7 is an integral-membrane **ABC-2-type transporter permease-family** protein (NosY-like),
i.e. the membrane permease component, NOT the ATP-hydrolyzing (nucleotide-binding) ATPase subunit.
UniProt/Phobius predicts six transmembrane helices (residues ~21-40, 52-76, 103-124, 130-151,
158-178, 236-254), consistent with a polytopic integral membrane permease. A permease component
of an ABC transporter provides the transmembrane translocation pathway but does not itself
hydrolyze ATP; full "ABC-type transporter activity" (ATP-coupled primary active transport) is a
property of the complete transporter (permease + nucleotide-binding domain), not of the permease
subunit alone.

Provenance for the family assignment used in this review:
B2IXC7 (FraE ortholog, Npun_R1225) is classified by InterPro as IPR032688 "ABC-2 type transporter
permease protein NosY-like" (Pfam PF12679; PANTHER PTHR43471), i.e. an integral-membrane
ABC-2-type transporter permease-family protein that is the permease (not ATPase) component.

## Caveats / knowledge gaps

- B2IXC7 is the *N. punctiforme* ortholog of the least-characterized member of the fraC-fraD-fraE
  operon. Its ABC-2 permease classification is domain-based (IEA from IPR032688), and there is no
  direct experimental data specifically on this protein; the functional picture is inferred by
  orthology (ISS) to PCC 7120 FraE.
- No specific transported substrate is known. Do not over-claim a substrate.
- Because its operon partners FraC and FraD are structural septal-junction proteins rather than
  canonical substrate transporters, it remains possible that FraE also acts primarily in filament
  integrity / septal-junction context (a purely structural role) rather than as a classical
  substrate-transporting permease. The two GOA IEA annotations (transmembrane transport;
  ABC-type transporter activity) reflect the fold, not a demonstrated transport reaction.

## Existing GOA annotations (IEA, GO_REF:0000002, from InterPro IPR032688)

- GO:0055085 transmembrane transport (BP, involved_in) — general BP consistent with an
  integral-membrane permease fold; domain-based. ACCEPT.
- GO:0140359 ABC-type transporter activity (MF, enables) — the "enables" qualifier over-claims for
  a permease-only subunit, which contributes to but does not independently enable ATP-coupled
  transporter activity. Better represented as contributes_to the complex-level activity, with a
  subunit-level transmembrane transporter activity (GO:0022857). MARK_AS_OVER_ANNOTATED.

## Key references

- PMID:20487302 — Merino-Puerto et al. 2010, Mol Microbiol. Establishes the fraC-fraD-fraE operon
  in PCC 7120, its constitutive expression, and mutant phenotypes (fragmentation, no diazotrophic
  growth). PRIMARY for the 7120 ortholog whose function is transferred here. Abstract only in cache.
- file:NOSP7/FraE/FraE-notes.md — these notes (orthology evidence, family assignment, provenance).
