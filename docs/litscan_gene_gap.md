# Find papers that close gaps in gene function

Every Saturday at 14:00 UTC, LitScan searches Europe PMC for recent primary
papers, measures how much experimental GO evidence exists for each matched gene,
and proposes issues to create or update a gene review. It follows the
[DisMech literature scan](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/literature-scan.yml)
pattern of deterministic retrieval followed by curator-oriented triage.

## Run a dry scan

```sh
export GITHUB_REPOSITORY=ai4curation/ai-gene-review
bash .github/scripts/litscan-issue-ledger.sh > /tmp/aigr-issue-ledger.json
just litscan-gene-gap --days 30 --ledger /tmp/aigr-issue-ledger.json
just litscan-validate-gene-gap conf/litscan/gene_gap.yaml reports/litscan/gene-gap/*-gene-gap.json
```

A local run writes a JSON packet, a ranked Markdown table and eligible issue
bodies to `reports/litscan/gene-gap/`. A single candidate can be validated as
`GapCandidate` using the [LinkML schema](../src/ai_gene_review/schema/litscan_gene_gap.yaml).
Omit the ledger to explore results without GitHub access. Specify
`--date-from YYYY-MM-DD --date-to YYYY-MM-DD` for a fixed inclusive window.
Manual workflow dispatch defaults to a dry run and uploads the packet artifact.

## Read the score

The [configuration](../conf/litscan/gene_gap.yaml) lists the search terms,
recognized model organisms and strains, limits, scoring bands, and weights.
Three capped searches cover unknown function, refutation and biochemical
characterization. They use first publication date, exclude reviews and errata,
and can include Europe PMC preprints with `--include-preprints`.

Each ranked row represents one paper and one UniProt accession. The score adds
the matching rules and the issue body shows each contribution.

| Signal | Measurement |
| --- | --- |
| Experimental gap | QuickGO annotation rows by source evidence code. Bare protein binding is subtracted from the informative experimental total and molecular-function count. Zero informative experimental rows scores +5, compared with −4 above 40. |
| Electronic or phylogenetic support only | A nonempty record consisting entirely of IEA and IBA earns +1. |
| Unknown protein or family | UniProt protein names, Pfam DUF/UPF domains, and the number of UniProtKB entries with experimental GO cross-references in an assigned PANTHER family. A family with indexed members and zero experimental members earns +3. |
| New primary evidence | First-characterization, changed-function and direct assay language add points. High-throughput, review-like and clinical language subtract points. |
| Review impact | An existing review missing the reference earns +2. A reference already used by GOA on this product loses 6 points. |

These counts describe what the databases currently contain. An absent family
assignment supplies no family score. UniProtKB family coverage and QuickGO
annotation counts have different denominators. A statement about a catalytic
mutant can resemble evidence for a naturally inactive enzyme, so a curator or
the triage step must check the experimental subject.

## From paper to issue

1. Collect identifiers from the titles and bodies of all issues, open and
   closed. Suppress papers already mentioned there and candidates whose gene
   review already cites their PMID, DOI or Europe PMC preprint ID.
2. Match gene symbols from the title or repeated abstract mentions to UniProt
   entries in the configured species. Prefer reviewed entries and allow an
   unreviewed title match if it resolves uniquely. Gene aliases, model species,
   expression hosts and cross-species studies can produce false matches.
3. Rank by score, then by informative experimental count, reference and
   accession. By default at most ten candidates qualify for triage, with one
   per paper and a minimum score of six. A dispatch can lower the cap.
4. A read-only triage agent checks the gene, species, experiment and, for an
   update, what the paper would change in the review. It returns eligible rank
   numbers. The publisher validates the selection, refreshes the issue ledger,
   and files the generated bodies. A new-review issue gives the exact UniProt
   accession to fetch. An update issue points to the existing review.

The [workflow](../.github/workflows/litscan-gene-gap.yml) serializes runs.
Network lookups use per-host pacing and bounded retries on transient failures.
Dry runs need only read access. Scheduled publication uses the repository's
ai4c-agent App after triage, with issue-write permission.

The scan samples a configured number of records per query. Papers without a
recognized organism or gene symbol, claims made only in the full text and
papers outside the retrieval vocabulary can be missed.
