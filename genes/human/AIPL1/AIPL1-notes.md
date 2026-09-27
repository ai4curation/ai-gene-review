# AIPL1 notes

## 2026-06-03 Proteostasis PN review

- Deep research status: `just deep-research-falcon human AIPL1 --fallback perplexity-lite` was attempted. Falcon timed out after 600 seconds, then the Perplexity-lite fallback failed with a quota/401 error. No provider-generated deep-research file was created, so this review proceeds from cached GOA, UniProt, PN projection files, and cached primary literature.

- PN projection context: `projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv` projects AIPL1 to `GO:0031072 heat shock protein binding` via the HSP70-HSP90 joint cochaperone class, and also shows `GO:0003755 peptidyl-prolyl cis-trans isomerase activity` as already in GOA through the FKBP-type PPIase branch. The review accepts the direction of the HSP90/co-chaperone projection but recommends the narrower, gene-supported `GO:0051879 Hsp90 protein binding` rather than the broad `GO:0031072`. The PPIase annotation is removed because AIPL1-specific evidence contradicts catalytic PPIase activity.

- AIPL1 is a photoreceptor/pineal protein with TPR motifs. The original gene paper describes "a new photoreceptor/pineal-expressed gene, AIPL1" and says its protein has "three tetratricopeptide (TPR) motifs" [PMID:10615133 "photoreceptor/pineal-expressed gene, AIPL1" / "three tetratricopeptide (TPR) motifs"].

- AIPL1 is present in human photoreceptors and interacts with NUB1, but this NUB1 binding is not the core PN proteostasis function. Akey et al. verified the interaction by co-immunoprecipitation and found AIPL1 in developing and adult photoreceptors [PMID:12374762 "The AIPL1-NUB1 interaction was verified by co-immunoprecipitation studies in Y79 retinoblastoma cells" / "AIPL1 is present in the developing photoreceptor layer of the human retina and within the photoreceptors of the adult retina"].

- Farnesyl/prenyl binding is a real AIPL1 function. Ramamurthy et al. showed that "AIPL1 interacts specifically with farnesylated proteins" and "AIPL1 enhances the processing of farnesylated proteins" [PMID:14555765]. Majumder et al. later mapped this to the FKBP-like domain, stating that "farnesylated-Cys binds exclusively to the FKBP domain of AIPL1" [PMID:23737531].

- Keep farnesyl/prenyl binding separate from the HSP90-dependent PDE6 maturation core function. Yadav et al. show that prenyl-binding-deficient AIPL1 retains co-chaperone activity and conclude that prenyl modification sequestration is not required for PDE6 maturation [PMID:35065964 "neither sequestration of the prenyl modifications is required for PDE6 maturation to proceed"].

- The FKBP-like domain should not be curated as PPIase activity. Majumder et al. state that "the FKBP domain of AIPL1 does not bind FK506 or exhibit peptidylprolylisomerase activity" [PMID:23737531]. This directly argues against retaining the InterPro/PN PPIase transfer.

- The strongest PN-relevant function is AIPL1-HSP90 co-chaperone activity for PDE6 maturation. Yadav et al. report that AIPL1 "preferentially binds to HSP90 in the closed state with a stoichiometry of 1:2" and that "Disruption of the AIPL1 interaction with HSP90 impedes maturation of PDE6" [PMID:35065964]. Sacristan-Reviriego et al. also describe AIPL1 as a "photoreceptor-specific co-chaperone that interacts with the molecular chaperone HSP90" [PMID:28973376].

- High-throughput generic protein-binding rows should not drive core function. The TINF2 row comes from a telomere interactome screen over about 12,000 proteins [PMID:21044950 "we identified over 300 proteins that associated with the six core telomeric proteins"]. The HuRI rows come from a genome-scale binary interactome resource whose paper notes that "the cellular function of most individual PPIs remains to be elucidated" [PMID:32296183]. These are useful interaction-screen records but not evidence for a core AIPL1 PN role.

## Falcon deep research findings (2026-06-07)

The Falcon (Edison Scientific) report largely confirms the existing PDE6 co-chaperone-centric review. Key NEW items vs the existing review:

- FAT10/NUB1 proteostasis axis (genuinely new mechanistic primary study, not previously cited). Boehm et al. show that FAT10 (a cytokine-inducible ubiquitin-like modifier) is conjugated to rod PDE6 and targets it for proteasomal degradation, while also non-covalently inhibiting PDE6 cGMP hydrolysis; AIPL1 stabilizes the FAT10 monomer and the PDE6-FAT10 conjugate, and FAT10 binds AIPL1 TPR motifs [PMID:32817338 "AIPL1 interacts with the cytokine-inducible ubiquitin-like modifier FAT10" / "We found that AIPL1 stabilizes the FAT10 monomer and the PDE6-FAT10 conjugate" (doi:10.1074/jbc.RA120.013873)]. This gives mechanistic meaning to the existing (otherwise generic) AIPL1-NUB1 protein-binding annotation, connecting AIPL1 to inflammation-linked PDE6 proteostasis. I did NOT change any annotation action on this basis since it does not contradict existing calls; added as a reference and a suggested question.

- Prenylation as a molecular-recognition element (prenyl-dependent assembly model). The 2024 prenylation review frames PDE6 prenylation not merely as a membrane anchor but as a recognition feature that enables AIPL1 FKBP-domain binding and stable AIPL1-HSP90-PDE6 ternary complex formation; rod PDE6A is farnesylated, PDE6B/cone PDE6 geranylgeranylated [Ashok & Rao 2024, doi:10.3389/fopht.2024.1410874, review]. Consistent with the existing review; note the existing review (citing PMID:35065964) holds that prenyl sequestration is NOT strictly required for PDE6 maturation, so this remains an open mechanistic point. Review-level, not used to change annotations.

- 2024 human iPSC retinal-organoid gene-replacement study (new primary translational evidence). AAV-mediated AIPL1 replacement rescued loss of rod PDE6 and normalized elevated cGMP in AIPL1-KO and patient LCA4 organoids, with PDE6 transcripts unchanged - i.e. a post-transcriptional/proteostasis rescue, independently supporting AIPL1's chaperone (not transcriptional) mechanism [PMID:38439910 "the loss of retinal phosphodiesterase 6 was rescued and elevated cyclic guanosine monophosphate (cGMP) levels were reduced following treatment" (doi:10.1016/j.omtn.2024.102148)]. Reinforces visual perception / protein maturation annotations; added as reference.

- Localization refinement (review-level, low weight). AIPL1 is placed mainly along the synapse-to-inner-segment/connecting-cilium axis, favoring a PDE6 maturation/assembly role rather than direct outer-segment trafficking; adult human retina shows strongest detection in rods with developmental expression also in cones, yet AIPL1 remains important for cone viability [galieva2025 / ashok2024, reviews]. Coherent with existing GO:0001917 photoreceptor inner segment ACCEPT; no change.

- Clinical/translational context (not annotation-relevant). 2024 LCA cohort: AIPL1 variants in 4/52 (7.7%) children, recurrent c.421C>T p.Q141X [Zhou et al. 2024, doi:10.1007/s00417-024-06450-9]; active early-phase trial NCT07063030 (LX107 subretinal gene therapy for AIPL1-IRD). Background only; not used for GO annotations.

- Recent review: Galieva, Karabelsky & Egorov 2025, "Restoring Sight: The Journey of AIPL1 from Discovery to Therapy" [PMID:41465493, doi:10.3390/ijms262412066] - synthesizes AIPL1 as a unique FKBP-family member essential for PDE6, useful secondary reference.

PMIDs confirmed via PubMed ID conversion (DOI->PMID): Boehm 2020 = PMID:32817338; Sai 2024 = PMID:38439910; Galieva 2025 = PMID:41465493; Ashok 2024 = PMID:39026984; Zhou 2024 = PMID:38662103.

## 2026-09-27 ClinGen Mendelian substantive audit

### Baseline, identity and source integrity

HGNC:359 is Approved AIPL1, with previous symbol LCA4 in the authoritative
project HGNC snapshot. The immutable UniProt record is Q9NZN9; AIPL2 appears
there as an alternative-product synonym, not a different gene used in this
review. All nine gene files were independently byte-verified against current
main `23787fa952f4d41c0b92795752e367b2d9a207b1` before editing. The root's
canonical/LCA4 open-PR searches were empty, with no historical-symbol directory
conflict. There are 13 machine-seeded review objects plus one earlier author-
proposed HSP90-binding row, 17 reference identities and five alternative products.
The HuRI object groups four original interaction tuples; that grouping is
preserved. No source GOA, UniProt, original Falcon report/artifacts or generated
PN note was edited. No cached GO-CAM index hit for Q9NZN9 was found, and this
seed contains no IBA annotation. The sole ortholog transfer was traced as such.

### Genuine research and publication attempts

The standard deep-research wrapper was invoked with Falcon and fallback
perplexity-lite, a 1,200-second provider timeout, the actual UniProt context,
and a fresh `/tmp/AIPL1-fresh-research/AIPL1` output directory. This preserved
the genuine 2026-06-07 Falcon report and its artifacts. Both new attempts failed
before provider execution because `uvx` could not resolve PyPI while obtaining
`deep-research-client[cyberian]==0.2.7rc1`; each exited 2 and the wrapper exited 1.
No new provider report was created. The per-process UV tool/bin/cache directories
were the authorized writable `/tmp/aigr-uv-*` paths. Failure log:
`/tmp/AIPL1-fresh-research.log`. Manual source review below is not provider output.

Publication caching ran concurrently: all 12 YAML PMIDs were already cached.
The normal additional fetch of the two existing notes citations, PMID:38662103
and PMID:39026984, failed DNS with 0/2 records recovered. These remain the
notes-inclusive cache gates. Their identities were independently verified on
[PubMed 38662103](https://pubmed.ncbi.nlm.nih.gov/38662103/) and
[PubMed 39026984](https://pubmed.ncbi.nlm.nih.gov/39026984/): the former is the
LCA cohort and the latter the prenylation review already discussed above.
They are background citations, not the basis for a new molecular annotation.
No machine publication was manually rewritten or fabricated.

### Direct localization and propagation provenance

The original [human AIPL1/NUB1 publication](https://pubmed.ncbi.nlm.nih.gov/12374762/)
exposes Figure 6 on PubMed. Its caption explicitly identifies nuclear staining
in differentiating human photoreceptors at fetal weeks 14 and 16, and ONL/inner-
segment staining in child and adult retina. Thus the nuclear rows are supported
positive observations, retained as developmental context rather than rejected
because the main molecular function is cytoplasmic. Nuclear transport remains
only a motif-based proposal in the discovery abstract [PMID:10615133]. The
original PMID:12374762 record lists an erratum whose content was not recovered;
no scientific correction, invalidation or retraction is inferred from that notice.
Its publication cache is still abstract-only despite the external figure access.

The cytoplasm vocabulary source is UniProtKB-SubCell:SL-0086, and the nuclear
source is SL-0191, both with the cached UniProt PMID:12374762 attribution. The
inner-segment transfer names mouse Aipl1 Q924K1 and ENSMUSP00000036279. The
[historical MGI comparative graph](https://www.informatics.jax.org/GOgraphs/OrthoDisease/GeneGraphs/AIPL1.html),
generated 2007-12-07, traces the mouse IDA to PMID:14555765. That paper's mouse
retinal staining and the independent human Figure 6 support conservation. No
donor-count or circular-self-support argument is used.

### Chemistry and the farnesylation-process boundary

The InterPro source for the PPIase IEA is IPR046357. The domain is real, but
PMID:23737531 explicitly reports lack of PPIase activity, citing earlier work,
and maps farnesyl recognition to the FKBP-like domain. The full cached
PMID:35065964 Discussion agrees that this is a non-isomerase co-chaperone.
The catalytic annotation remains REMOVE. This does not imply that the 2013
paper itself performed a new negative PPIase assay or that its partially
extracted cache contains the omitted Methods/Results.

The [full original farnesyl-client paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC240669/)
was recovered through indexed primary text. The farnesyl-binding evidence uses
nonprenylatable client mutants and farnesyltransferase-deficient yeast. In the
HEK293 processing experiment (Figure 3), AIPL1 increases the faster-migrating
DNAJA2 species approximately 2.5-fold; the Cys-to-Ser client and AIP provide
controls, and AIPL1 disease variants alter this effect (Figure 5). The authors
leave the affected step unresolved: lipid attachment, later ER processing,
trafficking, or protection of a processed client are considered. The live AmiGO
GO:0018343 definition is covalent attachment of a farnesyl group. A noncatalytic
chaperone/cofactor can participate, so absence of transferase catalysis is not
a sufficient reason to reject participation. Conversely, the mobility assay
does not isolate that chemical step. The exact process becomes UNDECIDED;
the earlier MODIFY-to-maturation rationale claiming proven downstream-only
action is superseded. The source ID, evidence and original qualifier remain
unchanged. Independent read-only consultation by annotation_a4galt confirmed
this assay/interpretation boundary.

The current ontology was also inspected through the existing local OAK GO
adapter: GO:0051604 covers attainment of a protein's full functional capacity;
GO:0051879 specifies HSP90 binding; GO:0001918 specifies farnesylated-protein
binding. No obsolete-term claim or invented identifier is used.

### Human and mouse HSP90 evidence

The full cached PMID:35065964 Methods explicitly use **mouse AIPL1**, recombinant
human HSP90β, and human PDE6C in HEK293T cells; the PDE6A-farnesylation mutant
animal is mouse. Its activity readout is direct cGMP hydrolysis after removal
of the inhibitory PDE6 subunit. This is strong mechanistic ortholog evidence,
but cannot itself be labeled a direct human AIPL1 IDA. It also shows productive
maturation of unprenylated PDE6C and with a prenyl-binding-deficient AIPL1
variant. These are bounded systems, not proof that prenyl recognition has no
physiological role. The paper itself discusses a possible kinetic contribution.

The [original human AIPL1 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5886190/)
[PMID:28973376] was recovered as indexed primary Results/Figures 3–5 and
Discussion. Reciprocal co-IP, directed interaction assays and quantitative
ELISA with human HSP90α/β support human AIPL1 binding. The sole prior NEW row
therefore retains GO:0051879 but corrects its **author-generated** reference
and evidence from PMID:35065964/IDA to PMID:28973376/IPI; the former remains
corroborating evidence. None of the 13 machine-seeded source objects is changed.
The human study's cellular cGMP abundance readouts are distinguished from the
later direct hydrolysis assay. Its
[publisher correction](https://doi.org/10.1093/hmg/ddy024) adds two omitted
co-authors and does not change a scientific result. The local 2017 cache remains
abstract-only despite external primary access.

No new process assertion is added. The existing specific HSP90-binding proposal
is supported by direct human interaction evidence and is distinct from the
farnesylated-client binding activity; rejected generic protein-binding rows do
not supply a retained redundant ancestor. The two complementary core activities
are described in positive biological terms. Core protein maturation is supported
by the human and mouse experiments even though the original farnesylation row
is now unresolved; a possible validator coverage advisory is accepted rather
than forcing that row into an unrelated replacement. No additional broad heat-
shock-binding, folding-process, proteolysis or retinal-survival NEW is asserted.

### Interaction screens and reference coherence

NUB1 binding in PMID:12374762 is directly supported, including human Y79 co-IP.
The annotation's generic protein-binding term is removed as uninformative, not
as a denial of that interaction. The separate FAT10/PDE6 findings in
PMID:32817338 do not by themselves define an NUB1-specific molecular activity.
The TINF2 split-YFP row and HuRI group receive the same generic-binding action.
The source partners are retained in the rationale: TINF2 Q9BSI4; LBX1 P52954,
SMAP1 Q8IYB5-2, PLSCR3 Q9NRY6 and TXNL4B Q9NX01. Their pair-level supplementary
validation was not reconstructed. No telomere mechanism, absence of interaction,
or assumed misattribution is inferred from that limitation.

All 17 references received source-specific assessments. Local availability flags
reflect actual caches: PMID:21044950 and PMID:23737531 have cached full-text
sections and remain `full_text_unavailable: false`, with their missing Results/
Methods sections explicitly noted. Abstract-only entries remain true, including
PMID:32817338's nonstandard cache. Original identifiers/titles are preserved.
The 2024 organoid study [PMID:38439910] supports post-transcriptional rescue of
PDE6 and cGMP phenotypes in human cells, but its models did not show overt
photoreceptor degeneration; that absent phenotype is not claimed as rescued.
The 2018 and 2025 reviews are secondary corroboration, not substitute primary
assays [PMID:29721967; PMID:41465493]. The PN projection file was read for
provenance and is retained as such; it is not experimental evidence.

### Handoff checks

The frozen manifest records targeted validation, history validation, normal HTML
rendering, source/isoform preservation, exact case-sensitive whitespace-normalized
quotes, notes-inclusive cache census and file hashes. DRAFT is used while the
two notes-only cache gates and any documented validation advisories remain.
The dated earlier notes remain historical provenance; the current source scopes
and decisions above supersede their broader mechanistic interpretations.

The early HSP90 yeast-interaction test in PMID:14555765 was negative. This
assay-specific result is retained in the source assessment alongside the later
positive human co-IP and ELISA experiments in PMID:28973376; the evidence is not
presented as uniformly positive across all methods. It does not alter the
source-corrected HSP90-binding proposal.

The parent independently read all 14 decisions, both cores and the questions,
and accepted the biological draft. A separate bounded peer read of the original
farnesyl-processing experiments agreed that the exact affected processing step
is unresolved. Final targeted validation passed with two intentional advisories
(unreferenced historical provider report and core protein-maturation coverage);
history validation and normal rendering passed.


## 2026-09-27 PR feedback: processing scope and localization trail

The [current review](https://github.com/ai4curation/ai-gene-review/pull/3257#issuecomment-5853253376)
was checked against the original sources and live GO definitions. The
[2003 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC240669/) uses human AIPL1 and
human DNAJA2 constructs. Its mobility assay and mutant controls establish increased
client processing, while the exact affected CAAX-processing step is unresolved.
The corresponding assertion now uses MODIFY to [protein maturation](https://amigo.geneontology.org/amigo/term/GO:0051604),
which accommodates the measured assistance without choosing a specific chemical
step. The source IDA and acts_upstream_of_or_within qualifier remain unchanged.
This also provides an actionable counterpart for the existing maturation core.
No new annotation is added. Visual perception is retained as a supported non-core
physiological consequence; the direct core process is client maturation.

The [original localization Results and Figure 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC2585502/)
were recovered and checked for human fetal, child and adult retinal material.
The nuclear and inner-segment rows now separate their external compartment-specific
Results from the abstract-only local record. Their short external quotations are
marked supporting_text_fulltext; the actual local availability flag stays true.
Exact UniProt GO lines supply explicitly identified database corroboration, not
additional primary experiments. File quotations were manually substring-checked;
the standard validator does not validate file-reference quotations. Actions for
these location rows are unchanged, and curator evidence is retained.

The co-chaperone activity remains explicit in positive biological prose. A new
question distinguishes active protein-folding assistance from generic unfolded-
protein binding and holdase activity before proposing an additional human MF.
The existing HSP90-binding term remains grounded in the direct human experiments;
no complex identifier or autonomous folding activity was inferred from a binding
result alone. Historical UniProt-only GO terms are outside the preserved GOA seed
and are not silently added. The two notes-only source4 cache gates remain pending;
removing their provenance or treating an earlier COMPLETE status as proof of the
current review's completion would not resolve those access limits.

A bounded independent peer read found no biological blocker in these changes.
Targeted validation passes with one intentional unused-provider advisory; the
previous core-process-coverage advisory is resolved. History, rendering and
source/isoform/reference preservation checks pass. The source4 cache gates
remain PMID:38662103 and PMID:39026984.
