import React from 'react';
import './styles/BondDataSelection.css';

const bondDataList = [
  // Add your bond data objects here with their respective types and data
  { type: 'Bond Type 1', data: { /* Bond data for type 1 */ } },
  { type: 'Bond Type 2', data: { /* Bond data for type 2 */ } },
  { type: 'Bond Type 3', data: { /* Bond data for type 3 */ } },
  { type: 'Bond Type 4', data: { /* Bond data for type 4 */ } },
];

const BondDataSelection = ({ onBondDataSelect }) => {
  const handleClick = (bondData) => {
    if (onBondDataSelect) {
      onBondDataSelect(bondData);
    }
  };

  return (
    <div className="bond-data-selection">
      {bondDataList.map((bondData, index) => (
        <div key={index} className="bond-data-column">
          <button onClick={() => handleClick(bondData.data)}>
            Select {bondData.type}
          </button>
        </div>
      ))}
    </div>
  );
};

export default BondDataSelection;
