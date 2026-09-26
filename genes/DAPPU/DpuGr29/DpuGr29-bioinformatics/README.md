# DpuGr29 motif check

Run `just` in this folder. Standard-library Python, managed by the local uv project, reads the unchanged cached UniProt inputs and searches the explicitly supplied `TY.{5}QF` pattern used by the provider. The second input is unrelated human AKIRIN1, a parser/generalization control rather than a biological loss test. JSON outputs contain exact input hashes, sequence length and 1-based coordinates. This is a sequence-pattern check only: it does not compute structural alignment, channel opening, ion selectivity or oligomerization.
