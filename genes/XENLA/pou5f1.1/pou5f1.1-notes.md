# pou5f1.1 (Xenopus laevis, Q7T103) review notes

Project: NEURAL_CREST_ORIGINS, Tier 3 (blastula pluripotency programme retained in the crest).
Reviewed 2026-10-07.

## Identity and paralog bookkeeping

- UniProt Q7T103, "POU domain, class 5, transcription factor 1.1", AltName Oct-25 / XOct-25.
  RefSeq NP_001079832.1; **Xenbase pou5f3.2.L** (XB-GENE-919851). UniProt calls it pou5f1.1,
  Xenbase calls it pou5f3.2; same protein (RefSeq cross-reference in the UniProt entry; York 2024
  lists "Xenopus laevis pou5f3.2 NP_001079832.1" in its methods).
- The three X. laevis POU-V (Pou5f3) paralogs, with names used in the literature:
  | Literature name | Xenbase | UniProt (reviewed) | Expression |
  |---|---|---|---|
  | Oct-25 / XOct-25 | pou5f3.2 | Q7T103 (pou5f1.1) | maternal low + zygotic, peaks gastrula |
  | Oct-91 | pou5f3.1 | B7ZQA9 (pou5f1.2) | zygotic after MBT |
  | Oct-60 | pou5f3.3 | Q91989 (pou5f1.3) | maternal only |
  [PMID:25931449 "In Xenopus, the Pou5F1 factors expressed in ectoderm are Pou5F3.1 (Oct91), Pou5F3.2 (Oct25) and Pou5F3.3 (Oct60)"]
  [PMID:1732736 "Transcripts from a second POU-domain gene, Oct-25, were present at low levels in oocytes and early embryos and were dramatically upregulated during early gastrulation"]
- Homeologs: Q7T103 is the .L homeolog; GOA rows sit on Q7T103 only. York 2024 used L and S
  morpholinos for both pou5f3.1 and pou5f3.2.

### Which paralog each experiment addressed

| Paper | Paralog(s) perturbed | Notes |
|---|---|---|
| Hinkley 1992 PMID:1732736 | Oct-25, Oct-60, Oct-91 cloned; octamer binding | expression + DNA binding |
| Cao 2004 PMID:15292233 | Oct-25 only | Xvent-2B promoter; Smad1/4, Vent2 interaction; OE |
| Cao 2006 PMID:16860542 | OE of Oct-25, -60, -91, mOct4; LOF = Oct-25 + Oct-60 MOs | abstract only. Same morpholino-phenotype rows also sit on oct-60 (Q91989) |
| Cao 2007 PMID:17541407 | OE Oct-25 or Oct-60; LOF Oct25MO + Oct60MO mix; biochemistry on Oct-25 (also Oct-60/91/mOct4 pull-downs) | full text |
| Takebayashi-Suzuki 2007 PMID:17950579 | XOct-25 OE and LOF (MO) | abstract only |
| Cao 2008 PMID:18922797 | Oct25 only (Oct25MO; OE; biochemistry) | full text |
| Nicetto 2013 PMID:23382689 | Oct-25 knockdown epistatic to Suv4-20h | full text |
| York 2024 PMID:39060477 | GOF: pou5f3.1, .2, .3 each, and lamprey pou5; LOF: pou5f3.1 + pou5f3.2 MOs (L+S); rescue with pou5f3.1 OR pou5f3.2 OR lamprey pou5 | full text |

## Molecular activity

- Octamer-binding POU-V transcription factor (POU-specific + POU homeodomain)
  [PMID:1732736 "Sequences encoding three novel octamer binding-proteins were isolated from Xenopus cDNA libraries"].
- Direct promoter binding (EMSA + ChIP in embryos) at Xnr1 and Siamois
  [PMID:17541407 "In conclusion, both in vitro and in vivo studies support that Oct-25 interacts with Xnr1 and Siamois promoters."]
  and at Gsc [PMID:18922797 "EMSAs demonstrated strong binding between Oct25 and the first octamer motif"].
- Activates when bound directly to octamer sites (Xvent-2B; artificial reporters)
  [PMID:15292233 "Luciferase reporter gene assay demonstrated that Oct-25 stimulates transcription of the Xvent-2B gene"]
  [PMID:18922797 "OctLuc8x was mildly stimulated by wild-type Oct25 but strongly stimulated by VP16-Oct25"].
- But its dominant embryonic mode is **repression via protein-protein recruitment** onto
  promoters bound by other TFs/signal transducers — a co-repressor mode:
  - VegT and Tcf3 (Wnt): [PMID:17541407 "Oct-25, VegT and Tcf3 interact with each other and form repression complexes on promoters of VegT and beta-Catenin target genes"]
    [PMID:17541407 "Therefore, in the absence of its binding site, Oct-25 serves as a co-repressor for VegT or Tcf3 to regulate transcription of target genes."]
  - FoxH1/FAST1, WBSCR11 (Gtf2ird1), Smad2 (Nodal/activin): [PMID:18922797 "The inhibitory effect is achieved by forming repression complexes on the promoters of Gsc and Mix2 between Oct25 and the signal transducers of the nodal/activin pathway, WBSCR11, FAST1, and Smad2"]
  - Smad1/4 and Vent2 at Xvent-2B (BMP): [PMID:15292233 "Oct-25 interacts in vitro with components of the Xvent-2B transcription complex, like Smad1/4 and Xvent-2"]
- MF conclusion: GO:0000981 (pol II DNA-binding TF) as core; the `protein binding` IPIs
  (Vent2, VegT, Tcf3) map to GO:0140297 DNA-binding transcription factor binding (all three
  partners are DNA-binding TFs); NEW GO:0003714 transcription corepressor activity
  (repression independent of its own site, through Tcf3/VegT).

## Biological role 1: germ-layer timing / anti-differentiation (best supported, core)

- Antagonises the primary mesendoderm inducers in the nucleus: VegT, beta-catenin/Tcf3,
  Nodal/activin (and FGF) — and BMP in the ectoderm:
  [PMID:16860542 "Loss of Oct-25 and Oct-60 function results in elevated transcription of mesendodermal marker genes and ectopic formation of endoderm in the equatorial region of gastrula stage embryos"]
  [PMID:16860542 "We conclude that Xenopus Oct proteins are required to control the levels of embryonic signaling pathways, thereby ensuring the correct specification of germ layers"]
  [PMID:18922797 "Our results provide a novel view in that Oct25 controls the nodal/activin pathway and thus maintains the undifferentiated state of embryonic cells in preventing them from premature differentiation."]
- Ectoderm: limits competence to respond to BMP, promotes neural vs epidermal fate
  [PMID:17950579 "XOct-25 suppressed early BMP responses of ectodermal cells downstream of BMP receptor activation and promoted neural induction while suppressing epidermal differentiation"]
  [PMID:17950579 "inhibition of XOct-25 function in the prospective neuroectoderm resulted in expansion of epidermal ectoderm at the expense of neuroectoderm"]
  [PMID:16860542 "Within the ectoderm, Oct-25 promotes neural fate by upregulating neuroectodermal genes, such as Xsox2, which prevent differentiation of neural progenitors into neurons"].
- It must then be switched off for neural differentiation: Suv4-20h/H4K20me3 silences it
  [PMID:23382689 "Since knockdown of Oct-25 protein significantly rescues the neural differentiation defect in xSuv4-20h double-morphant embryos"].
  Expression: [PMID:23382689 "Oct-25 is initially expressed throughout the animal hemisphere at early gastrula, but gets restricted to the presumptive floor plate (notoplate) by midneurula"].
- Mammalian Oct4 behaves as a functional homolog in these frog assays (PMID:16860542,
  PMID:17541407), so the anti-differentiation role is a conserved POU-V function.

## Biological role 2: neural crest formation (competence factor) — York 2024

- Expression: [PMID:39060477 "zygotic pou5f3.1 and pou5f3.2 expressed in the neural plate border and neural crest"]
  (Extended Data; note the tension with Nicetto 2013, which describes notoplate restriction by
  midneurula — open issue.)
- GOF: [PMID:39060477 "All pou5 factors were found to expand the expression domain of neural plate border and neural crest markers pax3, zic1, and snai2 to comparable extents"]
- LOF (pou5f3.1 + pou5f3.2 MOs, both homeologs): [PMID:39060477 "pou5f3 depletion resulted in a near-total loss of snai2 and foxd3 neural crest expression"]
  pax3 reduced, zic1 expanded (neural expansion). Rescue with pou5f3.2 (= this protein) alone:
  [PMID:39060477 "We found that lamprey and Xenopus pou5 orthologs were indistinguishable in their ability to restore snai2 and foxd3 expression"].
- Authors' interpretation is competence/progenitor-state maintenance, not specification:
  [PMID:39060477 "we hypothesize that pou5 activity helps maintain a similar progenitor state in the neural crest"].
- Amniote corroboration (orthologs; not frog): mouse Oct4 reactivated in CNCC precursors and
  needed for ectomesenchyme [PMID:33542111 "Pluripotency factor Oct4 is transiently reactivated in CNCCs and is required for the subsequent formation of ectomesenchyme"];
  chick/human OCT4-SOX2 bind NC enhancers with TFAP2A
  [PMID:36182685 "Binding of OCT4-SOX2 to neural crest enhancers requires pioneer factor TFAP2A"].
  The amniote data show the POU5 protein acting *at crest enhancers* — participation, not only necessity.

### Layer placement and term choice

- Oct25 is **both**: a general blastula/gastrula anti-differentiation (germ-layer timing) factor
  — the best-evidenced, core role — and a competence factor whose activity at the neural
  plate border is required for crest formation. It is not a crest specifier: it is expressed
  broadly in ectoderm before the border is defined, alone it promotes neural as well as border
  fates (sox3 expansion, epidermis loss in York 2024), and its LOF reduces border (pax3) as
  well as crest markers. Under the project convention it gets GO:0014029 (not GO:0014036).
- Participation test: Oct25 is a DNA-binding TF expressed in the border/crest cells it
  affects; ortholog OCT4 binds crest enhancers (Hovland 2022). It does part of the work
  (transcriptional regulation in the forming crest), not substrate/consumed. Passes, with the
  caveat that direct frog Oct25 occupancy of crest enhancers is not shown.
- GO:0019827 stem cell population maintenance: **not added.** In frog there is no
  self-renewing stem cell population maintained by Oct25: the blastula animal cap is transient,
  and Oct25 phenotypes are changes in germ-layer specification and ectodermal fate choice
  (ectopic endoderm, epidermis vs neural), plus delayed neural differentiation when it is not
  silenced. GO:0019827 on mouse Pou5f1 (MGI IMP, ICM/ES self-renewal) does not transfer to this
  biology. Raised as a question for the module's competence knowledge gap.

### Comparator check (QuickGO, 2026-10-07)

Query 1 — NC branch on POU5 family members, all evidence:
`https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?geneProductId=UniProtKB:Q7T103,UniProtKB:B7ZQA9,UniProtKB:Q91989,UniProtKB:B3DM25,UniProtKB:B3DM23,UniProtKB:Q01860,UniProtKB:P20263,UniProtKB:Q90270,UniProtKB:A7Y7W2&goId=GO:0014029,GO:0014032,GO:0014033,GO:0001755,GO:0014034,GO:0014036&goUsage=descendants&goUsageRelationships=is_a,part_of`
(X. laevis Oct-25/Oct-91/Oct-60, X. tropicalis pou5f1.1/pou5f1.3, human POU5F1, mouse Pou5f1,
zebrafish pou5f3, chicken POU5F3) → **0 rows**. Positive control with same query on mouse
Tfap2a P34056 and frog id3-a Q91399 returned their known NC rows (GO:0014032 IMP; GO:0014029 IMP x5).

Query 2 — per-taxon NC-branch download (`taxonId=7955|10090|9606|8355|8364|9031|10116`,
taxonUsage=exact, same goIds) and grep for symbols starting pou/oct → **0 POU-family rows in
any taxon**. The same files show the *same-layer* blastula/crest potency peers do carry NC
terms: zebrafish mych GO:0014032 IMP, zebrafish foxd3 GO:0014032/GO:0001755, X. laevis id3-a
GO:0014029 IMP, snai1 GO:0014036 IMP, foxd3-a GO:0014034 IMP.

Query 3 — GO:0019827 descendants on the same POU5 set: mouse Pou5f1 GO:0019827 IMP (5 papers)
and GO:0030718 germ-line stem cell population maintenance; human POU5F1 GO:0035019 somatic stem
cell population maintenance (IMP/IDA). No frog or fish POU5 carries any.

Query 4 — are the crest papers curated? grep of all nine POU5 annotation sets for
PMID:33542111, 36182685, 39060477 → none.

Interpretation: the absence of NC terms on POU5 proteins is not a convention. The POU5 crest
literature is recent (2021-2024) and entirely uncurated; same-layer peers carry the term. So the
gap is ordinary curation lag, and NEW GO:0014029 on Q7T103 (IMP+rescue, PMID:39060477) is
justified. Analogous to the myc-a outcome.

## Evolution

- pou5 is a vertebrate innovation that evolved from a pou3-like ancestor:
  [PMID:39060477 "Thus, the ability of pou5 to promote neural crest development is not a general feature of pou-family proteins but rather a synapomorphy of the pou5 clade that emerged after diverging from a pou3-like ancestor"].
  pou3 inhibits crest and promotes neural plate; pou5 retains the ancestral neural-promoting
  activity (sox3 expansion) and added crest-promoting activity.
- Lamprey pou5 is expressed in animal pole cells but not in crest
  [PMID:39060477 "a lamprey pou5 orthologue is expressed in animal pole cells but is absent from neural crest"],
  yet lamprey pou5 rescues frog crest — so the protein activity was present at the vertebrate
  base, and crest *expression* was either lost in cyclostomes or gained in gnathostomes
  (a cis-regulatory change). Pou5 and Xenopus Pou5f3 cannot engage the lamprey crest GRN.
  This is the mirror image of Id3/SoxE co-option: here the protein is new and its deployment
  in the crest differs between the two vertebrate clades.
- The blastula role (anti-differentiation, partner repression of inducers) is the conserved
  POU-V function shared with mammalian Oct4 (cross-species functional rescue in frog assays).

## GOA row decisions (summary)

- MF: DNA binding/TF/cis-regulatory rows accepted. 3 `protein binding` → MODIFY GO:0140297.
  SMAD binding and DNA-binding TF binding accepted. NEW GO:0003714 corepressor.
- CC: nucleus, transcription regulator complex (repression complexes) accepted.
- BP: negative regulation of activin receptor signalling and BMP signalling, negative regulation
  of epidermal differentiation accepted (core); negative regulation of DNA-templated
  transcription → GO:0000122; gastrulation, neural tube, head, neurogenesis rows non-core;
  A/P axis specification and post-anal tail morphogenesis over-annotated (indirect phenotypes
  of combined Oct-25/Oct-60 knockdown; abstract only). NEW GO:0014029.

## Open issues

- Nomenclature: UniProt pou5f1.1 vs Xenbase pou5f3.2 for the same protein.
- Expression conflict: York 2024 places zygotic pou5f3.2 at the NPB/crest; Nicetto 2013 says
  notoplate by midneurula. Needs stage-matched in situ / HCR with paralog-specific probes.
- York's LOF hit pou5f3.1 and pou5f3.2 together; single-paralog requirement untested, although
  pou5f3.2 alone rescues.
- No direct evidence that frog Oct25 binds crest enhancers (OCT4-SOX2-TFAP2A shown in chick/human).
