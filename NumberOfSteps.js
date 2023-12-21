let num = 14;
let i = 0;

while(num > 0){
    if(num%2==0){
        num = num/2;
    }   
    else{
        num = num - 1;
    }
    i += 1;
}
console.log("%d", i);