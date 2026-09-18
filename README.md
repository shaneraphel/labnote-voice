# Lab notebook voice agent

A laboratory notebook that listens on an AssemblyAI Voice Agent session and writes instrument commands only after a user turn is finished.

Partial transcripts (`transcript.user.delta`) are shown in the live buffer. A tool runs only on `transcript.user`. If the speaker barges in, `reply.done` with `status=interrupted` cancels the in-flight tool.

## Setup

```bash
export ASSEMBLYAI_API_KEY=...
python -m labnote_voice.cli
```

The session uses AssemblyAI Voice Agent events: `session.ready`, `transcript.user.delta`, `transcript.user`, `tool.call`, `reply.done`.
