# Research notes: A0A3B6GK97 (WHEAT) — PNPLA/patatin domain-containing protein

> Deep-research providers (falcon, perplexity) were **not available** in this environment
> (no API keys; the falcon attempt failed with a template/credentials error). Per project
> guidance, the manual research below is recorded in this notes file rather than a
> `-deep-research-{provider}.md` file. No PMIDs are cited in the GOA (annotations are all
> homology-based IEA), so `fetch-gene-pmids` returned nothing to cache.

## Identity

- **UniProt**: A0A3B6GK97 (UniProtKB/**TrEMBL, Unreviewed**), entry version 31, 302 aa.
- **Organism**: *Triticum aestivum* (bread wheat), NCBI:txid4565. Hexaploid crop.
- **Gene model**: EnsemblPlants/Gramene `TraesCS3D02G033600` (chromosome **3D**, IWGSC
  Chinese Spring assembly). No HGNC-style symbol exists; the accession is used as the
  directory/file name. Homoeologs/related models exist across sub-genomes and pangenome
  assemblies (e.g. TraesCS3D03G0060600, TraesKAR3D..., TraesRN3D...).
- **Protein name**: "PNPLA domain-containing protein" (name from PROSITE profile match only).
- **Evidence level**: PE 3 (Inferred from homology). Entry derives from a single large-scale
  genomic-DNA submission (Rossello M., 2018) + EnsemblPlants identification. **No
  gene-specific functional/experimental literature exists for this locus.**

## Domain / family

- **PROSITE**: PS51635 (PNPLA profile) matches residues **1–134** → patatin-like
  phospholipase domain.
- **InterPro**: IPR002641 (PNPLA domain) and IPR016035 (Acyl transferase/acyl
  hydrolase/lysophospholipase superfamily). **SUPFAM** SSF52151 (FabD/lysophospholipase-like).
  **Gene3D** 3.40.1090.10 (cytosolic phospholipase A2 catalytic domain fold).
- **UniProt SIMILARITY**: "Belongs to the **patatin family**" (ARBA00010240).
- **PANTHER**: PTHR32176 (subfamily SF103 "OS08G0376550 protein"; the family-level name
  "XYLOSE ISOMERASE" attached to PTHR32176 is a spurious/mis-propagated PANTHER family label
  and is **not** relevant — the domain architecture is unambiguously patatin/PNPLA, not a
  TIM-barrel xylose isomerase).

## Functional inference (family-level, no direct evidence for this protein)

- The patatin/PNPLA domain is a **lipid acyl hydrolase** module using a non-canonical
  **Ser–Asp catalytic dyad** (not the classical Ser-His-Asp triad), with the nucleophilic
  Ser in a Gly-X-Ser-X-Gly–type elbow and an oxyanion hole; established from the potato
  patatin crystal structure [PMID:12779324 "The Crystal Structure, Mutagenesis, and Activity
  Studies Reveal that Patatin Is a Lipid Acyl Hydrolase with a Ser-Asp Catalytic Dyad"].
- Patatin/PNPLA enzymes have broad **non-specific lipolytic acyl hydrolase (LAH)** activity:
  they hydrolyze phospholipids, galactolipids and mono/di-acylglycerols, releasing free fatty
  acids (the UniProt ARBA FUNCTION text for this entry: "Possesses non-specific lipolytic
  acyl hydrolase (LAH) activity. Hydrolyzes phospholipids as well as galactolipids. May play
  a role in disease resistance." — ARBA00025642).
- In plants, several patatin-like proteins (pPLA/PLP) are **pathogen-inducible** and
  contribute to lipid signaling in defense (e.g. Arabidopsis PLP2/PLP7 induced by fungal and
  bacterial pathogens; PLP2 is a cytoplasmic LAH of wide substrate specificity)
  [PMID:16297072 La Camera et al., Plant J 2005, "A pathogen-inducible patatin-like lipid acyl
  hydrolase facilitates fungal and bacterial host colonization in Arabidopsis"]. This is the
  basis for the UniProt "Plant defense" keyword and the ARBA "may play a role in disease
  resistance" statement — **family-level, not demonstrated for this wheat protein.**

## GOA annotations to review (from QuickGO; both IEA)

1. **GO:0006629 lipid metabolic process** — IEA, GO_REF:0000002 (InterPro2GO),
   WITH InterPro:IPR002641 (PNPLA domain). Defensible: the PNPLA domain is a lipid hydrolase
   module; lipid metabolic process is the correct (if general) BP. → ACCEPT (non-core / keep;
   this is the most specific safe BP given only a domain match).
2. **GO:0016787 hydrolase activity** — IEA, GO_REF:0000117 (ARBA), WITH ARBA:ARBA00026276.
   Correct but **very general** MF. The patatin domain specifically supports
   acylglycerol/lipid **acyl-hydrolase / phospholipase** activity, so a more informative MF
   (e.g. GO:0052689 carboxylic ester hydrolase activity, or GO:0004620 phospholipase activity)
   would be preferable. However it is not *wrong*. → MODIFY toward a more specific hydrolase
   term, or KEEP_AS_NON_CORE if remaining conservative for a homology-only entry.

### IBA lipase annotations missing from QuickGO GOA pull (confirmed in AmiGO) — IMPORTANT
The UniProt flat file lists two **IBA** molecular-function terms that are **absent from the
QuickGO `-goa.tsv` pull** used to seed the review (which returned only the 2 IEAs above).
I verified these directly against **AmiGO/GOlr** (via the GO MCP `search_annotations` on
`UniProtKB:A0A3B6GK97`; web record:
http://amigo.geneontology.org/amigo/gene_product/UniProtKB:A0A3B6GK97):

| GO term | Label | Evidence | Reference | Assigned by | Date |
|---|---|---|---|---|---|
| GO:0004620 | glycerophospholipase activity | IBA (ECO:0000318) | GO_REF:0000033 | GO_Central | 2017-02-28 |
| GO:0047372 | monoacylglycerol lipase activity | IBA (ECO:0000318) | GO_REF:0000033 | GO_Central | 2017-02-28 |

QuickGO and AmiGO are **complementary** here: QuickGO returned only the 2 IEAs
(InterPro2GO + ARBA); AmiGO/GOlr returned only the 2 GO_Central IBAs. These IBA
annotations are manually-reviewed phylogenetic (PAINT) assertions that this protein is a
**lipase** (glycerophospholipase + monoacylglycerol lipase), which is stronger and more
specific than the generic IEA hydrolase term.

**Handling decision (per maintainer):** do NOT add these IBAs to `existing_annotations` —
the CI consistency check requires `existing_annotations` to mirror the seeded GOA tsv, so
adding rows it doesn't contain would fail CI. Instead they are recorded as **out-of-band
knowledge**: cited via `GO_REF:0000033` (with the AmiGO URL) in the references list and
woven into the `GO:0016787` MODIFY reasoning and `core_functions`. They reinforce (but do
not change) the MODIFY of the generic hydrolase IEA toward carboxylic ester hydrolase
activity, the immediate informative parent of both IBA lipase terms.

The UniProt flat file additionally lists GO:0006952 defense response (IEA:UniProtKB-KW),
also not in the GOA pull; defense response for this specific locus is unsupported beyond
keyword propagation and is not asserted here.

## Bioinformatics analysis (subfamily + catalytic-site integrity) — IMPORTANT
Reproducible analysis in `A0A3B6GK97-bioinformatics/` (see RESULTS.md). MSA of the query
against 13 characterized plant pPLAs (Arabidopsis pPLAI/II/III, rice PLP1/2, potato patatin)
with FAMSA + BioPython; input-driven control included.

Two findings:
1. **Subfamily = pPLAII.** The query is 42–50% identical to the pPLAII subfamily and rice
   pPLAs, vs only ~23% to pPLAIII and ~16% to pPLAI; NJ tree places it in the pPLAII/rice/
   patatin clade. So it is the soluble acyl-hydrolase (defense/wounding/stress) clade, NOT
   the pPLAIII galactolipase/growth clade or the large iPLA2-like pPLAI. Single-domain
   architecture + this placement make a **membrane-trafficking role very unlikely** (answers
   the trafficking question raised in review).
2. **The deposited 302-aa model lacks the catalytic serine.** It is fully gapped through the
   N-terminal patatin catalytic core: no oxyanion **DGGG** block and no catalytic-Ser
   **G-T-S-T-G** nucleophile elbow (zero G-x-S-x-G motifs in 302 aa); it retains only the
   C-terminal portion incl. the catalytic Asp (D121). Every active reference has GTSTG+DGGG;
   the annotated-inactive PLP9 control also lacks GTSTG. **Predicted catalytically inactive
   as modeled.** Most parsimonious = **incomplete/incorrect gene model** (~100–130 aa shorter
   than orthologs, missing a clean N-terminal block), though a true degenerate pseudo-enzyme
   cannot be excluded from sequence alone (would need genomic/homoeolog/RNA-seq checks).

Consequence: the GO_Central IBA lipase calls (GO:0004620, GO:0047372) were propagated
phylogenetically and do NOT verify active-site integrity, so they are not supported by the
current sequence. The review keeps the MODIFY → carboxylic ester hydrolase activity as the
family-level term but adds this explicit caveat, and flags the gene model for curation.

## Bottom line
A plausibly-real but entirely **uncharacterized** wheat patatin/PNPLA-family lipid acyl
hydrolase. All evidence is homology/profile-based (IEA). No experimental data, no
gene-specific publications. Reviews should stay conservative: the two IEA annotations are
biologically reasonable; the MF (hydrolase activity) is under-specific and is the main
candidate for refinement.
