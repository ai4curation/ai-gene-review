# NSs (Rift Valley fever virus, strain ZH-548 M12; UniProt P21698) — curation notes

> **Deep research was unavailable for this review.** No deep-research API keys are
> configured in this container, so `just deep-research` was not run and no
> `-deep-research-<provider>.md` file exists for this gene. The literature below was
> assembled by hand from the cached `publications/PMID_*.md` records, the UniProt flat
> file (`NSS-uniprot.txt`), PubMed Central (for figure-level detail where the cached
> record is abstract-only), and QuickGO/OLS for term definitions and comparator
> annotations. Where a cited paper's cached record is abstract-only, that is flagged.

## Summary of the gene product

NSs is the 265-aa nonstructural protein encoded in the genomic-sense ORF of the
ambisense S segment of RVFV, and is the virus's principal virulence factor. It is
dispensable for genome replication in interferon-incompetent cells but required for
infection of interferon-competent cells, where it dismantles two arms of the host
antiviral response by acting as a substrate-recognition adaptor that redirects host
SCF ubiquitin ligases onto host proteins:

- **Nuclear pool → TFIIH.** NSs binds the p62/GTF2H1 subunit of the general
  transcription factor TFIIH through a short ΩXaV motif at its C-terminus, recruits the
  F-box protein FBXO3 (with SKP1), and so drives proteasomal destruction of p62. It
  also competes with XPD for p44 and sequesters p44 and XPB into nuclear filaments.
  TFIIH depletion shuts down host RNA polymerase II transcription initiation globally,
  which is how NSs prevents induction of the IFN-β gene.
- **Cytoplasmic pool → PKR.** NSs binds EIF2AK2/PKR and recruits FBXW11, degrading PKR
  and so preventing eIF2α phosphorylation and preserving translation.
- **Downstream cytopathology.** By blocking host transcription NSs also prevents the
  antiviral upregulation of Abl2, perturbing the actin cytoskeleton, lamellipodia and
  adherens junctions.

## Localization

NSs is the only RVFV protein found in the nucleus, which is unexpected for a virus
that replicates entirely in the cytoplasm.

- A 34-kDa nonstructural protein was identified in nuclei of RVFV-infected Vero cells
  [PMID:7108491 "A non-structural protein of mol. wt. 34 X 10(3) was demonstrated in the
  nuclei of Rift Valley fever virus-infected Vero cells by SDS-polyacrylamide gel
  electro-phoresis."] (cached record is abstract-only).
- NSs expressed alone forms the same nuclear filaments seen in infected cells, and the
  acidic C-terminal domain is needed for filaments but not for nuclear import
  [PMID:10233964 "deletion of this acidic carboxy-terminal domain prevents the protein
  from forming filaments but does not affect its nuclear localization"] (full text
  cached). The same paper maps self-association to the last 10–17 C-terminal residues by
  two-hybrid analysis.
- UniProt records both compartments with experimental evidence:
  `Host nucleus {ECO:0000269|PubMed:10233964, ECO:0000269|PubMed:25918396,
  ECO:0000269|PubMed:7108491}. Host cytoplasm {ECO:0000269|PubMed:25918396}`
  [file:RVFVZ/NSS/NSS-uniprot.txt "SUBCELLULAR LOCATION: Host nucleus"].

## Mechanism 1 — TFIIH destruction and host transcription shutoff

- RVFV infection causes a rapid collapse of host RNA synthesis tracking the loss of
  TFIIH, and NSs binds p44, forming nuclear filaments that also contain XPB
  [PMID:14980221 "infection by RVFV leads to a rapid and drastic suppression of host
  cellular RNA synthesis that parallels a decrease of the TFIIH transcription factor
  cellular concentration"; "By competing with XPD, the natural partner of p44 within
  TFIIH, and sequestering p44 and XPB subunits, NSs prevents the assembly of TFIIH
  subunits"] (abstract-only in cache).
- The p62 subunit is destroyed via the ubiquitin/proteasome system, and NSs recruits the
  F-box protein FBXO3 to do it; FBXO3 or SKP1 knockdown rescues p62 and raises IFN
  transcription [PMID:24403578 "Small interfering RNA (siRNA)-mediated depletion of
  FBXO3 rescued p62 protein levels in RVFV-infected cells and elevated IFN transcription
  by 1 order of magnitude"; "NSs recruits FBXO3 to destroy the general host cell
  transcription factor TFIIH-p62, resulting in suppression of the transcriptional
  upregulation of innate immunity"] (abstract-only in cache). Cullin 1, cullin 7 and
  Rbx1 knockdowns did *not* rescue p62, so the ligase composition is unusual.
- A ΩXaV motif (residues 261–265) mediates p62 binding; mutating Phe261 abolishes both
  filament formation and p62 degradation and attenuates virulence [PMID:25918396 "the
  ΩXaV motif is required for both nuclear filament formation and degradation of p62"]
  (abstract-only in cache). The motif mimics host NER/transcription factors that dock on
  p62.
- UniProt's curated summary ties the two pools together: `Cytoplasmic NSs interacts with
  host FBXW11 to degrade PKR whereas` ... `nuclear pool binds to host FBXO3 to target
  TFIIH subunit GTF2H1 for proteasomal degradation with the help of the linker protein
  SKP1` [file:RVFVZ/NSS/NSS-uniprot.txt].

## Mechanism 2 — interferon antagonism is at the level of IFN induction

This distinction matters for the GO review. NSs does **not** interfere with signalling
downstream of the type I IFN receptor; it prevents the IFN-β gene from being transcribed
in the first place.

- NSs alone blocks IFN-β at the transcriptional level, while leaving IRF-3, NF-κB and
  AP-1 activation intact [PMID:15331713 "we demonstrate that NSs is sufficient to block
  IFN-beta gene expression at the transcriptional level"; "In the presence of NSs, IRF-3
  was still activated and moved to the nucleus. Likewise, NF-kappaB and AP-1 were
  activated normally, as shown in electrophoretic mobility shift assays"]. The paper's
  own conclusion is that the block is general, not IFN-specific: [PMID:15331713 "NSs was
  found to inhibit transcriptional activity of a constitutive promoter, in agreement with
  recent findings showing that NSs targets the basal cellular transcription factor
  TFIIH"] and [PMID:15331713 "NSs, unlike other viral IFN antagonists, does not inhibit
  IFN-specific transcription factors but blocks IFN gene expression at a subsequent
  step"].
- Figure-level detail (from PMC514997, outside the cached abstract, consulted for
  judgment only): IFN-β promoter–luciferase reporters in 293 cells (Fig. 1D, Fig. 3A/C,
  dose titration to >95% inhibition), RT-PCR and Northern blots for IFN-β mRNA after
  ZH548 vs clone 13 infection (Fig. 1A/B), cytoplasmic NSs mutants losing inhibition
  (Fig. 5A), suppression of a CMV-driven β-galactosidase reporter and of the SV40 early
  promoter (Figs. 3B, 5B, 7D), and EMSAs showing normal NF-κB/AP-1 activation (Fig.
  6D/E). So the assays are reporter/transcript assays of IFN **production** and of
  constitutive promoters — none of them an IFN-receptor signalling assay.
- Reverse genetics confirms the same at the level of the virus: NSs-deletion mutants of
  MP-12 induce IFN-β mRNA and lose host shutoff [PMID:16501102 "accumulation of beta
  interferon mRNA occurred after infection by these NSs deletion mutants, but not after
  infection by MP-12"; "failed to shut off host protein synthesis in Vero cells"].

**Consequence for GO.** `GO:0039502` is defined as interference with "a type I
interferon-mediated signaling in the host organism", and its parent `GO:0140886` as
reducing "interferon-mediated signaling in the host organism" — i.e. the branch for
antagonists of the IFN receptor → JAK/STAT → ISG axis. What NSs is shown to do is
suppress type I IFN *production*. GO currently has no symbiont-mediated counterpart of
`GO:0032480 negative regulation of type I interferon production` (checked by QuickGO
search: the only symbiont-mediated interferon terms are GO:0039502, GO:0140884,
GO:0140885 and GO:0140886, all signalling-pathway terms), so the production-blocking
viruses are all parked on the signalling term. Comparator check confirms this is a
consortium-wide convention rather than a student error: influenza A NS1 (P03496), the
textbook IFN-induction antagonist, carries GO:0039502 only by the same
`UniProtKB-KW:KW-1114` IEA mapping, and Ebola VP35 (Q05127) carries GO:0039502 by a
CACAO IMP. Hence this review records a `proposed_new_terms` entry and treats the four
RVFV rows on this axis as MODIFY-to-NTR rather than as errors of the annotators.

## Mechanism 3 — PKR degradation

- NSs induces specific degradation of PKR [PMID:19211744 title: "NSs protein of rift
  valley fever virus induces the specific degradation of the double-stranded RNA-dependent
  protein kinase"] and thereby blocks eIF2α phosphorylation [PMID:19197350 "Rift Valley
  fever virus NSs protein promotes post-transcriptional downregulation of protein kinase
  PKR and inhibits eIF2alpha phosphorylation"] (titles taken from the UniProt reference
  block; these papers are not separately cached).
- The responsible ligase is SCF^FBXW11 [PMID:26837067 title "Protein Kinase R degradation
  is essential for Rift valley fever Virus infection and is regulated by SKP1-CUL1-F-box
  (SCF)FBXW11-NSs E3 ligase"], and transcription inhibition is separable from PKR
  degradation [PMID:23063407 title "Rift Valley fever virus NSs inhibits host
  transcription independently of the degradation of dsRNA-dependent protein kinase PKR"].
- Note on the molecular function: the mechanism is **degradation**, not occupancy-based
  inhibition of the kinase active site. The UniProt keyword `KW-1102 Inhibition of host
  PKR by virus` maps to `GO:0030291 protein serine/threonine kinase inhibitor activity`
  ("Binds to and stops, prevents or reduces the activity of a protein serine/threonine
  kinase"), which mis-describes the activity. `GO:1990756 ubiquitin-like ligase-substrate
  adaptor activity` ("The binding activity of a molecule that brings together a
  ubiquitin-like ligase ... and its substrate. Usually mediated by F-box BTB/POZ domain
  proteins") is the activity NSs actually has, for both PKR/FBXW11 and p62/FBXO3, and it
  is a descendant of the `GO:0030674` term UniProt already annotates by IDA (QuickGO
  ancestors of GO:1990756: GO:0140767, GO:0030674, GO:0060090, GO:0003674).

## Mechanism 4 — nuclear filaments

- NSs self-associates and builds filaments without any other viral protein
  [PMID:10233964 "we expressed NSs in mammalian cells via a recombinant Semliki Forest
  virus and demonstrated that the protein alone was able to form structures similar to
  those observed in RVF virus-infected cells, indicating that the presence of other RVF
  virus proteins is not required for filament formation"].
- UniProt adds that the filaments are amyloid-like and may sequester NSs partners,
  causing cell cycle arrest (PubMed:28915104, PubMed:32612175), and reports the crystal
  structure of the core domain (PDB 5OOO) and the NMR structure of the ΩXaV peptide bound
  to p62 (PDB 2N0Y).

## Mechanism 5 — cytoskeleton and junctions (SigSci rows)

- NSs prevents the antiviral upregulation of Abl2 and reshapes the actin cytoskeleton
  [PMID:33087469 "NSs expression prevented the upregulation of Abl2 (a major regulator of
  the actin cytoskeleton) expression otherwise induced by avirulent infections and
  identified here as part of the antiviral response"], with "reduction of lamellipodia,
  cell spreading, and dissolution of adherens junctions" in hepatocytes (full text
  cached). These effects are real but are downstream readouts of the transcriptional
  block, so they are kept as non-core.

## The CACAO rows

Six GOA rows carry `ASSIGNED BY = CACAO`, all dated 2014-04-02/05, from three papers.
The GONUTS wiki could not be consulted: `https://gowiki.tamu.edu/wiki/index.php/PMID:15331713`
and `.../PMID:16501102` both return "This site is temporarily offline while we perform
upgrades", and the Internet Archive has no snapshot of either page
(`archived_snapshots: {}`). All three cited papers are abstract-only in the cache, so
PMC was used for figure-level reading of PMID:15331713 and the curator-deference rule was
applied throughout.

| Term | Evid | PMID | Verdict |
|---|---|---|---|
| GO:0039602 suppression of host transcription initiation from Pol II promoter | IDA | 14980221 | Matches. The paper's mechanism *is* TFIIH disassembly, and TFIIH is a Pol II general transcription factor required for preinitiation-complex function. Right term, right granularity. |
| GO:0039653 suppression of host transcription | IMP | 15331713 | Matches. The paper shows inhibition of a constitutive promoter in addition to IFN-β, i.e. general transcription. |
| GO:0039657 suppression of host gene expression | IMP | 16501102 | Matches. ΔNSs viruses "failed to shut off host protein synthesis", so NSs is responsible for host shutoff; the gene-expression term is the right non-committal level for a protein-synthesis readout. |
| GO:0039502 suppression of host type I IFN-mediated signalling | IMP | 15331713 | Wrong branch, not wrong biology: the assays score IFN-β **production** (promoter reporters, IFN-β transcripts), not IFN-receptor signalling. Shared with the UniProt IEA and with influenza NS1/Ebola VP35, so it is a convention, not a student slip. |
| GO:0039502 suppression of host type I IFN-mediated signalling | IMP | 16501102 | Same wrong branch; the datum is IFN-β **mRNA accumulation** in ΔNSs infections. |
| GO:0039689 negative stranded viral RNA replication | IMP | 16501102 | **Not supported, and contradicted by the cited abstract.** The paper's point is that NSs is dispensable: "Mutants of MP-12 partially or completely lacking the NSs open reading frame were viable. These NSs deletion mutants replicated efficiently in Vero and 293 cells", and NSs expression from a plasmid actually "abolished virus rescue". Genome replication is performed by the L polymerase and N; NSs contributes none of the work of RNA synthesis. |

The GO:0039689 row looks like a new failure shape for the CACAO taxonomy, distinct from
"phenotype read as process": a **viral fitness/growth requirement read as participation
in genome replication**. Here even the fitness premise fails in the cited cell lines —
the attenuation is IFN-dependent, and the paper reports it only in MRC-5 cells. It is
the same category error the repository's `NEW`-action guidance warns about (necessity
for an outcome mistaken for performing a step of it), applied to a term for an activity
that NSs demonstrably does not carry out.

## References consulted but not cached separately

PMID:19197350, PMID:19211744, PMID:19751406, PMID:21543505, PMID:23063407,
PMID:26837067, PMID:28915104, PMID:32612175, PMID:39366381 — all appear in the UniProt
reference block with `ECO:0000269` evidence attached to the curated FUNCTION, SUBUNIT and
DOMAIN statements, and are used here only through those curated UniProt statements (cited
as `file:RVFVZ/NSS/NSS-uniprot.txt`) rather than as independent quotations.
