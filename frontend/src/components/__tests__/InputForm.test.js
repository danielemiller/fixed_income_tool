import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import InputForm from '../InputForm';

test('renders InputForm', () => {
  render(<InputForm />);
  expect(screen.getByTestId('input-form')).toBeInTheDocument();
});

test('contains all input fields', () => {
  render(<InputForm />);
  expect(screen.getByLabelText('Type')).toBeInTheDocument();
  expect(screen.getByLabelText('Face Value')).toBeInTheDocument();
  // ...add other input fields
});

test('submits the form', () => {
  const handleSubmit = jest.fn();
  render(<InputForm onSubmit={handleSubmit} />);

  fireEvent.submit(screen.getByTestId('input-form'));
  expect(handleSubmit).toHaveBeenCalledTimes(1);
});
