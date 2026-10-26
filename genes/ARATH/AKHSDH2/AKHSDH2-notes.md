# AKHSDH2 annotation review notes

PMID:12602885 explicitly studies akthr2 on chromosome 4 and complements yeast hom6 and hom3. PMID:16216875 full text explicitly maps At4g19710 to isoform II and compares it with At1g31230 isoform I; its HSDHII is relatively insensitive at physiological Thr while high concentrations can inhibit. PMID:11812230 reports a470-kDa apparent oligomer converting to a320-kDa form with Thr; this is not an obligatory in vivo dimer claim. PMID:12435751 specifies the Q443/Q524 regulatory sites on isoform II. PMID:8204822 is the older akthr1 cloning paper, not direct new characterization of AKHSDH2; the common aspartate-metabolism claim is independently supported by isoform-II studies. NADPH/NADP assays are established, whereas NAD+ binding is retained as unresolved, not rejected from lack of NADH assay.

## Evidence access and provenance

Applied review and annotation-reviewer skills; reciprocal scientific consultation with the fungal-panel reviewer confirmed shared precursor participation and cofactor distinctions. Normal gene seeding used the exact UniProt accession. Falcon research and publication fetching were launched in parallel; Falcon returned403 and the actual perplexity-lite fallback returned401 (quota). No provider report was fabricated. Manual primary-source reading, normal publication caching, and reproducible supplemental-table extraction supply the evidence. All original annotation payload fields are preserved. The seeded panel contains no negated rows; this was explicitly checked rather than applying a generic negation rule.

Supplementary localization evidence is in ../TS1/TS1-source-analysis/ (same ARATH parent). PMID:18431481 exact locus rows support chloroplast/stromal assignment;28887381 labels TS1 plastid. Supplement endpoints for25293756 and PMID:20061580 returned no usable ZIP; no absent-row inference is made.

Final QA: the CLAUDE.md root-organelle exception explicitly excludes plastids, so supported chloroplast-to-stroma refinements follow the general refinement policy. Original negated-row count is zero. PMID:22303247 contains an incorrect HSK locus and a homoserine-dehydrogenase wording slip; primary evidence governs the identities and reactions.


## PR #5569 source-specific corrective review (2026-10-26)

Repaired mangled PMID/GO citation strings and spacing in reviewer prose. Source quotations, original annotations, evidence judgments, and target-specific supplemental source analyses remain unchanged.

Annotation actions are unchanged; revisions clarify evidence or narrative.

All 26 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.


## 2026-10-26 PR #5569 second follow-up

The earlier NAD-reaction MODIFY and NAD-binding uncertainty are superseded. RHEA:15757 specifies NAD-dependent homoserine oxidation, and the live GO:0004022 definition includes oxidation of an alcohol with NAD+. Homoserine carries the appropriate primary alcohol. GO:0004412 currently specifies NADP+; it is a sibling activity, not a more precise synonym for the NAD reaction. The curated NAD activity and integral NAD binding are retained, and the broad oxidoreductase refinement includes both cofactor forms, consistently with thrA, metL, HOM6 and hom6.

AKHSDH2/O81852 curates NAD chemistry by similarity to AKHSDH1/Q9SA18; this is not an independently inspected isoform-II NAD assay. The author-uploaded full text of PMID:16216875 was re-read: its documented HSDH assays use 200 µM NADPH, and no matched NADH comparison was found. Those methods do not establish NAD exclusion and do not invalidate the separately curated reaction. The retained reaction is therefore explicitly attributed to curated target chemistry, without claiming that the inspected methods directly demonstrate NAD use or equal cofactor efficiencies. The matched-cofactor question remains, and a separate question asks whether GO should generalize the NADP-specific term or create a substrate-specific NAD sibling. Normal ResearchGate URL recovery returned HTTP 403; the accessible author text was read through the web tool, and no cache was hand-written.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.
