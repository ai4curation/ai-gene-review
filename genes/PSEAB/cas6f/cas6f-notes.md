# cas6f / Csy4 (Q02MM2) — Pseudomonas aeruginosa UCBPP-PA14 — curation notes

Deep research was unavailable in this environment (no provider API keys), so this
file is my own literature journal. Every assertion carries an inline PMID plus a
verbatim quote from the cached record in `publications/`.

## System context

PA14 carries a type I-F (Yersinia-subtype, "Csy") CRISPR-Cas system at
PA14_33300–PA14_33350: `cas6f`/`csy4`, `csy3`, `csy2`, `csy1`, `cas2-3` (annotated
`cas3`), `cas1`, flanked by two CRISPR arrays. Unusually for type I, Cas2 is not a
separate protein: [PMID:26586803 "A specific feature of type I-F systems is a fusion of
cas2 and cas3 homologs, which are encoded on separate genes in other CRISPR"].

The interference effector is the Csy surveillance complex:
[PMID:32170016 "The Csy complex is comprised of four types of Cas proteins (Cas5f-8f)
and a single 60-nt crRNA"], arranged as
[PMID:32170016 "the maps exhibit an asymmetric spiral, with one Cas6f subunit in the
head, one Cas5f and one Cas8f in the tail, and six Cas7f comprising the spiral
backbone"]. In the PA14 nomenclature Cas8f = Csy1, Cas5f = Csy2, Cas7f = Csy3,
Cas6f = Csy4. This matches UniProt's stoichiometry
`Csy1(1),Csy2(1),Csy3(6),Cas6/Csy4(1)-crRNA(1)` and the original biochemistry
[PMID:21536913 "the Csy proteins (Csy1-4) assemble into a 350 kDa ribonucleoprotein
complex that facilitates target recognition by enhancing sequence-specific
hybridization between the CRISPR RNA and complementary target sequences"].

This is the host side of the anti-CRISPR system reviewed in
`genes/BPZF4/AcrF8/AcrF8-ai-review.yaml`: AcrIF8 binds the Cas7f (Csy3) backbone and
the crRNA; AcrIF3 sequesters Cas3.

## Cas6f/Csy4 is the pre-crRNA endoribonuclease

Csy4 is the enzyme that makes mature crRNA:
[PMID:20829488 "we concluded that Csy4 is the endoribonuclease responsible for crRNA
biogenesis"]. The substrate is RNA, not DNA, and catalysis is metal-independent:
[PMID:20829488 "CRISPR transcript cleavage is a rapid, metal ion-independent reaction"].
Independently confirmed: [PMID:22522703 "crRNA biogenesis requires the endoribonuclease
Csy4, which binds and cleaves the repetitive sequence of the CRISPR transcript"].

Recognition is sequence- and structure-specific for the repeat hairpin:
[PMID:20829488 "the protein makes extensive interactions with the ssRNA-dsRNA junction
at the base of the crRNA stem as well as with the major groove of the RNA hairpin"].
Catalysis uses a Ser/His dyad; the catalytic residues are separable from binding:
[PMID:20829488 "Mutations of His 29 or Ser 148 (to alanine and cysteine, respectively)
completely abolished cleavage activity without disrupting RNA binding"]. That last
result is the cleanest evidence that Csy4 has **two separable activities** — RNA
endonuclease and high-affinity crRNA binding.

## Dual role: enzyme and retained complex subunit

Like E. coli Cas6e/CasE, Csy4 does not release its product:
[PMID:22522703 "Considering that Csy4 recognizes a single cellular substrate and
sequesters the cleavage product"], and this retention is what builds the effector:
[PMID:22522703 "We show that this RNA cleavage step is essential for assembly of the
Csy protein-crRNA complex that facilitates target recognition"]. Structurally it sits
at the PAM-distal head on the crRNA 3' hairpin
[PMID:28985564 "Cas6f is located at the 3′ stem-loop of the crRNA, Cas8f and Cas5f are
located at the 5′ handle of crRNA, and six interlocking copies of Cas7f are located
along the length of the crRNA spacer"]. The IntAct
interaction behind GOA's two `GO:0005515` rows is Csy4–Csy3 (Q02MM2–Q02MM1, NbExp=12),
i.e. the head-to-backbone contact of this same complex.

## In vivo requirement

Loss of Csy4 abolishes crRNA:
[PMID:21398535 "proteins Csy4 and Csy2 are essential for small CRISPR RNA (crRNA)
production in vivo, while the Csy1 and Csy3 proteins are not absolutely required for
production of these small RNAs"]. The catalytic residue is required for spacer
acquisition as well as interference:
[PMID:26586803 "Deleting the csy3 gene (lane 6), or mutating the catalytic residue
His29 of Csy4 nuclease (lane 7) that is needed for generation of mature crRNA also
abolished spacer acquisition"] — the adaptation defect is downstream of the crRNA
defect, since [PMID:26586803 "both modes require, in addition to Cas1 and Cas2, intact
Csy complex, an ortholog of the E. coli Cascade, and crRNA"].

## Curation decisions

- `GO:0004519 endonuclease activity` (IEA, InterPro IPR013396) is the correct branch
  but one level too general. The substrate is RNA and the measurement is direct, so
  `GO:0004521 RNA endonuclease activity` is better supported. **Comparator check:** the
  type I-E counterpart Cas6e/CasE (Q46897) carries exactly `GO:0004521` by IDA from
  PMID:18703739 (`genes/ECOLI/casE/casE-goa.tsv`). So the specific term is the
  convention for this family, and PA14 Cas6f is simply lagging. → MODIFY.
- Both `GO:0005515 protein binding` rows are uninformative per project policy. The
  Csy4–Csy3 IPI samples a contact internal to the Csy complex: Cas6f clamps the crRNA
  3' stem-loop at the PAM-distal head and abuts the Cas7f backbone from there, and
  because it never releases the product it cleaved, that clamp nucleates the whole
  assembly. → MODIFY both to `GO:0005198 structural molecule activity`.

  **Aspect correction (follow-up).** My first pass proposed
  `part_of GO:0032991 protein-containing complex` as the replacement, reasoning from the
  E. coli comparator where all five Cascade subunits carry exactly that. That was wrong
  in form: these GOA rows carry `qualifier: enables`, so they are molecular-function
  rows, and a gene product cannot *enable* a cellular component. However
  well-supported complex membership is, it cannot be expressed by swapping a CC term
  into an `enables` MF row. The E. coli reviews were not making this mistake — their
  GOA already contained separate `part_of GO:0032991` rows, which they MODIFY to
  `GO:1990904`; their `enables GO:0005515` rows went to `GO:0005198` instead.
  Reconciled to the same convention:

  - **MODIFY the `enables` rows to `GO:0005198 structural molecule activity`** ("the
    action of a molecule that contributes to the structural integrity of a complex").
    Aspect-correct, and none of its 22 children fits a non-ribosomal ribonucleoprotein,
    so the parent is the right level. Each row is backed by the verbatim structural
    quote naming the contact this subunit actually makes.
  - **Carry complex membership on its own `NEW part_of GO:1990904 ribonucleoprotein
    complex` row.** PA14 has no `part_of` complex row for any Csy subunit, unlike all
    five E. coli Cascade subunits, so this is a real missing annotation rather than a
    reformulation. `GO:1990904` rather than the bare `GO:0032991` root because the
    60-nt crRNA is an integral component, not a ligand.
  - **`core_functions[].in_complex` → `GO:1990904`** for the same reason.
  - **Added a `proposed_new_terms` entry** for a "CRISPR RNA-guided surveillance
    complex" CC term under `GO:1990904`, identical in substance to the one the five
    E. coli Cascade reviews carry, so the two systems request one term rather than two.
    GO's entire CRISPR vocabulary is five BP terms (`GO:0099048`, `GO:0043571`,
    `GO:0098672` and the obsolete `GO:0110132`/`GO:0110133`); ComplexPortal models the
    type I-E complex as CPX-1005, GO does not.
- `GO:0043571 maintenance of CRISPR repeat elements` — both the IEA and the CACAO IMP
  are right. The term's definition explicitly includes "transcription of the CRISPR
  repeat arrays into RNA and processing" and "capture of new spacer elements", which is
  precisely what Csy4 does and what the H29A phenotype shows. → ACCEPT both.

## Gaps identified (missing annotations)

- `GO:0003723 RNA binding` — held by all five E. coli Cascade subunits by IDA; here it
  is separately demonstrated from catalysis by the H29A/S148C result. → NEW.
- `GO:0099048 CRISPR-cas system` — held by all five E. coli Cascade subunits by IDA
  (PMID:18703739). Not an ancestor or descendant of `GO:0043571` or `GO:0051607`
  (checked via QuickGO ancestors), so not redundant. Csy4 performs the crRNA-biogenesis
  stage named in the term's own definition. → NEW.
- No molecular-function term exists for crRNA-guided target recognition, the activity
  the assembled Csy complex actually has. This is recorded as an open ontology gap in
  `modules/crispr_cas_adaptive_immunity.yaml` and I have not substituted an ill-fitting
  id; raised in `suggested_questions` instead.
- Not proposed: `GO:0051607 defense response to virus`. The PA14 native array's
  antiviral role is contested in the primary literature
  [PMID:21398535 "the Yersinia-subtype CRISPR region of Pseudomonas aeruginosa strain
  UCBPP-PA14 plays no detectable role in viral immunity but instead is required for
  bacteriophage DMS3-dependent inhibition of biofilm formation"] versus
  [PMID:23242138 "The CRISPR-sensitive phages fail to replicate on PA14 due to the
  action of the CRISPR/Cas system14, but are able to replicate on PA14"] (ΔCR/cas).
  The second is a whole-locus deletion, not a `cas6f` allele, so there is no
  gene-specific antiviral evidence to annotate. `GO:0099048` already carries the
  immunity role without over-claiming.
- Deliberately not annotated: the use of Csy4 as a laboratory RNA-processing reagent.
  That is a biotechnology application, not a function of the gene in its host.
