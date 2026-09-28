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
