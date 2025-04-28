import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { FormPage } from './pages/FormPage';
import { LandingPage } from './pages/LandingPage';
import FadeWrapper from './components/FadeWrapper';
import { Navbar } from './components/Navbar';
import { Disclaimer } from './pages/Disclaimer';
function App() {
  return (
    <Router>
      <Navbar />
      <FadeWrapper>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/form" element={<FormPage />} />
        <Route path="/disclaimer" element={<Disclaimer />} />
      </Routes>
      </FadeWrapper>
    </Router>
  );
}

export default App;
