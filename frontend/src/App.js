import React, { useState } from "react";
import CommitInput from "./components/CommitInput";
import Timeline from "./components/Timeline";
import "./App.css";

function App() {
  const [phases, setPhases] = useState([]);

  return (
    <div className="App">
      <h1>Git Commit → Project Story Generator</h1>
      <CommitInput onResult={setPhases} />
      {phases.length > 0 && <Timeline phases={phases} />}
    </div>
  );
}

export default App;
