import React from 'react';
import './styles/BondInfoModal.css';

const BondInfoModal = ({ show, onClose, bondData }) => {
  if (!show) {
    return null;
  }

  return (
    <div className="bond-info-modal">
      <div className="modal-content">
        <p>Brief description of this bond and what makes it great.</p>
        <h2>{bondData.type}</h2>
        <p>Issuer: {bondData.data.issuer}</p>
        <p>Maturity Date: {bondData.data.maturity_date}</p>
        <p>Face Value: {bondData.data.face_value}</p>
        <p>Coupon Rate: {bondData.data.coupon_rate}</p>
        <p>Years to Maturity: {bondData.data.years_to_maturity}</p>
        <p>Credit Rating: {bondData.data.credit_rating}</p>
        <p>Currency: {bondData.data.currency}</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default BondInfoModal;
