# NAP1 curation notes

## 2026-09-02 - Audit update: fixed misattributed evidence for GO:0051082 (unfolded protein binding)

While auditing the existing review, found that the annotation `GO:0051082 unfolded
protein binding` (evidence_type IDA, original_reference_id PMID:31062022) had been
reviewed with `action: MODIFY`, proposing to replace it with `GO:0000511 H2A-H2B
histone complex chaperone activity`.

This is a genuine oversight: PMID:31062022 (Rossler et al. 2019, "Tsr4 and Nap1, two
novel members of the ribosomal protein chaperOME") is specifically about Nap1 acting
as a dedicated chaperone for the ribosomal protein **Rps6/eS6**, not H2A-H2B:

> "We report the identification of Nap1 and Tsr4 as direct binding partners of Rps6
> and Rps2, respectively. Both factors promote the solubility of their r-protein
> clients in vitro." [PMID:31062022, Abstract, "Nap1 and Tsr4 as direct binding
> partners of Rps6 and Rps2"]

The MODIFY action's justification quoted a Falcon deep-research statement ("The
primary substrate of Nap1 is the H2A-H2B dimer") that is drawn from different papers
(Fung et al. 2024, PMID:39601790; Nagae et al. 2023) discussing Nap1's H2A-H2B
chaperone role in general - it does not describe PMID:31062022's finding and should
not have been used to justify re-terming this specific Rps6-linked annotation as an
H2A-H2B chaperone activity. Replacing GO:0051082 with GO:0000511 for this reference
would misattribute Rps6-chaperone evidence to the histone-chaperone function.

Fix: changed the action from MODIFY (proposed_replacement_terms: GO:0000511) to
KEEP_AS_NON_CORE, kept the term GO:0051082 as-is (a defensible generic description of
Nap1's Rps6-chaperoning activity), and replaced the review's justification/supported_by
with a verbatim quote directly from PMID:31062022. This is consistent with the
existing KEEP_AS_NON_CORE treatment already given to the other PMID:31062022-derived
annotation, GO:0042274 ribosomal small subunit biogenesis, both reflecting Nap1's
peripheral ribosome-biogenesis-chaperone role distinct from its core H2A-H2B chaperone
function (GO:0000511, GO:0042393), which remains correctly and independently
supported by PMID:39601790 and PMID:27225933.

## 2026-09-02 - Fixed two non-verbatim reference findings for PMID:39601790

While validating the above change, `ai-gene-review validate --terms` reported two
pre-existing ERROR-level failures unrelated to the GO:0051082 fix: the `findings`
entries under the top-level `references:` block for PMID:39601790 quoted
markdown-bolded text lifted from the Falcon deep-research summary (e.g. "Nap1 is
described as the **principal cytosolic H2A-H2B chaperone**...") rather than verbatim
text from the cached publication `publications/PMID_39601790.md`, so they failed the
verbatim-substring check.

Fixed both `supporting_text` values to genuine verbatim substrings of the cached full
text of PMID:39601790:
- "mostly localized to the yeast cytoplasm where it chaperones newly synthesized and
  folded H2A-H2B" [PMID:39601790, Introduction]
- "Nap12•H2A-H2B•Kap114•RanGTP complex explains how both Kap114 and Nap12 interact"
  [PMID:39601790, Introduction]

The `statement` summaries (which are not verbatim-checked) were left unchanged as they
accurately paraphrase these passages. Other `supported_by`/`supporting_text` entries
elsewhere in the file that cite `file:yeast/NAP1/NAP1-deep-research-falcon.md` (rather
than the PMID directly) using this same bolded phrasing are correct as-is, since that
phrasing is verbatim within the deep-research file itself.

Both `ai-gene-review validate --verbose --terms` and `ai-gene-review validate-goa`
pass after these changes (validate passes with pre-existing, unrelated warnings about
abstract-only PMIDs, which are out of scope for this fix).
