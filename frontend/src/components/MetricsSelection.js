import React, { useState } from 'react';
import './styles/MetricsSelection.css';

const metrics = [
  { id: 'bondPrice', label: 'Bond Price' },
  { id: 'yieldToMaturity', label: 'Yield to Maturity' },
  { id: 'yieldToCall', label: 'Yield to Call (YTC)' },
  { id: 'optionAdjustedSpread', label: 'Option-Adjusted Spread (OAS)' },
  { id: 'averageLife', label: 'Average Life' },
  { id: 'priceEarningsRatio', label: "Price/Earnings (P/E) Ratio" },
  { id: 'yieldCurve', label: 'Yield Curve' }
];

const MetricsSelection = ({ onChange }) => {
  const [selectedMetrics, setSelectedMetrics] = useState({});

  const handleCheckboxChange = (event) => {
    const { id, checked } = event.target;
    setSelectedMetrics({ ...selectedMetrics, [id]: checked });

    if (onChange) {
      onChange(id, checked);
    }
  };

  return (
    <div data-testid="metrics-selection">
      {metrics.map((metric) => (
        <div key={metric.id}>
          <input
            type="checkbox"
            id={metric.id}
            checked={selectedMetrics[metric.id] || false}
            onChange={handleCheckboxChange}
          />
          <label htmlFor={metric.id}>{metric.label}</label>
        </div>
      ))}
    </div>
  );
};

export default MetricsSelection;
