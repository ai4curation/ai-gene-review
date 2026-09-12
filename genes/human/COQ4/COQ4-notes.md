# COQ4 (human) — gene review notes

UniProt: Q9Y3A0 (COQ4_HUMAN). HGNC:19693. Gene ID 51117. Chromosome 9.
265 aa precursor; mitochondrial transit peptide 1–30; mature chain 31–265.

## Summary of function

COQ4 is a subunit of the mitochondrial coenzyme Q (ubiquinone) biosynthetic
complex ("COQ synthome" / COQ metabolon) that sits on the matrix face of the
inner mitochondrial membrane. It has two, non-exclusive roles that have both been
established experimentally:

1. **Structural/organizing role** — historically COQ4 was regarded as a scaffold
   that stabilizes the multi-subunit complex and is essential for its assembly and
   for CoQ biosynthesis. This is the classical view [PMID:18474229; PMID:27499296;
   PMID:28927698].

2. **Catalytic role (established 2024)** — two independent 2024 studies showed that
   COQ4 is itself a **Zn2+-dependent C1 decarboxylase** (EC 4.1.1.130) that
   catalyzes the oxidative/decarboxylation step at position C1 of the CoQ head
   group. This is now the RecName-linked activity in UniProt (GO:0120539,
   "4-hydroxy-3-methoxy-5-polyprenylbenzoate decarboxylase activity"), with IDA
   experimental support [PMID:38295803; PMID:38425362].

IMPORTANT: The older "non-catalytic scaffold only" framing has been superseded by
the 2024 catalytic evidence now captured in the UniProt entry. Both roles are real;
the catalytic decarboxylase activity is the current core molecular function.

## Location

- Mitochondrion inner membrane; peripheral membrane protein on the matrix side.
  [file:human/COQ4/COQ4-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"]
  ["Peripheral membrane protein; Matrix side."]
- Localizes to mitochondrion (LIFEdb GFP, HPA immunofluorescence, high-confidence
  mito proteome PMID:34800366).

## Complex membership (COQ synthome / metabolon)

- "Component of a multi-subunit COQ enzyme complex, composed of at least COQ3,
  COQ4, COQ5, COQ6, COQ7 and COQ9." [file:human/COQ4/COQ4-uniprot.txt]
  [PMID:27499296 "identified a dynamic human coenzyme Q biosynthetic complex that includes multiple MXPs"]
- ComplexPortal CPX-3642 "CoQ biosynthetic complex". GO:0110142 (ubiquinone
  biosynthesis complex) definition explicitly lists COQ3/4/5/6/7/9.
- Direct binary interactions (IntAct, from PMID:27499296): COQ3 (Q9NZJ6),
  COQ5 (Q5HYK3), COQ6 (Q9Y2Z9), COQ7 (Q99807). Also MAGEA2B (P43356) from the
  binary interactome map [PMID:32296183].
- COQ5 paper describes the assembly as the "CoQ-synthome" whose stability requires
  each Coq polypeptide [PMID:25152161 "assemble with the multi-subunit complex termed the CoQ-synthome"].

## Catalytic activity — detail

- Reaction (UniProt / Rhea RHEA:81275): 4-hydroxy-3-methoxy-5-(all-trans-
  decaprenyl)benzoate + H+ = 2-methoxy-6-(all-trans-decaprenyl)phenol + CO2;
  EC=4.1.1.130.
- Cofactor: Zn(2+). Zn-binding residues 163, 164, 167, 179 (canonical HD-xx-H-(x)11-E
  motif). [file:human/COQ4/COQ4-uniprot.txt "COFACTOR: Name=Zn(2+)"]
- PMID:38425362 (Nat Catal, full text): reconstructed the whole animal COQ metabolon
  in vitro. "COQ4 is the only system that possesses a canonical Zn-binding motif...
  we found that COQ4 exercised decarboxylase activity and production of 4a...
  These findings attest to COQ4's role as the C1 decarboxylase in CoQ biosynthesis."
  Zn dependency shown (EC50 2.4 µM ZnCl2; abolished by EDTA; metal-site mutants
  H142A-H146A and D143A-E158A inactive — numbering in the truncated ancestral
  construct, corresponding to human 163/164/167/etc).
- PMID:38295803 (Mol Cell, abstract only in cache): "these two reactions occur in a
  single oxidative decarboxylation step catalyzed by COQ4... COQ4 complements an
  Escherichia coli strain deficient for C1 decarboxylation and hydroxylation and
  that COQ4 displays oxidative decarboxylation activity in the non-CoQ producer
  Corynebacterium glutamicum... COQ4 contributes to CoQ biosynthesis, not only via
  its previously proposed structural role but also via the oxidative decarboxylation
  of CoQ precursors."
- Note the two 2024 papers differ on the C1 *hydroxylation* step: PMID:38295803
  proposes COQ4 mediates a combined oxidative decarboxylation (decarb+hydroxyl in one
  step), whereas PMID:38425362 assigns the separate C1 hydroxylation to COQ6 and
  restricts COQ4 to decarboxylation. UniProt CAUTION notes this. Either way COQ4 =
  the C1 decarboxylase; GO:0120539 (decarboxylase) is the appropriate MF.
- Zn-binding mutagenesis: "HDMLH->ADMLA: Abolished zinc-binding." and "D->A:
  Abolished zinc-binding... Abolished zinc-binding and ability to promote formation
  of ubiquinone." [file:human/COQ4/COQ4-uniprot.txt] — links the metal site to
  ubiquinone production.

## Biological process / requirement

- "Functional characterization of human COQ4, a gene required for coenzyme Q10
  biosynthesis" [PMID:18474229 title] — establishes requirement for CoQ10 synthesis.
- Loss-of-function COQ4 variants reduce ubiquinone biosynthesis: patient fibroblasts
  and knockout complementation lines show "lower ubiquinone biosynthesis"
  [PMID:38014483 "decreased mitochondrial membrane potential, and lower ubiquinone biosynthesis"];
  IMP annotation to GO:0006744.
- Leigh syndrome patient with G124S: "levels of CoQ10 ... were clearly lower in
  cultured fibroblasts derived from the patient" [PMID:30659264]; IMP to GO:0006744.

## Disease

- Primary coenzyme Q10 deficiency-7 (COQ10D7; MIM:616276): autosomal recessive;
  decreased CoQ10, severe cardiac or neurologic symptoms soon after birth
  [file:human/COQ4/COQ4-uniprot.txt "Coenzyme Q10 deficiency, primary, 7 (COQ10D7)"].
  Broad spectrum described in PMID:25658047.
- Spastic ataxia 10, autosomal recessive (SPAX10; MIM:620666): lower-limb
  spasticity, generalized ataxia [file:human/COQ4/COQ4-uniprot.txt "Spastic ataxia 10"].
- HSP phenotype confirmed by biallelic variants [PMID:38014483].

## Post-translational modification

- Phosphoserine at Ser-108 (large-scale phosphoproteomics) [PMID:23186163].

## Annotation review decisions (see COQ4-ai-review.yaml)

- Catalytic decarboxylase MF (GO:0120539): ACCEPT the IDA annotations (2024 primary
  evidence). IBA/IEA/TAS versions KEEP_AS_NON_CORE or ACCEPT (consistent, redundant).
- ubiquinone biosynthetic process (GO:0006744): core BP; ACCEPT the strongest
  (IDA/IMP) versions; others consistent.
- zinc ion binding (GO:0008270, IEA): ACCEPT — genuinely supported cofactor
  (Zn2+ in UniProt with experimental FT BINDING sites and 2024 metal-dependence data).
- carboxy-lyase activity (GO:0016831, IEA): parent of GO:0120539; ACCEPT as a
  correct-but-general ancestor (non-core; the specific term is the core).
- Complex/location terms (GO:0110142, GO:0005743, GO:0031314, GO:0005739,
  GO:0032991): ACCEPT/KEEP_AS_NON_CORE as appropriate. GO:0032991 (protein-containing
  complex) is a generic ancestor of GO:0110142 → MARK as over-general (KEEP_AS_NON_CORE).
- protein binding (GO:0005515, IPI): the four PMID:27499296 IntAct entries capture
  COQ3/5/6/7 co-complex partners (real synthome interactions) → MARK_AS_OVER_ANNOTATED
  (uninformative bare term; better modeled as complex membership). PMID:32296183
  (MAGEA2B) and PMID:25152161 (COQ5) IPIs likewise MARK_AS_OVER_ANNOTATED.
- Do NOT REMOVE any experimental annotations. IEA carboxy-lyase and the redundant
  Reactome location TAS entries are all biologically defensible → keep.
