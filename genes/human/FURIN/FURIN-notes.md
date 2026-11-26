# FURIN review notes

## Review context

- `just fetch-gene human FURIN` and `just fetch-gene-pmids human FURIN` were run before this review worktree was handed off.
- Provider deep research was attempted before handoff, but the available Falcon and Perplexity providers were unavailable and `claude-code` was not logged in. No genuine provider report was produced, and this review does not create a fake `FURIN-deep-research-{provider}.md` file.
- `just paint-losses human FURIN` could not run through the wrapper against `/srv/home/cmungall/orca/venvs/ai-gene-review`, because that environment did not contain `ai_gene_review`. Running the same module directly with `PYTHONPATH=src .venv/bin/python -m ai_gene_review.validation.gene_paint_losses human FURIN` reported: "No IRD or IKR loss on this gene's lineage."

## GO-CAM 6796b94c00004996 consistency note

The SARS-CoV-2 entry GO-CAM annoton `gomodel:6796b94c00004996/6796b94c00005002` correctly names human FURIN and gives SARS-CoV-2 spike as the `has_input` substrate, but its molecular function is the generic `GO:0008236 serine-type peptidase activity`, while FURIN's supported direct function is `GO:0004252 serine-type endopeptidase activity`. The annoton also lacks both `occurs_in` and `part_of`. FURIN primes SARS-CoV-2 spike at the S1/S2 site in the secretory pathway of virus-producing cells, so this activity is mechanistically different from a target-cell plasma-membrane TMPRSS2 entry step and from an endosomal cathepsin route. Its `enabled_by` evidence, PMID:9325052, is a TMPRSS2 cloning paper rather than a FURIN or spike-cleavage paper.
