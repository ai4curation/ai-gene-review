# PGL-1 focused report assessment, 2026-09-21

The OpenScientist report and its HTML/PDF artifacts were read and critically compared
with the exact PAINT lineage, live sequence/domain records, and primary experiments.
The report supports the established RNA-binding/RNase scaffold model and identifies
a meaningful structural conflict with conventional DEAD-box ancestry. Its stronger
claim that helicase, splicing and export have been experimentally refuted is not
supported. All three existing annotations remain UNDECIDED. This is a completed
report review with a specific curator follow-up, not a request for duplicate research.

## Provider claims and independent checks

The report is `pgl-1-hypotheses/pgl-fold-and-inherited-helicase-rna-processing/openscientist.md`.
The HTML and PDF contain the same substantive conclusions and limitations, with no
executable sequence-analysis artifacts. The report proposes removing or negating the
three inherited terms, while explicitly acknowledging that noncatalytic participation
is untested and that the actual PAINT topology was not independently reconstructed.

1. The motif scan needs correction. Its strict GxxxxGKT/S and QxxGRxGR patterns fail
   on the report's own GLH-1 control. The actual control sites are AQTGSGKT (385–392)
   and HRIGRTGR (692–699); DEAD is present at 499–502. Expanded patterns recover
   those sites and remain absent in PGL-1. This is reproducible evidence against a
   conventional DEAD-box architecture, not a functional assay or a universal
   catalytic-residue-loss test. See pgl-1-bioinformatics/RESULTS.md.
2. The live PTHR23237 GAR1 match covers only PGL-1 residues 629–728, with reported
   score 0.00072, in its RGG-rich tail. Strong PGL_N and PGL_C matches cover 10–211
   and 220–448. A partial GAR1 match does not reclassify the full protein, establish
   a GAR1 biological function, or independently demonstrate a PAINT misgraft.
3. The actual tree contains exact Q9TZQ3/PTN002773363 below all three relevant
   positive IBD nodes, without either known helicase-loss node on its lineage.
   Its DDX39-like neighbors include HEL-1 and Hel25E. No checked evidence establishes
   the report's proposed GLH/PGL partner-confusion mechanism. Co-localization does
   not itself explain a sequence-based tree. The unresolved issue is the alignment
   and sequence identity supporting this actual placement, not donor number.
4. The report's restriction of mRNA export work to the inner nuclear face is too
   narrow. The live GO definition describes directed movement to the cytoplasm.
   Perinuclear P granules receive nascent exported transcripts (PMID:20223759,
   granule-level evidence; cached abstract only). Full PMID:22991439 discusses
   granules as an extension of the pore environment and demonstrates PGL-1-dependent
   recruitment of FBF-2 and efficient target-mRNA binding. These observations do not
   prove that PGL-1 executes export, but cytoplasmic localization does not refute it.
5. The report calls the RNase-T1 annotation experimental. The current source row is
   IEA from EC mapping and is preserved as supplied. Primary IDA supports the broader
   RNA endonuclease row. The report's blanket characterization of other germline
   phenotypes as indirect does not replace the source-specific review of regulatory
   work, including CED-4 protein regulation in the retained apoptosis proposal.

## Primary structure and catalytic scope

PMID:26787882 was read from the full six-page OSTI article, including Results,
Figures 1–4 and Methods, saved in pgl-1-primary-evidence/ with hashes. The main cache
contains only Abstract/Discussion despite its full-text flag; it was not overwritten.
The 13-alpha-helical dimerization structure concerns a central protein fragment,
with C. remanei and C. elegans domain structures. It is not a full-length structure.
The paper demonstrates guanosine-specific single-stranded RNA cleavage by the
C. elegans recombinant domain. A longer pos-1 RNA was an in vitro substrate;
physiological substrates were not identified.

The complementary-oligonucleotide experiment measures protection of duplex RNA
from cleavage, not ATP-dependent strand unwinding. Its cleavage buffer contains
EDTA and no added ATP. ATP used during RNA preparation supplies radiolabel, not
energy for an unwinding assay. No direct helicase-negative assay is reported in
these Results or Methods. The current GO:0003724 definition explicitly requires
ATP-driven unwinding, so a dedicated unwinding/ATP-turnover experiment would be
needed to test that claim directly.

Q342A strongly reduces RNase activity while preserving dimerization and RNA binding,
which supports attribution of the measured cleavage to PGL-1. Endogenous Q342A
animals retained fertility in the tested conditions, including 26.5 degrees C,
where pgl-1-null animals were sterile. That distinguishes RNase activity from the
fertility requirement; it does not establish that RNase activity has no in vivo
function in any condition. The catalytic chemistry remains unresolved. This novel
RNase itself illustrates why absence of a familiar enzyme motif is not a universal
negative functional test.

## Later primary evidence omitted from the report

Full PMID:33579952, including Results and Methods, adds an N-terminal dimerization
domain and an assay of RNA repression. The 1.5-angstrom structure is from C. japonica
PGL-1, with eleven alpha helices and one beta strand. C. elegans PGL-1/PGL-3 NtDD
biochemistry and C. elegans gene editing test the conserved assembly interface.
Assembly-disrupting mutations impair granules and fertility. This does not turn the
two partial domain structures into an experimentally solved full-length structure.

PGL-1 tethered to a reporter mRNA promotes repression in heterozygous animals;
the tethered PGL-1 homozygotes were sterile. PGL-3 tethering did not reproduce this
repression. WAGO-1 loss strongly but incompletely relieves repression even while
PGL-1 granules remain, showing that assembly alone is insufficient. Reporter-mRNA
abundance changes are consistent with turnover, but the experiments do not assign
that turnover to PGL-1 RNase catalysis or identify native cleavage targets. This
supports the scaffold's direct organizational work in post-transcriptional RNA
regulation, separately from its in vitro RNase activity. No NEW process row is added.

## Remaining questions

- Can a PAINT curator inspect the exact Q9TZQ3 sequence/MSA correspondence beneath
  PTN002774595 and PTN002776405 and reconcile it with both PGL dimerization domains?
  The positive topology is established; neither partner confusion nor a full-length
  GAR1 reassignment has been demonstrated.
- Does full-length PGL-1 have ATP-driven RNA-unwinding activity under appropriate
  substrate/cofactor conditions? The published RNase assay is not that test.
- Does PGL-1 itself contribute to spliceosomal processing or the export step, including
  a noncatalytic scaffold role, independently of the helicase claim? Target-resolved
  processing/export measurements would discriminate this from post-export repression.

The provider's exact hypothesis already covers these open issues; another identical
provider request is not justified. Retain the three UNDECIDED source assertions,
maintain the experimentally supported scaffold/RNA functions, and seek curator or
new experimental resolution of the specified conflict.
