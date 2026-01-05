"""FastAPI backend for AI4CUI dashboard.

This API server provides HTTP endpoints for job status queries,
with in-memory caching to avoid blocking file I/O on every request.

Architecture:
- Loads all job statuses at startup (~17s for 343 genes)
- Caches in memory for fast reads
- Background task refreshes cache every 30s
- Dashboard queries via HTTP instead of direct file I/O

Example:
    # Start the API server (default port 5124)
    uv run python -m ai4cui.api

    # Or with custom port
    uv run python -m ai4cui.api --port 8000
"""

import asyncio
import sys
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import from local cyberian package
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "cyberian" / "src"))

from ai4cui.job_manager import JobManager
from ai4cui.models import JobStatus
from ai4cui.plugin import CurationPlugin


# Response models
class JobSummary(BaseModel):
    """Summary info for a job."""

    job_id: str
    display_name: str
    progress_percent: float
    status: str
    has_agent: bool
    agent_port: Optional[int] = None


class JobStatusResponse(BaseModel):
    """Detailed job status response."""

    job_id: str
    display_name: str
    status: str
    progress_percent: float
    has_agent: bool
    agent_port: Optional[int] = None
    agent_status: Optional[str] = None
    criteria_results: List[dict]
    error_message: Optional[str] = None


class StatsResponse(BaseModel):
    """Dashboard statistics."""

    total_jobs: int
    active_agents: int
    cache_age_seconds: float
    last_refresh: str


# Global state
status_cache: Dict[str, JobStatus] = {}
cache_timestamp: float = 0.0
job_manager: Optional[JobManager] = None
plugin_instance: Optional[CurationPlugin] = None


async def refresh_cache_background():
    """Background task to refresh the status cache periodically."""
    global status_cache, cache_timestamp

    while True:
        await asyncio.sleep(30)  # Refresh every 30 seconds

        try:
            print("[API] Refreshing status cache...")
            start = time.time()

            # Run blocking operation in thread pool
            loop = asyncio.get_event_loop()
            new_cache = await loop.run_in_executor(None, load_all_statuses)

            status_cache = new_cache
            cache_timestamp = time.time()

            elapsed = time.time() - start
            print(f"[API] Cache refreshed in {elapsed:.2f}s ({len(status_cache)} jobs)")

        except Exception as e:
            print(f"[API] Error refreshing cache: {e}")


def load_all_statuses() -> Dict[str, JobStatus]:
    """Load all job statuses (blocking operation for thread pool)."""
    if not job_manager or not plugin_instance:
        return {}

    job_ids = plugin_instance.get_all_job_ids()
    cache = {}

    for job_id in job_ids:
        try:
            cache[job_id] = job_manager.get_job_status(job_id)
        except Exception as e:
            print(f"[API] Error loading status for {job_id}: {e}")

    return cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown tasks."""
    global status_cache, cache_timestamp, job_manager, plugin_instance

    # Startup: Load cache
    print("[API] Starting up...")
    print("[API] Loading initial status cache (this may take ~17s for 343 jobs)...")

    # Import plugin (must be done here to get the right implementation)
    from ai_gene_review.plugins import GeneReviewProgressPlugin

    plugin_instance = GeneReviewProgressPlugin()
    job_manager = JobManager(plugin_instance)

    start = time.time()
    loop = asyncio.get_event_loop()
    status_cache = await loop.run_in_executor(None, load_all_statuses)
    cache_timestamp = time.time()

    elapsed = time.time() - start
    print(f"[API] Initial cache loaded in {elapsed:.2f}s ({len(status_cache)} jobs)")

    # Start background refresh task
    refresh_task = asyncio.create_task(refresh_cache_background())

    yield

    # Shutdown: Cancel background task
    print("[API] Shutting down...")
    refresh_task.cancel()


# Create FastAPI app
app = FastAPI(
    title="AI4CUI API",
    description="Fast HTTP API for AI curation job management",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware to allow dashboard to query API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to dashboard origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "cache_size": len(status_cache),
        "cache_age_seconds": time.time() - cache_timestamp if cache_timestamp else None,
    }


@app.get("/stats", response_model=StatsResponse)
async def get_stats():
    """Get dashboard statistics."""
    if not job_manager:
        raise HTTPException(status_code=503, detail="Job manager not initialized")

    running_agents = job_manager.get_running_agents()

    from datetime import datetime

    return StatsResponse(
        total_jobs=len(status_cache),
        active_agents=len(running_agents),
        cache_age_seconds=time.time() - cache_timestamp,
        last_refresh=datetime.fromtimestamp(cache_timestamp).isoformat(),
    )


@app.get("/jobs", response_model=List[JobSummary])
async def list_jobs():
    """List all jobs with summary info.

    Returns cached status for all jobs (~300 jobs).
    Payload size: ~30KB JSON for 300 jobs (totally fine).
    """
    if not plugin_instance:
        raise HTTPException(status_code=503, detail="Plugin not initialized")

    summaries = []

    for job_id, status in status_cache.items():
        try:
            job = plugin_instance.get_job(job_id)
            summaries.append(
                JobSummary(
                    job_id=job_id,
                    display_name=job.display_name,
                    progress_percent=status.progress_percent,
                    status=status.status.value,
                    has_agent=status.has_agent,
                    agent_port=status.agent_port,
                )
            )
        except Exception as e:
            print(f"[API] Error getting job summary for {job_id}: {e}")

    return summaries


@app.get("/jobs/{job_id:path}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """Get detailed status for a specific job.

    Args:
        job_id: Job identifier (e.g., "human/TP53")

    Returns:
        Detailed job status from cache (instant)
    """
    if not plugin_instance:
        raise HTTPException(status_code=503, detail="Plugin not initialized")

    # Get from cache
    status = status_cache.get(job_id)
    if not status:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    try:
        job = plugin_instance.get_job(job_id)
        criteria = plugin_instance.get_progress_criteria(job_id)

        # Convert criteria results to dict
        criteria_dicts = []
        for i, result in enumerate(status.criteria_results):
            crit = criteria[i] if i < len(criteria) else None
            criteria_dicts.append(
                {
                    "name": crit.name if crit else "Unknown",
                    "met": result.met,
                    "message": result.message,
                    "hint": result.hint,
                }
            )

        return JobStatusResponse(
            job_id=job_id,
            display_name=job.display_name,
            status=status.status.value,
            progress_percent=status.progress_percent,
            has_agent=status.has_agent,
            agent_port=status.agent_port,
            agent_status=status.agent_status,
            criteria_results=criteria_dicts,
            error_message=status.error_message,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting job status: {e}")


@app.post("/jobs/{job_id:path}/refresh")
async def refresh_job_status(job_id: str):
    """Force refresh status for a specific job.

    Useful after agent makes changes and user wants immediate update.
    """
    global status_cache, cache_timestamp

    if not job_manager:
        raise HTTPException(status_code=503, detail="Job manager not initialized")

    if job_id not in status_cache:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    try:
        # Refresh this one job (blocking, but just one is fast)
        loop = asyncio.get_event_loop()
        new_status = await loop.run_in_executor(None, job_manager.get_job_status, job_id)

        status_cache[job_id] = new_status
        cache_timestamp = time.time()

        return {"status": "ok", "job_id": job_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refreshing job: {e}")


@app.post("/cache/refresh")
async def refresh_cache():
    """Force refresh of entire cache.

    This is a manual trigger for the background refresh.
    Takes ~17s for 343 jobs.
    """
    global status_cache, cache_timestamp

    print("[API] Manual cache refresh triggered...")
    start = time.time()

    loop = asyncio.get_event_loop()
    new_cache = await loop.run_in_executor(None, load_all_statuses)

    status_cache = new_cache
    cache_timestamp = time.time()

    elapsed = time.time() - start

    return {
        "status": "ok",
        "jobs_refreshed": len(status_cache),
        "elapsed_seconds": elapsed,
    }


def create_app(plugin: CurationPlugin) -> FastAPI:
    """Create FastAPI app with custom plugin.

    Args:
        plugin: CurationPlugin implementation

    Returns:
        Configured FastAPI app
    """
    global plugin_instance, job_manager

    plugin_instance = plugin
    job_manager = JobManager(plugin)

    return app


if __name__ == "__main__":
    import uvicorn

    # Parse command line args for port
    port = 5124
    if len(sys.argv) > 1 and sys.argv[1] == "--port":
        port = int(sys.argv[2])

    print(f"[API] Starting AI4CUI API server on port {port}...")
    print(f"[API] Dashboard should query http://localhost:{port}")

    uvicorn.run(app, host="0.0.0.0", port=port)
