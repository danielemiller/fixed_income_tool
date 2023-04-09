import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import MetricsSelection from '../MetricsSelection';

test('renders MetricsSelection', () => {
  render(<MetricsSelection />);
  expect(screen.getByTestId('metrics-selection')).toBeInTheDocument();
});

test('contains all checkboxes', () => {
  render(<MetricsSelection />);
  expect(screen.getByLabelText('Bond Price')).toBeInTheDocument();
  expect(screen.getByLabelText('Yield to Maturity')).toBeInTheDocument();
  expect(screen.getByLabelText('Yield to Call (YTC)')).toBeInTheDocument();
  expect(screen.getByLabelText('Option-Adjusted Spread (OAS)')).toBeInTheDocument();
  expect(screen.getByLabelText('Average Life')).toBeInTheDocument();
  expect(screen.getByLabelText('Price/Earnings (P/E) Ratio')).toBeInTheDocument();
  expect(screen.getByLabelText('Yield Curve')).toBeInTheDocument();
  // ...add other metric checkboxes
});

test('selecting a metric updates the state', () => {
  const handleSelectionChange = jest.fn();
  render(<MetricsSelection onChange={handleSelectionChange} />);

  fireEvent.click(screen.getByLabelText('Bond Price'));
  expect(handleSelectionChange).toHaveBeenCalledTimes(1);
  expect(handleSelectionChange).toHaveBeenCalledWith('bondPrice', true);
});
