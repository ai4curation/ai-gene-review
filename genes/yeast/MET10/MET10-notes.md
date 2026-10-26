# MET10 (YFR030W, P39692) notes

Evidence journal (UniProt and cached publications).

- NADPH-sulfite reductase is an alpha2beta2 hemoflavoprotein [PMID:6751400 "The enzyme consists of two types of subunit, alpha and beta, having molecular weights of 116,000 and 167,000, respectively."]; it contains 2 FAD, 2 FMN and 2 hemes per molecule [PMID:6751400 "this enzyme contains two FAD, two FMN and two hemes per molecule"].
- MET10 encodes the alpha (flavoprotein) subunit, with FAD/NADPH motifs but no obvious FMN motif [PMID:7928966 "together with a lack of obvious flavin mononucleotide-binding motifs in the MET10 deduced amino acid sequence, suggests that the yeast assimilatory sulfite reductase is a distinct type of sulfite reductase"].
- Domain check (UniProt DR lines): Met10 has Pfam FAD_binding_1 and NAD_binding_1 plus a PFOR-like N-terminal region (IPR002869) and no flavodoxin domain. Met5 has Pfam Flavodoxin_1 (PF00258) [UniProt:P47169]. **The FMN domain sits on the beta subunit in yeast**, unlike E. coli CysJ. The IBA for FMN binding on Met10 was therefore REMOVED.
- In vivo: MET10/MET5 point mutants cut wine H2S by 50-99% [PMID:19236486 "Specific mutations in the MET10 and MET5 genes, which encode the catalytic alpha- and beta-subunits of the sulfite reductase enzyme, respectively, were identified in six of the isolated strains."].
- Mms19 (CIA targeting) co-purification [PMID:22678362 "facilitates iron-sulfur cluster insertion into apoproteins involved in methionine biosynthesis"]: probably maturation of the SiR complex. Protein-binding rows REMOVED as uninformative.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 25 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

The NADPH/FAD electron-input alpha subunit contributes to the assembled sulfite reductase; it does not independently execute the whole six-electron sulfite-to-sulfide reaction. PMID:6751400 measured holoenzyme FAD, FMN, heme and alpha/beta stoichiometry; it did not localize every cofactor by isolated-subunit assay. PMID:7928966 identified MET10 FAD/NADPH motifs and lack of an obvious FMN module. Positive beta-subunit architecture is now supported by PMID:11319255 publisher full text: Figure 3F/G and the results explicitly identify S. cerevisiae P47169, place the CPR-like FMN domain on beta, and FAD/NADP modules on Met10. The canonical PMID cache remains abstract-only; the full text was cached through the normal URL fetcher at url:https://oup.silverchair-cdn.com/article-minimal/1018655. FMN binding on alpha remains REMOVE based on domain architecture and the existing PTHR19384 fungal-subfamily adjudication, not simply missing annotation or low donor count. The competing UniProt ECO:0000250 FMN note is acknowledged without inventing a particular donor. MMS19 association does not establish that Met10 carries an Fe-S cluster or prove direct CIA-mediated maturation of Met5. Wine-yeast H2S variants and peripheral cellular phenotypes are retained at their demonstrated scope.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids yeast MET10` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-yeast-MET10-*.log`.

## 2026-10-26 PR #5560 evidence follow-up

Replaced the bare CDN citation with canonical PMID:11319255 and a reproducible source-analysis reference carrying exact Results/Figure 3F/G text and the durable DOI. Normal PMID refresh/warming did not recover the full body; no cache was hand-edited. Retained the target-specific FMN-placement argument. Generic oxidoreductase rows now MODIFY to the already asserted holoenzyme activity with contribution explicit.

All original annotation payloads and row order are preserved. Focused validation and automatic record-section backfill pass; generated pages and append-only history record this follow-up.
