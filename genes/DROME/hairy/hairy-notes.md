# hairy (h / hry, CG6494, UniProt P14003, HAIR_DROME) — curation notes

> Reviewing **hairy = P14003**, the ~337 aa pair-rule bHLH-Orange (HES-family) transcriptional
> repressor of *Drosophila melanogaster*. This is a DISTINCT gene from **Hairless (H, Q02308)**;
> no Hairless data is used here. Directory aliased `hairy` to avoid the `h`/`H` collision.

## 1. Identity, domains, and architecture

Hairy is the founding member of the *Drosophila* Hairy/Enhancer-of-split (HES) subfamily of
**basic helix-loop-helix–Orange (bHLH-O)** transcription factors. The UniProt record
(`hairy-uniprot.txt`) gives the domain layout: a **bHLH domain at residues 31–88**, an
**Orange domain at 107–136**, disordered/low-complexity C-terminal regions, and a terminal
**WRPW motif at residues 334–337**. The bHLH is of the "repressor-specific" type: UniProt notes
"Has a particular type of basic domain (presence of a helix-interrupting proline) that binds to
the N-box (CACNAG), rather than the canonical E-box (CANNTG)." Family assignment is corroborated
by InterPro (IPR050370 HES_HEY; IPR003650 Orange), Pfam PF07527 (Hairy_orange) + PF00010 (HLH),
and PANTHER PTHR10985 (HES-related bHLH), plus CDD cd18913 "bHLH-O_hairy_like."

UniProt FUNCTION: "Pair-rule protein that regulates embryonic segmentation and adult bristle
patterning. Transcriptional repressor of genes that require a bHLH protein for their transcription
(e.g. ftz)." SUBCELLULAR LOCATION: Nucleus.

## 2. Molecular function: sequence-specific DNA-binding transcriptional repressor

Hairy is a **sequence-specific DNA-binding transcriptional repressor**, established directly in
vivo/in vitro: [PMID:7958929 "h, a basic-helix-loop-helix (bHLH) protein, is a sequence-specific"
DNA-binding protein and transcriptional repressor]. The same study identified *achaete* as a
direct target: [PMID:7958929 "We identify the proneural gene achaete (ac) as a direct downstream
target of h regulation in vivo"], and mutation of a single conserved high-affinity Hairy site
upstream of *ac* produced ectopic sensory organs, showing [PMID:7958929 "direct repression of ac
by h plays an essential role in" pattern formation in the PNS].

Hairy-related proteins are defined by "both a repressor-specific bHLH DNA binding domain and a
**carboxyl-terminal WRPW** (Trp-Arg-Pro-Trp) motif" [PMID:8649374 "presence of both a
repressor-specific bHLH DNA binding domain and a carboxyl-terminal WRPW"]. Binding-site
preference: although a canonical **E-box binding** IDA exists (FlyBase, from PMID:7958929),
UniProt emphasises Hairy's proline-interrupted basic region binds the **N-box (CACNAG)**
preferentially; the *achaete* high-affinity site is a Hairy "class C" site. Both the E-box IDA
and the N-box preference reflect genuine sequence-specific DNA binding — they are not
contradictory, and the more informative MF here is "DNA-binding transcription repressor activity,
RNA polymerase II-specific" (GO:0001227).

Dimerization: bHLH proteins generally dimerize (InterPro IEA GO:0046983). Note, however, that in a
comprehensive yeast two-hybrid survey [PMID:9371806 "Hairy displays no interactions with any of
the HLH proteins tested"] — Hairy did **not** heterodimerize with proneural/E(spl)/Da bHLH
proteins; its key partner is the non-bHLH corepressor Groucho. So the generic "protein
dimerization activity" IEA is defensible at the family level (bHLH-O homodimerization) but Hairy
does not promiscuously heterodimerize with class I/II bHLH factors.

## 3. Repression mechanism: Groucho recruitment via WRPW (and CtBP)

The core mechanistic function is recruitment of the **Groucho (Gro/TLE)** corepressor through the
C-terminal WRPW tetrapeptide: [PMID:8649374 "These results directly demonstrate that Groucho
family proteins are active transcriptional corepressors for Hairy-related proteins and are
recruited by the 4-amino acid protein-protein interaction domain, WRPW"]. In transgenic embryos,
[PMID:9892668 "Hairy-mediated repression depends on the Groucho interaction sequence (WRPW)"] and
Hairy is one of "the two long-range repressors, Hairy and Dorsal, [that] recruit a different
corepressor protein, Groucho" [PMID:9892668 "the two long-range repressors, Hairy and Dorsal,
recruit a different corepressor"]. A direct Hairy–Groucho physical interaction was also shown in a
neural-fate two-hybrid network: [PMID:9371806 "It does interact with the non-HLH protein
Groucho"].

Hairy additionally contacts the **CtBP** corepressor through a weak C-terminal PLSLV motif:
[PMID:9524128 "dCtBP interacts" specifically and directly with a small, previously uncharacterized
C-terminal region of Hairy], and dCtBP is [PMID:9524128 "essential for proper embryonic
segmentation"]. However, in vivo the WRPW/Groucho pathway is dominant and the two corepressors can
act antagonistically: [PMID:9892668 "recruit a different corepressor" and dCtBP/Gro "mediate
separate pathways of transcriptional repression"]. The Groucho/WRPW paradigm generalises to other
FRPW/WRPW repressors (e.g. Huckebein) [PMID:10433905 "WRPW Groucho-recruitment domain found in"
Hairy-related repressor proteins].

Both **CtBP** and **Groucho** are transcription corepressors; therefore several GOA "protein
binding" (GO:0005515) IPI annotations whose actual partner is Groucho or CtBP are more informatively
captured as **transcription corepressor binding (GO:0001222)**.

## 4. Post-translational regulation (E3 ligases bind Hairy)

Two RING E3 ubiquitin ligases bind Hairy and antagonise its repression:
- **Topors (dTopors)**: [PMID:14871887 "binds specifically to the basic region of Hairy"] and
  [PMID:14871887 "dTopors mediates Hairy polyubiquitination"], targeting Hairy for regulated
  proteolysis required for correct segmentation.
- **Degringolade (Dgrn)**, a SUMO-targeted ubiquitin ligase: [PMID:21343912 "Dgrn is a negative
  regulator of the repressor Hairy and its corepressor Groucho"], where [PMID:21343912 "it targets
  Hairy for SUMO-independent ubiquitylation that inhibits the recruitment of its corepressor Gro"].

Because both partners are ubiquitin ligases that bind Hairy, the corresponding "protein binding"
IPIs are more informatively **ubiquitin protein ligase binding (GO:0031625)**.

## 5. Biological processes

### 5a. Pair-rule segmentation (CORE)
Hairy is a **primary pair-rule / segmentation gene**: [PMID:9524128 "hairy is a Drosophila
pair-rule segmentation gene that functions genetically as" a repressor]. It represses *fushi
tarazu (ftz)*: [PMID:7768186 "runt and hairy are required for the proper" transcriptional
regulation of ftz], acting through an fDE1 element where ftz expression depends on "activation by
runt and repression by hairy" [PMID:7768186 "repression by hairy"]. In the segmentation-evolution
literature Hairy is grouped among the [PMID:15382142 "primary pair-rule genes of Drosophila"].
Supports: periodic partitioning by pair rule gene (GO:0007366), trunk segmentation (GO:0035290),
posterior head segmentation (GO:0035289), anterior/posterior pattern specification (GO:0009952).

### 5b. Peripheral nervous system / bristle (SOP) patterning (CORE)
Hairy patterns the adult PNS by repressing proneural *achaete-scute*, controlling sensory
bristle/chaeta spacing: [PMID:7958929 "hairy is a direct" transcriptional repressor of achaete],
acting as a [PMID:7958929 "negative regulator in both embryonic segmentation and adult" PNS
development]. In the neural-fate network Hairy is one of the proneural antagonists
[PMID:9371806 "antagonized by" the products of E(spl), hairy, and extramacrochaetae]. Supports:
regulation of neurogenesis (GO:0050767), nervous system development (GO:0007399).

### 5c. Pleiotropic / peripheral roles (NON-CORE)
- **Salivary gland / tube morphogenesis**: a new hairy allele causes salivary tube defects, but
  **indirectly**, via failure to repress *huckebein*: [PMID:12526813 "hairy mutations cause
  branching and bulging of the normally" unbranched salivary tube, in part through
  [PMID:12526813 "prolonged expression of huckebein"]]. These are downstream morphogenetic
  consequences of loss of Hairy repression, not a distinct molecular function — keep as non-core
  (GO:0007435, GO:0035239, GO:0000902).
- **Hypoxia tolerance / metabolic switch**: in laboratory-selected hypoxia-tolerant flies,
  [PMID:18927626 "The transcriptional suppressor, hairy, was up-regulated" in the microarrays],
  with [PMID:18927626 "hairy acting as a metabolic switch"] repressing metabolic genes. Genuine
  but pleiotropic/context-specific — keep as non-core (GO:0001666).
- **Sxl repression assay**: Hairy is used as a WRPW/Gro-dependent repressor tool where
  [PMID:25569482 "Repression depends on the WRPW motif of Hairy"] — supports negative regulation
  of transcription (consistent with the core repressor function).

## 6. Localization
Nucleus (UniProt PROSITE-derived; bHLH DNA-binding TF). GOA carries nucleus by IBA, IEA, and IC
(GO:0005634) — all consistent and accepted.

## 7. Over-annotation flags
- **GO:0061024 membrane organization (TAS, PMID:12593813)**: PMID:12593813 is a *Current Biology*
  dispatch on tube lumen size / intracellular vesicle transport; it does not describe a Hairy
  molecular function. "Membrane organization" for a sequence-specific nuclear transcriptional
  repressor is a distal phenotypic-consequence annotation (via hkb-dependent salivary tube
  effects), not a function of Hairy — flag as over-annotated.
- **GO:0007424 open tracheal system development (IMP, PMID:15848387)**: the cached full text of
  PMID:15848387 (available) does not mention "hairy" (0 occurrences); the paper foregrounds btl,
  pointed, kni/knrl. Cannot verify the supporting evidence for hairy from the cache — mark
  UNDECIDED rather than accept or remove an experimental IMP.
- **Bare GO:0005515 protein binding IPIs**: uninformative, but the partner is always named by the
  GOA `WITH/FROM` column and resolved by the `CC INTERACTION` block of `hairy-uniprot.txt`
  (CtBP `O46036` at line 126; gro `P16371` at line 128; gro isoform 2 `P16371-2` at line 129).
  Where the partner is Groucho/CtBP → corepressor binding (GO:0001222); where the partner is an
  E3 ligase (Topors, Dgrn) → ubiquitin protein ligase binding (GO:0031625); Ubx (Hox) partner kept
  as non-core. The two rows previously left UNDECIDED are covered by the same rule and should not
  have been: PMID:17898168 has `WITH/FROM = UniProtKB:P16371-2` and PMID:19805071 has
  `WITH/FROM = UniProtKB:P16371`, both Groucho → GO:0001222. Being unable to confirm an interaction
  from an abstract is irrelevant when the partner is supplied as curated data.

## 8. Core function summary
1. **Sequence-specific DNA-binding transcriptional repressor** (bHLH-O; N-box/class-C sites) —
   GO:0001227 / GO:0000978.
2. **Groucho corepressor recruitment via the C-terminal WRPW motif** — GO:0001222, driving
   long-range repression.
3. Deployed in **pair-rule segmentation** (GO:0007366) and **PNS/bristle patterning via
   achaete-scute repression** (GO:0050767) in the **nucleus** (GO:0005634).

## 9. Reference-block sweep (round 2 review follow-up)

When the five bare-`protein binding` IPIs were switched to `MODIFY → GO:0001222`, the matching
`reference_review` blocks in the `references:` list were not swept and still asserted the
superseded "left UNDECIDED" verdicts. Corrected here for `PMID:17898168` and `PMID:19805071`:
`correctness: UNVERIFIED` is retained, because it is a claim about what the *cached text*
supports, but the prose now records that the partner comes from the GOA `WITH/FROM` column
(`UniProtKB:P16371-2` and `UniProtKB:P16371`, both gro) rather than from the paper.

Also added `UniProtKB:P14003` as a reference so the two Groucho `MODIFY` rows carry a
`supported_by` anchor. The SUBUNIT block is the right source, since the partner is curated
input data rather than something asserted by either cited paper
[UniProtKB:P14003 "Interacts with gro (via WPRW motif)"].
