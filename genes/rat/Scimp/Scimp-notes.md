# Scimp (rat, A0ABK0LNG9; RGD:1593299) review notes

Reviewed together with human SCIMP (Q6UWF3) and mouse Scimp (Q3UU41); see
`genes/human/SCIMP/SCIMP-notes.md` for the literature summary. No deep research was run
separately for rat (the provider failed for human and mouse with an authentication error) and no
rat-specific literature was found: a PubMed search for SCIMP returns no rat functional studies.

The UniProt entry is unreviewed (TrEMBL). Every GOA row is either an ISO transfer from mouse
Scimp (MGI:3610314) or human SCIMP, or an InterPro (IPR028181) mapping. Each row therefore gets
the same action as the matching row in the source review: signaling adaptor activity replaces
molecular adaptor activity, plasma membrane replaces membrane, TLR4 signalling, IL-6/IL-12
production and ERK1/2 regulation are accepted, and the remaining processes and locations are kept
as non-core.

GO-CAM: no production GO-CAM model includes SCIMP in any species (checked the local
`gocams/index.tsv` and the GO API `gp/<id>/models` for human and mouse on 2026-10-16).

Toll-like receptor 4 binding (GO:0035662) is proposed for human SCIMP by similarity to mouse but
not for rat. The human UniProt entry carries curated SUBUNIT text recording the TLR4 interaction
(By similarity); the rat entry is unreviewed TrEMBL with no SUBUNIT text, and conservation of the
interaction-relevant residues in rat has not been checked (see the first suggested question).
