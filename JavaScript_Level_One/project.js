var firstName = prompt('Enter your first name: ');
var lastName = prompt('Enter your last name: ');
var age = prompt('Enter your age in years: ');
var pet = prompt('Enter the name of your pet: ');
var height = prompt('Enter your height in cm: ');

if ((firstName[0]===lastName[0]) && (20<age<30) && (height>=175) && (pet.slice(-1)==='y')) {
    console.log('Congrats, you are a spy!')
}