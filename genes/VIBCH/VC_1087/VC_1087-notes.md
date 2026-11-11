# VC_1087 (Q9KT18, HnoD) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_QKKU01000066.1_29` (*Vibrio cholerae*, 447 aa), https://gene-annotate-dashboard.kbase.us/review/NZ_QKKU01000066.1_29
- Strata shown on the dashboard: Human Pathogen, Core, Annotation-Promoted, GLOB. Homologs in 10 organisms across 10 genera. DeepTMHMM: cytoplasmic 1-447.
- UniParc UPI000893570D (MD5 02493ECE8AED924600384071F87CA7A1) has no active UniProtKB entry. The review is therefore filed on N16961 Q9KT18 (VC_1087), which is 91.3% identical to the dashboard protein (408/447, full length, no gaps).
- Is it an ortholog or a paralog? Identity of 91% is low for two strains of one species, so the whole N16961 proteome was searched (`VC_1087-bioinformatics/`, beril run `20261030T213524Z-vc1087-ortholog-hdgyp`). VC_1087 scores 2093. The next hit is VC_1086 at 193, matching the REC domain only. The REC-HD-GYP paralogs VC_1348 and VC_A0210 are about 25% identical. The dashboard protein is unambiguously the VC_1087 ortholog. Its 39 differences cluster in the REC N-terminus (17) and the coiled-coil linker; 4 lie in the HD-GYP domain. The phosphoacceptor Asp60 and the degenerate HD-GYP motifs are identical to VC_1087. The source genome is probably a divergent non-O1 or environmental lineage. PaperBLAST on the dashboard page reports 88.6% identity, which reflects a different alignment method.
- The other hits in the batch mapping run (`20261030T212608Z-map-vibch-uniprot`), such as RtxA at 41% and VC_A0849 at 37%, are k-mer/alignment artefacts of that run against very long proteins. They are not real homologs.

## Dashboard LLM call under review

> HnoD-like phosphoacceptor response regulator with a degenerate HD-GYP domain, receiving phosphotransfer from HnoK and HnoS. (Tier A; GO:0000156 phosphorelay response regulator activity, GO:0000160 phosphorelay signal transduction system)

My verdict is that the call is **supported**.
- VC1087 is the V. cholerae HnoD. Plate & Marletta 2012 (PMID:22542454) name hnoB (VC1086) and hnoD (VC1087) and show phosphotransfer from V. cholerae HnoK (VCA0719) and HnoS to both, using the V. cholerae proteins.
- The HD-GYP domain is degenerate: GLM**HQ**IG in place of HD, and DGTG**KP** in place of GYP. McKee et al. 2014 (PMID:25343965) found no c-di-GMP hydrolysis by VC1087 in vitro or in vivo.
- GO:0000156 is COR (new). GO:0000160 is CNN (already in GOA as InterPro IEA).
- What the call omits: the probable output of HnoD, phosphorylation-reversible inhibition of the HnoB EAL phosphodiesterase. This was shown only for the S. oneidensis proteins and has not been tested for VC1086/VC1087.
- The name "HnoS" is used for one of the two histidine kinases in the VC1080-VC1087 operon. The paper does not give its locus tag; STRING partners are VC_1084 and VC_1085.

## GOA decisions

- GO:0000160 IEA (InterPro): ACCEPT, with IDA-level support from PMID:22542454. A separate NEW IDA row was not added, because `just validate` rejects NEW for a term already in GOA.
- GO:0008081 phosphoric diester hydrolase activity, IEA (ARBA): REMOVE. This is a pseudoenzyme.
- NEW: GO:0000156 IDA PMID:22542454.
- No term was added for the HnoB-inhibition output (for example enzyme inhibitor activity). The evidence comes from a Shewanella ortholog at about 30% identity.

## Tooling notes

- `just fetch-gene` was not rerun. The directory had already been seeded through ubergraph because EBI OLS was down.
- `just fetch-gene-pmids VIBCH VC_1087`: the stub YAML had no PMIDs, so nothing was fetched. The key papers were fetched with `just fetch-pmid` (22542454, 23131828, 25343965, 26000450, 30060647, 30420597, 30557874, 31658256), all with full text.
- `just fetch-fitness VIBCH VC_1087` failed: there is no local FEBA data, the bulk download failed, and VIBCH is not a Fitness Browser orgId. The dashboard page also reports no fitness data for this protein.
- `just deep-research-claude-code VIBCH VC_1087` completed. Its summary overstates the HnoB-inhibition role as "established" for V. cholerae, but its own gaps section correctly notes that this was shown only for Shewanella.
- `just validate-terms` on the predictions sidecar fails with "No such slot locus_tag as an attribute of GeneReview" because the recipe validates against the GeneReview class. `validate-prediction-terms`, which `validate-predictions` runs, passes.
- beril run: the first attempt, `20261030T213451Z-vc1087-ortholog-hdgyp`, failed (exit 1, numpy int64 JSON error) and left a literal `$BERIL_RUN_DIR` directory, which was removed. The successful run is `20261030T213524Z-vc1087-ortholog-hdgyp`. `BERIL_RUN_DIR` already ends in `/out`, so its outputs are under `out/out/`.
