# AXIN2 review notes

## 2026-09-30 — Source recovery and initial evidence assessment

Human AXIN2 is UniProt Q9Y2T1, HGNC:904, an 843-residue nonenzymatic scaffold with RGS and DIX domains. The normal seed contains 117 distinct source annotations and no alternative-product section. Preserve these source objects, including supporting entities, during review. The immutable UniProt feature record distinguishes annotated domains from transferred interaction regions; it does not give AXIN2 kinase, ubiquitin-ligase or ADP-ribosyltransferase catalysis.

Seed38 recovered the three primary files. Ten absent normal caches (eight publications and two human Reactome events) were imported byte-for-byte; 28 existing caches were preserved and two PANTHER exports remain quarantined. Larger staged versions of some existing publications can inform manual reading without replacing the normal canonical caches. The Falcon command with the Perplexity-lite fallback failed once on 2026-09-30 and generated no report. Its exit status and output hash are retained in the temporary provider-attempt record; no provider research success is claimed.

[PMID:11940574](https://pubmed.ncbi.nlm.nih.gov/11940574/) supports a Wnt-responsive negative feedback mechanism: AXIN2 expression responds to beta-catenin/TCF, while the AXIN2-containing destruction machinery limits beta-catenin abundance. The complete normal abstract distinguishes rat transformation, mouse epithelial experiments and human cancer-cell observations. AXIN2's own promoter regulation does not make the AXIN2 protein a transcription factor. [PMID:15042511](https://pubmed.ncbi.nlm.nih.gov/15042511/) supplies human genetic evidence linking AXIN2 variants with tooth agenesis and colorectal neoplasia; this developmental outcome should remain distinct from its molecular scaffold activity.

### Centrosome and centromere terms

The normal [PMID:20300119](https://pmc.ncbi.nlm.nih.gov/articles/PMC2854593/) cache has partial HTML; the larger, unchanged Seed38 record was read through the Results/Discussion and Methods. Human SW480/U2OS experiments and mouse fibroblast perturbations connect C-Nap1-dependent AXIN2 localization with suppression of premature centrosome splitting. AXIN2 promotes GSK3-beta-dependent beta-catenin phosphorylation; it is not the kinase. Rescue, interaction-domain deletions and beta-catenin perturbations support a local mechanism separable from beta-catenin transcriptional output. Figure pixels and supplements were not inspected.

[GO:0070602](https://amigo.geneontology.org/amigo/term/GO%3A0070602) concerns sister chromatids at a chromosomal centromere. [GO:0046603](https://amigo.geneontology.org/amigo/term/GO%3A0046603) concerns suppression of centrosome separation; its parents include regulation of mitotic centrosome separation and negative regulation of cell-cycle process. These official indexed definitions were checked. For the PMID:20300119 IMP row (zero-based index 108), refinement to GO:0046603 is supported by the measured organelle endpoint. The adjacent IBA assertion requires a separate phylogenetic assessment; this reading does not inspect its PAINT tree or establish that all donor assertions have the same defect.

### Evidence boundaries still being investigated

The PMID:11017067 cache contains bibliographic text and an erratum pointer but no scientific abstract. Publisher access failed; the mismatch-repair assertion cannot be rejected from its title. The complete PMID:18755497 abstract describes AXIN2 repeat-sequence frameshift mutations in unstable gastric cancers, which alone does not establish that AXIN2 performs repeat maintenance. The complete PMID:17072303 abstract describes GSK3-beta trafficking and Snail1 protein stabilization, which alone does not establish mRNA stabilization. Their respective experimental annotation rows remain open for source-specific adjudication rather than being removed from incomplete evidence.

An independent annotation-reviewer consultation is in progress for all 117 rows. No curated review decisions, completed status, authoritative PANTHER assignment or new process annotation are asserted by these notes.


## Integrated all-annotation assessment (2026-09-30T02:12:31.429431+00:00)

The independent annotation-reviewer consultation covers all 117 original source
objects. Root reviewed its complete unique rationales, the individual partner
identifiers for the 35 HuRI rows, and the proposed core. The prospective review
has 30 ACCEPT, 30 KEEP_AS_NON_CORE, 49 UNDECIDED and eight MODIFY, with no NEW
assertions. All original source objects remain exact; no alternative products
were present and none were invented.

The proposed principal function is protein complex scaffold activity in the
beta-catenin destruction complex. The current official
[AmiGO scaffold definition](https://amigo.geneontology.org/amigo/term/GO%3A0140378)
was independently checked: this denotes integral structural organization of a
complex. AXIN2 performs that organizing work; it does not supply the kinase or
ubiquitin-ligase chemistry. Existing annotations provide the process coverage,
so no NEW process is needed. The beta-catenin turnover role is distinct from
AXIN2 being consumed during its own TNKS/RNF146-dependent degradation.

Root independently checked the PubMed record and figure descriptions for
[PMID:21383061](https://pubmed.ncbi.nlm.nih.gov/21383061/). Human AXIN2 is explicitly
included in the complex purification, while the inspected localization figures
use AXIN1 reagents. The normal AXIN2 cache for this paper remains abstract-only.
For PMID:20300119, the normal cache contains Introduction and complete Methods;
the richer verified staged record supplies the Results and Discussion read
separately. Figure pixels and supplements were not inspected. The eight
refinements include kinase/beta-catenin binding, cytosol, canonical Wnt
regulation, destruction-complex membership, complex scaffolding and the
centrosome-separation correction. The separate PAINT centromeric-cohesion
assertion remains unresolved pending its ancestral and descendant evidence.

The two additional normal-cache requests, PMID:28069701 (mouse valves) and
PMID:23996200 (rat adipogenesis), failed once with DNS errors and created no
cache. Their official abstracts were read by the independent reviewer, but
formal added reference objects await source recovery. The provisional YAML
is under tmp; canonical integration and focused checks remain pending.


## Completed initial curation — 2026-09-30

All 117 original annotations have now been assessed after the independent
annotation-reviewer consultation: 30 ACCEPT, 30 KEEP_AS_NON_CORE, 49 UNDECIDED
and eight MODIFY. Source assertions and their evidence, references, qualifiers
and supporting entities are preserved. The record remains DRAFT and contains
no NEW annotation or invented alternative product.

Source77 recovered [PMID:23996200](https://pubmed.ncbi.nlm.nih.gov/23996200/) and
[PMID:28069701](https://pubmed.ncbi.nlm.nih.gov/28069701/) through the ordinary
fetcher; both complete normal abstracts were read and both remain abstract-only.
The rat glucocorticoid/adipogenesis and mouse valve-maturation evidence supports
the existing transferred annotations with explicit organism boundaries. The
two papers are now included as formal references. Their exact normal cache
bytes and every previously available source cache are preserved.

The principal core is the nonenzymatic beta-catenin destruction-complex
scaffold. The centrosome-versus-centromere correction is limited to the direct
human/mouse experimental row. The distinct ancestral IBA and unavailable
source-specific mismatch-repair, repeat-maintenance, mRNA-stabilization and
interaction experiments remain unresolved. Supported generic interactions
remain non-core under the user-supplied action definitions. No unsupported
enzymatic activity or NEW process is inferred from perturbation phenotypes.

The failed deep-research attempt is retained as a failure; these are manual
research notes. Focused validation, rendering and generated history validation
are recorded separately after this integration.

Final focused validation passed with four nonblocking advisories: two generic
interactions, one cytoplasmic location refinement, and the deliberately distinct
experimental versus ancestral cohesion decisions. Structured propagation metadata
records term granularity for the scaffold refinement and unresolved inheritance
for the cohesion assertion. Rendering and generated history validation passed.


## First PR feedback correction (2026-09-30)

The earlier proposed GO:0046603 replacement imposed an unsupported mitotic restriction. [PMID:20300119](https://pubmed.ncbi.nlm.nih.gov/20300119/) measures premature centrosomal splitting in asynchronous cultures, with an interphase C-Nap1/rootletin-linker context. The corrected replacement is [GO:1903127 positive regulation of centriole-centriole cohesion](https://amigo.geneontology.org/amigo/term/GO%3A1903127), whose [regulation parent](https://amigo.geneontology.org/amigo/term/GO%3A0030997) and [cohesion target](https://amigo.geneontology.org/amigo/term/GO%3A0010457) were checked. This correction supersedes the earlier mitotic-term choice in these append-only notes. AXIN2 organizes the GSK3/beta-catenin mechanism; it is not the kinase. The independent consultant additionally read the staged Results/Discussion and confirmed the rescue interpretation.

Seven generic-binding assertions with curated beta-catenin or GSK3 partners are refined to beta-catenin binding or protein kinase binding. This follows the experimental curator's partner attribution and independently supported AXIN2 interactions in [PMID:22056988](https://pubmed.ncbi.nlm.nih.gov/22056988/), [PMID:30824926](https://pubmed.ncbi.nlm.nih.gov/30824926/) and PMID:20300119. It does not establish that the original supplementary interaction rows or constructs were independently inspected, and co-complex detection does not establish purified direct binding. The existing reference-level access and erratum limits remain. Forty other generic-binding rows retain their existing decisions pending the outstanding policy question.

The broad cytoplasmic assertion is retained as non-core because it covers both cytosolic and centrosomal pools. Unread mismatch-repair/repeat-maintenance experiments remain UNDECIDED; the abstract alone does not justify overruling an experimental curator. The distinct IBA cohesion assertion is unchanged. Independent review passed the nine changed annotations and added question. All 117 source objects, all references and the single scaffold core remain intact: 30 ACCEPT, 31 KEEP_AS_NON_CORE, 42 UNDECIDED, 14 MODIFY and no NEW annotations.
