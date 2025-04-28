import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import '../css/FadeTransition.css'; // Import the CSS for fade effect

const FadeWrapper = ({ children }) => {
  const location = useLocation();
  const [fade, setFade] = useState(false);

  useEffect(() => {
    setFade(false); // Start with fade out
    document.documentElement.scrollTop = 0; // Teleport to the top of the page without triggering scroll events
    const timer = setTimeout(() => setFade(true), 150); // Delay to allow fade out before fade in
    return () => clearTimeout(timer);

  }, [location]);

  return (
    <div className={`fade-wrapper-${fade ? 'active' : 'inactive'}`} style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
        {children}
    </div>
  );
};

export default FadeWrapper;
