# VC_0658 (Q9KU65, CdgI) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_JABEED010000006.1_102` (*V. cholerae*, 681 aa). Strata: Human Pathogen, Core, Annotation-Promoted; homologs in 24 organisms across 4 genera. DeepTMHMM puts it in the inner membrane with 2 TM helices.
- Mapping: N16961 reference entry Q9KU65 (VC_0658, 685 aa) is 99.7% identical. The hackathon mapping table (`final_mapping.tsv`) gives 679/681. Run `20261030T213403Z-vc0658-motifs` gives the differences as N170H, C376S and a 4-aa deletion (A531/I533/T534/G535) in an EAL loop away from the catalytic residues.
- Gene name: **cdgI**, from Fong & Yildiz 2008 (PMID:18708497). It is not PdeS (PdeS is VC1710) and not MbaA (VC0703).

## Dashboard LLM call under review

> Integral inner-membrane c-di-GMP-binding protein containing GGDEF and EAL domains. (Tier A; GO:0035438 cyclic-di-GMP binding, GO:0005886 plasma membrane)

Verdict: **supported but under-called.** Both terms are correct. c-di-GMP binding comes from the DRaCALA screen of the exact N16961 ORF (PMID:26506097) and is novel to GOA, so it is scored COR. Plasma membrane is already in GOA by IBA, so it is scored CNN. The call explicitly withheld PDE activity. That is defensible from the evidence it was shown, but the stronger answer is cyclic-guanylate-specific phosphodiesterase activity (GO:0071111, already in GOA by IBA) for three reasons:
- the EAL catalytic residues are all intact;
- the ΔcdgI phenotype (more biofilm in Δcrp) led the authors to conclude that it acts as a PDE;
- the c-di-GMP binding was attributed to the EAL domain, because the protein has no I-site.

The dashboard evidence did not include the cdgI genetics. No purified-enzyme assay exists, so PDE activity is still an inference. The GGDEF A-site is intact too, so DGC activity cannot be excluded on sequence grounds, but nothing supports it.

## Literature caveats

- Two recent papers say CdgI "has been shown to be involved in dispersal": Esteves et al. 2025 (PMID:41329732) and James et al. 2025 (PMC11980369). Both cite Bridges, Fei & Bassler 2020 (PMID:33288715). The Bridges text says only "multiple c-di-GMP signaling proteins"; the loci are listed in Table 1, which is an image, and the cached full text never names VC0658. I did not add a dispersal annotation.
- NO upregulates VC0658 transcription (PMID:41329732). I did not treat this as evidence for the ARBA term "cellular response to nitric oxide", which I marked over-annotated.
- RpoS binds the cdgI promoter (PMID:40953128). This is context only and was not annotated.

## Tooling notes

- `just fetch-gene` was not rerun; the directory was seeded via `ubergraph:` because EBI OLS was down.
- `just fetch-gene-pmids`: the seeded YAML has no PMIDs, so it fetched nothing.
- `just fetch-fitness VIBCH VC_0658` failed: no local FEBA data, and the bulk download failed (`fetch-fitness` recipe line 900, exit 1). There is no Fitness Browser data for this gene.
- `just fetch-pmid 41329732` failed on the first try and succeeded on retry.
- `just deep-research-claude-code VIBCH VC_0658` was started in the background (it logged "agentapi not found in PATH"). It had not finished when the review was written, and the review does not depend on it.
- `just validate-terms` on the sidecar `VC_0658-dashboard-predictions-review.yaml` fails as expected: it validates against the GeneReview class, which has no `locus_tag` slot. `just validate-predictions` (which includes `validate-prediction-terms`) passes.
- Bioinformatics script: `VC_0658-bioinformatics/vc0658_motifs.py`, run via `beril run --name vc0658-motifs`.
