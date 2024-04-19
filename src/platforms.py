PLATFORMS: dict[str, tuple[int, list[list[int]]]] = {
    "tenerife": (5, [[1, 0], [2, 0], [2, 1], [3, 2], [3, 4], [4, 2]]),
    "melbourne": (
        14,
        [
            [1, 0],
            [1, 2],
            [2, 3],
            [4, 3],
            [4, 10],
            [5, 4],
            [5, 6],
            [5, 9],
            [6, 8],
            [7, 8],
            [9, 8],
            [9, 10],
            [11, 3],
            [11, 10],
            [11, 12],
            [12, 2],
            [13, 1],
            [13, 12],
        ],
    ),
    "tokyo": (
        20,
        [
            [0, 1],
            [0, 5],
            [1, 0],
            [1, 2],
            [1, 6],
            [1, 7],
            [2, 1],
            [2, 6],
            [3, 8],
            [4, 8],
            [4, 9],
            [5, 0],
            [5, 6],
            [5, 10],
            [5, 11],
            [6, 1],
            [6, 2],
            [6, 5],
            [6, 7],
            [6, 10],
            [6, 11],
            [7, 1],
            [7, 6],
            [7, 8],
            [7, 12],
            [8, 3],
            [8, 4],
            [8, 7],
            [8, 9],
            [8, 12],
            [8, 13],
            [9, 4],
            [9, 8],
            [10, 5],
            [10, 6],
            [10, 11],
            [10, 15],
            [11, 5],
            [11, 6],
            [11, 10],
            [11, 12],
            [11, 16],
            [11, 17],
            [12, 7],
            [12, 8],
            [12, 11],
            [12, 13],
            [12, 16],
            [13, 8],
            [13, 12],
            [13, 14],
            [13, 18],
            [13, 19],
            [14, 13],
            [14, 18],
            [14, 19],
            [15, 10],
            [15, 16],
            [16, 11],
            [16, 12],
            [16, 15],
            [16, 17],
            [17, 11],
            [17, 16],
            [17, 18],
            [18, 13],
            [18, 14],
            [18, 17],
            [19, 13],
            [19, 14],
        ],
    ),
    "sycamore": (
        54,
        [
            [0, 6],
            [1, 6],
            [1, 7],
            [2, 7],
            [2, 8],
            [3, 8],
            [3, 9],
            [4, 9],
            [4, 10],
            [5, 10],
            [5, 11],
            [6, 12],
            [6, 13],
            [7, 13],
            [7, 14],
            [8, 14],
            [8, 15],
            [9, 15],
            [9, 16],
            [10, 16],
            [10, 17],
            [11, 17],
            [12, 18],
            [13, 18],
            [13, 19],
            [14, 19],
            [14, 20],
            [15, 20],
            [15, 21],
            [16, 21],
            [16, 22],
            [17, 22],
            [17, 23],
            [18, 24],
            [18, 25],
            [19, 25],
            [19, 26],
            [20, 26],
            [20, 27],
            [21, 27],
            [21, 28],
            [22, 28],
            [22, 29],
            [23, 29],
            [24, 30],
            [25, 30],
            [25, 31],
            [26, 31],
            [26, 32],
            [27, 32],
            [27, 33],
            [28, 33],
            [28, 34],
            [29, 34],
            [29, 35],
            [30, 36],
            [30, 37],
            [31, 37],
            [31, 38],
            [32, 38],
            [32, 39],
            [33, 39],
            [33, 40],
            [34, 40],
            [34, 41],
            [35, 41],
            [36, 42],
            [37, 42],
            [37, 43],
            [38, 43],
            [38, 44],
            [39, 44],
            [39, 45],
            [40, 45],
            [40, 46],
            [41, 46],
            [41, 47],
            [42, 48],
            [42, 49],
            [43, 49],
            [43, 50],
            [44, 50],
            [44, 51],
            [45, 51],
            [45, 52],
            [46, 52],
            [46, 53],
            [47, 53],
        ],
    ),
    "rigetti80": (
        80,
        [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 0],
            [0, 13],
            [1, 12],
            [2, 47],
            [3, 46],
            [8, 9],
            [9, 10],
            [10, 11],
            [11, 12],
            [12, 13],
            [13, 14],
            [14, 15],
            [15, 8],
            [8, 21],
            [9, 20],
            [10, 55],
            [11, 54],
            [16, 17],
            [17, 18],
            [18, 19],
            [19, 20],
            [20, 21],
            [21, 22],
            [22, 23],
            [23, 16],
            [16, 29],
            [17, 28],
            [18, 63],
            [19, 62],
            [24, 25],
            [25, 26],
            [26, 27],
            [27, 28],
            [28, 29],
            [29, 30],
            [30, 31],
            [31, 24],
            [24, 37],
            [25, 36],
            [26, 71],
            [27, 70],
            [32, 33],
            [33, 34],
            [34, 35],
            [35, 36],
            [36, 37],
            [37, 38],
            [38, 39],
            [39, 32],
            [34, 79],
            [35, 78],
            [40, 41],
            [41, 42],
            [42, 43],
            [43, 44],
            [44, 45],
            [45, 46],
            [46, 47],
            [47, 40],
            [40, 53],
            [41, 52],
            [48, 49],
            [49, 50],
            [50, 51],
            [51, 52],
            [52, 53],
            [53, 54],
            [54, 55],
            [55, 48],
            [48, 61],
            [49, 60],
            [56, 57],
            [57, 58],
            [58, 59],
            [59, 60],
            [60, 61],
            [61, 62],
            [62, 63],
            [63, 56],
            [56, 69],
            [57, 68],
            [64, 65],
            [65, 66],
            [66, 67],
            [67, 68],
            [68, 69],
            [69, 70],
            [70, 71],
            [71, 64],
            [64, 77],
            [65, 76],
            [72, 73],
            [73, 74],
            [74, 75],
            [75, 76],
            [76, 77],
            [77, 78],
            [78, 79],
            [79, 72],
        ],
    
    ),
    "eagle": (
        127,
        [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 8],
            [9, 10],
            [10, 11],
            [11, 12],
            [12, 13],
            [0, 14],
            [14, 18],
            [4, 15],
            [15, 22],
            [8, 16],
            [16, 26],
            [12, 17],
            [17, 30],
            [18, 19],
            [19, 20],
            [20, 21],
            [21, 22],
            [22, 23],
            [23, 24],
            [24, 25],
            [25, 26],
            [26, 27],
            [27, 28],
            [28, 29],
            [29, 30],
            [30, 31],
            [31, 32],
            [20, 33],
            [33, 39],
            [24, 34],
            [34, 43],
            [28, 35],
            [35, 47],
            [32, 36],
            [36, 51],
            [37, 38],
            [38, 39],
            [39, 40],
            [40, 41],
            [41, 42],
            [42, 43],
            [43, 44],
            [44, 45],
            [45, 46],
            [46, 47],
            [47, 48],
            [48, 49],
            [49, 50],
            [50, 51],
            [37, 52],
            [52, 56],
            [41, 53],
            [53, 60],
            [45, 54],
            [54, 64],
            [49, 55],
            [55, 68],
            [56, 57],
            [57, 58],
            [58, 59],
            [59, 60],
            [60, 61],
            [61, 62],
            [62, 63],
            [63, 64],
            [64, 65],
            [65, 66],
            [66, 67],
            [67, 68],
            [68, 69],
            [69, 70],
            [58, 71],
            [71, 77],
            [62, 72],
            [72, 81],
            [66, 73],
            [73, 85],
            [70, 74],
            [74, 89],
            [75, 76],
            [76, 77],
            [77, 78],
            [78, 79],
            [79, 80],
            [80, 81],
            [81, 82],
            [82, 83],
            [83, 84],
            [84, 85],
            [85, 86],
            [86, 87],
            [87, 88],
            [88, 89],
            [75, 90],
            [90, 94],
            [79, 91],
            [91, 98],
            [83, 92],
            [92, 102],
            [87, 93],
            [93, 106],
            [94, 95],
            [95, 96],
            [96, 97],
            [97, 98],
            [98, 99],
            [99, 100],
            [100, 101],
            [101, 102],
            [102, 103],
            [103, 104],
            [104, 105],
            [105, 106],
            [106, 107],
            [107, 108],
            [96, 109],
            [100, 110],
            [110, 118],
            [104, 111],
            [111, 112],
            [108, 112],
            [112, 126],
            [113, 114],
            [114, 115],
            [115, 116],
            [116, 117],
            [117, 118],
            [118, 119],
            [119, 120],
            [120, 121],
            [121, 122],
            [122, 123],
            [123, 124],
            [124, 125],
            [125, 126],
        ],
    ),
}