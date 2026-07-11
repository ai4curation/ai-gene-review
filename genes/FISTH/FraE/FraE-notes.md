# FraE research notes (Fischerella thermalis JSC-11)

Gene: **fraE** ortholog, ordered locus **FJSC11DRAFT_2569**, *Fischerella thermalis* JSC-11
(Stigonematales; true-branching, heterocyst-forming cyanobacterium).
UniProt: **G6FUM2** (G6FUM2_9CYAN, unreviewed/TrEMBL), 259 aa, PE=4 (Predicted).
Taxon: NCBITaxon:741277. RefSeq WP_009457248.1; EMBL EHC12952.1; AlphaFoldDB G6FUM2.

## Summary

G6FUM2 is the **FraE ortholog** in *Fischerella thermalis* JSC-11 of the well-studied *Nostoc*
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

*Fischerella thermalis* belongs to the Stigonematales (true-branching cyanobacteria), a
deep-branching heterocystous lineage more distant from *Nostoc/Anabaena* than the other FraE
orthologs reviewed here (*N. punctiforme*, *A. variabilis*). The conserved fraC-fraD-fraE operon
reaching this lineage is consistent with the SepN discovery paper's report that the
septal-junction machinery spans Nostocaceae, Oscillatoriales and Stigonematales
[PMID:36470860]. Functional inference for G6FUM2 is transferred by orthology (ISS) to PCC 7120 FraE.

## Orthology evidence

The FraE ortholog assignment for G6FUM2 rests on reciprocal-best-hit homology plus conserved
operon synteny (a module genome scan; modules/septal_junction/RESULTS.md):

- **Homology (RBH)**: G6FUM2 is the reciprocal best hit of PCC 7120 FraE (A0ACD7RSN5), forward
  E = 1.3e-101, 65.0% identity — G6FUM2 is the reciprocal best-scoring FraE match in
  *F. thermalis* JSC-11.
- **Protein family (broad, non-diagnostic on its own)**: InterPro **IPR032688** "ABC-2 type
  transporter permease protein NosY-like"; Pfam **PF12679** "ABC-2 family transporter protein"
  (ABC2_membrane_2); PANTHER **PTHR43471** "ABC Transporter Permease" (subfamily PTHR43471:SF10,
  SLL1107 protein). This ABC-2 permease family is broad and present across cyanobacteria, so
  family membership alone does not discriminate the true FraE ortholog.
- **Conserved operon synteny (the decisive evidence)**: the FraC/FraD/FraE best hits carry
  consecutive accessions in *F. thermalis* — **FJSC11DRAFT_2571 (fraC, G6FUM4) – 2570 (fraD,
  G6FUM3) – 2569 (fraE, G6FUM2)** — reproducing the intact, syntenic fraC-fraD-fraE operon.
  Because the ABC-2 family is non-diagnostic, this conserved operon context is the key evidence
  that G6FUM2 is the true FraE ortholog rather than an unrelated ABC-2 permease paralog. In the
  same scan all six septal-junction components were detected reciprocal in *F. thermalis*
  (48–66% identity): FraD G6FUM3, FraC G6FUM4, FraE G6FUM2, SepN G6FVY1, SepJ G6FMI5, AmiC G6FW05.

Provenance sentence (quotable): G6FUM2 is the FraE ortholog of Nostoc sp. PCC 7120 FraE
(A0ACD7RSN5) by reciprocal-best-hit phmmer homology (forward E = 1.3e-101, 65.0% identity) and
by conserved operon synteny of the fraC-fraD-fraE operon (FJSC11DRAFT_2571/2570/2569, i.e.
G6FUM4-G6FUM3-G6FUM2 in F. thermalis).

## Protein family / domain architecture

G6FUM2 is an integral-membrane **ABC-2-type transporter permease-family** protein (NosY-like),
i.e. the membrane permease component, NOT the ATP-hydrolyzing (nucleotide-binding) ATPase subunit.
UniProt/Phobius predicts six transmembrane helices (residues 21-40, 52-76, 103-124, 130-146,
153-177, 236-254), consistent with a polytopic integral membrane permease. A permease component
of an ABC transporter provides the transmembrane translocation pathway but does not itself
hydrolyze ATP; full "ABC-type transporter activity" (ATP-coupled primary active transport) is a
property of the complete transporter (permease + nucleotide-binding domain), not of the permease
subunit alone.

Provenance for the family assignment used in this review:
G6FUM2 (FraE ortholog, FJSC11DRAFT_2569) is classified by InterPro as IPR032688 "ABC-2 type
transporter permease protein NosY-like" (Pfam PF12679; PANTHER PTHR43471), i.e. an
integral-membrane ABC-2-type transporter permease-family protein that is the permease (not
ATPase) component.

## Caveats / knowledge gaps

- G6FUM2 is the *F. thermalis* ortholog of the least-characterized member of the fraC-fraD-fraE
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
- PMID:36470860 — Weiss et al. 2022. Reports the septal-junction machinery (SepN) across
  Nostocaceae, Oscillatoriales and Stigonematales; contextual for the operon reaching *Fischerella*.
- file:FISTH/FraE/FraE-notes.md — these notes (orthology evidence, family assignment, provenance).
