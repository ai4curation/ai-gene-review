# relA (PA0934, Q9I524) notes

## Identity

- UniProt Q9I524 (unreviewed, PE 3), 747 aa, "GTP pyrophosphokinase"; locus PA0934. Long RSH
  architecture: HD-like (Pfam HD_4), synthetase (RelA_SpoT), TGS, alpha-helical, ZFD/RIS and ACT
  domains (UniProt DR lines). PANTHER PTHR21262:SF31.
- P. aeruginosa, like other beta- and gamma-proteobacteria, has two long RSHs: RelA (PA0934) and SpoT
  (PA5338, Q9HTM0), plus a small alarmone hydrolase (SAH) [PMID:33448498 abstract].

## Function

- RelA is the ribosome-associated (p)ppGpp synthetase activated by uncharged tRNA during amino-acid
  starvation [PMID:15385461 "During amino acid starvation, production of the nucleotides guanosine
  tetraphosphate and guanosine pentaphosphate (ppGpp and pppGpp, respectively) is enhanced via the
  ribosome-associated RelA protein"].
- In PAO1 a relA mutant makes no detectable (p)ppGpp after serine hydroxamate (serine starvation), and
  multicopy relA restores synthesis even without inducer [PMID:15385461 "ppGpp and pppGpp were
  undetectable in the relA mutant, whereas wild-type PAO1 produced high levels of ppGpp and pppGpp"; "We
  were also able to restore ppGpp and pppGpp production through overexpressing the relA gene"].
- Downstream phenotypes of relA loss (reduced Drosophila virulence, altered 3-oxo-C12-HSL and PQS, more
  pyocyanin, less elastase, lower RpoS) are consequences of the alarmone, not RelA's own processes
  [PMID:15385461 abstract].
- SpoT supplies (p)ppGpp under carbon/other starvation and in stationary phase; relA spoT double mutant
  is ppGpp-null under all conditions [PMID:21788391 "no (p)ppGpp synthesis could be detected in the relA
  spoT double mutant under any growth condition tested"; PMID:18776018 abstract "accumulation of ppGpp in
  the wild type and the DeltarelA mutant in stationary phase, indicating a SpoT-derived control"].
- Hydrolase: in beta/gamma-proteobacteria RelA lost (p)ppGpp hydrolase activity after the Rel
  duplication; SpoT kept it [PMID:21858139 "Rel[HS] and SpoT[HS] are well conserved in residues that line
  the HD binding pocket, while RelA is clearly more divergent, consistent with its loss of hydrolase
  activity"]. No hydrolase activity has been reported for P. aeruginosa RelA; I did not test the HD
  motif directly.

## Annotation decisions

- GO:0008728 GTP diphosphokinase (IBA): ACCEPT, core MF.
- GO:0008893 ppGpp 3'-diphosphatase (IBA, from E. coli SpoT seed P0AG24 at the RelA+SpoT ancestor
  node): REMOVE; over-propagated to the RelA paralog, which lost hydrolase activity. GO_CENTRAL defect.
- GO:0015969 guanosine tetraphosphate metabolic process (IBA, IEA): MODIFY to GO:0015970 biosynthetic
  process (RelA only synthesises).
- GO:0015949 nucleobase-containing small molecule interconversion (ARBA IEA): MODIFY to GO:0015970.
- GO:0015968 stringent response (IMP PseudoCAP): ACCEPT, core BP.
- GO:0042594 response to starvation (IBA): MODIFY to GO:0015968, which the gene already carries.

## PseudoCAP IBA-seed assessment

PTN001083175 is the ancestor of the proteobacterial RelA/SpoT duplication plus Rel orthologs: its 23
leaves are RelA and SpoT pairs from 11 beta/gamma-proteobacteria plus Rel of Helicobacter (HP_0775),
Geobacter (Q74AW3) and Bradyrhizobium (bll5065) (local PAINT leaf GAF, 2026-10-28).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001083175 | GO:0042594 response to starvation | 1 (sole) | 23 (13 taxa) | GO:0015968 stringent response, IMP, PMID:15385461 (PseudoCAP) | SOUND | The relA deletion abolishes (p)ppGpp under amino-acid starvation and multicopy relA restores it; RelA itself makes the alarmone that constitutes the stringent response, so it does the work of the process rather than being a downstream phenotype. Generalising to response to starvation at the RelA+SpoT+Rel node is appropriate: every member synthesises (p)ppGpp in response to some starvation (amino acid for RelA, carbon/fatty acid/iron for SpoT). |

Other IBDs at this node are seeded from E. coli (not PseudoCAP). The GO:0008893 hydrolase IBD from
SpoT (P0AG24) is mis-placed for the RelA leaves; noted as a GO_CENTRAL defect.
