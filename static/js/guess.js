// 为开始游戏按钮添加点击事件监听器
document.getElementById('start-button').addEventListener('click', function() {
    // 向服务器发送请求以启动游戏
    fetch('/start_guess', {
        method: 'POST' // 使用 POST 方法
    })
    .then(response => response.json()) // 解析返回的 JSON 响应
    .then(data => {
        document.getElementById('result').innerText = data.status; // 显示游戏状态
        document.getElementById('guess-input').disabled = false; // 启用输入框
        document.getElementById('guess-button').disabled = false; // 启用猜测按钮
        document.getElementById('guess-input').value = ''; // 清空输入框
    })
    .catch(error => {
        console.error('Error:', error); // 处理错误
    });
});

// 为猜测按钮添加点击事件监听器
document.getElementById('guess-button').addEventListener('click', function() {
    const guess = parseInt(document.getElementById('guess-input').value); // 获取并解析用户输入的猜测
    // 向服务器发送猜测请求
    fetch('/guess', {
        method: 'POST', // 使用 POST 方法
        headers: {
            'Content-Type': 'application/json' // 设置请求头为 JSON 格式
        },
        body: JSON.stringify({ number: guess }) // 将猜测数字转为 JSON 字符串
    })
    .then(response => response.json()) // 解析返回的 JSON 响应
    .then(data => {
        document.getElementById('result').innerText = data.message; // 显示结果信息
        if (data.attempts !== undefined) { // 如果有尝试次数信息
            document.getElementById('result').innerText += ` (第 ${data.attempts} 次猜测)`; // 显示猜测次数
        }
        if (data.correct_number !== undefined) { // 如果猜对了
            document.getElementById('guess-input').disabled = true; // 禁用输入框
            document.getElementById('guess-button').disabled = true; // 禁用猜测按钮
        }
    })
    .catch(error => {
        console.error('Error:', error); // 处理错误
    });
});

// 添加重复的事件监听器（可以去掉）
document.getElementById('start-button').addEventListener('click', startGame);
document.getElementById('guess-button').addEventListener('click', makeGuess);

// 启动游戏的函数
function startGame() {
    // 向服务器发送请求以启动游戏
    fetch('/guess/start_guess', {
        method: 'POST', // 使用 POST 方法
        headers: {
            'Content-Type': 'application/json' // 设置请求头为 JSON 格式
        }
    })
    .then(response => response.json()) // 解析返回的 JSON 响应
    .then(data => {
        if (data.status === "Game started") { // 检查游戏是否成功启动
            document.getElementById('result').innerText = "游戏已开始！请猜一个数字。"; // 显示游戏开始信息
            document.getElementById('guess-input').disabled = false; // 启用输入框
            document.getElementById('guess-button').disabled = false; // 启用猜测按钮
        }
    })
    .catch(error => console.error('Error:', error)); // 处理错误
}

// 处理用户猜测的函数
function makeGuess() {
    const userGuess = parseInt(document.getElementById('guess-input').value, 10); // 获取并解析用户输入的猜测

    // 向服务器发送猜测请求
    fetch('/guess/guess', {
        method: 'POST', // 使用 POST 方法
        headers: {
            'Content-Type': 'application/json' // 设置请求头为 JSON 格式
        },
        body: JSON.stringify({ number: userGuess }) // 将猜测数字转为 JSON 字符串
    })
    .then(response => response.json()) // 解析返回的 JSON 响应
    .then(data => {
        if (data.error) { // 如果返回了错误信息
            document.getElementById('result').innerText = data.error; // 显示错误信息
        } else {
            const status = data.status || "unknown"; // 获取状态，默认值为 "unknown"
            document.getElementById('result').innerText = `你的猜测是 ${userGuess}，结果是：${data.message}。`; // 显示猜测结果
            if (data.remaining !== undefined) { // 如果有剩余猜测次数信息
                document.getElementById('result').innerText += ` 剩余猜测次数：${data.remaining}`; // 显示剩余次数
            }
            if (status === "correct") { // 如果猜对了
                document.getElementById('guess-input').disabled = true; // 禁用输入框
                document.getElementById('guess-button').disabled = true; // 禁用猜测按钮
            }
        }
    })
    .catch(error => console.error('Error:', error)); // 处理错误
}