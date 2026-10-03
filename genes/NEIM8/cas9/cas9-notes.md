# cas9 (Nme1Cas9), *Neisseria meningitidis* serogroup C strain 8013 — curation notes

UniProt: C9X1G5 (CAS9_NEIM8, reviewed, 1082 aa). Type II-C subtype.
Taxon: NCBITaxon:604162. Locus NMV_1993.

No deep-research provider was available in this environment (no API keys), so this
file is the research journal. Every assertion below carries an inline verbatim quote
from a cached publication.

## Scope decision

Like SpCas9, this protein is used as a genome-editing reagent (it is the compact
"Nme1Cas9" platform, and its close relative Nme2Cas9 differs only in the PI domain).
That is not a biological function of the gene, so `description` and `core_functions`
describe only what the enzyme does in *N. meningitidis*: the interference step of a
compact type II-C CRISPR-Cas system. The UniProt entry's own
`BIOTECHNOLOGY: Coexpression with both gRNAs or a synthetic gRNA in human embryonic
or pluripotent stem cells...` comment is deliberately not reflected in any annotation.

## 1. What makes this a type II-C enzyme, and why it must be kept separate from SpCas9

**Locus architecture.** The meningococcal locus is minimal — three *cas* genes, with
neither of the type II-A/II-B adaptation accessories:

- [PMID:23706818 "included a set of only three predicted protein-coding genes (cas9, cas1 and cas2) but neither csn2 nor cas4"]

**PAM.** Long and purine-rich, not SpCas9's NGG:

- [PMID:31668930 "This divergence leads to distinct PAM specificities: N4GAYW/N4GYTT/N4GTCT for Nme1Cas9"]

**Size.** 1082 aa versus SpCas9's 1368 aa; HNH domain at 512–667 with catalytic
His588 (SpCas9: 770–921, His840), RuvC catalytic Asp16 (SpCas9: Asp10).

**Anti-CRISPR target set.** Nme1Cas9 is the AcrIIC1/AcrIIC2/AcrIIC3 target; SpCas9 is
the AcrIIA2/AcrIIA4 target. These are unrelated protein families with different
mechanisms, so nothing transfers between the two reviews.

No experimental result has been carried across from Q99ZW2 in this review. Where only
the *S. pyogenes* orthologue has been assayed (notably the role in spacer acquisition,
PMID:25707807), the corresponding claim is simply not made for C9X1G5 — see §4.

## 2. Interference: Cas9 is the sole effector, and both nuclease motifs are required

- [PMID:23706818 "CRISPR function is abolished in both the transposon-induced (cas9::Tn) and deletion (Δcas9) mutations in cas9"]
- [PMID:23706818 "We engineered alanine mutants in corresponding catalytic residues (D16 in the RuvC domain and H588 in the HNH domain)"]
- [PMID:23706818 "these analyses demonstrate that the Neisseria Type II-C CRISPR/Cas system requires cas9 but not cas1 or cas2 for interference of natural transformation, and that the presence of intact RuvC-like and HNH motifs are essential for cas9 function"]

Structural evidence for the guide-loaded, DNA-engaged states, and for the Mg2+
cofactor in the HNH active site:

- [PMID:31668930 "we report structures of meningococcal Cas9 homologs in complex with sgRNA, dsDNA, or the AcrIIC3 anti-CRISPR protein"]
- [PMID:31668930 "The 8 nts of the TS base pair with seed nts 17-24 of the sgRNA guide region to form an RNA-DNA heteroduplex"]
- [PMID:31668930 "In our DNA-bound Nme1Cas9 complex, a Mg2+ ion is located in the catalytic pocket of the HNH domain, coordinating with the side-chains of the catalytic residues Asp587 and Asn611"]
- [PMID:31668930 "The HNH domains of Cas9 orthologs use a metal ion cofactor to catalyze TS cleavage between nts 3 and 4 of the protospacer"]

## 3. The dual-nuclease architecture, and why the HNH/RuvC split is not two GO functions

The best single datum on this question comes from this orthologue:

- [PMID:31668930 "The HNH active conformation activates the RuvC domain"]

The two nuclease centres are allosterically coupled: HNH reaching its catalytic
conformation is what licenses RuvC. Consistent with that, occluding HNH alone does not
yield a nickase but inactivates the enzyme outright, while leaving target binding
intact:

- [PMID:28844692 "AcrIIC1 is a broad-spectrum Cas9 inhibitor that prevents DNA cutting by multiple divergent Cas9 orthologs through direct binding to the conserved HNH catalytic domain of Cas9"]
- [PMID:28844692 "A crystal structure of an AcrIIC1-Cas9 HNH domain complex shows how AcrIIC1 traps Cas9 in a DNA-bound but catalytically inactive state"]
- [PMID:28844692 "AcrIIC1 blocks DNA cleavage by multiple Cas9 orthologs without impacting DNA binding, effectively transforming catalytically active Cas9 into catalytically inactive dCas9"]

So: **one** core function for cleavage (GO:0004520), with the HNH/RuvC division of
labour as prose. But AcrIIC1 also shows that **recognition and cleavage are separable**
— binding survives, catalysis does not — which is the empirical argument for giving
guide-directed recognition its own molecular function (§5) rather than folding it into
the nuclease term.

For the counterpart review (`genes/NEIME/acrIIC1`): the Acr's target is a *domain*, not
the protein, and GO has no way to say so. The suppression module
(`modules/anti_crispr_suppression.yaml`) records "occlusion of a single catalytic
domain within a multidomain nuclease" as an open ontology gap and asserts no id; this
review does not attempt to fill it from the Cas9 side.

## 4. crRNA biogenesis in this system is unusual — and GO:0043571 still fits

Two findings, both specific to this strain:

- Cas9 is required for guide accumulation but does not process the precursor:
  [PMID:23706818 "CrRNAs are also strongly depleted in cas9 mutants, but unlike in the rnc::Tn mutant, pre-crRNAs do not accumulate"]
  (the authors read this as Cas9 stabilising the guides rather than cleaving them).
- RNase III processing is dispensable for immunity here, because crRNAs can arise from
  promoters inside each CRISPR repeat:
  [PMID:23706818 "RNase III-catalyzed pre-crRNA processing occurs within the bacterial cell but is dispensable for interference"]

GO:0043571 *maintenance of CRISPR repeat elements* sits under GO:0043570 maintenance of
DNA repeat elements (a DNA-metabolism branch, **not** defence), and its definition
covers "capture of new spacer elements, expansion or contraction of clusters, ...
transcription of the CRISPR repeat arrays into RNA and processing". The guide-stability
limb of that definition is directly supported here, so the UniRule IEA is `ACCEPT`ed.

**What is deliberately not claimed for C9X1G5**: the spacer-acquisition role. In
*S. pyogenes* Cas9 is a member of the Cas1-Cas2-Csn2 acquisition complex and supplies
PAM selection (PMID:25707807) — but that strain has *csn2*, which this locus lacks
(§1), *cas1* and *cas2* are dispensable for interference here, and adaptation has not
been assayed in strain 8013 at all. So the GO:0043571 `ACCEPT` rests on the biogenesis
limb only, and the reason field says so. This is the chief place where the two reviews
differ and where transferring the *S. pyogenes* result would have been wrong.

## 5. Ontology gap: no MF term for guide-RNA-directed recognition

Same gap as for Q99ZW2, and the same proposed term is carried in both reviews so they
can be compared:

- **proposed_name**: `guide RNA-directed nucleic acid target recognition activity`
- **proposed_parent**: GO:0003676 nucleic acid binding

The assertion is that target specificity resides in a separate, non-covalently bound
guide RNA, so changing the guide changes the target with no change to the polypeptide.
PAM dependence is excluded from the definition on purpose — it is protein-encoded and
differs between orthologues, as this gene demonstrates (N4GAYW-class here, NGG in
SpCas9, N4CC in Nme2Cas9). The downstream chemistry is excluded too; it is already
covered by GO:0004520 / GO:0004521 / GO:0004530, which is exactly why a term is needed
for the part that is not.

## 6. Annotation calls (5 GOA rows, all IEA — this entry has no experimental GOA rows)

- **GO:0003676 nucleic acid binding** (IEA, InterPro IPR036397 = RNase H-like
  superfamily) → `MODIFY` to GO:0003723 RNA binding. Root-level and uninformative; the
  substantive, structurally demonstrated content absent from GOA is sgRNA
  (crRNA:tracrRNA) binding. The DNA half is added as a separate `NEW` row rather than
  crowded into this one.
- **GO:0004519 endonuclease activity** (IEA) → `MODIFY` to GO:0004520 DNA endonuclease
  activity. Cas9's substrate is DNA, demonstrated genetically (RuvC/HNH catalytic
  mutants fail to complement) and structurally (cleaved-target-DNA-bound state).
  Unlike Q99ZW2 there is no GO:0004520 row already present, so this is a real gain in
  precision rather than a collapse onto an existing child.
- **GO:0043571 maintenance of CRISPR repeat elements** (IEA) → `ACCEPT`, on the
  biogenesis limb (§4).
- **GO:0046872 metal ion binding** (IEA, UniRule) → `MODIFY` to GO:0000287 magnesium
  ion binding. HAMAP assigns Mg(2+) as the cofactor, and the Mg2+ ion is resolved in the
  HNH catalytic pocket coordinated by Asp587/Asn611 (PMID:31668930) — i.e. there is
  direct structural evidence for *this* protein, not only rule-based inference.
- **GO:0051607 defense response to virus** (IEA, UniRule) → `MODIFY` to GO:0099048
  CRISPR-cas system. This is the one call where the two orthologues legitimately
  diverge. For Q99ZW2, phage immunity is directly demonstrated. Here, the demonstrated
  interference substrate is DNA entering by **natural transformation** — plasmid and
  neisserial genomic DNA — and no viral target has been shown in strain 8013. The
  UniRule transfer therefore asserts a substrate class the evidence does not reach,
  while GO:0099048 (under GO:0099046 clearance of foreign intracellular nucleic acids)
  names the system and covers the substrates that were actually assayed. This is an
  argument against an electronic inference on biological grounds, which CLAUDE.md
  permits; no experimental curator call is being second-guessed.
- **NEW GO:0003690 double-stranded DNA binding**. Absent from GOA entirely. Supported
  by the sgRNA-dsDNA ternary structures and by the PAM-duplex read-out.

I searched PubMed for a report of meningococcal CRISPR restriction of a phage or
prophage and found none I could cite; rather than guess an identifier, the GO:0051607
call is made on the evidence that exists. If such a paper is identified the MODIFY
should be revisited — recorded in `suggested_questions`.

## 7. Things deliberately not annotated

- Genome editing in human cells, and the Nme2Cas9 platform work.
- Spacer acquisition (see §4).
- `GO:0005515 protein binding` for the AcrIIC1/AcrIIC3 interactions. Being *inhibited*
  by a phage protein is not a function of the host enzyme; it belongs on the Acr, and
  it is the Acr reviews and the suppression module that carry it.
