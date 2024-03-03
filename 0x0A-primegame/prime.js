function isprime(number){
    if (number<2 || number==4) return false;
    for (i= 2; i < number/2; i++) {
        if (number % i == 0) return false
    }

    return true;
}

function prime(rounds, arr) {
    let maria = 0
let ben = 0
for (let i = 0; i < rounds; i++) {
    if (arr[i]%2 == 0){
        ben ++
    }
    else if (arr[i] == 1) ben ++
    else if (arr[i]%2 == 1){
        maria ++
    }
    else if (isprime(arr[i])) maria++
    else ben ++
}

if(maria > ben) console.log('maria wins', maria, ben)
else console.log('ben wins', ben, maria);
}

prime(3, [4, 5, 1]);
