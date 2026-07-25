import React, { useState } from "react";

type Mode = "fluency" | "formal" | "concise" | "creative";

const backendBase = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

export default function App() {
  const [text, setText] = useState("");
  const [mode, setMode] = useState<Mode>("fluency");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function submit() {
    setError(null);
    setResult(null);

    if (!text.trim()) {
      setError("Enter text to paraphrase.");
      return;
    }

    setLoading(true);
    try {
      const resp = await fetch(`${backendBase}/api/paraphrase`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, mode })
      });

      if (!resp.ok) {
        const body = await resp.json().catch(() => ({}));
        throw new Error(body.detail || resp.statusText || "Request failed");
      }

      const data = await resp.json();
      setResult(data.paraphrase);
    } catch (err: any) {
      setError(err.message || "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <h1>Paraphrase MVP</h1>

      <label>Text</label>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste text to paraphrase..."
      />

      <div className="controls">
        <label>Mode</label>
        <select value={mode} onChange={(e) => setMode(e.target.value as Mode)}>
          <option value="fluency">Fluency</option>
          <option value="formal">Formal</option>
          <option value="concise">Concise</option>
          <option value="creative">Creative</option>
        </select>
        <button onClick={submit} disabled={loading}>
          {loading ? "Working..." : "Paraphrase"}
        </button>
      </div>

      {error && <div className="error">{error}</div>}

      {result && (
        <div className="result">
          <h3>Paraphrase</h3>
          <div className="box">{result}</div>

          <h3>Original</h3>
          <div className="box">{text}</div>
        </div>
      )}
    </div>
  );
}
