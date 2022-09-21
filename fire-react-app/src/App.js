import React from "react"
import Navbar from "./Navbar"
import Home from "./pages/Home"
import About from "./pages/About"
import Admin from "./pages/Admin"
import Data from "./pages/Data"
import "./styles.css"
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <>
      <Navbar />
      <div className="page_container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Data" element={<Data />} />
          <Route path="/About" element={<About />} />
          <Route path="/Admin" element={<Admin />} />
        </Routes>
      </div>
      </>
  )
}

export default App;
