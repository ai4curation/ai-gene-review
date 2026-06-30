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
