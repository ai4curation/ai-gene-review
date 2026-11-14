# HemJ (Cereibacter sphaeroides 2.4.1, Q53229) review notes

UniProtKB: Q53229 (HEMJ_CERS4). No UniProt gene name; OrderedLocusName RHOS4_28450, ORF RSP_1232
(orf1 upstream of rho in PMID:8606169). Folder genes/CERS4/hemJ per task; gene_symbol set to the
ordered locus name RHOS4_28450 (as genes/PSEPK/PP_0431 does), because UniProt assigns no symbol.

## Deep research

Not available in this session (no provider keys / template missing). Built from UniProt and cached
literature.

## Biology

- The R. sphaeroides slr1790 (hemJ) homolog has Protox activity when expressed in E. coli.
  [PMID:20823222 "We overexpressed an slr1790 homolog of Rhodobacter sphaeroides in Escherichia coli and found that this recombinant protein possesses Protox activity in vitro."]
  Strain/locus not stated in the abstract; 2.4.1 has one HemJ, so attributed to Q53229.
- Synechocystis HemJ: heme b protein, dimer, no activity with O2/artificial acceptors.
  [PMID:29925590 "Using both oxygen and artificial electron acceptors, we detected no enzymatic activity with the purified HemJ.f"]
- A. baylyi hemJ deletion: heme auxotroph. [PMID:21642412 "the organism became auxotrophic for heme"]
- Alpha-proteobacteria use HemJ. [PMID:25108393 "Indeed, these bacteria possess HemJ sequences as do most of the other α-Proteobacteria, and therefore HemJ probably functions as a Protox in these bacteria."]

## Decisions

- GO:0070818 ACCEPT (acceptor-unspecified; agrees with coordinator PTHR40255 family review).
- plasma membrane IEA + ISS ACCEPT.
- heme biosynthetic process MODIFY -> heme B biosynthetic process.
- NEW bacteriochlorophyll biosynthetic process (IC), NEW heme binding (ISS).
