import React from 'react';

const ItemForm = (props) => {

    return (
        <div className="itemForm">
            <label className="labelForm" htmlFor={props.post.htmlFor}>{props.post.title}</label>
            <input type={props.post.type} className="inputForm" id={props.post.id_input} placeholder={props.post.placeholder}/>
        </div>
    );
};

export default ItemForm;