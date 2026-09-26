# ACAN (human aggrecan) — curation notes

UniProt P16112. HGNC:319. PANTHER PTHR22804 (hyaluronan-binding proteoglycan / lectican family:
ACAN, VCAN, NCAN, BCAN plus the HAPLN link proteins).

## What the protein is

A very large secreted chondroitin-sulfate proteoglycan with a tridomain architecture: an N-terminal
G1 (Ig + two Link modules) that binds hyaluronan, a G2 (two further Link modules), a huge central
keratan-sulfate/chondroitin-sulfate attachment region, and a C-terminal G3 (EGF + C-type lectin +
CCP/Sushi).

[file:human/ACAN/ACAN-uniprot.txt "CC   -!- DOMAIN: Two globular domains, G1 and G2, comprise the N-terminus of the"]

[file:human/ACAN/ACAN-uniprot.txt "CC   -!- FUNCTION: This proteoglycan is a major component of extracellular"]
[file:human/ACAN/ACAN-uniprot.txt "CC       resist compression in cartilage. It binds avidly to hyaluronic acid via"]

Secreted; UniProt subcellular location is extracellular matrix, and expression is essentially
restricted to cartilage plus a distinct CNS pool in perineuronal nets.

[file:human/ACAN/ACAN-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Secreted, extracellular space, extracellular"]
[file:human/ACAN/ACAN-uniprot.txt "CC       (PubMed:36213313). Restricted to cartilage (PubMed:7524681)."]

## Core biology

**Aggregate formation is the function.** Many aggrecan monomers bind a single hyaluronan filament
through G1, each junction stabilised by a HAPLN link protein, generating >200 MDa assemblies. The
dense negative charge of the ~100 chondroitin-sulfate chains draws in water; the resulting swelling
pressure, restrained by the collagen II network, is what makes cartilage resist compression.

[PMID:25701227 "is the principal load-bearing proteoglycan of cartilage"]
[PMID:25701227 "These large aggregates generate a densely-packed, hydrated gel enmeshed in a network of reinforcing collagen fibrils and other proteoglycans"]
[PMID:25701227 "The G1/hyaluronan/link protein ternary complex is very stable thereby immobilizing the aggrecan into enormous complexes that maintain a stable network and provide mechanical properties to cartilage."]
[PMID:27068509 "Negatively charged glycans on the surface of aggrecan attract water and therefore confer resistance to compression."]

**Hyaluronan binding is now structurally and biophysically nailed down for the human protein.**
Otsuka et al. 2025 solved the cocrystal structure of the human ACAN G1 region with an HA
decasaccharide and measured the affinity by biolayer interferometry. This matters for curation:
GOA still carries hyaluronic acid binding only as an InterPro IEA.

[PMID:40273987 "Amino acid numbering corresponds to human ACAN (UniProt ID# P16112)"]
[PMID:40273987 "We demonstrate that the single immunoglobulin domain and the two Link modules that comprise the G1 region form a single structural unit, and that HA is clamped inside a groove that spans the length of the tandem Link domains."]
[PMID:40273987 "In these experiments, ACAN binds to immobilized HA with an affinity of 234 nM, which is consistent with the value of 226 nM reported in an earlier study using surface plasmon resonance"]

**The G3 C-type lectin binds other matrix proteins.** Tenascins, fibulins, sulfated glycolipids.
Human missense variants in this repeat cause familial osteochondritis dissecans and both reduce
secretion and reduce ligand binding.

[PMID:25701227 "Moreover, the G3 domain of aggrecan interacts with tenascins, fibulins and sulfated glycolipids"]
[PMID:20137779 "Binding studies with recombinant mutated and wild-type G3 proteins showed loss of fibulin-1, fibulin-2, and tenascin-R interactions for the V2303M protein."]
[PMID:35338222 "The variant proteins also showed decreased binding to known cartilage extracellular matrix ligands."]
[PMID:35338222 "Functional studies showed that neither recombinant variant proteins, nor full-length variant aggrecan proteoglycan from heterozygous patient cartilage, were secreted to the same level as wild-type aggrecan."]

**COMP is a validated partner.** Solid-phase binding, calcium-dependent on COMP's side, mediated
partly through aggrecan's GAG chains.

[PMID:17588949 "Using a solid-phase binding assay, we have shown that COMP/TSP5 can bind aggrecan."]
[PMID:17588949 "Soluble glycosaminoglycans (GAGs) partially inhibited binding, suggesting that the interaction was mediated in part through aggrecan GAG side chains."]

**The CNS pool is perineuronal nets.** Aggrecan is the lectican most specific to PNNs, and human
G1 and G1-G2 fragments bind PNNs on cortical neurons. Notably, HA binding contributes to but is not
required for PNN incorporation, so there is a second, still-unidentified anchoring activity.

[PMID:25701227 "Aggrecan is also expressed in the brain, and unlike other hyalectans, is expressed primarily in the perineuronal nets"]
[PMID:40273987 "both fragments of ACAN bound highly and very specifically to PNNs on cultured cortical neurons"]
[PMID:40273987 "Thus, these results suggest that ACAN can be recruited into PNNs independently of its HA-binding activity."]

**Aggrecan is a protease substrate, not a protease.** The interglobular domain between G1 and G2
carries the aggrecanase (ADAMTS4/5) site; cleavage at Glu373-Ala374 releases the GAG-bearing bulk of
the molecule into synovial fluid in osteoarthritis, leaving the G1 tethered to hyaluronan.

[PMID:1569188 "This NH2 terminus results from cleavage of the human aggrecan core protein at the Glu 373-Ala 374 bond within the interglobular domain between the G1 and G2 domains."]
[PMID:25701227 "An interglobular region, between G1 and G2, has a rod-like structure and harbors several protease-sensitive sites involved in the partial degradation of aggrecan in arthritis and other inflammatory diseases."]
[file:human/ACAN/ACAN-uniprot.txt "CC       stages of human osteoarthritis is the result of cleavage by"]

## WITH/FROM resolution (the highest-yield check)

IPI partners:

| accession | gene | verdict |
|---|---|---|
| UniProtKB:P49747 | COMP | real, direct solid-phase binding (PMID:17588949); an ECM ligand |
| UniProtKB:P05067 | APP | yeast-two-hybrid neurodegeneration interactome screen (PMID:32814053); no orthogonal validation, no functional follow-up |

IBA donors (resolved via the Alliance API):

| id | gene | species |
|---|---|---|
| MGI:MGI:99602 | Acan | mouse |
| MGI:MGI:1096385 | Bcan | mouse |
| MGI:MGI:104694 | Ncan | mouse |
| MGI:MGI:1337006 | Hapln1 | mouse |
| MGI:MGI:2679531 | Hapln4 | mouse |
| RGD:68358 | Acan | rat |
| RGD:2194 | Bcan | rat |
| RGD:619940 | Vcan | rat |
| RGD:619941 | Ncan | rat |
| ZFIN:ZDB-GENE-030131-2185 | vcanb | zebrafish |

Every IBA row includes at least one true ACAN ortholog (mouse or rat Acan), so none of them is a
pure paralog transfer. The problems that remain are term-scoping, not donor choice.

## Annotation problems found

1. **`involved_in GO:0006508 proteolysis` (NAS, PMID:1569188) is backwards.** The cited paper shows
   aggrecan being *cleaved* by a cartilage proteinase. Being a substrate is not participating in
   proteolysis; the agents are ADAMTS4/ADAMTS5 and the MMPs. Substrate-as-agent role conflation.
2. **`involved_in GO:0007155 cell adhesion` (IEA, InterPro:IPR000538).** The Link-domain family
   mapping carries both hyaluronic acid binding and cell adhesion. The cell-adhesion half comes from
   the cell-surface HA receptors in the family (CD44, TSG-6), not from the secreted lecticans.
   Aggrecan is not a cell adhesion molecule and has no membrane anchor.
3. **`is_active_in GO:0045202 synapse` (IBA).** GO deliberately places perineuronal net outside the
   synapse: GO:0072534's ancestors run perisynaptic extracellular matrix (GO:0098966) →
   synapse-associated extracellular matrix (GO:0099535) → specialized extracellular matrix
   (GO:0140047)/extracellular matrix, and GO:0045202 is not among them (checked via QuickGO
   `/ontology/go/terms/GO:0072534/ancestors`). The same IBA batch already gives the precise term.
4. **Reactome reaction-level export dominates the record.** 14 of 40 rows are `located_in Golgi
   lumen` and 6 are `located_in extracellular region`, one per keratan-sulfate biosynthesis reaction.
   Five of the Golgi rows come from *defective*-enzyme disease reactions (R-HSA-3656230,
   R-HSA-3656258, R-HSA-3656269, R-HSA-9035949, R-HSA-9035950), where the biology being modelled is
   a congenital disorder of glycosylation, not aggrecan function.
5. **No correct biological process is annotated at all.** After removing proteolysis and cell
   adhesion, GOA's only BP terms are two broad development terms. Nothing states that aggrecan
   builds the matrix — extracellular matrix organization (GO:0030198) / assembly (GO:0085029) is the
   obvious gap.
6. **`GO:0005540 hyaluronic acid binding` is still only IEA** despite a 2025 human cocrystal
   structure and BLI affinity measurement (PMID:40273987). Straightforward IDA/IPI upgrade.
7. UniProt's DR block lists `GO:0005615 extracellular space` (IBA), `GO:0030246 carbohydrate binding`
   and `GO:0046872 metal ion binding` (both `IEA:UniProtKB-KW`), none of which appear in the GOA TSV
   snapshot. The keyword-derived pair is expected — GO_REF:0000043 SPKW annotations were withdrawn.

## Things deliberately *not* annotated

- The three UniProt DISEASE entries (SEDK, SEMDAG, SSOAOD) are disease associations, not GO
  processes. Short stature is a phenotype of haploinsufficiency.
- The affinage narrative is dominated by *regulators of ACAN transcription* — SOX9, the SOX trio,
  SHOX2, TET1, SIRT1, HDAC2, miR-140, mTOR/4E-BP1. Being a transcriptional target of SOX9 is not an
  ACAN function; those findings belong on the regulators.
- Two affinage findings rest on bioRxiv preprints with no PMID. One of them (the G1-HA cocrystal /
  PNN integration study) has since been published as PMID:40273987 and is used here in its published
  form; the other (Amigo2-Acan CA2 conditional knockout) has not been, and is not used.

## 2026-09-26 cached-source re-audit

This section supersedes conflicting interpretations in the earlier notes above. The prior review was already COMPLETE; this is an audit of its evidence and reasoning, not a new seed. No new provider output was requested or authored: the existing genuine affinage report, UniProt record, GOA-derived YAML, nine cached publications, and available Reactome records were inspected. The annotation-reviewer and core-function-synthesizer criteria were applied directly.

### Baseline and scope

At the start of the audit, the local review exactly matched GitHub main blob `c895b62b3f46eccc3e98fd8229faccee05c3d6ac`. Main resolved to `6455f59face473d84f2976a81c54aa47df26f398`, and the GitHub open-PR search returned no ACAN PR. The baseline contained 40 source rows plus one previous reviewer-authored NEW row. Baseline validation passed with the generic-protein-binding policy warning and an advisory that no annotation cited the provider report.

All 40 source rows retain their original term, evidence code, reference and other source fields. The previous NEW GO:0085029 row was withdrawn; no source annotation was deleted. The final actions are 8 ACCEPT, 21 KEEP_AS_NON_CORE, 8 MODIFY, 1 REMOVE and 2 UNDECIDED. No NEW annotation is proposed.

### Biological corrections

- **Cell adhesion:** the old REMOVE rationale incorrectly required a membrane anchor and described soluble TSG-6 as a cell-surface protein. The GO definition includes adhesion to extracellular substrates. The primary [CD44-aggrecan study](https://pubmed.ncbi.nlm.nih.gov/11222505/) reports binding of CD44-positive cells and soluble CD44 to immobilized rat chondrosarcoma and bovine cartilage aggrecan. Blocking and enzyme-treatment results implicate chondroitin sulfate chains. This contradicts categorical exclusion of aggrecan from adhesion, but does not directly validate the human Link-domain mapping. The source inference is now UNDECIDED. The identifier, title and abstract were verified; the full study was not fully recovered. A normal `fetch-pmid 11222505` attempt failed DNS and created no cache. The uncached reference is explicitly flagged and must be cached normally before completion of publication requirements.
- **APP interaction:** the cached [PMID:32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/) is abstract-only. UniProt records APP as the partner with three experiments. The abstract describes both systematic screening and literature integration; it cannot establish lack of replication or orthogonal validation for this pair. Publisher and institutional full-text routes were located but could not be opened successfully. The row becomes UNDECIDED and the unsupported LOW_QUALITY judgment is withdrawn. Generic protein binding is uninformative, not inherently over-annotation; no more specific function is invented from the interaction.
- **COMP versus G3 binding:** full cached PMID:17588949 identifies the signature domain of **COMP**, and implicates aggrecan glycosaminoglycan chains. It does not localize this interaction to aggrecan G3. The description, core-function synthesis and IPI refinement now separate this interaction from G3 binding to tenascins/fibulins. PMID:35338222 tests G3 interaction with fibulin-1, tenascin-C and tenascin-R; it does not establish a G3-matrilin interaction. The COMP Reactome record lists matrilins as additional COMP partners, not as proof that aggrecan binds matrilins.
- **Species and disease:** the Introduction of full cached PMID:35338222 explicitly assigns complete-deficiency lethality to mouse, cattle and chick. Its human cases include dominant disorders and recessive SEMD. The prior description inappropriately converted animal lethality into a human null-allele dosage series. The corrected description distinguishes these observations.
- **Gel phase:** [GO:0140150](https://zfin.org/GO:0140150) describes an interstitial hydrogel containing hyaluronan and proteoglycans. PMID:25701227 directly describes aggrecan aggregates as a hydrated cartilage gel. Cartilage is connective tissue; being specialized matrix does not establish disjointness from interstitial matrix. Both gel-phase rows are therefore ACCEPT, rather than restricting applicability to the vascular pool. The proposed cartilage-matrix term is deferred to a question until a current ontology-wide synonym search establishes whether a gap actually exists.
- **Synapse and PAINT:** refine the broad synapse term to the characterized perineuronal-net compartment without asserting that secreted proteins cannot occur at synapses. Lack of a synapse ancestor does not prove disjoint localization. Cached `interpro/panther/PTHR22804/PTHR22804-paint.tsv` places the CNS-development and skeletal-development IBDs at PTN000515588, and the synapse and perineuronal-net IBDs at PTN008374273. Propagation reviews now identify these actual ancestral nodes. A mix of paralog and ortholog descendant evidence is not itself evidence of bad propagation. No node-placement error or target-specific functional loss was established.

### Assembly proposal and comparator check

Full cached PMID:40273987 supports the human G1-hyaluronan structure and binding affinity. Its cell experiment adds human fragments to **already formed mouse cortical perineuronal nets**; residual binding by HA-binding-null fragments supports another retention mechanism. It is not a direct assay of de novo assembly by full-length aggrecan. The previous NEW rationale also claimed the source record had no valid biological process despite retained developmental annotations.

The [MGI GO:0085029 definition](https://www.informatics.jax.org/vocab/gene_ontology/GO%3A0085029) has cellular-component assembly and extracellular-matrix organization as parents. Aggrecan could in principle contribute structure during assembly; the term is not restricted to enzymes. The unresolved issue is the evidentiary and annotation convention, not a universal rule against structural constituents.

Same-role comparators were VCAN, BCAN and NCAN, all HA-binding lecticans. Direct QuickGO queries were unavailable. MGI's accessible [BCAN comparison](https://www.informatics.jax.org/homology/GOGraph/Bcan) and [NCAN comparison](https://www.informatics.jax.org/homology/GOGraph/Ncan) tables did not show GO:0085029 among their experimental annotations. These are explicitly dated 2023 graph snapshots, not a current all-evidence absence test. The VCAN endpoint failed. No matching ACAN activity was recovered from the local GO-CAM index. None of these limitations establishes a systematic cross-species absence or proves that curators prohibit the term.

[Reactome R-HSA-2318623](https://reactome.org/content/detail/R-HSA-2318623) already models human ACAN binding hyaluronan and HAPLN1 to form a ternary complex. This curated role and the core hyaluronan-binding activity are retained. The unsupported extra process assertion and its core-function BP entry are withdrawn pending a resolved comparator check and direct assembly evidence; the question remains explicit.

### Remaining source audit

The 14 Golgi-location rows describe proteoglycan biosynthesis or transit. Five arise from disease reactions involving a defective modifying enzyme; that does not invalidate the acceptor's location. The old “export artifact” accusation is removed. The three lysosomal rows describe a catabolic substrate location, not an aggrecan enzyme function. Reactome R-HSA-2046239 explicitly leaves the uptake mechanism uncertain. The three extracellular-region rows from the aggrecan-HA-HAPLN1, tenascin and COMP binding events are refined to extracellular matrix. Three secretion, uptake and HTRA1-cleavage rows remain non-core because they describe biosynthetic transit or catabolic substrate context.

Full cached PMID:27068509 identifies aggrecan in the human saphenous-vein guanidine fraction (Table 1), confirms it by targeted MRM (section 3.5), and reports transcript changes (section 3.6). The aortic PMID:20551380 extraction-method passage names aggrecan as an example of an expected proteoglycan substrate; that sentence alone is not a results-table identification. Its curated HDA is retained with the independent vascular evidence. Both compression-resistance RCA rows remain supported, distinguishing their descriptive mechanism from a direct mechanical assay.

PMID:1569188 remains abstract-only despite JCI/PubMed access attempts. Its explicit cleavage result supports the aggrecan-as-substrate interpretation, so the NAS proteolysis row remains REMOVE. No claim is made that the unread full paper lacks a developmental discussion. The cartilage-development refinement is independently supported by PMID:25701227 and PMID:35338222. The record now truthfully marks its full-text access limit. PMID:20137779 is also abstract-only; the stated G3 ligand-binding loss is explicitly in that abstract and is corroborated by the later full study.

All 19 Reactome source references were assessed from the eight existing caches and official web records for missing caches. Particularly informative records were [aggregate formation](https://reactome.org/content/detail/R-HSA-2318623), [COMP partners](https://reactome.org/content/detail/R-HSA-2424252), [lysosomal delivery](https://reactome.org/content/detail/R-HSA-2046239), and [HTRA1 cleavage](https://reactome.org/content/detail/R-HSA-8855825). No generated source, cached publication, provider report or GOA field was manually changed.

Final validation: `just validate human ACAN` passes with three warnings: uncached PMID:11222505, the intentionally different extracellular-region actions for matrix-binding versus transit/catabolic contexts, and the unused-provider advisory. The generic-protein-binding policy warning is resolved. All 40 seeded rows were compared field-for-field against the original review and preserved; immutable UniProt, GOA and affinage source blobs still match main. Publication is pending normal recovery of the missing reference cache.

Independent review identified the broad-location consistency issue: core matrix-binding reaction rows now use MODIFY to extracellular matrix, while secretion and catabolic-context rows remain non-core. This follows the same specificity policy as the existing broad structural-constituent refinement.

Final history validation and rendering pass. The final gene validation reports no supporting-quote mismatch or blocking error. The exact four-file publication manifest, including base and new blob hashes, is `/tmp/ACAN-audit-manifest.json`; no Git or remote changes were made by this audit.

Publication preflight: the top-level reference summaries for InterPro, PAINT, ARBA, defective B4GALT1 and the aggrecan aggregate reaction were brought into agreement with the final annotation judgments. Trailing whitespace was removed with parsed-YAML equality checked.
