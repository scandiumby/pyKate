import React from 'react';

const LoginForm = () => {
    return (
        <form>
            <div className="itemForm">
                <label className="labelForm" htmlFor="id_username">Email</label>
                <input type="email" className="inputForm" id="id_username" placeholder="example@gmail.com"/>
            </div>
            <div className="itemForm">
                <label className="labelForm" htmlFor="id_password">Password</label>
                <input type="password" className="inputForm" id="id_password" placeholder="Password"/>
            </div>

        </form>
    );
};

export default LoginForm;