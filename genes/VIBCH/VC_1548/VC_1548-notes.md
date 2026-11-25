# VC_1548 (H9L4R2) notes: TtpB2

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_KQ257329.1_600` (*Vibrio cholerae*, 252 aa). Strata: Human Pathogen, Core, Dark-Function, SP. It has homologs in 13 organisms across 5 genera.
- Mapping: the sequence matches H9L4R2 (VC_1548, N16961 reference proteome) exactly, 252/252 identical (hackathon run `20261030T212629Z-finalize-vibch-mapping`, `final_mapping.tsv`). The dashboard ID is recorded as an alias.
- Prior names: eggNOG/InterPro "Protein of unknown function (DUF3450)"; UniProt (ProtNLM) "TonB system biopolymer transport component". STRING's orthogroup is COG1196 "Smc", which is spurious; the call correctly rejected it.
- The frozen call and page are in `VC_1548-dashboard-prediction-evidence/`, copied from hackathon run `20261030T212649Z-dashboard-page-nz-kq257329-1-600`.

## Identity: VC1548 is TtpB2, not TtpC

- The N16961 tonB2 operon is VC1548 ttpB2 → VC1547 ttpC2 → exbB2 → exbD2 → VC1544 tonB2 → VC1543 ttpD2.
- Barnes et al. 2020 (PMID:31595707) list *V. cholerae* El Tor TtpB2 as NP_231188 and TtpD2 as NP_231183. The deep-research run verified with NCBI ESummary/efetch that these resolve to VC1548 and VC1543.
- TtpC (Stork et al. 2007, PMID:17189363) is VC1547: "open reading frame 1547 (tolR)" (PMID:15557661). Its ExbB/TolQ-like homology is limited to a C-terminal region with three TM helices. In STRING, VC_1547 is the "ExbB-related protein".

## Topology

- DeepTMHMM (from the frozen call) gives class SP: signal peptide 1–18 and no α-helical or β-strand membrane segment. UniProt SignalP gives SIGNAL 1..18.
- The protein is not a lipoprotein. There is no lipobox at the cleavage site (…LLPAHA|AS…), and its only Cys is C4, inside the signal peptide. This was checked by eye on the sequence; no tool was run.
- Coils predicts a coiled coil at 42–97, which corresponds to the N-terminal leucine zipper described by Barnes et al.
- Conclusion: soluble periplasmic protein, annotated GO:0042597 with ISM. **GO:0009279 cell outer membrane is wrong.** The GO extractor inferred it from "exported" + "TonB2", but the protein has no β-barrel and no lipid anchor.

## Dashboard call verdict: supported (with one bad GO term)

- Call: "Putative exported TonB2-associated accessory protein supporting ferric siderophore uptake." This is correct.
- The call's evidence cites the 55.2%-identical *V. vulnificus* TtpB2 and correctly declines to transfer siderophore specificity.
- The call did not recognise that the query *is* the *V. cholerae* TtpB2 (NP_231188). It could have used the gene name.
- GO terms:
  - GO:0015891 siderophore transport: COR (ISS from *V. vulnificus*)
  - GO:0006826 iron ion transport: COR, broad
  - GO:0009279 cell outer membrane: NPI (DOMAIN_ARCHITECTURE_MISMATCH)

## Caveats

- All functional evidence comes from the *V. vulnificus* ortholog. VC1548 has never been mutated in *V. cholerae*.
- In the Barnes et al. complementation, the *V. cholerae* ttpB2 clone came from strain CA401, not N16961. It did not complement *V. vulnificus* Δ*ttpB2*, which the authors read as species-specific partner contacts.
- The PaperBLAST hit labelling VC1548 as "zot" (PMID:34106768) is a locus-tag artefact, and the call rightly rejected it.
- GOA has no annotations for H9L4R2, so all annotations are NEW.

## Tooling notes

- `just fetch-gene` was not rerun; the gene directory was pre-seeded via ubergraph because EBI OLS was down.
- `just fetch-fitness VIBCH VC_1548` failed: "no FEBA data source was reachable" and there is no FEBA mapping for VIBCH. *V. cholerae* is not a Fitness Browser organism in any case.
- `just fetch-gene-pmids` found no PMIDs in the seeded YAML.
- `just fetch-pmid`: the first batch loop hit a 2-minute tool timeout. 17189363 failed once and was then cached on retry. 9781885, 34106768, 25649684 and 28717590 were never cached; they are not cited, and their content was taken from abstracts or PaperBLAST summaries only.
- Deep research: `just deep-research-claude-code VIBCH VC_1548` completed. It warned "agentapi not found in PATH" but still produced output.
- No bioinformatics directory was created. The call does not depend on a domain or motif question, and the topology came from DeepTMHMM in the frozen call.
