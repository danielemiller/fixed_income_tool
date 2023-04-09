import React from 'react';
import InputForm from './components/InputForm';
import MetricsSelection from './components/MetricsSelection';
import DataDisplay from './components/DataDisplay';
import ErrorHandling from './components/ErrorHandling';

function App() {
  return (
    <div>
      <InputForm />
      <MetricsSelection />
      <DataDisplay />
      <ErrorHandling />
    </div>
  );
}

export default App;