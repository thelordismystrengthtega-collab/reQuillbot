import React, { useState } from 'react';
import './App.css';
import TextEditor from './components/TextEditor';
import Header from './components/Header';

function App() {
  const [content, setContent] = useState('');
  const [result, setResult] = useState('');

  return (
    <div className="App">
      <Header />
      <main className="app-container">
        <TextEditor 
          content={content} 
          setContent={setContent}
          onAnalyze={() => handleAnalyze(content)}
        />
        {result && <div className="result-panel">{result}</div>}
      </main>
    </div>
  );
}

const handleAnalyze = async (text) => {
  try {
    const response = await fetch('http://localhost:8000/api/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });
    const data = await response.json();
    console.log('Analysis result:', data);
  } catch (error) {
    console.error('Error:', error);
  }
};

export default App;
