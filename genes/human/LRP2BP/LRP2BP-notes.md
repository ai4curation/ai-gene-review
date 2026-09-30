# LRP2BP literature and evidence notes

## Evidence hierarchy

The literature base is sparse. PMID:12508107 is the only seeded targeted study of MegBP/LRP2BP. It identifies MegBP as a TPR-containing scaffold associated with megalin/LRP2 and maps the receptor-side binding site to a proline-rich N-terminal region of the LRP2 cytoplasmic tail [PMID:12508107 "scaffold protein with tetratrico peptide repeats, the megalin-binding protein"] [PMID:12508107 "The binding site of MegBP was mapped"]. The cache is abstract-only and does not state the tested MegBP species or splice isoform. The reviewed human UniProt record maps this evidence to Q9P2M1, but that database assignment should not be mistaken for study-level proteoform resolution [file:human/LRP2BP/LRP2BP-uniprot.txt "CC   -!- SUBUNIT: Interacts with LRP2. {ECO:0000269|PubMed:12508107}."].

The interaction did not block receptor endocytosis in the reported experiment [PMID:12508107 "MegBP binding did not block the endocytic activity of the receptor;"] and MegBP overexpression caused cellular lethality [PMID:12508107 "however, overexpression resulted in cellular lethality."]. The proposed connection between megalin and transcriptional regulation is explicitly a model based on additional interaction-screen partners, including SKIP, rather than a demonstrated transcriptional activity of LRP2BP [PMID:12508107 "These finding suggest a model whereby megalin directly"] [PMID:12508107 "release of transcription factors via MegBP."].

## Screen-only interactions

PMID:28514442 is BioPlex 2.0 AP-MS; GOA/IntAct assigns an LRP2BP-GSTT1 co-association to it, but the pair is not named in the cached article body. The paper itself calls the network edges candidate interactions [PMID:28514442 "With more than 56,000 candidate interactions"]. PMID:33961781 reports BioPlex 3.0 and a second cell-line-specific network; GOA/IntAct again assigns LRP2BP-GSTT1, providing screen-system recurrence but not targeted mechanistic validation [PMID:33961781 "The first, BioPlex 3.0, results from affinity purification"].

PMID:32296183 is the HuRI proteome-scale binary yeast-two-hybrid map. GOA/IntAct attributes 18 LRP2BP partners to this source, but none is named with LRP2BP in the cached article body. The screen used repeated search-space screens and pairwise verification [PMID:32296183 "To map the reference interactome, we performed nine screens of Space III, followed by pairwise verification by quadruplicate retesting and sequence confirmation."]. These pairs are human binary-interaction leads; without targeted follow-up they do not establish stable complexes, shared pathways, localization, or adapter function.

## Human protein, isoforms, architecture, and structure

Reviewed Q9P2M1 is a 347-residue cytoplasmic protein. UniProt records vesicular staining near the plasma membrane and throughout the cytoplasm [file:human/LRP2BP/LRP2BP-uniprot.txt "CC       Note=Detected in a vesicular staining pattern close to the plasma"]. Its architecture is repeat-rich: one annotated TPR at residues 59–92 and six Sel1-like repeats extending through residues 297–332 [file:human/LRP2BP/LRP2BP-uniprot.txt "FT   REPEAT          59..92"] [file:human/LRP2BP/LRP2BP-uniprot.txt "FT                   /note=\"Sel1-like 6\""]. These repeats are compatible with a protein-interaction scaffold, but the paper maps the binding site on LRP2, not an interface on LRP2BP.

UniProt names two splice isoforms [file:human/LRP2BP/LRP2BP-uniprot.txt "CC       Event=Alternative splicing; Named isoforms=2;"]. Isoform 2 carries the small VSP_030664 change at residue 35, recorded as T to TKS [file:human/LRP2BP/LRP2BP-uniprot.txt "FT                   /note=\"T -> TKS (in isoform 2)\""]. No cited functional experiment is isoform-resolved, so the LRP2 interaction, localization, and screen results must not be assigned specifically to isoform 1 or 2.

The reviewed record has AlphaFoldDB and SMR cross-references but no PDB cross-reference [file:human/LRP2BP/LRP2BP-uniprot.txt "DR   AlphaFoldDB; Q9P2M1; -."]. Thus there is a predicted structural model, but no curated experimental structure and no experimentally resolved LRP2BP-LRP2 interface.

## Orthology and paralog boundaries

The fetched PANTHER table places human Q9P2M1 with mouse Q9D4C6, rat Q569C2, macaque Q4R3N2, zebrafish A5PLI4, and Xenopus Q6IND7 in exact subfamily PTHR44554:SF1 [file:interpro/panther/PTHR44554/PTHR44554-entries.csv "Q9P2M1,LRP2-binding protein,protein,9606,Homo sapiens,Homo sapiens (Human),LRP2BP,347,PTHR44554:SF1,LRP2-BINDING PROTEIN,True"]. This supports a conserved vertebrate ortholog group and similar protein lengths, not automatic transfer of LRP2 binding or the proposed transcriptional model. No distinct human paralog is present in the fetched representative table; this does not prove that paralogs are absent from every broader database classification.

## Curation boundaries

- Direct targeted evidence supports physical association with LRP2 and mapping of the binding site on the LRP2 tail.
- The adapter/regulatory role is plausible but remains qualified as “may act” in the reviewed record [file:human/LRP2BP/LRP2BP-uniprot.txt "CC   -!- FUNCTION: May act as an adapter that regulates LRP2 function."].
- Screen partners should remain screen-level associations unless independently validated and functionally connected to LRP2BP.
- No evidence here licenses catalytic activity, autonomous receptor activity, a stable transcriptional complex, isoform-specific function, or an experimentally solved structure.
