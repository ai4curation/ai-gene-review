# Pmvk (CG10268, FBgn0032811, Q9VIT2) — Drosophila melanogaster phosphomevalonate kinase

## Identity check

- Stub `id: Q9VIT2` (PMVK_DROME), gene `Pmvk`, ORF CG10268, FBgn0032811, 189 aa, PE 2
  (transcript level). PANTHER PTHR13101:SF1 (PHOSPHOMEVALONATE KINASE), the animal P-loop
  (NMP-kinase-fold) PMVK family; InterPro IPR005919, NCBIfam TIGR01223, Pfam PF04275,
  PIRSF036639 (PMK_anim). All UniProt functional lines are by similarity to human PMVK (Q15126).
- `just mod-description-deep-research DROME Pmvk` returned `no_curated: 1`: FlyBase has no
  hand-written gene description for Pmvk, so no `-deep-research-flybase.md` file exists.
- FlyBase's automated summary (API, FB2026_03) lists "8 alleles" (transgenic constructs) with
  phenotypic classes "flightless; partially lethal - majority die; some die during pupal stage;
  visible" and phenotypes in the eye. These look like RNAi-screen results; their sources were not
  traced, so they are not used in the review. Lead for future work.

## Literature search (2026-11-18)

- NCBI `Drosophila AND (Pmvk OR CG10268 OR "phosphomevalonate kinase")` -> 0 hits in PubMed.
- NCBI `Drosophila AND "mevalonate pathway"` -> 14 hits; relevant context: PMID:14960281
  (Santos and Lehmann 2004, germ cell migration; GOA reference), PMID:16857902 (Yi et al. 2006,
  heart formation via Ggamma1 prenylation; abstract does not name Pmvk), Hmgcr papers.
- NCBI `(Drosophila OR insects) AND sterol auxotroph*` -> 32 hits; used PMID:20940226 (Carvalho
  et al. 2010) and the review PMID:15355237 (Belles et al. 2005).
- Europe PMC `Pmvk AND regrowth` -> one bioRxiv preprint (not in PubMed): Fahdan et al. 2025,
  doi:10.1101/2025.09.17.676757, "Comparative developmental transcriptomics of Drosophila mushroom
  body neurons highlights the mevalonate pathway as a regulator of axon growth" (eLife reviewed
  preprint 109630). Abstract (bioRxiv API): Pmvk knockdown/mutants impair developmental axon
  regrowth of gamma Kenyon cells; other mevalonate pathway enzymes are also required; genetic
  interaction places Pmvk upstream of Rheb. Necessity evidence for the pathway in neurons, not a
  new molecular function; not used for any annotation.
- No paper assays the enzymatic activity or the subcellular location of fly Pmvk.

## Key points

1. Activity: by orthology only. Pmvk is a single-copy member of the animal PMVK family with the
   P-loop ATP site; human PMVK activity is established biochemically. Accept the MF rows.
2. Flies cannot make sterols. The fly genome lacks enzymes of the sterol branch
   [PMID:14960281 "we found that the fly genome lacks several enzymes required for cholesterol
   biosynthesis"], Drosophila is a sterol auxotroph [PMID:20940226 "Drosophila cannot synthesize
   sterols, but do require them for development."], and the insect mevalonate pathway lacks the
   sterol branch [PMID:15355237 "The mevalonate pathway in insects has two important
   peculiarities, the absence of the sterol branch and the synthesis of juvenile hormone (JH)"].
   So all three GO:0006695 cholesterol biosynthetic process rows (IBA from PTN000991923, InterPro2GO
   from IPR005919, FlyBase ISS from human PMVK) are wrong for this gene: REMOVE.
   - Comparator check (QuickGO, GO:0006695, taxon 7227 exact, 2026-11-18; query returned 5 hits,
     so it can return positives): only Pmvk (IBA, IEA, ISS), Mvk (IBA, from PTHR43290
     PTN000825262) and Mvd (IEA, UniPathway UPA00063) carry the term in fly. Fly Hmgcr does not.
     The same over-propagation affects fly Mvk through PTHR43290.
3. Peroxisome (ISS, PMID:22758915): Faust et al. listed fly homologs of human proteins annotated
   as peroxisomal in UniProt, found by BLAST [PMID:22758915, full text PMC3443258, read during
   this review; the committed cache is abstract only: "Each human protein was used to query the
   Drosophila proteome at FlyBase (23) using the BLAST algorithm (24)."]. Pmvk is not discussed
   in the main text and its localization was not tested. The donor's peroxisomal claim was later
   refuted: human PMVK is cytosolic (PMID:14729858; NOT peroxisome IDA in the human review; UniProt
   CAUTION "Was originally thought to be located in the peroxisome"). Fly Pmvk ends in ...LDRLQLQYR,
   with no PTS1 (S/A/C-K/R/H-L/M), and Drosophila appears to import matrix proteins only via PTS1
   [PMID:22758915 "Similar to Caenorhabditis elegans, Drosophila appears to only utilize the
   peroxisome targeting signal type 1 system for matrix protein import."]. Under
   projects/ORGANELLES.md rule 3, this synthesis row's source does not support the organelle:
   REMOVE (over-propagation of a refuted donor localization). No sub-compartment row.
4. Cytosol (IEA, UniProt SubCell by similarity) and cytoplasm (IEA, InterPro2GO): consistent
   with a soluble enzyme without targeting signals and with the human data. ACCEPT.
5. Processes: IPP biosynthesis via mevalonate (IBA, IEA) ACCEPT, core; isoprenoid biosynthetic
   process (IC, PMID:14960281) ACCEPT. Flies use the mevalonate pathway for non-sterol isoprenoids
   (juvenile hormone, protein prenylation, dolichol, ubiquinone).
   - Juvenile hormone biosynthesis was not proposed: QuickGO GO:0006718 in taxon 7227 has 5 rows,
     all on jhamt and CG15739; no fly mevalonate-pathway enzyme carries it, and there is no
     Pmvk-specific evidence.

## PAINT / family findings (PTHR13101, PTN000991923)

- PTN000991923 (family root, taxon field empty) carries GO:0004631 (sound for Pmvk), GO:0019287
  (sound) and GO:0006695 (over-propagated to insects). `just paint-losses DROME Pmvk`: no IRD/IKR
  on the lineage. The family review's node assessment marks GO:0006695 SOUND on the basis of the
  human member only; for the coordinator: the IBD should be moved to a vertebrate node, or an
  IRD/IKR added at the insect/arthropod node.
