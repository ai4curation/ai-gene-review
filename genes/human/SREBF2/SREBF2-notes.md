# SREBF2 (human, Q12772) review notes

## Deep research status

- 2026-10-18: `just deep-research human SREBF2 --provider falcon` was tried once and failed
  with `Exception: Failed to authenticate` (Falcon/Edison key not authorised). No
  `-deep-research-*.md` file exists for this gene; the review below is built from the
  UniProt record, the cached GOA-cited publications, and a few extra primary papers and
  reviews cached with `ai-gene-review fetch-pmid` (PMID:8674110, PMID:11994399).

## Gene product overview

- SREBP-2 is a 1141-residue bHLH-Zip transcription factor made as an ER membrane-bound
  precursor [PMID:7903453 "Human SREBP-2 contains 1141 amino acids and is 47% identical to
  human SREBP-1a, the first recognized member of this family"].
- Three domains: N-terminal bHLH-Zip transcription factor (~480 aa), a hairpin of two TM
  segments with a short luminal loop, and a C-terminal regulatory domain (~590 aa) that
  binds SCAP [PMID:11994399 "Each SREBP precursor of about 1150 amino acids is organized
  into three domains"; PMID:9242699 "Complex formation occurs when cells express only the
  COOH-terminal domain of either SREBP-2 or SCAP, indicating that the complex forms between
  the two COOH-terminal domains."].
- Sterol-regulated two-step proteolysis releases the N-terminal domain: S1P in the luminal
  loop, then S2P inside TM1 [PMID:8674110 "The first, regulated by sterols, occurs in the
  lumenal loop. The second, not regulated by sterols, occurs within the first
  transmembrane domain."; "The liberated NH2-segment enters the nucleus and activates genes
  controlling cholesterol synthesis and uptake."].
- SCAP escorts SREBP from ER to Golgi in COPII vesicles in sterol-depleted cells; sterols
  promote SCAP-INSIG binding and ER retention [PMID:12202038 "In sterol-depleted cells,
  SCAP escorts SREBPs from ER to Golgi for proteolytic processing, thereby allowing SREBPs
  to stimulate cholesterol synthesis."]; INSIG-2 behaves the same way
  [PMID:12242332 "insig-2 binds to the SCAP/SREBP-2 complex only in the presence of
  sterols"].
- Golgi anchoring by PAQR3 promotes processing [PMID:26311497 "when SREBP-2 was
  co-expressed with PAQR3, the majority of SREBP-2 was localized in the GA together with
  PAQR3"]. TRC8/RNF139 binds SREBP-2 and SCAP and hampers ER exit [PMID:19706601].
- Nuclear form is imported by importin-beta as a dimer (Reactome R-HSA-1655831, R-HSA-2065550)
  and is rapidly degraded by the ubiquitin-proteasome system [PMID:11477106 "The active
  SREBPs translocate to the nucleus, induce the expression of responsive genes, and are
  degraded very rapidly."].

## Transcriptional function and specificity

- Binds SRE-1 like SREBP-1a and activates SRE reporters [PMID:7903453 "In vitro SREBP-2
  bound SRE-1 with the same specificity as SREBP-1a."].
- Preferential activator of cholesterol synthesis genes and LDLR; weak on lipogenic
  SRE-like promoters; binds but does not activate an E-box reporter [PMID:12177166
  "cholesterogenic genes containing classic SREs in their promoters are strongly and
  efficiently activated by both SREBP-1a and SREBP-2, but not by SREBP-1c"; "SREBP-2 was
  inactive in spite of its ability to bind to the E-box"]; [PMID:11994399 "SREBP-2
  preferentially activates the LDL receptor gene and various genes required for
  cholesterol synthesis"].
- In vivo, nSREBP-2 transgenic liver: 75-fold HMGCR mRNA increase, 28-fold cholesterol
  synthesis increase [PMID:11994399].
- Activates INSIG1 (feedback loop) [PMID:12242332 "Ponasterone A-mediated induction of
  nuclear SREBP-1a or SREBP-2 in these cells led to a marked increase in insig-1 mRNA"].
- Coactivators: CBP/p300 KIX domain and Mediator MED15/ARC105 KIX-like domain
  [PMID:16799563 "SREBPs use the evolutionarily conserved ARC105 (also called MED15)
  subunit to activate target genes"]. HNF-4 binds SREBP-2 and potentiates it
  [PMID:12855700].
- Context-specific repression: nSREBP-2 represses ABCA1 via an E-box in endothelial cells
  [PMID:15358760 "The conserved E-box motif was responsible for the SREBP2(N)-mediated
  inhibition"]; it is also the proposed LRP1 repressor in vascular smooth muscle
  [PMID:19098903, indirect knockdown evidence]. These are non-core.

## Cautions found during review

- PMID:12941800 (Vidal et al. 2003) characterises "SRBP-2", an SR31747A-binding protein of
  206 aa homologous to the sterol isomerase HSI/EBP (i.e. an EBP-like protein), not SREBP-2.
  The abstract states it explicitly: "The 1142-bp cDNA was found to encode a 206 amino acid
  protein not related to SRBP-1." The four GOA rows drawn from it (ER, nucleus, cytoplasm,
  NOT C-8 sterol isomerase activity) therefore rest on a different protein. The location
  claims happen to be true of SREBF2 from other evidence, so they are judged on the claim;
  the NOT isomerase row is removed.
- PMID:24912190 (mitophagy RNAi screen) does not mention SREBF2 in the cached text; the HMP
  rows are screen hits, and the text centres on SREBF1.
- PMID:15358760 abstract reports oscillatory (not laminar) flow activating SREBP2; the NAS
  "cellular response to laminar fluid shear stress" row is not supported by the abstract.
- PMID:32497488 is an SREBF1 IFAP-syndrome paper; the abstract does not show SREBF2 assays,
  but the SREBF2 IMP rows (TF activity, nucleus) are biologically correct and are accepted
  in deference to the curator, who read the full text.

## GO-CAM context

- gocams/6205c24300000880 (Regulation of cholesterol biosynthesis by SREBP and retention by
  SREBP-SCAP complex, human) models SREBF2 with GO:0000981 part_of GO:0045542 in the
  nucleus, consistent with the core function chosen here.
