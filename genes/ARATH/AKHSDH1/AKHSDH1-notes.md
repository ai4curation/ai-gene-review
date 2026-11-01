# AKHSDH1 annotation review notes

PMID:16216875 independently studied both isoforms. Author-uploaded full text was read at https://www.researchgate.net/publication/7548936_Identification_of_six_novel_allosteric_effectors_of_Arabidopsis_thaliana_Aspartate_kinase-Homoserine_dehydrogenase_Physiological_context_sets_the_specificity . Methods and Results identify At1g31230 as isoform I and At4g19710 as II. The earlier recombinant enzyme in PMID:11812230 and the site-directed regulation in PMID:12435751 belong to II, while PMID:12602885 explicitly complements with akthr2. Neither distinction negates the direct isoform-I activity in PMID:16216875. Assays use NADPH, not NADH; UniProt separately curates a NAD-dependent reaction, but the cited primary did not resolve its target-specific support. NAD+ binding remains UNDECIDED rather than inferred absent. Physiological effector conclusions are bounded to leaf chloroplast composition. The kinase first step participates in lysine production; the HSDH third step does not itself lie on the lysine branch.

## Evidence access and provenance

Applied review and annotation-reviewer skills; reciprocal scientific consultation with the fungal-panel reviewer confirmed shared precursor participation and cofactor distinctions. Normal gene seeding used the exact UniProt accession. Falcon research and publication fetching were launched in parallel; Falcon returned403 and the actual perplexity-lite fallback returned401 (quota). No provider report was fabricated. Manual primary-source reading, normal publication caching, and reproducible supplemental-table extraction supply the evidence. All original annotation payload fields are preserved. The seeded panel contains no negated rows; this was explicitly checked rather than applying a generic negation rule.

Supplementary localization evidence is in ../TS1/TS1-source-analysis/ (same ARATH parent). PMID:18431481 exact locus rows support chloroplast/stromal assignment;28887381 labels TS1 plastid. Supplement endpoints for PMID:25293756 and PMID:20061580 returned no usable ZIP; no absent-row inference is made.

Final QA: the CLAUDE.md root-organelle exception explicitly excludes plastids, so supported chloroplast-to-stroma refinements follow the general refinement policy. Original negated-row count is zero. PMID:22303247 contains an incorrect HSK locus and a homoserine-dehydrogenase wording slip; primary evidence governs the identities and reactions.


## PR #5569 source-specific corrective review (2026-10-26)

Repaired mangled PMID/GO citation strings and spacing in reviewer prose. Source quotations, original annotations, evidence judgments, and target-specific supplemental source analyses remain unchanged.

Annotation actions are unchanged; revisions clarify evidence or narrative.

All 25 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.


## 2026-10-26 PR #5569 second follow-up

The earlier NAD-reaction MODIFY and NAD-binding uncertainty are superseded. RHEA:15757 specifies NAD-dependent homoserine oxidation, and the live GO:0004022 definition includes oxidation of an alcohol with NAD+. Homoserine carries the appropriate primary alcohol. GO:0004412 currently specifies NADP+; it is a sibling activity, not a more precise synonym for the NAD reaction. The curated NAD activity and integral NAD binding are retained, and the broad oxidoreductase refinement includes both cofactor forms, consistently with thrA, metL, HOM6 and hom6.

AKHSDH1/Q9SA18 explicitly links its curated NAD reaction to PMID:16216875 with ECO:0000269. The author-uploaded full text of PMID:16216875 was re-read: its documented HSDH assays use 200 µM NADPH, and no matched NADH comparison was found. Those methods do not establish NAD exclusion and do not invalidate the separately curated reaction. The retained reaction is therefore explicitly attributed to curated target chemistry, without claiming that the inspected methods directly demonstrate NAD use or equal cofactor efficiencies. The matched-cofactor question remains, and a separate question asks whether GO should generalize the NADP-specific term or create a substrate-specific NAD sibling. Normal ResearchGate URL recovery returned HTTP 403; the accessible author text was read through the web tool, and no cache was hand-written.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.
