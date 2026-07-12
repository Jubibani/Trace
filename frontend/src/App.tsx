import { FormEvent, useState } from 'react';

type ChatResponse = {
  message: string;
  model: string;
  source: string;
};

const initialPrompt = 'Explain the execution path for a request in this codebase.';

export default function App() {
  const [prompt, setPrompt] = useState(initialPrompt);
  const [reply, setReply] = useState<ChatResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/v1/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: prompt }),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = (await response.json()) as ChatResponse;
      setReply(data);
    } catch (error_) {
      setError(error_ instanceof Error ? error_.message : 'Unknown request failure');
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="shell">
      <section className="hero">
        <div>
          <p className="eyebrow">Trace</p>
          <h1>Local AI for code understanding.</h1>
          <p className="lede">
            Ask a question, trace the execution path, and get a focused response from the backend AI
            service.
          </p>
        </div>

        <div className="status-card">
          <span className="status-dot" />
          <div>
            <strong>Connected</strong>
            <p>Frontend proxy is wired to the backend chat endpoint.</p>
          </div>
        </div>
      </section>

      <section className="workspace">
        <form className="composer" onSubmit={handleSubmit}>
          <label htmlFor="prompt">Prompt</label>
          <textarea
            id="prompt"
            value={prompt}
            onChange={(event) => setPrompt(event.target.value)}
            rows={6}
            placeholder="Ask Trace to explain a flow, dependency, or bug..."
          />
          <div className="actions">
            <button type="submit" disabled={loading}>
              {loading ? 'Tracing...' : 'Send to AI'}
            </button>
            <span>POST /api/v1/chat</span>
          </div>
        </form>

        <aside className="reply-panel">
          <h2>Assistant response</h2>
          {error ? <p className="error">{error}</p> : null}
          {reply ? (
            <article className="reply">
              <p>{reply.message}</p>
              <dl>
                <div>
                  <dt>Model</dt>
                  <dd>{reply.model}</dd>
                </div>
                <div>
                  <dt>Source</dt>
                  <dd>{reply.source}</dd>
                </div>
              </dl>
            </article>
          ) : (
            <p className="placeholder">Submit a prompt to see the backend response here.</p>
          )}
        </aside>
      </section>
    </main>
  );
}