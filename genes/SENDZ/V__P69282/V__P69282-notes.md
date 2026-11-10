# Sendai virus (strain Z) protein V (UniProt P69282) — curation notes

## Provenance and scope of this research

Deep research was **unavailable** for this gene: no deep-research API keys are
configured in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists. These notes were written directly
from the cached publications in `publications/`, the UniProt flat file
`V__P69282-uniprot.txt`, PubMed, and GO/QuickGO term records.

The GONUTS wiki (`gowiki.tamu.edu`), which records the CACAO students'
evidence per PMID, is **still offline** (2026-10-29): every page redirects to
`https://gowiki.tamu.edu/maintenance.html`. This did not matter here, because
all three papers behind CACAO rows on this entry have full text cached
(`full_text_available: true`), so the student annotations could be judged
against the figures themselves.

## Identity: which protein is this?

P69282 is **protein V**, one of several products of the Sendai virus
**P/V/C gene**. UniProt's gene name for the entry is therefore `P/V/C`, and the
review keeps `gene_symbol: P/V/C` — this is the correct value taken from the
record, not a placeholder. Because the peptide shares an accession-less symbol
with its host gene, the folder follows the CLAUDE.md convention
`genes/SENDZ/V__P69282/` with `id: P69282`.

V is **not** an alternative-ORF protein in the strict sense: it is the product of
co-transcriptional RNA editing of the P mRNA. UniProt records
`RNA EDITING: Modified_positions=318`, with the note that "The sequence displayed
here is the V protein, derived from the +1G edited RNA. The unedited RNA gives
rise to the P protein (AC P04860), the +2G edited RNA gives rise to the W protein
(AC P69283)." Consequently:

- V and P share residues 1–317 (the "P/V common region"); V carries a unique
  67-residue cysteine-rich C terminus, "Vu" (318–384).
- The **C/Y proteins** are translated from an overlapping, frame-shifted ORF in
  the same gene (`MISCELLANEOUS: The P/V/C gene has two overlapping open reading
  frames. One encodes the P/V/W proteins and the other the C/Y proteins.`).
- **The literature must be read carefully**: P is the polymerase cofactor, C is a
  separate interferon antagonist (it is C, not V, that targets STAT1), and W is
  the +2G product. Claims about "the P gene products" are not automatically
  claims about V. [PMID:10933690 "the V and P proteins have the same 317 residues
  at the amino terminus (the P/V common region), while the V protein contains a
  67-residue unique carboxyl terminus (the Vu region)"]

V is dispensable for replication in cell culture but required for pathogenicity
in mice [PMID:10933690 "The V protein of Sendai virus (SeV) is nonessential to
virus replication in cell culture but indispensable to viral pathogenicity in
mice."], which is why almost every functional experiment uses a recombinant
V-deficient virus, SeV V(-), as the perturbation.

## Zinc-binding C-terminal domain (Vu)

The Vu region carries the paramyxovirus V zinc-finger-like motif
(CX3CX11CXCX2CX3CX2C; Pfam PF13008 `zf-Paramyx-P`, InterPro IPR024279). Zinc
binding was shown **directly and experimentally for SeV V**: a GST-Vu fusion
bound 65Zn, while GST-P/V-common did not [PMID:10933690 "GST-Vu bound 7.2-fold
more zinc than did GST, exhibiting its potential zinc-binding capacity"], and
the binding is cysteine-dependent [PMID:10933690 "the zinc-binding capacities of
the mutant proteins were greatly impaired"]. The metal is **zinc specifically**,
not an unspecified metal ion, so `GO:0046872 metal ion binding` understates what
is known; `GO:0008270 zinc ion binding` is the supported term. UniProt models two
Zn(2+) sites over eight ligand residues (318, 337, 341, 353, 355, 358, 362, 365).

Cysteine mutants that lose zinc binding are attenuated in mice but replicate
normally in culture, so the zinc site is a structural requirement for the
immune-antagonist function rather than a catalytic site
[PMID:10933690 "the mutant viruses were strongly attenuated in mice"].

## Innate-immune antagonism: which arm, and against what?

This is the part of the review where a recurring project-level error has to be
avoided. GO distinguishes:

- interference with **interferon production/induction** (sensing → RLR → IRF3 →
  IFN-beta transcription), for which GO has symbiont-mediated terms only at the
  level of the sensors and IRF3 (`GO:0039537` and children), and **no**
  symbiont-mediated counterpart of `GO:0032480` negative regulation of type I
  interferon production; and
- interference with **interferon signalling** downstream of the IFNAR receptor
  (`GO:0039502`), i.e. the JAK/STAT cascade.

**Everything measured for SeV V belongs to the production arm.** No assay in any
of the cited papers touches IFNAR, JAK or STAT (STAT1 antagonism in Sendai virus
is the job of the **C** protein, not V). Encouragingly, **neither CACAO nor
UniProt placed a `GO:0039502` row on this entry**, so the "wrong arm of a
bidirectional pathway" failure catalogued elsewhere in the CACAO project did not
happen here. Note, though, that UniProt's own FUNCTION prose is loose about it:
"Blocks the type I interferon signaling pathway by disrupting the RIG-I signaling
pathway (PubMed:29321315)" describes induction, not IFNAR signalling.

### IRF3 — the best-supported target

[PMID:22532687] is the central paper. In mice, MDA5 turned out to be largely
irrelevant to what V suppresses in vivo ["we infected MDA5-knockout mice with
V-deficient SeV and found that MDA5 was largely unrelated to the innate immunity
that the V protein suppresses in vivo"], which pushed the authors downstream. They
showed:

- V co-immunoprecipitates with RIG-I, MDA5 and IRF3, and with the constitutively
  active IRF3-5D (Fig. 3) ["Here we reproduced those results showing that the SeV
  V protein physically interacted with RIG-I and IRF3 as well as MDA5 by
  IP-Western blotting"].
- In SeV-infected, poly(I:C)-stimulated HeLa cells, endogenous IRF3 fails to enter
  the nucleus unless V is absent (Fig. 5) ["In SeV WT-infected cells, nuclear
  staining of IRF3 was not observed"; "These results suggest that the V protein
  also retained IRF3 in the cytosol in SeV-infected cells."].
- In an IRF3-responsive reporter assay (p-55C1B-EGFP), V blocks activation driven
  by MDA5, by constitutively active RIG-I, by constitutively active TRIF, **and by
  IRF3-5D itself** (Fig. 6) ["When the signal was induced by IRF3-5D, the IRF3
  activation was restricted in the presence of the V protein but not in the
  presence of the P/V and Vu proteins."]. Blocking a constitutively active IRF3
  is the key control: it places the block at IRF3 itself, not merely upstream.
- Across paramyxoviruses, inhibition tracks with IRF3 binding (MeV and NDV V bind
  and inhibit; MuV and NiV V do neither), which argues the interaction is the
  mechanism.

So `GO:0039548` (suppression of host cytoplasmic PRR signalling via inhibition of
IRF3 activity) is squarely supported by direct assay. Independent earlier support:
[PMID:15231393 "C or V inhibited the double-stranded (ds) RNA- or Newcastle disease virus"]
(dsRNA- or NDV-induced IRF-3 and NF-kappaB activation and IFN-beta promoter
activity; note this paper's virus mutants disrupt V/W together, and it studies C
alongside V).

### RIG-I / TRIM25

[PMID:29321315] reports that paramyxovirus V proteins bind the RIG-I CARDs and the
TRIM25 SPRY domain and thereby block TRIM25-mediated RIG-I ubiquitination and the
downstream RIG-I–MAVS interaction ["we show that V interaction with TRIM25 and
RIG-I prevents TRIM25-mediated ubiquitination of RIG-I and disrupts downstream
RIG-I signaling to the mitochondrial antiviral signaling protein"].

**Careful reading of what was done with SeV V specifically**: SeV V (Cantell
strain construct) appears only in the interaction experiments — Fig. 3A
(co-IP with TRIM25) and Fig. 3C (co-IP with RIG-I) ["Immunoprecipitation revealed
that both V proteins coprecipitated with RIG-I but not with the empty vector or
GFP-Flag"]. The functional experiments — IFN-beta reporter inhibition, the
ubiquitination block (Fig. 9) and loss of RIG-I–MAVS association (Fig. 10) — were
done with **NiV V, MeV V and PIV5 V**, not SeV V. The authors generalise on
conservation of the V C-terminal domain ["This result indicates that multiple
paramyxovirus V proteins can inhibit RIG-I ubiquitination, and thus, this is a
conserved mechanism."]. SeV-specific functional support for an effect on RIG-I
signalling comes instead from [PMID:22532687], where V inhibited IRF3 activation
driven by constitutively active RIG-I (Fig. 6C). The claim therefore stands, but
its SeV-specific basis is interaction plus a downstream reporter, not the
ubiquitination assay.

### MDA5

UniProt records the MDA5/LGP2 interaction largely "By similarity" (from P69280),
and KW-1089 drives the `GO:0039554` IEA row. SeV-specific data do exist but are
mixed: V binds MDA5 through the Vu region and reduces MDA5-driven IRF3 activation
in reporter assays [PMID:22532687 "Overexpression of MDA5 induced IRF3
activation"; "The activation was reduced in the presence of the V protein"], yet
the same paper's mouse genetics argue MDA5 is not the physiologically important
target in vivo, RIG-I is ["However, the present work showed that RIG-I is more
important for virus pathogenesis in relation to the SeV V protein."]. This is a
real but peripheral activity for this virus.

### NLRP3 inflammasome

[PMID:30021903] is a thorough, SeV-specific study: SeV V(-) infection of THP1
macrophages induces IL-1beta secretion and NLRP3 specks, which wild-type virus
does not; stable V expression suppresses LPS+ATP-driven IL-1beta; V
co-immunoprecipitates with NLRP3; truncations map binding to the region needed for
inhibition; and BRET plus speck assays show V blocks NLRP3 self-oligomerization
and NLRP3–ASC association ["we showed that the V protein of SeV inhibits NLRP3
self-oligomerization by interacting with NLRP3 to block the NLRP3-mediated ASC
oligomerization required for full activation of the inflammasome"]. Note the
interesting detail that the zinc-coordinating point mutant Vcys still bound NLRP3
and still inhibited, whereas the Vn and Vc truncations did not — so this activity
needs the whole protein rather than an intact zinc site.

**Ontology point.** The CACAO row uses `GO:1900226 negative regulation of NLRP3
inflammasome complex assembly`, whose parents are `GO:0031333 negative regulation
of protein-containing complex assembly` and `GO:1900225`: a within-organism
regulation term. For a viral protein acting on a *host* complex, GO's
interspecies branch now has `GO:0141081 symbiont-mediated suppression of host
inflammasome-mediated signal transduction` (made a child of `GO:0039537` in
2024). That term did not exist when the row was made in 2018, so this is an
instance of the project's "own-process term for a host-directed activity" shape
that has since become fixable. `GO:0141081` has no child specifying the
mechanism, so a `via inhibition of NLRP3` child is worth proposing, by analogy
with `GO:0039540` (RIG-I) and `GO:0039548` (IRF3).

## Localization

Immunofluorescence of V expressed alone shows diffuse cytoplasmic signal
[PMID:22532687 "When only the V protein was expressed, it appeared to be dispersed
in the cytosol."]; the truncations localize differently (P/V cytosolic, Vu both
cytosolic and nuclear). UniProt records `SUBCELLULAR LOCATION: Host cytoplasm
{ECO:0000269|PubMed:22532687}`. Cytoplasmic localization is functionally
meaningful rather than incidental: the mechanism against IRF3 is retention of
IRF3 in the cytosol, and the RLR sensors and NLRP3 that V engages are themselves
cytosolic.

## Summary of the functional picture

V is a multifunctional, intrinsically disordered (UniProt MobiDB-lite: residues
38–317 disordered) accessory protein with a structured zinc-binding C terminus. It
is not part of the replication machinery. It works in the host cytosol as a
protein-interaction hub that disables several arms of cytosolic innate immune
sensing: it binds and retains IRF3 (the best-supported and most downstream
target), binds RIG-I CARDs and TRIM25 to block RIG-I activation, binds MDA5, and
binds NLRP3 to prevent inflammasome assembly. The common consequence is reduced
IFN-beta and IL-1beta output and increased virulence in mice.

## CACAO assessment (4 rows, all on this entry)

| Term | Evidence | PMID | Action | Note |
|---|---|---|---|---|
| GO:0039548 inhibition of host IRF3 | IDA | 22532687 | ACCEPT | Exactly what Figs. 3-6 show, including the IRF3-5D control; correct granularity. |
| GO:0044164 host cell cytosol | IDA | 22532687 | ACCEPT | Fig. 4 images V itself; the protein, not just host machinery, is localized. |
| GO:0052170 suppression of host innate immune response | IMP | 22532687 | ACCEPT | SeV V(-) in mice/MEFs; the production-arm readout has no more specific symbiont-mediated term, so this parent is the right landing place. |
| GO:1900226 negative regulation of NLRP3 inflammasome complex assembly | IMP | 30021903 | MODIFY | Biology is right and well shown, but the term is the within-organism one; `GO:0141081` is the host-directed equivalent (it postdates the annotation). |

No "phenotype read as process", no "paper not about the gene", no single-assay
localization, and notably no interferon production/signalling arm confusion. The
one correction is ontological, not evidential.

## Other review decisions

- `GO:0046872 metal ion binding` (IEA) MODIFIED to `GO:0008270 zinc ion binding`: the
  metal is identified experimentally for this protein, so the parent understates it.
- `GO:0052029` and `GO:0052031` (IEA) called TOO_GENERAL: both are ancestors of terms
  retained here and neither names a pathway or a branch of immunity.
- `GO:0039554` (MDA5, IEA) KEPT AS NON-CORE: supported in cells, but the same paper's
  mouse genetics make it peripheral for this virus.
- One `NEW` row added: `GO:0140311 protein sequestering activity`. GOA gives this entry
  no informative molecular function, yet every process row is a consequence of a single
  activity - binding a host protein and withdrawing it from the interaction it must make
  (IRF3 from the nucleus, NLRP3 from itself and from ASC).
