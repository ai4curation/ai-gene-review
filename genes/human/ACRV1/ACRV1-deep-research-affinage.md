---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACRV1
affinage_run_date: 2026-06-09T22:02:39
uniprot_accession: P26436
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 13
citation_count: 13
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACRV1 (human)

## Current model (mechanistic narrative)

ACRV1 (SP-10) is a testis-specific intra-acrosomal protein expressed in round spermatids that functions in the terminal steps of sperm–egg interaction [PMID:2310816, PMID:10529272]. It encodes a hydrophilic protein with an N-terminal signal peptide and an internal block of three amino-acid repeat types, with no homology to other characterized sequences, and is expressed as alternatively spliced mRNAs [PMID:1693291]. SP-10 is synthesized as a ~45 kDa precursor that is proteolytically processed by trypsin-like (acrosin-type) and other intra-acrosomal endoproteases into a heterogeneous family of 18–32 kDa peptides, with maturation beginning in the testis and continuing in the proximal epididymis [PMID:1637938, PMID:7888499]. Rather than being an integral membrane protein, it is a peripheral acrosomal protein tethered to the acrosomal membranes through a chaotrope-sensitive, detergent-resistant anchor [PMID:1591355]. During the acrosome reaction it redistributes to the inner acrosomal membrane of the equatorial segment, where it mediates sperm–oolemma binding in a beta-1 integrin-independent manner without participating in sperm–zona binding [PMID:2310816, PMID:10775167]. Transcription is controlled by a TATA-less 294-bp proximal promoter sufficient for round spermatid-specific expression [PMID:10529272]; TDP-43 binds GTGTGT motifs within this promoter to repress transcription and pause RNA polymerase II in spermatocytes through its RNA-binding RRM1 domain, while NF45/NF90 act through a Pu-box (AGAAAA) element to upregulate promoter activity [PMID:21252238, PMID:17942973]. The same promoter region functions as a CpG-free vertebrate insulator in somatic cells, where TDP-43-dependent tethering to the nuclear matrix blocks enhancer–promoter communication [PMID:14512027, PMID:17932037]. In ovarian cancer cells, ectopic ACRV1 acts together with ZNF280A and CUX2 to activate PI3K/AKT signaling and glycolysis [PMID:41338461].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity
- **localization:** GO:0031410 cytoplasmic vesicle, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-74160 Gene expression (Transcription)
- **partners:** TARDBP, NF45, NF90, ZNF280A, CUX2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1990 | High | SP-10 (ACRV1) is an intra-acrosomal protein localized throughout the acrosome, specifically in a bilaminar array associated with the inner aspect of the outer acrosomal membrane and the outer aspect of the inner acrosomal membrane; after the acrosome reaction it remains displayed on the sperm head associated with the inner acrosomal membrane and equatorial segment. | PMID:2310816 | Biology of reproduction |
| 1990 | High | SP-10 (ACRV1) encodes a 265-amino acid protein with a hydrophobic signal peptide at the N-terminus and a central region containing three types of amino acid repeats occurring 16 times; alternative splicing generates at least two SP-10 mRNAs (including one with a 57-bp in-frame deletion); the protein is unique with no homology to other known sequences. | PMID:1693291 | Biology of reproduction |
| 1992 | High | SP-10 heterogeneity (17.5–34 kDa peptides) results from endoproteolytic cleavage at five different peptide bonds (following arginine, serine, proline, glycine, and glutamic acid), consistent with action of a trypsin-like protease (possibly acrosin) and previously undescribed intra-acrosomal protease specificities. | PMID:1637938 | Biology of reproduction |
| 1992 | High | SP-10 is a hydrophilic peripheral acrosomal membrane protein (not an integral membrane protein), associated with the acrosomal membranes via a TX-114-resistant anchor; a chaotropic salt (sodium thiocyanate) and pH extremes fully release this TX-114-resistant pool, whereas repeated TX-114 or 1.5 M NaCl washes do not. | PMID:1591355 | Biology of reproduction |
| 1994 | High | A full-length ~45 kDa SP-10 precursor is present in testis and is proteolytically processed to 32–26 kDa peptides in testis and/or via alternative splicing; further processing to 25–18 kDa peptides occurs in the initial segment or caput epididymidis; no additional processing occurs during epididymal transit, ejaculation, or capacitation. After the acrosome reaction, SP-10 is concentrated on the inner acrosomal membrane of the equatorial segment and associated with hybrid vesicles. | PMID:7888499 | Biology of reproduction |
| 1996 | Medium | Anti-SP-10 antibodies inhibit bovine in vitro fertilization by reducing sperm-zona secondary binding and reducing the ability of capacitated spermatozoa to complete the acrosome reaction; they also reduce motility of capacitated (but not noncapacitated) spermatozoa. | PMID:8882296 | Journal of reproduction and fertility |
| 1999 | High | A 294-bp proximal promoter region (-266 to +28 bp) of the mouse SP-10 (Acrv1) gene is sufficient to direct round spermatid-specific transcription in vivo; the core promoter lacks a TATA box but contains a canonical initiator (Inr) element at the transcription start site; the -91/+28 fragment lacks promoter activity. | PMID:10529272 | Biology of reproduction |
| 2000 | Medium | SP-10 expressed on the equatorial region of acrosome-reacted sperm mediates sperm-oolemma binding in a beta-1 integrin-independent manner, but does not mediate sperm-zona binding. | PMID:10775167 | Biology of reproduction |
| 2003 | High | The SP-10 proximal promoter (-408/-92 region) functions as an insulator in somatic cells by blocking enhancer-promoter interactions in a position- and orientation-dependent manner; insulator activity maps to the -186/-135 region, and mutation of two ACACAC motifs abolishes insulator function. | PMID:14512027 | Developmental biology |
| 2007 | High | TDP-43 binds to the SP-10 insulator via GTGTGT motifs, tethers the SP-10 gene to the nuclear matrix in somatic cells (sequestering the core promoter and preventing transcription), and is required for enhancer-blocking; TDP-43 knockdown by siRNA releases the enhancer-blocking effect, and mutation of TDP-43 binding sites abolishes this effect. A 50-bp subfragment containing TDP-43 binding sites is a minimal insulator sufficient to silence ectopic transgene expression in somatic tissues of transgenic mice. | PMID:17932037 | The Journal of biological chemistry |
| 2007 | Medium | NF45 binds to the mouse SP-10 promoter via an AGAAAA (Pu-box) element at -154 in a site-specific manner in gel shift assays; co-transfection of NF45 and NF90 upregulates SP-10 promoter-driven luciferase expression in spermatogenic GC2 cells, requiring the AGAAAA site; however, NF45-NF90 stimulation alone was not sufficient to activate an SP-10 promoter-driven GFP transgene in chromatin context. | PMID:17942973 | Journal of andrology |
| 2011 | High | TDP-43 is a transcriptional repressor of the acrv1 gene: it binds to the acrv1 promoter in vivo through GTGTGT motifs (confirmed by plasmid ChIP and ChIP on isolated germ cells), represses transcription via its N-terminal RRM1 domain in a histone deacetylase-independent manner, and is associated with RNA polymerase II pausing at the acrv1 promoter in spermatocytes. RNA-binding-defective TDP-43 (but not splice variant isoforms) relieves repressor function. | PMID:21252238 | The Journal of biological chemistry |
| 2025 | Medium | ZNF280A enhances ACRV1 transcription by interacting with transcription factor CUX2, which facilitates CUX2 recruitment to the ACRV1 promoter; elevated ACRV1 (together with ZNF280A) activates PI3K/AKT signaling and increases glycolytic enzyme expression (PKM2 and LDHA), glucose uptake, lactate production, and ATP generation in ovarian cancer cells; pharmacological inhibition of AKT or glycolysis abrogates these effects. | PMID:41338461 | The Journal of biological chemistry |

## Citations

- PMID:10529272
- PMID:10775167
- PMID:14512027
- PMID:1591355
- PMID:1637938
- PMID:1693291
- PMID:17932037
- PMID:17942973
- PMID:21252238
- PMID:2310816
- PMID:41338461
- PMID:7888499
- PMID:8882296
