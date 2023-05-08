import React from 'react';
import './styles/BondDataSelection.css';
import BondInfoModal from './BondInfoModal';
import './styles/BondInfoModal.css';


const BondDataSelection = ({ bondDataList, onBondDataSelect }) => {
  const [showModal, setShowModal] = React.useState(false);
  const [selectedBondData, setSelectedBondData] = React.useState(null);
  
  const handleClick = (bondData) => {
    console.log("i've been clicked")
    if (onBondDataSelect) {
      console.log('Entered the onBondDataSelect')
      console.log(bondData)
      onBondDataSelect({...bondData});
    }
  };

  const handleInfoClick = (bondData) => {
    console.log("i've been clicked")
    console.log(bondData)
    setSelectedBondData(bondData);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    console.log("i've been clicked")
    setShowModal(false);
  };

  return (
    <div className="bond-data-selection">
      {bondDataList.length === 0 ? (
        <p>Loading sample bond data...</p>
      ) : (
        bondDataList.map((bondData, index) => (
          <div key={index} className="bond-data-column">
            <button onClick={() => handleClick(bondData)}>
              Select {bondData.type}
            </button>
            <button onClick={() => handleInfoClick(bondData)}>
              {bondData.type} Info
            </button>
          </div>
        ))
      )}
      {showModal && selectedBondData && (
      <BondInfoModal
        key={selectedBondData.type}
        show={showModal}
        onClose={handleCloseModal}
        bondData={selectedBondData}
      />
    )}
      {/* <BondInfoModal  key={selectedBondData ? selectedBondData.type : 'initial'} show={showModal} onClose={handleCloseModal} bondData={selectedBondData} /> */}
    </div>
  );
};

export default BondDataSelection;


