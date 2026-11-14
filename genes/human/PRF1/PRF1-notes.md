# PRF1 (perforin-1, UniProtKB:P14222) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for PRF1. `just deep-research-falcon human PRF1
--fallback perplexity-lite` was attempted and both providers failed in this environment
(`ERROR - Provider 'falcon' not available. Available: openscientist, claude_code`, then the
same for `perplexity`), so there was no provider output to work from. These are my own notes
from the cached publications, the UniProt record and QuickGO queries, deliberately **not**
named as a provider file. Every assertion below carries its source.

## What the protein is

67 kDa secreted glycoprotein, three domains: an N-terminal MACPF/cholesterol-dependent-cytolysin
domain, an EGF-like domain, and a C-terminal C2 domain.

> "Perforin is a thin 'key-shaped' molecule, comprising an amino-terminal membrane attack complex
> perforin-like (MACPF)/cholesterol dependent cytolysin (CDC) domain followed by an epidermal
> growth factor (EGF) domain that, together with the extreme carboxy-terminal sequence, forms a
> central shelf-like structure." [PMID:21037563]

UniProt places it in the complement C6/C7/C8/C9 family (`CC SIMILARITY`), with SIGNAL 1..21,
CHAIN 22..555, two beta-stranded TRANSMEM segments (CH1 129..149, CH2 257..279), MACPF domain
27..375, EGF-like 376..408 and C2 397..519. PANTHER family PTHR46096 ("Perforin-1 pore-forming"),
subfamily SF3.

## Mechanism, step by step

1. **Stored as soluble granule cargo.** Cytolytic granules are secretory lysosomes. Perforin is
   in the lumen, not the granule membrane, which is why `GO:1904856 cytolytic granule lumen` is
   the precise location. Colocalises with granzyme B and LAMP-1 but not EEA1 [PMID:24088571].
2. **Released into the synapse, which forms first.** This ordering matters for the review:
   > "releasing the contents of cytotoxic granules1 into the immune synapse formed with their
   > target cell" [PMID:21685908]
3. **Calcium-dependent membrane binding by the C2 domain.**
   > "A C-terminal C2 domain mediates initial, Ca(2+)-dependent membrane binding." [PMID:21037563]

   > "Calcium titrations, together with dodecylphosphocholine micelle experiments, confirmed that
   > multiple Ca(2+) ions bind within the calcium-binding regions, activating perforin with
   > respect to membrane binding." [PMID:26306037]

   The dependence is absolute, not modulatory: "In the absence of Ca2+, no permeabilization of
   GUVs was observed" [PMID:20889983].
4. **Oligomerisation through a pre-pore.** Two membrane-bound conformations were resolved,
   "interpreted as pre-pore and pore states of the protein" [PMID:20889983]; the 4 Å pore
   structure is in [PMID:35148176].
5. **Pore, heterogeneous and cargo-selective.** "perforin pores exhibit a broad range of
   conductances, from 0.15 to 21 nanosiemens" [PMID:20889983]. Not an indiscriminate hole:
   "perforin preferentially delivers cationic molecules while anionic and neutral cargoes are
   delivered inefficiently" [PMID:24558045], attributed to a conserved anionic lumen.
6. **Two delivery routes.** At the plasma membrane, and via endosomes: perforin "activates
   clathrin- and dynamin-dependent endocytosis, which removes perforin and granzymes from the
   plasma membrane to early endosomes" [PMID:20038786], and then "perforin formed pores in the
   gigantosome membrane, allowing endosomal cargo, including granzymes, to be gradually released"
   [PMID:21685908]. A gigantosome is an enlarged EEA1-positive early endosome [PMID:21685908].

## Loss of function

Mouse: two independent knockout lines. CTL and NK killing lost or sharply reduced while the cells
themselves are normal in number [PMID:8164737]; "impaired but not abolished", with about a third
of killing surviving [PMID:7972104] — a useful constraint on how absolutely to read the
cytotoxicity annotations. Mice "fail to clear lymphocytic choriomeningitis virus and they
eliminate fibrosarcoma tumour cells with reduced efficiency" [PMID:8164737].

Human: familial haemophagocytic lymphohistiocytosis type 2. "Cultured lymphocytes from patients
had defective cytotoxic activity, and immunostaining revealed little or no perforin in the
granules" [PMID:10583959]; "Cytotoxic T and natural killer (NK) cell activity is markedly reduced
or absent in these patients" [PMID:11179007].

## Review decisions worth recording

### The two annotations I removed: `GO:0001771` immunological synapse formation (IBA + IDA)

Perforin is cargo delivered **into** a synapse built by TCR/adhesion-molecule clustering; the
term's definition names that clustering as the mechanism. Perforin-null lymphocytes conjugate with
targets and fail at lysis, not at synapse assembly. The IDA is cited to a Syntaxin-7 paper in
which perforin antibody is the lytic-granule marker and Stx7 is the protein shown to be required
[PMID:21438968]; the underlying observation (perforin-stained granules at the synapse) is a
localisation result, already captured by the CC term `GO:0001772`, which the review accepts.
The IBA's PAINT node draws on that same human IDA, so the scoping error is inherited.

GO already carries a NOT annotation on `GO:0001771` for human CORO1A (PMID:24760828, per the
QuickGO term record), so the term is actively policed.

### The term choice I expected to change and did not: `GO:0022829` vs `GO:0140911`

From the definitions alone, `GO:0140911 pore-forming activity` ("a protein is inserted into the
membrane of another cell where it forms transmembrane pores") looks like the better fit, and
`GO:0022829 wide pore channel activity` reads oddly (its definition is about propanediol
diffusion through gap junctions and porins). I was going to propose MODIFY. The comparator check
reversed it — QuickGO, human, exact-term:

| Term | Human genes carrying it |
|---|---|
| `GO:0022829` | C6, C7, C8A, C8B, C8G, C9 (all IDA), MPEG1 (IDA), GSDMD, GSDME, PANX1-3, PRF1 |
| `GO:0140911` | DEFA1–DEFA6 (IBA/IDA), MMD (IEA), PRF1 (IEA) |

`GO:0022829` is where GO puts the MACPF/CDC and gasdermin pore-formers, experimentally, including
perforin's own complement family. `GO:0140911` is in practice a defensin term. Proposing a move
would have made perforin the only member of its family on a different term. Both are kept: they
sit in unrelated branches (`GO:0022829` under channel activity, `GO:0140911` directly under
`molecular_function`), so neither entails the other. **The real defect is in the ontology, not the
gene**: two unrelated terms for one activity class, which is why a protein like perforin lands on
both by different routes. Raised as a suggested question.

### `GO:0042267` natural killer cell mediated cytotoxicity — proposed as NEW

The human record had the T-cell child and the parent but not the NK child. Comparator check
(QuickGO, human, exact): GZMB — the granule effector in the same role — carries it by IDA **and**
IMP, and the term's 33 human genes include factors more peripheral to the killing step than
perforin (ARL8B, KIF5B, PLEKHM2, all IMP; LYST by IMP). So the absence reads as a gap rather than
a convention. Against: GZMA and GNLY also lack it, and so does mouse Prf1 — the mouse record
probably wants the same addition. Participation is not in doubt: perforin performs the
membrane-breaching step, it is not a substrate of the process.

### `GO:0009306` protein secretion — re-levelled, and the same issue sits in a GO-CAM

Traces to the finding that caspase-7 exits the cell through perforin pores [PMID:35705808]; UniProt
records "Perforin pores allow the release of mature caspase-7 (CASP7) into the extracellular
milieu". Efflux through a lytic lesion is not "the controlled release of proteins from a cell".
`GO:0071806 protein transmembrane transport` describes it and the gene already carries it.
GO-CAM `gomodel:62b4ffe300000081` uses the same `GO:0009306` framing.

## Open mechanistic disputes (not resolvable from the annotations)

- **Which membrane delivers granzymes in physiological killing?** Plasma membrane pores versus
  endosomal escape. Both are documented by the same group; [PMID:21685908] argues the
  endosomal route predominates at sublytic, physiological perforin concentrations.
- **Pore-independent translocation.** Metkar et al. report that perforin and perforin–serglycin
  complexes deliver granzyme B–serglycin "without producing detectable plasma membrane pores"
  [PMID:11911826]. If right, perforin has a translocator function distinct from its channel
  activity and the MF annotations would need a non-channel term. Recorded as `DISPUTED` on that
  reference, not as a citation defect.
- **`GO:0005544` calcium-dependent phospholipid binding** is arguably the C2 domain's real
  measured activity and is more informative than `GO:0005509` calcium ion binding alone. Neither
  the human nor the mouse record carries it. Not added unilaterally; raised as a question.
- **Perforin + granulysin killing of intracellular *M. tuberculosis*** [PMID:9756476]. No
  defense-response-to-bacterium annotation proposed: the paper attributes the killing to
  granulysin, with perforin granting access. Raised as a question instead.

## Reference-level problems flagged

- `PMID:21438968` (Syntaxin-7) — `MISCITED` with respect to `GO:0001771` for perforin.
- `PMID:9756476` (granulysin) — fine for the granule location, poor choice for
  `GO:0140507 granzyme-mediated programmed cell death signaling pathway`, which it does not
  address. Re-referencing suggestion, not asserted as an error: full text not in the cache.
- `PMID:11911826` — `DISPUTED` (contested mechanism, correctly cited).
- `Reactome:R-HSA-9851131` is a gene-expression event (NPM1-ALK-stimulated PRF1 expression) cited
  for a protein location; the location is right but the link is indirect.

## Separate ontology issue noticed, outside this gene

`GO:0001772 immunological synapse` is asserted `part_of GO:0005886 plasma membrane` in
`go-edit.obo`, which does not square with its own definition of a contact zone contributed to by
both cells. Not a defect in any PRF1 annotation and not acted on here; it belongs upstream in
geneontology/go-ontology.
