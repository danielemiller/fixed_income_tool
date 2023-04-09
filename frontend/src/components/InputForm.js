import React, { useState } from 'react';

const InputForm = ({ onSubmit }) => {
  const [issueDate, setIssueDate] = useState('');
  const [maturityDate, setMaturityDate] = useState('');
  const [couponRate, setCouponRate] = useState('');
  const [yieldToMaturity, setYieldToMaturity] = useState('');
  const [creditRating, setCreditRating] = useState('');
  const [currency, setCurrency] = useState('');
  const [issuer, setIssuer] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ issueDate, maturityDate, couponRate, yieldToMaturity, creditRating, currency, issuer });
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

      <label htmlFor="yield-to-maturity">Yield to Maturity</label>
      <input
        id="yield-to-maturity"
        type="number"
        value={yieldToMaturity}
        onChange={(e) => setYieldToMaturity(e.target.value)}
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

      <button type="submit">Submit</button>
    </form>
  );
};

export default InputForm;
