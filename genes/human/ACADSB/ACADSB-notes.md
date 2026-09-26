# ACADSB (P45954) — curation notes

Human short/branched-chain specific acyl-CoA dehydrogenase, mitochondrial (SBCAD;
2-methylbutyryl-CoA dehydrogenase; ACADSB). HGNC:91, gene ID 36, chromosome 10.
UniProt reviewed entry P45954; 432 aa precursor with an N-terminal mitochondrial
transit peptide (residues 1..33) cleaved to give the mature matrix enzyme.

## Identity and family

- Member of the acyl-CoA dehydrogenase (ACAD) family: "Belongs to the acyl-CoA
  dehydrogenase family." [file:human/ACADSB/ACADSB-uniprot.txt "Belongs to the acyl-CoA dehydrogenase family."].
- FAD-dependent flavoprotein oxidoreductase; EC 1.3.8.1 (short-chain acyl-CoA:ETF
  oxidoreductase) and EC 1.3.8.5 (2-methylbutanoyl-CoA:ETF oxidoreductase). Recombinant
  human SBCAD was originally isolated as "a novel member (gene symbol ACADSB) of the ACD
  gene family" with "significant sequence similarity to other members of the acyl-CoA
  dehydrogenase family, with the greatest homology (38%) to the short chain acyl-CoA
  dehydrogenase" [PMID:7698750 "with the greatest homology (38%) to the short"].

## Molecular function (core)

- Catalyzes the FAD-dependent, ETF-coupled alpha,beta-dehydrogenation of acyl-CoA
  thioesters. UniProt: "catalyzes the proR-proR stereospecific alpha,beta-dehydrogenation
  of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their
  physiologic electron acceptor" [file:human/ACADSB/ACADSB-uniprot.txt "physiologic electron acceptor"].
- Substrate specificity: short and branched chain acyl-CoAs. Recombinant human protein has
  "activity toward the short branched chain acyl-CoA derivatives ((S)-2-methylbutyryl-CoA,
  isobutyryl-CoA, and 2-methylhexanoyl-CoA), as well as toward the short straight chain
  acyl-CoAs (butyryl-CoA and hexanoyl-CoA)" [PMID:7698750 "((S)-2-methylbutyryl-CoA, isobutyryl-CoA, and 2-methylhexanoyl-CoA)"].
- The physiologically important reaction is dehydrogenation of (S)-2-methylbutyryl-CoA to
  tiglyl-CoA in isoleucine catabolism. Reactome: "Mitochondrial 2-methyl branched-chain
  acyl-CoA dehydrogenase (ACADSB) catalyzes the reaction of alpha-methylbutyryl-CoA and FAD
  to form 'tiglyl-CoA and FADH2" [file:reactome/R-HSA-70800.md].
- FAD cofactor: UniProt COFACTOR "Name=FAD" with multiple FAD-binding site features
  (BINDING 174..183, 207..209, 319, 330, 387..391, 416..418) established by the 2JIF crystal
  structure. FAD binding is a core molecular function (GO:0050660), consistent with the
  flavoprotein family assignment.
- Homotetramer: "Homotetramer." [file:human/ACADSB/ACADSB-uniprot.txt "Homotetramer."], confirmed
  by the crystal structure (2JIF; SGC) and by PMID:11013134 ("both wild-type proteins are
  imported into mitochondria and form tetramers"). This is the basis of the GO:0042802
  identical protein binding IDA annotation (self-association into the homotetramer).

## Substrate breadth / promiscuity

- SBCAD is catalytically promiscuous within the short/branched class: 2-methylbutanoyl-CoA
  (the physiological substrate), 2-methylpropanoyl-CoA (isobutyryl-CoA), 2-methylhexanoyl-CoA,
  butanoyl-CoA, hexanoyl-CoA, and the xenobiotic valproyl-CoA. Kinetics (UniProt): KM 2.7 uM
  for (2S)-2-methylbutanoyl-CoA vs 36 uM for hexanoyl-CoA vs 130 uM for 2-methylpropanoyl-CoA,
  i.e. the branched-chain isoleucine substrate is strongly preferred.
- Hexanoyl-CoA (C6) is a straight-chain substrate at the boundary between short and medium
  chain; GOA carries a RHEA-derived GO:0070991 "medium-chain fatty acyl-CoA dehydrogenase
  activity" IEA from the hexanoyl-CoA reaction (RHEA:43464). This is a real in vitro activity
  but not the biological role of the enzyme (over-annotation of substrate breadth).
- Valproyl-CoA: SBCAD is "the most probable candidate for the first dehydrogenation step of
  VPA beta-oxidation" and is competitively inhibited by valproyl-CoA [PMID:21430231 "the first
  dehydrogenation step of VPA"; "did inhibit SBCAD activity by a purely competitive mechanism"].
  Xenobiotic/drug metabolism, not a distinct GO function beyond the dehydrogenase activity.

## Biological process (core)

- L-isoleucine catabolism. UniProt PATHWAY "Amino-acid degradation; L-isoleucine degradation"
  and FUNCTION: "Plays an important role in the metabolism of L-isoleucine by catalyzing the
  dehydrogenation of 2-methylbutyryl-CoA, one of the steps of the L-isoleucine catabolic
  pathway" [file:human/ACADSB/ACADSB-uniprot.txt "one of the steps of the L-isoleucine catabolic"].
- Genetic evidence for the isoleucine-specific role: a patient with isolated
  2-methylbutyrylglycinuria had a homozygous SBCAD exon-10-skipping mutation, and study showed
  "it results in an isolated defect in isoleucine catabolism" [PMID:11013134 "an isolated defect
  in isoleucine catabolism"]. This paper also distinguishes SBCAD (isoleucine) from ACAD8/IBD
  (valine): "indicate that ACAD-8 is a mitochondrial enzyme that functions in valine metabolism".
- Fatty acid metabolic process: SBCAD also acts on short straight-chain acyl-CoAs (butyryl-CoA,
  hexanoyl-CoA); UniProt also lists PATHWAY "Lipid metabolism; mitochondrial fatty acid
  beta-oxidation" [file:human/ACADSB/ACADSB-uniprot.txt "mitochondrial fatty acid beta-oxidation"].
  This is a genuine but secondary/non-core contribution relative to isoleucine catabolism.

## Cellular location (core)

- Mitochondrial matrix. UniProt SUBCELLULAR LOCATION "Mitochondrion matrix"
  [file:human/ACADSB/ACADSB-uniprot.txt "Mitochondrion matrix"]. Consistent with the cleaved
  N-terminal transit peptide (1..33) and with IDA mitochondrial localization (PMID:11013134),
  HPA IDA (GO_REF:0000052), and mitochondrial proteome MS (PMID:34800366). Reactome TAS
  annotations place it in the mitochondrial matrix (GO:0005759).

## Disease

- Short/branched-chain acyl-CoA dehydrogenase deficiency (SBCADD; 2-methylbutyryl-CoA
  dehydrogenase deficiency), MIM:610006, autosomal recessive. UniProt DISEASE: "a defect in
  catabolism of L-isoleucine which is characterized by an increase of 2-methylbutyrylglycine
  and 2-methylbutyrylcarnitine in blood and urine" [file:human/ACADSB/ACADSB-uniprot.txt
  "2-methylbutyrylglycine and 2-methylbutyrylcarnitine in"]. First case: PMID:10832746
  (L222F variant; "absence of enzyme activity for the 2-MBCDase protein expressed in
  Escherichia coli"). Molecular basis / first gene mutation: PMID:11013134. Detected on
  newborn screening as elevated C5 (2-methylbutyryl) acylcarnitine; frequently benign and
  notably common in Hmong populations (background, not in cached publications).

## Notes on the annotation set (GOA)

- Multiple redundant MF annotations to GO:0003853 (short-chain 2-methyl fatty acyl-CoA
  dehydrogenase activity) from EXP/IDA (PMID:7698750, 10832746, 11013134, 21430231) — this is
  the correctly specific term for the isoleucine step and is the primary core MF. IEA to the
  same term (GO_REF:0000120, Rhea/EC 1.3.8.5) corroborates.
- GO:0016937 (short-chain fatty acyl-CoA dehydrogenase activity) IDA (PMID:7698750) captures
  the straight-chain butyryl/hexanoyl activity — a genuine secondary MF.
- GO:0003995 (acyl-CoA dehydrogenase activity) IBA/IEA is the correct general parent; keep as
  non-core because more specific children are annotated.
- GO:0016627 (oxidoreductase, CH-CH group of donors) IEA is a very general grandparent —
  over-annotation.
- GO:0070991 (medium-chain fatty acyl-CoA dehydrogenase activity) IEA from the hexanoyl-CoA
  Rhea reaction — over-annotation of substrate breadth (C6 boundary), not the biological role.
- GO:0006631 (fatty acid metabolic process) IDA (PMID:7698750) / IEA and GO:0046395
  (carboxylic acid catabolic process) IEA are correct but non-core relative to isoleucine
  catabolism.
- Reactome TAS to GO:0005759 via R-HSA-9838081 / R-HSA-9838093 are "LONP1 degrades/binds
  mitochondrial matrix proteins" — these place ACADSB in the matrix only as a LONP1 substrate;
  the location call is correct but the process context is protein turnover, not SBCAD function.
</content>
</invoke>

## 2026-09-26 complete source and annotation re-review

This entry supersedes the earlier annotation conclusions above where they differ. The prior journal is retained. The scope was all 28 existing assertions (no NOT annotations and no proposed NEW rows), the three previous core-function entries, all five cached PMIDs, and all propagated-source identifiers. Seeded assertion fields and both alternative-product records were preserved. The resulting review contains 24 ACCEPT and four KEEP_AS_NON_CORE decisions, with one integrated enzymatic core.

### Identity, baseline and provenance

ACADSB is the canonical human symbol (HGNC:91; UniProt P45954; NCBI Gene 36). HGNC-attributed [ClinGen gene facts](https://search.clinicalgenome.org/kb/genes/HGNC:91) list SBCAD and ACAD7; Ensembl also exposes 2-MEBCAD. This is distinct from ACADS, ACAD8 and ACADM. The remote main revision checked was `21121fc735d20bcb2dbf8328aa82d5da30185e5e`; all five local ACADSB files matched their remote main blob identifiers. A GitHub open-PR search for ACADSB returned zero results at the baseline check. The initial YAML blob was `691bbbbc55ba2035e8eff56408601c1179b86879` (status INITIALIZED). Baseline files and hashes were retained separately for source-tuple and publication integrity checks.

The default genuine Falcon attempt ran with a 1200-second requested timeout and automatic perplexity-lite fallback, concurrently with publication caching. Both provider paths failed while bootstrapping `deep-research-client[cyberian]==0.2.7rc1`: PyPI DNS resolution failed after three retries. The Falcon backend and the fallback backend were never reached. This was neither a completed literature report nor a service timeout/quota result. No provider-named report was written or invented. `fetch-gene-pmids` completed with all five existing papers already cached and unchanged. A separate supported forced fetch of 11013134 and 12855692 to a temporary output directory failed DNS for both. The review therefore used cached material and directly inspected primary web sources; machine-owned cache files were not edited.

### Core chemistry and substrate scope

The principal physiological reaction is (S)-2-methylbutyryl-CoA to tiglyl-CoA in isoleucine degradation. The human recombinant-enzyme study explicitly reports branched and straight-chain substrates [PMID:7698750, cached abstract; "activity toward the short branched chain acyl-CoA derivatives"]. Human patient studies independently identify this particular metabolic block [PMID:10832746, cached abstract; "2-methylbutyryl-CoA dehydrogenase"; PMID:11013134, abstract and accessible methods/figures, [PubMed](https://pubmed.ncbi.nlm.nih.gov/11013134/)]. ACADSB itself performs the dehydrogenation, so its existing isoleucine process annotation is supported by participation as well as perturbation. The reaction is one step of the pathway; the earlier unsupported wording calling it the committed step was removed.

Two ontology distinctions materially change the earlier interpretation:

- [GO:0016937](https://amigo.geneontology.org/amigo/term/GO%3A0016937) specifies a short aliphatic chain, less than six carbons, without requiring an unbranched substrate. Its specific 2-methyl child captures the core ACADSB reaction. It is therefore not a separate exclusively straight-chain mechanism. Butyryl activity also supports it; hexanoyl activity does not supply the short-chain example under this GO boundary.
- [GO:0070991](https://amigo.geneontology.org/amigo/term/GO%3A0070991) covers 6–12 carbons. The original human hexanoyl-CoA activity and the human UniProt RHEA:43464 record fall within this definition. The prior OVER decision based on a C6 boundary and enzyme name was not justified. KEEP_AS_NON_CORE records the real secondary molecular activity without asserting major physiological medium-chain oxidation or activity on every substrate in that size interval.

The butyryl evidence is assay-dependent. PMID:7698750 reports recombinant human activity. The accessible figure 3 caption of PMID:11013134 reports no butyryl or isovaleryl activity above the control background in the transfected COS-7 experiment. That paper's methods used cleared cell lysates, added FAD, ferricenium acceptor and HPLC product detection. Neither result alone justifies a universal assertion about all assay systems. The two fatty-acid metabolic process annotations remain non-core: the positive substrate chemistry supports retention, while the papers examined do not establish the magnitude of ACADSB-dependent whole-cell fatty-acid flux. The null COS-7 result is not treated as disproving every earlier activity result or all physiological contribution.

The 2011 study directly assayed purified human SBCAD with 2-methylbutyryl-CoA, in addition to characterizing valproyl-CoA turnover and inhibition [PMID:21430231, [PubMed figures 3–5](https://pubmed.ncbi.nlm.nih.gov/21430231/); cached introduction/discussion]. It supports the catalytic core. Its discussion explicitly leaves clinical toxicity causation unresolved; no toxicity, drug-response or new xenobiotic process annotation is proposed. The original 2003 substrate-specificity paper [PMID:12855692, [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/12855692/)] reports differences between rat and human substrate preference despite high sequence identity. Its full paper/cache was not recovered, so exact kinetic tables, catalytic efficiencies and residue-level mechanistic conclusions are not incorporated into the review. In particular, Km alone is not used to rank catalytic efficiency, and the rat-inferred human UniProt (2R)-substrate reaction is not promoted into an experimentally tested human core.

### Compartment, assembly and structural evidence

PMID:11013134 figure 4 details import of in-vitro-translated human precursor into isolated **rat mitochondria**, processing and native PAGE assembly. This directly supports human-protein mitochondrial targeting and tetramers in that experimental setting. The accessible immunostaining-method paragraph describes ACAD8, not an additional ACADSB microscopy experiment. The mitochondrial-matrix annotation also relies on curated UniProt and Reactome compartment knowledge; organelle import is not described as microscopy resolving the matrix.

The primary [human 2JIF structure](https://www.rcsb.org/structure/2JIF) has a D2 homotetramer biological assembly, with FAD modeled for each chain. This independently corroborates cofactor binding and oligomerization. The identical-protein-binding row is kept as a non-core positive self-association observation. FAD binding is part of the same dehydrogenase mechanism, not a second independent core function. The construct truncation discussed by Reactome is not used to infer a physiological targeting-peptide cleavage position.

General mitochondrial location, acyl-CoA dehydrogenase activity, CH-CH oxidoreductase activity and carboxylic-acid catabolism are core-compatible annotations even when more specific descendants are present. Their breadth alone does not warrant non-core or over-annotated status. Nine previous NON_CORE decisions and one previous OVER decision were changed to ACCEPT on that basis, with source-specific biological support.

### Source access and propagated annotations

- PMID:7698750 and PMID:10832746: cached abstracts expose the relevant human assays; full papers were not recovered. Original IDA/EXP assertions and explicit abstract findings support the judgments; no unobserved assay details are invented.
- PMID:11013134: the cache's alleged partial-PDF body is download-page boilerplate, not article text. PubMed abstract and figure captions are accessible. Portions of the primary PMC introduction/methods were read, but later requests returned a browser check before a complete full-paper read. The YAML explicitly records this access limit.
- PMID:21430231: the cache claims full text but contains the abstract, introduction and discussion without methods, results or tables. PubMed figure captions were inspected independently. Conclusions are limited to those accessible components.
- PMID:34800366: the full main mitochondrial proteomics article is cached and was inspected. The ACADSB-specific supplementary measurement was not independently extracted. The HTP mitochondrial row is accepted with curator deference and separate direct import evidence; it is not claimed to establish matrix resolution.
- Reactome R-HSA-70800 directly describes the ACADSB-catalyzed matrix reaction. R-HSA-9838081 and R-HSA-9838093 are broad LONP1 turnover/binding events whose cached summaries do not name ACADSB. The matrix locations are retained independently; these rows are not extended into individually demonstrated ACADSB-LONP1 assays or a new proteolytic function of ACADSB.

All 13 IBA/IEA rows now carry propagation_review with traced source_entities. The IBA sources are ancestral nodes PTN000744030 and PTN000097586. The target's own experimental evidence among descendants is legitimate, not circularity; no independent reconstruction of the full tree/MSA is claimed. InterPro matches support broad catalytic/cofactor architecture, not arbitrary family-wide substrate transfers. Rhea/EC entries were read in the human UniProt catalytic records, distinguishing stereospecific 48256, unspecified 43780, isobutyryl 44180, butanoyl 24004, generic short-chain 47196 and hexanoyl 43464. ARBA rule identifiers are traced but detailed predicates were not inspected, so their source statuses remain UNRESOLVED even where independent human biology supports ACCEPT or NON_CORE. SL-0170 maps the explicit curated matrix statement; UniPathway UPA00364 maps the isoleucine-degradation role.

No new annotation was needed. The cached GO-CAM index has no ACADSB/P45954 hit; no missing model was interpreted as a curation gap. The two prior additional core entries were consolidated into the single enzyme mechanism. Disease context is limited to the established biallelic biochemical defect; the earlier uncited epidemiological and generalized benignity statements are not carried into the standalone description.
