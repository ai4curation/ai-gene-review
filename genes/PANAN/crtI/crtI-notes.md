# crtI (P21685, *Pantoea ananatis* / *Erwinia uredovora*) — curation notes

Research journal for the de-novo review. Every assertion carries inline provenance.

## 1. Identity

UniProt P21685 is `CRTI_PANAN`, "Phytoene desaturase (lycopene-forming)", EC 1.3.99.31,
gene `crtI`, organism *Pantoea ananas (Erwinia uredovora)*, NCBI taxon 553, 492 aa
[file:PANAN/crtI/crtI-uniprot.txt "RecName: Full=Phytoene desaturase (lycopene-forming);"].

The identity chain across the three primary papers is unambiguous:

- The gene was cloned from *Erwinia uredovora* 20D3 (ATCC 19321)
  [PMID:2254247 "These genes were cloned from a phytopathogenic bacterium, Erwinia uredovora 20D3 (ATCC 19321), in Escherichia coli and located on a 6,918-bp fragment whose nucleotide sequence was determined."].
  UniProt's reference [1] is this paper and cites the same strain
  [file:PANAN/crtI/crtI-uniprot.txt "STRAIN=ATCC 19321 / DSM 30080 / NCPPB 800 / NRRL B-14773 / 20D3;"].
- The 1992 biochemistry paper expressed "the complete crtI gene encoding phytoene desaturase
  from Erwinia uredovora" [PMID:1400305 "A plasmid has been constructed by cloning the complete crtI gene encoding"].
- The 2012 structure paper states it purified this same protein under the modern genus name
  [PMID:22745782 "This allowed very high conversion rates with purified CRTI from Pantoea ananatis (formerly Erwinia uredovora), overexpressed in E. coli."].
  Its structure is PDB 4DGK, which is the structure cross-referenced from P21685
  [file:PANAN/crtI/crtI-uniprot.txt "DR   PDB; 4DGK; X-ray; 2.35 A; A=1-492."].

So all three papers describe P21685 itself, not a paralog or a same-symbol gene from another
organism. No name-confusion caveat is needed anywhere in this review.

## 2. Cached publication status

| PMID | `full_text_available:` | Use |
|---|---|---|
| PMID:1400305 (Fraser 1992, JBC) | **false** (abstract only) | source of the three IDA rows |
| PMID:2254247 (Misawa 1990, J Bacteriol) | **false** (abstract only; the "Full Text" section reproduces the abstract) | pathway position, four-step claim |
| PMID:22745782 (Schaub 2012, PLoS ONE) | **true** (XML full text) | mechanism, cofactor, acceptor, topology, structure |
| PMID:39322757 (Castaño-Cerezo 2024, EMBO J) | **true** | in-vivo corroboration in a heterologous host |

PMID:22745782 and PMID:39322757 were not in the cache and were fetched with
`uv run ai-gene-review fetch-pmid`. The two GOA-cited papers were already cached.

Note on PMID:2254247: although the cached file has a "## Full Text" heading, the content under
it is the abstract text again (`full_text_extraction_method: html_abstract_only`), so all quotes
drawn from it are abstract quotes.

## 3. What the enzyme does

**Overall reaction.** One polypeptide performs the whole phytoene-to-lycopene conversion. This
was the central conclusion of the original pathway reconstruction
[PMID:2254247 "only one gene product (CrtI) for the conversion of phytoene to lycopene is required, a conversion in which four sequential desaturations should occur via the intermediates phytofluene, zeta-carotene, and neurosporene."],
and it is what UniProt records as the catalytic activity
[file:PANAN/crtI/crtI-uniprot.txt "Reaction=15-cis-phytoene + 4 A = all-trans-lycopene + 4 AH2;"],
mapped to Rhea:RHEA:15585 and EC 1.3.99.31
[file:PANAN/crtI/crtI-uniprot.txt "Xref=Rhea:RHEA:15585, ChEBI:CHEBI:13193, ChEBI:CHEBI:15948,"].

**Purified-enzyme demonstration (the IDA source).** Fraser et al. purified the recombinant
enzyme to homogeneity, restored activity after urea removal, and showed the product directly
[PMID:1400305 "The isolated desaturase catalyzed the conversion of 15-cis-phytoene to trans-lycopene as well as to bisdehydrolycopene."].
The same abstract is the source of the FAD cofactor claim and of the NAD/NADP inhibition that
UniProt records under ACTIVITY REGULATION
[PMID:1400305 "FAD was involved in desaturation, whereas NAD and NADP were inhibitory."].

**Confirmation in a defined membrane system.** Schaub et al. reconstituted the reaction with
phytoene embedded in liposomes and saw clean conversion with no intermediate build-up
[PMID:22745782 "HPLC analysis revealed all-trans-lycopene formation at the expense of 15-cis-phytoene without accumulation of appreciable amounts of desaturation intermediates."].
The transformation comprises four desaturations plus one isomerization
[PMID:22745782 "Right, CRTI-mediated phytoene desaturation encompassing all four desaturation steps and one cis-trans isomerization step to form all-trans-lycopene."].

**In vivo, heterologous.** The 2024 study expressed P. ananatis CrtI (PaCrtI) in engineered
yeast and quantified its substrate and product intracellularly
[PMID:39322757 "For PaCrtI, the observed concentrations of phytoene (substrate) and lycopene (product) are either equivalent to or lower than those obtained with the two fungal CrtI enzymes."],
corroborating that phytoene in, lycopene out is the activity of this specific protein in a cell
and not only in a purified assay.

## 4. Cofactor and electron acceptor

FAD is the only redox cofactor
[PMID:22745782 "we conclude that FAD is the sole cofactor effective in CRTI-mediated phytoene desaturation"],
consistent with UniProt's COFACTOR line
[file:PANAN/crtI/crtI-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692;"].
FAD is not only catalytic but structural: it is required at the moment the enzyme associates
with the membrane, and cannot be supplied afterwards
[PMID:22745782 "In contrast, CRTI obtained by membrane association in the absence of FAD was inactive and could not be reactivated by subsequent addition of FAD"];
holoenzyme formation and membrane binding are one event
[PMID:22745782 "In fact, holoenzyme formation appears to occur in a cooperative manner concomitant with its association to the membrane."].
This is a strong, direct demonstration of FAD binding beyond the 1992 abstract's
"FAD was involved" phrasing, so `GO:0071949 FAD binding` is solidly grounded.

Terminal acceptor: oxygen aerobically
[PMID:22745782 "Thus, oxygen must play the role of a terminal electron acceptor."],
with quinones able to substitute anaerobically
[PMID:22745782 "Quinones were investigated as alternative electron acceptors under anaerobic conditions."].
Which acceptor operates in native *P. ananatis* is not established by any retrieved study —
recorded below as an open question rather than asserted.

## 5. Localization

UniProt: "SUBCELLULAR LOCATION: Cell membrane", evidenced from the 1992 paper
[file:PANAN/crtI/crtI-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:1400305}."].
That 1992 paper described the enzyme as membrane-integrated
[PMID:1400305 "This is the first time that a membrane-integrated carotenogenic enzyme has been purified and finally obtained in an active state."].

The 2012 structure revises the *topology* but not the *compartment*: the protein is peripheral,
not integral
[PMID:22745782 "CRTI is a membrane-peripheral oxidoreductase which utilizes FAD as the sole redox-active cofactor."],
possibly monotopic
[PMID:22745782 "The mode of membrane-association may well be monotopic"].
A peripheral or monotopic protein that does its chemistry on a bilayer-embedded substrate is
still correctly `located_in` the membrane it works on, so `GO:0005886 plasma membrane` stands.
I considered `GO:0009898 cytoplasmic side of plasma membrane` as a more precise replacement and
rejected it: no retrieved source establishes which leaflet, and the liposome work says nothing
about the native bacterial membrane's sidedness. Left as a question instead.

## 6. Reasoning on each contentious annotation

**Principle applied across the nine rows.** The electronic rows (InterPro2GO and ARBA) are
family- or domain-level rules; a correct but broad term is the appropriate output of such a
rule, and CLAUDE.md/the annotation-reviewer skill explicitly permit accepting IEAs that are
broader than the literature supports. The two IDA rows are different: they rest on an
experiment that pins the exact substrate and exact product, so the term should be as specific
as that experiment. I therefore ACCEPT all electronic rows and MODIFY only the two IDA rows
whose evidence pins the chemistry (the FAD-binding IDA is already precise, so it is ACCEPTed).

- `GO:0016491 oxidoreductase activity` IEA / InterPro:IPR002937 — IPR002937 is the generic
  amine-oxidase (Pfam PF01593) domain shared with monoamine oxidase and protoporphyrinogen IX
  oxidoreductase, a kinship the structure confirms
  [PMID:22745782 "The first crystal structure of apo-CRTI reveals that CRTI belongs to the flavoprotein superfamily comprising"].
  The root oxidoreductase term is all that domain can legitimately assert. ACCEPT, not MODIFY:
  the mapping is doing the right thing for the evidence it has.
- `GO:0016627 ... CH-CH group of donors` IDA/PMID:1400305 — true but one level above the
  demonstrated activity. `GO:0016166 phytoene dehydrogenase activity` is a verified
  (non-obsolete) child of GO:0016627 — checked via QuickGO ancestors, which returns
  `['GO:0016627', 'GO:0003824', 'GO:0016491', 'GO:0016166', 'GO:0003674']` — and matches the
  assayed reaction exactly. MODIFY.
- `GO:0016120 carotene biosynthetic process` IDA/PMID:1400305 — the experiment made lycopene
  specifically, and `GO:1901177 lycopene biosynthetic process` is a verified child of
  GO:0016120 (QuickGO ancestors for GO:1901177 include GO:0016120). MODIFY.
  I deliberately did **not** touch the GO:0016117 / GO:0016120 branch relationship: in the
  current ontology GO:0016120 is not a descendant of GO:0016117, and that is not this review's
  business to assert otherwise or "fix".
- `GO:0016117 carotenoid biosynthetic process` IEA / InterPro:IPR014105 — IPR014105 is the
  carotenoid/retinoid oxidoreductase family, and TIGR02734 `crtI_fam` matches this protein
  [file:PANAN/crtI/crtI-uniprot.txt "DR   NCBIfam; TIGR02734; crtI_fam; 1."]. Lycopene is a
  carotenoid and the module-level process is right. ACCEPT.
- Duplicated terms (GO:0016120 x2, GO:0016627 x2, GO:0071949 x2) are fine; duplicates with
  different evidence codes need no reconciliation, per the reviewer guidance.

**No REMOVE anywhere.** There is no InterPro2GO row here assigning a paralog activity the
protein lacks (nothing like squalene synthase or GGPP synthase activity appears in this GOA
file), no `GO:0005515 protein binding` row, and no negated row. Every one of the nine rows is
biologically true of this protein at some level of granularity.

**No UNDECIDED.** The two abstract-only papers are the IDA sources, but their abstracts state
the assayed result explicitly (product, cofactor, inhibitors), and the full-text 2012 paper
independently confirms every one of those claims. Nothing here required deferring.

## 7. The isomerase question (why I did *not* propose GO:0046608)

CrtI's overall reaction includes a cis-to-trans isomerization at the central double bond
[PMID:22745782 "which are capable of catalyzing the entire desaturation sequence including one cis-to-trans isomerization reaction at the central double bond"],
and the enzyme can act as an isomerase under anaerobic, reduced-FAD conditions
[PMID:22745782 "Prolycopene isomerization reactions were carried out with CRTI under anaerobic conditions and in the presence of FADred (see Experimental Procedures) with all buffers and solutions made with 2H2O."].

It is tempting to add `GO:0046608 carotenoid isomerase activity` as a NEW annotation. I checked
the term definition against what the experiment actually produced, and it fails:

- GO:0046608 is defined (QuickGO) as "Catalysis of the isomerization of poly-cis-carotenoids to
  **all-trans**-carotenoids."
- What CrtI actually did to prolycopene was partial:
  [PMID:22745782 "led to the formation of a novel tri-cis-lycopene species accompanied by smaller amounts of the half-side isomerized 7,9-di-cis-lycopene"].
  Tri-cis and di-cis products are not all-trans carotenoids, so the demonstrated activity does
  not satisfy the term's definition. This is exactly the CRTISO-versus-CrtI distinction the
  paper is drawing, not evidence that CrtI is a CRTISO.
- The physiological central-bond isomerization *is* real, but it is an internal step of the
  overall 15-cis-phytoene -> all-trans-lycopene conversion that `GO:0016166` plus Rhea:15585
  already represent; annotating it separately would double-count one reaction.

So: no NEW annotation. The gap is recorded as a suggested question and as a proposed new term
(below) instead.

## 8. Granularity gap -> proposed new term

`GO:0016166 phytoene dehydrogenase activity` is defined as "Catalysis of the dehydrogenation of
phytoene to produce a carotenoid intermediate such as phytofluene" (QuickGO), and it has **no
children** (QuickGO returns an empty child list). It is therefore used for both the plant/
cyanobacterial plastoquinone-dependent PDS reaction (EC 1.3.5.5) and the bacterial four-step
lycopene-forming CrtI reaction (EC 1.3.99.31). The repository's own pathway module records the
same problem
[file:../../../modules/carotene_backbone_biosynthesis.yaml "GO has no child of GO:0016166 specific to the"].
A child term for the lycopene-forming EC 1.3.99.31 / RHEA:15585 activity would let GO
distinguish the two mutually exclusive desaturation routes by function term rather than only by
Rhea and taxon. Entered under `proposed_new_terms`.

## 9. Open questions carried into the review

1. Native terminal electron acceptor in *P. ananatis* (oxygen vs. membrane quinone) — both work
   in vitro; neither is established in vivo.
2. Membrane sidedness/topology — peripheral and possibly monotopic is established, the leaflet
   is not, so no `GO:0009898` annotation.
3. Whether the anaerobic prolycopene isomerization has any physiological role, and whether a
   partial-isomerization GO term is warranted.
