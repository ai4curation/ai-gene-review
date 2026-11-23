# AcrIIA5 (Streptococcus phage D4276, UniProt A0A220GHA5) — curation notes

## Provenance of this review

Deep-research providers were **unavailable** in this container (no API keys), so no
`-deep-research-<provider>.md` file was generated. The literature below was assembled
directly from the cached publications in `publications/`, PubMed MCP searches
(`AcrIIA5`, 15 hits total), and from two additional papers that I cached during this
review with `just fetch-pmid` (PMID:31722192, PMID:31775029).

The GONUTS/CACAO wiki pages that would record the students' own evidence statements
(`https://gowiki.tamu.edu/wiki/index.php/PMID:28785032` and `.../PMID:30046034`) were
**offline** at the time of review ("This site is temporarily offline while we perform
upgrades"), so the CACAO rows below were assessed against the cited papers directly.

## Gene symbol choice

UniProt gives this entry no gene name (`GN ORFNames=D4276_028`), so `just fetch-gene`
fell back to the accession for `gene_symbol`. I set `gene_symbol: acrIIA5`, following
the repository's own anti-CRISPR precedents `genes/LISMN/acrIIA4` (`gene_symbol:
acrIIA4`) and `genes/NEIME/acrIIC1` (`gene_symbol: acrIIC1`), and matching the folder
name. `acrIIA5` is the name used throughout the primary literature and is the name
UniProt itself carries in `DE SubName: Full=AcrIIA5`; the Acr nomenclature (type,
subtype, serial number) is the community-standard naming system for anti-CRISPRs, so
it is the closest thing to an authoritative symbol for a phage ORF of this kind.

## What the protein is

- 140 aa, basic, monomeric: [PMID:32544231 "AcrIIA5 (a.a. 1–140) is a basic protein with
  a theoretical isoelectric point of 9.4, and elutes as a monomer in solution by size
  exclusion chromatography"].
- Novel fold with an N-terminal intrinsically disordered region (IDR):
  [PMID:32544231 "AcrIIA5 comprises seven β-strands and two α-helices, preceded by an
  extended N-terminal disordered region"] and [PMID:32544231 "A search for structural
  homologs of AcrIIA5 using the DALI program did not return a similar fold, indicating
  that AcrIIA5 adopts a novel fold"]. NMR structure PDB 6LKF; UniProt `FT REGION 1..23
  /note="Disordered"` (MobiDB-lite) agrees with the experimental IDR assignment.
- Encoded by a **virulent** (strictly lytic) phage, not a prophage — this matters for the
  cellular-component call below: [PMID:28785032 "we have identified an unrelated Acr in a
  virulent phage of Streptococcus thermophilus"].

## Discovery and in vivo anti-CRISPR activity (CACAO-cited papers)

**PMID:28785032 (Hynes et al. 2017, Nat Microbiol) — the discovery paper, cached
ABSTRACT ONLY (`full_text_available: false`).** Phage D4276 escaped CRISPR immunity far
more often than its relatives: [PMID:28785032 "we found one that evaded the
CRISPR-encoded immunity >40,000× more often than the others"]. Systematic cloning
located the responsible gene: [PMID:28785032 "Through systematic cloning of its genes,
we identified an Acr solely responsible for the abolished immunity."] The protein also
blocks the heterologous SpCas9 system: [PMID:28785032 "We extended our findings by
demonstrating activity in another S. thermophilus strain, against unrelated phages, and
in another bacterial genus immunized using the heterologous SpCas9 system favoured for
genome editing."] and [PMID:28785032 "This Acr completely abolishes SpCas9-mediated
immunity in our assays."]. The assay throughout is phage plaquing on CRISPR-immunized
hosts, which is exactly what the CACAO rows' ECO code says (ECO:0007040 = plaque assay
evidence used in manual assertion).

**PMID:30046034 (Hynes et al. 2018, Nat Commun) — full text available.** Principally the
AcrIIA6 discovery paper, but **AcrIIA5_D4276 (the 140-aa protein of this entry) is itself
assayed side by side** in Table 1 and Figs. 4–5, so this is not a "paper about another
gene": [PMID:30046034 "All AcrIIA6 and AcrIIA5 orthologs completely restored the plaquing
efficiency of phages targeted by the CR1 system of S. thermophilus (Fig. 4), indicating
they are blocking the activity of St1Cas9."], [PMID:30046034 "Both AcrIIA5s almost
completely abolished SpCas9 activity in this bacterial system"], [PMID:30046034 "Of all
the Acrs tested in human cells and in the bacterial assays, AcrIIA5 displayed the broadest
range of activity"], and [PMID:30046034 "we demonstrate that both Acr families from
S. thermophilus phages inhibit Cas9-mediated genome editing of human cells"]. Note the one
quantitative limit specific to *this* orthologue: [PMID:30046034 "Notably, AcrIIA5D4276
comes from a phage infecting a S. thermophilus host which lacks the CR3 locus, and its
activity is limited to a 10-fold inhibition of CR3 activity25."] — i.e. D4276 AcrIIA5 is
potent against St1Cas9 and SpCas9 but only weakly active against St3Cas9, whereas the
D1126 orthologue fully inhibits St3Cas9.

## Breadth of Cas9 targets

[PMID:31722192 "We discovered that the previously identifed anti-CRISPR, AcrIIA5 from
Streptococcus thermophilus phage D4276 (Hynes et al., 2017), has the broadest Cas9
inhibitory activity described to date, inhibiting all of the Cas9 proteins commonly used
in genome-editing applications."] and [PMID:31722192 "here we identify one anti-CRISPR,
called AcrIIA5, that potently inhibits nine diverse type II-A and type II-C Cas9 homologs,
including those currently used for genome editing"]. Garcia et al. characterised the
**D4276 protein itself**, so this is direct evidence for this accession. Independently,
[PMID:31775029 "We found that AcrIIA5 is a potent and broad-spectrum inhibitor of
CRISPR-Cas9, which can inhibit diverse Cas9 orthologs of type II-A, type II-B, and type
II-C."] (abstract only in cache).

## Molecular mechanism

Inhibition is of **nuclease activity**, not of target-DNA engagement:
[PMID:31775029 "AcrIIA5 inhibits Cas9 by preventing DNA target cleavage, but DNA target
binding of Cas9 is unaffected."] and [PMID:31775029 "it can affect the activity of the
RuvC nuclease domain of Cas9 independent of the HNH nuclease domain"].

In vitro with purified protein: [PMID:32544231 "Purified AcrIIA5 completely inhibited
target double-stranded DNA (dsDNA) cleavage of Cas9–sgRNA in the in vitro nuclease
activity assay, demonstrating that AcrIIA5 alone is sufficient for Cas9 inhibition"]
(Fig. 3A). Specificity: [PMID:32544231 "AcrIIA5 did not inhibit L. bacterium Cas12a,
another RNA-guided endonuclease from the type V-A CRISPR–Cas system"].

The binding target is the **guide-loaded Cas9 ribonucleoprotein**, not free RNA and not
apo-Cas9: [PMID:32544231 "Titration of AcrIIA5 into Cas9–sgRNA resulted in sgRNA
super-shifts owing to the ternary complex formation, demonstrating a direct interaction
between AcrIIA5 and Cas9–sgRNA"] (Fig. 4A, EMSA; corroborated by NMR line-broadening,
Fig. 4E), and [PMID:32544231 "We note that AcrIIA5 interacted only with the preformed
Cas9–sgRNA complex, and not with apo-Cas9."]. Summary statement:
[PMID:32544231 "AcrIIA5 selectively binds to sgRNA-loaded Cas9 and inhibits the nuclease
activity without competing with target DNA binding, which is unique among Cas9
inhibitors."].

Determinants: [PMID:32544231 "Remarkably, AcrIIA5Δ20 completely lost its ability to
inhibit Cas9, revealing that the N-terminal disordered region is essential for Acr
activity"]; [PMID:32544231 "the length of the IDR provides a scaffold for association
between AcrIIA5 and Cas9–sgRNA, while the positive charges of the IDR serve as a
regulatory switch that hinders Cas9 function upon binding"]; and
[PMID:32544231 "the key residues of AcrIIA5 required for Cas9 inhibition are located at
the mobile loop region in the middle of the compact fold, in addition to the N-terminal
IDR"] (the β3–β4 loop, where the in vivo loss-of-function residues Asp50/Arg62/Asp74/
Lys88/His66/Asn70/His73 of Garcia et al. map).

## A contested finding worth flagging

Garcia et al. reported sgRNA cleavage in vivo and inferred an RNA-directed mechanism:
[PMID:31722192 "We show that the activity of AcrIIA5 results in partial in vivo cleavage
of a single-guide RNA (sgRNA), suggesting that its mechanism involves RNA interaction."],
reinforced by [PMID:31722192 "Purified Nme1Cas9 that was co-expressed with the inactive
mutants was not associated with cleaved sgRNA, supporting the connection between AcrIIA5
inhibition of Cas9 and sgRNA cleavage"]. An et al. then tested AcrIIA5 for intrinsic
ribonuclease activity and found none: [PMID:32544231 "Treatment of free sgRNA or the
Cas9–sgRNA complex with AcrIIA5 did not digest sgRNA, and the AcrIIA5-treated sgRNA bands
remained intact in the urea gel"], concluding [PMID:32544231 "the sgRNA cleavage observed
in previously reported co-expression systems can be attributed to endogenous
ribonucleases"]. So the *observation* of sgRNA cleavage stands, but the inference that
AcrIIA5 itself cleaves (or must engage) RNA is overturned for the catalytic reading and
disputed for the "mechanism involves RNA interaction" reading. Garcia et al. also note
the practical reason the mechanism was hard to pin down:
[PMID:31722192 "Despite extensive efforts, AcrIIA5 could not be purified in a soluble and
active form on its own."], whereas An et al. succeeded by using an MBP tag and 500 mM NaCl.

## Consequences for the annotation review

1. **GO:0098672 symbiont-mediated suppression of host CRISPR-cas system** (3 CACAO rows,
   IDA) is correct and maximally specific; the evidence is direct and on this protein.
   The one defect is the **qualifier** on the 2025 row:
   `acts_upstream_of_or_within_positive_effect` understates a process the protein itself
   executes; `involved_in` (used by the other two rows) is right. Recorded as a
   `source_defects` entry (WRONG_QUALIFIER) rather than as a REMOVE.
2. **GO:0003723 RNA binding** (DisProt, IPI, WITH RNAcentral sgRNA) is the wrong
   granularity *and* the wrong entity: the assayed interaction is with the Cas9–sgRNA
   ribonucleoprotein, and the paper that the IPI cites is the one that showed AcrIIA5 has
   no RNase activity and binds only the preformed complex. MODIFY to **GO:0043021
   ribonucleoprotein complex binding** (the term the repo's acrIIA4 review uses for the
   same Acr–Cas9/sgRNA relationship).
3. **GO:0140678 molecular function inhibitor activity** (DisProt, IMP) is true but
   uninformative when the target enzyme class is known. MODIFY to **GO:0140721 nuclease
   inhibitor activity** (an `is_a` descendant via GO:0004857), as used for acrIIC1 in this
   repo. I stopped short of GO:0060703 deoxyribonuclease inhibitor activity: AcrIIA5's
   substrate-level target is the Cas9 RNP rather than a classical DNase, and its reported
   effect is on the RuvC domain of an RNA-guided enzyme, so the parent term is the
   defensible stopping point.
4. **GO:0030430 host cell cytoplasm** added as NEW/IC. This entry's taxon is the phage
   (NCBITaxon:2006928), and the phage is virulent rather than a resident prophage, so —
   unlike the `genes/LISMN/acrIIA4` case, which is filed under the *Listeria* taxon and
   therefore uses GO:0005737 — the compartment AcrIIA5 occupies belongs to a separate host
   cell. No localisation experiment exists; the location is a curator inference from the
   target (cytoplasmic Cas9 RNP) plus in-cell inhibition, hence IC.

## Open questions

- Which surface of Cas9 does the IDR contact, and does it occlude RuvC directly or act
  allosterically? An et al. explicitly leave this open; no AcrIIA5–Cas9 co-structure exists.
- Why do the His66/Asn70/His73 mutants behave differently in vivo (active against SpCas9,
  per Garcia et al.) and in vitro (inactive, per An et al.)?
- Whether the in vivo sgRNA cleavage is a consequence of destabilised Cas9–sgRNA assembly
  exposing the guide to host RNases, as An et al. propose, has not been tested directly.
