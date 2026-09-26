# Rice momilactone biosynthesis: manual literature research

## 2026-09-12: primary-source pathway and cluster check

Scope: the functional route from geranylgeranyl diphosphate (GGPP) to rice
momilactones A and B, including enzymes encoded outside the chromosome 4
biosynthetic gene cluster. This is a manually assembled literature research report, not a
provider-generated report. PMIDs and titles below were checked
against PubMed; pathway details were checked in the indexed primary-paper full
text and figure captions. Direct PMC page opens for the two 2021 papers returned
a browser challenge, but their indexed Results/Discussion sections were
accessible through targeted web searches. The 2025 full text was additionally
retrieved as Europe PMC XML. No cached publication was edited.

### Genomic cluster and functional module are different boundaries

[MIBiG BGC0000671, version 3](https://mibig.secondarymetabolites.org/repository/BGC0000671.3/index.html)
is the momilactone B cluster from *Oryza sativa* Japonica Group, mapped to
GenBank AP008210.2. At inspection it was active, with quality **questionable** and
completeness **unknown**. Its displayed genomic region is a database region,
not evidence that every enzyme needed for the functional pathway is encoded
there. Use this identifier as a cluster association, not a completeness claim.

The original cluster paper experimentally established linked cyclases,
CYP99A2/CYP99A3 and a short-chain dehydrogenase, with elicitor/UV induction.
Joint CYP99A2/CYP99A3 knockdown reduced momilactones but did not distinguish
their individual contributions. Supporting passage: “The double knockdown of
CYP99A2 and CYP99A3 specifically suppressed the elicitor-inducible production
of momilactones”. [PMID:17872948, *Identification of a biosynthetic gene cluster
in rice for momilactones*](https://pubmed.ncbi.nlm.nih.gov/17872948/), abstract.

The chromosome 4 cluster contains CPS4, KSL4, CYP99A2/CYP99A3 and MAS paralogs.
CYP76M8 belongs to the chromosome 2 diterpenoid BGC; CYP701A8 is on chromosome 6,
and CYP76M14 is on chromosome 1. Thus the complete functional module spans four
chromosomes. Cluster architecture and functional alternatives differ across
*Oryza*: do not propagate the exact cultivated-rice gene arrangement across
the genus. The 2025 study detected momilactone A but not B in *O. coarctata*
under its analytical conditions; non-detection is not proof that B is impossible.
[PMID:39887739, *Evolution and diversification of the momilactone biosynthetic
gene cluster in the genus Oryza*](https://pmc.ncbi.nlm.nih.gov/articles/PMC11840401/),
Introduction, Results, and Discussion.

### Scaffold formation

CPS4 catalyzes GGPP → syn-copalyl diphosphate. This precursor also supplies other
rice diterpenoids, so this is not an exclusively momilactone-specific role.
[PMID:15255861, *Functional identification of rice syn-copalyl diphosphate
synthase and its role in initiating biosynthesis of diterpenoid
phytoalexin/allelopathic natural products*](https://pubmed.ncbi.nlm.nih.gov/15255861/).

KSL4 (historically OsDTS2) catalyzes syn-copalyl diphosphate →
9βH-pimara-7,15-diene (syn-pimaradiene), the committed scaffold-forming step.
[PMID:15299118, *Identification of syn-pimara-7,15-diene synthase reveals
functional clustering of terpene synthases involved in rice
phytoalexin/allelochemical biosynthesis*](https://pubmed.ncbi.nlm.nih.gov/15299118/).

### Lactone formation and momilactone A

The preferred biochemical sequence is:

1. CYP99A2 **or** CYP99A3 oxidizes syn-pimaradiene at C19 to the aldehyde.
2. CYP76M8 introduces the C6β hydroxyl.
3. The resulting hydroxy-aldehyde cyclizes spontaneously to a
   19,6β-hemiacetal.
4. A clustered momilactone synthase SDR oxidizes the hemiacetal to the lactone.
5. CYP701A8 supplies C3β hydroxylation; subsequent oxidation gives the C3
   ketone of momilactone A.

Cell-free assays favor CYP99A2/3 before CYP76M8, although reverse-order
conversion was detectable. Both tested MS paralogs oxidized the hemiacetal;
their efficiencies on the later C3 alcohol differed. The final ketone can be
made by an SDR; a further CYP701A8 oxidation was also considered. Model a
supported route while keeping alternative ordering and terminal enzyme
division explicit. Do not replace hemiacetal oxidation with an unsupported
carboxylic-acid dehydration mechanism. Supporting passage: “This CYP76M8 acts
after the CYP99A2/3”.
[PMID:33793769, *Interdependent evolution of biosynthetic gene clusters for
momilactone production in rice*](https://pmc.ncbi.nlm.nih.gov/articles/PMC8136919/),
Abstract, Results (“Ordering CYP activity”, “Lactonization of hemiacetal
intermediate by OsMS1/2”), and Figure 8.

### Momilactone B and experimental limits

Complete heterologous reconstruction used CPS4, KSL4, CYP99A3, CYP76M8, OsMAS,
CYP701A8 and CYP76M14. CYP76M14 supplies C20 hydroxylation; closure against the
C3 carbonyl accounts for the extra hemiacetal ring in momilactone B. The
demonstrated substrate is the pre-C3 lactone. Combined expression with the
C3-tailoring enzyme yields B, but it does not directly establish isolated
momilactone A as a CYP76M14 substrate. The module therefore branches C20
hydroxylation from the lactone and leaves native C3/C20 ordering unresolved. Purified recombinant-pathway momilactone B inhibited
*Arabidopsis* germination and root growth.

The authors explicitly distinguish complete product reconstruction from
assigning every intermediate conversion to one enzyme. Endogenous tobacco
enzymes can contribute, and CYP701A8 versus OsMAS contributions to the C3
ketone remain distinguishable possibilities. Supporting passage:
“pathway reconstitution using N. benthamiana does not reveal the precise order
of biosynthetic steps”.
[PMID:33106662, *Rerouting plant terpene biosynthesis enables momilactone
pathway elucidation*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7990393/), Results,
Figure 4, and Discussion; [PubMed identity check](https://pubmed.ncbi.nlm.nih.gov/33106662/).

### MAS names require accession-level care

The 2016 primary study uses OsMAS/SDR110C-MS1 and OsSDR110C-MS2 and reports more
efficient terminal momilactone A formation by MS2.
[PMID:27337377, *Investigating inducible short-chain alcohol
dehydrogenases/reductases clarifies rice oryzalexin biosynthesis*](https://pubmed.ncbi.nlm.nih.gov/27337377/).
UniProt identifies [Q7FAE1, OsMAS](https://www.uniprot.org/uniprotkb/Q7FAE1/entry)
as LOC_Os04g10010 / Os04g0179200 and records NAD- or NADP-dependent conversion
of the C3-hydroxy lactone to momilactone A. Numeric MAS/MS names are inconsistent
across pathway diagrams; retain the locus/accession when grounding a role.
The primary comparative study independently lists both LOC_Os04g10000 and
LOC_Os04g10010 as MAS loci, but its slash-separated list alone does not resolve
which numeric name belongs to which locus.
[PMID:35781905, *Lateral transfers lead to the birth of momilactone biosynthetic
gene clusters in grass*](https://pmc.ncbi.nlm.nih.gov/articles/PMC9544640/), Methods.

### Curation decisions

- Represent the chromosome 4 BGC association and its external enzymatic
  dependencies explicitly.
- Treat CYP99A2/CYP99A3 and the lactonizing SDRs as alternatives where supported;
  do not require every paralog as an independent chemical step.
- Keep C20 tailoring optional for a module whose minimum output is momilactone A.
- Record spontaneous chemistry as a connection explanation, not a fabricated
  enzyme participant.
- Keep GGPP supply, P450 electron transfer, secretion, ecological regulation,
  and metabolon assembly outside the represented enzyme sequence unless
  separately evidenced and explicitly scoped.
