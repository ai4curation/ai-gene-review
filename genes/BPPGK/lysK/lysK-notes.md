# LysK (Q6Y7T6) — Staphylococcus phage K endolysin — curation notes

**Provenance note.** No deep-research API keys are available in this container, so
`just deep-research` was not run and there is no `-deep-research-<provider>.md` file for
this gene. All of the material below was assembled by hand from the cached publications
in `publications/`, the UniProt flat file `lysK-uniprot.txt`, and OLS/QuickGO term
lookups. The GONUTS wiki (`gowiki.tamu.edu`), which would record the CACAO students'
per-paper evidence, was queried for `PMID:19493008` on 2026-10-29 and returned only
"This site is temporarily offline while we perform upgrades" — the same state the
CACAO project page records for batch 1.

## Identity and naming

UniProt entry `ENLYS_BPPGK` / Q6Y7T6, 495 aa, "Endolysin LysK", from *Staphylococcus*
phage K (NCBITaxon:221915, genus *Kayvirus*; known host *Staphylococcus aureus*,
`OH NCBI_TaxID=1280`). The entry carries **no gene name**: `GN ORFNames=ORF30/ORF32,
PhageK_071 {ECO:0000312|EMBL:AHB79986.1}`, and GOA therefore prints `ORF30/ORF32` in its
SYMBOL column. The literature (O'Flaherty 2005, Becker 2009, Horgan 2009,
Sanz-Gaitero 2014) uniformly calls the gene *lysK* and the protein LysK, so this review
uses `gene_symbol: lysK`, matching the folder name. `ORF30/ORF32` is an ORF designation,
not a symbol, and the stub's placeholder `Q6Y7T6` is an accession.

## Domain architecture

Three modules, N→C [PMID:19493008 "LysK is a staphylococcal bacteriophage endolysin
composed of three domains: an N-terminal cysteine, histidine-dependent
amidohydrolases/peptidases (CHAP) endopeptidase domain, a midprotein amidase 2 domain,
and a C-terminal SH3b_5 (SH3b) cell wall-binding domain."]:

- **CHAP endopeptidase**, residues 29-160 (`FT DOMAIN ... Peptidase C51`), papain-like
  cysteine protease fold with a Cys54/His117/Glu134 catalytic triad
  [PMID:25064136 "The structure of CHAP(K) revealed a papain-like topology with a
  hydrophobic cleft, where the catalytic triad is located."].
- **Amidase_2 / N-acetylmuramoyl-L-alanine amidase**, residues 205-334.
- **SH3b cell-wall-binding domain**, residues 412-481; it is required for full activity
  [PMID:19493008 "A fusion of the CHAP domain to the SH3b domain has near full-length
  LysK lytic activity, suggesting the need for a C-terminal binding domain."].

## Two catalytic activities, two bonds

Both catalytic domains were shown active on purified peptidoglycan by MS
[PMID:19493008 "Both catalytic domains are active on purified peptidoglycan by
positive-ion electrospray ionization MS."], with the cut sites identified as
[PMID:19493008 "with cleavage between d-alanine of the stem peptide and glycine of the
cross-bridge peptide, and N-acetylmuramoyl-l-alanine amidase activity"]. The structure
paper restates the division of labour
[PMID:25064136 "The LysK amidase domain cleaves peptidoglycan between N-acetylmuramic
acid and L-alanine of the stem peptide, while the CHAP domain hydrolyzes it between the
D-alanine of the tetra-peptide stem and the first glycine of the penta-glycine
cross-bridge"].

So: amidase domain = EC 3.5.1.28 (amide bond, MurNAc–L-Ala), well served by
`GO:0008745`. CHAP domain = EC 3.4.22.- , a **D-alanyl-glycyl endopeptidase**; GO has no
term for that bond specificity, and the nearest honest MF term is `GO:0004197
cysteine-type endopeptidase activity`, grounded in the papain fold and the triad.

The CHAP domain is the one that matters against live cells
[PMID:19493008 "Truncations of the LysK containing just the CHAP domain lyse
Staphylococcus aureus cells in zymogram analysis, plate lysis, and turbidity reduction
assays but have no detectable activity in a minimal inhibitory concentration (MIC)
assay."] whereas [PMID:19493008 "truncations harboring just the amidase lytic domain
show faint activity in both the zymogram and turbidity reduction assays, but no
detectable activity in either plate lysis or MIC assays."] — hence the paper's title.
Independently confirmed by [PMID:19047377 "A truncated derivative of the phage endolysin
LysK containing only the CHAP (cysteine- and histidine-dependent
amidohydrolase/peptidase) domain exhibited lytic activity against live clinical
staphylococcal isolates, including methicillin-resistant Staphylococcus aureus."].

## Metals

The CHAP domain structure (PDB 4CSH, 4CT3, 1.69-1.79 Å) resolves two metals
[PMID:25064136 "CHAP(K) contains an additional lobe in its N-terminal domain, with a
structural calcium ion, coordinated by residues Asp45, Asp47, Tyr49, His51 and Asp56."]
and [PMID:25064136 "The presence of a zinc ion in the active site was also apparent,
coordinated by the catalytic residue Cys54 and a possible substrate analogue."]. Both
were confirmed by X-ray fluorescence
[PMID:25064136 "The presence of calcium and zinc ions in the structure was confirmed by
X-ray fluorescence emission spectroscopy."]. The calcium is functionally required
[PMID:25064136 "Zymogram analysis demonstrated that mutation of residues Asp45, Asp47
and Asp56 resulted in the complete abolishment of the staphylolytic activity of the
enzyme"], the zinc is not pinned down
[PMID:25064136 "A zinc ion was found more loosely bound."]. UniProt additionally places
a Zn site in the amidase domain at 214/324/332 by similarity to D6QY02, with the note
"Zn(2+) is required for amidase activity" (by similarity to P00806). So calcium ion
binding is experimentally established; zinc ion binding is well supported but inferential.

## Activity against live staphylococci (host range)

[PMID:16199588 "These results confirmed that recombinant LysK from lactococci is
enzymatically active and capable of degrading staphylococcal cell walls."] — a 54 kDa
lytic zone on a zymogram containing heat-killed MRSA DPC5645 (Fig. 1A, lane 5), matching
the predicted mass. Kill curve: [PMID:16199588 "In kill curves using a human MRSA strain
(DPC5645), a 99% reduction in staphylococcal cell numbers was observed 1 h after the
addition of lysates containing LysK (Fig. 1B ), demonstrating that recombinant LysK is
capable of killing live pathogenic staphylococci."]. Genus-restricted:
[PMID:16199588 "The lysin-containing lactococcal extract was incapable of lysing other
gram-positive bacteria, such as Listeria innocua, Bacillus cereus, Lactobacillus
rhamnosus , and Lactobacillus paracasei ."]. Confirmed for untreated cells in
[PMID:19493008 "Both LysK and the CHAP-SH3b fusion were shown to lyse untreated S.
aureus and the coagulase-negative strains."].

Note the *lysK* transcript timing: [PMID:16199588 "Reverse transcription-PCR results
demonstrated that the lysK transcript appears between 10 and 20 min after phage
infection (data not shown)."] — late expression, consistent with a lysis-timing role,
but "data not shown".

## Direction of the interaction: what the terms must respect

LysK is encoded by the phage and acts on its **host's** peptidoglycan. Two annotation
shapes in GOA get this backwards, both of them electronic:

1. `GO:0009253 peptidoglycan catabolic process` (IEA, InterPro2GO from IPR002502 /
   IPR036505). The term sits entirely in the metabolic branch — peptidoglycan metabolic
   process → aminoglycan → macromolecule catabolic process, all under `GO:0009987
   cellular process` (checked in OLS). It describes an organism turning over *its own*
   peptidoglycan. A phage has none. The host-directed counterpart is `GO:0052009
   symbiont-mediated disruption of host cell wall`, under the interspecies-interaction
   branch. This is the same failure the CACAO batch-1 review found on PRD1 endolysin P15
   with `GO:0044277 cell wall disassembly`, arriving here by a different route
   (InterPro2GO rather than a student), which suggests the own-process/host-directed
   confusion is a property of the ontology's two parallel branches rather than of any one
   annotation pipeline.
2. `GO:0042742 defense response to bacterium` (IEA from `KW-0081` Antimicrobial). The
   phage attacks the bacterium; it does not defend itself against one. Identical to the
   PRD1 P15 case, which was reported upstream as a keyword-mapping defect.

The correct in-vivo frame is the lytic end of the infection cycle:
`GO:0001897 symbiont-mediated cytolysis of host cell`, and below it
`GO:0044659 viral release from host cell by cytolysis`. UniProt curates the release role
as an inference — "Endolysin that degrades host peptidoglycans and participates in the
sequential events which lead to the programmed host cell lysis releasing the mature
viral particles (Probable)" — and the entry carries both the `Host cell lysis by virus`
and `Viral release from host cell` keywords, yet no `GO:0044659` row reached GOA. Neither
cached paper assays progeny release during infection (both apply purified or
lysate-borne enzyme from the outside), so `GO:0001897` is the better-supported of the two
and `GO:0044659` is added here as an `IC` inference rather than claimed as demonstrated.

## CACAO rows (ASSIGNED BY = CACAO in `lysK-goa.tsv`)

| Term | Evid | PMID | Verdict |
|---|---|---|---|
| GO:0008745 N-acetylmuramoyl-L-alanine amidase activity | IDA | 19493008 | matches the MS assay exactly |
| GO:0008233 peptidase activity | IMP | 19493008 | right claim, too general — CHAP is a cysteine endopeptidase |
| GO:0001897 symbiont-mediated cytolysis of host cell | IDA | 16199588 | correct, and correctly on the interspecies branch |
| GO:0001897 symbiont-mediated cytolysis of host cell | IDA | 19493008 | same, from the live-cell lysis assays |

Notable: the students chose the host-directed `GO:0001897` where the automated pipelines
chose own-process and host-defence terms. On this gene the CACAO rows are the *better*
annotations; the errors are all electronic.

`PMID:19493008` is abstract-only in the cache (`full_text_available: false`), but its
abstract states the amidase assay, the cut sites, the CHAP-domain truncation results and
the live-cell lysis directly, so no row here rests on evidence that could not be seen.
No `REMOVE` is applied to any experimental row.

## Open questions

- Is the zinc at Cys54 catalytic, regulatory, or adventitious?
  [PMID:25064136 "Zinc ions may play a regulatory role, and their binding near Cys54
  suggests they may regulate access of the substrate to the catalytic site."]
- Does phage K use a holin, and is LysK's access to the sacculus holin-dependent as in
  PRD1? No lysis-timing or holin genetics exists for phage K, which is why the
  `GO:0044659` row is an inference.
- Why does the CHAP-only truncation lyse cells in plate and turbidity assays but score
  nothing in MIC — a potency/stability issue, or a difference in what the assays measure?
