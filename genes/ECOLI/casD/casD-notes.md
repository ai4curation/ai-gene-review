# casD (Cas5e), *Escherichia coli* K-12 — UniProt Q46898

Curation journal. All assertions carry inline provenance as
`[PMID:xxxxxxx "verbatim supporting text"]`, copied verbatim from the cached records in
`publications/`.

## Session 1 (2026-10-01): initial full review

Reviewed together with casA, casB, casC and casE as one complex.

### Position and role

CasD is the single Cas5 subunit, and it caps the 5' end of the guide at the tail of the
complex
[PMID:25123481 "Cas5 caps the tail of the Cas7 filament at the 5′-end of the crRNA"],
where it is one of three proteins sandwiching that end
[PMID:25103409 "Cas6e binds the 3′ end of the crRNA at the head of the complex, while the 5′-end of the crRNA is sandwiched between three protein subunits (Cas5, Cas7.6 and Cse1) in the tail"].
Its fold is a modified RRM "fist" with a thumb that arches over the top, and it performs
three distinguishable jobs at once
[PMID:25103409 "these six nucleotides (-8 to -3) are recognized by Cas5e, which may block propagation of Cas7 oligomerization at the 5′-end of the crRNA, induce a conformational change in the finger domain of Cas7.6, and provide a platform for the recruitment of Cse1 to the tail"]:
it reads the repeat-derived 5' handle, it terminates the CasC filament, and it provides
the docking platform for CasA.

### Nucleic-acid binding

Unlike CasC, CasD reads sequence
[PMID:25103409 "Unlike Cas6e and Cas5e, which make sequence-specific interactions with portions of the CRISPR repeat sequence, the Cas7 proteins polymerize along the crRNA via non-sequence specific interactions"],
with the 5' handle threaded along the thumb arch
[PMID:25103409 "The last 7-nts on the 5′-end of the crRNA form a unique S-shaped curve that follows along the arch of the Cas5e thumb"],
and specific hydrogen bonds to individual bases
[PMID:25123481 "the position of C7 is stabilized through sequence specific hydrogen bonds with Arg108 from the Cas5 thumb"].
So the two GOA `RNA binding` IDA rows are solid and are, if anything, under-specific.

CasD also carries a `GO:0071667 DNA/RNA hybrid binding` IDA row. This is directly
supported by the target-bound structure
[PMID:25123481 "two residues from the thumb of Cas5 (Tyr85 and Gln105) stabilize the first duplex segment (positions 1-5) through van der Waals contacts with the exposed face of the base at position 1 of the hybrid"].
Note the significance: positions 1-5 are the PAM-proximal "seed", the segment where
complementarity matters most, so CasD's hybrid contact is at the point where target
recognition is initiated.

### The structural-subunit problem

CasD's single `GO:0005515 protein binding` IDA row is about intra-complex contacts with
CasA and CasC (UniProt Q46898 SUBUNIT: "Interacts directly with CasA and CasC"). As for
casA, casB, casC and casE, I MODIFY it to GO:0005198 structural molecule activity, which
is exactly what the structure supports — CasD terminates the filament, remodels the
adjacent Cas7.6 finger domain, and creates the pore that CasA's L1 helix plugs into
[PMID:25103409 "In the Cascade structure the L1-helix inserts into the Cas5e helix-binding pore and makes base-specific interactions with the AAC triplet"].
GO has no child of GO:0005198 for a non-ribosomal ribonucleoprotein, so the parent is
the correct level, and the same term is used for all five subunits.

### The GO:0043571 IEA row — kept, but non-core

GOA carries `involved_in GO:0043571 maintenance of CRISPR repeat elements` as an IEA from
InterPro:IPR021124 (CRISPR-associated protein, Cas5). GO:0043571's definition is broad
and does include processing: "transcription of the CRISPR repeat arrays into RNA and
processing".

Comparator check. Querying QuickGO for non-IEA annotations to GO:0043571 returns 14 rows,
and they include `UniProtKB:D4GQN7 cas5 IMP PMID:24459147` — a Cas5 protein with
experimental support for this term — alongside Cas1, Cas2, Cas3, Cas6f, Csy3 and Cas9.
So the term is used for Cas5-family proteins by convention, and the IEA is not an
out-of-family mis-mapping.

But for *E. coli* CasD the direct evidence argues it is not core. Brouns first saw crRNA
lost in the casD knockout
[PMID:18703739 "The same product was present in much higher amounts in the casA, casB, and casC knockout strains but absent from strains lacking the overlapping genes casD and casE"],
explicitly flagging the overlap of casD and casE as a confound, and the reconstitution in
a cas-free host settled it
[PMID:18703739 "the small crRNA was absent only in the strain that lacked casE"],
[PMID:18703739 "showing that CasE is an unusual endoribonuclease that does not require the other Cascade subunits"].
CasD therefore is not required for pre-crRNA cleavage; it binds and stabilises the
already-cleaved 5' handle. UniProt records the consequence as "Decreased levels of
crRNA" rather than failure of cleavage. Hence `KEEP_AS_NON_CORE`: the term is within
family convention and not wrong, but CasD's core job is interference, not array
maintenance.

By the same logic I do **not** propose GO:0043571 as a new annotation for CasD, and I do
propose it for CasE, which does the cleaving.

### Redundant IEA rows

`GO:0003723 RNA binding` IEA (IPR010147, CRISPR-associated protein CasD) and
`GO:0051607 defense response to virus` IEA (same signature) are both duplicated by
experimental rows on the same protein. They are correct and consistent with the direct
evidence, so I ACCEPT them rather than calling them redundant; an IEA that agrees with
an IDA is corroboration, not noise.

### Complex term

Same as the other four subunits: Cascade is demonstrably a ribonucleoprotein
[PMID:25103409 "both assemblies consist of 11 protein subunits and a single 61-nt crRNA that traverses the length of the complex"],
[PMID:23079036 "The E. coli Cascade complex is a 405 KDa ribonucleoprotein complex assembled from crRNA and five functionally essential Cse proteins"],
so GO:0032991 is MODIFYed to GO:1990904 ribonucleoprotein complex and the missing
CRISPR-specific CC term is proposed. A QuickGO ontology search for "CRISPR" returns five
terms, all biological_process; there is no CC term, though ComplexPortal models the
complex as CPX-1005.
