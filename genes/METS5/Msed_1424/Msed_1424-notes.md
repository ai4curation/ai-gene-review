# Msed_1424 (A4YGN0, SUCD_METS5) — curation notes

Metallosphaera sedula DSM 5348. ARCHAEA project gene.

**Provenance note:** automated deep research was unavailable in this session; no
`-deep-research-*.md` file was created. Literature was searched manually (NCBI E-utilities
esearch/esummary, cached publications). PMIDs cited here were cached with `just fetch-pmid`.

## Bottom line: UniProt's name and EC are wrong

UniProt (Swiss-Prot, entry v101) names A4YGN0 "Succinate-semialdehyde dehydrogenase
(acetylating)", EC 1.2.1.76 (RHEA:26450, succinate semialdehyde + NADP+ + CoA = succinyl-CoA
+ NADPH), with ECO:0000269 citing Berg et al. 2007 (PMID:18079405). Its FUNCTION text reads
"Catalyzes the reduction of succinate semialdehyde to succinyl-CoA", which is chemically
incoherent (going from the aldehyde to the thioester is an oxidation).

The primary literature says something different. Msed_1424 is the **succinic semialdehyde
reductase (SSR)**, which reduces succinate semialdehyde with NADPH to **4-hydroxybutyrate**
(a Zn-dependent medium-chain alcohol dehydrogenase). The succinyl-CoA reductase step
(EC 1.2.1.76) belongs to Msed_0709, the promiscuous malonyl-CoA/succinyl-CoA reductase
(see genes/METS5/Msed_0709/). So the two genes do not conflict; UniProt has given Msed_1424
the EC of the step just upstream of the one it catalyses.

- [PMID:19684143 "Succinic semialdehyde is then reduced with NADPH to 4-hydroxybutyrate by succinic semialdehyde reductase, an enzyme belonging to the Zn-dependent alcohol dehydrogenase family."]
- Native enzyme purified from autotrophic cells, identified by peptide mass fingerprinting:
  [PMID:19684143 "The best hit was with the gene gi|146304190 (100% identity, 65% coverage) annotated as a Zn-dependent alcohol dehydrogenase gene encoding a 37.9-kDa protein (Msed_1424; 360 amino acids)."]
- Recombinant enzyme: [PMID:19684143 "The succinic semialdehyde reductase gene Msed_1424 was expressed in E. coli Rosetta 2(DE3)."]
  [PMID:19684143 "The purified enzyme catalyzed the expected reaction at a rate of 700 μmol min −1 mg −1 protein at 65°C."]
- Kinetics / cofactor: [PMID:19684143 "the apparent K m for succinic semialdehyde (determined with NADPH) was 52 ± 8 μM, the apparent K m for NADPH was 6 ± 2 μM, and the apparent K m for NADH was 180 ± 25 μM."]
- Substrate specificity: [PMID:19684143 "Malonic semialdehyde, acetaldehyde, butyraldehyde, propionaldehyde, or glutaraldehyde did not serve as a substrate"]
- Homodimer: [PMID:19684143 "The native molecular mass determined by gel filtration was 74 ± 7 kDa, suggesting a homodimeric subunit composition."]
- The authors assign EC 1.1.1.2: [PMID:19684143 "Succinic semialdehyde reductase (EC 1.1.1.2) (Fig. 1 ) strongly prefers NADPH as the electron donor and does not act on malonic semialdehyde."]
- Rhea has the exact reaction: RHEA:26381, 4-hydroxybutanoate + NADP(+) = succinate
  semialdehyde + NADPH + H(+) (EC 1.1.1.n11), with no GO cross-reference (Rhea REST query,
  2026-10-31). The NAD+ reaction RHEA:23948 maps to GO:0047577 4-hydroxybutyrate dehydrogenase
  activity, which is defined with NAD+ only.

## Zinc

- UniProt family: zinc-containing alcohol dehydrogenase family (MDR); InterPro IPR002328
  ADH_Zn_CS (PROSITE PS00059), IPR013154/IPR013149 ADH N/C, PANTHER PTHR43350:SF2. It is not an
  aldehyde dehydrogenase (ALDH, PF00171) family protein, which is what a CoA-acylating
  EC 1.2.1.76 enzyme would usually be. The family is itself evidence against UniProt's name.
- Zinc was measured: [PMID:19684143 "Metal analysis (27 elements) of succinic semialdehyde reductase using plasma emission spectroscopy revealed the presence of 1.9 mol of zinc per mol of enzyme monomer, whereas other metals could not be detected."]
- Both sites: [PMID:19684143 "Apparently, both zinc binding sites are loaded with zinc since the enzyme contains 1.9 mol of zinc per mol of enzyme monomer."]
  Catalytic site GHE (58-60) with Cys38/Cys165; structural CXCXXCXXXXXXXC (Cys89, 92, 95, 103).
  These match the UniProt BINDING features (38, 59, 165 catalytic; 89, 92, 95, 103 structural).
- EDTA did not inactivate; zinc is not EDTA-accessible, probably due to thermostability.

## Pathway

- 3HP/4HB autotrophic CO2-fixation cycle, second half (succinyl-CoA -> 2 acetyl-CoA).
  [PMID:18079405 "This intermediate was reduced to 4-hydroxybutyrate and converted into two acetyl-CoA molecules via 4-hydroxybutyryl-CoA dehydratase."]
- Autotrophic induction: [PMID:19684143 "No (<0.01 μmol min −1 mg −1 of protein) succinic semialdehyde-dependent oxidation of NADPH or NADH was observed with heterotrophically grown cells."]
- Gene neighbourhood: [PMID:19684143 "The succinic semialdehyde reductase gene is located two genes downstream of the acryloyl-CoA reductase gene (Msed_1426)"]
- Homologs: T. neutrophilus Tneu_0419 (DC/4HB cycle) is the SSR there.
  [PMID:21169482 "T. neutrophilus contains a gene in the autotrophy-related gene cluster that is similar (53 and 75% aa identity and similarity) to M. sedula succinic semialdehyde reductase (Msed_1424)"]
- Used as "SSR" in the in vitro cycle reconstruction:
  [PMID:27771364 "The genes hpcs (Msed_1456), hpcd (Msed_2001), acr (Msed_1426), mcr (Msed_0709), and ssr (Msed_1424) were amplified from genomic DNA using the primers listed in Supplementary Table S1."]

## Where did EC 1.2.1.76 come from?

Unverified. UniProt cites Berg et al. 2007 (PMID:18079405), which predates the gene
identification in Kockelkorn & Fuchs 2009; only the abstract is cached, and I could not read the
Science supplement. Possibly the 2007 paper's supplement listed Msed_1424 as a candidate for
the succinyl-CoA/succinate semialdehyde step, and the Swiss-Prot entry (integrated 2011) was
not updated after PMID:19684143. Whatever the origin, the 2009 and 2011 papers identify the
protein by purification and recombinant expression as SSR, and the succinyl-CoA reductase as
Msed_0709.

## Annotation decisions

- GO:0008270 zinc ion binding (IEA, IPR002328) — ACCEPT: 1.9 Zn/monomer measured; the
  catalytic and structural sites are conserved.
- GO:0016491 oxidoreductase activity (IEA) — MODIFY to GO:0008106 alcohol dehydrogenase
  (NADP+) activity (EC 1.1.1.2, the EC the authors assign; 4-hydroxybutanoate is a primary
  alcohol and succinate semialdehyde an aldehyde). No GO term exists for the exact reaction
  (RHEA:26381); a new term "succinate-semialdehyde reductase (NADPH) activity" is proposed.
- NOT proposed: "succinyl-CoA reductase (NADP+) activity" (the Msed_0709 proposed term). It
  is the wrong activity for this gene.
- NEW GO:0015977 carbon fixation (IDA, PMID:19684143), consistent with Msed_0709; the enzyme
  catalyses a cycle step.

## Pattern for the catalogue

A UniProt/Swiss-Prot name and EC (and Rhea catalytic activity) assigned to the wrong step of a
pathway: Msed_1424 carries EC 1.2.1.76 (succinyl-CoA reductase) but is the downstream
succinate semialdehyde reductase. No GO row derives from it yet, but a Rhea-to-GO mapping for
RHEA:26450 (for example a new succinyl-CoA reductase term) would put the wrong activity on it.
The InterPro family (MDR zinc ADH) already contradicts the name.
