# EIF2S1 (eIF2-alpha, UniProtKB:P05198) curation notes

Curation journal for the ISR project review ([projects/INTEGRATED_STRESS_RESPONSE.md](../../../projects/INTEGRATED_STRESS_RESPONSE.md),
issue #3951). Append, do not rewrite.

## 2026-11-02 — initial review (102 GOA rows)

### Provenance of the literature search

`just deep-research human EIF2S1 --provider perplexity` **failed**: the runner has
no `agentapi` on PATH and the only available provider was `claude_code`
(`ERROR - Provider 'perplexity' not available. Available: claude_code`). Per
`CLAUDE.md` no file was written under a `-deep-research-<provider>.md` name. The
review was therefore grounded in:

- the fetched UniProt record `EIF2S1-uniprot.txt` (curated FUNCTION, ACTIVITY
  REGULATION, SUBUNIT, SUBCELLULAR LOCATION, PTM, CAUTION blocks);
- the 54 GOA-seeded references, with full text read where cached;
- four references fetched during this review with `just fetch-pmid`:
  PMID:19131336, PMID:15207627, PMID:18032499, PMID:31048492 (plus
  PMID:15489334, see the mis-citation note below);
- `interpro/panther/PTHR10602/PTHR10602-paint.tsv` for the IBD node placements;
- QuickGO queries for the comparator check on the ISR branch terms.

Full text was available in the cache for PMID:38340717, PMID:32132707,
PMID:23063529, PMID:31836389, PMID:26095357, PMID:19131336, PMID:18032499,
PMID:35031321 and PMID:22934019. The rest are abstract-only; this is recorded
per reference with `full_text_unavailable` and in `reference_review.review_notes`.

### The mechanism, as the record supports it

eIF2-alpha is the regulatory subunit of the eIF2 heterotrimer. Its canonical job
is carried out by the trimer, not by the subunit alone
[file:human/EIF2S1/EIF2S1-uniprot.txt "Eukaryotic translation initiation factor 2
eIF2 is a heterotrimeric complex composed of an alpha (EIF2S1), a beta (EIF2S2)
and a gamma (EIF2S3) chain"], which is why `core_functions` entry 1 uses
`contributes_to_molecular_function` rather than `molecular_function`.

The regulatory switch is well grounded on the **human** record with experimental
evidence, not only by similarity
[file:human/EIF2S1/EIF2S1-uniprot.txt "Activity is regulated by phosphorylation at
Ser-49 and Ser-52, which stabilizes the eIF2/GDP/eIF2B complex and prevents the
eIF2B-mediated exchange of GDP for GTP, thereby preventing the formation of the
43S pre-initiation complex (43S PIC)"]. The same idea is stated mechanistically in
PMID:38340717 ["Phosphorylation of the α subunit of EIF2 by the ISR kinases causes
EIF2 to change from a substrate to a competitive inhibitor of EIF2B."]. This
matters for the `involved_in` test: eIF2-alpha is not merely the substrate of the
four kinases, it is the entity that then performs the inhibition of eIF2B, so the
`GO:0032057` rows are participation and not necessity.

Note on residue numbering: the literature's "Ser-51" and the record's "Ser-52"
are the same residue (mature protein vs. full precursor numbering). No
`residue_mappings` were added because no finding in this review states a residue
number as its claim; the numbers appear only inside quotations.

### Mitophagy: why this is participation, not necessity

The strongest reason to `ACCEPT` `GO:0000423` is not the knockdown data (which
would only establish necessity) but the gain-of-function tethering:
rapalog-induced recruitment of **phosphomimetic** eIF2-alpha(S51D) to the
mitochondrial outer membrane induced mitophagy with no stress applied, while
wild-type and S51A did not [PMID:38340717 "Taken together, these results indicate
that phosphorylation and mitochondrial localization of EIF2α are necessary and
sufficient to trigger mitophagy."]. The step eIF2-alpha contributes to is
autophagosome recruitment, downstream of PINK1/PARKIN marking [PMID:38340717 "it
did result in a clear reduction in the association of LC3B-GFP with mitochondria,
indicating a defect in the recruitment of autophagosomes to mitochondria"]. The
effect is organelle-selective: the same tethering to peroxisomes did not induce
pexophagy [PMID:38340717 "it failed to induce pexophagy, in contrast to
starvation"], which is why the remaining receptor/mechanism is recorded as a
BIOLOGY knowledge gap on core function 3 rather than guessed at.

### Mitochondrion stays at the root term

Per `projects/ORGANELLES.md` the organelle term is kept and **not** refined. Two
direct lines agree on the organelle (mitochondrial fraction enrichment; TOM20
colocalisation) and the ER confound was explicitly controlled [PMID:38340717
"Analysis of the subcellular fractions with an ER marker showed no evidence of ER
enrichment of p-EIF2α upon DFP treatment"]. But `GO:0005741` mitochondrial outer
membrane was **not** added: eIF2-alpha has no transmembrane segment or targeting
presequence, and what is observed is stress-dependent peripheral recruitment to
the cytosolic face — exactly the "transient recruitment to the organelle surface
is not an outer-membrane location" case the project page warns about.

### Granularity refinements (MODIFY), and why each one

Following the "correct but general is MODIFY" rule. In each case the replacement
is an `is_a` descendant and in all but one case the gene already carries it:

| rows | term | → | note |
|---|---|---|---|
| 5,6,7,8 | GO:0003743 translation initiation factor activity | GO:0160296 (+GO:0160297 on the IDA row) | both children already carried, from PMID:16289705 |
| 61,62,63 | GO:0006413 translational initiation | GO:0002183 cytoplasmic translational initiation | *not* yet carried; mitochondrial initiation uses MTIF2/MTIF3, and the IDA was a HeLa cytoplasmic extract |
| 1 | GO:0003676 nucleic acid binding | GO:0003723 RNA binding | no DNA ligand reported; RNA binding carried by two HDA rows |
| 64 | GO:0006446 regulation of translational initiation | GO:0032057 | all established regulation is the stress-triggered negative arm |
| 35,36 | GO:0005737 cytoplasm | GO:0005829 cytosol | cytoplasm is not a root organelle term, so the refinement rule applies |
| 80,81,83 | GO:0034976 response to ER stress | GO:0036499 PERK-mediated UPR | GOA records GO:0036499 from the same reference (PMID:33384352) |
| 82 | GO:0034976 response to ER stress | GO:0036490 | PMID:18508033 raises PERK **and** PKR, so the PERK-specific term is not isolated by this row; GO:0036490 is carried from the same paper |

`GO:0003723` itself was deliberately **not** refined to `GO:0003729` mRNA binding
even though the two HDA rows come from oligo(dT)/UV-crosslinking mRNA-interactome
capture: eIF2-alpha's physiological RNA ligands include initiator Met-tRNA as well
as mRNA, so the parent is the honest level.

### Protein binding (25 rows)

Policy (`protein_binding_policy.py`): `REMOVE` unless the paper supports a more
informative MF. Five rows were `MODIFY`d instead:

- PKR/EIF2AK2 (P19525) × 3 → `GO:0019901 protein kinase binding`. PMID:9431994 is
  the direct in vitro mapping ["pK3, eIF2alpha, and the truncated form of
  eIF2alpha all bind to the C-terminus of PKR containing the catalytic domain, but
  not to the regulatory N-terminus."].
- mouse PERK (Q9Z2B5) → `GO:0019901`; PMID:16288713 reports Kd ≈ 0.74 µM and shows
  the contact does not need the phosphoacceptor.
- PPP1CA (P62136) → `GO:0019903 protein phosphatase binding`; PMID:26095357 is the
  GADD34:PP1 eIF2-alpha phosphatase structure, i.e. the off-switch.

The eIF2S2/eIF2S3 rows (seven of them, across BioPlex/HuRI/structures) were
removed rather than modified: subunit-subunit contact inside a known complex is
already said by the five `GO:0005850` rows, and no MF follows from it. The
reproducible **PRMT7** pair (PMID:32296183 and PMID:33961781 independently) is
removed too, but flagged in `suggested_questions` — a reproducible interaction
without a mechanism is an experiment to run, not an annotation.

### The GCN2 branch asymmetry (deliberately not a NEW row)

The gene carries `GO:0140468` HRI-mediated signaling (IDA ×3) and `GO:0036499`
PERK-mediated UPR (IDA ×2), and QuickGO shows GO annotates `GO:0140468` across the
whole HRI chain — OMA1, DELE1, EIF2AK1, **EIF2S1**, ATF4, DDIT3 — so the branch
terms are not reserved for the kinase. The sibling `GO:0140469` GCN2-mediated
signaling is annotated to EIF2AK4, GCN1, IMPACT and MAP3K20 but **not** to
EIF2S1. By the comparator logic this looks like a genuine gap rather than a
convention.

It was still **not** proposed as `NEW`, because the human evidence is not there:
UniProt's GCN2 statement is `(By similarity)` ["Phosphorylation on Ser-52 by the
EIF2AK4/GCN2 protein kinase occurs in response to amino acid starvation and UV
irradiation (By similarity)"] and the amino-acid-starvation rows in GOA are
ISS/IEA. Recorded as a `suggested_questions` entry plus a matching
`suggested_experiments` design (S52A knock-in with branch-selective pharmacology).
If a human IDA turns up, this is a one-row addition.

### Over-annotations

- `GO:0016020` membrane (HDA, PMID:19946888, NK-cell membrane proteome) — no TM
  segment, signal peptide or lipid anchor in UniProt; membrane-enriched fractions
  routinely retain abundant cytosolic and ribosome-associated proteins.
- `GO:0070062` extracellular exosome (HDA, PMID:20458337) — same class of
  argument; no secretory route.
- `GO:0005634` nucleus (IEA, Ensembl Compara from mouse Q6ZWX6) — the human
  subcellular-location block lists stress granule, cytosol and mitochondrion only.
- `GO:0097451` glial limiting end-foot (IEA, from rat P68101) — a ubiquitous
  cytosolic factor being present in a cellular subdomain is expected and
  uninformative.

None of these is `REMOVE`: each is a real detection or a projection of a real
ortholog annotation, and the problem is interpretation rather than falsity.

### Source-record observation (not filed as a defect)

UniProt's PTM block cites `PubMed:15489334` for "Substrate for at least 4 kinases:
EIF2AK1/HRI, EIF2AK2/PKR, EIF2AK3/PERK and EIF2AK4/GCN2". PMID:15489334 is the MGC
full-length cDNA project paper (Gerhard et al., *Genome Res* 2004) and says
nothing about eIF2-alpha kinases. This looks like a mis-keyed citation, but it was
**not** recorded as a `source_defects` entry: the correct replacement identifier
has not been established, and a defect entry needs `asserted_value` →
`corrected_value`. Worth revisiting if the intended reference can be identified.

### Loose ends for the project

- `PPP1R15A`/`PPP1R15B` (the two phosphatase regulatory subunits) and `DDIT3`,
  `EIF2AK2` have no gene folder yet; they are the natural next items on #3951.
- The ISR module, once built, should model the four-kinase convergence on this
  protein and the eIF2B inhibition step; `Reactome:R-HSA-381111`,
  `Reactome:R-HSA-9835885` and `Reactome:R-HSA-9840415` already model three of the
  four phosphorylation events.
