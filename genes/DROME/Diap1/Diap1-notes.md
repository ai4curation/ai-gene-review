# Diap1 notes

Reviewed `Diap1` for the APOPTOSIS conserved-comparator slice.

DIAP1 is the essential fly IAP-family brake on inappropriate caspase
activity. It binds caspases through BIR domains and uses its C-terminal RING
E3 activity to ubiquitylate the initiator caspase Dronc and the effector
caspases DrICE and Dcp-1. The clearest Dronc paper mapped the Dronc-binding
surface on BIR2 and found that the same surface is competed by Reaper, Hid,
and Grim [PMID:14517550, "the second BIR (BIR2) domain of DIAP1 recognizes a
12-residue sequence in Dronc"]. The effector-caspase work showed that cleaved
DIAP1 binds Dronc, DrICE, and Dcp-1, and that "DIAP1, blocks effector
caspases by targeting them for polyubiquitylation and nonproteasomal
inactivation" [PMID:19026784]. I treated generic `protein binding` rows for
Dronc, DrICE, and Dcp-1 as candidates for `GO:0089720 caspase binding`.

The Reaper/Hid/Grim, Sickle, Jafrac2, and dOmi/HtrA2 rows are real physical
interactions with Diap1 regulators rather than separate Diap1 catalytic
activities. Reaper, Hid, and Grim trigger apoptosis by binding DIAP1
[PMID:10675328, "REAPER and HID with DIAP1 is critical for the induction of
apoptosis"]; Sickle is an IAP-binding protein whose N terminus bound BIR2
[PMID:11818065, "specifically bound to the BIR2 domain of DIAP1"]; mature
Jafrac2 binds DIAP1 and displaces Dronc [PMID:12356728, "Jafrac2 displaces
Dronc from DIAP1"]; and dOmi/HtrA2 both antagonizes DIAP1 and can be
polyubiquitinated by DIAP1 [PMID:18259196, "DIAP1 induces
polyubiquitination of dOmi"]. I kept these as non-core binding rows unless the
local source did not expose the exact figure-level interaction.

Several `GO:0000209 protein polyubiquitination` rows are direct but describe
different substrates. DTRAF1 is degraded in a DIAP1/ubiquitin-dependent branch
that restrains JNK [PMID:12198495, "DIAP1-induced DTRAF1 degradation"]. Dronc
is directly ubiquitinated by the DIAP1 RING [PMID:12021771, "promotes the
ubiquitination of both itself and of Dronc"]. DIAP1 autoubiquitination exists
but probably uses Lys63 rather than Lys48 chains [PMID:17205079, "does not
involve formation of Lys48-based polyubiquitin chains"]. Grim can be
K48-ubiquitinated by DIAP1 in a UbcD1-dependent manner [PMID:23940367,
"K48-linked ubiquitin chains are added almost exclusively to BIR2-bound
Grim"]. DIAP1 also has a NEDD8-E3 branch that neddylates effector caspases
[PMID:21145488, "targeting effector caspases for neddylation and
inactivation"].

Nonapoptotic developmental rows need careful separation from core apoptosis.
The border-cell migration row is direct enough to keep as non-core because
Diap1-mediated Dronc inhibition modulates Rac-dependent motility rather than
cell survival [PMID:15242648, "apoptosis-independent role for DIAP1-mediated
Dronc inhibition in Rac-mediated cell motility"]. SOP/chaeta development is
also direct but non-core: DmIKKepsilon-dependent turnover of DIAP1 gates
Dronc activity during shaft-cell morphogenesis [PMID:19822670, "the temporal
regulation of DIAP1 turnover determines whether caspases function
nonapoptotically"]. By contrast, overexpressing DIAP1 in spermatids in
PMID:14737191 was used as a caspase-inhibition tool, so it establishes a
requirement for caspase activity rather than an endogenous Diap1
individualization function. The 2022 Toll row is even more indirect: the paper
shows DrICE/Dcp-1 cleavage of DIF, while Diap1 is only an upstream inhibitor of
those effector caspases.

The Wnt/Wingless rows were kept as non-core. They reflect a conserved nuclear
IAP E3 output in which DIAP1/XIAP promotes canonical Wnt signaling through
Groucho/TLE ubiquitination and release from TCF/Lef [PMID:22304967,
"identified DIAP1 as a positive regulator of Wingless signaling in a
Drosophila S2 cell-based RNAi screen"].
