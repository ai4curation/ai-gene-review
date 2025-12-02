"""Fast NiceGUI dashboard using FastAPI backend.

This dashboard queries a FastAPI server for job statuses instead of
doing file I/O directly. Much faster and more responsive.

Architecture similar to Cyberian dashboard:
- All job data comes from HTTP GET /jobs (cached by API)
- Agent monitoring via async HTTP (5-10 agents max)
- No blocking file I/O in the dashboard
- Pagination is instant (just slicing in-memory list)

Usage:
    # Start API server first (in separate terminal)
    uv run python -m ai4cui.api

    # Then start dashboard
    uv run python -m ai4cui --use-api
"""

import asyncio
import httpx
from datetime import datetime
from typing import Dict, List, Optional

from nicegui import ui

from ai4cui.job_manager import JobManager
from ai4cui.plugin import CurationPlugin


class JobSummary:
    """Client-side model for job summary from API."""

    def __init__(self, data: dict):
        self.job_id: str = data["job_id"]
        self.display_name: str = data["display_name"]
        self.progress_percent: float = data["progress_percent"]
        self.status: str = data["status"]
        self.has_agent: bool = data["has_agent"]
        self.agent_port: Optional[int] = data.get("agent_port")


class CurationDashboardV2:
    """Fast dashboard that queries FastAPI backend.

    No file I/O - all data from HTTP endpoints.
    Similar architecture to Cyberian dashboard.
    """

    def __init__(
        self,
        plugin: CurationPlugin,
        title: str = "AI Curation Dashboard",
        api_base_url: str = "http://localhost:5124",
    ):
        """Initialize dashboard.

        Args:
            plugin: CurationPlugin (still needed for agent operations)
            title: Dashboard title
            api_base_url: Base URL for FastAPI backend
        """
        self.plugin = plugin
        self.title = title
        self.api_base_url = api_base_url
        self.manager = JobManager(plugin)

        # UI state (all from API cache, no file I/O)
        self.jobs: List[JobSummary] = []
        self.jobs_per_page = 50
        self.current_page = 0

        # Agent monitoring state (async HTTP only)
        self.agent_states: Dict[str, dict] = {}
        self.agent_monitor_task = None

        # Containers for dynamic updates
        self.stats_container = None
        self.jobs_container = None

    def build(self) -> None:
        """Build the dashboard UI.

        Creates the main dashboard page at the root path.
        """
        @ui.page('/')
        def main_page():
            """Main dashboard page."""
            self._build_ui()

    def _build_ui(self) -> None:
        """Build the dashboard UI components."""
        ui.page_title(self.title)

        with ui.header().classes("items-center justify-between"):
            ui.label(self.title).classes("text-2xl")
            with ui.row().classes("items-center gap-4"):
                ui.button("Refresh Jobs", on_click=lambda: asyncio.create_task(self.refresh_jobs())).props(
                    "flat icon=refresh size=sm"
                ).tooltip("Refresh job list from API")

        with ui.column().classes("w-full p-4"):
            # Stats row
            with ui.row().classes("w-full gap-4 mb-4"):
                self.stats_container = ui.row().classes("gap-4")

            # Job list
            with ui.column().classes("w-full gap-2"):
                self.jobs_container = ui.column().classes("w-full gap-2")

        # Start agent monitor (only monitors RUNNING agents via HTTP)
        self.agent_monitor_task = ui.timer(5, lambda: asyncio.create_task(self._monitor_agents()))

        # Initial load (async from API) - use timer to schedule after event loop starts
        ui.timer(0.1, lambda: asyncio.create_task(self.startup()), once=True)

    async def startup(self):
        """Startup: load jobs from API."""
        # Check if API is available
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f"{self.api_base_url}/health", timeout=2.0)
                if resp.status_code != 200:
                    ui.notify(
                        f"API server returned {resp.status_code}. Is it running?",
                        type="negative",
                        timeout=10000,
                    )
                    return
        except httpx.ConnectError:
            ui.notify(
                f"Cannot connect to API at {self.api_base_url}. Start it with: just ui-api",
                type="negative",
                timeout=10000,
            )
            return
        except Exception as e:
            ui.notify(f"Error connecting to API: {e}", type="negative", timeout=10000)
            return

        # Load data from API
        await self.refresh_stats()
        await self.refresh_jobs()

    async def refresh_stats(self):
        """Refresh statistics from API."""
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f"{self.api_base_url}/stats", timeout=5.0)
                if resp.status_code == 200:
                    stats = resp.json()

                    self.stats_container.clear()
                    with self.stats_container:
                        self._stat_card("Total Jobs", stats["total_jobs"], "blue")
                        self._stat_card("Active Agents", stats["active_agents"], "purple")

                        # Show cache age
                        cache_age = stats.get("cache_age_seconds", 0)
                        with ui.card().classes("bg-gray-100 p-4"):
                            ui.label("Cache Age").classes("text-sm text-gray-600")
                            ui.label(f"{cache_age:.0f}s").classes("text-xl font-bold")

        except Exception as e:
            print(f"[Dashboard] Error fetching stats: {e}")
            ui.notify(f"Failed to fetch stats: {e}", type="negative")

    async def refresh_jobs(self):
        """Refresh job list from API (fast - just HTTP GET)."""
        try:
            async with httpx.AsyncClient() as client:
                # GET /jobs returns all ~300 jobs with summary info
                # Payload: ~30KB JSON, totally fine
                resp = await client.get(f"{self.api_base_url}/jobs", timeout=10.0)

                if resp.status_code == 200:
                    jobs_data = resp.json()
                    self.jobs = [JobSummary(j) for j in jobs_data]

                    # Sort: running agents first, then by progress (low to high)
                    running_agents = self.manager.get_running_agents()
                    self.jobs.sort(
                        key=lambda j: (
                            0 if j.job_id in running_agents else 1,  # Running first
                            j.progress_percent,  # Then by progress
                            j.job_id,  # Then alphabetically
                        )
                    )

                    # Render
                    await self._render_jobs()

                else:
                    ui.notify(f"API error: {resp.status_code}", type="negative")

        except httpx.ConnectError:
            ui.notify(
                "Cannot connect to API server. Start it with: uv run python -m ai4cui.api",
                type="negative",
                timeout=10000,
            )
        except Exception as e:
            print(f"[Dashboard] Error refreshing jobs: {e}")
            ui.notify(f"Failed to refresh jobs: {e}", type="negative")

    async def _monitor_agents(self):
        """Monitor ONLY running agents via async HTTP.

        Same as before - polls agent status and messages.
        """
        try:
            running = self.manager.get_running_agents()  # {job_id: port}

            if not running:
                return

            # Monitor each running agent
            for job_id, port in running.items():
                try:
                    async with httpx.AsyncClient() as client:
                        # Get status
                        status_resp = await client.get(f"http://localhost:{port}/status", timeout=2.0)
                        status_data = status_resp.json()
                        agent_status = status_data.get("status", "unknown")

                        # Get ALL messages to count and get most recent
                        msg_resp = await client.get(f"http://localhost:{port}/messages", timeout=2.0)
                        msg_data = msg_resp.json()
                        messages = msg_data.get("messages", [])

                        # Update agent state
                        self.agent_states[job_id] = {
                            "status": agent_status,
                            "last_message": messages[-1] if messages else None,
                            "message_count": len(messages),
                        }

                except Exception as e:
                    print(f"[Dashboard] Error monitoring {job_id} on port {port}: {e}")
                    continue

        except Exception as e:
            print(f"[Dashboard] Error in agent monitor: {e}")

    def _stat_card(self, label: str, value: int, color: str) -> None:
        """Render a statistics card."""
        with ui.card().classes(f"bg-{color}-100 p-4"):
            ui.label(label).classes("text-sm text-gray-600")
            ui.label(str(value)).classes("text-3xl font-bold")

    async def _render_jobs(self) -> None:
        """Render job list with pagination.

        Instant - just slicing in-memory list (no file I/O).
        """
        self.jobs_container.clear()

        with self.jobs_container:
            # Calculate pagination
            start_idx = self.current_page * self.jobs_per_page
            end_idx = start_idx + self.jobs_per_page
            page_jobs = self.jobs[start_idx:end_idx]

            # Show pagination controls if needed
            total_pages = (len(self.jobs) + self.jobs_per_page - 1) // self.jobs_per_page
            if total_pages > 1:
                with ui.row().classes("w-full justify-between items-center mb-4"):
                    ui.label(
                        f"Showing {start_idx + 1}-{min(end_idx, len(self.jobs))} of {len(self.jobs)} jobs"
                    ).classes("text-sm text-gray-600")

                    with ui.row().classes("gap-2"):
                        ui.button(
                            "Previous",
                            on_click=lambda: asyncio.create_task(self._previous_page()),
                        ).props("flat size=sm").set_enabled(self.current_page > 0)

                        ui.label(f"Page {self.current_page + 1} of {total_pages}").classes("text-sm")

                        ui.button(
                            "Next",
                            on_click=lambda: asyncio.create_task(self._next_page()),
                        ).props("flat size=sm").set_enabled(self.current_page < total_pages - 1)

            # Render jobs for current page
            for job in page_jobs:
                self._render_job_card(job)

    async def _previous_page(self) -> None:
        """Go to previous page."""
        if self.current_page > 0:
            self.current_page -= 1
            await self._render_jobs()

    async def _next_page(self) -> None:
        """Go to next page."""
        total_pages = (len(self.jobs) + self.jobs_per_page - 1) // self.jobs_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            await self._render_jobs()

    def _render_job_card(self, job: JobSummary) -> None:
        """Render a single job card.

        All data from in-memory JobSummary (fast).
        """
        # Get monitored agent state if available
        agent_state = self.agent_states.get(job.job_id, {})

        # Color based on status
        status_colors = {
            "completed": "green",
            "agent_running": "purple",
            "in_progress": "orange",
            "not_started": "gray",
        }
        border_color = status_colors.get(job.status, "gray")

        with ui.card().classes(f"w-full border-l-4 border-{border_color}-500"):
            with ui.row().classes("w-full items-center justify-between"):
                # Left: Job info
                with ui.column().classes("flex-1"):
                    ui.label(job.display_name).classes("text-lg font-bold")
                    ui.label(job.job_id).classes("text-sm text-gray-500")

                    # Progress bar
                    with ui.row().classes("items-center gap-2 mt-2"):
                        ui.linear_progress(
                            value=job.progress_percent / 100,
                            show_value=False,
                        ).classes("flex-1")
                        ui.label(f"{job.progress_percent:.0f}%").classes("text-sm")

                    # Agent info
                    if job.has_agent:
                        monitored_status = agent_state.get("status", "")
                        status_emoji = "💭" if monitored_status.lower() in ["idle", "ready", "stable", "waiting"] else "⚙️"

                        agent_label = f"{status_emoji} Agent on port {job.agent_port}"
                        if monitored_status:
                            agent_label += f" ({monitored_status})"

                        # Add message count if available
                        msg_count = agent_state.get("message_count", 0)
                        if msg_count > 0:
                            agent_label += f" · {msg_count} messages"

                        ui.label(agent_label).classes("text-sm text-purple-600")

                        chat_url = f"http://localhost:{job.agent_port}/chat"
                        ui.link("Open Chat", chat_url, new_tab=True).classes(
                            "text-xs text-blue-600 underline"
                        ).tooltip("Open agent chat interface in new tab")

                    # Show most recent agent message (from monitored state)
                    last_msg = agent_state.get("last_message")
                    if last_msg:
                        role = last_msg.get("role", "unknown")
                        content = last_msg.get("content", "")
                        # Truncate to 150 chars
                        truncated = content[:150] + ("..." if len(content) > 150 else "")
                        # Show with subtle styling
                        msg_label = f"💬 {role}: {truncated}"
                        ui.label(msg_label).classes("text-xs text-gray-600 italic mt-1")

                # Right: Actions
                with ui.column().classes("gap-2"):
                    if job.has_agent:
                        # Show Play button if agent is idle/stable
                        monitored_status = agent_state.get("status", "")
                        is_idle = monitored_status.lower() in ["idle", "ready", "stable", "waiting"]

                        if is_idle:
                            ui.button(
                                "▶ Play",
                                on_click=lambda j=job.job_id: self._send_initial_message(j),
                            ).props("flat color=green size=sm").tooltip(
                                "Send instructions + progress report to start work"
                            )

                        ui.button(
                            "Send Message",
                            on_click=lambda j=job.job_id: self._show_message_dialog(j),
                        ).props("flat size=sm")

                        ui.button(
                            "Stop Agent",
                            on_click=lambda j=job.job_id: self._stop_agent(j),
                        ).props("flat color=red size=sm")

                        ui.button(
                            "Details",
                            on_click=lambda j=job.job_id: self._show_details(j),
                        ).props("flat size=sm")
                    else:
                        ui.button(
                            "Start Agent",
                            on_click=lambda j=job.job_id: self._start_agent(j),
                        ).props("flat color=primary size=sm")

    def _start_agent(self, job_id: str) -> None:
        """Start an agent for a job."""
        try:
            ui.notify(f"Starting agent for {job_id}...", type="info")
            port = self.manager.start_job_agent(job_id)
            ui.notify(f"Agent started on port {port}", type="positive")

            # Refresh jobs to show agent (schedule as async task)
            asyncio.create_task(self._refresh_after_start(job_id))

        except Exception as e:
            ui.notify(f"Failed to start agent: {e}", type="negative")

    async def _refresh_after_start(self, job_id: str) -> None:
        """Refresh UI after starting an agent."""
        await self.refresh_jobs()
        await self.refresh_stats()

    def _stop_agent(self, job_id: str) -> None:
        """Stop the agent for a job."""
        try:
            self.manager.stop_job_agent(job_id)
            ui.notify(f"Agent stopped for {job_id}", type="positive")

            # Remove from agent states
            if job_id in self.agent_states:
                del self.agent_states[job_id]

            # Refresh jobs (schedule as async task)
            asyncio.create_task(self._refresh_after_stop(job_id))

        except Exception as e:
            ui.notify(f"Failed to stop agent: {e}", type="negative")

    async def _refresh_after_stop(self, job_id: str) -> None:
        """Refresh UI after stopping an agent."""
        await self.refresh_jobs()
        await self.refresh_stats()

    def _send_initial_message(self, job_id: str) -> None:
        """Send initial instructions + progress report to agent."""
        try:
            ui.notify(f"▶ Sending instructions to {job_id}...", type="info")

            # Get initial instructions from plugin
            instructions = self.plugin.get_initial_instructions(job_id)

            # Generate progress report
            progress_report = self.manager._generate_progress_report(job_id)

            # Combine them
            full_message = f"{instructions}\n\n{progress_report}"

            # Send to agent
            self.manager.send_job_message(job_id, full_message)

            ui.notify(
                f"✓ Instructions sent to {job_id}. Agent should start working.", type="positive", timeout=5000
            )

        except Exception as e:
            ui.notify(f"Failed to send message: {e}", type="negative", timeout=5000)

    def _show_message_dialog(self, job_id: str) -> None:
        """Show dialog to send custom message to agent."""
        with ui.dialog() as dialog, ui.card().classes("w-96"):
            ui.label(f"Send message to {job_id}").classes("text-lg font-bold mb-2")

            message_input = ui.textarea(label="Message", placeholder="Enter your instructions...").classes(
                "w-full"
            )

            with ui.row().classes("w-full justify-end gap-2 mt-2"):
                ui.button("Cancel", on_click=dialog.close).props("flat")

                def send():
                    try:
                        self.manager.send_job_message(job_id, message_input.value)
                        ui.notify("Message sent", type="positive")
                        dialog.close()
                    except Exception as e:
                        ui.notify(f"Failed to send: {e}", type="negative")

                ui.button("Send", on_click=send).props("color=primary")

        dialog.open()

    def _show_details(self, job_id: str) -> None:
        """Show detailed view of a job (fetch from API)."""
        # Create dialog immediately (synchronous)
        with ui.dialog() as dialog, ui.card().classes("w-full max-w-4xl"):
            ui.label(f"Job Details: {job_id}").classes("text-xl font-bold mb-4")

            # Container for dynamic content
            content_container = ui.column().classes("w-full")

            # Loading indicator
            with content_container:
                ui.spinner(size="lg")
                ui.label("Loading job details...").classes("text-sm text-gray-500")

            # Close button
            with ui.row().classes("w-full justify-end mt-4"):
                ui.button("Close", on_click=dialog.close)

        # Open dialog immediately
        dialog.open()

        # Load data asynchronously
        async def load_details():
            """Load details from API."""
            try:
                async with httpx.AsyncClient() as client:
                    # Fetch detailed status from API
                    resp = await client.get(f"{self.api_base_url}/jobs/{job_id}", timeout=5.0)

                    if resp.status_code != 200:
                        content_container.clear()
                        with content_container:
                            ui.label(f"Failed to fetch job details: {resp.status_code}").classes("text-red-600")
                        return

                    job_data = resp.json()

                # Clear loading indicator and populate with data
                content_container.clear()
                with content_container:
                    # Progress criteria
                    ui.label("Progress Criteria:").classes("text-lg font-bold mt-4 mb-2")

                    for crit in job_data["criteria_results"]:
                        with ui.card().classes("w-full mb-2"):
                            with ui.row().classes("items-center gap-2"):
                                icon = "✓" if crit["met"] else "✗"
                                color = "green" if crit["met"] else "red"
                                ui.label(icon).classes(f"text-2xl text-{color}-600")

                                with ui.column().classes("flex-1"):
                                    ui.label(crit["name"]).classes("font-bold")
                                    ui.label(crit["message"]).classes("text-sm")

                                    if crit.get("hint") and not crit["met"]:
                                        ui.label(f"💡 {crit['hint']}").classes("text-sm text-blue-600 mt-1")

                    # Messages
                    if job_data["has_agent"]:
                        ui.label("Recent Messages (most recent first):").classes("text-lg font-bold mt-4 mb-2")

                        try:
                            messages = self.manager.get_job_messages(job_id, last=10)
                            # Reverse to show most recent first
                            for msg in reversed(messages):
                                role = msg.get("role", "unknown")
                                content = msg.get("content", "")
                                with ui.card().classes("w-full mb-2 p-2"):
                                    ui.label(f"[{role}]").classes("text-sm font-bold")
                                    ui.label(content[:200] + ("..." if len(content) > 200 else "")).classes(
                                        "text-sm"
                                    )
                        except Exception as e:
                            ui.label(f"Could not load messages: {e}").classes("text-red-600")

            except Exception as e:
                content_container.clear()
                with content_container:
                    ui.label(f"Error loading details: {e}").classes("text-red-600")

        # Schedule async load
        asyncio.create_task(load_details())


def launch_dashboard_v2(
    plugin: CurationPlugin,
    title: str = "AI Curation Dashboard",
    port: int = 5123,
    api_base_url: str = "http://localhost:5124",
) -> None:
    """Launch the V2 dashboard with FastAPI backend.

    Args:
        plugin: CurationPlugin implementation
        title: Dashboard title
        port: Port for NiceGUI dashboard
        api_base_url: URL for FastAPI backend
    """
    dashboard = CurationDashboardV2(plugin, title, api_base_url)
    dashboard.build()

    ui.run(
        title=title,
        port=port,
        reload=False,
        show=False,
    )
