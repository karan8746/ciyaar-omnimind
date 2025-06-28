import React, { useState } from 'react';

function App() {
  const [greet, setGreet] = useState('');
  const [name, setName] = useState('');

  const handleGreet = async () => {
    const response = await fetch(
      'https://YOUR-BACKEND-URL/api/greet/' + name
    );
    const data = await response.json();
    setGreet(data.greeting);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>Ciyaar OmniMind Frontend</h1>
      <input
        value={name}
        placeholder="Enter your name"
        onChange={e => setName(e.target.value)}
      />
      <button onClick={handleGreet}>Greet</button>
      <div style={{ marginTop: 20 }}>{greet}</div>
    </div>
  );
}

export default App;
