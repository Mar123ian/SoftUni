function toggle() {
    
    let a =document.getElementById("extra")
    let button=document.getElementsByClassName("button")[0];
    if(a.style.display!="block"){
        a.style.display="block";
        button.innerText="Less"
    }
    else{
        a.style.display="none";
        button.innerText="More"
    }
    
}