function listNames (arr) {
    let newArr;
    
 newArr = arr.sort ();
  

    for (let i=0;i<newArr.length;i++) {
       console.log((i+1)+"."+newArr[i])
    }

}
listNames (["John",

"Bob",

"Christina",

"Ema"]);
