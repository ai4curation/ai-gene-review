# DnaJ annotation review notes

## 2026-08-29 — dedicated annotation-reviewer audit

Audited all 49 physical rows in `DnaJ-goa.tsv` one-for-one, including the two
PMID:15690043 protein-binding rows that share term, qualifier, evidence, and reference
but have distinct WITH/FROM partners (MalT/P06993 and DnaK/P0A6Y8). The qualifier
distribution is 26 `enables`, nine `acts_upstream_of_or_within`, seven `involved_in`,
five `located_in`, one `is_active_in`, and one `part_of`. Evidence codes are 20 IDA,
11 IPI, ten IEA, four IMP, three IBA, and one IEP.

### Core biology

DnaJ is the canonical type-I J-domain co-chaperone of DnaK. It binds non-native
clients, presents them to ATP-bound DnaK, and its HPD-containing J domain stimulates
DnaK ATP hydrolysis. The reviewed UniProt record states that "Unfolded proteins bind
initially to DnaJ" and describes multiple rounds of the DnaJ-DnaK-GrpE cycle as
necessary for efficient folding. The cached literature directly supports DnaJ-DnaK
binding [PMID:9860950, "DnaJ binds to at least two sites on the Escherichia coli Hsp70
family member DnaK"], refolding/unfolding by the complete system [PMID:20953191,
"one Hsp70 molecule consumed five ATPs to effectively unfold a single misfolded protein
into an intermediate that, upon chaperone dissociation, spontaneously refolded to the
native state"], and sigma32 antagonism [PMID:8599944, "DnaK and DnaJ cooperatively
inhibit sigma32 activity in heat shock gene transcription and GrpE partially reverses
this inhibition."]. GO:0001671 *ATPase activator activity* is current and defined as
binding to and increasing an ATP hydrolysis activity; PMID:1826368 directly shows that
DnaJ accelerates hydrolysis of DnaK-bound ATP. The three synthesized core functions
are therefore protein-folding chaperone activity, DnaK ATPase activator activity, and
the specialized sigma-factor antagonist output in heat-shock feedback.

The experimentally reported thiol-disulfide reductase activity is retained as
non-core [PMID:11732919, "DnaJ shows reductase activity and oxidase activity but little,
if any, isomerase activity."]. The older protein-disulfide isomerase row is MODIFY to
the reductase term because the later mechanistic abstract explicitly limits isomerase
activity. Homodimerization, lambda/plasmid replication, viral process, and historical
membrane association are retained as supported non-core properties or contexts.

### Obsolete GO:0051082

The three evidence-backed/non-CAFA GO:0051082 rows are MODIFY to current GO:0044183
*protein folding chaperone*. DnaJ's unfolded-client binding occurs in a productive
folding/refolding cycle and is not passive binding. Carrier-specific GO:0140309 is not
appropriate: DnaJ transfers clients to DnaK within a molecular chaperone cycle rather
than escorting an unfolded protein to a location or acceptor in the carrier sense.
A general holdase NTR would also understate DnaJ's DnaK ATPase activation and productive
folding-cycle function. No new ontology term is proposed.

### PAINT audit

Retrieved PTHR43096 PAINT through the public wrapper on 2026-08-29:
`just fetch-panther-paint PTHR43096 --extra-uniprot P08622`. Current PAINT retains
GO:0005737 and GO:0042026 at `PANTHER:PTN002454318`; both IBA rows are valid core
transfers (`NO_FAILURE_CORE`). DnaJ itself is valid descendant evidence and is not
circular. Current PAINT contains no GO:0051082 assertion at that node, so the historical
GO:0051082 IBA is `SOURCE_STALE_OR_MISSING`; its direct DnaJ biology supports the
replacement term, not a current propagation claim.

### CAFA citation mismatch

Five physical rows were assigned by CAFA with PMID:9103205. The cached record is
abstract-only, but its title and complete abstract explicitly describe the crystal
structure of GrpE bound to DnaK and never mention DnaJ. This is a verified citation
mismatch, not an inference from a foregrounded paralog and not a MOD experimental
curation decision. The reference is marked `MISCITED`. All five rows are marked
over-annotated because their DnaJ biology is plausible or independently established
but their cited source does not support the claims. The DnaJ-DnaK binding term remains
supported through correctly cited IPI rows; the generic complex and assembly terms
remain excluded from the retained term set because the CAFA source assays a GrpE-DnaK
complex without DnaJ.

### Evidence limitations and final decisions

All physical PMID caches except PMID:24561554 are abstract-only. Experimental rows
were retained or modified only where the abstract directly supports the decision or
where the function is independently secure; no MOD experimental annotation was removed
for absence of inaccessible full text. The five CAFA provenance cases are uniformly
marked over-annotated because their source mismatch is explicit while the broader
biology is not refuted. The erroneous electronic ATP-binding row is removed: DnaJ
stimulates hydrolysis of DnaK-bound ATP but does not itself bind ATP.

Final physical GOA-row action counts: ACCEPT 18, MODIFY 15, KEEP_AS_NON_CORE 8,
REMOVE 1, MARK_AS_OVER_ANNOTATED 7, with no PENDING or UNDECIDED rows. One
author-supplied NEW row proposes GO:0001671 from the direct ATPase-stimulation assay.

The two high-throughput DnaJ-MalT protein-binding rows are marked over-annotated:
neither binary screen establishes a client state or physiological consequence, so
bare GO:0005515 is not retained for a promiscuous chaperone. The generic DNA replication
IMP is narrowed to GO:0044829 *host-mediated activation of viral genome replication*,
matching the demonstrated lambda-phage phenotype. The direct historical membrane
assays remain non-core rather than being overruled; the open question is what mechanism
or fractionation behavior explains that experimentally observed pool.
