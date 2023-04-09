import React from 'react';
import { render, screen } from '@testing-library/react';
import DataDisplay from '../DataDisplay';

const mockData = {
  bondPrice: 1000,
  yieldToMaturity: 0.05,
  // ...add other metric values
};

test('renders DataDisplay', () => {
  render(<DataDisplay data={mockData} />);
  expect(screen.getByTestId('data-display')).toBeInTheDocument();
});

test('displays data in the correct format', () => {
  render(<DataDisplay data={mockData} />);
  expect(screen.getByText('Bond Price: 1000')).toBeInTheDocument();
  expect(screen.getByText('Yield to Maturity: 5.00%')).toBeInTheDocument();
  // ...add other metric display assertions
});
