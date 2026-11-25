# MET1 (YKR069W) notes

## Identity
- Uroporphyrinogen-III C-methyltransferase (SUMT, urogen III methylase), EC 2.1.1.107; synonym MET20; 593 aa [UniProt:P36150].
- Reaction: uroporphyrinogen III + 2 SAM = precorrin-2 + 2 SAH + H+ (RHEA:32459) [UniProt:P36150].
- Domains: C-terminal tetrapyrrole methylase (Pfam PF00590; InterPro IPR000878/IPR006366 CobA/CysG_C), plus fungal-specific Met1 family signature IPR012066; PANTHER PTHR45790:SF6 [UniProt:P36150].

## Evidence
- MET1 cloned and shown identical to MET20; Met1p and Met8p both required for siroheme synthesis [PMID:9003798 "Sequence similitudes as well as complementation studies indicate that Met1p and Met8p are both involved in siroheme biosynthesis."].
- Siroheme is the sulfite reductase prosthetic group [PMID:9003798 "Siroheme is a uroporphyrinogen III-derivative used by sulfite reductase as a prosthetic group."].
- Complementation of bacterial cysG mutants defines MET1 as the SAM-dependent methyltransferase [PMID:10051442 "The conclusion drawn from these experiments is that MET1 encodes the S-adenosyl-l-methionine uroporphyrinogen III transmethylase activity, and MET8 encodes the dehydrogenase and chelatase activities"].
- Nucleus HDA from SWAT-tag library screen (PMID:26928762); MET1 not named in cached text (supplementary data).

## Pathway context
- Siroheme biosynthesis in yeast: Met1p (step 1, SUMT) -> Met8p (steps 2 and 3, dehydrogenase + ferrochelatase). Bacterial CysG fuses all three. Siroheme is the cofactor of sulfite reductase (Met5p/Met10p), hence met1 mutants are methionine auxotrophs.
- YeastPathways superpathway PWY3O-69 (heme and siroheme) gives MET1 a "heme biosynthetic process" RCA. GO:0019354 siroheme biosynthetic process is_a GO:0006783 heme biosynthetic process (runoak), so the term is logically implied but MET1 has no role in protoheme synthesis.
