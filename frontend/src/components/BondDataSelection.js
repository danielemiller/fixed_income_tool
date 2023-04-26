import React from 'react';
import './styles/BondDataSelection.css';
import BondInfoModal from './BondInfoModal';
import {sampleBondData} from './sampleBondData';

const bondDataList = sampleBondData;

const BondDataSelection = ({ onBondDataSelect }) => {
  const [showModal, setShowModal] = React.useState(false);
  const [selectedBondData, setSelectedBondData] = React.useState(null);
  
  const handleClick = (bondData) => {
    if (onBondDataSelect) {
      onBondDataSelect(bondData);
    }
  };

  const handleInfoClick = (bondData) => {
    setSelectedBondData(bondData);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  return (
    <div className="bond-data-selection">
    {bondDataList.map((bondData, index) => (
      <div key={index} className="bond-data-column">
        <button onClick={() => handleClick(bondData.data)}>
          Select {bondData.type}
        </button>
        <button onClick={() => handleInfoClick(bondData)}>
          {bondData.type} Info
        </button>
      </div>
    ))}
    <BondInfoModal show={showModal} onClose={handleCloseModal} bondData={selectedBondData} />
  </div>
  );
};

export default BondDataSelection;
