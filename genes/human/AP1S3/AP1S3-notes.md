# AP1S3 (human, Q96PC3) — curation notes

σ1C / sigma-3, one of three interchangeable small subunits of the heterotetrameric AP-1
clathrin adaptor. 154 aa, no catalytic machinery, a single longin/roadblock fold. The gene is
best known clinically as a pustular-psoriasis susceptibility locus (PSORS15), and that
literature dominates a Europe PMC search on the symbol — but the cell-biological substance of
the gene is now carried by two high-resolution structures in which AP1S3 *itself* is the
crystallised or imaged chain, and both were missed by the affinage record.

Accession check: `AP1S3-uniprot.txt` is `ID AP1S3_HUMAN`, `AC Q96PC3;` — the expected protein,
not a merged redirect. Entry version 178, 2026-09-02.

## 1. What the gene product is

AP-1 is a cytosolic heterotetramer that coats trans-Golgi-network and endosomal membranes
[PMID:24791904 "Adaptor protein (AP) complexes are cytosolic heterotetramers that promote the
assembly and trafficking of small transport vesicles."]. Its four chains are two large
adaptins (γ/AP1G1, β1/AP1B1), a medium adaptin (μ1/AP1M1 or AP1M2) and one small adaptin —
and UniProt states plainly that the small slot is filled by any of three gene products
[file:human/AP1S3/AP1S3-uniprot.txt "(sigma-type subunit AP1S1 or AP1S2 or AP1S3)."]. So
AP1S3 is not a distinct complex, it is one of three variants of the same complex. The
ComplexPortal makes that explicit as a named object,
[file:human/AP1S3/AP1S3-uniprot.txt "DR   ComplexPortal; CPX-5049; Ubiquitous AP-1 Adaptor complex, sigma1c variant."],
whose declared composition is AP1B1:AP1G1:AP1M1:AP1S3.

Family placement: PANTHER PTHR11753 ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY. The reviewed-entry
index `interpro/panther/PTHR11753/PTHR11753-entries.csv` lists **seven** human members —
AP2S1, AP1S2, AP3S2, AP1S1, AP3S1, AP1S3, AP4S1. AP5S1 is *not* in that index, so the family
should not be described as spanning AP1–AP5 on the basis of this slice.

## 2. The two structures that actually contain AP1S3

This is the part of the record that neither the affinage report nor GOA currently reflects.

**PDB 7R4H — 2.34 Å cryo-EM, ARF1-activated AP-1 core bound to TBK1-phosphorylated STING**
(PMID:36261523). The recombinant complex is
[PMID:36261523 "His-tagged AP-1β 1–584, GST-tagged AP-1γ 1–595, AP-1μ 1–423 and AP-1σ 1–154 were cloned into a pST44 vector and referred to as AP-1 core."]
— σ 1–154, and 154 aa is AP1S3's full length. PDBe SIFTS maps chain S of 7R4H to Q96PC3
residues 1–154. The structure shows the σ subunit reading a classical acidic dileucine sorting
motif:
[PMID:36261523 "STING L364 and I365 of the EXXXLI sorting motif engage L65, F67, H85, V88 and V98 of the σ subunit through hydrophobic interactions"],
with an added phospho-readout
[PMID:36261523 "the phospho-moiety on S366 makes hydrogen bonds with a conserved basic patch formed by K60 and R61 of the σ subunit"].

**PDB 9DDT — 1.68 Å X-ray, AAGAB pseudoGTPase domain bound to AP1S3** (PMID:40752490). Here
the construct is named outright: "Full-length human AP1S3 (Uniprot Q96PC3–1)", and
[PMID:40752490 "we determined the crystal structure of wild type AAGAB psGD in complex with AP1σ3 at the resolution of 1.68 Å"].
The interface is large and specific
[PMID:40752490 "The psGD:AP1σ3 interface buries an area of 994 Å2"], and crucially it is *the
same surface* as the cargo site:
[PMID:40752490 "the aromatic side chain of F153 fits into a hydrophobic pocket lined by Y62, V88, and V98 in AP1σ3"]
and
[PMID:40752490 "Superposing our AAGAB psGD:AP1σ3 structure with AP1 or AP2 σ subunit loaded with cargo peptides immediately reveals steric clashes between the AAGAB psGD and the cargo peptides"].
AAGAB is the assembly chaperone
[PMID:40752490 "AAGAB is the assembly chaperone for AP1 and AP2 adaptor complexes that are key to clathrin-mediated membrane trafficking."]
and it is what makes a σ subunit fold at all
[PMID:40752490 "To confirm that AAGAB aids the solubility and folding of σ subunits"].

So the σ subunit of AP-1 has a real, subunit-level biochemical job: it supplies the
hydrophobic pockets that read the `[DE]XXXL[LI]` sorting signal in a cargo tail, and that same
pocket is capped by the chaperone until the tetramer is built. That is a far more informative
statement than the `protein binding` and `protein targeting` rows GOA currently carries.

### Bioinformatics check (see `AP1S3-bioinformatics/RESULTS.md`)

Because both papers describe "the σ subunit" by residue number only, I tested whether the
numbering is AP1S3's. `sigma_site_check.py` fetches Q96PC3/P61966/P56377/P53680 live, asserts
their lengths, and resolves 23 published positions.

- **22/23 resolve exactly** in AP1S3 numbering (K60, R61, L65, F67, H85, V88, V98, I103 from
  PMID:36261523; R10, K13, L40, S41, R61, Y62, A63, V88, V98, L101, Q124, R154 from
  PMID:40752490; F4, R33 from PMID:24791904).
- **One does not**: PMID:40752490 writes "AP1σ3 L101 and L104", but position 104 is
  isoleucine in AP1S3 *and* in AP1S1 (AP1S2 F104, AP2S1 V104). No AP-1 σ paralogue has Leu
  there, so this is a single-letter slip for I104; Ile and Leu are interchangeable in the
  hydrophobic packing role described, so nothing mechanistic turns on it. Recorded rather than
  smoothed over.
- **Numbering alone does not discriminate AP1S3 from AP1S1**: 20 of the 22 verified sites are
  the identical residue at the identical position in AP1S1. Only S41 (AP1S1 has A41) and R154
  (AP1S1 has E154, and runs to 158) discriminate — and both are cited by PMID:40752490, which
  independently pins that structure's numbering to AP1S3. For 7R4H the identification rests on
  the construct length (1–154) and the SIFTS mapping.
- Pairwise identity to AP1S3: AP1S1 68.8%, AP1S2 72.1%, AP2S1 44.4%.

**A caveat this analysis surfaced, and which changes what can be annotated.** The *cellular*
mutagenesis in PMID:36261523 (σKR K60A/R61A, σ V88D, σ I103S abolishing STING–AP-1 binding)
was not done on AP1S3:
[PMID:36261523 "AP1G1(R15E), AP1S1(I103S) and AP1S1(V88D) were obtained by single-amino-acid mutagenesis."]
— the plasmid is pCDNA3-HA-**AP1S1**. Because V88 and I103 are the same residue at the same
position in both paralogues, the result bears on the shared σ site, but it is loss-of-function
data on AP1S1. AP1S3's own evidence in that paper is structural (chain S of 7R4H). I therefore
do **not** propose a STING/type-I-interferon process row for AP1S3; the loss-of-function
subunit in that paper's cell work is AP1S1, and `siAP1S3` appears only in its reagent list.

## 3. Loss-of-function phenotypes that *are* AP1S3's own

**TLR3 delivery to endosomes** (PMID:24791904). Three knockdown lines, in two backgrounds, and
it is worth keeping straight which result came from which. The two stable shRNA lines are
keratinocytes —
[PMID:24791904 "we generated two stable AP1S3 -knockdown cell lines ( Figure 3 A) through the lentiviral transduction of HaCaT immortalized keratinocytes with targeted small hairpin RNA (shRNA) constructs"]
— and they carry both the trafficking readout
[PMID:24791904 "We found that TLR-3 trafficking was disrupted in both knockdown cell lines, where the ratio between endosomal and newly synthesized receptor was markedly reduced."]
and the interferon readout
[PMID:24791904 "the induction of IFNB1 transcripts was virtually abolished in one knockdown cell line and significantly reduced in the second"].
A **third**, separately generated knockdown line is HEK293 —
[PMID:24791904 "We generated another AP1S3 -knockdown cell line by silencing gene expression in HEK293 cells"]
— and it reproduces the trafficking defect but not (because it was not measured there) the
interferon one:
[PMID:24791904 "In keeping with the results obtained in HaCaT keratinocytes, we were able to show that AP1S3 deficiency resulted in reduced processing of transfected TLR-3"].
So the localisation defect is **not** keratinocyte-restricted, while the IFNB1 result is a
keratinocyte measurement. This is knockdown evidence — IMP-grade, not IDA — and GOA codes it
IMP, correctly. The readout is specifically *where TLR3 ends up*, which is why
`protein targeting` (GO:0006605) is under-informative for it and `protein localization to
endosome` (GO:0036010) is the right grain.

**Autophagosome formation** (PMID:27388993). Two independent perturbations plus a rescue:
[PMID:27388993 "We found that LC3-II levels were significantly reduced in AP1S3 knockdown versus control cell lines"]
in HaCaT, confirmed in a CRISPR knockout —
[PMID:27388993 "AP1S3 silencing causes a very significant decrease in starvation-induced LC3-II accumulation"]
— and, decisively for direction,
[PMID:27388993 "This phenotype was rescued by the overexpression of wild-type but not mutant (p.Arg33Trp) AP1S3 constructs"].
The mechanistic premise is complex-level
[PMID:27388993 "Because autophagosome formation requires a functional AP-1 complex"], i.e.
AP1S3 acts through AP-1-dependent membrane traffic rather than as autophagy machinery. Note
the knockout was made in **HEK293**, not a keratinocyte, so the autophagy requirement is not
keratinocyte-restricted; only the *inflammatory* consequence (p62 → NF-κB → IL-36α) was
studied in keratinocytes. This is the basis for proposing GO:0000045 as a NEW row.

**Disease variants.** p.Phe4Cys destabilises the protein
[PMID:24791904 "we observed decreased levels of the p.Phe4Cys protein upon transfection of mutant and wild-type (WT) constructs into human embryonic kidney 293 (HEK293) and HaCaT cells"];
p.Arg33Trp acts on assembly, not on cargo —
[PMID:24791904 "Arg33 is critically located at the AP-1 σ1C/μ1A interface"]. Both sit outside
the cargo surface mapped in 7R4H/9DDT, consistent with loss of functional complex rather than
altered cargo selectivity.

**Virus host factor** (PMID:27079945, abstract only): AP1S3 silencing in Huh7.5.1 cells
reduces HCV progeny, and AP1S3 co-immunoprecipitates HCV E2, protecting it from proteasomal
degradation. Real but a host-factor role for a viral protein, not a native function; not
proposed for annotation.

**Cancer association studies** (PMID:34367317 glioma, PMID:40555003 breast cancer): TCGA
expression correlations plus knockdown proliferation/migration assays. Too far downstream of a
housekeeping trafficking adaptor to support a process annotation.

## 4. Expression — the "restricted expression" premise does not hold

UniProt says [file:human/AP1S3/AP1S3-uniprot.txt "CC   -!- TISSUE SPECIFICITY: Widely expressed."],
Bgee reports expression in an islet of Langerhans "and 106 other cell types or tissues", and
HPA calls it [file:human/AP1S3/AP1S3-uniprot.txt "DR   HPA; ENSG00000152056; Tissue enhanced (epididymis)."]
— *enhanced*, not restricted. The only quantitative comparison in the primary literature is
PMID:27388993's survey of disease-relevant cells
[PMID:27388993 "Although transcript levels were low in neutrophils and virtually undetectable in CD4+ T lymphocytes, we observed abundant gene expression in keratinocytes"],
which is a statement about three haematopoietic/epithelial populations, not a tissue atlas.
Nothing in the record warrants down-grading the TGN/endosome location rows on expression
grounds: the compartment claims are about where the protein acts when present, and AP1S3 is
present broadly.

## 5. The single IBA, traced

GOA carries exactly one IBA: `GO:0016192 vesicle-mediated transport`, `involved_in`,
GO_REF:0000033, dated 20250902, with WITH/FROM
`CGD:CAL0000182525|FB:FBgn0039132|FB:FBgn0043012|MGI:MGI:1098244|MGI:MGI:1889383|PANTHER:PTN000204281|PomBase:SPAP27G11.06c|RGD:620188|SGD:S000003561|SGD:S000004160|UniProtKB:P53680|WB:WBGene00000157`
— the node plus eleven gene-level donors.

`interpro/panther/PTHR11753/PTHR11753-paint.tsv` contains the family's whole PAINT slice: two
IBD rows, both on **PTN000204281** — `GO:0016192` (P) and `GO:0043231` (C). The GO:0016192 IBD
row (refreshed 20260828) lists ten seeds; the 2025 IBA WITH/FROM carries the same ten plus
`FB:FBgn0043012`, which is a seed of the *other* IBD row on the same node. The difference is a
snapshot-date artefact, not a defect. No IRD or IKR row exists anywhere in this family's slice.

Donor resolution (UniProt xref lookups, ≥2 hits requested; QuickGO for each donor's own
annotations under GO:0016192 and descendants):

| WITH/FROM | resolves to | own evidence under GO:0016192 |
|---|---|---|
| CGD:CAL0000182525 | Q59QC5 APS3, *C. albicans* AP-3 σ | GO:0006896 IMP (PMID:20870878) |
| FB:FBgn0039132 | AP-1σ (CG5864), *D. melanogaster*, TrEMBL only | IEA/ISS only — no experimental |
| FB:FBgn0043012 | Q9VDC3 AP-2σ (CG6056), *D. melanogaster* | GO:0035615 IMP (PMID:20226669); GO:0016192 NAS |
| MGI:MGI:1098244 | P61967 Ap1s1 mouse | GO:0042147 IMP (PMID:24928897) |
| MGI:MGI:1889383 | Q9DB50 Ap1s2 mouse | GO:0016192 IMP (PMID:24928897); GO:0016182, GO:0036465 IDA/IMP |
| PomBase:SPAP27G11.06c | Q9P7N2 aps1/vas2 *S. pombe* | GO:0042147, GO:0099638 IDA (PMID:19624755) |
| RGD:620188 | P62744 Ap2s1 rat | GO:0098884 EXP/IDA/IMP (PMID:17289840) |
| SGD:S000003561 | P47064 APS3 *S. cerevisiae* | GO:0006896 IMP (PMID:9335339) |
| SGD:S000004160 | P35181 APS1 *S. cerevisiae* | GO:0006896 IMP (PMID:17003107) |
| UniProtKB:P53680 | AP2S1 human | GO:0048488 IDA/IMP (PMID:11102472); GO:0072583 TAS |
| WB:WBGene00000157 | Q19123 aps-2 *C. elegans* | GO:0072583 IMP (PMID:25303366) |

Ten of eleven donors carry experimental evidence, but they carry it in *different descendant
branches* — Golgi-to-vacuole transport, endosome-to-Golgi transport, clathrin-dependent
endocytosis, synaptic vesicle endocytosis, postsynaptic receptor internalisation. That is
precisely the situation in which the parent `vesicle-mediated transport` is the correct least
common ancestor, and it is why this IBA is not a granularity failure: a more specific child
would have to pick one compartment and would be wrong for the rest of the clade. Root cause
`NO_FAILURE_CORE`.

AP1S3 is not among its own donors — it has no experimental GO:0016192 of its own — so this is
not a self-referential IBA. AP1S3 sits squarely inside the clade: PANTHER classifies it into
PTHR11753 with no subfamily assignment, and it retains the entire σ fold and, per §2, the
functional cargo site.

One loose end worth recording rather than asserting: the same node carries an IBD for
`GO:0043231 intracellular membrane-bounded organelle`, but no corresponding IBA appears in
AP1S3's GOA. I do not know whether that reflects the GOA snapshot date (the IBA is 20250902,
the IBD row 20260528) or a GOA filter on very general CC terms, and I have not asserted
either.

## 6. Where the remaining 44 rows come from

- **24 TAS rows, all Reactome**, spanning the TGN-coat-assembly / cargo-capture / scission /
  uncoating reaction series, the TGN→lysosome vesicle series, HIV-1 Nef-mediated MHC-I
  downregulation, and `CLAT:AP1:CLVS bind PI(3,5)P2`. Reactome models the AP-1 σ slot as a
  set, so AP1S3 inherits every reaction the σ1A/σ1B forms get. They give ten `cytosol`, six
  `Golgi membrane`, four `trans-Golgi network membrane`, two `cytoplasmic vesicle membrane`
  and two `lysosomal membrane` rows.
- **7 NAS rows** from the ComplexPortal curation of CPX-5049: `AP-1 adaptor complex` and
  `trans-Golgi network membrane` cited to the AP-1 core structure (PMID:15377783, mouse σ1A,
  abstract-only in our cache), and `lysosomal membrane`, `early endosome`,
  `vesicle-mediated transport`, `melanosome assembly`, `platelet dense granule organization`
  cited to a Rab32/Rab38 review (PMID:23247405). That review's relevant claim is
  [PMID:23247405 "AP-1 and AP-3-to traffic specialized cargoes to"] melanosomes in melanocytes
  — an AP-1-complex-level statement, with no σ1C-specific experiment anywhere in it.
- **10 IEA**: three InterPro2GO signatures (IPR000804 clathrin small-chain conserved site,
  IPR016635 AP complex small subunit, IPR044733 AP1_sigma), two UniProt SubCell mappings
  (SL-0132 Golgi apparatus, SL-0069 clathrin-coated pit, SL-0089 cytoplasmic vesicle
  membrane), and one ARBA rule.
- **2 IPI** rows, both with partner `UniProtKB:Q6PD74` = AAGAB, from two proteome-scale
  interactome papers (PMID:25416956 Y2H; PMID:33961781 AP-MS). AAGAB is the *only* curated
  binary interactor in UniProt's INTERACTION block for this entry. With 9DDT these stop being
  uninformative: the partner is a folding/assembly chaperone and the interaction is a
  1.68 Å co-crystal.
- **1 IMP** (GO:0006605, PMID:24791904) and the single IBA above.

### The ARBA rule, checked rather than waved through

`ARBA00033972` confers exactly one annotation, `GO:0032588`, through ten unrelated condition
sets (EF-hand, protein-kinase, ARM-repeat and other FunFams, each with its own taxon
restriction). The set that fires for AP1S3 is **CS9: FunFam `3.30.450.60:FF:000005` +
taxon Catarrhini** — and `3.30.450.60:FF:000005` is precisely the FunFam UniProt assigns to
this entry ("FunFam; 3.30.450.60:FF:000005; AP complex subunit sigma"). The matching condition
set is therefore σ-specific, not an accidental fold match, and the conferred location is one
UniProt and Reactome both assert independently. Accepted.

## 7. Curation decisions, and why

- `GO:0030121 AP-1 adaptor complex` — core, and now has direct structural grounding in two
  PDB entries that contain this exact protein. ACCEPT.
- `GO:0035615 clathrin-cargo adaptor activity` (IEA, InterPro IPR044733) — accepted, with a
  recorded ontology caveat: the term's definition says "responsible for the formation of
  endocytic vesicles", which is AP-2 language, yet GO uses the term across AP-1 subunits
  (AP1G1, AP1M1, AP1M2 all carry it by IBA/IDA). The definition, not the annotation, is what
  needs fixing.
- `GO:0006605 protein targeting` (IMP) — MODIFY to `GO:0036010 protein localization to
  endosome`. The experiment measured where TLR3 arrives, and the parent term loses that.
- The two `GO:0005515 protein binding` IPI rows — MODIFY to `GO:0051087 protein-folding
  chaperone binding`. The partner is resolved (AAGAB), the functional follow-up exists
  (9DDT; solubility/folding rescue; pull-downs showing psGD is necessary and sufficient
  [PMID:40752490 "GST-AP1σ3 was able to pull down FL AAGAB and psGD, but not AAGABΔpsGD"]),
  and GO has no "assembly chaperone binding" term — GO:0051087 is the only chaperone-binding
  MF and AAGAB demonstrably performs a folding function on this client.
- `GO:1903232 melanosome assembly` and `GO:0060155 platelet dense granule organization` (NAS,
  ComplexPortal) — KEEP_AS_NON_CORE. Real AP-1 biology in melanocytes and megakaryocytes,
  inherited by the σ1C variant complex by definition rather than by experiment; no study has
  tested whether the σ1C form is the one used in those cell types.
- `GO:0005765 lysosomal membrane` (2 TAS + 1 NAS) — KEEP_AS_NON_CORE. AP-1 is on the vesicle
  that docks at the lysosome, and Reactome models scission/uncoating there; it is not a
  steady-state AP-1 compartment, and UniProt's SUBCELLULAR LOCATION does not list it.
- Ten `cytosol` TAS rows — ACCEPT. The unrecruited AP-1 tetramer genuinely is cytosolic
  (PMID:24791904, quoted in §1), and Reactome models the cytosolic pool explicitly.
- NEW: `GO:0000045 autophagosome assembly`, IMP, PMID:27388993 — two perturbations plus a
  variant-discriminating rescue, in two cell backgrounds.
- NEW: `GO:0005198 structural molecule activity`, IC from the gene's own `GO:0030121`
  membership, PMID:24791904 (the basis term is carried in `supporting_entities`, which is GO's
  convention for an IC). This is the only subunit-level MF GO can currently express for
  sigma-1C; the activity one would rather state (dileucine sorting-signal binding) is filed
  under `proposed_new_terms`, together with a second gap the AAGAB rows expose — GO has no
  `assembly chaperone binding` term, and does not even classify AAGAB itself as a chaperone
  (its own record carries `protein binding` as its only molecular function), so `GO:0051087` is
  the best existing home rather than an exact fit.

Counts, produced by `.scratch/reconcile.py` rather than typed: 45 GOA rows reconcile one-for-one
with 45 reviewed YAML entries (identical term/evidence/reference/`supporting_entities`); actions
are ACCEPT 37, KEEP_AS_NON_CORE 5, MODIFY 3, NEW 2; 12 rows carry a `propagation_review` (1 IBA,
10 IEA, and the IC NEW row whose basis term is recorded machine-readably) and every
`source_entities` list matches its row's `supporting_entities` exactly; 36 references, all with a
`reference_review`; 162 `supporting_text` quotes, all verified by `checkquotes.py`; 8
`residue_claims`, 24 checks, 0 failures.

## 8. What affinage missed, and what it got right

The record's frontmatter is clean (`self_evaluation_pairwise: win`, `faith_pct: 100.0`) and
`.affinage.log` reports "AP1S3: trust gates clear", so no gate tripped. Its six citations are all numeric PMIDs, all
real, and its narrative correctly identifies σ1C, TLR3 trafficking, autophagy/p62/IL-36 and
the HCV E2 interaction. It also honestly flags that PMID:27411398 characterises σ1A and σ1B
and not σ1C — and indeed that paper does not contain the string "AP1S3" at all.

What it missed is the entire structural literature: **PMID:36261523** (cited by UniProt as
reference [6] of this very entry, with FUNCTION and SUBUNIT evidence) and **PMID:40752490**
(the 2025 paper whose crystallised protein *is* AP1S3). Both are titled for the partner —
"Clathrin-associated AP-1 controls termination of STING signalling" and "Structural basis of
pseudoGTPase-mediated protein-protein interactions" — which is the documented affinage failure
mode: precision, not recall. Neither surfaces on a naive `AP1S3` Europe PMC search either;
36261523 was found by reading the UniProt reference list, and 40752490 by searching the PDB
accession `9DDT` that UniProt's DR lines carry. Its `mechanism_profile` grounding
(`GO:0060090 molecular adaptor activity`, `GO:0005768 endosome`) was not imported; the
grounding here is re-derived from UniProt, the structures and the GO definitions.

Also absent from affinage: **PMID:18428203**, which supplies the redundancy framing that makes
sense of AP1S3's mild, tissue-limited phenotype —
[PMID:18428203 "functional redundancy among AP-1 sigma subunits"] (σ1A, σ1B, σ1C) — and the
statement that σ subunits are essential for AP-complex stability. Abstract-only in our cache.

## 9. Open questions

1. Is there any cargo that the σ1C form of AP-1 selects and the σ1A/σ1B forms do not? Nothing
   in the record addresses this, and it is the question that would decide whether AP1S3
   deserves its own process annotations at all rather than inheriting the complex's.
2. Why is the phenotype epidermal if the gene is widely expressed and the complex redundant?
   The candidate answer in the literature is relative abundance in keratinocytes plus the IL-36
   amplification loop, but no isoform-swap experiment has been done.
3. Which AP-1 σ variant handles STING? 7R4H used AP1S3; the cellular knockdowns and mutants in
   the same paper used AP1S1. These may be interchangeable, but it has not been tested.
4. Four isoforms are annotated, two of them NMD candidates, and the MANE-Select transcript
   encodes isoform 4 (C-terminus `TMEEYMNKPTF`) while the UniProt canonical is isoform 1
   (`VSTVSQTMGER`). Both structures used isoform 1. Nothing is known about isoform-specific
   function, and no GO annotation is isoform-qualified.
