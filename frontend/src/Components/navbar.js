import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  }

  return (
    <nav>
      <div className="navbar">
        <Link to="/" className="navbar-brand">My Website</Link>
        <button className="navbar-toggler" onClick={handleToggle}>
          <i className="fas fa-bars"></i>
        </button>
        <div className={`navbar-menu ${isOpen ? 'is-active' : ''}`}>
          <Link to="/about" className="navbar-item" onClick={handleToggle}>About</Link>
          <Link to="/projects" className="navbar-item" onClick={handleToggle}>My Projects</Link>
          <Link to="/publications" className="navbar-item" onClick={handleToggle}>My Publications</Link>
          <Link to="/contact" className="navbar-item" onClick={handleToggle}>Contact Me</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
