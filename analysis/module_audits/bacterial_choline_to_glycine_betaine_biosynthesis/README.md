# Choline uptake and glycine betaine synthesis audit

The required boundary is import of extracellular choline followed by its
oxidation to glycine betaine. E. coli BetT supplies a BCCT implementation and
Bacillus OpuB supplies a four-subunit-type ABC implementation. The oxidative
segment can use separate BetA/GbsB and BetB/GbsA enzymes or two independently
evidenced activities of a single Arthrobacter CodA protein. GbsB is a type III
alcohol-dehydrogenase-family enzyme, not a GMC flavoprotein implementation.

Thirteen completed reviews span E. coli, P. putida, B. subtilis and A. globiformis.
Eighteen curated references include four comparative/mechanistic reviews and
primary evidence placed on the relevant steps, subunits and connections.
Acinetobacter remains a literature comparator: its reported PMS-coupled assay
and unresolved N-terminal construct mapping do not establish an exact current
exemplar or native BetB dispensability. KT2440 BetT-I is an unresolved negative
comparator; this does not claim every KT2440 transporter has unknown specificity.

Run `uv run python modules/bacterial_choline_to_glycine_betaine_biosynthesis-source-analysis/check_audit.py`.
The 43 cases combine production topology with explicit family, activity,
complex-member, substrate-specific and bacterial-context evidence. Both CodA
steps must be present: GO:0033713 covers the first and substrate-qualified
GO:0004031 the second. A generic aldehyde oxidase does not establish oxidation
of betaine aldehyde. `curated-substrate-capabilities.yaml` binds that additional
manual judgment to the reviewed core and primary sources. Synthetic controls
test this distinction and taxon filtering; they do not assert native proteins.

All 94 historical rows, 26 raw UniProt/GOA files and four provider artifacts are
preserved. Eleven newly added annotations give 105 current rows, including three
inherited proposals. Six unresolved claims remain explicit; COMPLETE means the
curation decisions are finished, not that every biological question is settled.
New Falcon attempts failed with HTTP403 and are documented as manual research.

Focused gene, history and module checks pass. Five module advisories are retained:
one official PANTHER/UniProt classification disagreement for OpuBD and four
family-scope warnings. Characterized substrate-restricted activities are not
asserted family-wide merely to silence those warnings. Full-corpus validation,
publication, remote review/CI and actual merge remain pending.
