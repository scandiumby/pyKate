import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import LeftSidebar from "./components/LeftSidebar";
import RightSidebar from "./components/RightSidebar";
import Content from "./components/Content";

function App() {
  return (
    <div className="App">
        <Header/>
        <LeftSidebar/>
        <RightSidebar/>
        <Content/>
        <Footer/>
    </div>
  );
}

export default App;