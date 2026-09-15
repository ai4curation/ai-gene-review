# AP3S1 (sigma3A) — review notes

UniProt Q92572, 193 aa, `AP3S1_HUMAN`. Accession asserted against the fetched record:
`ID   AP3S1_HUMAN             Reviewed;         193 AA.` / `AC   Q92572;` — this is the
expected protein, not a merged accession returning something else. PANTHER family
PTHR11753 (ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY), shared with AP1S1, AP1S2, AP1S3,
AP2S1, AP3S2 and AP4S1. HGNC:2013, 5q22.3-q23.1, previous symbol CLAPS3 (HGNC REST,
checked live).

GOA seeded 30 rows, and the evidence-code census (scripted off the tsv) is one IBA, one IDA,
one IPI, two ISS, fourteen IEA, eight NAS and three TAS; by assigner, eight ComplexPortal,
six UniProt, five InterPro, four Ensembl, three PINC, two GOC, one GO_Central and one
FlyBase. Everything mechanistic about this protein is in papers GOA has not used.

## 1. What the protein is

sigma3A is the small subunit of AP-3, the adaptor that sorts transmembrane cargo out of
tubular sorting endosomes towards lysosomes and lysosome-related organelles (LROs). The GO
definition of GO:0030123 names the subunit and both of its isoforms explicitly, which
settles the complex-membership rows without argument: "A heterotetrameric AP-type membrane
coat adaptor complex that consists of beta3, delta, mu3 and sigma3 subunits and is found
associated with endosomal membranes. AP-3 does not appear to associate with clathrin in all
organisms. In at least humans, the AP-3 complex can be heterogeneric due to the existence
of multiple subunit isoforms encoded by different genes (beta3A and beta3B, mu3A and mu3B,
and sigma3A and sigma3B)."

UniProt's FUNCTION is complex-level and reflects the 1997 literature:
`CC   -!- FUNCTION: Part of the AP-3 complex, an adaptor-related complex which is` …
"It facilitates the budding of vesicles from the Golgi membrane and may be directly
involved in trafficking to lysosomes." The SUBUNIT line gives the composition and
partners: two large adaptins (AP3D1 plus AP3B1 or AP3B2), a medium adaptin (AP3M1 or
AP3M2), a small adaptin (AP3S1 or AP3S2), interaction with AGAP1, and association with
BLOC-1. Localisation is Golgi apparatus and cytoplasmic vesicle membrane, peripheral, on
the cytoplasmic side.

sigma3A and sigma3B were identified together in the paper that named AP-3
[PMID:9118953 "We have identified two closely related human proteins (sigma3A and sigma3B) that are homologous to the small chains, sigma1 and sigma2, of clathrin-associated adaptor complexes."],
and independently as subunits of the same complex in
[PMID:9151686 "Antibodies raised against recombinant delta and sigma3 show that they are the other two subunits of the adaptor-like complex."].

Where the complex acts has moved since 1997. Simpson's immunofluorescence put AP-3 "in the
Golgi region of the cell as well as with more peripheral structures"; the compartment that
survived is endosomal
[PMID:15051738 "we propose that AP-3 defines a novel pathway by which lysosomal membrane proteins are transported from tubular sorting endosomes to lysosomes."]
and, in pigment cells,
[PMID:16162817 "The results indicate that tyrosinase traffics through the early endocytic system and that mammalian AP-3 functions on early endosomes to divert tyrosinase away from a pathway leading to multivesicular endosomes and toward one leading to melanosomes."].
This matters for the `Golgi to vacuole transport` row in §6.

**A stale locus in the citation trail.** The `AP-type membrane coat adaptor complex` TAS
row cites PMID:8697810, whose title asserts "mapping to 12p 13.2 --> p13.1 of CLAPS3". That
FISH assignment is superseded: HGNC places AP3S1 at 5q22.3-q23.1, UniProt files it under
`Proteomes; UP000005640; Chromosome 5` and CCDS4123.1. The paper's other content — the 193
aa ORF, the ubiquitous 1.35 kb transcript — is correct and is what the annotations rest on,
so this is a footnote, not a reason to doubt the rows.

## 2. The molecular function: sigma3A is half of the AP-3 dileucine cargo-signal site

This is the substantive finding, and it is entirely absent from GOA. The AP-1 case was
worked out in this repository's [AP1S1 review](../AP1S1/AP1S1-notes.md); most of the
reasoning transfers, and §2.3 below records where it does not.

### 2.1 What transfers unchanged

Cargo signals come in two flavours and bind different parts of an AP complex. Tyrosine
YXXØ motifs bind the mu subunit. Acidic dileucine motifs bind **no single subunit** — they
bind the large-subunit/sigma hemicomplex:

- [PMID:14691137 "signals from the human immunodeficiency virus negative factor protein and the lysosomal integral membrane protein II interact with combinations of the gamma and sigma1 subunits of AP-1 and the delta and sigma3 subunits of AP-3, but not the analogous combinations of AP-2 and AP-4 subunits"]
- [PMID:21097499 "signals, on the other hand, do not bind to any single AP subunit but to combinations of γ-σ1, α-σ2, and δ-σ3 subunits, as demonstrated by the use of yeast three-hybrid (Y3H) and in vitro binding assays"]
- [PMID:21097499 "The requirement of residues in two subunits of each complex (γ and σ1 for AP-1, α and σ2 for AP-2, and δ and σ3 for AP-3) explains why it was necessary to use Y3H assays to detect interactions"]

The "not any single subunit" clause is what the `contributes_to` qualifier exists for, and
it is why the core function below uses `contributes_to_molecular_function`.

### 2.2 The evidence is on sigma3A specifically, not on AP-3 generically

This is the distinction a subunit review is supposed to draw, and for AP-3 it is unusually
clean, because the 2011 mutagenesis paper mutated sigma3A itself:

- [PMID:21097499 "This is evidenced by the loss of signal binding by the σ2 V88D or L103S substitutions and the homologous σ1A V88D and I103S and σ3A V94D and L109S substitutions."]
- [PMID:21097499 "In contrast, substitution of the corresponding residues in σ3A (Arg 15 and Leu 107 ) decreased the interaction of (D/E) XXX L(L/I) signals with δ-σ3A (especially in the case of tyrosinase)."]
- [PMID:21097499 "We found that interaction with γ1-σ1A depends mainly on γ1 Arg 15 , whereas interactions with the other hemicomplexes involve basic residues on both subunits, namely α Arg 21 and σ2 Arg 15 in α-σ2 and δ Arg 26 and σ3A Arg 15 in δ-σ3A"]

So for AP-3 the acidic-residue contact is genuinely shared between delta and sigma3A,
whereas in AP-1 it sits mainly on gamma1. Four distinct signals were tested against
delta-sigma3A and bound
[PMID:21097499 "we found that all of these signals interact with the AP-1 γ1-σ1A, AP-2 αC-σ2, and AP-3 δ-σ3A hemicomplexes but not with the homologous AP-4 ϵ-σ4 hemicomplex"],
and the original demonstration was
[PMID:14691137 "Thus, the ability of Nef to interact with AP-1 and AP-3 appears to be a function of the γ1–σ1A and δ–σ3A hemicomplexes."].

The specific cargo that GOA already records as an AP3S1 interactor — tyrosinase, the
`protein binding` IPI partner — is a dileucine cargo of exactly this site
[PMID:16162817 "Using this assay, the tyrosinase cytoplasmic domain interacts with hemicomplexes from AP-1 and AP-3 but not with those of AP-2 and AP-4"] and
[PMID:16162817 "we show for the first time that the cytoplasmic dileucine-based sorting signal of tyrosinase binds not only to the δ-σ3 hemicomplexes of AP-3, confirming an AP-3 interaction ( Honing et al ., 1998 ) but also to the γ1-σ1A hemicomplex of AP-1."].
That is the functional content the bare `GO:0005515 protein binding` row throws away.

### 2.3 Where the AP-1 reasoning does **not** transfer

Three places:

1. **The GO term to use.** The AP1S1 review annotated the hemicomplex activity through
   GO:0035615 `clathrin-cargo adaptor activity`, noting that the definition — "Bringing
   together a cargo protein with clathrin, responsible for the formation of endocytic
   vesicles" — names the wrong compartment for AP-1. For AP-3 that mismatch is worse, not
   equal: AP-3 is not an endocytic coat at all, it acts on endosomal exit
   [PMID:15051738], and AP-3's clathrin association is itself conditional (the GO:0030123
   definition says AP-3 "does not appear to associate with clathrin in all organisms", and
   a beta3A point mutant with a dead clathrin box gives full functional rescue
   [PMID:11807095 "a beta3A point mutant lacking a functional clathrin binding site. All six constructs assembled into complexes and were recruited onto membranes. However, only beta3A, beta3B, and the point mutant gave full functional rescue, as assayed by LAMP-1 sorting."]).
   So this review uses the parent, GO:0140312 `cargo adaptor activity`, instead. I checked
   that GO:0035615 is GO:0140312's **only** child via the QuickGO children endpoint, so
   the parent is not a lazy generalisation — it is the most specific term in that lineage
   that does not assert endocytosis.
2. **The acidic-residue contact.** In AP-1 it is mainly on the large subunit; in AP-3 both
   delta R26 and sigma3A R15 contribute (§2.2). The sigma subunit carries proportionally
   more of the AP-3 site than of the AP-1 site.
3. **A structure of the assembled complex exists for AP-3 too, and it says something the
   AP-1 structure did not.** In the human AP-3 cryo-EM structures the pocket is not empty
   and not occupied by cargo: [PMID:39705307 "Surprisingly, the dileucine cargo-binding site on σ3 is occupied by the N-terminal extension of β3"],
   with the authors proposing that "full activation requires ejection on the β3 tail,
   potentially by engagement of a dileucine cargo motif". The AP-1 structure
   (PDB 4P6Z) had a dileucine mimic bound in the sigma1 pocket; the AP-3 structure has an
   autoinhibitory occupant in the sigma3 pocket. Same site, opposite snapshot.

### 2.4 There is still no GO term for it

Checked independently rather than inherited from the AP1S1 review: QuickGO's ontology
search returns **zero** hits for `dileucine`; `targeting sequence binding` returns
GO:0089710 `endocytic targeting sequence binding`, whose definition requires "an essential
tyrosine (Y)" and internalization by clathrin-coated pits, i.e. the other motif class; and
the molecular-function children of GO:0140312 `cargo adaptor activity` are exactly one
term, GO:0035615. There is no dileucine counterpart. Hence a `proposed_new_terms` entry
and an ONTOLOGY knowledge gap, consistent with the one AP1S1 raised — the same term would
serve both genes and their large-subunit partners.

## 3. A sigma3A-specific regulatory mechanism GOA does not record

AP-3 membrane recruitment is controlled by an interaction that targets sigma3 directly:
[PMID:15469849 "Here, we report an interdomain interaction involving the ear domain of the delta subunit and the sigma3 subunit of AP-3. This interaction interferes with the binding of AP-3 to Arf but not to dileucine-based sorting signals."],
with the consequence that "the delta-ear inhibits the recruitment of AP-3 to membranes both
in vitro and in vivo and impairs the sorting of lysosomal membrane proteins". This is a
regulatory interaction *on* sigma3, not an activity *of* sigma3, so it does not become an
annotation here; it is recorded as a suggested question and as context for the structural
role in §4.

## 4. The structural role, and why it is worth a NEW row

GOA gives AP3S1 exactly one molecular-function term, `GO:0035651 AP-3 adaptor complex
binding`, which §7 argues should go. The subunit's actual subunit-level job — holding the
complex together — is annotated nowhere.

The evidence is direct and in human protein:

- The human complex was reconstituted from its four subunits including sigma3A and solved
  by cryo-EM [PMID:39705307 "To understand the mechanism of AP-3 membrane recruitment and activation, we reconstituted human AP-3 and determined multiple structures in the soluble and membrane-bound states using electron cryo-microscopy."].
  UniProt maps four of those entries to this protein — `DR   PDB; 9C59; EM; 4.30 A; S/s=1-193.`
  and three others — so chain S of the solved AP-3 core **is** AP3S1, full length.
- sigma3 is one half of a stable hemicomplex with delta, and the pairing survives loss of
  the other half: [PMID:39705307 "Comparing the binding of AP-3 hemicomplexes, it is apparent that the δ-σ3 complex binds nearly as well as the full complex, with binding of the β3-μ3 hemicomplex barely above background levels in the Arf1GTP state."]
  (the Arf1 site itself is on delta, not sigma3 — this is not a claim that sigma3A binds
  Arf1).
- Genetically, in mouse cells lacking one or the other large subunit, sigma3's partner
  dependence is explicit: [PMID:11807095 "In mocha cells, the beta3 and mu3 subunits coassemble into a heterodimer, whereas the sigma3 subunit remains monomeric. In pearl cells, the delta and sigma3 subunits coassemble into a heterodimer, whereas mu3 gets destroyed."]

Coded IDA on PMID:39705307, because the reconstitution and the structures are direct assays
of the human protein's contribution to the assembled complex; the mouse hemicomplex
genetics is cited as corroboration, not as the human evidence.

## 5. The IBA: one row, the pan-AP-sigma node, and the right LCA term

The single IBA is GO:0016192 `vesicle-mediated transport`, GO_REF:0000033, WITH/FROM
listing 11 gene-level donors plus `PANTHER:PTN000204281`.

The family PAINT slice is already in the repo
(`interpro/panther/PTHR11753/PTHR11753-paint.tsv`). PTN000204281 carries two IBD
assertions:

| node | term | aspect | seeds in the slice |
|---|---|---|---|
| PTN000204281 | GO:0043231 intracellular membrane-bounded organelle | C | 13, incl. `UniProtKB:P61966` (AP1S1) and `UniProtKB:P56377` (AP1S2) |
| PTN000204281 | GO:0016192 vesicle-mediated transport | P | 10 |

`UniProtKB:Q92572` is **not** among the seeds of either IBD, so this is not a
self-referential IBA and there is no redundancy question either way. (GO:0043231 does not
appear as an IBA row in AP3S1's GOA, so there is nothing to review for it.)

Every donor resolved:

| WITH/FROM | resolves to | subunit | how |
|---|---|---|---|
| CGD:CAL0000182525 | Q59QC5 *C. albicans* Aps3 | AP-3 sigma | UniProt `xref:cgd-` |
| FB:FBgn0039132 | *D. melanogaster* AP-1sigma (4 TrEMBL entries) | AP-1 sigma | UniProt `xref:flybase-` |
| FB:FBgn0043012 | *D. melanogaster* AP-2sigma (2 TrEMBL entries) | AP-2 sigma | UniProt `xref:flybase-` |
| MGI:MGI:1098244 | P61967 mouse Ap1s1 | AP-1 sigma1A | UniProt `xref:mgi-` |
| MGI:MGI:1889383 | Q9DB50 mouse Ap1s2 | AP-1 sigma1B | UniProt `xref:mgi-` |
| PomBase:SPAP27G11.06c | Q9P7N2 pombe vas2 | AP-1 sigma1 | UniProt `xref:pombase-` |
| RGD:620188 | P62744 rat Ap2s1 | AP-2 sigma | UniProt `xref:rgd-` |
| SGD:S000003561 | P47064 yeast Aps3 | AP-3 sigma | UniProt `xref:sgd-` |
| SGD:S000004160 | P35181 yeast Aps1 | AP-1 sigma1 | UniProt `xref:sgd-` |
| UniProtKB:P53680 | human AP2S1 | AP-2 sigma | in `PTHR11753-entries.csv` |
| WB:WBGene00000157 | Q19123 *C. elegans* aps-2 | AP-2 sigma | GO API gives synonym F02E8.3; UniProt `xref:wormbase-F02E8.3` returns aps-2 |

Eleven gene-level donors spanning AP-1, AP-2 and AP-3 sigma subunits across fungi,
nematode, fly, rodent and human. The node is the deep pan-AP-sigma ancestor, not an AP-3
node.

**That is why GO:0016192 is the correct term and not a granularity failure.** The tempting
review is "vesicle-mediated transport is vague; AP-3 does endosome-to-lysosome delivery, so
MODIFY". `GRANULARITY_MISMATCH` applies only when the donors agree and a more specific term
was available. Here they do not agree: the AP-1 sigmas work at the TGN/endosome interface,
the AP-2 sigmas in endocytosis at the plasma membrane, the AP-3 sigmas in lysosome/LRO
delivery. `vesicle-mediated transport` is precisely their least common ancestor, and a
compartment-specific term at this node would over-propagate onto the AP-1 and AP-2 members.
Verdict `NO_FAILURE_CORE`.

Two AP-3-clade donors carry their own experimental grounding for the fungal form of this
process, which is the strongest link from the node to AP3S1's own subfamily: yeast Aps3
GO:0006896 IMP PMID:9335339 (plus GO:0030123 IMP/IPI PMID:9250663), and *C. albicans* Aps3
GO:0006896 IMP PMID:20870878 (QuickGO, checked live).

**One discrepancy worth recording, checked not assumed.** The row's WITH/FROM carries
`FB:FBgn0043012`, but the GO:0016192 IBD seed list in the fetched PAINT slice does not —
it has 10 seeds, not 11. The slice's GO:0016192 row is dated 20260828 and the GOA row
20250902, so this is a snapshot difference rather than a defect; `FBgn0043012` does appear
in the same node's GO:0043231 seed list. The same difference is visible in the AP1S1
review, independently.

**Every human sigma paralog gets this identical row.** Queried via QuickGO: AP1S1
(P61966), AP1S3 (Q96PC3), AP2S1 (P53680), AP3S1 (Q92572), AP3S2 (P59780) and AP4S1
(Q9Y587) all carry GO:0016192 IBA with a byte-identical 12-entry WITH/FROM. Note that
AP2S1 is both a donor and a recipient — for *that* gene the IBA is self-referential and
legitimately so; for AP3S1 it is not.

## 6. The InterPro and UniProt-vocabulary rows

Three InterPro signatures carry six GO mappings between them, producing the five
`GO_REF:0000002` rows and contributing to the one `GO_REF:0000120` row (counted off the tsv,
not estimated). IPR000804 (clathrin adaptor small-chain conserved site, matched here as
PROSITE PS00989 on the UniProt record) maps to GO:0006886, GO:0016192 and GO:0030117 — all
three true of any AP sigma. IPR016635 ('Adaptor protein complex, sigma subunit') maps to
GO:0015031 only. Those are all correct and appropriately general.

**IPR027155 is the interesting one.** It is the AP-3-sigma-specific entry (`APS3`), and it
maps to GO:0006896 `Golgi to vacuole transport`. That term is real and not fungus-only —
GO:0090160 `Golgi to lysosome transport` is its child and lysosome is_a vacuole, so nothing
excludes mammals a priori — but the donor compartment it names is the fungal ALP pathway,
where the seed evidence sits (yeast and *C. albicans* Aps3, both IMP, §5). Human AP-3's
demonstrated route starts at the endosome, not the Golgi: [PMID:15051738] again, and
[PMID:16162817 "These data show that tyrosinase is concentrated in AP-3-coated membranes essentially of endosomal origin."].
So the row is compartment-shifted rather than wrong, and the review MODIFYs it to
GO:0008333 `endosome to lysosome transport` (verified: BP, not obsolete, is_a GO:0007041 /
GO:0016192).

The ARBA half of the GO:0030123 IEA was fetched and read
(`https://rest.uniprot.org/arba/ARBA00033921`): one condition set, `FunFam id =
3.30.450.60:FF:000001` AND `taxon = Primates`, annotating GO:0030123. That looks loose —
a FunFam plus a clade — so I checked whether the FunFam actually separates AP-3 sigmas from
the rest of the family. It does: among the seven human sigma paralogs, only AP3S1 and
AP3S2 carry `3.30.450.60:FF:000001`; AP1S1 and AP1S3 carry FF:000005, AP1S2 FF:000009,
AP2S1 FF:000004 and AP4S1 FF:000010 (UniProt `xref_funfam`, queried live). The rule is
discriminative. It does not separate sigma3A from sigma3B — but neither does anything else
(§8), and GO:0030123 is correct for both.

## 7. The one annotation that is actually wrong: `AP-3 adaptor complex binding`

GO:0035651, MF, IEA GO_REF:0000107, WITH/FROM `UniProtKB:Q9DCR2|ensembl:ENSMUSP00000025357`.

The term's definition is "Binding to an AP-3 adaptor complex", and AP3S1 **is** an AP-3
adaptor complex subunit. GO already expresses that relation, three times over, as
GO:0030123 `part_of` (IDA, NAS and IEA rows on this gene). Typing a constitutive subunit as
a *ligand* of its own complex is a role conflation, and it is the whole reason the
`part_of` relation exists.

This is not a one-off. A QuickGO query for GO:0035651 restricted to human returns 29
annotations over 28 entities, and **all seven human AP-3 subunit genes are among them** —
AP3B1, AP3B2, AP3D1, AP3M1, AP3M2, AP3S1, AP3S2 — every one of them by IEA. The entities
with experimental evidence for the term are the ones that genuinely bind AP-3 from outside:
PI4K2A (IDA), RAB32 and RAB38 (IPI). So the complex's own subunits have been swept in
alongside its binding partners.

The proximate source is the mouse Ap3s1 row, GO:0035651 IDA PMID:19010779 (QuickGO). That
paper is an AP-3 cross-linking/mass-spectrometry study in which AP-3 was the bait and
BLOC-1, BLOC-2, HOPS, clathrin and PI4KIIalpha were the associated proteins
[PMID:19010779 "AP-3 was co-isolated with BLOC-1, BLOC-2, and homotypic fusion and vacuole protein sorting complex subunits; clathrin; and phosphatidylinositol-4-kinase type II alpha (PI4KIIalpha)."] —
i.e. the subunits are the complex, not its ligands. The cache is abstract-only for that
paper, so I am not second-guessing an assay I cannot see; the argument does not need the
assay. It is that no experiment can make a constitutive subunit a ligand of the complex it
constitutes, and the row being reviewed here is the human IEA, not the mouse IDA.
`REMOVE`, `root_cause: TERM_SCOPING_PROBLEM`, `failure_modes: [ROLE_CONFLATION]`.

## 8. sigma3A versus sigma3B: inherited, and correctly so

The prompt asked whether GOA distinguishes the two sigma3 isoforms or whether AP3S1 simply
inherits. Answer, from a QuickGO diff of Q92572 (30 rows) against P59780 (25 rows):

- The **complex-level rows are shared verbatim**: the same GO:0030123 IDA (PMID:9118953),
  the same ComplexPortal NAS set (PMID:9151686, PMID:9545220, PMID:15537701, PMID:23247405),
  the same InterPro2GO rows, the same ARBA rule, and the byte-identical GO:0016192 IBA.
- The **ortholog-transfer rows are paralog-correct**, not confused: AP3S1's Compara/ISS
  donor is mouse Ap3s1 (Q9DCR2) and AP3S2's is mouse Ap3s2 (Q8BSZ2). I checked both
  accessions in UniProt rather than assuming.
- Scripted diff on (GO id, evidence code, reference): QuickGO returns 30 rows for Q92572 and
  25 for P59780, of which **24 are shared**. Six rows are unique to AP3S1 -- the three PINC
  TAS rows (PMID:8697810 cloned CLAPS3 = sigma3A; PMID:9118953; PMID:9792713), the
  `protein binding` IPI to tyrosinase (PMID:16162817), a `membrane` Compara row and the
  `presynapse` inter-ontology row that follows from AP3S1's `synaptic vesicle coating` row.
  The first four come from sigma3A-specific papers; the last two are pipeline consequences,
  not new biology. One row is unique to AP3S2, a `synaptic vesicle` IEA transferred from rat
  (UniProtKB:A0A0G2K302).

That is not curation laziness. The biochemistry says the two are interchangeable at the
tested site: [PMID:14691137 "yeast three-hybrid analyses showed that the cytosolic tail of LIMP-II interacted with γ1–σ1A, δ–σ3A, and δ–σ3B (σ3A and σ3B are two isoforms of σ3), but not with αC–σ2, ɛ–σ4, μ3A, or the VHS domain of GGA1"]
and [PMID:14691137 "Together, these experiments demonstrate that the LIMP-II cytosolic tail binds to the AP-1 and AP-3 complexes through γ1–σ1A and δ–σ3 (A or B isoforms)."].
The bioinformatics in §9 adds the sequence-level counterpart: the two proteins differ at 31
of 193 positions but are identical at every pocket residue the literature names.

Worth flagging for the sibling AP3S2 review: the Nef result *does* separate the two large
subunits, but not the sigmas — only two of five Nef variants bound delta-sigma3A
[PMID:14691137 "All five Nefs bound to γ1–σ1A, whereas only the NLA4-3 and 248 Nefs bound to δ–σ3A"] —
and sigma3B was not tested against Nef at all.

## 9. Bioinformatics: the site is retained; retention is not the evidence

`AP3S1-bioinformatics/` (`uv run python sigma3_pocket.py`) fetches ten sigma subunits live
from UniProt, asserts each length, and maps the structurally defined sigma2 pocket onto
each by pairwise alignment. Results in
`file:human/AP3S1/AP3S1-bioinformatics/RESULTS.md`. Four outcomes:

1. All five literature-named sigma3A positions verify against the live Q92572 sequence:
   R15, V94, D98, L107, L109.
2. The alignment independently reproduces both correspondences PMID:21097499 asserts
   (sigma2 88 -> sigma3A 94, sigma2 103 -> sigma3A 109), and the sigma1A pair as well. The
   mapping method is sound.
3. **The negative control defeats the conservation argument.** sigma4 (AP4S1) is in the
   same PANTHER family and its hemicomplex demonstrably does not bind these signals, yet it
   scores 4/5 identical at the pocket — the same as sigma1A, sigma1B and sigma1C, all
   binders. sigma3A scores 5/5, a better match to the sigma2 anchor than any AP-1 sigma
   (Leu, not Ile, at the sigma2 L103 position), but 5/5 versus 4/5 is not a separation when
   the non-binder is inside the 4/5 group. So "AP3S1 retains the dileucine pocket" is true
   and carries no weight by itself; the direct sigma3A mutagenesis does.
4. sigma3A vs sigma3B: 83.9% identical overall (31 differing positions), **identical at all
   five pocket positions**; and human AP3S1 vs mouse Ap3s1 is 100% identical over 193 aa,
   which is why the Compara and ISS rows in §10 are unusually safe transfers.

Recorded as `residue_claims` (RETAINED) on the molecular-function row, because that is the
checkable form — while the propagation reasoning for the IBA is explicitly *not*
residue-based and says so.

## 10. The Ensembl-Compara and ISS rows, and the perturbation behind them

Four rows come from `GO_REF:0000107` with `UniProtKB:Q9DCR2|ensembl:ENSMUSP00000025357`,
and two more restate two of them as curator ISS (`GO_REF:0000024`). Q9DCR2 is mouse Ap3s1,
checked in UniProt — the 1:1 ortholog, not the sigma3B paralog, and sequence-identical to
the human protein (§9).

The mouse sources, from QuickGO:

| term | mouse evidence | reference |
|---|---|---|
| GO:0008089 anterograde axonal transport | IMP | PMID:21998198 |
| GO:0048490 anterograde synaptic vesicle transport | IMP | PMID:21998198 |
| GO:0035651 AP-3 adaptor complex binding | IDA | PMID:19010779 |
| GO:0016020 membrane | IMP (CACAO) | PMID:16837549 |

**The perturbation in PMID:21998198 is not an Ap3s1 mutant.** The paper's genetics is the
mocha allele, `Ap3d1mh/mh` — a delta-subunit null that removes the whole complex — and
sigma3 appears as an assay readout rather than as the perturbed gene
[PMID:21998198 "Synaptosome fractions from control brains (lanes 1–8) and AP-3–deficient mocha (Ap3d1mh/mh) brains (lanes 1′–8′) were resolved on SDS–PAGE, and the contents were analyzed by immunoblot with antibodies against synaptic vesicle markers (SV2, synaptophysin), AP-3–dependent synaptic vesicle cargoes (PI4KIIα, VAMP7, ZnT3), and AP-3 σ3 subunit."].
Annotating an obligate-complex subunit from a complex-null phenotype is standard GO
practice and I am not calling it a defect. It does determine the grade: the claim is
complex-level and neuronal-context, so the axonal/synaptic-transport rows and the
inter-ontology `axon cytoplasm` row that follows from them are `KEEP_AS_NON_CORE`, not
core, for a subunit of a ubiquitously expressed adaptor. `root_cause:
NO_FAILURE_NON_CORE`.

`GO:0016020 membrane` is root-ish and uninformative — AP-3 is a peripheral membrane coat,
so it is true of the whole complex — and its mouse source is a CACAO IMP on a
BLOC-1/AP-3 interaction study [PMID:16837549]. `KEEP_AS_NON_CORE`.

## 11. The ComplexPortal NAS rows, sized by projection

Eight rows come from ComplexPortal as NAS. Rather than guess how gene-specific they are, I
counted entities per reference in QuickGO (paginated; entity counts, not annotation
counts):

| reference | annotations | entities | what that means |
|---|---|---|---|
| PMID:9118953 | 3 | 2 | Q92572 and P59780 only — the two sigma3 proteins the paper identified. Specific. |
| PMID:9151686 | 17 | 14 | the AP-3 subunits, human and mouse. Complex-level. |
| PMID:9545220 | 38 | 22 | AP-3 subunits plus eight ComplexPortal complexes. Complex-level. |
| PMID:15537701 | 39 | 15 | AP-3 subunits plus four complexes. Complex-level. |
| PMID:23247405 | 178 | 48 | AP-1, AP-3 and BLOC-2 subunits plus 16 complexes, human and mouse. Broad. |

So the melanosome-assembly, platelet-dense-granule and early-endosome rows are one
statement about AP-3 projected across every subunit, and they are graded
`KEEP_AS_NON_CORE` accordingly — real biology, cell-type-restricted, not evidence about
sigma3A. The underlying claims do hold for AP-3: pigment and platelet phenotypes are the
defining consequence of AP-3 loss
[PMID:9697856 "Our results demonstrate that the AP-3 complex is responsible for cargo selection to lysosome-related organelles such as melanosomes and platelet dense granules as well as to neurotransmitter vesicles."]
and [PMID:10024875 "Our results suggest that AP-3 functions in protein sorting to lysosomes"],
and there is a gene-level in-vivo perturbation of the *ap3s1* orthologue itself
[PMID:20713646 "partial knockdown of the analogous Ap3s1 and Ap1s1 trafficking components in zebrafish sensitized developing melanocytes to hypopigmentation in low-copper environmental conditions"].

`GO:0035654 clathrin-coated vesicle cargo loading, AP-3-mediated` is the exception among
the NAS rows: its definition is "Formation of a macromolecular complex between proteins of
the AP-3 adaptor complex and proteins and/or lipoproteins that are going to be transported
by a clathrin-coated vesicle", which is exactly the cargo-recognition step sigma3A performs
(§2). ACCEPT, core.

`GO:0016183 synaptic vesicle coating` is the one NAS row whose *term* is wrong. Its
definition is "The formation of clathrin coated pits in the presynaptic membrane endocytic
zone, triggered by the presence of high concentrations of synaptic vesicle components" —
plasma-membrane coated pits, which is AP-2's job, not AP-3's. AP-3's synaptic role is
budding vesicles from endosomes, and GO has a term for that: GO:0016182 `synaptic vesicle
budding from endosome`, defined as "Budding of synaptic vesicles during the formation of
constitutive recycling vesicles from early endosomes". MODIFY. The sibling row
`GO:0098793 presynapse`, which the inter-ontology pipeline derives from GO:0016183, is kept
as non-core on its own merits: sigma3A is a subunit of the neuronal AP-3 variant as well as
the ubiquitous one (UniProt lists `ComplexPortal; CPX-5055; Neuronal AP-3 Adaptor complex,
sigma3a variant`), and the neuronal complex is targeted to processes
[PMID:15537701 "beta3B-containing AP-3 complexes were preferentially targeted to neuronal processes."].

## 12. Insulin receptor signalling

`GO:0008286`, TAS, PMID:9792713. The paper found sigma3A in an expression-library screen
for IRS-1 binders in 3T3-L1 adipocytes and closed with a hypothesis: "These results are
consistent with the hypothesis that sigma3A serves as an IRS-1 receptor that may dictate
the subcellular localization and the signaling functions of IRS-1." No step of the insulin
receptor signalling cascade — the term's definition is "The series of molecular signals
generated as a consequence of the insulin receptor binding to insulin" — is shown to be
executed by sigma3A. Twenty-eight years on, the finding stands alone: PubMed's cited-in
link set for PMID:9792713 returns 5 citing papers (against 119 for PMID:14691137 and 70 for
PMID:21097499, same query), a PubMed search for "sigma3A adaptor" returns 2 papers total,
and UniProt's SUBUNIT line for Q92572 does not list IRS1. `MARK_AS_OVER_ANNOTATED` — an
unreplicated binding observation, not a demonstrated pathway role, and TAS rather than an
experimental code so there is no curator-read-the-full-text deference owed.

## 13. Affinage record

Trust gates clear (`self_evaluation_pairwise: win`, `faith_pct: 100.0`, and
`.affinage.log` reports "trust gates clear"). The record describes the right protein — it
opens on CLAPS3/AP3S1 as a clathrin-adaptor small chain and an AP-3 subunit, and its
UniProt accession field is Q92572 — so there is no AGT/AGXT-style symbol collision here.
The citation list is four numeric PMIDs, no bioRxiv ids. Graded `MEDIUM` / `VERIFIED`: the
four claims it makes are each traceable to their PMID, and I re-read all four.

Two cautions on its content, both checked:

- Its `mechanism_profile` proposes GO:0060090 `molecular adaptor activity`. Not imported.
  Re-grounded from the narrative and the PMIDs to GO:0140312 (§2.3).
- Two of its four findings are `Low` confidence and are association studies with no
  mechanism: an siRNA/co-IP virology screen [PMID:38560106] and an ovarian-cancer
  oncodrive analysis [PMID:38609993]. Neither becomes an annotation. Neither does the
  pan-cancer expression paper [PMID:35874816] or the cervical-carcinoma expression paper
  [PMID:17125464] that I found separately.

**What affinage missed** — again, the whole molecular-function story. PMID:14691137,
PMID:21097499 and PMID:16162817 are the three papers that establish what sigma3A does, and
none appear in its citation list. Nor does the human AP-3 structure that contains this
protein (PMID:39705307, PDB 9C58/9C59/9C5B/9C5C), nor the delta-ear/sigma3 regulatory
mechanism (PMID:15469849), nor the subunit-assembly genetics (PMID:11807095), nor the
compartment paper (PMID:15051738). This is the documented failure mode exactly: the
decisive papers are titled for the complex, for the cargo, or for a virus, never for
AP3S1. Found instead by PubMed searches on "dileucine AND (AP-3 OR sigma3)", "sigma3A
adaptor", "AP-3 adaptor complex AND (cryo-EM OR crystal structure)" and by resolving the
PDB entries in the UniProt `DR   PDB;` lines through the RCSB API, which named the PNAS
paper. Europe PMC's REST search returned HTTP 503 for the whole session, so all literature
search here went through NCBI E-utilities and RCSB instead.

## 14. Annotation dispositions

- AP-3 complex membership (GO:0030123 x3, GO:0030119, GO:0030117): ACCEPT. The GO term
  definition names sigma3A and sigma3B.
- Golgi apparatus, cytoplasmic vesicle membrane, transport vesicle, early endosome:
  ACCEPT for the first two (curated UniProt locations, vocabulary-mapped), KEEP_AS_NON_CORE
  for the last two.
- vesicle-mediated transport (IBA, IEA, NAS), protein transport, intracellular protein
  transport, clathrin-coated vesicle cargo loading: ACCEPT.
- Golgi to vacuole transport: MODIFY -> GO:0008333 (§6).
- synaptic vesicle coating: MODIFY -> GO:0016182 (§11).
- protein binding (IPI, tyrosinase): MODIFY -> GO:0140312 (§2.2).
- AP-3 adaptor complex binding: REMOVE (§7).
- insulin receptor signaling pathway: MARK_AS_OVER_ANNOTATED (§12).
- anterograde axonal transport x2, anterograde synaptic vesicle transport x2, axon
  cytoplasm, presynapse, synaptic vesicle recycling, membrane, melanosome assembly,
  platelet dense granule organization: KEEP_AS_NON_CORE (§10, §11).
- NEW: one row, GO:0005198 `structural molecule activity`, IDA, PMID:39705307 (§4). The
  more interesting subunit-level MF — dileucine sorting-signal binding — gets no NEW row
  because no GO term exists for it; that is the `proposed_new_terms` entry and the ONTOLOGY
  knowledge gap.

## 15. Final counts (all scripted, none asserted from memory)

- 30 GOA rows, 30 seeded review rows, reconciled one-to-one on
  (GO id, evidence code, reference, normalized WITH/FROM) by `.scratch/reconcile.py`.
- Actions, counted by `.scratch/reconcile.py`: ACCEPT 13, KEEP_AS_NON_CORE 12, MODIFY 3,
  MARK_AS_OVER_ANNOTATED 1, REMOVE 1, NEW 1 (31 rows in total).
- 18 rows carry WITH/FROM; all 18 have `supporting_entities`, and the 17 that the brief
  requires it for (1 IBA + 16 IEA/ISS) have a `propagation_review`; the IPI row carries one
  too, because the schema puts `residue_claims` inside that object. All 34 `source_entities`
  are generated from the seeded lists by `.scratch/build_review.py` rather than typed, so
  they cannot drift, and `.scratch/reconcile.py` asserts the two lists are equal per row.
- 32 references, every one with a `reference_review`; 168 `supporting_text` quotes, all
  verbatim per `checkquotes.py`.
- 3 residue claims, all RETAINED, all resolving against the live sequences.
