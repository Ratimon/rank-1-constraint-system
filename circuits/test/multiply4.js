const chai = require("chai");
const path = require("path");
const F1Field = require("ffjavascript").F1Field;
const Scalar = require("ffjavascript").Scalar;
exports.p = Scalar.fromString("21888242871839275222246405745257275088548364400416034343698204186575808495617");
const Fr = new F1Field(exports.p);

const wasm_tester = require("circom_tester").wasm;

const assert = chai.assert;

describe("multiply4 Test ", function (){
    this.timeout(100000);

    it("Should create a multiply4 circuit", async()=>{
        const circuit = await wasm_tester(path.join(__dirname,"../multiply4","multiply4.circom"));
        await circuit.loadConstraints();
        let witness;

        const expectedOutput = 210;

        witness = await circuit.calculateWitness({"x":2,"y":3,"z":5,"u":7 }, true);
        console.log("witness -> ", witness);

        assert(Fr.eq(Fr.e(witness[0]), Fr.e(1)));
        assert(Fr.eq(Fr.e(witness[1]), Fr.e(expectedOutput)));
    
    })
})