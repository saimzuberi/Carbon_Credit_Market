pragma solidity ^0.5.5;

//  Import the following contracts from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC20Detailed`
//    * `ERC20Mintable`
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

// // Create a constructor for the KaseiCoin contract and have the contract inherit the libraries that you imported from OpenZeppelin.
contract CarbonTokenC is ERC20Detailed, ERC20, ERC20Mintable {

    constructor(
        string memory CarbonCreditGradeC,
        string memory CCGC,
        uint decimals
        )
        ERC20Detailed(CarbonCreditGradeC, CCGC, 18)
        public
    {
        // constructor can stay empty
    }

}