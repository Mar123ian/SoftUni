function rotation(arr, a){

for(let j=0;j<a;j++){
    let last=arr[arr.length-1];
    let first=arr[0];
    arr[0]=last;
    let current;
    let moving=first;

    for(i=1;i<arr.length;i++){
        current=arr[i];
        arr[i]=moving;
        moving=current;
    }

}
let string="";
for(let i=0;i<arr.length;i++){
    string+=(arr[i])+" ";
}
