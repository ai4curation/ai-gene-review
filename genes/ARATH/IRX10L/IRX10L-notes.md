# IRX10L notes (IRX10 family review, 2026-10-29)

## Deep research

`just deep-research-falcon ARATH IRX10L --fallback perplexity-lite` failed in this
session (no provider available: "Provider 'perplexity' not available"). The review
rests on the cached primary literature listed below, read directly.

## The IRX10 clade (GT47)

Arabidopsis has two members, IRX10 (At1g27440, Q9FZJ1) and IRX10-L (At5g61840,
Q940Q8), PANTHER PTHR11062:SF370 within the exostosin-related GT47 family. Both
are xylan backbone beta-1,4-xylosyltransferases (xylan synthases).

- Biochemistry: purified IRX10-L polymerises beta-1,4-xylan from UDP-Xyl
  [PMID:25141999 "These data unambiguously establish that IRX10-L is a polymerizing
  GT that forms β-(1→4) linkages by transferring multiple xylosyl residues from
  UDP-Xyl to the non-reducing end of xylooligosaccharide acceptors"]. AtIRX10 is
  active but weak in vitro [PMID:25139408 "We also find lower but reproducible
  xylan xylosyltransferase activity with A. thaliana IRX10"].
- Genetics: redundant pair [PMID:18980662 "irx10 irx10-L double mutant plants
  showed a much more severe irx and whole-plant phenotype, suggesting considerable
  functional redundancy between these two genes"]. IRX10 is the major
  secondary-wall gene [PMID:20424005], IRX10L the primary-wall gene
  [PMID:26043357 "IRX9L, IRX10L and IRX14 are required for xylan backbone
  synthesis in primary cell wall synthesising tissues"].
- Complex: in asparagus, IRX9, IRX10 and IRX14A are all needed for activity in
  planta and form a Golgi complex [PMID:26951434].

## Curation issues found

1. GO:0080116 glucuronoxylan glucuronosyltransferase activity (IMP, PMID:18980662,
   on both genes; IBA on IRX10L from PTN001667002) is the wrong MF. The paper
   reports loss of beta(1,4) xylosyltransferase activity. GlcA transfer is done by
   GT8 GUX enzymes [PMID:26043357 "GUX3 is the only glucuronyltransferase required
   for the addition of the GlcA decorations on the xylan"]. MODIFY to GO:0047517;
   recorded as a TAIR source defect. The term probably stems from the GUT1/GUT2
   aliases (after tobacco NpGUT1).
2. GO:0009101 glycoprotein biosynthetic process (InterPro2GO, IPR004263) does not
   apply to plant xylan synthases; removed.
3. IRX10L rows citing PMID:25141999 as IMP (cell wall biogenesis) and IDA (Golgi
   apparatus): the paper is in vitro biochemistry only and cites Sogaard et al.
   2012 for topology. Terms kept/refined, evidence-code defects recorded.
4. UniProt naming: both Q9FZJ1 and Q940Q8 carry the alt names "Glucuronoxylan
   glucuronosyltransferase 1/2" (AtGUT1/AtGUT2), and the IRX10 FUNCTION text says
   "especially in the formation of GlcUA side chain of xylans". Both are legacy and
   conflict with the direct biochemistry. Worth reporting to UniProt.
5. Topology: UniProt models residues 1-21/2-22 as a type II signal anchor, while
   Wu et al. 2009 and Urbanowicz et al. 2014 describe a signal peptide; AoIRX10 is
   described as lumenal and held by IRX9/IRX14. Golgi membrane kept as the
   location; the anchoring mechanism is left as a question.
