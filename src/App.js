import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({ members: [] });

  useEffect(() => {
    fetch('/members')
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      })
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      {data.members.length === 0 ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  );
}

export default App;
