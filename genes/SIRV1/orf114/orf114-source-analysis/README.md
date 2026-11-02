# Publisher evidence for the 2025 AcrIII-1 exchange

The papers have two canonical identities: PMID:40240860 (Comment, DOI:10.1038/s41586-025-08649-0) and PMID:40240850 (Reply, DOI:10.1038/s41586-025-08650-7). The normal PMID caches do not contain informative abstracts or complete article text. Do not insert publisher text into those caches manually.

`publisher-preview-excerpts.md` is a derived evidence artifact, not another publication. Reproduce it from the repository root:

```sh
uv run python genes/SIRV1/orf114/orf114-source-analysis/extract_publisher_previews.py
```

The script requires verbatim matches in normally fetched publisher caches and writes the input paths, canonical identities and SHA256 digests to `publisher-preview-extraction.json`. The historical cookies-error string occurs only in an existing input-cache filename. It is not part of the Reply's canonical URL or identifier. No third-party reproduction enters this extraction.

The main preview and Figure 1 caption distinguish viral-genome from plasmid expression. Figure 2 names the SIRV2 Para-gp29 construct and its induction conditions. These accessible passages establish experimental scope and design, without supplying the complete Comment's results or Reply's objections. The Reply preview reiterates cA4 chemistry and the previously demonstrated plasmid-expression phenotype. Earlier main-text inspection remains documented in the gene notes with its access/provenance limitations; the extracted preview is not represented as a complete revalidation of those texts.

The additional Figure 1 and Figure 2 pages were cached using the normal `ReferenceFetcher` URL provider. To refresh normally, instantiate `ReferenceFetcher(ReferenceValidationConfig(cache_dir=Path("publications")))` and call `fetch("url:" + publisher_url)` for the stable figure URLs recorded in the extraction manifest. Do not edit generated publication caches or the extracted passages to bypass quote validation.
