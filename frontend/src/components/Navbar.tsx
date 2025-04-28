import { Navbar as BootstrapNavbar, Nav, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import '../css/Navbar.css'; // Import the new CSS file
import { FaBrain } from 'react-icons/fa';

export const Navbar = () => {
  const navigate = useNavigate();

  return (
    <BootstrapNavbar expand="lg" className="navbar">
      <BootstrapNavbar.Brand onClick={() => navigate('/')} className="navbar-brand mx-2">
        <div className="logo">
            <FaBrain size={30} />
        </div>
      </BootstrapNavbar.Brand>
      {/* <Nav className="navbar-nav">
        <Button variant="dark" onClick={() => navigate('/form')} className="navbar-button mx-1">
            Go to Form
        </Button>
        <Button variant="dark" onClick={() => navigate('/')} className="navbar-button mx-1">
          <BiHomeAlt />
        </Button>
      </Nav> */}
    </BootstrapNavbar>
  );
}
