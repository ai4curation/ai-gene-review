# FraE (alr2394) research notes

Gene: **fraE** = ordered locus **alr2394**, Nostoc sp. (Anabaena sp.) strain PCC 7120.
UniProt: **A0ACD7RSN5** (unreviewed/TrEMBL), 267 aa, PE=4 (Predicted).
Taxon: NCBITaxon:103690.

## Summary

FraE is the third and least-characterized gene of the **fraC(alr2392)-fraD(alr2393)-fraE(alr2394)** operon
in the filamentous, heterocyst-forming cyanobacterium Nostoc/Anabaena sp. PCC 7120. The operon is
constitutively expressed, and single mutants of the operon genes fragment under nitrogen deprivation and fail
to grow diazotrophically despite forming heterocysts [PMID:20487302 "constitutively expressed as an operon
together with two downstream genes, alr2393 (fraD) and alr2394 (fraE)"; PMID:20487302 "Single mutants of these
genes showed filament fragmentation under nitrogen deprivation and did not grow diazotrophically, although they
formed heterocysts"].

Whereas FraC and FraD have been localized to the intercellular septa and characterized as structural
components of the septal junction (SJ), the gap-junction-like intercellular channel that connects adjacent
cells in a filament [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the
intercellular septa"], FraE itself has little direct functional characterization. Its molecular classification
is essentially domain-based.

## Protein family / domain architecture

InterPro/Pfam/PANTHER classification (domain-based, IEA):

- **IPR032688** "ABC-2 type transporter permease protein NosY-like"
- Pfam **PF12679** "ABC-2 family transporter protein"
- PANTHER **PTHR43471** "ABC Transporter Permease"

Thus FraE is an integral-membrane **ABC-2-type transporter permease-family** protein (NosY-like), i.e. a
membrane permease component. It is NOT the ATP-hydrolyzing (nucleotide-binding) ATPase subunit. A permease
component of an ABC transporter provides the transmembrane translocation pathway but does not itself hydrolyze
ATP; full "ABC-type transporter activity" (ATP-coupled primary active transport) is a property of the complete
transporter (permease + nucleotide-binding domain), not of the permease subunit alone.

Provenance for the family assignment used in this review:
FraE (alr2394) is classified by InterPro as IPR032688 "ABC-2 type transporter permease protein NosY-like"
(Pfam PF12679; PANTHER PTHR43471), i.e. an integral-membrane ABC-2-type transporter permease-family protein
that is the permease (not ATPase) component.

The 267-aa sequence is strongly hydrophobic and consistent with a polytopic integral membrane protein
(multiple predicted transmembrane helices), matching the permease classification.

## Caveats / knowledge gaps

- FraE is the least-characterized member of the fraC-fraD-fraE operon. Its ABC-2 permease classification is
  domain-based (IEA from IPR032688), and there is little direct experimental data specifically on FraE.
- No specific transported substrate is known. Do not over-claim a substrate.
- Because its operon partners FraC and FraD are structural septal-junction proteins rather than canonical
  substrate transporters, it remains possible that FraE also acts primarily in filament integrity / septal
  junction context rather than as a classical substrate-transporting permease. The two GOA IEA annotations
  (transmembrane transport; ABC-type transporter activity) reflect the fold, not a demonstrated transport
  reaction.

## Existing GOA annotations (IEA, GO_REF:0000002, from InterPro IPR032688)

- GO:0055085 transmembrane transport (BP, involved_in) — general BP consistent with an integral-membrane
  permease fold; domain-based.
- GO:0140359 ABC-type transporter activity (MF, enables) — the "enables" qualifier over-claims for a
  permease-only subunit, which contributes to but does not independently enable ATP-coupled transporter
  activity. Better represented as contributes_to the complex-level activity, with a subunit-level
  transmembrane transporter activity (GO:0022857).

## Key references

- PMID:20487302 — Merino-Puerto et al. 2010, Mol Microbiol. Establishes the fraC-fraD-fraE operon,
  constitutive expression, and mutant phenotypes (fragmentation, no diazotrophic growth). PRIMARY. Abstract
  only in cache.
- PMID:7883709 — Bauer et al. 1995, J Bacteriol. Original short-filament (fraC) fragmentation mutant; operon
  context. Abstract/limited full text in cache.
- PMID:36470860 — SepN septal-junction plug component (FraD partner); background on the SJ machinery.
- PMID:42424141 — SepN-FraD structural module (cryoET). Background on the SJ; FraD-focused, not FraE.
