import React, { useState } from 'react';
import axios from 'axios';
import InputForm from './components/InputForm';
import MetricsSelection from './components/MetricsSelection';
import DataDisplay from './components/DataDisplay';
import ErrorHandling from './components/ErrorHandling';
import './App.css';

const App = () => {
  const [bondData, setBondData] = useState({});
  const [selectedMetrics, setSelectedMetrics] = useState({});
  const [calculatedData, setCalculatedData] = useState({});
  const [error, setError] = useState(null);

  const handleFormSubmit = (data) => {
    setBondData(data);
    // setCalculatedData({}); 
  };

  const handleMetricsChange = (metricId, isSelected) => {
    setSelectedMetrics({ ...selectedMetrics, [metricId]: isSelected });
  };

  const fetchDataAndCalculateMetrics = async () => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/api/process_bond_data/`, {
        bondData: bondData,
        selectedMetrics: selectedMetrics,
        useApiData: bondData.useApiData,
        isCallOptionSelected: bondData.isCallOptionSelected,
        optionalData: {
          issuer: bondData.issuer,
          currency: bondData.currency,
          bondPrice: bondData.optionalBondPrice,
          yieldToMaturity: bondData.optionalYtm,
          riskFreeYield: bondData.optionalRiskFreeYield,
          benchmarkYield: bondData.optionalBenchmarkYield,
          optionValue: bondData.optionalOptionValue,
          optionValueCalculation: bondData.optionalData.optionValueCalculation,
        },
      });
      setCalculatedData(response.data);
      setError(null);
    } catch (err) {
      setError(err.message || 'An error occurred while fetching data.');
    }
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
