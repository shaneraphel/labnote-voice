"""Bind AssemblyAI Voice Agent events to lab tools."""

from __future__ import annotations

from labnote_voice.tools import LabTools


def on_event(event: dict, tools: LabTools, inflight: dict) -> str:
    if event.get("type") == "session.ready":
        return "ready"
    if event.get("type") == "transcript.user":
        handle = tools.dispatch(event.get("text") or "")
        inflight["tool"] = handle
        return "dispatched"
    if event.get("type") == "reply.done" and event.get("status") == "interrupted":
        tools.cancel(inflight.pop("tool", None))
        return "cancelled"
    return "ignored"
