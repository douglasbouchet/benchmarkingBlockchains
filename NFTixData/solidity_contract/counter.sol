pragma solidity >=0.7.0;

/**
 * @title Counter
 * @dev Implements a simpler version of selling an NFTix ticket
 */
contract Counter {
    // int private count = 0;
    // function Add() public {
    //     count += 1;
    // }

    // function primarySale(
    //     address _destinationAddress,
    //     address _eventAddress,
    //     uint256 _primaryPrice,
    //     uint256 _basePrice,
    //     uint256 _orderTime,
    //     bytes32[] memory _ticketMetadata
    // ) public {}

    function primarySale() public pure {
        // simpler version of primary sale without arguments for now
        uint32 counter = 0;
        counter += 1;
    }
}
