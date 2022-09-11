// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

contract PixelWar {
    //uint256 public unlockTime;
    //address payable public owner;
    string[3][3] pixels;

    //event Withdrawal(uint256 amount, uint256 when);

    constructor() payable {
        //require(
        //    block.timestamp < _unlockTime,
        //    "Unlock time should be in the future"
        //);

        // unlockTime = _unlockTime;
        //owner = payable(msg.sender);
        for (uint8 i = 0; i < 3; i++) {
            for (uint8 j = 0; j < 3; j++) {
                pixels[i][j] = "white";
            }
        }
    }

    // function withdraw() public {
    //     // Uncomment this line, and the import of "hardhat/console.sol", to print a log in your terminal
    //     // console.log("Unlock time is %o and block timestamp is %o", unlockTime, block.timestamp);

    //     require(block.timestamp >= unlockTime, "You can't withdraw yet");
    //     require(msg.sender == owner, "You aren't the owner");

    //     emit Withdrawal(address(this).balance, block.timestamp);

    //     owner.transfer(address(this).balance);
    // }

    function getPixels() public view returns (string[3][3] memory) {
        return pixels;
    }

    function setPixel(
        uint8 x,
        uint8 y,
        string memory color
    ) public payable {
        require(x > -1 && x < 3, "x should be less than 3");
        require(y > -1 && y < 3, "y should be less than 3");
        //require(
        //    keccak256(abi.encodePacked(color)) ==
        //        keccak256(abi.encodePacked("red")) ||
        //        keccak256(abi.encodePacked(color)) ==
        //        keccak256(abi.encodePacked("green")) ||
        //        keccak256(abi.encodePacked(color)) ==
        //        keccak256(abi.encodePacked("blue")),
        //    "color should be red, green or blue"
        //);

        pixels[x][y] = color;
    }
}
