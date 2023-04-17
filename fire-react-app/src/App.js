import React, { Component } from "react";
import Navbar from "./Navbar";
import Home from "./pages/Home";
import About from "./pages/About";
import Admin from "./pages/Admin";
import Data from "./pages/Data";
import "./styles.css";
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AdminLogin from './components/AdminLogin';
import AdminDashboard from './components/AdminDashboard';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const lightTheme = createTheme({
  palette: {
    mode: 'light',
  },
});

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      // heatMapData: []
    };
  }

  render() {
    return (
      <Router>
        <Navbar />
        <ThemeProvider theme={lightTheme}>
          <CssBaseline />
          <div className="page_container">
            <Routes>
              <Route
                path="/"
                element={<Home />}
              />
              <Route
                path="/Data"
                element={<Data />}
              />
              <Route
                path="/About"
                element={<About />}
              />
              <Route
                path="/Admin"
                element={<Admin />}
              />
              <Route path="/admin_panel/login/" element={<AdminLogin />} />
              <Route path="/admin_panel/dashboard/" element={<AdminDashboard />} />
            </Routes>
          </div>
        </ThemeProvider>
      </Router>
    );
  }
}

export default App;
