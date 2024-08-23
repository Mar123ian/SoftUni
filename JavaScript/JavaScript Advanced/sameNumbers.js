function sameNumbers (num) {
let a=num.toString()
let b=true
let sum=0 
for (let index = 0; index < a.length-1; index++) {
    let element = a[index];
    let nextElement=a[index+1]
    sum+=Number(element)
    if (element!=nextElement){
        b=false
    }
}
sum+=Number(a[a.length-1])
console.log(b);
console.log(sum);
}
sameNumbers (2222222);
sameNumbers (1234);
