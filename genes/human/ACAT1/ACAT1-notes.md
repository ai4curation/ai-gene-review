# ACAT1 (P24752) research notes

Gene: ACAT1 (HGNC:93); UniProt P24752 (THIL_HUMAN); EC 2.3.1.9.
Protein: Acetyl-CoA acetyltransferase, mitochondrial; AltNames: Acetoacetyl-CoA thiolase; "T2".
427 aa precursor (1-33 mitochondrial transit peptide; mature chain 34-427). Homotetramer.

## CRITICAL nomenclature warning: ACAT1 (P24752) is NOT the cholesterol-esterifying enzyme

There is a long-standing naming collision. "ACAT" / "ACAT1" is used in two unrelated senses:
- **This gene/protein (HGNC:93, P24752)** = mitochondrial **acetoacetyl-CoA thiolase / T2**,
  EC 2.3.1.9, a matrix homotetramer in **ketone body** and **isoleucine** metabolism.
- **SOAT1 (HGNC:11177)** = **sterol O-acyltransferase 1 / acyl-CoA:cholesterol acyltransferase**,
  EC 2.3.1.26, an **ER** integral-membrane enzyme that esterifies cholesterol. SOAT1's old/alias
  name is also "ACAT1" (and SOAT2's alias is "ACAT2"). These are entirely different proteins.

This collision has produced wrong-gene GO annotations on P24752 (see PMID:32944968 below).

## Core enzymatic function (thiolase, EC 2.3.1.9)

T2 is a CoA-dependent thiolase catalyzing a reversible Claisen condensation / thiolytic cleavage.
- Reversible reaction: 2 acetyl-CoA <=> acetoacetyl-CoA + CoA (RHEA:21036; EC 2.3.1.9)
  [UniProt P24752 CATALYTIC ACTIVITY].
- Also degrades the isoleucine-pathway intermediate 2-methylacetoacetyl-CoA:
  propanoyl-CoA + acetyl-CoA <=> 2-methyl-3-oxobutanoyl-CoA + CoA (RHEA:30719) [UniProt P24752].
- UniProt FUNCTION: "The activity of the enzyme is reversible and it can also catalyze the
  condensation of two acetyl-CoA molecules into acetoacetyl-CoA (PubMed:17371050). Thereby, it
  plays a major role in ketone body metabolism" [UniProt P24752 FUNCTION].

PMID:17371050 (Haapalainen et al., Biochemistry 2007; crystal structures of human T2; ABSTRACT
ONLY in cache, full_text_available: false): "Mitochondrial acetoacetyl-coenzyme A (CoA) thiolase
(T2) is important in the pathways for the synthesis and degradation of ketone bodies as well as
for the degradation of 2-methylacetoacetyl-CoA." "A unique property of T2 is its activation by
potassium ions." "The potassium ion is bound near the CoA binding site and the catalytic site."
"A unique property of T2 is its ability to use 2-methyl-branched acetoacetyl-CoA as a substrate,
whereas the other structurally characterized thiolases cannot utilize the 2-methylated compounds."
"The kinetic measurements show that T2 can degrade acetoacetyl-CoA and 2-methylacetoacetyl-CoA
with similar catalytic efficiencies." [PMID:17371050 abstract].
-> Supports: acetyl-CoA C-acetyltransferase activity (GO:0003985), C-acetyltransferase activity
   (GO:0016453), potassium ion binding (GO:0030955), homotetramer, ketone body + isoleucine roles.

Activation by potassium ions, not sodium [UniProt ACTIVITY REGULATION, ECO:0000269|PubMed:17371050].
Active sites: Cys126 (acyl-enzyme intermediate), His413 (proton donor/acceptor) [UniProt FT].

## Subcellular location

Mitochondrion / mitochondrial matrix.
- PMID:1979337 (Fukao et al. 1990): "Pulse labeling followed by subcellular fractionation revealed
  that the T2 proteins in the fibroblasts from these patients are present in the mitochondria."
  [PMID:1979337 abstract]. -> Supports mitochondrion (GO:0005739).
- Mitochondrial matrix (GO:0005759) is the standard CC for a soluble matrix thiolase; supported by
  Reactome TAS annotations and UniProt-IEA. Consistent with the homotetramer crystal structures
  (soluble protein).

## Ketone body metabolism (ketogenesis AND ketolysis)

T2 sits at the acetoacetyl-CoA <-> 2 acetyl-CoA node, central to both ketone body synthesis and
utilization. PMID:17371050: "important in the pathways for the synthesis and degradation of
ketone bodies." [PMID:17371050 abstract].
GOA captures: ketone body catabolic process (GO:0046952, IMP PMID:1979337) and ketone body
metabolic process (GO:1902224, IC) [GOA / UniProt GO xrefs].

## Isoleucine catabolism + 3-ketothiolase / beta-ketothiolase deficiency (3KTD)

T2 catalyzes the final thiolytic step of isoleucine catabolism (2-methylacetoacetyl-CoA -> 
propionyl-CoA + acetyl-CoA). Loss causes "beta-ketothiolase deficiency" / 3KTD (MIM:203750).
- PMID:9744475 (Fukao et al. 1998): "Mitochondrial acetoacetyl-CoA thiolase (T2) deficiency is an
  inborn error of ketone body and isoleucine catabolisms." [PMID:9744475 abstract].
- UniProt DISEASE: "3-ketothiolase deficiency (3KTD)... An autosomal recessive inborn error of
  isoleucine catabolism characterized by intermittent ketoacidotic attacks... Urinary excretion of
  2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, triglylglycine, butanone is increased."
  [UniProt P24752 DISEASE].
- Disease-variant papers (all ABSTRACT ONLY in cache), each characterizing missense alleles with
  reduced/abolished thiolase activity:
  - PMID:1715688 (347Ala->Thr / A380T): unstable T2 protein.
  - PMID:7728148 (N158D, T297M, A301P): "only the mutant T2 polypeptide with T297M appeared to
    have a detectable residual activity"; expression confirmed reduced activity.
  - PMID:9744475 (N93S, I312T, A333P): destabilizing missense, reduced residual thiolase activity.
  - PMID:8103405 (two original 2-methylacetoacetic-aciduria families; "K(+)-activated enzyme,
    mitochondrial acetoacetyl-coenzyme A thiolase (T2)"): unstable/translation-impairing alleles.
  - PMID:1979337: original cloning + four 3KTD fibroblast lines.
These collectively support GO:0003985 (MF), GO:0006550 L-isoleucine catabolic process (BP), and
GO:0046952 ketone body catabolic process. The IMP/EXP annotations rest on patient-fibroblast and
expression assays (loss/reduction of thiolase activity in disease alleles).

## WRONG-GENE annotations from PMID:32944968 (cholesterol acyltransferase / ER) -> REMOVE

PMID:32944968 (Wang et al., EMBO J 2020; "Cholesterol 25-Hydroxylase inhibits SARS-CoV-2...";
full text available). The paper studies CH25H/25HC activating the **ER acyl-CoA:cholesterol
acyltransferase (ACAT)** to deplete plasma-membrane cholesterol:
- "25HC inhibits viral membrane fusion by activating the ER-localized acyl-CoA:cholesterol
  acyltransferase (ACAT) which leads to the depletion of accessible cholesterol from the plasma
  membrane." [PMID:32944968 abstract].
- "the enzyme catalyzing the esterification of cholesterol, ACAT" ... knockdown "by lentiviral
  vectors carrying ... shRNAs targeting ACAT1 and ACAT2." [PMID:32944968 results].
The "ACAT" here is the cholesterol-esterifying **SOAT1/SOAT2** (EC 2.3.1.26), an ER enzyme — NOT
the mitochondrial thiolase P24752 (EC 2.3.1.9). The mitochondrial T2 has no cholesterol
O-acyltransferase activity and is not an ER protein. The two GOA annotations derived from this
paper on P24752 are therefore wrong-gene mis-attributions caused by the ACAT1/SOAT1 name collision:
- GO:0034736 cholesterol O-acyltransferase activity (IDA, PMID:32944968) -> REMOVE.
- GO:0005783 endoplasmic reticulum (IDA "is_active_in", PMID:32944968) -> REMOVE.

## Moonlighting: ACAT1 tetramer as a protein acetyltransferase (acetylates IDH2/PDH)

A genuine, separate moonlighting activity of the mitochondrial T2 tetramer (Fan et al., Mol Cell
2016, PMID:27867011): tetrameric ACAT1 acetylates pyruvate dehydrogenase complex components (PDHA1,
PDP1) and IDH2 (K413), inhibiting them; relevant in cancer metabolism. Captured in GOA only as the
Reactome reaction "ACAT1 tetramer acetylates IDH2 dimer" (Reactome:R-HSA-9854415), used here as a
mitochondrial-matrix **location** TAS annotation. This protein-lysine-acetyltransferase activity is
NOT in the GOA MF set being reviewed; noted for suggested questions / proposed terms.
(Not citing as supporting_text since PMID:27867011 is not in the publications cache.)

## Proteomics / exosome / mitochondrial-proteome localizations (non-core)

- GO:0070062 extracellular exosome (HDA, PMID:23533145 prostatic-secretion exosomes; PMID:19056867
  urinary exosomes): high-throughput vesicle proteomics; ubiquitous-contaminant-type CC, not the
  functional location. KEEP_AS_NON_CORE.
- GO:0005739 mitochondrion (HTP, PMID:34800366 quantitative mito proteome): supports mitochondrial
  localization; consistent but less specific than matrix. KEEP_AS_NON_CORE / ACCEPT.

## Electronic / ortholog-transfer BP terms (Ensembl GO_REF:0000107) — likely over-annotation

liver development (GO:0001889), response to hormone (GO:0009725), response to starvation
(GO:0042594), adipose tissue development (GO:0060612), metanephric proximal convoluted tubule
development (GO:0072229): all IEA transferred from rodent orthologs. These reflect tissue
expression/physiology contexts, not direct molecular roles of the thiolase. MARK_AS_OVER_ANNOTATED
or KEEP_AS_NON_CORE. (T2 is expressed kidney/liver-enhanced per HPA; "response to starvation" is
plausible given ketogenesis but is an indirect ortholog inference.)

## Other MF terms

- GO:0016453 C-acetyltransferase activity (IDA PMID:17371050): correct, slightly more general
  parent of GO:0003985; KEEP_AS_NON_CORE.
- GO:0016746 / GO:0016747 acyltransferase activity (InterPro IEA): correct but very general
  parents; KEEP_AS_NON_CORE.
- GO:0030955 potassium ion binding (IDA PMID:17371050): correct — T2 is K+-activated and the
  crystal structure resolves bound K+; ACCEPT (cofactor/activator binding, supporting but not the
  catalytic core MF).
- GO:0120225 coenzyme A binding (IEA): correct — CoA is substrate/cosubstrate; KEEP_AS_NON_CORE.
- GO:0019899 enzyme binding (IEA ortholog): generic; over-annotation/non-core.
- GO:0042802 identical protein binding (IEA ortholog): T2 is a homotetramer, so self-association is
  real, but "identical protein binding" is uninformative; KEEP_AS_NON_CORE.

## CoA / acetyl-CoA process terms (PMID:17371050, BHF-UCL IDA)

acetyl-CoA biosynthetic process (GO:0006085), acetyl-CoA catabolic process (GO:0046356), coenzyme A
metabolic process (GO:0015936), coenzyme A biosynthetic process (GO:0015937), propionyl-CoA
biosynthetic process (GO:1902860): these are BHF-UCL curator inferences from the in-vitro
reversible thiolase reactions. They are chemically defensible (the reaction produces/consumes
acetyl-CoA and CoA, and the isoleucine branch yields propionyl-CoA precursor) but are reaction-level
restatements rather than the gene's physiological process. KEEP_AS_NON_CORE; the physiological BP
core is ketone body metabolism + isoleucine catabolism.

## fatty acid beta-oxidation (GO:0006635)

UniProt PATHWAY: "Lipid metabolism; fatty acid beta-oxidation." and FUNCTION describes T2 as "one
of the enzymes that catalyzes the last step of the mitochondrial beta-oxidation pathway." However,
T2/ACAT1's physiologically dominant role is the acetoacetyl-CoA node (ketone bodies) and the
2-methyl-branched isoleucine intermediate; the unbranched long-chain 3-oxoacyl-CoA thiolysis of
classic beta-oxidation is mainly ACAA2 (medium/short-chain) and the MTP/HADHB (long-chain). The
beta-oxidation annotation (IEA via UniPathway) is defensible at the parent level but non-core for
this gene. KEEP_AS_NON_CORE.

## Summary of decisions

- Core MF: acetyl-CoA C-acetyltransferase activity (GO:0003985).
- Core BP: ketone body metabolic process and L-isoleucine catabolic process.
- Core CC: mitochondrial matrix (GO:0005759).
- REMOVE (wrong gene, SOAT1/SOAT2 collision): GO:0034736 cholesterol O-acyltransferase activity
  and GO:0005783 endoplasmic reticulum (both PMID:32944968).
- Over-annotation (ortholog IEA tissue/physiology BP): liver dev, adipose dev, metanephric tubule
  dev, response to hormone, (response to starvation borderline).
- Non-core but correct: matrix/mito CC variants, K+/CoA binding, general transferase parents,
  exosome CC, CoA/acetyl-CoA reaction-level BP terms, fatty acid beta-oxidation.
</content>
</invoke>

## 2026-09-26 complete re-review — supersedes the historical decisions above

The earlier notes are retained as history. Their confident SOAT1-only attribution,
protein-acetyltransferase conclusions, blanket developmental rejections, and broad-term
non-core designations are superseded by this source audit.

Identity and baseline: approved human ACAT1, HGNC:93, UniProt P24752; aliases ACAT,
MAT, T2 and THIL. The HGNC-sourced [Ensembl record](https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075239)
and [ORDO](https://www.orpha.net/ORDO/Orphanet_117724) corroborate identity. Parent independently
verified main `488555581d3642ba24843fc05bcb6d6517dabcd9`: the YAML, notes and HTML
matched the local baseline, with no overlapping open ACAT1 PR. All 49 seeded source
assertions, including evidence, terms, references and flags, are preserved.

### Research execution and access

A genuine default Falcon attempt with Perplexity-lite fallback used writable per-process
UV tool/cache directories. Both invocations failed during dependency installation with
PyPI DNS errors after three retries (Falcon subprocess exit 2 after 8.5 seconds;
fallback exit 2 after 4.6 seconds; wrapper exit 1). No provider was reached, no provider
report was produced, and these notes are manual research. The concurrently run normal
publication command confirmed all eleven original PMIDs already cached. Logs:
`/tmp/ACAT1-falcon.log` and `/tmp/ACAT1-publications.log`.

All original cached PMID records and eight Reactome summaries were read. Abstract-only
records are not treated as full-text reviews. The [JCI primary PDF for PMID:1979337](https://www.jci.org/articles/view/114946/files/pdf)
exposed methods, results and discussion: pulse-labeled T2 was in the particulate fraction
while LDH was cytosolic; the authors interpreted this as mitochondrial import. This
supports the organelle term without assuming matrix resolution. The local cache remains
abstract-only. The original PMID:17371050 full article was not recovered. Its
[primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/17371050/) and the corresponding
results/discussion in [Meriläinen's author thesis](https://oulurepo.oulu.fi/bitstream/10024/35950/1/isbn978-951-42-9198-2.pdf)
were read: both reaction directions were measured, and mass spectrometry identified
acetyl-CoA and propionyl-CoA after branched-substrate cleavage. Racemate consumption
alone cannot establish recognition of both stereoisomers because the thesis discusses
possible interconversion under assay conditions. This thesis is not claimed as the
full original article. Correction to the earlier residue note: position 413 is Cys,
not His; the cached UniProt ACT_SITE annotation at 413 identifies proton transfer.

### Cholesterol-paper conflict: retain uncertainty, not a confident gene swap

PMID:32944968 full methods report the exact target sequence
`GCCACTAAGCTTGGTTCCATT`. The independent annotation-reviewer consultation recovered,
and this review independently checked, [Broad GPP's transcript/reagent table](https://portals.broadinstitute.org/gpp/public/trans/details?transName=NM_000019.4):
TRCN0000035583 has that target and a perfect SDR match to human ACAT1 transcript
NM_000019.4, gene 38. Broad reports no equal-or-better other-human-gene match for this
construct. This identifies the reported sequence, not independent verification of the
reagent actually used, its knockdown specificity, or an absence of off-target effects.

Thus the older claim that the paper only perturbed SOAT1/SOAT2 is not justified.
The human Calu-3 viral-entry and lipid-droplet findings do not alone show purified
mitochondrial thiolase catalyzing cholesterol esterification or acting in the ER.
Both experimental rows are now UNDECIDED. [GO:0034736](https://amigo.geneontology.org/amigo/term/GO%3A0034736)
requires the acyl-CoA/cholesterol esterification reaction. Cached model
`gocams/6796b94c00004996/6796b94c00004996-src.yaml` explicitly carries P24752 with
this MF and ER location from the same paper: shared provenance, not another assay.
No source or GO-CAM file was edited.

### Moonlighting and reference precision

PMID:27867011 full cached text was assessed with independent consultation. Its purified
ACAT1 assay follows acetoacetyl-CoA thiolysis at 303 nm; cellular Y407F and substrate
acetylation-site experiments link tetramer regulation to the PDHA1/PDP1 axis. Those
experiments are not themselves a direct purified protein-lysine transfer assay.
The paper attributes the earlier direct assignment to prior work. Reactome 9854415
instead cites Chen et al. 2021 for IDH2 K413; this is not the 2016 PDHA1/PDP1 source.
The 2021 primary experiment was not recovered. Matrix location can remain accepted
without endorsing all event mechanisms. The proposed gene-specific GO term was withdrawn:
[GO:0061733 protein-lysine-acetyltransferase activity](https://amigo.geneontology.org/amigo/term/GO%3A0061733)
already describes the chemistry. A question preserves the evidence gap; no NEW MF or
process is asserted from incomplete catalytic assessment.

### Propagation audit

Sixteen IBA/IEA rows have source-specific propagation assessments. GOA was consulted
only for provenance and joined by term, evidence and reference, not row number.
PAINT source entries contain PTN ancestors 000432378 (thiolase) and 000432235
(mitochondrion). Human descendants appearing in WITH/FROM are not circular evidence.
ARBA and InterPro rule internals were not reconstructed and are explicitly unresolved;
independent human evidence supports the accepted biochemical annotations.

Rat P17764 / ENSRNOP00000010573 is Acat1, RGD:2016, NCBI Gene 25014, as established
by the [NCBI/RGD record](https://www.ncbi.nlm.nih.gov/gene/25014) and
[Reactome cross-references](https://www.reactome.org/content/detail/R-RNO-70838).
Mouse Q8QZT1 / ENSMUSP00000034547 is Acat1, MGI:87870, as established by
[Reactome](https://www.reactome.org/content/detail/R-MMU-70838).
The rat record links specific donor terms to these primary records:

| Donor term | Evidence | Primary source | Access and assessment |
| --- | --- | --- | --- |
| CoA binding | IPI | [PMID:1672610](https://pubmed.ncbi.nlm.nih.gov/1672610/) | Abstract describes tight/covalent CoA modification of thiolase; human CoA-complex structures independently support ligand binding, without assuming the donor modification mechanism transfers. |
| Enzyme binding | IPI | [PMID:1684101](https://pubmed.ncbi.nlm.nih.gov/1684101/) | Partner and experiment inaccessible; UNDECIDED. |
| Identical protein binding; matrix | IPI; IDA | [PMID:11988101](https://pmc.ncbi.nlm.nih.gov/articles/PMC1222570/) | Abstract explicitly identifies matrix thiolase and oligomeric forms; full PDF not inspected. Human tetramer and curated matrix reactions corroborate. |
| Liver development | IEP | [PMID:5166591](https://pubmed.ncbi.nlm.nih.gov/5166591/) | Full source unavailable; donor identity resolved, participation unresolved. |
| Hormone response | IEP | [PMID:6144148](https://pubmed.ncbi.nlm.nih.gov/6144148/) | Experiment unavailable; UNDECIDED. |
| Starvation response | IEP | [PMID:2985752](https://pubmed.ncbi.nlm.nih.gov/2985752/) | Full primary source not recovered; a plausible fasting connection does not settle the transfer. |
| Adipose development | IEP | [PMID:2866764](https://pubmed.ncbi.nlm.nih.gov/2866764/) | Abstract measures developmental enzyme activity and tissue acetoacetate oxidation; full participation evidence unavailable. |
| Metanephric proximal convoluted tubule development | IEP | [PMID:7733320](https://pubmed.ncbi.nlm.nih.gov/7733320/) | Abstract measures postnatal enzyme activities and thyroid perturbation; it does not by itself establish thiolase-driven morphogenesis. |

All five contextual process transfers remain UNDECIDED pending primary interpretation.
This supersedes earlier confident judgments made without the term-specific donor chain.
One normal batch fetch was attempted for these eight additional PMIDs; its terminal
outcome is recorded below. No source text was manually placed in the publication cache.

### Core chemistry and localization decisions

Broad C-acetyltransferase/acyltransferase, mitochondrial and direct acetyl-/propionyl-CoA
product-process annotations describe genuine core activity at their source resolution.
They are accepted rather than called peripheral simply because more specific terms exist.
The two previous enzyme-core entries are consolidated, with both ketone-body catabolism
and L-isoleucine catabolism. The exact [GO:0003985 reaction](https://www.informatics.jax.org/vocab/gene_ontology/GO%3A0003985)
encodes the unbranched acetyl-CoA reaction; branched substrate specificity is stated
separately in core prose and the Reactome 70844 evidence.

CoA consumption/release direction is corrected: thiolysis consumes free CoA;
condensation releases it. [GO:0015937](https://flybase.org/reports/GO%3A0015937) does
not explicitly say de novo biosynthesis. The existing experimental biosynthetic-process
annotation is UNDECIDED pending clarification of cofactor regeneration versus biosynthesis,
rather than rejected on an invented definition. The broad CoA metabolic process is accepted.
The cached UniProt beta-oxidation statement is retained as a secondary short-chain
contribution, without claiming long-chain thiolysis. No redundant NEW process was added.

The urinary-exosome detections remain non-core with curator deference. Individual ACAT1
supplementary entries were not re-extracted; neither contamination nor a special
extracellular catalytic function was established. MitoCoP supports the curated HTP
mitochondrial assertion, without claiming independent re-extraction of its ACAT1 entry.
CLPXP/LONP1 event summaries describe broad substrate sets: location is accepted, but
ACAT1-specific degradation and protease function are not inferred. All reference findings
were reconciled with these source limits, including the prior misleading SOAT1-only and
IDH2/PDHA1 conflations.

Additional-source cache result: the normal eight-PMID batch exited 1 with
`<urlopen error [Errno 8] nodename nor servname provided, or not known>` for each
record; cached 0/8. The missing donor records are 1672610, 1684101, 11988101,
2866764, 5166591, 7733320, 6144148 and 2985752. Public primary reads described above
remain manual access, not local publication-cache contents. The unresolved rows do
not treat inaccessible donor papers as negative evidence. Targeted validation passes,
but it does not check these PubMed links in the notes; cache recovery remains explicit
follow-up. Original PMID and Reactome caches were unchanged.
