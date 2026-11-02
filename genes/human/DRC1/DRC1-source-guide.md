---
title: DRC1 source and assay guide
gene: DRC1
annotation_scope:
  imported_annotations: 23
  new_annotations: 0
---

# DRC1 source and assay guide

The review separates the N-DRC structural scaffold from the dynein motor complex. All 23 imported source assertions remain identifiable, including four distinct partner contexts. The one core integrates scaffold activity, axoneme assembly and ciliary-movement regulation without asserting autonomous motor catalysis.

## Primary originals and constructs

| Source | Evidence and exact scope |
|---|---|
| [PMID:23354437, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3818796/) | Original Methods, Results, Discussion and relevant captions were independently read. Human respiratory cilia lack N-DRC links and lose GAS8/LRRC48 localization while retaining DNALI1/CCDC39 and gross arm structure; bending and beat frequency change. The selective inner-arm and associated-complex assembly defects are algal pf3/DRC1 findings. This supports conserved structural participation without claiming wholesale human dynein-arm loss. |
| [PMID:34169321, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC8522639/) | Original Results, Methods, Figure 4 and its caption, plus the linked genuine supplementary document were independently read. Human infertility/MMAF and mouse axoneme phenotypes are distinguished. Mouse spermatid axonemes form before later disorganization; respiratory cilia retain gross 9+2/radial-spoke/dynein arrangements. Figure 4 shows controlled HA-DRC1/Flag-DRC2/3/4/5 co-IP in HEK293T. Main and supplementary Methods do not authenticate transfected ORF species or sequence; human host cells do not establish human constructs. |
| [PMID:37258679, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC10266980/) — [publisher supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-023-06140-2/MediaObjects/41586_2023_6140_MOESM1_ESM.pdf) | Operative structural Results, human ALI culture/deciliation and modeling Methods were read. Supplementary Table 3 begins on physical PDF page 10, printed page 9; physical page 11, printed page 10, lists the DRC1 and four partner rows under the human external-protein inventory. The selected target-page pixels were inspected. Detailed scaffold contacts are algal; human homologous subcomplex predictions are placed in cryo-EM density. The paper explicitly leaves human IDAe docking dependence unresolved. |

The human Table 3 records are DRC1 Q96MC2 (740 residues), DRC2 Q8IXS2 (484), DRC3 Q9H069 (523), DRC4 O95995 (478) and DRC5 Q5JU00 (501). These are the structural model inventory, not independently measured pairwise affinities or evidence that the 2021 transfected ORFs have those exact sequences. The human respiratory specimens in PMID:37258679 are not human sperm.

The [official Q96MC2 record](https://www.uniprot.org/uniprotkb/Q96MC2/entry) and FASTA establish one displayed 740-residue human product. No alternative-products block was present. Patient truncations and engineered mouse alleles remain experimental or clinical contexts, not extra natural products.

## Binding-class and complex definitions

[GO:0008092 cytoskeletal protein binding](https://www.ebi.ac.uk/QuickGO/term/GO:0008092) is a child of protein binding and covers protein components of actin, microtubule or intermediate-filament cytoskeletons. [GO:0005931 axonemal nexin link](https://www.ebi.ac.uk/QuickGO/term/GO:0005931) is part of the [axoneme](https://www.ebi.ac.uk/QuickGO/term/GO:0005930), itself part of the [cytoskeleton](https://www.ebi.ac.uk/QuickGO/term/GO:0005856). The positive co-IP assertions plus independently established structural identities support the four binding-class refinements. Purified direct contact and native downstream function are distinct unresolved questions, not additional prerequisites for naming the partner class.

The source pairs remain Q96MC2 with [DRC4 O95995](https://www.uniprot.org/uniprotkb/O95995/entry), [DRC5 Q5JU00](https://www.uniprot.org/uniprotkb/Q5JU00/entry), [DRC2 Q8IXS2](https://www.uniprot.org/uniprotkb/Q8IXS2/entry) and [DRC3 Q9H069](https://www.uniprot.org/uniprotkb/Q9H069/entry). They are literal UniProt-assigned human source contexts dated 2023-02-14. The [IntAct publication query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/pubid:34169321?format=tab27) returned an empty successful response in the inspected snapshot. It is not used to invent clone sequences or negate the original controlled co-IP. Unrelated records from the broader target query are not substituted for these pairs.

[GO:0005858 axonemal dynein complex](https://www.ebi.ac.uk/QuickGO/term/GO:0005858) identifies the motor complex. Refining that membership to the nexin link corrects complex identity. It does not reject the separate [GO:0070286 assembly](https://www.ebi.ac.uk/QuickGO/term/GO:0070286) assertions, supported by the original selective algal assembly phenotype, conserved structure and phylogenetic inference. The compact core uses [GO:0140378 scaffold activity](https://www.ebi.ac.uk/QuickGO/term/GO:0140378); the binding refinements do not claim that every individual association is an independent scaffold function.

## Location and donor resolution

The [HPA target XML](https://www.proteinatlas.org/ENSG00000157856.xml) reports approved ICC/IF nucleoplasm and primary-cilium transition-zone staining with HPA051247, including cultured ciliated human cells. Metadata and target assay records were inspected; images were not independently scored. These results preserve a broader cilium context without establishing diffuse cytosol or replacing the primary native-axoneme evidence.

[PMID:27914912](https://pubmed.ncbi.nlm.nih.gov/27914912/) remains abstract-only after bounded original-access attempts. Current mouse [Q3USS3 annotations](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AQ3USS3) include cytosol IDA from that paper, but the Drc1-specific experiment was not inspected. The transfer remains undecided, with no claim of source error or target exclusion.

[PMID:20876659, original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2951471/) was recovered separately from the abstract-only normal cache. Inspected Methods and Results use procyclic Trypanosoma brucei CMF70/Q384U1: endogenous-locus HA tagging, detergent/salt fractionation, flagellar immunofluorescence, RNAi motility tracks and genetic suppression. Those findings ground the DRC2-branch donor context; they are not human DRC1 assays.

## Phylogeny and electronic mappings

The [PANTHER PTHR21625 family](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR21625) tree contains 182 nodes. The human DRC1 leaf PTN002502523 has a 19-node path and an ungapped alignment exactly matching the 740-residue official sequence. The common root PTN000492844 carries four literal PAINT IBDs covering movement regulation, axoneme localization, cilium-dependent cell motility and dynein-complex assembly. DRC1 and DRC2 descendants belong to the shared ancestral judgment; the target's experimental evidence among descendants is legitimate, not circular.

The donor identities are preserved: Q32KY1 is bovine DRC1, Q384U1 is trypanosome CMF70/DRC2, and Q3USS3 is mouse Drc1. The exact bovine experimental assay is not reconstructed, and no algal identity is substituted. Independent human structure and primary target phenotypes corroborate the conserved claims. The [PAINT evidence release](https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf) supplies the literal IBD provenance.

[ARBA00045042](https://www.uniprot.org/arba/ARBA00045042) and [ARBA00029057](https://www.uniprot.org/arba/ARBA00029057) contain matching target conditions involving IPR029440, IPR039505 and IPR039750. The inspected [InterPro IPR039750](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR039750/) mapping emits both motor-complex membership and assembly. Each is assessed on its biological meaning: membership is refined, while assembly is retained with organism-specific limits. The inspected GO-CAM target index contains no Q96MC2 activity; absence is not evidence for an annotation gap.

## Access and preservation

| PMID | Effective normal cache | Actual read scope |
|---|---|---|
| 23354437 | Full XML | Independent original Methods, Results, Discussion and relevant captions; human and algal scope distinguished. |
| 34169321 | Full XML | Independent original Methods/Results, Figure 4 blot/caption and genuine supplementary document; ORF identity unresolved. |
| 37258679 | Existing full XML | Operative structural/culture/modeling Methods and Results plus human supplemental inventory and selected table-page pixels. |
| 20876659 | Abstract only | Separately recovered genuine PMC original target Methods and Results. |
| 27914912 | Abstract only | Complete abstract and donor annotation record; target localization experiment unavailable. |

The three pre-existing sequence-resource caches PMID:14702039, PMID:15815621 and PMID:17974005 are preserved without additional functional claims or an original-body read claim. All protected source bytes and access flags remain unchanged. Failed routes and challenge responses are retained as access provenance, not biological evidence. Genuine configured research-provider failures yielded no report. The one short publication excerpt appears only once in the core; this guide adds no quotations.
