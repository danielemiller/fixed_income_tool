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
  const [optionType, setOptionType] = useState('');
  const [strikePrice, setStrikePrice] = useState('');
  const [underlyingPrice, setUnderlyingPrice] = useState('');
  const [riskFreeRate, setRiskFreeRate] = useState('');
  const [volatility, setVolatility] = useState('');
  const [expirationDate, setExpirationDate] = useState('');
  const [faceValue, setFaceValue] = useState('');
  const [dateFirstParCall, setDateFirstParCall] = useState('');
  const [errorMessages, setErrorMessages] = useState({});


  const validateOptionalInputs = () => {
    const errors = {};
  
    const allOptionalInputs = [
      optionalBondPrice,
      optionalYtm,
      optionalRiskFreeYield,
      optionalBenchmarkYield,
      optionalOptionValue,
    ];
  
    const hasEmptyOptionalInputs = allOptionalInputs.some((input) => input === '');
    if (!useApiData && hasEmptyOptionalInputs) {
      errors.missingOptionalInputs = 'You must provide all optional inputs or select "Use API Data".';
    }
  
    return errors;
  };

  const validateInputs = () => {
    const errors = {};
  
    if (!issueDate) {
      errors.issueDate = 'Issue Date is required.';
    }
    if (!maturityDate) {
      errors.maturityDate = 'Maturity Date is required.';
    }
    if (!couponRate) {
      errors.couponRate = 'Coupon Rate is required.';
    }
    if (!yearsToMaturity) {
      errors.yearsToMaturity = 'Years to Maturity is required.';
    }
    if (!faceValue) {
      errors.faceValue = 'Face Value is required.';
    }
    if (!creditRating) {
      errors.creditRating = 'Credit Rating is required.';
    }
    if (!dateFirstParCall) {
      errors.dateFirstParCall = 'Date of First Par Call is required.';
    }
    if (!bondCusip) {
      errors.bondCusip = 'Bond Cusip is required.';
    }
  
    if (optionType) {
      if (!strikePrice) {
        errors.strikePrice = 'Strike Price is required when Call Option is selected.';
      }
      if (!underlyingPrice) {
        errors.underlyingPrice = 'Underlying Price is required when Call Option is selected.';
      }
      if (!riskFreeRate) {
        errors.riskFreeRate = 'Risk-Free Rate is required when Call Option is selected.';
      }
      if (!volatility) {
        errors.volatility = 'Volatility is required when Call Option is selected.';
      }
      if (!expirationDate) {
        errors.expirationDate = 'Expiration Date is required when Call Option is selected.';
      }
    }
  
    if (optionalOptionValue && optionType) {
      errors.optionValueConflict = 'You cannot submit both an optional value and select the Call Option. Please choose one method.';
    }
    
    const optionalErrors = validateOptionalInputs();
    Object.assign(errors, optionalErrors);

    if(errors){
      errors.mainSubmitError = 'There seems to be a problem with some of your inputs'
    }

    return errors;
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const errors = validateInputs();

    if (Object.keys(errors).length === 0) {
      // No errors, proceed with submission
      onSubmit({
        issue_date: issueDate,
        maturity_date: maturityDate,
        coupon_rate: couponRate,
        years_to_maturity: yearsToMaturity,
        credit_rating: creditRating,
        bond_cusip: bondCusip,
        face_value: faceValue,
        date_first_par_call: dateFirstParCall,
        useApiData: useApiData, // Changed from use_api_data
        isCallOptionSelected: optionType,
        optionalData: { // Changed from optional_data
          issuer: issuer,
          currency: currency,
          bond_price: optionalBondPrice,
          ytm: optionalYtm,
          risk_free_yield: optionalRiskFreeYield,
          benchmark_yield: optionalBenchmarkYield,
          option_value: optionalOptionValue,
          optionValueCalculation: { // Changed from option_value_calculation
            strike_price: strikePrice,
            underlying_price: underlyingPrice,
            risk_free_rate: riskFreeRate,
            volatility: volatility,
            expiration_date: expirationDate,
          },
        },
      });

      
    } else {
      setErrorMessages(errors);
    }
  };

  return (
    <form data-testid="input-form" onSubmit={handleSubmit}>
      <h3>Required Inputs</h3>

      {/* ... */}
      <div className="form-field">
        <label htmlFor="issue-date">Issue Date</label>
        <input
          id="issue-date"
          type="date"
          value={issueDate}
          onChange={(e) => setIssueDate(e.target.value)}
        />
        {errorMessages.issueDate && <p className="error">{errorMessages.issueDate}</p>}
      </div>
      {/* ... */}

      <div className="form-field">
        <label htmlFor="maturity-date">Maturity Date</label>
        <input
          id="maturity-date"
          type="date"
          value={maturityDate}
          onChange={(e) => setMaturityDate(e.target.value)}
        />
        {errorMessages.maturityDate && <p className="error">{errorMessages.maturityDate}</p>}
      </div>

      <div className="form-field">
        <label htmlFor="coupon-rate">Coupon Rate</label>
        <input
          id="coupon-rate"
          type="number"
          value={couponRate}
          onChange={(e) => setCouponRate(e.target.value)}
        />
        {errorMessages.couponRate && <p className="error">{errorMessages.couponRate}</p>}
      </div>

      <div className="form-field">
        <label htmlFor="years-to-maturity">Years to Maturity</label>
        <input
          id="years-to-maturity"
          type="number"
          value={yearsToMaturity}
          onChange={(e) => setYearsToMaturity(e.target.value)}
        />
        {errorMessages.yearsToMaturity && <p className="error">{errorMessages.yearsToMaturity}</p>}
      </div>
      
      <div className="form-field">
        <label htmlFor="face-value">Face Value</label>
        <input
          id="face-value"
          type="number"
          value={faceValue}
          onChange={(e) => setFaceValue(e.target.value)}
        />
        {errorMessages.faceValue && <p className="error">{errorMessages.faceValue}</p>}
      </div>

      <div className="form-field">
        <label htmlFor="credit-rating">Credit Rating</label>
        <select
          id="credit-rating"
          value={creditRating}
          onChange={(e) => setCreditRating(e.target.value)}
        >
          <option value="AAA">AAA</option>
          <option value="AA+">AA+</option>
          <option value="AA">AA</option>
          <option value="AA-">AA-</option>
          <option value="A+">A+</option>
          <option value="A">A</option>
          <option value="A-">A-</option>
          <option value="BBB+">BBB+</option>
          <option value="BBB">BBB</option>
          <option value="BBB-">BBB-</option>
          <option value="BB+">BB+</option>
          <option value="BB">BB</option>
          <option value="BB-">BB-</option>
          <option value="B+">B+</option>
          <option value="B">B</option>
          <option value="B-">B-</option>
          <option value="CCC+">CCC+</option>
          <option value="CCC">CCC</option>
          <option value="CCC-">CCC-</option>
          <option value="CC">CC</option>
          <option value="C">C</option>
          <option value="D">D</option>
        </select>
        {errorMessages.creditRating && <p className="error">{errorMessages.creditRating}</p>}
      </div>
      
      <div className="form-field">
        <label htmlFor="dateFirstParCall">Date of First Par Call:</label>
          <input
            type="date"
            id="dateFirstParCall"
            name="dateFirstParCall"
            value={dateFirstParCall}
            onChange={(e) => setDateFirstParCall(e.target.value)}
          />
          {errorMessages.dateFirstParCall && <p className="error">{errorMessages.dateFirstParCall}</p>} 
        </div>

      <div className="form-field">
        <label htmlFor="bond-cusip">Bond Cusip</label>
        <input
          id="bond-cusip"
          type="text"
          value={bondCusip}
          onChange={(e) => setBondCusip(e.target.value)}
        />
        {errorMessages.bondCusip && <p className="error">{errorMessages.bondCusip}</p>}
      </div>

      <h3>Optional Inputs</h3>

      <div className="form-field">
        <label htmlFor="use-api-data">Use API Data</label>
        <input
          id="use-api-data"
          type="checkbox"
          checked={useApiData}
          onChange={(e) => setUseApiData(e.target.checked)}
        />
        {errorMessages.missingOptionalInputs && <p className="error">{errorMessages.missingOptionalInputs}</p>}
      </div>

      <div className="form-field">
        <label htmlFor="optional-bond-price">Bond Price (optional)</label>
        <input
          id="optional-bond-price"
          type="number"
          value={optionalBondPrice}
          onChange={(e) => setOptionalBondPrice(e.target.value)}
        />
      </div>

      <div className="form-field">
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
      </div>

      <div className="form-field">
        <label htmlFor="issuer">Issuer</label>
        <input
          id="issuer"
          type="text"
          value={issuer}
          onChange={(e) => setIssuer(e.target.value)}
        />
      </div>

      <div className="form-field">
        <label htmlFor="optional-ytm">Yield to Maturity (optional)</label>
        <input
          id="optional-ytm"
          type="number"
          value={optionalYtm}
          onChange={(e) => setOptionalYtm(e.target.value)}
        />
      </div>

      <div className="form-field">
        <label htmlFor="optional-risk-free-yield">Risk-Free Yield (optional)</label>
        <input
          id="optional-risk-free-yield"
          type="number"
          value={optionalRiskFreeYield}
          onChange={(e) => setOptionalRiskFreeYield(e.target.value)}
        />
      </div>

      <div className="form-field">
        <label htmlFor="optional-benchmark-yield">Benchmark Yield (optional)</label>
        <input
          id="optional-benchmark-yield"
          type="number"
          value={optionalBenchmarkYield}
          onChange={(e) => setOptionalBenchmarkYield(e.target.value)}
        />
      </div>

      <div className="form-field">
        <label htmlFor="optional-option-value">Option Value (optional)</label>
        <input
          id="optional-option-value"
          type="number"
          value={optionalOptionValue}
          onChange={(e) => setOptionalOptionValue(e.target.value)}
        />
      </div>

      <h3>Option Value Calculation (optional)</h3>

      <div className="form-field">
        <label htmlFor="option-type">Call Option:</label>
        <input
          type="checkbox"
          id="option-type"
          checked={optionType}
          onChange={(e) => setOptionType(e.target.checked)}
        />
      </div>

      {/* ... */}
      <div className="form-field">
        <label htmlFor="strike-price">Strike Price</label>
        <input
          id="strike-price"
          type="number"
          value={strikePrice}
          onChange={(e) => setStrikePrice(e.target.value)}
        />
        {errorMessages.strikePrice && <p className="error">{errorMessages.strikePrice}</p>}
      </div>
      {/* ... */}

      <div className="form-field">
        <label htmlFor="risk-free-rate">Risk-Free Rate</label>
        <input
          id="risk-free-rate"
          type="number"
          value={riskFreeRate}
          onChange={(e) => setRiskFreeRate(e.target.value)}
        />
        {errorMessages.riskFreeRate && <p className="error">{errorMessages.riskFreeRate}</p>}
      </div>
      <div className="form-field">
        <label htmlFor="volatility">Volatility</label>
        <input
          id="volatility"
          type="number"
          value={volatility}
          onChange={(e) => setVolatility(e.target.value)}
        />
        {errorMessages.volatility && <p className="error">{errorMessages.volatility}</p>}
      </div>
      <div className="form-field">
        <label htmlFor="expiration-date">Expiration Date</label>
        <input
          id="expiration-date"
          type="date"
          value={expirationDate}
          onChange={(e) => setExpirationDate(e.target.value)}
        />
        {errorMessages.expirationDate && <p className="error">{errorMessages.expirationDate}</p>}
      </div>

      <button type="submit">Submit</button>
      {errorMessages.mainSubmitError && <p className="error">{errorMessages.mainSubmitError}</p>}
    </form>
  );
};

export default InputForm;
        
