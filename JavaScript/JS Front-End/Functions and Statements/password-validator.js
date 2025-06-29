function passwordValidator(pass){

    const regexalnum = /^[A-Za-z0-9]+$/gm;
    const regexnum = /\d/gm;
    let isValid=true;

    if (pass.length<6 || pass.length>10){
        console.log("Password must be between 6 and 10 characters");
        isValid=false;
    }

    if(!regexalnum.test(pass)){
        console.log("Password must consist only of letters and digits");
        isValid=false;
    }

    if((!pass.match(regexnum)) || pass.match(regexnum).length<2){
        console.log("Password must have at least 2 digits");
        isValid=false;
    }

    if (isValid){
        console.log("Password is valid");
    }


}

passwordValidator('Pa$s$s')