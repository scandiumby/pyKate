import React from 'react';
import LoginForm from "./LoginForm";

const LoginPage = () => {
    return (
        <div>
            <h1 style={{textAlign: 'center'}}>Login Page</h1>
            <br/>
            <LoginForm/>
            <br/>
            <a href="/">Назад</a>
        </div>
    );
};

export default LoginPage;