import React, {useState} from 'react';
import ItemForm from "./ItemForm";

const ListForm = () => {

    const [items, setItems] = useState([
        {id: 1, htmlFor: "id_username", id_input: "id_username", title: "Email",  type: "email", placeholder: "example@gmail.com"},
        {id: 2, htmlFor: "id_password", id_input: "id_password", title: "Password", type: "password", placeholder: "password"}
    ]);

    return (
        <div>
            {items.map((item) =>
                <ItemForm post={item} key={item.id}/>
            )}
        </div>
    );
};

export default ListForm;