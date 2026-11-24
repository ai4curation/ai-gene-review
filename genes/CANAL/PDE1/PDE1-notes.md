# PDE1 (Candida albicans, Q5AGE4, orf19.11710 / C5_02290W_A) — curation notes

## Identity
- Low-affinity class II cyclic nucleotide phosphodiesterase (Pfam PF02112 PDEase_II; PROSITE PS00607; PANTHER PTHR28283:SF1).
- Orthologs: S. cerevisiae PDE1 (SGD:S000003217), S. pombe cgs2/pde1 (SPCC285.09c), Dictyostelium PdsA.
- Paralog-in-function: PDE2 (high-affinity class I PDE, distinct family).

## Biochemistry
- Cloned by complementation of a S. cerevisiae PDEase-deficient mutant [PMID:8075796 "We have cloned a Candida albicans gene, which encodes a cyclic nucleotide phosphodiesterase (PDEase), by complementation in a Saccharomyces cerevisiae PDEase-deficient mutant."]
- Hydrolyses cAMP and cGMP [PMID:8075796 "it hydrolyses both cAMP (Km = 0.49 mM) and cGMP (Km = 0.25 mM)"]; no divalent cation requirement, poorly inhibited by standard PDE inhibitors.

## Physiology
- Pde1 (not Pde2) terminates glucose- and acidification-induced cAMP signalling [PMID:20558315 "Pde1, but not Pde2, is responsible for down-regulation of cAMP signalling induced by glucose addition or intracellular acidification"]. Same division of labour as S. cerevisiae [PMID:9880329 "We show that deletion of PDE1, but not PDE2, results in a much higher cAMP accumulation upon addition of glucose or upon intracellular acidification."]
- Morphogenesis/stress phenotypes are mainly synthetic with GPA2 [PMID:20558315 "the genetic interactions of PDE1 and in some cases PDE2, with GPA2 caused synthetic defects in growth, morphogenesis and responses to some stresses"].
- Virulence: secondary to PDE2; pde1 pde2 double mutant avirulent [PMID:20558315].
- Not required for farnesol repression of hyphae [PMID:18078440 "Neither Pde1 nor Pde2 was necessary for the repression of hyphal growth by farnesol or dodecanol."]
- S. cerevisiae Pde1 PKA site (Ser252) conserved in C. albicans Pde1 [PMID:9880329].

## Review decisions
- MF: cAMP PDE (core), cGMP PDE (accept; physiological relevance unclear), general PDE terms accepted.
- BP: negative regulation of cAMP/PKA signalling and of glucose-activated GPCR pathway accepted (Pde1 directly destroys the second messenger); cAMP catabolism accepted. (superseded for GO:0110034; see the Gpa2 and OpenScientist sections below)
- Filamentous growth IMPs kept as non-core (indirect, largely synthetic with gpa2; full text not cached).
- CC: no localisation data; ND accepted.
- Full text of PMID:20558315 and PMID:8075796 not available in cache (abstract only).

## Deep research status (2026-10-02)
- `just deep-research-falcon CANAL PDE1 --fallback perplexity-lite`: the wrapper reported failure (falcon timed out after 600 s; perplexity not configured), but the falcon job itself completed at 898 s and wrote PDE1-deep-research-falcon.md, which was then used.
- Literature was instead gathered manually via PubMed search ("Candida albicans PDE1 phosphodiesterase" returned 5 hits: PMID:30299574, 20558315, 18078440, 9880329, 8075796), plus PMID:14523128 (PDE2). All cached publications are abstract-only.

## Interaction with Gpa2 (follow-up, 2026-10-02)
There is no evidence of a physical Pde1-Gpa2 interaction; the "regulatory module" of Wilson et al. 2010 is functional/genetic.
- Gpa2 drives acidification-induced cAMP [PMID:20558315 "Our biochemical evidence shows that Gpa2 stimulates cAMP signalling in response to intracellular acidification"]; Pde1 terminates both glucose- and acidification-induced spikes.
- Synthetic pde1 gpa2 defects (growth, morphogenesis, stress) are read by the authors as Gpa2 acting outside the cAMP pathway [PMID:20558315 "suggesting that Gpa2 mediates its effects on these processes in a cAMP pathway-independent manner"]. Consistent with Gpa2 having a MAPK-linked role [PMID:12477787 "These defects cannot be reversed by exogenous addition of cyclic AMP. However, overexpression of HST7, which encodes a component of the filament-inducing mitogen-activated protein kinase (MAPK) cascade, bypasses the Gpa2 requirement."]
- Is the Gpr1-Gpa2 module glucose-activated in C. albicans? Disputed:
  - Yes: [PMID:15302825 "Biochemical studies also reveal that GPR1 and GPA2 are required for a glucose-dependent increase in cellular cAMP."]
  - No: [PMID:15673611 "deletion of neither CaGpr1 nor CaGpa2 affects glucose-induced cAMP signaling. In contrast, the latter is abolished in strains lacking CaCdc25 or CaRas1"]; ligands appear to be methionine/lactate [PMID:30761119 "However, it seems that the ligand(s) for CaGpr1 are not sugars but lactate and methionine."]; Gpr1 mediates lactate-induced beta-glucan masking [PMID:27941860].
- Consequence for review: IBA GO:0110034 (negative regulation of adenylate cyclase-activating *glucose-activated* GPCR signalling, donor S. pombe cgs2) changed ACCEPT -> MARK_AS_OVER_ANNOTATED (TERM_SCOPING_PROBLEM). Receptor-agnostic GO:0141162 retained as core. PMID:15302825 finding marked DISPUTED.
- Deep research also notes (citing Inglis & Sherlock 2013) that a pde1 single mutant filaments normally, consistent with keeping the filamentous growth IMPs as non-core.

## Locus identifiers
Falcon flagged that some literature labels PDE1 as orf19.4235 whereas UniProt Q5AGE4 lists orf19.11710. CGD's own PDE1 locus (CAL0000177603) cross-references Q5AGE4 and is the source of the IDA/IMP annotations, so the gene-to-accession mapping is CGD's. (Assembly 19 assigned separate orf19 numbers to allelic ORFs, which likely explains the two numbers; not independently verified here.)

## OpenScientist run on the glucose-activated component (2026-10-02)
- Hypothesis (free-text, function-assignment): the cAMP rise Pde1 terminates after glucose addition is generated through Gpr1/Gpa2. References given: PMID:20558315, 15302825, 15673611. The review's verdict was withheld. 3 iterations, 827 s. Report: `PDE1-hypotheses/pde1-glucose-gpcr-pathway/openscientist.md`.
- Verdict: "Partially supported but over-annotated". It agrees that Pde1 terminates glucose-induced cAMP, and that the glucose-activated GPCR source is contradicted by PMID:15673611 and the Gpr1 ligand is ambiguous [PMID:15667329 "it remains unclear whether Gpr1 senses sugars, as in Saccharomyces cerevisiae, or specific amino acids like methionine"].
- It recommended the parent GO:1902660 (negative regulation of glucose mediated signaling pathway). Verified via OLS that GO:1902660 is a direct parent of GO:0110034, and that GO:0010255 glucose mediated signaling pathway does not require a GPCR. Adopted: GO:0110034 changed from MARK_AS_OVER_ANNOTATED to MODIFY -> GO:1902660.
- Errors in the report, not imported: it calls the S. cerevisiae paradigm the source of the IBA (the PAINT donor is S. pombe cgs2, where Git3 is a genuine glucose receptor), and it treats Miwa 2004 as superseded rather than disputed. Its QuickGO evidence-code counts were not re-checked.
- No local bioinformatics holdout existed for PDE1, so there was nothing to compare against.
