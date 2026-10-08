# glpF notes

E. coli `glpF` encodes an inner-membrane aquaglyceroporin/glycerol facilitator
that conducts glycerol through a passive pore. The crystal structure placed
glycerol molecules in single file in the GlpF channel and showed three and a
half membrane-spanning helices in each repeat [PMID:11039922, "We report the
crystal structure of the Escherichia coli glycerol facilitator (GlpF) with its
primary permeant substrate glycerol"]. A follow-up structure modeled GlpF with
bound water and explained the aquaporin-family selectivity architecture
[PMID:11964478, "We have determined the structure of the Escherichia coli
aquaglyceroporin GlpF with bound water"].

Classic E. coli genetics and transport work supports the GO biological-process
annotation to glycerol transmembrane transport: wild-type cells have an
inducible system that "catalyzes facilitated diffusion of glycerol into the
cell", and `glpF+` improves growth at millimolar glycerol independently of the
ATP-dependent glycerol kinase GlpK [PMID:4563976].

Substrate-specificity assays showed that the E. coli glycerol facilitator
passes glycerol and some related small uncharged solutes but not analogous
sugars, and the temperature-insensitive xylitol transport led Heller et al. to
conclude that "the facilitator behaves as a membrane channel" [PMID:6998951].
Abrami et al. used GlpF-injected Xenopus oocytes in glycerol-flux inhibitor
assays and showed phloretin inhibition of glycerol uptake through GlpF
[PMID:8584435]. The PMID:8584435 GOA NOT rows for water-channel activity and
water transport are in tension with later structures that place ordered water in
the pore, while the cached Abrami abstract does not show the underlying water
assay, so they are left UNDECIDED pending a full-text recheck.

The `GO:0071288 cellular response to mercury ion` row from PMID:8584435 should
be removed. The evidence is an inhibitor experiment with
p-chloromercuribenzene sulphonate in oocyte glycerol-flux assays, not evidence
that GlpF performs an E. coli cellular mercury-response process.
