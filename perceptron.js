// Formula input 0 * weight 0 + input 1 * weight 1
/*

First Step - Get the sum of inputs and weights ( Formula Above )
Second Step - Activation Function receives the result of the first step and decides if the neuron should fire or not ( 1 , -1 )
Third Step - Pass training data and get the optimal weight after the training 
           - Use gradient descent to calc the optimal weight ( new w = w + ( error * input * learning rate ) ) 
Fouth Step - With the neuron trained , pass the data you wish to classify

*/


// Neuron ( Perceptron )
class Perceptron {
    weights = [];
    error = 0;
    lr = 0.1;

    // Initialize weights randomly
    constructor (){
        for ( let i = 0 ; i < 8 ; i++ ){
            this.weights[i] = Math.random();
        }
    }

    getW(){
        return this.weights;
    }

    guess (inputs) {
        let num = 0;
        for ( let i = 0 ; i < inputs.length; i++ ){
            num += inputs[i] * this.weights[i];
        }
        return pActivation(num);
    }

    train ( inputs , desired ){
        this.error = desired - this.guess(desired);

        //Adjusts the weights according to the error
        for ( let i = 0 ; i < this.weights.length; i++ ){
            this.weights[i] += this.error * inputs[i] * this.lr;
        }
    }
}

// Activation Function
function pActivation( n ) {

    if ( n > 0.5){
        return 1;
    } else {
        return 0;
    }
}




// ==================================          Tests         =========================================

let p1 = new Perceptron();

let trainingParams = [ 0.4,0.6,0,7,0.1,0.55,0.99, 0.36]; // Check if a number is multiple of 5
let trainingResults = [ 0,1,1,0,1,1,0 ]; // 0 for FALSE and 1 for TRUE

//p1.train( trainingParams , trainingResults );

for( let i = 1; i < 10 ; i++ ){
    console.log(p1.guess( [0.23] ));
    console.log(p1.getW());
}