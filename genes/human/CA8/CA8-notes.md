# CA8 (P35219) — review journal

## The contested annotation, and the thing that makes this case unusual

GOA carries `GO:0004089` carbonate dehydratase activity **twice**, and I checked the
evidence codes myself in `CA8-goa.tsv`:

| row | evidence | reference | assigned by |
|-----|----------|-----------|-------------|
| `enables GO:0004089` | **IEA** (`ECO:0000256`) | `GO_REF:0000002`, InterPro IPR018338/IPR023561 | InterPro |
| `enables GO:0004089` | **TAS** (`ECO:0000304`) | **PMID:8977131** | PINC |
| `enables GO:0008270` zinc ion binding | **IEA** (`ECO:0000256`) | `GO_REF:0000002`, same InterPro signatures | InterPro |

There is **no IDA, IMP or EXP row for either term** anywhere in the file. So the catalytic
assignment rests on (a) a fold/domain match and (b) a single traceable author statement.

### The TAS contradicts its own source

PMID:8977131 is Sjöblom et al., *FEBS Lett* 1996;398(2-3):322-5,
"Two point mutations convert a catalytically inactive carbonic anhydrase-related protein
(CARP) to an active enzyme", DOI 10.1016/s0014-5793(96)01263-x — verified against PubMed,
abstract-only in cache (`full_text_available: false`).

The title alone says it, and the abstract is unambiguous:
[PMID:8977131 "While unmodified CARP is catalytically inactive, the mutant catalyzes CO2
hydration with a significantly higher efficiency than the mammalian low-activity carbonic
anhydrase isozyme III."]

The whole point of the paper is that you have to **engineer** two substitutions
(Arg117→His, Glu115→Gln) to get activity:
[PMID:8977131 "By introducing two mutations, Arg117 --> His and Glu115 --> Gln, we created
a metal-binding center homologous to that in the carbonic anhydrases from the animal
kingdom."]

And the same sentence that establishes zinc binding establishes it **for the mutant, by
contrast with the wild-type**:
[PMID:8977131 "In contrast to unmodified CARP, this double mutant was isolated as a 1:1
zinc-protein complex."]

So the PINC TAS for `GO:0004089` is a misannotation of the very paper it cites: the source
reports the *absence* of the activity in the wild-type protein. That also disposes of the
`GO:0008270` zinc-ion-binding IEA — unmodified CARP was not isolated as a zinc complex, and
the fold-based signature that produced the IEA is exactly what the experiment refutes.

(The paper works on **murine** CARP, the CA8 ortholog. That is not a problem for the
argument: the human protein has the identical active-site substitution, UniProt flags it,
and PINC used this paper for the human entry in the first place.)

### Independent confirmation that CA8 is acatalytic

- UniProt P35219 `FUNCTION: Does not have a carbonic anhydrase catalytic activity.` and
  `CAUTION: Although it belongs to the alpha-carbonic anhydrase family, Arg-116 is present
  instead of the conserved His which is a zinc-binding residue. It is therefore expected
  that this protein lacks carbonic anhydrase activity.`
- HGNC name: "carbonic anhydrase 8 (**inactive**)".
- [PMID:32316137 "Human carbonic anhydrase 8 (CA-VIII) is an acatalytic isoform of the α
  -CA family."] and [PMID:32316137 "Though the protein cannot hydrate CO2, CA-VIII is
  essential for calcium (Ca2+) homeostasis within the body, and achieves this by
  allosterically inhibiting the binding of inositol 1,4,5-triphosphate (IP3) to the IP3
  receptor type 1 (ITPR1) protein."]
- [PMID:42268453 "However, carbonic anhydrase VIII (CA VIII) represents a catalytically
  inactive member of this family due to the absence of one of the three histidine residues
  required for enzymatic activity"]

**Decision:** `GO:0004089` (both the IEA and the TAS rows — same term must carry the same
action) and `GO:0008270` → **REMOVE**. This is not second-guessing an experimental
annotation: there is no experimental annotation to second-guess, and the one cited paper
says the opposite of what the TAS asserts.

## What CA8 actually does

The fold is retained and repurposed as a protein-interaction surface. The primary finding
is Hirota et al., *Biochem J* 2003 (PMID:12611586, verified; abstract-only in cache):

- [PMID:12611586 "Western blot analysis revealed that CARP is expressed exclusively in
  Purkinje cells of the cerebellum, in which IP(3)R1 is abundantly expressed."]
- [PMID:12611586 "Using deletion mutagenesis, we established that amino acids 45-291 of
  CARP are essential for its association with IP(3)R1, and that the CARP-binding site is
  located within the modulatory domain of IP(3)R1 amino acids 1387-1647."]
- [PMID:12611586 "CARP inhibits IP(3) binding to IP(3)R1 by reducing the affinity of the
  receptor for IP(3)."]

Mechanism, restated by the structural work:
[PMID:32316137 "CA-VIII allosterically inhibits ITPR1 by reducing the receptor’s affinity
for IP3 without altering the maximum number of ligand binding sites."]

The interaction is reciprocally validated from the receptor side by Ando et al., *PNAS*
2018 (PMID:30429331):
[PMID:30429331 "The SCA29 mutation V1538M within the CA8-binding site of IP3R1 completely
eliminated its interaction with CA8 and CA8-mediated IP3R1 inhibition."] and
[PMID:30429331 "Furthermore, pathological mutations in CA8 decreased CA8-mediated
suppression of IP3R1 by reducing protein stability and the interaction with IP3R1."]
This is the strongest part of the case: mutations on *either* side of the interface
converge on the same functional readout.

Disease: recessive CA8 mutations cause cerebellar ataxia (SCAR34 / CAMRQ3).
[PMID:19461874 "We demonstrate that the mutation S100P is associated with
proteasome-mediated degradation, and thus presumably represents a null mutation comparable
to the Ca8 mutation underlying the previously described waddles mouse, which exhibits
ataxia and appendicular dystonia."]

Directionality: CA8 is a **negative** regulator —
[PMID:42268453 "CA VIII is thought to act as a negative regulator of IP3R1, reducing
excessive calcium release and maintaining intracellular calcium homeostasis"], and it acts
on the receptor, not on the ligand:
[PMID:42268453 "Biochemical and functional studies have demonstrated that CA VIII directly
interacts with the modulatory domain of IP3R1 rather than binding IP3 itself, thereby
reducing the sensitivity of IP3R1 to IP3 and influencing calcium release dynamics within
neurons"]

## Choosing the replacement molecular function

IP3R1 (ITPR1) is a ligand-gated intracellular calcium-release channel. CA8 binds it and
reduces its activity. I looked up candidates rather than guessing:

| candidate | verdict |
|---|---|
| `GO:0019855` calcium channel inhibitor activity (MF) — "Binds to and stops, prevents, or reduces the activity of a calcium channel." | **chosen**; the definition is almost a paraphrase of the CA8 result |
| `GO:0005246` calcium channel regulator activity (MF) | correct but less specific — CA8's effect is unidirectional inhibition |
| `GO:0044325` transmembrane transporter binding (MF) | records the binding but drops the functional consequence |
| `GO:0070679` inositol 1,4,5 trisphosphate binding (MF) | **wrong** — CA8 binds the receptor's modulatory domain, not IP3 (PMID:42268453 above) |
| `GO:0051280` negative regulation of release of sequestered calcium ion into cytosol (BP) | **chosen** as the process |

There is no GO term for "IP3 receptor binding" specifically; `GO:0019855` is the most
informative MF available and it is in the molecular_function branch (checked via QuickGO),
so it passes the strict branch validation on `core_functions`.

## Other GOA rows

- `GO:0005515` protein binding × 5 IPI rows (PMIDs 25416956, 25910212, 27107012, 31515488,
  32296183) — all systematic binary-interactome/Y2H screens. Partners are CRX, GGA2,
  HSD17B14, INTS7, KLHL8, LMNB2, LNX1, MAGED1, RAB34, SPDL1, TBX3. **ITPR1 — the one
  partner that carries the biology — does not appear in GOA at all.** Marked
  `MARK_AS_OVER_ANNOTATED` per project guidance (same action on every row of the same
  term).
- `GO:0005737` cytoplasm (IEA, `GO_REF:0000107`, Ensembl Compara from mouse P28651) —
  ACCEPT. CA8 is a soluble cytosolic protein engaging the cytoplasmic modulatory domain of
  an ER-membrane channel; nothing more specific is supported.

## Honest uncertainties

- **Is CA8 a *complete* pseudoenzyme, or does it retain a vestigial/alternative activity?**
  The literature is uniform that it cannot hydrate CO2, but "no measurable CA activity" is
  not the same as "no catalytic activity of any kind", and no one has screened for one.
- **Quantitative stoichiometry and affinity of the CA8–IP3R1 interaction** are not
  established in a purified reconstituted system, so the "inhibitor" call rests on
  IP3-binding assays and cell-based calcium readouts rather than on single-channel
  recordings.
- **Non-neural roles.** The 2026 review notes reported roles in tumour progression and
  metabolic regulation but calls them less well characterised; I did not annotate them.
- PMID:26399641 reports CA8 overexpression stunting Purkinje dendritic growth *without*
  detectable direct binding to IP3R1 in that system — a dissenting data point on the
  universality of the interaction. Noted; it does not overturn the two reciprocal
  mutational studies, but it belongs in the record.

## Validation notes

- `references:` titles filled with `fill_refs.py`.
- All `supporting_text` verified as normalised verbatim substrings of the cached
  `publications/PMID_*.md` files.
- GO ids for `core_functions` (`GO:0019855`, `GO:0051280`, `GO:0005737`) and the CL id
  `CL:0000121` Purkinje cell were each looked up (QuickGO / OLS), not written from memory.


## 2026-10-03: source-complete reassessment

The September review and its history are preserved above as historical evidence. This reassessment supersedes its generic-binding removals, its implication that the former catalytic cavity is an experimentally established ITPR1 interface, and any transfer of mouse construct numbering to the 290-residue human protein.

The existing normal GOA file contains 26 assertions. The earlier YAML collapsed these into nine source/reference groups, omitting individual partners. Running the normal seeder in an isolated temporary output restored 17 additional partner records and backfilled source metadata in eight retained rows. All nine older source groups remain represented, and each of the 26 raw assertions maps to exactly one restored source object. This is restoration of machine source assertions, not 17 scientifically proposed NEW annotations. The two pre-existing authored NEW annotations are retained after independent mechanistic and ontology review; no additional NEW is proposed. Raw UniProt, GOA, publication caches and the earlier history are unchanged. There is no alternative-products slot to manufacture or infer.

The final direction is three REMOVE decisions for the unsupported wild-type catalytic/zinc-site assignments, 22 KEEP_AS_NON_CORE interaction assertions, one ACCEPT for cytoplasm, and the two retained NEW proposals for channel inhibition and direct negative regulation of calcium release. Supported generic binding is kept under the [standing project instruction](../../../projects/CLINGEN_MENDELIAN.md); limited informativeness alone is not a biological reason to remove it. The distinct binding consultation read all five source abstracts and available assay-framework passages, and corroborated all 22 literal partners against the human UniProt interaction list. It did not inspect individual CA8 supplemental target cells or claim that every pair received orthogonal or native-context validation. In particular, KLHL8 remains the literal UniProtKB:Q9P2G9-2 product. None of these partners is presumed to mediate ITPR1 inhibition.

For PMID:25416956 and PMID:25910212, the HTML caches contain Abstract and Introduction/Discussion, without the target Results/table. PMID:27107012 provides the barcode-fusion yeast-two-hybrid framework; PMID:31515488 describes Y2H screening and selected human-293T PCA validation; PMID:32296183 describes HuRI screening and retesting. Those framework results support qualified curator deference, not a claim that the CA8-specific supplemental results were personally verified. The consultant's reference-only recommendations were joined to the exact raw records; no new quotations were assigned to these rows.

### Mechanism and source boundaries

- [PMID:8977131](https://pubmed.ncbi.nlm.nih.gov/8977131/): the complete normal abstract explicitly distinguishes catalytically inactive recombinant murine CARP from an engineered double mutant that acquires zinc-dependent carbon dioxide hydration. The human sequence has the corresponding canonical zinc-ligand replacement, Arg116. The active engineered product does not establish native human carbonate dehydratase activity. The zinc-site conclusion does not assert that CA8 can never contact zinc under any condition.
- [PMID:12611586](https://pubmed.ncbi.nlm.nih.gov/12611586/): the complete abstract describes the mouse-brain library interaction, mapping and reduced IP3 affinity. Its nominal Full Text section repeats that abstract; detailed Methods are unavailable. The cited mouse 45–291 segment is not presented as a 291-residue human construct. CA8 regulates the channel; ITPR1 supplies the pore.
- [PMID:19461874](https://pubmed.ncbi.nlm.nih.gov/19461874/): the complete abstract and selected unique Methods/Results were read. Human fibroblast-derived CA8 and ITPR1 regulatory fragment were expressed using baculovirus/Sf9 and tested by blot overlay. Stable human CA8 expression in HEK cells supports S100P destabilization with partial proteasome-inhibitor rescue. The blot-overlay assay found no WT/S100P binding difference, so instability is not conflated with universal loss of intrinsic affinity. Figures and all supplementary clinical material were not inspected.
- [PMID:30429331](https://pubmed.ncbi.nlm.nih.gov/30429331/): the normal cache contains Abstract and Discussion, plus a supplementary-Methods pointer, despite its positive full-text flag. Additional indexed official PMC Results and Figure 4 text describe receptor-defined HeLa experiments, pulldown/co-IP and calcium imaging. CA8 binds IP3R1 and IP3R2, but functionally inhibits IP3R1 in these assays; it does not bind or inhibit IP3R3. Detailed supplementary construct provenance and figure images were not fully recovered. The G162R binding effect and the S100P stability result are not made interchangeable.
- [PMID:32316137](https://pubmed.ncbi.nlm.nih.gov/32316137/): the complete abstract and selected unique structural/computational sections were read. SiteMap, CPORT and molecular dynamics identify possible surfaces and 38 predicted contacts. They do not experimentally resolve the CA8–ITPR1 interface. The 2026 review [PMID:42268453](https://pubmed.ncbi.nlm.nih.gov/42268453/) is contextual synthesis, not an additional direct assay of cavity repurposing or a separate scaffold function.

The one integrated core links CA8's own calcium-channel inhibitor activity to negative regulation of release from intracellular stores. CA8 supplies regulatory work itself; it is not the transported calcium, pore, or a merely necessary cargo. The existing process proposal was checked against its regulation/transport parents. A local comparator check found the more specific GO:0060315 child on the noncatalytic channel regulator CALM1 and broader calcium-regulation annotations on BCL2. This is not a claim of exhaustive comparator coverage or systematic absence across MODs. No CA8 activity was found in the local GO-CAM index. No additional developmental, disease or parent/child process annotation is proposed.

The provider attempt used the installed Falcon client and its configured perplexity-lite fallback once. Both failed DNS resolution and produced no research output. Manual primary-source reading and the independently attributed binding consultation therefore supply the evidence account; no provider-named research file was invented. Further questions retain the context-dependent negative interaction result, the unresolved contact surface and the possibility that some neuronal effects are not exclusively mediated through ITPR1.

The two additional references were retrieved through the ordinary reference fetcher in isolated hosted storage, authenticated and imported as new normal caches without changing existing files. PMID:26399641 is abstract-only and explicitly reports no detected direct binding in its Purkinje-culture study. PMID:19360879 is bibliographic-only despite its Abstract heading; its full structural paper was not read. The primary human PDB 2W2J identity was separately inspected, but is not presented as a substitute for reading every paper-specific structural claim. Both references are listed with these access limits.

All 26 source assertions and the two previously authored proposals have been assessed. Full normal candidate validation, including references, GOA and ontology terms, passed with 22 generic-binding policy advisories and no errors. The status is DRAFT because those advisories persist under the standing binding instruction; it does not mean these records were left unreviewed. The nine short YAML quote occurrences match normal canonical caches exactly, with aggregate reuse totals of 20, 18 and 12 words in the three quoted sources.

## 2026-10-03: canonical application

The independently reviewed candidate was applied after ROOT science approval. Full normal canonical validation passed with the 22 documented binding advisories, the status report retained DRAFT, and the standard EDIT history passed validation. The 26 restored source assertions and 2 retained prior NEW annotations are unchanged from the reviewed candidate. Existing GOA, UniProt, all 13 publication caches and the earlier history remain unchanged. Targeted HTML rendering was completed; remote publication is recorded separately.


## 2026-10-03: evidence and specificity follow-up

The follow-up preserves all 26 normal source assertions, both prior NEW objects, every partner identifier and all 16 reference identities. It refines the broad cytoplasm decision to cytosol and uses that location in the existing single core. The resulting decisions are 3 REMOVE, 22 KEEP_AS_NON_CORE, 1 MODIFY and 2 retained NEW; there is no additional NEW annotation.

The mechanism anchors now retain the complete affinity-reduction clause in [PMID:12611586](https://pubmed.ncbi.nlm.nih.gov/12611586/) and the receptor-side V1538M binding/inhibition result in [PMID:30429331](https://pubmed.ncbi.nlm.nih.gov/30429331/). The selected Introduction passage in [PMID:32316137](https://pubmed.ncbi.nlm.nih.gov/32316137/) supplies concise allosteric context, and the Discussion synthesis in [PMID:42268453](https://pubmed.ncbi.nlm.nih.gov/42268453/) distinguishes receptor interaction from binding the IP3 ligand. These latter passages summarize established work; they are not represented as new direct assays. No solved CA8 contact surface or experimentally proven repurposing of the former active-site cavity is inferred.

The alternative-term assessment is explicit. [GO:0019855 calcium channel inhibitor activity](https://flybase.org/cgi-bin/cvreport.pl?cvterm=GO%3A0019855) captures binding plus inhibition. Its [GO:0005246 regulator parent](https://amigo.geneontology.org/amigo/term/GO:0005246) does not specify direction; [GO:0044325 transmembrane transporter binding](https://amigo.geneontology.org/amigo/term/GO:0044325) omits the functional consequence. GO:0070679 denotes IP3 ligand binding, which is not established as CA8's activity. The preserved process proposal describes CA8's own inhibitory contribution to calcium release and retains its prior participation/comparator justification.

[GO:0005829 cytosol](https://amigo.geneontology.org/amigo/term/GO:0005829) is the non-organelle portion of the cytoplasm and is related to cytoplasm by part_of. The explicit cytosolic description in the complete cached PMID:30429331 Discussion supports the more precise location, alongside the previously reviewed human-fragment interaction work in PMID:19461874. This is cross-source refinement of an existing location assertion, not a newly claimed localization experiment or integral ER-membrane assignment. The original Ensembl source fields remain intact.

PMID:19360879 remains in the bibliography with its bibliographic-only access caveat and is removed from all positive supported_by lists. No paper-specific conclusion is inferred from its title. PMID:26399641 remains visible as countervailing evidence in the annotation reasons, core description, reference assessment and an assay-context question, but is removed from positive support for inhibition. Its negative cultured-Purkinje result does not invalidate every positive recombinant or receptor-defined HeLa experiment, and the positive experiments do not erase the negative result. No unread Methods or image analysis is claimed.

The substantive questions about targeted ITPR1 curation, CA10/CA11 propagation, term specificity and possible residual chemistry have been restored. They are questions rather than assumptions of a missed annotation, a shared CARP interface or an undiscovered catalytic activity. Structural characterization of the CA8–ITPR1 complex and controlled residual-activity screening are again concrete experimental suggestions. The 22 interaction reasons retain each exact partner and curator-deference basis in shorter prose; individual target-table cells and pair-specific orthogonal validation remain uninspected, as detailed above.

Ten verbatim YAML quotation entries have aggregate reuse totals of 20 words from PMID:8977131, 20 from PMID:32316137, 23 from PMID:12611586, 22 from PMID:30429331 and 15 from PMID:42268453. The mechanism-bearing clauses are retained without restoring the previous duplicated long quotations. The old history is append-only and is not rewritten for spacing corrections; any follow-up provenance is recorded in a new standard history entry.

Full normal candidate validation, including reference quotes, GOA consistency and authored term checks, passed with 22 expected standing-policy binding advisories and no errors. DRAFT is retained.

### Follow-up application

The independently approved candidate was applied and passed full normal validation, a status dry run, targeted rendering and standard EDIT history validation. DRAFT retains 22 binding-policy advisories. All 26 source assertions, two prior NEW assertions, 16 reference identities, products, caches and earlier history remain preserved. The sole action change refines cytoplasm to cytosol. See the [follow-up history](https://github.com/ai4curation/ai-gene-review/blob/main/history/genes/human/CA8/2026-10-03T203742Z-codex-7d7f6b.yaml).
