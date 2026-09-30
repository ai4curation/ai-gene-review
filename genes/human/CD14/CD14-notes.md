# CD14 (human, P08571) review notes

## Identity and structure

- Monocyte differentiation antigen CD14; 375 aa precursor, signal peptide 1-19, mature
  membrane form 20-345 with C-terminal propeptide removed on GPI-anchor addition (UniProt).
- No transmembrane or cytoplasmic domain: GPI-anchored.
  [PMID:2462937 "all monocyte CD14 is joined to the plasma membrane by a phosphatidylinositol phospholipid"]
  [PMID:3385210 "Treatment of monocytes as well as a CD14-expressing neuroglioma cell line with PI-phospholipase C removed CD14 from the cell surface"]
- Soluble CD14 (sCD14) exists in serum and culture supernatants, by release of the anchored form
  and by secretion of an anchor-less form.
  [PMID:2779588 "The soluble form occurring in serum and in supernatants of cultured monocytes thus probably arises by phospholipase-mediated cleaving off the cell surface antigen"]
  [PMID:3385210 "the CD14-expressing neuroglioma cell line, which had been transfected with a single CD14 cDNA, released a soluble form of CD14 into the supernatant"]
  [PMID:25497142 "Treatment with 27OHChol also resulted in the enhanced secretion of MMP-9 and soluble CD14 (sCD14)"]
- Crystal structure: bent LRR solenoid with an N-terminal hydrophobic pocket for acyl chains.
  [PMID:23264655 "The structure reveals a bent solenoid typical of leucine-rich repeat proteins with an amino-terminal pocket that presumably binds acylated ligands including LPS"]

## Molecular function: lipid-PAMP binding and transfer (carrier)

- CD14 binds LPS monomers (1-2 per CD14), loaded catalytically by LBP.
  [PMID:7537731 "LBP catalyzes LPS binding to sCD14"]
  [PMID:7537731 "Complexes of LPS with sCD14 do not form large aggregates, consisting of only 1-2 LPS bound to a single sCD14 even at high multiples of LPS to sCD14"]
- CD14 hands LPS on to TLR4-MD2; in vitro reconstitution shows sequential transfer.
  [PMID:27986454 "LPS transfer to TLR4-MD2 is catalyzed by both LPS binding protein (LBP) and CD14"]
  [PMID:27986454 "Subsequently, the single LPS molecule bound to CD14 was transferred to TLR4-MD2 in a TLR4-dependent manner"]
- Same carrier logic for triacylated lipopeptides and TLR1/TLR2: sCD14 is not in the final complex.
  [PMID:23430250 "However, neither LBP nor sCD14 was physically associated with the final ternary complex"]
  [PMID:23430250 "either LBP or sCD14 can drive ternary complex formation and TLR activation by acting as mobile carriers of triacylated lipopeptides or lipoproteins"]
- Other ligands: LTA [PMID:12594207 "formation of complexes of LTA with LBP and soluble CD14 as well as catalytic transfer of LTA to CD14 by LBP was verified by PhastGel(TM) native gel electrophoresis"],
  di/triacylated lipopeptides [PMID:15294986 "we were able to show that LBP transfers lipopeptides to CD14 on human monocytes using FACS analysis"],
  peptidoglycan [PMID:8798531 "70Z/3-CD14 cells were responsive to both insoluble and soluble peptidoglycan"],
  electronegative LDL [PMID:23880187 "CD14 and TLR4 mediate cytokine release induced by LDL(-) in human monocytes"],
  apoptotic cells [PMID:9548256 "Here we show that apoptotic cells interact with CD14, triggering phagocytosis of the apoptotic cells"].
- Summary statement from the structure paper:
  [PMID:23264655 "CD14 physically delivers these lipidated microbial products to various TLR signaling complexes that subsequently induce intracellular proinflammatory signaling cascades upon ligand binding"]
- The production GO-CAMs (gocams/index.tsv; 5f46c3b700001031 TLR4 MyD88 pathway and
  5fb9cc0600000727 TLR1-TLR2 triacyl lipopeptide) both model CD14 as GO:0140104 molecular
  carrier activity in extracellular region. This is the MF used as core.

## Is CD14 "the receptor"? (project question: which protein performs recognition)

- CD14 is the first host protein to bind LPS at the cell surface, and early work called it the
  LPS receptor [PMID:1698311 "CD14, a differentiation antigen of monocytes, was found to bind complexes of LPS and LBP, and blockade of CD14 with monoclonal antibodies prevented synthesis of TNF-alpha by whole blood incubated with LPS"].
- But it has no transmembrane or signalling domain; transmembrane signalling is done by TLR4
  (with MD-2) or TLR2 heterodimers. LPS cross-links to all three proteins of the tripartite complex
  [PMID:11274165 "Thus, LPS binds directly to each of the members of the tripartite LPS receptor complex"].
- Conclusion: CD14 does real work in recognition (ligand extraction and delivery; ligand-binding
  pocket), so it is a genuine participant in TLR4 and TLR2 signalling pathways and a member of the
  LPS receptor complex (GO:0046696). It is not itself the signal-transducing LPS immune receptor
  (GO:0001875, whose definition requires transmitting the signal across the membrane). MF best
  captured as LPS binding + molecular carrier activity; GO:0001875 on CD14 MODIFY -> GO:0140104.
- Membrane CD14 has an additional, TLR4-independent signalling role: it drives LPS-induced TLR4
  endocytosis via Syk/PLCgamma2, required for TRIF-dependent IFN output (mouse DCs/macrophages).
  [PMID:22078883 "the plasma membrane localized Pattern Recognition Receptor (PRR) CD14 is required for the microbe-induced endocytosis of TLR4"]
  [PMID:22078883 "This cascade begins with CD14 transporting LPS to TLR4, and culminates with CD14 delivering TLR4 to the endosomal signaling machinery that is needed to induce IFN expression"]
  This could justify coreceptor activity (GO:0015026); left as a suggested question rather than
  a new annotation.
- mCD14 required for LPS-induced TLR4/MD-2 dimerization
  [PMID:20133493 "We found that LPS-induced TLR4/MD-2 dimerization occurred only in membrane-associated CD14 (mCD14)-expressing cells"].

## In vivo

- Cd14-/- mice resist endotoxic shock and have reduced bacteraemia.
  [PMID:8612135 "CD14-deficient mice were found to be highly resistant to shock induced by either live Gram-negative bacteria or LPS"]

## Annotation decisions (summary)

- ACCEPT: LPS binding, LTA binding, molecular carrier activity, TLR4 signalling, cell-surface PRR
  signalling, cellular responses to LPS/LTA/lipopeptides, LPS receptor complex, plasma membrane,
  external side of PM, membrane raft, extracellular region.
- MODIFY: LPS immune receptor activity -> molecular carrier activity; peptidoglycan immune receptor
  activity -> peptidoglycan binding; TLR2/TLR1/TLR6 protein binding -> Toll-like receptor binding;
  generic cell surface receptor signalling -> cell surface PRR signalling; phagocytosis ->
  apoptotic cell clearance.
- REMOVE: apoptotic process (CD14 recognises apoptotic cells, does not execute apoptosis);
  protein binding with FSTL1 and MYO18A (uninformative).
- MARK_AS_OVER_ANNOTATED: opsonin receptor activity (TAS to an LBP paper; CD14 is GPI anchored).
- KEEP_AS_NON_CORE: cytokine-production regulation terms, Golgi, endosome membrane, secretory
  granule membrane, exosome, type I/II IFN production.

## Deep research

Falcon deep research status is recorded below once the background job finishes.

Falcon deep research completed (genes/human/CD14/CD14-deep-research-falcon.md) and agrees with
the synthesis above: "The primary molecular function of CD14 is to serve as a co-receptor that
captures, concentrates, and transfers pathogen-associated molecular patterns (PAMPs) and
damage-associated molecular patterns (DAMPs) to downstream signaling receptors". It also reports
(from reviews, not read here as primary papers) CD14 roles in TLR4-independent NFAT signalling,
CD14-dependent cytosolic LPS delivery for the non-canonical (caspase-11/4/5) inflammasome
(Vasudevan 2022, Cell Rep), and flotillin-dependent CD14 trafficking through early endosomes,
recycling endosomes and TGN (Matveichuk 2024). None of these primary papers were cached, so no
NEW annotations were proposed from them.
