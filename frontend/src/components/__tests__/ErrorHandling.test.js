import React from 'react';
import { render, screen } from '@testing-library/react';
import ErrorHandling from '../ErrorHandling';

test('renders ErrorHandling', () => {
  render(<ErrorHandling />);
  expect(screen.getByTestId('error-handling')).toBeInTheDocument();
});

test('displays error message when there is an error', () => {
  const errorMessage = 'An error has occurred';
  render(<ErrorHandling error={errorMessage} />);

  expect(screen.getByText(errorMessage)).toBeInTheDocument();
});
