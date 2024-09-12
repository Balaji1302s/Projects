const inputBox = document.getElementById("input_box");
const listcontainer = document.getElementById("todo_list");
// console.log(inputBox.value);
function addTask(){
    // consolelog(5);
    if(inputBox.value === '')
    {
        alert("you Must Write Something");
    }
    else{
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        listcontainer.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML='\u00d7'
        li.appendChild(span)
    }
    inputBox.value ='';
    saveData();
}
listcontainer.addEventListener("click",function(eve){
    
    if(eve.target.tagName === "LI"){
        eve.target.classList.toggle("checked");
        saveData()
    }
    else if(eve.target.tagName === "SPAN"){
        eve.target.parentElement.remove();
        saveData()
    }
},false);
function saveData(){
    localStorage.setItem("data",todo_list.innerHTML);
}
function showlist(){
    listcontainer.innerHTML = localStorage.getItem("data");
}
showlist();
