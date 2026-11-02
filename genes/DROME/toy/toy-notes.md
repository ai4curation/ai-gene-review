# toy (twin of eyeless) - curation notes

UniProt: Q9V490 (unreviewed TrEMBL canonical, 543 aa); FlyBase FBgn0019650.
Domains (UniProt/InterPro): N-terminal paired domain (PF00292, IPR001523), paired-type homeodomain
(PF00046, IPR001356); PANTHER PTHR45636:SF41 (PAX6-related). Subcellular location: nucleus (ARBA/ProRule).

Automated deep research failed for this gene (falcon provider returned HTTP 402, OpenAI returned 401),
so these notes are from my own reading of cached PubMed records (publications/) and a web check of
Blanco et al. 2005 full text. No `-deep-research-<provider>.md` file was produced.

## Identity and evolution

- toy is the second Drosophila Pax6 gene, arising by an insect-lineage duplication
  [PMID:10198632 "Drosophila contains a second Pax-6 gene, twin of eyeless (toy), due to a duplication during insect evolution"].
- Toy is closer to vertebrate Pax6 than Ey [PMID:10198632 "Toy is more similar to vertebrate Pax-6 proteins than Ey with regard to overall sequence conservation, DNA-binding function, and early expression in the embryo"].
- The ey/toy redundancy is ancient in arthropods [PMID:28993201 "this gene regulatory network module dates back to the dawn of arthropod evolution, securing the embryonic development of the ocular head segment"].

## Molecular function: sequence-specific DNA-binding transcription factor

- Directly regulates the eye-specific enhancer of ey [PMID:10198632 "Toy functions upstream of ey by directly regulating the eye-specific enhancer of ey"].
- Binds the so10 enhancer of sine oculis at sites distinct from Ey [PMID:11830564 "both Drosophila Pax6 proteins namely EY and TOY bind and positively regulate so10 expression through different binding sites"].
- Binds multiple paired-domain sites at the Clock locus by EMSA [PMID:24916389 "toy binds multiple sites at the Clk locus"].
- Blanco et al. 2005 (abstract-only in cache; full text checked online): His-TOY binds the chicken
  delta1-crystallin DC5 enhancer in EMSA and, together with SoxN, activates DC5 in S2 cells and in vivo;
  however D-Pax2 is the physiological regulator of DC5 in cone cells
  [PMID:15790965 "regulation of the DC5 enhancer is carried out not by Pax6, but by Pax2 (D-Pax2; shaven--FlyBase) in combination with the Sox2 homologue SoxN"].
  This supports a generic Pax6-type DNA-binding TF activity for Toy (IDA for GO:0000981).
- Paired domain of Toy has DNA-binding properties distinct from Ey, and the C-terminal region differs in
  transactivation [PMID:15253940 "one of the main functional differences between toy and ey lies in the C-terminal region of their protein products, implying differences in their transactivation potential"].
- Phosphorylated by Hipk in paired domain and C-terminal transactivation domain [PMID:29205612 "we mapped four Hipk phosphorylation sites of Toy, one in the paired domain (Ser121 ) and three in the C-terminal transactivation domain"].

## Biological roles

- Compound eye: acts upstream of ey; required for ey initiation; ectopic Toy induces eyes via Ey
  [PMID:10198632 "Toy is therefore required for initiation of ey expression in the embryo and acts through Ey to activate the eye developmental program"].
  Toy can also induce eyes in ey mutants [PMID:15253940 "they all are capable of inducing ectopic eye development in an ey mutant background"].
- Eye-antennal disc / head: strong toy mutants are headless [PMID:11861484 "Strong mutants of twin of eyeless or of eyeless are headless, which suggests that they are required for the development of all structures derived from eye-antennal discs"];
  ey+toy together promote proliferation/survival of the whole disc via tsh and eyg [PMID:28584125 "Pax6 controls eye progenitor cell survival and proliferation through the activation of teashirt (tsh) and eyg"].
- Ocelli (dorsal head simple eyes): toy is the main Pax6 for ocelli; it initiates eya/so in ocellar
  primordium with hh [PMID:21104743 "the role of the pax6 gene toy, together with the hh signaling pathway, in the initiation of eya and so expression"];
  effect on so is largely eya-mediated [PMID:20580700 "the toy positive effect on so expression is largely eya-mediated"];
  TOY binding sites in so10 are required for ocellus development [PMID:11830564 "the EY and TOY binding sites are required for compound eye and ocellus development respectively"].
- Brain: toy mutants show embryonic neuromere and mushroom body defects [PMID:19901536 "Mutations of toy perturb brain neuromere formation in the embryonic stages, and result in severe deformation of the MB lobes in pharate adult brains"].
  Earlier, null/RNAi showed no gross embryonic CNS defects [PMID:11335113 "Studies of genetic null alleles and dsRNA interference did not reveal any gross neuroanatomical effects of ey, toy, or ey/toy elimination in the embryonic CNS"].
- Circadian pacemaker neurons: regulates Clk in s-LNvs [PMID:24916389 "TWIN-OF-EYELESS (TOY; dPax6) regulates Clk expression in small ventrolateral neurons (s-LNvs)"]. Not in GOA; not proposed as NEW (single study; process would be "regulation of gene expression" in a cell type rather than circadian rhythm execution).
- Partial interchangeability with ey [PMID:19484263 "Toy and Ey, to some extent, can substitute for each other"].
- Upstream regulation of toy: oc and salm positive, ems repressive [PMID:26976323 "ocelliless (oc) and spalt major (salm) appear to act as positive regulators of toy gene expression"].

## Curation summary

Core: Pol II DNA-binding TF (paired + homeodomain), positive regulator of transcription of eye
determination genes (ey, so, eya); compound eye specification upstream of ey; ocellus development;
eye-antennal disc development. Non-core: brain/mushroom body development, sensory organ morphogenesis.
Generic ARBA terms (post-embryonic development, cell differentiation, system development) and
"DNA-templated transcription" judged over-annotations.
