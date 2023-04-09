import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import InputForm from '../InputForm';

test('renders InputForm', () => {
  render(<InputForm />);
  expect(screen.getByTestId('input-form')).toBeInTheDocument();
});

test('contains all input fields', () => {
  render(<InputForm />);
  expect(screen.getByLabelText('Issue Date')).toBeInTheDocument();
  expect(screen.getByLabelText('Maturity Date')).toBeInTheDocument();
  expect(screen.getByLabelText('Coupon Rate')).toBeInTheDocument();
  expect(screen.getByLabelText('Yield to Maturity')).toBeInTheDocument();
  expect(screen.getByLabelText('Credit Rating')).toBeInTheDocument();
  expect(screen.getByLabelText('Currency')).toBeInTheDocument();
  expect(screen.getByLabelText('Issuer')).toBeInTheDocument();
});

test('submits the form', () => {
  const handleSubmit = jest.fn();
  render(<InputForm onSubmit={handleSubmit} />);

  fireEvent.change(screen.getByLabelText('Issue Date'), { target: { value: '2023-01-01' } });
  fireEvent.change(screen.getByLabelText('Maturity Date'), { target: { value: '2033-01-01' } });
  fireEvent.change(screen.getByLabelText('Coupon Rate'), { target: { value: '5' } });
  fireEvent.change(screen.getByLabelText('Yield to Maturity'), { target: { value: '4.5' } });
  fireEvent.change(screen.getByLabelText('Credit Rating'), { target: { value: 'AAA' } });
  fireEvent.change(screen.getByLabelText('Currency'), { target: { value: 'USD' } });
  fireEvent.change(screen.getByLabelText('Issuer'), { target: { value: 'SomeIssuer' } });

  fireEvent.submit(screen.getByTestId('input-form'));
  expect(handleSubmit).toHaveBeenCalledTimes(1);
  expect(handleSubmit).toHaveBeenCalledWith({
    issueDate: '2023-01-01',
    maturityDate: '2033-01-01',
    couponRate: '5',
    yieldToMaturity: '4.5',
    creditRating: 'AAA',
    currency: 'USD',
    issuer: 'SomeIssuer',
  });
});
