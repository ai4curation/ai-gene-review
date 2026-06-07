# CRTAP (Cartilage-associated protein) — review notes

UniProt: O75718 (CRTAP_HUMAN), 401 aa precursor; gene CRTAP (synonym CASP); chr 3.
HGNC:2379. Member of the leprecan family (SIM, UniProt). Signal peptide 1-26;
secreted/ER-resident glycoprotein (N-glyc at 87, 363).

## Core biology

CRTAP is a non-catalytic, essential component of the endoplasmic reticulum
collagen prolyl 3-hydroxylation complex, together with prolyl 3-hydroxylase 1
(P3H1/LEPRE1, UniProt Q32P28) and cyclophilin B / peptidyl-prolyl isomerase B
(PPIB/CyPB). This ternary complex 3-hydroxylates a single specific proline,
Pro986, of the α1(I) and α1(II) fibrillar (pro)collagen chains in the ER lumen.
- [PMID:19846465 "CRTAP and P3H1 form a complex with cyclophilin B (CyPB) in the
  endoplasmic reticulum (ER) which 3-hydroxylates the Pro986 residue of alpha1(I)
  and alpha1(II) collagen chains."]
- [PMID:20089953 "the collagen prolyl 3-hydroxylation complex, consisting of P3H1
  ... CRTAP, and CyPB, modifies the α1(I)Pro986 residue."]

P3H1 carries the catalytic prolyl 3-hydroxylase activity and is the only complex
member with a KDEL ER-retrieval signal; CRTAP acts as the "helper protein" /
non-catalytic subunit, NOT the catalytic hydroxylase.
- [PMID:19846465 "P3H1 ... contains the enzymatic activity of the complex and is
  the only complex component with a KDEL ER-retrieval signal ... CRTAP ... acts as
  the helper protein of the complex."]

## Mutual stabilization & chaperone role

CRTAP and P3H1 mutually stabilize each other in the ER: a null mutation in one
gene causes loss/reduction of BOTH proteins despite normal transcript levels of
the non-mutated gene. Proteasome inhibition partially rescues P3H1 in CRTAP-null
cells, indicating destabilized partner is degraded.
- [PMID:19846465 "a null mutation for one of these proteins results in absence or
  substantial decrease of both proteins ... despite normal levels of transcript ...
  These data indicate that CRTAP and P3H1 are mutually stabilized in the collagen
  prolyl 3-hydroxylation complex."]
- [PMID:19846465 "Proteasomal inhibitors partially rescue P3H1 protein in
  CRTAP-null cells."]

The complex also functions as a collagen chaperone/foldase: loss of P3H1 or CRTAP
delays collagen helix folding, causing overmodification (excess 4-hydroxylation /
lysyl hydroxylation) of the helical region. The complex has classical chaperone
activity in vitro (inhibits citrate synthase aggregation, rhodanese refolding) and
modulates collagen fibril formation.
- [PMID:19846465 "The prolyl 3-hydroxylation complex has recently been reported ...
  to function as a chaperone in both classical chaperone assays inhibiting citrate
  synthase aggregation and rhodanese refolding and aggregation, as well as in a
  fibril formation assay of type I collagen ... the complex also has a general
  function to assist protein folding."]
- [PMID:20089953 "In the absence of P3H1 or CRTAP, α1(I)Pro986 3-hydroxylation is
  decreased and collagen folding is delayed, resulting in overmodification of the
  helical lysine and proline residues."]

Note (negative regulation of PTM): the IMP annotation GO:1901874 "negative
regulation of post-translational protein modification" reflects that the complex
LIMITS overmodification by P4H/LH — i.e., its absence causes overmodification.
This is an indirect/consequential phenotype of the chaperone/foldase role, not a
direct enzymatic activity of CRTAP. Best regarded as non-core.

## Subcellular location

Primary functional location is the ER lumen. Endogenous CRTAP detected in ER by
IDA (PMID:19846465, PMID:20089953). A minor fraction is secreted to the
extracellular space/matrix: in normal cells ~10-12% of CRTAP is secreted, rising
to 15-20% in LEPRE1-null cells (because P3H1's KDEL normally retains CRTAP).
- [PMID:19846465 "in conditioned media from control cells ... about 10-12% of
  total CRTAP is secreted ... in LEPRE1-null cells, P3H1 is not present to retain
  CRTAP in the ER, and the proportion of CRTAP secreted ... is more than tripled,
  accounting for 15-20%"]
The UniProt SUBCELLULAR LOCATION line lists "Secreted, extracellular space,
extracellular matrix" (by similarity, ECO:0000250); the dominant biology is ER.

## Structure

Cryo-EM structures of the human P3H1/CRTAP/PPIB ternary complex (PDB 8K0E, 8K0F,
8K0I, 8K0M, 8K17, 8KC9). The active sites of P3H1 and PPIB form a face-to-face
bifunctional reaction center; the complex binds collagen peptide across multiple
sites forming a "substrate interacting zone"; a dual-ternary state is observed.
CRTAP is a TPR-like α-helical (leprecan-domain) scaffold subunit.
- [PMID:39245686 "We determine cryo-EM structures of the P3H1/CRTAP/PPIB complex.
  The active sites of P3H1 and PPIB form a face-to-face bifunctional reaction
  center ... The structure of the P3H1/CRTAP/PPIB/collagen peptide complex reveals
  multiple binding sites, suggesting a substrate interacting zone."]

## Disease

Biallelic loss-of-function CRTAP variants cause autosomal recessive osteogenesis
imperfecta type VII (OI7, MIM:610682), a severe-to-lethal bone dysplasia with
rhizomelia, overmodified type I collagen, reduced bone mass, fractures.
- [PMID:17055431 "CRTAP is required for prolyl 3-hydroxylation and mutations cause
  recessive osteogenesis imperfecta." (title; UniProt FUNCTION + DISEASE)]
- UniProt DISEASE: OI7 autosomal recessive (ECO:0000269|PubMed:17055431,
  18566967, 19550437, 21955071).
Crtap-knockout mice have recessive osteochondrodystrophy with loss of prolyl
3-hydroxylation in cartilage and bone.
- [PMID:19846465 "Crtap knock-out mice have a recessive osteochondrodystrophy
  associated with lack of the prolyl 3-hydroxylation modification in cartilage and
  bone."]

## Interaction evidence supporting "protein binding" (GO:0005515) IPI annotations

All three IPI GO:0005515 annotations (PMID:30021884, PMID:33961781, PMID:39245686)
use WITH/FROM UniProtKB:Q32P28 = P3H1, i.e. they capture the CRTAP–P3H1
interaction. PMID:39245686 (cryo-EM ternary complex) is direct, specific
structural evidence; PMID:33961781 (BioPlex affinity-MS interactome) and
PMID:30021884 (XL-MS) are high-throughput. Bare "protein binding" is
uninformative; the meaningful, specific statement is membership in the
P3H1/CRTAP/PPIB complex.

## Annotation assessment summary

- GO:0005518 collagen binding (IBA, contributes_to): the complex binds collagen
  substrate; CRTAP contributes to substrate binding within the complex (substrate
  interacting zone, PMID:39245686). Supportable as contributes_to; keep
  non-core (it is the complex, not CRTAP alone, that binds — but reasonable).
- GO:0005783 endoplasmic reticulum (multiple IBA/IEA/IDA): well supported, core
  location. ACCEPT IDA; IBA/IEA redundant but correct.
- GO:0005788 endoplasmic reticulum lumen (TAS Reactome x4): more precise than ER;
  correct. ACCEPT (one representative); others redundant.
- GO:0030199 collagen fibril organization (IBA): supported (chaperone modulates
  fibril formation; OI collagen disorganized). Keep non-core / accept.
- GO:0005515 protein binding (IPI x3): bare term — MARK_AS_OVER_ANNOTATED; the
  specific content is P3H1 binding / complex membership.
- GO:0005783 IEA (GO_REF:0000120) — redundant with IDA, over-annotated/non-core.
- GO:0007283 spermatogenesis (IEA, Ensembl from mouse): broad ortholog transfer,
  no human evidence; MARK_AS_OVER_ANNOTATED / non-core.
- GO:0050821 protein stabilization (IMP, PMID:19846465): supported — CRTAP
  stabilizes P3H1 (mutual stabilization). ACCEPT, but specific to complex partner.
- GO:0006457 protein folding (ISS): supported (complex is collagen chaperone).
  Keep; could be more specific (protein folding in ER / chaperone).
- GO:0032991 protein-containing complex (ISS): correct but generic; the specific
  complex is the prolyl 3-hydroxylase / collagen-modifying complex. MODIFY toward
  more specific if available, else keep non-core.
- GO:0005576 extracellular region (IDA, PMID:19846465): a minor secreted fraction
  is real but the dominant biology is ER; KEEP_AS_NON_CORE.
- GO:1901874 negative regulation of post-translational protein modification (IMP):
  indirect consequence (loss → overmodification); KEEP_AS_NON_CORE.
</content>
</invoke>
