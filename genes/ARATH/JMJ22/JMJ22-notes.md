# JMJ22 (At5g06550, Q67XX3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: JMJ22 is the experimentally characterised relative used as the transfer reference
for wheat A0A3B6RKV1 (same PANTHER subfamily PTHR12480:SF21, same PAINT node PTN001753861,
of which JMJ22 is the IBD donor). This review evaluates JMJ22 in its own right. No ProtNLM2
output was opened or used.

### Deep research

`just deep-research-falcon ARATH JMJ22 --fallback perplexity-lite` failed: falcon raised
"Failed to authenticate" (Edison auth) and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists; the review relies on the primary
literature below, UniProt, and the PANTHER/PAINT files in `interpro/panther/PTHR12480/`.

### Protein

- 502 aa; N-terminal F-box (80-126) and a C-terminal JmjC domain (279-439) with the
  Fe(II)-binding triad H324/D326/H407 (PROSITE-ProRule PRU00538)
  [Q67XX3 UniProt FT BINDING lines]. An isoform 2 lacks 427-502 (part of the JmjC domain).
- PANTHER PTHR12480:SF21 ("JMJC DOMAIN-CONTAINING PROTEIN 8"); the paralog JMJ20 is in SF6.
  Human JMJD8 (SF21) lacks the F-box. The FEBS Lett 2022 paper calls JMJ22 a
  "D6-class Jumonji C protein (JMJD6)" — a class-level label; it does not establish
  orthology to human JMJD6, and I do not transfer JMJD6 lysyl-hydroxylase/splicing functions.
- No sequence-specific DNA-binding domain is present (only F-box + JmjC/cupin).

### Experimental literature (Arabidopsis)

1. Cho et al. 2012 Dev Cell (PMID:22483719; abstract-only in cache, full text paywalled; 403
   from cell.com and sciencedirect). Abstract: "the histone arginine demethylases, JMJ20 and
   JMJ22, act redundantly as positive regulators of seed germination. When PHYB is inactive,
   JMJ20/JMJ22 are directly repressed by the zinc-finger protein SOMNUS. However, upon PHYB
   activation, JMJ20/JMJ22 are derepressed, resulting in increased gibberellic acid levels
   through the removal of repressive histone arginine methylations at GA3ox1/GA3ox2".
   UniProt (curated, ECO:0000269 PubMed:22483719): "Histone demethylase that demethylates
   'Arg-3' (H4R3me) of histone H4 with a specific activity for H4R3me2"; catalytic activity
   RHEA:58352 (dimethyl-Arg -> monomethyl-Arg); nuclear localisation; red-light induction;
   double-mutant phenotype (reduced germination after R pulse, lower GA3ox1/GA3ox2, lower GA).
   Mutant phenotypes are reported for the jmj20 jmj22 double mutant (redundancy).
2. Matsuo et al. 2022 FEBS Lett (PMID:35962471; abstract-only): sac59, a suppressor of the
   thermospermine-deficient acl5 dwarf, is a point mutation in JMJ22; jmj22-2 T-DNA also
   partially suppresses acl5 while jmj20 and jmj21 do not, "suggesting a unique role for JMJ22
   in plant development"; SAC51-family mRNAs "are more stabilized in acl5 jmj22-2 than in
   acl5". Mechanism unknown; not in GOA. This is a single-gene (non-redundant) role
   distinct from the JMJ20-redundant germination role.
3. Taylor-Teeples et al. 2015 Nature (PMID:25533953): high-throughput Y1H screen of
   secondary-wall gene promoters against 1,664 TF clones; JMJ22 is not discussed in the main
   text; the GOA IPI row (with AT5G49720/KOR1) comes from the supplementary interaction table.
4. Lu et al. 2008 (PMID:18713399; abstract-only): family nomenclature and expression.

### PAINT / phylogeny

PTN001753861 (PTHR12480) IBD terms: GO:0005634 nucleus (seeds AT5G06550, Q386V9, Q96S16)
and GO:0000987 cis-regulatory region sequence-specific DNA binding (seed AT5G06550 only).
JMJ22's own IGI "histone demethylase activity" was NOT propagated at this node — a
deliberate PAINT decision; I treat demethylase activity as experimentally established for
JMJ22 but not as an inherited SF21-wide function. For the wheat transfer, this means the
only PAINT-sanctioned transfers are nucleus and the (over-annotated, see below) DNA-binding
term; H4R3 demethylase activity would rest on the shared F-box/JmjC architecture and
collinearity, not PAINT.

### Decisions

- histone demethylase activity (IGI) -> MODIFY to GO:0033749 histone H4R3 demethylase activity
  (UniProt curated specificity for H4R3me2).
- GO:0000987 IDA/IBA and GO:0000976 IPI -> MARK_AS_OVER_ANNOTATED: the protein has no DBD;
  chromatin occupancy at GA3ox promoters (likely ChIP; abstract says "at GA3ox1/GA3ox2") and a
  single unvalidated Y1H hit do not establish sequence-specific DNA binding as an enabled MF.
  Not REMOVE, because I cannot read the Cho 2012 full text.
- gibberellin mediated signaling pathway -> MODIFY to GO:0010372 positive regulation of
  gibberellin biosynthetic process: JMJ22 acts via GA3ox1/2 expression and GA levels, i.e.
  upstream of GA synthesis, not within GA signal transduction.
- positive regulation of seed germination (IMP/IGI) -> ACCEPT (the established role; redundant
  with JMJ20).
- epigenetic regulation of gene expression -> ACCEPT.
- response to red light (IEP/IMP), regulation of photomorphogenesis (IMP) -> KEEP_AS_NON_CORE
  (red-light/PHYB context; photomorphogenesis claim not visible in the abstract, deferred to
  the curator).
- nucleus (IDA, IBA, IEA, ISM) -> ACCEPT.
- No NEW terms: the thermospermine/SAC51 mRNA-stability role is real but mechanistically
  undefined (abstract-only), so recorded as a question rather than a process annotation.
