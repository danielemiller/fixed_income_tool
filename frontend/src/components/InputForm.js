import React, { useState } from 'react';
import './styles/InputForm.css';

const InputForm = ({ onSubmit }) => {
  const [issueDate, setIssueDate] = useState('');
  const [maturityDate, setMaturityDate] = useState('');
  const [couponRate, setCouponRate] = useState('');
  const [yearsToMaturity, setYearsToMaturity] = useState('');
  const [creditRating, setCreditRating] = useState('');
  const [currency, setCurrency] = useState('');
  const [issuer, setIssuer] = useState('');
  const [bondCusip, setBondCusip] = useState('');
  const [useApiData, setUseApiData] = useState(false);
  const [optionalBondPrice, setOptionalBondPrice] = useState('');
  const [optionalYtm, setOptionalYtm] = useState('');
  const [optionalRiskFreeYield, setOptionalRiskFreeYield] = useState('');
  const [optionalBenchmarkYield, setOptionalBenchmarkYield] = useState('');
  const [optionalOptionValue, setOptionalOptionValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      issue_date: issueDate,
      maturity_date: maturityDate,
      coupon_rate: couponRate,
      years_to_maturity: yearsToMaturity,
      credit_rating: creditRating,
      currency: currency,
      issuer: issuer,
      bond_cusip: bondCusip,
      use_api_data: useApiData,
      optional_data: {
        bond_price: optionalBondPrice,
        ytm: optionalYtm,
        risk_free_yield: optionalRiskFreeYield,
        benchmark_yield: optionalBenchmarkYield,
        option_value: optionalOptionValue,
      },
    });
  };
  

  return (
    <form data-testid="input-form" onSubmit={handleSubmit}>
      <label htmlFor="issue-date">Issue Date</label>
      <input
        id="issue-date"
        type="date"
        value={issueDate}
        onChange={(e) => setIssueDate(e.target.value)}
      />

      <label htmlFor="maturity-date">Maturity Date</label>
      <input
        id="maturity-date"
        type="date"
        value={maturityDate}
        onChange={(e) => setMaturityDate(e.target.value)}
      />

      <label htmlFor="coupon-rate">Coupon Rate</label>
      <input
        id="coupon-rate"
        type="number"
        value={couponRate}
        onChange={(e) => setCouponRate(e.target.value)}
      />

      <label htmlFor="years-to-maturity">Years to Maturity</label>
      <input
        id="years-to-maturity"
        type="number"
        value={yearsToMaturity}
        onChange={(e) => setYearsToMaturity(e.target.value)}
      />

      <label htmlFor="credit-rating">Credit Rating</label>
      <select
        id="credit-rating"
        value={creditRating}
        onChange={(e) => setCreditRating(e.target.value)}
      >
        {/* Add available credit ratings */}
        <option value="AAA">AAA</option>
        <option value="AA+">AA+</option>
        {/* ... */}
      </select>

      <label htmlFor="currency">Currency</label>
      <select
        id="currency"
        value={currency}
        onChange={(e) => setCurrency(e.target.value)}
      >
        {/* Add available currencies */}
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        {/* ... */}
      </select>

      <label htmlFor="issuer">Issuer</label>
      <input
        id="issuer"
        type="text"
        value={issuer}
        onChange={(e) => setIssuer(e.target.value)}
      />
      
      <label htmlFor="bond-cusip">Bond Cusip</label>
      <input
        id="bond-cusip"
        type="text"
        value={bondCusip}
        onChange={(e) => setBondCusip(e.target.value)}
      />

      <label htmlFor="use-api-data">Use API Data</label>
      <input
              id="use-api-data"
              type="checkbox"
              checked={useApiData}
              onChange={(e) => setUseApiData(e.target.checked)}
            />
        
            {/* Add optional inputs for bond price, yield to maturity, risk-free yield, benchmark yield, and option value */}
            <label htmlFor="optional-bond-price">Bond Price (optional)</label>
            <input
              id="optional-bond-price"
              type="number"
              value={optionalBondPrice}
              onChange={(e) => setOptionalBondPrice(e.target.value)}
            />
        
            <label htmlFor="optional-ytm">Yield to Maturity (optional)</label>
            <input
              id="optional-ytm"
              type="number"
              value={optionalYtm}
              onChange={(e) => setOptionalYtm(e.target.value)}
            />
        
            <label htmlFor="optional-risk-free-yield">Risk-Free Yield (optional)</label>
            <input
              id="optional-risk-free-yield"
              type="number"
              value={optionalRiskFreeYield}
              onChange={(e) => setOptionalRiskFreeYield(e.target.value)}
            />
        
            <label htmlFor="optional-benchmark-yield">Benchmark Yield (optional)</label>
            <input
              id="optional-benchmark-yield"
              type="number"
              value={optionalBenchmarkYield}
              onChange={(e) => setOptionalBenchmarkYield(e.target.value)}
            />
        
            <label htmlFor="optional-option-value">Option Value (optional)</label>
            <input
              id="optional-option-value"
              type="number"
              value={optionalOptionValue}
              onChange={(e) => setOptionalOptionValue(e.target.value)}
            />
        
            <button type="submit">Submit</button>
          </form>
        );
        };
        
        export default InputForm;
        
