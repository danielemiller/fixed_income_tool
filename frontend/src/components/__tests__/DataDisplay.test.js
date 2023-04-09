import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import DataDisplay from '../DataDisplay';

// create a dummy component that mocks the Bar component from react-chartjs-2
jest.mock('react-chartjs-2', () => ({
  Bar: () => <div data-testid="chart"></div>,
}));

const mockData = {
  bondPrice: 1000,
  yieldToMaturity: 0.05,
  yieldToCall: 0.045,
  optionAdjustedSpread: 0.02,
  averageLife: 5,
  priceEarningsRatio: 20,
  yieldCurve: 0.03,
};

test('renders DataDisplay', () => {
  render(<DataDisplay data={mockData} />);
  expect(screen.getByTestId('data-display')).toBeInTheDocument();
});

test('displays data in the correct format', () => {
  const { container } = render(<DataDisplay data={mockData} />);
  const chartCanvas = container.querySelector('[data-testid="chart"]');
  expect(chartCanvas).toBeInTheDocument();
});
