// DataDisplay.js
import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import './styles/DataDisplay.css';

const DataDisplay = ({ data }) => {
  if (!data || !data.yield_curve) {
    return <div>Loading...</div>;
  }

  const yieldCurveData = data.yield_curve.map(([x, y]) => ({ x, y }));

  return (
    <div data-testid="data-display">
      <h3>Bond Metrics</h3>
      <ul>
        <li>Bond Price: {data.bond_price}</li>
        <li>Yield to Maturity: {data.yield_to_maturity}</li>
        <li>Yield to Call: {data.yield_to_call}</li>
        <li>Option Adjusted Spread: {data.option_adjusted_spread}</li>
        <li>Average Life: {data.average_life}</li>
      </ul>

      <h3>Yield Curve</h3>
      <LineChart
        width={600}
        height={300}
        data={yieldCurveData}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="x" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="y" stroke="#8884d8" />
      </LineChart>
    </div>
  );
};

export default DataDisplay;
