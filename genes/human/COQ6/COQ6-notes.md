# COQ6 (human) review notes

UniProt: Q9Y2Z9 (COQ6_HUMAN). HGNC:20233. Gene on chromosome 14. 468 aa precursor
with an N-terminal mitochondrial transit peptide (1..28); mature chain 29..468.

## Core biology

COQ6 is the mitochondrial **FAD-dependent (flavin) monooxygenase** of the UbiH/COQ6
family that carries out **aromatic-ring hydroxylation** steps of **coenzyme Q10
(ubiquinone) biosynthesis**.

- **C5-ring hydroxylation** (canonical, conserved across life): hydroxylation of
  4-hydroxy-3-(all-trans-decaprenyl)benzoate → 3,4-dihydroxy-5-(all-trans-decaprenyl)benzoate.
  EC 1.14.15.45; GO:0106364 (4-hydroxy-3-all-trans-polyprenylbenzoate oxygenase activity).
  [file:human/COQ6/COQ6-uniprot.txt "Required for the C5-ring hydroxylation during"]
  [PMID:38425362 "COQ6, a class A flavin-dependent monooxygenase, represents the first protein in the CoQ head group biosynthetic pathway and performs C5 hydroxylation"]
  [PMID:28927698 "The C5-hydroxylation is catalyzed by COQ6 in eukaryotes"]

- **C1-hydroxylation** (second, non-consecutive step; established in animals by
  Nicoll et al. 2024): hydroxylation of 2-methoxy-6-(all-trans-decaprenyl)phenol →
  2-methoxy-6-(all-trans-decaprenyl)benzene-1,4-diol. EC 1.14.15.46; GO:0120538
  (2-methoxy-6-polyprenolphenol 4-hydroxylase activity).
  [file:human/COQ6/COQ6-uniprot.txt "FAD-dependent monooxygenase required for two non-consecutive"]
  [PMID:38425362 "corroborating its dual functionality as both a C5 and C1 hydroxylase"]

Both reactions consume O2 and use electrons delivered from NAD(P)H via the
ferredoxin/ferredoxin-reductase couple **FDX2/FDXR** (not NAD(P)H directly).
[file:human/COQ6/COQ6-uniprot.txt "The electrons required for the hydroxylation"]
[PMID:38425362 "COQ6 activity, and the first reaction step in CoQ biosynthesis, is triggered by a coupled ferredoxin pair−FDXR and FDX2"]

Cofactor: **FAD**. [PMID:38425362 "Full-length COQ6 was purified as a flavin adenine dinucleotide (FAD)-bound protein"]
[file:human/COQ6/COQ6-uniprot.txt "Name=FAD"]

## Complex and localization

COQ6 is a component of the **COQ synthome / complex Q** (a.k.a. ubiquinone
biosynthesis complex, GO:0110142) on the matrix face of the mitochondrial inner
membrane, together with COQ3, COQ4, COQ5, COQ7, COQ9 (and organized by COQ8A/B).
[file:human/COQ6/COQ6-uniprot.txt "Component of a multi-subunit COQ enzyme complex, composed of"]
[PMID:27499296 "identify a dynamic human coenzyme Q biosynthetic complex that includes multiple MXPs"]
[PMID:28927698 "peripherally associated with the matrix face of the inner membrane"]

IntAct/UniProt binary interactions (PMID:27499296): COQ3 (Q9NZJ6), COQ4 (Q9Y3A0),
COQ5 (Q5HYK3), COQ7 (Q99807) — all partners within the same synthome, so the four
IPI "protein binding" annotations reflect intra-complex assembly, not an
informative stand-alone MF.

Subcellular location: mitochondrion inner membrane, peripheral membrane protein,
matrix side.
[file:human/COQ6/COQ6-uniprot.txt "Mitochondrion inner membrane"]
[file:human/COQ6/COQ6-uniprot.txt "Matrix side"]
The HAMAP rule also lists **Golgi apparatus** and **cell projection** ("Localizes
to cell processes and Golgi apparatus in podocytes"), a disease-cell-type
observation propagated by rule; these are non-core and IEA-only.
[file:human/COQ6/COQ6-uniprot.txt "Golgi apparatus"]
[file:human/COQ6/COQ6-uniprot.txt "Localizes to cell processes and Golgi apparatus in podocytes"]

## Disease

Biallelic loss-of-function causes **primary coenzyme Q10 deficiency-6 (COQ10D6,
MIM:614650)** — steroid-resistant nephrotic syndrome (focal segmental
glomerulosclerosis, end-stage renal failure) with **sensorineural deafness**.
[file:human/COQ6/COQ6-uniprot.txt "Coenzyme Q10 deficiency, primary, 6 (COQ10D6)"]
A germline missense (D208H) has additionally been linked to schwannomatosis
susceptibility.
[file:human/COQ6/COQ6-uniprot.txt "may play a role in susceptibility to"]

## Annotation review reasoning

- Two IDA MF terms (GO:0106364 C5-hydroxylase; GO:0120538 C1-hydroxylase) from
  PMID:38425362 are the **core molecular functions** — ACCEPT.
- FAD binding (GO:0071949) IEA is well supported experimentally (FAD-bound protein)
  and is a genuine cofactor-binding MF — ACCEPT; GO:0050660 (flavin adenine
  dinucleotide binding) is a near-synonymous/parent IEA, KEEP_AS_NON_CORE to avoid
  redundancy.
- Broad oxidoreductase MF parents (GO:0016491, GO:0016705, GO:0016712) are correct
  but less informative than the two specific hydroxylase terms — KEEP_AS_NON_CORE.
  GO:0004497 (monooxygenase activity) ARBA IEA is correct but generic —
  KEEP_AS_NON_CORE.
- ubiquinone biosynthetic process (GO:0006744) is core BP — ACCEPT the strongest
  (IDA PMID:38425362); the IBA/IEA/NAS duplicates KEEP_AS_NON_CORE.
- Localization: mitochondrion (GO:0005739) and mitochondrial inner membrane
  (GO:0005743) are correct core CC — ACCEPT the best-evidenced (IDA/IBA); Reactome
  TAS duplicates and HTP/other duplicates KEEP_AS_NON_CORE. extrinsic component of
  mitochondrial inner membrane (GO:0031314) captures the peripheral/matrix-side
  attachment — ACCEPT (informative). Golgi apparatus (GO:0005794) IEA is a
  rule-propagated podocyte observation — MARK_AS_OVER_ANNOTATED (do not treat as a
  core biosynthetic site).
- ubiquinone biosynthesis complex (GO:0110142, part_of, IPI PMID:27499296) — core
  CC of the synthome, ACCEPT.
- Four IPI GO:0005515 "protein binding" (COQ3/COQ4/COQ5/COQ7) collapse to a single
  seeded annotation — MARK_AS_OVER_ANNOTATED per policy (never REMOVE an IPI bare
  protein binding); the informative content is captured by the complex membership
  term.
</content>
</invoke>
