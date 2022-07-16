
console.log('example');


function getUsersFromBackend(){
    const value = document.getElementById('input_number_backend').value;
    fetch(`http://localhost:5000/assignment4/outer_source/json?number=${value}`).then(
        response => response.json()
    ).then(
        response => put_users_inside_html_from_backend(response.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html_from_backend(response_obj_data) {
    // console.log(response_obj_data);

    const curr_main = document.getElementById("main_backend");
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">Send Email</a>
        </div>
        `;
        curr_main.innerHTML = section.innerHTML;

}

function getUsers(){
    const value = document.getElementById('input_number').value;
    fetch(`https://reqres.in/api/users/${value}`).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">Send Email</a>
        </div>
        `;
        curr_main.innerHTML = section.innerHTML;

}





