# UMPS (human) — review notes

UniProtKB:P11172, HGNC:12563. Bifunctional **uridine 5'-monophosphate synthase** (UMP synthase).
Deep research: falcon provider is out of credits (HTTP 402); no `-deep-research-falcon.md`. Review grounded in
`UMPS-uniprot.txt`, seeded GOA, and cached `publications/PMID_*.md`.

## Core biology

UMP synthase catalyzes the **final two steps of de novo pyrimidine biosynthesis** on a single
polypeptide (bifunctional / multifunctional enzyme):

1. **Orotate phosphoribosyltransferase (OPRT; EC 2.4.2.10)** — N-terminal domain (residues ~2–214):
   condenses orotate + PRPP -> orotidine-5'-monophosphate (OMP) + PPi.
2. **Orotidine-5'-phosphate decarboxylase (ODC / OMPdecase; EC 4.1.1.23)** — C-terminal domain
   (residues ~221–480): decarboxylates OMP -> uridine monophosphate (**UMP**) + CO2.

UMP is the parent pyrimidine ribonucleotide; all other pyrimidine nucleotides (UDP, UTP, CTP, dCTP,
dTTP) derive from UMP via downstream kinases/synthases, **not** by UMPS itself.

- Bifunctional / single polypeptide: [PMID:9042911 "Uridine monophosphate (UMP) synthase is a bifunctional enzyme catalyzing the last two steps of de novo pyrimidine biosynthesis, orotate phosphoribosyltransferase (OPRT) and orotidine-5'-monophosphate decarboxylase (ODC)"]; [PMID:6893554 "the last two enzyme activities of de novo UMP biosynthesis occur on a single polypeptide chain of approximately 51500 daltons"].
- Structural / mechanistic (C-terminal OMPD, active site D312/K314/D317, covalent mechanism, homodimer): [PMID:18184586 "The C-terminal domain of UMPS is orotidine-5'-monophosphate decarboxylase (OMPD), a cofactor-less yet extremely efficient enzyme"]. UniProt: "Homodimer; dimerization is required for enzymatic activity."
- Assay of both activities as a bifunctional protein: [PMID:11730338 "the two enzymatic activities of orotate phosphoribosyltransferase (OPRTase) and orotidine 5'-monophosphate decarboxylase (ODCase), either as a bifunctional protein (uridine 5'-monophosphate synthase, UMPS)"].

## Localization

Cytosolic enzyme (Reactome R-HSA-73564, R-HSA-73567; UniProt cytoplasm). A minor nuclear pool is
reported alongside CAD: [PMID:15890648 "UMP synthase, the bifunctional protein that catalyzes the last two steps in the pathway, was also found in both the cytoplasm and nucleus"]. Catalysis is cytosolic; nucleus kept as non-core.

## Disease

Orotic aciduria 1 (ORAC1, MIM:258900): autosomal recessive; megaloblastic anemia, failure to thrive,
massive urinary orotic acid excretion; uridine-responsive. ORAC1 missense variants (R96G, V109G, G429R)
reduce OPRT and/or ODC activity: [PMID:9042911 "Loss of either enzymatic activity results in hereditary orotic aciduria, a rare autosomal recessive disorder characterized by retarded growth, anemia, and excessive urinary excretion of orotic acid"].

## Annotation decisions (summary)

- OPRT (GO:0004588) + ODC (GO:0004590) MF, all evidence codes -> ACCEPT (core; both are the defining activities).
- UMP biosynthetic process (GO:0006222) and 'de novo' UMP biosynthetic process (GO:0044205) -> ACCEPT (core BP).
- 'de novo' pyrimidine nucleobase biosynthetic (GO:0006207) -> ACCEPT (correct, slightly broader parent).
- pyrimidine nucleotide biosynthetic (GO:0006221) and pyrimidine nucleobase biosynthetic (GO:0019856) -> KEEP_AS_NON_CORE (correct but broad grouping terms).
- **UDP biosynthetic process (GO:0006225)** and **'de novo' CTP biosynthetic process (GO:0044210)** -> **REMOVE**. Both are IEA Ensembl-Compara ortholog transfers (GO_REF:0000107) that mis-state the product: UMPS makes UMP, not UDP or CTP. These are over-propagated electronic inferences arguable on biochemical grounds.
- cytosol (GO:0005829) TAS x2, cytoplasm (GO:0005737) IDA -> ACCEPT.
- nucleus (GO:0005634) IDA -> KEEP_AS_NON_CORE (minor pool; not the site of the de novo pyrimidine reactions).
- protein binding (GO:0005515) IPI x2 (both with EPHA4/P54764, from BioPlex AP-MS) -> MARK_AS_OVER_ANNOTATED (bare `protein binding`; uninformative; not removed per policy).
