# ninaE (Rh1, P06002) - manual literature synthesis

No deep-research API was available for this review; this summary was compiled by hand from the
cached publications in `publications/` and the UniProt record. Every statement carries provenance.

## Identity and structure

- ninaE encodes Rh1, the major rhodopsin of the R1-R6 outer photoreceptors of the compound eye
  [PMID:15014127 "we identified a dominant mutation in the ninaE gene (NinaE(pp100)) that encodes the rhodopsin that is expressed in photoreceptors R1-R6"].
- A 373-aa seven-transmembrane opsin of the GPCR class A (rhodopsin-like) family
  [file:DROME/ninaE/ninaE-uniprot.txt "Belongs to the G protein-coupled receptor 1 family. Opsin subfamily."].
- The chromophore is attached through a Schiff base to Lys319
  [file:DROME/ninaE/ninaE-uniprot.txt "N6-(retinylidene)lysine"]; absorption maximum 480 nm
  [file:DROME/ninaE/ninaE-uniprot.txt "Abs(max)=480 nm"].
- Chromophore chemistry: 11-cis-retinal binds opsin and is photoisomerized
  [PMID:15917458 "11-cis-retinal binds to opsin and undergoes a light-driven isomerization to all-trans-retinal."];
  the fly chromophore is 3-hydroxy-11-cis retinal
  [PMID:17452532 "The photopigment, rhodopsin, consists of a seven-transmembrane protein, opsin, and a chromophore (3-hydroxy-11-cis retinal and 11-cis retinal in Drosophila and mammals, respectively)"].

## Molecular function and signalling

- Light-activated Rh1 (metarhodopsin) activates the eye Gq heterotrimer and thereby NorpA PLC-beta
  [PMID:7759511 "PLC activation depends on the photoconversion of rhodopsin to metarhodopsin and is reduced in norpAEE5 PLC and ninaEP332 rhodopsin mutants."];
  [PMID:7759511 "These results indicate that G beta e functions as the beta subunit of the G protein coupling rhodopsin to NorpA PLC."].
- Spectral sensitivity of both rhodopsin and metarhodopsin is set by multiple opsin regions
  [PMID:8338666 "multiple regions of the opsin protein are involved in regulating rhodopsin spectral sensitivity"].
- Deactivation: metarhodopsin binds arrestin (Arr2); a dominant constitutively active allele
  stabilizes the Rh1-Arr2 complex and desensitizes photoreceptors
  [PMID:15014127 "This desensitization primarily resulted from both the persistent binding of arrestin (ARR2) to the NINAE(pp100) mutant opsin and the constitutive activity of the phototransduction cascade."].
- Rh1 has been reported in the INAD "signalplex" with TRP, NORPA and calmodulin
  [PMID:9010208 "TRP forms a complex with phospholipase C-beta (NORPA), rhodopsin (RH1), calmodulin, and the PDZ domain containing protein INAD."]
  [PMID:10611962 "most of the proteins central to Drosophila phototransduction are coupled into a supramolecular signaling complex, signalplex, through association with a PDZ-containing scaffold protein."].
  Rh1 is generally considered a transient rather than core member of this complex (caveat; not
  verified in the cached abstracts).

## Physiology and behaviour

- ERG/PDA phenotype: reduced Rh1 abolishes the PDA
  [PMID:17452532 "Thus, when the Rh1 level is decreased, as occurs upon mutation of the structural gene for the Rh1 opsin (ninaE), a PDA is not produced"].
- Motion vision and phototaxis require R1-R6/Rh1, including the UV peak
  [PMID:19303299 "Flies without ninaE showed no detectable motion responses (Figures 1D and 1G) and largely compromised phototaxis to blue and UV light (Figures 1F and 1G), thus indicating a functional role for the UV absorption peak observed for Rh1 [11, 12]."].
- Light-independent role in larval thermotaxis
  [PMID:21393546 "This role for rhodopsin in thermotaxis toward 18°C was light-independent."];
  [PMID:27705783 "Because Rh1 contributes to thermal selection in the comfortable range during the early to mid-third-instar stage"].

## Biogenesis, trafficking and localisation

- Synthesised in the ER, requires the cyclophilin NinaA, transits secretory vesicles to the rhabdomere
  [PMID:1913822 "In Drosophila, the major rhodopsin Rh1 is synthesized in endoplasmic reticulum (ER)-bound ribosomes of the R1-R6 photoreceptor cells and is then transported to the rhabdomeres where it functions in phototransduction."].
- ER-to-Golgi transit requires PAPLA1/COPII [PMID:25002678]; post-Golgi transport needs MyoV/Rab11/dRip11
  and Crumbs stabilises MyoV
  [PMID:22105348 "Loss of MyoV in crb mutant photoreceptors was accompanied by defective transport of the MyoV cargo Rh1 to the light-sensing organelle, the rhabdomere."].
- Immuno-EM: rhabdomeric microvilli, rough ER, subrhabdomeric cisternae, MVBs, lysosomes
  [PMID:1838762 "Numerous gold particles were observed on the rhabdomeric microvilli of R1-R6 retinular cells."].
- Light-triggered clathrin-mediated endocytosis to Rab5 early endosomes
  [PMID:28507272 "Following photon absorption, Rh1 is phosphorylated, binds arrestin and is removed from the PM by CME to a Rab5-labelled compartment from where it is either recycled or degraded via late endocytic compartments"];
  Gq-driven, arrestin-independent endocytosis [PMID:18034157].

## Development and degeneration

- Rh1 is required for rhabdomere morphogenesis, during a critical window
  [PMID:9245510 "There is a critical developmental period in which rhodopsin plays its key role in photoreceptor morphogenesis."]
  [PMID:11110667 "rhodopsin appears to organize the actin cytoskeleton through Drac1, contributing a structural support essential for photoreceptor morphogenesis."].
- Misfolding (P37H) and constitutive activity alleles cause photoreceptor apoptosis
  [PMID:16049034 "Rh1P37H transgenic flies show dominant photoreceptor degeneration that mimics age-, light-dependent and progressive ADRP."].
