# AP5M1 (human) — review notes

Working journal for the PAINT-backlog review of human **AP5M1 / Q9H0R1**, the
mu subunit of the fifth adaptor protein complex. Every assertion below carries
its provenance inline.

---

## 1. Identity check

`AP5M1-uniprot.txt` is `ID AP5M1_HUMAN`, `AC Q9H0R1;` (secondaries O95354,
Q6ZMD7, Q96DX3, Q9NVC5), `DE RecName: Full=AP-5 complex subunit mu-1`, 490 aa,
sequence version 2, `OX NCBI_TaxID=9606`. That is the protein the prompt names,
so no merged-accession substitution has happened. Gene names in the record:
`GN Name=AP5M1; Synonyms=C14orf108, MUDENG`, with protein-level aliases **Mu5**,
**Mu-2-related death-inducing protein (MuD)** and "Putative HIV-1
infection-related protein". The alias set matters: the literature is split
between papers that call this protein μ5/C14orf108 (membrane traffic) and papers
that call it MUDENG/MuD (cell death), and they barely cite one another.

Domain architecture, from the record itself:

- `FT DOMAIN 206..476 /note="MHD"` (PROSITE PS51072), i.e. a **mu-homology
  domain** — in AP-1/AP-2 this is the cargo-binding domain.
- `DR CDD; cd09256; AP_MuD_MHD; 1.` and `DR Pfam; PF00928; Adap_comp_sub; 1.`
- `DR PANTHER; PTHR16082; AP-5 COMPLEX SUBUNIT MU-1; 1.` and
  `PTHR16082:SF2`. **This is the family the IBAs come from, and it is not the
  general AP mu-subunit family.** See §5.
- Two isoforms; isoform 2 replaces 241–284 and deletes 285–490, i.e. it removes
  most of the MHD, and UniProt notes it "May be due to an intron retention". No
  annotation in the GOA record is isoform-scoped.
- No ACT_SITE, no BINDING, no metal — as expected for a non-catalytic adaptor
  subunit. No CAUTION line.

UniProt's own summary is deliberately hedged: *"As part of AP-5, a probable fifth
adaptor protein complex it may be involved in endosomal transport. According to
PubMed:18395520, it may play a role in cell death."* Subcellular location:
`Cytoplasm, cytosol {ECO:0000269|PubMed:22022230}`, plus late endosome membrane
and lysosome membrane as `ECO:0000305` (curator inference) with
`Note=May cycle on and off membranes.`

## 2. What AP-5 is

Hirst et al. 2011 (PMID:22022230) is the founding paper and is the source of
every experimental GOA row on this gene. Cached full text is available. The
relevant sequence of findings, in their own words:

- μ5 was found as an orphan MHD protein: *"The third type of MHD protein is
  encoded in humans by a gene on chromosome 14 and has been called C14orf108,
  FLJ10813, or MUDENG"*, and at the time *"otherwise nothing is known about its
  function"*.
- A yeast two-hybrid screen with full-length C14orf108 as bait pulled out
  DKFZp761E198 (= AP5B1/β5) from 136 colonies out of 69.8 million screened, and
  the interaction maps to β5 residues 16–229 — the same N-terminal quarter that
  contacts μ in AP-1 and AP-2.
- Reciprocal stability: *"knocking down DKFZp761E198 also decreased the intensity
  of the C14orf108 band, indicating that, like AP μ and β subunits [23],
  C14orf108 is stabilised by binding to DKFZp761E198."* [PMID:22022230
  "C14orf108 is stabilised by binding to DKFZp761E198."]
- Phylogeny: the μ homologues resolve into the four known AP clades plus *"an
  additional clade of C14orf108 homologues strongly supported"*, and the
  concatenated β+μ analysis supports a fifth clade, hence [PMID:22022230 "we
  suggest that C14orf108 and DKFZp761E198 should be renamed μ5 and β5,
  respectively, and that the complex that they form should be called AP-5."]
- AP-5 is ancient but patchily retained: [PMID:22022230 "AP-5 subunits can be
  found in all five eukaryotic supergroups, but they have been co-ordinately lost
  in many organisms."] Hirst 2018 names the losses that matter for model-organism
  curation: [PMID:29381698 "It is expressed at relatively low levels (only about
  10,000 copies in a HeLa cell, compared with about 300,000–1,000,000 copies for
  APs 1, 2, or 3)"] and it *"has been lost from several model organisms,
  including Drosophila melanogaster, Caenorhabditis elegans, and Saccharomyces
  cerevisiae"*.
- Not a clathrin adaptor: [PMID:22022230 "AP-5 does not associate with clathrin
  and is insensitive to brefeldin A."] The fractionation behind that:
  [PMID:22022230 "C14orf108 partitions approximately equally between membranes
  and cytosol, indicating that it cycles on and off the membrane; but unlike
  clathrin and AP-1, it is not enriched—or even detectable—in the CCV fraction."]
- The tetramer was completed by σ5 (C20orf29) and ζ (KIAA0415/SPG48); co-IP of
  GFP-tagged σ5 showed [PMID:22022230 "the anti-GFP antibody not only brings down
  the construct itself, but also C14orf108 and DKFZp761E198."]

The complex is actually a **heterohexamer**. Hirst 2013 (PMID:23825025,
abstract-only in cache) showed [PMID:23825025 "we show that the four AP-5
subunits can be coimmunoprecipitated with SPG11 and SPG15, both from cytosol and
from detergent-extracted membranes, with a stoichiometry of ∼1:1:1:1:1:1."],
[PMID:23825025 "In addition, AP-5, SPG11, and SPG15 colocalize on a late
endosomal/lysosomal compartment."] and proposed the architecture:
[PMID:23825025 "We propose that AP-5, SPG15, and SPG11 form a coat-like complex,
with AP-5 involved in protein sorting"]. Critically for this review, the
knockdown series included μ5: [PMID:23825025 "all six knockdowns cause the
cation-independent mannose 6-phosphate receptor to become trapped in clusters of
early endosomes."]

Mai et al. 2025 (PMID:40175557; **abstract only** in cache, `full_text_available:
false`) solved it: [PMID:40175557 "SPG11-SPG15 can cooperate with the fifth
adaptor protein complex (AP5) involved in membrane sorting of late endosomes."],
[PMID:40175557 "The AP5 complex is in a super-open conformation."],
[PMID:40175557 "the N-terminal region of SPG11 is required for AP5 complex
interaction and assembly."] and, the one molecular-activity statement anywhere in
the AP-5 literature, [PMID:40175557 "AP5-SPG11-SPG15 complex can bind PI3P
molecules, sense membrane curvature and drive membrane remodeling in vitro"],
[PMID:40175557 "essential for the initiation of autolysosome tubulation"].

I checked the depositions behind that paper directly (RCSB REST,
`data.rcsb.org/rest/v1/core/entry/…`): **8YAB** ("AP5 complex bound to
SPG11-SPG15") and **8YAH** ("full length AP5 complex bound to SPG11-SPG15"). Both
are five-entity cryo-EM models. The μ5 entity in both maps to **Q8BJ63, the
*mouse* orthologue**, as does ζ (Q3U829), while β5 (Q2VPB7), σ5 (Q9NUS5) and
spatacsin (Q96JI7) are human — so the reconstitution is mixed-species, and no PDB
entry maps to human Q9H0R1 (consistent with the UniProt record carrying no `DR
PDB` line). In 8YAH the μ5 chain is essentially fully modelled (unobserved only
at residue 1 and in five short stretches: 146–150, 188–190, 201–205, 285–290,
364–365). Mouse and human μ5 are 85.1% identical over the alignment (§4), so this
is a fair structural proxy, but it is a proxy, and it is the reason this review
does not treat the structure paper as direct evidence *on the human protein*.

## 3. What is known about mu-5 specifically, as opposed to about AP-5

This is the question that decides how the experimental rows are graded, so I
separated the two.

**Evidence that perturbs or observes μ5 itself**

| Finding | Source | Grade |
|---|---|---|
| siRNA (SMARTpool + individual oligos) against C14orf108 → CIMPR and Vps26 in larger perinuclear puncta; swollen MVBs with emanating tubules | PMID:22022230 | IMP, μ5-specific |
| GFP-μ5 (after siRNA damping of endogenous protein) punctate, overlapping LAMP1 | PMID:22022230 | IDA, μ5-specific, tagged + perturbed background |
| μ5 partitions ~50:50 membrane/cytosol, absent from CCVs | PMID:22022230 | IDA, μ5-specific, endogenous |
| μ5 co-immunoprecipitates with σ5-GFP together with β5 | PMID:22022230 | IDA, μ5-specific |
| μ5 is one of the "six knockdowns" that trap CIMPR in early endosomes | PMID:23825025 | IMP, μ5-specific (abstract) |
| μ5 protein falls when AP5Z1 is lost or spastizin is depleted | PMID:26085577 | μ5 measured, not perturbed |
| Bi-allelic LoF in *AP5M1* causes recessive macular dystrophy; anti-AP5M1 puncta in RPE | PMID:40081374 | human genetics + IDA-grade IF |
| MuD/AP5M1 is the μ subunit of AP5; TurboID proximity labelling | PMID:41915273 | abstract only |

**Evidence that is about AP-5 or the hexamer, with μ5 inferred**

- Hirst 2015 (PMID:26085577): three *AP5Z1*-nonsense patient fibroblast lines,
  [PMID:26085577 "complete loss of AP-5 ζ protein and a reduction in the
  associated AP-5"] µ5 protein, because [PMID:26085577 "concomitant reduction in
  levels of µ5 compared with controls, which is due to protein instability of AP
  subunits that occurs in the absence of complex assembly"]. Phenotype:
  multilamellar endolysosomal storage, hence [PMID:26085577 "AP-5 deficiency
  represents a new type of LSDs"].
- Hirst 2018 (PMID:29381698): CRISPR knockout of *AP5Z1* in HeLa, then
  fractionation profiling + MS. [PMID:29381698 "impaired retrieval of the
  cation-independent mannose 6-phosphate receptor (CIMPR), GOLIM4, and GOLM1 from
  endosomes back to the Golgi region"], with [PMID:29381698 "sortilin may act as
  a link between Golgi proteins and the AP-5/SPG11/SPG15 complex"], and
  [PMID:29381698 "The AP-5/SPG11/SPG15 complex localises to late endosomes and
  lysosomes"].

Because μ5 is destabilised when ζ is lost (Hirst 2015, quoted above), an *AP5Z1*
knockout is functionally an AP-5 knockout, and the CIMPR phenotype it produces is
the same one that μ5's own knockdown produces (Hirst 2011, Hirst 2013). That
concordance is what licenses giving AP5M1 the endosome-to-Golgi retrieval term;
it is not inferred from complex membership alone.

## 4. Does mu-5 have a working cargo-binding site? (the MHD question)

AP5M1 has a *bona fide* MHD by every domain resource (UniProt `DOMAIN 206..476`,
PROSITE PS51072, CDD `cd09256 AP_MuD_MHD`, Pfam PF00928). In AP-1/AP-2 the MHD is
the receptor for YxxΦ sorting signals, so "has an MHD" reads, wrongly, as "binds
cargo". Both Hirst papers say it does not, but neither names a residue:

- [PMID:22022230 "are altered in C14orf108, suggesting that if C14orf108 is
  involved in cargo recognition, it probably interacts with a different type of
  motif."] (the clause before this, elided here only because the cached sentence
  carries a `[21]` citation marker, is "The key residues in the μ subunits that
  bind to YXXΦ sorting signals")
- [PMID:29381698 "the highly conserved cargo binding sites found in the other AP
  complexes are absent in AP-5."]

I tested it rather than repeating it — `AP5M1-bioinformatics/`, written up in
`RESULTS.md`. Method in brief: derive the pocket from the solved complex (PDB
**1BXX**, μ2 second domain with the TGN38 DYQRLN peptide) by taking every μ2
residue within 4.5 Å of the peptide, after verifying the PDB author numbering
against Q96CW1 residue-by-residue; then map those 14 positions through a MAFFT
L-INS-i alignment of the five human μ subunits plus mouse and *Arabidopsis* μ5.

Result: **AP5M1 retains 3 of the 14** (K240, I461, R465), against 11/14 for
AP4M1, 10/14 for AP1M1 and 5/14 for AP3M1. The three closest contacts to the
signal tyrosine — μ2 F174 (3.75 Å), D176 (2.43 Å, the shortest contact in the
interface) and W421 (3.06 Å) — are **S210, S212 and A463** in μ5: no aromatic, no
acidic side chain, no bulk at any of the three. AP4M1 and AP1M1 keep all three;
even AP3M1, which also works without clathrin, keeps an aromatic and the
aspartate.

The obvious objection is that μ5 is simply the most divergent member (18.0%
identity to AP2M1), so any alignment-based count would look bad. Two controls
answer it. (i) The alignment reproduces a correspondence published independently
of this analysis: [PMID:40081374 "a missense affecting Tyr284 of AP4M1, the
corresponding amino acid residue of Tyr313 in AP5M1, is linked to spastic
paraplegia type 50"] — my alignment puts AP5M1 Y313 in the same column as AP4M1
Y284, and finds a tyrosine there in all seven sequences. (ii) Mouse Ap5m1, 85.1%
identical to the human protein, gives the same residue at 13 of the 14 positions.

**Conclusion carried into the review.** μ5 has the MHD *fold* but not the
tyrosine-signal *site*, and no sorting motif of any kind has been identified for
AP-5. So: no cargo-binding or cargo-receptor MF is proposed for AP5M1, and the
"has an MHD therefore binds cargo" inference is explicitly blocked in the review
text. This is the mirror of the fold-name-propagates-into-GO error, checked in
the direction the brief asks for — I did not assert "fold without function"
without testing the residues.

## 5. The five IBAs — and why the AP3M1 argument does **not** transfer

All five IBA rows carry the identical `WITH/FROM`
`PANTHER:PTN002699615|UniProtKB:Q9H0R1`, reference GO_REF:0000033, dated
20190314. The committed PAINT slice
`interpro/panther/PTHR16082/PTHR16082-paint.tsv` resolves the node completely:

```
PTHR16082  PTN002699615  GO:0005764  C  IBD  seeds=UniProtKB:Q9H0R1  taxon:2759
PTHR16082  PTN002699615  GO:0005770  C  IBD  seeds=UniProtKB:Q9H0R1  taxon:2759
PTHR16082  PTN002699615  GO:0005829  C  IBD  seeds=UniProtKB:Q9H0R1  taxon:2759
PTHR16082  PTN002699615  GO:0030119  C  IBD  seeds=UniProtKB:Q9H0R1  taxon:2759
PTHR16082  PTN002699615  GO:0016197  P  IBD  seeds=UniProtKB:Q9H0R1  taxon:2759
```

Five IBDs, one node, one seed, no IRD or IKR anywhere in the family. The node is
placed at the eukaryotic root (`taxon:2759`), which matches the paper that made
the family: AP-5 subunits occur in all five supergroups but are repeatedly lost.
The family is small and clean — `PTHR16082-entries.csv` lists six reviewed
proteins, all named "AP-5 complex subunit mu-1"/"mu" (human, mouse, rat, macaque,
bovine, *Arabidopsis*), all in subfamily `PTHR16082:SF2`; family counters give
1889 member proteins across 3729 taxa, integrated as `IPR039591`.

**The target is its own seed.** This is the expected, valid configuration, not
circularity: AP5M1's own IDA/IMP annotations from Hirst 2011 are the descendant
evidence the PAINT curator used to place the IBD, and the IBA then adds the
claim that the localisation and process are ancestral to the family rather than
human-specific — a claim the 2011 phylogeny (five supergroups) directly
supports. None of these sources is marked `CIRCULAR_OR_REDUNDANT`.

**Does the AP3M1 finding apply here?** The merged `genes/human/AP3M1/` review on
main found that the *whole-family* mu-subunit node carries a clathrin-cargo
adaptor term seeded only by AP-1/AP-2 mu subunits, and modified it to a
clathrin-free term. I checked whether AP5M1 inherits anything of the kind. It
does not, for three separate reasons:

1. **Different family.** AP5M1's only PANTHER assignment is PTHR16082 ("AP-5
   COMPLEX SUBUNIT MU-1"), a family that contains AP-5 mu subunits and nothing
   else. It is not in the general AP mu-adaptin family, so no whole-family node
   reaches it. `interpro/panther/PTHR10529/` is not present in this worktree and
   is not needed — AP5M1 is not in it.
2. **Different seeds.** Every IBD above is seeded by AP5M1 itself, not by AP-1/
   AP-2 donors, so there is no cross-complex leakage to argue with.
3. **No clathrin term arrives.** The only complex term that does arrive,
   `GO:0030119 AP-type membrane coat adaptor complex`, is not a
   clathrin-requiring term in its definition — it reads "*Any of several
   heterotetrameric complexes that link clathrin (**or another coat-forming
   molecule**, as hypothesized for AP-3 and AP-4) to a membrane surface*"
   (QuickGO `/ontology/go/terms/GO:0030119/complete`). AP-5 sits comfortably
   under it, and the child `GO:0044599 AP-5 adaptor complex` is explicitly
   clathrin-agnostic: "*…it is not clear whether AP-5 forms clathrin coats in
   vivo*". There is nothing to strip.

What *is* wrong with the GO:0030119 rows is only granularity: a term one level
more specific and exactly right — GO:0044599, whose ancestors include GO:0030119
(verified via the QuickGO ancestors endpoint) — has existed all along and is
already on the gene from ComplexPortal. Both GO:0030119 rows are therefore
MODIFY→GO:0044599, not REMOVE.

The other four IBAs are sound. Lysosome and late endosome are where the complex
works; `is_active_in cytosol` is true (μ5 really is ~50% soluble) but describes
the off-membrane reservoir rather than the site of action, so those rows are kept
as non-core rather than accepted as core. `GO:0016197 endosomal transport` is the
right breadth for a family-level assertion: the deeper step is known only in
human cells and only for a handful of cargo, and AP-5 is absent from most model
organisms, so pushing the node's term deeper would over-claim.

## 6. The three SubCell IEAs

`GO:0005765 lysosomal membrane` (SL-0157), `GO:0005829 cytosol` (SL-0091) and
`GO:0031902 late endosome membrane` (SL-0151) come from GO_REF:0000044, i.e. the
UniProt subcellular-location → GO mapping. The corresponding `CC SUBCELLULAR
LOCATION` lines in `AP5M1-uniprot.txt` are `Cytoplasm, cytosol
{ECO:0000269|PubMed:22022230}` (experimental) and late endosome / lysosome
membrane at `{ECO:0000305|PubMed:22022230}` (curator inference from the LAMP1
colocalisation and the membrane fractionation). The mapping is mechanically
faithful to the record; the two membrane terms inherit the 305-grade inference,
which is exactly the right strength — and the 2025 RPE work has since
corroborated the compartment independently in a second cell type
[PMID:40081374 "Confocal microscopy imaging revealed punctate labeling of AP5Z1,
AP5M1, and AP5B1 in the cytoplasm of RPE cells"], with co-staining for Rab7 and
TGN markers.

## 7. The MUDENG / cell-death literature

This is the whole of what the affinage record returned (§9), so it needs an
explicit verdict rather than silence.

- PMID:18395520 (the naming paper, abstract-only): MUDENG came out of a
  randomised hybrid-ribozyme screen for pro-death genes; [PMID:18395520 "Ectopic
  expression of MUDENG induced cell death in Jurkat T cells and HeLa cells"].
  This is **overexpression**, i.e. IMP-grade at best and ectopic by construction.
- PMID:23665015 (abstract-only): [PMID:23665015 "Caspase cleavage sites (D276 and
  D290) were located in the adaptin domain of MUDENG, and cleaved MUDENG showed
  the reduced killing activity"]. I checked the sequence claim: Q9H0R1 (sv2) has
  D at both 276 and 290 and both lie inside the annotated MHD (206–476). Being a
  caspase substrate is a post-translational event that happens *to* the protein;
  per the standing rule it is not a molecular function of the protein and is not
  annotated.
- PMID:27136675 (full text): in U251-MG astroglioma, MuD is **anti**-apoptotic —
  its depletion sensitises to TRAIL, and the effect is abolished by Bid
  co-depletion. Also [PMID:27136675 "MuD localizes predominantly in the ER and
  partly in mitochondria, then is decreased upon TRAIL stimulation"]. That
  localisation rests on a crude microsomal preparation made with a commercial "ER
  isolation kit" (their Figure 4g); microsomal fractions co-purify endosomes and
  lysosomes, so this is not resolution enough to contradict the LAMP1
  colocalisation, the CCV-fraction controls, the RPE immunofluorescence or the
  hexamer co-IPs. No ER or mitochondrion term is proposed.
- PMID:31427081 (abstract-only): AP5M1 overexpression is pro-apoptotic in
  cervical carcinoma cells and depends on BAX. Overexpression again.
- PMID:41915273 (2026, abstract-only) finally joins the two literatures:
  [PMID:41915273 "TurboID-based proximity labeling revealed reproducible
  interactions with AP5B1 and AP5M1 subunits"], and reports MuD as
  **anti**-apoptotic for TRAIL but promoting TMZ cytotoxicity in glioblastoma.

Net: the cell-death phenotype is real in the sense of being reproducible in these
labs' hands, but its sign reverses between cell types (pro-death on
overexpression in Jurkat/HeLa/cervical carcinoma; anti-death on depletion in
astroglioma/GBM), and every positive result is an over- or under-expression
experiment with no mechanism tied to AP-5 membrane traffic. GOA carries no
apoptosis term for this gene and I am not proposing one; it goes in
`knowledge_gaps` and `suggested_experiments` instead. Note the direction of the
error to avoid: this is *not* grounds to doubt the trafficking annotations, and
it is *not* grounds to annotate apoptosis.

## 8. Human genetics

Kaminska et al. 2025 (PMID:40081374, full text): [PMID:40081374 "we uncover
bi-allelic assortments of 23 different (22 loss-of-function) variants in AP5Z1,
AP5M1, and AP5B1 as independent causes of recessive IRD in members of 19 families
from nine countries"]. Three of the 19 families carry *AP5M1* alleles —
c.97C>T (p.Arg33Ter), c.1166G>A (p.Trp389Ter) and the single missense in the
whole study, c.938A>G (p.Tyr313Cys). The paper notes the paralogous residue
(quoted in §4) is mutated in SPG50. This is the first disease association for
*AP5M1* itself; *AP5Z1* has long been SPG48. It corroborates that AP5M1 is
non-redundantly required in a lysosome-heavy tissue (RPE), which is the strongest
organismal support the endolysosomal annotations have.

No GO annotation is proposed from the disease association itself — a disease
phenotype is not a biological process the gene product executes.

## 9. What affinage missed

`AP5M1-deep-research-affinage.md` has `self_evaluation_pairwise: win`,
`faith_pct: 100.0`, 5 citations, and `.affinage.log` says "trust gates clear".
Its five cited findings (PMIDs 18395520, 23665015, 23909422, 27136675, 31427081)
are all real and all correctly summarised — and all five are MUDENG cell-death
papers. It returned **nothing** on AP-5. Its narrative ends: *"Beyond its role in
apoptotic signaling, no clathrin- or adaptor-complex trafficking function has
been characterized for AP5M1 in the available corpus."* That sentence is false
for the protein: the AP-5 characterisation (PMID:22022230) is the source of
nine of the twenty GOA rows and of the UniProt FUNCTION line, and there are at
least four further AP-5 papers (PMIDs 23825025, 26085577, 29381698, 40175557) and
a 2025 human-genetics paper (PMID:40081374).

This is the precision-not-recall failure the brief warns about, in its purest
form: the decisive papers are titled for the *complex* ("The fifth adaptor
protein complex") or for a *partner* ("…the hereditary spastic paraplegia
proteins SPG11 and SPG15"), never for the gene symbol, and the symbol-anchored
corpus is dominated by one small group's MUDENG series. Recovering them needed
independent searching on the complex name, the partners and the structure. The
record is therefore marked `LOW_QUALITY` in `references[]` — not because any
individual claim in it is wrong, but because its scope statement is wrong and
would mislead a curator who trusted it. (Europe PMC was intermittently returning
503s during this work; the PMIDs above were recovered through NCBI esearch and
targeted Europe PMC queries on "AP5M1", "AP-5 adaptor", "MUDENG".)

Its `mechanism_profile` grounding — `GO:0005783 endoplasmic reticulum`,
`GO:0005739 mitochondrion`, Reactome `R-HSA-5357801 Programmed Cell Death` — was
not imported, per §7.

## 10. Curation decisions

20 GOA rows over 11 distinct terms (16 cellular_component, 4 biological_process,
**0 molecular_function**), 0 NOT rows, 0 isoform-scoped rows. By evidence: 6 NAS,
5 IBA, 5 IDA, 3 IEA, 1 IMP; by source: 9 UniProt, 6 ComplexPortal, 5 GO_Central.
By reference: PMID:22022230 ×9, GO_REF:0000033 ×5, GO_REF:0000044 ×3,
PMID:40175557 ×3. Counts produced by
`AP5M1-bioinformatics/check_goa_reconciliation.py` and a one-off tally of the
GOA tsv, not by eye.

| Term | Codes | Action |
|---|---|---|
| GO:0044599 AP-5 adaptor complex | NAS | ACCEPT (core complex membership) |
| GO:0030119 AP-type membrane coat adaptor complex | IBA, IDA | MODIFY → GO:0044599 (granularity) |
| GO:0005770 late endosome | IBA, IDA, NAS ×2 | ACCEPT |
| GO:0005764 lysosome | IBA, IDA, NAS | ACCEPT |
| GO:0031902 late endosome membrane | IEA | ACCEPT |
| GO:0005765 lysosomal membrane | IEA | ACCEPT |
| GO:0016020 membrane | IDA | MODIFY → GO:0031902 + GO:0005765 |
| GO:0005829 cytosol | IBA, IDA, IEA | KEEP_AS_NON_CORE ×3 |
| GO:0016197 endosomal transport | IBA, IMP | ACCEPT |
| GO:0016192 vesicle-mediated transport | NAS | MODIFY → GO:0016197 |
| GO:0007040 lysosome organization | NAS | ACCEPT |
| **GO:0042147 retrograde transport, endosome to Golgi** | — | **NEW** (IMP) |

One NEW row. No REMOVEs: nothing in this record is contradicted, and the two rows
that are merely uninformative (GO:0016020, GO:0016192) are true parents that
deepen cleanly rather than errors to delete.

## 11. Open questions carried into the review

- **No molecular function is established for μ5 itself.** It has the MHD fold
  without the tyrosine-signal site (§4), and no AP-5 sorting motif is known
  (PMID:29381698). The only demonstrated complex-level activity is the *in vitro*
  membrane deformation of the AP5–SPG11–SPG15 assembly (PMID:40175557), and which
  subunits execute it is not resolved — μ5 contributes as a subunit, and the
  review says exactly that and no more.
- **Which cargo?** CIMPR, GOLIM4, GOLM1 and sortilin are all implicated through
  AP-5 loss, but the only direct binding shown is to SPG15, not to AP-5
  (PMID:29381698). If μ5 recognises anything, it is a motif nobody has defined.
- **GO has no term for autophagic lysosome reformation / autolysosome
  tubulation.** QuickGO's ontology search returns nothing for "reformation", the
  children of GO:0007040 are only regulation terms plus phagolysosome assembly
  and lysosomal membrane organization, and the closest existing terms are
  GO:0170064 lysosome fission and GO:0097749 membrane tubulation (with a child
  GO:0097750 for endosome membranes but none for autolysosomes). Proposed as a
  new term rather than forced into an existing one.
- **Isoform 2** removes most of the MHD and is annotated as possible intron
  retention; whether it makes protein and whether it assembles with β5 is
  untested.
