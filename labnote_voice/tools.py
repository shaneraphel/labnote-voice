"""Instrument tools for a spoken lab notebook."""

from __future__ import annotations


class ToolHandle:
    def __init__(self, name: str, text: str) -> None:
        self.name = name
        self.text = text
        self.cancelled = False

    def cancel(self) -> None:
        self.cancelled = True


class LabTools:
    def __init__(self) -> None:
        self.log: list[str] = []

    def dispatch(self, text: str) -> ToolHandle:
        handle = ToolHandle("append_observation", text)
        self.log.append(text)
        return handle

    def cancel(self, handle: ToolHandle | None) -> None:
        if handle is None:
            return
        handle.cancel()
        if handle.text in self.log:
            self.log.remove(handle.text)
