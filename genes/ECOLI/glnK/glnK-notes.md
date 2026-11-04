# glnK (P0AC55) notes

Provider deep research was NOT run for this gene (not available in this session); the review is
based on the cached publications (`publications/PMID_*.md`; PMID:11847102 full text, others abstract-only)
and the curated UniProt record.

## Summary
- PII paralog of GlnB in the glnK-amtB operon; activates GS adenylylation and is uridylylated by GlnD
  [PMID:8843440 "Like PII, purified GlnK can activate the adenylylation of glutamine synthetase in vitro, and, in vivo, the GlnK protein is uridylylated in a glnD-dependent fashion."]
- Inhibits AmtB: [PMID:14668330 "We have now shown that Escherichia coli AmtB is inactivated by formation of a membrane-bound complex with GlnK."];
  structure [PMID:17220269 "the tip of which inserts deeply into the cytoplasmic pore exit, blocking ammonia conduction"];
  [PMID:17190799 "the trimeric channel is blocked directly by GlnK"].
- Membrane sequestration depends on AmtB and deuridylylation [PMID:11847102 "the unmodified form of the protein then associates tightly with AmtB in the inner membrane"].
- ATP-dependent, 2-OG-sensitive complex [PMID:16864585 "The interaction of GlnK with AmtB is dependent on ATP and is also sensitive to 2-oxoglutarate."]
- ADP orients GlnK for blockade [PMID:17190799 "The hydrolyzed product, adenosine 5'-diphosphate orients the surface of GlnK for AmtB blockade."]
- Role in starvation [PMID:12366843 "Thus, one specific role of GlnK is to regulate the expression of Ntr genes during nitrogen starvation."]

## Curation decisions
- AmtB protein-binding rows (structures) MODIFY to GO:0016248 channel inhibitor activity; Y2H rows REMOVE.
- cytoplasm -> cytosol (MODIFY); plasma membrane -> cytoplasmic side of plasma membrane GO:0009898 (MODIFY).
- enzyme regulator activity -> enzyme activator activity (GlnE) MODIFY.
- positive regulation of nitrogen utilization (IMP, PMID:12366843) MODIFY to GO:0006808 since the reported effect is mixed in sign (limits Ntr expression, enables recovery).
- NEW: ADP binding (GO:0043531), PMID:17190799.
