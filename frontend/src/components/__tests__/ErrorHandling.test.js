import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import ErrorHandling from '../ErrorHandling';

test('renders ErrorHandling', () => {
  render(<ErrorHandling error="must pass something"/>);
  expect(screen.getByTestId('error-handling')).toBeInTheDocument();
});

test('does not render ErrorHandling if no error is passed', () => {
  render(<ErrorHandling />);
  expect(screen.queryByTestId('error-handling')).not.toBeInTheDocument();
});

test('displays error message when there is an error', () => {
  const errorMessage = 'An error has occurred';
  render(<ErrorHandling error={errorMessage} />);

  expect(screen.getByText(errorMessage)).toBeInTheDocument();
});
