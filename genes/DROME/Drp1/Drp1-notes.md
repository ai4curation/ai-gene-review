# Drp1 (Drosophila melanogaster) review notes

## Entry and fetch

- FlyBase FBgn0026479, CG3210. Reviewed accession: Q9VQE0 (isoform A, 735 aa, unreviewed TrEMBL
  entry; no FUNCTION comment; the catalytic-activity and location comments rest on ARBA rules).
  It carries 29 GOA rows, 9 of them PAINT IBA rows.
- QuickGO annotation searches with `includeFields=taxonName` still returned HTTP 500 on
  2026-11-17, so the GOA file was fetched with the project's `fetch-gene` command wrapped to drop
  only that field and fill the taxon name from taxon 7227. The rows are otherwise as QuickGO serves
  them.
- Deep research: no Falcon/Perplexity keys in this environment; the FlyBase hand-written
  description (`Drp1-deep-research-flybase.md`) is the only provider text.

## Literature searches run (PubMed E-utilities, 2026-11-17)

- `Drp1[tiab] AND peroxisom*[tiab] AND Drosophila[tiab]` (4 hits) and `Drp1 AND peroxisome AND
  Drosophila` (5 hits): the only fly peroxisome data are from the Wangler group, who expressed
  human DNM1L variants in flies (PMID:26931468, PMID:30850373). No study was found that scores
  peroxisomes after loss of fly Drp1.
- `(peroxisome fission OR peroxisome division OR peroxisomal fission OR peroxisome proliferation)
  AND Drosophila` (7 hits; nothing on fly Drp1 beyond the two above).
- `(Drp1 OR dynamin-related protein) AND microtubule* AND Drosophila` (4 hits): none tests
  microtubule binding or microtubule localization of fly Drp1. PMID:32755438 and PMID:29742430
  concern mitochondria moving on microtubules.
- `Drp1 AND Drosophila AND (GTPase activity OR GTP hydrolysis OR recombinant)` (0 hits): no
  biochemistry on the fly protein.
- `drp1 AND Drosophila AND oligomer*` (3 hits, none on Drp1 oligomerization) and `drp1 AND
  Drosophila AND (neuronal development OR dendrit* OR neurodegeneration OR photoreceptor*) AND
  (mutant* OR loss)` (7 hits).

## What Drp1 is

- The single fly member of the DNM1L/Drp1 clade of the dynamin family (PANTHER PTHR11566,
  subfamily SF21). The family root PTN000170013 is a duplication node above the split between the
  Drp1 clade and the classical dynamins, which include fly shibire
  (`Drp1-bioinformatics/RESULTS.md`).
- Domains: GTPase (Pfam Dynamin_N, 28-216), middle (Dynamin_M, 224-504) and GED (639-729), with
  no PH domain and only 6 residues after the GED; shibire and human DNM1 have a PH domain and a
  proline-rich C-terminal tail (RESULTS.md).

## Function in the fly (experimental)

- Mitochondrial fission: knockdown elongates mitochondria and overexpression fragments them in
  S2 cells [PMID:20194754 "Conversely, overexpression of Opa1 and Mfn caused a hyper-fused network
  whereas overexpression of Drp1 and Fis1 caused fragmentation"]; knockdown in lymph gland
  progenitors lengthens mitochondrial branches [PMID:34295888 "In anterior lymph gland lobes,
  mitochondrial branch length increased on Drp1 knockdown (domeGal4/+; UAS mito-GFP/+; UAS Drp1
  RNAi/+) indicating mitochondrial fission was inhibited"]; drp1 heterozygosity enhances pink1
  nulls and drp1 overexpression rescues pink1/parkin muscle phenotypes (PMID:18799731, abstract);
  required for programmed germline mitophagy and mtDNA quality control in the ovary
  (PMID:36323236, abstract).
- Location: a soluble pool and a mitochondrial pool; most Drp1-HA fractionates with mitochondria
  in adult flies [PMID:35867795 "we found that 80% of Drp1-HA is found in the mitochondrial
  fraction in heterozygous controls"]; HA-Drp1 forms foci on mitochondria in neurons
  [PMID:29249285 "In control flies, Drp1 staining appeared as discrete foci colocalized with
  mitochondria"]. Recruitment depends on Creld and on F-actin (PMID:35867795, PMID:29249285).
- Distribution of mitochondria: in drp1 mutant neurons mitochondria are largely absent from
  synapses [PMID:16055061 "DRP1 is required for proper cellular distribution of mitochondria, and
  in mutant neurons, mitochondria are largely absent from synapses"]; in spermatocytes they
  cluster [PMID:18690063 "absence of Drp1 leads to abnormal clustering of mitochondria in mature
  primary spermatocytes"].
- Development and signalling contexts: Fog-dependent ventral furrow cell shape change
  (PMID:24101729), lymph gland crystal cell differentiation with Asrij (PMID:34295888).
- Peroxisomes: human DNM1L G350R and Y691C, which fail to rescue drp1 lethality, enlarge and
  cluster peroxisomes when expressed in fly salivary glands, while wild-type DNM1L does not
  [PMID:30850373, PMC full text "Overexpression of the wild-type protein did not affect peroxisomal
  morphology"]. This is dominant-negative evidence that the fly peroxisome uses a
  Drp1-type division machinery, not a loss-of-function test of fly Drp1.

## IBA rows (PANTHER PTHR11566)

- Root PTN000170013 (duplication node): GTPase activity, cytoplasm, membrane, microtubule,
  microtubule binding.
  - GTPase activity: ACCEPT, core (all dynamins; fly Drp1 has the G1-G4 motifs).
  - cytoplasm: KEEP_AS_NON_CORE (the soluble pool; cytosol IEA row exists).
  - membrane: TOO_GENERAL (mitochondrial outer membrane is asserted).
  - microtubule binding (seed: fly shibire only) and microtubule (seeds: human DNM2, worm dyn-1,
    Arabidopsis DRP1A): MARK_AS_OVER_ANNOTATED. Placed above the paralog split; classical dynamin
    binds microtubules through its proline-rich domain, which Drp1 lacks, and no fly data exist.
    Mammalian DRP1 shows an isoform-dependent microtubule pool (the human DNM1L review keeps it as
    non-core), so the claim is not impossible, only unsupported for the fly.
- PTN008520527 (Unikonts, inside the Drp1 clade): peroxisome fission, seeded by human DNM1L, mouse
  Dnm1l and yeast Dnm1 and Vps1. ACCEPT: conserved from yeast to mammals, no loss recorded, and the
  dominant-negative DNM1L result in fly cells fits.
- PTN002480309 (Metazoa-Choanoflagellida): mitochondrial fission (ACCEPT, core), mitochondrion
  (ACCEPT), intracellular distribution of mitochondria (KEEP_AS_NON_CORE; fly drp1 mutant neurons
  lack synaptic mitochondria).

## Other decisions

- positive regulation (PMID:20194754) and regulation (PMID:24101729) of mitochondrial fission:
  MODIFY to mitochondrial fission. Drp1 is the fission GTPase; the rows' evidence is Drp1
  knockdown or overexpression changing fission, which is evidence for the process itself.
- mitochondrion organization (PMID:21274005, abstract only): MODIFY to mitochondrial fission; the
  paper uses drp1 as the fission arm in epistasis tests of mitochondrial shape.
- mitochondrion localization (PMID:16055061): MODIFY to intracellular distribution of mitochondria,
  the is_a child that the paper's result supports.
- No NEW rows.

## FlyBase description

"Dynamin related protein 1 (Drp1) encodes a dynamin-like GTPase that mediates mitochondrial
fission through a process that involves translocation to the mitochondrial outer membrane and
oligomerization. It is required for normal neuronal development and maintenance of postmitotic
neuronal function and viability."

- Traced: dynamin-like GTPase mediating mitochondrial fission (PMID:20194754, PMID:34295888);
  translocation from the cytoplasm to mitochondria (PMID:35867795, PMID:29249285); postmitotic
  neuronal function (synaptic transmission during intense stimulation, PMID:16055061).
- Not traced to fly data: oligomerization (shown for yeast Dnm1 and mammalian DRP1; no fly study
  found) and "normal neuronal development". Neither is contradicted. Correctness UNVERIFIED.
- Omissions: the role in distributing mitochondria to synapses and spermatocyte mitochondria, and
  peroxisome fission (for which fly data are indirect).
- UniProt: no FUNCTION comment, so no UniProt text to check.
