# ALG9 (Q9H6U8) review notes

## Summary of verified biology
ALG9 is an ER-lumenal alpha-1,2-mannosyltransferase in the dolichol-linked oligosaccharide (LLO)
assembly pathway for protein N-glycosylation. It catalyses **two** sequential lumenal steps using
**Dol-P-Man** (dolichyl-phosphate-mannose, NOT GDP-Man) as the mannose donor:

- Adds the **7th mannose** onto Man(6)GlcNAc(2)-PP-dolichol → EC 2.4.1.259 → GO:0052926
  (RHEA:29531). Reactome R-HSA-446215.
- Adds the **9th mannose** onto Man(8)GlcNAc(2)-PP-dolichol → EC 2.4.1.261 → GO:0052918
  (RHEA:29539). Reactome R-HSA-446216.

Multi-pass ER membrane protein (7 TM helices per UniProt topology); catalytic mannose transfer
occurs on the lumenal side of the ER membrane. GT22 family (CAZy), Glyco_transf_22 Pfam,
InterPro IPR005599.

## Disease
- ALG9-CDG (CDG-Il / CDG type IL), MIM:608776. Frank et al. 2004 (PMID:15148656, E523K) and
  Weinstein et al. 2005 (PMID:15945070, p.Y286C in the abstract's numbering). LLO profiling
  shows accumulation of GlcNAc2Man6 and GlcNAc2Man8 lipid-linked structures — exactly the two
  substrates whose downstream mannose is missing when ALG9 is defective.
- Gillessen-Kaesbach-Nishimura syndrome (GIKANIS), MIM:263210 — Tham et al. 2016
  (PMID:25966638), severe skeletal dysplasia / polycystic kidney disease.
- DIBD1 / bipolar association (PMID:12030331 translocation) was later refuted (PMID:16859551).

## Annotation review decisions
- GOA carries BOTH EC-specific MF terms (GO:0052926 Man6→7th; GO:0052918 Man8→9th) plus the
  parent GO:0000026 (alpha-1,2-mannosyltransferase activity). The two specific terms are the
  core MFs; GO:0000026 (parent) and GO:0016757 (glycosyltransferase activity, generic) are
  correct-but-general.
- BP: GO:0006488 (dolichol-linked oligosaccharide biosynthetic process) is the most precise
  core BP; GO:0006487 (protein N-linked glycosylation) is the correct broader outcome.
- CC: GO:0005789 (ER membrane) core; GO:0098553 (lumenal side of ER membrane) is a precise
  IC-supported refinement consistent with lumenal catalysis; GO:0016020 (membrane) HDA is
  correct but general (over-annotation).

## Provenance
All supporting_text quotes are verbatim substrings of the cited cached publication
(publications/PMID_15148656.md, PMID_15945070.md), the cached Reactome entries, or
file:human/ALG9/ALG9-uniprot.txt. All publications are abstract-only (full_text_available:
false) — experimental IMP/IGI/IC annotations from those PMIDs are ACCEPTED (curator read the
full text), not removed.

## 2026-09-27 substantive source audit

This audit supersedes the historical judgments above concerning seven transmembrane helices,
the blanket bipolar-association refutation, and classification of broad correct terms as
over-annotations. The original source assertions, four isoform entries and machine files are
preserved. HGNC:15672 approves ALG9; DIBD1 is its historical alias. Root's current-main/alias/open-PR
preflight was independently checked against all five canonical file hashes before authoring.

All 26 original annotations were reviewed individually: 20 ACCEPT and six MODIFY, with no NEW
or PENDING rows. The broad alpha-1,2-mannosyltransferase and glycosyltransferase activities are
correct parent activities; their replacements identify the two already-seeded substrate-specific
reactions. A broad membrane HDA assertion is retained at its source resolution because independent
human structural evidence establishes membrane association. The original YTS proteomics
supplementary target hit was not recovered and is not represented as independently verified.

### Direct human enzymology and structural context

[PMID:41807832] is genuinely cached with full Methods and Results.
It uses human ALG9 isoform 1 (Q9H6U8), yeast ALG3 (P38179) and chicken ALG12 (F1P077), expressed
in human 293 c18 cells. Species identity follows the construct, not the host cell. Human ALG9 was
expressed with an N-terminal FLAG-eYFP-HRV3C construct and purified after tag cleavage.

The Results state: “Assays with Dol25-PP-GlcNAc2Man6 or Dol25-PP-GlcNAc2Man8 acceptor substrates
confirmed the dual activity of ALG9 in vitro (Fig. 1d,f).” These are purified-enzyme assays using
synthetic, shortened dolichol analogs and Dol25-P-Man donor. Products are transferred to a
fluorescent reporter peptide by TbSTT3B and resolved by tricine SDS-PAGE; the reporter enzyme
does not replace ALG9's mannose-transfer step. Prolonged incubations add one mannose per
appropriate acceptor rather than indefinitely extending the chain. The two core functions
represent distinct Man6 and Man8 acceptors, separated in precursor assembly by ALG12's eighth
mannose addition, not duplicate umbrella activities.

Human ALG9 has 11 transmembrane helices in the resolved structure, with the catalytic cleft at
the luminal membrane interface. The historical “7 TM helices per UniProt” statement is not
supported by the actual downloaded feature list and is superseded by the human structure.
The substrate-trapped structural complexes use the activity-reducing D82A substitution; the
wild-type enzyme assays must be distinguished from these trapping constructs. Structure and
activity were not measured for all four human isoforms.

### Original annotation sources

- [PMID:15148656], locally abstract-only: the indexed
  full original [PMC1181998](https://pmc.ncbi.nlm.nih.gov/articles/PMC1181998/) Methods/Results
  were read externally. Human patient fibroblast lipid-linked and protein-linked glycan profiles
  show Man6/Man8 accumulation and transfer of incomplete precursors. Human patient-derived
  wild-type and E523K constructs were tested in a sensitized ALG9-deficient yeast background.
  This supports the genetic annotations and luminal-pathway IC, without being purified-human
  kinetics or a direct 2004 topology experiment. The added 2026 evidence independently resolves
  the two human catalytic activities.
- [PMID:15945070], locally abstract-only: human
  p.Y286C, fibroblast Man6/Man8 accumulation, transferrin hypoglycosylation and causal yeast
  complementation are explicitly reported. Full methods were not recovered; no extra assay
  details are inferred. Yeast P53868 in the IGI WITH/FROM chain identifies the complementation
  context, not a claim that all observations were made on yeast protein.
- [PMID:19946888], locally abstract-only: the YTS
  membrane screen and its preparation method are verified. The actual ALG9 supplementary
  identification remains unrecovered. The curator's broad membrane assertion is accepted with
  independent human structural corroboration, without assigning an ER or plasma-membrane pool
  from this screen alone.
- Reactome R-HSA-446215 and R-HSA-446216 specify the seventh and ninth mannose reactions,
  respectively. R-HSA-4720478 and R-HSA-9035514 model defective versions of those events;
  they are not positive catalytic assays of mutant protein. Their generic MF mappings are
  refined to the corresponding specific reaction while retaining the original machine rows.
  R-HSA-446193 supports LLO-pathway context, but its summary's “3 terminal GlcNAcs” is an
  apparent wording error; the completed precursor has three terminal glucoses. No cached
  source text was altered.

### Inference and ontology checks

The seeded PAINT nodes are PANTHER:PTN000509239 (activity and process) and PTN000509188
(ER membrane). The full IBD/tree was not independently reconstructed; source_entities records
that limitation. Independent human evidence supports the target judgments. A target appearing
among the extant evidence is legitimate PAINT grounding, not circularity.

The actual mapping `InterPro:IPR005599` to GO:0016757 was read in
`rules/arba/_interpro2go.txt`; its GPI-related family name does not by itself assign ALG9 a
GPI-specific substrate. UniProtKB-SubCell:SL-0097 maps the ER location. The cached human
RHEA:29531 / EC:2.4.1.259 and RHEA:29539 / EC:2.4.1.261 records match the two current GO
reaction definitions. Live AmiGO definitions for
[GO:0052926](https://amigo.geneontology.org/amigo/term/GO:0052926) and
[GO:0052918](https://amigo.geneontology.org/amigo/term/GO:0052918) establish both as children
of GO:0000026, under glycosyltransferase activity. Specificity refinements do not imply false
parent activities.

Cached GO-CAM `65c57c3400000687` already models human ALG9 twice, with GO:0052926 and
GO:0052918, LLO biosynthesis and the luminal side of the ER membrane. The reviewed process
annotations describe work ALG9 catalyzes, not merely a requirement for downstream development.
There is no missing process assertion to manufacture; no NEW term or comparator-gap claim was
proposed. The two core reactions are distinct substrate steps rather than ancestor/descendant
duplicates.

### Historical citations and access gates

The three additional citations already present in the historical notes were verified against
primary PubMed identities and abstracts:

- [PMID:25966638], DOI:10.1038/ejhg.2015.91:
  severe human skeletal-dysplasia families, splice-site variant and glycosylation abnormalities;
  disease context, not an added developmental process.
- [PMID:12030331],
  DOI:10.1007/s10048-001-0129-x: a small-family translocation disrupting historical DIBD1;
  the abstract explicitly leaves general bipolar susceptibility unconfirmed.
- [PMID:16859551],
  DOI:10.1186/1744-9081-2-25: no association of tested common variations in two family samples.
  This does not prove the absence of every rare-variant or translocation effect. The historical
  notes and ancillary Reactome prose overstate the scope when calling the earlier hypothesis
  universally refuted.

One ordinary fetch of these three records exited 1 with 0/3 cached because of DNS failures
(`/tmp/ALG9-notes-fetch.log`). All three remain explicit cache gates; primary-page access is
not a substitute for normal machine caches. The three original GOA PMIDs were already cached
and the normal GOA-publication fetch completed 3/3. The required genuine Falcon attempt with
perplexity-lite fallback failed before either provider ran because dependency retrieval from
PyPI failed DNS (`/tmp/ALG9-provider.log`). No provider artifact was created or fabricated.

The recursive authored/source census includes all seven substantive PMIDs and their DOI links,
the five cited Reactome entries and the immutable UniProt/GOA sources. No provider artifact
exists. Exactly the three historical PMIDs above are missing; PMID:41807832 is a genuine
previously imported machine cache. The review remains DRAFT while cache warnings remain.

Root independently read all 26 judgments, 17 reference assessments and both cores, and checked the cached 2026 human Results. Two refinements were incorporated: each core retains the narrower LLO process alone, while the original broader N-linked glycosylation annotations remain accepted; the luminal-face IC row now attaches the explicit cached Reactome lumen statement. No original source assertion or action changed in this final refinement.


## 2026-09-27 recovered-source and review follow-up

The three missing records listed in the preceding audit are now present as unchanged normal
fetcher outputs from Actions run `36313594604`, source commit
`408e7c41d93c2fd63f54ac1da5d7201edbc901bb`. Their exact bytes were independently checked
against the archived and staged records before canonical import. This section supersedes the
earlier cache-absence statement; it does not change the historical record of the failed local fetch.

- [PMID:25966638], DOI:10.1038/ejhg.2015.91, is **abstract-only locally** despite its PMC identifier.
  The abstract reports two unrelated families and three affected fetuses with homozygous
  c.1173+2T>A, exon 10 skipping and increased monoglycosylated transferrin. Those observations
  connect severe Gillessen-Kaesbach-Nishimura skeletal dysplasia to ALG9-CDG; they do not assign
  ALG9 a separate skeletal-development reaction or measure purified enzyme kinetics.
- [PMID:12030331], DOI:10.1007/s10048-001-0129-x, is **abstract-only locally**. The translocation
  disrupts historical DIBD1/ALG9 in a small family. The abstract itself says the broader linkage
  and linkage-disequilibrium results generally did not support susceptibility and ends with the
  role unconfirmed. It is a historical hypothesis, not a demonstrated psychiatric function.
- [PMID:16859551], DOI:10.1186/1744-9081-2-25, contains **full Methods, Results and Discussion**.
  The human family study tested four repeat markers plus V289I by TRANSMIT analyses. Informative
  transmissions came from 166 NIMH families with 250 affected offspring and 129 PITT families with
  135 cases. These are the informative subsets, not the total recruited pedigree counts. No tested
  common allele or haplotype showed significant transmission disequilibrium. The study discusses
  limited marker/sample coverage and possible rare structural effects; it does not universally
  refute every ALG9 susceptibility hypothesis. Its historical introductory discussion of uncertain
  terminal mannose linkage is not substituted for the later direct human enzyme evidence.

The two bipolar papers remain low-relevance references because they substantiate the explicit
correction of the ancillary Reactome and historical-notes susceptibility language. Their retention
does not add a disease-process annotation. The clinical paper supports the named severe ALG9-CDG
presentation in the biological summary. Reference verification reflects actual primary identity
and scientific scope; prior network failure was an availability gate, not evidence that an
externally verified identifier was incorrect. Renewed direct PubMed opens during this follow-up
encountered a browser challenge; the original primary identity verification, independently
verified import receipt and actual recovered contents remain the evidential record.

All 26 original annotations, their source fields and actions, all four alternative products,
17 reference identities and both catalytic cores are preserved. The IBA refinement specifies
the measured human acceptor reactions; it does not claim that the unreconstructed ancestral node
had both precisely scoped activities. No new annotation is manufactured. Broad membrane HDA
remains ACCEPT at the source's resolution because independent human structural evidence supports
membrane association. The unrecovered YTS supplementary hit is still not claimed as independently
verified, and no narrower compartment is inferred from that screen. Correct broad process and
component annotations need not be duplicated in the compact core to remain core biology.

The original 2004 genetic assay remains supported by exact cached abstract quotations. Its
externally inspected full Methods/Results and sensitized yeast assay context remain documented
above, explicitly distinct from cached full-text availability. Short exact UniProt EC/Rhea
cross-references now accompany both electronic specific-reaction rows as curated database
corroboration, alongside the independent human experiments. The description states the enzyme
family, donor, two EC reactions and disease context; synthetic assay details stay in the evidence
assessments. The current recursive authored/provider citation census has seven required PMIDs
and five Reactome records, all cached. No provider report exists, and no new source request is
introduced by this follow-up.

An independent annotation-reviewer consultation read the recovered common-variant study's
Methods, Table 1 and Discussion and confirmed the informative-family counts and rare-variant
limitations. It found no objection to retaining the two bounded historical references or the
unchanged annotation/core decisions. Targeted validation passed without curation warnings;
with all required citations cached, the review is now COMPLETE.
