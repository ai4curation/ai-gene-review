# CYP71A12 (At2g30750, UniProt O49340) review notes

## Identity

- Cytochrome P450 71A12, 497 aa, N-terminal single-pass helical anchor (aa 4-24, UniProt
  ECO:0000255), heme-thiolate Cys439 (UniProt ECO:0000250). PANTHER PTHR47955:SF15
  (CYTOCHROME P450 71A2-LIKE) per UniProt DR line.
- Tandem paralog of CYP71A13 (At2g30770) on chromosome 2; ~89% amino-acid identity
  [PMID:25953104 "CYP71A13 shows 89% identity on the amino acid level compared with CYP71A12, and the corresponding genes are located as tandem copies on chromosome 2."]
- Third close homolog CYP71A18 [PMID:25953104 "A third homolog, CYP71A18, shares 87% and 85% identity on the amino acid level to CYP71A12 and CYP71A13, respectively."]

## Catalytic activity

- Converts indole-3-acetaldoxime (IAOx). In vitro (yeast microsomes), CYP71A12 turns
  IAOx over at a rate similar to CYP71A13 but partitions products differently, favouring
  indole-3-carbaldehyde (IAL/ICHO) + cyanide over the Cys-IAN adduct that leads to camalexin
  [PMID:24151049 "Although CYP71A12 turned over IAOx at a rate comparable to that of CYP71A13, the final products IAL and Cys-IAN accumulated in different ratios with these two enzymes"]
  [PMID:24151049 "Conversion to oxidized products at the assay endpoint is illustrative: CYP71A13 produced Cys-IAN (20%) and IAL (2%), while CYP71A12 produced Cys-IAN (3%) and IAL (18%)."]
- 18O2 labelling shows monooxygenation via an alpha-hydroxy-IAN (indole cyanohydrin)
  intermediate [PMID:24151049 "With 97% 18O2, both CYP71A13 and CYP71A12 catalyze incorporation of the isotopic label into IAL (74% and 81% 18O incorporation, respectively, Figure S10), providing clear evidence for an α-hydroxy-IAN intermediate."]
- Müller et al. 2015: ICHO major product; NADPH-dependent IAN -> ICHO + cyanide
  [PMID:25953104 "For CYP71A12, after 30 min of enzymatic reaction, ICHO was the major product of the IAOx turnover independent of reduced glutathione addition"]
- In N. benthamiana reconstitution CYP71A12 can substitute for CYP71A13 (abstract only)
  [PMID:23830903 "This has provided biochemical evidence for CYP71A12 conducting same reaction as CYP71A13 in the pathway."]
- Rajniak et al. 2015: CYP71A12 is the cyanohydrin-forming step of the 4-OH-ICN pathway
  [PMID:26352477 "Correlation analysis implicated CYP71A12, a P450 linked to camalexin biosynthesis18, as the most likely candidate gene for the cyanohydrin formation step (SI Table 3)."]
- GO term choice: GO:0047720 indoleacetaldoxime dehydratase activity (IAOx = IAN + H2O)
  is what CYP71A13 carries (IDA, PMID:17573535). CYP71A12 performs the same IAOx turnover
  but the chemistry is a heme-dependent monooxygenation through a cyanohydrin; the net
  IAN-forming route is shared. Accept GO:0047720 as NEW for CYP71A12 (Klein 2013 IDA-type
  evidence, Møldrup 2013), and keep monooxygenase activity. No GO term exists for
  "IAOx -> indole cyanohydrin" (noted as suggested question rather than NTR).

## Biological roles

### Indole-3-carboxylic acid (ICOOH/ICA) and 4-OH-ICN branch - the main in vivo role
- [PMID:25953104 "A major role of CYP71A12 was identified for the inducible biosynthesis of ICOOH ."]
- [PMID:25953104 "Specifically, the ICOOH methyl ester was reduced to 12% of the wild-type level in AgNO 3 -challenged cyp71a12 leaves."]
- [PMID:26352477 "all ICN derivatives with the exception of A6 are at ~10% of WT levels in the cyp71A12 mutant, but unaffected in the cyp71A13 and cyp71A18 mutants"]
- So for ICN/ICA metabolites CYP71A12 is non-redundant, whereas for camalexin
  CYP71A13 is dominant. No GO process term exists for ICOOH or 4-OH-ICN biosynthesis.

### Camalexin biosynthesis - minor in leaves, major in roots
- Leaves: [PMID:25953104 "Based on the comparison of cyp71a13 and cyp71a12 cyp71a13 phenotypes, the contribution of CYP71A12 to camalexin formation in leaves is significant but minor in relation to CYP71A13."]
- Roots, flg22: [PMID:20348432 "Indeed, a cyp71A12 insertion mutant was dramatically impaired for camalexin accumulation in the roots ( Figure 3 )."]
- Metabolon: CYP71A12 synthesizes indole-3-cyanohydrin used for camalexin
  (PMID:31511315, abstract only): "indole-3-cyanohydrin, which is synthesized by CYP71A12 and especially CYP71A13".
  The metabolon co-IP/FRET data were mostly on CYP71A13/CYP71B15 baits; the IPI with
  CYP71B15 (Q9LW27) is UniProt/IntAct-curated.

### Defense
- Pst susceptibility: [PMID:26352477 "Using surface inoculation to mimic the natural infection process, we found that compared to WT, the adult leaves of cyp71A12 and cyp82C2 are more susceptible to the virulent bacterial hemibiotroph Pst (Pseudomonas syringae pv."]
- Rhizobacterium-induced resistance (Pf.SS101): cyp71A12 among mutants that lose Pst
  resistance induction [PMID:23073694]; note this response is SA-dependent, while GO:0009682
  "induced systemic resistance" is defined as SA-independent - a mismatch.
- GNSR (general non-self response) gene, microbiota: cyp71a12 cyp71a13 double mutant
  allowed 120-fold more Pst [PMID:39627368].

### Expression (project ARATH_SINGLE_CELL_FUNGAL)
- Tang et al. 2023 (PMID:37741284, cache abstract only; full text from user-supplied PDF):
  in C. higginsianum-infected leaves, CYP71A12 induced at infection sites mainly in
  epidermis, CYP71A13 almost exclusively in vasculature. Full-text sentence (PDF, not in
  cache): "CYP71A12 was induced mainly in the epidermis, whereas CYP71A13 was almost
  exclusively induced in the vasculature cells (Figure S6B)". Expression only; does not
  ground any GO annotation.

### Antifungal immunity and ICA (Pastorczyk et al. 2020, abstract only)
- [PMID:31411742 "Our results indicate that CYP71A12, but not CYP71A13, is the major enzyme responsible for the accumulation of ICA in Arabidopsis in response to pathogen ingression."]
- [PMID:31411742 "We also show that both enzymes are key players in the resistance of Arabidopsis against selected filamentous pathogens after they invade."]
- Downstream ICA pathway: CYP71B6 converts IAN to ICHO/ICOOH and AAO1 oxidizes ICHO
  [PMID:24728709 "CYP71B6 was expressed in Saccharomyces cerevisiae and shown to efficiently convert indole-3-acetonitrile into ICHO and ICOOH, thereby releasing cyanide."]

## Rhea / UniProt / PAINT cross-check
- UniProt O49340 has no CATALYTIC ACTIVITY/Rhea line (EC 1.14.-.-, ECO:0000305); function
  text from PMID:26352477 (IAOx -> indole cyanohydrin).
- Paralog CYP71A13 (O49342) UniProt: RHEA:23156 "(E)-(indol-3-yl)acetaldehyde oxime =
  (indol-3-yl)acetonitrile + H2O", EC 4.8.1.3 (ECO:0000269, PMID:17573535) = GO:0047720.
- Rhea has no reaction for IAOx -> 2-hydroxy-2-(indol-3-yl)acetonitrile (cyanohydrin)
  (searched 2026-10-02); hence GO:0047720 used as nearest term for CYP71A12.
- IBA: oxidoreductase activity from deep node PTN009217258 (CYP71 clan, fine).
  ISR from PTN005384924, whose only Arabidopsis descendants with evidence are AT2G30750
  (CYP71A12) and AT2G30770 (CYP71A13), both from PMID:23073694 (Pf.SS101, SA-dependent).

## Localization
- No cached direct localization study. UniProt: Membrane, single-pass (sequence
  prediction). Typical plant class-II P450: ER-anchored, catalytic domain cytosolic.
- GOA IDA "endoplasmic reticulum lumen" from PMID:33831160 (TAIR, 2022-02-03): this PMID
  does not resolve in NCBI esummary ("cannot get document summary") or Europe PMC
  (hitCount 0) - likely a deleted/withdrawn PMID. Same IDA is on CYP71A13. Cannot read
  evidence -> UNDECIDED, with topology caveat (lumen unlikely for an N-anchored P450 whose
  catalytic domain faces the cytosol).

## Decisions summary
- IEA MF (monooxygenase, heme, iron, 16705) ACCEPT; IBA oxidoreductase ACCEPT.
- protein binding IPI REMOVE (uninformative).
- defense response NAS MODIFY -> defense response to bacterium.
- camalexin biosynthesis NAS ACCEPT (Millet 2010 roots; Müller 2015 leaves).
- ISR IMP and IBA both KEEP_AS_NON_CORE (caveat: Pf.SS101 response is SA-dependent, GO ISR definition is SA-independent; PAINT node worth re-examination).
- NEW: GO:0047720 indoleacetaldoxime dehydratase activity (IDA, PMID:24151049).
- NEW: GO:0050832 defense response to fungus (IMP, PMID:31411742). Participation: CYP71A12
  catalyses synthesis of the antifungal indolics. Comparator: CYP71A13 (IMP, PMID:17573535)
  and PAD3/CYP71B15 (IMP, PMID:26813622, QuickGO) carry this term.

## Deep research provenance
- `just deep-research-falcon ARATH CYP71A12 --fallback perplexity-lite` failed (2026-10-02):
  falcon timed out after 600 s; fallback failed ("Provider 'perplexity' not available.
  Available: falcon, asta, openscientist"). No deep-research file was generated; this review
  is based on manual PubMed searching and the cached primary papers listed above
  (PMID:24151049, 25953104, 26352477, 20348432, 23830903, 30798200, 31411742, 24728709 newly
  cached).
- Retried with `just deep-research ARATH CYP71A12 --provider asta`: it ran and wrote
  CYP71A12-deep-research-asta.md, but the retrieved papers are entirely off-topic (IgAN
  subtypes, avian immunome, LIPID MAPS, etc. - retrieval keyed on template boilerplate, not
  on CYP71A12). That file contributed nothing, was not used as evidence, and was deleted rather than committed.

## Update: late falcon deep research (2026-10-02)

The falcon job reported as timed out above kept running server-side and later wrote
`CYP71A12-deep-research-falcon.md`. The review was completed before it arrived and does not
rely on it; it is kept as a provenance record and a source of leads for future re-review.

## PMID:33831160 follow-up (coordinator check, 2026-10-02)

Rechecked directly: NCBI esummary returns "cannot get document summary", efetch returns an
empty PubmedArticleSet, and Europe PMC (EXT_ID:33831160) has 0 hits. The PubMed web page
(pubmed.ncbi.nlm.nih.gov/33831160/) serves a bot challenge, so any duplicate/redirect notice
could not be read; the record is therefore unidentified, not shown to be deleted.
QuickGO lists six TAIR annotations citing it, all dated 2022-02-03: GO:0005788 ER lumen (IDA)
on CYP71A12, CYP71A13 and CYP71B15; GO:0005783 ER (IDA) on CYP71B15; and two GO:0005515 IPI
rows on CYP71B15. This content resembles Mucha et al. 2019 (PMID:31511315, camalexin
metabolon), but per docs/reference_curation.md no replacement is recorded from similarity
alone. Someone with browser access to PubMed, or TAIR, can settle it in one lookup.

## PMID:33831160 resolved (2026-10-02)

PubMed's redirection notice (read in a browser by the project lead): "PMID: 33831160 was deleted
because it is a duplicate of PMID: 31511315" (Mucha et al. 2019, camalexin metabolon). Recorded as
`replacement: {reference_id: PMID:31511315, reason: DUPLICATE_RECORD}` on the reference.
Mucha's full text (read on PMC, PMC6881122; not cacheable, PMC serves abstract only) shows
CYP71A12, CYP71A13 and CYP71B15 fusions colocalizing with the ER lumenal marker RFP-HDEL
(Supplemental Figure 4), and states that eukaryotic P450s are anchored to the ER membrane with
the catalytic centre facing the cytosol. The ER lumen IDA was therefore changed from UNDECIDED to
MODIFY -> GO:0005789 endoplasmic reticulum membrane: the organelle call is sound, the lumen call
over-reads a confocal colocalization.

## 2026-10-09: combined with independent review

An independent review of CYP71A12 (PR 4451 branch) was merged into this file. Decisions that changed
relative to the previous version:

- **GO:0005506 iron ion binding (IEA)**: ACCEPT -> KEEP_AS_NON_CORE. The independent review marked it
  over-annotated (as for CYP71B15); CYP71A13 keeps it as non-core. The iron belongs to the heme
  cofactor already captured by heme binding.
- **GO:0042742 defense response to bacterium (IEP, PMID:39627368)**: ACCEPT -> KEEP_AS_NON_CORE. IEP
  basis is induction; the mutant data are necessity downstream of biosynthesis. Consistent with the
  defense-to-bacterium IMP rows in the CYP71A13 and CYP79B2 reviews. Removed from core_functions.
- **NEW GO:0047720 indoleacetaldoxime dehydratase activity**: kept, re-sourced to PMID:25953104 (Müller
  et al. 2015, full text), which assayed CYP71A12 kinetics directly: "it is clear that both enzymes are
  efficiently dehydrating IAOx" and "CYP71A12 catalyzed two consecutive reactions, the dehydration of
  IAOx to IAN , which is then further converted to ICHO and cyanide". Klein et al. 2013 (PMID:24151049)
  also reports "persistent production of the dehydration product IAN alongside oxidized products from
  IAOx" for these enzymes. The independent review had withheld this term because the 18O2 data show a
  monooxygenation via an alpha-hydroxy-IAN intermediate. Resolution: GO:0047720 describes the net
  conversion (and matches the CYP71A13 IDA comparator); the mechanistic caveat is kept as a proposed new
  term (cyanohydrin-forming monooxygenase) and a suggested question. Note that
  modules/camalexin_biosynthesis.yaml gives CYP71A12 only GO:0004497 monooxygenase activity (not edited).
- **NEW GO:0106148 4-hydroxyindole-3-carbonyl nitrile biosynthesis (IMP, PMID:26352477)**: added. This
  replaces the independent review's NEW GO:0042435 indole-containing compound biosynthetic process,
  dropped because it is an ancestor of the accepted GO:0010120 camalexin biosynthetic process, and its
  proposed new term "indole-3-carbonyl nitrile biosynthetic process", which already exists in GO as
  GO:0106148 (created from Rajniak et al. 2015, currently with zero annotations, so no contrary
  convention; CYP82C2 carries only the GO:0106149 MF). CYP71A12 performs the cyanohydrin-forming step,
  shown by reconstitution with FOX1 and CYP82C2. The GO definition wrongly calls 4-OH-ICN a cyanogenic
  glucoside (question raised).
- **NEW GO:0050832 defense response to fungus (IMP, PMID:31411742)**: kept (independent review judged it
  necessity-only). Comparator: CYP71A13 and CYP71B15 both carry it by IMP and are accepted as core. The
  disagreement is recorded in suggested_questions because the CYP71A12 data are abstract-only and largely
  in a pen2 background.
- Unchanged from this file where the reviews differed: ER lumen IDA stays MODIFY -> ER membrane (Mucha
  full text read on PMC; independent review had UNDECIDED); membrane IEA/NAS stay ACCEPT (independent
  review had MODIFY -> ER membrane, sourced partly from a falcon quote not present in the repo file, which
  was dropped); defense response NAS stays MODIFY -> defense response to bacterium; ISR IBA propagation
  review kept as SOURCE_BAD.
- Added PMID:21712415 (GGP1/GGP3 paper; cytosol-facing ER P450 topology statement) from the independent
  review as additional support for the ER-membrane MODIFY, and cited the repo falcon deep research for the
  metabolon evidence.

Provenance from the independent notes: UniProt O49340 function "Converts indole-3-acetaldoxime to indole
cyanohydrin. Involved in the biosynthetic pathway to 4-hydroxyindole-3-carbonyl nitrile (4-OH-ICN)";
cyp71A12 ICN derivatives at ~10% of wild type [PMID:26352477 "all ICN derivatives with the exception of A6
are at ~10% of WT levels in the cyp71A12 mutant, but unaffected in the cyp71A13 and cyp71A18 mutants"];
ICOOH methyl ester at 12% of wild type in AgNO3-challenged cyp71a12 leaves [PMID:25953104].
