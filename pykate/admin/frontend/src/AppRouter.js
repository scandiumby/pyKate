import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import HomePage from './components/HomePage';
import './style/App.css';

function AppRouter() {
    return (
        <div className="container" style={{marginTop: 150}}>
        <Router>
            <Routes>
                <Route path="/login" element={<LoginPage />} />
                <Route path="/" element={<HomePage />} />
            </Routes>
        </Router>
        </div>
    );
}

export default AppRouter;
