# COQ2 (human) — gene review notes

UniProt: Q96H96 (COQ2_HUMAN). Gene: COQ2 (HGNC:25223), synonym CL640. Chromosome 4.
371 aa; precursor with N-terminal mitochondrial transit peptide (1–34).

## Core identity and function

COQ2 is **4-hydroxybenzoate polyprenyltransferase, mitochondrial** (para-hydroxybenzoate:polyprenyltransferase; PHB:PPT), EC 2.5.1.39, a member of the **UbiA prenyltransferase family**.

- UniProt RecName: "4-hydroxybenzoate polyprenyltransferase, mitochondrial" [file:human/COQ2/COQ2-uniprot.txt].
- FUNCTION: "Mediates the second step in the final reaction sequence of coenzyme Q (CoQ) biosynthesis ... Catalyzes the prenylation of para-hydroxybenzoate (PHB) with an all-trans polyprenyl donor (such as all-trans-decaprenyl diphosphate) ... in humans, the side chain is comprised of 10 isoprenyls (decaprenyl) producing CoQ10 (also known as ubiquinone)" [file:human/COQ2/COQ2-uniprot.txt].
- Catalytic activity (Rhea RHEA:44504): "an all-trans-polyprenyl diphosphate + 4-hydroxybenzoate = a 4-hydroxy-3-(all-trans-polyprenyl)benzoate + diphosphate; EC=2.5.1.39" [file:human/COQ2/COQ2-uniprot.txt]. Human-specific decaprenyl form is RHEA:44564.
- COFACTOR: Mg(2+) [file:human/COQ2/COQ2-uniprot.txt].
- PATHWAY: "Cofactor biosynthesis; ubiquinone biosynthesis." (UniPathway UPA00232) [file:human/COQ2/COQ2-uniprot.txt].
- This is the committed prenylation/condensation step attaching the aromatic ring (4-HB) to the isoprenoid tail made by PDSS1/PDSS2, producing 3-decaprenyl-4-hydroxybenzoate (DHB) [Reactome R-HSA-2162192, "COQ2 catalyses the combination of 4-hydroxybenzoic acid ... with the polyisoprenoid tail all-trans-decaprenyl diphosphate ... to form 3-decaprenyl-4-hydroxybenzoate (DHB)"].

## Subcellular location and topology

- SUBCELLULAR LOCATION: "Mitochondrion inner membrane ...; Multi-pass membrane protein ...; Matrix side" [file:human/COQ2/COQ2-uniprot.txt].
- Seven transmembrane helices (TRANSMEM 84–104, 109–129, 149–169, 173–193, 204–224, 232–252, 278–298, 301–321, 333–353 in UniProt FT); C-terminus faces intermembrane space [file:human/COQ2/COQ2-uniprot.txt].
- IDA localization to mitochondrial inner membrane established in [PMID:27493029]: "its protein product localizes to mitochondria with the C-terminus facing the intermembrane space."
- HTP mitochondrial proteome dataset [PMID:34800366] localizes COQ2 to mitochondrion (aspect C).

## Functional / biochemical evidence

- [PMID:15153069 Forsgren et al. 2004]: cloned human COQ2, functional expression. "The human COQ2 gene, when expressed in yeast Coq2 null mutant cells, rescued the growth of this yeast strain in the absence of a non-fermentable carbon source and restored CoQ biosynthesis." "CoQ formed when cells were incubated with labelled decaprenyl pyrophosphate and nonaprenyl pyrophosphate, showing that the human enzyme is active and that it participates in the biosynthesis of CoQ." Basis of EXP MF annotation and IGI (vs yeast SGD:S000005324). Tissue specificity: widely expressed, higher in skeletal muscle, adrenal glands, heart.
- [PMID:16400613 Quinzii et al. 2006]: first molecular cause of primary CoQ10 deficiency; homozygous Y297C (a.a. numbering per that paper) missense in COQ2. "Radioisotope assays confirmed a severe defect of CoQ(10) biosynthesis in the fibroblasts of one patient." Basis of IMP for GO:0006744 and GO:0008412.
- [PMID:17374725 López-Martín et al. 2007]: full text available. Pathogenicity via yeast complementation: "human wild-type, but not mutant COQ2, functionally complements COQ2 defective yeast." "Polyprenyl-pHB transferase activity was 33-45% of controls in COQ2 mutant fibroblasts." Also: "The product of COQ2 catalyzes the transfer of para-hydroxybenzoate to the polyprenyl chain, one of the initial steps of CoQ biosynthesis." Additional phenotype: CoQ10 deficiency also impairs de novo pyrimidine synthesis (uridine rescue) — a downstream consequence of respiratory-chain / dihydroorotate dehydrogenase dependence on CoQ, not a direct COQ2 function. Basis of IMP annotations.
- [PMID:27493029 Desbats et al. 2016]: defined COQ2 structure/topology, IDA localization, and genotype–phenotype correlation via yeast complementation of all reported mutant alleles; "the residual activity of the mutant proteins correlates with the clinical phenotypes." Basis of IDA (inner membrane) and IMP (GO:0006744).

## Disease

- Primary coenzyme Q10 deficiency, type 1 (COQ10D1, MIM 607426): autosomal recessive; encephalomyopathy, infantile multisystem disease, cerebellar ataxia, Leigh syndrome, isolated myopathy, and nephropathy (COQ2 nephropathy) [file:human/COQ2/COQ2-uniprot.txt; PMID:16400613; PMID:17374725; PMID:17855635; PMID:27493029].
- Multiple system atrophy 1 (MSA1, MIM 146500): susceptibility variants reported [PMID:23758206]; noted in UniProt DISEASE section.

## Existing-annotation review decisions (summary)

Core, experimentally supported:
- GO:0008412 4-hydroxybenzoate polyprenyltransferase activity (EXP/IMP/IBA/TAS/IEA) — ACCEPT the experimental ones; this is the defining MF.
- GO:0006744 ubiquinone biosynthetic process (IDA/IMP/IBA/TAS/IEA/IGI) — ACCEPT; defining BP.
- GO:0005743 mitochondrial inner membrane (IDA/IBA/IEA/TAS) — ACCEPT; established location and topology.

Non-core / general / redundant:
- GO:0004659 prenyltransferase activity (IEA, IGI) — parent of GO:0008412; less informative. IGI is experimental so MARK_AS_OVER_ANNOTATED (per policy, do not REMOVE experimental); IEA MODIFY→GO:0008412.
- GO:0016765 transferase activity, transferring alkyl or aryl (other than methyl) groups (IEA InterPro) — grandparent; MODIFY to specific GO:0008412.
- GO:0008299 isoprenoid biosynthetic process (IEA) — COQ2 uses/consumes the polyprenyl-PP but does not itself make isoprenoids; it condenses the tail onto 4-HB. Over-general/borderline-wrong for the MF; the isoprenoid tail is made by PDSS1/PDSS2 and the mevalonate pathway. MARK_AS_OVER_ANNOTATED (keep, but not core; it is downstream isoprenoid utilization for ubiquinone).
- GO:0016020 membrane (IEA InterPro) — generic; located_in mitochondrial inner membrane is the specific form. MODIFY→GO:0005743.
- GO:0005739 mitochondrion (HTP) — coarse but correct location; KEEP_AS_NON_CORE (inner membrane is the specific term).
- GO:0006071 glycerol metabolic process (IGI, with UniProtKB:P32378 = yeast GPD1) — this looks like a legacy/erroneous cross-species IGI (P32378 is S. cerevisiae glycerol-3-phosphate dehydrogenase); COQ2 has no established role in glycerol metabolism. It is experimental (IGI), so per policy do not REMOVE; MARK_AS_OVER_ANNOTATED (very likely spurious).

## core_functions

Single core function:
- MF: GO:0008412 4-hydroxybenzoate polyprenyltransferase activity
- directly_involved_in BP: GO:0006744 ubiquinone biosynthetic process
- location: GO:0005743 mitochondrial inner membrane

## Term id checks (OLS)

- GO:0008412 4-hydroxybenzoate polyprenyltransferase activity — valid (not obsolete).
- GO:0006744 ubiquinone biosynthetic process — valid.
- GO:0005743 mitochondrial inner membrane — valid.
- GO:0002083 (4-hydroxybenzoate decaprenyltransferase activity) — OBSOLETE; do NOT use. GO:0008412 is the current term.
