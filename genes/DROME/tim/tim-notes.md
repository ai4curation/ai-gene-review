# tim (timeless, FBgn0014396, UniProtKB:P49021) review notes

Date: 2026-11-16. De-novo review for the MOD descriptions project (IBA-novel batch).

## Sources used

- FlyBase hand-written description (`tim-deep-research-flybase.md`), UniProt P49021, GOA (66 rows).
- No Falcon/Perplexity deep research (no API keys). Literature searched with WebSearch and PubMed
  E-utilities; queries recorded below.
- PANTHER 19.0 tree for PTHR22940 and the PAINT IBD.gaf snapshot, analysed in
  `tim-bioinformatics/RESULTS.md`.
- QuickGO's `includeFields=taxonName` returned HTTP 500 on 2026-11-16 (its taxonomy backend refused
  connections), so `just fetch-gene` wrote an empty GOA file. I re-ran the fetch through a wrapper that
  drops that one include field and fills the taxon name from the taxon id (7227); all other columns are
  as QuickGO served them.

## Literature queries run

- WebSearch: "Drosophila timeless tim DNA replication checkpoint timeout tim-2 chromosome stability Benna 2010"
- WebSearch: "Drosophila "timeless" tim1 mutant DNA replication follicle cell amplification OR S phase OR endocycle"
- FlyBase gene report FBgn0014396 (read online) for the source of "DNA replication": the only
  replication-related items are the four PAINT IBA rows (FBrf0258542, GO Reference Genome Project);
  no phenotype or paper on DNA replication is listed.
- PubMed E-utilities: Benna 2010 timeless2 (PMID:20153199), Gotter 2000 mouse Tim (PMID:10903565),
  Rubin 2006 honey bee clock (PMID:17065608), Sehgal 1994 (PMID:8128246), Darlington 1998 (PMID:9616122),
  Koh 2006 JETLAG (PMID:16794082).

## Core biology

- TIM was cloned as a PER-binding protein; a segment of TIM binds the PER PAS region
  [PMID:7481773 "A restricted segment of TIM binds directly to a part of the PER dimerization domain PAS."].
- tim null mutants are arrhythmic for eclosion and locomotor activity
  [PMID:8128246 "a clock mutation, timeless (tim), is described that produces arrhythmia for both behaviors"],
  and PER fails to enter the nucleus in tim mutants
  [PMID:8128247 "the nuclear localization of PER is blocked by timeless (tim)"].
- tim RNA cycles with per and is under PER/TIM feedback
  [PMID:7481772 "The tim RNA oscillations were found to be dependent on the presence of PER and TIM proteins"].
- CLK-CYC activate per and tim; PER and TIM block CLK transactivation
  [PMID:9616122 "PERIOD and TIMELESS proteins blocked dCLOCK's ability to transactivate their promoters via the E-box."].
  But nuclear TIM alone does not repress
  [PMID:12944510 "Unlike PER, nuclear TIM alone has no ability to repress transcription."]; its main
  role is to stabilise PER and set the timing of its nuclear entry
  [PMID:12944510 "We propose that TIM drives cycles of PER expression by regulating its stability"].
- PER-TIM binding and nuclear entry timing in S2 cells
  [PMID:16410523 "these proteins bind rapidly and persist in the cytoplasm while gradually accumulating in discrete foci"].
- Light input: TIM is rapidly degraded by light
  [PMID:8625406 "the expression of TIM, but not PER, is rapidly reduced by light, suggesting that TIM mediates light-induced resetting of the circadian clock"];
  CRY binds TIM in a light-dependent way
  [PMID:10417378 "CRY and TIM are part of the same complex and directly interact in yeast in a light-dependent fashion."];
  the F-box protein JET targets TIM for degradation
  [PMID:16794082 "Expression of JET along with the circadian photoreceptor cryptochrome (CRY) in cultured S2R cells confers light-dependent degradation onto TIM"].
  The TIM light response is relevant to phase shifts [PMID:9697866].
- Natural ls-tim/s-tim polymorphism affects diapause and light sensitivity [PMID:17600215, PMID:17068124].
- Outputs that need tim: mating activity rhythm [PMID:11470898], male copulation duration (clock
  independent) [PMID:15324667], night-time peak of phagocytosis [PMID:22253593], temperature preference
  rhythm [PMID:22981774], cardiac function under time-restricted feeding [PMID:25766238], larval
  light avoidance [PMID:19285485], sleep [PMID:12015603, PMID:16938867, PMID:25148297, PMID:33078445].

## The DNA replication question (key IBA test)

- Drosophila has two TIMELESS-family genes. tim1 (tim) arose by duplication from tim2 (timeout)
  [PMID:20153199 "Phylogenetic analyses suggest that tim1 originated as a duplication of tim2 around the time of the Cambrian explosion."].
  The single TIMELESS of most organisms is the tim2 type and works in DNA synthesis
  [PMID:20153199 "Many organisms possess a single tim2-like gene that has been implicated in DNA synthesis"].
  Fly tim2 is essential for chromosome integrity
  [PMID:20153199 "tim2 is an essential gene required for normal DNA metabolism and chromosome integrity"].
- Hardin's review noted the second fly tim gene and that mouse Tim may not be the ortholog of fly tim
  [PMID:11178250 "Searching the Drosophila genome database has, however, led to the discovery of another tim gene, thus opening up the possibility that mTim is not the true homolog of the Drosophila tim clock gene [6]."];
  mouse Tim is essential for development
  [PMID:10903565 "mTim is essential for embryonic development, but does not have substantiated circadian function"].
- The tim1-type gene is dispensable for replication across animals: honey bee has no tim1
  [PMID:17065608 "The honey bee genome does not encode an ortholog of Drosophila Timeless (Tim1)"],
  and mammals lost the Drosophila-type set
  [PMID:17065608 "Drosophila diverged from the ancestral insect clock and specialized in using a set of clock gene orthologs that was lost by both mammals and bees"].
- tim null flies (tim01) develop to adults and mate [PMID:8128246, PMID:11470898], unlike loss of a
  replisome TIMELESS (tim2 knockout lethality in flies; mouse Tim essential).
- PANTHER tree (tim-bioinformatics/RESULTS.md): the five replication IBDs sit on the family root
  PTN000533813 (Eukaryota). The tim/timeout duplication is PTN008585095 (below Eumetazoa); fly tim is in
  the SF5 clade PTN008585096 and fly timeout, human TIMELESS and worm tim-1 are in PTN000533822. PAINT
  has no IKR/IRD on the SF5 clade. So fly tim inherits the replication terms only through the
  pre-duplication ancestor, and the biology says the function stayed with the timeout lineage.
- FlyBase "DNA replication": the gene report shows no paper or phenotype for this; the only
  replication items on FlyBase are the four PAINT IBA GO rows. The statement is untraced and most
  likely restates the IBA predictions (or conflates tim with timeout). Recorded as a FlyBase defect.

## Verdicts on the non-duplicative IBA rows

| Term | Action | Short reason |
|---|---|---|
| GO:0031298 replication fork protection complex | REMOVE | root IBD above the tim/timeout duplication; function kept by timeout |
| GO:0043111 replication fork arrest | REMOVE | same |
| GO:0000076 DNA replication checkpoint signaling | REMOVE | same; seeded only by yeast Tof1 |
| GO:0006281 DNA repair | REMOVE | same; seeded only by yeast Tof1 |
| GO:0003677 DNA binding | MARK_AS_OVER_ANNOTATED | HTH_TIMELESS domain kept, but no fly assay and UniProt curators record no DNA binding |

GO:0009649 entrainment of circadian clock (IBA, seeded by tim itself at PTN001118055) is ACCEPTed;
it is not one of the non-duplicative rows (an IMP row exists).

## UniProt FUNCTION text

Accurate for the core clock role. "Nuclear activity of the heterodimer" and "rhythmic formation and
nuclear localization of the TIM-PER complex" follow the 1990s model; later work shows PER and TIM can
enter the nucleus separately [PMID:16410523, PMID:12944510], but the field still describes a complex,
so I did not file a defect.
