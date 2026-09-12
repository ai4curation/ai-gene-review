# Manual deep-research synthesis for human KLB

Date: 2026-07-18

## Scope and retrieval

This synthesis covers human KLB (UniProtKB Q86Z14) using the reviewed UniProt
record, the complete fetched GOA set, four GOA-cited PubMed records, and two
additional structure/function papers. The requested Falcon deep-research run
failed with HTTP 402; its Perplexity-lite fallback failed with HTTP 401 because
the configured quota was unavailable. No provider-labelled report was retained.

## Molecular identity and localization

KLB encodes beta-Klotho, a 1,044-residue, N-glycosylated, single-pass type III
cell-membrane protein. Its extracellular region contains tandem glycoside
hydrolase-1-like domains, but it is a receptor-like pseudoenzyme rather than a
carbohydrate hydrolase. The human crystal structure shows loss of one essential
catalytic glutamate in each domain: [PMID:29342135, "The first glutamate in D1 is
replaced by N241, whereas the second glutamate in D2 is replaced by A889,
indicating that neither GH domain in β-Klotho can function as an active
glycoside-hydrolase enzyme."]. This directly contradicts the InterPro-derived
hydrolase annotation and removes the mechanistic basis for the associated
carbohydrate-metabolism transfer.

## Endocrine-FGF recognition and receptor-complex function

KLB directly recognizes the carboxyl termini of FGF19 and FGF21. FGF21 binding
is specifically lost as its carboxyl terminus is truncated [PMID:19059246,
"FGF21 binds directly to beta-Klotho through its C-terminus."]. Independent
structure/function work reached the same conclusion [PMID:19117008, "Binding
studies with betaKlotho revealed that the interaction with the co-receptor
involves the C-terminus"]. For FGF19, chimeric-ligand experiments demonstrate
Klotho-family specificity [PMID:18829467, "These results identified the
C-terminal tail of FGF19 as a region necessary for its recognition of Klotho
family proteins."].

The human KLB-FGF21 crystal structure and cell assays show that KLB is the
high-affinity ligand-recognition component, while FGFR supplies kinase activity
[PMID:29342135, "In this model, β-Klotho functions as a primary high affinity
receptor for FGF21, whereas FGFR1c functions as a catalytic subunit that
mediates receptor dimerization and intracellular signaling."]. A second
structure resolved FGF19 bound to human KLB and found that FGF19 and FGF21 use
the same two KLB sites [PMID:30944224, "FGF19CT and FGF21CT bind to the same
binding site on sKLB"].

KLB also associates functionally with FGFRs. FGF19 requires the KLB-FGFR4
combination for liver-selective signaling [PMID:17627937, "KLB is required for
FGF19 binding to FGFR4, intracellular signaling, and downstream modulation of
gene expression."]. The structural FGF21 study measured direct extracellular
FGFR1c-KLB affinity and demonstrated that cells require KLB for FGF21-induced
FGFR1c phosphorylation [PMID:29342135, "β-Klotho is required for FGFR1c-mediated
signaling induced by FGF21."]. These data support both the existing ligand- and
FGFR-binding annotations and a more informative coreceptor-activity annotation.

## Physiological output and evidence boundary

In the liver, the FGF19-KLB-FGFR4 axis represses CYP7A1 and thereby limits bile
acid synthesis. The cited study reports that FGF19 injection in mice causes
"repression of CYP7A1" and identifies KLB as the required FGFR4 coreceptor
[PMID:17627937]. Because the physiological experiment is in mouse, transfer of
the negative bile-acid-biosynthesis role to human KLB is represented
conservatively with ISS rather than direct human experimental evidence.

KLB is a plasma-membrane endocrine-FGF receptor component that binds FGF19 and
FGF21, associates with FGFR1/FGFR4, and enables Klotho-dependent FGFR signaling.
Evidence conclusion: KLB is an endocrine-FGF coreceptor at the plasma membrane.
The evidence does not support glycosidase activity despite the retained GH1-like
fold. Broad metabolic phenotypes downstream of FGF19/FGF21 are not treated as
independent KLB molecular activities.
