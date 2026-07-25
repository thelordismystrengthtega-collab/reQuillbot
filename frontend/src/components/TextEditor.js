import React from 'react';
import './TextEditor.css';

const TextEditor = ({ content, setContent, onAnalyze }) => {
  return (
    <div className="text-editor">
      <div className="editor-header">
        <h2>Enter Your Text</h2>
      </div>
      <textarea
        className="editor-textarea"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Paste or type your content here..."
      />
      <div className="editor-actions">
        <button className="btn btn-primary" onClick={onAnalyze}>
          Analyze
        </button>
        <button className="btn btn-secondary" onClick={() => setContent('')}>
          Clear
        </button>
      </div>
    </div>
  );
};

export default TextEditor;
