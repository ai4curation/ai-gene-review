# GET4 (TRC35, C7orf20) review notes

UniProt: Q7L5D6 (GET4_HUMAN), 327 aa. HGNC:21690. Gene names: GET4; synonyms C7orf20, CEE, TRC35; ORF CGI-20.

## Identity / nomenclature
- "Golgi to ER traffic protein 4 homolog"; AltNames: Conserved edge-expressed protein (CEE); Transmembrane domain recognition complex 35 kDa subunit (TRC35) [file:human/GET4/GET4-uniprot.txt "Short=TRC35"].
- Yeast ortholog is Get4 (Yor164C); GET4 belongs to the GET4 family [file:human/GET4/GET4-uniprot.txt "Belongs to the GET4 family"].
- Fold: TPR-like all-α helical solenoid (Gene3D 1.25.40.10; FunFam; PANTHER PTHR12875; Pfam PF04190 GET4; InterPro IPR007317). Crystal structure 6AU8 (res 23-305) is essentially all helices.

## Core biology: pre-targeting / bridging complex of the GET/TRC pathway
GET4/TRC35 is a scaffold subunit of the heterotrimeric BAG6/BAT3 (a.k.a. "Bag6 complex" / TRC pretargeting bridging complex) composed of BAG6, UBL4A and GET4/TRC35 [file:human/GET4/GET4-uniprot.txt "Component of the BAG6/BAT3 complex, at least composed of BAG6, UBL4A and GET4/TRC35"]. It functions in the post-translational targeting of tail-anchored (TA) membrane proteins to the ER:

- The Bag6 complex (Bat3+TRC35+Ubl4A) facilitates TA-protein capture by TRC40/GET3 [PMID:20676083 "we identify a conserved three-protein complex composed of Bat3, TRC35 and Ubl4A that facilitates TA protein capture by TRC40"].
- TRC35 = C7ORF20, identified as a 35 kD component co-purifying with Bat3 [PMID:20676083 "co-purified with proteins of ~18 kD and 35 kD ... that we identified by mass spectrometry as Ubl4A and C7ORF20, for which we propose the name TRC35"].
- The complex is recruited to ribosomes, interacts with TMDs of newly released TA proteins, and transfers them to TRC40 [PMID:20676083 "This Bat3 complex is recruited to ribosomes synthesizing membrane proteins, interacts with the TMDs of newly released TA proteins, and transfers them to TRC40 for targeting"].
- The minimal Bag6 complex facilitates TA substrate transfer from SGTA to TRC40 [PMID:25535373 "the minimal Bag6 complex defined here facilitates tail-anchored substrate transfer from small glutamine-rich tetratricopeptide repeat-containing protein α to TRC40"]; D84 mutagenesis reduces TA-protein delivery [file:human/GET4/GET4-uniprot.txt "D->K: Reduces tail-anchored protein delivery."].
- Cryo-EM of the metazoan pretargeting GET complex: Get4 (TRC35) directly contacts the Get3/TRC40 ATPase; the Get3 helix-8/Get4 C-terminus form a composite lid over the substrate chamber, and Get4-Get3 secondary interactions facilitate TA transfer from SGTA to Get3 [PMID:34887561 "Get3 helix 8 and the Get4 C terminus form a composite lid over the Get3 substrate-binding chamber that is opened by SGTA"; "Both interactions facilitate TA protein transfer from SGTA to Get3"].
- Get4 R25D/K29D loses Get3 interaction and impairs TA delivery [file:human/GET4/GET4-uniprot.txt "R->D: Loss of interaction with GET3"]; direct GET3 interaction documented [file:human/GET4/GET4-uniprot.txt "Interacts with GET3 (PubMed:34887561)"].

So the CORE molecular role is a **pre-targeting/bridging scaffold (protein carrier chaperone)** that loads TA cargo onto GET3/TRC40 — process = post-translational TA protein insertion into the ER membrane.

## Secondary / quality-control roles of the complex
- The BAG6 complex also acts as a holdase / sorting platform in protein quality control: maintaining mislocalized/retrotranslocated hydrophobic substrates soluble and sorting them to the proteasome or ER (ERAD, mislocalized-protein degradation) [PMID:21636303 "a ubiquitin ligase-associated multiprotein complex comprising Bag6, Ubl4A, and Trc35, which chaperones retrotranslocated polypeptides en route to the proteasome to improve ERAD efficiency"].
- TRC35 keeps BAG6 in the cytosol so BAG6 can engage in ERAD [PMID:21636303 "Trc35, a cofactor that keeps Bag6 outside the nucleus for engagement in ERAD"].

## Distinct (regulatory) function: cytoplasmic retention of BAG6
- TRC35 binding occludes the BAG6 nuclear localization sequence, retaining BAG6 in the cytosol, and protects TRC35 from RNF126-mediated ubiquitination/degradation [PMID:29042515 "TRC35 binding is critical not only for occluding the Bag6 nuclear localization sequence from karyopherin α to retain Bag6 in the cytosol but also for preventing TRC35 from succumbing to RNF126-mediated ubiquitylation and degradation"]. BAG6-binding region maps to residues 195-271 [file:human/GET4/GET4-uniprot.txt "REGION 195..271 /note=\"Interacts with BAG6\""].

## Localization
- Cytoplasm, cytosol [file:human/GET4/GET4-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"]. Multiple IDA cytosol annotations (PMID:20676083, 29042515) and IDA cytoplasm (PMID:21636303).

## Disease
- Biallelic missense GET4 variants (p.Arg122His, p.Ile279Met) cause CDG2Y; they destabilize all three TRC proteins (BAG6/UBL4A/GET4) by 70-90% and impair TA-protein (syntaxin 5) targeting [PMID:32395830 "We identified an individual with compound heterozygous missense variants (p.Arg122His, p.Ile279Met) in GET4 that reduced all three TRC proteins by 70% to 90%"; "the TA protein, syntaxin 5, is poorly targeted to Golgi membranes"].

## PTM
- N-terminal Met removed, N-acetyl-Ala at position 2; phospho-Ser12. Ubiquitinated by RNF126 (when unassembled from BAG6) leading to proteasomal degradation [file:human/GET4/GET4-uniprot.txt "Ubiquitinated by RNF12, leading to proteasomal degradation"].

## GO annotation assessment summary
- CORE MF: GO:0140597 protein carrier activity ("protein carrier chaperone") — loads TA cargo onto GET3 (IMP PMID:21636303, IBA). ACCEPT.
- CORE BP: GO:0071816 tail-anchored membrane protein insertion into ER membrane (IDA/IMP), GO:0006620 post-translational protein targeting to ER membrane (IDA, ComplexPortal). ACCEPT.
- GO:0045048 protein insertion into ER membrane (more general parent of 0071816) — ACCEPT but more general; keep as supporting.
- CC: GO:0071818 BAT3 complex (multiple IDA/IPI/IBA) — ACCEPT core. GO:0005829 cytosol / GO:0005737 cytoplasm — ACCEPT.
- GO:0031647 regulation of protein stability (IMP/IDA PMID:21636303): the holdase/cofactor role; KEEP_AS_NON_CORE (secondary QC role; also relates to TRC35 stabilizing BAG6).
- GO:0036503 ERAD pathway (IMP PMID:21636303): complex-level QC role; KEEP_AS_NON_CORE.
- GO:0036506 maintenance of unfolded protein: in UniProt GO list (IMP ParkinsonsUK-UCL) but NOT in goa.tsv; not reviewed (not in GOA).
- GO:0006511 ubiquitin-dependent protein catabolic process (IDA PMID:20676083, ComplexPortal): the complex routes substrates to proteasome; KEEP_AS_NON_CORE (PMID:20676083 is primarily the TA-targeting/capture paper; catabolic role is the alternative QC branch).
- GO:0051087 protein-folding chaperone binding (IPI PMID:25535373, partner BAG6/P46379): real direct interaction with BAG6; more informative than bare protein binding but is an interaction term; KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI, many): bare/uninformative; KEEP_AS_NON_CORE. Includes the functionally meaningful GET3 (O43681) and BAG6 (P46379) interactions but the term itself is uninformative.
- The interactome-screen IPIs (PMID:21516116, 24722188, 25416956, 28514442, 32296183, 33961781, 40205054) are high-throughput protein-binding; KEEP_AS_NON_CORE. Among these the GET3 (O43681) and BAG6 (P46379-2) captures are biologically meaningful; FBN1/NUP85/KRTAP9-3/DUSP21/etc. are likely incidental.

No REMOVE warranted: all experimental annotations are consistent with established GET4 biology; the IEA/IBA are also consistent. No MODIFY strictly required, though GO:0045048 is a more general parent — I keep it ACCEPT as a valid (if general) term rather than MODIFY, since 0071816/0006620 already capture the specific function and both are present.
</content>
</invoke>
