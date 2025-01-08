// 定义行数
const rows = 5; // 可以设定行数
// 定义列数
const cols = 5; // 可以设定列数
// 定义地雷数量
const mines = 5; // 可以设定雷数

// 启动游戏的函数
function startGame() {
    // 向后端发送请求以启动游戏
    fetch('/minesweeper/start_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        // 将行数、列数和雷数转换为 JSON 格式
        body: JSON.stringify({ rows, cols, mines })
    })
    // 处理响应
    .then(response => response.json())
    .then(data => {
        // 创建游戏棋盘
        createBoard();
        // 显示游戏开始的信息
        document.getElementById('message').innerText = "游戏开始！";
    });
}

// 创建游戏棋盘的函数
function createBoard() {
    // 获取棋盘元素
    const board = document.getElementById('game-board');
    // 清空棋盘内容
    board.innerHTML = '';
    // 遍历行
    for (let x = 0; x < rows; x++) {
        // 创建行元素
        const row = document.createElement('div');
        // 设置行的类名
        row.className = 'row';
        // 遍历列
        for (let y = 0; y < cols; y++) {
            const cell = document.createElement('div'); // 创建单元格元素
            cell.className = 'cell'; // 设置单元格的类名
            cell.setAttribute('data-x', x); // 设置单元格的 x 坐标
            cell.setAttribute('data-y', y); // 设置单元格的 y 坐标
            cell.innerText = '-'; // 设置单元格初始文本为 '-'
            // 为单元格添加点击事件监听器
            cell.addEventListener('click', function() {
                revealCell(x, y); // 点击时揭示该单元格
            });
            row.appendChild(cell); // 将单元格添加到行中
        }
        board.appendChild(row); // 将行添加到棋盘中
    }
}

// 揭示单元格的函数
function revealCell(x, y) {
    // 向后端发送请求以揭示指定单元格
    fetch('/minesweeper/reveal_cell', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ x, y }) // 将坐标转换为 JSON 格式
    })
    .then(response => response.json()) // 处理响应
    .then(data => {
        const cells = document.querySelectorAll('.cell'); // 获取所有单元格
        // 遍历雷区数据
        data.minefield.forEach((row, r) => {
            row.forEach((cell, c) => {
                const cellElement = Array.from(cells).find(el => el.dataset.x == r && el.dataset.y == c); // 找到对应的单元格元素
                if (cellElement) {
                    cellElement.innerText = cell; // 更新单元格的文本
                    if (cell === 'M') {
                        cellElement.style.backgroundColor = 'red'; // 如果是地雷，设置背景颜色为红色
                    }
                }
            });
        });
        // 检查游戏状态
        if (data.game_won) {
            document.getElementById('message').innerText = "恭喜你，成功扫雷！"; // 游戏胜利的信息
        } else if (data.status === "Hit a mine") {
            document.getElementById('message').innerText = "你踩到了雷，游戏结束！"; // 踩雷的信息
        }
    });
}

// 添加重置游戏按钮的事件监听器
document.getElementById('reset-button').addEventListener('click', function() {
    // 向后端发送请求以重置游戏
    fetch('/minesweeper/reset_game', {
        method: 'POST'
    })
    .then(response => response.json()) // 处理响应
    .then(data => {
        document.getElementById('message').innerText = "游戏已重置！"; // 显示重置的信息
        startGame(); // 重新开始游戏
    });
});

// 页面加载时开始游戏
window.onload = startGame;