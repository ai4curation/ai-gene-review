# FTCD (Formimidoyltransferase-cyclodeaminase) — review notes

UniProt: O95954 (FTCD_HUMAN). Gene: FTCD, HGNC:3974, chromosome 21q22.3.
All primary facts below are grounded in the local UniProt record
(`file:human/FTCD/FTCD-uniprot.txt`), the GOA TSV, and cached publications.

## Core biology

FTCD is a **bifunctional enzyme** ("Multifunctional enzyme" keyword) that catalyzes
the last two steps of L-histidine catabolism, channeling the histidine-derived
one-carbon (formimino) unit into the folate one-carbon pool.

UniProt names two catalytic activities [file:human/FTCD/FTCD-uniprot.txt "Formimidoyltransferase-cyclodeaminase"]:

1. **Glutamate formimidoyltransferase** (EC 2.1.2.5), N-terminal domain:
   [file:human/FTCD/FTCD-uniprot.txt "Reaction=5-formimidoyltetrahydrofolate + L-glutamate = N-formimidoyl-L-"]
   i.e. transfers the formimino group between N-formimidoyl-L-glutamate and
   tetrahydrofolate. The physiological direction produces L-glutamate +
   5-formimino-THF from N-formimino-L-glutamate + THF. → GO:0030409.
2. **Formimidoyltetrahydrofolate cyclodeaminase** (EC 4.3.1.4), C-terminal domain:
   [file:human/FTCD/FTCD-uniprot.txt "Reaction=5-formimidoyltetrahydrofolate + 2 H(+) = (6R)-5,10-"]
   converts 5-formimino-THF to 5,10-methenyl-THF, releasing NH4+. → GO:0030412.

FUNCTION summary: [file:human/FTCD/FTCD-uniprot.txt "Folate-dependent enzyme, that displays both transferase and"]
[file:human/FTCD/FTCD-uniprot.txt "formiminoglutamate to the folate pool."]

PATHWAY: [file:human/FTCD/FTCD-uniprot.txt "Amino-acid degradation; L-histidine degradation into L-"]
(UniPathway UPA00379/UER00555; Reactome R-HSA-70921 Histidine catabolism, and the
FTCD reaction R-HSA-70920).

Domain architecture [file:human/FTCD/FTCD-uniprot.txt]: N-subdomain (1-181) +
C-subdomain (182-326) = formiminotransferase; linker (327-334); C-terminal
cyclodeaminase/cyclohydrolase (335-541). Active sites: His82 (formimidoyltransferase),
residue 412 (cyclodeaminase). SIMILARITY: N-terminal formiminotransferase family;
C-terminal cyclodeaminase/cyclohydrolase family.

Quaternary structure: **homooctamer** ("Homooctamer, including four polyglutamate
binding sites. The subunits are arranged as a tetramer of dimers, and form a planar
ring-shaped structure") — supports folic-acid (polyglutamate) binding, GO:0005542.

## Localization

Primary: **cytosol** — [file:human/FTCD/FTCD-uniprot.txt "Cytoplasm, cytosol"].
This is where catalysis occurs (Reactome "Cytosolic formimidoyltransferase-cyclodeaminase (FTCD)").
Human IDA support: PMID:14697341 reports the antigen "free in the cytosol and
associated with the Golgi membranes".

Secondary, genuine localizations:
- **Golgi apparatus / Golgi membrane** — the historical "58K Golgi protein" is FTCD.
  [file:human/FTCD/FTCD-uniprot.txt "Golgi apparatus"]. Human data: PMID:14697341
  "The human formiminotransferase-cyclodeaminase binds reversibly to the Golgi
  membranes". Reversible association, not the catalytic compartment → non-core.
- **Centrosome / centriole** — [file:human/FTCD/FTCD-uniprot.txt
  "microtubule\n... organizing center, centrosome, centriole"] from PubMed:16534631
  (Golgi 58K protein localized to the centrosome; "More abundantly located around the
  mother centriole"). Secondary/structural → non-core.
- **ER / ERGIC / smooth ER membrane** — ISS from rat ortholog (O88618) and one human
  IDA (GO:0030868 smooth ER membrane, PMID:14697341). Membrane-associated pool,
  non-core.

## Cytoskeleton / vimentin — treat with caution for human

UniProt FUNCTION (by similarity to mouse O88618):
[file:human/FTCD/FTCD-uniprot.txt "Binds and promotes bundling of vimentin filaments originating"]
[file:human/FTCD/FTCD-uniprot.txt "from the Golgi."]
This underlies the microtubule-binding (GO:0008017), cytoskeleton-organization
(GO:0007010) annotations, all transferred by ISS/IEA from the rat/mouse ortholog.

**Important human-specific caveat:** the dedicated human study explicitly found NO
cytoskeleton interaction: PMID:14697341 abstract — "human formiminotransferase-
cyclodeaminase does not interact with liver-specific cytoskeleton proteins" and "In
rats, this octameric protein ... binds brain microtubules (MTs) and vimentin". So the
vimentin/MT-bundling activity is documented for rat/mouse but was not reproduced for
the human protein. The human GO:0008017 microtubule-binding IDA (PMID:14697341,
BHF-UCL) is therefore weakly supported / arguably contradicted by that same paper's
abstract; I mark it and the derived cytoskeleton terms as over-annotations rather than
core, but retain (do not delete experimental annotations).

## Disease

**Glutamate formiminotransferase deficiency** (FIGLU-URIA, MIM:229100), autosomal
recessive; second most common inborn error of folate metabolism.
[PMID:12815595 "Glutamate formiminotransferase deficiency, an autosomal recessive
disorder and the second most common inborn error of folate metabolism, is presumed to
be due to defects in the bifunctional enzyme glutamate formiminotransferase-
cyclodeaminase (FTCD)"]. Hallmark: urinary FIGLU excretion on histidine loading;
severe form has megaloblastic anemia + intellectual disability. Disease variants
R135C and R299P reduce formiminotransferase activity to 61% and 57% of wild-type
respectively in porcine-FTCD mutagenesis [PMID:12815595 "the R135C mutation reduced
formiminotransferase activity to 61% of wild-type, whereas the R299P mutation reduced
this activity to 57% of wild-type"]. This is the experimental basis of the
GO:0030409 IDA.

## Autoantigen note (not a molecular function)

FTCD is the **LC1 autoantigen** in type 2 autoimmune hepatitis
[PMID:10029623 "This enzyme is a liver-specific antigen recognized by the sera of
patients with autoimmune hepatitis"; PMID:14697341 "hFTCD is the autoantigen
recognized by anti-liver cytosol type 1 (LC1) autoantibodies"]. Liver-enriched
expression (UniProt HPA "Tissue enriched (liver)"). This is a disease/immunology
observation, not a GO molecular function.

## Protein–protein interactions

The GO:0005515 "protein binding" IPIs come from two large systematic binary
interactome screens (PMID:25416956 Rolland et al. Cell 2014; PMID:32296183 Luck et al.
HuRI, Nature 2020). These are high-throughput Y2H maps with no FTCD-specific
functional follow-up; the interactors (AGR2, CCDC183, HGS, KASH5, MED4, PALS1) do not
point to a coherent additional function. Bare "protein binding" is uninformative →
over-annotated.

## Annotation decisions (summary)

- GO:0030409 glutamate formimidoyltransferase activity — CORE MF (IDA PMID:12815595).
- GO:0030412 formimidoyltetrahydrofolate cyclodeaminase activity — CORE MF (IBA/ISS;
  by homology, EC 4.3.1.4; second catalytic activity of this bifunctional enzyme).
- GO:0005542 folic acid binding — accept (genuine THF/polyglutamate substrate binding).
- GO:0003824 catalytic activity, GO:0016740 transferase activity — over-annotated
  (generic parents of the specific catalytic terms).
- GO:0006760 folic acid-containing compound metabolic process — CORE BP (channels
  one-carbon unit into folate pool). L-histidine catabolic process (GO:0006548) is the
  more specific missing BP → proposed.
- GO:0005829 cytosol — CORE CC.
- GO:0005737 cytoplasm — accept, non-core (general).
- Golgi (GO:0005794, GO:0000139), centriole (GO:0005814), ER (GO:0005783), ERGIC
  (GO:0005793), smooth ER membrane (GO:0030868) — genuine secondary localizations,
  KEEP_AS_NON_CORE.
- GO:0008017 microtubule binding, GO:0007010 cytoskeleton organization — over-annotated
  for human (rat/mouse property; human paper found no cytoskeleton interaction).
- GO:0005515 protein binding (×2 IPI) — over-annotated (HT interactome, uninformative).
- GO:0070062 extracellular exosome — over-annotated (urinary-exosome proteomics
  bystander detection).
</content>
</invoke>
