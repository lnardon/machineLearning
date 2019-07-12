// Formula wx + b 

let w = 0;
let b = 0;
const learningRate = 0.05;

const features = [ ]; // Input Features Here
const KnownAnswers = [  ]; // Input Know answers here

// Stochastic Method ( Values improved one by one )
for ( let i = 0; i < features.length ; i++  ){

    let x = features[i];
    let y = KnownAnswers[i];

    let guess = w * x + b;
    let error = y - guess;

    w += ( error * x) * learningRate;
    b += error * learningRate; 


}