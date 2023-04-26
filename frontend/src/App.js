import React, { useState } from 'react';
import axios from 'axios';
import InputForm from './components/InputForm';
import MetricsSelection from './components/MetricsSelection';
import DataDisplay from './components/DataDisplay';
import ErrorHandling from './components/ErrorHandling';
import Header from './components/Header';
import BondDataSelection from './components/BondDataSelection';
import './App.css';

const App = () => {
  const [bondData, setBondData] = useState({});
  const [selectedMetrics, setSelectedMetrics] = useState({});
  const [calculatedData, setCalculatedData] = useState({});
  const [error, setError] = useState(null);
  const [formError, setFormError] = useState(null);
  const [success, setSuccess] = useState(null);



  const validateInputData = (data) => {
    // Implement your validation logic here, return true if the data is valid, false otherwise
    let errors = {};
  
    // Bond Price validation
    if (data.selectedMetrics.includes('Bond Price') && !data.optionalData.bond_price) {
      errors.bondPrice = 'Bond price is required.';
    }
  
    // Yield to Maturity validation
    if (data.selectedMetrics.includes('Yield to Maturity') && !data.optionalData.ytm) {
      errors.yieldToMaturity = 'Yield to maturity is required.';
    }
  
    // Add validation for the other metrics here...
  
    const isValid = Object.keys(errors).length === 0;
    return { isValid, errors };
  };

  const handleFormSubmit = (data) => {
    const { isValid, errors } = validateInputData(data);
    if (isValid) {
      setBondData(data);
      setSuccess('Inputs submitted successfully.');
      setFormError(null);
    } else {
      setFormError('There was an error processing your input.');
    }
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
      <Header />
      <h2>
        Bond Analysis Tool: Calculate and analyze key bond metrics to make informed investment decisions
      </h2>
      <BondDataSelection onBondDataSelect={setBondData} />
      <MetricsSelection onChange={handleMetricsChange} />
      <InputForm onSubmit={handleFormSubmit} success={success} formError={formError} bondData={bondData} />
      <button onClick={fetchDataAndCalculateMetrics}>Calculate Metrics</button>
      <DataDisplay data={calculatedData} />
      <ErrorHandling error={error} />
    </div>
  );
};

export default App;
