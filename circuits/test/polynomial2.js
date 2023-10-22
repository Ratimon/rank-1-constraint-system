const chai = require("chai");
const path = require("path");
const F1Field = require("ffjavascript").F1Field;
const Scalar = require("ffjavascript").Scalar;
exports.p = Scalar.fromString("21888242871839275222246405745257275088548364400416034343698204186575808495617");
const Fr = new F1Field(exports.p);

const wasm_tester = require("circom_tester").wasm;

const assert = chai.assert;

describe("polynomial2 Test ", function (){
    this.timeout(100000);

    it("Should create a polynomial2 circuit", async()=>{
        const circuit = await wasm_tester(path.join(__dirname,"../polynomial2","polynomial2.circom"));
        await circuit.loadConstraints();
        let witness;

        const x = 2;
        const y = 2;

        witness = await circuit.calculateWitness({"x":x,"y":y }, true);
        console.log("witness -> ", witness);

        assert(Fr.eq(Fr.e(witness[0]), Fr.e(1)));
        assert(Fr.eq(Fr.e(witness[1]), Fr.e(1/2 *x*x*x*y*y + (-1/2) *x*x*x*y + (-1)*y*y*x*x + 2*x*x*y +  1/2*x*y*y + (-3/2)*x*y + x)));
    
    })
})