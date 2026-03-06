# SNIPE (Surface-associated Nuclease Inhibiting Phage Entry) — Research Notes

## Key Identity Question: UniProt Accession Unknown

The SNIPE protein was originally identified as **PD-lambda-1** from prophage phiR26.1 in a diverse E. coli strain
from the ECOR collection (likely ECOR26). It is **NOT** in E. coli K-12 MG1655. The exact UniProt accession
must be determined from the Vassallo et al. 2022 supplementary data or the Saxton et al. 2026 Nature paper.

**DefenseFinder reference:** WP_197909633.1 from *Gemmata massiliana* (a distant homologue used for HMM profiling)

**Do NOT confuse with:**
- Q47715 / ydbA (an intimin/invasin family inverse autotransporter — completely unrelated)
- P45423 / yhcG (a PD-(D/E)XK nuclease family protein — different nuclease superfamily)

---

## Gene/Protein Overview

SNIPE is a single-gene bacterial anti-phage defense system that constitutively localizes to the inner membrane
of E. coli and cleaves phage DNA during genome injection [PMID pending — Saxton et al. Nature 2026,
DOI: 10.1038/s41586-026-10207-1].

Originally identified as PD-lambda-1 in a functional selection screen of 71 diverse E. coli strains
[PMID:36123438 Vassallo et al. 2022, "A functional selection reveals previously undetected anti-phage
defence systems in the E. coli pangenome"].

## Domain Architecture

SNIPE is an elongated protein with three functional domains:

1. **N-terminal transmembrane domain** (~residues 1-50?)
   - Single-pass TM domain in the inner membrane
   - N-terminus is periplasmic; the rest of the protein is cytoplasmic
   - Associates with ManYZ complex (mannose PTS permease)
   - Low sequence conservation; variable length across homologues
   - >50% of homologues have 1-2 TM domains; ~34% lack TM and use DivIVA-like domains
   - Functions as a modular adapter tuning phage specificity

2. **Central DUF4041 domain** (Pfam PF13262, InterPro IPR025280)
   - Required for defense function (deletion abolishes defense)
   - Binds phage tape measure protein (TMP) at the injection site
   - Harbors conserved positively charged region implicated in DNA binding
   - Moderate evolutionary diversification at TMP-interaction interfaces
   - Mutations E223K and W257R enhance binding to Bas14 phage TMP

3. **C-terminal GIY-YIG nuclease domain**
   - Catalytic domain that cleaves incoming phage DNA
   - Most highly conserved domain across 500+ homologues
   - Key catalytic residue: E414 (E414A mutation abolishes defense)
   - Without TM domain, GIY-YIG nuclease is toxic (cleaves host DNA)
   - E414A mutation rescues toxicity of deltaTM construct

## Mechanism of Action

1. SNIPE constitutively resides at the inner membrane via its TM domain
2. N-terminal region associates with ManYZ complex (mannose PTS)
3. Phages (lambda, siphoviruses) use ManYZ as receptor for DNA injection
4. Upon phage attachment, SNIPE is brought near the injection machinery
5. DUF4041 domain binds the phage tape measure protein (TMP) and incoming DNA
6. GIY-YIG nuclease domain cleaves phage DNA during injection
7. Phage genome is destroyed before it enters the cytoplasm

**Self/non-self discrimination:** Spatial rather than sequence-based. SNIPE only encounters DNA
passing through the phage injection apparatus at the membrane. Host chromosomal DNA in the
cytoplasm is not accessible to the membrane-bound nuclease.

## Evolutionary Conservation

- 500+ homologues across bacterial phyla
- 33% of well-sequenced bacterial clades harbor at least one SNIPE homologue
- Some clades have SNIPE in up to 10% of genomes
- Found in prophages as well as chromosomal defense islands

## Key References

1. **Saxton, DeWeirdt, Doering, Roney & Laub (2026)** — "A membrane-bound nuclease directly cleaves phage
   DNA during genome injection." *Nature*. DOI: 10.1038/s41586-026-10207-1
   - Main characterization paper for SNIPE

2. **Vassallo, Doering, Littlehale, Teodoro & Laub (2022)** — "A functional selection reveals previously
   undetected anti-phage defence systems in the E. coli pangenome." *Nature Microbiology* 7:1568-1579.
   PMID:36123438
   - Original discovery of PD-lambda-1 from screen of 71 diverse E. coli strains

3. **Vassallo, Doering & Laub (2025)** — "E. coli prophages encode an arsenal of defense systems to
   protect against temperate phages." *Cell Host & Microbe*.
   - Follow-up showing PD-lambda-1 in prophage phiR26.1, defense in ECOR13 background

4. **PLOS Pathogens commentary (2026)** — "It's not me, it's you: Anti-phage nuclease specificity
   inside a bacterium." DOI: 10.1371/journal.ppat.1013959
   - Perspective placing SNIPE alongside Zorya and Kiwa as membrane-localized defense systems

## Related Defense Systems (Membrane-Localized)

- **Zorya** (Type I): ZorA/ZorB proton-driven rotary motor + ZorC/ZorD nucleases. PG-binding triggers activation.
- **Kiwa**: KwaA TM sensor + KwaB DNA-binding lattice. Forms "fence-like" supercomplex. Does NOT cleave DNA.
- **SNIPE**: Single-gene system. TM + DUF4041 + GIY-YIG nuclease. Directly cleaves DNA.

## Host Genes Involved

- **ManY** / **ManZ**: Mannose PTS permease inner membrane components. SNIPE associates with ManYZ.
  Certain phages use ManYZ as receptor for genome injection.

## Phages Tested Against

- Phage lambda (primary model)
- Diverse siphoviruses (likely including Bas14 based on TMP interaction data)

## Annotation Concerns

The InterPro-to-GO mapping for GIY-YIG domain (IPR047296) maps to GO:0006289 (nucleotide-excision repair),
based on UvrC. SNIPE uses GIY-YIG for phage DNA cleavage, NOT DNA repair. Automated annotation of 500+
SNIPE homologues through this InterPro entry would produce incorrect GO annotations.

## TODO

- [ ] Determine exact UniProt accession (check Saxton 2026 supplementary data)
- [ ] Determine exact E. coli strain source (likely ECOR26)
- [ ] Fetch UniProt flat file and GOA data once accession is known
- [ ] Complete annotation review
- [ ] Determine if any GO terms exist for "defense response to bacteriophage via DNA cleavage"

Last updated: 2026-03-01
