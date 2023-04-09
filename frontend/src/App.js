import React, { useState } from 'react';
import InputForm from './components/InputForm';
import MetricsSelection from './components/MetricsSelection';
import DataDisplay from './components/DataDisplay';
import ErrorHandling from './components/ErrorHandling';

const App = () => {
  const [bondData, setBondData] = useState({});
  const [selectedMetrics, setSelectedMetrics] = useState({});
  const [calculatedData, setCalculatedData] = useState({});
  const [error, setError] = useState(null);

  const handleFormSubmit = (data) => {
    setBondData(data);
    // Here you can call your API to process the bond data and calculate the metrics
    // Update the calculatedData state with the response from the API
  };

  const handleMetricsChange = (metricId, isSelected) => {
    setSelectedMetrics({ ...selectedMetrics, [metricId]: isSelected });
  };

  const fetchDataAndCalculateMetrics = () => {
    // Fetch data from the API and calculate the metrics based on bondData and selectedMetrics
    // Update the calculatedData state with the calculated metrics
    // If an error occurs, update the error state
  };

  return (
    <div className="App">
      <h1>Fixed Income Tool</h1>
      <InputForm onSubmit={handleFormSubmit} />
      <MetricsSelection onChange={handleMetricsChange} />
      <button onClick={fetchDataAndCalculateMetrics}>Calculate Metrics</button>
      <DataDisplay data={calculatedData} />
      <ErrorHandling error={error} />
    </div>
  );
};

export default App;
