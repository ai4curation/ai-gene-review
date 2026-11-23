#!/usr/bin/env python3
"""Attach to an already-submitted OpenScientist job instead of submitting a new one.

Usage:
    uv run python scripts/openscientist_attach_job.py <job_id|submit> <deep-research-client research args...>

With ``submit`` in place of a job id, a new job is submitted normally but is still
polled without a client-side deadline or cancel, so it can wait out a busy queue.

The research args are the ones `scripts/gene_hypothesis_deep_research.py run ... --dry-run`
prints after `command=uv run deep-research-client`. This runs the normal
deep-research-client CLI with the OpenScientist provider patched so that:

- the job is not re-submitted (`_submit_job` returns <job_id>);
- polling has no client-side deadline, and the job is never cancelled by the client.
  The server queue can hold a job for hours, and the provider's normal timeout counts
  queue time and then cancels the job.

Output format, citations and artifacts are therefore identical to a regular run. Use
this when a local wrapper died (container restart) or timed out while its job was
still queued or running server-side. List jobs and their status with
GET https://www.openscientist.io/api/v1/jobs (Bearer OPENSCIENTIST_API_KEY).
"""

import sys

from deep_research_client.providers import openscientist as osp


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    job_id = sys.argv.pop(1)
    orig_poll = osp.OpenScientistProvider._poll_until_done

    async def _submit(self, client, query, max_iterations, *args, **kwargs):
        return job_id

    async def _poll(self, client, jid, timeout, poll_interval):
        return await orig_poll(self, client, jid, 10**7, poll_interval)

    async def _no_cancel(self, client, jid):
        return None

    if job_id != "submit":
        osp.OpenScientistProvider._submit_job = _submit
    osp.OpenScientistProvider._poll_until_done = _poll
    osp.OpenScientistProvider._cancel_job = _no_cancel

    from deep_research_client.cli import main as cli_main

    sys.argv[0] = "deep-research-client"
    return cli_main()


if __name__ == "__main__":
    sys.exit(main())
