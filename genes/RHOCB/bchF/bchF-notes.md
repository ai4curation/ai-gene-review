# bchF (P26165) — *Rhodobacter capsulatus* SB1003 — curation notes

**Deep research was unavailable for this review.** No deep-research API keys exist in this
container, so `just deep-research` was not run and no `-deep-research-<provider>.md` file
exists. All literature below was found and read directly (cached `publications/PMID_*.md`,
NCBI E-utilities, Europe PMC, Crossref, QuickGO, InterPro, and web search), and every claim
carries inline provenance.

## 1. Identity and locus

- P26165 = `BCHF_RHOCB`, 171 aa, gene `bchF`, ordered locus `RCAP_rcc00666`, strain
  ATCC BAA-309 / NBRC 16581 / SB1003, NCBI taxon 272942.
- Family: Pfam PF07284 (BCHF), NCBIfam TIGR02020 (BchF), InterPro IPR009905
  ("2-vinyl bacteriochlorophyllide hydratase")
  [file:genes/RHOCB/bchF/bchF-uniprot.txt "NCBIfam; TIGR02020; BchF; 1."],
  [file:genes/RHOCB/bchF/bchF-uniprot.txt "Pfam; PF07284; BCHF; 1."].
- UniProt protein existence is **PE 4: Predicted**
  [file:genes/RHOCB/bchF/bchF-uniprot.txt "PE   4: Predicted;"]; the entry carries no
  features besides the full-length CHAIN, no TRANSMEM, and no CC FUNCTION. The enzyme name
  uses the legacy "2-vinyl" numbering; current nomenclature is **3-vinyl**
  bacteriochlorophyllide a hydratase (EC 4.2.1.165; UniProt cross-references BRENDA
  4.2.1.165).
- Pathway assignment is UniPathway UPA00671
  [file:genes/RHOCB/bchF/bchF-uniprot.txt "PATHWAY: Porphyrin-containing compound metabolism; bacteriochlorophyll biosynthesis (light-independent)."].

## 2. The reaction BchF catalyses

BchF hydrates the C-3 vinyl group of (bacterio)chlorophyllide a to a 3-(1-hydroxyethyl)
group; BchC then oxidises that to the 3-acetyl group of bacteriochlorophyllide a:

> "followed by hydration of the 3V group to the 3-hydroxyethyl (3HE) group of 3HE-Bchlide a
> by 3-vinyl (bacterio)chlorophyllide a [3V-(B)Chlide a] hydratase (BchF)"
> [PMID:36971575]

> "oxidation of the 3HE group by 3HE-Bchlide a dehydrogenase (BchC) to form the acetyl group
> of Bchlide a, which is a direct precursor of Bchl a" [PMID:36971575]

Direct enzymology exists for the **family**, on the *Chlorobaculum tepidum* orthologue:
BchF and its paralogue BchV, expressed in *E. coli*, hydrate the C3-vinyl group in vitro and
run the reaction reversibly
[PMID:36822492 "BchF and BchV enzymes catalyze the hydration of a C3-vinyl to C3-1-hydroxyethyl group"],
[PMID:36822492 "The results indicated that both BchF and BchV did function as a hydratase/dehydratase and could play a role in the C31-epimerization."],
[PMID:36822492 "obtained from extracts of Escherichia coli overexpressing the respective genes from Chlorobaculum tepidum"].
A wider in vitro survey of 3-vinyl hydratases from *Chlorobaculum tepidum*,
*Chlorobaculum limnaeum*, *Chloroflexus aurantiacus* and *Chloracidobacterium thermophilum*
found that "All the hydratases showed hydration activities." [PMID:28643169], and notes that
"This 3-vinyl hydration also occurs in BChl a biosynthesis, followed by oxidation that
introduces an acetyl group at the 3-position." [PMID:28643169].

There is **no in vitro assay of the *R. capsulatus* BchF protein** that I could find. The
*R. capsulatus* evidence is genetic.

## 3. *R. capsulatus*-specific genetic evidence

**Burke, Alberti & Hearst 1993 (PMID:8385667)** is the paper that defined this locus. It is
reference [1] of the UniProt entry and it both sequences and assigns *bchF*:

> "The pigments accumulated in strains with physically mapped transposon insertion mutations
> are analyzed by absorbance and fluorescence spectroscopy, allowing us to assign the genes
> as bchF, bchN, bchB, and bchH, in that order." [PMID:8385667]

> "bchF encodes a bacteriochlorophyll alpha-specific enzyme that adds water across the
> 2-vinyl group." [PMID:8385667]

("2-vinyl" is the pre-1990s numbering for the same carbon as today's C-3.) The same abstract
establishes that *R. capsulatus* BChl synthesis runs in the dark:
[PMID:8385667 "bchN and bchB are required for protochlorophyllide reduction in the dark (along with bchL)"].
This paper is **not** cited by any GOA row for P26165 — it is the strongest *R. capsulatus*
evidence for the gene and is uncited.

**Bollivar, Suzuki, Beatty, Dobrowolski & Bauer 1994 (PMID:8158642)** — the paper the CACAO
row cites — is a cluster-wide mutational analysis of the same 46 kb photosynthesis gene
cluster (cached abstract only; `full_text_available: false`):

> "Previous studies have established that most if not all of the genes required for synthesis
> of the Rhodobacter capsulatus essential photosystem are clustered on a 46 kb region of the
> chromosome known as the photosynthesis gene cluster." [PMID:8158642]

> "we have undertaken a systematic directed mutational analysis of 12 open reading frames in
> the photosynthesis gene cluster to evaluate whether individual open reading frames have a
> role in photopigment biosynthesis" [PMID:8158642]

> "mutations constructed in seven open reading frames resulted in a loss of
> bacteriochlorophyll biosynthesis, concomitant with the accumulation of specific
> intermediates in the Mg-tetrapyrrole biosynthetic pathway" [PMID:8158642]

The abstract names no individual ORF, so whether *bchF* is one of the twelve cannot be read
off it. It can be established indirectly: a 2023 peer-reviewed paper cites **this exact DOI**
as a source for the *R. capsulatus bchF* deletion phenotype —

> "Deletion of bchF in Rhodobacter sphaeroides and Rhodobacter capsulatus results in the
> accumulation of Chlide a and 3V-Bchlide a" [PMID:36971575]

— whose references 2–4 for that sentence include `10.1006/jmbi.1994.1260`, i.e. PMID:8158642
(verified against the Crossref reference list for `10.1128/spectrum.03878-22`; reference 3 of
that list is `10.1006/jmbi.1994.1260`). So an independent group treats Bollivar 1994 as
reporting a *bchF* mutant of *R. capsulatus* that accumulates the unhydrated intermediate —
exactly the phenotype expected of a lost 3-vinyl hydratase, and exactly the claim the CACAO
row makes.

## 4. Testing the predicted failure shape: cross-isolate transfer — **ABSENT**

The screen ("references spanning sibling taxa", `projects/CACAO/batch3-screens.yaml`) flagged
PMID:8158642 because its four CACAO rows span two taxon ids:

| accession | entry | gene | taxon id | taxon name |
|---|---|---|---|---|
| P26165 | BCHF_RHOCB | bchF | 272942 | *R. capsulatus* strain ATCC BAA-309 / NBRC 16581 / SB1003 |
| P26168 | BCHE_RHOCB | bchE | 272942 | same |
| P26169 | BCHJ_RHOCB | bchJ | 272942 | same |
| P26236 | BCHM_**RHOCA** | bchM | **1061** | *Rhodobacter capsulatus* (species level, no strain) |

Findings:

1. **No isolate boundary is crossed.** The paper works in *R. capsulatus* and all four
   entries are *R. capsulatus*. Taxon 1061 is the species node and 272942 is a strain node
   beneath it; they are not sibling isolates.
2. **The split is a property of the UniProt entries, not of the annotation.** P26236 is the
   legacy `_RHOCA` entry (created before strain-level proteomes, no `RC STRAIN=` line, not
   mapped to the SB1003 reference proteome), while the other three were re-filed as `_RHOCB`
   on the SB1003 genome. A CACAO student annotating four genes from one paper picked the
   UniProt entry that exists for each gene; the taxon id came with the entry.
3. **One paper, three/four *bch* genes is legitimate here.** The alternative hypothesis in the
   launch prompt — neighbour mis-attribution within the cluster, since *bchF* (RCAP_rcc00666),
   *bchE* (rcc00669) and *bchJ* (rcc00670) are adjacent — is also not supported: Bollivar 1994
   is explicitly a systematic analysis of twelve ORFs of that very cluster, so citing it for
   several of them is correct use of a cluster-wide paper, not over-harvesting.

Verdict: **shape absent**. The screen fired on UniProt taxon-granularity drift between sibling
entries of one species, which is a property of the protein records and not an annotation
defect. Nothing here is reportable against CACAO.

## 5. What *is* wrong: a GO term homonym in InterPro2GO

`GO:0019685 "photosynthesis, dark reaction"` is **the Calvin cycle**, not "the
light-independent reactions of bacteriochlorophyll synthesis". Its GO definition:

> "A complex cycle of enzyme-mediated reactions which catalyzes the reduction of carbon
> dioxide to sugar. As well as carbon dioxide the cycle requires reducing power in the form of
> reduced nicotinamide adenine dinucleotide phosphate (NADP) and chemical energy in the form of
> adenosine triphosphate (ATP). The reduced NADP (NADPH) and ATP are produced by the 'light'
> reactions." (QuickGO, 2026-11-01)

BchF has no role in carbon fixation. The row arrives from InterPro2GO:

```
InterPro:IPR009905 2-vinyl bacteriochlorophyllide hydratase > GO:photosynthesis, dark reaction ; GO:0019685
```

and the InterPro entry's own description explains how: it says IPR009905 "is involved in the
light-independent bacteriochlorophyll biosynthesis pathway by adding water across the 2-vinyl
group". "Light-independent" was mapped to the term *named* "dark reaction".

This is systematic, not a one-off. All four InterPro2GO rules that use GO:0019685 are
light-independent (bacterio)chlorophyll-synthesis families
(`current.geneontology.org/ontology/external2go/interpro2go`, retrieved 2026-11-01):

```
InterPro:IPR005969 Light-independent protochlorophyllide reductase, B subunit   > GO:0019685
InterPro:IPR005970 Light-independent protochlorophyllide reductase, N subunit   > GO:0019685
InterPro:IPR005971 Light-independent protochlorophyllide reductase, iron-sulphur ATP-binding protein > GO:0019685
InterPro:IPR009905 2-vinyl bacteriochlorophyllide hydratase                     > GO:0019685
```

QuickGO (2026-11-01) returns **3,731 annotations to GO:0019685, and 3,731 of them cite
GO_REF:0000002 (InterPro2GO)** — i.e. every annotation to this Calvin-cycle term in GOA comes
from these four chlorophyll-pathway rules. The correct term for all four is `GO:0036070
light-independent bacteriochlorophyll biosynthetic process` (for the *bch* families) or the
chlorophyll counterpart. Recorded as a `source_defects` entry (WRONG_TERM, resource OTHER =
InterPro / InterPro2GO) on the GO:0019685 row.

## 6. Ontology gap: no GO term for the BchF reaction

GO has `GO:0036354 bacteriochlorophyllide-a dehydrogenase activity` for the **next** step
(BchC) but no term for the hydratase step itself; searching QuickGO for
"bacteriochlorophyllide" returns only GO:0036354, and `GO:0016836 hydro-lyase activity` has no
suitable child (checked 2026-11-01). So the IEA MF row sits at the generic hydro-lyase parent
with nowhere more specific to go. Filed as a `proposed_new_terms` entry,
"3-vinyl bacteriochlorophyllide a hydratase activity" (EC 4.2.1.165, RHEA/MetaCyc
MONOMER-13252, BRENDA 4.2.1.165), and used as the `proposed_replacement_terms` NTR for that
row and as the core function's `proposed_molecular_function`.

## 7. GONUTS — now permanently retired

`projects/CACAO.md` records that gowiki.tamu.edu was "temporarily offline while we perform
upgrades" through batches 1–2. Retried 2026-11-01: the host now returns **HTTP 410 Gone** with
the page title "GONUTS has been retired" and the body "The GO wiki that was at gowiki.tamu.edu
is no longer online. For Gene Ontology terms and annotations, see the Gene Ontology
Consortium. The lab's other wikis are still here: EcoliWiki and OMP." The Wayback availability
API has no snapshot for `UniProtKB:P26165`, `PMID:8158642` or
`Rhodobacter_capsulatus:bchF` on that host. **The GONUTS route is gone for good**, so the
project's standing plan to "re-check the abstract-only rows when GONUTS returns" cannot be
carried out; abstract-only CACAO rows must be judged from the literature, as here.

## 8. Open points

- No *R. capsulatus* BchF protein has been purified or assayed; the activity assignment for
  this specific protein rests on mutant pigment phenotypes plus orthologue enzymology.
- The sequence is strongly hydrophobic over roughly residues 30–165 and BchF is generally
  discussed as a membrane-bound enzyme, but the UniProt entry asserts no TRANSMEM feature and
  GOA carries no cellular-component row at all. I did not assert a CC annotation: one
  hydropathy impression is a single line of evidence. Raised as a suggested question and
  experiment instead.
- Whether BchF acts on Chlide a before, or on 3V-Bchlide a after, chlorophyllide reductase
  (BchXYZ) is not settled for *R. capsulatus*; PMID:36971575 draws both routes and the BF
  mutant accumulates both Chlide a and 3V-Bchlide a.
