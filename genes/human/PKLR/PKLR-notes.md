# PKLR (human) review notes

UniProtKB: P30613 (KPYR_HUMAN). HGNC:9020. Gene: PKLR (synonyms PK1, PKL).
No falcon deep-research file (falcon out of credits, HTTP 402). Review grounded in
`PKLR-uniprot.txt`, `PKLR-goa.tsv`, and cached `publications/PMID_*.md`.

## Core biology (from UniProt + literature)

- PKLR encodes the **L (liver) and R (red-blood-cell) isozymes** of pyruvate kinase,
  produced by alternative promoters/splicing of a single gene (exon 1 = R mRNA, exon 2 =
  L mRNA) [PMID:1445295]. The separate **PKM** gene encodes the M1/M2 isozymes.
  UniProt MISCELLANEOUS: "There are 4 isozymes of pyruvate kinase in mammals: L, R, M1
  and M2. L type is major isozyme in the liver, R is found in red cells, M1 is the main
  form in muscle, heart and brain, and M2 is found in early fetal tissues."
- **Reaction (EC 2.7.1.40):** phosphoenolpyruvate (PEP) + ADP → pyruvate + ATP; the
  final, essentially irreversible, second ATP-generating step of glycolysis
  (glycolysis step 5/5, pyruvate from D-glyceraldehyde 3-phosphate; UniPathway UPA00109).
  UniProt CATALYTIC ACTIVITY: "Reaction=pyruvate + ATP = phosphoenolpyruvate + ADP + H(+)".
  FUNCTION: "Pyruvate kinase that catalyzes the conversion of phosphoenolpyruvate to
  pyruvate with the synthesis of ATP, and which plays a key role in glycolysis
  (PubMed:11960989)." [PMID:11960989]
- **Cofactors:** Mg2+ (or Mn2+ in vitro) and K+ required. UniProt COFACTOR lists Mg(2+),
  Mn(2+), K(+). Crystal structure (2VGB/2VGF, 2.73 A) solved with K+ and Mn2+ ions;
  K+ binding residues 118/120/156/157, Mn2+ (catalytic divalent) at 315/339 [PMID:11960989].
  GO magnesium ion binding GO:0000287 and potassium ion binding GO:0030955 (IEA/InterPro)
  are structurally supported.
- **Allosteric regulation:** activated by fructose 1,6-bisphosphate (feed-forward);
  FBP-binding residues 475-480, 525, 532, 559-564 [PMID:11960989]. UniProt ACTIVITY
  REGULATION: "Allosterically activated by fructose 1,6-bisphosphate." Homotetramer
  (UniProt SUBUNIT). Liver isoform additionally inhibited by phosphorylation
  (glucagon/PKA) and by ATP/alanine (classic biochemistry).
- **Side reaction / metabolite repair:** also produces the side product 2-phospholactate
  ((S)-lactate + ATP = (2S)-2-phospholactate + ADP + H+), removed by PGP [PMID:27294321].
  (PMID:27294321 not cached; UniProt-only, so not used as a supporting_text.)
- **Structure:** 574 aa homotetramer; classic PK fold (Pfam PK PF00224 + PK_C PF02887;
  InterPro IPR001697). Many X-ray structures (2VGB, 4IMA, 6NN4, etc.).

## Disease

- **CNSHA2 / pyruvate kinase deficiency** (MIM:266200): autosomal recessive; most common
  glycolytic-enzyme cause of hereditary nonspherocytic hemolytic anemia. Mature
  erythrocytes lack mitochondria and depend entirely on glycolytic ATP, so RPK loss is
  hemolytic. Dozens of CNSHA2 missense variants in UniProt. [PMID:11960989] abstract:
  "Deficiency of human erythrocyte isozyme (RPK) is, together with glucose-6-phosphate
  dehydrogenase deficiency, the most common cause of the nonspherocytic hemolytic anemia."
- **PKHYP** (MIM:102900): autosomal dominant increase of RBC ATP (variant K37Q/G37E)
  [PMID:9090535].
- Drug: mitapivat (PK activator) approved for PK deficiency (UniProt DrugBank DB16236).

## Annotation review decisions (summary)

Core, accepted:
- GO:0004743 pyruvate kinase activity — multiple EXP/TAS/IBA/IEA; core MF. ACCEPT all.
- GO:0006096 glycolytic process — IBA + IEA; core BP. ACCEPT.
- GO:0005829 cytosol — TAS Reactome; correct cellular location. ACCEPT.
- GO:0000287 magnesium ion binding (IEA/InterPro) — structurally supported cofactor. ACCEPT.
- GO:0030955 potassium ion binding (IEA/InterPro) — structurally supported cofactor. ACCEPT.
- GO:0005737 cytoplasm (IBA) — correct but general; cytosol is the informative term. KEEP_AS_NON_CORE.

Accepted non-core / kept:
- GO:0042866 pyruvate biosynthetic process (TAS Reactome, IEA) — pyruvate is the product;
  acceptable framing of the same reaction. KEEP_AS_NON_CORE.
- GO:0061621 canonical glycolysis (TAS Reactome) — more specific glycolysis term; ACCEPT.
- GO:0070062 extracellular exosome (HDA) — high-throughput proteomics localization; a
  common HDA finding for abundant cytosolic enzymes, not a functional site. KEEP_AS_NON_CORE.

Over-annotations (kept, flagged):
- GO:0005515 protein binding (IPI, HuRI Y2H hit vs CPNE7, Q9UBL6-2) — bare protein binding,
  uninformative, single large-scale Y2H. MARK_AS_OVER_ANNOTATED (policy: not REMOVE).
- GO:0032869 cellular response to insulin stimulus (IBA + IEA) — regulatory/physiological
  context transferred from rat ortholog; not PKLR's molecular function. MARK_AS_OVER_ANNOTATED.
- GO:0048029 monosaccharide binding (IEA/Ensembl from rat) — over-broad; FBP is a
  bisphosphorylated sugar allosteric activator, but "monosaccharide binding" is a
  misleading generalization of that. MARK_AS_OVER_ANNOTATED.

IEA physiological-response transfers from the rat ortholog (P12928) via GO_REF:0000107
(Ensembl Compara orthology projection) — these describe regulation of the liver enzyme's
expression/activity by hormones/nutrients, not PKLR's own molecular activity. Keep as
non-core where biologically plausible:
- GO:0001666 response to hypoxia — KEEP_AS_NON_CORE
- GO:0007584 response to nutrient — KEEP_AS_NON_CORE
- GO:0009749 response to glucose — KEEP_AS_NON_CORE
- GO:0010038 response to metal ion — KEEP_AS_NON_CORE (Mg/K/Mn are cofactors; plausible)
- GO:0033198 response to ATP — KEEP_AS_NON_CORE (ATP is substrate/product + inhibitor)
- GO:0051591 response to cAMP — KEEP_AS_NON_CORE (glucagon/PKA regulation of L isoform)
- GO:0071872 cellular response to epinephrine stimulus — KEEP_AS_NON_CORE

## Reference notes

- PMID:15996096 is a structure paper on **PKM2** (the PKM gene isozyme), used by Reactome
  to support GO:0004743 for PKLR by family analogy. Per curation policy, EXP annotation is
  not removed on abstract-only grounds; the M2/R isozymes share the catalytic mechanism.
  ACCEPT the pyruvate kinase activity annotation; flag the reference relevance as MEDIUM.
- PMID:19056867 (urinary exosome proteomics) supports the HDA extracellular exosome
  localization; PKLR is not named in the cached abstract (large proteome list). Kept
  non-core; reference is LOW relevance to core function.
</content>
</invoke>
