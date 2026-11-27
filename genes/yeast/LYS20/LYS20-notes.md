# LYS20 (YDL182W, P48570) notes

Pathway context: LYSINE-AMINOAD-PWY-2 step 1 (EC 2.3.3.14 homocitrate synthase).

- Activity: [PMID:8923736 "Disruption and overexpression of ORF D1298 demonstrate that this gene, named LYS20, encodes a homocitrate synthase."]; major isozyme [PMID:8923736 "We have also shown that the product of LYS20 is responsible for the greater part of the lysine production."]; purified enzyme kinetics [PMID:14984204 "Histidine-tagged homocitrate synthase from Saccharomyces cerevisiae was purified to about 98% using a Ni-NTA resin"].
- Paralog specialisation: [PMID:18524920 "Our results show that during growth on ethanol, homocitrate is mainly synthesized through Lys21p, while under fermentative metabolism, Lys20p and Lys21p play redundant roles."]
- Location: nucleus [PMID:9099739 "Cell fractionation studies localize the 47- and 49-kDa proteins to the nucleus."]; [PMID:10103047 "encoding two homocitrate synthase isoenzymes which are located in the nucleus"]; no MTS [PMID:8923736 "The N-terminal end of homocitrate synthase isoform coded by LYS20 contains no typical mitochondrial targeting sequence, suggesting that this enzyme is not located in the mitochondria."]. Mito proteome HDA hits kept non-core.
- Moonlighting in DSB repair [PMID:25628362 "A lys20-E155A mutant is unable to catalyze lysine synthesis, yet it still suppresses esa1 DNA damage sensitivity, suggesting that Lys20 has a second, moonlighting function in DNA damage repair (26)."] -> DNA repair IGI (with ESA1, TEL1) KEEP_AS_NON_CORE.
- Decisions: protein binding (Lys20-Lys21; PCA and AE-MS) REMOVE; generic catalytic/acyltransferase IEA MODIFY -> GO:0004410; zinc ion binding (zinc proteome prediction) non-core; cytosol RCA non-core.
