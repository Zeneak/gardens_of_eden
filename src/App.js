import logo from './logo.svg';
import './App.css';
import DiceButton from './components/dice-button';
import { useState } from 'react';

function App() {
  const [roll, setRoll] = useState()

  return (
    <div >
      <div >
        <DiceButton die={20} onRoll={(num) => setRoll(num)}/>
        <DiceButton die={10} onRoll={(num) => setRoll(num)}/>
        <DiceButton die={6} onRoll={(num) => setRoll(num)}/>
      </div>
      <div>
      {roll && <p>
        You rolled a {roll}!
      </p>}
    </div>
    </div>

  );
}

export default App;


