# ACRV1 (SP-10) — review notes

Working journal for the PAINT + affinage review of human ACRV1 / P26436 / ASPX_HUMAN.

## 1. What the gene is

265-aa precursor with a signal peptide (1–21), testis-restricted, product of a single
gene on chromosome 11. Named SP-10 from the MHS-10 monoclonal antibody that defined it;
`ACRV1` ("acrosomal vesicle protein 1") is the HGNC symbol. It was designated a primary vaccine
candidate
[PMID:2310816 "by a World Health Organization Taskforce on Contraceptive Vaccines"], which is why so
much of the literature is immunolocalisation rather than biochemistry.

UniProt `PE 1: Evidence at protein level` — the protein is directly sequenced
(residues 78–100, 106–122, 127–151), so this is not a gene lacking protein-level
evidence. What it lacks is *biochemical* evidence.

## 2. Localisation — the best-supported part of the record

- Immunocytochemistry on human testis and sperm places SP-10 through the whole acrosome,
  in a bilaminar array against the inner face of the outer acrosomal membrane and the
  outer face of the inner acrosomal membrane; after an ionophore-induced acrosome
  reaction it stays on the sperm head with the inner acrosomal membrane and equatorial
  segment
  [PMID:2310816 "Light and electron microscopic immunocytochemistry localized SP-10 throughout the acrosome, and electron microscopic evidence demonstrated a bilaminar array in association with the inner aspect of the outer acrosomal membrane and the outer aspect of the inner acrosomal membrane."].
- It is *not* on the surface of acrosome-intact sperm
  [PMID:2310816 "Immunofluorescence showed that SP-10 was not associated with the surface of acrosome-intact, ejaculated sperm."] —
  i.e. it is a lumenal/matrix protein of an intact secretory organelle, and only becomes
  exposed after the acrosome reaction.
- Phase partitioning shows it is *peripheral*, not integral: both the Triton X-114-released
  and TX-114-resistant pools are hydrophilic, and the resistant pool comes off with a
  chaotrope (150 mM NaSCN) or pH extremes but not with repeated detergent or 1.5 M NaCl
  [PMID:1591355 "Phase partitioning of TX-114-released and TX-114-resistant SP-10 pools showed that both were hydrophilic, indicating that these pools consist of proteins that are peripherally associated with, rather than integral to, the acrosomal membranes."].
- EM immunogold on epididymal/ejaculated/capacitated sperm concentrates label in the
  principal segment and posterior bulb of the equatorial segment; after a follicular
  fluid-induced acrosome reaction it is on the inner acrosomal membrane of the equatorial
  segment and on hybrid vesicles
  [PMID:7888499 "After a follicular fluid-induced acrosome reaction, SP-10 was detected on the inner acrosomal membrane in the equatorial segment and was associated with hybrid vesicles."].

So `GO:0001669 acrosomal vesicle` is right, and `GO:0043159 acrosomal matrix` /
`GO:0002079 inner acrosomal membrane` are the finer terms the evidence actually supports.
Neither is currently annotated.

## 3. Processing and isoform heterogeneity

Two independent sources of size heterogeneity, and the literature separates them cleanly.

- *Proteolysis.* Eight purified SP-10 peptides were Edman-sequenced; their amino termini
  map along the deduced sequence and imply endoproteases cutting after Arg (trypsin-like,
  possibly acrosin) plus after Ser, Pro, Gly and Glu
  [PMID:1637938 "endoproteases that act at five different peptide bonds are predicted to cleave SP-10: these hydrolyze following arginine (a trypsin-like protease, possibly acrosin), and following serine, proline, glycine, and glutamic acid (previously undescribed intra-acrosomal protease specificities)."].
  A ~45 kDa full-length precursor is present in testis but absent from epididymal and
  ejaculated sperm; the 25–18 kDa species first appear in caput epididymal sperm and
  nothing further happens during epididymal transit, ejaculation or capacitation
  [PMID:7888499 "no additional SP-10 bands were detected in extracts of cauda epididymal, ejaculated, or capacitated sperm, suggesting that no further processing of the 32-18-kDa SP-10 peptides occurred during epididymal transit, ejaculation, and capacitation."].
- *Alternative splicing.* Eleven authentic spliced mRNAs encoding 81–265 aa, all from
  one or two in-frame deletions in exons 2 and/or 3, with the four largest accounting for
  >99% of testis message and isoform 1 alone for 53–72%
  [PMID:7619499 "the longest SP-10 mRNA, SP10-1, which encoded a 265 amino acid protein, was consistently the most abundant, comprising 53-72% of the total SP-10 message."].

Consequence for curation, computed in `ACRV1-bioinformatics/`: mapping every UniProt
`VAR_SEQ` deletion onto the folded domain shows all nine isoforms with measurable
abundance keep the Ly-6/uPAR domain complete; only isoforms 8 and 11 (each <1% of
message, combined with the other rare ones) truncate it by 37 residues. The splice
variation therefore lengthens or shortens the low-complexity spacer, not the folded
module. That is why I set no `isoform:` field on any GOA row: GOA carries none, and the
biology does not suggest isoform-specific function. `alternative_products` (seeded from
UniProt) records the 11 forms.

## 4. Function — what is and is not established

The only functional experiments are antibody blocking.

- A mAb against human SP-10 residues 135–149 inhibited sperm–oolemma binding in the
  zona-free hamster egg penetration test but did *not* inhibit sperm–zona binding in the
  hemizona assay, and the oolemmal ligand is not a beta-1 integrin
  [PMID:10775167 "Monoclonal Ab pep-SP10 inhibited sperm-oolemma binding in the zona-free hamster egg penetration test, but it did not inhibit sperm-zona binding in the hemizona assay."],
  [PMID:10775167 "human SP-10, expressed on the equatorial region of acrosome-reacted sperm, indeed mediates sperm-oolemma binding in a beta(1) integrin-independent manner, but not sperm-zona binding"].
  The paper is candid that this was the first functional handle
  [PMID:10775167 "While the molecular characterization of the SP-10 protein has been clarified, little is yet known of its functional role in fertilization."].
- In bovine IVF, mono- and polyclonal anti-human-SP-10 reduced fertilisation rates, acting
  on sperm–zona *secondary* binding and on the ability of capacitated sperm to complete
  the acrosome reaction
  [PMID:8882296 "SP-10 antibodies exerted their anti-fertilization effect by reducing sperm-zona secondary binding."].

These two look contradictory on the zona point but are not: the hemizona assay scores
*primary* binding by acrosome-intact sperm, whereas "secondary binding" is the post-acrosome-reaction
attachment of the inner acrosomal membrane to the zona. SP-10 is inaccessible before the
acrosome reaction [PMID:2310816], so a role restricted to the post-AR steps is consistent
with both results. Worth stating explicitly because a curator reading only the two titles
would conclude the papers conflict.

**The countervailing evidence, which decides how strongly to annotate.** CRISPR knockout
of mouse *Acrv1* leaves male fertility intact:
[PMID:38697008 "We found that the average number of pups sired by each KO male was 7 to 10 pups per litter during the mating period, comparable to the WT control (about 9 pups per litter), suggesting that there was no significant difference between the fecundity of KO and WT males."],
[PMID:38697008 "Taken together, our results revealed that all 12 genes abundant in mouse testes and/or round spermatids are unnecessary for male fertility in mice by generating knockout mice for each gene."].
The same paper notes that immunising male rodents against SP-10 did not arrest
spermiogenesis
[PMID:38697008 "Furthermore, the immunization with anti-human SP-10 antibody in male rodents did not induce the arrest of spermiogenesis (Sehgal et al., 1996)."].

So: participation in the post-acrosome-reaction gamete-binding step is supported (two
species, antibody blocking), but the gene is dispensable for fertility in mouse. In GO
terms that argues for annotating participation (`GO:0007342`) while *not* claiming a
requirement, and against `GO:0007283 spermatogenesis`, which the KO histology and the
immunisation result both fail to support.

**Evidence code.** A function-blocking antibody is a specific inhibitor, so the inference
runs from a perturbation phenotype, not from direct observation of the protein acting. That
is `IMP` territory, not `IDA` — the native-versus-overexpressed distinction that first
tempted me is not the IDA/IMP discriminator. The two proposed localisation terms stay `IDA`,
because immunogold EM and phase partitioning *are* direct observations of where the protein is.

**One bovine result deliberately not annotated.** The same antibodies also
[PMID:8882296 "reduced the ability of capacitated spermatozoa to complete the acrosome reaction"],
which would suggest `GO:0007340 acrosome reaction`. Against taking it: the reagents are
anti-human antibodies applied to bovine sperm; the same abstract reports they
[PMID:8882296 "affected the motility of capacitated spermatozoa, while not affecting the motility of noncapacitated spermatozoa"],
so a general effect on capacitated cells is not excluded as the cause; and a protein that
only becomes accessible *after* the acrosome reaction is awkward to place as a participant in
triggering it. The sperm–oolemma result avoids the second objection because it used human
sperm, a defined-epitope monoclonal, and an assay scoring binding rather than progression.

## 5. Molecular function — a tested negative, not an assumption

The 1990 cloning paper concluded SP-10 was unique
[PMID:1693291 "SP-10 cDNA sequences did not show any significant homology to other sequences found in the Genbank, National Biomedical Research Foundation, or Swiss sequence banks."].
That is now superseded, and it matters because it is the reason nobody looked for a
family-based function. `ACRV1-bioinformatics/RESULTS.md` computes the current picture:

- Residues 188–264 are a canonical Ly-6/uPAR (LU, "three-finger") domain — InterPro
  IPR016054, Pfam PF00021, CDD cd23628 (`TFP_LU_ECD_SP10_like`) — carrying 10 cysteines,
  the modal count across the 38 LU domains of the 30 reviewed human LU-domain proteins.
  Every cysteine in the protein is inside this domain.
- The 166-residue region between the signal peptide and the domain is 18.7% Ser, 17.5%
  Glu, 13.3% Gly and is MobiDB-lite disordered over 62–181; it is the S-E-H-[GA]-S /
  S-G-E-H / [SV]-G-E-Q-[PSA] repeat block of [PMID:1693291].
- ACRV1 is one of 11 of 30 reviewed human LU-domain proteins with no GPI anchor, matching
  the experimental finding that it is a chaotrope-releasable peripheral protein
  [PMID:1591355]. **But anchoring is not the discriminator I first took it for**: PATE1,
  PATE4, SLURP1 and SLURP2 are unanchored too, and they are precisely the
  acetylcholine-receptor modulators. The discriminator that works is reachability — all 11
  members carrying an acetylcholine-receptor function are annotated to a secreted or
  cell-membrane location where a surface receptor can be engaged, whereas ACRV1's only
  annotated location is the acrosomal lumen, and it is the sole member of the family with no
  extracellular-accessible location at all. PATE4 is the sharpest test of this and survives
  it: it shares ACRV1's acrosomal annotation but is *also* annotated as secreted.
- ACRV1 is a subfamily singleton in human: neither PTHR17571 nor cd23628 contains another
  reviewed human LU protein, so no paralogue-based transfer is available — only orthologue
  transfer (mouse Acrv1, baboon ACRV1, red fox FSA-ACR.1).
- Across the family, the most widely shared experimental MF is nicotinic acetylcholine
  receptor modulation (7/30). This is the honest complication: PATE1 and PATE4 carry
  `GO:0030548`, and the CDD model matching ACRV1 is named for SP-10 *and* the PATE-like
  proteins. Transfer is still unjustified — on topology (above), on the term not being
  family-wide, and on ACRV1 belonging to neither the Ly-6/LYNX/SLURP nor the PATE PANTHER
  subfamily — but the reason has to be stated rather than assumed, and stated correctly.

Conclusion I acted on: no MF term is currently justifiable for ACRV1. Its only
experimental MF annotation is bare `GO:0005515`, and neither its own record nor its family
supplies a specific alternative.

## 6. Resolving the GOA WITH/FROM fields

**Rows 1–2, `GO:0005737 cytoplasm` and `GO:0031982 vesicle`, IBA, GO_REF:0000033.**
WITH/FROM = `MGI:MGI:104590 | PANTHER:PTN008565525 | UniProtKB:P26436`.

- `MGI:MGI:104590` resolves (UniProt `xref:mgi-104590`, bare number — the doubled-prefix
  form 400s) to **P50289 / ASPX_MOUSE**, mouse Acrv1, the true orthologue.
- Querying what that donor itself carries (QuickGO `geneProductId=UniProtKB:P50289`,
  `goId=GO:0005737`/`GO:0031982`, `goUsage=descendants`): 5 hits each, of which **two are
  its own IDA annotations to `GO:0001669 acrosomal vesicle`** (PMID:1591350,
  PMID:16093322), plus an ISO and an IEA to the same term, plus the IBA row itself.
- `GO:0001669` is a confirmed descendant of both `GO:0005737` and `GO:0031982`
  (QuickGO ancestors of GO:0001669 include both).
- `PANTHER:PTN008565525` is an internal tree node, not a protein; PTHR17571 contains no
  other reviewed human member.
- `UniProtKB:P26436` is the gene itself — a self-referential token, which in PAN-GO
  records the curator treating the human protein as an annotated member of the node, not a
  circular inference.

So the propagation is mechanically sound and the donor is the correct orthologue, but the
term chosen is three levels *less* precise than the IDA it was drawn from, and human ACRV1
already has its own IDA to `GO:0001669`. Hence MODIFY on both rows rather than REMOVE:
the statement is true, just needlessly vague, and the fix is to say what the donor's
evidence says. The qualifier goes with it — the replacement is `located_in GO:0001669`,
matching the two existing rows for that term, not `is_active_in`, which presupposes a
molecular activity ACRV1 has not been shown to have. One caveat I record rather than
suppress: PAN-GO annotates from a restricted term set, so the vague terms may be pipeline
policy rather than a curator's misjudgement; `TERM_SCOPING_PROBLEM` describes where the
annotation sits relative to its evidence either way, and the question is put to GO Central.

**Rows 4–8, `GO:0005515`, IPI, PMID:32814053.** IntAct REST
(`/intact/ws/interaction/findInteractions/P26436`) shows all five GOA partners come from
that one publication and each is recorded three times — `two hybrid array`,
`two hybrid pooling`, `validated two hybrid` — every one with both partners
`over-expressed`, MI-score 0.56. The UniProt `NbExp=3` therefore counts **three yeast
two-hybrid variants within a single screen, not three independent methods**; the aliases
carry CCSB ORFeome clone ids (ACRV1 = CCSB_1488). IntAct also holds two interactions that
GOA did not import (TRIM68, anti-tag co-IP, PMID:33961781; CFTR, ubiquitin
reconstruction, PMID:35156780), so the five are not even the whole physical-interaction
record.

Partner identities (UniProt REST):

| accession | gene | localisation | relation to acrosome biology |
|---|---|---|---|
| P50897 | PPT1 | lysosome, secreted, Golgi, ER | palmitoyl-protein thioesterase; none reported |
| Q7Z699 | SPRED1 | cell membrane, caveola, nucleus | RTK/MAPK suppressor; none reported |
| Q86WV8 | "TSC1" | — | **unreviewed TrEMBL, 366 aa** submission "Tuberous sclerosis 1" from AAH47772; canonical TSC1 is Q92574, 1164 aa |
| Q8N5K1 | CISD2 | ER membrane, mitochondrial outer membrane | autophagy regulator; none reported |
| Q9BZ23-2 | PANK2 | cytoplasm (UniProt's named isoform 3; only isoform 1 is mitochondrial) | pantothenate kinase; none reported |

Every one is cytosol-facing. ACRV1 has a signal peptide and lives in the lumen of a
secretory organelle, so in vivo it is on the far side of a membrane from all five, and the
Y2H assay put a signal-peptide-bearing ORF in a yeast nucleus where that peptide is
inert. Add the 166-residue disordered low-complexity spacer, a canonical sticky-prey
feature, and the set reads as screen noise. Hence MARK_AS_OVER_ANNOTATED on all five
rather than REMOVE — a Y2H hit is a real observation, it just does not license a
functional claim, and `GO:0005515` conveys nothing anyway.

**Row 10, `GO:0007283 spermatogenesis`, NAS, PMID:21252238.** The cited paper is entirely
about TDP-43 as a repressor of the *mouse acrv1 promoter*
[PMID:21252238 "our study shows that TDP-43 is a transcriptional repressor and that it regulates spatiotemporal expression of the acrv1 gene during spermatogenesis"] —
`acrv1` is the transcriptional *target*, and the paper contains no assay of ACRV1 protein
function. Combined with the fertile mouse null (§4), this is an expression-timing
statement dressed as a process annotation.

## 7. Ectopic expression in tumours

A 2026 study reports ZNF280A recruiting CUX2 to the ACRV1 promoter in ovarian cancer, with
ACRV1 knockdown attenuating ZNF280A-driven AKT phosphorylation and glycolysis
[PMID:41338461 "Mechanistically, ZNF280A enhanced ACRV1 transcription by interacting with the transcription factor CUX2, thereby facilitating its recruitment to the ACRV1 promoter."],
[PMID:41338461 "Elevated ZNF280A or ACRV1 expression activated PI3K/AKT signaling and increased glycolytic enzyme expression (PKM2 and LDHA), glucose uptake, lactate production, ATP generation, and extracellular acidification rate"].
This is the only loss/gain-of-function
work on human ACRV1, but it is in cell lines aberrantly expressing a testis-restricted
protein, so it describes a consequence of ectopic expression, not a normal function. Kept
out of the annotations; raised as a question instead.

## 8. Actions taken

| GOA row | term | evidence | action |
|---|---|---|---|
| 1 | GO:0005737 cytoplasm | IBA | MODIFY → GO:0001669 |
| 2 | GO:0031982 vesicle | IBA | MODIFY → GO:0001669 |
| 3 | GO:0001669 acrosomal vesicle | IEA (SubCell) | ACCEPT |
| 4 | GO:0005515 (PPT1) | IPI | MARK_AS_OVER_ANNOTATED |
| 5 | GO:0005515 (SPRED1) | IPI | MARK_AS_OVER_ANNOTATED |
| 6 | GO:0005515 ("TSC1") | IPI | MARK_AS_OVER_ANNOTATED |
| 7 | GO:0005515 (CISD2) | IPI | MARK_AS_OVER_ANNOTATED |
| 8 | GO:0005515 (PANK2) | IPI | MARK_AS_OVER_ANNOTATED |
| 9 | GO:0001669 acrosomal vesicle | IDA (HPA) | ACCEPT |
| 10 | GO:0007283 spermatogenesis | NAS | MARK_AS_OVER_ANNOTATED |
| — | GO:0007342 fusion of sperm to egg plasma membrane involved in single fertilization | IMP (proposed) | NEW |
| — | GO:0002079 inner acrosomal membrane | IDA (proposed) | NEW |
| — | GO:0043159 acrosomal matrix | IDA (proposed) | NEW |

Two ACCEPT, two MODIFY, six MARK_AS_OVER_ANNOTATED, three NEW; no REMOVE. Nothing needed
`UNDECIDED` — every cited paper was retrievable, though only two of the fourteen cited PMIDs
(PMID:38697008, PMID:41338461) have full text cached; the other twelve are abstract-only, which is
why every conclusion here is anchored to a sentence that appears in the abstract rather than to an
inference about what the full text might contain.

## 9. Process log

- `just fetch-gene human ACRV1` — 10 GOA rows, 6 seeded (the five IPI rows collapse to one
  in the stub; expanded back to one entry per GOA row, in GOA order).
- `affinage_deep_research.py human ACRV1 --write` — trust gates clear at fetch time (no
  `self_evaluation_pairwise` score), `faith_pct: 100`,
  13 citations, all numeric PMIDs. Two claims in its narrative needed correction against
  the sources rather than being taken on trust: it presents the sperm–zona results as a
  flat contradiction, and it repeats the 1990 "no homology" conclusion without noting the
  LU domain. Both are handled above.
- Bioinformatics: `ACRV1-bioinformatics/fetch_data.py` snapshots UniProt / InterPro /
  QuickGO into `data/`; `analyze.py` recomputes `results.json` + `RESULTS.md` from the
  snapshot with no network access, so a fresh run reproduces the committed report
  byte-for-byte (verified with `diff`).
