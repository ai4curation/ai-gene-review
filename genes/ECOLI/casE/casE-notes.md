# casE (Cas6e / Cse3), *Escherichia coli* K-12 — UniProt Q46897

Curation journal. All assertions carry inline provenance as
`[PMID:xxxxxxx "verbatim supporting text"]`, copied verbatim from the cached records in
`publications/`.

## Session 1 (2026-10-01): initial full review

Reviewed together with casA, casB, casC and casD as one complex. CasE is the only one of
the five with a demonstrated catalytic activity, and it is dual-role: it is both the
pre-crRNA processing enzyme and a structural subunit of the complex it builds. Both have
to survive the review, and the catalysis must not be buried under the complex membership.

### The catalysis is subunit-intrinsic

Of the five subunits, only casE is required for pre-crRNA cleavage. Brouns deleted the
genes individually in the native strain and then, to rule out polar effects on the
overlapping casD/casE genes, rebuilt Cascade subunit by subunit in a host with no cas
genes
[PMID:18703739 "the small crRNA was absent only in the strain that lacked casE"].
Purified CasE alone, as a MalE fusion, cleaved the cognate pre-crRNA
[PMID:18703739 "showing that CasE is an unusual endoribonuclease that does not require the other Cascade subunits"],
and the chemistry needs no cofactor
[PMID:18703739 "The RNA cleavage reaction proceeded in the absence of divalent metal ions and adenosine triphosphate"],
consistent with the family as a whole
[PMID:25103409 "all Cas6 proteins are metal-independent endoribonucleases that selectively bind and cleave long CRISPR RNA transcripts"].
The active-site assignment rests on a conserved histidine, and the mutant separates
catalysis from assembly cleanly
[PMID:18703739 "although the mutated CasE was still incorporated into Cascade, the pre-crRNA cleaving ability of purified Cascade was abolished"].
That same H20A allele also shows the processing step is mechanistically required for
immunity, not just correlated with it
[PMID:18703739 "strains containing Cas3 and Cascade-CasEH20A displayed a sensitive phenotype, which shows that pre-crRNA cleavage is mechanistically required for phage resistance"].

So `GO:0004521 RNA endonuclease activity` (IDA, PMID:18703739) is ACCEPTed as a core
function, and `GO:0006396 RNA processing` (IMP) is ACCEPTed as the matching process. I
keep GO:0006396 at the parent level because GO has no crRNA-processing child; a QuickGO
ontology search for "crRNA" returns zero terms and for "CRISPR" returns only five, all
biological_process.

### Adding GO:0043571, with the comparator check done first

CasE is missing `GO:0043571 maintenance of CRISPR repeat elements`, whose definition
explicitly includes "transcription of the CRISPR repeat arrays into RNA and processing".
Before proposing it as `NEW` I ran the required checks:

- **Who performs the step?** CasE itself cleaves the array transcript, shown as a
  purified protein acting alone on its cognate substrate. This is not a necessity
  argument from a knockout; it is the enzyme in a tube with the RNA.
- **Comparator check.** QuickGO returns 14 non-IEA annotations to GO:0043571. Among them:
  `UniProtKB:Q02MM2 cas6f IMP PMID:26586803` — the type I-F orthologue of casE — and
  `UniProtKB:Q8U1S4 cas6 IDA PMID:19141480`, a standalone type III Cas6. Within this
  repository, `genes/PSEAB/cas6f/cas6f-ai-review.yaml` ACCEPTs GO:0043571 on both its IEA
  and IMP rows. So Cas6-family processing enzymes do carry this term, and casE's absence
  is an uncurated gap in a populated term, not a convention excluding it.
- **Not an ancestor or descendant of anything casE already carries.** GO:0043571 sits in
  a different part of the process branch from GO:0006396 and GO:0099048.
- **Mirror check against casD.** casD carries GO:0043571 as an IEA from
  InterPro:IPR021124. I mark that one `KEEP_AS_NON_CORE` precisely because casD does *not*
  do the cleaving (see above), which is the same test applied in the opposite direction.

### The structural role, which must not be lost either

Cleavage does not release the enzyme. CasE stays on its own product
[PMID:25103409 "After cleavage Cas6e remains tightly associated with the 3′ stem-loop of the mature crRNA"],
and is tethered into the complex by a helix from the first backbone subunit entering the
cleft on its non-RNA face
[PMID:25103409 "The V-shaped cleft, opposite the RNA binding face of Cas6e, provides a binding site for a short helix from Cas7.1 that tethers Cas6e to the helical backbone of Cascade"],
so the enzyme-product pair is read as the seed of assembly
[PMID:25103409 "this sub-complex may serve as a platform for the ordered assembly of the remaining 10 protein subunits that compose the backbone, tail, and belly of Cascade"].
Its RNA recognition is sequence-specific, unlike the backbone's
[PMID:25103409 "Unlike Cas6e and Cas5e, which make sequence-specific interactions with portions of the CRISPR repeat sequence, the Cas7 proteins polymerize along the crRNA via non-sequence specific interactions"].

Hence the intra-complex `GO:0005515` row is MODIFYed to GO:0005198 structural molecule
activity, the same replacement used for casA, casB, casC and casD. This is what keeps the
dual role visible: GO:0004521 for the chemistry, GO:0003723 for the sequence-specific
3' hairpin recognition, GO:0005198 for capping the head of the complex.

### The Cas1 (YgbT) row — here there *is* a better term

CasE's second `GO:0005515` row is an IPI with UniProtKB:Q46896 (Cas1/YgbT). Unlike the
equivalent casC row, this one has a demonstrated functional consequence in the same paper
[PMID:21219465 "purified recombinant YgcH (a Cascade subunit) inhibited the HJ cleavage activity of YgbT in a concentration-dependent manner"],
with the interaction itself validated in both directions
[PMID:21219465 "we reproducibly detected two subunits of the CRISPR-associated Cascade complex, YgcJ (CasC) and YgcH (CasE)"],
[PMID:21219465 "In each case, mass spectrometry analyses of the affinity-purified protein confirmed its association with YgbT"].
UniProt Q46897 records it as a function in its own right: "Partially inhibits the cleavage
of Holliday junctions by YgbT (Cas1)."

Cas1's activity here is on branched DNA, so the precise term is `GO:0060703
deoxyribonuclease inhibitor activity` ("Binds to and stops, prevents or reduces the
activity of deoxyribonuclease") rather than the parent GO:0140721. I MODIFY to it. This
is an in vitro inhibition whose physiological role is not established, and I say so in the
`reason` and raise it in `suggested_questions` rather than promoting it to a core
function. Note the asymmetry with casC, which is deliberate: for casC the same paper
offers no functional readout, so there is no evidence-backed replacement and that row is
REMOVEd instead.

### Complex term

Same as the other four subunits. Cascade is demonstrably a ribonucleoprotein
[PMID:25103409 "both assemblies consist of 11 protein subunits and a single 61-nt crRNA that traverses the length of the complex"],
[PMID:23079036 "The E. coli Cascade complex is a 405 KDa ribonucleoprotein complex assembled from crRNA and five functionally essential Cse proteins"],
so both GO:0032991 rows are MODIFYed to GO:1990904 ribonucleoprotein complex — including
the IPI row from the Babu paper, because that paper itself names the complex
("two subunits of the CRISPR-associated Cascade complex"). GO has no CC term for Cascade
or any CRISPR surveillance complex; ComplexPortal has CPX-1005. The missing term is
proposed in `proposed_new_terms`.

### Divergence from the type I-F reviews in this repository, recorded deliberately

`genes/PSEAB/csy1` and `genes/PSEAB/cas6f` MODIFY their `GO:0005515` rows to GO:0032991
(a cellular-component term offered as a replacement for a molecular function) and use
`in_complex: GO:0032991` in core functions. I have instead used GO:0005198 for the
molecular-function rows and GO:1990904 for the complex, which keeps the aspect correct
and is more specific. I have not altered those files, but the inconsistency between the
I-E and I-F sets is worth a curator's attention.
