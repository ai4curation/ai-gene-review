#!/usr/bin/env python3
"""Run ProTrek sequence-to-text retrieval for a set of query proteins.

ProTrek (Su et al., Nat Biotechnol 2026, doi:10.1038/s41587-025-02836-0) is a
contrastive trimodal model; it does not emit GO terms directly. Its
protein-to-function "prediction" is a nearest-neighbour retrieval of UniProt
annotation sentences from a precomputed text index. This script reproduces the
`sequence -> text` mode of the public server (search-protrek.com) locally:

  1. embed each query amino-acid sequence with the ProTrek protein encoder
     (ESM-2 650M backbone + projection to the 1024-d joint space),
  2. search the released SwissProt faiss text indexes for the closest
     annotation sentences in each requested subsection,
  3. write the ranked hits, with the ProTrek score (inner product / temperature).

Only the protein encoder is needed: the text side is the precomputed index.

Prerequisites (not committed - see README.md in this directory):
  weights/ProTrek_650M/            from https://huggingface.co/westlake-repl/ProTrek_650M
  faiss_index/<Subsection>.index   from https://huggingface.co/datasets/westlake-repl/faiss_index
  faiss_index/<Subsection>_ids.tsv   (SwissProt/ProTrek_650M_UniRef50/text/subsections/)

Example:
  python run_protrek_retrieval.py \
      --weights /path/weights/ProTrek_650M \
      --faiss-dir /path/faiss_index \
      --queries argo50_sequences.tsv \
      --subsections GO_annotation Function Subcellular_location Catalytic_activity \
      --topk 20 --out argo50_protrek_hits.tsv
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

import faiss
import numpy as np
import torch
from torch.nn.functional import normalize
from transformers import EsmConfig, EsmModel, EsmTokenizer


class ProTrekProteinEncoder(torch.nn.Module):
    """Protein branch of the ProTrek trimodal model.

    Mirrors model/ProTrek/protein_encoder.py in westlake-repl/ProTrek: the CLS
    hidden state of the ESM-2 backbone passed through a linear projection to the
    shared 1024-d space, then L2-normalised.
    """

    def __init__(self, esm_dir: Path, checkpoint: Path, repr_dim: int = 1024):
        super().__init__()
        config = EsmConfig.from_pretrained(str(esm_dir))
        self.esm = EsmModel(config, add_pooling_layer=False)
        self.out = torch.nn.Linear(config.hidden_size, repr_dim)
        self.tokenizer = EsmTokenizer.from_pretrained(str(esm_dir))

        state = torch.load(str(checkpoint), map_location="cpu", weights_only=False)["model"]
        # Checkpoint keys are indexed by encoder slot: 1 = protein, 2 = text,
        # 3 = structure, "0" = learnable temperature.
        self.temperature = float(state["0"])
        esm_sd, out_sd = {}, {}
        for key, value in state.items():
            if key.startswith("1.model.esm."):
                esm_sd[key[len("1.model.esm."):]] = value
            elif key.startswith("1.out."):
                out_sd[key[len("1.out."):]] = value
        missing, unexpected = self.esm.load_state_dict(esm_sd, strict=False)
        # contact_head is dropped by ProTrek; position_ids/position_embeddings are
        # non-parameters under the rotary embedding configuration.
        ignorable = ("contact_head", "position_ids", "position_embeddings")
        unexpected = [k for k in unexpected if not any(i in k for i in ignorable)]
        missing = [k for k in missing if not any(i in k for i in ignorable)]
        if missing or unexpected:
            raise RuntimeError(f"ESM weight mismatch: missing={missing[:5]} unexpected={unexpected[:5]}")
        self.out.load_state_dict(out_sd)
        self.eval()

    @torch.no_grad()
    def embed(self, sequences: list[str], max_len: int | None = None) -> np.ndarray:
        vecs = []
        for seq in sequences:
            if max_len is not None and len(seq) > max_len:
                seq = seq[:max_len]
            inputs = self.tokenizer(seq, return_tensors="pt")
            hidden = self.esm(**inputs).last_hidden_state[:, 0, :]
            vecs.append(normalize(self.out(hidden), dim=-1))
        return torch.cat(vecs, dim=0).numpy().astype("float32")


def load_index(faiss_dir: Path, subsection: str):
    index = faiss.read_index(str(faiss_dir / f"{subsection}.index"), faiss.IO_FLAG_MMAP)
    index.metric_type = faiss.METRIC_INNER_PRODUCT
    texts = (faiss_dir / f"{subsection}_ids.tsv").read_text().splitlines()
    if index.ntotal != len(texts):
        raise RuntimeError(f"{subsection}: index has {index.ntotal} vectors but {len(texts)} texts")
    return index, texts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--weights", required=True, type=Path, help="ProTrek_650M weights directory")
    ap.add_argument("--faiss-dir", required=True, type=Path, help="directory holding <Subsection>.index / _ids.tsv")
    ap.add_argument("--queries", required=True, type=Path, help="TSV with accession + sequence columns")
    ap.add_argument("--subsections", nargs="+", default=["GO_annotation"])
    ap.add_argument("--topk", type=int, default=20)
    ap.add_argument("--max-len", type=int, default=None, help="truncate query sequences to this many residues")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--embeddings-out", type=Path, default=None, help="optional .npz of query embeddings")
    args = ap.parse_args()

    rows = list(csv.DictReader(args.queries.open(), delimiter="\t"))
    accs = [r["accession"] for r in rows]
    seqs = [r["sequence"] for r in rows]
    print(f"loaded {len(rows)} query proteins", file=sys.stderr)

    encoder = ProTrekProteinEncoder(args.weights / "esm2_t33_650M_UR50D", args.weights / "ProTrek_650M.pt")
    print(f"model loaded (temperature={encoder.temperature:.6f})", file=sys.stderr)

    t0 = time.time()
    embs = []
    for i, (acc, seq) in enumerate(zip(accs, seqs), 1):
        embs.append(encoder.embed([seq], max_len=args.max_len))
        print(f"  [{i}/{len(accs)}] {acc} len={len(seq)} ({time.time() - t0:.0f}s)", file=sys.stderr)
    emb = np.concatenate(embs, axis=0)

    if args.embeddings_out:
        np.savez_compressed(args.embeddings_out, accessions=np.array(accs), embeddings=emb)

    with args.out.open("w", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(["accession", "subsection", "rank", "protrek_score", "cosine", "text"])
        for subsection in args.subsections:
            index, texts = load_index(args.faiss_dir, subsection)
            print(f"searching {subsection} ({index.ntotal} entries)", file=sys.stderr)
            scores, ids = index.search(emb, args.topk)
            for acc, srow, irow in zip(accs, scores, ids):
                for rank, (s, idx) in enumerate(zip(srow, irow), 1):
                    if idx < 0:
                        continue
                    writer.writerow([acc, subsection, rank,
                                     f"{s / encoder.temperature:.4f}", f"{s:.6f}", texts[idx]])
    print(f"wrote {args.out}", file=sys.stderr)

    meta = {
        "model": "ProTrek_650M",
        "temperature": encoder.temperature,
        "n_queries": len(accs),
        "subsections": args.subsections,
        "topk": args.topk,
        "max_len": args.max_len,
        "text_db": "SwissProt/ProTrek_650M_UniRef50",
    }
    args.out.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
