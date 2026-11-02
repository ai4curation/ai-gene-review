# CAD (human, UniProtKB:P27708) review notes

## Summary of biology

CAD is a large (2225 aa) multifunctional cytosolic protein that catalyses the first
three (committed) steps of de novo pyrimidine biosynthesis. It combines four enzymatic
activities across four domains, from N- to C-terminus:

1. **Glutamine amidotransferase (GATase, EC 3.5.1.2)** + **Carbamoyl-phosphate synthetase
   (CPSase)** together constitute the **glutamine-dependent carbamoyl phosphate synthetase II
   (CPS II, EC 6.3.5.5)**: L-glutamine + 2 ATP + HCO3- -> carbamoyl phosphate + L-glutamate
   + 2 ADP + Pi. This is the *cytosolic* pyrimidine CPS, distinct from the mitochondrial
   urea-cycle CPS1 (CPS I). The ammonia-dependent partial reaction is EC 6.3.4.16.
2. **Aspartate transcarbamylase (ATCase, EC 2.1.3.2)**: carbamoyl phosphate + L-aspartate ->
   N-carbamoyl-L-aspartate + Pi.
3. **Dihydroorotase (DHOase, EC 3.5.2.3, Zn2+-dependent)**: N-carbamoyl-L-aspartate ->
   (S)-dihydroorotate (reversible; the cyclization/dehydration step).

The endogenously produced carbamoyl phosphate is channeled from the CPS active site to the
ATCase active site [UniProt FUNCTION]. CAD assembles into a homohexamer (~1.5 MDa)
[PMID:24332717].

## Regulation

- Activity is allosterically regulated (PRPP activates; UMP/UTP inhibit the CPSase reaction).
- **MAP kinase (Erk1/2)** phosphorylates Thr-456 just prior to S phase, activating the pathway;
  PKA phosphorylation downregulates it as cells leave S phase [PMID:15890648; UniProt PTM].
- **mTOR/S6K1 (RPS6KB1)** phosphorylates Ser-1859, promoting oligomerization and stimulating
  the pathway [UniProt PTM; PMID:23429703, PMID:23429704 — mTORC1/S6K1 activates de novo
  pyrimidine synthesis].
- On EGF stimulation, phospho-Thr-456 CAD translocates to the nucleus; nuclear import promotes
  optimal cell growth [PMID:15890648].

## Disease

Biallelic (autosomal recessive) loss-of-function variants cause **CAD deficiency /
Developmental and epileptic encephalopathy 50 (DEE50, MIM:616457)**, a uridine-responsive
epileptic encephalopathy with anemia/anisopoikilocytosis; it is also classified as a
congenital disorder of glycosylation (CAD-CDG) because impaired pyrimidine synthesis
depletes UDP-sugar glycosylation donors [PMID:25678555]. Uridine supplementation rescues the
metabolic and clinical phenotype.

## Interactions

- **Rad9** (checkpoint protein) binds the CPSase domain of CAD and stimulates CPSase activity
  ~2-fold [PMID:15326225] -> supports GO:0019899 enzyme binding (with Rad9, UniProtKB:Q99638).
- **14-3-3 (YWHAZ)** [PMID:15161933, IntAct], **CNTROB** [PMID:35709258, IntAct], and
  self-interaction (homohexamer) [PMID:24332717] — generic protein binding IPIs.
- **Adenovirus preterminal protein (pTP)** binds CAD at nuclear-matrix viral replication
  sites [PMID:9525610] — supports nuclear matrix localization.

## Curation decisions (headline)

Core MFs (all strongly supported by structure/enzymology + IBA + EC/ISS):
- GO:0004088 carbamoyl-phosphate synthase (glutamine-hydrolyzing) activity (CPS II)
- GO:0004087 carbamoyl-phosphate synthase (ammonia) activity (partial CPS reaction)
- GO:0004359 glutaminase activity (GATase partial reaction)
- GO:0004070 aspartate carbamoyltransferase activity (ATCase; EXP PMID:24332717)
- GO:0004151 dihydroorotase activity (DHOase; IDA/EXP PMID:24332717, Zn2+)
Core BP: GO:0044205 'de novo' UMP biosynthetic process; GO:0006207 'de novo' pyrimidine
nucleobase biosynthetic process. Core CC: GO:0005829 cytosol.

Flag / over-annotation:
- GO:0004672 protein kinase activity (ISS from P08955): CAD has NO kinase domain; this is a
  spurious ISS transfer (P08955 is Dictyostelium; CAD is a substrate of kinases, not a kinase).
  MARK_AS_OVER_ANNOTATED (do not REMOVE — ISS, not IEA-EC; but biologically unsupported).
- Bare GO:0005515 protein binding IPIs (14-3-3, CNTROB) and GO:0042802 identical protein
  binding: uninformative; keep experimental but MARK_AS_OVER_ANNOTATED per policy.
- GO:0016020 membrane (HDA, NK-cell membrane proteome) and GO:0070062 extracellular exosome
  (HDA): CAD is cytosolic; these are proteomic co-purification, not genuine locations ->
  over-annotated.
- Ensembl GO_REF:0000107 rat/mouse ortholog transfers (liver development, heart development,
  lactation, response to caffeine/cortisol/insulin/testosterone, xenobiotic metabolism,
  L-citrulline biosynthesis, etc.): these are pleiotropic physiology / whole-animal responses
  transferred electronically; not core. L-citrulline biosynthesis (GO:0019240) and xenobiotic
  metabolism are biologically dubious for the cytosolic pyrimidine CPS -> over-annotated.

## 2026-10-04 UTC — Completed manual reassessment of the existing human CAD review

The earlier notes above are retained as a historical record. Several earlier conclusions
are corrected by the present reassessment; they must not be treated as the final
assessment of kinase activity, localization, protein binding, or clinical rescue.
All 84 original annotation objects and their machine-supplied terms, evidence,
references and other source fields are preserved. The three catalytic cores remain
CPS II, ATCase and DHO, with distinct chemical steps in the same cytosolic pathway.
CAD releases dihydroorotate; DHODH and UMPS perform the subsequent reactions producing
UMP. The UniProt text describes CPS-to-ATCase channeling. It does not justify an
additional claim that a demonstrated continuous channel connects all three modules.

The normal deep-research wrapper attempted Falcon and then perplexity-lite once in
isolation. Both failed with connection errors and produced no provider report. The
work documented here is manual source review, not a successful provider study.

### Evidence read and limitations

All ten original cached publication abstracts, the available OpenCell Discussion,
the three complete cached Reactome reaction summaries, and the relevant UniProt
function, catalytic, interaction, localization and disease sections were read.
The OpenCell cache has `full_text_available: true` but actually contains the abstract
and Discussion; its CAD-specific interaction table was not available. Original
full-paper figures and supplements were not generally accessible. The reference
assessments distinguish available sections from flags or titles.

An indexed primary copy of the CAD–RAD9A paper additionally exposed Results,
captions and Discussion: [PMID:15326225](https://pmc.ncbi.nlm.nih.gov/articles/PMC516061/).
The reported complex comes from coexpression, and purified-protein mixing did not
recreate stable association or stimulation. The kinetic readout couples CPS and
ATCase. This supports the CAD catalytic/interaction context without assigning
RAD9A activity to CAD, or treating the binding label as evidence of CAD activating
RAD9A. Full Methods and original images were not inspected.

The human DHO paper [PMID:24332717](https://pubmed.ncbi.nlm.nih.gov/24332717/)
directly supports DHO catalysis and zinc coordination. Its isolated-domain structure
is not a whole-protein human CAD hexamer structure. Reactome explicitly distinguishes
purified human activities from hamster-based inference about the predominant
hexameric assembly. The older Reactome statement that human DHO had not been
directly assayed is superseded by the later human domain experiments.

### Corrected interpretations

* The exact ISS donor P08955 is golden-hamster CAD, recorded as taxon 10036 in the
  PTHR11405 member table, not Dictyostelium. The IBA glutamine-metabolism node has a
  separate Dictyostelium descendant; those provenance chains must not be conflated.
  The official kinase definition concerns phosphorylation of protein residues, not
  possession of a canonical kinase fold. Primary autophosphorylation evidence in
  [PMID:11986331](https://pubmed.ncbi.nlm.nih.gov/11986331/) makes the older domain-only
  rejection unsound. The normal abstract is now cached and read: it reports
  Thr1037 modification, SDS purification/renaturation controls and a partly
  concentration-dependent reaction. Indexed primary Methods identify hamster-cell
  and recombinant preparations; no direct human autophosphorylation assay is claimed.
* The 2005 nuclear-localization claim and 2020 cytoplasm-only study are genuinely
  conflicting reports. The former does not establish MAPK phosphorylation as the
  cause of nuclear import. Nuclear rows remain unresolved pending exact assay
  comparison. The adenovirus-associated nuclear-matrix result is retained as a
  conditional experiment, not a general nuclear metabolic core.
* Human CAD deficiency and uridine rescue of cellular nucleotide/glycosylation
  abnormalities are established by PMID:25678555. The 2017 clinical response and
  2020 variant-complementation studies provide different kinds of evidence. Their
  normal caches were imported and read. The latter uses human U2OS CAD-knockout
  cells, GFP-tagged human CAD, defined inactivating controls and patient variants.
  It predicts benefit from individual-variant complementation, rather than testing
  combined patient alleles or constituting a treatment trial. Clinical improvement
  must not be attributed to the 2015 cellular-rescue experiment alone.
* The immutable UniProt disease block attaches PMID:28087732 to CAD, while that
  record's own title and the official abstract concern GNB1. This citation
  discrepancy remains explicit and unresolved. No identifier was remapped and
  that paper is not used as positive CAD evidence.
* Supported CAD–YWHAZ and CAD–CNTROB generic-binding assertions are retained as
  non-core under the project's standing user instruction. Exact GOA partners are
  independently present in the immutable human UniProt interaction block. The
  target screen tables remain unread; no finer activity is inferred. Predominantly
  cytosolic location does not refute membrane association or vesicular packaging.
  The two HDA localization rows remain unresolved rather than being labelled
  contamination without target-level evidence.

### Propagation and process scope

Six exact term/node/descendant sets were joined to the local PAINT file
`interpro/panther/PTHR11405/PTHR11405-paint.tsv`. A target self-source is legitimate;
neither donor count nor a mixed family architecture is a reason to reject a node.
The full tree/MSA was not reconstructed, and unreviewed LLM family descriptions
were excluded from the evidence.

The [official MGI/RGD comparative Cad graph](https://www.informatics.jax.org/homology/GOGraph/Cad)
was generated in March 2023. It exposes historical rat experimental provenance but
is not claimed as a reconstruction of the exact current Ensembl transfer. Its
developmental/hormone rows include expression-based studies, while insulin/starvation
have direct-assay evidence. Those original experiments were not broadly reread,
so individual unresolved decisions replace unsupported blanket mechanistic claims.
Fine neuronal localization is not rejected from a title. The recovered complete
PMID:1673139 abstract reports rat/hamster glial staining and rat GFAP confirmation;
it does not expose the neuronal-body or terminal-bouton assay. The unread full
article could contain additional experiments, so those fine locations remain
unresolved.

Two donor findings need specific attention. The recovered complete abstract of
[PMID:18515330](https://pubmed.ncbi.nlm.nih.gov/18515330/) reports rat DHOase-dependent
metabolism of ring-opened dexrazoxane metabolites, contrary to the old categorical
xenobiotic-metabolism removal. The citrulline mapping points to a CPS II study,
[PMID:7053379](https://pubmed.ncbi.nlm.nih.gov/7053379/); its abstract distinguishes
CPS II from CPS I. A coupling enzyme can produce citrulline as an assay readout,
which does not by itself establish physiological CAD participation in that process.
Both normal caches are now available and were read. The DHOase role concerns the
second ring-opening step after dihydropyrimidinase makes the B/C intermediates,
not the first dexrazoxane ring opening. The complete original Methods remain
uninspected; no direct human drug-metabolism assay is claimed.

Broad, correct activity/process labels are refined where a directly supported
specific term is available. Existing UTP/CTP/UDP pathway assertions are retained
as broader metabolic context without assigning terminal nucleotide-kinase or CTP
synthase chemistry to CAD. The nucleoside row remains distinct from nucleotide
biosynthesis. The local GO-CAM index has no exact P27708 activity entry; this is
not evidence of a curation gap. No NEW process or molecular function is proposed,
so no missing-term claim is made from comparator absence. Each core uses the
already-established de novo UMP pathway and its own catalytic activity.

### Completed assessment and validation

The five normal papers PMID:11986331, PMID:23429703, PMID:28007989, PMID:31997698
and PMID:32461667 have been imported without overwriting prior caches. Complete
available abstracts were read. For PMID:23429703, all main narrative paragraphs
were read, but the supplemental Methods/figures were not available in the cache.
For PMID:32461667, unique Methods, relevant Results, captions and Discussion were
read; original images and supplementary data were not inspected. The 2017 clinical,
2020 localization and 2002 autophosphorylation caches remain abstract-only.

The insulin and starvation assertions now have specific non-core support from
PMID:23429703. The main text reports CAD phosphorylation and regulated pyrimidine
flux, including suppression by amino-acid starvation. This does not identify CAD
as a nutrient sensor, and the exact starvation supplement/model remains unread.
An independent bounded annotation-reviewer consultation agreed with these two
judgments and the directional CAD–RAD9A binding interpretation.

For the enzyme-binding annotation, the separate official abstract of
[PMID:10713044](https://pubmed.ncbi.nlm.nih.gov/10713044/) reports human RAD9
expressed in E. coli, purified and characterized as a 3-prime-to-5-prime exonuclease.
That external abstract, rather than the CAD–RAD9A association paper, is the
inspected basis for the partner enzyme premise. No full Methods were read and no
normal cache was generated for it. The existing annotation retains curator
deference; no new or more specific CAD function depends on this external paper.

All 84 source assertions are preserved, with 28 ACCEPT,
26 KEEP_AS_NON_CORE, 10 MODIFY and 20 UNDECIDED. The normal full candidate
validation passed with three generic-binding policy warnings, consistent with the
standing instruction to retain supported generic binding as non-core. Status is
DRAFT. The 87 legacy quotation instances were replaced with eleven selected short
anchors, including one exact legacy quote retained; maximum aggregate quoted words
per source, counting repeated uses, is 16. The three additional donor sources
PMID:18515330, PMID:7053379 and PMID:1673139 were imported and their complete
available abstracts read. There are 31 assessed references and three catalytic
cores; no new annotation or structured isoform field was manufactured. The twenty
unresolved assertions record biological or source-access limits despite completion
of the review. Canonical authored application and publication require the separate
independent review step; existing source files and earlier notes remain unchanged.

## 2026-10-04: response and pathway follow-up

This focused reassessment preserves all 84 machine assertions, their rat donor identifiers, the biological description and the three catalytic cores. The historical MGI/RGD graph remains a March 2023 view, not a verified reconstruction of the current Ensembl transfer. An IEP label does not establish that an experiment measured only transcripts or passive expression; the newly inspected amine and caffeine abstracts report enzyme activities.

The citrulline annotation is changed to MARK_AS_OVER_ANNOTATED. The normal CPS II abstract (PMID:7053379) separates the enzyme from CPS I. The inspected primary indexed Methods passage describes an added bacterial ornithine carbamoyltransferase in the activity assay. Producing citrulline through that coupling reaction does not establish physiological CAD participation in L-citrulline biosynthesis. Human CAD channels cytosolic carbamoyl phosphate to its own ATCase, whereas physiological ornithine-to-citrulline synthesis uses mitochondrial OTC. This interpretation combines the assay context and compartmentalized reactions; it neither disputes measured CPS II activity nor claims that pathological metabolite exchange is impossible. The full original assay protocol and the curator's original reasoning remain uninspected. The [official GO definition and parents](https://amigo.geneontology.org/amigo/term/GO:0019240) describe amino-acid formation, distinct from the laboratory detection of CPS activity.

The pyrimidine-nucleoside biosynthesis annotation is refined to the already represented de novo UMP pathway, GO:0044205. CAD contributes its initial catalytic steps; DHODH and UMPS then act through orotate and OMP to UMP. Free nucleoside production is a different metabolic branch. The replacement does not assign the terminal UMPS reaction to CAD and is not a NEW annotation.

Eight other donor-context decisions remain UNDECIDED after individual source checks. Their limits are recorded below; none is dismissed merely because it was transferred from rat or assigned with IEP.

| Context | Historical donor source | Inspected evidence and remaining limit |
| --- | --- | --- |
| Liver and heart development | PMID:14160653 | Official record has no abstract; publisher preview describes ATCase tissue distribution but does not expose the developmental experiment. Adult-heart activity does not settle heart development. Independent CPS II activity in differentiating liver (PMID:7053379) does not resolve the exact developmental contribution. |
| Pregnancy | PMID:6020217 | Verified mammary-gland ATCase/nucleic-acid bibliographic identity; abstract/body unavailable, so the relationship between enzyme activity and the pregnancy process remains unresolved. |
| Lactation | PMID:1476792 | Historical graph attaches both lactation IEP and pyrimidine-biosynthesis IDA to this source. The abstract/body was not recovered; assay tissue and functional coupling remain unverified. |
| Regeneration | PMID:13671431 | Primary record has no abstract and the donor experiment was not inspected. Independent elevated rat liver CPS II activity (PMID:7053379) is compatible with growth but does not resolve regeneration-specific participation. |
| Testosterone response | PMID:6030068 | Official mammary-tumour bibliographic indexing includes testosterone. Exact hormone treatment and CAD-associated activity results remain inaccessible. |
| Cortisol response | PMID:2353918 | The primary abstract/body was not recovered, leaving the treatment, tissue and CAD readout unresolved. |
| Xenobiotic response | PMID:8548770 | Complete official indexed abstract reports cyclin-D1-associated CAD gene amplification in rat liver epithelial cells. The uninspected selection protocol does not distinguish functional dosage-mediated adaptation from CAD as a selected genomic marker. |

Those uncached donor identifiers are access/provenance pointers in this notes table, not positive reference anchors in the YAML. No whole-paper reading, original figure inspection or exact current donor-snapshot reconstruction is claimed.

The two additional normal abstracts resolve the amine and caffeine decisions to KEEP_AS_NON_CORE. PMID:2864015 measures rat hepatic enzyme activities after dimethylnitrosamine exposure, including the CPS II/ATCase/DHO pathway; PMID:6149265 reports increased rat-brain ATCase and DHO activities following high caffeine intake. These are activity responses, not proof of CAD-mediated drug degradation, and neither is presented as a measured human treatment response. The original Ensembl donor fields remain unchanged. Full protocols, individual data and figures were not inspected.

The final 84-source decisions are 28 ACCEPT, 28 KEEP_AS_NON_CORE, 11 MODIFY, 16 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED. Twelve reviews changed, with four action changes; all other decisions, description, three cores and machine fields remain exact. Two new reference assessments bring the bibliography to 33. The two new verbatim anchors contain 14 and 24 words respectively, each used once. No existing quotation was removed or changed.
