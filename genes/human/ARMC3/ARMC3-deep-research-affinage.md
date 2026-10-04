---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5W041
self_evaluation_pairwise: tie
faith_pct: 83.33333333333333
n_discoveries: 16
citation_count: 16
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMC3 (human)

## Current model (mechanistic narrative)

ARMC3 (mammalian) and its yeast ortholog Vac8 are armadillo-repeat proteins that act as membrane-anchored scaffolds coupling the vacuolar/lysosomal membrane to autophagic and membrane-inheritance machinery [PMID:31512555, PMID:34705610]. Vac8 is targeted to the vacuolar membrane by N-terminal myristoylation, with deletion of the myristoylation site abolishing localization and producing fragmented vacuoles and inheritance defects [PMID:9664035]; stable membrane attachment further requires palmitoylation of N-terminal cysteines, a modification installed by the DHHC acyltransferase Pfa3 — whose recognition of Vac8 is conferred specifically by the 11th armadillo repeat — and which adds functional roles beyond mere anchoring [PMID:16301533, PMID:16720644, PMID:19416974]. Through its ARM domain, Vac8 anchors the phagophore assembly site to the vacuole by binding Atg13, thereby recruiting the Atg1 initiation complex, and additionally recruits class III PI3K complex I via the Atg14 C-terminus to drive autophagosome biogenesis [PMID:31512555, PMID:32508216, PMID:37436710]. The same scaffold supports vacuole inheritance through a tripartite Myo2–Vac17–Vac8 complex [PMID:bio_10.1101_2025.03.24.645041]. These activities are made mutually exclusive by the protein's quaternary state: an intramolecular H1-helix/ARM1 contact governs Vac8 self-association, and Vac17 binding clamps H1 to ARM1 to block dimerization and thereby competitively exclude the Nvj1 and Atg13 interactions [PMID:31512555, PMID:37094131]. In mammals, ARMC3 is the functional homolog of Vac8, with its ARM domains recruiting PtdIns3K-CI to initiate autophagosome formation; loss of ARMC3 blocks ribophagy in spermatids, lowers mitochondrial energy, and produces immotile flagella [PMID:34705610]. Truncating ARMC3 mutations cause sterilizing sperm tail defects in cattle and asthenozoospermia with disrupted flagellar ultrastructure in humans, establishing ARMC3 as required for normal spermatogenesis [PMID:26923438, PMID:39221575].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005773 vacuole
- **pathway (Reactome):** R-HSA-9612973 Autophagy, R-HSA-9609507 Protein localization
- **partners:** ATG13, ATG14, VAC17, MYO2, NVJ1, PFA3, YKT6, ATG11
- **complexes:** Myo2-Vac17-Vac8 vacuole inheritance complex, Vac8-Atg13-Atg1 initiation complex, Vac8-PI3K complex I (via Atg14)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | Medium | Yeast Vac8 (ARMC3 ortholog) localizes to the vacuolar membrane via N-terminal myristylation; deletion of the myristylation site abolishes vacuolar localization. Loss of Vac8 causes accumulation of small fragmented vacuoles and defective vacuolar inheritance. | PMID:9664035 | Journal of cell science |
| 2005 | Medium | Vac8 palmitoylation on isolated yeast vacuoles is mediated by the R-SNARE Ykt6 and is part of a SNARE subcomplex distinct from the Nyv1-containing complex; this reaction is ATP-independent, restricted to a narrow time window, and stimulated by EDTA (ion chelation). Palmitoylation is required for vacuole fusion. | PMID:15701652 | The Journal of biological chemistry |
| 2005 | Medium | The DHHC palmitoyl acyltransferase Pfa3 is specifically required for efficient vacuolar localization of Vac8 in vivo; Pfa3 deletion impairs Vac8 palmitoylation and reduces vacuole fusion, while vacuole morphology and inheritance appear normal. | PMID:16301533 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | Medium | Stable vacuolar membrane binding of Vac8 requires two N-terminal cysteines for palmitoylation regardless of their combination; palmitoylation adds functional roles beyond membrane anchoring — a basic-residue replacement mutant that still localizes to vacuoles can support cytoplasm-to-vacuole transport but requires at least one palmitoylation cysteine for vacuolar morphology and inheritance functions. | PMID:16720644 | Journal of cell science |
| 2006 | Medium | In Pichia pastoris, Vac8 ARM repeat domains (central region) are required for formation of vacuolar arm-like extensions that engulf peroxisomes during micropexophagy, and Vac8 is essential for recruitment of Atg11 to the vacuolar membrane during glucose-induced pexophagy; palmitoylation/myristoylation sites are required for protein stability and vacuolar association. | PMID:16921262 | Autophagy |
| 2006 | Medium | In Pichia pastoris, the ARM repeat domain of Vac8 is required for vacuolar inheritance but not for micropexophagy; deletion of both ARM and C-terminal domains abolishes vacuolar sequestering membrane formation and abolishes recruitment of Atg11 to the vacuolar membrane during micropexophagy. | PMID:16874085 | Autophagy |
| 2009 | High | Pfa3 palmitoylates each of the three N-terminal cysteines of Vac8 in vitro, with efficiency enhanced by prior N-myristoylation; the 11th armadillo repeat of Vac8 is a key determinant for specific recognition by Pfa3, as shown by chimeric protein and competition experiments. | PMID:19416974 | The Journal of biological chemistry |
| 2019 | High | Crystal structure of Vac8 bound to Atg13 reveals that the Atg13 extended loop (70 Å) binds the ARM domain of Vac8 in an antiparallel manner; the N-terminal H1 helix of Vac8 intramolecularly associates with ARM1 and regulates Vac8 self-association (dimerization), which is required differentially for Cvt and PMN autophagy pathways. Different quaternary structures of Vac8 (Atg13-bound heterotetramer vs. Nvj1-bound complex) mediate distinct autophagic functions. | PMID:31512555 | Autophagy |
| 2019 | Medium | The Atg13 C-terminus binds lipid membranes via electrostatic interactions and hydrophobic insertion of a Phe residue; this phospholipid binding and Vac8 binding are mutually exclusive because they involve overlapping residues in the Atg13 IDR, and both interactions are required for efficient autophagy. | PMID:31352862 | Autophagy |
| 2020 | Medium | Vac8 anchors the phagophore assembly site (PAS) to the vacuolar membrane by binding Atg13 and thereby recruiting the Atg1 initiation complex; VAC8 deletion or Vac8 mislocalization reduce autophagy activity, establishing Vac8 as required for correct vacuolar localization of the PAS. | PMID:32508216 | Autophagy |
| 2016 | Medium | A 1 bp frameshift deletion (p.A451fs26) in bovine ARMC3 that truncates the protein by 401 amino acids (46%) is causally associated with a sterilizing tail stump sperm defect characterized by severely disorganized, immotile spermatozoa tails, establishing ARMC3 as required for normal spermatogenesis. | PMID:26923438 | BMC genetics |
| 2021 | Medium | Mouse ARMC3 is the functional homolog of yeast Vac8; its ARM domains recruit PtdIns3K-CI (class III PI3K complex I) to the phagophore assembly site to initiate autophagosome formation via PtdIns3P generation. Armc3 knockout mice show blocked ribophagy in spermatids, low mitochondrial energy levels, immotile flagella, and male infertility. | PMID:34705610 | Autophagy |
| 2023 | High | X-ray crystal structure of the Vac8-Vac17 complex reveals a bipartite interaction interface; binding of Vac17 to Vac8 clamps the H1 helix to ARM1, preventing Vac8 dimerization and thereby competitively inhibiting Vac8 interactions with Nvj1 and Atg13. Mutation of key interface residues severely impairs vacuole inheritance in vivo. | PMID:37094131 | Proceedings of the National Academy of Sciences of the United States of America |
| 2023 | Medium | PI3KCI interacts with the vacuolar membrane anchor Vac8 via the Atg14 C-terminal region in a constitutive manner; this interaction cooperates with Atg38-Atg1 complex and Vps30-Atg9 interactions to target PI3KCI to the PAS for autophagosome biogenesis. | PMID:37436710 | The Journal of cell biology |
| 2024 | Medium | A homozygous splicing variant (c.916+1G>A) in human ARMC3 causes exon 8 skipping, producing a truncated protein undetectable by Western blot in patient sperm, and results in asthenozoospermia with disrupted flagellar ultrastructure including vacuolated sperm mitochondria at the midpiece. | PMID:39221575 | Clinical genetics |
| 2025 | Low | The vacuole-specific adaptor Vac17 interacts with Myo2 (yeast myosin V) through two distinct binding sites (handhold mechanism); cryo-EM and structure prediction show one of these sites links to Vac8 on the vacuole membrane, forming the Myo2-Vac17-Vac8 complex for vacuole transport to daughter cells. | PMID:bio_10.1101_2025.03.24.645041 | bioRxiv |

## Citations

- PMID:15701652
- PMID:16301533
- PMID:16720644
- PMID:16874085
- PMID:16921262
- PMID:19416974
- PMID:26923438
- PMID:31352862
- PMID:31512555
- PMID:32508216
- PMID:34705610
- PMID:37094131
- PMID:37436710
- PMID:39221575
- PMID:9664035
- PMID:bio_10.1101_2025.03.24.645041
