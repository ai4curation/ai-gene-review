# MET5 (YJR137C, P47169) notes

Evidence journal (UniProt and cached publications).

- Beta (hemoprotein) subunit of NADPH-sulfite reductase, alpha2beta2 [UniProt:P47169 "SUBUNIT: Alpha(2)-beta(2). The alpha component is a flavoprotein, the"]; purified enzyme [PMID:6751400].
- Needed for active SiR along with MET1, MET8, MET10, MET20 [PMID:1479340 "the products of at least five genes are needed for the synthesis of an enzymically active sulphite reductase. These genes are MET1, MET5, MET8, MET10 and MET20."].
- Siroheme prosthetic group made by Met1/Met8 [PMID:9003798 "Siroheme is a uroporphyrinogen III-derivative used by sulfite reductase as a prosthetic group."].
- Domains: flavodoxin-like FMN domain (aa 682-831; PF00258) plus NIR_SIR and NIR_SIR_ferr (siroheme/[4Fe-4S]) [UniProt:P47169]. FMN binding (IEA) was accepted for Met5; see the MET10 notes on the swapped domain.
- Wine-yeast MET5 mutants make less H2S [PMID:19236486].
- HDA vacuole and cell periphery (SWAT library, PMID:26928762) and stress granule (PMID:26777405): non-core, unconfirmed.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 33 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

The beta subunit supplies the sulfite-reducing siroheme/[4Fe-4S] catalytic module to the alpha2beta2 enzyme. PMID:6751400 is whole-enzyme biochemistry; cofactor biosynthesis is performed by Met1/Met8, not by Met5 itself (PMID:9003798). FMN placement has positive flavodoxin-domain evidence, not just absence from alpha. PMID:11319255 publisher full text explicitly names P47169 and Figure 3F/G identifies the beta FMN-domain architecture. Full text is normally cached as url:https://oup.silverchair-cdn.com/article-minimal/1018655; the PMID record remains abstract-only. The FMN-binding assignment is domain-based inference combined with holoenzyme FMN measurement, not a direct isolated-subunit FMN assay. The broad iron-sulfur-binding assertion is refined to the supported [4Fe-4S] term. Peripheral HDA vacuole, cell-periphery and stress-granule localizations are retained without inventing a tag artifact or requiring an established local function. Wine-yeast mutant H2S output (PMID:19236486) informs phenotype without asserting every allele abolishes all activity.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids yeast MET5` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-yeast-MET5-*.log`.

## 2026-10-26 PR #5560 evidence follow-up

Replaced the bare CDN citation with canonical PMID:11319255 and a reproducible source-analysis reference carrying exact Results/Figure 3F/G text and the durable DOI. Normal PMID refresh/warming did not recover the full body; no cache was hand-edited. Preserved domain-supported FMN binding without describing it as an isolated-subunit binding assay. Refined generic oxidoreductase to contribution to the holoenzyme activity and shortened the FMN summary.

All original annotation payloads and row order are preserved. Focused validation and automatic record-section backfill pass; generated pages and append-only history record this follow-up.


## 2026-10-26 approved-review citation follow-up

Added the verbatim Figure 3F/G legend adjacent to the existing PuSR domain quotation in FMN evidence. The legend identifies PuSR as yeast P47169 (Met5) and separately identifies Met10, making the target assignment explicit within the supporting evidence. Both passages remain cited to the committed reproducible source-analysis artifact accompanying canonical PMID:11319255; its source-cache SHA256 was rechecked. No annotation action, machine payload, cofactor inference strength or subunit role changed. This is comparative domain evidence, not a new isolated-subunit FMN-binding assay.
