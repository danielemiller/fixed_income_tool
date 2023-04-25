import React, { useState } from 'react';
import './styles/Header.css';
import logo from './images/logo.png';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const handleMenuClick = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="header">
      <div className="header-logo">
        <img src={logo} alt="Logo" />
        <h1 className="header-title">The Fixed Income App</h1>
      </div>
      <nav className={`header-nav ${isMenuOpen ? 'header-nav-open' : ''}`}>
        <ul>
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a href="/documentation">Documentation</a>
          </li>
          <li>
            <a href="/blog">Fixed Income Blog</a>
          </li>
        </ul>
      </nav>
      <div className="hamburger-menu" onClick={handleMenuClick}>
        <span></span>
        <span></span>
        <span></span>
      </div>
    </header>
  );
};

export default Header;
