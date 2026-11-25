# Syt1 (Drosophila melanogaster) review notes

## Entry and fetch

- UniProt P21521 (SY65_DROME, reviewed, 474 aa), FlyBase FBgn0004242. The symbol search hit a
  UniProt HTTP 429, so the gene was fetched with `--uniprot-id P21521`. Two unreviewed isoform
  entries (X2J4C1, X2J979) carry only IEA rows.
- As for Atg18a, QuickGO's annotation search failed on 2026-11-16 whenever `taxonName` was
  requested; the GOA file was fetched with the unmodified `fetch-gene` command wrapped to drop that
  one include field (taxon name filled from taxon id 7227). 62 QuickGO rows collapse to 60 TSV rows.
- Deep research: FlyBase description only (no provider keys in this environment).

## Literature searches run (PubMed E-utilities, 2026-11-16)

- `Drosophila[tiab] AND synaptotagmin[tiab] AND (dense core[tiab] OR neuropeptide[tiab])`
  (6 hits; PMID:25253864 and the review PMID:33619613 are the relevant ones).
- `Drosophila[tiab] AND synaptotagmin[tiab] AND (plasma membrane[tiab])` (18 hits; PMID:25775572,
  PMID:24297851, PMID:21307261 relevant).
- Author/title lookups for the Ca2+-sensor papers: PMID:12467593 (Yoshihara and Littleton 2002),
  PMID:12110842 (Mackler et al. 2002), PMID:20679236 (Yoshihara et al. 2010).

## What Syt1 does in the fly

- The only synaptotagmin on synaptic vesicles [PMID:15263020 "We conclude from these experiments
  that the remaining synaptotagmins are not present on synaptic vesicles in vivo, indicating Syt 1
  is the only synaptic vesicle isoform in Drosophila."]. Syt4 is postsynaptic, Syt7 sits in a
  peri-active-zone tubular compartment, Syt-alpha and Syt-beta are in neuroendocrine cells
  [PMID:15263020; PMID:33619613].
- Major Ca2+ sensor for synchronous release; null removes synchronous release and unmasks
  asynchronous release [PMID:12467593 "These results indicate that synaptotagmin is the major
  Ca(2+) sensor for evoked release and functions to trigger synchronous fusion in response to
  Ca(2+), while suppressing asynchronous release."]. C2B Ca2+-binding aspartates essential
  [PMID:12110842 "These studies show that the Ca(2+)-binding motif of the C(2)B domain of
  synaptotagmin is essential for synaptic transmission."]; C2A Ca2+ binding part of an
  electrostatic switch [PMID:22279210]; C2A Ca2+ binding suppresses asynchronous release, C2B
  Ca2+ binding drives synchronous release [PMID:20679236]. C2B membrane penetration couples Ca2+
  binding to fusion [PMID:21307261].
- Must be tethered to the synaptic vesicle: cytoplasmic or plasma-membrane-tethered Syt1 cannot
  restore synchronous release or clamp spontaneous release [PMID:25775572 "Transgenic animals
  expressing only the cytoplasmic C2 domains or full-length Syt1 tethered to the plasma membrane
  failed to restore synchronous synaptic vesicle fusion, and also failed to clamp spontaneous
  vesicle release."].
- Biochemistry on fly SYT1 (control protein in a SYT4 paper): Ca2+-dependent binding to PS
  liposomes and Ca2+-promoted t-SNARE binding; supports Ca2+-triggered SNARE-mediated fusion
  [PMID:20688915].
- Clamp: null mutants have raised spontaneous release [PMID:7938019; PMID:8104705]; in
  invertebrates complexin is the more prominent clamp [PMID:33619613 "Although SYT1 is the primary
  candidate for a fusion clamp to prevent spontaneous release in mammals, that role is mediated
  more prominently by CPX at invertebrate synapses."].
- Endocytosis: needed for compensatory SV endocytosis (FALI) [PMID:14634669]; C2B poly-lysine and
  Ca2+-binding residues control vesicle size and endocytic rate [PMID:16600855]; docking and
  endocytosis largely Ca2+-independent [PMID:23283333; PMID:33619613]. Binds Stoned A/B
  (PMID:11069931).
- Non-neuronal: Rab39/Syx1A/Syt1-mediated secretion of lysosomal acid sphingomyelinase in the
  embryonic trachea, needed for airway gas filling [PMID:37992718, abstract only].
- Plasma membrane: Syt1 is trapped on the presynaptic plasma membrane when endocytosis is blocked
  in shibire mutants [PMID:15824135; PMID:24297851], i.e. a transient post-fusion pool.

## IBA rows

- PANTHER PTHR10024 (synaptotagmin); subfamily PTHR10024:SF227 (SYNAPTOTAGMIN 1). No local PAINT
  table for this family; node ids come from WITH/FROM: PTN000001283 (family-level node, donors
  include fly Syt4, Syt7, Syt-alpha and mammalian Syt1-13) and PTN000740739 (Syt1/2-type node:
  mouse Syt1, Syt2, Syt9/5, rat Syt1, worm SNT-2).
- GO:0061891 calcium ion sensor activity (PTN000001283; mouse/rat Syt1, worm SNT-1, SNT-3):
  fly Syt1 is the textbook case. ACCEPT, core.
- GO:0099502 calcium-dependent activation of synaptic vesicle fusion (PTN000740739): ACCEPT, core.
- GO:2000300 regulation of synaptic vesicle exocytosis (PTN000740739): Syt1 both triggers
  synchronous fusion and suppresses asynchronous and spontaneous fusion; bidirectional, so the
  undirected regulation term fits. ACCEPT.
- GO:0017158 regulation of calcium ion-dependent exocytosis (PTN000001283): true, broader framing;
  ACCEPT.
- GO:0005886 plasma membrane (PTN000001283; donors exclude fly Syt1; fly donors are the PM- or
  non-SV paralogs Syt4, Syt7, Syt-alpha): MARK_AS_OVER_ANNOTATED.
- GO:0031045 dense core granule (PTN000740739; mouse Syt1, Syt9/5, rat Syt1, worm SNT-2):
  sound for mammalian Syt1, untested in the fly, where Syt-alpha/beta are the DCV isoforms
  [PMID:33619613 "It is unclear if the more abundant SYT isoforms (SYT1, SYT4, SYT7) also serve as
  Ca2+-sensors for DCV fusion in Drosophila, given their established role for this step in many
  mammalian neurons."]. UNDECIDED.

## Text sources

- FlyBase: "Synaptotagmin 1 (Syt1) encodes a synaptic vesicle calcium binding protein that
  functions as the fast calcium sensor for neurotransmitter release at synapses." Every claim
  traced (PMID:15263020, PMID:22279210, PMID:12467593). VERIFIED.
- UniProt CC FUNCTION (PubMed:1840599, 1991): "May have a regulatory role in the membrane
  interactions during trafficking of synaptic vesicles at the active zone of the synapse." Hedged
  pre-genetics text, outdated by the fly genetics showing Syt1 is the Ca2+ sensor for synchronous
  release. OUTDATED_STATEMENT, CONFIRMED.
- FlyBase GO row GO:0060024 rhythmic synaptic transmission (IDA, PMID:22279210): the term is about
  rhythmic synchronous inputs in a neural circuit; the paper is about synchronous vesicle fusion.
  Mis-chosen term; WRONG_TERM, PROBABLE (abstract-only cache).
- GO:1904049 negative regulation of spontaneous neurotransmitter secretion was considered for a
  NEW row (clamp) and not added: comparator check (QuickGO, 2026-11-16) finds it only on PRKN and
  its electronic orthologs, not on mammalian Syt1 or complexins, and the clamp is already covered
  by the accepted GO:2000300 row.
- Protein-binding rows: `Syt1-goa.tsv` has six GO:0005515 IPI rows for PMID:11069931, and the
  review has four. The two missing rows repeat the UniProtKB:Q24211 and UniProtKB:Q24212
  WITH/FROM pairs of the IntAct rows and differ only in assigned_by (UniProt). The review stub
  is seeded with one row per term, evidence code, reference and WITH/FROM, so the collapse is
  deterministic and drops no distinct claim. All four rows are REMOVE under the protein-binding
  policy.
