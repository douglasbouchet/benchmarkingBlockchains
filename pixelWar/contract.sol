pragma solidity >=0.7.0;

contract pixelWar {
    bytes7[2000][2000] pixels;

    //initialize the pixels
    constructor() {
        for (uint256 i = 0; i < 2000; i++) {
            for (uint256 j = 0; j < 2000; j++) {
                pixels[i][j] = "#000000";
            }
        }
    }

    // function setPixel(
    //     uint256 x,
    //     uint256 y,
    //     bytes7 color
    // ) public {
    //     pixels[x][y] = color;
    // }
    // function setPixel(
    //     uint256 x,
    //     uint256 y
    //     //uint256 color
    // ) public {
    //     pixels[x][y] = "#000000";
    // }
    function setPixel(uint256 x, uint256 y) public {
        pixels[x][y] = "#000001";
    }
}
