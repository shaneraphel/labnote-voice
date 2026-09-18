from labnote_voice.session import on_event
from labnote_voice.tools import LabTools


def test_partial_does_not_commit():
    tools = LabTools()
    inflight = {}
    assert on_event({"type": "transcript.user.delta", "text": "set oven"}, tools, inflight) == "ignored"
    assert tools.log == []


def test_final_turn_commits():
    tools = LabTools()
    inflight = {}
    assert on_event({"type": "transcript.user", "text": "set oven 180"}, tools, inflight) == "dispatched"
    assert tools.log == ["set oven 180"]
    assert on_event({"type": "reply.done", "status": "interrupted"}, tools, inflight) == "cancelled"
    assert tools.log == []
