// DataDisplay.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import DataDisplay from '../DataDisplay';

describe('DataDisplay', () => {
  it('renders the chart with provided data', () => {
    const data = {
      BondPrice: 100,
      YieldToMaturity: 5,
      YieldToCall: 4.5,
      OAS: 50,
    };

    render(<DataDisplay data={data} />);

    const chart = screen.getByTestId('data-display');
    expect(chart).toBeInTheDocument();
  });
});
