---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AIG1
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9NVV5
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AIG1 (human)

## Current model (mechanistic narrative)

AIG1 is the founding member of an evolutionarily conserved class of atypical integral-membrane threonine hydrolases that catabolize bioactive lipids, specifically hydrolyzing fatty acid esters of hydroxy fatty acids (FAHFAs) via a catalytic dyad of conserved threonine and histidine residues [PMID:27018888]. Acting together with the related hydrolase ADTRP, AIG1 sets endogenous FAHFA tone in vivo, as combined loss elevates tissue FAHFA levels (notably 9-position isomers) without altering other lipid classes, an effect phenocopied by acute dual pharmacological inhibition [PMID:32152231]. This FAHFA-hydrolyzing activity is physiologically deployed in adipocytes, where AIG1 is induced downstream of IRF3 and drives obesity-associated insulin resistance that is reversed by AIG1 inhibition [PMID:38816388]. Independently of its lipase function, AIG1 binds the Pirh2 E3 ubiquitin ligase to promote ubiquitination and degradation of p53; in cardiomyocytes this AIG1–Pirh2–p53 axis restrains doxorubicin-induced ferroptosis and oxidative stress, with p53 inhibition rescuing the AIG1-deficient phenotype [PMID:40303337, PMID:21622095]. AIG1 was originally identified as an androgen-inducible gene in dermal papilla cells [PMID:11266118].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0140098 catalytic activity, acting on RNA
- **localization:** GO:0005783 endoplasmic reticulum
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-5357801 Programmed Cell Death
- **partners:** PIRH2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | AIG1 is an atypical integral membrane hydrolase that depends on conserved threonine and histidine residues for catalysis. AIG1 specifically hydrolyzes bioactive fatty acid esters of hydroxy fatty acids (FAHFAs) but not other major classes of lipids, establishing it as a founding member of an evolutionarily conserved class of transmembrane threonine hydrolases involved in bioactive lipid metabolism. | PMID:27018888 | Nature chemical biology |
| 2020 | High | AIG1 and ADTRP are endogenous FAHFA hydrolases that control FAHFA levels in vivo. Tissues from mice lacking both AIG1 and ADTRP (DKO) showed elevated FAHFA concentrations (particularly 9-position isomers) due to decreased FAHFA hydrolysis activity, while other lipid classes were unaltered. A dual AIG1/ADTRP inhibitor (ABD-110207) administered acutely to wild-type mice elevated FAHFA levels, confirming the enzymatic function in vivo. | PMID:32152231 | The Journal of biological chemistry |
| 2024 | High | IRF3 induces AIG1 expression in adipocytes, and AIG1 promotes insulin resistance by hydrolyzing FAHFAs. Adipocyte-specific overexpression of AIG1 on a high-fat diet promoted insulin resistance, while pharmacological inhibition of AIG1 reversed obesity-induced insulin resistance in mice with adipocyte IRF3 overexpression, identifying the adipocyte IRF3/AIG1 axis as a link between obesity-induced inflammation and metabolic dysfunction. | PMID:38816388 | Nature communications |
| 2025 | High | AIG1 directly interacts with the Pirh2 E3 ubiquitin ligase to promote ubiquitination and degradation of p53 in cardiomyocytes. AIG1 deficiency (global KO or cardiac-specific knockdown) aggravated doxorubicin-induced ferroptosis and oxidative stress, whereas cardiac-specific AIG1 overexpression inhibited ferroptosis and improved cardiac function. Cardiac-specific Pirh2 knockdown exacerbated ferroptosis by enhancing p53 activity, and pharmacological p53 inhibition (PFT-α) rescued the AIG1-KO phenotype, establishing an AIG1–Pirh2–p53 signaling axis. | PMID:40303337 | Theranostics |
| 2011 | Medium | AIG1 interacts with the Pirh2 E3 ubiquitin ligase (identified by yeast two-hybrid and confirmed in vitro and in vivo) and activates the NFAT signaling pathway in a dose-dependent manner when overexpressed in HEK293T cells. | PMID:21622095 | Frontiers in bioscience (Elite edition) |
| 2016 | Medium | AIG1 is a multipass transmembrane protein localized to the ER membrane with five transmembrane domains, a luminal N-terminus, a cytosolic C-terminus, and a hydrophobic stretch between TM3 and TM4 that does not cross the membrane. AIG1 overexpression increases ER Ca²⁺ content and susceptibility to oxidative stress-induced cell death. | PMID:27040980 | Gene |
| 2001 | Low | AIG1 was cloned from human dermal papilla cells as an androgen-inducible gene. Northern blot and RT-PCR showed that AIG1 mRNA is induced by dihydrotestosterone (DHT) in dermal sheath cells, with higher expression in males than females. Bioinformatic analysis predicted five hydrophobic (transmembrane) domains in the protein. | PMID:11266118 | Molecules and cells |

## Citations

- PMID:11266118
- PMID:21622095
- PMID:27018888
- PMID:27040980
- PMID:32152231
- PMID:38816388
- PMID:40303337
