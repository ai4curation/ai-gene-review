---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASZ1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WWH4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASZ1 (human)

## Current model (mechanistic narrative)

ASZ1 (GASZ) is a germ cell-specific protein essential for piRNA biogenesis, transposon silencing, and fertility [PMID:19730684]. It localizes to the outer mitochondrial membrane through a functional mitochondrial targeting signal and self-associates there, promoting mitofusin-dependent mitochondrial fusion and clustering; this mitochondrial localization is required for nuage (intermitochondrial cement) formation, transposon repression, and spermatogenesis [PMID:26711429]. Within nuage, ASZ1 co-localizes with and stabilizes the piRNA pathway protein MILI, and its loss causes MILI downregulation, global piRNA depletion, retrotransposon derepression and hypomethylation, and a zygotene-pachytene spermatocyte arrest [PMID:19730684]. Mechanistically, ASZ1 acts as a mitochondrial anchoring platform: together with its binding partner Daedalus it recruits and retains the piRNA biogenesis factor Armitage near the Zucchini processing machinery, making it essential for Zucchini-mediated piRNA production [PMID:31123065]. The protein architecture comprises ankyrin repeats, a SAM domain, and a bZIP domain, consistent with a scaffolding role in protein-protein interactions [PMID:12040005].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005739 mitochondrion, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-1474165 Reproduction
- **partners:** MILI, DAEDALUS, ARMITAGE, MFN
- **complexes:** intermitochondrial cement (nuage)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | Medium | GASZ (ASZ1) was identified as a novel germ cell-specific protein containing four ankyrin repeats, a sterile-alpha motif (SAM), and a basic leucine zipper (bZIP) domain, localizing to the cytoplasm of pachytene spermatocytes, early spermatids, oocytes, and early preimplantation embryos, consistent with a role as a cytoplasmic signal transducer mediating protein-protein interactions during germ cell maturation. | PMID:12040005 | Molecular endocrinology (Baltimore, Md.) |
| 2004 | Low | GASZ (ASZ1) orthologs are evolutionarily conserved across vertebrates (pufferfish, zebrafish, frog), retaining germ cell-specific expression and cytoplasmic localization in pachytene spermatocytes and oocytes; in frog oocytes, GASZ protein localizes to a cytoplasmic structure resembling the Balbiani body. | PMID:14766731 | Biology of reproduction |
| 2009 | High | GASZ (ASZ1) co-localizes with MILI in intermitochondrial cement (nuage) in male germ cells; knockout of Gasz in mice causes dramatic downregulation of MILI protein levels, phenocopies the zygotene-pachytene spermatocyte block and male sterility of MILI-null mice, and results in increased retrotransposon expression, hypomethylation of retrotransposons, and global downregulation of piRNAs (repeat-associated, known, and novel), establishing an essential structural role for GASZ in stabilizing MILI in nuage. | PMID:19730684 | PLoS genetics |
| 2015 | High | GASZ (ASZ1) contains a functional mitochondrial targeting signal and localizes predominantly to mitochondria in germ cells endogenously and in somatic cells when ectopically expressed; GASZ interacts with itself at the outer mitochondrial membrane and promotes mitofusion in a mitofusin/MFN-dependent manner; deletion of the mitochondrial targeting signal in mice reveals that mitochondrial localization of GASZ is essential for nuage formation, mitochondrial clustering, transposon repression, and spermatogenesis. | PMID:26711429 | EMBO reports |
| 2019 | High | Drosophila Gasz (ortholog of ASZ1) interacts with Daedalus (Daed) on the outer mitochondrial membrane and together they form a mitochondrial anchoring platform that recruits and retains the piRNA biogenesis factor Armitage (Armi) proximal to Zucchini for piRNA processing; Gasz is essential for Zucchini-mediated piRNA production and correct localization of Armi. | PMID:31123065 | Genes & development |

## Citations

- PMID:12040005
- PMID:14766731
- PMID:19730684
- PMID:26711429
- PMID:31123065
