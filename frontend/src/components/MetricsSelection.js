import React, { useState } from 'react';
import './styles/MetricsSelection.css';

const metrics = [
  { id: 'bondPrice', label: 'Bond Price', gridArea: 'a' },
  { id: 'yieldToMaturity', label: 'Yield to Maturity', gridArea: 'b' },
  { id: 'yieldToCall', label: 'Yield to Call (YTC)', gridArea: 'c' },
  { id: 'optionAdjustedSpread', label: 'Option-Adjusted Spread (OAS)', gridArea: 'd' },
  { id: 'averageLife', label: 'Average Life', gridArea: 'e' },
  { id: 'yieldCurve', label: 'Yield Curve', gridArea: 'f' }
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
    <div className="container">
      <h3 className='metrics-head'>Select the metrics you would like to analyze below:</h3>
      <div className="metrics-selection" data-testid="metrics-selection">
        {metrics.map((metric) => (
          <div key={metric.id} className="metrics-item" style={{ gridArea: metric.gridArea }}>
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
    </div>
  );
} 

export default MetricsSelection;
