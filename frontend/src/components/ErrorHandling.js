import React from 'react';
import './styles/ErrorHandling.css';

const ErrorHandling = ({ error }) => {
  if (!error) {
    return null;
  }

  return (
    <div data-testid="error-handling" className="error-message">
      {error}
    </div>
  );
};

export default ErrorHandling;
