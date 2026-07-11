# MMUT (P22033) review notes

Deep research file `MMUT-deep-research-falcon.md` did not materialize within the 8-min poll
window; review grounded in the UniProt record (`MMUT-uniprot.txt`), seeded GOA
(`MMUT-goa.tsv`), cached `publications/PMID_*.md`, and the disorder KB
`~/repos/dismech/kb/disorders/Methylmalonic_Acidemia.yaml`.

## Core biology (well established)

- MMUT (formerly MUT; UniProt MUTA_HUMAN, EC 5.4.99.2) is the mitochondrial-matrix
  **adenosylcobalamin (AdoCbl / coenzyme B12)-dependent methylmalonyl-CoA mutase**. It
  catalyses the reversible carbon-skeleton isomerization **(R)-methylmalonyl-CoA
  (L-methylmalonyl-CoA) <-> succinyl-CoA** (Rhea:RHEA:22888), the final step of
  propionyl-CoA catabolism [PMID:25125334, PMID:29056341, UniProt CC FUNCTION].
- Physiological direction is left-to-right (MM-CoA -> succinyl-CoA); this funnels
  propionate derived from Ile/Val/Met/Thr, odd-chain fatty acids, and the cholesterol
  side chain into the TCA cycle as succinyl-CoA (anaplerosis) [PMID:25125334, PMID:29056341].
- **Homodimer** (PDB 2XIJ/2XIQ/3BIC); each protomer has an N-terminal (β/α)8 TIM-barrel
  substrate-binding domain and a C-terminal B12-binding domain (residues ~614-746). The
  cofactor Co is axially coordinated by His627 [UniProt FT BINDING 627; PMID:20876572].
- Cofactor delivery / repair: apo-MUT interacts with the **MMAA** GTPase (cblA) in a
  GTP-dependent manner; MMAA gates loading of AdoCbl (made by **MMAB**, cblB) into MUT
  and, via GTP hydrolysis, removes/replaces oxidized inactive cofactor (OH2Cbl) formed
  during catalysis, protecting/reactivating MUT [PMID:20876572, PMID:21138732, PMID:28943303].
- Inhibited by itaconyl-CoA, a suicide substrate analog that inactivates the B12 cofactor
  (links immunometabolite itaconate / CLYBL loss to functional B12 deficiency)
  [PMID:29056341]; also inhibited by malyl-CoA [UniProt CC, PMID:40108300].
- Disease: biallelic loss-of-function -> **isolated methylmalonic aciduria/acidemia,
  mut type (MAMM; MIM 251000)**, mut0 (no residual activity) vs mut- (residual, partly
  OHCbl-responsive). Distinct from cblA (MMAA) and cblB (MMAB) cofactor-delivery defects
  [PMID:25125334, PMID:27167370, PMID:28101778; disorder KB].

## Annotation triage rationale

- **GO:0004494 methylmalonyl-CoA mutase activity** — core MF. Supported by many EXP/IDA/IMP
  and IBA/IEA lines. ACCEPT all (duplicates across evidence codes are fine).
- **GO:0031419 cobalamin binding** — core MF (AdoCbl cofactor). ACCEPT (IDA + IBA); IEA ACCEPT.
- **GO:1902859 propionyl-CoA catabolic process** (IBA) — correct BP; the valid,
  non-obsolete term for MUT's pathway role (GO:0019678 "propionate metabolic process,
  methylmalonyl pathway" is now OBSOLETE). ACCEPT; use as core BP.
- **GO:1901290 succinyl-CoA biosynthetic process** (IDA PMID:1978672; IEA) — accurate
  product-oriented description of the same reaction. ACCEPT (IDA); IEA ACCEPT.
- **GO:0005759 mitochondrial matrix** (IDA PMID:24458; TAS Reactome; IEA) — correct
  localization. ACCEPT the experimental/loosest one as core; keep others.
- **GO:0005739 mitochondrion** (IBA/IEA/IDA/HTP/TAS) — parent of matrix; ACCEPT.
- **GO:0005737 cytoplasm** (IBA/IEA/IDA PMID:28943303) — MUT is matrix; cytoplasm is a
  broad/less-precise localization (UniProt lists Cytoplasm from PMID:28943303, likely
  reflecting apoenzyme/import-intermediate pool). MARK_AS_OVER_ANNOTATED (imprecise; matrix
  is the informative term). Not REMOVE (has an IDA behind it).
- **GO:0003824 catalytic activity / GO:0016853 isomerase activity / GO:0016866
  intramolecular transferase activity** (IEA InterPro) — correct but general ancestors of
  GO:0004494. Keep (ACCEPT the broad ones as non-misleading IEA rollups; they are valid,
  just less specific). Per guidance, broad IEAs above a well-supported specific term can be
  accepted.
- **GO:0046872 metal ion binding** (IEA) — MUT binds Co (in AdoCbl). Broad but true. ACCEPT.
- **GO:0005515 protein binding** (IPI x7, various partners: MMAA Q8IVH4, HTT P42858,
  CRYZ Q08257) — bare, uninformative MF. Per policy MARK_AS_OVER_ANNOTATED (do not REMOVE
  IPIs; do not attach a functional MF label). The biologically meaningful interaction
  (apo-MUT with MMAA) is captured better elsewhere.
- **GO:0042802 identical protein binding / GO:0042803 protein homodimerization activity**
  (IDA PMID:20876572) — MUT is a homodimer; homodimerization is real and structurally
  supported. ACCEPT homodimerization (informative); identical protein binding is the
  weaker synonym — KEEP_AS_NON_CORE.
- **GO:0003924 GTPase activity** (IDA PMID:20876572) — the GTPase in that paper is **MMAA**,
  not MUT. MUT has no GTPase activity/domain (no P-loop; it is a B12 mutase). This IDA
  appears to be a mis-assignment of MMAA's activity to its partner MUT. However, per the
  do-not-overrule-experimental-IDA policy and inability to read full text to confirm the
  assay attribution, use UNDECIDED (flag the concern; the abstract explicitly attributes
  GTPase activity to MMAA and shows it is "modulated by MUT").
- **GO:0043547 positive regulation of GTPase activity** (IDA PMID:20876572, PMID:28497574)
  — MUT (apoenzyme) stimulates MMAA's GTPase activity via their interaction; this is
  documented (28497574: GTPase activity "stimulated by an interaction with MUT"). ACCEPT
  as KEEP_AS_NON_CORE (regulatory, not the core catalytic function).
- **GO:0050667 homocysteine metabolic process** (IDA PMID:20031578) — this is a GWAS
  association of a MUT-locus SNP with plasma homocysteine; the paper itself states MUT's
  "catalytic activity is hardly related to homocysteine." Not a direct molecular role of
  MUT in homocysteine metabolism. MARK_AS_OVER_ANNOTATED (indirect/associative; not a
  bona fide involvement). Not REMOVE per policy caution around experimental codes, but the
  claim is only an epidemiological/mechanistically-indirect link.
- **GO:0072341 modified amino acid binding** (IDA PMID:20031578) — same GWAS paper; there
  is no biochemical demonstration that MUT binds a modified amino acid. The term does not
  fit MUT's characterized ligands (methylmalonyl-CoA, AdoCbl). MARK_AS_OVER_ANNOTATED.

## core_functions (author-supplied ids — strictly validated against current go.db)
- MF: GO:0004494 methylmalonyl-CoA mutase activity
- MF (cofactor): GO:0031419 cobalamin binding
- directly_involved_in BP: GO:1902859 propionyl-CoA catabolic process
- location: GO:0005759 mitochondrial matrix
