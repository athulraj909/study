function date(){
    document.getElementById('demo').innerHTML=Date();
}

function show(){
    b=document.getElementById('a');
    b.innerHTML="hello";
    b.style.display='block';
}

function altertext(){
    var b=document.getElementById('a');
    b.style.color='red';
    b.style.fontSize='35px';
    b.style.display='block'
}

function hide(){
    document.getElementById('a').style.display='none'
}

function statement(){
    let x, y, z;  // Statement 1
x = 5;        // Statement 2
y = 6;        // Statement 3
z = x + y;    // Statement 4

document.getElementById("demo").innerHTML =
"The value of z is " + z + ".";  
}

const person = {
    firstName : "John",
    lastName  : "Doe",
    age     : 50,
    eyeColor  : "blue"
  };
  
  document.getElementById("d").innerHTML =
  person.firstName +" "+person.lastName+ " is " + person.age + " years old.";