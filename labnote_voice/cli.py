"""Open an AssemblyAI Voice Agent websocket."""

from __future__ import annotations

import asyncio
import json
import os

from labnote_voice.session import on_event
from labnote_voice.tools import LabTools


async def run(url: str) -> None:
    import websockets

    tools = LabTools()
    inflight: dict = {}
    async with websockets.connect(url, additional_headers={"Authorization": os.environ["ASSEMBLYAI_API_KEY"]}) as ws:
        await ws.send(json.dumps({"type": "session.update", "session": {"input": {"turn_detection": {}}}}))
        async for raw in ws:
            event = json.loads(raw)
            on_event(event, tools, inflight)


def main() -> None:
    url = os.environ.get("ASSEMBLYAI_VOICE_URL", "wss://api.assemblyai.com/v2/voice-agent")
    asyncio.run(run(url))


if __name__ == "__main__":
    main()
