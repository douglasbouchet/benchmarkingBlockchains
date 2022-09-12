// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

contract PixelWar {
    string[3][3] pixels;

    constructor() payable {
        for (uint8 i = 0; i < 3; i++) {
            for (uint8 j = 0; j < 3; j++) {
                pixels[i][j] = "white";
            }
        }
    }

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
