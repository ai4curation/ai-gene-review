# acrIIC1 (A0A2D0TCG3, Neisseria meningitidis prophage) — curation notes

## Identity

Unreviewed TrEMBL entry, 86 aa, named only `SubName: Full=Anti-CRISPR protein (AcrIIC1)
{ECO:0000313|PDB:5VGB}` — the name comes from a PDB deposition, not from a curator.
`PE 1: Evidence at protein level`. Taxon NCBITaxon:487 (*Neisseria meningitidis*),
assigned to the bacterium rather than to a phage because the gene lies in a resident
prophage / mobile element of *N. meningitidis*.

**The accession is the assayed protein.** `PDB; 5VGB; X-ray; 1.50 A; B=1-86` is the
NmeCas9 HNH domain bound to AcrIIC1, and RCSB gives its primary citation as PMID:28844692
"A Broad-Spectrum Inhibitor of CRISPR-Cas9" with structure title "Crystal structure of
NmeCas9 HNH domain bound to anti-CRISPR AcrIIC1". Three further structures of this
sequence exist (7X31 NMR, 7X4B 1.61 Å, 8IF0 1.57 Å), 7X31/7X4B from PMID:36400778. CDD
`cd22213 AcrIIC1`. So experimental evidence codes are appropriate on this accession.

Like L7P7R7, this is an instance of the curation gap recorded in
`modules/anti_crispr_suppression.yaml`: four deposited structures, a mechanism established
in *Cell*, and a UniProt name that says only "Anti-CRISPR protein".

## Discovery

Pawluk et al. found the AcrIIC family by looking for Cas9 inhibitors in *Neisseria*
[PMID:27984730 "Here, we report the discovery of three distinct families of anti-CRISPRs that specifically inhibit the CRISPR-Cas9 system of Neisseria meningitidis."],
[PMID:27984730 "We show that these proteins bind directly to N. meningitidis Cas9 (NmeCas9) and can be used as potent inhibitors of genome editing by this system in human cells."].
This is the reference GOA (CACAO) cites for the IDA row.

## Mechanism: the module's HNH-blockade assignment holds exactly

The module (annoton `acriic1_hnh_blocker`) places AcrIIC1 in
`cas9_hnh_blockade_variant`, describing it as binding the HNH catalytic domain and
permitting target binding while preventing cleavage, with breadth across orthologues
because the HNH fold is conserved. **Every element of that is directly supported.**

Harrington et al. establish, in order:

1. Breadth
   [PMID:28844692 "AcrIIC1 is a broad-spectrum Cas9 inhibitor that prevents DNA cutting by multiple"]
   (title-level statement, truncated in cache).
2. DNA binding is *not* blocked — this is the diagnostic that separates AcrIIC1 from the
   DNA mimics
   [PMID:28844692 "The ability of AcrIIC1 to inhibit multiple Cas9 orthologs without preventing DNA binding suggested that it targets a conserved region of Cas9 involved in DNA cleavage."].
3. The target is the HNH domain, shown by domain-swap chimeras between an AcrIIC1-binding
   and a non-binding Cas9 ortholog
   [PMID:28844692 "These results indicated that the HNH domain is the primary site of interaction for AcrIIC1."].
4. The contact is at the HNH active site itself
   [PMID:28844692 "AcrIIC1 binds to the active site interface of the HNH domain through several ionic and hydrogen-bonding interactions."].
5. The functional outcome is a trapped, DNA-bound, catalytically dead complex
   [PMID:28844692 "These results suggested that AcrIIC1 traps Cas9 in its DNA-bound state, while inhibiting DNA cleavage."],
   [PMID:28844692 "how AcrIIC1 traps Cas9 in a DNA-bound but catalytically inactive state"].
6. The explanation of breadth
   [PMID:28844692 "The ability of AcrIIC1 to bind to the most conserved domain of Cas9 explains its ability to robustly inhibit related Cas9 orthologs"].

An additional layer not in the module: AcrIIC1 activity is redox-regulated through an
intersubunit disulphide (Cys17–Cys80, recorded in the UniProt FT DISULFID lines from
7X4B), with the dimer being the inactive form
[PMID:36400778 "we report the discovery of a redox switch for NmeAcrIIC1, which regulates NmeAcrIIC1's monomer-dimer interconversion and inhibitory activity on Cas9."],
[PMID:36400778 "a pair of conserved cysteines mediates the formation of inactive NmeAcrIIC1 dimer and directs the redox cycle"].
This is interesting but is **not** annotated: the physiological relevance of a redox
switch was demonstrated in the context of eukaryotic cellular environments for
gene-editing purposes, and whether the switch operates in the native *Neisseria*
cytoplasm is not established. It is recorded as a knowledge gap and a question instead.

## Molecular function: GO:0140721 is adequate and is asserted

The module deliberately asserts no GO id here, saying "No GO id asserted: the activity is
occlusion of a catalytic domain within a multidomain nuclease, leaving DNA binding intact,
and no GO molecular-function term captures that."

**I disagree in part.** `GO:0140721 nuclease inhibitor activity` is defined as "Binds to
and modulates the activity of a nuclease", and that is exactly and literally what AcrIIC1
does — it binds Cas9, a nuclease, at the active-site interface of one of its two nuclease
domains, and abolishes cleavage. The term is *less specific* than the mechanism (it does
not say that one domain of a multidomain nuclease is occluded while the other activities,
including DNA binding, survive), but it is not wrong, and GO curation practice is to
annotate the nearest correct existing term and request the specific one, rather than to
assert nothing. Asserting nothing leaves this protein with no molecular function at all,
which is strictly less informative.

So: `GO:0140721` is asserted as the core molecular function, and no new term is proposed
for it in this review. The gap — that GO cannot express single-domain occlusion within a
multidomain enzyme, and therefore cannot distinguish AcrIIC1 from an inhibitor that
disables the whole enzyme — is recorded as an ONTOLOGY knowledge gap with the specific
observation that the *diagnostic* feature (DNA binding survives) is the part GO loses.

I deliberately do **not** propose a term for it. Writing a term for "occlusion of one
catalytic domain within a multidomain nuclease" would be a term about protein architecture
rather than about activity, and GO molecular-function terms are about what the gene
product does; the better request is probably an extension on the existing term naming the
occluded domain, which is a curation-mechanism question rather than a new class. Recorded
as a question for ontology editors.

I also do **not** assert `GO:0043021 ribonucleoprotein complex binding` here, unlike the
other reviews in this round. AcrIIC1 binds the isolated HNH *domain* in solution — that is
how the chimera and size-exclusion experiments were done, and the crystal structure 5VGB
is of the free HNH domain, not of a Cas9-guide complex. So guide dependence, which is the
basis for the GO:0043021 assertions on AcrIIA4, AcrIIA2 and AcrF8, is not established for
AcrIIC1 and is in fact contraindicated.

## GOA row and qualifier adjudication

One row: `acts_upstream_of_or_within_positive_effect GO:0098672`, IDA, PMID:27984730,
assigned by CACAO. Same adjudication as for AcrIIA4: the term is correct and maximally
specific, the evidence is on this sequence, so ACCEPT. The qualifier is poorly chosen —
AcrIIC1 does not act upstream of the suppression, its binding to the Cas9 HNH domain *is*
the suppression, so `involved_in` is better supported; and the `positive_effect` component
reads as though the protein up-regulated something. Flagged in `review.reason` for CACAO
rather than rewritten, since a qualifier change is not a term change.
