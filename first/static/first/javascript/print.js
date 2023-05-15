function setTime(){
    const weekend = ["Воскресень", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    const month = ["Января","Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    var today = new Date();
    var ww = weekend[today.getDay()]
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = month[today.getMonth()];
    var yyyy = today.getFullYear();
    today = ww + " " + dd  + " " + mm + " " + yyyy + " года";
    document.getElementById("datetime").innerHTML = today
}
function setNumber(){
    var number = document.getElementById("number").value
    document.getElementById("main-number").innerHTML = number
}
function setReason(){
    var reason = document.getElementById("typed-reason").value
    if(reason == ""){
        document.getElementById("reason").innerHTML = "обслед"
    }else{
        document.getElementById("reason").innerHTML = reason
    }
}
function setFinance(){
    var finance = document.getElementById("typed-finance").value
    if (finance == ""){
        document.getElementById("finance").innerHTML = "гос.заказ"
    }else{
        document.getElementById("finance").innerHTML = finance
    }   
}
function setWhere(){
    var place = document.getElementById("where-to").value
    if(place == ""){
        document.getElementById("where").innerHTML = "НАО МУК"
    }else{
        document.getElementById("where").innerHTML = place
    }
}
function deleteForm(){
    const form = document.getElementById("form")
    form.remove()
}
function printPage(){
    window.print()
}