# AMT (Aminomethyltransferase, mitochondrial) — review notes

UniProt: P48728 (GCST_HUMAN). Gene AMT / GCST. HGNC:473. EC 2.1.2.10.
403 aa precursor; residues 1-28 mitochondrial transit peptide; mature chain 29-403.
Belongs to the GcvT family. PANTHER PTHR43757:SF16 (AMINOMETHYLTRANSFERASE, MITOCHONDRIAL).

## Function (verified)

AMT is the **T-protein (aminomethyltransferase)** of the mitochondrial **glycine cleavage
system (GCS)**, a four-protein multienzyme complex: P-protein (GLDC), T-protein (AMT),
L-protein (DLD), and H-protein (GCSH). The GCS catalyses the reversible oxidative
decarboxylation/degradation of glycine.

AMT catalyses the **third step**: it acts on the aminomethyl (methylamine) moiety of glycine
that is carried, after decarboxylation, on the reduced lipoate arm of H-protein
(the aminomethyl-dihydrolipoyl-GCSH intermediate). AMT **releases ammonia (NH3)** and
**transfers the remaining one-carbon (methylene) unit to tetrahydrofolate (THF), forming
(6R)-5,10-methylenetetrahydrofolate (5,10-CH2-THF)**, leaving GCSH in its dihydrolipoyl
(reduced-lipoate) form, which is subsequently reoxidised by the L-protein (DLD).
This THF-dependent reaction couples glycine catabolism to one-carbon/folate metabolism.

Catalytic activity (UniProt/RHEA:16945; EC 2.1.2.10):
N6-[(R)-S8-aminomethyldihydrolipoyl]-L-lysyl-[protein] + (6S)-5,6,7,8-tetrahydrofolate
= N6-[(R)-dihydrolipoyl]-L-lysyl-[protein] + (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + NH4(+)

[PMID:16051266 "T-protein, a component of the glycine cleavage system, catalyzes the formation of ammonia and 5,10-methylenetetrahydrofolate from the aminomethyl moiety of glycine attached to the lipoate cofactor of H-protein"]

Reactome R-HSA-5693977 ("AMT transfers NH2CH2 from GCSH:SAMDLL to THF") describes the same
reaction: AMT degrades the H-protein-bound aminomethyl moiety to ammonia + GCSH-reduced-lipoate,
with THF accepting the one-carbon unit to form 5,10-MTHF.

## Localisation (verified)

Mitochondrion / mitochondrial matrix. Nuclear-encoded, imported via an N-terminal transit
peptide (aa 1-28). Present in the high-confidence human mitochondrial proteome (MitoCoP,
PMID:34800366). UniProt: "SUBCELLULAR LOCATION: Mitochondrion".

## Structure (verified)

2.0 A crystal structure of human T-protein, free and bound to 5-CH3-THF (PDB 1WSR/1WSV;
PMID:16051266). Cloverleaf three-domain fold with a central folate-binding cavity; substrate
binding residues (UniProt BINDING 232, 261, 399). Disease residues cluster around the cavity.

## Disease (verified)

Deficiency of AMT causes **nonketotic hyperglycinemia (NKH) / glycine encephalopathy**
(Glycine encephalopathy 2, GCE2; MIM:620398), the second most common cause after GLDC
(P-protein). ~80% of NKH is GLDC (P-protein); the remainder are largely T-protein (AMT).
Many pathogenic missense variants (H42R, G47R, R94W, N145I, E211K, R222C, R265C, G269D,
D276H, R296C, R320H) reduce/abolish aminomethyltransferase activity.

[PMID:9600239 "Nonketotic hyperglycinemia (NKH) is caused by a mutation in the genes encoding the components of the glycine cleavage multi-enzyme system"]
[PMID:9600239 "T-protein activity was deficient in the liver specimen from one propositus"]

## Annotation review summary

- MF: GO:0004047 aminomethyltransferase activity — ACCEPT (multiple lines: EXP, IMP
  PMID:16051266; IBA; IEA EC/RHEA). This is the core molecular function.
- BP: GO:0019464 glycine decarboxylation via glycine cleavage system (IBA, IMP) and
  GO:0006546 glycine catabolic process (IEA, TAS) — ACCEPT. Core process.
- CC: GO:0005739 mitochondrion (IBA/IEA/IDA/HTP/IC/TAS) and GO:0005759 mitochondrial matrix
  (TAS) — ACCEPT. GO:0005960 glycine cleavage complex (IEA InterPro, part_of) — ACCEPT;
  T-protein is a constituent of the GCS complex.
- transaminase / aminotransferase keyword (GO:0008483) appears in UniProt DR line
  (IEA:UniProtKB-KW) from the "Aminotransferase" keyword but is NOT in the seeded GOA TSV,
  so it is not reviewed as an existing annotation. AMT is an aminomethyltransferase, not a
  classic PLP transaminase; the keyword-derived transaminase term would be an over-annotation
  if present.

## 2026-09-27 full source audit

This entry supersedes the earlier unqualified assay, step-number, variant and localization claims above. The review now separates what each primary source actually establishes from curator-supported assertions and database synthesis. All 17 original source assertions, four alternative-product records and 12 original reference identities are preserved. All 17 decisions remain ACCEPT; no NEW annotation or new core term is introduced. The single integrated core remains aminomethyltransferase activity within glycine cleavage, in the mitochondrial matrix and glycine cleavage system.

### Baseline and research provenance

The five canonical files exactly matched the independently captured main snapshot `fab4fc281b77ba8752eee20e62e271116908e88c`. HGNC:473 approves AMT; GCST and NKH are aliases. The coordinator's canonical/alias directory and open-PR preflight was clear. A byte-based baseline and immutable-source snapshot were saved before editing. No raw GOA, UniProt, publication, Reactome or PANTHER record was modified.

A genuine Falcon research launch with the documented installed matching deep-research-client 0.2.7rc1 override and perplexity-lite fallback failed on provider DNS/connectivity. It produced no research report; this is a manual review, not a generated provider report. In parallel, the ordinary `fetch-gene-pmids human AMT` command completed successfully, finding all four requested records already cached. Terminal logs are `tmp/AMT-full-review/deep-research.log` (exit 1) and `tmp/AMT-full-review/fetch-gene-pmids.log` (exit 0, 4/4). No forced re-fetch or source replacement occurred.

### Chemistry and primary evidence

- [PMID:16051266], DOI `10.1016/j.jmb.2005.06.056`: indexed PubMed and the original [RCSB 1WSR](https://www.rcsb.org/structure/1WSR)/[1WSV](https://www.rcsb.org/structure/1WSV) records independently verify identity and the human AMT construct. The deposited chain is 375 residues, derived from human P48728 and expressed in *E. coli*. The free structure is 2.0 Å; the 5-methyl-THF-bound structure is 2.6 Å. The bound ligand is a structural folate analogue, not the physiological 5,10-methylene product. The local publication contains the abstract, not full Methods or the complete variant activity table. The abstract explicitly describes aminomethyl transfer from the H-protein lipoate arm, ammonia release, and folate-dependent product formation. It also reports structural/mutational analyses of the folate-binding region. Mature Asp101 and Arg292 correspond to precursor Asp129 and Arg320 after the 28-residue targeting segment; these numbering schemes must not be mixed. UniProt independently attributes the Asp129 substitutions' loss of activity to this paper. The broad earlier list of variants above is not a claim that every variant was biochemically tested or abolished activity in this experiment. A peer independently read the same abstract and structural records; no full human 2005 assay recovery is claimed.
- [PMID:9600239], [primary PubMed](https://pubmed.ncbi.nlm.nih.gov/9600239/), DOI `10.1007/s004390050716`: the human kindred study measures deficient T-protein activity in liver from **one** affected propositus and describes H42R segregation among 26 relatives. At least 14 affected children are reported. Association and the patient-liver enzyme result support glycine catabolism; the abstract does not establish purified H42R kinetic parameters or activity for every disease variant. The historical estimate of the proportion of P- versus T-protein defects is not used as a current prevalence estimate in the description.
- [PMID:8188235], [primary PubMed identity](https://pubmed.ncbi.nlm.nih.gov/8188235/), DOI `10.1006/geno.1994.1007`: this is a human placental cosmid-library genomic study, including mapping and sequencing. Its accessible abstract identifies the T-protein but does **not** explicitly describe mitochondrial localization. Direct PubMed full-page access intermittently returned a browser challenge; the indexed primary title/identifier were retrieved. The original TAS location is retained with curator deference and independent HPA/UniProt support, not by pretending the genomic abstract contains a localization assay. The cached record lists a correction in *Genomics* 1994 Apr;20(3):519. Targeted searches and the original publisher's issue URL did not establish a separate correction PMID or recover the notice body (publisher 403). No identifier, correction content or biological effect is guessed. No genomic mapping conclusion from this paper is needed for the core enzyme assignment.
- [PMID:34800366], [primary PubMed](https://pubmed.ncbi.nlm.nih.gov/34800366/), DOI `10.1016/j.cmet.2021.11.001`, PMC8664129: the cached full XML includes actual Results/Methods describing subcellular fractionation and mitochondrial importomics in human HEK293T, HeLa, Huh7 and U2OS cells. The MitoCoP aggregate comprises 1,134 protein-coding genes, but the cached text has no AMT/P48728-specific result and the exact supplementary target row was not recovered. The seeded HTP localization is accepted with curator deference plus independent human localization evidence. No AMT peptide count, quantitative abundance or matrix-specific detection is inferred from the proteome-wide result. Its local full-text flag stays true; the other three papers remain abstract-only.

AMT directly catalyzes the folate-dependent conversion **after** GLDC decarboxylation; calling it unconditionally the “third step” was ambiguous. Reactome enumerates its reaction second among the three enzyme transformations. The carrier H-protein is lipoylated; this does not make AMT a lipoyl carrier or establish AMT PLP binding. The precise product is 5,10-**methylene**-THF. Reactome's summary uses “methyl group” shorthand, so the detailed authored chemistry follows the primary abstract and RHEA/GO reaction. GLDC decarboxylation and DLD reoxidation are assigned to those proteins. Glycine-catabolism participation is supported by AMT's own catalytic work, not merely by a knockout or disease phenotype.

### Localization and source-resolution checks

The live R-HSA-5693977 Catalyst Activity field reads: aminomethyltransferase activity of AMT [mitochondrial matrix].

This short access receipt is a transcription of the official human reaction page, not an independent experiment or a claim that the normal cached summary includes its structured participant fields. The live page explicitly locates the AMT catalyst, lipoyl-GCSH substrate and folate participants in the matrix. The cached summary independently supplies the reaction chemistry. The [R-HSA-6783984](https://reactome.org/content/detail/R-HSA-6783984) human glycine-degradation pathway lists AMT as the T component and includes the specific AMT child reaction. Both existing normal Reactome caches were read and remain unchanged; unused bibliography of those records was not recursively promoted into additional cited experiments.

The directly read [Human Protein Atlas AMT page](https://www.proteinatlas.org/ENSG00000145020-AMT/subcellular) reports supported mitochondrial localization with antibody HPA005566. HeLa and Hep-G2 list mitochondria plus nucleoplasm; U2OS is listed as no staining in the assay shown. The additional nucleoplasmic staining means that exclusive mitochondrial localization is not established. It does not negate the main mitochondrial result. No new nucleoplasm annotation is proposed from this bounded observation alone; isoform, specificity and physiological function remain questions. The seeded HPA, PAINT, vocabulary-mapping, HTP, IC and historical TAS organelle rows retain their original resolution rather than being mechanically changed to matrix.

### PAINT, ontology and synthesis

The local PTHR43757 metadata identifies the family as AMINOMETHYLTRANSFERASE. Its cached PAINT table explicitly contains IBD node PTN000354058 for GO:0004047 and IBD node PTN000354060 for GO:0019464 and GO:0005739. Human P48728 appears as legitimate experimental descendant support. Each structured IBA assessment names only its ancestral PTN. The complete phylogeny/MSA was not reconstructed, and donor count or target self-evidence is not treated as a weakness. The InterPro proximate source is IPR006223. Full ARBA00085463 rule conditions were not recovered; the target catalytic evidence supports its broad catabolic assertion without pretending the rule itself was experimentally inspected.

Live [GO:0004047](https://amigo.geneontology.org/amigo/term/GO:0004047) defines the exact carrier-bound aminomethyl/THF reaction and cross-references RHEA16945 and EC2.1.2.10. [GO:0019464](https://amigo.geneontology.org/amigo/term/GO:0019464) explicitly encompasses oxidative cleavage by the enzyme system and is a child of glycine catabolic process. [GO:0005960](https://amigo.geneontology.org/amigo/term/GO:0005960) defines the glycine-cleavage protein complex, including P, H, T and L components; this is not a requirement for an invariant intact heteromer in every assay. An exact P48728 lookup in the local GO-CAM index returned no target model. No missing-model claim or NEW assertion follows from that absence.

The earlier speculative GO:0008483 discussion is outside the 17 seeded assertions and is not used to manufacture a removal or a replacement. Likewise, no separate folate-binding annotation or redundant one-carbon process is added merely to restate the existing catalytic mechanism. The four machine-recorded isoforms are retained; the mature canonical crystal construct does not establish equal activity or localization of all alternative products.

### Citation census and checks

The authored YAML and complete historical-plus-appended notes cite four distinct PMIDs (16051266, 34800366, 8188235, 9600239), all normal caches present, and two Reactome IDs (5693977, 6783984), both present. Each explicit DOI maps to one of those same PMIDs. PMC8664129 maps to PMID34800366. RCSB1WSR/1WSV point to PMID16051266. No genuine provider report exists to extend the census. Unused UniProt bibliography and references merely listed on a visited webpage are not asserted as new evidence. The unnumbered 1994 correction remains an explicitly unresolved source-access limit rather than a fabricated cache request.

The full `just validate human AMT` run passed with no curation warnings. Source preservation and 33 case-sensitive, whitespace-normalized supporting quotations passed independently; no quotation required case folding. Rendering and scaffolded-history validation passed. Status is COMPLETE because all seeded decisions and reference assessments are finished and the actual citation census is closed; the explicit assay-access limits above remain part of the scientific assessment. No separate full-text cache is claimed for the three abstract-only papers.
