//// ADJUST BUTTONS

let minusBtn = document.getElementsByClassName("adjust-btn-minus")

let plusBtn = document.getElementsByClassName("adjust-btn-plus")


/// increase

for (let i = 0; i < plusBtn.length; i++) {
    const button = plusBtn[i];
    button.addEventListener("click", function (event) {
        let btnClicked = event.target;

        let input = btnClicked.parentElement.parentElement.children[0]

        let inputValue = input.value;

        let newValue = parseInt(inputValue) + 1;

        input.value = newValue
    })

}


/// decrease

for (let i = 0; i < minusBtn.length; i++) {
    const button = minusBtn[i];
    button.addEventListener("click", function (event) {
        let btnClicked = event.target;

        let input = btnClicked.parentElement.parentElement.children[0]

        let inputValue = input.value;

        let newValue = parseInt(inputValue) - 1;

        if (newValue >= 0) {
            input.value = newValue;
        } else {
            newValue = 0
        }
    })

}


//// ADD ROLE 

let addRoleBtn = document.getElementById("add-role-btn")

addRoleBtn.addEventListener("click", function () {
    let newInput = document.createElement("select");
    // let option1 = document.createElement("option")

    newInput.innerHTML = ` <select name="role" id="role">
    <option value=""></option>
    <option value="manager">Manažer</option>
    <option value="seller">Prodavač</option>
    <option value="whman">Skladník</option>
    <option value="shift-leader">Vedoucí směny</option>
</select>`

    newInput.style.marginTop = "10px"

    document.querySelector(".role-input").appendChild(newInput)
    // document.querySelector(".role-input").appendChild(option1)

    // newInput.setAttribute("name", "role")
    // newInput.setAttribute("id", "role")
})



    // < select name = "role" id = "role" >
    //                     <option value=""></option>
    //                     <option value="manager">Manažer</option>
    //                     <option value="seller">Prodavač</option>
    //                     <option value="whman">Skladník</option>
    //                     <option value="shift-leader">Vedoucí směny</option>
    //                 </select >