# TP53 notes

This notes file was created for the premetazoan-origin pass below. The main
review (TP53-ai-review.yaml, status COMPLETE) predates it; its sources are the
deep-research files in this folder. Automated deep research was not run for the
section below; it is based on PubMed searches and the cached papers cited inline.

## Premetazoan origin (ORIGINS_OF_MULTICELLULARITY, 2026-10-01)

### What is in unicellular relatives of animals

- The choanoflagellate genome has p53-family genes
  [PMID:18273011 "Members of the metazoan p53, Myc and Sox/TCF families were identified"].
  The authors suggest a role in cell-type differentiation, but this is speculation
  [PMID:18273011 "These transcription factors may have had early and critical roles in the evolution of metazoan ancestors by regulating the differential expression of genes to allow multiple cell types to exist in a single organism, and their study in choanoflagellates is a promising future direction."].
- Monosiga has two family members, one with and one without a SAM domain
  [PMID:17924139 "both a p53- and a p63/p73-type sequence are present in the unicellular choanoflagellate, Monosiga brevicollis"].
  Abstract only. The "p53-type" label means "no SAM domain". It does not show
  orthology to vertebrate TP53, which arose much later (below).
- Homologs are also found in Filasterea (*Capsaspora*), Ichthyosporea and Corallochytrea
  [PMID:31861340 "we present a detailed characterization of p53 family homologs in remote members of the Holozoa group, in the unicellular clades Filasterea, Ichthyosporea and Corallochytrea"].
  The DNA-binding domain is conserved, including the DNA-contact arginines R248 and R273 and two zinc ligands
  [PMID:31861340 "The positive charge of the key DNA binding amino acid residues 248 and 273 of the human canonical p53 sequence is conserved in all remote homologs"];
  [PMID:31861340 "two of four zinc-coordinated amino acid residues, particularly C176 and C238, are 100% conserved in all remote homologs"].
  But there is no transactivation domain
  [PMID:31861340 "None have homology with the p53 family transactivation domain"],
  and no experiments have been done
  [PMID:31861340 "The biological role of the remote homologs found in Holozoa is unclear."].
  The family is restricted to Holozoa; the reported *Entamoeba* homolog was rejected as a false positive (same paper, Discussion).
- I found no experimental study of any choanoflagellate, *Capsaspora* or
  ichthyosporean p53-family protein (PubMed searches: "p53 family evolution
  (choanoflagellate OR Monosiga OR Capsaspora OR unicellular)", "Nematostella p53").

### Early-branching animals: the p63-like germline role

- Sea anemone nvp63 binds the p53 response element and mediates UV-induced death of
  gametes, not somatic cells
  [PMID:17848985 "ultraviolet (UV) irradiation at low levels selectively induces programmed cell death in early gametes but not somatic cells of adult N. vectensis polyps. We demonstrate with RNA interference that nvp63 mediates this cell death in vivo."];
  [PMID:17848985 "In summary, nvp63 bound to the consensus DNA sequence recognized by hup53 and transactivated target gene transcription in vitro."].
  The authors read this as an ancestral germ-cell-protective pathway
  [PMID:17848985 "The genotoxic stress induced and nvp63 mediated apoptosis in N. vectensis gametes reveals an evolutionary ancient germ cell protective pathway which relies on p63-like proteins and is conserved from cnidarians to vertebrates."].
- Fly and nematode p53 proteins also kill mainly germ cells after DNA damage
  [PMID:20081368 "the early p53 proteins, like their human counterparts, are responsible for DNA damage-induced cellular apoptosis, albeit restricted to the germ cell compartment in model organisms such as the nematode and fruit fly"].
  The same abstract places p53 and its inhibitor Mdm2 in placozoans
  [PMID:20081368 "We have found that the p53 gene and the Mdm2 gene are present in Placozoans"]. Abstract only;
  I did not read the primary Drosophila or C. elegans papers.
- Vertebrate p53 is a later duplication of a p63/p73-like ancestor
  [PMID:20516129 "This p63/p73 common ancestor gene is found in almost all invertebrates and first duplicates to produce a p53 gene and a p63/p73 ancestor in cartilaginous fish."].
  Abstract only (review). Its claim that the family is "first detected" in sea
  anemones is out of date given PMID:17924139 and PMID:31861340.

### Classification of the review's core functions

| Core function (existing review) | Classification | Basis |
|---|---|---|
| Sequence-specific DNA binding to p53 response elements (GO:0000976) | Ancestral as a domain property (inferred); experimentally shown only from cnidarians onward | Unicellular DBDs keep DNA-contact residues (PMID:31861340), but binding is untested; nvp63 binds the consensus RE (PMID:17848985) |
| Transcriptional activation / repression by RNA pol II (GO:0045944, GO:0000122) | Unresolved before animals; activation shown in cnidarians | Unicellular homologs lack a transactivation domain (PMID:31861340) |
| DNA damage response and p53-mediated intrinsic apoptosis (GO:0030330, GO:0072332) | Ancestral within animals, in the germ line, through a p63-like protein; unknown in unicellular holozoans | PMID:17848985, PMID:20081368 |
| Negative regulation of mitotic cell cycle; regulation of senescence (GO:0045930, GO:2000772) | Animal-specific on current evidence; not studied in invertebrates in the papers I read | No source above tests it |
| Somatic tumour suppression (TP53 as a gene) | Vertebrate-specific | TP53 arises by duplication in cartilaginous fish (PMID:20516129) |

So the ancestral role, as far as the cited papers go, is p63-like: DNA damage-induced
germ-cell death. The vertebrate TP53 role in somatic tumour suppression came later.
Nothing is known about what the unicellular homologs do.

### Track C (propagation audit) check

TP53 has 8 IBA rows on two PANTHER nodes (PTHR11447):
- PTN000893833: chromatin, nucleus, regulation of apoptotic process (GO:0042981),
  positive regulation of transcription by RNA pol II, promoter-specific chromatin
  binding, DNA-binding TF activity (RNA pol II), and pol II cis-regulatory sequence-specific DNA binding.
- PTN000154790: intrinsic apoptotic signaling pathway in response to DNA damage by
  p53 class mediator (GO:0042771).

QuickGO withFrom queries (2026-10-01; taxonUsage=descendants):
- PTN000893833 / Choanoflagellata (28009): 14 IBA rows. All 7 terms reach both
  *Monosiga brevicollis* proteins, A9UZX3 (MONBRDRAFT_25618) and A9V4M3
  (MONBRDRAFT_27210). None reach *Salpingoeca*. None reach Filasterea or Ichthyosporea.
- PTN000154790 / Filasterea (2687318): 3 TreeGrafter IEA rows (GO_REF:0000118) on
  *Capsaspora* A0A0D2X0F0 (CAOG_000511): GO:0000978, GO:0000981, GO:0006357. The
  p53-class apoptosis term GO:0042771 was not transferred.
  Choanoflagellata and Ichthyosporea: 0 rows.
- No animal tissue, organ or development term reaches a unicellular organism.
- Borderline: GO:0042981 regulation of apoptotic process (IBA, PTN000893833)
  reaches both *Monosiga* proteins. It is a cellular process, not a tissue term, but
  nothing shows these proteins regulate cell death. For comparison, InterPro2GO maps
  IPR002117 (p53 tumour suppressor family) to GO:0006915 apoptotic process on all
  three unicellular proteins (A9UZX3, A9V4M3, A0A0D2X0F0). Both are untested
  extrapolations from animals (PMID:31861340 "The biological role of the remote homologs found in Holozoa is unclear.").
- Changes to the human TP53 rows: none. These node placements do not contradict the
  human annotations, and GO:0042771 sits on a node that does not reach choanoflagellates by IBA.
