# CEBPZOS notes

## 2026-10-03 — initial review (MICROPROTEINS Tier 2)

**Identity.** UniProt A8MTT3 (CEBOS_HUMAN), Protein CEBPZOS, 80 aa, PE1. Gene is on the
strand opposite CEBPZ (HGNC alias CEBPZ-AS1, "CEBPZ opposite strand"). The protein is the
canonical product of its own gene (own UniProt accession and HGNC symbol), so the normal
`genes/human/CEBPZOS/` folder is correct; it is not an alternative ORF of CEBPZ.
Predicted single transmembrane helix at residues 15-32 (UniProt FT TRANSMEM, ECO:0000255);
sequence MARTLEPLAKKIFKGVLVAELVGVFGAYFLFSKMHTSQDFRQTMSKKYPFILEVYYKSTEKSGMYGIRELDQKTWLNSKN.
Family: InterPro IPR037764 (CEBPZOS), PANTHER PTHR38001 "PROTEIN CEBPZOS"; no known domain.

**Conservation.** Conserved to Drosophila: fly CG42371 is listed as the CEBPZOS ortholog
[PMID:37889754 "three previously uncharacterized smORFs (CG17931/ SERFs, CG42371/ CEBPZOS, bc10/BLCAP) that were required for normal developmental progression on stressful food diets"].

**Localization (the only direct human evidence).**
- Identified in the IMS-APEX proximity proteome in HEK293T and validated as a new
  mitochondrial protein [PMID:25002142 "we have identified 9 novel mitochondrial proteins that we validated by imaging or western blotting"; "three proteins of unknown function (A8MTT3, C1orf163, and CCDC127)"].
  IMS-APEX labels proteins exposed to the IMS, consistent with a membrane protein with an
  IMS-facing segment; which membrane (inner vs outer) is not resolved.
- In MitoCoP (high-confidence mitochondrial proteome; PMID:34800366) — basis of the
  FlyBase HTP row. The cached text does not name CEBPZOS (in supplementary data); GOA row
  is consistent with the APEX evidence.
- HeLa "dark mitochondrial proteome" table lists NX_A8MTT3-1 Protein CEBPZOS as known,
  sub-mitochondrial location IMS (PMID:32195257); this is a compiled annotation table rather than new localization data.

**Function.** No direct mechanistic study found. PubMed searches (CEBPZOS, CEBPZ opposite
strand, CEBPZ-AS1) return only 4 papers, all transcriptomic/prognostic signatures
(HCC prognosis models PMID:39349287, 37305349, 35602603; teriparatide MSC lncRNA
screen PMID:40609214) that treat CEBPZOS as a transcript, not as a protein. PMC full-text
mentions:
- Upregulated in HEK293 cells after EtBr-induced mtDNA depletion; considered but not
  pursued [PMID:31226201 "among upregulated proteins we identified proteins of unknown function in mtRNA/mtDNA metabolism. We selected four poorly characterized proteins C16orf58, METTL7A, CEBPZOS, C6orf203 (renamed MTRES1)"].
- Fly CG42371 KO viable on normal food but low viability on high-salt (2 alleles) and
  high-fat (1 allele) food [PMID:37889754 "two independent alleles of CG42371-KO showed low viability on high salt food, and one CG42371 allele had low viability on high fat food"].
- I could NOT find any paper establishing CEBPZOS as a regulator of the integrated stress
  response or as a respiratory-complex assembly factor. The MICROPROTEINS project table
  groups CEBPZOS with "mitochondrial assembly factors", but I found no evidence for that
  placement; it should be treated as unverified.

**Conclusion.** Function unknown. Solid evidence: mitochondrial, membrane-integrated,
IMS-exposed. All three GOA rows (CC only) are correct; no MF/BP can be supported. No NEW.
