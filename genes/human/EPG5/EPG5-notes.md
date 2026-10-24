# EPG5 notes (human, Q9HCE0)

Deep research: not run (falcon times out after 600 s in this environment and perplexity-lite is not
installed). Review based on cached publications, the UniProt record and PubMed abstracts.

## Key findings
- Rab7 effector setting autophagosome fusion specificity [PMID:27588602 "EPG5 is recruited to late endosomes/lysosomes by direct interaction with Rab7 and the late endosomal/lysosomal R-SNARE VAMP7/8"].
- Binds LC3 and STX17-SNAP29; stabilizes trans-SNAREs [PMID:27588602 "EPG5 stabilizes and facilitates the assembly of STX17-SNAP29-VAMP7/8 trans-SNARE complexes, and promotes STX17-SNAP29-VAMP7-mediated fusion of reconstituted proteoliposomes"]. Full text not cached (abstract only).
- Vici syndrome; autophagosome clearance block [PMID:23222957 "Further studies showed a severe block in autophagosomal clearance in muscle and fibroblasts from individuals with mutant EPG5"].
- mEPG5 needed for degradative autolysosomes [PMID:20550938 "EI24 and mEPG5 are required for formation of degradative autolysosomes."].
- Autophagy-independent endolysosomal delivery of CpG to TLR9 compartments [PMID:29130391 "Here we show that EPG5 also plays autophagy-independent roles in the trafficking of molecules from the EEs to LEs and lysosomes."].

## Decisions
- nucleotide transport (IMP) -> MODIFY to endosome to lysosome transport: cargo is a CpG oligonucleotide inside vesicles.
- cellular response to dsDNA -> over-annotated; TLR9 pathway kept as non-core (acts upstream).
- NEW: vesicle membrane tethering activity (core MF), small GTPase binding, SNARE binding (all from PMID:27588602).


## 2026-10-24 original-source augmentation

The earlier entries above are retained as historical notes. The current assessment supersedes the earlier dsDNA over-annotation decision and tethering-core confidence; precise sources and access limits are recorded in [EPG5-source-guide.md](EPG5-source-guide.md).

All 12 imported annotations and the three inherited proposed annotations remain in their original order with unchanged source fields. All 33 inherited YAML supporting-text occurrences remain unchanged, as do both natural products. No publication quotations or annotation rows were added. The final action distribution is six ACCEPT, four KEEP_AS_NON_CORE, one MODIFY, two UNDECIDED and two retained NEW. The inherited DRAFT status is retained for the publisher's separate status transition.

The 2017 human original establishes RAN association in cell extracts, perinuclear localization, and EPG5-dependent vesicular CpG delivery. Supported generic RAN binding is retained as non-core under campaign policy. Localization is not dismissed because the proposed karyopherin mechanism remains unproven. Nucleotide transport is refined to endosome-to-lysosome transport. The TLR9 phenotype supports a contextual trafficking contribution. The dsDNA-response row remains unresolved: the signaling reagent is single-stranded CpG ODN, while the separate dsDNA baculovirus assay integrates multiple trafficking and expression steps. No reasoning depends on the imported relationship qualifier.

The original 2016 supplement directly demonstrates human-fragment Rab7 binding and binding to SNAREs/assembled SNARE complexes, with human-cell association and knockdown evidence. The proteoliposome lipid-mixing system instead uses worm proteins. The main article remains unavailable; the recovered supplement and main Figure 6 image do not remove that limitation. The inherited small-GTPase-binding and SNARE-binding proposals are retained. The inherited vesicle-tethering proposal is UNDECIDED, not removed: a current valid term requires physical membrane bridging, and the inspected evidence does not isolate this activity for human EPG5.

Independent human structural originals from 2021 and 2025 support elongated architecture and GABARAP interaction. The 2025 full-length-cell and peptide results revise the earlier speculative multivalent LIR model; modeled unresolved loops are not direct structural contacts. Both papers support a tethering model without providing an isolated human membrane-bridging assay. Their normal publication files were genuinely fetched as separate additions; all 16 preexisting archived/runtime publication files remained exact.

The first core now uses directly supported SNARE binding at the lysosomal membrane in autophagosome-lysosome fusion/clearance. The second remains endocytic cargo delivery, with no invented distinct molecular function. No nuclear carrier, kinase, nucleic-acid sensor, transporter, universal binary partner binding or short-natural-product equivalence is inferred.

Actual PAINT topology/MSA and the current IBD export support the cytoplasmic and lysosomal location inferences. The displayed human sequence matches exactly. The imported fusion IBA remains in current QuickGO, but its corresponding IBD was not recovered from that export; the fish record is itself IBA. This provenance gap is explicit, while biological acceptance rests on independently read human originals. No target self-WITH or donor-count objection is used. No negated record was found on the inspected target path within the available IBD export; a separate NOT export was not recovered.

Reviewer reference flags record main-original access rather than modifying normal cache metadata. PMID:27588602 remains main-full-text unavailable despite the recovered supplement; PMID:20550938 remains abstract-only in this assessment. The two new structural references use exact genuinely fetched titles. Original findings and quotations are preserved as prior provenance. Source guide, evidence scopes and private validation receipts accompany this candidate; canonical history, rendering and publication remain the publisher's responsibility.


## Inherited proposal withdrawal, 2026-10-24

The inherited curator-authored GO:7770062 vesicle membrane tethering activity proposal is marked `retired: true`. It is withdrawn from active proposed annotations because isolated human membrane-bridging activity remains unresolved. This is retirement of our historical proposal, not a claim that GOA withdrew a source row: the assertion was never among the 12 imported GOA contexts. Its UNDECIDED review, original term/evidence/reference fields and every inherited supporting quotation remain intact at the same YAML paths. No machine-sourced row is retired or altered.

The document contains 14 active annotation records (12 imported and two retained NEW binding proposals) plus one retired unresolved historical proposal. Active actions are six ACCEPT, four KEEP_AS_NON_CORE, one MODIFY, one UNDECIDED and two NEW; the retired record carries the second UNDECIDED assessment. All 33 inherited quotation values and paths remain unchanged. The preexisting suggested question and experiment continue to address whether human EPG5 can bridge membranes directly. This metadata correction makes no new biological assertion and changes neither core function.

Canonical validation on 2026-10-24: normal review validation, strict GO-term validation, computed-status check and HTML rendering all passed. The existing HTML was refreshed; source files and publication caches were preserved.
