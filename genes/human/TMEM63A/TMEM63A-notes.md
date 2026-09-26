# TMEM63A review notes

## Why this gene was selected

Reviewed as the paralog partner of TMEM63B in a contested-function pair: mechanically
activated cation channel vs mechanically activated lipid scramblase. The two paralogs were
reviewed together so the reasoning is consistent, but they were **not** assumed to behave
identically — and they do not.

## Position taken

**For TMEM63A, only the mechanosensitive cation channel activity is core.** The scramblase
claim, which is core for TMEM63B, is *not* established for TMEM63A in cells; GOA carries the
opposite assertion (`NOT|enables GO:0017128`, IDA, PMID:39716028) and the 2026 reconstitution
work that does report TMEM63A lipid translocation explicitly agrees that it does not happen
in the cellular context at rest.

## Channel function (core, uncontested)

Family-level founding demonstration: [PMID:30382938 "Here, we show that various members of the
OSCA and TMEM63 family of proteins from plants, flies, and mammals confer mechanosensitivity to
naïve cells."].

Human genetics: [PMID:31587869 "Here we report heterozygous missense mutations in the gene
encoding the MA ion channel TMEM63A that result in an infantile disorder resembling a
hypomyelinating leukodystrophy."].

Structure and biophysics, monomeric with a single restricted pore:
[PMID:37543036 "Functional analyses demonstrated that TMEM63s are bona fide mechanosensitive
ion channels, characterized by small conductance and high thresholds."] and
[PMID:37543036 "Here, we uncover an unanticipated monomeric configuration of TMEM63 proteins."].

In vivo lung physiology, alongside TMEM63B:
[PMID:38127458 "we show that loss of the mechanosensitive channels TMEM63A and TMEM63B
(TMEM63A/B) resulted in atelectasis and respiratory failure in mice due to a deficit of
surfactant secretion"] with the localisation
[PMID:38127458 "TMEM63A/B were predominantly localized at the limiting membrane of the lamellar
body (LB), a lysosome-related organelle that stores pulmonary surfactant and ATP in AT2
cells."].

The 2026 Neuron paper is a purely channel-framed account in the cell type where TMEM63A matters
most: [PMID:41483808 "we identified TMEM63A as a key mechanosensitive channel in
oligodendrocytes. TMEM63A enabled oligodendrocytes to sense membrane stretch and translate it
into Ca2+ signals."] with the loss-of-function phenotype
[PMID:41483808 "In the absence of TMEM63A, developmental myelination was severely impaired with
shorter and thinner myelin sheaths on large-diameter axons, ectopic myelination of very
small-diameter axons, and increased sheath retractions."]. (Abstract-only in the cache;
`full_text_available: false`.)

## The scramblase question for TMEM63A — the `NOT` annotation is sound

GOA carries `NOT|enables GO:0017128 phospholipid scramblase activity`, IDA, PMID:39716028.
That paper deliberately compared paralogs in a scramblase-null background:
[PMID:39716028 "We expressed human TMEM63 paralogs, TMEM63B orthologs, and plant OSCA1.1 in
Tmem63b-deficient mouse pro-B cells and found that vertebrate TMEM63B orthologs exhibit
scramblase activity at the PM."] — i.e. the activity tracked with TMEM63B orthology, not with
family membership.

The 2026 Nat Commun paper appears at first to contradict this, since it reports lipid
translocation by purified hTMEM63A: [PMID:41617699 "Interestingly, GUVs containing hTMEM63A or
hTMEM63B also showed a reduction in fluorescence ratio significantly below the negative
controls."]. But the **same paper states the cellular result agrees with the NOT annotation**:
[PMID:41617699 "Results from our experimental scrambling assays show that WT TMEM63A
translocates lipids in GUVs but this is not the case in the cellular context."]. Only when
force is actively applied does cellular PS exposure appear:
[PMID:41617699 "We saw a profound increase in PS exposure indicated by annexinV-FITC labeled
cells in the mTMEM63A expressing group that was not present in untransfected Piezo1"].

So the two results are reconcilable, and the reconciliation is about **gating state, not
identity**: TMEM63A retains the structural capacity to scramble, but under resting cellular
conditions it does not. The `NOT` annotation is therefore accepted as written, with the
condition-dependence recorded in the review `reason` and the open question moved to
`suggested_questions`. This is *not* treated as a straight contradiction of the IDA.

Mechanistically, the V→M latch variants make the same point from the other direction: the
TMEM63A V53M disease substitution *creates* constitutive scrambling
[PMID:40480214 "We first found that TMEM63B p.V44M and the homologous TMEM63A p.V53M are
gain-of-function mutations that do not enhance channel activity but instead evoke constitutive
lipid scramblase activity."] — which only makes sense if WT TMEM63A does not normally scramble.

The authors of that structural work leave the WT question open:
[PMID:40480214 "A further question is whether the scramblase activity of endogenous WT TMEM63
channels is associated with physiological functions."].

## Term-choice problems found in the existing annotation set

### `GO:0003676` nucleic acid binding (IEA, InterPro IPR035979) — remove

This is a **fold-only** inference. The InterPro matches for O94886 include
`SSF54928 RNA-binding domain, RBD` → `IPR035979 RNA-binding domain superfamily` and
`IPR012677 Nucleotide-binding alpha-beta plait domain superfamily`, both of which are
structural-superfamily hits on the CSC1/OSCA1-like **cytosolic domain** (`IPR027815`), which
adopts an RRM-like alpha-beta plait fold. There is no report of nucleic acid binding by any
OSCA/TMEM63 protein, and TMEM63A is an 11-TM integral membrane channel of the lysosomal and
plasma membranes. Notably the paralog TMEM63B does **not** carry this annotation, so the
pipeline is not even internally consistent. This is precisely the class of demonstrably wrong
electronic inference that `REMOVE` exists for.

### `GO:0005227` calcium-activated cation channel activity — wrong gating stimulus

Identical issue to TMEM63B; see `TMEM63B-notes.md` for the full argument. In brief, the GO
definition requires the channel to open **when a calcium cation has been bound**, whereas
TMEM63A opens in response to membrane stretch and is Ca2+-**permeable**. The InterPro family
behind the IEA is literally named "Calcium **permeable** stress-gated cation channel 1-like"
(IPR045122) and is mapped to the calcium-**activated** term. `MODIFY` → `GO:0140135` +
`GO:0005262` on both the IBA and the IEA.

### `GO:0008381` mechanosensitive monoatomic ion channel activity — correct but under-specific

TMEM63A conducts cations (Ca2+, and the family conducts Na+/K+/Cs+); `GO:0140135`
mechanosensitive monoatomic **cation** channel activity is available and is what TMEM63B
already carries from an IDA. `MODIFY` all four rows (IEA, IDA x2, IMP) to GO:0140135.

## Localisation

Native TMEM63A is principally lysosomal/endolysosomal, with plasma-membrane presence in some
cell types (and in heterologous over-expression, which is how the currents are recorded).
This is stated in the 2026 reconstitution paper's own framing and matches the GOA set
(lysosomal membrane: IDA PMID:39716028, IDA PMID:38127458, IDA PMID:20957757, HDA
PMID:17897319). The lysosome-organization annotation transfers by ISS from *Drosophila*
Tmem63 (UniProtKB:Q6NP91), the single fly ortholog — kept as non-core.

HPA `GO:0034451 centriolar satellite` (IDA, GO_REF:0000052) is a single-antibody
immunofluorescence call that is incompatible with the established multi-pass
endolysosomal/plasma-membrane topology and is not corroborated by any focused study; marked as
over-annotated rather than removed, since it is an experimental-code annotation.

`GO:0070062 extracellular exosome` comes from urinary-exosome shotgun proteomics
(PMID:19056867) — a high-throughput co-purification term with no functional content here.
