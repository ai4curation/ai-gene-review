# GAL3ST1 (Q99999) — review notes

Reviewed alongside SULT1B1 as the "negative control" pair of the contested-functions batch.
**Headline finding: the 2026 histone-tyrosine-sulfotransferase claim has NOT entered GOA for
GAL3ST1, and the established sulfatide-synthase annotations are sound.**

## 1. Established function: galactosylceramide 3'-O-sulfotransferase (cerebroside sulfotransferase, CST)

GAL3ST1 is the single gene responsible for sulfoglycolipid synthesis in mammals. It is a type II
single-pass Golgi membrane protein that transfers sulfate from PAPS to the 3-OH of the non-reducing
terminal beta-galactose of galactolipids, producing sulfatide (3-O-sulfogalactosylceramide) and
seminolipid.

- Purification from human renal cancer cells, EC 2.8.2.11:
  [PMID:8830034 "We have purified 3'-phosphoadenosine-5'-phosphosulfate:GalCer sulfotransferase [EC
  2.8.2.11] from a human renal cancer cell line SMKT-R3 through a combination of affinity
  chromatographies using galactosylsphingosine, 3',5'-bisphosphoadenosine and heparin as ligands."]
- Acceptor specificity (this is what grounds both the sphingolipid and the glycerolipid BP
  annotations):
  [PMID:8830034 "GalCer was the best acceptor for the purified enzyme. LacCer, GalAAG, and GalDG were
  also good acceptors."]
  [PMID:8830034 "These observations suggest that the sulfotransferase prefers beta-glycoside,
  especially beta-galactoside, at the nonreducing termini of sugar chains attached to a lipid moiety."]
  GalAAG (galactosyl alkylacylglycerol) and GalDG (galactosyl diacylglycerol) are glycerolipids, so
  the `GO:0046486 glycerolipid metabolic process` IDA is correctly grounded, not a stray.
- cDNA cloning and heterologous expression:
  [PMID:9030544 "When the cDNA was inserted into the expression vector pSVK3 and transfected into
  COS-1 cells, galactosylceramide sulfotransferase activity in the transfected cells increased from
  8- to 16-fold over that of controls, and the enzyme product, sulfatide, was expressed on the
  transformed cells."]
  [PMID:9030544 "The deduced amino acid sequence predicts a type II transmembrane topology and
  contains two potential N-glycosylation sites."]
- Physiology, from the mouse Cst (Gal3st1) knockout — one gene makes both sulfoglycolipids, and its
  loss causes paranodal/myelin and spermatogenic failure:
  [PMID:11917099 "Cst(-/-) mice lacked sulfatide in brain and seminolipid in testis, proving that a
  single gene copy is responsible for their biosynthesis."]
  [PMID:11917099 "Although compact myelin was preserved, Cst(-/-) mice displayed abnormalities in
  paranodal junctions."]
  [PMID:11917099 "These data show a critical role for sulfoglycolipids in myelin function and
  spermatogenesis."]
  This is the experimental basis behind the `GO:0042552 myelination` IBA (WITH/FROM MGI:MGI:1858277 =
  mouse Gal3st1), so that IBA rests on a real, strong descendant annotation and is accepted.
- UniProt places the protein in the Golgi apparatus membrane as a single-pass type II membrane
  protein (TRANSMEM 15..35, TOPO_DOM 36..423 lumenal), with PATHWAY "Lipid metabolism; sphingolipid
  metabolism".

### Two legacy TAS rows I removed

Both are 2003 PINC-era TAS annotations traced to PMID:9030544, and both misread the paper:

- `GO:0005886 plasma membrane` — 9030544 reports that the *product* sulfatide "was expressed on the
  transformed cells", i.e. the glycolipid reaches the cell surface. The *enzyme* is a Golgi type II
  membrane protein. Wrong entity.
- `GO:0006487 protein N-linked glycosylation` — derives from "contains two potential N-glycosylation
  sites". GAL3ST1 is a *substrate* of N-glycosylation, not a participant in the glycosylation
  machinery. Classic substrate/enzyme inversion.

## 2. The 2026 histone-sulfation claim — and why GOA has not taken the bait

[PMID:41686426 "Mechanistically, GAL3ST1 functioned as a histone sulfotransferase to sulfate nascent
histone H3 at tyrosine 99 (H3Y99sulf) in the cytosol of gastric cancer cells."]
[PMID:41686426 "We further demonstrated the ability of GAL3ST1 to act as a novel histone
sulfotransferase, which catalyzes H3Y99 sulfation on nascent histone H3 in the cytoplasm."]

Why this is hard to accept as it stands:

1. **It conflicts with the enzyme's own cell biology.** GAL3ST1 is a type II Golgi membrane protein
   whose catalytic domain faces the Golgi *lumen*. The claimed reaction is on nascent histone H3 in
   the *cytosol*. The paper does not resolve how a lumenal catalytic domain reaches a cytosolic
   substrate; it reports an in vitro assay with purified His-GAL3ST1 and immunoblot readout
   ("Purified recombinant His-GAL3ST1 protein was incubated with purified histone H3 in HST buffer
   (50 mmol/L Tris-HCl and 15 mmol/L MgCl2, pH 7.5) at 37°C... H3Y99sulf levels were determined by
   immunoblotting"), plus AlphaFold/HADDOCK docking.
2. **The mark itself is disputed.** The H3Y99sulf modification was defined in PMID:36805701 and
   formally challenged in PMID:40890505, which reannotated the original raw MS data, showed the
   spectra fit a **phospho**tyrosine peptide far better than a sulfotyrosine one, and found no
   sulfation of recombinant histone H3.2 by recombinant SULT1B1 in an assay that did sulfate T3:
   [PMID:40890505 "Taken together, our new results along with reannotation of MS raw data from Yu et
   al. do not support the presence of histone H3 sulfation."]
3. **The detection reagent is the one under question.** The refutation's specific warning is that the
   anti-H3Y99sulf antibody was validated only on an N-terminal histone peptide array and that CUT&Tag
   signal could reflect phosphorylation:
   [PMID:40890505 "Because Y99 is near the C-terminus, additional validation of this antibody seems
   warranted. Therefore, it is possible that the CUT&Tag results presented in Yu et al. may be due to
   phosphorylation rather than sulfation."]
   PMID:41686426's H3Y99sulf readouts are immunoblot/CUT&RUN with that class of antibody.
4. **The refutation is not cited.** I grepped the full text of PMID:41686426 for "Youssef" and
   "refute": no hits. The paper cites PMID:36805701 (its ref 13) as settled background.
5. **It also conflicts with the original attribution.** PMID:36805701 assigns the writer role to
   SULT1B1; PMID:41686426 assigns it to GAL3ST1 and notes SULT1B1 levels were unchanged
   [PMID:41686426 "SULT1B1 in gastric cancer cells remained unchanged after coculture with CAFs,
   suggesting that H3Y99sulf in gastric cancer cells might be regulated by alternative
   sulfotransferases."]. So there are now two incompatible enzyme assignments for a mark whose
   existence a third paper denies.

**GOA status check (2026-09-17):** `GAL3ST1-goa.tsv` contains no histone, chromatin, nucleus,
cytosol or protein-tyrosine-sulfotransferase annotation of any kind; every row is
galactolipid/sulfotransferase/Golgi. The 2026 claim has not been curated. Recorded here as the
finding, not as an annotation change.

## 3. Is there a GO term for this at all?

Yes — and that is what makes the absence informative rather than a vocabulary gap.
`GO:0008476 protein-tyrosine sulfotransferase activity` and `GO:0006478 peptidyl-tyrosine sulfation`
both exist. A QuickGO query (goId=GO:0008476, goUsage=exact, taxonId=9606, retrieved 2026-09-17)
returns 24 human rows, all of them TPST1 (O60507) or TPST2 (O60704) and their isoform accessions.
Neither GAL3ST1 nor SULT1B1 is annotated to it. The ontology could express the disputed claim; GO
has declined to.

## 4. Review decisions summary

Core: `GO:0001733 galactosylceramide sulfotransferase activity` in the Golgi membrane
(`GO:0000139`), driving sulfoglycolipid (sulfatide/seminolipid) biosynthesis and, downstream,
myelination. Accepted essentially unchanged. Small cleanups: two generic parents
(`GO:0008146 sulfotransferase activity`, `GO:0016020 membrane`, `GO:0009247 glycolipid biosynthetic
process`) modified to specific terms; two legacy PINC TAS rows (`GO:0005886 plasma membrane`,
`GO:0006487 protein N-linked glycosylation`) removed as misreadings of PMID:9030544.
**No annotation was added or changed on account of the 2026 histone-sulfation claim.**
