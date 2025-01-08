// 获取画布元素和绘图上下文
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// 初始化玩家位置、敌人、子弹、分数、游戏状态等变量
let playerPos = [400, 550]; // 玩家初始位置
let enemies = []; // 敌人数组
let bullets = []; // 子弹数组
let score = 0; // 游戏分数
let gameOver = false; // 游戏是否结束标志
let gameLoopId; // 用于存储请求动画帧的 ID

// 绘制游戏场景
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 清空画布

    // 绘制玩家
    ctx.fillStyle = 'black';
    ctx.fillRect(playerPos[0], playerPos[1], 50, 50); // 绘制玩家方块

    // 绘制敌人
    enemies.forEach(enemy => {
        ctx.fillRect(enemy[0], enemy[1], 50, 50); // 绘制每个敌人
    });

    // 绘制子弹
    bullets.forEach(bullet => {
        ctx.fillStyle = 'red';
        ctx.fillRect(bullet[0], bullet[1], 10, 10); // 绘制每个子弹
    });

    // 更新分数显示
    document.getElementById('score').innerText = `Score: ${score}`;
}

// 更新游戏状态
function update() {
    fetch('/shooter/update') // 请求更新游戏状态
        .then(response => response.json()) // 解析为 JSON
        .then(data => {
            // 更新玩家位置、敌人、子弹、分数和游戏状态
            playerPos = data.player_pos;
            enemies = data.enemies;
            bullets = data.bullets;
            score = data.score;
            gameOver = data.game_over;

            // 如果游戏结束，停止游戏循环并显示重新开始按钮
            if (gameOver) {
                cancelAnimationFrame(gameLoopId); // 停止游戏循环
                document.getElementById('restartButton').style.display = 'inline'; // 显示重新开始按钮
            }
        });
}

// 移动玩家
function move(direction) {
    fetch(`/shooter/move/${direction}`) // 请求移动玩家
        .then(response => response.json()) // 解析为 JSON
        .then(data => {
            playerPos = data.player_pos; // 更新玩家位置
        });
}

// 玩家射击
function shoot() {
    fetch('/shooter/shoot', { method: 'POST' }) // 发送 POST 请求以射击
        .then(() => {
            bullets.push([playerPos[0] + 20, playerPos[1]]); // 添加新子弹到数组
        });
}

// 监听键盘事件
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') { // 如果按下左箭头
        move('left'); // 移动玩家向左
    } else if (event.key === 'ArrowRight') { // 如果按下右箭头
        move('right'); // 移动玩家向右
    } else if (event.key === ' ') { // 如果按下空格键
        shoot(); // 射击
    }
});

// 重新开始游戏的按钮事件
document.getElementById('restartButton').addEventListener('click', () => {
    fetch('/shooter/restart', { method: 'POST' }) // 发送请求以重新启动游戏
        .then(() => {
            // 重置游戏状态
            playerPos = [400, 550];
            enemies = [];
            bullets = [];
            score = 0;
            gameOver = false;
            document.getElementById('restartButton').style.display = 'none'; // 隐藏重新开始按钮
            gameLoop(); // 重新启动游戏循环
        });
});

// 游戏主循环
function gameLoop() {
    draw(); // 绘制场景
    update(); // 更新游戏状态
    gameLoopId = requestAnimationFrame(gameLoop); // 请求下一个动画帧，并存储 ID
}

// 启动游戏循环
gameLoop();